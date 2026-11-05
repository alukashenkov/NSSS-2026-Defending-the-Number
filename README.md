# Scanner Comparison Demo

![NSSS 2026: Beyond Compliance, Building Resilience](slides/nsss-2026-banner.png)

**Talk:** [Defending the Number: Making an SBOM → CRA Decision You Can Explain Later](https://nsss.se/f2026/talks/making-an-sbom/)
(Andrey Lukashenkov, NSSS Fall 2026 — Nordic Software Security Summit, Stockholm, 4–6 November 2026)

**Slides:** [NSSS-Defending-the-Number-v1.pdf](slides/NSSS-Defending-the-Number-v1.pdf) (the deck as delivered)

Demo material for that talk. A deliberately vulnerable container image is
built, SBOMs are generated from it with two different tools (syft and Trivy), and four
vulnerability scanners are pointed at each SBOM so their findings can be compared side
by side. OSV runs twice, once by binary package name and once by source package
(*Src OSV*), so the report has five columns.

The interesting result is not the vulnerability count. It is how far the scanners
disagree while looking at *identical* input, how much the same scanner's answer moves
when a different tool wrote the SBOM or a different lookup key is used, and how few
of the findings actually warrant attention.

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
   credits a month run out quickly here. A full refresh makes one SBOM audit per SBOM,
   plus CVE lookups in batches of 100: once for the report, and once for each OSV
   mode's enrichment. The request count therefore grows with the number of CVEs found.
   Kernel-heavy results dominate it: Trivy on its own 24.04 SBOM, and Src OSV on
   every SBOM. A single run can exceed the free plan's monthly credits, and the daily
   refresh repeats it every day you run it.
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
| `-o cyclonedx-json=…` | CycloneDX is the one format every scanner here accepts. |

Note that `SYFT_GOLANG_CAPTURE_SYMBOLS` is deliberately **not** set: Go function
symbols have nowhere to live in CycloneDX, so enabling it changes nothing but syft's
internal package-id hashes. Grype will warn that Go matching falls back to module
granularity; that is the format's limit, not something a flag can fix.

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
changes what Grype and Trivy themselves find. See *Same image, different SBOM*. Src
OSV is the one column that reads both spellings (see *OSV by source package*).

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
Grype misses most of its Ubuntu findings (see *Same image, different SBOM*). The
score measures document completeness, not whether the SBOM works.

## 3. Compare the scanners

```sh
python3 compare_scanners.py                 # every SBOM in sboms/, refresh anything not scanned today
python3 compare_scanners.py --refresh force # delete scan data, rescan everything (OSV record cache kept)
python3 compare_scanners.py --refresh never # re-render from existing artifacts, no network
python3 compare_scanners.py sboms/insecureapp-20.04.syft.cdx.json sboms/insecureapp-20.04.trivy.cdx.json
```

Re-rendering takes a few seconds. A rescan runs the scanners concurrently, and
fetches OSV records through a pool shared across SBOMs. Src OSV pulls in far more OSV
records than plain OSV (about 5,000, mostly Ubuntu kernel CVEs), so the very first run,
and any `--refresh force`, takes several minutes fetching them. After that the records
are cached across days: OSV's batch query reports each record's `modified` timestamp,
and only records whose timestamp has changed since they were cached are fetched again.

The OSV scanner is also usable on its own, which is handy for showing a single
source's view before the full comparison:

```sh
python3 query_osv_purl.py sboms/insecureapp-20.04.syft.cdx.json            # binary names, as the SBOM spells them
python3 query_osv_purl.py sboms/insecureapp-20.04.syft.cdx.json --source   # deb packages by source package
```

### OSV by source package (Src OSV)

OSV's Ubuntu records are keyed by *source* package. A query for `openssl` at
`1.1.1f-1ubuntu2.24` returns its advisories, while `libssl1.1` at the same version
returns nothing. Querying the
SBOM's binary PURLs as-is therefore only matches debs whose binary name equals their
source name. The **Src OSV** column asks OSV about each deb's source package instead
and reports the hits against the binary PURL. PyPI and Go packages are queried
unchanged.

The source package is read from wherever the generator put it:

| | syft | Trivy |
|---|---|---|
| Source name | `upstream=util-linux` PURL qualifier | `aquasecurity:trivy:SrcName` property |
| Source version | `upstream=util-linux%402.34-0.1ubuntu9.6`; absent means same as the binary | `SrcEpoch` + `SrcVersion` + `SrcRelease` properties |
| No source recorded | the deb is its own source | the deb is its own source |

The query is written as `pkg:deb/ubuntu/<source>@<epoch%3Aversion>?distro=…`, with
the epoch inline. That matters for Trivy SBOMs: OSV ignores an `?epoch=1` qualifier
and matches Ubuntu records against exact version lists that carry the epoch, so
`diffutils@3.7-3?epoch=1` matches nothing while `diffutils@1%3A3.7-3` matches. A
dropped epoch is a miss, not an over-match. Plain OSV makes the same fix: it queries
each PURL as the SBOM spells it but moves a `?epoch=` inline, so it gives the same
answer on both SBOMs of an image. The SBOM file itself is never rewritten.
Both generators' encodings resolve to identical source queries (293 debs → 160 sources
on 20.04, 249 → 140 on 24.04), so Src OSV gives the same answer for both SBOMs of an
image.

