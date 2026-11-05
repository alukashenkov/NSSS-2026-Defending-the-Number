#!/usr/bin/env python3
"""
compare_scanners.py — run five vulnerability scanners against a CycloneDX SBOM
and print their findings side by side.

Scanners: OSV, Src OSV (OSV queried by deb source package), Grype, Trivy, Vulners.

Every SBOM gets its own artifact directory under results/, holding each
scanner's raw output plus the rendered report:

    results/<sbom-name>/{osv,osv-src,grype,trivy,vulners}.json
    results/<sbom-name>/report-<sbom-name>.md

Vulnerability data is refreshed daily: any artifact not written today is
re-scanned before the report is built, so a once-a-day run always compares
current data. Use --refresh force to rescan now, or --refresh never to report
on whatever is already on disk.

Usage:
    python3 compare_scanners.py [SBOM ...] [--refresh auto|force|never]
"""

# pylint: disable=too-many-lines,missing-function-docstring,missing-class-docstring
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
import urllib.parse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed  # pylint: disable=no-name-in-module
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

import requests
from dotenv import load_dotenv

import query_osv_purl

# ── Configuration ─────────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_SBOM_GLOB = "sboms/*.cdx.json"
RESULTS_ROOT = PROJECT_ROOT / "results"

VULNERS_SBOM_API = "https://vulners.com/api/v4/audit/sbom"
VULNERS_TIMEOUT = 180

# ── Colour helpers ────────────────────────────────────────────────────────

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"

USE_COLOR = True


def col(text, colour):
    return f"{colour}{text}{RESET}" if USE_COLOR else str(text)


def note(message, colour=DIM):
    """Progress output — goes to stderr so it stays out of the report file."""
    with StatusLine.lock:
        StatusLine.erase()
        print(col(message, colour), file=sys.stderr, flush=True)


class StatusLine:
    """
    One self-redrawing line on stderr while slow work runs: a spinner, what
    each job is doing ("OSV details 340/912", "Grype running") and the time
    elapsed. note() prints above it, so completions appear as they happen.
    Draws nothing when stderr is not a terminal (piped or redirected runs).
    """

    lock = threading.Lock()
    _shown = False  # whether a status line is on screen right now
    FRAMES = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"

    def __init__(self, title: str):
        self.title = title
        self.jobs: dict[str, str] = {}
        self.enabled = sys.stderr.isatty()
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._spin, daemon=True)
        self._started = time.monotonic()

    @classmethod
    def erase(cls) -> None:
        if cls._shown:
            sys.stderr.write("\r\033[K")
            cls._shown = False

    def set(self, job: str, state: str) -> None:
        self.jobs[job] = state

    def done(self, job: str) -> None:
        self.jobs.pop(job, None)

    def progress_for(self, job: str):
        """A callback that reports a job's sub-steps onto this line."""
        return lambda text: self.set(job, text)

    def _spin(self) -> None:
        frame = 0
        while not self._stop.wait(0.1):
            elapsed = int(time.monotonic() - self._started)
            jobs = " · ".join(
                f"{name} {state}".strip() for name, state in list(self.jobs.items())
            )
            line = (
                f"{self.FRAMES[frame % len(self.FRAMES)]} {self.title}"
                f"{': ' + jobs if jobs else ''}  {elapsed // 60}m{elapsed % 60:02d}s"
            )
            width = shutil.get_terminal_size((100, 20)).columns - 1
            if len(line) > width:
                line = line[: width - 1] + "…"
            with StatusLine.lock:
                sys.stderr.write("\r\033[K" + col(line, YELLOW))
                sys.stderr.flush()
                StatusLine._shown = True
            frame += 1

    def __enter__(self):
        if self.enabled:
            self._thread.start()
        return self

    def __exit__(self, *exc):
        self._stop.set()
        if self.enabled:
            self._thread.join()
        with StatusLine.lock:
            StatusLine.erase()
            sys.stderr.flush()
        return False


# ── PURL helpers ──────────────────────────────────────────────────────────

# PURL types whose namespace is part of the package name.
NAMESPACED_TYPES = {"pkg:golang", "pkg:npm", "pkg:github"}


def normalise_purl(purl: str) -> str:
    """
    Strip qualifiers (?arch=… &distro=…) from a PURL to get a canonical key.

    The one qualifier that is part of the version is a deb epoch: syft writes
    it inline (bsdutils@1%3A2.34…), Trivy as ?epoch=1. Fold it back inline so
    both spellings, and Vulners' "1:2.34…", land on the same key.
    """
    base, _, qualifiers = purl.partition("?")
    epoch = urllib.parse.parse_qs(qualifiers).get("epoch", [""])[0]
    name, at, version = base.rpartition("@")
    if epoch and at and ":" not in urllib.parse.unquote(version):
        return f"{name}@{epoch}%3A{version}"
    return base


def name_version_from_purl(purl: str) -> tuple[str, str]:
    """Extract (name, version) from a PURL like pkg:pypi/foo@1.2.3."""
    base = normalise_purl(purl)
    purl_type, _, remainder = base.partition("/")
    if not remainder:
        return base, ""

    if "@" in remainder:
        name_part, _, version = remainder.rpartition("@")
    else:
        name_part, version = remainder, ""

    name_part = urllib.parse.unquote(name_part)
    version = urllib.parse.unquote(version)

    if purl_type not in NAMESPACED_TYPES:
        name_part = name_part.rsplit("/", 1)[-1]
    return name_part, version


def normalize_version(v: str) -> str:
    """Strip 'v' or 'go' prefixes so scanners' version spellings line up."""
    if not v:
        return ""
    v = v.strip().lower()
    if v.startswith("v"):
        v = v[1:]
    if v.startswith("go"):
        v = v[2:]
    return v


ECOSYSTEM_LABELS = {
    "pypi": "Python (PyPI)",
    "golang": "Go",
    "deb": "Debian/Ubuntu (deb)",
    "rpm": "RPM",
    "npm": "npm",
    "maven": "Maven/Java",
    "nuget": "NuGet/.NET",
    "cargo": "Rust (Cargo)",
    "gem": "Ruby (Gem)",
}

ECOSYSTEM_ORDER = ["pypi", "deb", "golang", "npm", "maven", "cargo", "gem", "rpm", "nuget"]


def ecosystem_from_purl(purl: str) -> str:
    """pkg:pypi/foo@1.2.3 → 'pypi'."""
    return purl[4:].split("/", 1)[0] if purl.startswith("pkg:") else "other"


def ecosystem_label(eco: str) -> str:
    return ECOSYSTEM_LABELS.get(eco, eco)


