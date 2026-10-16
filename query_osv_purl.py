#!/usr/bin/env python3
"""
query_osv_purl.py — OSV vulnerability scan for the PURLs in a CycloneDX SBOM.

Queries https://api.osv.dev/v1/querybatch for every PURL, then fetches the full
record for each hit so advisories that share a CVE can be folded together
(USN-1234-1 + GHSA-xxxx → CVE-2024-1234).

Optionally enriches each CVE with CVSS/EPSS/exploited-in-the-wild flags from
Vulners, which OSV itself does not provide as numeric scores.

Importable: compare_scanners.py calls scan() directly instead of shelling out.

Usage:
    python3 query_osv_purl.py SBOM [-o OUT.json] [--all] [--no-enrich]
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor  # pylint: disable=no-name-in-module
from pathlib import Path

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

# Detail records are cached for the day, so scanning a second SBOM (or re-running
# after a crash) costs almost nothing while data still refreshes daily.
CACHE_PATH = PROJECT_ROOT / "results" / ".osv-details-cache.json"


def _log(message: str, quiet: bool = False, end: str = "\n") -> None:
    """Progress goes to stderr — stdout may be a report being captured."""
    if not quiet:
        print(message, file=sys.stderr, end=end, flush=True)


# ── SBOM input ───────────────────────────────────────────────────────


def load_purls(sbom_path: Path) -> list[str]:
    """Unique PURLs from a CycloneDX components list, in document order."""
    sbom = json.loads(Path(sbom_path).read_text(encoding="utf-8"))
    seen = set()
    purls = []
    for comp in sbom.get("components", []):
        purl = comp.get("purl")
        if purl and purl not in seen:
            seen.add(purl)
            purls.append(purl)
    return purls


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


def query_purl_vulns(session: requests.Session, purls: list[str], quiet: bool) -> dict:
    """Batch-query OSV for every PURL. Returns {purl: [vuln_id, ...]} for hits only."""
    hits: dict[str, list[str]] = {}
    batches = [
        purls[i : i + PURL_BATCH_SIZE] for i in range(0, len(purls), PURL_BATCH_SIZE)
    ]
    done = 0

    def run_batch(batch: list[str]) -> list[dict]:
        queries = [{"package": {"purl": p}} for p in batch]
        resp = session.post(OSV_BATCH_URL, json={"queries": queries}, timeout=60)
        resp.raise_for_status()
        return resp.json().get("results", [])

    with ThreadPoolExecutor(max_workers=min(MAX_WORKERS, len(batches) or 1)) as pool:
        for batch, results in zip(batches, pool.map(run_batch, batches)):
            done += 1
            _log(f"\r🔍 OSV querybatch {done}/{len(batches)}...", quiet, end="")
            for purl, result in zip(batch, results):
                ids = [v["id"] for v in result.get("vulns", []) if v.get("id")]
                if ids:
                    hits.setdefault(purl, []).extend(ids)
    _log("", quiet)
    return hits


def _load_cache() -> dict:
    try:
        cached = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    # Daily refresh: yesterday's records are discarded wholesale.
    if cached.get("date") != dt.date.today().isoformat():
        return {}
    return cached.get("vulns", {})


def _save_cache(details: dict) -> None:
    try:
        CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
        CACHE_PATH.write_text(
            json.dumps({"date": dt.date.today().isoformat(), "vulns": details}),
            encoding="utf-8",
        )
    except OSError:
        pass  # a cache we cannot write is not worth failing a scan over


def fetch_vuln_details(
    session: requests.Session, vuln_ids: set[str], quiet: bool
) -> dict:
    """Fetch /v1/vulns/{id} for each ID, in parallel, reusing today's cache."""
    cache = _load_cache()
    details = {vid: cache[vid] for vid in vuln_ids if vid in cache}
    todo = sorted(vuln_ids - details.keys())
    if details:
        _log(f"📋 {len(details)} vulnerability records from today's cache", quiet)
    if not todo:
        return details

    done = 0

    def fetch(vid: str) -> tuple[str, dict]:
        try:
            resp = session.get(f"{OSV_VULN_URL}/{vid}", timeout=30)
            resp.raise_for_status()
            return vid, resp.json()
        except requests.RequestException:
            return vid, {"id": vid}

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        for vid, record in pool.map(fetch, todo):
            done += 1
            details[vid] = cache[vid] = record
            _log(f"\r📋 Fetching details {done}/{len(todo)}...", quiet, end="")
    _log("", quiet)

    # Save the whole cache, not just this SBOM's slice — the next SBOM in the
    # run shares most of these records.
    _save_cache(cache)
    return details


