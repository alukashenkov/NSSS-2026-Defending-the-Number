#!/usr/bin/env python3
"""
query_osv_purl.py — OSV vulnerability scan for the PURLs in a CycloneDX SBOM.

Queries https://api.osv.dev/v1/querybatch for every PURL, then fetches the full
record for each hit so advisories that share a CVE can be folded together
(USN-1234-1 + GHSA-xxxx → CVE-2024-1234).

Two lookup modes:

  binary  (default) — query each PURL as the SBOM spells it, with a Trivy
                      ?epoch= moved inline (OSV ignores the qualifier).
  source            — query deb packages by their *source* package instead.
                      OSV's Debian/Ubuntu records are keyed by source package
                      (openssl, not libssl1.1), so a binary-name lookup misses
                      every package whose name differs from its source. Hits
                      are still reported against the binary PURL. Other
                      ecosystems have no source/binary split and are queried
                      as-is.

Syft and Trivy record the source package differently, so both are read:

  syft   upstream= PURL qualifier: upstream=util-linux%402.34-0.1ubuntu9.6, or
         just upstream=docker-ce when the source version equals the binary's.
  Trivy  component properties aquasecurity:trivy:SrcName / SrcVersion /
         SrcRelease / SrcEpoch; the PURL itself carries nothing.

In both modes the version is written with its epoch inline (1%3A3.7-3). OSV
ignores an ?epoch= qualifier and matches Ubuntu records against exact,
epoch-bearing version lists, so a missing epoch means a miss, not an
over-match. Left as ?epoch=, Trivy's epoch-bearing debs would find nothing.

Optionally enriches each CVE with CVSS/EPSS/exploited-in-the-wild flags from
Vulners, which OSV itself does not provide as numeric scores.

Importable: compare_scanners.py calls scan() directly instead of shelling out.

Usage:
    python3 query_osv_purl.py SBOM [-o OUT.json] [--source] [--all] [--no-enrich]
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import threading
import urllib.parse
from concurrent.futures import ThreadPoolExecutor  # pylint: disable=no-name-in-module
from pathlib import Path
from typing import Callable, Optional

import requests
from dotenv import load_dotenv

# ── Configuration ────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).resolve().parent

OSV_BATCH_URL = "https://api.osv.dev/v1/querybatch"
OSV_VULN_URL = "https://api.osv.dev/v1/vulns"
VULNERS_ID_URL = "https://vulners.com/api/v3/search/id/"

PURL_BATCH_SIZE = 100  # PURLs per querybatch request
VULNERS_BATCH_SIZE = 100  # CVEs per Vulners request
MAX_WORKERS = 8  # concurrent HTTP requests

# Detail records are cached across runs and days. Each querybatch answer says
# when every record it names last changed, so a cached record is reused only
# while that timestamp still matches and is refetched as soon as OSV edits it:
# fresh data without downloading thousands of unchanged records every day.
CACHE_PATH = PROJECT_ROOT / "results" / ".osv-details-cache.json"
# Bumped whenever what a cached record holds changes; any other file is discarded.
# Written as the document's first key so a stale file is recognised from its
# first bytes, without parsing it (format 1 held whole records and reached 4 GB;
# format 2 had no modified timestamps and was discarded daily).
CACHE_FORMAT = 3


# Optional sink for one-line progress ("details 340/912"), used by callers that
# draw their own status line and run this module quietly.
Progress = Optional[Callable[[str], None]]


def _log(message: str, quiet: bool = False, end: str = "\n") -> None:
    """Progress goes to stderr — stdout may be a report being captured."""
    if not quiet:
        print(message, file=sys.stderr, end=end, flush=True)


# ── SBOM input ───────────────────────────────────────────────────────


TRIVY_SRC_PREFIX = "aquasecurity:trivy:Src"


def _deb_source(comp: dict) -> tuple[str, str] | None:
    """
    (source name, source version) for a deb component, or None when the SBOM
    records no source package for it.

    The version comes back with its epoch inline ("5:28.1.1-1~…"), ready to be
    percent-encoded into a PURL.
    """
    purl = comp.get("purl", "")
    base, _, qualifiers = purl.partition("?")
    quals = urllib.parse.parse_qs(qualifiers)

    # Trivy: properties, with the epoch and Debian revision split out.
    props = {
        prop["name"][len(TRIVY_SRC_PREFIX) :]: prop.get("value", "")
        for prop in comp.get("properties", [])
        if prop.get("name", "").startswith(TRIVY_SRC_PREFIX)
    }
    if props.get("Name"):
        version = props.get("Version", "")
        if not version:
            return props["Name"], _binary_version(base, quals)
        if props.get("Release"):
            version = f"{version}-{props['Release']}"
        if props.get("Epoch"):
            version = f"{props['Epoch']}:{version}"
        return props["Name"], version

    # syft: upstream=name or upstream=name@version (parse_qs has decoded %40).
    upstream = quals.get("upstream", [""])[0]
    if upstream:
        name, at, version = upstream.partition("@")
        return name, version if at else _binary_version(base, quals)
    return None


def _binary_version(base: str, quals: dict) -> str:
    """The component's own version, with a Trivy ?epoch= folded inline."""
    version = urllib.parse.unquote(base.rpartition("@")[2])
    epoch = quals.get("epoch", [""])[0]
    if epoch and ":" not in version:
        version = f"{epoch}:{version}"
    return version