# ── Severity helpers ──────────────────────────────────────────────────────

SEV_ORDER = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "NEGLIGIBLE": 4}

# Scanners spell the same band differently: GHSA says MODERATE, Red Hat says
# IMPORTANT, Grype says Negligible. Fold them onto one vocabulary.
SEV_ALIASES = {
    "MODERATE": "MEDIUM",
    "IMPORTANT": "HIGH",
    "SEVERE": "HIGH",
    "UNKNOWN": None,
    "UNTRIAGED": None,
    "NONE": None,
    "": None,
}


def norm_sev(severity: str | None) -> str | None:
    s = (severity or "").strip().upper()
    return SEV_ALIASES.get(s, s) or None


def sev_colour(severity: str | None) -> str:
    s = norm_sev(severity)
    if s == "CRITICAL":
        return RED + BOLD
    if s == "HIGH":
        return RED
    if s == "MEDIUM":
        return YELLOW
    return DIM


# ── Scan result container ─────────────────────────────────────────────────


def _empty_vulns() -> dict:
    return defaultdict(dict)


@dataclass
class ScanResult:
    """One scanner's view of one SBOM, keyed by canonical PURL after re-keying."""

    packages: dict = field(default_factory=dict)
    vulns: dict = field(default_factory=_empty_vulns)
    # Packages a name+version scanner reported that no SBOM PURL matched.
    unmatched: dict = field(default_factory=dict)
    available: bool = False
    # What produced this artifact, for the report header.
    tool: str = ""

    @property
    def detected(self) -> set:
        """PURLs this scanner found at least one vulnerability in."""
        return {purl for purl, vmap in self.vulns.items() if vmap}

    @property
    def vuln_ids(self) -> set:
        ids = set()
        for vmap in self.vulns.values():
            ids.update(vmap)
        return ids


# ── Loaders ───────────────────────────────────────────────────────────────


def tool_version(tools) -> str:
    """Pull 'name X.Y.Z' out of a CycloneDX metadata.tools block."""
    components = tools.get("components", []) if isinstance(tools, dict) else tools or []
    for tool in components:
        if tool.get("name"):
            return f"{tool['name']} {tool.get('version', '?')}".strip()
    return ""


def load_sbom(path: Path) -> tuple[int, dict, dict]:
    """Master component list plus provenance from the source CycloneDX SBOM."""
    data = json.loads(path.read_text())
    components = data.get("components", [])
    metadata = data.get("metadata", {})
    subject = metadata.get("component", {})

    packages = {}
    for comp in components:
        purl_raw = comp.get("purl", "")
        if not purl_raw:
            continue
        packages[normalise_purl(purl_raw)] = {
            "purl": purl_raw,
            "name": comp.get("name", ""),
            "version": comp.get("version", ""),
            "cpe": comp.get("cpe", ""),
        }

    # Identifies what was actually scanned, so a report is meaningful on its own.
    # Syft records the digest as the subject's version; Trivy only in its pkg:oci PURL.
    digest = subject.get("version", "")
    if not digest and subject.get("purl", "").startswith("pkg:oci/"):
        digest = urllib.parse.unquote(normalise_purl(subject["purl"]).rpartition("@")[2])
    provenance = {
        "image": subject.get("name", ""),
        "digest": digest,
        "format": f"{data.get('bomFormat', '')} {data.get('specVersion', '')}".strip(),
        "generator": tool_version(metadata.get("tools", {})),
        "created": metadata.get("timestamp", ""),
    }
    return len(components), packages, provenance


def load_osv(path: Path) -> ScanResult:
    """Output of query_osv_purl.py: {"packages": [{purl, vulnerabilities: [...]}]}."""
    data = json.loads(path.read_text())

    mode = data.get("meta", {}).get("mode", "binary")
    tool = "api.osv.dev" + (", by source package" if mode == "source" else "")
    result = ScanResult(available=True, tool=tool)
    for pkg in data.get("packages", []):
        purl = normalise_purl(pkg["purl"])
        result.packages[purl] = {
            "purl": pkg["purl"],
            "name": pkg.get("name", ""),
            "version": pkg.get("version", ""),
        }
        for v in pkg.get("vulnerabilities", []):
            vid = v["id"].upper()
            result.vulns[purl][vid] = {
                "id": vid,
                "severity": v.get("severity"),
                "cvss": v.get("cvss"),
                "epss": v.get("epss"),
                "sourceAdvisories": v.get("sourceAdvisories", []),
            }
    return result


def load_grype(path: Path) -> ScanResult:  # pylint: disable=too-many-locals,too-many-branches
    """Grype CycloneDX JSON: components[] for inventory, vulnerabilities[]→affects[]."""
    data = json.loads(path.read_text())

    tool = tool_version(data.get("metadata", {}).get("tools", {}))
    result = ScanResult(available=True, tool=tool)
    ref_map = {}  # bom-ref → purl

    for comp in data.get("components", []):
        purl_raw = comp.get("purl", "")
        if not purl_raw:
            continue
        purl = normalise_purl(purl_raw)
        if comp.get("bom-ref"):
            ref_map[comp["bom-ref"]] = purl
        result.packages[purl] = {
            "purl": purl_raw,
            "name": comp.get("name", ""),
            "version": comp.get("version", ""),
        }

    for v in data.get("vulnerabilities", []):
        raw_id = v.get("id", "").upper()

        source_id = next(
            (
                p.get("value", "").upper()
                for p in v.get("properties", [])
                if p.get("name") == "security:vulnerability:source:id"
            ),
            None,
        )

        # Prefer a CVE as the primary identifier.
        if source_id and source_id.startswith("CVE-"):
            vid = source_id
        elif raw_id.startswith("CVE-"):
            vid = raw_id
        else:
            vid = source_id or raw_id

        severity = cvss_val = epss_val = None
        for rating in v.get("ratings", []):
            source = rating.get("source", {})
            if (rating.get("method") or "").startswith("CVSS"):
                if cvss_val is None:
                    cvss_val = rating.get("score")
                if severity is None:
                    severity = rating.get("severity")
            elif epss_val is None and (
                source.get("name") == "FIRST"
                or "epss" in str(source.get("url", "")).lower()
            ):
                epss_val = rating.get("score")

        provenance = sorted({i for i in (raw_id, source_id) if i and i != vid})

        for affected in v.get("affects", []):
            ref = affected.get("ref")
            purl = ref_map.get(ref)
            if purl is None:
                # Some Grype outputs put the PURL straight into the ref.
                if not (ref and ref.startswith("pkg:")):
                    continue
                purl = normalise_purl(ref)
            result.vulns[purl].setdefault(
                vid,
                {
                    "id": vid,
                    "severity": severity,
                    "cvss": cvss_val,
                    "epss": epss_val,
                    "sourceAdvisories": provenance,
                },
            )
    return result