OSV also ignores the `distro=` qualifier. The hits are still release-correct, because Ubuntu
records list the affected versions explicitly for each release. A match means the
installed source version appears in that release's own entry.

What the extra findings are:

- **Mostly kernel CVEs against the kernel headers.** syft's `upstream=linux` has no
  version, which Src OSV reads as "same as the binary", so `linux-libc-dev` is
  queried as source `linux` at the kernel version. These are the bulk of Src OSV's
  findings on both images. This is the same trap Trivy falls into on its
  own 24.04 SBOM (see *Same image, different SBOM*). A container never runs the
  kernel whose headers it ships.
- **Ubuntu's full per-CVE tracker.** Most hits are `UBUNTU-CVE-*` records, which
  include CVEs Ubuntu has not fixed or has deferred. Kernel hits also bring
  `LSN-*` Livepatch notices, which only apply to a running host kernel. Notices
  (`USN-*` and `LSN-*`) list every CVE they cover across every release they
  cover, and OSV matches the notice as a whole, so a notice is shown only as
  provenance on CVEs whose own `UBUNTU-CVE-*` record also matched, and never adds
  a finding of its own.
- **Genuine misses by plain OSV.** For example, `libssl1.1` picks up the `openssl`
  USNs, which plain OSV cannot see under the binary name.

For non-deb packages, and debs whose binary and source names match, both modes send
the same query. Src OSV is therefore a superset of plain OSV,
and plain OSV should have no exclusive findings. What its column shows is how much a
binary-name lookup misses.

## Output

Each SBOM gets its own directory, named after it (`results/insecureapp-20.04.syft/`),
with one file per scanner:

```
results/<sbom-name>/osv.json                # via query_osv_purl.py
results/<sbom-name>/osv-src.json            # via query_osv_purl.py --source
results/<sbom-name>/grype.json              # grype, CycloneDX
results/<sbom-name>/trivy.json              # trivy, native JSON
results/<sbom-name>/vulners.json            # Vulners SBOM audit API
results/<sbom-name>/vulners-cve-data.json   # per-CVE CVSS/EPSS/KEV
results/<sbom-name>/report-<sbom-name>.md   # the rendered comparison
results/.osv-details-cache.json             # shared OSV record cache: identity, severity, modified; kept across days
```

The sbomqs reports are the exception: they describe an SBOM rather than a scan, so
they sit beside it in `sboms/` as `<sbom-name>.sbomqs-cisa2026.{txt,json}`.

The report is written only to the Markdown file. The terminal shows progress instead:
a live status line while scanners run, one line per scanner as it finishes, the report
path per SBOM, and a closing **Comparison status** table with one row per SBOM. In that
table ✅ means scanned today, `⚠ 10-31` means kept from an earlier day (its refresh
failed or was skipped), and `❌ none` means no artifact. The exit code is 0 only when
every comparison is complete and current.