def binary_purl(purl: str) -> str:
    """
    The PURL to ask OSV about in binary mode: the SBOM's own spelling, except
    that a Trivy ?epoch= qualifier is moved inline (bsdutils@1%3A2.34-…).

    OSV ignores ?epoch= and matches Ubuntu records against their exact,
    epoch-bearing version lists, so diffutils@3.7-3?epoch=1 matches nothing
    while diffutils@1%3A3.7-3 matches. The SBOM itself is never rewritten;
    hits are still reported against its PURL.
    """
    if not purl.startswith("pkg:deb/"):
        return purl
    base, _, qualifiers = purl.partition("?")
    pairs = urllib.parse.parse_qsl(qualifiers, keep_blank_values=True)
    if not any(key == "epoch" for key, _ in pairs):
        return purl
    quals = urllib.parse.parse_qs(qualifiers)
    name = base.rpartition("@")[0]
    base = f"{name}@{urllib.parse.quote(_binary_version(base, quals))}"
    rest = urllib.parse.urlencode([(k, v) for k, v in pairs if k != "epoch"])
    return f"{base}?{rest}" if rest else base


def source_purl(comp: dict) -> str:
    """
    The PURL to ask OSV about in source mode.

    For a deb that is its source package, keeping only the distro qualifier.
    A deb with no recorded source *is* its own source (syft omits upstream= in
    that case), so it still gets the inline-epoch rewrite. Everything else is
    returned unchanged.
    """
    purl = comp["purl"]
    if not purl.startswith("pkg:deb/"):
        return purl
    base, _, qualifiers = purl.partition("?")
    quals = urllib.parse.parse_qs(qualifiers)
    namespace = base.rpartition("@")[0].rsplit("/", 1)[0]

    source = _deb_source(comp)
    name, version = source or (
        urllib.parse.unquote(base.rpartition("@")[0].rsplit("/", 1)[1]),
        _binary_version(base, quals),
    )
    query = f"{namespace}/{urllib.parse.quote(name)}@{urllib.parse.quote(version)}"
    distro = quals.get("distro", [""])[0]
    return f"{query}?distro={distro}" if distro else query


def load_query_purls(sbom_path: Path, mode: str) -> dict[str, str]:
    """
    {SBOM PURL: PURL to query OSV with}, unique, in document order.

    In binary mode the two differ only by an epoch moved inline (see
    binary_purl); in source mode deb packages are queried by source package
    (see source_purl).
    """
    sbom = json.loads(Path(sbom_path).read_text(encoding="utf-8"))
    queries: dict[str, str] = {}
    for comp in sbom.get("components", []):
        purl = comp.get("purl")
        if purl and purl not in queries:
            queries[purl] = source_purl(comp) if mode == "source" else binary_purl(purl)
    return queries