def load_trivy(path: Path) -> ScanResult:
    """Trivy JSON: Results[].Packages[] and Results[].Vulnerabilities[]."""
    data = json.loads(path.read_text())

    version = (data.get("Trivy") or {}).get("Version", "")
    result = ScanResult(available=True, tool=f"trivy {version}".strip())
    for section in data.get("Results", []):
        for pkg in section.get("Packages", []):
            purl_raw = pkg.get("Identifier", {}).get("PURL", "")
            if not purl_raw:
                continue
            result.packages[normalise_purl(purl_raw)] = {
                "purl": purl_raw,
                "name": pkg.get("Name", ""),
                "version": pkg.get("Version", ""),
            }

        for v in section.get("Vulnerabilities", []):
            purl_raw = v.get("PkgIdentifier", {}).get("PURL", "")
            if not purl_raw:
                continue
            purl = normalise_purl(purl_raw)
            vid = v.get("VulnerabilityID", "").upper()

            cvss_val = None
            for scores in v.get("CVSS", {}).values():
                for key in ("V40Score", "V3Score", "V2Score"):
                    if key in scores:
                        cvss_val = scores[key]
                        break
                if cvss_val is not None:
                    break

            result.vulns[purl].setdefault(
                vid,
                {
                    "id": vid,
                    "severity": v.get("Severity"),
                    "cvss": cvss_val,
                    "epss": None,
                    "sourceAdvisories": [],
                },
            )
    return result


def load_vulners(path: Path) -> ScanResult:  # pylint: disable=too-many-locals
    """
    Vulners reports bare package name + version, not PURLs, so its packages and
    vulns come back keyed by (name, version); rekey_by_name_version() maps them
    onto PURLs once the SBOM index exists.
    """
    data = json.loads(path.read_text())

    result = ScanResult(available=True, tool="vulners.com audit API v4")
    for item in data.get("data", {}).get("data", []):
        name = item.get("package", "")
        version = item.get("version", "")
        key = (name, version)
        result.packages[key] = {"name": name, "version": version}

        for adv in item.get("applicableAdvisories", []):
            adv_id = adv.get("id", "")
            cvss_block = adv.get("metrics", {}).get("cvss", {}) or {}
            severity = cvss_block.get("severity")
            cvss_val = cvss_block.get("score")

            epss_data = adv.get("epss") or []
            epss_val = (
                epss_data[0].get("epss")
                if epss_data and isinstance(epss_data[0], dict)
                else None
            )

            cve_list = [c.upper() for c in adv.get("cvelist", [])]
            if not cve_list:
                # No CVE — fall back to the advisory ID minus the Vulners
                # source prefix (OSV:GHSA-… → GHSA-…).
                cve_list = [adv_id.upper().split(":", 1)[-1]]

            for vid in cve_list:
                result.vulns[key][vid] = {
                    "id": vid,
                    "severity": severity,
                    "cvss": cvss_val,
                    "epss": epss_val,
                    "sourceAdvisories": [adv_id] if adv_id.upper() != vid else [],
                }
    return result


# ── Refreshers ────────────────────────────────────────────────────────────
#
# Each writes to a temp file and moves it into place only on success: a crashed
# scan must not leave a truncated artifact that tomorrow's freshness check
# mistakes for a good one.


def refresh_osv(sbom: Path, out_path: Path, progress=None) -> None:
    query_osv_purl.scan(sbom, out_path, quiet=True, progress=progress)


def refresh_osv_source(sbom: Path, out_path: Path, progress=None) -> None:
    query_osv_purl.scan(sbom, out_path, quiet=True, mode="source", progress=progress)


def run_quietly(cmd: list[str], **kwargs) -> None:
    """
    Run a scanner CLI with its stderr captured. Grype and Trivy draw their own
    progress bars and logs there, which garble each other (and the status line)
    when they run side by side. On failure the tail of that output is the error.
    """
    proc = subprocess.run(cmd, stderr=subprocess.PIPE, text=True, check=False, **kwargs)
    if proc.returncode:
        tail = " | ".join(proc.stderr.strip().splitlines()[-3:])
        raise RuntimeError(f"{cmd[0]} exited {proc.returncode}: {tail}")


def refresh_grype(sbom: Path, out_path: Path, progress=None) -> None:  # pylint: disable=unused-argument
    tmp_path = out_path.with_name(out_path.name + ".tmp")
    try:
        with tmp_path.open("w") as f:
            run_quietly(
                ["grype", f"sbom:{sbom}", "-o", "cyclonedx-json", "--by-cve"], stdout=f
            )
        tmp_path.replace(out_path)
    finally:
        tmp_path.unlink(missing_ok=True)


def refresh_trivy(sbom: Path, out_path: Path, progress=None) -> None:  # pylint: disable=unused-argument
    tmp_path = out_path.with_name(out_path.name + ".tmp").resolve()
    try:
        # Run from the SBOM's directory so Trivy records the bare file name as
        # ArtifactName/Target, not an absolute path from whoever ran the scan.
        run_quietly(
            ["trivy", "sbom", sbom.name, "--format", "json", "--output", str(tmp_path)],
            stdout=subprocess.DEVNULL,
            cwd=sbom.parent,
        )
        tmp_path.replace(out_path)
    finally:
        tmp_path.unlink(missing_ok=True)


def refresh_vulners(sbom: Path, out_path: Path, progress=None) -> None:  # pylint: disable=unused-argument
    """POST the SBOM to the Vulners audit API and normalise the response."""
    load_dotenv()
    api_key = os.getenv("VULNERS_API_KEY")
    if not api_key:
        raise RuntimeError("VULNERS_API_KEY not set (expected in .env)")

    with sbom.open("rb") as f:
        resp = requests.post(
            VULNERS_SBOM_API,
            headers={"X-Api-Key": api_key, "Accept": "application/json"},
            files={"file": (sbom.name, f, "application/json")},
            timeout=VULNERS_TIMEOUT,
        )
    if not resp.ok:
        # The body usually says why (bad key, quota, oversized upload); a bare
        # "502 Server Error" does not.
        body = " ".join(resp.text.split())[:300]
        raise RuntimeError(
            f"HTTP {resp.status_code} {resp.reason} after "
            f"{resp.elapsed.total_seconds():.0f}s: {body or '(empty body)'}"
        )
    try:
        raw = resp.json()
    except ValueError as exc:
        body = " ".join(resp.text.split())[:300]
        raise RuntimeError(f"HTTP {resp.status_code}, body is not JSON: {body}") from exc

    # The API has been seen returning both a flat list and {data: [...]}.
    section = raw.get("data", raw.get("result", {}))
    if isinstance(section, list):
        payload = {"data": section}
    elif isinstance(section, dict) and isinstance(section.get("data"), list):
        payload = dict(section)
    elif isinstance(section, dict):
        payload = {
            "data": next(
                (
                    val
                    for val in section.values()
                    if isinstance(val, list)
                    and val
                    and isinstance(val[0], dict)
                    and "package" in val[0]
                ),
                [],
            )
        }
    else:
        payload = {"data": []}
    payload.setdefault("totalPackages", len(payload["data"]))

    tmp_path = out_path.with_name(out_path.name + ".tmp")
    try:
        tmp_path.write_text(
            json.dumps({"meta": raw.get("meta", {}), "data": payload}, indent=2)
        )
        tmp_path.replace(out_path)
    finally:
        tmp_path.unlink(missing_ok=True)