# ── Advisory deduplication ───────────────────────────────────────────


def collect_ids(vuln: dict) -> tuple[set[str], set[str]]:
    """All CVE and GHSA identifiers attached to one OSV record."""
    cves, ghsas = set(), set()
    for ident in (
        vuln.get("id", ""),
        *vuln.get("aliases", []),
        *vuln.get("related", []),
        *vuln.get("upstream", []),
    ):
        if ident.startswith("CVE-"):
            cves.add(ident)
        elif ident.startswith("GHSA-"):
            ghsas.add(ident)
    return cves, ghsas


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
    advisory covering several CVEs is listed as a source under each of them.
    """
    groups: dict[str, set[str]] = {}
    severities: dict[str, str | None] = {}

    for vid in vuln_ids:
        record = details.get(vid, {"id": vid})
        cves, ghsas = collect_ids(record)
        severity = osv_severity(record)

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

    return [
        (canon, sorted(s for s in groups[canon] if s != canon), severities.get(canon))
        for canon in sorted(groups)
    ]


# ── Vulners enrichment (CVSS / EPSS / exploited in the wild) ──────────


def fetch_vulners_scores(cve_ids: list[str], quiet: bool) -> dict:
    """{cve: {cvss, severity, epss, wild_exploited}} — empty without an API key."""
    load_dotenv()
    api_key = os.getenv("VULNERS_API_KEY")
    if not api_key:
        _log("   ⚠️  VULNERS_API_KEY not set — skipping CVSS/EPSS enrichment", quiet)
        return {}

    batches = [
        cve_ids[i : i + VULNERS_BATCH_SIZE]
        for i in range(0, len(cve_ids), VULNERS_BATCH_SIZE)
    ]
    scores: dict[str, dict] = {}
    done = 0

    def run_batch(batch: list[str]) -> dict:
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
            return {}

    with ThreadPoolExecutor(max_workers=min(4, len(batches) or 1)) as pool:
        for docs in pool.map(run_batch, batches):
            done += 1
            _log(f"\r🔒 Vulners enrichment {done}/{len(batches)}...", quiet, end="")
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
    return scores


# ── Scan ─────────────────────────────────────────────────────────────


def scan(
    sbom_path: Path | str,
    out_path: Path | str | None = None,
    quiet: bool = False,
    enrich: bool = True,
) -> dict:
    """
    Run the full OSV scan for one SBOM and return the result document.
    Writes it to out_path when given.
    """
    # pylint: disable=too-many-locals
    sbom_path = Path(sbom_path)
    purls = load_purls(sbom_path)
    _log(f"📦 {len(purls)} unique PURLs in {sbom_path.name}", quiet)

    session = _session()
    purl_hits = query_purl_vulns(session, purls, quiet) if purls else {}

    all_ids = {vid for ids in purl_hits.values() for vid in ids}
    details = fetch_vuln_details(session, all_ids, quiet) if all_ids else {}

    # Fold advisories per package, collecting the CVEs worth enriching.
    per_package = [(purl, dedupe_vulns(purl_hits.get(purl, []), details)) for purl in purls]
    canonical_ids = {canon for _, deduped in per_package for canon, _, _ in deduped}

    cves = sorted(c for c in canonical_ids if c.startswith("CVE-"))
    scores = fetch_vulners_scores(cves, quiet) if (enrich and cves) else {}

    affected = sum(1 for _, deduped in per_package if deduped)
    document: dict = {
        "meta": {
            "tool": "query_osv_purl",
            "sbomFile": str(sbom_path),
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
        document = scan(args.sbom_path, args.output, enrich=not args.no_enrich)
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