# ── OSV queries ──────────────────────────────────────────────────────


def _session() -> requests.Session:
    s = requests.Session()
    s.headers["Content-Type"] = "application/json"
    # One pooled connection per worker beats a fresh TLS handshake per request.
    adapter = requests.adapters.HTTPAdapter(
        pool_connections=MAX_WORKERS, pool_maxsize=MAX_WORKERS, max_retries=2
    )
    s.mount("https://", adapter)
    return s


def query_purl_vulns(
    session: requests.Session,
    purls: list[str],
    quiet: bool,
    progress: Progress = None,
    modified: dict[str, str] | None = None,
) -> dict:
    """
    Batch-query OSV for every PURL. Returns {purl: [vuln_id, ...]} for hits only.

    querybatch also says when each record last changed; that lands in
    `modified` ({vuln_id: timestamp}) so cached records can be checked against it.
    """
    hits: dict[str, list[str]] = {}
    batches = [
        purls[i : i + PURL_BATCH_SIZE] for i in range(0, len(purls), PURL_BATCH_SIZE)
    ]
    done = 0

    def run_batch(batch: list[str]) -> list[dict]:
        """One querybatch call, then follow pagination for every capped query.

        /v1/querybatch returns AT MOST 1000 vulns per query and signals the rest
        with next_page_token. Reading only result["vulns"] silently truncates any
        package with more than 1000 records — on this corpus that is the kernel
        source package and nothing else, where it turned 4,402 CVEs into 1,141
        and looked like a 3.8x disagreement with Trivy (2026-10-24; see
        wiki/analysis/src-osv-trivy-kernel-gap-2026-10-24.md in the vault).
        A round 1000 in a result set is the shape of a cap, not an answer.
        """
        queries = [{"package": {"purl": p}} for p in batch]
        resp = session.post(OSV_BATCH_URL, json={"queries": queries}, timeout=60)
        resp.raise_for_status()
        results = resp.json().get("results", [])

        for idx, result in enumerate(results):
            token = result.get("next_page_token")
            guard = 0
            while token and guard < 200:
                guard += 1
                page = session.post(
                    OSV_BATCH_URL,
                    json={"queries": [{"package": {"purl": batch[idx]},
                                       "page_token": token}]},
                    timeout=60,
                )
                page.raise_for_status()
                more = (page.json().get("results") or [{}])[0]
                result.setdefault("vulns", []).extend(more.get("vulns", []))
                token = more.get("next_page_token")
            if guard >= 200:
                _log(f"\n⚠️  {batch[idx]}: stopped paging at {guard} pages", quiet)
        return results

    with ThreadPoolExecutor(max_workers=min(MAX_WORKERS, len(batches) or 1)) as pool:
        for batch, results in zip(batches, pool.map(run_batch, batches)):
            done += 1
            _log(f"\r🔍 OSV querybatch {done}/{len(batches)}...", quiet, end="")
            if progress:
                progress(f"querybatch {done}/{len(batches)}")
            for purl, result in zip(batch, results):
                ids = [v["id"] for v in result.get("vulns", []) if v.get("id")]
                if modified is not None:
                    for v in result.get("vulns", []):
                        if v.get("id") and v.get("modified"):
                            modified[v["id"]] = v["modified"]
                if ids:
                    hits.setdefault(purl, []).extend(ids)
    _log("", quiet)
    return hits