# ── Scanner registry ──────────────────────────────────────────────────────


@dataclass(frozen=True)
class Scanner:
    key: str  # artifact filename stem
    label: str  # column heading
    letter: str  # single-char marker in the detail view
    # (sbom, out_path, progress) — progress takes a short status string or is None.
    refresh: Callable[[Path, Path, Callable[[str], None] | None], None]
    load: Callable[[Path], ScanResult]
    keyed_by_purl: bool = True
    requires: str | None = None  # executable that must be on PATH


SCANNERS = (
    Scanner("osv", "OSV", "O", refresh_osv, load_osv),
    # Same API, deb packages looked up by source package; loads like OSV.
    Scanner("osv-src", "Src OSV", "S", refresh_osv_source, load_osv),
    Scanner("grype", "Grype", "G", refresh_grype, load_grype, requires="grype"),
    Scanner("trivy", "Trivy", "T", refresh_trivy, load_trivy, requires="trivy"),
    Scanner(
        "vulners", "Vulners", "V", refresh_vulners, load_vulners, keyed_by_purl=False
    ),
)


CVE_ENRICHMENT_FILE = "vulners-cve-data.json"


def load_cve_enrichment(artifact_dir: Path, cve_ids: set[str], mode: str) -> dict:
    """
    Vulners' own CVSS, EPSS and exploited-in-the-wild flag for every CVE in the
    report, keyed by CVE.

    The per-advisory data the SBOM audit returns carries neither EPSS-per-CVE
    nor a usable exploitation flag, so this asks Vulners about the CVEs
    directly. Cached alongside the scan artifacts and refreshed daily like
    everything else; without an API key it simply returns nothing and the
    scanners' own numbers are used.
    """
    path = artifact_dir / CVE_ENRICHMENT_FILE

    cached, queried = {}, set()
    if path.exists():
        try:
            blob = json.loads(path.read_text())
            if mode == "never" or blob.get("date") == dt.date.today().isoformat():
                cached = blob.get("cves", {})
                queried = set(blob.get("queried", cached.keys()))
        except (OSError, json.JSONDecodeError):
            pass

    if mode == "never":
        return cached

    todo = sorted(cve_ids if mode == "force" else cve_ids - queried)
    if not todo:
        return cached

    note(f"   Enriching {len(todo)} CVEs with Vulners CVSS/EPSS/KEV ...", YELLOW)
    try:
        with StatusLine("Enriching") as status:
            scores, failed = query_osv_purl.fetch_vulners_scores(
                todo, quiet=True, progress=status.progress_for("")
            )
    except Exception as exc:  # pylint: disable=broad-exception-caught
        note(f"   ⚠  CVE enrichment failed ({exc}) — using scanner-reported scores", YELLOW)
        return cached
    cached.update(scores)
    if failed:
        note(f"   ⚠  CVE enrichment failed for {len(failed)} CVEs — retried next run", YELLOW)

    try:
        path.write_text(
            json.dumps(
                {
                    "date": dt.date.today().isoformat(),
                    # Track what was answered, not just what came back, so CVEs
                    # Vulners does not know are not re-requested all day — but
                    # CVEs from a failed batch are, on the next run.
                    "queried": sorted(queried | (set(todo) - failed)),
                    "cves": cached,
                },
                indent=2,
            )
        )
    except OSError:
        pass
    return cached


def artifact_date(path: Path) -> dt.date:
    """When an artifact was written: the day its scanner last succeeded."""
    return dt.date.fromtimestamp(path.stat().st_mtime)


def is_fresh(path: Path) -> bool:
    """True if the artifact was written today — vulnerability data is refreshed daily."""
    if not path.exists():
        return False
    return artifact_date(path) == dt.date.today()


def clear_scan_data(artifact_dir: Path) -> None:
    """
    Delete everything a previous run left for one SBOM: every scanner artifact,
    the CVE enrichment, the report and any half-written temp file. A forced
    refresh then starts from nothing, so a scanner that fails shows as missing
    rather than quietly reusing yesterday's answer.
    """
    names = [f"{s.key}.json" for s in SCANNERS] + [CVE_ENRICHMENT_FILE]
    for path in [artifact_dir / n for n in names] + [
        *artifact_dir.glob("report-*.md"),
        *artifact_dir.glob("*.tmp"),
    ]:
        path.unlink(missing_ok=True)


def refresh_artifacts(sbom: Path, artifact_dir: Path, mode: str) -> None:
    """Re-scan whatever is stale. The scanners are independent, so run them together."""
    if mode == "never":
        return
    if mode == "force":
        clear_scan_data(artifact_dir)

    pending = []
    for scanner in SCANNERS:
        out_path = artifact_dir / f"{scanner.key}.json"
        if mode == "auto" and is_fresh(out_path):
            note(f"   {scanner.label}: up to date ({out_path.name})")
            continue
        if scanner.requires and not shutil.which(scanner.requires):
            note(
                f"   {scanner.label}: '{scanner.requires}' not on PATH — skipping", YELLOW
            )
            continue
        pending.append((scanner, out_path))

    if not pending:
        return

    note(f"   Refreshing: {', '.join(s.label for s, _ in pending)} ...", YELLOW)

    with StatusLine("Scanning") as status:

        def run(job):
            scanner, out_path = job
            started = time.monotonic()
            status.set(scanner.label, "running")
            try:
                scanner.refresh(sbom, out_path, status.progress_for(scanner.label))
                return job, None, time.monotonic() - started
            except Exception as exc:  # one scanner failing must not sink the report  # pylint: disable=broad-exception-caught
                return job, exc, time.monotonic() - started
            finally:
                status.done(scanner.label)

        # Report each scanner the moment it finishes, not in submission order.
        with ThreadPoolExecutor(max_workers=len(pending)) as pool:
            futures = [pool.submit(run, job) for job in pending]
            for future in as_completed(futures):
                (scanner, out_path), error, took = future.result()
                if error is None:
                    note(f"   ✅ {scanner.label} refreshed ({took:.0f}s)", GREEN)
                else:
                    kept = (
                        f"keeping the {artifact_date(out_path)} artifact"
                        if out_path.exists()
                        else "no artifact, column omitted"
                    )
                    note(
                        f"   ❌ {scanner.label} failed after {took:.0f}s — "
                        f"{type(error).__name__}: {error} ({kept})",
                        RED,
                    )


