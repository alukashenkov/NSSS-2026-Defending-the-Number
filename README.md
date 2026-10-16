# Scanner Comparison Demo

**Talk:** [Defending the Number: Making an SBOM → CRA Decision You Can Explain Later](https://nsss.se/f2026/talks/making-an-sbom/)
(Andrey Lukashenkov, NSSS Fall 2026 — Nordic Software Security Summit, Stockholm, 4–6 November 2026)

Demo material for that talk. A deliberately vulnerable container image is
built, SBOMs are generated from it with two different tools (syft and Trivy), and four
vulnerability scanners are pointed at each SBOM so their findings can be compared side
by side.

The interesting result is not the vulnerability count. It is how far four scanners
disagree while looking at *identical* input, how much the same scanner's answer moves
when a different tool wrote the SBOM, and how few of the 755 findings actually
warrant attention.

> **⚠️ The application is intentionally insecure.** It hands arbitrary command
> execution to anyone who can reach port 8080. Run it only in a throwaway container on
> an isolated network, never on a shared host and never exposed beyond localhost. The
> hardcoded credentials in `insecure-app/app.py` are fake.

## Requirements

| Tool | Purpose |
|---|---|
| Docker | building the target images |
| [syft](https://github.com/anchore/syft) | SBOM generator |
| [grype](https://github.com/anchore/grype) | scanner |
| [trivy](https://github.com/aquasecurity/trivy) | SBOM generator and scanner |
| [sbomqs](https://github.com/interlynk-io/sbomqs) | SBOM quality / compliance scoring (optional) |
| Python 3.10+ | the comparison tooling |

```sh
python3 -m pip install -r requirements.txt
```

That file is for the tooling at the repo root. `insecure-app/requirements.txt` is the
target application's, pinned to vulnerable versions on purpose — keep the two apart.

OSV is queried over its public API, so it needs no local install.

### Vulners API key

The Vulners column and the CVSS/EPSS/KEV enrichment need a
[Vulners](https://vulners.com) API key.

1. Sign up or log in at [vulners.com](https://vulners.com/login).
2. **Recommended:** start the free 30-day trial from your account (see
   [pricing](https://vulners.com/pricing)). The free plan works too, but its 100 API
   credits a month run out quickly here. A full refresh of all four SBOMs makes on
   the order of 130 Vulners requests: four SBOM audits, plus CVE lookups in batches of
   100 (once for the report, once for OSV's enrichment). Most of them come from the
   4,480 CVEs on the 24.04 Trivy SBOM. That is more than the free plan's monthly
   credits in a single run, and the daily refresh repeats it every day you run it.
3. Open the **API keys** tab in your account and generate a key. Give it a name,
   choose the **`api`** scope, and pick the license you want it billed against. Each
   license (free, trial, paid) needs its own key, so if you started the trial,
   generate the key under the trial license.
4. Put the key in a `.env` file at the repo root:

   ```
   VULNERS_API_KEY=your-key-here
   ```

   `.env` is gitignored, so the key stays out of commits. Both scripts load it
   automatically via `python-dotenv`, and it is sent only as the `X-Api-Key` header.

See the [authentication docs](https://docs.vulners.com/docs/quickstart/authentication/)
for the full key options, such as IP allow-listing.

Without a key, the Vulners column and the CVSS/EPSS/KEV enrichment degrade quietly and
the rest of the report still renders. Grype and Trivy are optional in the same way — a
missing binary drops that column instead of failing the run.

## 1. Build the images

Two base images, built as separate tags so both can be scanned side by side:

```sh
cd insecure-app
docker build -t insecureapp-20.04 -f Dockerfile .
docker build -t insecureapp-24.04 -f Dockerfile.24.04 .
```

The two Dockerfiles are identical except for the base image and the
`--break-system-packages` pip flag that Ubuntu 24.04's PEP 668 requires. Keep them in
sync. `add-apt-repository` hardcodes `arch=arm64`, so amd64 hosts need `--platform` or
an edit.

To run the app: `docker run --rm -p 8080:8080 insecureapp-20.04` → http://localhost:8080

## 2. Generate the SBOMs

Each image gets two SBOMs, one from syft and one from Trivy, so the comparison covers
the SBOM generator as well as the scanner. All four live in `sboms/`, named
`<image>.<generator>.cdx.json`:

```sh
cd sboms
for tag in 20.04 24.04; do
  SYFT_FILE_METADATA_SELECTION=none \
  SYFT_GOLANG_MAIN_MODULE_VERSION_FROM_CONTENTS=true \
  SYFT_FORMAT_PRETTY=true \
  syft "insecureapp-${tag}:latest" \
    --source-name "insecureapp-${tag}:latest" \
    -o "cyclonedx-json=insecureapp-${tag}.syft.cdx.json"
  trivy image "insecureapp-${tag}:latest" \
    --image-src docker \
    --detection-priority comprehensive \
    --format cyclonedx \
    --output "insecureapp-${tag}.trivy.cdx.json"
done
```

Both generators read the same local image, so any difference between an image's two
SBOMs comes from the generator, not the input. If you rebuild an image, regenerate
both of its SBOMs together.

### syft parameters

Every parameter is load-bearing:

| Parameter | Why |
|---|---|
| `--source-name "…:latest"` | Puts the full `name:tag` in `metadata.component.name`. Syft otherwise records the repo name without the tag, leaving two SBOMs that are hard to tell apart on a slide. The image digest still lands in `metadata.component.version`. |
| `SYFT_FILE_METADATA_SELECTION=none` | Suppresses ~11k per-file components. They bury the 684 packages the demo is about and quadruple the file size. |
| `SYFT_GOLANG_MAIN_MODULE_VERSION_FROM_CONTENTS=true` | Recovers versions for Go main modules built without VCS stamping. Without it, syft emits version-less PURLs such as `pkg:golang/github.com/docker/compose/v2`, which no version-matching scanner can resolve — they showed up as packages Vulners "failed" to scan. |
| `SYFT_FORMAT_PRETTY=true` | Indented JSON. Same content, readable and diffable. |
| `-o cyclonedx-json=…` | CycloneDX is the one format all four scanners accept. |

Note that `SYFT_GOLANG_CAPTURE_SYMBOLS` is deliberately **not** set: Go function
symbols have nowhere to live in CycloneDX, so enabling it changes nothing but syft's
internal package-id hashes. Grype will warn that Go matching falls back to module
granularity; that is the format's limit, and in practice it costs nothing here —
every Grype-exclusive finding in both images is a `deb` package, not a Go module.

### Trivy parameters

Trivy's defaults (0.76.0) already give what the syft parameters above have to ask
for: CycloneDX 1.7, `name:tag` in `metadata.component.name`, no per-file components,
versioned Go main modules and indented JSON. Only these flags matter:

| Parameter | Why |
|---|---|
| `--detection-priority comprehensive` | Keeps Python packages that were installed by dpkg. By default (`precise`) Trivy drops any language package whose files belong to an OS package. That loses 15 of 39 PyPI packages on 20.04, including the distro's copy of the requests stack (see *Known gaps*), and 3 of 27 on 24.04 (`pip`, `setuptools`, `wheel`). With this flag the PyPI and deb sets match syft's exactly. |
| `--image-src docker` | Pins the source to the local Docker daemon, which syft reads too. Docker is first in Trivy's default order anyway, but without the pin a missing local image would silently be pulled from a registry instead. |
| `--format cyclonedx` | A CycloneDX SBOM with an empty `vulnerabilities` array. Vulnerabilities are only added with `--scanners vuln`, which would turn the SBOM into a scan result. |

### What still differs between generators

These differences come from each tool's output format, and no flag removes them:

| | syft | Trivy |
|---|---|---|
| Packages (20.04 / 24.04) | 684 / 616 | 683 / 615 — no `github.com/docker/cli/cmd/docker` main module |
| Deb epoch | in the version: `bsdutils@1%3A2.34-…` | a qualifier: `bsdutils@2.34-…?epoch=1` |
| Deb source package | `upstream=util-linux` PURL qualifier | `aquasecurity:trivy:SrcName` / `SrcVersion` properties |
| Image digest | `metadata.component.version`, the manifest digest | only in the `pkg:oci` PURL, the Docker image ID |
| Extra components | none | an `application` per Go binary (`docker`, `docker-compose`, `docker-buildx`) and an `operating-system`, none with a PURL |
| Supplier / hashes | none | supplier on every deb, hashes on PyPI packages |
| Dependency graph | per-package `dependencies`, but none from the root | root declares its top-level dependencies |

The epoch spelling is folded together by `compare_scanners.py` (see *How packages
and vulnerabilities are matched*). The source-package spelling is not, because it
changes what the scanners themselves find. See *Same image, different SBOM*.

### SBOM quality

All four SBOMs are also scored against the NTIA minimum elements (the 2026 revision, which
sbomqs also exposes as `--cisa-2026`):

```sh
cd sboms
for sbom in *.cdx.json; do
  stem="${sbom%.cdx.json}"
  sbomqs compliance --cisa-2026 "$sbom" > "${stem}.sbomqs-cisa2026.txt"
  sbomqs compliance --cisa-2026 --json "$sbom" > "${stem}.sbomqs-cisa2026.json"
done
```

Both reports live next to the SBOM they describe, `.txt` being the per-element table
sbomqs prints and `.json` the same report machine-readably (`summary` plus a
`sections` entry per element). Like the SBOMs, they are generated artifacts —
regenerate rather than hand-edit. `--basic` prints just the score if that is all you
need.

| Element | 20.04 syft | 20.04 Trivy | 24.04 syft | 24.04 Trivy |
|---|---|---|---|---|
| **Score** | **5.0** | **5.6** | **5.0** | **5.5** |
| Data format, spec version, tool name/version, SBOM version, timestamp | ✔ | ✔ | ✔ | ✔ |
| Author, generation context | ✘ | ✘ | ✘ | ✘ |
| Relationships | ✘ | ✔ | ✘ | ✔ |
| Component name | 686 / 686 | 688 / 688 | 618 / 618 | 620 / 620 |
| Component version | 686 / 686 | 684 / 688 | 618 / 618 | 616 / 620 |
| Component unique ID (PURL) | 685 / 686 | 684 / 688 | 617 / 618 | 616 / 620 |
| Component license | 331 / 686 | 276 / 688 | 272 / 618 | 223 / 620 |
| Component producer | 29 / 686 | 293 / 688 | 18 / 618 | 249 / 620 |
| Component hash algorithm / value | 0 / 686 | 39 / 688 | 0 / 618 | 27 / 620 |

sbomqs scores every component in the file, including the root, so its counts are one
above the package count for syft. For Trivy they are four above: the root container,
the `operating-system` component, and the per-binary `application` components. Those
extra components are also the ones with no version or PURL.

syft's gaps come from its CycloneDX output: no `metadata.authors`, no lifecycle
phase, no dependencies declared from the root, and no `hashes` on deb, pypi or golang
packages. Trivy fills in the root relationships, deb suppliers and PyPI hashes, so it
scores higher, but it records fewer licences.

That makes a useful counterpoint on a slide. The better-scoring SBOM is the one on which
Grype finds 26 vulnerable Ubuntu packages instead of 157 (see *Same image, different SBOM*). The
score measures document completeness, not whether the SBOM works.

## 3. Compare the scanners

```sh
python3 compare_scanners.py                 # every SBOM in sboms/, refresh anything not scanned today
python3 compare_scanners.py --refresh force # rescan now
python3 compare_scanners.py --refresh never # re-render from existing artifacts, no network
python3 compare_scanners.py sboms/insecureapp-20.04.syft.cdx.json sboms/insecureapp-20.04.trivy.cdx.json
```

A full forced rescan of all four SBOMs takes ~50 s; re-rendering takes a few seconds.

The OSV scanner is also usable on its own, which is handy for showing a single
source's view before the four-way comparison:

```sh
python3 query_osv_purl.py sboms/insecureapp-20.04.syft.cdx.json
```

## Output

Each SBOM gets its own directory, named after it (`results/insecureapp-20.04.syft/`),
with one file per scanner:

```
results/<sbom-name>/osv.json                # via query_osv_purl.py
results/<sbom-name>/grype.json              # grype, CycloneDX
results/<sbom-name>/trivy.json              # trivy, native JSON
results/<sbom-name>/vulners.json            # Vulners SBOM audit API
results/<sbom-name>/vulners-cve-data.json   # per-CVE CVSS/EPSS/KEV
results/<sbom-name>/report-<sbom-name>.md   # the rendered comparison
results/.osv-details-cache.json             # shared OSV record cache
```

The sbomqs reports are the exception: they describe an SBOM rather than a scan, so
they sit beside it in `sboms/` as `<sbom-name>.sbomqs-cisa2026.{txt,json}`.

The report prints to the terminal in colour and to the Markdown file without it. The
filename carries the SBOM name, and with it the image and the generator
(`report-insecureapp-20.04.trivy.md`), so reports stay distinguishable once they are
copied out of `results/`.

### Reading the report

Each report opens with the provenance of what it describes, so it stays meaningful
once it is moved out of `results/`, mailed around or pasted into slides:

```markdown
# Vulnerability Comparison Report — insecureapp-20.04:latest

- **Image:** `insecureapp-20.04:latest`
- **Digest:** `sha256:ca3fa0cb11c0295b461fc4674d29bf9569df312c71dc62e468b85baab422102d`
- **SBOM:** `insecureapp-20.04.syft.cdx.json` — CycloneDX 1.7, syft 1.54.1, built 2026-10-16T12:38:24+02:00
- **Report generated:** 2026-10-16T12:40:38
- **Scanners:** OSV (api.osv.dev) · Grype (grype 0.120.1) · Trivy (trivy 0.76.0) · Vulners (vulners.com audit API v4)
```

The image name and digest come from the SBOM's `metadata.component`, and each scanner
version is read from its own artifact — so the header describes the run that actually
happened, not what the commands were supposed to do.

Then, per package:

```
┌─ pkg:pypi/aiohttp@3.9.1
│ OGTV
│ ✔✔✔✔ CVE-2024-23334    HIGH    7.5  76.9% KEV  ↳ O:GHSA-5h86-8mv2-jq9f,PYSEC-2024-24 | V:GHSA-5H86-8MV2-JQ9F
┌─ pkg:pypi/cryptography@3.3.2
│ OGTV
│ ✔✘✘✔ CVE-2026-69248    HIGH    8.3   0.3%   ·  ↳ O:PYSEC-2026-3554 | V:OSV:PYSEC-2026-3554
│ ✘✘✘✔ CVE-2026-34180    HIGH    7.5   1.0%   ·  ↳ V:SNYK:PYTHON-CRYPTOGRAPHY-17344551
```

`OGTV` are OSV, Grype, Trivy and Vulners. Per scanner: `✔` found it, `✘` scanned the
package but did not report it, `-` never saw the package at all — a distinction that
matters, because "didn't find" and "didn't look" are very different claims.

`↳ provenance` lists the IDs each scanner *originally* used before they were folded
onto the CVE, so a disagreement can be traced to a naming difference rather than a
genuine miss.

Severity, CVSS, EPSS and the KEV flag come from a single Vulners lookup of the CVE
itself, so a row's label and score always agree; scanner-reported values only fill
gaps. `KEV` is Vulners' `wildExploited` flag — exploited in the wild, which is broader
than the CISA KEV catalogue alone.

### How packages and vulnerabilities are matched

Two normalisation layers do the real work, and both matter when a result looks wrong.

**Package identity.** Scanners spell the same package differently. Qualifiers
(`?arch=arm64`) get stripped, `v`/`go` version prefixes are normalised, and names are
compared case-insensitively — Trivy and Vulners lowercase Go module paths while syft,
Grype and OSV preserve the upstream spelling, so `github.com/AlecAivazis/survey/v2`
would otherwise be counted twice. Only the join key is folded; the report still shows
the SBOM's own spelling. Version-less PURLs are folded onto a versioned sibling when
the name has exactly one known version. A deb epoch is the one qualifier kept: Trivy
writes it as `?epoch=1` where syft and Vulners put it in the version (`1:2.34-…`), so
it is moved back into the version before joining.

**Vulnerability identity.** The same issue arrives as a CVE, a GHSA, a USN or a PYSEC
ID. Each finding's provenance is used to fold aliases together per package, always
preferring the CVE, and alias chains are resolved to a fixed point. Severity
vocabularies are unified too (GHSA `MODERATE` → `MEDIUM`, Red Hat `IMPORTANT` →
`HIGH`).

### Daily refresh

Vulnerability data changes daily, so freshness is tracked per artifact: anything whose
mtime is not today is re-scanned before the report renders. One run a day always
compares current data, and a second run the same day is nearly free. Grype and Trivy
update their own databases on each invocation; the OSV record cache and the CVE
enrichment self-discard when the date rolls over.

## Current results

These are from the 2026-10-16 run, whose reports are in `results/`. A rerun on a
later day will change the numbers.

| | 20.04 syft | 20.04 Trivy | 24.04 syft | 24.04 Trivy |
|---|---|---|---|---|
| SBOM components | 685 | 687 | 617 | 619 |
| Deduplicated PURLs | 541 | 540 | 535 | 534 |
| Packages with findings | 206 | 172 | 152 | 133 |
| OSV / Grype / Trivy / Vulners — vuln IDs | 513 / 688 / 222 / 533 | 511 / 477 / 223 / 533 | 275 / 360 / 197 / 311 | 274 / 252 / 4381 / 311 |
| All four agree | 222 | 222 | 188 | 187 |
| Total distinct | 755 | 681 | 422 | 4499 |
| Exclusive to one scanner | OSV 33, Grype 77, Trivy 0, Vulners 29 | OSV 33, Grype 2, Trivy 1, Vulners 165 | OSV 21, Grype 28, Trivy 0, Vulners 30 | OSV 21, Grype 0, Trivy 4105, Vulners 31 |
| Exploited in the wild | 1 | 1 | 1 | 4 |

All four scanners cover every package in every SBOM. On the syft SBOMs, only one of
the 755 / 422 findings is known to be exploited in the wild: `CVE-2024-23334` in
aiohttp, with 76.9% EPSS.

### Same image, different SBOM

OSV and Vulners give nearly the same answer for both SBOMs of an image, because they
match on name and version alone. Grype and Trivy do not. Both match Ubuntu
advisories by *source* package, and each reads the source package only from its own
generator's SBOM format:

- **Grype on a Trivy SBOM** reads source packages from syft's `upstream=` PURL
  qualifier. Trivy records them in `aquasecurity:trivy:Src*` properties instead, so
  Grype only matches debs whose binary name equals their source name. On 20.04 it
  finds 26 vulnerable Ubuntu packages instead of 157; all 131 it misses are packages
  like `bsdutils` (source `util-linux`). Grype's exclusive findings fall from 77 to 2,
  and the findings it shared with Vulners become Vulners-exclusive (29 → 165).
- **Trivy on its own SBOM** gets `SrcName=linux` *and* `SrcVersion` for
  `linux-libc-dev`, so on 24.04 it matches Ubuntu's whole kernel CVE list against the
  kernel headers package: 4,102 findings (2,682 affected, 1,420 fixed). Three of them
  are exploited in the wild. syft's `upstream=linux` carries no version, so Trivy
  finds none of these on the syft SBOM, and no other scanner flags `linux-libc-dev` on
either SBOM.
  On 20.04, Trivy reports nothing against `linux-libc-dev` from either SBOM.

Scanning the same image, the same scanner reports 197 or 4,381 findings depending on
which tool wrote the SBOM. Neither generator's output is "wrong", but each is only fully
understood by its own vendor's scanner.

## Adding a scanner

Add one `Scanner(...)` entry to `SCANNERS` in `compare_scanners.py` plus a
`refresh_*` / `load_*` pair. Every report section iterates that tuple, so nothing else
needs touching. A loader returns a `ScanResult` keyed by PURL, or by `(name, version)`
with `keyed_by_purl=False` when the scanner does not emit PURLs, as Vulners does not.

## Known gaps

- On 20.04, pip installs the `requests==2.19.1` pin (and its `urllib3` 1.23 /
  `idna` 2.7 dependencies) alongside the distro's `python3-requests` deb, so the image
  carries two copies of each: `requests` 2.19.1 + 2.22.0, `urllib3` 1.23 + 1.25.8,
  `idna` 2.7 + 2.8, and both versions show up in its report. 24.04 has only the pinned
  copies.
- `tutorial.db` is never created. The startup `SELECT` in `app.py` is wrapped in a
  bare `except: pass` and always fails silently — the query exists to be flagged by
  static analysis, not to work.