def slim_record(record: dict) -> dict:
    """
    The part of an OSV record this module reads: its identity (id, aliases,
    upstream; see collect_ids) and its severity label (see osv_severity).

    Everything else is dropped before caching. Ubuntu kernel records list every
    affected version of 164 kernel flavours and run to 2 MB each; cached whole,
    a day's records reached 4 GB, and loading or saving them held the GIL for
    half a minute, freezing every other scanner thread in the process (the
    Vulners audit upload among them). aliases and upstream are always present,
    so a slim record is never mistaken for a bare {"id": ...} failure stub.
    `modified` is what the cache is validated against (see fetch_vuln_details).
    """
    slim = {
        "id": record.get("id", ""),
        "modified": record.get("modified", ""),
        "aliases": record.get("aliases") or [],
        "upstream": record.get("upstream") or [],
    }
    severity = (record.get("database_specific") or {}).get("severity")
    if severity is not None:
        slim["database_specific"] = {"severity": severity}
    return slim


# One cache per process, shared by every scan in it: OSV and Src OSV run
# concurrently and fetch largely the same records. The lock guards the dict
# while one thread adds records and another saves it.
_cache_lock = threading.Lock()
_cache: dict = {"loaded": False, "vulns": {}}


def _load_cache() -> dict:
    """The cached records, read from disk once per process."""
    with _cache_lock:
        if _cache["loaded"]:
            return _cache["vulns"]
        vulns: dict = {}
        try:
            with CACHE_PATH.open(encoding="utf-8") as f:
                head = f.read(32)
                # Another format's file is discarded wholesale. Checking the
                # head first means an old multi-gigabyte file is never parsed.
                if head.startswith(f'{{"format": {CACHE_FORMAT},'):
                    vulns = json.loads(head + f.read()).get("vulns", {})
        except (OSError, json.JSONDecodeError):
            pass
        _cache.update(loaded=True, vulns=vulns)
        return vulns


def _save_cache() -> None:
    try:
        with _cache_lock:
            text = json.dumps({"format": CACHE_FORMAT, "vulns": _cache["vulns"]})
        CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = CACHE_PATH.with_name(f"{CACHE_PATH.name}.{threading.get_ident()}.tmp")
        tmp_path.write_text(text, encoding="utf-8")
        tmp_path.replace(CACHE_PATH)  # concurrent savers never interleave a file
    except OSError:
        pass  # a cache we cannot write is not worth failing a scan over


def cached_is_current(cached: dict | None, modified: str | None) -> bool:
    """
    Whether a cached record can stand in for a fetch.

    It must be a real record, not a bare {"id": ...} failure stub, and carry
    the same `modified` timestamp querybatch just reported for it. With no
    timestamp from querybatch there is nothing to compare, so it is trusted.
    """
    if not cached or len(cached) <= 1:
        return False
    return modified is None or cached.get("modified") == modified


def fetch_vuln_details(
    session: requests.Session,
    vuln_ids: set[str],
    quiet: bool,
    progress: Progress = None,
    modified: dict[str, str] | None = None,
) -> dict:
    """
    Fetch /v1/vulns/{id} for each ID, in parallel, reusing every cached record
    OSV has not changed since (see cached_is_current). `modified` is
    querybatch's {vuln_id: timestamp}.

    A failed fetch is stood in for by a bare {"id": vid} for this scan only and
    never cached: with no aliases it cannot fold onto its CVE, and caching it
    would repeat that for every later scan. Bare stubs a cache already holds
    are fetched again for the same reason.
    """
    modified = modified or {}
    cache = _load_cache()
    with _cache_lock:
        details = {
            vid: cache[vid]
            for vid in vuln_ids
            if cached_is_current(cache.get(vid), modified.get(vid))
        }
    todo = sorted(vuln_ids - details.keys())
    if details:
        _log(f"📋 {len(details)} unchanged vulnerability records from the cache", quiet)
    if not todo:
        return details

    done = 0
    failed = []

    def fetch(vid: str) -> tuple[str, dict | None]:
        try:
            resp = session.get(f"{OSV_VULN_URL}/{vid}", timeout=30)
            resp.raise_for_status()
            # Slim in the worker, so a 2 MB kernel record is freed at once.
            record = slim_record(resp.json())
            # Store querybatch's spelling of the timestamp: it is what the next
            # scan compares against, and it is less precise than the record's.
            if modified.get(vid):
                record["modified"] = modified[vid]
            return vid, record
        except (requests.RequestException, ValueError, AttributeError):
            return vid, None

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        for vid, record in pool.map(fetch, todo):
            done += 1
            if record is None:
                failed.append(vid)
                details[vid] = {"id": vid}
            else:
                details[vid] = record
                with _cache_lock:
                    cache[vid] = record
            _log(f"\r📋 Fetching details {done}/{len(todo)}...", quiet, end="")
            if progress:
                progress(f"details {done}/{len(todo)}")
    _log("", quiet)
    if failed:
        _log(
            f"⚠️  {len(failed)} OSV records could not be fetched and stay unfolded: "
            + ", ".join(failed[:5]) + (" …" if len(failed) > 5 else ""),
            quiet,
        )

    # Save the whole cache, not just this SBOM's slice — the next SBOM in the
    # run shares most of these records.
    _save_cache()
    return details