# ── Canonical PURL mapping ────────────────────────────────────────────────


def match_key(name: str, version: str) -> tuple[str, str]:
    """
    The key packages are joined on across scanners.

    Case-folded because scanners disagree on it: Trivy and Vulners lowercase Go
    module paths while syft, Grype and OSV preserve the upstream spelling, so
    `github.com/AlecAivazis/survey/v2` would otherwise be two packages. Only the
    join is case-insensitive — the report still shows the SBOM's own spelling.
    """
    return name.lower(), normalize_version(version)


def build_purl_index(sbom_purls: set, scanner_purls: set) -> tuple[dict, dict]:
    """
    Scanners spell the same package differently (qualifiers, 'v' prefixes,
    letter case), so collapse every spelling onto one primary PURL per
    (name, version).

    Returns (canonical_map: any purl → primary purl, nv_to_primary).
    """
    canonical_map, nv_to_primary = {}, {}
    # SBOM PURLs go first: they are the source of truth for spelling.
    for purl in sorted(sbom_purls) + sorted(scanner_purls - sbom_purls):
        nv = match_key(*name_version_from_purl(purl))
        canonical_map[purl] = nv_to_primary.setdefault(nv, purl)

    # Syft emits a main-module entry with no version alongside the versioned
    # one (pkg:golang/github.com/docker/buildx and …/buildx@v0.23.0). Nothing
    # that matches on version can resolve the first, so fold it onto the second
    # when the name has exactly one known version.
    versions_by_name = defaultdict(set)
    for name, version in nv_to_primary:
        if version:
            versions_by_name[name].add(version)

    merged = {}
    for nv in [nv for nv in nv_to_primary if not nv[1]]:
        candidates = versions_by_name.get(nv[0], set())
        if len(candidates) == 1:
            target = nv_to_primary[(nv[0], next(iter(candidates)))]
            merged[nv_to_primary[nv]] = target
            nv_to_primary[nv] = target

    if merged:
        canonical_map = {
            purl: merged.get(primary, primary) for purl, primary in canonical_map.items()
        }
    return canonical_map, nv_to_primary


def rekey_by_purl(result: ScanResult, canonical_map: dict) -> ScanResult:
    out = ScanResult(available=result.available)
    for purl, info in result.packages.items():
        primary = canonical_map.get(purl, purl)
        out.packages.setdefault(primary, info)
        if purl in result.vulns:
            out.vulns[primary].update(result.vulns[purl])
    return out


def rekey_by_name_version(result: ScanResult, nv_to_primary: dict) -> ScanResult:
    out = ScanResult(available=result.available)
    for (name, version), _info in result.packages.items():
        primary = nv_to_primary.get(match_key(name, version))
        vdict = result.vulns.get((name, version), {})
        if primary is None:
            if vdict:
                out.unmatched[(name, version)] = vdict
            continue
        out.packages[primary] = {"purl": primary, "name": name, "version": version}
        if vdict:
            out.vulns[primary].update(vdict)
    return out


# ── Vulnerability ID consolidation ────────────────────────────────────────


def _resolve_chain(alias_map: dict, vid: str) -> str:
    """Follow alias links (USN→GHSA→CVE) to a fixed point, guarding against cycles."""
    seen = {vid}
    current = vid
    while True:
        nxt = alias_map.get(current, current)
        if nxt == current or nxt in seen:
            return current
        seen.add(nxt)
        current = nxt


def build_alias_maps(results: list[ScanResult], purls: set) -> dict:
    """
    Scanners report the same issue under different IDs (CVE vs GHSA vs USN).
    Use each finding's own provenance list to fold the aliases together per
    package, always preferring the CVE as canonical.
    """
    alias_maps = {}
    for purl in purls:
        alias_map = {}
        for result in results:
            for vid, vinfo in result.vulns.get(purl, {}).items():
                for alias in vinfo.get("sourceAdvisories") or ():
                    if not vid.startswith("CVE-") and alias.startswith("CVE-"):
                        canon, other = alias, vid
                    else:
                        canon, other = vid, alias
                    previous = alias_map.get(other)
                    if previous is None or (
                        not previous.startswith("CVE-") and canon.startswith("CVE-")
                    ):
                        alias_map[other] = canon
        if alias_map:
            alias_maps[purl] = alias_map
    return alias_maps


def consolidate(result: ScanResult, alias_maps: dict) -> None:
    """Rewrite a scanner's findings in place onto the consolidated IDs."""
    for purl, vmap in list(result.vulns.items()):
        alias_map = alias_maps.get(purl)
        if not alias_map:
            continue

        merged = {}
        for vid, vinfo in vmap.items():
            canon = _resolve_chain(alias_map, vid)
            target = merged.get(canon)
            if target is None:
                target = merged[canon] = dict(vinfo, id=canon)
            else:
                for key in ("cvss", "epss", "severity"):
                    if target.get(key) is None and vinfo.get(key) is not None:
                        target[key] = vinfo[key]

            advisories = set(target.get("sourceAdvisories") or ())
            advisories.update(vinfo.get("sourceAdvisories") or ())
            if vid != canon:
                advisories.add(vid)
            target["sourceAdvisories"] = sorted(a for a in advisories if a != canon)
        result.vulns[purl] = merged


# ── Printing helpers ──────────────────────────────────────────────────────


def section_header(title: str) -> None:
    print(f"\n## {title}\n")


def mark(scanned: bool, detected: bool) -> str:
    if not scanned:
        return col("-", DIM)
    return col("✔", GREEN) if detected else col("✘", RED)


def rule(widths: list[int]) -> str:
    return "  " + "-+-".join("-" * w for w in widths)


# ── Report ────────────────────────────────────────────────────────────────