`--refresh force` deletes each SBOM's artifacts, CVE enrichment and report just before
that SBOM is rescanned. The shared OSV record cache is kept, since every cached record
is checked against OSV's `modified` timestamp and refetched if it changed. A scanner that then fails
shows as missing rather than as yesterday's answer. Grype's and Trivy's own
vulnerability databases are not deleted; both update them on every run anyway. The
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
- **Report generated:** 2026-11-02T15:41:06
- **Scanners:** OSV (api.osv.dev) · Src OSV (api.osv.dev, by source package) · Grype (grype 0.121.0) · Trivy (trivy 0.76.1) · Vulners (vulners.com audit API v4)
```

The image name and digest come from the SBOM's `metadata.component`, and each scanner
version is read from its own artifact — so the header describes the run that actually
happened, not what the commands were supposed to do.

Then, per package (values illustrative; they move with every rescan):

```
┌─ pkg:pypi/aiohttp@3.9.1
│ OSGTV
│ ✔✔✔✔✔ CVE-2024-23334    HIGH      7.5  76.9% KEV  ↳ O:GHSA-5h86-8mv2-jq9f,PYSEC-2024-24 | S:GHSA-5h86-8mv2-jq9f,PYSEC-2024-24 | V:GHSA-5H86-8MV2-JQ9F
┌─ pkg:deb/ubuntu/libssl1.1@1.1.1f-1ubuntu2.24
│ OSGTV
│ ✘✔✘✘✘ CVE-2024-5535     CRITICAL  9.1   5.6%   ·  ↳ S:USN-8678-2
┌─ pkg:deb/ubuntu/linux-libc-dev@5.4.0-216.236
│ OSGTV
│ ✘✔✘✘✘ CVE-2023-2640     HIGH      7.8  15.2% KEV  ↳ S:UBUNTU-CVE-2023-2640
```

`OSGTV` are OSV, Src OSV, Grype, Trivy and Vulners. Per scanner: `✔` found it, `✘` scanned the
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
update their own databases on each invocation; the CVE enrichment self-discards when
the date rolls over, and the OSV record cache refetches any record OSV has modified. If a scanner's refresh fails, its
previous artifact is kept and the report header lists it under **⚠ Not scanned today**,
so a column that is days older than its neighbours is visible rather than silent.

## Reading the comparison

The report states the numbers. These are the principles for reading them:

- **Agreement is the stable signal.** "All five agree" is the set every lookup
  method finds. It is typically the PyPI and Go findings, which have no binary/source
  split to get wrong. Totals move with every
  rescan and with every change of lookup method. The agreed core moves far less.
- **Exclusive counts usually measure a matching method, not a scanner's
  knowledge.** A column with thousands of exclusive findings is almost always
  matching a source package that others don't. Src OSV and Trivy-on-Trivy match
  the kernel source against `linux-libc-dev`. A column that drops to near-zero
  exclusives has usually lost its source mapping, as Grype does on a Trivy SBOM.
  Check the `↳ provenance` IDs before reading a difference as a miss.
- **Exploited-in-the-wild needs context.** The KEV flag is per CVE, not per
  deployment. Kernel CVEs matched against kernel headers carry it like any other
  CVE, yet a container never runs that kernel. The application-dependency rows
  (aiohttp, cryptography, requests…) are the ones that describe code the container
  actually executes. The more complete the lookup, the more alarming-looking
  findings it adds that are about a kernel the container does not run.

### Same image, different SBOM

OSV and Vulners give nearly the same answer for both SBOMs of an image, because they
match on name and version alone. Src OSV gives *exactly* the same answer, because it
reads both generators' source-package encodings. Grype and Trivy do not. Both match Ubuntu
advisories by *source* package, and each reads the source package only from its own
generator's SBOM format:

- **Grype on a Trivy SBOM** reads source packages from syft's `upstream=` PURL
  qualifier. Trivy records them in `aquasecurity:trivy:Src*` properties instead, so
  Grype only matches debs whose binary name equals their source name. It misses every
  package like `bsdutils` (source `util-linux`). Its exclusive findings all but
  vanish, and the findings it shared with Vulners become Vulners-exclusive.
- **Trivy on its own SBOM** gets `SrcName=linux` *and* `SrcVersion` for
  `linux-libc-dev`. On 24.04 that makes it match Ubuntu's whole kernel CVE list,
  fixed and unfixed, against the kernel headers package. syft's `upstream=linux`
  carries no version, so Trivy finds none of these on the syft SBOM. On 20.04, Trivy
  reports nothing against `linux-libc-dev` from either SBOM.
- **Src OSV** treats syft's version-less `upstream=linux` as "same version as the
  binary", so it flags `linux-libc-dev` on every SBOM. On the 24.04 Trivy SBOM most
  of those overlap with Trivy's kernel findings, which is why Src OSV's exclusive
  count is much lower there than on syft's SBOM.

Scanning the same image, the same scanner can report an order of magnitude more
findings depending on which tool wrote the SBOM. Neither generator's output is "wrong", but each is only fully
understood by its own vendor's scanner.

## Adding a scanner

Add one `Scanner(...)` entry to `SCANNERS` in `compare_scanners.py` plus a
`refresh_*(sbom, out_path, progress)` / `load_*` pair; `progress` is an optional
callback for the live status line. Every report section iterates that tuple, so nothing else
needs touching. A loader returns a `ScanResult` keyed by PURL, or by `(name, version)`
with `keyed_by_purl=False` when the scanner does not emit PURLs, as Vulners does not.

## Tests

`test_query_osv_purl.py` pins the rules the OSV columns depend on: how `dedupe_vulns`
folds aliases and Ubuntu notices, how a Trivy `?epoch=` moves inline in binary-mode
queries, and when a cached OSV record is reused. It is stdlib `unittest` only and
makes no network calls:

```sh
python3 -m unittest test_query_osv_purl
```

## Known gaps

- On 20.04, pip installs the `requests==2.19.1` pin (and its `urllib3` 1.23 /
  `idna` 2.7 dependencies) alongside the distro's `python3-requests` deb, so the image
  carries two copies of each: `requests` 2.19.1 + 2.22.0, `urllib3` 1.23 + 1.25.8,
  `idna` 2.7 + 2.8, and both versions show up in its report. 24.04 has only the pinned
  copies.
- `tutorial.db` is never created. The startup `SELECT` in `app.py` is wrapped in a
  bare `except: pass` and always fails silently — the query exists to be flagged by
  static analysis, not to work.

## License

[MIT](LICENSE).