# ── Advisory deduplication ───────────────────────────────────────────


def collect_ids(vuln: dict) -> tuple[set[str], set[str]]:
    """
    The CVE and GHSA identifiers one OSV record IS: its id, aliases and upstream.

    `related` is left out. The OSV schema defines it as a different, merely
    connected vulnerability, so folding it in would report that vulnerability
    against a package its own record does not match (GHSA-w8rr-5gcm-pp58 is
    CVE-2026-39882 and only *related* to CVE-2026-44967). Ubuntu records carry
    their CVEs in `upstream`, so nothing else depends on `related`.
    """
    cves, ghsas = set(), set()
    for ident in (
        vuln.get("id", ""),
        *vuln.get("aliases", []),
        *vuln.get("upstream", []),
    ):
        if ident.startswith("CVE-"):
            cves.add(ident)
        elif ident.startswith("GHSA-"):
            ghsas.add(ident)
    return cves, ghsas


# Ubuntu Security Notices and Livepatch Security Notices (see dedupe_vulns).
NOTICE_PREFIXES = ("USN-", "LSN-")


def osv_severity(vuln: dict) -> str | None:
    """OSV's own severity label, when the ecosystem provides one."""
    specific = vuln.get("database_specific") or {}
    severity = specific.get("severity")
    return severity.upper() if isinstance(severity, str) else None