def run_report(  # pylint: disable=too-many-locals,too-many-branches,too-many-statements
    sbom: Path, artifact_dir: Path, refresh_mode: str, sbom_data: tuple
) -> None:
    sbom_raw_count, sbom_pkgs, provenance = sbom_data
    sbom_purls = set(sbom_pkgs)

    # Header first, so a report file read on its own says what it describes.
    print(f"# Vulnerability Comparison Report — {provenance['image'] or sbom.name}")
    print()
    print(f"- **Image:** `{provenance['image'] or 'unknown'}`")
    if provenance["digest"]:
        print(f"- **Digest:** `{provenance['digest']}`")
    print(
        f"- **SBOM:** `{sbom.name}` — {provenance['format']}"
        + (f", {provenance['generator']}" if provenance["generator"] else "")
        + (f", built {provenance['created']}" if provenance["created"] else "")
    )
    print(f"- **Report generated:** {dt.datetime.now().isoformat(timespec='seconds')}")

    results: dict[str, ScanResult] = {}
    for scanner in SCANNERS:
        path = artifact_dir / f"{scanner.key}.json"
        if not path.exists():
            note(f"   ⚠  {scanner.label}: no artifact — column omitted", YELLOW)
            results[scanner.key] = ScanResult()
            continue
        try:
            results[scanner.key] = scanner.load(path)
        except (json.JSONDecodeError, KeyError, TypeError) as exc:
            note(f"   ❌ {scanner.label}: unreadable artifact ({exc}) — column omitted", RED)
            results[scanner.key] = ScanResult()

    active = [s for s in SCANNERS if results[s.key].available]
    if not active:
        print("\nNo scanner results available — nothing to compare.")
        return

    print(
        "- **Scanners:** "
        + " · ".join(
            f"{s.label} ({results[s.key].tool})" if results[s.key].tool else s.label
            for s in active
        )
    )
    # A failed refresh keeps the previous artifact, so a column can silently be
    # days older than its neighbours. Say so wherever that is the case.
    today = dt.date.today()
    stale = [
        f"{s.label} ({artifact_date(artifact_dir / f'{s.key}.json').isoformat()})"
        for s in active
        if artifact_date(artifact_dir / f"{s.key}.json") != today
    ]
    if stale:
        print(f"- **⚠ Not scanned today:** {', '.join(stale)}")
        note(f"   ⚠  Not scanned today: {', '.join(stale)}", YELLOW)

    # Collapse every spelling of a package onto one primary PURL.
    scanner_purls = set()
    for scanner in active:
        if scanner.keyed_by_purl:
            scanner_purls.update(results[scanner.key].packages)
    canonical_map, nv_to_primary = build_purl_index(sbom_purls, scanner_purls)

    for scanner in active:
        if scanner.keyed_by_purl:
            results[scanner.key] = rekey_by_purl(results[scanner.key], canonical_map)
        else:
            results[scanner.key] = rekey_by_name_version(
                results[scanner.key], nv_to_primary
            )

    all_purls = set(nv_to_primary.values())
    active_results = [results[s.key] for s in active]

    # Fold CVE/GHSA/USN aliases together, but only where there is something to fold.
    purls_with_findings = {
        purl for r in active_results for purl, vmap in r.vulns.items() if vmap
    }
    alias_maps = build_alias_maps(active_results, purls_with_findings)
    for result in active_results:
        consolidate(result, alias_maps)

    vuln_purls = purls_with_findings

    # Show packages with findings, plus any package some scanner never looked at.
    display_purls = set(vuln_purls)
    for purl in all_purls:
        if any(purl not in results[s.key].packages for s in active):
            display_purls.add(purl)

    eco_groups = defaultdict(list)
    for purl in sorted(display_purls, key=name_version_from_purl):
        eco_groups[ecosystem_from_purl(purl)].append(purl)
    eco_order = [e for e in ECOSYSTEM_ORDER if e in eco_groups]
    eco_order += sorted(set(eco_groups) - set(ECOSYSTEM_ORDER))

    # ── Summary ───────────────────────────────────────────────────────────
    section_header("Summary")
    print(f"  {col('SBOM Components (Raw):', DIM):<32} {sbom_raw_count}")
    print(f"  {col('Deduplicated PURLs:', DIM):<32} {len(all_purls)}")
    by_eco = Counter(ecosystem_from_purl(p) for p in all_purls)
    eco_counts = [e for e in ECOSYSTEM_ORDER if e in by_eco] + sorted(set(by_eco) - set(ECOSYSTEM_ORDER))
    print(f"  {col('  by ecosystem:', DIM):<32} {' · '.join(f'{e} {by_eco[e]}' for e in eco_counts)}")
    print(f"  {col('Clean (0 vulns):', DIM):<32} {len(all_purls) - len(vuln_purls)}")
    print(f"  {col('Vulnerable:', DIM):<32} {len(vuln_purls)}")
    print()

    row_fmt = "  {:<20} | {:>14} | {:>14} | {:>14}"
    print(
        col(
            row_fmt.format("Scanner", "Pkgs Scanned", "Pkgs w/ Vulns", "Total Vuln IDs"),
            BOLD,
        )
    )
    print(rule([20, 14, 14, 14]))

    vuln_id_sets = {}
    for scanner in active:
        result = results[scanner.key]
        vuln_id_sets[scanner.key] = result.vuln_ids
        print(
            row_fmt.format(
                scanner.label,
                len(result.packages),
                len(result.detected),
                len(vuln_id_sets[scanner.key]),
            )
        )
    print()

    sets = list(vuln_id_sets.values())
    all_vuln_ids = set().union(*sets)
    consensus = set.intersection(*sets)
    at_least_two = {vid for vid in all_vuln_ids if sum(vid in s for s in sets) >= 2}

    cve_count = sum(1 for v in all_vuln_ids if v.startswith("CVE-"))
    ghsa_count = sum(1 for v in all_vuln_ids if v.startswith("GHSA-"))
    other_count = len(all_vuln_ids) - cve_count - ghsa_count

    print(
        f"  {col(f'All {len(sets)} agree:', GREEN):<18} {len(consensus):<8}"
        f"{col('≥2 agree:', BOLD):<18} {len(at_least_two):<8}"
        f"{col('Total:', BOLD):<8} {len(all_vuln_ids):<8}"
        f"{col(f'(CVE:{cve_count} GHSA:{ghsa_count} Other:{other_count})', DIM)}"
    )

    exclusive = []
    for scanner in active:
        own = vuln_id_sets[scanner.key]
        others = [vuln_id_sets[s.key] for s in active if s.key != scanner.key]
        count = len(own.difference(*others)) if others else len(own)
        exclusive.append(f"{scanner.label}:{count}")
    print(f"  {col('Exclusive to:', DIM)} {'  '.join(exclusive)}")

    unmatched_notes = [
        f"{s.label}: {len(results[s.key].unmatched)} pkgs "
        f"({len({vid for v in results[s.key].unmatched.values() for vid in v})} vulns)"
        for s in active
        if results[s.key].unmatched
    ]
    if unmatched_notes:
        print(col("  ⚠  No PURL match | " + " | ".join(unmatched_notes), YELLOW))

    # ── Package inventory ─────────────────────────────────────────────────
    legend = " ".join(f"[{s.letter}]{s.label[1:]}" for s in active)
    section_header(f"VULNERABLE PACKAGES — {legend} findings")

    for i, eco in enumerate(eco_order):
        if i:
            print()
        purls = eco_groups[eco]
        print(col(f"  ▸ {ecosystem_label(eco)} ({len(purls)} packages)", BOLD + WHITE))
        for purl in purls:
            marks = "".join(
                mark(
                    purl in results[s.key].packages,
                    bool(results[s.key].vulns.get(purl)),
                )
                for s in active
            )
            print(f"    {marks}  {purl}")

    # ── Packages that could not be matched to a PURL ──────────────────────
    for scanner in active:
        unmatched = results[scanner.key].unmatched
        if not unmatched:
            continue
        section_header(
            f"UNMATCHED {scanner.label.upper()} — {len(unmatched)} packages not mapped to a PURL"
        )
        print(f"  {col(f'Reported by {scanner.label}, but no SBOM PURL has the same', DIM)}")
        print(f"  {col('name and version, so they cannot be compared.', DIM)}")
        for (name, version), vdict in sorted(unmatched.items()):
            ver = f"@{version}" if version else ""
            print(
                f"    {name}{ver}  {col(f'({len(vdict)} vulns)', DIM)}  "
                f"{col(', '.join(sorted(vdict)), DIM)}"
            )

    # ── Vulnerability detail ──────────────────────────────────────────────
    enrichment = load_cve_enrichment(
        artifact_dir,
        {vid for vid in all_vuln_ids if vid.startswith("CVE-")},
        refresh_mode,
    )

    section_header("VULNERABILITY DETAIL — All Scanner Findings")
    print("  Every vulnerability found, and which scanners agree on it.")
    print(
        "  CVSS, EPSS and KEV come from Vulners where it knows the CVE, "
        "otherwise from the scanner that reported it."
    )
    report_cves = {vid for vid in all_vuln_ids if vid.startswith("CVE-")}
    known = [enrichment[c] for c in report_cves if c in enrichment]
    scored = sum(1 for e in known if e.get("cvss") is not None and e.get("epss") is not None)
    pct = f" ({100 * scored / len(report_cves):.1f}%)" if report_cves else ""
    print(
        f"  Vulners CVE data: {len(known)} of {len(report_cves)} CVEs known, "
        f"CVSS+EPSS on {scored}{pct}."
    )
    header = " ".join(f"{col(s.letter, BOLD)}{s.label[1:]}" for s in active)
    print(f"  {header}   SEVERITY   CVSS   EPSS  KEV   {col('↳ provenance', MAGENTA)}")

    for i, eco in enumerate(eco_order):
        eco_purls = [p for p in eco_groups[eco] if p in vuln_purls]
        if not eco_purls:
            continue
        if i:
            print()
        print(col(f"  ━━ {ecosystem_label(eco)} ━━", BOLD + CYAN))

        for purl in eco_purls:
            findings = {s.key: results[s.key].vulns.get(purl, {}) for s in active}
            all_vids = set().union(*findings.values())
            if not all_vids:
                continue

            # Full PURL, so the ecosystem is visible without reading the group header.
            print(col(f"  ┌─ {purl}", BOLD + WHITE))
            print(f"  │ {''.join(col(s.letter, BOLD) for s in active)}")

            def sort_key(vid, findings=findings):
                # Order by the severity actually shown, so Vulners' view wins here too.
                sev = norm_sev(enrichment.get(vid, {}).get("severity"))
                for vmap in findings.values():
                    if sev:
                        break
                    if vid in vmap:
                        sev = norm_sev(vmap[vid].get("severity"))
                return (0 if vid.startswith("CVE-") else 1, SEV_ORDER.get(sev, 99), vid)

            for vid in sorted(all_vids, key=sort_key):
                # Vulners is the default source for scores; the scanners' own
                # numbers only fill in what it does not have.
                vulners_data = enrichment.get(vid, {})
                severity = norm_sev(vulners_data.get("severity"))
                cvss = vulners_data.get("cvss")
                epss = vulners_data.get("epss")
                kev = bool(vulners_data.get("wild_exploited"))

                for vmap in findings.values():
                    entry = vmap.get(vid)
                    if not entry:
                        continue
                    severity = severity or norm_sev(entry.get("severity"))
                    if cvss is None:
                        cvss = entry.get("cvss")
                    if epss is None:
                        epss = entry.get("epss")

                marks = "".join(
                    mark(purl in results[s.key].packages, vid in findings[s.key])
                    for s in active
                )
                sev_display = col(
                    f"{(severity or '?').upper():<10}", sev_colour(severity)
                )
                cvss_display = f"{cvss:.1f}" if isinstance(cvss, (int, float)) else "  - "
                epss_display = (
                    f"{epss * 100:5.1f}%" if isinstance(epss, (int, float)) else "     -"
                )
                kev_display = col("KEV", RED + BOLD) if kev else col("  ·", DIM)

                provenance = [
                    f"{s.letter}:{','.join(findings[s.key][vid]['sourceAdvisories'])}"
                    for s in active
                    if findings[s.key].get(vid, {}).get("sourceAdvisories")
                ]
                prov_str = (
                    col(f"  ↳ {' | '.join(provenance)}", MAGENTA) if provenance else ""
                )
                print(
                    f"  │ {marks} {vid:<22} {sev_display} {cvss_display:>5} "
                    f"{epss_display} {kev_display}{prov_str}"
                )

            print(f"  └{'─' * 100}")


# ── Output plumbing ───────────────────────────────────────────────────────

ANSI_RE = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


class ReportFile:
    """
    Stands in for stdout while a report renders: everything goes to the report
    file, colour stripped, and nothing to the terminal. The full comparison is
    too long to read scrolling past; the terminal gets status lines instead.
    """

    def __init__(self, file_path: Path):
        self.terminal = sys.stdout
        self.file = file_path.open("w", encoding="utf-8")
        self.buffer = ""

    def write(self, message):
        self.buffer += ANSI_RE.sub("", message)
        while "\n" in self.buffer:
            line, self.buffer = self.buffer.split("\n", 1)
            self.file.write(line.rstrip() + "\n")

    def flush(self):
        self.file.flush()

    def close(self):
        if self.buffer:
            self.file.write(self.buffer.rstrip() + "\n")
        self.file.close()


def artifact_dir_for(results_dir: Path, sbom: Path) -> Path:
    """results/<sbom stem>/ — one directory per SBOM, stripping .cdx.json."""
    stem = sbom.name
    for suffix in (".json", ".cdx"):
        stem = stem.removesuffix(suffix)
    return results_dir / stem


def report_name_for(sbom: Path) -> str:
    """
    report-<sbom stem>.md, so a report carries its subject once it leaves
    results/. SBOMs are named <image>.<generator>.cdx.json, and the generator
    matters as much as the image now that each image has several SBOMs.
    """
    return f"report-{artifact_dir_for(Path('.'), sbom).name}.md"