def dedupe_vulns(
    vuln_ids: list[str], details: dict
) -> list[tuple[str, list[str], str | None]]:
    """
    Fold a package's advisories into unique vulnerabilities.

    Returns [(canonical_id, source_advisory_ids, severity)] sorted by ID. An
    advisory covering several CVEs is listed as a source under each of them,
    except an Ubuntu notice (USN/LSN), which only joins CVEs whose own record
    OSV also returned for this query.
    """
    groups: dict[str, set[str]] = {}
    severities: dict[str, str | None] = {}

    # A NOTICE is a USN-* or LSN-* record: one release announcement listing,
    # in `upstream`, every CVE it covers across every Ubuntu release it covers.
    # OSV matches the notice as a whole, on its own fixed versions, NOT each CVE
    # inside it, so expanding a notice into findings invents results. The CVE's
    # own UBUNTU-CVE-* record is what says whether it affects this release and
    # version; when OSV did not return that record, the CVE does not apply.
    #
    # USN-8502-1 on gnutls28 3.6.13-2ubuntu1.12 (20.04) matches through its
    # Ubuntu:Pro:20.04 fix at …1.12+esm2 and lists ten CVEs, among them
    # CVE-2024-0553, whose own record is fixed for 20.04 at …1.10. Expanding
    # notices produced 59 such findings per 20.04 SBOM and 63 per 24.04 SBOM
    # (2026-10-25). Checked against each CVE's own record: none applied. The
    # record either had no entry for the release or was fixed at or below the
    # installed version (four were unfixed only in the separate Pro FIPS
    # openssl build).
    #
    # Measured 2026-10-25 on insecureapp-24.04.trivy: one record, LSN-0122-1,
    # carries 150 CVEs; expanding it added 140 that Ubuntu had already fixed
    # BELOW the installed 6.8.0-136.136 (OSV's own paginated answer for that
    # version contains none of them). On 20.04 the same expansion put four
    # phantoms into the exploitation set, three of them fixed in 5.4.0-211.231
    # or earlier against an installed 5.4.0-216.236.
    #
    # So: a notice contributes PROVENANCE to findings that already exist on
    # their own record, and never creates one. This keys on the record's own
    # id, not on how many CVEs it names: a UBUNTU-CVE-* record carries its one
    # CVE in `upstream` too, and a GHSA or GO record may alias several CVEs;
    # both still stand on their own. A notice naming no CVE at all has nothing
    # to corroborate and is kept as its own finding.
    notices: list[tuple[str, set[str], str | None]] = []

    for vid in vuln_ids:
        record = details.get(vid, {"id": vid})
        cves, ghsas = collect_ids(record)
        severity = osv_severity(record)

        if vid.startswith(NOTICE_PREFIXES) and cves:
            notices.append((vid, cves, severity))
            continue
        if cves:
            canons = sorted(cves)
        elif ghsas:
            canons = [sorted(ghsas)[0]]
        else:
            canons = [vid]

        for canon in canons:
            groups.setdefault(canon, set()).add(vid)
            if severities.get(canon) is None:
                severities[canon] = severity

    # Provenance only. A notice none of whose CVEs was corroborated adds nothing.
    for vid, cves, severity in notices:
        for canon in cves & groups.keys():
            groups[canon].add(vid)
            if severities.get(canon) is None:
                severities[canon] = severity

    return [
        (canon, sorted(s for s in groups[canon] if s != canon), severities.get(canon))
        for canon in sorted(groups)
    ]


# ── Vulners enrichment (CVSS / EPSS / exploited in the wild) ──────────


def fetch_vulners_scores(
    cve_ids: list[str], quiet: bool, progress: Progress = None
) -> tuple[dict, set[str]]:
    """
    ({cve: {cvss, severity, epss, wild_exploited}}, CVEs not asked about).

    The second set holds every CVE whose batch failed, or all of them without
    an API key, so a caller that remembers what it queried can tell "Vulners
    does not know this CVE" apart from "the question never got an answer".
    """
    load_dotenv()
    api_key = os.getenv("VULNERS_API_KEY")
    if not api_key:
        _log("   ⚠️  VULNERS_API_KEY not set — skipping CVSS/EPSS enrichment", quiet)
        return {}, set(cve_ids)

    batches = [
        cve_ids[i : i + VULNERS_BATCH_SIZE]
        for i in range(0, len(cve_ids), VULNERS_BATCH_SIZE)
    ]
    scores: dict[str, dict] = {}
    failed: set[str] = set()
    done = 0

    def run_batch(batch: list[str]) -> dict | None:
        try:
            resp = requests.post(
                VULNERS_ID_URL,
                json={"id": batch, "fields": ["epss", "cvss", "enchantments"]},
                headers={"X-Api-Key": api_key},
                timeout=60,
            )
            resp.raise_for_status()
            return resp.json().get("data", {}).get("documents", {})
        except (requests.RequestException, ValueError):
            return None

    with ThreadPoolExecutor(max_workers=min(4, len(batches) or 1)) as pool:
        for batch, docs in zip(batches, pool.map(run_batch, batches)):
            done += 1
            _log(f"\r🔒 Vulners enrichment {done}/{len(batches)}...", quiet, end="")
            if progress:
                progress(f"Vulners CVE scores {done}/{len(batches)}")
            if docs is None:
                failed.update(batch)
                continue
            for cve_id, info in docs.items():
                cvss = info.get("cvss") or {}
                epss_list = info.get("epss") or []
                exploitation = (info.get("enchantments") or {}).get("exploitation") or {}
                scores[cve_id] = {
                    "cvss": cvss.get("score"),
                    "severity": cvss.get("severity"),
                    "epss": epss_list[0].get("epss") if epss_list else None,
                    "wild_exploited": bool(exploitation.get("wildExploited", False)),
                }
    _log("", quiet)
    if failed:
        _log(f"   ⚠️  Vulners enrichment failed for {len(failed)} CVEs", quiet)
    return scores, failed