def main() -> int:
    global USE_COLOR  # pylint: disable=global-statement

    parser = argparse.ArgumentParser(
        description="Compare OSV, Src OSV, Grype, Trivy and Vulners findings for a CycloneDX SBOM."
    )
    parser.add_argument(
        "sboms",
        nargs="*",
        type=Path,
        help=f"CycloneDX SBOM files (default: {DEFAULT_SBOM_GLOB})",
    )
    parser.add_argument(
        "--refresh",
        choices=("auto", "force", "never"),
        default="auto",
        help="auto: rescan artifacts not written today (default); "
        "force: delete scan data, then rescan everything (OSV record cache kept); "
        "never: use existing artifacts only",
    )
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=RESULTS_ROOT,
        help=f"Where per-SBOM artifact directories are created (default: {RESULTS_ROOT})",
    )
    parser.add_argument("--no-color", action="store_true", help="Disable ANSI colour")
    args = parser.parse_args()

    # Only status lines reach the terminal now, and they go to stderr.
    USE_COLOR = not args.no_color and sys.stderr.isatty()

    sboms = args.sboms or sorted(PROJECT_ROOT.glob(DEFAULT_SBOM_GLOB))
    if not sboms:
        note(f"❌ No SBOM found matching {DEFAULT_SBOM_GLOB}", RED)
        return 1

    missing = [s for s in sboms if not s.exists()]
    if missing:
        for path in missing:
            note(f"❌ SBOM file not found: {path}", RED)
        return 1

    # The OSV record cache lives beside the artifacts it was built for.
    query_osv_purl.CACHE_PATH = args.results_dir / query_osv_purl.CACHE_PATH.name
    if args.refresh == "force":
        # The OSV record cache is kept: each record is checked against OSV's
        # modified timestamp anyway, so clearing it would only re-download
        # thousands of unchanged records.
        note("Forced refresh: each SBOM's scan data is deleted before it is rescanned "
             "(OSV record cache kept; changed records are refetched).", YELLOW)

    started = time.monotonic()
    rows = []
    for number, sbom in enumerate(sboms, 1):
        sbom_started = time.monotonic()
        note(f"\n[{number}/{len(sboms)}] {sbom.name}", BOLD + CYAN)
        artifact_dir = artifact_dir_for(args.results_dir, sbom)
        artifact_dir.mkdir(parents=True, exist_ok=True)

        refresh_artifacts(sbom, artifact_dir, args.refresh)
        report_path = artifact_dir / report_name_for(sbom)
        report = ReportFile(report_path)
        sys.stdout = report
        error = None
        try:
            run_report(sbom, artifact_dir, args.refresh, load_sbom(sbom))
        except Exception as exc:  # one SBOM failing must not sink the others  # pylint: disable=broad-exception-caught
            error = f"{type(exc).__name__}: {exc}"
        finally:
            sys.stdout = report.terminal
            report.close()
        took = time.monotonic() - sbom_started
        if error:
            report_path.unlink(missing_ok=True)
            note(f"   ❌ Report failed — {error}", RED)
        else:
            shown = (
                report_path.relative_to(Path.cwd())
                if report_path.is_relative_to(Path.cwd())
                else report_path
            )
            note(f"   📄 Report → {shown}  ({fmt_duration(took)})", GREEN)
        rows.append((sbom, artifact_dir, error))

    return print_summary(rows, time.monotonic() - started)


def fmt_duration(seconds: float) -> str:
    seconds = int(seconds)
    return f"{seconds // 60}m{seconds % 60:02d}s" if seconds >= 60 else f"{seconds}s"


def print_summary(rows: list, elapsed: float) -> int:
    """
    One line per SBOM: is each column from today's scan, and did the report
    render. A comparison is complete only when every column is current; a
    column kept from an earlier day or missing outright is called out, since
    the report would otherwise compare it against fresh data without saying so.
    Returns the exit code: 0 when every comparison is complete.
    """
    today = dt.date.today()
    name_width = max(len(artifact_dir.name) for _, artifact_dir, _ in rows)
    widths = [max(len(s.label), 7) for s in SCANNERS]

    note("\nComparison status", BOLD)
    note("  " + "SBOM".ljust(name_width) + "  "
         + "  ".join(s.label.ljust(w) for s, w in zip(SCANNERS, widths)) + "  Report", BOLD)
    complete = 0
    for _sbom, artifact_dir, error in rows:
        cells, current = [], True
        for scanner, width in zip(SCANNERS, widths):
            path = artifact_dir / f"{scanner.key}.json"
            if not path.exists():
                cell, colour, current = "❌ none", RED, False
            elif artifact_date(path) != today:
                cell, colour, current = f"⚠ {artifact_date(path):%m-%d}", YELLOW, False
            else:
                cell, colour = "✅", GREEN
            # Emoji are two columns wide; pad on the visible width.
            pad = width - len(cell) - (1 if cell.startswith(("✅", "❌")) else 0)
            cells.append(col(cell, colour) + " " * max(pad, 0))
        report_cell = col("❌ failed", RED) if error else col("✅", GREEN)
        complete += bool(current and not error)
        note("  " + artifact_dir.name.ljust(name_width) + "  " + "  ".join(cells)
             + "  " + report_cell, RESET)

    total = len(rows)
    if complete == total:
        note(f"\n✅ All {total} comparisons complete and current ({fmt_duration(elapsed)})",
             BOLD + GREEN)
        return 0
    note(f"\n⚠  {complete} of {total} comparisons complete and current "
         f"({fmt_duration(elapsed)}); see the rows above. ⚠ = kept from that date, "
         "❌ = missing.", BOLD + YELLOW)
    return 1


if __name__ == "__main__":
    sys.exit(main())