# ── Scan ─────────────────────────────────────────────────────────────


def scan(
    sbom_path: Path | str,
    out_path: Path | str | None = None,
    quiet: bool = False,
    enrich: bool = True,
    mode: str = "binary",
    progress: Progress = None,
) -> dict:
    """
    Run the full OSV scan for one SBOM and return the result document.
    Writes it to out_path when given. mode is "binary" or "source".
    progress, if given, receives a short line at every step.
    """
    # pylint: disable=too-many-locals
    sbom_path = Path(sbom_path)
    query_for = load_query_purls(sbom_path, mode)
    purls = list(query_for)
    unique_queries = list(dict.fromkeys(query_for.values()))
    _log(
        f"📦 {len(purls)} unique PURLs in {sbom_path.name}"
        + (f" → {len(unique_queries)} source-package queries" if mode == "source" else ""),
        quiet,
    )

    session = _session()
    # Binaries built from one source share a query; fan the hits back out.
    modified: dict[str, str] = {}
    query_hits = (
        query_purl_vulns(session, unique_queries, quiet, progress, modified) if purls else {}
    )
    purl_hits = {
        purl: query_hits[query_for[purl]] for purl in purls if query_for[purl] in query_hits
    }

    all_ids = {vid for ids in purl_hits.values() for vid in ids}
    details = (
        fetch_vuln_details(session, all_ids, quiet, progress, modified) if all_ids else {}
    )

    # Fold advisories per package, collecting the CVEs worth enriching.
    per_package = [(purl, dedupe_vulns(purl_hits.get(purl, []), details)) for purl in purls]
    canonical_ids = {canon for _, deduped in per_package for canon, _, _ in deduped}

    cves = sorted(c for c in canonical_ids if c.startswith("CVE-"))
    scores = fetch_vulners_scores(cves, quiet, progress)[0] if (enrich and cves) else {}

    affected = sum(1 for _, deduped in per_package if deduped)
    document: dict = {
        "meta": {
            "tool": "query_osv_purl",
            "mode": mode,
            "sbomFile": sbom_path.name,
            "created": dt.datetime.now().isoformat(timespec="seconds"),
            "totalPackages": len(purls),
            "affectedPackages": affected,
            "totalAdvisories": sum(len(ids) for ids in purl_hits.values()),
            "uniqueVulnerabilities": len(canonical_ids),
            "enriched": bool(scores),
        },
        "packages": [],
    }

    for purl, deduped in per_package:
        name_ver = purl.split("?", 1)[0].rsplit("/", 1)[-1]
        name, _, version = name_ver.partition("@")
        document["packages"].append(
            {
                "purl": purl,
                **({"queryPurl": query_for[purl]} if query_for[purl] != purl else {}),
                "name": name,
                "version": version,
                "uniqueVulnCount": len(deduped),
                "vulnerabilities": [
                    {
                        "id": canon,
                        "cvss": scores.get(canon, {}).get("cvss"),
                        # OSV's own label wins; Vulners fills the gaps.
                        "severity": severity or scores.get(canon, {}).get("severity"),
                        "epss": scores.get(canon, {}).get("epss"),
                        "wildExploited": scores.get(canon, {}).get("wild_exploited", False),
                        "sourceAdvisories": sources,
                    }
                    for canon, sources, severity in deduped
                ],
            }
        )

    if out_path is not None:
        out_path = Path(out_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(document, indent=2), encoding="utf-8")
        _log(f"💾 OSV results → {out_path}", quiet)

    return document


# ── CLI table ────────────────────────────────────────────────────────


def print_table(document: dict, show_all: bool) -> None:
    """Print the findings in an ASCII table."""
    # pylint: disable=too-many-locals
    rows: list[tuple[str, str, str, str, str]] = []
    separator = ("", "", "", "", "")

    for pkg in document["packages"]:
        vulns = pkg["vulnerabilities"]
        if not vulns and not show_all:
            continue

        purl = pkg["purl"].split("?", 1)[0]
        header = f"{purl}  ({len(vulns)} unique)"

        if not vulns:
            rows.append((header, "✅ CLEAN", "", "", ""))
        else:
            for i, v in enumerate(vulns):
                cvss = v.get("cvss")
                severity = v.get("severity") or ""
                epss = v.get("epss")
                rows.append(
                    (
                        header if i == 0 else "",
                        f"🔴 {v['id']}" if v.get("wildExploited") else v["id"],
                        f"{cvss} {severity[:1]}".strip() if cvss is not None else "",
                        f"{epss:.4f}" if epss is not None else "",
                        ", ".join(v["sourceAdvisories"]),
                    )
                )
        rows.append(separator)

    if rows and rows[-1] == separator:
        rows.pop()
    if not rows:
        print("✅ No vulnerabilities found for any PURL.")
        return

    headings = ("PURL", "Vulnerability", "CVSS", "EPSS", "Also reported as")
    widths = [
        max(len(headings[i]), max((len(r[i]) for r in rows), default=0)) for i in range(5)
    ]
    sep = "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    meta = document["meta"]
    print(
        f"⚠️  {meta['uniqueVulnerabilities']} unique vulnerabilities across "
        f"{meta['affectedPackages']} packages "
        f"(deduplicated from {meta['totalAdvisories']} advisories)\n"
    )
    print(sep)
    print("| " + " | ".join(h.ljust(w) for h, w in zip(headings, widths)) + " |")
    print(sep)
    for row in rows:
        if row == separator:
            print("|" + "+".join("-" * (w + 2) for w in widths) + "|")
        else:
            print("| " + " | ".join(c.ljust(w) for c, w in zip(row, widths)) + " |")
    print(sep)
    print(
        f"\n📊 Summary: {meta['uniqueVulnerabilities']} unique vulns in "
        f"{meta['affectedPackages']}/{meta['totalPackages']} packages"
    )


def main() -> int:
    """Parse args and run the OSV query tool."""
    parser = argparse.ArgumentParser(description="Query the OSV API for a CycloneDX SBOM's PURLs.")
    parser.add_argument("sbom_path", type=Path, help="Path to a CycloneDX SBOM JSON file")
    parser.add_argument(
        "-o", "--output", type=Path, help="Where to write the JSON result document"
    )
    parser.add_argument(
        "--source",
        action="store_true",
        help="Query deb packages by source package (syft upstream= / Trivy Src* properties)",
    )
    parser.add_argument(
        "--all", action="store_true", help="Include clean packages in the table"
    )
    parser.add_argument(
        "--no-enrich",
        action="store_true",
        help="Skip the Vulners CVSS/EPSS lookup (OSV data only)",
    )
    args = parser.parse_args()

    if not args.sbom_path.exists():
        print(f"❌ File not found: {args.sbom_path}", file=sys.stderr)
        return 1

    try:
        document = scan(
            args.sbom_path,
            args.output,
            enrich=not args.no_enrich,
            mode="source" if args.source else "binary",
        )
    except json.JSONDecodeError as exc:
        print(f"❌ Invalid SBOM JSON: {exc}", file=sys.stderr)
        return 1
    except requests.RequestException as exc:
        print(f"❌ OSV API error: {exc}", file=sys.stderr)
        return 1

    print_table(document, args.all)
    return 0


if __name__ == "__main__":
    sys.exit(main())
