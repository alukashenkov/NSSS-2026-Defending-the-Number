# Vulnerability Comparison Report — insecureapp-24.04:latest

- **Image:** `insecureapp-24.04:latest`
- **Digest:** `sha256:18a28020dd5cf4d3243ac372e7860ddca3e32fd2caa79aa7c541cb860db27952`
- **SBOM:** `insecureapp-24.04.syft.cdx.json` — CycloneDX 1.7, syft 1.54.1, built 2026-10-16T12:38:30+02:00
- **Report generated:** 2026-11-02T15:43:13
- **Scanners:** OSV (api.osv.dev) · Src OSV (api.osv.dev, by source package) · Grype (grype 0.121.0) · Trivy (trivy 0.76.1) · Vulners (vulners.com audit API v4)

## Summary

  SBOM Components (Raw):   617
  Deduplicated PURLs:      535
    by ecosystem:          pypi 27 · deb 249 · golang 259
  Clean (0 vulns):         370
  Vulnerable:              165

  Scanner              |   Pkgs Scanned |  Pkgs w/ Vulns | Total Vuln IDs
  ---------------------+----------------+----------------+---------------
  OSV                  |            535 |             50 |            287
  Src OSV              |            535 |            157 |           5042
  Grype                |            535 |            152 |            396
  Trivy                |            535 |             47 |            211
  Vulners              |            535 |            106 |            335

  All 5 agree: 211     ≥2 agree:  407     Total: 5079    (CVE:5046 GHSA:8 Other:25)
  Exclusive to: OSV:0  Src OSV:4635  Grype:0  Trivy:0  Vulners:37

## VULNERABLE PACKAGES — [O]SV [S]rc OSV [G]rype [T]rivy [V]ulners findings

  ▸ Python (PyPI) (12 packages)
    ✔✔✔✔✔  pkg:pypi/aiohttp@3.9.1
    ✔✔✔✔✔  pkg:pypi/certifi@2026.7.22
    ✔✔✔✔✔  pkg:pypi/cryptography@3.3.2
    ✔✔✔✔✔  pkg:pypi/flask@3.0.2
    ✔✔✔✔✔  pkg:pypi/idna@2.7
    ✔✔✔✔✔  pkg:pypi/multidict@6.7.1
    ✔✔✔✔✔  pkg:pypi/pip@24.0
    ✔✔✔✔✔  pkg:pypi/requests@2.19.1
    ✔✔✔✔✔  pkg:pypi/setuptools@68.1.2
    ✔✔✔✔✔  pkg:pypi/urllib3@1.23
    ✔✔✔✔✔  pkg:pypi/werkzeug@3.1.8
    ✔✔✔✔✔  pkg:pypi/wheel@0.42.0

  ▸ Debian/Ubuntu (deb) (125 packages)
    ✔✔✔✔✔  pkg:deb/ubuntu/binutils@2.42-4ubuntu2.10
    ✘✔✔✘✔  pkg:deb/ubuntu/binutils-aarch64-linux-gnu@2.42-4ubuntu2.10
    ✘✔✔✘✔  pkg:deb/ubuntu/binutils-common@2.42-4ubuntu2.10
    ✘✔✔✘✘  pkg:deb/ubuntu/bsdutils@1%3A2.39.3-9ubuntu6.5
    ✔✔✔✔✔  pkg:deb/ubuntu/bzip2@1.0.8-5.1build0.1
    ✔✔✘✘✘  pkg:deb/ubuntu/ca-certificates@20260601~24.04.1
    ✔✔✔✔✔  pkg:deb/ubuntu/coreutils@9.4-3ubuntu6.2
    ✘✔✔✘✘  pkg:deb/ubuntu/cpp@4%3A13.2.0-7ubuntu1
    ✘✔✔✘✘  pkg:deb/ubuntu/cpp-13@13.3.0-6ubuntu2~24.04.1
    ✘✔✔✘✘  pkg:deb/ubuntu/cpp-13-aarch64-linux-gnu@13.3.0-6ubuntu2~24.04.1
    ✘✔✔✘✘  pkg:deb/ubuntu/cpp-aarch64-linux-gnu@4%3A13.2.0-7ubuntu1
    ✔✔✔✔✔  pkg:deb/ubuntu/curl@8.5.0-2ubuntu10.11
    ✔✔✔✔✔  pkg:deb/ubuntu/dash@0.5.12-6ubuntu5
    ✔✔✔✔✔  pkg:deb/ubuntu/diffutils@1%3A3.10-1build1
    ✘✔✔✘✘  pkg:deb/ubuntu/dirmngr@2.4.4-2ubuntu17.4
    ✘✔✔✘✘  pkg:deb/ubuntu/g%2B%2B@4%3A13.2.0-7ubuntu1
    ✘✔✔✘✘  pkg:deb/ubuntu/g%2B%2B-13@13.3.0-6ubuntu2~24.04.1
    ✘✔✔✘✘  pkg:deb/ubuntu/g%2B%2B-13-aarch64-linux-gnu@13.3.0-6ubuntu2~24.04.1
    ✘✔✔✘✘  pkg:deb/ubuntu/g%2B%2B-aarch64-linux-gnu@4%3A13.2.0-7ubuntu1
    ✘✔✔✘✘  pkg:deb/ubuntu/gcc@4%3A13.2.0-7ubuntu1
    ✔✔✔✘✘  pkg:deb/ubuntu/gcc-13@13.3.0-6ubuntu2~24.04.1
    ✘✔✔✘✘  pkg:deb/ubuntu/gcc-13-aarch64-linux-gnu@13.3.0-6ubuntu2~24.04.1
    ✘✔✔✘✘  pkg:deb/ubuntu/gcc-13-base@13.3.0-6ubuntu2~24.04.1
    ✘✔✔✘✘  pkg:deb/ubuntu/gcc-aarch64-linux-gnu@4%3A13.2.0-7ubuntu1
    ✘✔✔✘✘  pkg:deb/ubuntu/gnupg@2.4.4-2ubuntu17.4
    ✘✔✔✘✘  pkg:deb/ubuntu/gnupg-l10n@2.4.4-2ubuntu17.4
    ✘✔✔✘✘  pkg:deb/ubuntu/gnupg-utils@2.4.4-2ubuntu17.4
    ✘✔✔✘✘  pkg:deb/ubuntu/gpg@2.4.4-2ubuntu17.4
    ✘✔✔✘✘  pkg:deb/ubuntu/gpg-agent@2.4.4-2ubuntu17.4
    ✘✔✔✘✘  pkg:deb/ubuntu/gpg-wks-client@2.4.4-2ubuntu17.4
    ✘✔✔✘✘  pkg:deb/ubuntu/gpgconf@2.4.4-2ubuntu17.4
    ✘✔✔✘✔  pkg:deb/ubuntu/gpgsm@2.4.4-2ubuntu17.4
    ✘✔✔✘✘  pkg:deb/ubuntu/gpgv@2.4.4-2ubuntu17.4
    ✔✔✔✔✔  pkg:deb/ubuntu/gzip@1.12-1ubuntu3.1
    ✘✔✔✘✘  pkg:deb/ubuntu/keyboxd@2.4.4-2ubuntu17.4
    ✘✔✔✘✘  pkg:deb/ubuntu/krb5-locales@1.20.1-6ubuntu2.7
    ✘✔✔✘✘  pkg:deb/ubuntu/libacl1@2.3.2-1build1.1
    ✘✔✔✘✔  pkg:deb/ubuntu/libaom3@3.8.2-2ubuntu0.1
    ✘✔✔✘✔  pkg:deb/ubuntu/libattr1@1%3A2.5.2-1build1.1
    ✘✔✔✘✔  pkg:deb/ubuntu/libbinutils@2.42-4ubuntu2.10
    ✘✔✔✘✘  pkg:deb/ubuntu/libblkid1@2.39.3-9ubuntu6.5
    ✘✔✔✘✔  pkg:deb/ubuntu/libbrotli1@1.1.0-2build2
    ✘✔✔✘✘  pkg:deb/ubuntu/libbz2-1.0@1.0.8-5.1build0.1
    ✘✔✔✘✔  pkg:deb/ubuntu/libc-bin@2.39-0ubuntu8.8
    ✘✔✔✘✔  pkg:deb/ubuntu/libc-dev-bin@2.39-0ubuntu8.8
    ✘✔✔✘✔  pkg:deb/ubuntu/libc-devtools@2.39-0ubuntu8.8
    ✘✔✔✘✔  pkg:deb/ubuntu/libc6@2.39-0ubuntu8.8
    ✘✔✔✘✘  pkg:deb/ubuntu/libc6-dev@2.39-0ubuntu8.8
    ✘✔✔✘✔  pkg:deb/ubuntu/libctf-nobfd0@2.42-4ubuntu2.10
    ✘✔✔✘✔  pkg:deb/ubuntu/libctf0@2.42-4ubuntu2.10
    ✘✔✔✘✔  pkg:deb/ubuntu/libcurl4t64@8.5.0-2ubuntu10.11
    ✘✔✔✘✔  pkg:deb/ubuntu/libexpat1@2.6.1-2ubuntu0.4
    ✘✔✔✘✔  pkg:deb/ubuntu/libexpat1-dev@2.6.1-2ubuntu0.4
    ✘✔✔✘✔  pkg:deb/ubuntu/libfreetype6@2.13.2%2Bdfsg-1ubuntu0.1
    ✘✔✔✘✘  pkg:deb/ubuntu/libgcc-13-dev@13.3.0-6ubuntu2~24.04.1
    ✔✔✔✔✔  pkg:deb/ubuntu/libgcrypt20@1.10.3-2ubuntu0.1
    ✘✔✔✘✘  pkg:deb/ubuntu/libgd3@2.3.3-9ubuntu5
    ✘✔✔✘✔  pkg:deb/ubuntu/libgnutls30t64@3.8.3-1.1ubuntu3.6
    ✘✔✔✘✔  pkg:deb/ubuntu/libgprofng0@2.42-4ubuntu2.10
    ✘✔✔✘✘  pkg:deb/ubuntu/libgssapi-krb5-2@1.20.1-6ubuntu2.7
    ✘✔✔✘✔  pkg:deb/ubuntu/libheif-plugin-aomdec@1.17.6-1ubuntu4.6
    ✘✔✔✘✔  pkg:deb/ubuntu/libheif-plugin-aomenc@1.17.6-1ubuntu4.6
    ✘✔✔✘✔  pkg:deb/ubuntu/libheif1@1.17.6-1ubuntu4.6
    ✘✘✘✘✔  pkg:deb/ubuntu/libhwasan0@14.2.0-4ubuntu2~24.04.1
    ✘✔✔✘✘  pkg:deb/ubuntu/libjpeg-turbo8@2.1.5-2ubuntu2
    ✘✔✔✘✘  pkg:deb/ubuntu/libk5crypto3@1.20.1-6ubuntu2.7
    ✘✔✔✘✘  pkg:deb/ubuntu/libkrb5-3@1.20.1-6ubuntu2.7
    ✘✔✔✘✘  pkg:deb/ubuntu/libkrb5support0@1.20.1-6ubuntu2.7
    ✘✔✘✘✘  pkg:deb/ubuntu/liblz4-1@1.9.4-1build1.1
    ✘✔✘✘✘  pkg:deb/ubuntu/liblzma5@5.6.1%2Breally5.4.5-1ubuntu0.3
    ✘✔✔✘✘  pkg:deb/ubuntu/libmount1@2.39.3-9ubuntu6.5
    ✘✔✔✘✔  pkg:deb/ubuntu/libncursesw6@6.4%2B20240113-1ubuntu2
    ✘✔✔✘✔  pkg:deb/ubuntu/libp11-kit0@0.25.3-4ubuntu2.1
    ✘✔✔✘✔  pkg:deb/ubuntu/libpam-modules@1.5.3-5ubuntu5.5
    ✘✔✔✘✘  pkg:deb/ubuntu/libpam-modules-bin@1.5.3-5ubuntu5.5
    ✘✔✔✘✘  pkg:deb/ubuntu/libpam-runtime@1.5.3-5ubuntu5.5
    ✘✔✔✘✘  pkg:deb/ubuntu/libpam0g@1.5.3-5ubuntu5.5
    ✘✔✔✘✔  pkg:deb/ubuntu/libpcre2-8-0@10.42-4ubuntu2.1
    ✘✔✔✘✔  pkg:deb/ubuntu/libperl5.38t64@5.38.2-3.2ubuntu0.3
    ✘✔✔✘✔  pkg:deb/ubuntu/libpng16-16t64@1.6.43-5ubuntu0.6
    ✘✔✔✘✘  pkg:deb/ubuntu/libpython3.12-dev@3.12.3-1ubuntu0.15
    ✘✔✔✘✘  pkg:deb/ubuntu/libpython3.12-minimal@3.12.3-1ubuntu0.15
    ✘✔✔✘✘  pkg:deb/ubuntu/libpython3.12-stdlib@3.12.3-1ubuntu0.15
    ✘✔✔✘✔  pkg:deb/ubuntu/libpython3.12t64@3.12.3-1ubuntu0.15
    ✘✔✔✘✘  pkg:deb/ubuntu/librtmp1@2.4%2B20151223.gitfa8646d.1-2build7
    ✘✔✔✘✔  pkg:deb/ubuntu/libsasl2-2@2.1.28%2Bdfsg1-5ubuntu3.1
    ✘✔✔✘✔  pkg:deb/ubuntu/libsasl2-modules@2.1.28%2Bdfsg1-5ubuntu3.1
    ✘✔✔✘✔  pkg:deb/ubuntu/libsasl2-modules-db@2.1.28%2Bdfsg1-5ubuntu3.1
    ✘✔✔✘✔  pkg:deb/ubuntu/libsframe1@2.42-4ubuntu2.10
    ✘✔✔✘✘  pkg:deb/ubuntu/libsmartcols1@2.39.3-9ubuntu6.5
    ✘✔✔✘✔  pkg:deb/ubuntu/libsqlite3-0@3.45.1-1ubuntu2.7
    ✘✔✔✘✔  pkg:deb/ubuntu/libssh-4@0.10.6-2ubuntu0.4
    ✘✔✔✘✔  pkg:deb/ubuntu/libssl3t64@3.0.13-0ubuntu3.12
    ✘✔✔✘✘  pkg:deb/ubuntu/libstdc%2B%2B-13-dev@13.3.0-6ubuntu2~24.04.1
    ✘✔✔✘✔  pkg:deb/ubuntu/libsystemd0@255.4-1ubuntu8.16
    ✘✔✔✘✘  pkg:deb/ubuntu/libtiff6@4.5.1%2Bgit230720-4ubuntu2.5
    ✘✔✔✘✔  pkg:deb/ubuntu/libtinfo6@6.4%2B20240113-1ubuntu2
    ✘✔✔✘✔  pkg:deb/ubuntu/libudev1@255.4-1ubuntu8.16
    ✘✔✔✘✘  pkg:deb/ubuntu/libuuid1@2.39.3-9ubuntu6.5
    ✘✔✔✘✔  pkg:deb/ubuntu/libx11-6@2%3A1.8.7-1build1
    ✘✔✔✘✘  pkg:deb/ubuntu/libx11-data@2%3A1.8.7-1build1
    ✘✔✔✘✔  pkg:deb/ubuntu/libxpm4@1%3A3.5.17-1ubuntu0.24.04.1
    ✘✔✘✘✘  pkg:deb/ubuntu/linux-libc-dev@6.8.0-136.136
    ✘✔✔✘✔  pkg:deb/ubuntu/login@1%3A4.13%2Bdfsg1-4ubuntu3.2
    ✘✔✔✘✘  pkg:deb/ubuntu/mount@2.39.3-9ubuntu6.5
    ✘✔✔✘✔  pkg:deb/ubuntu/ncurses-base@6.4%2B20240113-1ubuntu2
    ✘✔✔✘✔  pkg:deb/ubuntu/ncurses-bin@6.4%2B20240113-1ubuntu2
    ✔✔✔✔✔  pkg:deb/ubuntu/openssl@3.0.13-0ubuntu3.12
    ✘✔✔✘✔  pkg:deb/ubuntu/passwd@1%3A4.13%2Bdfsg1-4ubuntu3.2
    ✔✔✔✔✔  pkg:deb/ubuntu/patch@2.7.6-7build3
    ✔✔✔✔✔  pkg:deb/ubuntu/perl@5.38.2-3.2ubuntu0.3
    ✘✔✔✘✔  pkg:deb/ubuntu/perl-base@5.38.2-3.2ubuntu0.3
    ✘✔✔✘✔  pkg:deb/ubuntu/perl-modules-5.38@5.38.2-3.2ubuntu0.3
    ✘✔✔✘✔  pkg:deb/ubuntu/python3-pip@24.0%2Bdfsg-1ubuntu1.3
    ✘✔✔✘✘  pkg:deb/ubuntu/python3-pkg-resources@68.1.2-2ubuntu1.2
    ✘✔✔✘✘  pkg:deb/ubuntu/python3-setuptools@68.1.2-2ubuntu1.2
    ✘✔✔✘✔  pkg:deb/ubuntu/python3-wheel@0.42.0-2
    ✔✔✔✔✔  pkg:deb/ubuntu/python3.12@3.12.3-1ubuntu0.15
    ✘✔✔✘✘  pkg:deb/ubuntu/python3.12-dev@3.12.3-1ubuntu0.15
    ✘✔✔✘✘  pkg:deb/ubuntu/python3.12-minimal@3.12.3-1ubuntu0.15
    ✔✔✔✔✔  pkg:deb/ubuntu/tar@1.35%2Bdfsg-3build1
    ✔✔✔✔✔  pkg:deb/ubuntu/util-linux@2.39.3-9ubuntu6.5
    ✔✔✘✘✘  pkg:deb/ubuntu/xz-utils@5.6.1%2Breally5.4.5-1ubuntu0.3
    ✘✔✔✘✔  pkg:deb/ubuntu/zlib1g@1%3A1.3.dfsg-3.1ubuntu2.1
    ✘✔✔✘✔  pkg:deb/ubuntu/zlib1g-dev@1%3A1.3.dfsg-3.1ubuntu2.1

  ▸ Go (28 packages)
    ✔✔✔✔✔  pkg:golang/github.com/containerd/containerd/v2@v2.2.5
    ✔✔✔✔✔  pkg:golang/github.com/containerd/containerd/v2@v2.3.3
    ✘✘✘✘✔  pkg:golang/github.com/docker/buildx@v0.35.0
    ✘✘✘✘✔  pkg:golang/github.com/docker/buildx@v0.36.0
    ✔✔✔✔✔  pkg:golang/github.com/docker/docker@v28.5.2%2Bincompatible
    ✘✘✘✘✔  pkg:golang/github.com/go-openapi/swag/jsonutils@v0.26.1
    ✘✘✘✘✔  pkg:golang/github.com/go-openapi/swag/yamlutils@v0.26.1
    ✔✔✔✔✔  pkg:golang/github.com/klauspost/compress@v1.18.6
    ✘✘✘✘✔  pkg:golang/github.com/moby/buildkit@v0.31.1
    ✘✘✘✘✔  pkg:golang/github.com/moby/buildkit@v0.32.0
    ✔✔✔✔✔  pkg:golang/github.com/moby/go-archive@v0.2.0
    ✔✔✔✔✔  pkg:golang/github.com/moby/go-archive@v0.2.1
    ✘✘✘✘✔  pkg:golang/github.com/pelletier/go-toml/v2@v2.3.1
    ✔✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace@v1.44.0
    ✔✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc@v1.44.0
    ✔✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp@v1.44.0
    ✔✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/sdk@v1.44.0
    ✔✔✔✔✔  pkg:golang/golang.org/x/crypto@v0.53.0
    ✔✔✔✔✔  pkg:golang/golang.org/x/crypto@v0.54.0
    ✔✔✔✔✔  pkg:golang/golang.org/x/mod@v0.38.0
    ✔✔✔✔✔  pkg:golang/golang.org/x/net@v0.56.0
    ✔✔✔✔✔  pkg:golang/golang.org/x/net@v0.57.0
    ✔✔✔✔✔  pkg:golang/golang.org/x/text@v0.38.0
    ✔✔✔✔✔  pkg:golang/golang.org/x/text@v0.40.0
    ✔✔✔✔✔  pkg:golang/google.golang.org/grpc@v1.81.1
    ✔✔✔✔✔  pkg:golang/google.golang.org/grpc@v1.82.1
    ✔✔✔✔✔  pkg:golang/stdlib@1.26.4
    ✔✔✔✔✔  pkg:golang/stdlib@1.26.5

## VULNERABILITY DETAIL — All Scanner Findings

  Every vulnerability found, and which scanners agree on it.
  CVSS, EPSS and KEV come from Vulners where it knows the CVE, otherwise from the scanner that reported it.
  Vulners CVE data: 5046 of 5046 CVEs known, CVSS+EPSS on 5036 (99.8%).
  OSV Src OSV Grype Trivy Vulners   SEVERITY   CVSS   EPSS  KEV   ↳ provenance
  ━━ Python (PyPI) ━━
  ┌─ pkg:pypi/aiohttp@3.9.1
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-34520         CRITICAL     9.1   0.5%   ·  ↳ O:GHSA-63hf-3vf5-4wqf,PYSEC-2026-2102 | S:GHSA-63hf-3vf5-4wqf,PYSEC-2026-2102 | V:SNYK:PYTHON-AIOHTTP-15873704
  │ ✘✘✘✘✔ CVE-2023-47627         HIGH         7.5   0.9%   ·  ↳ V:OSV:PYSEC-2024-26
  │ ✔✔✔✔✔ CVE-2024-23334         HIGH         7.5  76.9% KEV  ↳ O:GHSA-5h86-8mv2-jq9f,PYSEC-2024-24 | S:GHSA-5h86-8mv2-jq9f,PYSEC-2024-24 | V:GHSA-5H86-8MV2-JQ9F
  │ ✔✔✔✔✔ CVE-2024-30251         HIGH         7.5   1.1%   ·  ↳ O:GHSA-5m98-qgg9-wh84,PYSEC-2026-1098 | S:GHSA-5m98-qgg9-wh84,PYSEC-2026-1098 | V:GHSA-5M98-QGG9-WH84
  │ ✔✔✔✔✔ CVE-2024-52304         HIGH         7.5   0.6%   ·  ↳ O:GHSA-8495-4g3g-x7pr,PYSEC-2026-1103 | S:GHSA-8495-4g3g-x7pr,PYSEC-2026-1103 | V:SNYK:PYTHON-AIOHTTP-8383923
  │ ✔✔✔✔✔ CVE-2025-53643         HIGH         7.5   0.4%   ·  ↳ O:GHSA-9548-qrrj-x5pj,PYSEC-2026-1104 | S:GHSA-9548-qrrj-x5pj,PYSEC-2026-1104 | V:GHSA-9548-QRRJ-X5PJ
  │ ✔✔✔✔✔ CVE-2025-69223         HIGH         7.5   0.6%   ·  ↳ O:GHSA-6mq8-rvhq-8wgg,PYSEC-2026-1101 | S:GHSA-6mq8-rvhq-8wgg,PYSEC-2026-1101 | V:SNYK:PYTHON-AIOHTTP-14871876
  │ ✔✔✔✔✔ CVE-2025-69227         HIGH         8.7   0.4%   ·  ↳ O:GHSA-jj3x-wxrx-4x23,PYSEC-2026-1107 | S:GHSA-jj3x-wxrx-4x23,PYSEC-2026-1107 | V:SNYK:PYTHON-AIOHTTP-14871979
  │ ✔✔✔✔✔ CVE-2025-69228         HIGH         8.7   0.4%   ·  ↳ O:GHSA-6jhg-hg63-jvvf,PYSEC-2026-1100 | S:GHSA-6jhg-hg63-jvvf,PYSEC-2026-1100 | V:SNYK:PYTHON-AIOHTTP-14871877
  │ ✔✔✔✔✔ CVE-2025-69229         HIGH         8.7   0.4%   ·  ↳ O:GHSA-g84x-mcqj-x9qq,PYSEC-2026-1106 | S:GHSA-g84x-mcqj-x9qq,PYSEC-2026-1106 | V:SNYK:PYTHON-AIOHTTP-14871954
  │ ✔✔✔✔✔ CVE-2026-111064        HIGH         8.2   0.4%   ·  ↳ O:GHSA-5wr8-gcqf-gqf3 | S:GHSA-5wr8-gcqf-gqf3 | V:SNYK:PYTHON-AIOHTTP-21248799
  │ ✔✔✔✔✔ CVE-2026-111066        HIGH         8.2   0.4%   ·  ↳ O:GHSA-9xw5-w5jj-pvcg | S:GHSA-9xw5-w5jj-pvcg | V:MEND:CVE-2026-111066
  │ ✔✔✔✔✔ CVE-2026-22815         HIGH         7.5   0.5%   ·  ↳ O:GHSA-w2fm-2cpv-w7v5,PYSEC-2026-2094 | S:GHSA-w2fm-2cpv-w7v5,PYSEC-2026-2094 | V:SNYK:PYTHON-AIOHTTP-15873739
  │ ✔✔✔✔✔ CVE-2026-34513         HIGH         7.5   0.5%   ·  ↳ O:GHSA-hcc4-c3v8-rx92,PYSEC-2026-2095 | S:GHSA-hcc4-c3v8-rx92,PYSEC-2026-2095 | V:SNYK:PYTHON-AIOHTTP-15873737
  │ ✔✔✔✔✔ CVE-2026-34515         HIGH         8.7   0.4%   ·  ↳ O:GHSA-p998-jp59-783m,PYSEC-2026-2097 | S:GHSA-p998-jp59-783m,PYSEC-2026-2097 | V:SNYK:PYTHON-AIOHTTP-15873738
  │ ✔✔✔✔✔ CVE-2026-34516         HIGH         8.7   0.5%   ·  ↳ O:GHSA-m5qp-6w8w-w647,PYSEC-2026-2098 | S:GHSA-m5qp-6w8w-w647,PYSEC-2026-2098 | V:SNYK:PYTHON-AIOHTTP-15873732
  │ ✔✔✔✔✔ CVE-2026-34993         HIGH         7.3   0.2%   ·  ↳ O:GHSA-jg22-mg44-37j8,PYSEC-2026-2104 | S:GHSA-jg22-mg44-37j8,PYSEC-2026-2104 | V:GHSA-JG22-MG44-37J8
  │ ✔✔✔✔✔ CVE-2026-47265         HIGH         8.7   0.1%   ·  ↳ O:GHSA-hg6j-4rv6-33pg,PYSEC-2026-2105 | S:GHSA-hg6j-4rv6-33pg,PYSEC-2026-2105 | V:GHSA-HG6J-4RV6-33PG
  │ ✔✔✔✔✔ CVE-2026-50269         HIGH         7.5   0.5%   ·  ↳ O:GHSA-m6qw-4cw2-hm4m,PYSEC-2026-2106 | S:GHSA-m6qw-4cw2-hm4m,PYSEC-2026-2106 | V:SNYK:PYTHON-AIOHTTP-17342380
  │ ✔✔✔✔✔ CVE-2026-54273         HIGH         8.7   0.5%   ·  ↳ O:GHSA-4fvr-rgm6-gqmc,PYSEC-2026-2107 | S:GHSA-4fvr-rgm6-gqmc,PYSEC-2026-2107 | V:SNYK:PYTHON-AIOHTTP-17342416
  │ ✔✔✔✔✔ CVE-2026-54274         HIGH         8.7   0.5%   ·  ↳ O:GHSA-xcgm-r5h9-7989,PYSEC-2026-2108 | S:GHSA-xcgm-r5h9-7989,PYSEC-2026-2108 | V:SNYK:PYTHON-AIOHTTP-17342364
  │ ✔✔✔✔✔ CVE-2026-54275         HIGH         7.5   0.5%   ·  ↳ O:GHSA-4m7w-qmgq-4wj5,PYSEC-2026-237 | S:GHSA-4m7w-qmgq-4wj5,PYSEC-2026-237 | V:SNYK:PYTHON-AIOHTTP-17342400
  │ ✔✔✔✔✔ CVE-2026-54277         HIGH         8.7   0.6%   ·  ↳ O:GHSA-63hw-fmq6-xxg2,PYSEC-2026-2110 | S:GHSA-63hw-fmq6-xxg2,PYSEC-2026-2110 | V:SNYK:PYTHON-AIOHTTP-17342401
  │ ✔✔✔✔✔ CVE-2026-54278         HIGH         8.7   0.5%   ·  ↳ O:GHSA-g3cq-j2xw-wf74,PYSEC-2026-2111 | S:GHSA-g3cq-j2xw-wf74,PYSEC-2026-2111 | V:SNYK:PYTHON-AIOHTTP-17342413
  │ ✔✔✔✔✔ CVE-2026-54279         HIGH         7.5   0.5%   ·  ↳ O:GHSA-2fqr-mr3j-6wp8,PYSEC-2026-2112 | S:GHSA-2fqr-mr3j-6wp8,PYSEC-2026-2112 | V:SNYK:PYTHON-AIOHTTP-17342393
  │ ✔✔✔✔✔ CVE-2026-54280         HIGH         7.5   0.5%   ·  ↳ O:GHSA-9x8q-7h8h-wcw9,PYSEC-2026-2113 | S:GHSA-9x8q-7h8h-wcw9,PYSEC-2026-2113 | V:SNYK:PYTHON-AIOHTTP-17342415
  │ ✔✔✔✔✔ CVE-2026-69244         HIGH         7.1   0.5%   ·  ↳ O:GHSA-cq5v-8q36-5273,PYSEC-2026-3545 | S:GHSA-cq5v-8q36-5273,PYSEC-2026-3545 | V:SNYK:PYTHON-AIOHTTP-18517003
  │ ✔✔✔✔✔ CVE-2024-23829         MEDIUM       6.5   1.0%   ·  ↳ O:GHSA-8qpw-xqxj-h4r2,PYSEC-2024-26 | S:GHSA-8qpw-xqxj-h4r2,PYSEC-2024-26 | V:OSV:PYSEC-2024-26
  │ ✔✔✔✔✔ CVE-2024-27306         MEDIUM       6.1   0.7%   ·  ↳ O:GHSA-7gpw-8wmc-pm8g,PYSEC-2026-1102 | S:GHSA-7gpw-8wmc-pm8g,PYSEC-2026-1102 | V:GHSA-7GPW-8WMC-PM8G
  │ ✔✔✔✔✔ CVE-2025-69224         MEDIUM       6.5   0.2%   ·  ↳ O:GHSA-69f9-5gxw-wvc2,PYSEC-2026-1099 | S:GHSA-69f9-5gxw-wvc2,PYSEC-2026-1099 | V:SNYK:PYTHON-AIOHTTP-14871873
  │ ✔✔✔✔✔ CVE-2025-69225         MEDIUM       6.9   0.3%   ·  ↳ O:GHSA-mqqc-3gqh-h2x8,PYSEC-2026-1109 | S:GHSA-mqqc-3gqh-h2x8,PYSEC-2026-1109 | V:SNYK:PYTHON-AIOHTTP-14871929
  │ ✔✔✔✔✔ CVE-2025-69226         MEDIUM       6.3   0.4%   ·  ↳ O:GHSA-54jq-c3m8-4m76,PYSEC-2026-1097 | S:GHSA-54jq-c3m8-4m76,PYSEC-2026-1097 | V:SNYK:PYTHON-AIOHTTP-14871888
  │ ✔✔✔✔✔ CVE-2025-69230         MEDIUM       6.9   0.4%   ·  ↳ O:GHSA-fh55-r93g-j68g,PYSEC-2026-1105 | S:GHSA-fh55-r93g-j68g,PYSEC-2026-1105 | V:SNYK:PYTHON-AIOHTTP-14872000
  │ ✔✔✔✔✔ CVE-2026-111063        MEDIUM       6.3   0.2%   ·  ↳ O:GHSA-494j-54xm-rwp3 | S:GHSA-494j-54xm-rwp3 | V:SNYK:PYTHON-AIOHTTP-21248800
  │ ✔✔✔✔✔ CVE-2026-111065        MEDIUM       6.9   0.4%   ·  ↳ O:GHSA-6cjc-53gc-5rqm | S:GHSA-6cjc-53gc-5rqm | V:MEND:CVE-2026-111065
  │ ✔✔✔✔✔ CVE-2026-111748        MEDIUM       6.3   0.4%   ·  ↳ O:GHSA-f9xw-jh8m-3mwq | S:GHSA-f9xw-jh8m-3mwq | V:MEND:CVE-2026-111748
  │ ✔✔✔✔✔ CVE-2026-111750        MEDIUM       6.3   0.4%   ·  ↳ O:GHSA-pqxq-w44r-73xw | S:GHSA-pqxq-w44r-73xw | V:MEND:CVE-2026-111750
  │ ✔✔✔✔✔ CVE-2026-34514         MEDIUM       6.9   0.3%   ·  ↳ O:GHSA-2vrm-gr82-f7m5,PYSEC-2026-2096 | S:GHSA-2vrm-gr82-f7m5,PYSEC-2026-2096 | V:SNYK:PYTHON-AIOHTTP-15873736
  │ ✔✔✔✔✔ CVE-2026-34517         MEDIUM       6.9   0.4%   ·  ↳ O:GHSA-3wq7-rqq7-wx6j,PYSEC-2026-2099 | S:GHSA-3wq7-rqq7-wx6j,PYSEC-2026-2099 | V:SNYK:PYTHON-AIOHTTP-15873734
  │ ✔✔✔✔✔ CVE-2026-34518         MEDIUM       6.9   0.4%   ·  ↳ O:GHSA-966j-vmvw-g2g9,PYSEC-2026-2100 | S:GHSA-966j-vmvw-g2g9,PYSEC-2026-2100 | V:SNYK:PYTHON-AIOHTTP-15873735
  │ ✔✔✔✔✔ CVE-2026-34519         MEDIUM       6.9   0.3%   ·  ↳ O:GHSA-mwh4-6h8g-pg8w,PYSEC-2026-2101 | S:GHSA-mwh4-6h8g-pg8w,PYSEC-2026-2101 | V:SNYK:PYTHON-AIOHTTP-15873731
  │ ✔✔✔✔✔ CVE-2026-34525         MEDIUM       6.3   0.3%   ·  ↳ O:GHSA-c427-h43c-vf67,PYSEC-2026-2103 | S:GHSA-c427-h43c-vf67,PYSEC-2026-2103 | V:SNYK:PYTHON-AIOHTTP-15873733
  │ ✔✔✔✔✔ CVE-2026-54276         MEDIUM       6.3   0.3%   ·  ↳ O:GHSA-hpj7-wq8m-9hgp,PYSEC-2026-2109 | S:GHSA-hpj7-wq8m-9hgp,PYSEC-2026-2109 | V:SNYK:PYTHON-AIOHTTP-17342365
  │ ✔✔✔✔✔ CVE-2026-59881         MEDIUM       6.9   0.5%   ·  ↳ O:GHSA-mq44-7p77-q5h7,PYSEC-2026-3547 | S:GHSA-mq44-7p77-q5h7,PYSEC-2026-3547 | V:SNYK:PYTHON-AIOHTTP-18517004
  │ ✔✔✔✔✔ CVE-2026-69243         MEDIUM       6.3   0.4%   ·  ↳ O:GHSA-mfx4-hv73-q22v,PYSEC-2026-3546 | S:GHSA-mfx4-hv73-q22v,PYSEC-2026-3546 | V:SNYK:PYTHON-AIOHTTP-18517005
  │ ✔✔✔✔✔ CVE-2026-111749        LOW          2.3   0.4%   ·  ↳ O:GHSA-gx76-c99x-2c96 | S:GHSA-gx76-c99x-2c96 | V:MEND:CVE-2026-111749
  │ ✔✔✔✔✔ GHSA-2G87-PP6C-29X5    HIGH         8.7      -   ·
  │ ✘✘✘✘✔ PYTHON-AIOHTTP-21248798 HIGH         8.7      -   ·  ↳ V:SNYK:PYTHON-AIOHTTP-21248798
  │ ✘✘✘✘✔ WS-2026-0114           MEDIUM       6.3      -   ·  ↳ V:MEND:WS-2026-0114
  │ ✘✘✘✘✔ WS-2026-0116           MEDIUM       6.3      -   ·  ↳ V:MEND:WS-2026-0116
  │ ✘✘✘✘✔ WS-2026-0119           MEDIUM       6.3      -   ·  ↳ V:MEND:WS-2026-0119
  │ ✘✘✘✘✔ WS-2026-0120           MEDIUM       6.9      -   ·  ↳ V:MEND:WS-2026-0120
  │ ✘✘✘✘✔ WS-2026-0121           MEDIUM       6.9      -   ·  ↳ V:MEND:WS-2026-0121
  │ ✘✘✘✘✔ WS-2026-0115           LOW          3.1      -   ·  ↳ V:MEND:WS-2026-0115
  │ ✘✘✘✘✔ WS-2026-0117           LOW          3.1      -   ·  ↳ V:MEND:WS-2026-0117
  │ ✘✘✘✘✔ WS-2026-0118           LOW          3.1      -   ·  ↳ V:MEND:WS-2026-0118
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/certifi@2026.7.22
  │ OSGTV
  │ ✔✔✔✔✔ GHSA-6Q48-6C7W-9GW2    CRITICAL     9.1      -   ·  ↳ O:PYSEC-2026-4320 | S:PYSEC-2026-4320 | V:OSV:GHSA-6Q48-6C7W-9GW2,OSV:PYSEC-2026-4320,PYSEC-2026-4320
  │ ✘✘✘✘✔ PYTHON-CERTIFI-21280764 CRITICAL     9.1      -   ·  ↳ V:SNYK:PYTHON-CERTIFI-21280764
  │ ✘✘✘✘✔ WS-2026-0133           CRITICAL     9.1      -   ·  ↳ V:MEND:WS-2026-0133
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/cryptography@3.3.2
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2023-0286          HIGH         7.4  69.3%   ·  ↳ O:GHSA-x4qr-2fvf-3mr5,PYSEC-2026-800 | S:GHSA-x4qr-2fvf-3mr5,PYSEC-2026-800 | V:GHSA-X4QR-2FVF-3MR5
  │ ✔✔✔✔✔ CVE-2023-49083         HIGH         7.5   1.0%   ·  ↳ O:GHSA-jfhm-5ghh-2f97,PYSEC-2023-254 | S:GHSA-jfhm-5ghh-2f97,PYSEC-2023-254 | V:GHSA-JFHM-5GHH-2F97
  │ ✔✔✔✔✔ CVE-2023-50782         HIGH         7.5   1.1%   ·  ↳ O:GHSA-3ww4-gg4f-jr7f,PYSEC-2026-1283 | S:GHSA-3ww4-gg4f-jr7f,PYSEC-2026-1283 | V:MEND:CVE-2023-50782
  │ ✔✔✔✔✔ CVE-2026-26007         HIGH         8.2   0.4%   ·  ↳ O:GHSA-r6ph-v2qm-q3c2,PYSEC-2026-2141 | S:GHSA-r6ph-v2qm-q3c2,PYSEC-2026-2141 | V:MEND:CVE-2026-26007
  │ ✘✘✘✘✔ CVE-2026-34180         HIGH         7.5   1.0%   ·  ↳ V:SNYK:PYTHON-CRYPTOGRAPHY-17344551
  │ ✔✔✘✘✔ CVE-2026-69248         HIGH         8.3   0.2%   ·  ↳ O:PYSEC-2026-3554 | S:PYSEC-2026-3554 | V:OSV:PYSEC-2026-3554
  │ ✔✔✘✘✔ CVE-2026-69249         HIGH         8.7   0.3%   ·  ↳ O:PYSEC-2026-3553 | S:PYSEC-2026-3553 | V:OSV:PYSEC-2026-3553
  │ ✔✔✔✔✔ CVE-2023-23931         MEDIUM       6.5   1.3%   ·  ↳ O:GHSA-w7pp-m8wf-vj6r,PYSEC-2023-11 | S:GHSA-w7pp-m8wf-vj6r,PYSEC-2023-11 | V:GHSA-W7PP-M8WF-VJ6R
  │ ✔✔✔✔✔ CVE-2024-0727          MEDIUM       5.5   3.2%   ·  ↳ O:GHSA-9v9h-cgj8-h64p,PYSEC-2026-1285 | S:GHSA-9v9h-cgj8-h64p,PYSEC-2026-1285 | V:MEND:CVE-2024-0727
  │ ✔✔✔✔✔ CVE-2026-34073         MEDIUM       6.3   0.2%   ·  ↳ O:GHSA-m959-cc7f-wv43,PYSEC-2026-35 | S:GHSA-m959-cc7f-wv43,PYSEC-2026-35 | V:MEND:CVE-2026-34073
  │ ✔✔✔✔✔ GHSA-537C-GMF6-5CCF    HIGH         7.5      -   ·
  │ ✔✔✔✔✔ GHSA-5CPQ-8WJ7-HF2V    LOW          0.0      -   ·  ↳ V:OSV:GHSA-5CPQ-8WJ7-HF2V
  │ ✔✔✔✔✔ GHSA-JM77-QPHF-C4W8    LOW          0.0      -   ·
  │ ✔✔✔✔✔ GHSA-V8GR-M533-GHJ9    LOW          0.0      -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/flask@3.0.2
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-27205         MEDIUM       4.3   0.4%   ·  ↳ O:GHSA-68rp-wp8r-4726,PYSEC-2026-2151 | S:GHSA-68rp-wp8r-4726,PYSEC-2026-2151 | V:GHSA-68RP-WP8R-4726
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/idna@2.7
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2024-3651          HIGH         7.5   1.4%   ·  ↳ O:GHSA-jjg7-2v4v-x38h,PYSEC-2024-60 | S:GHSA-jjg7-2v4v-x38h,PYSEC-2024-60 | V:MEND:CVE-2024-3651
  │ ✔✔✔✔✔ CVE-2026-45409         MEDIUM       6.9   0.4%   ·  ↳ O:GHSA-65pc-fj4g-8rjx,PYSEC-2026-215 | S:GHSA-65pc-fj4g-8rjx,PYSEC-2026-215 | V:MEND:CVE-2026-45409
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/multidict@6.7.1
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-104874        MEDIUM       5.3   0.4%   ·  ↳ O:GHSA-54p9-h82j-f925,PYSEC-2026-4244 | S:GHSA-54p9-h82j-f925,PYSEC-2026-4244 | V:OSV:PYSEC-2026-4244
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/pip@24.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-8643          HIGH         8.0   0.3%   ·  ↳ O:GHSA-wf93-45jw-7689,PYSEC-2026-196 | S:GHSA-wf93-45jw-7689,PYSEC-2026-196 | V:MEND:CVE-2026-8643
  │ ✔✔✔✔✔ CVE-2025-8869          MEDIUM       5.9   0.5%   ·  ↳ O:GHSA-4xh5-x5gv-qwph,PYSEC-2026-1795 | S:GHSA-4xh5-x5gv-qwph,PYSEC-2026-1795 | V:MEND:CVE-2025-8869
  │ ✔✔✔✔✔ CVE-2026-13346         MEDIUM       6.5   0.3%   ·  ↳ O:GHSA-qwm4-qh6w-59xr,PYSEC-2026-3721 | S:GHSA-qwm4-qh6w-59xr,PYSEC-2026-3721 | V:MEND:CVE-2026-13346
  │ ✔✔✔✔✔ CVE-2026-3219          MEDIUM       4.6   0.1%   ·  ↳ O:GHSA-58qw-9mgm-455v,PYSEC-2026-2875 | S:GHSA-58qw-9mgm-455v,PYSEC-2026-2875 | V:MEND:CVE-2026-3219
  │ ✔✔✔✔✔ CVE-2026-6357          MEDIUM       5.3   0.1%   ·  ↳ O:GHSA-jp4c-xjxw-mgf9,PYSEC-2026-2876 | S:GHSA-jp4c-xjxw-mgf9,PYSEC-2026-2876 | V:SNYK:PYTHON-PIP-16316401
  │ ✔✔✔✔✔ CVE-2026-1703          LOW          2.0   0.4%   ·  ↳ O:GHSA-6vgw-5pg2-w6jp,PYSEC-2026-1796 | S:GHSA-6vgw-5pg2-w6jp,PYSEC-2026-1796 | V:MEND:CVE-2026-1703
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/requests@2.19.1
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2018-18074         HIGH         7.5   6.9%   ·  ↳ O:GHSA-x84v-xcm2-53pg,PYSEC-2018-28 | S:GHSA-x84v-xcm2-53pg,PYSEC-2018-28 | V:OSV:PYSEC-2018-28
  │ ✔✔✔✔✔ CVE-2023-32681         MEDIUM       6.1   3.0%   ·  ↳ O:GHSA-j8r2-6x86-q33q,PYSEC-2023-74 | S:GHSA-j8r2-6x86-q33q,PYSEC-2023-74 | V:GHSA-J8R2-6X86-Q33Q
  │ ✔✔✔✔✔ CVE-2024-35195         MEDIUM       5.6   0.3%   ·  ↳ O:GHSA-9wx4-h78v-vm56,PYSEC-2026-1873 | S:GHSA-9wx4-h78v-vm56,PYSEC-2026-1873 | V:GHSA-9WX4-H78V-VM56
  │ ✔✔✔✔✔ CVE-2024-47081         MEDIUM       5.3   1.0%   ·  ↳ O:GHSA-9hjg-9r4m-mvj7,PYSEC-2026-1872 | S:GHSA-9hjg-9r4m-mvj7,PYSEC-2026-1872 | V:MEND:CVE-2024-47081
  │ ✔✔✔✔✔ CVE-2026-25645         MEDIUM       5.5   0.2%   ·  ↳ O:GHSA-gc5v-m9x4-r6x2,PYSEC-2026-2275 | S:GHSA-gc5v-m9x4-r6x2,PYSEC-2026-2275 | V:GHSA-GC5V-M9X4-R6X2
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/setuptools@68.1.2
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2024-6345          HIGH         8.8   1.9%   ·  ↳ O:GHSA-cx63-2mw6-8hw5,PYSEC-2026-1918 | S:GHSA-cx63-2mw6-8hw5,PYSEC-2026-1918 | V:MEND:CVE-2024-6345
  │ ✔✔✔✔✔ CVE-2025-47273         HIGH         8.8   1.6%   ·  ↳ O:GHSA-5rjg-fvgr-3xxf,PYSEC-2025-49 | S:GHSA-5rjg-fvgr-3xxf,PYSEC-2025-49 | V:MEND:CVE-2025-47273
  │ ✔✔✔✔✔ CVE-2026-59890         MEDIUM       6.1   0.4%   ·  ↳ O:GHSA-h35f-9h28-mq5c,PYSEC-2026-3447 | S:GHSA-h35f-9h28-mq5c,PYSEC-2026-3447 | V:MEND:CVE-2026-59890
  │ ✔✔✔✔✔ GHSA-XMJ3-9GF7-H52W    LOW          1.0      -   ·  ↳ V:OSV:GHSA-XMJ3-9GF7-H52W
  │ ✘✘✘✘✔ PYTHON-SETUPTOOLS-21689156 LOW          3.3      -   ·  ↳ V:SNYK:PYTHON-SETUPTOOLS-21689156
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/urllib3@1.23
  │ OSGTV
  │ ✘✘✘✘✔ CVE-2018-20060         CRITICAL     9.8   4.5%   ·  ↳ V:OSV:PYSEC-2023-207
  │ ✔✔✔✔✔ CVE-2019-11324         HIGH         7.5   2.9%   ·  ↳ O:GHSA-mh33-7rrq-662w,PYSEC-2019-133 | S:GHSA-mh33-7rrq-662w,PYSEC-2019-133 | V:GHSA-MH33-7RRQ-662W
  │ ✘✘✘✘✔ CVE-2020-26116         HIGH         7.2   6.4%   ·  ↳ V:OSV:PYSEC-2020-148
  │ ✔✔✔✔✔ CVE-2023-43804         HIGH         8.1   1.4%   ·  ↳ O:GHSA-v845-jxx5-vc9f,PYSEC-2023-192 | S:GHSA-v845-jxx5-vc9f,PYSEC-2023-192 | V:GHSA-V845-JXX5-VC9F
  │ ✔✔✔✔✔ CVE-2025-66471         HIGH         8.9   0.7%   ·  ↳ O:GHSA-2xpw-w6gg-jr37,PYSEC-2026-1994 | S:GHSA-2xpw-w6gg-jr37,PYSEC-2026-1994 | V:MEND:CVE-2025-66471
  │ ✔✔✔✔✔ CVE-2026-21441         HIGH         8.9   2.9%   ·  ↳ O:GHSA-38jv-5279-wg99,PYSEC-2026-1996 | S:GHSA-38jv-5279-wg99,PYSEC-2026-1996 | V:MEND:CVE-2026-21441
  │ ✔✔✔✔✔ CVE-2026-44431         HIGH         8.2   0.3%   ·  ↳ O:GHSA-qccp-gfcp-xxvc,PYSEC-2026-141 | S:GHSA-qccp-gfcp-xxvc,PYSEC-2026-141 | V:MEND:CVE-2026-44431
  │ ✔✔✔✔✔ CVE-2026-97689         HIGH         8.9   0.3%   ·  ↳ O:GHSA-vxq7-64xx-v4gw,PYSEC-2026-4177 | S:GHSA-vxq7-64xx-v4gw,PYSEC-2026-4177 | V:MEND:CVE-2026-97689
  │ ✔✔✔✔✔ CVE-2018-25091         MEDIUM       6.1   0.6%   ·  ↳ O:GHSA-gwvm-45gx-3cf8,PYSEC-2023-207 | S:GHSA-gwvm-45gx-3cf8,PYSEC-2023-207 | V:OSV:PYSEC-2023-207
  │ ✔✔✔✔✔ CVE-2019-11236         MEDIUM       6.1   2.1%   ·  ↳ O:GHSA-r64q-w8jr-g9qp,PYSEC-2019-132 | S:GHSA-r64q-w8jr-g9qp,PYSEC-2019-132 | V:OSV:PYSEC-2019-132
  │ ✔✔✔✔✔ CVE-2020-26137         MEDIUM       6.5   2.3%   ·  ↳ O:GHSA-wqvq-5m8c-6g24,PYSEC-2020-148 | S:GHSA-wqvq-5m8c-6g24,PYSEC-2020-148 | V:OSV:PYSEC-2020-148
  │ ✔✔✔✔✔ CVE-2023-45803         MEDIUM       4.2   0.6%   ·  ↳ O:GHSA-g4mx-q9vg-27p4,PYSEC-2023-212 | S:GHSA-g4mx-q9vg-27p4,PYSEC-2023-212 | V:OSV:PYSEC-2023-212
  │ ✔✔✔✔✔ CVE-2024-37891         MEDIUM       6.5   1.1%   ·  ↳ O:GHSA-34jh-p97f-mpxf,PYSEC-2026-1995 | S:GHSA-34jh-p97f-mpxf,PYSEC-2026-1995 | V:GHSA-34JH-P97F-MPXF
  │ ✔✔✔✔✔ CVE-2025-50181         MEDIUM       6.1   0.5%   ·  ↳ O:GHSA-pq67-6m6q-mj2v,PYSEC-2026-1999 | S:GHSA-pq67-6m6q-mj2v,PYSEC-2026-1999 | V:MEND:CVE-2025-50181
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/werkzeug@3.1.8
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-102598        MEDIUM       6.3   0.4%   ·  ↳ O:GHSA-g6x2-hccm-hh4m,PYSEC-2026-4312 | S:GHSA-g6x2-hccm-hh4m,PYSEC-2026-4312 | V:OSV:PYSEC-2026-4312
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/wheel@0.42.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-24049         HIGH         7.1   0.4%   ·  ↳ O:GHSA-8rrh-rw8j-w5fx,PYSEC-2026-2047 | S:GHSA-8rrh-rw8j-w5fx,PYSEC-2026-2047 | V:OSV:PYSEC-2026-2047
  └────────────────────────────────────────────────────────────────────────────────────────────────────

  ━━ Debian/Ubuntu (deb) ━━
  ┌─ pkg:deb/ubuntu/binutils@2.42-4ubuntu2.10
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ O:UBUNTU-CVE-2017-13716 | S:UBUNTU-CVE-2017-13716 | V:UB:CVE-2017-13716
  │ ✔✔✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2025-66862 | S:UBUNTU-CVE-2025-66862
  │ ✔✔✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2025-66863 | S:UBUNTU-CVE-2025-66863
  │ ✔✔✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-66864 | S:UBUNTU-CVE-2025-66864
  │ ✔✔✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2025-66865 | S:UBUNTU-CVE-2025-66865
  │ ✔✔✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·  ↳ O:UBUNTU-CVE-2025-66866 | S:UBUNTU-CVE-2025-66866
  │ ✔✔✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·  ↳ O:UBUNTU-CVE-2026-3441 | S:UBUNTU-CVE-2026-3441
  │ ✔✔✔✘✘ CVE-2026-3442          HIGH         7.1   0.3%   ·  ↳ O:UBUNTU-CVE-2026-3442 | S:UBUNTU-CVE-2026-3442
  │ ✔✔✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-6846 | S:UBUNTU-CVE-2026-6846
  │ ✔✔✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-11495 | S:UBUNTU-CVE-2025-11495
  │ ✔✔✔✔✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ O:UBUNTU-CVE-2025-69644 | S:UBUNTU-CVE-2025-69644 | V:UB:CVE-2025-69644
  │ ✔✔✔✔✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-69645 | S:UBUNTU-CVE-2025-69645 | V:UB:CVE-2025-69645
  │ ✔✔✔✔✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-69646 | S:UBUNTU-CVE-2025-69646 | V:UB:CVE-2025-69646
  │ ✔✔✔✔✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ O:UBUNTU-CVE-2025-69647 | S:UBUNTU-CVE-2025-69647 | V:UB:CVE-2025-69647
  │ ✔✔✔✔✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ O:UBUNTU-CVE-2025-69648 | S:UBUNTU-CVE-2025-69648 | V:UB:CVE-2025-69648
  │ ✔✔✔✔✔ CVE-2025-69651         MEDIUM       5.5   0.3%   ·  ↳ O:UBUNTU-CVE-2025-69651 | S:UBUNTU-CVE-2025-69651 | V:UB:CVE-2025-69651
  │ ✔✔✔✔✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ O:UBUNTU-CVE-2025-69652 | S:UBUNTU-CVE-2025-69652 | V:UB:CVE-2025-69652
  │ ✔✔✔✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·  ↳ O:UBUNTU-CVE-2026-15003 | S:UBUNTU-CVE-2026-15003
  │ ✔✔✔✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2026-19548 | S:UBUNTU-CVE-2026-19548
  │ ✔✔✔✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·  ↳ O:UBUNTU-CVE-2026-4647 | S:UBUNTU-CVE-2026-4647
  │ ✔✔✔✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-6844 | S:UBUNTU-CVE-2026-6844
  │ ✔✔✔✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·  ↳ O:UBUNTU-CVE-2026-6845 | S:UBUNTU-CVE-2026-6845
  │ ✔✔✔✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·  ↳ O:UBUNTU-CVE-2026-90801 | S:UBUNTU-CVE-2026-90801
  │ ✔✔✔✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-90802 | S:UBUNTU-CVE-2026-90802
  │ ✔✔✔✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-90803 | S:UBUNTU-CVE-2026-90803
  │ ✔✔✔✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·  ↳ O:UBUNTU-CVE-2026-90804 | S:UBUNTU-CVE-2026-90804
  │ ✔✔✔✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·  ↳ O:UBUNTU-CVE-2026-90828 | S:UBUNTU-CVE-2026-90828
  │ ✔✔✔✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·  ↳ O:UBUNTU-CVE-2026-90829 | S:UBUNTU-CVE-2026-90829
  │ ✔✔✔✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·  ↳ O:UBUNTU-CVE-2026-90830 | S:UBUNTU-CVE-2026-90830
  │ ✔✔✔✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·  ↳ O:UBUNTU-CVE-2026-90831 | S:UBUNTU-CVE-2026-90831
  │ ✔✔✔✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-91779 | S:UBUNTU-CVE-2026-91779
  │ ✔✔✔✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-91780 | S:UBUNTU-CVE-2026-91780
  │ ✔✔✔✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-91781 | S:UBUNTU-CVE-2026-91781
  │ ✔✔✔✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-91782 | S:UBUNTU-CVE-2026-91782
  │ ✔✔✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1149 | S:UBUNTU-CVE-2025-1149
  │ ✔✔✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1150 | S:UBUNTU-CVE-2025-1150
  │ ✔✔✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1151 | S:UBUNTU-CVE-2025-1151
  │ ✔✔✔✔✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1152 | S:UBUNTU-CVE-2025-1152 | V:UB:CVE-2025-1152
  │ ✔✔✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·  ↳ O:UBUNTU-CVE-2025-66861 | S:UBUNTU-CVE-2025-66861
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/binutils-aarch64-linux-gnu@2.42-4ubuntu2.10
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ S:UBUNTU-CVE-2017-13716 | V:UB:CVE-2017-13716
  │ ✘✔✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66862
  │ ✘✔✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66863
  │ ✘✔✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-66864
  │ ✘✔✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66865
  │ ✘✔✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-66866
  │ ✘✔✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3441
  │ ✘✔✔✘✘ CVE-2026-3442          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-3442
  │ ✘✔✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6846
  │ ✘✔✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11495
  │ ✘✔✔✘✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2025-69644 | V:UB:CVE-2025-69644
  │ ✘✔✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69645 | V:UB:CVE-2025-69645
  │ ✘✔✔✘✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69646 | V:UB:CVE-2025-69646
  │ ✘✔✔✘✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69647 | V:UB:CVE-2025-69647
  │ ✘✔✔✘✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69648 | V:UB:CVE-2025-69648
  │ ✘✔✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-69651 | V:UB:CVE-2025-69651
  │ ✘✔✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69652 | V:UB:CVE-2025-69652
  │ ✘✔✔✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15003
  │ ✘✔✔✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19548
  │ ✘✔✔✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-4647
  │ ✘✔✔✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6844
  │ ✘✔✔✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6845
  │ ✘✔✔✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90801
  │ ✘✔✔✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90802
  │ ✘✔✔✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90803
  │ ✘✔✔✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90804
  │ ✘✔✔✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90828
  │ ✘✔✔✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90829
  │ ✘✔✔✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90830
  │ ✘✔✔✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90831
  │ ✘✔✔✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91779
  │ ✘✔✔✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91780
  │ ✘✔✔✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91781
  │ ✘✔✔✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91782
  │ ✘✔✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1149
  │ ✘✔✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1150
  │ ✘✔✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1151
  │ ✘✔✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1152 | V:UB:CVE-2025-1152
  │ ✘✔✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-66861
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/binutils-common@2.42-4ubuntu2.10
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ S:UBUNTU-CVE-2017-13716 | V:UB:CVE-2017-13716
  │ ✘✔✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66862
  │ ✘✔✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66863
  │ ✘✔✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-66864
  │ ✘✔✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66865
  │ ✘✔✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-66866
  │ ✘✔✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3441
  │ ✘✔✔✘✘ CVE-2026-3442          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-3442
  │ ✘✔✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6846
  │ ✘✔✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11495
  │ ✘✔✔✘✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2025-69644 | V:UB:CVE-2025-69644
  │ ✘✔✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69645 | V:UB:CVE-2025-69645
  │ ✘✔✔✘✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69646 | V:UB:CVE-2025-69646
  │ ✘✔✔✘✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69647 | V:UB:CVE-2025-69647
  │ ✘✔✔✘✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69648 | V:UB:CVE-2025-69648
  │ ✘✔✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-69651 | V:UB:CVE-2025-69651
  │ ✘✔✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69652 | V:UB:CVE-2025-69652
  │ ✘✔✔✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15003
  │ ✘✔✔✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19548
  │ ✘✔✔✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-4647
  │ ✘✔✔✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6844
  │ ✘✔✔✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6845
  │ ✘✔✔✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90801
  │ ✘✔✔✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90802
  │ ✘✔✔✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90803
  │ ✘✔✔✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90804
  │ ✘✔✔✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90828
  │ ✘✔✔✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90829
  │ ✘✔✔✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90830
  │ ✘✔✔✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90831
  │ ✘✔✔✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91779
  │ ✘✔✔✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91780
  │ ✘✔✔✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91781
  │ ✘✔✔✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91782
  │ ✘✔✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1149
  │ ✘✔✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1150
  │ ✘✔✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1151
  │ ✘✔✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1152 | V:UB:CVE-2025-1152
  │ ✘✔✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-66861
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/bsdutils@1%3A2.39.3-9ubuntu6.5
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-53612         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53612,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53613         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53613,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53614         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53614,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53615,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-76642
  │ ✘✔✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78408
  │ ✘✔✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78409
  │ ✘✔✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78410
  │ ✘✔✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-13595,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-27456         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-27456,USN-8702-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/bzip2@1.0.8-5.1build0.1
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-42250         MEDIUM       4.8   0.1%   ·  ↳ O:UBUNTU-CVE-2026-42250,USN-8685-1 | S:UBUNTU-CVE-2026-42250,USN-8685-1 | V:UB:CVE-2026-42250
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/ca-certificates@20260601~24.04.1
  │ OSGTV
  │ ✔✔✘✘✘ USN-8944-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/coreutils@9.4-3ubuntu6.2
  │ OSGTV
  │ ✔✔✔✘✘ CVE-2016-2781          MEDIUM       6.5   0.4%   ·  ↳ O:UBUNTU-CVE-2016-2781 | S:UBUNTU-CVE-2016-2781
  │ ✔✔✔✔✔ CVE-2025-5278          MEDIUM       4.4   0.3%   ·  ↳ O:UBUNTU-CVE-2025-5278,USN-8697-1 | S:UBUNTU-CVE-2025-5278,USN-8697-1 | V:UB:CVE-2025-5278
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/cpp@4%3A13.2.0-7ubuntu1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/cpp-13@13.3.0-6ubuntu2~24.04.1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/cpp-13-aarch64-linux-gnu@13.3.0-6ubuntu2~24.04.1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/cpp-aarch64-linux-gnu@4%3A13.2.0-7ubuntu1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/curl@8.5.0-2ubuntu10.11
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-11856         CRITICAL     9.8   0.7%   ·  ↳ O:UBUNTU-CVE-2026-11856 | S:UBUNTU-CVE-2026-11856 | V:UB:CVE-2026-11856
  │ ✔✔✔✔✔ CVE-2026-18924         CRITICAL     9.1   0.6%   ·  ↳ O:UBUNTU-CVE-2026-18924,USN-8820-1 | S:UBUNTU-CVE-2026-18924,USN-8820-1 | V:UB:CVE-2026-18924
  │ ✔✔✔✔✔ CVE-2026-86414         CRITICAL     9.1   0.7%   ·  ↳ O:UBUNTU-CVE-2026-86414,USN-8932-1 | S:UBUNTU-CVE-2026-86414,USN-8932-1 | V:UB:CVE-2026-86414
  │ ✔✔✔✔✔ CVE-2026-92388         CRITICAL     9.1   0.7%   ·  ↳ O:UBUNTU-CVE-2026-92388,USN-8932-1 | S:UBUNTU-CVE-2026-92388,USN-8932-1 | V:UB:CVE-2026-92388
  │ ✔✔✔✔✔ CVE-2026-13608         HIGH         7.4   0.5%   ·  ↳ O:UBUNTU-CVE-2026-13608,USN-8820-1 | S:UBUNTU-CVE-2026-13608,USN-8820-1 | V:UB:CVE-2026-13608
  │ ✔✔✔✔✔ CVE-2026-80230         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-80230,USN-8820-1 | S:UBUNTU-CVE-2026-80230,USN-8820-1 | V:UB:CVE-2026-80230
  │ ✔✔✔✔✔ CVE-2026-82209         HIGH         8.2   0.4%   ·  ↳ O:UBUNTU-CVE-2026-82209,USN-8820-1 | S:UBUNTU-CVE-2026-82209,USN-8820-1 | V:UB:CVE-2026-82209
  │ ✔✔✔✔✔ CVE-2026-86409         HIGH         8.1   1.1%   ·  ↳ O:UBUNTU-CVE-2026-86409,USN-8932-1 | S:UBUNTU-CVE-2026-86409,USN-8932-1 | V:UB:CVE-2026-86409
  │ ✔✔✔✔✔ CVE-2026-87862         HIGH         8.1   1.0%   ·  ↳ O:UBUNTU-CVE-2026-87862,USN-8932-1 | S:UBUNTU-CVE-2026-87862,USN-8932-1 | V:UB:CVE-2026-87862
  │ ✔✔✔✔✔ CVE-2026-87863         HIGH         8.1   0.8%   ·  ↳ O:UBUNTU-CVE-2026-87863,USN-8932-1 | S:UBUNTU-CVE-2026-87863,USN-8932-1 | V:UB:CVE-2026-87863
  │ ✔✔✔✔✔ CVE-2026-87864         HIGH         8.1   0.8%   ·  ↳ O:UBUNTU-CVE-2026-87864,USN-8932-1 | S:UBUNTU-CVE-2026-87864,USN-8932-1 | V:UB:CVE-2026-87864
  │ ✔✔✔✔✔ CVE-2026-8932          HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-8932,USN-8670-1 | S:UBUNTU-CVE-2026-8932,USN-8670-1 | V:UB:CVE-2026-8932
  │ ✔✔✔✔✔ CVE-2026-92389         HIGH         8.1   0.7%   ·  ↳ O:UBUNTU-CVE-2026-92389,USN-8932-1 | S:UBUNTU-CVE-2026-92389,USN-8932-1 | V:UB:CVE-2026-92389
  │ ✔✔✔✔✔ CVE-2026-92391         HIGH         7.5   1.2%   ·  ↳ O:UBUNTU-CVE-2026-92391,USN-8932-1 | S:UBUNTU-CVE-2026-92391,USN-8932-1 | V:UB:CVE-2026-92391
  │ ✔✔✔✔✔ CVE-2026-94266         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-94266,USN-8932-1 | S:UBUNTU-CVE-2026-94266,USN-8932-1 | V:UB:CVE-2026-94266
  │ ✔✔✘✘✘ USN-8651-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dash@0.5.12-6ubuntu5
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-102473        MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-102473 | S:UBUNTU-CVE-2026-102473 | V:UB:CVE-2026-102473
  │ ✔✔✔✔✔ CVE-2026-102474        MEDIUM       4.0   0.1%   ·  ↳ O:UBUNTU-CVE-2026-102474 | S:UBUNTU-CVE-2026-102474 | V:UB:CVE-2026-102474
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/diffutils@1%3A3.10-1build1
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-53910         LOW          2.1   0.3%   ·  ↳ O:UBUNTU-CVE-2026-53910,USN-8692-1 | S:UBUNTU-CVE-2026-53910,USN-8692-1 | V:UB:CVE-2026-53910
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dirmngr@2.4.4-2ubuntu17.4
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57062,USN-8720-1
  │ ✘✔✔✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/g%2B%2B@4%3A13.2.0-7ubuntu1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/g%2B%2B-13@13.3.0-6ubuntu2~24.04.1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/g%2B%2B-13-aarch64-linux-gnu@13.3.0-6ubuntu2~24.04.1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/g%2B%2B-aarch64-linux-gnu@4%3A13.2.0-7ubuntu1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc@4%3A13.2.0-7ubuntu1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc-13@13.3.0-6ubuntu2~24.04.1
  │ OSGTV
  │ ✔✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ O:UBUNTU-CVE-2026-102010 | S:UBUNTU-CVE-2026-102010
  │ ✔✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ O:UBUNTU-CVE-2026-114690 | S:UBUNTU-CVE-2026-114690
  │ ✔✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ O:UBUNTU-CVE-2026-114691 | S:UBUNTU-CVE-2026-114691
  │ ✔✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ O:UBUNTU-CVE-2026-115455 | S:UBUNTU-CVE-2026-115455
  │ ✔✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ O:UBUNTU-CVE-2026-115456 | S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc-13-aarch64-linux-gnu@13.3.0-6ubuntu2~24.04.1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc-13-base@13.3.0-6ubuntu2~24.04.1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc-aarch64-linux-gnu@4%3A13.2.0-7ubuntu1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gnupg@2.4.4-2ubuntu17.4
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57062,USN-8720-1
  │ ✘✔✔✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gnupg-l10n@2.4.4-2ubuntu17.4
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57062,USN-8720-1
  │ ✘✔✔✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gnupg-utils@2.4.4-2ubuntu17.4
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57062,USN-8720-1
  │ ✘✔✔✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg@2.4.4-2ubuntu17.4
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57062,USN-8720-1
  │ ✘✔✔✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg-agent@2.4.4-2ubuntu17.4
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57062,USN-8720-1
  │ ✘✔✔✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg-wks-client@2.4.4-2ubuntu17.4
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57062,USN-8720-1
  │ ✘✔✔✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpgconf@2.4.4-2ubuntu17.4
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57062,USN-8720-1
  │ ✘✔✔✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpgsm@2.4.4-2ubuntu17.4
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✔✘✔ CVE-2026-57062         LOW          2.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57062,USN-8720-1 | V:UB:CVE-2026-57062
  │ ✘✔✔✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpgv@2.4.4-2ubuntu17.4
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57062,USN-8720-1
  │ ✘✔✔✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gzip@1.12-1ubuntu3.1
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-41992         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-41992,USN-8512-1 | S:UBUNTU-CVE-2026-41992,USN-8512-1 | V:UB:CVE-2026-41992
  │ ✔✔✔✔✔ CVE-2026-41991         MEDIUM       4.7   0.1%   ·  ↳ O:UBUNTU-CVE-2026-41991,USN-8512-1 | S:UBUNTU-CVE-2026-41991,USN-8512-1 | V:UB:CVE-2026-41991
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/keyboxd@2.4.4-2ubuntu17.4
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57062,USN-8720-1
  │ ✘✔✔✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/krb5-locales@1.20.1-6ubuntu2.7
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-107778        HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-107778
  │ ✘✔✔✘✘ CVE-2026-107708        MEDIUM       6.9   0.5%   ·  ↳ S:UBUNTU-CVE-2026-107708
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libacl1@2.3.2-1build1.1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-54369         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-54369
  │ ✘✔✔✘✘ CVE-2026-54370         HIGH         7.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-54370
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libaom3@3.8.2-2ubuntu0.1
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-56208         HIGH         7.6   0.6%   ·  ↳ S:UBUNTU-CVE-2026-56208,USN-8772-1 | V:UB:CVE-2026-56208
  │ ✘✔✔✘✔ CVE-2026-56209         HIGH         7.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-56209,USN-8772-1 | V:UB:CVE-2026-56209
  │ ✘✔✔✘✔ CVE-2026-56210         HIGH         7.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-56210,USN-8772-1 | V:UB:CVE-2026-56210
  │ ✘✔✔✘✔ CVE-2026-56211         HIGH         7.1   0.9%   ·  ↳ S:UBUNTU-CVE-2026-56211,USN-8772-1 | V:UB:CVE-2026-56211
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libattr1@1%3A2.5.2-1build1.1
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-54371         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-54371,USN-8691-1 | V:UB:CVE-2026-54371
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libbinutils@2.42-4ubuntu2.10
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ S:UBUNTU-CVE-2017-13716 | V:UB:CVE-2017-13716
  │ ✘✔✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66862
  │ ✘✔✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66863
  │ ✘✔✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-66864
  │ ✘✔✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66865
  │ ✘✔✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-66866
  │ ✘✔✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3441
  │ ✘✔✔✘✘ CVE-2026-3442          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-3442
  │ ✘✔✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6846
  │ ✘✔✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11495
  │ ✘✔✔✘✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2025-69644 | V:UB:CVE-2025-69644
  │ ✘✔✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69645 | V:UB:CVE-2025-69645
  │ ✘✔✔✘✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69646 | V:UB:CVE-2025-69646
  │ ✘✔✔✘✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69647 | V:UB:CVE-2025-69647
  │ ✘✔✔✘✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69648 | V:UB:CVE-2025-69648
  │ ✘✔✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-69651 | V:UB:CVE-2025-69651
  │ ✘✔✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69652 | V:UB:CVE-2025-69652
  │ ✘✔✔✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15003
  │ ✘✔✔✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19548
  │ ✘✔✔✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-4647
  │ ✘✔✔✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6844
  │ ✘✔✔✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6845
  │ ✘✔✔✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90801
  │ ✘✔✔✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90802
  │ ✘✔✔✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90803
  │ ✘✔✔✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90804
  │ ✘✔✔✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90828
  │ ✘✔✔✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90829
  │ ✘✔✔✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90830
  │ ✘✔✔✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90831
  │ ✘✔✔✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91779
  │ ✘✔✔✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91780
  │ ✘✔✔✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91781
  │ ✘✔✔✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91782
  │ ✘✔✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1149
  │ ✘✔✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1150
  │ ✘✔✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1151
  │ ✘✔✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1152 | V:UB:CVE-2025-1152
  │ ✘✔✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-66861
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libblkid1@2.39.3-9ubuntu6.5
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-53612         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53612,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53613         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53613,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53614         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53614,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53615,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-76642
  │ ✘✔✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78408
  │ ✘✔✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78409
  │ ✘✔✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78410
  │ ✘✔✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-13595,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-27456         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-27456,USN-8702-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libbrotli1@1.1.0-2build2
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-111497        CRITICAL     9.8  82.6% KEV  ↳ S:UBUNTU-CVE-2026-111497,USN-8956-1 | V:UB:CVE-2026-111497
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libbz2-1.0@1.0.8-5.1build0.1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-42250         MEDIUM       4.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-42250,USN-8685-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc-bin@2.39-0ubuntu8.8
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6791,USN-8737-2
  │ ✘✔✔✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·  ↳ S:UBUNTU-CVE-2016-20013
  │ ✘✔✔✘✘ CVE-2026-19499         HIGH         7.7   0.3%   ·  ↳ S:UBUNTU-CVE-2026-19499,USN-8737-2
  │ ✘✔✔✘✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18374 | V:UB:CVE-2026-18374
  │ ✘✔✔✘✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19542,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-77117,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80489,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-8674
  │ ✘✔✔✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-86805
  │ ✘✔✔✘✔ CVE-2026-89092         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89092 | V:UB:CVE-2026-89092
  │ ✘✔✔✘✘ CVE-2026-6368          LOW          2.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6368,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-95818
  │ ✘✔✔✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97399
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc-dev-bin@2.39-0ubuntu8.8
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6791,USN-8737-2
  │ ✘✔✔✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·  ↳ S:UBUNTU-CVE-2016-20013
  │ ✘✔✔✘✘ CVE-2026-19499         HIGH         7.7   0.3%   ·  ↳ S:UBUNTU-CVE-2026-19499,USN-8737-2
  │ ✘✔✔✘✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18374 | V:UB:CVE-2026-18374
  │ ✘✔✔✘✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19542,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-77117,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80489,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-8674
  │ ✘✔✔✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-86805
  │ ✘✔✔✘✔ CVE-2026-89092         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89092 | V:UB:CVE-2026-89092
  │ ✘✔✔✘✘ CVE-2026-6368          LOW          2.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6368,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-95818
  │ ✘✔✔✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97399
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc-devtools@2.39-0ubuntu8.8
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6791,USN-8737-2
  │ ✘✔✔✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·  ↳ S:UBUNTU-CVE-2016-20013
  │ ✘✔✔✘✘ CVE-2026-19499         HIGH         7.7   0.3%   ·  ↳ S:UBUNTU-CVE-2026-19499,USN-8737-2
  │ ✘✔✔✘✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18374 | V:UB:CVE-2026-18374
  │ ✘✔✔✘✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19542,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-77117,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80489,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-8674
  │ ✘✔✔✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-86805
  │ ✘✔✔✘✔ CVE-2026-89092         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89092 | V:UB:CVE-2026-89092
  │ ✘✔✔✘✘ CVE-2026-6368          LOW          2.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6368,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-95818
  │ ✘✔✔✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97399
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc6@2.39-0ubuntu8.8
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-6791          CRITICAL     9.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6791,USN-8737-2 | V:UB:CVE-2026-6791
  │ ✘✔✔✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·  ↳ S:UBUNTU-CVE-2016-20013
  │ ✘✔✔✘✔ CVE-2026-19499         HIGH         7.7   0.3%   ·  ↳ S:UBUNTU-CVE-2026-19499,USN-8737-2 | V:UB:CVE-2026-19499
  │ ✘✔✔✘✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18374 | V:UB:CVE-2026-18374
  │ ✘✔✔✘✔ CVE-2026-19542         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19542,USN-8737-2 | V:UB:CVE-2026-19542
  │ ✘✔✔✘✔ CVE-2026-77117         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-77117,USN-8737-2 | V:UB:CVE-2026-77117
  │ ✘✔✔✘✔ CVE-2026-80489         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80489,USN-8737-2 | V:UB:CVE-2026-80489
  │ ✘✔✔✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-8674
  │ ✘✔✔✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-86805
  │ ✘✔✔✘✔ CVE-2026-89092         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89092 | V:UB:CVE-2026-89092
  │ ✘✔✔✘✔ CVE-2026-6368          LOW          2.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6368,USN-8737-2 | V:UB:CVE-2026-6368
  │ ✘✔✔✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-95818
  │ ✘✔✔✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97399
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc6-dev@2.39-0ubuntu8.8
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6791,USN-8737-2
  │ ✘✔✔✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·  ↳ S:UBUNTU-CVE-2016-20013
  │ ✘✔✔✘✘ CVE-2026-19499         HIGH         7.7   0.3%   ·  ↳ S:UBUNTU-CVE-2026-19499,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18374
  │ ✘✔✔✘✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19542,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-77117,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80489,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-8674
  │ ✘✔✔✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-86805
  │ ✘✔✔✘✘ CVE-2026-89092         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89092
  │ ✘✔✔✘✘ CVE-2026-6368          LOW          2.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6368,USN-8737-2
  │ ✘✔✔✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-95818
  │ ✘✔✔✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97399
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libctf-nobfd0@2.42-4ubuntu2.10
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ S:UBUNTU-CVE-2017-13716 | V:UB:CVE-2017-13716
  │ ✘✔✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66862
  │ ✘✔✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66863
  │ ✘✔✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-66864
  │ ✘✔✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66865
  │ ✘✔✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-66866
  │ ✘✔✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3441
  │ ✘✔✔✘✘ CVE-2026-3442          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-3442
  │ ✘✔✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6846
  │ ✘✔✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11495
  │ ✘✔✔✘✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2025-69644 | V:UB:CVE-2025-69644
  │ ✘✔✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69645 | V:UB:CVE-2025-69645
  │ ✘✔✔✘✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69646 | V:UB:CVE-2025-69646
  │ ✘✔✔✘✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69647 | V:UB:CVE-2025-69647
  │ ✘✔✔✘✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69648 | V:UB:CVE-2025-69648
  │ ✘✔✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-69651 | V:UB:CVE-2025-69651
  │ ✘✔✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69652 | V:UB:CVE-2025-69652
  │ ✘✔✔✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15003
  │ ✘✔✔✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19548
  │ ✘✔✔✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-4647
  │ ✘✔✔✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6844
  │ ✘✔✔✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6845
  │ ✘✔✔✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90801
  │ ✘✔✔✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90802
  │ ✘✔✔✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90803
  │ ✘✔✔✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90804
  │ ✘✔✔✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90828
  │ ✘✔✔✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90829
  │ ✘✔✔✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90830
  │ ✘✔✔✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90831
  │ ✘✔✔✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91779
  │ ✘✔✔✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91780
  │ ✘✔✔✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91781
  │ ✘✔✔✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91782
  │ ✘✔✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1149
  │ ✘✔✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1150
  │ ✘✔✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1151
  │ ✘✔✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1152 | V:UB:CVE-2025-1152
  │ ✘✔✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-66861
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libctf0@2.42-4ubuntu2.10
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ S:UBUNTU-CVE-2017-13716 | V:UB:CVE-2017-13716
  │ ✘✔✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66862
  │ ✘✔✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66863
  │ ✘✔✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-66864
  │ ✘✔✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66865
  │ ✘✔✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-66866
  │ ✘✔✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3441
  │ ✘✔✔✘✘ CVE-2026-3442          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-3442
  │ ✘✔✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6846
  │ ✘✔✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11495
  │ ✘✔✔✘✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2025-69644 | V:UB:CVE-2025-69644
  │ ✘✔✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69645 | V:UB:CVE-2025-69645
  │ ✘✔✔✘✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69646 | V:UB:CVE-2025-69646
  │ ✘✔✔✘✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69647 | V:UB:CVE-2025-69647
  │ ✘✔✔✘✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69648 | V:UB:CVE-2025-69648
  │ ✘✔✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-69651 | V:UB:CVE-2025-69651
  │ ✘✔✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69652 | V:UB:CVE-2025-69652
  │ ✘✔✔✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15003
  │ ✘✔✔✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19548
  │ ✘✔✔✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-4647
  │ ✘✔✔✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6844
  │ ✘✔✔✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6845
  │ ✘✔✔✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90801
  │ ✘✔✔✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90802
  │ ✘✔✔✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90803
  │ ✘✔✔✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90804
  │ ✘✔✔✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90828
  │ ✘✔✔✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90829
  │ ✘✔✔✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90830
  │ ✘✔✔✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90831
  │ ✘✔✔✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91779
  │ ✘✔✔✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91780
  │ ✘✔✔✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91781
  │ ✘✔✔✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91782
  │ ✘✔✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1149
  │ ✘✔✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1150
  │ ✘✔✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1151
  │ ✘✔✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1152 | V:UB:CVE-2025-1152
  │ ✘✔✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-66861
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libcurl4t64@8.5.0-2ubuntu10.11
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-11856         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-11856 | V:UB:CVE-2026-11856
  │ ✘✔✔✘✔ CVE-2026-18924         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-18924,USN-8820-1 | V:UB:CVE-2026-18924
  │ ✘✔✔✘✔ CVE-2026-86414         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-86414,USN-8932-1 | V:UB:CVE-2026-86414
  │ ✘✔✔✘✔ CVE-2026-92388         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-92388,USN-8932-1 | V:UB:CVE-2026-92388
  │ ✘✔✔✘✔ CVE-2026-13608         HIGH         7.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-13608,USN-8820-1 | V:UB:CVE-2026-13608
  │ ✘✔✔✘✔ CVE-2026-80230         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80230,USN-8820-1 | V:UB:CVE-2026-80230
  │ ✘✔✔✘✔ CVE-2026-82209         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-82209,USN-8820-1 | V:UB:CVE-2026-82209
  │ ✘✔✔✘✔ CVE-2026-86409         HIGH         8.1   1.1%   ·  ↳ S:UBUNTU-CVE-2026-86409,USN-8932-1 | V:UB:CVE-2026-86409
  │ ✘✔✔✘✔ CVE-2026-87862         HIGH         8.1   1.0%   ·  ↳ S:UBUNTU-CVE-2026-87862,USN-8932-1 | V:UB:CVE-2026-87862
  │ ✘✔✔✘✔ CVE-2026-87863         HIGH         8.1   0.8%   ·  ↳ S:UBUNTU-CVE-2026-87863,USN-8932-1 | V:UB:CVE-2026-87863
  │ ✘✔✔✘✔ CVE-2026-87864         HIGH         8.1   0.8%   ·  ↳ S:UBUNTU-CVE-2026-87864,USN-8932-1 | V:UB:CVE-2026-87864
  │ ✘✔✔✘✔ CVE-2026-8932          HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-8932,USN-8670-1 | V:UB:CVE-2026-8932
  │ ✘✔✔✘✔ CVE-2026-92389         HIGH         8.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-92389,USN-8932-1 | V:UB:CVE-2026-92389
  │ ✘✔✔✘✔ CVE-2026-92391         HIGH         7.5   1.2%   ·  ↳ S:UBUNTU-CVE-2026-92391,USN-8932-1 | V:UB:CVE-2026-92391
  │ ✘✔✔✘✔ CVE-2026-94266         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-94266,USN-8932-1 | V:UB:CVE-2026-94266
  │ ✘✔✘✘✘ USN-8651-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libexpat1@2.6.1-2ubuntu0.4
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2025-59375         HIGH         7.5   1.4%   ·  ↳ S:UBUNTU-CVE-2025-59375,USN-8790-1 | V:UB:CVE-2025-59375
  │ ✘✔✔✘✘ CVE-2026-102633        HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-102633
  │ ✘✔✔✘✘ CVE-2026-113351        HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-113351
  │ ✘✔✔✘✘ CVE-2026-115506        HIGH         8.7   0.5%   ·  ↳ S:UBUNTU-CVE-2026-115506
  │ ✘✔✔✘✘ CVE-2026-117610        HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-117610
  │ ✘✔✔✘✘ CVE-2026-118370        HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-118370
  │ ✘✔✔✘✔ CVE-2026-41080         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-41080,USN-8790-1 | V:UB:CVE-2026-41080
  │ ✘✔✔✘✔ CVE-2026-45186         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-45186,USN-8790-1 | V:UB:CVE-2026-45186
  │ ✘✔✔✘✔ CVE-2026-66046         HIGH         8.7   0.7%   ·  ↳ S:UBUNTU-CVE-2026-66046,USN-8813-1 | V:UB:CVE-2026-66046
  │ ✘✔✔✘✔ CVE-2026-76641         HIGH         8.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-76641,USN-8813-1 | V:UB:CVE-2026-76641
  │ ✘✔✔✘✔ CVE-2026-76957         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-76957,USN-8813-1 | V:UB:CVE-2026-76957
  │ ✘✔✔✘✘ CVE-2026-77214         HIGH         8.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-77214
  │ ✘✔✔✘✘ CVE-2026-93990         HIGH         8.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-93990
  │ ✘✔✔✘✔ CVE-2025-66382         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-66382 | V:UB:CVE-2025-66382
  │ ✘✔✔✘✔ CVE-2026-32776         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-32776,USN-8790-1 | V:UB:CVE-2026-32776
  │ ✘✔✔✘✔ CVE-2026-32777         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-32777,USN-8790-1 | V:UB:CVE-2026-32777
  │ ✘✔✔✘✔ CVE-2026-32778         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-32778,USN-8790-1 | V:UB:CVE-2026-32778
  │ ✘✔✔✘✔ CVE-2026-50219         MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-50219,USN-8790-1 | V:UB:CVE-2026-50219
  │ ✘✔✔✘✔ CVE-2026-56131         MEDIUM       4.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56131,USN-8813-1 | V:UB:CVE-2026-56131
  │ ✘✔✔✘✔ CVE-2026-56132         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56132,USN-8813-1 | V:UB:CVE-2026-56132
  │ ✘✔✔✘✔ CVE-2026-56403         MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56403,USN-8790-1 | V:UB:CVE-2026-56403
  │ ✘✔✔✘✔ CVE-2026-56404         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56404,USN-8790-1 | V:UB:CVE-2026-56404
  │ ✘✔✔✘✔ CVE-2026-56405         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56405,USN-8790-1 | V:UB:CVE-2026-56405
  │ ✘✔✔✘✔ CVE-2026-56406         MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56406,USN-8813-1 | V:UB:CVE-2026-56406
  │ ✘✔✔✘✔ CVE-2026-56407         MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56407,USN-8813-1 | V:UB:CVE-2026-56407
  │ ✘✔✔✘✔ CVE-2026-56408         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56408,USN-8790-1 | V:UB:CVE-2026-56408
  │ ✘✔✔✘✔ CVE-2026-56409         MEDIUM       6.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56409,USN-8813-1 | V:UB:CVE-2026-56409
  │ ✘✔✔✘✔ CVE-2026-56410         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56410,USN-8813-1 | V:UB:CVE-2026-56410
  │ ✘✔✔✘✔ CVE-2026-56411         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56411,USN-8813-1 | V:UB:CVE-2026-56411
  │ ✘✔✔✘✔ CVE-2026-56412         MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56412,USN-8790-1 | V:UB:CVE-2026-56412
  │ ✘✔✔✘✔ CVE-2026-72522         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72522,USN-8813-1 | V:UB:CVE-2026-72522
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libexpat1-dev@2.6.1-2ubuntu0.4
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2025-59375         HIGH         7.5   1.4%   ·  ↳ S:UBUNTU-CVE-2025-59375,USN-8790-1 | V:UB:CVE-2025-59375
  │ ✘✔✔✘✘ CVE-2026-102633        HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-102633
  │ ✘✔✔✘✘ CVE-2026-113351        HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-113351
  │ ✘✔✔✘✘ CVE-2026-115506        HIGH         8.7   0.5%   ·  ↳ S:UBUNTU-CVE-2026-115506
  │ ✘✔✔✘✘ CVE-2026-117610        HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-117610
  │ ✘✔✔✘✘ CVE-2026-118370        HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-118370
  │ ✘✔✔✘✔ CVE-2026-41080         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-41080,USN-8790-1 | V:UB:CVE-2026-41080
  │ ✘✔✔✘✔ CVE-2026-45186         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-45186,USN-8790-1 | V:UB:CVE-2026-45186
  │ ✘✔✔✘✔ CVE-2026-66046         HIGH         8.7   0.7%   ·  ↳ S:UBUNTU-CVE-2026-66046,USN-8813-1 | V:UB:CVE-2026-66046
  │ ✘✔✔✘✔ CVE-2026-76641         HIGH         8.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-76641,USN-8813-1 | V:UB:CVE-2026-76641
  │ ✘✔✔✘✔ CVE-2026-76957         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-76957,USN-8813-1 | V:UB:CVE-2026-76957
  │ ✘✔✔✘✘ CVE-2026-77214         HIGH         8.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-77214
  │ ✘✔✔✘✘ CVE-2026-93990         HIGH         8.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-93990
  │ ✘✔✔✘✘ CVE-2025-66382         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-66382
  │ ✘✔✔✘✔ CVE-2026-32776         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-32776,USN-8790-1 | V:UB:CVE-2026-32776
  │ ✘✔✔✘✔ CVE-2026-32777         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-32777,USN-8790-1 | V:UB:CVE-2026-32777
  │ ✘✔✔✘✔ CVE-2026-32778         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-32778,USN-8790-1 | V:UB:CVE-2026-32778
  │ ✘✔✔✘✔ CVE-2026-50219         MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-50219,USN-8790-1 | V:UB:CVE-2026-50219
  │ ✘✔✔✘✔ CVE-2026-56131         MEDIUM       4.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56131,USN-8813-1 | V:UB:CVE-2026-56131
  │ ✘✔✔✘✔ CVE-2026-56132         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56132,USN-8813-1 | V:UB:CVE-2026-56132
  │ ✘✔✔✘✔ CVE-2026-56403         MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56403,USN-8790-1 | V:UB:CVE-2026-56403
  │ ✘✔✔✘✔ CVE-2026-56404         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56404,USN-8790-1 | V:UB:CVE-2026-56404
  │ ✘✔✔✘✔ CVE-2026-56405         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56405,USN-8790-1 | V:UB:CVE-2026-56405
  │ ✘✔✔✘✔ CVE-2026-56406         MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56406,USN-8813-1 | V:UB:CVE-2026-56406
  │ ✘✔✔✘✔ CVE-2026-56407         MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56407,USN-8813-1 | V:UB:CVE-2026-56407
  │ ✘✔✔✘✔ CVE-2026-56408         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56408,USN-8790-1 | V:UB:CVE-2026-56408
  │ ✘✔✔✘✔ CVE-2026-56409         MEDIUM       6.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56409,USN-8813-1 | V:UB:CVE-2026-56409
  │ ✘✔✔✘✔ CVE-2026-56410         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56410,USN-8813-1 | V:UB:CVE-2026-56410
  │ ✘✔✔✘✔ CVE-2026-56411         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56411,USN-8813-1 | V:UB:CVE-2026-56411
  │ ✘✔✔✘✔ CVE-2026-56412         MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56412,USN-8790-1 | V:UB:CVE-2026-56412
  │ ✘✔✔✘✔ CVE-2026-72522         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72522,USN-8813-1 | V:UB:CVE-2026-72522
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libfreetype6@2.13.2%2Bdfsg-1ubuntu0.1
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-95512         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-95512,USN-8881-1 | V:UB:CVE-2026-95512
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgcc-13-dev@13.3.0-6ubuntu2~24.04.1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgcrypt20@1.10.3-2ubuntu0.1
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2024-2236          MEDIUM       5.9   1.1%   ·  ↳ O:UBUNTU-CVE-2024-2236,USN-8711-1 | S:UBUNTU-CVE-2024-2236,USN-8711-1 | V:UB:CVE-2024-2236
  │ ✘✘✘✘✔ CVE-2026-41990         MEDIUM       4.0   0.2%   ·  ↳ V:UB:CVE-2026-41990
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgd3@2.3.3-9ubuntu5
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-9672          ?             -       -   ·  ↳ S:UBUNTU-CVE-2026-9672
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgnutls30t64@3.8.3-1.1ubuntu3.6
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-88647         MEDIUM       6.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-88647 | V:UB:CVE-2026-88647
  │ ✘✔✔✘✔ CVE-2026-95184         MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-95184 | V:UB:CVE-2026-95184
  │ ✘✔✔✘✔ CVE-2026-95209         MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-95209 | V:UB:CVE-2026-95209
  │ ✘✔✔✘✔ CVE-2026-95210         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-95210 | V:UB:CVE-2026-95210
  │ ✘✔✔✘✔ CVE-2026-67693         LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-67693 | V:UB:CVE-2026-67693
  │ ✘✔✔✘✔ CVE-2026-88648         LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-88648 | V:UB:CVE-2026-88648
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgprofng0@2.42-4ubuntu2.10
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ S:UBUNTU-CVE-2017-13716 | V:UB:CVE-2017-13716
  │ ✘✔✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66862
  │ ✘✔✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66863
  │ ✘✔✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-66864
  │ ✘✔✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66865
  │ ✘✔✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-66866
  │ ✘✔✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3441
  │ ✘✔✔✘✘ CVE-2026-3442          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-3442
  │ ✘✔✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6846
  │ ✘✔✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11495
  │ ✘✔✔✘✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2025-69644 | V:UB:CVE-2025-69644
  │ ✘✔✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69645 | V:UB:CVE-2025-69645
  │ ✘✔✔✘✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69646 | V:UB:CVE-2025-69646
  │ ✘✔✔✘✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69647 | V:UB:CVE-2025-69647
  │ ✘✔✔✘✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69648 | V:UB:CVE-2025-69648
  │ ✘✔✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-69651 | V:UB:CVE-2025-69651
  │ ✘✔✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69652 | V:UB:CVE-2025-69652
  │ ✘✔✔✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15003
  │ ✘✔✔✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19548
  │ ✘✔✔✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-4647
  │ ✘✔✔✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6844
  │ ✘✔✔✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6845
  │ ✘✔✔✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90801
  │ ✘✔✔✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90802
  │ ✘✔✔✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90803
  │ ✘✔✔✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90804
  │ ✘✔✔✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90828
  │ ✘✔✔✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90829
  │ ✘✔✔✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90830
  │ ✘✔✔✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90831
  │ ✘✔✔✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91779
  │ ✘✔✔✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91780
  │ ✘✔✔✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91781
  │ ✘✔✔✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91782
  │ ✘✔✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1149
  │ ✘✔✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1150
  │ ✘✔✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1151
  │ ✘✔✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1152 | V:UB:CVE-2025-1152
  │ ✘✔✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-66861
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgssapi-krb5-2@1.20.1-6ubuntu2.7
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-107778        HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-107778
  │ ✘✔✔✘✘ CVE-2026-107708        MEDIUM       6.9   0.5%   ·  ↳ S:UBUNTU-CVE-2026-107708
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libheif-plugin-aomdec@1.17.6-1ubuntu4.6
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-84384         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-84384,USN-8846-1 | V:UB:CVE-2026-84384
  │ ✘✔✔✘✔ CVE-2026-84447         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-84447,USN-8846-1 | V:UB:CVE-2026-84447
  │ ✘✔✔✘✔ CVE-2026-62289         MEDIUM       4.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-62289,USN-8683-1 | V:UB:CVE-2026-62289
  │ ✘✔✔✘✔ CVE-2026-62291         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-62291,USN-8683-1 | V:UB:CVE-2026-62291
  │ ✘✔✔✘✔ CVE-2026-84448         MEDIUM       4.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-84448,USN-8846-1 | V:UB:CVE-2026-84448
  │ ✘✔✔✘✔ CVE-2026-84449         LOW          3.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-84449,USN-8846-1 | V:UB:CVE-2026-84449
  │ ✘✔✘✘✘ USN-8649-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libheif-plugin-aomenc@1.17.6-1ubuntu4.6
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-84384         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-84384,USN-8846-1 | V:UB:CVE-2026-84384
  │ ✘✔✔✘✔ CVE-2026-84447         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-84447,USN-8846-1 | V:UB:CVE-2026-84447
  │ ✘✔✔✘✔ CVE-2026-62289         MEDIUM       4.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-62289,USN-8683-1 | V:UB:CVE-2026-62289
  │ ✘✔✔✘✔ CVE-2026-62291         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-62291,USN-8683-1 | V:UB:CVE-2026-62291
  │ ✘✔✔✘✔ CVE-2026-84448         MEDIUM       4.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-84448,USN-8846-1 | V:UB:CVE-2026-84448
  │ ✘✔✔✘✔ CVE-2026-84449         LOW          3.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-84449,USN-8846-1 | V:UB:CVE-2026-84449
  │ ✘✔✘✘✘ USN-8649-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libheif1@1.17.6-1ubuntu4.6
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-84384         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-84384,USN-8846-1 | V:UB:CVE-2026-84384
  │ ✘✔✔✘✔ CVE-2026-84447         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-84447,USN-8846-1 | V:UB:CVE-2026-84447
  │ ✘✔✔✘✔ CVE-2026-62289         MEDIUM       4.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-62289,USN-8683-1 | V:UB:CVE-2026-62289
  │ ✘✔✔✘✔ CVE-2026-62291         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-62291,USN-8683-1 | V:UB:CVE-2026-62291
  │ ✘✔✔✘✔ CVE-2026-84448         MEDIUM       4.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-84448,USN-8846-1 | V:UB:CVE-2026-84448
  │ ✘✔✔✘✔ CVE-2026-84449         LOW          3.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-84449,USN-8846-1 | V:UB:CVE-2026-84449
  │ ✘✔✘✘✘ USN-8649-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libhwasan0@14.2.0-4ubuntu2~24.04.1
  │ OSGTV
  │ ✘✘✘✘✔ CVE-2021-3826          MEDIUM       6.5   1.5%   ·  ↳ V:UB:CVE-2021-3826
  │ ✘✘✘✘✔ CVE-2021-46195         MEDIUM       5.5   0.8%   ·  ↳ V:UB:CVE-2021-46195
  │ ✘✘✘✘✔ CVE-2022-27943         MEDIUM       5.5   1.0%   ·  ↳ V:UB:CVE-2022-27943
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libjpeg-turbo8@2.1.5-2ubuntu2
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2018-10126         MEDIUM       6.5   1.8%   ·  ↳ S:UBUNTU-CVE-2018-10126
  │ ✘✔✔✘✘ CVE-2026-75466         MEDIUM       6.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-75466
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libk5crypto3@1.20.1-6ubuntu2.7
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-107778        HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-107778
  │ ✘✔✔✘✘ CVE-2026-107708        MEDIUM       6.9   0.5%   ·  ↳ S:UBUNTU-CVE-2026-107708
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libkrb5-3@1.20.1-6ubuntu2.7
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-107778        HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-107778
  │ ✘✔✔✘✘ CVE-2026-107708        MEDIUM       6.9   0.5%   ·  ↳ S:UBUNTU-CVE-2026-107708
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libkrb5support0@1.20.1-6ubuntu2.7
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-107778        HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-107778
  │ ✘✔✔✘✘ CVE-2026-107708        MEDIUM       6.9   0.5%   ·  ↳ S:UBUNTU-CVE-2026-107708
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/liblz4-1@1.9.4-1build1.1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-62813         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2025-62813
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/liblzma5@5.6.1%2Breally5.4.5-1ubuntu0.3
  │ OSGTV
  │ ✘✔✘✘✘ USN-8945-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libmount1@2.39.3-9ubuntu6.5
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-53612         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53612,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53613         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53613,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53614         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53614,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53615,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-76642
  │ ✘✔✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78408
  │ ✘✔✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78409
  │ ✘✔✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78410
  │ ✘✔✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-13595,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-27456         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-27456,USN-8702-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libncursesw6@6.4%2B20240113-1ubuntu2
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2025-69720         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-69720 | V:UB:CVE-2025-69720
  │ ✘✔✔✘✘ CVE-2025-6141          MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-6141,USN-8709-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libp11-kit0@0.25.3-4ubuntu2.1
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-13757         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-13757,USN-8687-1 | V:UB:CVE-2026-13757
  │ ✘✔✔✘✔ CVE-2026-18938         MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18938,USN-8687-1 | V:UB:CVE-2026-18938
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-modules@1.5.3-5ubuntu5.5
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-54411         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-54411,USN-8601-1 | V:UB:CVE-2026-54411
  │ ✘✔✔✘✘ CVE-2024-10041         MEDIUM       4.7   0.3%   ·  ↳ S:UBUNTU-CVE-2024-10041
  │ ✘✔✘✘✘ USN-8688-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-modules-bin@1.5.3-5ubuntu5.5
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-54411         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-54411,USN-8601-1
  │ ✘✔✔✘✘ CVE-2024-10041         MEDIUM       4.7   0.3%   ·  ↳ S:UBUNTU-CVE-2024-10041
  │ ✘✔✘✘✘ USN-8688-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-runtime@1.5.3-5ubuntu5.5
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-54411         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-54411,USN-8601-1
  │ ✘✔✔✘✘ CVE-2024-10041         MEDIUM       4.7   0.3%   ·  ↳ S:UBUNTU-CVE-2024-10041
  │ ✘✔✘✘✘ USN-8688-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam0g@1.5.3-5ubuntu5.5
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-54411         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-54411,USN-8601-1
  │ ✘✔✔✘✘ CVE-2024-10041         MEDIUM       4.7   0.3%   ·  ↳ S:UBUNTU-CVE-2024-10041
  │ ✘✔✘✘✘ USN-8688-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpcre2-8-0@10.42-4ubuntu2.1
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-103111        HIGH         7.6   0.3%   ·  ↳ S:UBUNTU-CVE-2026-103111 | V:UB:CVE-2026-103111
  │ ✘✔✔✘✔ CVE-2026-86145         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-86145 | V:UB:CVE-2026-86145
  │ ✘✔✔✘✔ CVE-2026-89157         HIGH         7.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89157 | V:UB:CVE-2026-89157
  │ ✘✔✔✘✔ CVE-2026-89161         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89161 | V:UB:CVE-2026-89161
  │ ✘✔✔✘✔ CVE-2026-89156         MEDIUM       5.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89156 | V:UB:CVE-2026-89156
  │ ✘✔✔✘✔ CVE-2026-89158         MEDIUM       6.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89158 | V:UB:CVE-2026-89158
  │ ✘✔✔✘✔ CVE-2026-89160         MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89160 | V:UB:CVE-2026-89160
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libperl5.38t64@5.38.2-3.2ubuntu0.3
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-12087         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-12087,USN-8684-1
  │ ✘✔✔✘✘ CVE-2026-13221         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-13221,USN-8684-1
  │ ✘✔✔✘✘ CVE-2026-57433         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-57433,USN-8684-1
  │ ✘✔✔✘✘ CVE-2026-48959         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-48959,USN-8684-1
  │ ✘✔✔✘✘ CVE-2026-48962         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-48962,USN-8684-1
  │ ✘✔✔✘✘ CVE-2026-57432         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57432,USN-8684-1
  │ ✘✔✔✘✘ CVE-2026-7017          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-7017,USN-8684-1
  │ ✘✔✔✘✘ CVE-2026-82560         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-82560
  │ ✘✔✔✘✘ CVE-2026-9538          HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-9538,USN-8684-1
  │ ✘✔✔✘✘ CVE-2025-15649         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-15649,USN-8684-1
  │ ✘✔✔✘✔ CVE-2026-15534         MEDIUM       5.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15534,USN-8736-2 | V:UB:CVE-2026-15534
  │ ✘✔✔✘✔ CVE-2026-19487         MEDIUM       5.3   0.4%   ·  ↳ S:UBUNTU-CVE-2026-19487,USN-8736-2 | V:UB:CVE-2026-19487
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpng16-16t64@1.6.43-5ubuntu0.6
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-46675         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2026-46675,USN-8899-1 | V:UB:CVE-2026-46675
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.12-dev@3.12.3-1ubuntu0.15
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-115557        CRITICAL     9.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-115557
  │ ✘✔✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19445
  │ ✘✔✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-11940
  │ ✘✔✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2026-11972
  │ ✘✔✔✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-15308,USN-8744-1
  │ ✘✔✔✘✘ CVE-2026-19553         HIGH         7.6   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19553
  │ ✘✔✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57178
  │ ✘✔✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-7210
  │ ✘✔✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-82049
  │ ✘✔✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-84366
  │ ✘✔✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.9%   ·  ↳ S:UBUNTU-CVE-2025-12781
  │ ✘✔✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15366
  │ ✘✔✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15367
  │ ✘✔✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-0864
  │ ✘✔✔✘✘ CVE-2026-114583        MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-114583
  │ ✘✔✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-12345
  │ ✘✔✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15806
  │ ✘✔✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·  ↳ S:UBUNTU-CVE-2026-17084
  │ ✘✔✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19672
  │ ✘✔✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3446
  │ ✘✔✔✘✘ CVE-2026-4360          MEDIUM       5.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-4360,USN-8744-1
  │ ✘✔✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57175
  │ ✘✔✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57176
  │ ✘✔✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57177
  │ ✘✔✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57179
  │ ✘✔✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-87910
  │ ✘✔✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15310
  │ ✘✔✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18503
  │ ✘✔✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-6879
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.12-minimal@3.12.3-1ubuntu0.15
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-115557        CRITICAL     9.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-115557
  │ ✘✔✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19445
  │ ✘✔✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-11940
  │ ✘✔✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2026-11972
  │ ✘✔✔✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-15308,USN-8744-1
  │ ✘✔✔✘✘ CVE-2026-19553         HIGH         7.6   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19553
  │ ✘✔✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57178
  │ ✘✔✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-7210
  │ ✘✔✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-82049
  │ ✘✔✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-84366
  │ ✘✔✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.9%   ·  ↳ S:UBUNTU-CVE-2025-12781
  │ ✘✔✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15366
  │ ✘✔✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15367
  │ ✘✔✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-0864
  │ ✘✔✔✘✘ CVE-2026-114583        MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-114583
  │ ✘✔✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-12345
  │ ✘✔✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15806
  │ ✘✔✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·  ↳ S:UBUNTU-CVE-2026-17084
  │ ✘✔✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19672
  │ ✘✔✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3446
  │ ✘✔✔✘✘ CVE-2026-4360          MEDIUM       5.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-4360,USN-8744-1
  │ ✘✔✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57175
  │ ✘✔✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57176
  │ ✘✔✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57177
  │ ✘✔✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57179
  │ ✘✔✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-87910
  │ ✘✔✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15310
  │ ✘✔✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18503
  │ ✘✔✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-6879
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.12-stdlib@3.12.3-1ubuntu0.15
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-115557        CRITICAL     9.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-115557
  │ ✘✔✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19445
  │ ✘✔✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-11940
  │ ✘✔✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2026-11972
  │ ✘✔✔✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-15308,USN-8744-1
  │ ✘✔✔✘✘ CVE-2026-19553         HIGH         7.6   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19553
  │ ✘✔✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57178
  │ ✘✔✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-7210
  │ ✘✔✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-82049
  │ ✘✔✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-84366
  │ ✘✔✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.9%   ·  ↳ S:UBUNTU-CVE-2025-12781
  │ ✘✔✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15366
  │ ✘✔✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15367
  │ ✘✔✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-0864
  │ ✘✔✔✘✘ CVE-2026-114583        MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-114583
  │ ✘✔✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-12345
  │ ✘✔✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15806
  │ ✘✔✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·  ↳ S:UBUNTU-CVE-2026-17084
  │ ✘✔✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19672
  │ ✘✔✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3446
  │ ✘✔✔✘✘ CVE-2026-4360          MEDIUM       5.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-4360,USN-8744-1
  │ ✘✔✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57175
  │ ✘✔✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57176
  │ ✘✔✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57177
  │ ✘✔✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57179
  │ ✘✔✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-87910
  │ ✘✔✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15310
  │ ✘✔✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18503
  │ ✘✔✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-6879
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.12t64@3.12.3-1ubuntu0.15
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-115557        CRITICAL     9.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-115557
  │ ✘✔✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19445
  │ ✘✔✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-11940
  │ ✘✔✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2026-11972
  │ ✘✔✔✘✔ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-15308,USN-8744-1 | V:UB:CVE-2026-15308
  │ ✘✔✔✘✘ CVE-2026-19553         HIGH         7.6   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19553
  │ ✘✔✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57178
  │ ✘✔✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-7210
  │ ✘✔✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-82049
  │ ✘✔✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-84366
  │ ✘✔✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.9%   ·  ↳ S:UBUNTU-CVE-2025-12781
  │ ✘✔✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15366
  │ ✘✔✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15367
  │ ✘✔✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-0864
  │ ✘✔✔✘✘ CVE-2026-114583        MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-114583
  │ ✘✔✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-12345
  │ ✘✔✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15806
  │ ✘✔✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·  ↳ S:UBUNTU-CVE-2026-17084
  │ ✘✔✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19672
  │ ✘✔✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3446
  │ ✘✔✔✘✔ CVE-2026-4360          MEDIUM       5.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-4360,USN-8744-1 | V:UB:CVE-2026-4360
  │ ✘✔✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57175
  │ ✘✔✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57176
  │ ✘✔✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57177
  │ ✘✔✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57179
  │ ✘✔✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-87910
  │ ✘✔✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15310
  │ ✘✔✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18503
  │ ✘✔✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-6879
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/librtmp1@2.4%2B20151223.gitfa8646d.1-2build7
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-112060        MEDIUM       6.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-112060
  │ ✘✔✔✘✘ CVE-2026-112061        MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-112061
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsasl2-2@2.1.28%2Bdfsg1-5ubuntu3.1
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-107161        HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-107161 | V:UB:CVE-2026-107161
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsasl2-modules@2.1.28%2Bdfsg1-5ubuntu3.1
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-107161        HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-107161 | V:UB:CVE-2026-107161
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsasl2-modules-db@2.1.28%2Bdfsg1-5ubuntu3.1
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-107161        HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-107161 | V:UB:CVE-2026-107161
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsframe1@2.42-4ubuntu2.10
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ S:UBUNTU-CVE-2017-13716 | V:UB:CVE-2017-13716
  │ ✘✔✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66862
  │ ✘✔✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66863
  │ ✘✔✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-66864
  │ ✘✔✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66865
  │ ✘✔✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-66866
  │ ✘✔✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3441
  │ ✘✔✔✘✘ CVE-2026-3442          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-3442
  │ ✘✔✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6846
  │ ✘✔✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11495
  │ ✘✔✔✘✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2025-69644 | V:UB:CVE-2025-69644
  │ ✘✔✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69645 | V:UB:CVE-2025-69645
  │ ✘✔✔✘✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69646 | V:UB:CVE-2025-69646
  │ ✘✔✔✘✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69647 | V:UB:CVE-2025-69647
  │ ✘✔✔✘✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69648 | V:UB:CVE-2025-69648
  │ ✘✔✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-69651 | V:UB:CVE-2025-69651
  │ ✘✔✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69652 | V:UB:CVE-2025-69652
  │ ✘✔✔✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15003
  │ ✘✔✔✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19548
  │ ✘✔✔✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-4647
  │ ✘✔✔✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6844
  │ ✘✔✔✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6845
  │ ✘✔✔✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90801
  │ ✘✔✔✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90802
  │ ✘✔✔✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90803
  │ ✘✔✔✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90804
  │ ✘✔✔✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90828
  │ ✘✔✔✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90829
  │ ✘✔✔✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90830
  │ ✘✔✔✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90831
  │ ✘✔✔✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91779
  │ ✘✔✔✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91780
  │ ✘✔✔✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91781
  │ ✘✔✔✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91782
  │ ✘✔✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1149
  │ ✘✔✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1150
  │ ✘✔✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1151
  │ ✘✔✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1152 | V:UB:CVE-2025-1152
  │ ✘✔✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-66861
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsmartcols1@2.39.3-9ubuntu6.5
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-53612         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53612,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53613         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53613,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53614         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53614,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53615,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-76642
  │ ✘✔✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78408
  │ ✘✔✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78409
  │ ✘✔✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78410
  │ ✘✔✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-13595,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-27456         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-27456,USN-8702-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsqlite3-0@3.45.1-1ubuntu2.7
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-39113         MEDIUM       4.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-39113,USN-8775-1 | V:UB:CVE-2026-39113
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libssh-4@0.10.6-2ubuntu0.4
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-59847         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-59847,USN-8699-1 | V:UB:CVE-2026-59847
  │ ✘✔✔✘✔ CVE-2026-59850         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-59850,USN-8699-1 | V:UB:CVE-2026-59850
  │ ✘✔✔✘✔ CVE-2026-59843         MEDIUM       6.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-59843,USN-8699-1 | V:UB:CVE-2026-59843
  │ ✘✔✔✘✔ CVE-2026-59845         MEDIUM       5.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-59845,USN-8699-1 | V:UB:CVE-2026-59845
  │ ✘✔✔✘✔ CVE-2026-59848         MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-59848,USN-8699-1 | V:UB:CVE-2026-59848
  │ ✘✔✔✘✔ CVE-2026-59846         LOW          3.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-59846,USN-8699-1 | V:UB:CVE-2026-59846
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libssl3t64@3.0.13-0ubuntu3.12
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-75803         CRITICAL     9.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-75803,USN-8678-1 | V:UB:CVE-2026-75803
  │ ✘✔✔✘✔ CVE-2026-54874         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-54874,USN-8678-1 | V:UB:CVE-2026-54874
  │ ✘✔✔✘✔ CVE-2026-63072         HIGH         7.5   0.9%   ·  ↳ S:UBUNTU-CVE-2026-63072,USN-8678-1 | V:UB:CVE-2026-63072
  │ ✘✔✔✘✔ CVE-2026-63076         HIGH         7.5   1.6%   ·  ↳ S:UBUNTU-CVE-2026-63076,USN-8678-1 | V:UB:CVE-2026-63076
  │ ✘✔✔✘✔ CVE-2026-84782         HIGH         8.2   0.8%   ·  ↳ S:UBUNTU-CVE-2026-84782,USN-8847-1 | V:UB:CVE-2026-84782
  │ ✘✔✔✘✔ CVE-2026-35189         MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-35189,USN-8847-1 | V:UB:CVE-2026-35189
  │ ✘✔✔✘✔ CVE-2026-63074         MEDIUM       5.9   0.6%   ·  ↳ S:UBUNTU-CVE-2026-63074,USN-8678-1 | V:UB:CVE-2026-63074
  │ ✘✔✔✘✔ CVE-2026-75805         MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-75805,USN-8847-1 | V:UB:CVE-2026-75805
  │ ✘✔✔✘✔ CVE-2026-75806         MEDIUM       5.3   1.1%   ·  ↳ S:UBUNTU-CVE-2026-75806,USN-8847-1 | V:UB:CVE-2026-75806
  │ ✘✔✔✘✔ CVE-2026-54872         LOW          3.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-54872,USN-8847-1 | V:UB:CVE-2026-54872
  │ ✘✔✔✘✔ CVE-2026-77696         LOW          3.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-77696,USN-8847-1 | V:UB:CVE-2026-77696
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libstdc%2B%2B-13-dev@13.3.0-6ubuntu2~24.04.1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsystemd0@255.4-1ubuntu8.16
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-15059         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15059
  │ ✘✔✔✘✘ CVE-2026-16742         MEDIUM       6.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-16742
  │ ✘✔✔✘✔ CVE-2026-40228         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-40228 | V:UB:CVE-2026-40228
  │ ✘✔✘✘✘ USN-8626-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libtiff6@4.5.1%2Bgit230720-4ubuntu2.5
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-12912         HIGH         7.3   0.4%   ·  ↳ S:UBUNTU-CVE-2026-12912
  │ ✘✔✔✘✘ CVE-2026-4775          HIGH         7.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-4775
  │ ✘✔✔✘✘ CVE-2026-18495         MEDIUM       6.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18495
  │ ✘✔✔✘✘ CVE-2026-36849         ?             -       -   ·  ↳ S:UBUNTU-CVE-2026-36849
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libtinfo6@6.4%2B20240113-1ubuntu2
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2025-69720         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-69720 | V:UB:CVE-2025-69720
  │ ✘✔✔✘✔ CVE-2025-6141          MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-6141,USN-8709-1 | V:UB:CVE-2025-6141
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libudev1@255.4-1ubuntu8.16
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-15059         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15059
  │ ✘✔✔✘✘ CVE-2026-16742         MEDIUM       6.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-16742
  │ ✘✔✔✘✔ CVE-2026-40228         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-40228 | V:UB:CVE-2026-40228
  │ ✘✔✘✘✘ USN-8626-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libuuid1@2.39.3-9ubuntu6.5
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-53612         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53612,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53613         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53613,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53614         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53614,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53615,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-76642
  │ ✘✔✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78408
  │ ✘✔✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78409
  │ ✘✔✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78410
  │ ✘✔✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-13595,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-27456         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-27456,USN-8702-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libx11-6@2%3A1.8.7-1build1
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-88806         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-88806,USN-8913-1 | V:UB:CVE-2026-88806
  │ ✘✔✔✘✔ CVE-2026-94283         MEDIUM       6.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-94283,USN-8913-1 | V:UB:CVE-2026-94283
  │ ✘✔✔✘✔ CVE-2026-94284         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-94284,USN-8913-1 | V:UB:CVE-2026-94284
  │ ✘✔✔✘✔ CVE-2026-94285         MEDIUM       5.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-94285,USN-8913-1 | V:UB:CVE-2026-94285
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libx11-data@2%3A1.8.7-1build1
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-88806         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-88806,USN-8913-1
  │ ✘✔✔✘✘ CVE-2026-94283         MEDIUM       6.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-94283,USN-8913-1
  │ ✘✔✔✘✘ CVE-2026-94284         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-94284,USN-8913-1
  │ ✘✔✔✘✘ CVE-2026-94285         MEDIUM       5.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-94285,USN-8913-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libxpm4@1%3A3.5.17-1ubuntu0.24.04.1
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-94287         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-94287,USN-8862-1 | V:UB:CVE-2026-94287
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/linux-libc-dev@6.8.0-136.136
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2021-3773          CRITICAL     9.8   5.3%   ·  ↳ S:UBUNTU-CVE-2021-3773
  │ ✘✔✘✘✘ CVE-2024-50106         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2024-50106
  │ ✘✔✘✘✘ CVE-2025-10263         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2025-10263,USN-8817-1
  │ ✘✔✘✘✘ CVE-2025-39933         CRITICAL     9.4   0.3%   ·  ↳ S:UBUNTU-CVE-2025-39933
  │ ✘✔✘✘✘ CVE-2025-40074         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-40074
  │ ✘✔✘✘✘ CVE-2025-68745         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-68745
  │ ✘✔✘✘✘ CVE-2026-100075        CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-100075
  │ ✘✔✘✘✘ CVE-2026-23240         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-23240
  │ ✘✔✘✘✘ CVE-2026-25702         CRITICAL     9.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-25702
  │ ✘✔✘✘✘ CVE-2026-31536         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-31536
  │ ✘✔✘✘✘ CVE-2026-43083         CRITICAL     9.1   0.6%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-43083,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-43197         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-43197,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-43198         CRITICAL     9.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-43198,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-43379         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-43379
  │ ✘✔✘✘✘ CVE-2026-43465         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-43465,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-46325         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-46325,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-52914         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-52914,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-52924         CRITICAL     9.8   0.7%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-52924,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-52931         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-52931,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-53131         CRITICAL     9.4   0.4%   ·  ↳ S:UBUNTU-CVE-2026-53131,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-53151         CRITICAL     9.8   0.7%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-53151,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-53176         CRITICAL     9.8   0.8%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-53176,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-53186         CRITICAL     9.1   0.5%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-53186,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-53215         CRITICAL     9.8   0.5%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-53215,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-53216         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53216,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-53221         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-53221,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-53224         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-53224,USN-8643-1
  │ ✘✔✘✘✘ CVE-2026-53225         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-53225,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-53228         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-53228,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-53246         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-53246,USN-8643-1
  │ ✘✔✘✘✘ CVE-2026-53247         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-53247,USN-8643-1
  │ ✘✔✘✘✘ CVE-2026-53355         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-53355,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-53384         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53384,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53398         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53398,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53399         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-53399,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63795         CRITICAL    10.0   0.6%   ·  ↳ S:UBUNTU-CVE-2026-63795,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63800         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-63800,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63808         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-63808,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63825         CRITICAL     9.8   0.9%   ·  ↳ S:UBUNTU-CVE-2026-63825
  │ ✘✔✘✘✘ CVE-2026-63830         CRITICAL     9.4   0.4%   ·  ↳ S:UBUNTU-CVE-2026-63830,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63886         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-63886,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-63887         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-63887,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-63888         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-63888,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-63912         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-63912,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-63922         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-63922,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-63924         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-63924,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-63940         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63940,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63978         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-63978
  │ ✘✔✘✘✘ CVE-2026-63979         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-63979
  │ ✘✔✘✘✘ CVE-2026-63984         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-63984,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-63992         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-63992,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-63993         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-63993,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-63994         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-63994,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-64000         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64000,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-64007         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64007,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-64018         CRITICAL     9.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64018,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64025         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64025,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64033         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64033,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64034         CRITICAL     9.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64034,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64046         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64046,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64047         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64047,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64055         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64055,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64056         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-64056,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64089         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-64089,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64091         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64091,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-64102         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64102,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64106         CRITICAL     9.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64106,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64113         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64113,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64125         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-64125,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64136         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64136,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64160         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64160
  │ ✘✔✘✘✘ CVE-2026-64268         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-64268,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64269         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-64269,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64303         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-64303,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64319         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-64319,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64320         CRITICAL     9.1   0.8%   ·  ↳ S:UBUNTU-CVE-2026-64320,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64355         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64355,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64383         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64383,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64384         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64384,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64385         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64385,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64386         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64386,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64387         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64387,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64391         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64391,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64392         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64392,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64393         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64393,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64397         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64397,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64399         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64399,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64450         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64450,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64523         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64523
  │ ✘✔✘✘✘ CVE-2026-64530         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-64530,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64534         CRITICAL     9.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64534,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64535         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64535,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64541         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-64541,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64551         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64551,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64564         CRITICAL     9.8   1.4%   ·  ↳ S:UBUNTU-CVE-2026-64564,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64597         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64597,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68082         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68082
  │ ✘✔✘✘✘ CVE-2026-68083         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68083,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68117         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68117,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68123         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-68123,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68124         CRITICAL     9.6   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68124,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68127         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68127,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68136         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68136,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68137         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68137,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68144         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68144,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68154         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68154,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68156         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68156,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68158         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68158,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68159         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68159
  │ ✘✔✘✘✘ CVE-2026-68160         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-68160,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68161         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68161,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68300         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-68300,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68302         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68302,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68343         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68343,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68381         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68381,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68388         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68388,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68426         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68426
  │ ✘✔✘✘✘ CVE-2026-68431         CRITICAL     9.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68431
  │ ✘✔✘✘✘ CVE-2026-68457         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68457,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68476         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68476,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68477         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68477,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72014         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72014,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72020         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72020,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72033         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-72033,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72041         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72041,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72065         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72065,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72069         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72069,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72083         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72083,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72084         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72084,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72085         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72085,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72098         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72098
  │ ✘✔✘✘✘ CVE-2026-72129         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72129,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72130         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-72130,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72191         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72191,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72192         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72192,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72194         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-72194,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72200         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72200
  │ ✘✔✘✘✘ CVE-2026-72217         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72217,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72221         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72221,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72222         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72222,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72226         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-72226,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72234         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72234,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72251         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72251,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72288         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72288
  │ ✘✔✘✘✘ CVE-2026-72289         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72289,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72296         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72296,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72299         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72299,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72317         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72317,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72318         CRITICAL     9.4   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72318,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72319         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72319,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72320         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72320,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72322         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72322,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72323         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72323,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72329         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72329
  │ ✘✔✘✘✘ CVE-2026-72339         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72339,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72348         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72348,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72351         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72351,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72398         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-72398
  │ ✘✔✘✘✘ CVE-2026-72399         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72399,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72421         CRITICAL    10.0   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72421,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72422         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72422,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72436         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72436,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72451         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72451,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72463         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-72463
  │ ✘✔✘✘✘ CVE-2026-72466         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72466,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72472         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72472
  │ ✘✔✘✘✘ CVE-2026-72473         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72473,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72491         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72491,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72493         CRITICAL     9.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-72493
  │ ✘✔✘✘✘ CVE-2026-72494         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72494
  │ ✘✔✘✘✘ CVE-2026-72495         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72495
  │ ✘✔✘✘✘ CVE-2026-72496         CRITICAL     9.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-72496
  │ ✘✔✘✘✘ CVE-2026-74255         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74255,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74267         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-74267,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74268         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-74268
  │ ✘✔✘✘✘ CVE-2026-74269         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-74269
  │ ✘✔✘✘✘ CVE-2026-74279         CRITICAL    10.0   0.8%   ·  ↳ S:UBUNTU-CVE-2026-74279,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74280         CRITICAL    10.0   0.8%   ·  ↳ S:UBUNTU-CVE-2026-74280,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74287         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-74287,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74310         CRITICAL     9.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74310,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74345         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74345,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74350         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-74350
  │ ✘✔✘✘✘ CVE-2026-74376         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74376,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74384         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74384,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74394         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74394,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74398         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74398,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74401         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-74401,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74406         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74406,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74427         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-74427,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74436         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74436,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74439         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74439,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74473         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74473
  │ ✘✔✘✘✘ CVE-2026-74474         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74474
  │ ✘✔✘✘✘ CVE-2026-74475         CRITICAL    10.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74475
  │ ✘✔✘✘✘ CVE-2026-74476         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74476
  │ ✘✔✘✘✘ CVE-2026-74478         CRITICAL     9.8   0.9%   ·  ↳ S:UBUNTU-CVE-2026-74478
  │ ✘✔✘✘✘ CVE-2026-74480         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-74480
  │ ✘✔✘✘✘ CVE-2026-74493         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74493
  │ ✘✔✘✘✘ CVE-2026-74495         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74495
  │ ✘✔✘✘✘ CVE-2026-74521         CRITICAL     9.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74521
  │ ✘✔✘✘✘ CVE-2026-74556         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74556
  │ ✘✔✘✘✘ CVE-2026-74569         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74569
  │ ✘✔✘✘✘ CVE-2026-74581         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74581
  │ ✘✔✘✘✘ CVE-2026-74586         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74586
  │ ✘✔✘✘✘ CVE-2026-74587         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74587
  │ ✘✔✘✘✘ CVE-2026-74588         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74588
  │ ✘✔✘✘✘ CVE-2026-74597         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74597
  │ ✘✔✘✘✘ CVE-2026-74608         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74608
  │ ✘✔✘✘✘ CVE-2026-74611         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74611
  │ ✘✔✘✘✘ CVE-2026-74612         CRITICAL    10.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74612
  │ ✘✔✘✘✘ CVE-2026-74616         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74616
  │ ✘✔✘✘✘ CVE-2026-74628         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74628
  │ ✘✔✘✘✘ CVE-2026-74662         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74662
  │ ✘✔✘✘✘ CVE-2026-74669         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74669
  │ ✘✔✘✘✘ CVE-2026-74688         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74688
  │ ✘✔✘✘✘ CVE-2026-74705         CRITICAL    10.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74705
  │ ✘✔✘✘✘ CVE-2026-74723         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74723
  │ ✘✔✘✘✘ CVE-2026-74730         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74730
  │ ✘✔✘✘✘ CVE-2026-74737         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-74737
  │ ✘✔✘✘✘ CVE-2026-74743         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74743
  │ ✘✔✘✘✘ CVE-2026-74744         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74744
  │ ✘✔✘✘✘ CVE-2026-74746         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74746
  │ ✘✔✘✘✘ CVE-2026-74752         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74752
  │ ✘✔✘✘✘ CVE-2026-80528         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-80528
  │ ✘✔✘✘✘ CVE-2026-80551         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80551
  │ ✘✔✘✘✘ CVE-2026-80554         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80554
  │ ✘✔✘✘✘ CVE-2026-80557         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-80557
  │ ✘✔✘✘✘ CVE-2026-80558         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-80558
  │ ✘✔✘✘✘ CVE-2026-80561         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-80561
  │ ✘✔✘✘✘ CVE-2026-80585         CRITICAL     9.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-80585
  │ ✘✔✘✘✘ CVE-2026-80586         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80586
  │ ✘✔✘✘✘ CVE-2026-80587         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80587
  │ ✘✔✘✘✘ CVE-2026-80589         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80589
  │ ✘✔✘✘✘ CVE-2026-80600         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-80600,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80603         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-80603,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80609         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-80609,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80630         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-80630,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80634         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-80634
  │ ✘✔✘✘✘ CVE-2026-80668         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-80668
  │ ✘✔✘✘✘ CVE-2026-80670         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-80670
  │ ✘✔✘✘✘ CVE-2026-80671         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80671
  │ ✘✔✘✘✘ CVE-2026-80681         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-80681
  │ ✘✔✘✘✘ CVE-2026-80684         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80684
  │ ✘✔✘✘✘ CVE-2026-80693         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80693
  │ ✘✔✘✘✘ CVE-2026-80694         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-80694
  │ ✘✔✘✘✘ CVE-2026-80714         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-80714
  │ ✘✔✘✘✘ CVE-2026-80725         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-80725
  │ ✘✔✘✘✘ CVE-2026-80945         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-80945
  │ ✘✔✘✘✘ CVE-2026-80976         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-80976
  │ ✘✔✘✘✘ CVE-2026-80980         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-80980
  │ ✘✔✘✘✘ CVE-2026-81002         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-81002
  │ ✘✔✘✘✘ CVE-2026-89448         CRITICAL     9.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89448
  │ ✘✔✘✘✘ CVE-2026-89478         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89478
  │ ✘✔✘✘✘ CVE-2026-89479         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89479
  │ ✘✔✘✘✘ CVE-2026-89482         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89482
  │ ✘✔✘✘✘ CVE-2026-89485         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89485
  │ ✘✔✘✘✘ CVE-2026-89492         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89492
  │ ✘✔✘✘✘ CVE-2026-89494         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89494
  │ ✘✔✘✘✘ CVE-2026-89495         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89495
  │ ✘✔✘✘✘ CVE-2026-89526         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89526
  │ ✘✔✘✘✘ CVE-2026-89530         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89530
  │ ✘✔✘✘✘ CVE-2026-89532         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89532
  │ ✘✔✘✘✘ CVE-2026-89533         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89533
  │ ✘✔✘✘✘ CVE-2026-89536         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89536
  │ ✘✔✘✘✘ CVE-2026-89537         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89537
  │ ✘✔✘✘✘ CVE-2026-89538         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89538
  │ ✘✔✘✘✘ CVE-2026-89541         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89541
  │ ✘✔✘✘✘ CVE-2026-89542         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89542
  │ ✘✔✘✘✘ CVE-2026-89550         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89550
  │ ✘✔✘✘✘ CVE-2026-89551         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89551
  │ ✘✔✘✘✘ CVE-2026-89555         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89555
  │ ✘✔✘✘✘ CVE-2026-89631         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89631
  │ ✘✔✘✘✘ CVE-2026-89633         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89633
  │ ✘✔✘✘✘ CVE-2026-89634         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89634
  │ ✘✔✘✘✘ CVE-2026-89636         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89636
  │ ✘✔✘✘✘ CVE-2026-89637         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89637
  │ ✘✔✘✘✘ CVE-2026-89643         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89643
  │ ✘✔✘✘✘ CVE-2026-89649         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89649
  │ ✘✔✘✘✘ CVE-2026-89650         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89650
  │ ✘✔✘✘✘ CVE-2026-89652         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89652
  │ ✘✔✘✘✘ CVE-2026-89653         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89653
  │ ✘✔✘✘✘ CVE-2026-89654         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89654
  │ ✘✔✘✘✘ CVE-2026-89655         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89655
  │ ✘✔✘✘✘ CVE-2026-89656         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89656
  │ ✘✔✘✘✘ CVE-2026-89659         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89659
  │ ✘✔✘✘✘ CVE-2026-89662         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89662
  │ ✘✔✘✘✘ CVE-2026-89669         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89669
  │ ✘✔✘✘✘ CVE-2026-89671         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89671
  │ ✘✔✘✘✘ CVE-2026-89672         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89672
  │ ✘✔✘✘✘ CVE-2026-89674         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89674
  │ ✘✔✘✘✘ CVE-2026-89675         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89675
  │ ✘✔✘✘✘ CVE-2026-89676         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89676
  │ ✘✔✘✘✘ CVE-2026-89686         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89686
  │ ✘✔✘✘✘ CVE-2026-89697         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89697
  │ ✘✔✘✘✘ CVE-2026-89702         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89702
  │ ✘✔✘✘✘ CVE-2026-89708         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89708
  │ ✘✔✘✘✘ CVE-2026-89712         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89712
  │ ✘✔✘✘✘ CVE-2026-89713         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89713
  │ ✘✔✘✘✘ CVE-2026-89778         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89778
  │ ✘✔✘✘✘ CVE-2026-89779         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89779
  │ ✘✔✘✘✘ CVE-2026-89783         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89783
  │ ✘✔✘✘✘ CVE-2026-89786         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89786
  │ ✘✔✘✘✘ CVE-2026-89788         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89788
  │ ✘✔✘✘✘ CVE-2026-89846         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89846
  │ ✘✔✘✘✘ CVE-2026-89847         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89847
  │ ✘✔✘✘✘ CVE-2026-89857         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89857
  │ ✘✔✘✘✘ CVE-2026-89930         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89930
  │ ✘✔✘✘✘ CVE-2026-89969         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89969
  │ ✘✔✘✘✘ CVE-2026-89970         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-89970
  │ ✘✔✘✘✘ CVE-2026-89972         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89972
  │ ✘✔✘✘✘ CVE-2026-90011         CRITICAL     9.1   0.8%   ·  ↳ S:UBUNTU-CVE-2026-90011
  │ ✘✔✘✘✘ CVE-2026-90036         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-90036
  │ ✘✔✘✘✘ CVE-2026-90037         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-90037
  │ ✘✔✘✘✘ CVE-2026-90042         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-90042
  │ ✘✔✘✘✘ CVE-2026-90048         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90048
  │ ✘✔✘✘✘ CVE-2026-90049         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90049
  │ ✘✔✘✘✘ CVE-2026-90104         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90104
  │ ✘✔✘✘✘ CVE-2026-90110         CRITICAL     9.4   0.6%   ·  ↳ S:UBUNTU-CVE-2026-90110
  │ ✘✔✘✘✘ CVE-2026-90151         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90151
  │ ✘✔✘✘✘ CVE-2026-90230         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-90230
  │ ✘✔✘✘✘ CVE-2026-90235         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90235
  │ ✘✔✘✘✘ CVE-2026-90413         CRITICAL     9.1   0.8%   ·  ↳ S:UBUNTU-CVE-2026-90413
  │ ✘✔✘✘✘ CVE-2026-90414         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-90414
  │ ✘✔✘✘✘ CVE-2026-92489         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-92489
  │ ✘✔✘✘✘ CVE-2026-93207         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-93207
  │ ✘✔✘✘✘ CVE-2026-93228         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-93228
  │ ✘✔✘✘✘ CVE-2026-97413         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-97413
  │ ✘✔✘✘✘ CVE-2026-98323         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-98323
  │ ✘✔✘✘✘ CVE-2026-98365         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-98365
  │ ✘✔✘✘✘ CVE-2026-98432         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-98432
  │ ✘✔✘✘✘ CVE-2026-98464         CRITICAL     9.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98464
  │ ✘✔✘✘✘ CVE-2026-98490         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-98490
  │ ✘✔✘✘✘ CVE-2026-98548         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-98548
  │ ✘✔✘✘✘ CVE-2026-98549         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-98549
  │ ✘✔✘✘✘ CVE-2026-98959         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-98959
  │ ✘✔✘✘✘ CVE-2026-99078         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-99078
  │ ✘✔✘✘✘ CVE-2026-99079         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-99079
  │ ✘✔✘✘✘ CVE-2026-99153         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-99153
  │ ✘✔✘✘✘ CVE-2026-99154         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-99154
  │ ✘✔✘✘✘ CVE-2026-99999         CRITICAL     9.3   0.8% KEV  ↳ S:UBUNTU-CVE-2026-99999
  │ ✘✔✘✘✘ CVE-2013-7445          HIGH         7.8   2.8%   ·  ↳ S:UBUNTU-CVE-2013-7445
  │ ✘✔✘✘✘ CVE-2017-13165         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2017-13165
  │ ✘✔✘✘✘ CVE-2018-12930         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2018-12930
  │ ✘✔✘✘✘ CVE-2018-12931         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2018-12931
  │ ✘✔✘✘✘ CVE-2019-14899         HIGH         7.4   0.8%   ·  ↳ S:UBUNTU-CVE-2019-14899
  │ ✘✔✘✘✘ CVE-2019-15794         HIGH         7.2   1.2%   ·  ↳ S:UBUNTU-CVE-2019-15794
  │ ✘✔✘✘✘ CVE-2019-19378         HIGH         7.8   2.3%   ·  ↳ S:UBUNTU-CVE-2019-19378
  │ ✘✔✘✘✘ CVE-2019-19814         HIGH         9.3   3.3%   ·  ↳ S:UBUNTU-CVE-2019-19814
  │ ✘✔✘✘✘ CVE-2019-20426         HIGH         7.8   1.9%   ·  ↳ S:UBUNTU-CVE-2019-20426
  │ ✘✔✘✘✘ CVE-2020-14356         HIGH         7.8   1.0%   ·  ↳ S:UBUNTU-CVE-2020-14356
  │ ✘✔✘✘✘ CVE-2020-26556         HIGH         7.5   0.9%   ·  ↳ S:UBUNTU-CVE-2020-26556
  │ ✘✔✘✘✘ CVE-2020-26557         HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2020-26557
  │ ✘✔✘✘✘ CVE-2020-26559         HIGH         8.8   0.9%   ·  ↳ S:UBUNTU-CVE-2020-26559
  │ ✘✔✘✘✘ CVE-2020-26560         HIGH         8.1   0.9%   ·  ↳ S:UBUNTU-CVE-2020-26560
  │ ✘✔✘✘✘ CVE-2021-26934         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2021-26934
  │ ✘✔✘✘✘ CVE-2021-3864          HIGH         7.0   0.8%   ·  ↳ S:UBUNTU-CVE-2021-3864
  │ ✘✔✘✘✘ CVE-2022-0400          HIGH         7.5   1.9%   ·  ↳ S:UBUNTU-CVE-2022-0400
  │ ✘✔✘✘✘ CVE-2022-1247          HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2022-1247
  │ ✘✔✘✘✘ CVE-2022-25265         HIGH         7.8   1.1%   ·  ↳ S:UBUNTU-CVE-2022-25265
  │ ✘✔✘✘✘ CVE-2022-25836         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2022-25836
  │ ✘✔✘✘✘ CVE-2022-25837         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2022-25837
  │ ✘✔✘✘✘ CVE-2022-2961          HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2022-2961
  │ ✘✔✘✘✘ CVE-2022-3238          HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-3238
  │ ✘✔✘✘✘ CVE-2022-45885         HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2022-45885
  │ ✘✔✘✘✘ CVE-2022-50090         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50090
  │ ✘✔✘✘✘ CVE-2022-50240         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50240
  │ ✘✔✘✘✘ CVE-2022-50551         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50551
  │ ✘✔✘✘✘ CVE-2023-0030          HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-0030
  │ ✘✔✘✘✘ CVE-2023-26242         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-26242
  │ ✘✔✘✘✘ CVE-2023-33053         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2023-33053
  │ ✘✔✘✘✘ CVE-2023-3397          HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-3397
  │ ✘✔✘✘✘ CVE-2023-3640          HIGH         7.8   0.8%   ·  ↳ S:UBUNTU-CVE-2023-3640
  │ ✘✔✘✘✘ CVE-2023-52879         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52879
  │ ✘✔✘✘✘ CVE-2023-54187         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54187
  │ ✘✔✘✘✘ CVE-2024-14040         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-14040
  │ ✘✔✘✘✘ CVE-2024-25743         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2024-25743
  │ ✘✔✘✘✘ CVE-2024-27022         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-27022
  │ ✘✔✘✘✘ CVE-2024-35948         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35948
  │ ✘✔✘✘✘ CVE-2024-38581         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-38581
  │ ✘✔✘✘✘ CVE-2024-40954         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-40954
  │ ✘✔✘✘✘ CVE-2024-41008         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-41008
  │ ✘✔✘✘✘ CVE-2024-43872         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2024-43872
  │ ✘✔✘✘✘ CVE-2024-44932         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-44932
  │ ✘✔✘✘✘ CVE-2024-44951         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-44951
  │ ✘✔✘✘✘ CVE-2024-44964         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-44964
  │ ✘✔✘✘✘ CVE-2024-49932         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49932
  │ ✘✔✘✘✘ CVE-2024-49940         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-49940
  │ ✘✔✘✘✘ CVE-2024-50217         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-50217
  │ ✘✔✘✘✘ CVE-2024-52560         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-52560
  │ ✘✔✘✘✘ CVE-2024-53098         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53098
  │ ✘✔✘✘✘ CVE-2024-53207         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53207
  │ ✘✔✘✘✘ CVE-2024-53216         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53216
  │ ✘✔✘✘✘ CVE-2024-56552         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2024-56552,USN-8917-1
  │ ✘✔✘✘✘ CVE-2024-56591         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-56591
  │ ✘✔✘✘✘ CVE-2024-57857         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-57857
  │ ✘✔✘✘✘ CVE-2024-57976         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-57976
  │ ✘✔✘✘✘ CVE-2024-58015         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2024-58015
  │ ✘✔✘✘✘ CVE-2024-58089         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-58089
  │ ✘✔✘✘✘ CVE-2024-58094         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-58094
  │ ✘✔✘✘✘ CVE-2024-58098         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-58098
  │ ✘✔✘✘✘ CVE-2024-58100         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-58100
  │ ✘✔✘✘✘ CVE-2024-58241         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2024-58241
  │ ✘✔✘✘✘ CVE-2025-1272          HIGH         7.7   0.3%   ·  ↳ S:UBUNTU-CVE-2025-1272
  │ ✘✔✘✘✘ CVE-2025-21687         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21687,USN-8917-1
  │ ✘✔✘✘✘ CVE-2025-21693         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21693
  │ ✘✔✘✘✘ CVE-2025-21984         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-21984
  │ ✘✔✘✘✘ CVE-2025-21985         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21985,USN-8917-1
  │ ✘✔✘✘✘ CVE-2025-22043         HIGH         8.1   0.5%   ·  ↳ S:UBUNTU-CVE-2025-22043
  │ ✘✔✘✘✘ CVE-2025-22104         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22104
  │ ✘✔✘✘✘ CVE-2025-22108         HIGH         8.6   0.4%   ·  ↳ S:UBUNTU-CVE-2025-22108
  │ ✘✔✘✘✘ CVE-2025-22109         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-22109
  │ ✘✔✘✘✘ CVE-2025-23132         HIGH         7.0   0.4%   ·  ↳ S:UBUNTU-CVE-2025-23132
  │ ✘✔✘✘✘ CVE-2025-37776         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2025-37776
  │ ✘✔✘✘✘ CVE-2025-37876         HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37876
  │ ✘✔✘✘✘ CVE-2025-37906         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37906
  │ ✘✔✘✘✘ CVE-2025-38064         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-38064
  │ ✘✔✘✘✘ CVE-2025-38069         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38069,USN-8917-1
  │ ✘✔✘✘✘ CVE-2025-38187         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38187,USN-8917-1
  │ ✘✔✘✘✘ CVE-2025-38189         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38189
  │ ✘✔✘✘✘ CVE-2025-38204         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38204
  │ ✘✔✘✘✘ CVE-2025-38206         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38206
  │ ✘✔✘✘✘ CVE-2025-38242         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-38242
  │ ✘✔✘✘✘ CVE-2025-38261         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38261
  │ ✘✔✘✘✘ CVE-2025-38372         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38372
  │ ✘✔✘✘✘ CVE-2025-38421         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38421
  │ ✘✔✘✘✘ CVE-2025-38498         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38498
  │ ✘✔✘✘✘ CVE-2025-38525         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-38525
  │ ✘✔✘✘✘ CVE-2025-38563         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2025-38563,USN-8917-1
  │ ✘✔✘✘✘ CVE-2025-38565         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38565,USN-8917-1
  │ ✘✔✘✘✘ CVE-2025-38636         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38636
  │ ✘✔✘✘✘ CVE-2025-38717         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-38717
  │ ✘✔✘✘✘ CVE-2025-39677         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39677
  │ ✘✔✘✘✘ CVE-2025-39789         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39789
  │ ✘✔✘✘✘ CVE-2025-39859         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39859
  │ ✘✔✘✘✘ CVE-2025-39862         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-39862
  │ ✘✔✘✘✘ CVE-2025-39896         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39896
  │ ✘✔✘✘✘ CVE-2025-39958         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39958
  │ ✘✔✘✘✘ CVE-2025-39990         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39990
  │ ✘✔✘✘✘ CVE-2025-40014         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40014,USN-8917-1
  │ ✘✔✘✘✘ CVE-2025-40025         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40025
  │ ✘✔✘✘✘ CVE-2025-40040         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2025-40040
  │ ✘✔✘✘✘ CVE-2025-40054         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40054
  │ ✘✔✘✘✘ CVE-2025-40064         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40064
  │ ✘✔✘✘✘ CVE-2025-40075         HIGH         8.1   0.5%   ·  ↳ S:UBUNTU-CVE-2025-40075
  │ ✘✔✘✘✘ CVE-2025-40139         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40139
  │ ✘✔✘✘✘ CVE-2025-40158         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-40158
  │ ✘✔✘✘✘ CVE-2025-40168         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2025-40168
  │ ✘✔✘✘✘ CVE-2025-40170         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40170
  │ ✘✔✘✘✘ CVE-2025-40190         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40190
  │ ✘✔✘✘✘ CVE-2025-40203         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40203
  │ ✘✔✘✘✘ CVE-2025-40274         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40274
  │ ✘✔✘✘✘ CVE-2025-40344         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40344
  │ ✘✔✘✘✘ CVE-2025-40354         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40354
  │ ✘✔✘✘✘ CVE-2025-68174         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68174
  │ ✘✔✘✘✘ CVE-2025-68212         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-68212
  │ ✘✔✘✘✘ CVE-2025-68304         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68304
  │ ✘✔✘✘✘ CVE-2025-68360         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2025-68360
  │ ✘✔✘✘✘ CVE-2025-68730         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68730
  │ ✘✔✘✘✘ CVE-2025-68822         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68822
  │ ✘✔✘✘✘ CVE-2025-71073         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71073
  │ ✘✔✘✘✘ CVE-2025-71074         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71074
  │ ✘✔✘✘✘ CVE-2025-71080         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-71080
  │ ✘✔✘✘✘ CVE-2025-71202         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71202
  │ ✘✔✘✘✘ CVE-2025-71289         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2025-71289,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-100072        HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-100072
  │ ✘✔✘✘✘ CVE-2026-23208         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23208
  │ ✘✔✘✘✘ CVE-2026-23239         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23239
  │ ✘✔✘✘✘ CVE-2026-23327         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23327
  │ ✘✔✘✘✘ CVE-2026-23393         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23393
  │ ✘✔✘✘✘ CVE-2026-23459         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-23459
  │ ✘✔✘✘✘ CVE-2026-31479         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31479
  │ ✘✔✘✘✘ CVE-2026-31486         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31486,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-31493         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31493
  │ ✘✔✘✘✘ CVE-2026-31568         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31568
  │ ✘✔✘✘✘ CVE-2026-31630         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31630
  │ ✘✔✘✘✘ CVE-2026-31663         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31663,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-31771         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-31771
  │ ✘✔✘✘✘ CVE-2026-43009         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43009
  │ ✘✔✘✘✘ CVE-2026-43029         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-43029
  │ ✘✔✘✘✘ CVE-2026-43042         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43042
  │ ✘✔✘✘✘ CVE-2026-43048         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-43048
  │ ✘✔✘✘✘ CVE-2026-43101         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-43101
  │ ✘✔✘✘✘ CVE-2026-43116         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43116,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-43126         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43126
  │ ✘✔✘✘✘ CVE-2026-43172         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-43172
  │ ✘✔✘✘✘ CVE-2026-43213         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-43213
  │ ✘✔✘✘✘ CVE-2026-43263         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43263
  │ ✘✔✘✘✘ CVE-2026-43303         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43303,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-43352         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43352
  │ ✘✔✘✘✘ CVE-2026-43353         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43353
  │ ✘✔✘✘✘ CVE-2026-43464         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-43464
  │ ✘✔✘✘✘ CVE-2026-45894         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45894
  │ ✘✔✘✘✘ CVE-2026-45932         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45932
  │ ✘✔✘✘✘ CVE-2026-45944         HIGH         7.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45944,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-46054         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46054
  │ ✘✔✘✘✘ CVE-2026-46130         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46130
  │ ✘✔✘✘✘ CVE-2026-46140         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46140,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-46175         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46175
  │ ✘✔✘✘✘ CVE-2026-46181         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46181
  │ ✘✔✘✘✘ CVE-2026-46203         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46203,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-46242         HIGH         7.8   4.4%   ·  ↳ S:UBUNTU-CVE-2026-46242,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-46275         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-46275,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-46320         HIGH         7.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-46320,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-46321         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46321,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-46322         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46322,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-46324         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46324
  │ ✘✔✘✘✘ CVE-2026-46330         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-46330
  │ ✘✔✘✘✘ CVE-2026-46331         HIGH         7.8   0.6% KEV  ↳ S:UBUNTU-CVE-2026-46331,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-52908         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52908,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-52909         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52909,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-52910         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52910,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-52912         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-52912,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-52915         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52915,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-52917         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52917,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-52918         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-52918,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-52919         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52919,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-52922         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-52922,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-52923         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-52923,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-52927         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52927,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-52929         HIGH         7.5   0.9%   ·  ↳ S:UBUNTU-CVE-2026-52929,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-52934         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-52934,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-52935         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52935,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-52942         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52942,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-52943         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-52943,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-52946         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-52946
  │ ✘✔✘✘✘ CVE-2026-52947         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52947,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-52953         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52953
  │ ✘✔✘✘✘ CVE-2026-52956         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-52956
  │ ✘✔✘✘✘ CVE-2026-52988         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52988
  │ ✘✔✘✘✘ CVE-2026-52991         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52991
  │ ✘✔✘✘✘ CVE-2026-53000         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53000
  │ ✘✔✘✘✘ CVE-2026-53005         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53005,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53009         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53009
  │ ✘✔✘✘✘ CVE-2026-53024         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53024
  │ ✘✔✘✘✘ CVE-2026-53025         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53025
  │ ✘✔✘✘✘ CVE-2026-53053         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53053
  │ ✘✔✘✘✘ CVE-2026-53070         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53070,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53078         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53078,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53089         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53089
  │ ✘✔✘✘✘ CVE-2026-53090         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53090,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53091         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53091
  │ ✘✔✘✘✘ CVE-2026-53109         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53109
  │ ✘✔✘✘✘ CVE-2026-53118         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53118
  │ ✘✔✘✘✘ CVE-2026-53120         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53120
  │ ✘✔✘✘✘ CVE-2026-53129         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53129
  │ ✘✔✘✘✘ CVE-2026-53132         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53132,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53133         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53133,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53136         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53136,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53137         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53137,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53138         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53138,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53143         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53143,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53146         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53146,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53147         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53147,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53148         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53148,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53149         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53149,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53156         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53156,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53157         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53157,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53159         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53159,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53160         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53160,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53161         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53161,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53178         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-53178
  │ ✘✔✘✘✘ CVE-2026-53179         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53179
  │ ✘✔✘✘✘ CVE-2026-53182         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53182,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53183         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53183,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53184         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53184,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53185         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53185,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53189         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53189
  │ ✘✔✘✘✘ CVE-2026-53194         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53194,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53195         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53195,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53198         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-53198,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53199         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53199,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53202         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53202,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53205         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53205,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53209         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53209,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53212         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-53212,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-53217         HIGH         8.6   0.4%   ·  ↳ S:UBUNTU-CVE-2026-53217,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53223         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53223,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53229         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53229,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53230         HIGH         8.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53230,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53232         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53232,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53239         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53239,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53242         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53242,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53250         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53250
  │ ✘✔✘✘✘ CVE-2026-53253         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53253,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53254         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53254,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53255         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53255,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53256         HIGH         8.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53256,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53262         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53262,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53264         HIGH         7.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53264,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53265         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53265,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53266         HIGH         8.8   0.9% KEV  ↳ S:UBUNTU-CVE-2026-53266,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53267         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53267,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53268         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53268,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53270         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53270,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53272         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53272
  │ ✘✔✘✘✘ CVE-2026-53273         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53273,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53275         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53275,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53281         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53281
  │ ✘✔✘✘✘ CVE-2026-53284         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53284
  │ ✘✔✘✘✘ CVE-2026-53329         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53329,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53330         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53330
  │ ✘✔✘✘✘ CVE-2026-53354         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53354,USN-8817-1
  │ ✘✔✘✘✘ CVE-2026-53356         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53356,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53357         HIGH         8.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53357,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-53358         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53358,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53359         HIGH         8.8   1.4%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-53359,USN-8630-1
  │ ✘✔✘✘✘ CVE-2026-53361         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53361,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53362         HIGH         7.8   0.7% KEV  ↳ S:UBUNTU-CVE-2026-53362,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53365         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53365,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53366         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53366,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53368         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53368
  │ ✘✔✘✘✘ CVE-2026-53381         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53381,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53383         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-53383,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53387         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53387,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53388         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53388,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53389         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53389,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53390         HIGH         8.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53390,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53391         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53391,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53392         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53392,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53397         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53397,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53400         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53400,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53401         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53401
  │ ✘✔✘✘✘ CVE-2026-53402         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53402,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63794         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63794,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63796         HIGH         8.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-63796,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63797         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63797,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63801         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-63801,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63802         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63802,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63803         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63803,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63804         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63804,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63805         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63805
  │ ✘✔✘✘✘ CVE-2026-63806         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63806,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63807         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63807,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63809         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63809,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63812         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63812,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63814         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63814,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63815         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63815,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63816         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63816,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63817         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63817,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63818         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63818,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63819         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63819
  │ ✘✔✘✘✘ CVE-2026-63823         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63823,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63824         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63824,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63827         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63827,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63828         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63828,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63829         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63829,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63831         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-63831,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63833         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63833,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63853         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63853
  │ ✘✔✘✘✘ CVE-2026-63858         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63858
  │ ✘✔✘✘✘ CVE-2026-63867         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-63867,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63869         HIGH         7.6   0.3%   ·  ↳ S:UBUNTU-CVE-2026-63869,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63870         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63870,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63875         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63875,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63879         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63879
  │ ✘✔✘✘✘ CVE-2026-63881         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63881,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63883         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63883,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63884         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63884,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63889         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-63889,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63893         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-63893,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63898         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63898,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63899         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63899,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63901         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63901,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63902         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63902,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63903         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63903,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63904         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63904,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63905         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63905,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63906         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63906,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63909         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-63909,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63913         HIGH         8.2   1.0%   ·  ↳ S:UBUNTU-CVE-2026-63913,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63914         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63914,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63915         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-63915,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63916         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-63916,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63917         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63917,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63919         HIGH         8.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-63919,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63920         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63920,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63921         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63921,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63925         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-63925,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63926         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63926,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63927         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63927,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63928         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63928,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63930         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63930,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63934         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63934,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63942         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63942,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63943         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63943,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63944         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-63944,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63945         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63945,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63946         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-63946,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63947         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-63947,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63949         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63949,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63952         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63952,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63954         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63954,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63956         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63956,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63957         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63957,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63967         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63967,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63968         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-63968,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63970         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63970,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63971         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63971,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63974         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-63974,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63975         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-63975,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63976         HIGH         8.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-63976,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63980         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-63980,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63985         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63985,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64001         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64001,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64002         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64002,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64003         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64003,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64004         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64004,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64005         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64005,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64009         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64009,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64010         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64010,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64011         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64011,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64014         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64014,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64015         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64015,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64017         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64017
  │ ✘✔✘✘✘ CVE-2026-64023         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64023
  │ ✘✔✘✘✘ CVE-2026-64026         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64026,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64029         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64029,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64032         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64032,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64036         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64036
  │ ✘✔✘✘✘ CVE-2026-64039         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64039,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64048         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64048,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64051         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64051,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64073         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64073,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64076         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64076
  │ ✘✔✘✘✘ CVE-2026-64077         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64077
  │ ✘✔✘✘✘ CVE-2026-64078         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64078
  │ ✘✔✘✘✘ CVE-2026-64082         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64082
  │ ✘✔✘✘✘ CVE-2026-64084         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64084,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64085         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64085,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64086         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64086,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64088         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64088,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64093         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64093,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64095         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64095,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64096         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64096,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64097         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64097,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64098         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64098,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64099         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64099,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64103         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64103,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64108         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64108,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64109         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64109,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64111         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64111,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64112         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64112
  │ ✘✔✘✘✘ CVE-2026-64114         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64114,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64115         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64115,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64116         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64116,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64117         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64117
  │ ✘✔✘✘✘ CVE-2026-64118         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64118,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64121         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64121,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64123         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64123,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64126         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64126,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64133         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64133,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64134         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64134,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64137         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64137,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64138         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64138,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64148         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64148,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64153         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64153,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64178         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64178,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64188         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64188,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64189         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64189,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64191         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64191,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64206         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64206,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64210         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64210
  │ ✘✔✘✘✘ CVE-2026-64217         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64217,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64218         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64218,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64219         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64219,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64221         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64221,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64222         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64222,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64225         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64225,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64237         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64237,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64239         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64239,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64242         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64242,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64243         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64243,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64245         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64245,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64246         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64246,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64247         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64247,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64249         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64249,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64255         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64255
  │ ✘✔✘✘✘ CVE-2026-64266         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64266,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64270         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64270,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64271         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64271,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64272         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64272,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64273         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64273,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64274         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64274,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64276         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64276,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64277         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64277,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64279         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64279,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64280         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64280,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64283         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64283
  │ ✘✔✘✘✘ CVE-2026-64286         HIGH         8.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64286,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64287         HIGH         8.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64287,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64296         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64296,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64298         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64298,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64299         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64299,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64304         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64304,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64305         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64305,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64312         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64312,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64313         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64313,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64315         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64315,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64317         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64317,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64318         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64318,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64322         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64322,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64323         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64323,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64324         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64324,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64329         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64329,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64330         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64330,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64333         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64333,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64340         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64340,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64341         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64341,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64342         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64342,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64343         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64343,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64344         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64344,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64346         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64346,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64348         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64348,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64352         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64352,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64361         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64361,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64362         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64362,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64363         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64363,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64364         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64364,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64365         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64365,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64368         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64368,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64372         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64372,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64374         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64374,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64375         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64375,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64377         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64377,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64378         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64378,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64379         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64379,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64380         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64380,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64381         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64381,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64382         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64382,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64388         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64388
  │ ✘✔✘✘✘ CVE-2026-64389         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64389
  │ ✘✔✘✘✘ CVE-2026-64390         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64390,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64394         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64394,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64395         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64395,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64396         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64396,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64398         HIGH         8.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64398,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64400         HIGH         8.6   0.6%   ·  ↳ S:UBUNTU-CVE-2026-64400
  │ ✘✔✘✘✘ CVE-2026-64401         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64401,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64402         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64402,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64403         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64403,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64406         HIGH         8.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64406,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64407         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64407,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64408         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64408,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64411         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64411,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64412         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64412,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64413         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64413,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64418         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64418,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64420         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64420,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64421         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64421,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64422         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64422,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64423         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64423,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64424         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64424,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64430         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64430,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64432         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64432,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64433         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64433,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64434         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64434,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64435         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64435,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64436         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64436,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64437         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64437,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64438         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64438,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64440         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64440,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64441         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64441,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64442         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64442,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64443         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64443,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64444         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64444,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64445         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64445,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64446         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64446,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64448         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64448,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64449         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64449,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64452         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64452,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64456         HIGH         7.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64456,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64463         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64463,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64468         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64468,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64469         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64469,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64475         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64475,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64481         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64481,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64496         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64496,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64510         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64510,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64524         HIGH         7.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64524,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64529         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64529
  │ ✘✔✘✘✘ CVE-2026-64531         HIGH         7.8   0.4%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-64531,USN-8643-1
  │ ✘✔✘✘✘ CVE-2026-64532         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64532,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64533         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64533,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64536         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64536,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64539         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64539,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64540         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64540,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64543         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64543,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64545         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-64545,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64546         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64546,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64547         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64547,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64548         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64548,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64550         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64550,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64552         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64552,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64554         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64554,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64555         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64555,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64556         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64556,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64557         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64557,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64560         HIGH         7.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64560,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64561         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64561,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64562         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64562,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64563         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64563
  │ ✘✔✘✘✘ CVE-2026-64567         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64567,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64568         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64568,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64570         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64570,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64574         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64574,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64576         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64576,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64577         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-64577,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64578         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64578,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64580         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64580,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64581         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64581
  │ ✘✔✘✘✘ CVE-2026-64582         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64582,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64583         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64583,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64584         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64584,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64585         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64585,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64586         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64586
  │ ✘✔✘✘✘ CVE-2026-64598         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64598,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64599         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64599,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64600         HIGH         7.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64600,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68085         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68085,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68091         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68091,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68096         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68096,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68097         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68097,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68098         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68098,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68100         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68100,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68103         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68103
  │ ✘✔✘✘✘ CVE-2026-68104         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68104,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68106         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68106,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68107         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68107,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68108         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68108,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68116         HIGH         7.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68116,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68118         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68118
  │ ✘✔✘✘✘ CVE-2026-68119         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68119,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68121         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68121,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68125         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68125,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68129         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68129,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68131         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68131,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68138         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68138
  │ ✘✔✘✘✘ CVE-2026-68140         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68140,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68141         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68141,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68142         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68142,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68143         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68143,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68145         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68145,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68147         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68147,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68148         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68148,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68149         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68149,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68152         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68152
  │ ✘✔✘✘✘ CVE-2026-68153         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68153,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68155         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68155,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68157         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68157,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68162         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68162,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68178         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68178,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68179         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68179,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68189         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68189,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68192         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68192,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68196         HIGH         8.3   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68196,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68198         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68198
  │ ✘✔✘✘✘ CVE-2026-68199         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68199,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68202         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68202,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68204         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68204,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68206         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68206,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68209         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68209,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68210         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68210,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68213         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68213,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68216         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68216,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68219         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68219,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68222         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68222,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68228         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68228,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68229         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68229,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68236         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68236,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68245         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68245
  │ ✘✔✘✘✘ CVE-2026-68253         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68253
  │ ✘✔✘✘✘ CVE-2026-68255         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68255,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68257         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68257
  │ ✘✔✘✘✘ CVE-2026-68258         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68258
  │ ✘✔✘✘✘ CVE-2026-68260         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68260,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68262         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68262,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68263         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68263,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68266         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68266
  │ ✘✔✘✘✘ CVE-2026-68273         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68273
  │ ✘✔✘✘✘ CVE-2026-68284         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68284,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68287         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68287
  │ ✘✔✘✘✘ CVE-2026-68290         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68290,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68293         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68293,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68294         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68294,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68297         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68297,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68299         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68299,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68314         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68314,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68315         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68315,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68320         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68320,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68323         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68323
  │ ✘✔✘✘✘ CVE-2026-68326         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68326,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68329         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68329,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68335         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68335,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68338         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68338,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68340         HIGH         7.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68340,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68348         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68348,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68352         HIGH         8.3   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68352,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68353         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68353,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68354         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68354,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68370         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68370,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68371         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68371,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68373         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68373,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68374         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68374
  │ ✘✔✘✘✘ CVE-2026-68376         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-68376,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68377         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68377,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68382         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68382
  │ ✘✔✘✘✘ CVE-2026-68383         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68383
  │ ✘✔✘✘✘ CVE-2026-68389         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68389,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68391         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68391,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68392         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68392,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68397         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68397,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68398         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68398,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68399         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68399,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68400         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68400
  │ ✘✔✘✘✘ CVE-2026-68401         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68401
  │ ✘✔✘✘✘ CVE-2026-68402         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68402,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68404         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68404
  │ ✘✔✘✘✘ CVE-2026-68409         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68409
  │ ✘✔✘✘✘ CVE-2026-68414         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68414,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68417         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68417,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68419         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68419,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68425         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68425,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68427         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68427,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68432         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68432,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68433         HIGH         8.6   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68433,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68442         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68442,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68445         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68445,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68446         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68446,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68447         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68447
  │ ✘✔✘✘✘ CVE-2026-68451         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68451
  │ ✘✔✘✘✘ CVE-2026-68452         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68452
  │ ✘✔✘✘✘ CVE-2026-68453         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68453
  │ ✘✔✘✘✘ CVE-2026-68454         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68454,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68461         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68461,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68466         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68466,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68467         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68467,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68470         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68470
  │ ✘✔✘✘✘ CVE-2026-68471         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68471
  │ ✘✔✘✘✘ CVE-2026-68474         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68474,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68479         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68479,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72005         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72005,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72009         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-72009
  │ ✘✔✘✘✘ CVE-2026-72012         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-72012,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72019         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72019,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72021         HIGH         8.2   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72021,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72024         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-72024,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72029         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-72029,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72035         HIGH         8.2   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72035,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72036         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72036,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72042         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72042
  │ ✘✔✘✘✘ CVE-2026-72045         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72045,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72049         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-72049,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72051         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72051,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72052         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72052,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72053         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72053,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72054         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72054,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72055         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72055,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72057         HIGH         8.2   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72057,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72061         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72061,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72066         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72066,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72067         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72067,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72071         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72071,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72072         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72072,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72089         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72089,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72099         HIGH         7.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-72099,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72102         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72102,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72105         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72105,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72107         HIGH         8.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72107,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72108         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-72108,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72109         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72109,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72110         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72110,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72111         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72111
  │ ✘✔✘✘✘ CVE-2026-72113         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72113,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72114         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72114,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72115         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-72115,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72116         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72116,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72119         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72119,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72120         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72120,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72121         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-72121,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72122         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72122,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72123         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72123,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72124         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-72124,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72125         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72125,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72126         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72126,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72133         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72133,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72135         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72135,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72136         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72136,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72144         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72144,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72146         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72146,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72148         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-72148,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72149         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72149,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72157         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-72157,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72160         HIGH         8.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72160,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72162         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72162
  │ ✘✔✘✘✘ CVE-2026-72164         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72164,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72165         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72165,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72170         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72170,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72171         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72171,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72172         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72172,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72175         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72175,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72181         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72181,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72195         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72195,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72196         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72196,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72197         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72197,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72198         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72198
  │ ✘✔✘✘✘ CVE-2026-72203         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72203
  │ ✘✔✘✘✘ CVE-2026-72213         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72213,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72225         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72225,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72227         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-72227,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72231         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72231,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72232         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72232,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72233         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-72233,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72235         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-72235,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72242         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72242,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72243         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72243,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72244         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72244,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72247         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72247,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72250         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72250,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72252         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72252,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72253         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72253,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72254         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72254,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72255         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72255,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72261         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72261,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72262         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72262,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72282         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72282,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72284         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72284,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72297         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72297,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72298         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72298,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72301         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72301,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72302         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72302,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72304         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72304,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72310         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72310,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72312         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72312,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72314         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72314,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72315         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72315
  │ ✘✔✘✘✘ CVE-2026-72330         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72330,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72334         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-72334
  │ ✘✔✘✘✘ CVE-2026-72335         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72335,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72338         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72338,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72340         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72340,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72342         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72342,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72343         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72343,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72345         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72345
  │ ✘✔✘✘✘ CVE-2026-72347         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72347,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72350         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72350,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72352         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72352,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72369         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72369,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72371         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72371,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72373         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72373,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72374         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72374,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72375         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72375
  │ ✘✔✘✘✘ CVE-2026-72378         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72378,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72380         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-72380
  │ ✘✔✘✘✘ CVE-2026-72382         HIGH         8.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72382,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72383         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72383
  │ ✘✔✘✘✘ CVE-2026-72389         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72389,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72390         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72390,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72395         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72395,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72397         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72397
  │ ✘✔✘✘✘ CVE-2026-72400         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72400,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72404         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72404
  │ ✘✔✘✘✘ CVE-2026-72405         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-72405,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72406         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72406,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72409         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72409,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72410         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72410,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72416         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72416,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72418         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72418,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72419         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72419,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72420         HIGH         8.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72420,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72423         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72423
  │ ✘✔✘✘✘ CVE-2026-72425         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72425,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72427         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72427,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72434         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72434,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72435         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72435,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72438         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-72438
  │ ✘✔✘✘✘ CVE-2026-72440         HIGH         7.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-72440
  │ ✘✔✘✘✘ CVE-2026-72444         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-72444,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72449         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72449,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72450         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72450,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72454         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72454
  │ ✘✔✘✘✘ CVE-2026-72459         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-72459,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72460         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-72460,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72464         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72464,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72469         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-72469,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72470         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72470,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72476         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72476,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72478         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72478,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72480         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72480,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72483         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72483,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72485         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72485
  │ ✘✔✘✘✘ CVE-2026-72487         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72487,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72488         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72488
  │ ✘✔✘✘✘ CVE-2026-72489         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72489,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72492         HIGH         8.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72492,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72499         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72499
  │ ✘✔✘✘✘ CVE-2026-72502         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72502,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74256         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74256,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74257         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74257
  │ ✘✔✘✘✘ CVE-2026-74258         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74258
  │ ✘✔✘✘✘ CVE-2026-74262         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74262,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74264         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74264
  │ ✘✔✘✘✘ CVE-2026-74270         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74270,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74281         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-74281,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74282         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-74282,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74283         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74283,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74288         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74288,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74289         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74289
  │ ✘✔✘✘✘ CVE-2026-74292         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74292,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74293         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74293,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74294         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74294
  │ ✘✔✘✘✘ CVE-2026-74295         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74295,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74296         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74296,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74297         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74297,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74300         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74300,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74302         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74302,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74305         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74305,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74312         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74312,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74313         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74313,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74314         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74314
  │ ✘✔✘✘✘ CVE-2026-74317         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74317
  │ ✘✔✘✘✘ CVE-2026-74321         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-74321,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74330         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74330,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74334         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74334
  │ ✘✔✘✘✘ CVE-2026-74338         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74338
  │ ✘✔✘✘✘ CVE-2026-74340         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74340,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74341         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74341,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74344         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74344
  │ ✘✔✘✘✘ CVE-2026-74347         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74347
  │ ✘✔✘✘✘ CVE-2026-74349         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74349,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74356         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74356,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74359         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74359,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74363         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74363,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74365         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74365,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74374         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-74374
  │ ✘✔✘✘✘ CVE-2026-74377         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74377,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74378         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74378,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74380         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74380,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74385         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74385
  │ ✘✔✘✘✘ CVE-2026-74387         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74387,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74388         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74388
  │ ✘✔✘✘✘ CVE-2026-74390         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74390,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74397         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74397,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74405         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74405
  │ ✘✔✘✘✘ CVE-2026-74407         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74407
  │ ✘✔✘✘✘ CVE-2026-74408         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74408,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74410         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74410,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74411         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74411,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74417         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74417,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74435         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-74435,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74438         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74438,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74440         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74440
  │ ✘✔✘✘✘ CVE-2026-74443         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74443
  │ ✘✔✘✘✘ CVE-2026-74444         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74444
  │ ✘✔✘✘✘ CVE-2026-74446         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74446
  │ ✘✔✘✘✘ CVE-2026-74450         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74450
  │ ✘✔✘✘✘ CVE-2026-74453         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74453
  │ ✘✔✘✘✘ CVE-2026-74454         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74454
  │ ✘✔✘✘✘ CVE-2026-74456         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74456
  │ ✘✔✘✘✘ CVE-2026-74461         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74461
  │ ✘✔✘✘✘ CVE-2026-74465         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74465
  │ ✘✔✘✘✘ CVE-2026-74467         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74467
  │ ✘✔✘✘✘ CVE-2026-74469         HIGH         8.8   1.5%   ·  ↳ S:UBUNTU-CVE-2026-74469
  │ ✘✔✘✘✘ CVE-2026-74470         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74470
  │ ✘✔✘✘✘ CVE-2026-74471         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74471
  │ ✘✔✘✘✘ CVE-2026-74479         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74479
  │ ✘✔✘✘✘ CVE-2026-74481         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74481
  │ ✘✔✘✘✘ CVE-2026-74482         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74482
  │ ✘✔✘✘✘ CVE-2026-74485         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74485
  │ ✘✔✘✘✘ CVE-2026-74488         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74488
  │ ✘✔✘✘✘ CVE-2026-74490         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74490
  │ ✘✔✘✘✘ CVE-2026-74492         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74492
  │ ✘✔✘✘✘ CVE-2026-74496         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74496
  │ ✘✔✘✘✘ CVE-2026-74497         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74497
  │ ✘✔✘✘✘ CVE-2026-74506         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74506
  │ ✘✔✘✘✘ CVE-2026-74507         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74507
  │ ✘✔✘✘✘ CVE-2026-74508         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74508
  │ ✘✔✘✘✘ CVE-2026-74509         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74509
  │ ✘✔✘✘✘ CVE-2026-74510         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74510
  │ ✘✔✘✘✘ CVE-2026-74512         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74512
  │ ✘✔✘✘✘ CVE-2026-74515         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74515
  │ ✘✔✘✘✘ CVE-2026-74516         HIGH         8.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74516
  │ ✘✔✘✘✘ CVE-2026-74518         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74518
  │ ✘✔✘✘✘ CVE-2026-74519         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74519
  │ ✘✔✘✘✘ CVE-2026-74522         HIGH         8.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-74522
  │ ✘✔✘✘✘ CVE-2026-74523         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74523
  │ ✘✔✘✘✘ CVE-2026-74527         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74527
  │ ✘✔✘✘✘ CVE-2026-74530         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74530
  │ ✘✔✘✘✘ CVE-2026-74531         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74531
  │ ✘✔✘✘✘ CVE-2026-74533         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74533
  │ ✘✔✘✘✘ CVE-2026-74534         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74534
  │ ✘✔✘✘✘ CVE-2026-74535         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74535
  │ ✘✔✘✘✘ CVE-2026-74537         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74537
  │ ✘✔✘✘✘ CVE-2026-74538         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74538
  │ ✘✔✘✘✘ CVE-2026-74540         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74540
  │ ✘✔✘✘✘ CVE-2026-74541         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74541
  │ ✘✔✘✘✘ CVE-2026-74544         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74544
  │ ✘✔✘✘✘ CVE-2026-74548         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74548
  │ ✘✔✘✘✘ CVE-2026-74549         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74549
  │ ✘✔✘✘✘ CVE-2026-74550         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74550
  │ ✘✔✘✘✘ CVE-2026-74551         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74551
  │ ✘✔✘✘✘ CVE-2026-74557         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74557
  │ ✘✔✘✘✘ CVE-2026-74563         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74563
  │ ✘✔✘✘✘ CVE-2026-74564         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74564
  │ ✘✔✘✘✘ CVE-2026-74565         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74565
  │ ✘✔✘✘✘ CVE-2026-74567         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74567
  │ ✘✔✘✘✘ CVE-2026-74572         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74572
  │ ✘✔✘✘✘ CVE-2026-74574         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74574
  │ ✘✔✘✘✘ CVE-2026-74575         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74575
  │ ✘✔✘✘✘ CVE-2026-74578         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74578
  │ ✘✔✘✘✘ CVE-2026-74579         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74579
  │ ✘✔✘✘✘ CVE-2026-74580         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74580
  │ ✘✔✘✘✘ CVE-2026-74582         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74582
  │ ✘✔✘✘✘ CVE-2026-74583         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74583
  │ ✘✔✘✘✘ CVE-2026-74584         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74584,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74589         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74589
  │ ✘✔✘✘✘ CVE-2026-74590         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74590
  │ ✘✔✘✘✘ CVE-2026-74592         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74592
  │ ✘✔✘✘✘ CVE-2026-74594         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74594
  │ ✘✔✘✘✘ CVE-2026-74595         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74595
  │ ✘✔✘✘✘ CVE-2026-74598         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74598
  │ ✘✔✘✘✘ CVE-2026-74601         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74601
  │ ✘✔✘✘✘ CVE-2026-74603         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74603
  │ ✘✔✘✘✘ CVE-2026-74604         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74604
  │ ✘✔✘✘✘ CVE-2026-74605         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74605
  │ ✘✔✘✘✘ CVE-2026-74606         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74606
  │ ✘✔✘✘✘ CVE-2026-74607         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74607
  │ ✘✔✘✘✘ CVE-2026-74609         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74609
  │ ✘✔✘✘✘ CVE-2026-74610         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74610
  │ ✘✔✘✘✘ CVE-2026-74613         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74613
  │ ✘✔✘✘✘ CVE-2026-74614         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74614
  │ ✘✔✘✘✘ CVE-2026-74615         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74615
  │ ✘✔✘✘✘ CVE-2026-74621         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74621
  │ ✘✔✘✘✘ CVE-2026-74624         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74624
  │ ✘✔✘✘✘ CVE-2026-74625         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74625
  │ ✘✔✘✘✘ CVE-2026-74626         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74626
  │ ✘✔✘✘✘ CVE-2026-74630         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74630
  │ ✘✔✘✘✘ CVE-2026-74631         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74631
  │ ✘✔✘✘✘ CVE-2026-74632         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74632
  │ ✘✔✘✘✘ CVE-2026-74634         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74634
  │ ✘✔✘✘✘ CVE-2026-74635         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74635
  │ ✘✔✘✘✘ CVE-2026-74637         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74637
  │ ✘✔✘✘✘ CVE-2026-74641         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74641
  │ ✘✔✘✘✘ CVE-2026-74646         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74646
  │ ✘✔✘✘✘ CVE-2026-74647         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74647
  │ ✘✔✘✘✘ CVE-2026-74648         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74648
  │ ✘✔✘✘✘ CVE-2026-74649         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74649
  │ ✘✔✘✘✘ CVE-2026-74651         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74651
  │ ✘✔✘✘✘ CVE-2026-74655         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74655
  │ ✘✔✘✘✘ CVE-2026-74656         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74656
  │ ✘✔✘✘✘ CVE-2026-74660         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74660
  │ ✘✔✘✘✘ CVE-2026-74661         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74661
  │ ✘✔✘✘✘ CVE-2026-74663         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74663
  │ ✘✔✘✘✘ CVE-2026-74666         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74666
  │ ✘✔✘✘✘ CVE-2026-74667         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74667
  │ ✘✔✘✘✘ CVE-2026-74668         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74668
  │ ✘✔✘✘✘ CVE-2026-74670         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74670
  │ ✘✔✘✘✘ CVE-2026-74675         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74675
  │ ✘✔✘✘✘ CVE-2026-74678         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74678
  │ ✘✔✘✘✘ CVE-2026-74684         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74684
  │ ✘✔✘✘✘ CVE-2026-74687         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74687
  │ ✘✔✘✘✘ CVE-2026-74689         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74689
  │ ✘✔✘✘✘ CVE-2026-74690         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74690
  │ ✘✔✘✘✘ CVE-2026-74691         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74691
  │ ✘✔✘✘✘ CVE-2026-74692         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74692
  │ ✘✔✘✘✘ CVE-2026-74695         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74695
  │ ✘✔✘✘✘ CVE-2026-74696         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74696
  │ ✘✔✘✘✘ CVE-2026-74697         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74697
  │ ✘✔✘✘✘ CVE-2026-74700         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74700
  │ ✘✔✘✘✘ CVE-2026-74701         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74701
  │ ✘✔✘✘✘ CVE-2026-74704         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74704
  │ ✘✔✘✘✘ CVE-2026-74710         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74710
  │ ✘✔✘✘✘ CVE-2026-74711         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74711
  │ ✘✔✘✘✘ CVE-2026-74713         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74713
  │ ✘✔✘✘✘ CVE-2026-74714         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74714
  │ ✘✔✘✘✘ CVE-2026-74715         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74715
  │ ✘✔✘✘✘ CVE-2026-74717         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74717
  │ ✘✔✘✘✘ CVE-2026-74720         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74720
  │ ✘✔✘✘✘ CVE-2026-74724         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74724
  │ ✘✔✘✘✘ CVE-2026-74725         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74725
  │ ✘✔✘✘✘ CVE-2026-74726         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74726
  │ ✘✔✘✘✘ CVE-2026-74733         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74733
  │ ✘✔✘✘✘ CVE-2026-74736         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74736
  │ ✘✔✘✘✘ CVE-2026-74739         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74739
  │ ✘✔✘✘✘ CVE-2026-74747         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74747
  │ ✘✔✘✘✘ CVE-2026-74748         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74748
  │ ✘✔✘✘✘ CVE-2026-80521         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80521
  │ ✘✔✘✘✘ CVE-2026-80526         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80526
  │ ✘✔✘✘✘ CVE-2026-80527         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-80527
  │ ✘✔✘✘✘ CVE-2026-80536         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80536
  │ ✘✔✘✘✘ CVE-2026-80540         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80540
  │ ✘✔✘✘✘ CVE-2026-80541         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80541
  │ ✘✔✘✘✘ CVE-2026-80547         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80547
  │ ✘✔✘✘✘ CVE-2026-80548         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80548
  │ ✘✔✘✘✘ CVE-2026-80549         HIGH         8.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80549
  │ ✘✔✘✘✘ CVE-2026-80550         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80550
  │ ✘✔✘✘✘ CVE-2026-80552         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80552
  │ ✘✔✘✘✘ CVE-2026-80553         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80553
  │ ✘✔✘✘✘ CVE-2026-80555         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80555
  │ ✘✔✘✘✘ CVE-2026-80556         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80556
  │ ✘✔✘✘✘ CVE-2026-80559         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80559
  │ ✘✔✘✘✘ CVE-2026-80560         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80560
  │ ✘✔✘✘✘ CVE-2026-80565         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80565
  │ ✘✔✘✘✘ CVE-2026-80568         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80568
  │ ✘✔✘✘✘ CVE-2026-80569         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80569
  │ ✘✔✘✘✘ CVE-2026-80570         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80570
  │ ✘✔✘✘✘ CVE-2026-80572         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80572
  │ ✘✔✘✘✘ CVE-2026-80574         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80574
  │ ✘✔✘✘✘ CVE-2026-80576         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80576
  │ ✘✔✘✘✘ CVE-2026-80578         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80578
  │ ✘✔✘✘✘ CVE-2026-80579         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80579
  │ ✘✔✘✘✘ CVE-2026-80580         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80580
  │ ✘✔✘✘✘ CVE-2026-80583         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80583
  │ ✘✔✘✘✘ CVE-2026-80584         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80584
  │ ✘✔✘✘✘ CVE-2026-80590         HIGH         8.6   0.6%   ·  ↳ S:UBUNTU-CVE-2026-80590
  │ ✘✔✘✘✘ CVE-2026-80591         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80591,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80593         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80593,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80598         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80598,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80599         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80599,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80601         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80601,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80613         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80613,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80619         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80619,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80622         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80622,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80628         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80628
  │ ✘✔✘✘✘ CVE-2026-80631         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-80631
  │ ✘✔✘✘✘ CVE-2026-80635         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80635,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80637         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-80637,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80645         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80645,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80646         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-80646,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80649         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80649,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80653         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80653
  │ ✘✔✘✘✘ CVE-2026-80662         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80662
  │ ✘✔✘✘✘ CVE-2026-80663         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80663,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80664         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80664,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80677         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80677,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80678         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80678
  │ ✘✔✘✘✘ CVE-2026-80680         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80680
  │ ✘✔✘✘✘ CVE-2026-80691         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80691
  │ ✘✔✘✘✘ CVE-2026-80692         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80692
  │ ✘✔✘✘✘ CVE-2026-80700         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80700
  │ ✘✔✘✘✘ CVE-2026-80702         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80702
  │ ✘✔✘✘✘ CVE-2026-80706         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80706
  │ ✘✔✘✘✘ CVE-2026-80707         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-80707
  │ ✘✔✘✘✘ CVE-2026-80709         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80709
  │ ✘✔✘✘✘ CVE-2026-80710         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80710
  │ ✘✔✘✘✘ CVE-2026-80716         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80716
  │ ✘✔✘✘✘ CVE-2026-80717         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-80717
  │ ✘✔✘✘✘ CVE-2026-80718         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80718
  │ ✘✔✘✘✘ CVE-2026-80721         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80721
  │ ✘✔✘✘✘ CVE-2026-80722         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80722
  │ ✘✔✘✘✘ CVE-2026-80731         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80731
  │ ✘✔✘✘✘ CVE-2026-80732         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80732
  │ ✘✔✘✘✘ CVE-2026-80737         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80737
  │ ✘✔✘✘✘ CVE-2026-80738         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80738
  │ ✘✔✘✘✘ CVE-2026-80747         HIGH         8.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80747
  │ ✘✔✘✘✘ CVE-2026-80752         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80752
  │ ✘✔✘✘✘ CVE-2026-80754         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80754
  │ ✘✔✘✘✘ CVE-2026-80914         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80914
  │ ✘✔✘✘✘ CVE-2026-80921         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80921
  │ ✘✔✘✘✘ CVE-2026-80928         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80928
  │ ✘✔✘✘✘ CVE-2026-80931         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80931
  │ ✘✔✘✘✘ CVE-2026-80932         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80932
  │ ✘✔✘✘✘ CVE-2026-80933         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80933
  │ ✘✔✘✘✘ CVE-2026-80935         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-80935
  │ ✘✔✘✘✘ CVE-2026-80937         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-80937
  │ ✘✔✘✘✘ CVE-2026-80944         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80944
  │ ✘✔✘✘✘ CVE-2026-80947         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80947
  │ ✘✔✘✘✘ CVE-2026-80952         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80952
  │ ✘✔✘✘✘ CVE-2026-80967         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80967
  │ ✘✔✘✘✘ CVE-2026-80971         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80971
  │ ✘✔✘✘✘ CVE-2026-80977         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80977
  │ ✘✔✘✘✘ CVE-2026-80978         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80978
  │ ✘✔✘✘✘ CVE-2026-80979         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80979
  │ ✘✔✘✘✘ CVE-2026-80982         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80982
  │ ✘✔✘✘✘ CVE-2026-80987         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-80987
  │ ✘✔✘✘✘ CVE-2026-80989         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-80989
  │ ✘✔✘✘✘ CVE-2026-80991         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80991
  │ ✘✔✘✘✘ CVE-2026-80992         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80992
  │ ✘✔✘✘✘ CVE-2026-80994         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80994
  │ ✘✔✘✘✘ CVE-2026-81000         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-81000
  │ ✘✔✘✘✘ CVE-2026-81001         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-81001
  │ ✘✔✘✘✘ CVE-2026-81003         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-81003
  │ ✘✔✘✘✘ CVE-2026-81007         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-81007
  │ ✘✔✘✘✘ CVE-2026-81008         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-81008
  │ ✘✔✘✘✘ CVE-2026-81010         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-81010
  │ ✘✔✘✘✘ CVE-2026-81011         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-81011
  │ ✘✔✘✘✘ CVE-2026-81012         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-81012
  │ ✘✔✘✘✘ CVE-2026-81016         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-81016
  │ ✘✔✘✘✘ CVE-2026-81017         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-81017
  │ ✘✔✘✘✘ CVE-2026-89440         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89440
  │ ✘✔✘✘✘ CVE-2026-89441         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89441
  │ ✘✔✘✘✘ CVE-2026-89442         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89442
  │ ✘✔✘✘✘ CVE-2026-89443         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89443
  │ ✘✔✘✘✘ CVE-2026-89452         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89452
  │ ✘✔✘✘✘ CVE-2026-89456         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89456
  │ ✘✔✘✘✘ CVE-2026-89465         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89465
  │ ✘✔✘✘✘ CVE-2026-89466         HIGH         7.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89466
  │ ✘✔✘✘✘ CVE-2026-89469         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89469
  │ ✘✔✘✘✘ CVE-2026-89470         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89470
  │ ✘✔✘✘✘ CVE-2026-89471         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89471
  │ ✘✔✘✘✘ CVE-2026-89472         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89472
  │ ✘✔✘✘✘ CVE-2026-89476         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89476
  │ ✘✔✘✘✘ CVE-2026-89477         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89477
  │ ✘✔✘✘✘ CVE-2026-89480         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89480
  │ ✘✔✘✘✘ CVE-2026-89481         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89481
  │ ✘✔✘✘✘ CVE-2026-89483         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89483
  │ ✘✔✘✘✘ CVE-2026-89487         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89487
  │ ✘✔✘✘✘ CVE-2026-89488         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89488
  │ ✘✔✘✘✘ CVE-2026-89489         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89489
  │ ✘✔✘✘✘ CVE-2026-89493         HIGH         8.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89493
  │ ✘✔✘✘✘ CVE-2026-89497         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89497
  │ ✘✔✘✘✘ CVE-2026-89500         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89500
  │ ✘✔✘✘✘ CVE-2026-89501         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89501
  │ ✘✔✘✘✘ CVE-2026-89503         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89503
  │ ✘✔✘✘✘ CVE-2026-89504         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89504
  │ ✘✔✘✘✘ CVE-2026-89508         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89508
  │ ✘✔✘✘✘ CVE-2026-89510         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89510
  │ ✘✔✘✘✘ CVE-2026-89511         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89511
  │ ✘✔✘✘✘ CVE-2026-89520         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89520
  │ ✘✔✘✘✘ CVE-2026-89524         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89524
  │ ✘✔✘✘✘ CVE-2026-89528         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89528
  │ ✘✔✘✘✘ CVE-2026-89540         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89540
  │ ✘✔✘✘✘ CVE-2026-89544         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89544
  │ ✘✔✘✘✘ CVE-2026-89545         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89545
  │ ✘✔✘✘✘ CVE-2026-89547         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89547
  │ ✘✔✘✘✘ CVE-2026-89548         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89548
  │ ✘✔✘✘✘ CVE-2026-89549         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89549
  │ ✘✔✘✘✘ CVE-2026-89553         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89553
  │ ✘✔✘✘✘ CVE-2026-89554         HIGH         8.2   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89554
  │ ✘✔✘✘✘ CVE-2026-89557         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89557
  │ ✘✔✘✘✘ CVE-2026-89559         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89559
  │ ✘✔✘✘✘ CVE-2026-89560         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89560
  │ ✘✔✘✘✘ CVE-2026-89561         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89561
  │ ✘✔✘✘✘ CVE-2026-89562         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89562
  │ ✘✔✘✘✘ CVE-2026-89563         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89563
  │ ✘✔✘✘✘ CVE-2026-89564         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89564
  │ ✘✔✘✘✘ CVE-2026-89569         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89569
  │ ✘✔✘✘✘ CVE-2026-89573         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89573
  │ ✘✔✘✘✘ CVE-2026-89574         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89574
  │ ✘✔✘✘✘ CVE-2026-89579         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89579
  │ ✘✔✘✘✘ CVE-2026-89580         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89580
  │ ✘✔✘✘✘ CVE-2026-89583         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89583
  │ ✘✔✘✘✘ CVE-2026-89585         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89585
  │ ✘✔✘✘✘ CVE-2026-89586         HIGH         8.2   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89586
  │ ✘✔✘✘✘ CVE-2026-89587         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89587
  │ ✘✔✘✘✘ CVE-2026-89588         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89588
  │ ✘✔✘✘✘ CVE-2026-89594         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89594
  │ ✘✔✘✘✘ CVE-2026-89596         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89596
  │ ✘✔✘✘✘ CVE-2026-89597         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89597
  │ ✘✔✘✘✘ CVE-2026-89599         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89599
  │ ✘✔✘✘✘ CVE-2026-89601         HIGH         8.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89601
  │ ✘✔✘✘✘ CVE-2026-89605         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89605
  │ ✘✔✘✘✘ CVE-2026-89606         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89606
  │ ✘✔✘✘✘ CVE-2026-89607         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89607
  │ ✘✔✘✘✘ CVE-2026-89608         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89608
  │ ✘✔✘✘✘ CVE-2026-89609         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89609
  │ ✘✔✘✘✘ CVE-2026-89615         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89615
  │ ✘✔✘✘✘ CVE-2026-89616         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89616
  │ ✘✔✘✘✘ CVE-2026-89617         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89617
  │ ✘✔✘✘✘ CVE-2026-89622         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89622
  │ ✘✔✘✘✘ CVE-2026-89624         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89624
  │ ✘✔✘✘✘ CVE-2026-89626         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89626
  │ ✘✔✘✘✘ CVE-2026-89632         HIGH         8.2   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89632
  │ ✘✔✘✘✘ CVE-2026-89638         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89638
  │ ✘✔✘✘✘ CVE-2026-89640         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89640
  │ ✘✔✘✘✘ CVE-2026-89647         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89647
  │ ✘✔✘✘✘ CVE-2026-89648         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89648
  │ ✘✔✘✘✘ CVE-2026-89657         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89657
  │ ✘✔✘✘✘ CVE-2026-89663         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89663
  │ ✘✔✘✘✘ CVE-2026-89665         HIGH         8.2   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89665
  │ ✘✔✘✘✘ CVE-2026-89680         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89680
  │ ✘✔✘✘✘ CVE-2026-89682         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89682
  │ ✘✔✘✘✘ CVE-2026-89684         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89684
  │ ✘✔✘✘✘ CVE-2026-89685         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89685
  │ ✘✔✘✘✘ CVE-2026-89690         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89690
  │ ✘✔✘✘✘ CVE-2026-89691         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89691
  │ ✘✔✘✘✘ CVE-2026-89696         HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2026-89696
  │ ✘✔✘✘✘ CVE-2026-89699         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89699
  │ ✘✔✘✘✘ CVE-2026-89704         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89704
  │ ✘✔✘✘✘ CVE-2026-89705         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89705
  │ ✘✔✘✘✘ CVE-2026-89706         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89706
  │ ✘✔✘✘✘ CVE-2026-89707         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89707
  │ ✘✔✘✘✘ CVE-2026-89709         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89709
  │ ✘✔✘✘✘ CVE-2026-89711         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89711
  │ ✘✔✘✘✘ CVE-2026-89720         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89720
  │ ✘✔✘✘✘ CVE-2026-89723         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89723
  │ ✘✔✘✘✘ CVE-2026-89724         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89724
  │ ✘✔✘✘✘ CVE-2026-89725         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89725
  │ ✘✔✘✘✘ CVE-2026-89729         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89729
  │ ✘✔✘✘✘ CVE-2026-89731         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89731
  │ ✘✔✘✘✘ CVE-2026-89733         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89733
  │ ✘✔✘✘✘ CVE-2026-89736         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89736
  │ ✘✔✘✘✘ CVE-2026-89738         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89738
  │ ✘✔✘✘✘ CVE-2026-89741         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89741
  │ ✘✔✘✘✘ CVE-2026-89742         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89742
  │ ✘✔✘✘✘ CVE-2026-89743         HIGH         7.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89743
  │ ✘✔✘✘✘ CVE-2026-89744         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89744
  │ ✘✔✘✘✘ CVE-2026-89746         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89746
  │ ✘✔✘✘✘ CVE-2026-89747         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89747
  │ ✘✔✘✘✘ CVE-2026-89750         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89750
  │ ✘✔✘✘✘ CVE-2026-89755         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89755
  │ ✘✔✘✘✘ CVE-2026-89761         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89761
  │ ✘✔✘✘✘ CVE-2026-89762         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89762
  │ ✘✔✘✘✘ CVE-2026-89763         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89763
  │ ✘✔✘✘✘ CVE-2026-89771         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89771
  │ ✘✔✘✘✘ CVE-2026-89774         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89774,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-89777         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89777
  │ ✘✔✘✘✘ CVE-2026-89781         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89781
  │ ✘✔✘✘✘ CVE-2026-89782         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89782
  │ ✘✔✘✘✘ CVE-2026-89789         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89789
  │ ✘✔✘✘✘ CVE-2026-89792         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89792
  │ ✘✔✘✘✘ CVE-2026-89793         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89793
  │ ✘✔✘✘✘ CVE-2026-89795         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89795
  │ ✘✔✘✘✘ CVE-2026-89799         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89799
  │ ✘✔✘✘✘ CVE-2026-89801         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89801
  │ ✘✔✘✘✘ CVE-2026-89803         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89803
  │ ✘✔✘✘✘ CVE-2026-89806         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89806
  │ ✘✔✘✘✘ CVE-2026-89808         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89808
  │ ✘✔✘✘✘ CVE-2026-89810         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89810
  │ ✘✔✘✘✘ CVE-2026-89811         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89811
  │ ✘✔✘✘✘ CVE-2026-89818         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89818
  │ ✘✔✘✘✘ CVE-2026-89819         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89819
  │ ✘✔✘✘✘ CVE-2026-89823         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89823
  │ ✘✔✘✘✘ CVE-2026-89832         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89832
  │ ✘✔✘✘✘ CVE-2026-89838         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89838
  │ ✘✔✘✘✘ CVE-2026-89840         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89840
  │ ✘✔✘✘✘ CVE-2026-89844         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89844
  │ ✘✔✘✘✘ CVE-2026-89848         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89848
  │ ✘✔✘✘✘ CVE-2026-89849         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89849
  │ ✘✔✘✘✘ CVE-2026-89854         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89854
  │ ✘✔✘✘✘ CVE-2026-89856         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89856
  │ ✘✔✘✘✘ CVE-2026-89860         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89860
  │ ✘✔✘✘✘ CVE-2026-89861         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89861
  │ ✘✔✘✘✘ CVE-2026-89863         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89863
  │ ✘✔✘✘✘ CVE-2026-89870         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89870
  │ ✘✔✘✘✘ CVE-2026-89877         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89877
  │ ✘✔✘✘✘ CVE-2026-89880         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89880
  │ ✘✔✘✘✘ CVE-2026-89883         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89883
  │ ✘✔✘✘✘ CVE-2026-89887         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89887
  │ ✘✔✘✘✘ CVE-2026-89888         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89888
  │ ✘✔✘✘✘ CVE-2026-89890         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89890
  │ ✘✔✘✘✘ CVE-2026-89893         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89893
  │ ✘✔✘✘✘ CVE-2026-89894         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89894
  │ ✘✔✘✘✘ CVE-2026-89897         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89897
  │ ✘✔✘✘✘ CVE-2026-89899         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89899
  │ ✘✔✘✘✘ CVE-2026-89902         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89902
  │ ✘✔✘✘✘ CVE-2026-89903         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89903
  │ ✘✔✘✘✘ CVE-2026-89904         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89904
  │ ✘✔✘✘✘ CVE-2026-89906         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89906
  │ ✘✔✘✘✘ CVE-2026-89908         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89908
  │ ✘✔✘✘✘ CVE-2026-89912         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89912
  │ ✘✔✘✘✘ CVE-2026-89913         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89913
  │ ✘✔✘✘✘ CVE-2026-89920         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89920
  │ ✘✔✘✘✘ CVE-2026-89922         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89922
  │ ✘✔✘✘✘ CVE-2026-89927         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89927
  │ ✘✔✘✘✘ CVE-2026-89929         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89929
  │ ✘✔✘✘✘ CVE-2026-89932         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89932
  │ ✘✔✘✘✘ CVE-2026-89938         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89938
  │ ✘✔✘✘✘ CVE-2026-89947         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89947
  │ ✘✔✘✘✘ CVE-2026-89951         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89951
  │ ✘✔✘✘✘ CVE-2026-89954         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89954
  │ ✘✔✘✘✘ CVE-2026-89957         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89957
  │ ✘✔✘✘✘ CVE-2026-89959         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89959
  │ ✘✔✘✘✘ CVE-2026-89960         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89960
  │ ✘✔✘✘✘ CVE-2026-89961         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89961
  │ ✘✔✘✘✘ CVE-2026-89965         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89965
  │ ✘✔✘✘✘ CVE-2026-89968         HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2026-89968
  │ ✘✔✘✘✘ CVE-2026-89973         HIGH         8.2   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89973
  │ ✘✔✘✘✘ CVE-2026-89979         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89979
  │ ✘✔✘✘✘ CVE-2026-89988         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89988
  │ ✘✔✘✘✘ CVE-2026-89992         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89992
  │ ✘✔✘✘✘ CVE-2026-89995         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89995
  │ ✘✔✘✘✘ CVE-2026-89997         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89997
  │ ✘✔✘✘✘ CVE-2026-89998         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89998
  │ ✘✔✘✘✘ CVE-2026-89999         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89999
  │ ✘✔✘✘✘ CVE-2026-90000         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90000
  │ ✘✔✘✘✘ CVE-2026-90002         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90002
  │ ✘✔✘✘✘ CVE-2026-90003         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90003
  │ ✘✔✘✘✘ CVE-2026-90007         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90007
  │ ✘✔✘✘✘ CVE-2026-90013         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90013
  │ ✘✔✘✘✘ CVE-2026-90016         HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90016
  │ ✘✔✘✘✘ CVE-2026-90017         HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90017
  │ ✘✔✘✘✘ CVE-2026-90018         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90018
  │ ✘✔✘✘✘ CVE-2026-90022         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90022
  │ ✘✔✘✘✘ CVE-2026-90025         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90025
  │ ✘✔✘✘✘ CVE-2026-90026         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90026
  │ ✘✔✘✘✘ CVE-2026-90027         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90027
  │ ✘✔✘✘✘ CVE-2026-90030         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90030
  │ ✘✔✘✘✘ CVE-2026-90032         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90032
  │ ✘✔✘✘✘ CVE-2026-90041         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-90041
  │ ✘✔✘✘✘ CVE-2026-90044         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90044
  │ ✘✔✘✘✘ CVE-2026-90045         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90045
  │ ✘✔✘✘✘ CVE-2026-90057         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90057
  │ ✘✔✘✘✘ CVE-2026-90062         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90062
  │ ✘✔✘✘✘ CVE-2026-90067         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90067
  │ ✘✔✘✘✘ CVE-2026-90071         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90071
  │ ✘✔✘✘✘ CVE-2026-90091         HIGH         8.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90091
  │ ✘✔✘✘✘ CVE-2026-90092         HIGH         8.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90092
  │ ✘✔✘✘✘ CVE-2026-90093         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90093
  │ ✘✔✘✘✘ CVE-2026-90102         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90102
  │ ✘✔✘✘✘ CVE-2026-90103         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90103
  │ ✘✔✘✘✘ CVE-2026-90111         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90111
  │ ✘✔✘✘✘ CVE-2026-90137         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90137
  │ ✘✔✘✘✘ CVE-2026-90141         HIGH         7.3   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90141
  │ ✘✔✘✘✘ CVE-2026-90143         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90143
  │ ✘✔✘✘✘ CVE-2026-90146         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90146
  │ ✘✔✘✘✘ CVE-2026-90149         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90149
  │ ✘✔✘✘✘ CVE-2026-90153         HIGH         8.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-90153
  │ ✘✔✘✘✘ CVE-2026-90161         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90161
  │ ✘✔✘✘✘ CVE-2026-90162         HIGH         8.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90162
  │ ✘✔✘✘✘ CVE-2026-90174         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90174
  │ ✘✔✘✘✘ CVE-2026-90176         HIGH         8.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-90176
  │ ✘✔✘✘✘ CVE-2026-90199         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90199
  │ ✘✔✘✘✘ CVE-2026-90203         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90203
  │ ✘✔✘✘✘ CVE-2026-90204         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90204
  │ ✘✔✘✘✘ CVE-2026-90205         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90205
  │ ✘✔✘✘✘ CVE-2026-90207         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90207
  │ ✘✔✘✘✘ CVE-2026-90217         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90217
  │ ✘✔✘✘✘ CVE-2026-90223         HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90223
  │ ✘✔✘✘✘ CVE-2026-90224         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90224
  │ ✘✔✘✘✘ CVE-2026-90225         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90225
  │ ✘✔✘✘✘ CVE-2026-90227         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90227
  │ ✘✔✘✘✘ CVE-2026-90228         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90228
  │ ✘✔✘✘✘ CVE-2026-90229         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90229
  │ ✘✔✘✘✘ CVE-2026-90231         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90231
  │ ✘✔✘✘✘ CVE-2026-90234         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90234
  │ ✘✔✘✘✘ CVE-2026-90237         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90237
  │ ✘✔✘✘✘ CVE-2026-90255         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-90255
  │ ✘✔✘✘✘ CVE-2026-90256         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90256
  │ ✘✔✘✘✘ CVE-2026-90260         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90260
  │ ✘✔✘✘✘ CVE-2026-90286         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90286
  │ ✘✔✘✘✘ CVE-2026-90289         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90289
  │ ✘✔✘✘✘ CVE-2026-90291         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90291
  │ ✘✔✘✘✘ CVE-2026-90292         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90292
  │ ✘✔✘✘✘ CVE-2026-90293         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90293
  │ ✘✔✘✘✘ CVE-2026-90294         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90294
  │ ✘✔✘✘✘ CVE-2026-90301         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-90301
  │ ✘✔✘✘✘ CVE-2026-90308         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90308
  │ ✘✔✘✘✘ CVE-2026-90309         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90309
  │ ✘✔✘✘✘ CVE-2026-90316         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90316
  │ ✘✔✘✘✘ CVE-2026-90317         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90317
  │ ✘✔✘✘✘ CVE-2026-90320         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90320
  │ ✘✔✘✘✘ CVE-2026-90321         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90321
  │ ✘✔✘✘✘ CVE-2026-90324         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90324
  │ ✘✔✘✘✘ CVE-2026-90325         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90325
  │ ✘✔✘✘✘ CVE-2026-90326         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90326
  │ ✘✔✘✘✘ CVE-2026-90329         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-90329
  │ ✘✔✘✘✘ CVE-2026-90341         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90341
  │ ✘✔✘✘✘ CVE-2026-90343         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90343
  │ ✘✔✘✘✘ CVE-2026-90347         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90347
  │ ✘✔✘✘✘ CVE-2026-90353         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-90353
  │ ✘✔✘✘✘ CVE-2026-90357         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-90357
  │ ✘✔✘✘✘ CVE-2026-90358         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90358
  │ ✘✔✘✘✘ CVE-2026-90367         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90367
  │ ✘✔✘✘✘ CVE-2026-90372         HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90372
  │ ✘✔✘✘✘ CVE-2026-90379         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90379
  │ ✘✔✘✘✘ CVE-2026-90380         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-90380
  │ ✘✔✘✘✘ CVE-2026-90383         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90383
  │ ✘✔✘✘✘ CVE-2026-90387         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90387
  │ ✘✔✘✘✘ CVE-2026-90388         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90388
  │ ✘✔✘✘✘ CVE-2026-90392         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90392
  │ ✘✔✘✘✘ CVE-2026-90398         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-90398
  │ ✘✔✘✘✘ CVE-2026-90399         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90399
  │ ✘✔✘✘✘ CVE-2026-90401         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90401
  │ ✘✔✘✘✘ CVE-2026-90403         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-90403
  │ ✘✔✘✘✘ CVE-2026-90407         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90407
  │ ✘✔✘✘✘ CVE-2026-90408         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90408
  │ ✘✔✘✘✘ CVE-2026-90419         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90419
  │ ✘✔✘✘✘ CVE-2026-90435         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-90435
  │ ✘✔✘✘✘ CVE-2026-92485         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92485
  │ ✘✔✘✘✘ CVE-2026-92488         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-92488
  │ ✘✔✘✘✘ CVE-2026-92504         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-92504
  │ ✘✔✘✘✘ CVE-2026-92507         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92507
  │ ✘✔✘✘✘ CVE-2026-92508         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92508
  │ ✘✔✘✘✘ CVE-2026-92510         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-92510
  │ ✘✔✘✘✘ CVE-2026-92511         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-92511
  │ ✘✔✘✘✘ CVE-2026-92522         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-92522
  │ ✘✔✘✘✘ CVE-2026-92525         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92525
  │ ✘✔✘✘✘ CVE-2026-93037         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93037
  │ ✘✔✘✘✘ CVE-2026-93039         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93039
  │ ✘✔✘✘✘ CVE-2026-93042         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-93042
  │ ✘✔✘✘✘ CVE-2026-93046         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93046
  │ ✘✔✘✘✘ CVE-2026-93054         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93054
  │ ✘✔✘✘✘ CVE-2026-93063         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93063
  │ ✘✔✘✘✘ CVE-2026-93095         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93095
  │ ✘✔✘✘✘ CVE-2026-93105         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93105
  │ ✘✔✘✘✘ CVE-2026-93107         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-93107
  │ ✘✔✘✘✘ CVE-2026-93116         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93116
  │ ✘✔✘✘✘ CVE-2026-93122         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93122
  │ ✘✔✘✘✘ CVE-2026-93125         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93125
  │ ✘✔✘✘✘ CVE-2026-93137         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93137
  │ ✘✔✘✘✘ CVE-2026-93138         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93138
  │ ✘✔✘✘✘ CVE-2026-93144         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93144
  │ ✘✔✘✘✘ CVE-2026-93148         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93148
  │ ✘✔✘✘✘ CVE-2026-93151         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-93151
  │ ✘✔✘✘✘ CVE-2026-93154         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93154
  │ ✘✔✘✘✘ CVE-2026-93165         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93165
  │ ✘✔✘✘✘ CVE-2026-93170         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93170
  │ ✘✔✘✘✘ CVE-2026-93175         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93175
  │ ✘✔✘✘✘ CVE-2026-93176         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93176
  │ ✘✔✘✘✘ CVE-2026-93177         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93177
  │ ✘✔✘✘✘ CVE-2026-93178         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93178
  │ ✘✔✘✘✘ CVE-2026-93189         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-93189
  │ ✘✔✘✘✘ CVE-2026-93190         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93190
  │ ✘✔✘✘✘ CVE-2026-93192         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93192
  │ ✘✔✘✘✘ CVE-2026-93196         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93196
  │ ✘✔✘✘✘ CVE-2026-93203         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-93203
  │ ✘✔✘✘✘ CVE-2026-93221         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-93221
  │ ✘✔✘✘✘ CVE-2026-93229         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93229
  │ ✘✔✘✘✘ CVE-2026-93237         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93237
  │ ✘✔✘✘✘ CVE-2026-93250         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93250
  │ ✘✔✘✘✘ CVE-2026-93260         HIGH         7.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93260
  │ ✘✔✘✘✘ CVE-2026-93262         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93262
  │ ✘✔✘✘✘ CVE-2026-93280         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-93280
  │ ✘✔✘✘✘ CVE-2026-93282         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-93282
  │ ✘✔✘✘✘ CVE-2026-93287         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93287
  │ ✘✔✘✘✘ CVE-2026-93288         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93288
  │ ✘✔✘✘✘ CVE-2026-93782         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93782
  │ ✘✔✘✘✘ CVE-2026-93786         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-93786
  │ ✘✔✘✘✘ CVE-2026-93787         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-93787
  │ ✘✔✘✘✘ CVE-2026-93790         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-93790
  │ ✘✔✘✘✘ CVE-2026-93793         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-93793
  │ ✘✔✘✘✘ CVE-2026-93796         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93796
  │ ✘✔✘✘✘ CVE-2026-93798         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93798
  │ ✘✔✘✘✘ CVE-2026-93799         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93799
  │ ✘✔✘✘✘ CVE-2026-93801         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93801
  │ ✘✔✘✘✘ CVE-2026-93806         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-93806
  │ ✘✔✘✘✘ CVE-2026-93810         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93810
  │ ✘✔✘✘✘ CVE-2026-93813         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93813
  │ ✘✔✘✘✘ CVE-2026-93816         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93816
  │ ✘✔✘✘✘ CVE-2026-93817         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93817
  │ ✘✔✘✘✘ CVE-2026-93826         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93826
  │ ✘✔✘✘✘ CVE-2026-93827         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93827
  │ ✘✔✘✘✘ CVE-2026-93830         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-93830
  │ ✘✔✘✘✘ CVE-2026-97409         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97409
  │ ✘✔✘✘✘ CVE-2026-97415         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97415
  │ ✘✔✘✘✘ CVE-2026-97417         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-97417
  │ ✘✔✘✘✘ CVE-2026-97421         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97421
  │ ✘✔✘✘✘ CVE-2026-97428         HIGH         7.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97428
  │ ✘✔✘✘✘ CVE-2026-97429         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97429
  │ ✘✔✘✘✘ CVE-2026-97433         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97433
  │ ✘✔✘✘✘ CVE-2026-97437         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97437
  │ ✘✔✘✘✘ CVE-2026-97438         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97438
  │ ✘✔✘✘✘ CVE-2026-97442         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97442
  │ ✘✔✘✘✘ CVE-2026-97444         HIGH         7.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97444
  │ ✘✔✘✘✘ CVE-2026-97445         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97445
  │ ✘✔✘✘✘ CVE-2026-97448         HIGH         7.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97448
  │ ✘✔✘✘✘ CVE-2026-97450         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97450
  │ ✘✔✘✘✘ CVE-2026-97451         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97451
  │ ✘✔✘✘✘ CVE-2026-97452         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97452
  │ ✘✔✘✘✘ CVE-2026-97454         HIGH         7.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97454
  │ ✘✔✘✘✘ CVE-2026-97455         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97455
  │ ✘✔✘✘✘ CVE-2026-97474         HIGH         7.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97474
  │ ✘✔✘✘✘ CVE-2026-97478         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97478
  │ ✘✔✘✘✘ CVE-2026-97496         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97496
  │ ✘✔✘✘✘ CVE-2026-97497         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97497
  │ ✘✔✘✘✘ CVE-2026-97508         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97508
  │ ✘✔✘✘✘ CVE-2026-97509         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97509
  │ ✘✔✘✘✘ CVE-2026-97513         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97513
  │ ✘✔✘✘✘ CVE-2026-97520         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97520
  │ ✘✔✘✘✘ CVE-2026-97523         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-97523
  │ ✘✔✘✘✘ CVE-2026-97524         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-97524
  │ ✘✔✘✘✘ CVE-2026-97527         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97527
  │ ✘✔✘✘✘ CVE-2026-97528         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97528
  │ ✘✔✘✘✘ CVE-2026-97531         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97531
  │ ✘✔✘✘✘ CVE-2026-97536         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97536
  │ ✘✔✘✘✘ CVE-2026-97555         HIGH         8.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-97555
  │ ✘✔✘✘✘ CVE-2026-97557         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-97557
  │ ✘✔✘✘✘ CVE-2026-97562         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-97562
  │ ✘✔✘✘✘ CVE-2026-97573         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-97573
  │ ✘✔✘✘✘ CVE-2026-97575         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97575
  │ ✘✔✘✘✘ CVE-2026-97576         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97576
  │ ✘✔✘✘✘ CVE-2026-97577         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97577
  │ ✘✔✘✘✘ CVE-2026-97578         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97578
  │ ✘✔✘✘✘ CVE-2026-97579         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97579
  │ ✘✔✘✘✘ CVE-2026-97583         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-97583
  │ ✘✔✘✘✘ CVE-2026-97584         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97584
  │ ✘✔✘✘✘ CVE-2026-97594         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97594
  │ ✘✔✘✘✘ CVE-2026-97595         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97595
  │ ✘✔✘✘✘ CVE-2026-97602         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97602
  │ ✘✔✘✘✘ CVE-2026-97608         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97608
  │ ✘✔✘✘✘ CVE-2026-97609         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97609
  │ ✘✔✘✘✘ CVE-2026-97611         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97611
  │ ✘✔✘✘✘ CVE-2026-97612         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97612
  │ ✘✔✘✘✘ CVE-2026-97910         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97910
  │ ✘✔✘✘✘ CVE-2026-97926         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97926
  │ ✘✔✘✘✘ CVE-2026-97931         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97931
  │ ✘✔✘✘✘ CVE-2026-97940         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97940
  │ ✘✔✘✘✘ CVE-2026-97953         HIGH         7.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-97953
  │ ✘✔✘✘✘ CVE-2026-97957         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97957
  │ ✘✔✘✘✘ CVE-2026-97990         HIGH         7.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97990
  │ ✘✔✘✘✘ CVE-2026-97991         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97991
  │ ✘✔✘✘✘ CVE-2026-98017         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98017
  │ ✘✔✘✘✘ CVE-2026-98023         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98023
  │ ✘✔✘✘✘ CVE-2026-98027         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98027
  │ ✘✔✘✘✘ CVE-2026-98029         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98029
  │ ✘✔✘✘✘ CVE-2026-98030         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98030
  │ ✘✔✘✘✘ CVE-2026-98041         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98041
  │ ✘✔✘✘✘ CVE-2026-98052         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98052
  │ ✘✔✘✘✘ CVE-2026-98056         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-98056
  │ ✘✔✘✘✘ CVE-2026-98069         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-98069
  │ ✘✔✘✘✘ CVE-2026-98070         HIGH         8.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-98070
  │ ✘✔✘✘✘ CVE-2026-98073         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98073
  │ ✘✔✘✘✘ CVE-2026-98083         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98083
  │ ✘✔✘✘✘ CVE-2026-98096         HIGH         7.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-98096
  │ ✘✔✘✘✘ CVE-2026-98108         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98108
  │ ✘✔✘✘✘ CVE-2026-98111         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98111
  │ ✘✔✘✘✘ CVE-2026-98115         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-98115
  │ ✘✔✘✘✘ CVE-2026-98116         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98116
  │ ✘✔✘✘✘ CVE-2026-98122         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98122
  │ ✘✔✘✘✘ CVE-2026-98130         HIGH         8.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-98130
  │ ✘✔✘✘✘ CVE-2026-98154         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98154
  │ ✘✔✘✘✘ CVE-2026-98155         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98155
  │ ✘✔✘✘✘ CVE-2026-98156         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98156
  │ ✘✔✘✘✘ CVE-2026-98164         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98164
  │ ✘✔✘✘✘ CVE-2026-98169         HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-98169
  │ ✘✔✘✘✘ CVE-2026-98171         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-98171
  │ ✘✔✘✘✘ CVE-2026-98173         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-98173
  │ ✘✔✘✘✘ CVE-2026-98174         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-98174
  │ ✘✔✘✘✘ CVE-2026-98175         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-98175
  │ ✘✔✘✘✘ CVE-2026-98180         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98180
  │ ✘✔✘✘✘ CVE-2026-98197         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98197
  │ ✘✔✘✘✘ CVE-2026-98216         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98216
  │ ✘✔✘✘✘ CVE-2026-98229         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98229
  │ ✘✔✘✘✘ CVE-2026-98230         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98230
  │ ✘✔✘✘✘ CVE-2026-98239         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-98239
  │ ✘✔✘✘✘ CVE-2026-98241         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98241
  │ ✘✔✘✘✘ CVE-2026-98251         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98251
  │ ✘✔✘✘✘ CVE-2026-98252         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98252
  │ ✘✔✘✘✘ CVE-2026-98253         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98253
  │ ✘✔✘✘✘ CVE-2026-98254         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98254
  │ ✘✔✘✘✘ CVE-2026-98257         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-98257
  │ ✘✔✘✘✘ CVE-2026-98260         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98260
  │ ✘✔✘✘✘ CVE-2026-98261         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-98261
  │ ✘✔✘✘✘ CVE-2026-98276         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98276
  │ ✘✔✘✘✘ CVE-2026-98282         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98282
  │ ✘✔✘✘✘ CVE-2026-98283         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98283
  │ ✘✔✘✘✘ CVE-2026-98290         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98290
  │ ✘✔✘✘✘ CVE-2026-98311         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98311
  │ ✘✔✘✘✘ CVE-2026-98320         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98320
  │ ✘✔✘✘✘ CVE-2026-98330         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98330
  │ ✘✔✘✘✘ CVE-2026-98331         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98331
  │ ✘✔✘✘✘ CVE-2026-98339         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-98339
  │ ✘✔✘✘✘ CVE-2026-98341         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98341
  │ ✘✔✘✘✘ CVE-2026-98348         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98348
  │ ✘✔✘✘✘ CVE-2026-98349         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98349
  │ ✘✔✘✘✘ CVE-2026-98357         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-98357
  │ ✘✔✘✘✘ CVE-2026-98359         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98359
  │ ✘✔✘✘✘ CVE-2026-98360         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98360
  │ ✘✔✘✘✘ CVE-2026-98364         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98364
  │ ✘✔✘✘✘ CVE-2026-98366         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98366
  │ ✘✔✘✘✘ CVE-2026-98367         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98367
  │ ✘✔✘✘✘ CVE-2026-98368         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98368
  │ ✘✔✘✘✘ CVE-2026-98369         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98369
  │ ✘✔✘✘✘ CVE-2026-98374         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-98374
  │ ✘✔✘✘✘ CVE-2026-98378         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98378
  │ ✘✔✘✘✘ CVE-2026-98381         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98381
  │ ✘✔✘✘✘ CVE-2026-98382         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98382
  │ ✘✔✘✘✘ CVE-2026-98383         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98383
  │ ✘✔✘✘✘ CVE-2026-98401         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-98401
  │ ✘✔✘✘✘ CVE-2026-98419         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98419
  │ ✘✔✘✘✘ CVE-2026-98436         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98436
  │ ✘✔✘✘✘ CVE-2026-98441         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98441
  │ ✘✔✘✘✘ CVE-2026-98442         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98442
  │ ✘✔✘✘✘ CVE-2026-98443         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98443
  │ ✘✔✘✘✘ CVE-2026-98451         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-98451
  │ ✘✔✘✘✘ CVE-2026-98454         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-98454
  │ ✘✔✘✘✘ CVE-2026-98456         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98456
  │ ✘✔✘✘✘ CVE-2026-98465         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98465
  │ ✘✔✘✘✘ CVE-2026-98466         HIGH         8.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98466
  │ ✘✔✘✘✘ CVE-2026-98471         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98471
  │ ✘✔✘✘✘ CVE-2026-98479         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-98479
  │ ✘✔✘✘✘ CVE-2026-98485         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98485
  │ ✘✔✘✘✘ CVE-2026-98487         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98487
  │ ✘✔✘✘✘ CVE-2026-98491         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98491
  │ ✘✔✘✘✘ CVE-2026-98499         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-98499
  │ ✘✔✘✘✘ CVE-2026-98501         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-98501
  │ ✘✔✘✘✘ CVE-2026-98507         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98507
  │ ✘✔✘✘✘ CVE-2026-98510         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98510
  │ ✘✔✘✘✘ CVE-2026-98512         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98512
  │ ✘✔✘✘✘ CVE-2026-98515         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98515
  │ ✘✔✘✘✘ CVE-2026-98517         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98517
  │ ✘✔✘✘✘ CVE-2026-98524         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98524
  │ ✘✔✘✘✘ CVE-2026-98532         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-98532
  │ ✘✔✘✘✘ CVE-2026-98550         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-98550
  │ ✘✔✘✘✘ CVE-2026-98555         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-98555
  │ ✘✔✘✘✘ CVE-2026-98889         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98889
  │ ✘✔✘✘✘ CVE-2026-98895         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98895
  │ ✘✔✘✘✘ CVE-2026-98899         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98899
  │ ✘✔✘✘✘ CVE-2026-98911         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-98911
  │ ✘✔✘✘✘ CVE-2026-98932         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98932
  │ ✘✔✘✘✘ CVE-2026-98944         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98944
  │ ✘✔✘✘✘ CVE-2026-98945         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98945
  │ ✘✔✘✘✘ CVE-2026-98964         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-98964
  │ ✘✔✘✘✘ CVE-2026-98968         HIGH         8.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-98968
  │ ✘✔✘✘✘ CVE-2026-98975         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98975
  │ ✘✔✘✘✘ CVE-2026-98978         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98978
  │ ✘✔✘✘✘ CVE-2026-98980         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98980
  │ ✘✔✘✘✘ CVE-2026-98981         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98981
  │ ✘✔✘✘✘ CVE-2026-98993         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98993
  │ ✘✔✘✘✘ CVE-2026-98999         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98999
  │ ✘✔✘✘✘ CVE-2026-99002         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99002
  │ ✘✔✘✘✘ CVE-2026-99006         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99006
  │ ✘✔✘✘✘ CVE-2026-99012         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99012
  │ ✘✔✘✘✘ CVE-2026-99013         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99013
  │ ✘✔✘✘✘ CVE-2026-99014         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99014
  │ ✘✔✘✘✘ CVE-2026-99018         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99018
  │ ✘✔✘✘✘ CVE-2026-99032         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99032
  │ ✘✔✘✘✘ CVE-2026-99053         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99053
  │ ✘✔✘✘✘ CVE-2026-99054         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99054
  │ ✘✔✘✘✘ CVE-2026-99056         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99056
  │ ✘✔✘✘✘ CVE-2026-99059         HIGH         7.7   0.5%   ·  ↳ S:UBUNTU-CVE-2026-99059
  │ ✘✔✘✘✘ CVE-2026-99077         HIGH         7.4   0.4%   ·  ↳ S:UBUNTU-CVE-2026-99077
  │ ✘✔✘✘✘ CVE-2026-99081         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-99081
  │ ✘✔✘✘✘ CVE-2026-99082         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99082
  │ ✘✔✘✘✘ CVE-2026-99083         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-99083
  │ ✘✔✘✘✘ CVE-2026-99109         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99109
  │ ✘✔✘✘✘ CVE-2026-99110         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99110
  │ ✘✔✘✘✘ CVE-2026-99112         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99112
  │ ✘✔✘✘✘ CVE-2026-99117         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99117
  │ ✘✔✘✘✘ CVE-2026-99122         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99122
  │ ✘✔✘✘✘ CVE-2026-99123         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99123
  │ ✘✔✘✘✘ CVE-2026-99131         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-99131
  │ ✘✔✘✘✘ CVE-2026-99136         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99136
  │ ✘✔✘✘✘ CVE-2026-99142         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99142
  │ ✘✔✘✘✘ CVE-2026-99143         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99143
  │ ✘✔✘✘✘ CVE-2026-99152         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-99152
  │ ✘✔✘✘✘ CVE-2026-99156         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99156
  │ ✘✔✘✘✘ CVE-2026-99163         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99163
  │ ✘✔✘✘✘ CVE-2026-99167         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99167
  │ ✘✔✘✘✘ CVE-2026-99173         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99173
  │ ✘✔✘✘✘ CVE-2026-99180         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99180
  │ ✘✔✘✘✘ CVE-2026-99203         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99203
  │ ✘✔✘✘✘ CVE-2026-99212         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99212
  │ ✘✔✘✘✘ CVE-2026-99213         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99213
  │ ✘✔✘✘✘ CVE-2026-99216         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99216
  │ ✘✔✘✘✘ CVE-2012-4542          MEDIUM       4.6   0.3%   ·  ↳ S:UBUNTU-CVE-2012-4542
  │ ✘✔✘✘✘ CVE-2015-7837          MEDIUM       5.5   0.4%   ·  ↳ S:UBUNTU-CVE-2015-7837
  │ ✘✔✘✘✘ CVE-2016-8660          MEDIUM       5.5   0.4%   ·  ↳ S:UBUNTU-CVE-2016-8660
  │ ✘✔✘✘✘ CVE-2017-0537          MEDIUM       4.7   1.0%   ·  ↳ S:UBUNTU-CVE-2017-0537
  │ ✘✔✘✘✘ CVE-2017-13693         MEDIUM       5.5   0.4%   ·  ↳ S:UBUNTU-CVE-2017-13693
  │ ✘✔✘✘✘ CVE-2017-13694         MEDIUM       5.5   0.4%   ·  ↳ S:UBUNTU-CVE-2017-13694
  │ ✘✔✘✘✘ CVE-2018-1121          MEDIUM       5.9   4.1%   ·  ↳ S:UBUNTU-CVE-2018-1121
  │ ✘✔✘✘✘ CVE-2018-12928         MEDIUM       5.5   0.4%   ·  ↳ S:UBUNTU-CVE-2018-12928
  │ ✘✔✘✘✘ CVE-2018-12929         MEDIUM       5.5   0.4%   ·  ↳ S:UBUNTU-CVE-2018-12929
  │ ✘✔✘✘✘ CVE-2018-17977         MEDIUM       4.9   0.4%   ·  ↳ S:UBUNTU-CVE-2018-17977
  │ ✘✔✘✘✘ CVE-2019-15213         MEDIUM       4.9   0.7%   ·  ↳ S:UBUNTU-CVE-2019-15213
  │ ✘✔✘✘✘ CVE-2019-20794         MEDIUM       4.7   0.5%   ·  ↳ S:UBUNTU-CVE-2019-20794
  │ ✘✔✘✘✘ CVE-2020-11935         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2020-11935
  │ ✘✔✘✘✘ CVE-2020-14304         MEDIUM       4.4   0.4%   ·  ↳ S:UBUNTU-CVE-2020-14304
  │ ✘✔✘✘✘ CVE-2020-15802         MEDIUM       5.9   7.1%   ·  ↳ S:UBUNTU-CVE-2020-15802
  │ ✘✔✘✘✘ CVE-2020-26140         MEDIUM       6.5   2.9%   ·  ↳ S:UBUNTU-CVE-2020-26140
  │ ✘✔✘✘✘ CVE-2020-26142         MEDIUM       5.3   2.1%   ·  ↳ S:UBUNTU-CVE-2020-26142
  │ ✘✔✘✘✘ CVE-2020-26143         MEDIUM       6.5   4.2%   ·  ↳ S:UBUNTU-CVE-2020-26143
  │ ✘✔✘✘✘ CVE-2020-26146         MEDIUM       5.3   5.6%   ·  ↳ S:UBUNTU-CVE-2020-26146
  │ ✘✔✘✘✘ CVE-2021-31615         MEDIUM       5.3   0.4%   ·  ↳ S:UBUNTU-CVE-2021-31615
  │ ✘✔✘✘✘ CVE-2021-3714          MEDIUM       5.9   1.6%   ·  ↳ S:UBUNTU-CVE-2021-3714
  │ ✘✔✘✘✘ CVE-2022-0480          MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-0480
  │ ✘✔✘✘✘ CVE-2022-41848         MEDIUM       4.2   0.3%   ·  ↳ S:UBUNTU-CVE-2022-41848
  │ ✘✔✘✘✘ CVE-2022-44034         MEDIUM       6.4   0.3%   ·  ↳ S:UBUNTU-CVE-2022-44034
  │ ✘✔✘✘✘ CVE-2022-4543          MEDIUM       5.5   1.0%   ·  ↳ S:UBUNTU-CVE-2022-4543
  │ ✘✔✘✘✘ CVE-2022-48846         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48846
  │ ✘✔✘✘✘ CVE-2022-48929         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48929
  │ ✘✔✘✘✘ CVE-2022-49940         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49940
  │ ✘✔✘✘✘ CVE-2022-50230         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50230
  │ ✘✔✘✘✘ CVE-2022-50232         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50232
  │ ✘✔✘✘✘ CVE-2022-50380         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50380
  │ ✘✔✘✘✘ CVE-2023-0160          MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2023-0160
  │ ✘✔✘✘✘ CVE-2023-1193          MEDIUM       6.5   1.0%   ·  ↳ S:UBUNTU-CVE-2023-1193
  │ ✘✔✘✘✘ CVE-2023-20585         MEDIUM       5.6   0.1%   ·  ↳ S:UBUNTU-CVE-2023-20585,USN-8917-1
  │ ✘✔✘✘✘ CVE-2023-31082         MEDIUM       5.5   0.4%   ·  ↳ S:UBUNTU-CVE-2023-31082
  │ ✘✔✘✘✘ CVE-2023-53642         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53642
  │ ✘✔✘✘✘ CVE-2023-6238          MEDIUM       6.7   0.3%   ·  ↳ S:UBUNTU-CVE-2023-6238
  │ ✘✔✘✘✘ CVE-2023-6240          MEDIUM       6.5   1.0%   ·  ↳ S:UBUNTU-CVE-2023-6240
  │ ✘✔✘✘✘ CVE-2024-0564          MEDIUM       6.5   0.6%   ·  ↳ S:UBUNTU-CVE-2024-0564
  │ ✘✔✘✘✘ CVE-2024-14027         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-14027
  │ ✘✔✘✘✘ CVE-2024-2193          MEDIUM       5.7   1.3%   ·  ↳ S:UBUNTU-CVE-2024-2193
  │ ✘✔✘✘✘ CVE-2024-24864         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2024-24864
  │ ✘✔✘✘✘ CVE-2024-25740         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-25740
  │ ✘✔✘✘✘ CVE-2024-27025         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-27025
  │ ✘✔✘✘✘ CVE-2024-35895         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35895
  │ ✘✔✘✘✘ CVE-2024-35995         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35995
  │ ✘✔✘✘✘ CVE-2024-42107         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2024-42107
  │ ✘✔✘✘✘ CVE-2024-42139         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-42139
  │ ✘✔✘✘✘ CVE-2024-46742         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-46742
  │ ✘✔✘✘✘ CVE-2024-47729         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-47729
  │ ✘✔✘✘✘ CVE-2024-49908         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49908
  │ ✘✔✘✘✘ CVE-2024-49910         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49910
  │ ✘✔✘✘✘ CVE-2024-49916         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49916
  │ ✘✔✘✘✘ CVE-2024-49970         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-49970
  │ ✘✔✘✘✘ CVE-2024-49990         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49990
  │ ✘✔✘✘✘ CVE-2024-50003         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50003
  │ ✘✔✘✘✘ CVE-2024-50102         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50102
  │ ✘✔✘✘✘ CVE-2024-53056         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53056
  │ ✘✔✘✘✘ CVE-2024-53064         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53064
  │ ✘✔✘✘✘ CVE-2024-56544         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-56544
  │ ✘✔✘✘✘ CVE-2024-56617         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56617
  │ ✘✔✘✘✘ CVE-2024-56702         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56702
  │ ✘✔✘✘✘ CVE-2024-56712         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56712
  │ ✘✔✘✘✘ CVE-2024-57809         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-57809
  │ ✘✔✘✘✘ CVE-2024-57922         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-57922
  │ ✘✔✘✘✘ CVE-2024-58012         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-58012
  │ ✘✔✘✘✘ CVE-2024-58095         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-58095
  │ ✘✔✘✘✘ CVE-2025-12801         MEDIUM       6.5   0.5%   ·  ↳ S:UBUNTU-CVE-2025-12801
  │ ✘✔✘✘✘ CVE-2025-21696         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-21696
  │ ✘✔✘✘✘ CVE-2025-21752         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21752
  │ ✘✔✘✘✘ CVE-2025-21907         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21907
  │ ✘✔✘✘✘ CVE-2025-22002         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22002
  │ ✘✔✘✘✘ CVE-2025-22127         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22127
  │ ✘✔✘✘✘ CVE-2025-23131         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-23131,USN-8917-1
  │ ✘✔✘✘✘ CVE-2025-23135         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-23135
  │ ✘✔✘✘✘ CVE-2025-23162         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-23162
  │ ✘✔✘✘✘ CVE-2025-37743         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37743
  │ ✘✔✘✘✘ CVE-2025-37746         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37746
  │ ✘✔✘✘✘ CVE-2025-37747         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37747
  │ ✘✔✘✘✘ CVE-2025-37806         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37806
  │ ✘✔✘✘✘ CVE-2025-37807         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37807
  │ ✘✔✘✘✘ CVE-2025-37833         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37833
  │ ✘✔✘✘✘ CVE-2025-37834         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37834
  │ ✘✔✘✘✘ CVE-2025-37870         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37870
  │ ✘✔✘✘✘ CVE-2025-37880         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37880
  │ ✘✔✘✘✘ CVE-2025-37907         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37907
  │ ✘✔✘✘✘ CVE-2025-38029         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38029
  │ ✘✔✘✘✘ CVE-2025-38036         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38036
  │ ✘✔✘✘✘ CVE-2025-38038         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38038
  │ ✘✔✘✘✘ CVE-2025-38041         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38041
  │ ✘✔✘✘✘ CVE-2025-38042         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38042
  │ ✘✔✘✘✘ CVE-2025-38096         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38096
  │ ✘✔✘✘✘ CVE-2025-38132         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38132
  │ ✘✔✘✘✘ CVE-2025-38140         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38140
  │ ✘✔✘✘✘ CVE-2025-38188         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38188
  │ ✘✔✘✘✘ CVE-2025-38199         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38199
  │ ✘✔✘✘✘ CVE-2025-38203         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38203
  │ ✘✔✘✘✘ CVE-2025-38205         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38205
  │ ✘✔✘✘✘ CVE-2025-38207         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38207
  │ ✘✔✘✘✘ CVE-2025-38237         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38237
  │ ✘✔✘✘✘ CVE-2025-38272         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38272
  │ ✘✔✘✘✘ CVE-2025-38311         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-38311
  │ ✘✔✘✘✘ CVE-2025-38353         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-38353
  │ ✘✔✘✘✘ CVE-2025-38359         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38359
  │ ✘✔✘✘✘ CVE-2025-38360         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38360
  │ ✘✔✘✘✘ CVE-2025-38438         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38438
  │ ✘✔✘✘✘ CVE-2025-38597         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38597
  │ ✘✔✘✘✘ CVE-2025-38605         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38605
  │ ✘✔✘✘✘ CVE-2025-38621         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38621
  │ ✘✔✘✘✘ CVE-2025-39754         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39754
  │ ✘✔✘✘✘ CVE-2025-39762         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39762
  │ ✘✔✘✘✘ CVE-2025-39833         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39833
  │ ✘✔✘✘✘ CVE-2025-39910         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39910
  │ ✘✔✘✘✘ CVE-2025-39925         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39925
  │ ✘✔✘✘✘ CVE-2025-68211         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-68211
  │ ✘✔✘✘✘ CVE-2025-71227         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71227
  │ ✘✔✘✘✘ CVE-2025-71285         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71285
  │ ✘✔✘✘✘ CVE-2025-71313         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71313
  │ ✘✔✘✘✘ CVE-2025-71315         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71315
  │ ✘✔✘✘✘ CVE-2026-100070        MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-100070
  │ ✘✔✘✘✘ CVE-2026-100071        MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-100071
  │ ✘✔✘✘✘ CVE-2026-100074        MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-100074
  │ ✘✔✘✘✘ CVE-2026-100076        MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-100076
  │ ✘✔✘✘✘ CVE-2026-100077        MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-100077
  │ ✘✔✘✘✘ CVE-2026-100078        MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-100078
  │ ✘✔✘✘✘ CVE-2026-100079        MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-100079
  │ ✘✔✘✘✘ CVE-2026-23017         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23017
  │ ✘✔✘✘✘ CVE-2026-23137         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23137
  │ ✘✔✘✘✘ CVE-2026-23152         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23152
  │ ✘✔✘✘✘ CVE-2026-23201         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23201
  │ ✘✔✘✘✘ CVE-2026-23217         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23217
  │ ✘✔✘✘✘ CVE-2026-23247         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23247
  │ ✘✔✘✘✘ CVE-2026-23265         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23265
  │ ✘✔✘✘✘ CVE-2026-23346         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23346,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-23348         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23348
  │ ✘✔✘✘✘ CVE-2026-23371         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23371
  │ ✘✔✘✘✘ CVE-2026-23377         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23377
  │ ✘✔✘✘✘ CVE-2026-23385         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23385
  │ ✘✔✘✘✘ CVE-2026-23469         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23469,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-23472         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23472
  │ ✘✔✘✘✘ CVE-2026-31410         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31410
  │ ✘✔✘✘✘ CVE-2026-31420         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31420,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-31462         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31462
  │ ✘✔✘✘✘ CVE-2026-31526         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31526
  │ ✘✔✘✘✘ CVE-2026-31531         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31531
  │ ✘✔✘✘✘ CVE-2026-31537         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31537
  │ ✘✔✘✘✘ CVE-2026-31560         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31560,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-31579         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31579
  │ ✘✔✘✘✘ CVE-2026-31592         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31592
  │ ✘✔✘✘✘ CVE-2026-31692         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31692
  │ ✘✔✘✘✘ CVE-2026-31777         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31777
  │ ✘✔✘✘✘ CVE-2026-43010         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43010,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-43022         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43022
  │ ✘✔✘✘✘ CVE-2026-43034         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43034
  │ ✘✔✘✘✘ CVE-2026-43053         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43053
  │ ✘✔✘✘✘ CVE-2026-43115         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43115
  │ ✘✔✘✘✘ CVE-2026-43118         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43118
  │ ✘✔✘✘✘ CVE-2026-43127         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43127
  │ ✘✔✘✘✘ CVE-2026-43161         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43161
  │ ✘✔✘✘✘ CVE-2026-43191         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43191
  │ ✘✔✘✘✘ CVE-2026-43204         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43204
  │ ✘✔✘✘✘ CVE-2026-43216         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43216,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-43219         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43219,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-43220         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43220
  │ ✘✔✘✘✘ CVE-2026-43229         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43229
  │ ✘✔✘✘✘ CVE-2026-43234         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43234
  │ ✘✔✘✘✘ CVE-2026-43240         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43240,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-43294         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43294
  │ ✘✔✘✘✘ CVE-2026-43298         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43298
  │ ✘✔✘✘✘ CVE-2026-43299         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43299
  │ ✘✔✘✘✘ CVE-2026-43301         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43301
  │ ✘✔✘✘✘ CVE-2026-43308         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43308
  │ ✘✔✘✘✘ CVE-2026-43309         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43309
  │ ✘✔✘✘✘ CVE-2026-43310         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43310
  │ ✘✔✘✘✘ CVE-2026-43311         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43311,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-43331         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43331,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-43344         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43344
  │ ✘✔✘✘✘ CVE-2026-43410         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43410
  │ ✘✔✘✘✘ CVE-2026-43416         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43416
  │ ✘✔✘✘✘ CVE-2026-43443         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43443
  │ ✘✔✘✘✘ CVE-2026-43463         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43463
  │ ✘✔✘✘✘ CVE-2026-43485         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43485
  │ ✘✔✘✘✘ CVE-2026-45850         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45850,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-45897         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45897,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-45901         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45901,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-45930         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45930,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-45934         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45934
  │ ✘✔✘✘✘ CVE-2026-45940         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45940
  │ ✘✔✘✘✘ CVE-2026-45949         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45949
  │ ✘✔✘✘✘ CVE-2026-45961         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45961
  │ ✘✔✘✘✘ CVE-2026-45963         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45963
  │ ✘✔✘✘✘ CVE-2026-46014         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46014
  │ ✘✔✘✘✘ CVE-2026-46032         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46032
  │ ✘✔✘✘✘ CVE-2026-46059         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46059
  │ ✘✔✘✘✘ CVE-2026-46066         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46066
  │ ✘✔✘✘✘ CVE-2026-46071         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46071
  │ ✘✔✘✘✘ CVE-2026-46147         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46147
  │ ✘✔✘✘✘ CVE-2026-46148         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46148
  │ ✘✔✘✘✘ CVE-2026-46153         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46153
  │ ✘✔✘✘✘ CVE-2026-46158         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46158,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-46170         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46170,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-46171         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46171
  │ ✘✔✘✘✘ CVE-2026-46245         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-46245
  │ ✘✔✘✘✘ CVE-2026-46252         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46252,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-46272         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46272
  │ ✘✔✘✘✘ CVE-2026-46302         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46302
  │ ✘✔✘✘✘ CVE-2026-46315         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46315,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-52913         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52913,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-52916         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52916,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-52921         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52921,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-52926         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52926,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-52928         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52928,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-52930         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52930,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-52937         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52937
  │ ✘✔✘✘✘ CVE-2026-52939         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52939,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-52941         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52941,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-52944         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52944,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-52948         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52948,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-52972         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52972
  │ ✘✔✘✘✘ CVE-2026-52994         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52994
  │ ✘✔✘✘✘ CVE-2026-53017         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53017
  │ ✘✔✘✘✘ CVE-2026-53018         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53018
  │ ✘✔✘✘✘ CVE-2026-53027         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53027,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53080         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53080,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53102         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53102
  │ ✘✔✘✘✘ CVE-2026-53103         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53103
  │ ✘✔✘✘✘ CVE-2026-53104         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53104
  │ ✘✔✘✘✘ CVE-2026-53106         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53106
  │ ✘✔✘✘✘ CVE-2026-53107         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53107
  │ ✘✔✘✘✘ CVE-2026-53108         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53108
  │ ✘✔✘✘✘ CVE-2026-53113         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53113
  │ ✘✔✘✘✘ CVE-2026-53134         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53134,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53135         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53135,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53139         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53139
  │ ✘✔✘✘✘ CVE-2026-53140         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53140,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53142         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53142
  │ ✘✔✘✘✘ CVE-2026-53144         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53144,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53150         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53150,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53154         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53154,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53158         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53158,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53163         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53163,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53167         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53167,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53168         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53168,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53177         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53177,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53181         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53181,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53190         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53190,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53196         MEDIUM       6.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53196,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53207         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53207
  │ ✘✔✘✘✘ CVE-2026-53208         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53208,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53210         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53210,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53213         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53213,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53214         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53214,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53218         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53218,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53219         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53219,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53220         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53220,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53226         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53226,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53227         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53227,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53236         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53236,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53237         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53237,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53238         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53238,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53245         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53245,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53249         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53249,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53251         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53251,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53252         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53252,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53258         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53258
  │ ✘✔✘✘✘ CVE-2026-53261         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53261,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53263         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53263,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53269         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53269,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53274         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53274,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53285         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53285
  │ ✘✔✘✘✘ CVE-2026-53292         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53292
  │ ✘✔✘✘✘ CVE-2026-53297         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53297
  │ ✘✔✘✘✘ CVE-2026-53313         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53313
  │ ✘✔✘✘✘ CVE-2026-53317         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53317
  │ ✘✔✘✘✘ CVE-2026-53325         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53325,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53327         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53327,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53331         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53331,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53332         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53332,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53336         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53336,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53337         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53337,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53339         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53339,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53343         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53343,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53345         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53345,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53347         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53347,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53349         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53349,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53350         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53350,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53352         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53352,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53353         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53353,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-53377         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53377
  │ ✘✔✘✘✘ CVE-2026-53382         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53382,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53385         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53385,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53393         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53393,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-53403         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53403,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63798         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63798,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63868         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63868,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63876         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63876,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63877         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63877,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63897         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63897,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63900         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63900,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63908         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63908,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63931         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63931,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63933         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63933,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63948         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63948,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63958         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63958,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63959         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63959,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63960         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63960,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63961         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63961,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63962         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63962
  │ ✘✔✘✘✘ CVE-2026-63963         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63963
  │ ✘✔✘✘✘ CVE-2026-63964         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63964,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63973         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63973,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63990         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63990,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63991         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63991,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63999         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63999
  │ ✘✔✘✘✘ CVE-2026-64006         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64006,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64012         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64012,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64022         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64022
  │ ✘✔✘✘✘ CVE-2026-64038         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64038
  │ ✘✔✘✘✘ CVE-2026-64052         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64052
  │ ✘✔✘✘✘ CVE-2026-64060         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64060
  │ ✘✔✘✘✘ CVE-2026-64064         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64064,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64070         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64070
  │ ✘✔✘✘✘ CVE-2026-64079         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64079
  │ ✘✔✘✘✘ CVE-2026-64083         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64083,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64087         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64087,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64090         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64090,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64092         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64092,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64094         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64094,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64127         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64127,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64128         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64128,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64131         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64131,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64135         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64135,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64144         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64144,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64146         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64146
  │ ✘✔✘✘✘ CVE-2026-64147         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64147,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64154         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64154
  │ ✘✔✘✘✘ CVE-2026-64155         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64155,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64163         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64163,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64165         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64165,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64166         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64166,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64168         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64168,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64170         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64170,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64173         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64173,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64174         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64174,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64177         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64177,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64179         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64179,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64180         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64180,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64182         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64182,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64183         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64183,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64184         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64184,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64185         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64185,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64187         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64187,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64190         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64190
  │ ✘✔✘✘✘ CVE-2026-64192         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64192,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64205         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64205,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64213         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64213
  │ ✘✔✘✘✘ CVE-2026-64214         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64214,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64220         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64220,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64227         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64227
  │ ✘✔✘✘✘ CVE-2026-64231         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64231,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64233         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64233,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64234         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64234,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64240         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64240,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64241         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64241,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64244         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64244,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64254         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64254,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64256         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64256,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64275         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64275,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64289         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64289,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64294         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64294,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64297         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64297,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64301         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64301,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64306         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64306,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64316         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64316,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64321         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64321,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64326         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64326,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64331         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64331,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64332         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64332,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64334         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64334,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64335         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64335,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64336         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64336,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64337         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64337,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64338         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64338,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64345         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64345,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64347         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64347,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64350         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64350,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64351         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64351,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64358         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64358,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64359         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64359,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64360         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64360,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64369         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64369,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64370         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64370,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64371         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64371,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64373         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64373,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64376         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64376,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64404         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64404,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64405         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64405,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64409         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64409,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64417         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64417,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64419         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64419,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64425         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64425,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64428         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64428,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64429         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64429,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-98051         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98051
  │ ✘✔✘✘✘ CVE-2026-98054         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98054
  │ ✘✔✘✘✘ CVE-2026-98078         MEDIUM       4.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98078
  │ ✘✔✘✘✘ CVE-2026-98080         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98080
  │ ✘✔✘✘✘ CVE-2026-98082         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98082
  │ ✘✔✘✘✘ CVE-2026-98090         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98090
  │ ✘✔✘✘✘ CVE-2026-98091         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98091
  │ ✘✔✘✘✘ CVE-2026-98092         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98092
  │ ✘✔✘✘✘ CVE-2026-98094         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98094
  │ ✘✔✘✘✘ CVE-2026-98095         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98095
  │ ✘✔✘✘✘ CVE-2026-98097         MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-98097
  │ ✘✔✘✘✘ CVE-2026-98098         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98098
  │ ✘✔✘✘✘ CVE-2026-98099         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98099
  │ ✘✔✘✘✘ CVE-2026-98109         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98109
  │ ✘✔✘✘✘ CVE-2026-98113         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98113
  │ ✘✔✘✘✘ CVE-2026-98114         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98114
  │ ✘✔✘✘✘ CVE-2026-98121         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98121
  │ ✘✔✘✘✘ CVE-2026-98123         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98123
  │ ✘✔✘✘✘ CVE-2026-98124         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98124
  │ ✘✔✘✘✘ CVE-2026-98125         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98125
  │ ✘✔✘✘✘ CVE-2026-98126         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98126
  │ ✘✔✘✘✘ CVE-2026-98127         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98127
  │ ✘✔✘✘✘ CVE-2026-98128         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98128
  │ ✘✔✘✘✘ CVE-2026-98129         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98129
  │ ✘✔✘✘✘ CVE-2026-98131         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98131
  │ ✘✔✘✘✘ CVE-2026-98134         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98134
  │ ✘✔✘✘✘ CVE-2026-98142         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98142
  │ ✘✔✘✘✘ CVE-2026-98148         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98148
  │ ✘✔✘✘✘ CVE-2026-98151         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98151
  │ ✘✔✘✘✘ CVE-2026-98152         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98152
  │ ✘✔✘✘✘ CVE-2026-98157         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98157
  │ ✘✔✘✘✘ CVE-2026-98158         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98158
  │ ✘✔✘✘✘ CVE-2026-98159         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98159
  │ ✘✔✘✘✘ CVE-2026-98160         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98160
  │ ✘✔✘✘✘ CVE-2026-98161         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98161
  │ ✘✔✘✘✘ CVE-2026-98162         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98162
  │ ✘✔✘✘✘ CVE-2020-35501         LOW          3.6   0.2%   ·  ↳ S:UBUNTU-CVE-2020-35501
  │ ✘✔✘✘✘ CVE-2024-39286         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2024-39286
  │ ✘✔✘✘✘ CVE-2022-50128         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-50128
  │ ✘✔✘✘✘ CVE-2023-54105         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54105
  │ ✘✔✘✘✘ CVE-2023-54190         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54190
  │ ✘✔✘✘✘ CVE-2024-35923         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2024-35923
  │ ✘✔✘✘✘ CVE-2024-37353         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2024-37353
  │ ✘✔✘✘✘ CVE-2024-38391         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2024-38391
  │ ✘✔✘✘✘ CVE-2025-40003         ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2025-40003
  │ ✘✔✘✘✘ CVE-2025-40065         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40065
  │ ✘✔✘✘✘ CVE-2025-40086         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40086
  │ ✘✔✘✘✘ CVE-2025-40097         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40097
  │ ✘✔✘✘✘ CVE-2025-40098         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40098,USN-8917-1
  │ ✘✔✘✘✘ CVE-2025-40102         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40102
  │ ✘✔✘✘✘ CVE-2025-40136         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40136
  │ ✘✔✘✘✘ CVE-2025-40146         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40146
  │ ✘✔✘✘✘ CVE-2025-40247         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40247
  │ ✘✔✘✘✘ CVE-2025-40338         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40338
  │ ✘✔✘✘✘ CVE-2025-40340         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40340
  │ ✘✔✘✘✘ CVE-2025-40355         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40355
  │ ✘✔✘✘✘ CVE-2025-68188         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68188
  │ ✘✔✘✘✘ CVE-2025-68209         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68209
  │ ✘✔✘✘✘ CVE-2025-68230         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68230
  │ ✘✔✘✘✘ CVE-2025-68236         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68236
  │ ✘✔✘✘✘ CVE-2025-68251         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68251
  │ ✘✔✘✘✘ CVE-2025-68296         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68296,USN-8903-1
  │ ✘✔✘✘✘ CVE-2025-68324         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68324
  │ ✘✔✘✘✘ CVE-2025-68338         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68338
  │ ✘✔✘✘✘ CVE-2025-68353         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68353
  │ ✘✔✘✘✘ CVE-2025-68356         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68356
  │ ✘✔✘✘✘ CVE-2025-68376         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68376
  │ ✘✔✘✘✘ CVE-2025-68729         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68729
  │ ✘✔✘✘✘ CVE-2025-68768         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68768,USN-8903-1
  │ ✘✔✘✘✘ CVE-2025-68781         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68781
  │ ✘✔✘✘✘ CVE-2025-68802         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68802
  │ ✘✔✘✘✘ CVE-2026-63810         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63810,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63811         ?            0.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63811
  │ ✘✔✘✘✘ CVE-2026-63821         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63821,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63822         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63822,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63826         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63826,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63834         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63834,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63835         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63835,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63836         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63836,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-63871         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63871,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63882         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63882,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63890         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63890,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63891         ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-63891,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63892         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63892,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63895         ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-63895,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63896         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63896,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63969         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63969,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-63983         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63983
  │ ✘✔✘✘✘ CVE-2026-64454         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64454,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64455         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64455,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64458         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64458,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64461         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64461,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64462         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64462,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64465         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64465,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64470         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64470,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64471         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64471,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64472         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64472,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64473         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64473,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64474         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64474,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64476         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64476,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64478         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64478,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64479         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64479,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64480         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64480,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64482         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64482,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64483         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64483,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64484         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64484,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64486         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64486,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64487         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64487,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64488         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64488,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64489         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64489,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64493         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64493,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64494         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64494,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64495         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64495,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64497         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64497,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64500         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64500,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64503         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64503,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64504         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64504,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64505         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64505,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64507         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64507,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64508         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64508,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64511         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64511,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64512         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64512,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64513         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64513
  │ ✘✔✘✘✘ CVE-2026-64514         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64514,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64518         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64518,USN-8729-1
  │ ✘✔✘✘✘ CVE-2026-64525         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64525,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64527         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64527,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64528         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64528,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-64537         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64537,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64538         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64538,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64542         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64542,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64544         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64544,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64549         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64549,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64553         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64553,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64565         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64565,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64569         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64569,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64571         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64571,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64572         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64572,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64573         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64573,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64579         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64579,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64590         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64590,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64593         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64593,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64594         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64594,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64602         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64602,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64603         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64603,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-64604         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64604,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68081         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68081
  │ ✘✔✘✘✘ CVE-2026-68084         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68084,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68086         ?            0.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68086
  │ ✘✔✘✘✘ CVE-2026-68088         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68088,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68090         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68090,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68093         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68093,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68099         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68099,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68102         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68102
  │ ✘✔✘✘✘ CVE-2026-68105         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68105
  │ ✘✔✘✘✘ CVE-2026-68109         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68109
  │ ✘✔✘✘✘ CVE-2026-68110         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68110,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68111         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68111,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68112         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68112,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68113         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68113
  │ ✘✔✘✘✘ CVE-2026-68114         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68114
  │ ✘✔✘✘✘ CVE-2026-68115         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68115,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68126         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68126,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68130         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68130,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68132         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68132
  │ ✘✔✘✘✘ CVE-2026-68135         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68135,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68139         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68139,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68146         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68146,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68150         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68150
  │ ✘✔✘✘✘ CVE-2026-68151         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68151,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68164         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68164,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68165         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68165,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68166         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68166
  │ ✘✔✘✘✘ CVE-2026-68169         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68169
  │ ✘✔✘✘✘ CVE-2026-68175         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68175,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68176         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68176,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68180         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68180,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68181         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68181,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68182         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68182,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68183         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68183,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68184         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68184,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68186         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68186,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68187         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68187,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68188         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68188,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68190         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68190,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68193         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68193,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68194         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68194,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68195         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68195,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68197         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68197,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68203         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68203,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68205         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68205,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68207         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68207,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68211         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68211
  │ ✘✔✘✘✘ CVE-2026-68212         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68212,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68214         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68214,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68215         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68215,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68217         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68217,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68218         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68218,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68220         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68220,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68221         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68221,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68223         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68223,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68225         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68225,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68226         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68226,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68227         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68227,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68231         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68231,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68233         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68233
  │ ✘✔✘✘✘ CVE-2026-68234         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68234,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68235         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68235,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68238         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68238
  │ ✘✔✘✘✘ CVE-2026-68241         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68241
  │ ✘✔✘✘✘ CVE-2026-68242         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68242
  │ ✘✔✘✘✘ CVE-2026-68243         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68243,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68244         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68244,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68246         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68246,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68247         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68247,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68248         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68248,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68249         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68249,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68250         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68250,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68251         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68251,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68252         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68252
  │ ✘✔✘✘✘ CVE-2026-68254         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68254
  │ ✘✔✘✘✘ CVE-2026-68256         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68256,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68259         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68259,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68261         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68261,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68269         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68269,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68271         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68271,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68272         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68272,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68277         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68277,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68278         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68278,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68279         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68279,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68280         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68280,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68281         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68281,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68286         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68286
  │ ✘✔✘✘✘ CVE-2026-68288         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68288
  │ ✘✔✘✘✘ CVE-2026-68289         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68289
  │ ✘✔✘✘✘ CVE-2026-68291         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68291
  │ ✘✔✘✘✘ CVE-2026-68301         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68301,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68303         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68303
  │ ✘✔✘✘✘ CVE-2026-68304         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68304,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68306         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68306,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68308         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68308,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68309         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68309,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68310         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68310,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68312         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68312
  │ ✘✔✘✘✘ CVE-2026-68313         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68313,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68317         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68317,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68318         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68318,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68319         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68319,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68322         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68322
  │ ✘✔✘✘✘ CVE-2026-68324         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68324,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68325         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68325,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68327         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68327,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68328         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68328,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68331         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68331,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68333         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68333,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68336         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68336,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68337         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68337
  │ ✘✔✘✘✘ CVE-2026-68339         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68339,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68346         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68346,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68349         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68349,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68350         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68350,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68351         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68351,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68355         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68355,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68357         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68357,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68359         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68359,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68360         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68360,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68361         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68361,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68362         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68362,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68363         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68363,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68365         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68365,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68366         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68366,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68367         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68367
  │ ✘✔✘✘✘ CVE-2026-68368         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68368,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68369         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68369,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68372         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68372,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68386         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68386,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68395         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68395,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68396         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68396,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68403         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68403,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68405         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68405,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68406         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68406,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68407         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68407,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68408         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68408,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68410         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68410,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68411         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68411,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68412         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68412
  │ ✘✔✘✘✘ CVE-2026-68413         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68413,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68416         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68416,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68418         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68418
  │ ✘✔✘✘✘ CVE-2026-68422         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68422,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68428         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68428,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68429         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68429,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68430         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68430,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68436         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68436
  │ ✘✔✘✘✘ CVE-2026-68437         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68437,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68439         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68439,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68441         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68441
  │ ✘✔✘✘✘ CVE-2026-68443         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68443,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68444         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68444,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68448         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68448
  │ ✘✔✘✘✘ CVE-2026-68449         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68449,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68450         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68450,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68456         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68456,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68459         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68459,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68460         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68460,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68469         ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68469,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68475         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68475,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68478         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68478,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-68480         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68480
  │ ✘✔✘✘✘ CVE-2026-72004         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72004,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72007         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72007,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72010         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72010,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72013         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72013,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72015         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72015,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72017         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72017,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72022         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72022,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72023         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72023,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72025         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72025,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72028         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72028,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72030         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72030,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72037         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72037,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72038         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72038,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72039         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72039,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72040         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72040,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72047         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72047,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72048         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72048,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72056         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72056,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72058         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72058,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72059         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72059,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72062         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72062,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72063         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72063,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72068         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72068,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72070         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72070,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72073         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72073
  │ ✘✔✘✘✘ CVE-2026-72074         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72074,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72075         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72075,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72076         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72076,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72077         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72077,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72078         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72078,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72079         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72079,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72081         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72081,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72082         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72082,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72086         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72086,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72087         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72087,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72088         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72088,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72096         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72096,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72097         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72097,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72106         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72106,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72117         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72117,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72118         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72118,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72127         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72127,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72132         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72132,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72138         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72138,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72140         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72140,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72142         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72142,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72147         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72147,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72152         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72152,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72153         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72153,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72155         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72155,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72156         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72156,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72158         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72158,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72159         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72159,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72161         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72161,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72163         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72163,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72166         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72166,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72167         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72167,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72168         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72168,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72174         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72174,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72176         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72176,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72177         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72177,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72179         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72179,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72182         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72182,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72193         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72193,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72212         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72212,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72214         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72214,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72215         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72215,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72216         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72216,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72218         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72218,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72219         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72219,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72223         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72223,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72224         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72224,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72228         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72228,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72229         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72229,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72230         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72230,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72236         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72236,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72237         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72237,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72238         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72238,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72240         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72240,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72241         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72241,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72245         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72245,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72256         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72256,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72257         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72257,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72258         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72258,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72259         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72259,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72260         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72260,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72264         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72264,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72265         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72265,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72266         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72266,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72267         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72267,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72268         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72268,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72269         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72269,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72270         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72270,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72271         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72271,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72272         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72272,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72273         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72273,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72274         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72274,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72275         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72275,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72276         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72276,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72290         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72290,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72300         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72300,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72305         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72305,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72306         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72306,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72307         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72307,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72308         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72308,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72316         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72316,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72321         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72321
  │ ✘✔✘✘✘ CVE-2026-72324         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72324,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72325         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72325,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72326         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72326,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72327         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72327,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72336         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72336,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72337         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72337
  │ ✘✔✘✘✘ CVE-2026-72341         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72341
  │ ✘✔✘✘✘ CVE-2026-72349         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72349,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72361         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72361,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72362         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72362,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72376         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72376,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72379         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72379,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72384         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72384,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72391         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72391,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72392         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72392,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72396         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72396,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72402         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72402
  │ ✘✔✘✘✘ CVE-2026-72413         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72413
  │ ✘✔✘✘✘ CVE-2026-72414         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72414,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72424         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72424,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72428         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72428,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72430         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72430,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72433         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72433,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72437         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72437,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72439         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72439
  │ ✘✔✘✘✘ CVE-2026-72441         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72441,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72443         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72443,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72447         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72447,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72448         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72448,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72467         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72467,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72474         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72474,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72479         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72479,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72481         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72481,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72484         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72484,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72486         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72486,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-72501         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72501
  │ ✘✔✘✘✘ CVE-2026-74261         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74261
  │ ✘✔✘✘✘ CVE-2026-74263         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74263,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74265         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74265,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74271         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74271,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74272         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74272
  │ ✘✔✘✘✘ CVE-2026-74273         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74273
  │ ✘✔✘✘✘ CVE-2026-74276         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74276,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74278         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74278,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74284         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74284,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74290         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74290,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74291         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74291
  │ ✘✔✘✘✘ CVE-2026-74303         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74303,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74307         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74307,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74308         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74308,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74318         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74318,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74320         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74320,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74324         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74324
  │ ✘✔✘✘✘ CVE-2026-74327         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74327,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74329         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74329,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74331         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74331,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74337         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74337
  │ ✘✔✘✘✘ CVE-2026-74339         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74339,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74342         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74342
  │ ✘✔✘✘✘ CVE-2026-74346         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74346,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74348         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74348,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74351         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74351,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74362         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74362,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74368         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74368
  │ ✘✔✘✘✘ CVE-2026-74373         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74373
  │ ✘✔✘✘✘ CVE-2026-74375         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74375
  │ ✘✔✘✘✘ CVE-2026-74379         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74379,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74381         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74381,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74382         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74382,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74386         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74386,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74389         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74389,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74391         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74391,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74395         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74395,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74399         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74399,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74402         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74402,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74416         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74416,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74424         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74424,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74426         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74426,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74432         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74432,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-74441         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74441
  │ ✘✔✘✘✘ CVE-2026-74445         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74445
  │ ✘✔✘✘✘ CVE-2026-74448         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74448
  │ ✘✔✘✘✘ CVE-2026-74455         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74455
  │ ✘✔✘✘✘ CVE-2026-74457         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74457
  │ ✘✔✘✘✘ CVE-2026-74458         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74458
  │ ✘✔✘✘✘ CVE-2026-74459         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74459
  │ ✘✔✘✘✘ CVE-2026-74460         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74460
  │ ✘✔✘✘✘ CVE-2026-74463         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74463
  │ ✘✔✘✘✘ CVE-2026-74464         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74464
  │ ✘✔✘✘✘ CVE-2026-74466         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74466
  │ ✘✔✘✘✘ CVE-2026-74468         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74468
  │ ✘✔✘✘✘ CVE-2026-74472         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74472
  │ ✘✔✘✘✘ CVE-2026-74483         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74483
  │ ✘✔✘✘✘ CVE-2026-74484         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74484
  │ ✘✔✘✘✘ CVE-2026-74487         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74487
  │ ✘✔✘✘✘ CVE-2026-74494         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74494
  │ ✘✔✘✘✘ CVE-2026-74498         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74498
  │ ✘✔✘✘✘ CVE-2026-74499         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74499
  │ ✘✔✘✘✘ CVE-2026-74500         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74500
  │ ✘✔✘✘✘ CVE-2026-74501         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74501
  │ ✘✔✘✘✘ CVE-2026-74502         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74502
  │ ✘✔✘✘✘ CVE-2026-74505         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74505
  │ ✘✔✘✘✘ CVE-2026-74514         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74514
  │ ✘✔✘✘✘ CVE-2026-74525         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74525
  │ ✘✔✘✘✘ CVE-2026-74532         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74532
  │ ✘✔✘✘✘ CVE-2026-74536         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74536
  │ ✘✔✘✘✘ CVE-2026-74543         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74543
  │ ✘✔✘✘✘ CVE-2026-74546         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74546
  │ ✘✔✘✘✘ CVE-2026-74547         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74547
  │ ✘✔✘✘✘ CVE-2026-74552         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74552
  │ ✘✔✘✘✘ CVE-2026-74553         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74553
  │ ✘✔✘✘✘ CVE-2026-74555         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74555
  │ ✘✔✘✘✘ CVE-2026-74558         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74558
  │ ✘✔✘✘✘ CVE-2026-74559         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74559
  │ ✘✔✘✘✘ CVE-2026-74560         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74560
  │ ✘✔✘✘✘ CVE-2026-74566         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74566
  │ ✘✔✘✘✘ CVE-2026-74571         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74571
  │ ✘✔✘✘✘ CVE-2026-74577         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74577
  │ ✘✔✘✘✘ CVE-2026-74585         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74585
  │ ✘✔✘✘✘ CVE-2026-74599         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74599
  │ ✘✔✘✘✘ CVE-2026-74600         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74600
  │ ✘✔✘✘✘ CVE-2026-74602         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74602
  │ ✘✔✘✘✘ CVE-2026-74618         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74618
  │ ✘✔✘✘✘ CVE-2026-74619         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74619
  │ ✘✔✘✘✘ CVE-2026-74620         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74620
  │ ✘✔✘✘✘ CVE-2026-74622         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74622
  │ ✘✔✘✘✘ CVE-2026-74623         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74623
  │ ✘✔✘✘✘ CVE-2026-74636         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74636
  │ ✘✔✘✘✘ CVE-2026-74638         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74638
  │ ✘✔✘✘✘ CVE-2026-74650         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74650
  │ ✘✔✘✘✘ CVE-2026-74653         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74653
  │ ✘✔✘✘✘ CVE-2026-74654         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74654
  │ ✘✔✘✘✘ CVE-2026-74657         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74657
  │ ✘✔✘✘✘ CVE-2026-74658         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74658
  │ ✘✔✘✘✘ CVE-2026-74659         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74659
  │ ✘✔✘✘✘ CVE-2026-74664         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74664
  │ ✘✔✘✘✘ CVE-2026-74671         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74671
  │ ✘✔✘✘✘ CVE-2026-74672         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74672
  │ ✘✔✘✘✘ CVE-2026-74673         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74673
  │ ✘✔✘✘✘ CVE-2026-74676         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74676
  │ ✘✔✘✘✘ CVE-2026-74677         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74677
  │ ✘✔✘✘✘ CVE-2026-74679         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74679
  │ ✘✔✘✘✘ CVE-2026-74680         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74680
  │ ✘✔✘✘✘ CVE-2026-74682         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74682
  │ ✘✔✘✘✘ CVE-2026-74683         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74683
  │ ✘✔✘✘✘ CVE-2026-74693         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74693
  │ ✘✔✘✘✘ CVE-2026-74694         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74694
  │ ✘✔✘✘✘ CVE-2026-74718         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74718
  │ ✘✔✘✘✘ CVE-2026-74719         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74719
  │ ✘✔✘✘✘ CVE-2026-74722         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74722
  │ ✘✔✘✘✘ CVE-2026-74729         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74729
  │ ✘✔✘✘✘ CVE-2026-74734         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74734
  │ ✘✔✘✘✘ CVE-2026-74735         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74735
  │ ✘✔✘✘✘ CVE-2026-74740         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74740
  │ ✘✔✘✘✘ CVE-2026-74754         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74754
  │ ✘✔✘✘✘ CVE-2026-80529         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80529
  │ ✘✔✘✘✘ CVE-2026-80534         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80534
  │ ✘✔✘✘✘ CVE-2026-80539         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80539
  │ ✘✔✘✘✘ CVE-2026-80542         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80542
  │ ✘✔✘✘✘ CVE-2026-80562         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80562
  │ ✘✔✘✘✘ CVE-2026-80566         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80566
  │ ✘✔✘✘✘ CVE-2026-80567         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80567
  │ ✘✔✘✘✘ CVE-2026-80573         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80573
  │ ✘✔✘✘✘ CVE-2026-80581         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80581
  │ ✘✔✘✘✘ CVE-2026-80594         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80594,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80595         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80595,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80597         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80597,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80602         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80602,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80605         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80605,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80607         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80607
  │ ✘✔✘✘✘ CVE-2026-80611         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80611,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80616         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80616
  │ ✘✔✘✘✘ CVE-2026-80618         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80618,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80620         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80620,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80623         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80623
  │ ✘✔✘✘✘ CVE-2026-80624         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80624,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80626         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80626,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80627         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80627,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80629         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80629,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80636         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80636,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80643         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80643
  │ ✘✔✘✘✘ CVE-2026-80644         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80644,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80647         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80647,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80650         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80650,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80652         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80652,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80654         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80654,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80659         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80659,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80660         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80660,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80667         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80667,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80669         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80669,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80676         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80676,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80679         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80679
  │ ✘✔✘✘✘ CVE-2026-80686         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80686
  │ ✘✔✘✘✘ CVE-2026-80689         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80689
  │ ✘✔✘✘✘ CVE-2026-80695         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80695
  │ ✘✔✘✘✘ CVE-2026-80698         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80698
  │ ✘✔✘✘✘ CVE-2026-80703         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80703
  │ ✘✔✘✘✘ CVE-2026-80704         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80704
  │ ✘✔✘✘✘ CVE-2026-80708         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80708
  │ ✘✔✘✘✘ CVE-2026-80711         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80711
  │ ✘✔✘✘✘ CVE-2026-80715         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80715
  │ ✘✔✘✘✘ CVE-2026-80727         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80727
  │ ✘✔✘✘✘ CVE-2026-80730         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80730
  │ ✘✔✘✘✘ CVE-2026-80733         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80733
  │ ✘✔✘✘✘ CVE-2026-80739         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80739
  │ ✘✔✘✘✘ CVE-2026-80742         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80742
  │ ✘✔✘✘✘ CVE-2026-80743         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80743
  │ ✘✔✘✘✘ CVE-2026-80744         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80744
  │ ✘✔✘✘✘ CVE-2026-80755         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80755
  │ ✘✔✘✘✘ CVE-2026-80756         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80756
  │ ✘✔✘✘✘ CVE-2026-80757         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80757
  │ ✘✔✘✘✘ CVE-2026-80761         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80761
  │ ✘✔✘✘✘ CVE-2026-80762         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80762
  │ ✘✔✘✘✘ CVE-2026-80763         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80763
  │ ✘✔✘✘✘ CVE-2026-80764         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80764
  │ ✘✔✘✘✘ CVE-2026-80765         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80765
  │ ✘✔✘✘✘ CVE-2026-80766         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80766
  │ ✘✔✘✘✘ CVE-2026-80767         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80767
  │ ✘✔✘✘✘ CVE-2026-80768         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80768
  │ ✘✔✘✘✘ CVE-2026-80770         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80770
  │ ✘✔✘✘✘ CVE-2026-80771         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80771
  │ ✘✔✘✘✘ CVE-2026-80772         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80772
  │ ✘✔✘✘✘ CVE-2026-80774         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80774
  │ ✘✔✘✘✘ CVE-2026-80780         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80780
  │ ✘✔✘✘✘ CVE-2026-80781         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80781
  │ ✘✔✘✘✘ CVE-2026-80782         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80782
  │ ✘✔✘✘✘ CVE-2026-80783         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80783
  │ ✘✔✘✘✘ CVE-2026-80784         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80784
  │ ✘✔✘✘✘ CVE-2026-80785         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80785
  │ ✘✔✘✘✘ CVE-2026-80786         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80786
  │ ✘✔✘✘✘ CVE-2026-80788         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80788
  │ ✘✔✘✘✘ CVE-2026-80789         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80789
  │ ✘✔✘✘✘ CVE-2026-80790         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80790
  │ ✘✔✘✘✘ CVE-2026-80791         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80791
  │ ✘✔✘✘✘ CVE-2026-80792         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80792
  │ ✘✔✘✘✘ CVE-2026-80793         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80793
  │ ✘✔✘✘✘ CVE-2026-80794         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80794
  │ ✘✔✘✘✘ CVE-2026-80795         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80795
  │ ✘✔✘✘✘ CVE-2026-80796         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80796
  │ ✘✔✘✘✘ CVE-2026-80797         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80797
  │ ✘✔✘✘✘ CVE-2026-80798         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80798
  │ ✘✔✘✘✘ CVE-2026-80799         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80799
  │ ✘✔✘✘✘ CVE-2026-80800         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80800
  │ ✘✔✘✘✘ CVE-2026-80801         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80801
  │ ✘✔✘✘✘ CVE-2026-80802         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80802
  │ ✘✔✘✘✘ CVE-2026-80803         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80803
  │ ✘✔✘✘✘ CVE-2026-80805         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80805
  │ ✘✔✘✘✘ CVE-2026-80806         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80806
  │ ✘✔✘✘✘ CVE-2026-80807         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80807
  │ ✘✔✘✘✘ CVE-2026-80808         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80808
  │ ✘✔✘✘✘ CVE-2026-80809         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80809
  │ ✘✔✘✘✘ CVE-2026-80812         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80812
  │ ✘✔✘✘✘ CVE-2026-80814         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80814
  │ ✘✔✘✘✘ CVE-2026-80815         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80815
  │ ✘✔✘✘✘ CVE-2026-80819         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80819
  │ ✘✔✘✘✘ CVE-2026-80820         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80820
  │ ✘✔✘✘✘ CVE-2026-80823         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80823
  │ ✘✔✘✘✘ CVE-2026-80824         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80824
  │ ✘✔✘✘✘ CVE-2026-80825         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80825
  │ ✘✔✘✘✘ CVE-2026-80826         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80826
  │ ✘✔✘✘✘ CVE-2026-80827         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80827
  │ ✘✔✘✘✘ CVE-2026-80828         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80828
  │ ✘✔✘✘✘ CVE-2026-80829         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80829
  │ ✘✔✘✘✘ CVE-2026-80830         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80830
  │ ✘✔✘✘✘ CVE-2026-80831         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80831
  │ ✘✔✘✘✘ CVE-2026-80832         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80832
  │ ✘✔✘✘✘ CVE-2026-80833         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80833
  │ ✘✔✘✘✘ CVE-2026-80834         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80834
  │ ✘✔✘✘✘ CVE-2026-80835         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80835
  │ ✘✔✘✘✘ CVE-2026-80836         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80836
  │ ✘✔✘✘✘ CVE-2026-80837         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80837
  │ ✘✔✘✘✘ CVE-2026-80838         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80838
  │ ✘✔✘✘✘ CVE-2026-80839         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80839
  │ ✘✔✘✘✘ CVE-2026-80840         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80840
  │ ✘✔✘✘✘ CVE-2026-80841         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80841
  │ ✘✔✘✘✘ CVE-2026-80842         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80842
  │ ✘✔✘✘✘ CVE-2026-80843         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80843
  │ ✘✔✘✘✘ CVE-2026-80844         ?            0.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80844
  │ ✘✔✘✘✘ CVE-2026-80846         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80846
  │ ✘✔✘✘✘ CVE-2026-80847         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80847
  │ ✘✔✘✘✘ CVE-2026-80848         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80848
  │ ✘✔✘✘✘ CVE-2026-80849         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80849
  │ ✘✔✘✘✘ CVE-2026-80850         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80850
  │ ✘✔✘✘✘ CVE-2026-80851         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80851
  │ ✘✔✘✘✘ CVE-2026-80852         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80852
  │ ✘✔✘✘✘ CVE-2026-80854         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80854
  │ ✘✔✘✘✘ CVE-2026-80855         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80855
  │ ✘✔✘✘✘ CVE-2026-80856         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80856
  │ ✘✔✘✘✘ CVE-2026-80861         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80861
  │ ✘✔✘✘✘ CVE-2026-80863         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80863
  │ ✘✔✘✘✘ CVE-2026-80864         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80864
  │ ✘✔✘✘✘ CVE-2026-80865         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80865,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80866         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80866
  │ ✘✔✘✘✘ CVE-2026-80867         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80867,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80870         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80870,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80872         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80872
  │ ✘✔✘✘✘ CVE-2026-80875         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80875,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80876         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80876,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80877         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80877,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80878         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80878
  │ ✘✔✘✘✘ CVE-2026-80879         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80879,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80880         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80880,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80881         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80881,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80883         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80883,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80884         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80884
  │ ✘✔✘✘✘ CVE-2026-80886         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80886,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-80887         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80887
  │ ✘✔✘✘✘ CVE-2026-80888         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80888
  │ ✘✔✘✘✘ CVE-2026-80889         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80889
  │ ✘✔✘✘✘ CVE-2026-80890         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80890
  │ ✘✔✘✘✘ CVE-2026-80891         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80891
  │ ✘✔✘✘✘ CVE-2026-80892         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80892
  │ ✘✔✘✘✘ CVE-2026-80893         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80893
  │ ✘✔✘✘✘ CVE-2026-80901         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80901
  │ ✘✔✘✘✘ CVE-2026-80902         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80902
  │ ✘✔✘✘✘ CVE-2026-80904         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80904
  │ ✘✔✘✘✘ CVE-2026-80905         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80905
  │ ✘✔✘✘✘ CVE-2026-80906         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80906
  │ ✘✔✘✘✘ CVE-2026-80907         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80907
  │ ✘✔✘✘✘ CVE-2026-80908         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80908
  │ ✘✔✘✘✘ CVE-2026-80909         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80909
  │ ✘✔✘✘✘ CVE-2026-80910         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80910
  │ ✘✔✘✘✘ CVE-2026-80911         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80911
  │ ✘✔✘✘✘ CVE-2026-80912         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80912
  │ ✘✔✘✘✘ CVE-2026-80913         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80913
  │ ✘✔✘✘✘ CVE-2026-80916         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80916
  │ ✘✔✘✘✘ CVE-2026-80917         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80917
  │ ✘✔✘✘✘ CVE-2026-80918         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80918
  │ ✘✔✘✘✘ CVE-2026-80920         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80920
  │ ✘✔✘✘✘ CVE-2026-80922         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80922
  │ ✘✔✘✘✘ CVE-2026-80923         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80923
  │ ✘✔✘✘✘ CVE-2026-80925         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80925
  │ ✘✔✘✘✘ CVE-2026-80930         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80930
  │ ✘✔✘✘✘ CVE-2026-80938         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80938
  │ ✘✔✘✘✘ CVE-2026-80939         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80939
  │ ✘✔✘✘✘ CVE-2026-80941         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80941
  │ ✘✔✘✘✘ CVE-2026-80948         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80948
  │ ✘✔✘✘✘ CVE-2026-80949         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80949
  │ ✘✔✘✘✘ CVE-2026-80951         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80951
  │ ✘✔✘✘✘ CVE-2026-80963         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80963
  │ ✘✔✘✘✘ CVE-2026-80964         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80964
  │ ✘✔✘✘✘ CVE-2026-80965         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80965
  │ ✘✔✘✘✘ CVE-2026-80966         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80966
  │ ✘✔✘✘✘ CVE-2026-80968         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80968
  │ ✘✔✘✘✘ CVE-2026-80969         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80969
  │ ✘✔✘✘✘ CVE-2026-80972         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80972
  │ ✘✔✘✘✘ CVE-2026-80973         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80973
  │ ✘✔✘✘✘ CVE-2026-80974         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80974
  │ ✘✔✘✘✘ CVE-2026-80983         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80983
  │ ✘✔✘✘✘ CVE-2026-80984         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80984
  │ ✘✔✘✘✘ CVE-2026-80988         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80988
  │ ✘✔✘✘✘ CVE-2026-80990         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80990
  │ ✘✔✘✘✘ CVE-2026-80996         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80996
  │ ✘✔✘✘✘ CVE-2026-80999         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80999
  │ ✘✔✘✘✘ CVE-2026-81005         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-81005
  │ ✘✔✘✘✘ CVE-2026-81013         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-81013
  │ ✘✔✘✘✘ CVE-2026-81014         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-81014
  │ ✘✔✘✘✘ CVE-2026-89437         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89437
  │ ✘✔✘✘✘ CVE-2026-89438         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89438
  │ ✘✔✘✘✘ CVE-2026-89439         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89439
  │ ✘✔✘✘✘ CVE-2026-89444         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89444
  │ ✘✔✘✘✘ CVE-2026-89451         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89451
  │ ✘✔✘✘✘ CVE-2026-89457         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89457
  │ ✘✔✘✘✘ CVE-2026-89458         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89458
  │ ✘✔✘✘✘ CVE-2026-89460         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89460,USN-8917-1
  │ ✘✔✘✘✘ CVE-2026-89461         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89461
  │ ✘✔✘✘✘ CVE-2026-89462         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89462
  │ ✘✔✘✘✘ CVE-2026-89463         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89463
  │ ✘✔✘✘✘ CVE-2026-89464         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89464
  │ ✘✔✘✘✘ CVE-2026-89467         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89467
  │ ✘✔✘✘✘ CVE-2026-89468         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89468
  │ ✘✔✘✘✘ CVE-2026-89473         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89473
  │ ✘✔✘✘✘ CVE-2026-89474         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89474
  │ ✘✔✘✘✘ CVE-2026-89475         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89475
  │ ✘✔✘✘✘ CVE-2026-89484         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89484
  │ ✘✔✘✘✘ CVE-2026-89490         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89490
  │ ✘✔✘✘✘ CVE-2026-89491         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89491
  │ ✘✔✘✘✘ CVE-2026-89496         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89496
  │ ✘✔✘✘✘ CVE-2026-89498         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89498
  │ ✘✔✘✘✘ CVE-2026-89502         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89502
  │ ✘✔✘✘✘ CVE-2026-89512         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89512
  │ ✘✔✘✘✘ CVE-2026-89515         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89515
  │ ✘✔✘✘✘ CVE-2026-89525         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89525
  │ ✘✔✘✘✘ CVE-2026-89527         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89527
  │ ✘✔✘✘✘ CVE-2026-89531         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89531
  │ ✘✔✘✘✘ CVE-2026-89539         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89539
  │ ✘✔✘✘✘ CVE-2026-89543         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89543
  │ ✘✔✘✘✘ CVE-2026-89552         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89552
  │ ✘✔✘✘✘ CVE-2026-89565         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89565
  │ ✘✔✘✘✘ CVE-2026-89566         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89566
  │ ✘✔✘✘✘ CVE-2026-89567         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89567
  │ ✘✔✘✘✘ CVE-2026-89572         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89572
  │ ✘✔✘✘✘ CVE-2026-89575         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89575
  │ ✘✔✘✘✘ CVE-2026-89576         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89576
  │ ✘✔✘✘✘ CVE-2026-89582         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89582
  │ ✘✔✘✘✘ CVE-2026-89595         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89595
  │ ✘✔✘✘✘ CVE-2026-89598         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89598
  │ ✘✔✘✘✘ CVE-2026-89604         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89604
  │ ✘✔✘✘✘ CVE-2026-89618         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89618
  │ ✘✔✘✘✘ CVE-2026-89621         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89621
  │ ✘✔✘✘✘ CVE-2026-89623         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89623
  │ ✘✔✘✘✘ CVE-2026-89625         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89625
  │ ✘✔✘✘✘ CVE-2026-89627         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89627
  │ ✘✔✘✘✘ CVE-2026-89628         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89628
  │ ✘✔✘✘✘ CVE-2026-89642         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89642
  │ ✘✔✘✘✘ CVE-2026-89644         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89644
  │ ✘✔✘✘✘ CVE-2026-89645         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89645
  │ ✘✔✘✘✘ CVE-2026-89666         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89666
  │ ✘✔✘✘✘ CVE-2026-89673         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89673
  │ ✘✔✘✘✘ CVE-2026-89693         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89693
  │ ✘✔✘✘✘ CVE-2026-89694         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89694
  │ ✘✔✘✘✘ CVE-2026-89698         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89698
  │ ✘✔✘✘✘ CVE-2026-89710         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89710
  │ ✘✔✘✘✘ CVE-2026-89717         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89717
  │ ✘✔✘✘✘ CVE-2026-89718         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89718
  │ ✘✔✘✘✘ CVE-2026-89719         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89719
  │ ✘✔✘✘✘ CVE-2026-89722         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89722
  │ ✘✔✘✘✘ CVE-2026-89726         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89726
  │ ✘✔✘✘✘ CVE-2026-89730         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89730
  │ ✘✔✘✘✘ CVE-2026-89732         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89732
  │ ✘✔✘✘✘ CVE-2026-89735         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89735
  │ ✘✔✘✘✘ CVE-2026-89740         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89740
  │ ✘✔✘✘✘ CVE-2026-89749         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89749
  │ ✘✔✘✘✘ CVE-2026-89751         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89751
  │ ✘✔✘✘✘ CVE-2026-89752         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89752
  │ ✘✔✘✘✘ CVE-2026-89753         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89753
  │ ✘✔✘✘✘ CVE-2026-89756         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89756
  │ ✘✔✘✘✘ CVE-2026-89757         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89757
  │ ✘✔✘✘✘ CVE-2026-89759         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89759
  │ ✘✔✘✘✘ CVE-2026-89765         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89765
  │ ✘✔✘✘✘ CVE-2026-89776         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89776
  │ ✘✔✘✘✘ CVE-2026-89780         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89780
  │ ✘✔✘✘✘ CVE-2026-89784         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89784
  │ ✘✔✘✘✘ CVE-2026-89785         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89785
  │ ✘✔✘✘✘ CVE-2026-89787         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89787
  │ ✘✔✘✘✘ CVE-2026-89794         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89794
  │ ✘✔✘✘✘ CVE-2026-89796         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89796
  │ ✘✔✘✘✘ CVE-2026-89797         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89797
  │ ✘✔✘✘✘ CVE-2026-89800         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89800
  │ ✘✔✘✘✘ CVE-2026-89802         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89802
  │ ✘✔✘✘✘ CVE-2026-89813         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89813
  │ ✘✔✘✘✘ CVE-2026-89816         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89816
  │ ✘✔✘✘✘ CVE-2026-89817         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89817
  │ ✘✔✘✘✘ CVE-2026-89821         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89821
  │ ✘✔✘✘✘ CVE-2026-89822         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89822
  │ ✘✔✘✘✘ CVE-2026-89824         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89824
  │ ✘✔✘✘✘ CVE-2026-89827         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89827
  │ ✘✔✘✘✘ CVE-2026-89830         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89830
  │ ✘✔✘✘✘ CVE-2026-89833         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89833
  │ ✘✔✘✘✘ CVE-2026-89834         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89834
  │ ✘✔✘✘✘ CVE-2026-89835         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89835
  │ ✘✔✘✘✘ CVE-2026-89837         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89837
  │ ✘✔✘✘✘ CVE-2026-89839         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89839
  │ ✘✔✘✘✘ CVE-2026-89842         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89842
  │ ✘✔✘✘✘ CVE-2026-89843         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89843
  │ ✘✔✘✘✘ CVE-2026-89845         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89845
  │ ✘✔✘✘✘ CVE-2026-89850         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89850
  │ ✘✔✘✘✘ CVE-2026-89851         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89851
  │ ✘✔✘✘✘ CVE-2026-89852         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89852
  │ ✘✔✘✘✘ CVE-2026-89853         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89853
  │ ✘✔✘✘✘ CVE-2026-89855         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89855
  │ ✘✔✘✘✘ CVE-2026-89858         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89858
  │ ✘✔✘✘✘ CVE-2026-89859         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89859
  │ ✘✔✘✘✘ CVE-2026-89862         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89862
  │ ✘✔✘✘✘ CVE-2026-89864         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89864
  │ ✘✔✘✘✘ CVE-2026-89865         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89865
  │ ✘✔✘✘✘ CVE-2026-89866         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89866
  │ ✘✔✘✘✘ CVE-2026-89868         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89868
  │ ✘✔✘✘✘ CVE-2026-89871         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89871
  │ ✘✔✘✘✘ CVE-2026-89872         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89872
  │ ✘✔✘✘✘ CVE-2026-89874         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89874
  │ ✘✔✘✘✘ CVE-2026-89876         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89876
  │ ✘✔✘✘✘ CVE-2026-89878         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89878
  │ ✘✔✘✘✘ CVE-2026-89879         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89879
  │ ✘✔✘✘✘ CVE-2026-89881         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89881
  │ ✘✔✘✘✘ CVE-2026-89884         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89884
  │ ✘✔✘✘✘ CVE-2026-89891         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89891
  │ ✘✔✘✘✘ CVE-2026-89892         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89892
  │ ✘✔✘✘✘ CVE-2026-89895         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89895
  │ ✘✔✘✘✘ CVE-2026-89896         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89896
  │ ✘✔✘✘✘ CVE-2026-89900         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89900
  │ ✘✔✘✘✘ CVE-2026-89901         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89901
  │ ✘✔✘✘✘ CVE-2026-89909         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89909
  │ ✘✔✘✘✘ CVE-2026-89921         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89921
  │ ✘✔✘✘✘ CVE-2026-89923         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89923
  │ ✘✔✘✘✘ CVE-2026-89924         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89924
  │ ✘✔✘✘✘ CVE-2026-89925         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89925
  │ ✘✔✘✘✘ CVE-2026-89926         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89926
  │ ✘✔✘✘✘ CVE-2026-89931         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89931
  │ ✘✔✘✘✘ CVE-2026-89933         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89933
  │ ✘✔✘✘✘ CVE-2026-89934         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89934
  │ ✘✔✘✘✘ CVE-2026-89936         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89936
  │ ✘✔✘✘✘ CVE-2026-89937         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89937
  │ ✘✔✘✘✘ CVE-2026-89939         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89939
  │ ✘✔✘✘✘ CVE-2026-89944         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89944
  │ ✘✔✘✘✘ CVE-2026-89945         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89945
  │ ✘✔✘✘✘ CVE-2026-89946         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89946
  │ ✘✔✘✘✘ CVE-2026-89948         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89948
  │ ✘✔✘✘✘ CVE-2026-89949         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89949
  │ ✘✔✘✘✘ CVE-2026-89950         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89950
  │ ✘✔✘✘✘ CVE-2026-89952         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89952
  │ ✘✔✘✘✘ CVE-2026-89953         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89953
  │ ✘✔✘✘✘ CVE-2026-89955         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89955
  │ ✘✔✘✘✘ CVE-2026-89956         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89956
  │ ✘✔✘✘✘ CVE-2026-89958         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89958
  │ ✘✔✘✘✘ CVE-2026-89962         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89962
  │ ✘✔✘✘✘ CVE-2026-89964         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89964
  │ ✘✔✘✘✘ CVE-2026-89975         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89975
  │ ✘✔✘✘✘ CVE-2026-89982         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89982
  │ ✘✔✘✘✘ CVE-2026-89983         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89983
  │ ✘✔✘✘✘ CVE-2026-89984         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89984
  │ ✘✔✘✘✘ CVE-2026-89987         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89987
  │ ✘✔✘✘✘ CVE-2026-89989         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89989
  │ ✘✔✘✘✘ CVE-2026-89993         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89993
  │ ✘✔✘✘✘ CVE-2026-89996         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89996
  │ ✘✔✘✘✘ CVE-2026-90015         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90015
  │ ✘✔✘✘✘ CVE-2026-90019         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90019
  │ ✘✔✘✘✘ CVE-2026-90020         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90020
  │ ✘✔✘✘✘ CVE-2026-90021         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90021
  │ ✘✔✘✘✘ CVE-2026-90023         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90023
  │ ✘✔✘✘✘ CVE-2026-90024         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90024
  │ ✘✔✘✘✘ CVE-2026-90029         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90029
  │ ✘✔✘✘✘ CVE-2026-90031         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90031
  │ ✘✔✘✘✘ CVE-2026-90033         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90033
  │ ✘✔✘✘✘ CVE-2026-90034         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90034
  │ ✘✔✘✘✘ CVE-2026-90035         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90035
  │ ✘✔✘✘✘ CVE-2026-90053         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90053
  │ ✘✔✘✘✘ CVE-2026-90054         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90054
  │ ✘✔✘✘✘ CVE-2026-90055         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90055
  │ ✘✔✘✘✘ CVE-2026-90056         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90056
  │ ✘✔✘✘✘ CVE-2026-90058         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90058
  │ ✘✔✘✘✘ CVE-2026-90060         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90060
  │ ✘✔✘✘✘ CVE-2026-90061         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90061
  │ ✘✔✘✘✘ CVE-2026-90063         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90063
  │ ✘✔✘✘✘ CVE-2026-90066         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90066
  │ ✘✔✘✘✘ CVE-2026-90068         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90068
  │ ✘✔✘✘✘ CVE-2026-90070         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90070
  │ ✘✔✘✘✘ CVE-2026-90072         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90072
  │ ✘✔✘✘✘ CVE-2026-90073         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90073
  │ ✘✔✘✘✘ CVE-2026-90074         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90074
  │ ✘✔✘✘✘ CVE-2026-90075         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90075
  │ ✘✔✘✘✘ CVE-2026-90076         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90076
  │ ✘✔✘✘✘ CVE-2026-90078         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90078
  │ ✘✔✘✘✘ CVE-2026-90081         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90081
  │ ✘✔✘✘✘ CVE-2026-90083         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90083
  │ ✘✔✘✘✘ CVE-2026-90084         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90084
  │ ✘✔✘✘✘ CVE-2026-90086         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90086
  │ ✘✔✘✘✘ CVE-2026-90087         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90087
  │ ✘✔✘✘✘ CVE-2026-90088         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90088
  │ ✘✔✘✘✘ CVE-2026-90090         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90090
  │ ✘✔✘✘✘ CVE-2026-90097         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90097
  │ ✘✔✘✘✘ CVE-2026-90098         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90098
  │ ✘✔✘✘✘ CVE-2026-90099         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90099
  │ ✘✔✘✘✘ CVE-2026-90101         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90101
  │ ✘✔✘✘✘ CVE-2026-90105         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90105
  │ ✘✔✘✘✘ CVE-2026-90106         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90106
  │ ✘✔✘✘✘ CVE-2026-90107         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90107
  │ ✘✔✘✘✘ CVE-2026-90108         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90108
  │ ✘✔✘✘✘ CVE-2026-90109         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90109
  │ ✘✔✘✘✘ CVE-2026-90112         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90112
  │ ✘✔✘✘✘ CVE-2026-90114         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90114
  │ ✘✔✘✘✘ CVE-2026-90115         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90115
  │ ✘✔✘✘✘ CVE-2026-90116         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90116
  │ ✘✔✘✘✘ CVE-2026-90119         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90119
  │ ✘✔✘✘✘ CVE-2026-90122         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90122
  │ ✘✔✘✘✘ CVE-2026-90124         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90124
  │ ✘✔✘✘✘ CVE-2026-90125         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90125
  │ ✘✔✘✘✘ CVE-2026-90126         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90126
  │ ✘✔✘✘✘ CVE-2026-90128         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90128
  │ ✘✔✘✘✘ CVE-2026-90130         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90130
  │ ✘✔✘✘✘ CVE-2026-90135         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90135
  │ ✘✔✘✘✘ CVE-2026-90138         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90138
  │ ✘✔✘✘✘ CVE-2026-90139         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90139
  │ ✘✔✘✘✘ CVE-2026-90140         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90140
  │ ✘✔✘✘✘ CVE-2026-90144         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90144
  │ ✘✔✘✘✘ CVE-2026-90148         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90148
  │ ✘✔✘✘✘ CVE-2026-90150         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90150
  │ ✘✔✘✘✘ CVE-2026-90152         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90152
  │ ✘✔✘✘✘ CVE-2026-90154         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90154
  │ ✘✔✘✘✘ CVE-2026-90155         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90155
  │ ✘✔✘✘✘ CVE-2026-90156         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90156
  │ ✘✔✘✘✘ CVE-2026-90157         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90157
  │ ✘✔✘✘✘ CVE-2026-90158         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90158
  │ ✘✔✘✘✘ CVE-2026-90159         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90159
  │ ✘✔✘✘✘ CVE-2026-90160         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90160
  │ ✘✔✘✘✘ CVE-2026-90166         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90166
  │ ✘✔✘✘✘ CVE-2026-90167         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90167
  │ ✘✔✘✘✘ CVE-2026-90169         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90169
  │ ✘✔✘✘✘ CVE-2026-90170         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90170
  │ ✘✔✘✘✘ CVE-2026-90175         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90175
  │ ✘✔✘✘✘ CVE-2026-90178         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90178
  │ ✘✔✘✘✘ CVE-2026-90179         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90179
  │ ✘✔✘✘✘ CVE-2026-90180         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90180
  │ ✘✔✘✘✘ CVE-2026-90182         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90182
  │ ✘✔✘✘✘ CVE-2026-90183         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90183
  │ ✘✔✘✘✘ CVE-2026-90184         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90184
  │ ✘✔✘✘✘ CVE-2026-90185         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90185
  │ ✘✔✘✘✘ CVE-2026-90186         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90186
  │ ✘✔✘✘✘ CVE-2026-90187         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90187
  │ ✘✔✘✘✘ CVE-2026-90188         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90188
  │ ✘✔✘✘✘ CVE-2026-90189         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90189
  │ ✘✔✘✘✘ CVE-2026-90190         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90190
  │ ✘✔✘✘✘ CVE-2026-90194         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90194
  │ ✘✔✘✘✘ CVE-2026-90196         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90196
  │ ✘✔✘✘✘ CVE-2026-90198         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90198
  │ ✘✔✘✘✘ CVE-2026-90200         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90200
  │ ✘✔✘✘✘ CVE-2026-90202         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90202
  │ ✘✔✘✘✘ CVE-2026-90206         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90206
  │ ✘✔✘✘✘ CVE-2026-90208         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90208
  │ ✘✔✘✘✘ CVE-2026-90209         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90209
  │ ✘✔✘✘✘ CVE-2026-90213         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90213
  │ ✘✔✘✘✘ CVE-2026-90214         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90214
  │ ✘✔✘✘✘ CVE-2026-90216         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90216
  │ ✘✔✘✘✘ CVE-2026-90218         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90218
  │ ✘✔✘✘✘ CVE-2026-90219         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90219
  │ ✘✔✘✘✘ CVE-2026-90220         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90220
  │ ✘✔✘✘✘ CVE-2026-90221         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90221
  │ ✘✔✘✘✘ CVE-2026-90222         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90222
  │ ✘✔✘✘✘ CVE-2026-90226         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90226
  │ ✘✔✘✘✘ CVE-2026-90232         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90232
  │ ✘✔✘✘✘ CVE-2026-90245         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90245
  │ ✘✔✘✘✘ CVE-2026-90247         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90247
  │ ✘✔✘✘✘ CVE-2026-90248         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90248
  │ ✘✔✘✘✘ CVE-2026-90249         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90249
  │ ✘✔✘✘✘ CVE-2026-90250         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90250
  │ ✘✔✘✘✘ CVE-2026-90251         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90251
  │ ✘✔✘✘✘ CVE-2026-90253         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90253
  │ ✘✔✘✘✘ CVE-2026-90254         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90254
  │ ✘✔✘✘✘ CVE-2026-90257         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90257
  │ ✘✔✘✘✘ CVE-2026-90259         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90259
  │ ✘✔✘✘✘ CVE-2026-90261         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90261
  │ ✘✔✘✘✘ CVE-2026-90262         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90262
  │ ✘✔✘✘✘ CVE-2026-90263         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90263
  │ ✘✔✘✘✘ CVE-2026-90264         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90264
  │ ✘✔✘✘✘ CVE-2026-90265         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90265
  │ ✘✔✘✘✘ CVE-2026-90267         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90267
  │ ✘✔✘✘✘ CVE-2026-90273         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90273
  │ ✘✔✘✘✘ CVE-2026-90274         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90274
  │ ✘✔✘✘✘ CVE-2026-90275         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90275
  │ ✘✔✘✘✘ CVE-2026-90279         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90279
  │ ✘✔✘✘✘ CVE-2026-90280         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90280
  │ ✘✔✘✘✘ CVE-2026-90281         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90281
  │ ✘✔✘✘✘ CVE-2026-90282         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90282
  │ ✘✔✘✘✘ CVE-2026-90283         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90283
  │ ✘✔✘✘✘ CVE-2026-90284         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90284
  │ ✘✔✘✘✘ CVE-2026-90285         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90285
  │ ✘✔✘✘✘ CVE-2026-90287         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90287
  │ ✘✔✘✘✘ CVE-2026-90290         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90290
  │ ✘✔✘✘✘ CVE-2026-90295         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90295
  │ ✘✔✘✘✘ CVE-2026-90296         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90296
  │ ✘✔✘✘✘ CVE-2026-90297         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90297
  │ ✘✔✘✘✘ CVE-2026-90298         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90298
  │ ✘✔✘✘✘ CVE-2026-90300         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90300
  │ ✘✔✘✘✘ CVE-2026-90302         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90302
  │ ✘✔✘✘✘ CVE-2026-90303         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90303
  │ ✘✔✘✘✘ CVE-2026-90307         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90307
  │ ✘✔✘✘✘ CVE-2026-90311         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90311
  │ ✘✔✘✘✘ CVE-2026-90313         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90313
  │ ✘✔✘✘✘ CVE-2026-90314         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90314
  │ ✘✔✘✘✘ CVE-2026-90315         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90315
  │ ✘✔✘✘✘ CVE-2026-90318         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90318
  │ ✘✔✘✘✘ CVE-2026-90319         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90319
  │ ✘✔✘✘✘ CVE-2026-90322         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90322
  │ ✘✔✘✘✘ CVE-2026-90327         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90327
  │ ✘✔✘✘✘ CVE-2026-90328         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90328
  │ ✘✔✘✘✘ CVE-2026-90330         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90330
  │ ✘✔✘✘✘ CVE-2026-90333         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90333
  │ ✘✔✘✘✘ CVE-2026-90334         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90334
  │ ✘✔✘✘✘ CVE-2026-90335         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90335
  │ ✘✔✘✘✘ CVE-2026-90336         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90336
  │ ✘✔✘✘✘ CVE-2026-90337         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90337
  │ ✘✔✘✘✘ CVE-2026-90345         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90345
  │ ✘✔✘✘✘ CVE-2026-90346         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90346
  │ ✘✔✘✘✘ CVE-2026-90348         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90348
  │ ✘✔✘✘✘ CVE-2026-90351         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90351
  │ ✘✔✘✘✘ CVE-2026-90352         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90352
  │ ✘✔✘✘✘ CVE-2026-90354         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90354
  │ ✘✔✘✘✘ CVE-2026-90359         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90359
  │ ✘✔✘✘✘ CVE-2026-90360         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90360
  │ ✘✔✘✘✘ CVE-2026-90361         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90361
  │ ✘✔✘✘✘ CVE-2026-90362         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90362
  │ ✘✔✘✘✘ CVE-2026-90363         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90363
  │ ✘✔✘✘✘ CVE-2026-90364         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90364
  │ ✘✔✘✘✘ CVE-2026-90365         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90365
  │ ✘✔✘✘✘ CVE-2026-90366         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90366
  │ ✘✔✘✘✘ CVE-2026-90368         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90368
  │ ✘✔✘✘✘ CVE-2026-90370         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90370
  │ ✘✔✘✘✘ CVE-2026-90374         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90374
  │ ✘✔✘✘✘ CVE-2026-90375         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90375
  │ ✘✔✘✘✘ CVE-2026-90378         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90378
  │ ✘✔✘✘✘ CVE-2026-90382         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90382
  │ ✘✔✘✘✘ CVE-2026-90385         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90385
  │ ✘✔✘✘✘ CVE-2026-90386         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90386
  │ ✘✔✘✘✘ CVE-2026-90389         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90389
  │ ✘✔✘✘✘ CVE-2026-90390         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90390
  │ ✘✔✘✘✘ CVE-2026-90391         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90391
  │ ✘✔✘✘✘ CVE-2026-90393         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90393
  │ ✘✔✘✘✘ CVE-2026-90394         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90394
  │ ✘✔✘✘✘ CVE-2026-90395         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90395
  │ ✘✔✘✘✘ CVE-2026-90397         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90397
  │ ✘✔✘✘✘ CVE-2026-90400         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90400
  │ ✘✔✘✘✘ CVE-2026-90404         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90404
  │ ✘✔✘✘✘ CVE-2026-90410         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90410
  │ ✘✔✘✘✘ CVE-2026-90411         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90411
  │ ✘✔✘✘✘ CVE-2026-90415         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90415
  │ ✘✔✘✘✘ CVE-2026-90416         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90416
  │ ✘✔✘✘✘ CVE-2026-90417         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90417
  │ ✘✔✘✘✘ CVE-2026-90418         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90418
  │ ✘✔✘✘✘ CVE-2026-90420         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90420
  │ ✘✔✘✘✘ CVE-2026-90421         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90421
  │ ✘✔✘✘✘ CVE-2026-90422         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90422
  │ ✘✔✘✘✘ CVE-2026-90431         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90431
  │ ✘✔✘✘✘ CVE-2026-90433         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90433
  │ ✘✔✘✘✘ CVE-2026-90434         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90434
  │ ✘✔✘✘✘ CVE-2026-92476         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92476
  │ ✘✔✘✘✘ CVE-2026-92477         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92477
  │ ✘✔✘✘✘ CVE-2026-92480         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92480
  │ ✘✔✘✘✘ CVE-2026-92481         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92481
  │ ✘✔✘✘✘ CVE-2026-92482         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92482
  │ ✘✔✘✘✘ CVE-2026-92484         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92484
  │ ✘✔✘✘✘ CVE-2026-92490         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92490
  │ ✘✔✘✘✘ CVE-2026-92493         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92493
  │ ✘✔✘✘✘ CVE-2026-92494         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92494
  │ ✘✔✘✘✘ CVE-2026-92495         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92495
  │ ✘✔✘✘✘ CVE-2026-92496         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92496
  │ ✘✔✘✘✘ CVE-2026-92497         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92497
  │ ✘✔✘✘✘ CVE-2026-92498         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92498
  │ ✘✔✘✘✘ CVE-2026-92499         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92499
  │ ✘✔✘✘✘ CVE-2026-92500         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92500
  │ ✘✔✘✘✘ CVE-2026-92501         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92501
  │ ✘✔✘✘✘ CVE-2026-92502         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92502,USN-8903-1
  │ ✘✔✘✘✘ CVE-2026-92503         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92503
  │ ✘✔✘✘✘ CVE-2026-92506         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92506
  │ ✘✔✘✘✘ CVE-2026-92509         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92509
  │ ✘✔✘✘✘ CVE-2026-92512         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92512
  │ ✘✔✘✘✘ CVE-2026-92514         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92514
  │ ✘✔✘✘✘ CVE-2026-92519         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92519
  │ ✘✔✘✘✘ CVE-2026-92520         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92520
  │ ✘✔✘✘✘ CVE-2026-92521         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92521
  │ ✘✔✘✘✘ CVE-2026-92523         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92523
  │ ✘✔✘✘✘ CVE-2026-92524         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92524
  │ ✘✔✘✘✘ CVE-2026-93040         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93040
  │ ✘✔✘✘✘ CVE-2026-93041         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93041
  │ ✘✔✘✘✘ CVE-2026-93047         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93047
  │ ✘✔✘✘✘ CVE-2026-93048         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93048
  │ ✘✔✘✘✘ CVE-2026-93049         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93049
  │ ✘✔✘✘✘ CVE-2026-93050         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93050
  │ ✘✔✘✘✘ CVE-2026-93051         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93051
  │ ✘✔✘✘✘ CVE-2026-93052         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93052
  │ ✘✔✘✘✘ CVE-2026-93053         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93053
  │ ✘✔✘✘✘ CVE-2026-93055         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93055
  │ ✘✔✘✘✘ CVE-2026-93056         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93056
  │ ✘✔✘✘✘ CVE-2026-93058         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93058
  │ ✘✔✘✘✘ CVE-2026-93061         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93061
  │ ✘✔✘✘✘ CVE-2026-93062         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93062
  │ ✘✔✘✘✘ CVE-2026-93064         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93064
  │ ✘✔✘✘✘ CVE-2026-93065         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93065
  │ ✘✔✘✘✘ CVE-2026-93067         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93067
  │ ✘✔✘✘✘ CVE-2026-93072         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93072
  │ ✘✔✘✘✘ CVE-2026-93073         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93073
  │ ✘✔✘✘✘ CVE-2026-93081         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93081
  │ ✘✔✘✘✘ CVE-2026-93083         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93083
  │ ✘✔✘✘✘ CVE-2026-93084         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93084
  │ ✘✔✘✘✘ CVE-2026-93085         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93085
  │ ✘✔✘✘✘ CVE-2026-93086         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93086
  │ ✘✔✘✘✘ CVE-2026-93089         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93089
  │ ✘✔✘✘✘ CVE-2026-93090         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93090
  │ ✘✔✘✘✘ CVE-2026-93091         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93091
  │ ✘✔✘✘✘ CVE-2026-93092         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93092
  │ ✘✔✘✘✘ CVE-2026-93093         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93093
  │ ✘✔✘✘✘ CVE-2026-93097         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93097
  │ ✘✔✘✘✘ CVE-2026-93098         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93098
  │ ✘✔✘✘✘ CVE-2026-93099         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93099
  │ ✘✔✘✘✘ CVE-2026-93100         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93100
  │ ✘✔✘✘✘ CVE-2026-93101         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93101
  │ ✘✔✘✘✘ CVE-2026-93102         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93102
  │ ✘✔✘✘✘ CVE-2026-93103         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93103
  │ ✘✔✘✘✘ CVE-2026-93104         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93104
  │ ✘✔✘✘✘ CVE-2026-93108         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93108
  │ ✘✔✘✘✘ CVE-2026-93109         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93109
  │ ✘✔✘✘✘ CVE-2026-93110         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93110
  │ ✘✔✘✘✘ CVE-2026-93113         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93113
  │ ✘✔✘✘✘ CVE-2026-93114         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93114
  │ ✘✔✘✘✘ CVE-2026-93115         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93115
  │ ✘✔✘✘✘ CVE-2026-93117         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93117
  │ ✘✔✘✘✘ CVE-2026-93118         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93118
  │ ✘✔✘✘✘ CVE-2026-93119         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93119
  │ ✘✔✘✘✘ CVE-2026-93120         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93120
  │ ✘✔✘✘✘ CVE-2026-93123         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93123
  │ ✘✔✘✘✘ CVE-2026-93126         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93126
  │ ✘✔✘✘✘ CVE-2026-93128         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93128
  │ ✘✔✘✘✘ CVE-2026-93129         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93129
  │ ✘✔✘✘✘ CVE-2026-93130         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93130
  │ ✘✔✘✘✘ CVE-2026-93131         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93131
  │ ✘✔✘✘✘ CVE-2026-93136         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93136
  │ ✘✔✘✘✘ CVE-2026-93140         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93140
  │ ✘✔✘✘✘ CVE-2026-93141         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93141
  │ ✘✔✘✘✘ CVE-2026-93142         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93142
  │ ✘✔✘✘✘ CVE-2026-93145         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93145
  │ ✘✔✘✘✘ CVE-2026-93146         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93146
  │ ✘✔✘✘✘ CVE-2026-93149         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93149
  │ ✘✔✘✘✘ CVE-2026-93150         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93150
  │ ✘✔✘✘✘ CVE-2026-93152         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93152
  │ ✘✔✘✘✘ CVE-2026-93155         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93155
  │ ✘✔✘✘✘ CVE-2026-93156         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93156
  │ ✘✔✘✘✘ CVE-2026-93158         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93158
  │ ✘✔✘✘✘ CVE-2026-93159         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93159
  │ ✘✔✘✘✘ CVE-2026-93160         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93160
  │ ✘✔✘✘✘ CVE-2026-93161         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93161
  │ ✘✔✘✘✘ CVE-2026-93162         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93162
  │ ✘✔✘✘✘ CVE-2026-93163         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93163
  │ ✘✔✘✘✘ CVE-2026-93167         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93167
  │ ✘✔✘✘✘ CVE-2026-93168         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93168
  │ ✘✔✘✘✘ CVE-2026-93172         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93172
  │ ✘✔✘✘✘ CVE-2026-93174         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93174
  │ ✘✔✘✘✘ CVE-2026-93179         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93179
  │ ✘✔✘✘✘ CVE-2026-93181         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93181
  │ ✘✔✘✘✘ CVE-2026-93182         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93182
  │ ✘✔✘✘✘ CVE-2026-93183         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93183
  │ ✘✔✘✘✘ CVE-2026-93184         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93184
  │ ✘✔✘✘✘ CVE-2026-93185         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93185
  │ ✘✔✘✘✘ CVE-2026-93186         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93186
  │ ✘✔✘✘✘ CVE-2026-93188         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93188
  │ ✘✔✘✘✘ CVE-2026-93191         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93191
  │ ✘✔✘✘✘ CVE-2026-93199         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93199
  │ ✘✔✘✘✘ CVE-2026-93200         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93200
  │ ✘✔✘✘✘ CVE-2026-93202         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93202
  │ ✘✔✘✘✘ CVE-2026-93204         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93204
  │ ✘✔✘✘✘ CVE-2026-93205         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93205
  │ ✘✔✘✘✘ CVE-2026-93206         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93206
  │ ✘✔✘✘✘ CVE-2026-93208         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93208
  │ ✘✔✘✘✘ CVE-2026-93209         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93209
  │ ✘✔✘✘✘ CVE-2026-93210         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93210
  │ ✘✔✘✘✘ CVE-2026-93211         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93211
  │ ✘✔✘✘✘ CVE-2026-93213         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93213
  │ ✘✔✘✘✘ CVE-2026-93214         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93214
  │ ✘✔✘✘✘ CVE-2026-93215         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93215
  │ ✘✔✘✘✘ CVE-2026-93216         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93216
  │ ✘✔✘✘✘ CVE-2026-93219         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93219
  │ ✘✔✘✘✘ CVE-2026-93222         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93222
  │ ✘✔✘✘✘ CVE-2026-93223         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93223
  │ ✘✔✘✘✘ CVE-2026-93226         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93226
  │ ✘✔✘✘✘ CVE-2026-93230         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93230
  │ ✘✔✘✘✘ CVE-2026-93231         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93231
  │ ✘✔✘✘✘ CVE-2026-93234         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93234
  │ ✘✔✘✘✘ CVE-2026-93235         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93235
  │ ✘✔✘✘✘ CVE-2026-93236         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93236
  │ ✘✔✘✘✘ CVE-2026-93238         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93238
  │ ✘✔✘✘✘ CVE-2026-93239         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93239
  │ ✘✔✘✘✘ CVE-2026-93240         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93240
  │ ✘✔✘✘✘ CVE-2026-93241         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93241
  │ ✘✔✘✘✘ CVE-2026-93242         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93242
  │ ✘✔✘✘✘ CVE-2026-93243         ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-93243
  │ ✘✔✘✘✘ CVE-2026-93244         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93244
  │ ✘✔✘✘✘ CVE-2026-93245         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93245
  │ ✘✔✘✘✘ CVE-2026-93247         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93247
  │ ✘✔✘✘✘ CVE-2026-93251         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93251
  │ ✘✔✘✘✘ CVE-2026-93252         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93252
  │ ✘✔✘✘✘ CVE-2026-93256         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93256
  │ ✘✔✘✘✘ CVE-2026-93259         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93259
  │ ✘✔✘✘✘ CVE-2026-93261         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93261
  │ ✘✔✘✘✘ CVE-2026-93264         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93264
  │ ✘✔✘✘✘ CVE-2026-93268         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93268
  │ ✘✔✘✘✘ CVE-2026-93269         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93269
  │ ✘✔✘✘✘ CVE-2026-93271         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93271
  │ ✘✔✘✘✘ CVE-2026-93272         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93272
  │ ✘✔✘✘✘ CVE-2026-93273         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93273
  │ ✘✔✘✘✘ CVE-2026-93274         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93274
  │ ✘✔✘✘✘ CVE-2026-93275         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93275
  │ ✘✔✘✘✘ CVE-2026-93281         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93281
  │ ✘✔✘✘✘ CVE-2026-93283         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93283
  │ ✘✔✘✘✘ CVE-2026-93285         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93285
  │ ✘✔✘✘✘ CVE-2026-93286         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93286
  │ ✘✔✘✘✘ CVE-2026-93781         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93781
  │ ✘✔✘✘✘ CVE-2026-93783         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93783
  │ ✘✔✘✘✘ CVE-2026-93784         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93784
  │ ✘✔✘✘✘ CVE-2026-93785         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93785
  │ ✘✔✘✘✘ CVE-2026-93788         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93788
  │ ✘✔✘✘✘ CVE-2026-93789         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93789
  │ ✘✔✘✘✘ CVE-2026-93791         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93791
  │ ✘✔✘✘✘ CVE-2026-93792         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93792
  │ ✘✔✘✘✘ CVE-2026-93794         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93794
  │ ✘✔✘✘✘ CVE-2026-93795         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93795
  │ ✘✔✘✘✘ CVE-2026-93797         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93797
  │ ✘✔✘✘✘ CVE-2026-93800         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93800
  │ ✘✔✘✘✘ CVE-2026-93802         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93802
  │ ✘✔✘✘✘ CVE-2026-93803         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93803
  │ ✘✔✘✘✘ CVE-2026-93804         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93804
  │ ✘✔✘✘✘ CVE-2026-93805         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93805
  │ ✘✔✘✘✘ CVE-2026-93807         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93807
  │ ✘✔✘✘✘ CVE-2026-93808         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93808
  │ ✘✔✘✘✘ CVE-2026-93809         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93809
  │ ✘✔✘✘✘ CVE-2026-93811         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93811
  │ ✘✔✘✘✘ CVE-2026-93812         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93812
  │ ✘✔✘✘✘ CVE-2026-93814         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93814
  │ ✘✔✘✘✘ CVE-2026-93815         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93815
  │ ✘✔✘✘✘ CVE-2026-93818         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93818
  │ ✘✔✘✘✘ CVE-2026-93819         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93819
  │ ✘✔✘✘✘ CVE-2026-93820         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93820
  │ ✘✔✘✘✘ CVE-2026-93821         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93821
  │ ✘✔✘✘✘ CVE-2026-93822         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93822
  │ ✘✔✘✘✘ CVE-2026-93823         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93823
  │ ✘✔✘✘✘ CVE-2026-93824         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93824
  │ ✘✔✘✘✘ CVE-2026-93825         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93825
  │ ✘✔✘✘✘ CVE-2026-93828         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93828
  │ ✘✔✘✘✘ CVE-2026-93829         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93829
  │ ✘✔✘✘✘ CVE-2026-97407         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97407
  │ ✘✔✘✘✘ CVE-2026-97408         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97408
  │ ✘✔✘✘✘ CVE-2026-97410         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97410
  │ ✘✔✘✘✘ CVE-2026-97411         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97411
  │ ✘✔✘✘✘ CVE-2026-97412         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97412
  │ ✘✔✘✘✘ CVE-2026-97414         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97414
  │ ✘✔✘✘✘ CVE-2026-97416         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97416
  │ ✘✔✘✘✘ CVE-2026-97418         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97418
  │ ✘✔✘✘✘ CVE-2026-97419         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97419
  │ ✘✔✘✘✘ CVE-2026-97420         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97420
  │ ✘✔✘✘✘ CVE-2026-97422         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97422
  │ ✘✔✘✘✘ CVE-2026-97423         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97423
  │ ✘✔✘✘✘ CVE-2026-97424         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97424
  │ ✘✔✘✘✘ CVE-2026-97425         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97425
  │ ✘✔✘✘✘ CVE-2026-97426         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97426
  │ ✘✔✘✘✘ CVE-2026-97427         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97427
  │ ✘✔✘✘✘ CVE-2026-97430         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97430
  │ ✘✔✘✘✘ CVE-2026-97431         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97431
  │ ✘✔✘✘✘ CVE-2026-97432         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97432
  │ ✘✔✘✘✘ CVE-2026-97434         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97434
  │ ✘✔✘✘✘ CVE-2026-97435         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97435
  │ ✘✔✘✘✘ CVE-2026-97436         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97436
  │ ✘✔✘✘✘ CVE-2026-97439         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97439
  │ ✘✔✘✘✘ CVE-2026-97440         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97440
  │ ✘✔✘✘✘ CVE-2026-97441         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97441
  │ ✘✔✘✘✘ CVE-2026-97443         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97443
  │ ✘✔✘✘✘ CVE-2026-97446         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97446
  │ ✘✔✘✘✘ CVE-2026-97447         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97447
  │ ✘✔✘✘✘ CVE-2026-97449         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97449
  │ ✘✔✘✘✘ CVE-2026-97453         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97453
  │ ✘✔✘✘✘ CVE-2026-97456         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97456
  │ ✘✔✘✘✘ CVE-2026-97472         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97472
  │ ✘✔✘✘✘ CVE-2026-97473         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97473
  │ ✘✔✘✘✘ CVE-2026-97475         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97475
  │ ✘✔✘✘✘ CVE-2026-97476         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97476
  │ ✘✔✘✘✘ CVE-2026-97477         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97477
  │ ✘✔✘✘✘ CVE-2026-97479         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97479
  │ ✘✔✘✘✘ CVE-2026-97480         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97480
  │ ✘✔✘✘✘ CVE-2026-97481         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97481
  │ ✘✔✘✘✘ CVE-2026-97482         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97482
  │ ✘✔✘✘✘ CVE-2026-97483         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97483
  │ ✘✔✘✘✘ CVE-2026-97484         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97484
  │ ✘✔✘✘✘ CVE-2026-97485         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97485
  │ ✘✔✘✘✘ CVE-2026-97486         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97486
  │ ✘✔✘✘✘ CVE-2026-97487         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97487
  │ ✘✔✘✘✘ CVE-2026-97488         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97488
  │ ✘✔✘✘✘ CVE-2026-97489         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97489
  │ ✘✔✘✘✘ CVE-2026-97490         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97490
  │ ✘✔✘✘✘ CVE-2026-97491         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97491
  │ ✘✔✘✘✘ CVE-2026-97492         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97492
  │ ✘✔✘✘✘ CVE-2026-97493         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97493
  │ ✘✔✘✘✘ CVE-2026-97494         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97494
  │ ✘✔✘✘✘ CVE-2026-97495         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97495
  │ ✘✔✘✘✘ CVE-2026-97498         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97498
  │ ✘✔✘✘✘ CVE-2026-97499         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97499
  │ ✘✔✘✘✘ CVE-2026-97500         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97500
  │ ✘✔✘✘✘ CVE-2026-97501         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97501
  │ ✘✔✘✘✘ CVE-2026-97502         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97502
  │ ✘✔✘✘✘ CVE-2026-97503         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97503
  │ ✘✔✘✘✘ CVE-2026-97504         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97504
  │ ✘✔✘✘✘ CVE-2026-97505         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97505
  │ ✘✔✘✘✘ CVE-2026-97506         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97506
  │ ✘✔✘✘✘ CVE-2026-97507         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97507
  │ ✘✔✘✘✘ CVE-2026-97510         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97510
  │ ✘✔✘✘✘ CVE-2026-97511         ?            0.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97511
  │ ✘✔✘✘✘ CVE-2026-97512         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97512
  │ ✘✔✘✘✘ CVE-2026-97514         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97514
  │ ✘✔✘✘✘ CVE-2026-97515         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97515
  │ ✘✔✘✘✘ CVE-2026-97516         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97516
  │ ✘✔✘✘✘ CVE-2026-97517         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97517
  │ ✘✔✘✘✘ CVE-2026-97518         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97518
  │ ✘✔✘✘✘ CVE-2026-97519         ?            0.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97519
  │ ✘✔✘✘✘ CVE-2026-97521         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97521
  │ ✘✔✘✘✘ CVE-2026-97522         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97522
  │ ✘✔✘✘✘ CVE-2026-97529         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97529
  │ ✘✔✘✘✘ CVE-2026-97530         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97530
  │ ✘✔✘✘✘ CVE-2026-97532         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97532
  │ ✘✔✘✘✘ CVE-2026-97534         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97534
  │ ✘✔✘✘✘ CVE-2026-97535         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97535
  │ ✘✔✘✘✘ CVE-2026-97537         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97537
  │ ✘✔✘✘✘ CVE-2026-97539         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97539
  │ ✘✔✘✘✘ CVE-2026-97540         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97540
  │ ✘✔✘✘✘ CVE-2026-97541         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97541
  │ ✘✔✘✘✘ CVE-2026-97542         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97542
  │ ✘✔✘✘✘ CVE-2026-97545         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97545
  │ ✘✔✘✘✘ CVE-2026-97552         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97552
  │ ✘✔✘✘✘ CVE-2026-97554         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97554
  │ ✘✔✘✘✘ CVE-2026-97556         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97556
  │ ✘✔✘✘✘ CVE-2026-97558         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97558
  │ ✘✔✘✘✘ CVE-2026-97559         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97559
  │ ✘✔✘✘✘ CVE-2026-97560         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97560
  │ ✘✔✘✘✘ CVE-2026-97561         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97561
  │ ✘✔✘✘✘ CVE-2026-97563         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97563
  │ ✘✔✘✘✘ CVE-2026-97564         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97564
  │ ✘✔✘✘✘ CVE-2026-97565         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97565
  │ ✘✔✘✘✘ CVE-2026-97566         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97566
  │ ✘✔✘✘✘ CVE-2026-97567         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97567
  │ ✘✔✘✘✘ CVE-2026-97568         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97568
  │ ✘✔✘✘✘ CVE-2026-97572         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97572
  │ ✘✔✘✘✘ CVE-2026-97581         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97581
  │ ✘✔✘✘✘ CVE-2026-97582         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97582
  │ ✘✔✘✘✘ CVE-2026-97587         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97587
  │ ✘✔✘✘✘ CVE-2026-97592         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97592
  │ ✘✔✘✘✘ CVE-2026-97596         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97596
  │ ✘✔✘✘✘ CVE-2026-97597         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97597
  │ ✘✔✘✘✘ CVE-2026-97598         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97598
  │ ✘✔✘✘✘ CVE-2026-97599         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97599
  │ ✘✔✘✘✘ CVE-2026-97600         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97600
  │ ✘✔✘✘✘ CVE-2026-97601         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97601
  │ ✘✔✘✘✘ CVE-2026-97603         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97603
  │ ✘✔✘✘✘ CVE-2026-97604         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97604
  │ ✘✔✘✘✘ CVE-2026-97605         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97605
  │ ✘✔✘✘✘ CVE-2026-97606         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97606
  │ ✘✔✘✘✘ CVE-2026-97607         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97607
  │ ✘✔✘✘✘ CVE-2026-97613         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97613
  │ ✘✔✘✘✘ CVE-2026-97615         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97615
  │ ✘✔✘✘✘ CVE-2026-97616         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97616
  │ ✘✔✘✘✘ CVE-2026-97619         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97619
  │ ✘✔✘✘✘ CVE-2026-97620         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97620
  │ ✘✔✘✘✘ CVE-2026-97899         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97899
  │ ✘✔✘✘✘ CVE-2026-97900         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97900
  │ ✘✔✘✘✘ CVE-2026-97901         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97901
  │ ✘✔✘✘✘ CVE-2026-97902         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97902
  │ ✘✔✘✘✘ CVE-2026-97904         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97904
  │ ✘✔✘✘✘ CVE-2026-97905         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97905
  │ ✘✔✘✘✘ CVE-2026-97906         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97906
  │ ✘✔✘✘✘ CVE-2026-97907         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97907
  │ ✘✔✘✘✘ CVE-2026-97908         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97908
  │ ✘✔✘✘✘ CVE-2026-97909         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97909
  │ ✘✔✘✘✘ CVE-2026-97915         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97915
  │ ✘✔✘✘✘ CVE-2026-97916         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97916
  │ ✘✔✘✘✘ CVE-2026-97917         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97917
  │ ✘✔✘✘✘ CVE-2026-97918         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97918
  │ ✘✔✘✘✘ CVE-2026-97919         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97919
  │ ✘✔✘✘✘ CVE-2026-97920         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97920
  │ ✘✔✘✘✘ CVE-2026-97921         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97921
  │ ✘✔✘✘✘ CVE-2026-97922         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97922
  │ ✘✔✘✘✘ CVE-2026-97923         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97923
  │ ✘✔✘✘✘ CVE-2026-97924         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97924
  │ ✘✔✘✘✘ CVE-2026-97925         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97925
  │ ✘✔✘✘✘ CVE-2026-97927         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97927
  │ ✘✔✘✘✘ CVE-2026-97929         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97929
  │ ✘✔✘✘✘ CVE-2026-97930         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97930
  │ ✘✔✘✘✘ CVE-2026-97933         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97933
  │ ✘✔✘✘✘ CVE-2026-97934         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97934
  │ ✘✔✘✘✘ CVE-2026-97935         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97935
  │ ✘✔✘✘✘ CVE-2026-97936         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97936
  │ ✘✔✘✘✘ CVE-2026-97938         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97938
  │ ✘✔✘✘✘ CVE-2026-97939         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97939
  │ ✘✔✘✘✘ CVE-2026-97945         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97945
  │ ✘✔✘✘✘ CVE-2026-97948         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97948
  │ ✘✔✘✘✘ CVE-2026-97949         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97949
  │ ✘✔✘✘✘ CVE-2026-97950         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97950
  │ ✘✔✘✘✘ CVE-2026-97951         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97951
  │ ✘✔✘✘✘ CVE-2026-97954         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97954
  │ ✘✔✘✘✘ CVE-2026-97958         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97958
  │ ✘✔✘✘✘ CVE-2026-97959         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97959
  │ ✘✔✘✘✘ CVE-2026-97960         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97960
  │ ✘✔✘✘✘ CVE-2026-97961         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97961
  │ ✘✔✘✘✘ CVE-2026-97962         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97962
  │ ✘✔✘✘✘ CVE-2026-97963         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97963
  │ ✘✔✘✘✘ CVE-2026-97964         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97964
  │ ✘✔✘✘✘ CVE-2026-97965         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97965
  │ ✘✔✘✘✘ CVE-2026-97966         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97966
  │ ✘✔✘✘✘ CVE-2026-97969         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97969
  │ ✘✔✘✘✘ CVE-2026-97970         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97970
  │ ✘✔✘✘✘ CVE-2026-97973         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97973
  │ ✘✔✘✘✘ CVE-2026-97975         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97975
  │ ✘✔✘✘✘ CVE-2026-97977         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97977
  │ ✘✔✘✘✘ CVE-2026-97978         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97978
  │ ✘✔✘✘✘ CVE-2026-97979         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97979
  │ ✘✔✘✘✘ CVE-2026-97981         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97981
  │ ✘✔✘✘✘ CVE-2026-97982         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97982
  │ ✘✔✘✘✘ CVE-2026-97984         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97984
  │ ✘✔✘✘✘ CVE-2026-97985         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97985
  │ ✘✔✘✘✘ CVE-2026-97986         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97986
  │ ✘✔✘✘✘ CVE-2026-97987         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97987
  │ ✘✔✘✘✘ CVE-2026-97988         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97988
  │ ✘✔✘✘✘ CVE-2026-97989         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97989
  │ ✘✔✘✘✘ CVE-2026-97992         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97992
  │ ✘✔✘✘✘ CVE-2026-97993         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97993
  │ ✘✔✘✘✘ CVE-2026-97994         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97994
  │ ✘✔✘✘✘ CVE-2026-97995         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97995
  │ ✘✔✘✘✘ CVE-2026-97997         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97997
  │ ✘✔✘✘✘ CVE-2026-97998         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97998
  │ ✘✔✘✘✘ CVE-2026-98003         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98003
  │ ✘✔✘✘✘ CVE-2026-98006         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98006
  │ ✘✔✘✘✘ CVE-2026-98007         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98007
  │ ✘✔✘✘✘ CVE-2026-98008         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98008
  │ ✘✔✘✘✘ CVE-2026-98009         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98009
  │ ✘✔✘✘✘ CVE-2026-98010         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98010
  │ ✘✔✘✘✘ CVE-2026-98011         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98011
  │ ✘✔✘✘✘ CVE-2026-98012         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98012
  │ ✘✔✘✘✘ CVE-2026-98013         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98013
  │ ✘✔✘✘✘ CVE-2026-98014         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98014
  │ ✘✔✘✘✘ CVE-2026-98015         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98015
  │ ✘✔✘✘✘ CVE-2026-98016         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98016
  │ ✘✔✘✘✘ CVE-2026-98018         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98018
  │ ✘✔✘✘✘ CVE-2026-98019         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98019
  │ ✘✔✘✘✘ CVE-2026-98020         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98020
  │ ✘✔✘✘✘ CVE-2026-98021         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98021
  │ ✘✔✘✘✘ CVE-2026-98022         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98022
  │ ✘✔✘✘✘ CVE-2026-98024         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98024
  │ ✘✔✘✘✘ CVE-2026-98025         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98025
  │ ✘✔✘✘✘ CVE-2026-98026         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98026
  │ ✘✔✘✘✘ CVE-2026-98028         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98028
  │ ✘✔✘✘✘ CVE-2026-98031         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98031
  │ ✘✔✘✘✘ CVE-2026-98032         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98032
  │ ✘✔✘✘✘ CVE-2026-98033         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98033
  │ ✘✔✘✘✘ CVE-2026-98034         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98034
  │ ✘✔✘✘✘ CVE-2026-98037         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98037
  │ ✘✔✘✘✘ CVE-2026-98038         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98038
  │ ✘✔✘✘✘ CVE-2026-98039         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98039
  │ ✘✔✘✘✘ CVE-2026-98043         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98043
  │ ✘✔✘✘✘ CVE-2026-98044         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98044
  │ ✘✔✘✘✘ CVE-2026-98046         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98046
  │ ✘✔✘✘✘ CVE-2026-98055         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98055
  │ ✘✔✘✘✘ CVE-2026-98058         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98058
  │ ✘✔✘✘✘ CVE-2026-98063         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98063
  │ ✘✔✘✘✘ CVE-2026-98064         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98064
  │ ✘✔✘✘✘ CVE-2026-98066         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98066
  │ ✘✔✘✘✘ CVE-2026-98067         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98067
  │ ✘✔✘✘✘ CVE-2026-98068         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98068
  │ ✘✔✘✘✘ CVE-2026-98071         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98071
  │ ✘✔✘✘✘ CVE-2026-98072         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98072
  │ ✘✔✘✘✘ CVE-2026-98074         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98074
  │ ✘✔✘✘✘ CVE-2026-98075         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98075
  │ ✘✔✘✘✘ CVE-2026-98076         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98076
  │ ✘✔✘✘✘ CVE-2026-98077         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98077
  │ ✘✔✘✘✘ CVE-2026-98079         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98079
  │ ✘✔✘✘✘ CVE-2026-98081         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98081
  │ ✘✔✘✘✘ CVE-2026-98084         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98084
  │ ✘✔✘✘✘ CVE-2026-98085         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98085
  │ ✘✔✘✘✘ CVE-2026-98086         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98086
  │ ✘✔✘✘✘ CVE-2026-98087         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98087
  │ ✘✔✘✘✘ CVE-2026-98088         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98088
  │ ✘✔✘✘✘ CVE-2026-98089         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98089
  │ ✘✔✘✘✘ CVE-2026-98101         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98101
  │ ✘✔✘✘✘ CVE-2026-98102         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98102
  │ ✘✔✘✘✘ CVE-2026-98103         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98103
  │ ✘✔✘✘✘ CVE-2026-98104         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98104
  │ ✘✔✘✘✘ CVE-2026-98107         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98107
  │ ✘✔✘✘✘ CVE-2026-98167         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98167
  │ ✘✔✘✘✘ CVE-2026-98168         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98168
  │ ✘✔✘✘✘ CVE-2026-98170         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98170
  │ ✘✔✘✘✘ CVE-2026-98172         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98172
  │ ✘✔✘✘✘ CVE-2026-98176         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98176
  │ ✘✔✘✘✘ CVE-2026-98177         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98177
  │ ✘✔✘✘✘ CVE-2026-98179         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98179
  │ ✘✔✘✘✘ CVE-2026-98181         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98181
  │ ✘✔✘✘✘ CVE-2026-98182         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98182
  │ ✘✔✘✘✘ CVE-2026-98185         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98185
  │ ✘✔✘✘✘ CVE-2026-98186         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98186
  │ ✘✔✘✘✘ CVE-2026-98187         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98187
  │ ✘✔✘✘✘ CVE-2026-98188         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98188
  │ ✘✔✘✘✘ CVE-2026-98189         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98189
  │ ✘✔✘✘✘ CVE-2026-98190         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98190
  │ ✘✔✘✘✘ CVE-2026-98191         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98191
  │ ✘✔✘✘✘ CVE-2026-98192         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98192
  │ ✘✔✘✘✘ CVE-2026-98193         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98193
  │ ✘✔✘✘✘ CVE-2026-98194         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98194
  │ ✘✔✘✘✘ CVE-2026-98195         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98195
  │ ✘✔✘✘✘ CVE-2026-98196         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98196
  │ ✘✔✘✘✘ CVE-2026-98198         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98198
  │ ✘✔✘✘✘ CVE-2026-98199         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98199
  │ ✘✔✘✘✘ CVE-2026-98200         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98200
  │ ✘✔✘✘✘ CVE-2026-98201         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98201
  │ ✘✔✘✘✘ CVE-2026-98202         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98202
  │ ✘✔✘✘✘ CVE-2026-98203         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98203
  │ ✘✔✘✘✘ CVE-2026-98204         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98204
  │ ✘✔✘✘✘ CVE-2026-98205         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98205
  │ ✘✔✘✘✘ CVE-2026-98206         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98206
  │ ✘✔✘✘✘ CVE-2026-98207         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98207
  │ ✘✔✘✘✘ CVE-2026-98208         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98208
  │ ✘✔✘✘✘ CVE-2026-98209         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98209
  │ ✘✔✘✘✘ CVE-2026-98210         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98210
  │ ✘✔✘✘✘ CVE-2026-98211         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98211
  │ ✘✔✘✘✘ CVE-2026-98212         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98212
  │ ✘✔✘✘✘ CVE-2026-98213         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98213
  │ ✘✔✘✘✘ CVE-2026-98217         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98217
  │ ✘✔✘✘✘ CVE-2026-98218         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98218
  │ ✘✔✘✘✘ CVE-2026-98221         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98221
  │ ✘✔✘✘✘ CVE-2026-98222         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98222
  │ ✘✔✘✘✘ CVE-2026-98227         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98227
  │ ✘✔✘✘✘ CVE-2026-98231         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98231
  │ ✘✔✘✘✘ CVE-2026-98232         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98232
  │ ✘✔✘✘✘ CVE-2026-98233         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98233
  │ ✘✔✘✘✘ CVE-2026-98234         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98234
  │ ✘✔✘✘✘ CVE-2026-98235         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98235
  │ ✘✔✘✘✘ CVE-2026-98236         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98236
  │ ✘✔✘✘✘ CVE-2026-98237         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98237
  │ ✘✔✘✘✘ CVE-2026-98238         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98238
  │ ✘✔✘✘✘ CVE-2026-98245         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98245
  │ ✘✔✘✘✘ CVE-2026-98246         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98246
  │ ✘✔✘✘✘ CVE-2026-98247         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98247
  │ ✘✔✘✘✘ CVE-2026-98248         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98248
  │ ✘✔✘✘✘ CVE-2026-98249         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98249
  │ ✘✔✘✘✘ CVE-2026-98255         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98255
  │ ✘✔✘✘✘ CVE-2026-98262         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98262
  │ ✘✔✘✘✘ CVE-2026-98263         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98263
  │ ✘✔✘✘✘ CVE-2026-98264         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98264
  │ ✘✔✘✘✘ CVE-2026-98265         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98265
  │ ✘✔✘✘✘ CVE-2026-98266         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98266
  │ ✘✔✘✘✘ CVE-2026-98269         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98269
  │ ✘✔✘✘✘ CVE-2026-98270         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98270
  │ ✘✔✘✘✘ CVE-2026-98271         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98271
  │ ✘✔✘✘✘ CVE-2026-98272         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98272
  │ ✘✔✘✘✘ CVE-2026-98273         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98273
  │ ✘✔✘✘✘ CVE-2026-98275         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98275
  │ ✘✔✘✘✘ CVE-2026-98279         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98279
  │ ✘✔✘✘✘ CVE-2026-98284         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98284
  │ ✘✔✘✘✘ CVE-2026-98285         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98285
  │ ✘✔✘✘✘ CVE-2026-98286         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98286
  │ ✘✔✘✘✘ CVE-2026-98287         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98287
  │ ✘✔✘✘✘ CVE-2026-98288         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98288
  │ ✘✔✘✘✘ CVE-2026-98289         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98289
  │ ✘✔✘✘✘ CVE-2026-98292         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98292
  │ ✘✔✘✘✘ CVE-2026-98293         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98293
  │ ✘✔✘✘✘ CVE-2026-98294         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98294
  │ ✘✔✘✘✘ CVE-2026-98295         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98295
  │ ✘✔✘✘✘ CVE-2026-98297         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98297
  │ ✘✔✘✘✘ CVE-2026-98298         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98298
  │ ✘✔✘✘✘ CVE-2026-98299         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98299
  │ ✘✔✘✘✘ CVE-2026-98300         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98300
  │ ✘✔✘✘✘ CVE-2026-98301         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98301
  │ ✘✔✘✘✘ CVE-2026-98302         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98302
  │ ✘✔✘✘✘ CVE-2026-98303         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98303
  │ ✘✔✘✘✘ CVE-2026-98304         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98304
  │ ✘✔✘✘✘ CVE-2026-98306         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98306
  │ ✘✔✘✘✘ CVE-2026-98307         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98307
  │ ✘✔✘✘✘ CVE-2026-98308         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98308
  │ ✘✔✘✘✘ CVE-2026-98309         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98309
  │ ✘✔✘✘✘ CVE-2026-98312         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98312
  │ ✘✔✘✘✘ CVE-2026-98314         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98314
  │ ✘✔✘✘✘ CVE-2026-98317         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98317
  │ ✘✔✘✘✘ CVE-2026-98319         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98319
  │ ✘✔✘✘✘ CVE-2026-98321         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98321
  │ ✘✔✘✘✘ CVE-2026-98322         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98322
  │ ✘✔✘✘✘ CVE-2026-98325         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98325
  │ ✘✔✘✘✘ CVE-2026-98326         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98326
  │ ✘✔✘✘✘ CVE-2026-98327         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98327
  │ ✘✔✘✘✘ CVE-2026-98328         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98328
  │ ✘✔✘✘✘ CVE-2026-98329         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98329
  │ ✘✔✘✘✘ CVE-2026-98332         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98332
  │ ✘✔✘✘✘ CVE-2026-98333         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98333
  │ ✘✔✘✘✘ CVE-2026-98334         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98334
  │ ✘✔✘✘✘ CVE-2026-98335         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98335
  │ ✘✔✘✘✘ CVE-2026-98336         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98336
  │ ✘✔✘✘✘ CVE-2026-98337         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98337
  │ ✘✔✘✘✘ CVE-2026-98338         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98338
  │ ✘✔✘✘✘ CVE-2026-98340         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98340
  │ ✘✔✘✘✘ CVE-2026-98342         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98342
  │ ✘✔✘✘✘ CVE-2026-98343         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98343
  │ ✘✔✘✘✘ CVE-2026-98344         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98344
  │ ✘✔✘✘✘ CVE-2026-98345         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98345
  │ ✘✔✘✘✘ CVE-2026-98347         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98347
  │ ✘✔✘✘✘ CVE-2026-98351         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98351
  │ ✘✔✘✘✘ CVE-2026-98352         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98352
  │ ✘✔✘✘✘ CVE-2026-98353         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98353
  │ ✘✔✘✘✘ CVE-2026-98354         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98354
  │ ✘✔✘✘✘ CVE-2026-98355         ?            0.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98355
  │ ✘✔✘✘✘ CVE-2026-98358         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98358
  │ ✘✔✘✘✘ CVE-2026-98362         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98362
  │ ✘✔✘✘✘ CVE-2026-98363         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98363
  │ ✘✔✘✘✘ CVE-2026-98370         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98370
  │ ✘✔✘✘✘ CVE-2026-98373         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98373
  │ ✘✔✘✘✘ CVE-2026-98375         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98375
  │ ✘✔✘✘✘ CVE-2026-98377         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98377
  │ ✘✔✘✘✘ CVE-2026-98379         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98379
  │ ✘✔✘✘✘ CVE-2026-98380         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98380
  │ ✘✔✘✘✘ CVE-2026-98384         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98384
  │ ✘✔✘✘✘ CVE-2026-98386         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98386
  │ ✘✔✘✘✘ CVE-2026-98387         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98387
  │ ✘✔✘✘✘ CVE-2026-98388         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98388
  │ ✘✔✘✘✘ CVE-2026-98389         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98389
  │ ✘✔✘✘✘ CVE-2026-98393         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98393
  │ ✘✔✘✘✘ CVE-2026-98394         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98394
  │ ✘✔✘✘✘ CVE-2026-98398         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98398
  │ ✘✔✘✘✘ CVE-2026-98399         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98399
  │ ✘✔✘✘✘ CVE-2026-98400         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98400
  │ ✘✔✘✘✘ CVE-2026-98402         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98402
  │ ✘✔✘✘✘ CVE-2026-98403         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98403
  │ ✘✔✘✘✘ CVE-2026-98404         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98404
  │ ✘✔✘✘✘ CVE-2026-98406         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98406
  │ ✘✔✘✘✘ CVE-2026-98407         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98407
  │ ✘✔✘✘✘ CVE-2026-98409         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98409
  │ ✘✔✘✘✘ CVE-2026-98410         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98410
  │ ✘✔✘✘✘ CVE-2026-98413         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98413
  │ ✘✔✘✘✘ CVE-2026-98416         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98416
  │ ✘✔✘✘✘ CVE-2026-98417         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98417
  │ ✘✔✘✘✘ CVE-2026-98420         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98420
  │ ✘✔✘✘✘ CVE-2026-98421         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98421
  │ ✘✔✘✘✘ CVE-2026-98422         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98422
  │ ✘✔✘✘✘ CVE-2026-98423         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98423
  │ ✘✔✘✘✘ CVE-2026-98424         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98424
  │ ✘✔✘✘✘ CVE-2026-98425         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98425
  │ ✘✔✘✘✘ CVE-2026-98426         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98426
  │ ✘✔✘✘✘ CVE-2026-98427         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98427
  │ ✘✔✘✘✘ CVE-2026-98428         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98428
  │ ✘✔✘✘✘ CVE-2026-98429         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98429
  │ ✘✔✘✘✘ CVE-2026-98430         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98430
  │ ✘✔✘✘✘ CVE-2026-98431         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98431
  │ ✘✔✘✘✘ CVE-2026-98433         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98433
  │ ✘✔✘✘✘ CVE-2026-98435         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98435
  │ ✘✔✘✘✘ CVE-2026-98439         ?            0.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98439
  │ ✘✔✘✘✘ CVE-2026-98445         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98445
  │ ✘✔✘✘✘ CVE-2026-98449         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98449
  │ ✘✔✘✘✘ CVE-2026-98450         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98450
  │ ✘✔✘✘✘ CVE-2026-98452         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98452
  │ ✘✔✘✘✘ CVE-2026-98453         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98453
  │ ✘✔✘✘✘ CVE-2026-98455         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98455
  │ ✘✔✘✘✘ CVE-2026-98457         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98457
  │ ✘✔✘✘✘ CVE-2026-98458         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98458
  │ ✘✔✘✘✘ CVE-2026-98459         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98459
  │ ✘✔✘✘✘ CVE-2026-98460         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98460
  │ ✘✔✘✘✘ CVE-2026-98461         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98461
  │ ✘✔✘✘✘ CVE-2026-98462         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98462
  │ ✘✔✘✘✘ CVE-2026-98473         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98473
  │ ✘✔✘✘✘ CVE-2026-98476         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98476
  │ ✘✔✘✘✘ CVE-2026-98477         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98477
  │ ✘✔✘✘✘ CVE-2026-98481         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98481
  │ ✘✔✘✘✘ CVE-2026-98482         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98482
  │ ✘✔✘✘✘ CVE-2026-98483         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98483
  │ ✘✔✘✘✘ CVE-2026-98484         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98484
  │ ✘✔✘✘✘ CVE-2026-98486         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98486
  │ ✘✔✘✘✘ CVE-2026-98488         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98488
  │ ✘✔✘✘✘ CVE-2026-98489         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98489
  │ ✘✔✘✘✘ CVE-2026-98493         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98493
  │ ✘✔✘✘✘ CVE-2026-98494         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98494
  │ ✘✔✘✘✘ CVE-2026-98495         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98495
  │ ✘✔✘✘✘ CVE-2026-98498         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98498
  │ ✘✔✘✘✘ CVE-2026-98502         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98502
  │ ✘✔✘✘✘ CVE-2026-98503         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98503
  │ ✘✔✘✘✘ CVE-2026-98504         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98504
  │ ✘✔✘✘✘ CVE-2026-98505         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98505
  │ ✘✔✘✘✘ CVE-2026-98506         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98506
  │ ✘✔✘✘✘ CVE-2026-98508         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98508
  │ ✘✔✘✘✘ CVE-2026-98509         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98509
  │ ✘✔✘✘✘ CVE-2026-98511         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98511
  │ ✘✔✘✘✘ CVE-2026-98513         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98513
  │ ✘✔✘✘✘ CVE-2026-98514         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98514
  │ ✘✔✘✘✘ CVE-2026-98516         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98516
  │ ✘✔✘✘✘ CVE-2026-98519         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98519
  │ ✘✔✘✘✘ CVE-2026-98521         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98521
  │ ✘✔✘✘✘ CVE-2026-98522         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98522
  │ ✘✔✘✘✘ CVE-2026-98525         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98525
  │ ✘✔✘✘✘ CVE-2026-98526         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98526
  │ ✘✔✘✘✘ CVE-2026-98527         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98527
  │ ✘✔✘✘✘ CVE-2026-98529         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98529
  │ ✘✔✘✘✘ CVE-2026-98531         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98531
  │ ✘✔✘✘✘ CVE-2026-98535         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98535
  │ ✘✔✘✘✘ CVE-2026-98536         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98536
  │ ✘✔✘✘✘ CVE-2026-98537         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98537
  │ ✘✔✘✘✘ CVE-2026-98538         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98538
  │ ✘✔✘✘✘ CVE-2026-98539         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98539
  │ ✘✔✘✘✘ CVE-2026-98541         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98541
  │ ✘✔✘✘✘ CVE-2026-98544         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98544
  │ ✘✔✘✘✘ CVE-2026-98545         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98545
  │ ✘✔✘✘✘ CVE-2026-98547         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98547
  │ ✘✔✘✘✘ CVE-2026-98551         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98551
  │ ✘✔✘✘✘ CVE-2026-98553         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98553
  │ ✘✔✘✘✘ CVE-2026-98554         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98554
  │ ✘✔✘✘✘ CVE-2026-98556         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98556
  │ ✘✔✘✘✘ CVE-2026-98558         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98558
  │ ✘✔✘✘✘ CVE-2026-98559         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98559
  │ ✘✔✘✘✘ CVE-2026-98561         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98561
  │ ✘✔✘✘✘ CVE-2026-98565         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98565
  │ ✘✔✘✘✘ CVE-2026-98566         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98566
  │ ✘✔✘✘✘ CVE-2026-98567         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98567
  │ ✘✔✘✘✘ CVE-2026-98568         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98568
  │ ✘✔✘✘✘ CVE-2026-98569         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98569
  │ ✘✔✘✘✘ CVE-2026-98570         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98570
  │ ✘✔✘✘✘ CVE-2026-98572         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98572
  │ ✘✔✘✘✘ CVE-2026-98573         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98573
  │ ✘✔✘✘✘ CVE-2026-98575         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98575
  │ ✘✔✘✘✘ CVE-2026-98576         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98576
  │ ✘✔✘✘✘ CVE-2026-98577         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98577
  │ ✘✔✘✘✘ CVE-2026-98578         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98578
  │ ✘✔✘✘✘ CVE-2026-98579         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98579
  │ ✘✔✘✘✘ CVE-2026-98580         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98580
  │ ✘✔✘✘✘ CVE-2026-98581         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98581
  │ ✘✔✘✘✘ CVE-2026-98582         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98582
  │ ✘✔✘✘✘ CVE-2026-98583         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98583
  │ ✘✔✘✘✘ CVE-2026-98586         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98586
  │ ✘✔✘✘✘ CVE-2026-98588         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98588
  │ ✘✔✘✘✘ CVE-2026-98589         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98589
  │ ✘✔✘✘✘ CVE-2026-98590         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98590
  │ ✘✔✘✘✘ CVE-2026-98591         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98591
  │ ✘✔✘✘✘ CVE-2026-98593         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98593
  │ ✘✔✘✘✘ CVE-2026-98594         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98594
  │ ✘✔✘✘✘ CVE-2026-98597         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98597
  │ ✘✔✘✘✘ CVE-2026-98598         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98598
  │ ✘✔✘✘✘ CVE-2026-98599         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98599
  │ ✘✔✘✘✘ CVE-2026-98602         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98602
  │ ✘✔✘✘✘ CVE-2026-98605         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98605
  │ ✘✔✘✘✘ CVE-2026-98606         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98606
  │ ✘✔✘✘✘ CVE-2026-98607         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98607
  │ ✘✔✘✘✘ CVE-2026-98608         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98608
  │ ✘✔✘✘✘ CVE-2026-98609         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98609
  │ ✘✔✘✘✘ CVE-2026-98610         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98610
  │ ✘✔✘✘✘ CVE-2026-98612         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98612
  │ ✘✔✘✘✘ CVE-2026-98614         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98614
  │ ✘✔✘✘✘ CVE-2026-98620         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98620
  │ ✘✔✘✘✘ CVE-2026-98621         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98621
  │ ✘✔✘✘✘ CVE-2026-98622         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98622
  │ ✘✔✘✘✘ CVE-2026-98623         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98623
  │ ✘✔✘✘✘ CVE-2026-98624         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98624
  │ ✘✔✘✘✘ CVE-2026-98625         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98625
  │ ✘✔✘✘✘ CVE-2026-98626         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98626
  │ ✘✔✘✘✘ CVE-2026-98628         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98628
  │ ✘✔✘✘✘ CVE-2026-98629         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98629
  │ ✘✔✘✘✘ CVE-2026-98631         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98631
  │ ✘✔✘✘✘ CVE-2026-98632         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98632
  │ ✘✔✘✘✘ CVE-2026-98634         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98634
  │ ✘✔✘✘✘ CVE-2026-98636         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98636
  │ ✘✔✘✘✘ CVE-2026-98640         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98640
  │ ✘✔✘✘✘ CVE-2026-98642         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98642
  │ ✘✔✘✘✘ CVE-2026-98643         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98643
  │ ✘✔✘✘✘ CVE-2026-98644         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98644
  │ ✘✔✘✘✘ CVE-2026-98646         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98646
  │ ✘✔✘✘✘ CVE-2026-98647         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98647
  │ ✘✔✘✘✘ CVE-2026-98652         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98652
  │ ✘✔✘✘✘ CVE-2026-98655         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98655
  │ ✘✔✘✘✘ CVE-2026-98656         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98656
  │ ✘✔✘✘✘ CVE-2026-98657         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98657
  │ ✘✔✘✘✘ CVE-2026-98660         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98660
  │ ✘✔✘✘✘ CVE-2026-98661         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98661
  │ ✘✔✘✘✘ CVE-2026-98662         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98662
  │ ✘✔✘✘✘ CVE-2026-98663         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98663
  │ ✘✔✘✘✘ CVE-2026-98664         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98664
  │ ✘✔✘✘✘ CVE-2026-98665         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98665
  │ ✘✔✘✘✘ CVE-2026-98666         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98666
  │ ✘✔✘✘✘ CVE-2026-98668         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98668
  │ ✘✔✘✘✘ CVE-2026-98669         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98669
  │ ✘✔✘✘✘ CVE-2026-98670         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98670
  │ ✘✔✘✘✘ CVE-2026-98671         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98671
  │ ✘✔✘✘✘ CVE-2026-98672         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98672
  │ ✘✔✘✘✘ CVE-2026-98677         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98677
  │ ✘✔✘✘✘ CVE-2026-98679         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98679
  │ ✘✔✘✘✘ CVE-2026-98680         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98680
  │ ✘✔✘✘✘ CVE-2026-98681         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98681
  │ ✘✔✘✘✘ CVE-2026-98682         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98682
  │ ✘✔✘✘✘ CVE-2026-98683         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98683
  │ ✘✔✘✘✘ CVE-2026-98684         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98684
  │ ✘✔✘✘✘ CVE-2026-98685         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98685
  │ ✘✔✘✘✘ CVE-2026-98686         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98686
  │ ✘✔✘✘✘ CVE-2026-98687         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98687
  │ ✘✔✘✘✘ CVE-2026-98694         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98694
  │ ✘✔✘✘✘ CVE-2026-98695         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98695
  │ ✘✔✘✘✘ CVE-2026-98696         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98696
  │ ✘✔✘✘✘ CVE-2026-98697         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98697
  │ ✘✔✘✘✘ CVE-2026-98698         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98698
  │ ✘✔✘✘✘ CVE-2026-98699         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98699
  │ ✘✔✘✘✘ CVE-2026-98700         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98700
  │ ✘✔✘✘✘ CVE-2026-98701         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98701
  │ ✘✔✘✘✘ CVE-2026-98703         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98703
  │ ✘✔✘✘✘ CVE-2026-98704         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98704
  │ ✘✔✘✘✘ CVE-2026-98705         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98705
  │ ✘✔✘✘✘ CVE-2026-98706         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98706
  │ ✘✔✘✘✘ CVE-2026-98707         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98707
  │ ✘✔✘✘✘ CVE-2026-98708         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98708
  │ ✘✔✘✘✘ CVE-2026-98709         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98709
  │ ✘✔✘✘✘ CVE-2026-98710         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98710
  │ ✘✔✘✘✘ CVE-2026-98711         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98711
  │ ✘✔✘✘✘ CVE-2026-98714         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98714
  │ ✘✔✘✘✘ CVE-2026-98715         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98715
  │ ✘✔✘✘✘ CVE-2026-98716         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98716
  │ ✘✔✘✘✘ CVE-2026-98717         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98717
  │ ✘✔✘✘✘ CVE-2026-98720         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98720
  │ ✘✔✘✘✘ CVE-2026-98721         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98721
  │ ✘✔✘✘✘ CVE-2026-98722         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98722
  │ ✘✔✘✘✘ CVE-2026-98725         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98725
  │ ✘✔✘✘✘ CVE-2026-98726         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98726
  │ ✘✔✘✘✘ CVE-2026-98732         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98732
  │ ✘✔✘✘✘ CVE-2026-98733         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98733
  │ ✘✔✘✘✘ CVE-2026-98734         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98734
  │ ✘✔✘✘✘ CVE-2026-98735         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98735
  │ ✘✔✘✘✘ CVE-2026-98736         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98736
  │ ✘✔✘✘✘ CVE-2026-98737         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98737
  │ ✘✔✘✘✘ CVE-2026-98738         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98738
  │ ✘✔✘✘✘ CVE-2026-98739         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98739
  │ ✘✔✘✘✘ CVE-2026-98740         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98740
  │ ✘✔✘✘✘ CVE-2026-98741         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98741
  │ ✘✔✘✘✘ CVE-2026-98742         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98742
  │ ✘✔✘✘✘ CVE-2026-98743         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98743
  │ ✘✔✘✘✘ CVE-2026-98744         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98744
  │ ✘✔✘✘✘ CVE-2026-98745         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98745
  │ ✘✔✘✘✘ CVE-2026-98746         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98746
  │ ✘✔✘✘✘ CVE-2026-98747         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98747
  │ ✘✔✘✘✘ CVE-2026-98748         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98748
  │ ✘✔✘✘✘ CVE-2026-98749         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98749
  │ ✘✔✘✘✘ CVE-2026-98750         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98750
  │ ✘✔✘✘✘ CVE-2026-98751         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98751
  │ ✘✔✘✘✘ CVE-2026-98752         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98752
  │ ✘✔✘✘✘ CVE-2026-98753         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98753
  │ ✘✔✘✘✘ CVE-2026-98754         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98754
  │ ✘✔✘✘✘ CVE-2026-98755         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98755
  │ ✘✔✘✘✘ CVE-2026-98756         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98756
  │ ✘✔✘✘✘ CVE-2026-98757         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98757
  │ ✘✔✘✘✘ CVE-2026-98758         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98758
  │ ✘✔✘✘✘ CVE-2026-98760         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98760
  │ ✘✔✘✘✘ CVE-2026-98761         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98761
  │ ✘✔✘✘✘ CVE-2026-98762         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98762
  │ ✘✔✘✘✘ CVE-2026-98763         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98763
  │ ✘✔✘✘✘ CVE-2026-98764         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98764
  │ ✘✔✘✘✘ CVE-2026-98765         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98765
  │ ✘✔✘✘✘ CVE-2026-98766         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98766
  │ ✘✔✘✘✘ CVE-2026-98767         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98767
  │ ✘✔✘✘✘ CVE-2026-98768         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98768
  │ ✘✔✘✘✘ CVE-2026-98769         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98769
  │ ✘✔✘✘✘ CVE-2026-98770         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98770
  │ ✘✔✘✘✘ CVE-2026-98771         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98771
  │ ✘✔✘✘✘ CVE-2026-98772         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98772
  │ ✘✔✘✘✘ CVE-2026-98773         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98773
  │ ✘✔✘✘✘ CVE-2026-98775         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98775
  │ ✘✔✘✘✘ CVE-2026-98777         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98777
  │ ✘✔✘✘✘ CVE-2026-98778         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98778
  │ ✘✔✘✘✘ CVE-2026-98779         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98779
  │ ✘✔✘✘✘ CVE-2026-98780         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98780
  │ ✘✔✘✘✘ CVE-2026-98781         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98781
  │ ✘✔✘✘✘ CVE-2026-98782         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98782
  │ ✘✔✘✘✘ CVE-2026-98783         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98783
  │ ✘✔✘✘✘ CVE-2026-98784         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98784
  │ ✘✔✘✘✘ CVE-2026-98785         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98785
  │ ✘✔✘✘✘ CVE-2026-98786         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98786
  │ ✘✔✘✘✘ CVE-2026-98789         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98789
  │ ✘✔✘✘✘ CVE-2026-98790         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98790
  │ ✘✔✘✘✘ CVE-2026-98791         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98791
  │ ✘✔✘✘✘ CVE-2026-98792         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98792
  │ ✘✔✘✘✘ CVE-2026-98793         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98793
  │ ✘✔✘✘✘ CVE-2026-98794         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98794
  │ ✘✔✘✘✘ CVE-2026-98795         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98795
  │ ✘✔✘✘✘ CVE-2026-98796         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98796
  │ ✘✔✘✘✘ CVE-2026-98797         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98797
  │ ✘✔✘✘✘ CVE-2026-98798         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98798
  │ ✘✔✘✘✘ CVE-2026-98799         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98799
  │ ✘✔✘✘✘ CVE-2026-98800         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98800
  │ ✘✔✘✘✘ CVE-2026-98801         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98801
  │ ✘✔✘✘✘ CVE-2026-98802         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98802
  │ ✘✔✘✘✘ CVE-2026-98803         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98803
  │ ✘✔✘✘✘ CVE-2026-98805         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98805
  │ ✘✔✘✘✘ CVE-2026-98807         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98807
  │ ✘✔✘✘✘ CVE-2026-98808         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98808
  │ ✘✔✘✘✘ CVE-2026-98809         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98809
  │ ✘✔✘✘✘ CVE-2026-98810         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98810
  │ ✘✔✘✘✘ CVE-2026-98811         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98811
  │ ✘✔✘✘✘ CVE-2026-98812         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98812
  │ ✘✔✘✘✘ CVE-2026-98813         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98813
  │ ✘✔✘✘✘ CVE-2026-98814         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98814
  │ ✘✔✘✘✘ CVE-2026-98815         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98815
  │ ✘✔✘✘✘ CVE-2026-98816         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98816
  │ ✘✔✘✘✘ CVE-2026-98819         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98819
  │ ✘✔✘✘✘ CVE-2026-98820         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98820
  │ ✘✔✘✘✘ CVE-2026-98822         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98822
  │ ✘✔✘✘✘ CVE-2026-98823         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98823
  │ ✘✔✘✘✘ CVE-2026-98824         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98824
  │ ✘✔✘✘✘ CVE-2026-98825         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98825
  │ ✘✔✘✘✘ CVE-2026-98826         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98826
  │ ✘✔✘✘✘ CVE-2026-98827         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98827
  │ ✘✔✘✘✘ CVE-2026-98828         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98828
  │ ✘✔✘✘✘ CVE-2026-98829         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98829
  │ ✘✔✘✘✘ CVE-2026-98830         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98830
  │ ✘✔✘✘✘ CVE-2026-98831         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98831
  │ ✘✔✘✘✘ CVE-2026-98833         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98833
  │ ✘✔✘✘✘ CVE-2026-98834         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98834
  │ ✘✔✘✘✘ CVE-2026-98835         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98835
  │ ✘✔✘✘✘ CVE-2026-98836         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98836
  │ ✘✔✘✘✘ CVE-2026-98837         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98837
  │ ✘✔✘✘✘ CVE-2026-98838         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98838
  │ ✘✔✘✘✘ CVE-2026-98839         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98839
  │ ✘✔✘✘✘ CVE-2026-98840         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98840
  │ ✘✔✘✘✘ CVE-2026-98844         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98844
  │ ✘✔✘✘✘ CVE-2026-98846         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98846
  │ ✘✔✘✘✘ CVE-2026-98847         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98847
  │ ✘✔✘✘✘ CVE-2026-98848         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98848
  │ ✘✔✘✘✘ CVE-2026-98850         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98850
  │ ✘✔✘✘✘ CVE-2026-98851         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98851
  │ ✘✔✘✘✘ CVE-2026-98852         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98852
  │ ✘✔✘✘✘ CVE-2026-98853         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98853
  │ ✘✔✘✘✘ CVE-2026-98854         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98854
  │ ✘✔✘✘✘ CVE-2026-98855         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98855
  │ ✘✔✘✘✘ CVE-2026-98856         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98856
  │ ✘✔✘✘✘ CVE-2026-98857         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98857
  │ ✘✔✘✘✘ CVE-2026-98859         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98859
  │ ✘✔✘✘✘ CVE-2026-98862         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98862
  │ ✘✔✘✘✘ CVE-2026-98863         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98863
  │ ✘✔✘✘✘ CVE-2026-98872         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98872
  │ ✘✔✘✘✘ CVE-2026-98873         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98873
  │ ✘✔✘✘✘ CVE-2026-98874         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98874
  │ ✘✔✘✘✘ CVE-2026-98875         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98875
  │ ✘✔✘✘✘ CVE-2026-98876         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98876
  │ ✘✔✘✘✘ CVE-2026-98877         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98877
  │ ✘✔✘✘✘ CVE-2026-98878         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98878
  │ ✘✔✘✘✘ CVE-2026-98879         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98879
  │ ✘✔✘✘✘ CVE-2026-98880         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98880
  │ ✘✔✘✘✘ CVE-2026-98881         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98881
  │ ✘✔✘✘✘ CVE-2026-98882         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98882
  │ ✘✔✘✘✘ CVE-2026-98883         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98883
  │ ✘✔✘✘✘ CVE-2026-98884         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98884
  │ ✘✔✘✘✘ CVE-2026-98885         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98885
  │ ✘✔✘✘✘ CVE-2026-98886         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98886
  │ ✘✔✘✘✘ CVE-2026-98887         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98887
  │ ✘✔✘✘✘ CVE-2026-98888         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98888
  │ ✘✔✘✘✘ CVE-2026-98890         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98890
  │ ✘✔✘✘✘ CVE-2026-98891         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98891
  │ ✘✔✘✘✘ CVE-2026-98892         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98892
  │ ✘✔✘✘✘ CVE-2026-98893         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98893
  │ ✘✔✘✘✘ CVE-2026-98894         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98894
  │ ✘✔✘✘✘ CVE-2026-98896         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98896
  │ ✘✔✘✘✘ CVE-2026-98897         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98897
  │ ✘✔✘✘✘ CVE-2026-98898         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98898
  │ ✘✔✘✘✘ CVE-2026-98900         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98900
  │ ✘✔✘✘✘ CVE-2026-98901         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98901
  │ ✘✔✘✘✘ CVE-2026-98902         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98902
  │ ✘✔✘✘✘ CVE-2026-98903         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98903
  │ ✘✔✘✘✘ CVE-2026-98904         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98904
  │ ✘✔✘✘✘ CVE-2026-98905         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98905
  │ ✘✔✘✘✘ CVE-2026-98906         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98906
  │ ✘✔✘✘✘ CVE-2026-98907         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98907
  │ ✘✔✘✘✘ CVE-2026-98908         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98908
  │ ✘✔✘✘✘ CVE-2026-98909         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98909
  │ ✘✔✘✘✘ CVE-2026-98910         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98910
  │ ✘✔✘✘✘ CVE-2026-98912         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98912
  │ ✘✔✘✘✘ CVE-2026-98913         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98913
  │ ✘✔✘✘✘ CVE-2026-98914         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98914
  │ ✘✔✘✘✘ CVE-2026-98915         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98915
  │ ✘✔✘✘✘ CVE-2026-98916         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98916
  │ ✘✔✘✘✘ CVE-2026-98917         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98917
  │ ✘✔✘✘✘ CVE-2026-98923         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98923
  │ ✘✔✘✘✘ CVE-2026-98924         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98924
  │ ✘✔✘✘✘ CVE-2026-98925         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98925
  │ ✘✔✘✘✘ CVE-2026-98926         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98926
  │ ✘✔✘✘✘ CVE-2026-98929         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98929
  │ ✘✔✘✘✘ CVE-2026-98930         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98930
  │ ✘✔✘✘✘ CVE-2026-98931         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98931
  │ ✘✔✘✘✘ CVE-2026-98933         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98933
  │ ✘✔✘✘✘ CVE-2026-98934         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98934
  │ ✘✔✘✘✘ CVE-2026-98935         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98935
  │ ✘✔✘✘✘ CVE-2026-98936         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98936
  │ ✘✔✘✘✘ CVE-2026-98937         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98937
  │ ✘✔✘✘✘ CVE-2026-98940         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98940
  │ ✘✔✘✘✘ CVE-2026-98942         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98942
  │ ✘✔✘✘✘ CVE-2026-98946         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98946
  │ ✘✔✘✘✘ CVE-2026-98947         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98947
  │ ✘✔✘✘✘ CVE-2026-98948         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98948
  │ ✘✔✘✘✘ CVE-2026-98949         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98949
  │ ✘✔✘✘✘ CVE-2026-98950         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98950
  │ ✘✔✘✘✘ CVE-2026-98951         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98951
  │ ✘✔✘✘✘ CVE-2026-98953         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98953
  │ ✘✔✘✘✘ CVE-2026-98954         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98954
  │ ✘✔✘✘✘ CVE-2026-98955         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98955
  │ ✘✔✘✘✘ CVE-2026-98956         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98956
  │ ✘✔✘✘✘ CVE-2026-98957         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98957
  │ ✘✔✘✘✘ CVE-2026-98966         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98966
  │ ✘✔✘✘✘ CVE-2026-98967         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98967
  │ ✘✔✘✘✘ CVE-2026-98969         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98969
  │ ✘✔✘✘✘ CVE-2026-98970         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98970
  │ ✘✔✘✘✘ CVE-2026-98971         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98971
  │ ✘✔✘✘✘ CVE-2026-98972         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98972
  │ ✘✔✘✘✘ CVE-2026-98977         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98977
  │ ✘✔✘✘✘ CVE-2026-98979         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98979
  │ ✘✔✘✘✘ CVE-2026-98983         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98983
  │ ✘✔✘✘✘ CVE-2026-98984         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98984
  │ ✘✔✘✘✘ CVE-2026-98985         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98985
  │ ✘✔✘✘✘ CVE-2026-98989         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98989
  │ ✘✔✘✘✘ CVE-2026-98990         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98990
  │ ✘✔✘✘✘ CVE-2026-98992         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98992
  │ ✘✔✘✘✘ CVE-2026-98996         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98996
  │ ✘✔✘✘✘ CVE-2026-99004         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99004
  │ ✘✔✘✘✘ CVE-2026-99005         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99005
  │ ✘✔✘✘✘ CVE-2026-99007         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99007
  │ ✘✔✘✘✘ CVE-2026-99008         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99008
  │ ✘✔✘✘✘ CVE-2026-99009         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99009
  │ ✘✔✘✘✘ CVE-2026-99010         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99010
  │ ✘✔✘✘✘ CVE-2026-99015         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99015
  │ ✘✔✘✘✘ CVE-2026-99019         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99019
  │ ✘✔✘✘✘ CVE-2026-99020         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99020
  │ ✘✔✘✘✘ CVE-2026-99021         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99021
  │ ✘✔✘✘✘ CVE-2026-99022         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99022
  │ ✘✔✘✘✘ CVE-2026-99024         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99024
  │ ✘✔✘✘✘ CVE-2026-99025         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99025
  │ ✘✔✘✘✘ CVE-2026-99026         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99026
  │ ✘✔✘✘✘ CVE-2026-99027         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99027
  │ ✘✔✘✘✘ CVE-2026-99028         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99028
  │ ✘✔✘✘✘ CVE-2026-99031         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99031
  │ ✘✔✘✘✘ CVE-2026-99033         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99033
  │ ✘✔✘✘✘ CVE-2026-99034         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99034
  │ ✘✔✘✘✘ CVE-2026-99035         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99035
  │ ✘✔✘✘✘ CVE-2026-99036         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99036
  │ ✘✔✘✘✘ CVE-2026-99037         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99037
  │ ✘✔✘✘✘ CVE-2026-99038         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99038
  │ ✘✔✘✘✘ CVE-2026-99039         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99039
  │ ✘✔✘✘✘ CVE-2026-99040         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99040
  │ ✘✔✘✘✘ CVE-2026-99041         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99041
  │ ✘✔✘✘✘ CVE-2026-99043         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99043
  │ ✘✔✘✘✘ CVE-2026-99045         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99045
  │ ✘✔✘✘✘ CVE-2026-99049         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99049
  │ ✘✔✘✘✘ CVE-2026-99052         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99052
  │ ✘✔✘✘✘ CVE-2026-99057         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99057
  │ ✘✔✘✘✘ CVE-2026-99058         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99058
  │ ✘✔✘✘✘ CVE-2026-99060         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99060
  │ ✘✔✘✘✘ CVE-2026-99061         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99061
  │ ✘✔✘✘✘ CVE-2026-99062         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99062
  │ ✘✔✘✘✘ CVE-2026-99063         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99063
  │ ✘✔✘✘✘ CVE-2026-99067         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99067
  │ ✘✔✘✘✘ CVE-2026-99070         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99070
  │ ✘✔✘✘✘ CVE-2026-99071         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99071
  │ ✘✔✘✘✘ CVE-2026-99072         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99072
  │ ✘✔✘✘✘ CVE-2026-99074         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99074
  │ ✘✔✘✘✘ CVE-2026-99076         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99076
  │ ✘✔✘✘✘ CVE-2026-99080         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99080
  │ ✘✔✘✘✘ CVE-2026-99086         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99086
  │ ✘✔✘✘✘ CVE-2026-99087         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99087
  │ ✘✔✘✘✘ CVE-2026-99088         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99088
  │ ✘✔✘✘✘ CVE-2026-99089         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99089
  │ ✘✔✘✘✘ CVE-2026-99090         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99090
  │ ✘✔✘✘✘ CVE-2026-99091         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99091
  │ ✘✔✘✘✘ CVE-2026-99095         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99095
  │ ✘✔✘✘✘ CVE-2026-99100         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99100
  │ ✘✔✘✘✘ CVE-2026-99101         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99101
  │ ✘✔✘✘✘ CVE-2026-99103         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99103
  │ ✘✔✘✘✘ CVE-2026-99106         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99106
  │ ✘✔✘✘✘ CVE-2026-99113         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99113
  │ ✘✔✘✘✘ CVE-2026-99114         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99114
  │ ✘✔✘✘✘ CVE-2026-99115         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99115
  │ ✘✔✘✘✘ CVE-2026-99118         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99118
  │ ✘✔✘✘✘ CVE-2026-99121         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99121
  │ ✘✔✘✘✘ CVE-2026-99124         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99124
  │ ✘✔✘✘✘ CVE-2026-99126         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99126
  │ ✘✔✘✘✘ CVE-2026-99127         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99127
  │ ✘✔✘✘✘ CVE-2026-99128         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99128
  │ ✘✔✘✘✘ CVE-2026-99130         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99130
  │ ✘✔✘✘✘ CVE-2026-99132         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99132
  │ ✘✔✘✘✘ CVE-2026-99133         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99133
  │ ✘✔✘✘✘ CVE-2026-99134         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99134
  │ ✘✔✘✘✘ CVE-2026-99135         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99135
  │ ✘✔✘✘✘ CVE-2026-99138         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99138
  │ ✘✔✘✘✘ CVE-2026-99139         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99139
  │ ✘✔✘✘✘ CVE-2026-99140         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99140
  │ ✘✔✘✘✘ CVE-2026-99146         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99146
  │ ✘✔✘✘✘ CVE-2026-99147         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99147
  │ ✘✔✘✘✘ CVE-2026-99150         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99150
  │ ✘✔✘✘✘ CVE-2026-99155         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99155
  │ ✘✔✘✘✘ CVE-2026-99157         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99157
  │ ✘✔✘✘✘ CVE-2026-99161         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99161
  │ ✘✔✘✘✘ CVE-2026-99165         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99165
  │ ✘✔✘✘✘ CVE-2026-99166         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99166
  │ ✘✔✘✘✘ CVE-2026-99169         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99169
  │ ✘✔✘✘✘ CVE-2026-99171         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99171
  │ ✘✔✘✘✘ CVE-2026-99172         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99172
  │ ✘✔✘✘✘ CVE-2026-99174         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99174
  │ ✘✔✘✘✘ CVE-2026-99175         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99175
  │ ✘✔✘✘✘ CVE-2026-99176         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99176
  │ ✘✔✘✘✘ CVE-2026-99178         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99178
  │ ✘✔✘✘✘ CVE-2026-99179         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99179
  │ ✘✔✘✘✘ CVE-2026-99181         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99181
  │ ✘✔✘✘✘ CVE-2026-99182         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99182
  │ ✘✔✘✘✘ CVE-2026-99187         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99187
  │ ✘✔✘✘✘ CVE-2026-99189         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99189
  │ ✘✔✘✘✘ CVE-2026-99191         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99191
  │ ✘✔✘✘✘ CVE-2026-99192         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99192
  │ ✘✔✘✘✘ CVE-2026-99201         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99201
  │ ✘✔✘✘✘ CVE-2026-99202         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99202
  │ ✘✔✘✘✘ CVE-2026-99204         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99204
  │ ✘✔✘✘✘ CVE-2026-99206         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99206
  │ ✘✔✘✘✘ CVE-2026-99209         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99209
  │ ✘✔✘✘✘ CVE-2026-99211         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99211
  │ ✘✔✘✘✘ CVE-2026-99215         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99215
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/login@1%3A4.13%2Bdfsg1-4ubuntu3.2
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2024-56433         LOW          3.6   0.4%   ·  ↳ S:UBUNTU-CVE-2024-56433 | V:UB:CVE-2024-56433
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/mount@2.39.3-9ubuntu6.5
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-53612         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53612,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53613         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53613,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53614         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53614,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53615,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-76642
  │ ✘✔✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78408
  │ ✘✔✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78409
  │ ✘✔✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78410
  │ ✘✔✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-13595,USN-8702-1
  │ ✘✔✔✘✘ CVE-2026-27456         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-27456,USN-8702-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/ncurses-base@6.4%2B20240113-1ubuntu2
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2025-69720         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-69720 | V:UB:CVE-2025-69720
  │ ✘✔✔✘✘ CVE-2025-6141          MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-6141,USN-8709-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/ncurses-bin@6.4%2B20240113-1ubuntu2
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2025-69720         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-69720 | V:UB:CVE-2025-69720
  │ ✘✔✔✘✔ CVE-2025-6141          MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-6141,USN-8709-1 | V:UB:CVE-2025-6141
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/openssl@3.0.13-0ubuntu3.12
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-75803         CRITICAL     9.1   0.3%   ·  ↳ O:UBUNTU-CVE-2026-75803,USN-8678-1 | S:UBUNTU-CVE-2026-75803,USN-8678-1 | V:UB:CVE-2026-75803
  │ ✔✔✔✔✔ CVE-2026-54874         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-54874,USN-8678-1 | S:UBUNTU-CVE-2026-54874,USN-8678-1 | V:UB:CVE-2026-54874
  │ ✔✔✔✔✔ CVE-2026-63072         HIGH         7.5   0.9%   ·  ↳ O:UBUNTU-CVE-2026-63072,USN-8678-1 | S:UBUNTU-CVE-2026-63072,USN-8678-1 | V:UB:CVE-2026-63072
  │ ✔✔✔✔✔ CVE-2026-63076         HIGH         7.5   1.6%   ·  ↳ O:UBUNTU-CVE-2026-63076,USN-8678-1 | S:UBUNTU-CVE-2026-63076,USN-8678-1 | V:UB:CVE-2026-63076
  │ ✔✔✔✔✘ CVE-2026-84782         HIGH         8.2   0.8%   ·  ↳ O:UBUNTU-CVE-2026-84782,USN-8847-1 | S:UBUNTU-CVE-2026-84782,USN-8847-1
  │ ✔✔✔✔✘ CVE-2026-35189         MEDIUM       5.3   0.3%   ·  ↳ O:UBUNTU-CVE-2026-35189,USN-8847-1 | S:UBUNTU-CVE-2026-35189,USN-8847-1
  │ ✔✔✔✔✔ CVE-2026-63074         MEDIUM       5.9   0.6%   ·  ↳ O:UBUNTU-CVE-2026-63074,USN-8678-1 | S:UBUNTU-CVE-2026-63074,USN-8678-1 | V:UB:CVE-2026-63074
  │ ✔✔✔✔✘ CVE-2026-75805         MEDIUM       5.3   0.3%   ·  ↳ O:UBUNTU-CVE-2026-75805,USN-8847-1 | S:UBUNTU-CVE-2026-75805,USN-8847-1
  │ ✔✔✔✔✘ CVE-2026-75806         MEDIUM       5.3   1.1%   ·  ↳ O:UBUNTU-CVE-2026-75806,USN-8847-1 | S:UBUNTU-CVE-2026-75806,USN-8847-1
  │ ✔✔✔✔✘ CVE-2026-54872         LOW          3.7   0.4%   ·  ↳ O:UBUNTU-CVE-2026-54872,USN-8847-1 | S:UBUNTU-CVE-2026-54872,USN-8847-1
  │ ✔✔✔✔✘ CVE-2026-77696         LOW          3.7   0.4%   ·  ↳ O:UBUNTU-CVE-2026-77696,USN-8847-1 | S:UBUNTU-CVE-2026-77696,USN-8847-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/passwd@1%3A4.13%2Bdfsg1-4ubuntu3.2
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2024-56433         LOW          3.6   0.4%   ·  ↳ S:UBUNTU-CVE-2024-56433 | V:UB:CVE-2024-56433
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/patch@2.7.6-7build3
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2018-6952          HIGH         7.5   8.2%   ·  ↳ O:UBUNTU-CVE-2018-6952 | S:UBUNTU-CVE-2018-6952 | V:UB:CVE-2018-6952
  │ ✔✔✔✔✔ CVE-2019-20633         MEDIUM       5.5   1.0%   ·  ↳ O:UBUNTU-CVE-2019-20633 | S:UBUNTU-CVE-2019-20633 | V:UB:CVE-2019-20633
  │ ✔✔✔✔✔ CVE-2021-45261         MEDIUM       5.5   0.8%   ·  ↳ O:UBUNTU-CVE-2021-45261 | S:UBUNTU-CVE-2021-45261 | V:UB:CVE-2021-45261
  │ ✔✔✔✘✘ CVE-2026-115207        MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-115207 | S:UBUNTU-CVE-2026-115207
  │ ✔✔✔✔✔ CVE-2026-56288         MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-56288 | S:UBUNTU-CVE-2026-56288 | V:UB:CVE-2026-56289
  │ ✔✔✔✔✔ CVE-2026-56289         MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-56289 | S:UBUNTU-CVE-2026-56289 | V:UB:CVE-2026-56289
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/perl@5.38.2-3.2ubuntu0.3
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-12087         CRITICAL     9.1   0.6%   ·  ↳ O:UBUNTU-CVE-2026-12087,USN-8684-1 | S:UBUNTU-CVE-2026-12087,USN-8684-1 | V:UB:CVE-2026-12087
  │ ✔✔✔✔✔ CVE-2026-13221         CRITICAL     9.1   0.5%   ·  ↳ O:UBUNTU-CVE-2026-13221,USN-8684-1 | S:UBUNTU-CVE-2026-13221,USN-8684-1 | V:UB:CVE-2026-13221
  │ ✔✔✔✔✔ CVE-2026-57433         CRITICAL     9.8   0.5%   ·  ↳ O:UBUNTU-CVE-2026-57433,USN-8684-1 | S:UBUNTU-CVE-2026-57433,USN-8684-1 | V:UB:CVE-2026-57433
  │ ✔✔✔✔✔ CVE-2026-48959         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-48959,USN-8684-1 | S:UBUNTU-CVE-2026-48959,USN-8684-1 | V:UB:CVE-2026-48959
  │ ✔✔✔✔✔ CVE-2026-48962         HIGH         7.8   0.4%   ·  ↳ O:UBUNTU-CVE-2026-48962,USN-8684-1 | S:UBUNTU-CVE-2026-48962,USN-8684-1 | V:UB:CVE-2026-48962
  │ ✔✔✔✔✔ CVE-2026-57432         HIGH         8.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57432,USN-8684-1 | S:UBUNTU-CVE-2026-57432,USN-8684-1 | V:UB:CVE-2026-57432
  │ ✔✔✔✔✔ CVE-2026-7017          HIGH         7.1   0.3%   ·  ↳ O:UBUNTU-CVE-2026-7017,USN-8684-1 | S:UBUNTU-CVE-2026-7017,USN-8684-1 | V:UB:CVE-2026-7017
  │ ✔✔✔✘✘ CVE-2026-82560         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-82560 | S:UBUNTU-CVE-2026-82560
  │ ✔✔✔✔✔ CVE-2026-9538          HIGH         7.5   0.5%   ·  ↳ O:UBUNTU-CVE-2026-9538,USN-8684-1 | S:UBUNTU-CVE-2026-9538,USN-8684-1 | V:UB:CVE-2026-9538
  │ ✔✔✔✔✔ CVE-2025-15649         MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2025-15649,USN-8684-1 | S:UBUNTU-CVE-2025-15649,USN-8684-1 | V:UB:CVE-2025-15649
  │ ✔✔✔✔✘ CVE-2026-15534         MEDIUM       5.7   0.2%   ·  ↳ O:UBUNTU-CVE-2026-15534,USN-8736-2 | S:UBUNTU-CVE-2026-15534,USN-8736-2
  │ ✔✔✔✔✘ CVE-2026-19487         MEDIUM       5.3   0.4%   ·  ↳ O:UBUNTU-CVE-2026-19487,USN-8736-2 | S:UBUNTU-CVE-2026-19487,USN-8736-2
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/perl-base@5.38.2-3.2ubuntu0.3
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-12087         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-12087,USN-8684-1
  │ ✘✔✔✘✘ CVE-2026-13221         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-13221,USN-8684-1
  │ ✘✔✔✘✘ CVE-2026-57433         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-57433,USN-8684-1
  │ ✘✔✔✘✘ CVE-2026-48959         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-48959,USN-8684-1
  │ ✘✔✔✘✘ CVE-2026-48962         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-48962,USN-8684-1
  │ ✘✔✔✘✘ CVE-2026-57432         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57432,USN-8684-1
  │ ✘✔✔✘✘ CVE-2026-7017          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-7017,USN-8684-1
  │ ✘✔✔✘✘ CVE-2026-82560         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-82560
  │ ✘✔✔✘✘ CVE-2026-9538          HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-9538,USN-8684-1
  │ ✘✔✔✘✘ CVE-2025-15649         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-15649,USN-8684-1
  │ ✘✔✔✘✔ CVE-2026-15534         MEDIUM       5.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15534,USN-8736-2 | V:UB:CVE-2026-15534
  │ ✘✔✔✘✔ CVE-2026-19487         MEDIUM       5.3   0.4%   ·  ↳ S:UBUNTU-CVE-2026-19487,USN-8736-2 | V:UB:CVE-2026-19487
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/perl-modules-5.38@5.38.2-3.2ubuntu0.3
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-12087         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-12087,USN-8684-1 | V:UB:CVE-2026-12087
  │ ✘✔✔✘✔ CVE-2026-13221         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-13221,USN-8684-1 | V:UB:CVE-2026-13221
  │ ✘✔✔✘✔ CVE-2026-57433         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-57433,USN-8684-1 | V:UB:CVE-2026-57433
  │ ✘✔✔✘✔ CVE-2026-48959         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-48959,USN-8684-1 | V:UB:CVE-2026-48959
  │ ✘✔✔✘✔ CVE-2026-48962         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-48962,USN-8684-1 | V:UB:CVE-2026-48962
  │ ✘✔✔✘✔ CVE-2026-57432         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57432,USN-8684-1 | V:UB:CVE-2026-57432
  │ ✘✔✔✘✔ CVE-2026-7017          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-7017,USN-8684-1 | V:UB:CVE-2026-7017
  │ ✘✔✔✘✘ CVE-2026-82560         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-82560
  │ ✘✔✔✘✔ CVE-2026-9538          HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-9538,USN-8684-1 | V:UB:CVE-2026-9538
  │ ✘✔✔✘✔ CVE-2025-15649         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-15649,USN-8684-1 | V:UB:CVE-2025-15649
  │ ✘✔✔✘✘ CVE-2026-15534         MEDIUM       5.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15534,USN-8736-2
  │ ✘✔✔✘✘ CVE-2026-19487         MEDIUM       5.3   0.4%   ·  ↳ S:UBUNTU-CVE-2026-19487,USN-8736-2
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-pip@24.0%2Bdfsg-1ubuntu1.3
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2024-39689         HIGH         7.5   1.0%   ·  ↳ S:UBUNTU-CVE-2024-39689
  │ ✘✔✔✘✔ CVE-2025-66418         HIGH         8.9   0.7%   ·  ↳ S:UBUNTU-CVE-2025-66418 | V:UB:CVE-2025-66418
  │ ✘✔✔✘✔ CVE-2025-66471         HIGH         8.9   0.7%   ·  ↳ S:UBUNTU-CVE-2025-66471,USN-8344-3 | V:UB:CVE-2025-66471
  │ ✘✔✔✘✔ CVE-2026-21441         HIGH         8.9   2.9%   ·  ↳ S:UBUNTU-CVE-2026-21441 | V:UB:CVE-2026-21441
  │ ✘✔✔✘✘ CVE-2026-44431         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-44431
  │ ✘✔✔✘✘ CVE-2026-44432         HIGH         8.9   0.7%   ·  ↳ S:UBUNTU-CVE-2026-44432
  │ ✘✔✔✘✘ CVE-2026-57585         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-57585
  │ ✘✔✔✘✘ CVE-2026-8643          HIGH         8.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-8643
  │ ✘✔✔✘✘ CVE-2026-97687         HIGH         8.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97687
  │ ✘✔✔✘✘ CVE-2026-97689         HIGH         8.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97689
  │ ✘✔✔✘✔ CVE-2024-35195         MEDIUM       5.6   0.3%   ·  ↳ S:UBUNTU-CVE-2024-35195 | V:UB:CVE-2024-35195
  │ ✘✔✔✘✘ CVE-2026-13346         MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-13346
  │ ✘✔✔✘✘ CVE-2026-25645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-25645
  │ ✘✔✔✘✘ CVE-2026-3219          MEDIUM       4.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-3219
  │ ✘✔✔✘✘ CVE-2026-45409         MEDIUM       6.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-45409
  │ ✘✔✔✘✘ CVE-2026-6357          MEDIUM       5.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6357
  │ ✘✔✔✘✘ CVE-2026-97688         MEDIUM       6.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97688
  │ ✘✔✔✘✔ CVE-2026-1703          LOW          2.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-1703 | V:UB:CVE-2026-1703
  │ ✘✔✘✘✔ CVE-2026-9375          ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-9375 | V:UB:CVE-2026-9375
  │ ✘✔✘✘✘ USN-8344-1             ?             -       -   ·
  │ ✘✔✘✘✘ USN-8344-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-pkg-resources@68.1.2-2ubuntu1.2
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-59890         MEDIUM       6.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-59890
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-setuptools@68.1.2-2ubuntu1.2
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-59890         MEDIUM       6.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-59890
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-wheel@0.42.0-2
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-24049         HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-24049,USN-8221-1 | V:UB:CVE-2026-24049
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3.12@3.12.3-1ubuntu0.15
  │ OSGTV
  │ ✔✔✔✘✘ CVE-2026-115557        CRITICAL     9.4   0.5%   ·  ↳ O:UBUNTU-CVE-2026-115557 | S:UBUNTU-CVE-2026-115557
  │ ✔✔✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.5%   ·  ↳ O:UBUNTU-CVE-2026-19445 | S:UBUNTU-CVE-2026-19445
  │ ✔✔✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·  ↳ O:UBUNTU-CVE-2026-11940 | S:UBUNTU-CVE-2026-11940
  │ ✔✔✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·  ↳ O:UBUNTU-CVE-2026-11972 | S:UBUNTU-CVE-2026-11972
  │ ✔✔✔✔✔ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ O:UBUNTU-CVE-2026-15308,USN-8744-1 | S:UBUNTU-CVE-2026-15308,USN-8744-1 | V:UB:CVE-2026-15308
  │ ✔✔✔✘✘ CVE-2026-19553         HIGH         7.6   0.5%   ·  ↳ O:UBUNTU-CVE-2026-19553 | S:UBUNTU-CVE-2026-19553
  │ ✔✔✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57178 | S:UBUNTU-CVE-2026-57178
  │ ✔✔✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·  ↳ O:UBUNTU-CVE-2026-7210 | S:UBUNTU-CVE-2026-7210
  │ ✔✔✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-82049 | S:UBUNTU-CVE-2026-82049
  │ ✔✔✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·  ↳ O:UBUNTU-CVE-2026-84366 | S:UBUNTU-CVE-2026-84366
  │ ✔✔✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.9%   ·  ↳ O:UBUNTU-CVE-2025-12781 | S:UBUNTU-CVE-2025-12781
  │ ✔✔✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·  ↳ O:UBUNTU-CVE-2025-15366 | S:UBUNTU-CVE-2025-15366
  │ ✔✔✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·  ↳ O:UBUNTU-CVE-2025-15367 | S:UBUNTU-CVE-2025-15367
  │ ✔✔✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-0864 | S:UBUNTU-CVE-2026-0864
  │ ✔✔✔✘✘ CVE-2026-114583        MEDIUM       6.9   0.2%   ·  ↳ O:UBUNTU-CVE-2026-114583 | S:UBUNTU-CVE-2026-114583
  │ ✔✔✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.3%   ·  ↳ O:UBUNTU-CVE-2026-12345 | S:UBUNTU-CVE-2026-12345
  │ ✔✔✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·  ↳ O:UBUNTU-CVE-2026-15806 | S:UBUNTU-CVE-2026-15806
  │ ✔✔✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·  ↳ O:UBUNTU-CVE-2026-17084 | S:UBUNTU-CVE-2026-17084
  │ ✔✔✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·  ↳ O:UBUNTU-CVE-2026-19672 | S:UBUNTU-CVE-2026-19672
  │ ✔✔✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-3446 | S:UBUNTU-CVE-2026-3446
  │ ✔✔✔✔✔ CVE-2026-4360          MEDIUM       5.3   0.5%   ·  ↳ O:UBUNTU-CVE-2026-4360,USN-8744-1 | S:UBUNTU-CVE-2026-4360,USN-8744-1 | V:UB:CVE-2026-4360
  │ ✔✔✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57175 | S:UBUNTU-CVE-2026-57175
  │ ✔✔✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57176 | S:UBUNTU-CVE-2026-57176
  │ ✔✔✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·  ↳ O:UBUNTU-CVE-2026-57177 | S:UBUNTU-CVE-2026-57177
  │ ✔✔✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57179 | S:UBUNTU-CVE-2026-57179
  │ ✔✔✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.6%   ·  ↳ O:UBUNTU-CVE-2026-87910 | S:UBUNTU-CVE-2026-87910
  │ ✔✔✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·  ↳ O:UBUNTU-CVE-2026-15310 | S:UBUNTU-CVE-2026-15310
  │ ✔✔✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·  ↳ O:UBUNTU-CVE-2026-18503 | S:UBUNTU-CVE-2026-18503
  │ ✔✔✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·  ↳ O:UBUNTU-CVE-2026-6879 | S:UBUNTU-CVE-2026-6879
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3.12-dev@3.12.3-1ubuntu0.15
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-115557        CRITICAL     9.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-115557
  │ ✘✔✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19445
  │ ✘✔✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-11940
  │ ✘✔✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2026-11972
  │ ✘✔✔✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-15308,USN-8744-1
  │ ✘✔✔✘✘ CVE-2026-19553         HIGH         7.6   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19553
  │ ✘✔✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57178
  │ ✘✔✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-7210
  │ ✘✔✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-82049
  │ ✘✔✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-84366
  │ ✘✔✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.9%   ·  ↳ S:UBUNTU-CVE-2025-12781
  │ ✘✔✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15366
  │ ✘✔✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15367
  │ ✘✔✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-0864
  │ ✘✔✔✘✘ CVE-2026-114583        MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-114583
  │ ✘✔✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-12345
  │ ✘✔✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15806
  │ ✘✔✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·  ↳ S:UBUNTU-CVE-2026-17084
  │ ✘✔✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19672
  │ ✘✔✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3446
  │ ✘✔✔✘✘ CVE-2026-4360          MEDIUM       5.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-4360,USN-8744-1
  │ ✘✔✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57175
  │ ✘✔✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57176
  │ ✘✔✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57177
  │ ✘✔✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57179
  │ ✘✔✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-87910
  │ ✘✔✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15310
  │ ✘✔✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18503
  │ ✘✔✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-6879
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3.12-minimal@3.12.3-1ubuntu0.15
  │ OSGTV
  │ ✘✔✔✘✘ CVE-2026-115557        CRITICAL     9.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-115557
  │ ✘✔✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19445
  │ ✘✔✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-11940
  │ ✘✔✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2026-11972
  │ ✘✔✔✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-15308,USN-8744-1
  │ ✘✔✔✘✘ CVE-2026-19553         HIGH         7.6   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19553
  │ ✘✔✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57178
  │ ✘✔✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-7210
  │ ✘✔✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-82049
  │ ✘✔✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-84366
  │ ✘✔✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.9%   ·  ↳ S:UBUNTU-CVE-2025-12781
  │ ✘✔✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15366
  │ ✘✔✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15367
  │ ✘✔✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-0864
  │ ✘✔✔✘✘ CVE-2026-114583        MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-114583
  │ ✘✔✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-12345
  │ ✘✔✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15806
  │ ✘✔✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·  ↳ S:UBUNTU-CVE-2026-17084
  │ ✘✔✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19672
  │ ✘✔✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3446
  │ ✘✔✔✘✘ CVE-2026-4360          MEDIUM       5.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-4360,USN-8744-1
  │ ✘✔✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57175
  │ ✘✔✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57176
  │ ✘✔✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57177
  │ ✘✔✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57179
  │ ✘✔✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-87910
  │ ✘✔✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15310
  │ ✘✔✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18503
  │ ✘✔✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-6879
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/tar@1.35%2Bdfsg-3build1
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2025-45582         MEDIUM       4.1   0.5%   ·  ↳ O:UBUNTU-CVE-2025-45582,USN-8510-1 | S:UBUNTU-CVE-2025-45582,USN-8510-1 | V:UB:CVE-2025-45582
  │ ✔✔✔✔✔ CVE-2026-18477         MEDIUM       4.4   0.1%   ·  ↳ O:UBUNTU-CVE-2026-18477 | S:UBUNTU-CVE-2026-18477 | V:UB:CVE-2026-18477
  │ ✔✔✔✔✔ CVE-2026-18508         MEDIUM       4.4   0.1%   ·  ↳ O:UBUNTU-CVE-2026-18508 | S:UBUNTU-CVE-2026-18508 | V:UB:CVE-2026-18508
  │ ✔✔✔✔✔ CVE-2026-5704          MEDIUM       5.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-5704,USN-8477-2,USN-8477-3 | S:UBUNTU-CVE-2026-5704,USN-8477-2,USN-8477-3 | V:UB:CVE-2026-5704
  │ ✔✔✘✘✘ USN-8477-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/util-linux@2.39.3-9ubuntu6.5
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-53612         HIGH         7.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-53612,USN-8702-1 | S:UBUNTU-CVE-2026-53612,USN-8702-1 | V:UB:CVE-2026-53612
  │ ✔✔✔✔✔ CVE-2026-53613         HIGH         7.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-53613,USN-8702-1 | S:UBUNTU-CVE-2026-53613,USN-8702-1 | V:UB:CVE-2026-53613
  │ ✔✔✔✔✔ CVE-2026-53614         HIGH         7.0   0.1%   ·  ↳ O:UBUNTU-CVE-2026-53614,USN-8702-1 | S:UBUNTU-CVE-2026-53614,USN-8702-1 | V:UB:CVE-2026-53614
  │ ✔✔✔✔✔ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-53615,USN-8702-1 | S:UBUNTU-CVE-2026-53615,USN-8702-1 | V:UB:CVE-2026-53615
  │ ✔✔✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ O:UBUNTU-CVE-2026-76642 | S:UBUNTU-CVE-2026-76642
  │ ✔✔✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ O:UBUNTU-CVE-2026-78408 | S:UBUNTU-CVE-2026-78408
  │ ✔✔✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-78409 | S:UBUNTU-CVE-2026-78409
  │ ✔✔✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-78410 | S:UBUNTU-CVE-2026-78410
  │ ✔✔✔✔✔ CVE-2026-13595         MEDIUM       6.8   0.1%   ·  ↳ O:UBUNTU-CVE-2026-13595,USN-8702-1 | S:UBUNTU-CVE-2026-13595,USN-8702-1 | V:UB:CVE-2026-13595
  │ ✔✔✔✔✔ CVE-2026-27456         MEDIUM       4.7   0.2%   ·  ↳ O:UBUNTU-CVE-2026-27456,USN-8702-1 | S:UBUNTU-CVE-2026-27456,USN-8702-1 | V:UB:CVE-2026-27456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/xz-utils@5.6.1%2Breally5.4.5-1ubuntu0.3
  │ OSGTV
  │ ✔✔✘✘✘ USN-8945-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/zlib1g@1%3A1.3.dfsg-3.1ubuntu2.1
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-85091         HIGH         8.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-85091,USN-8954-1 | V:UB:CVE-2026-85091
  │ ✘✔✔✘✔ CVE-2026-27171         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-27171,USN-8706-1 | V:UB:CVE-2026-27171
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/zlib1g-dev@1%3A1.3.dfsg-3.1ubuntu2.1
  │ OSGTV
  │ ✘✔✔✘✔ CVE-2026-85091         HIGH         8.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-85091,USN-8954-1 | V:UB:CVE-2026-85091
  │ ✘✔✔✘✔ CVE-2026-27171         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-27171,USN-8706-1 | V:UB:CVE-2026-27171
  └────────────────────────────────────────────────────────────────────────────────────────────────────

  ━━ Go ━━
  ┌─ pkg:golang/github.com/containerd/containerd/v2@v2.2.5
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-95837         HIGH         7.8   0.1%   ·  ↳ O:GHSA-p7v4-vr35-mj6f,GO-2026-6791 | S:GHSA-p7v4-vr35-mj6f,GO-2026-6791 | V:OSV:GHSA-P7V4-VR35-MJ6F
  │ ✘✘✘✘✔ CVE-2026-95839         HIGH         7.1      -   ·  ↳ V:MEND:CVE-2026-95839
  │ ✔✔✔✔✔ CVE-2026-53493         MEDIUM       6.9   0.4%   ·  ↳ O:GHSA-pg57-6jwg-q645,GO-2026-6597 | S:GHSA-pg57-6jwg-q645,GO-2026-6597 | V:MEND:CVE-2026-53493
  │ ✔✔✔✔✔ CVE-2026-53495         MEDIUM       6.8   0.2%   ·  ↳ O:GHSA-7jxh-36q5-gcqv,GO-2026-6444 | S:GHSA-7jxh-36q5-gcqv,GO-2026-6444 | V:MEND:CVE-2026-53495
  │ ✔✔✔✔✔ CVE-2026-95838         MEDIUM       4.6   0.2%   ·  ↳ O:GHSA-rp3h-jf77-q9p4,GO-2026-6796 | S:GHSA-rp3h-jf77-q9p4,GO-2026-6796 | V:OSV:GHSA-RP3H-JF77-Q9P4
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/containerd/containerd/v2@v2.3.3
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-95837         HIGH         7.8   0.1%   ·  ↳ O:GHSA-p7v4-vr35-mj6f,GO-2026-6791 | S:GHSA-p7v4-vr35-mj6f,GO-2026-6791 | V:MEND:CVE-2026-95837
  │ ✘✘✘✘✔ CVE-2026-95839         HIGH         7.1      -   ·  ↳ V:MEND:CVE-2026-95839
  │ ✔✔✔✔✔ CVE-2026-53493         MEDIUM       6.9   0.4%   ·  ↳ O:GHSA-pg57-6jwg-q645,GO-2026-6597 | S:GHSA-pg57-6jwg-q645,GO-2026-6597 | V:MEND:CVE-2026-53493
  │ ✔✔✔✔✔ CVE-2026-53495         MEDIUM       6.8   0.2%   ·  ↳ O:GHSA-7jxh-36q5-gcqv,GO-2026-6444 | S:GHSA-7jxh-36q5-gcqv,GO-2026-6444 | V:MEND:CVE-2026-53495
  │ ✔✔✔✔✔ CVE-2026-95838         MEDIUM       4.6   0.2%   ·  ↳ O:GHSA-rp3h-jf77-q9p4,GO-2026-6796 | S:GHSA-rp3h-jf77-q9p4,GO-2026-6796 | V:OSV:GHSA-RP3H-JF77-Q9P4
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/buildx@v0.35.0
  │ OSGTV
  │ ✘✘✘✘✔ CVE-2026-103433        MEDIUM       6.9   0.3%   ·  ↳ V:MEND:CVE-2026-103433
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/buildx@v0.36.0
  │ OSGTV
  │ ✘✘✘✘✔ CVE-2026-103433        MEDIUM       6.9   0.3%   ·  ↳ V:MEND:CVE-2026-103433
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/docker@v28.5.2%2Bincompatible
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-33997         HIGH         8.4   0.4%   ·  ↳ O:GHSA-pxq6-2prw-chj9,GO-2026-4883 | S:GHSA-pxq6-2prw-chj9,GO-2026-4883 | V:OSV:GO-2026-4883
  │ ✔✔✔✘✔ CVE-2026-34040         HIGH         8.8   9.3%   ·  ↳ O:GO-2026-4887 | S:GO-2026-4887 | V:OSV:GO-2026-4887
  │ ✔✔✔✔✔ CVE-2026-41567         HIGH         7.5   0.2%   ·  ↳ O:GHSA-x86f-5xw2-fm2r,GO-2026-5746 | S:GHSA-x86f-5xw2-fm2r,GO-2026-5746 | V:OSV:GO-2026-5746
  │ ✔✔✔✔✔ CVE-2026-42306         HIGH         7.2   0.1%   ·  ↳ O:GHSA-rg2x-37c3-w2rh,GO-2026-5617 | S:GHSA-rg2x-37c3-w2rh,GO-2026-5617 | V:OSV:GO-2026-5617
  │ ✔✔✔✔✔ CVE-2026-41568         MEDIUM       6.1   0.1%   ·  ↳ O:GHSA-vp62-88p7-qqf5,GO-2026-5668 | S:GHSA-vp62-88p7-qqf5,GO-2026-5668 | V:OSV:GO-2026-5668
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/go-openapi/swag/jsonutils@v0.26.1
  │ OSGTV
  │ ✘✘✘✘✔ CVE-2026-93450         HIGH         8.7   0.9%   ·  ↳ V:MEND:CVE-2026-93450
  │ ✘✘✘✘✔ WS-2026-0063           HIGH         8.7      -   ·  ↳ V:MEND:WS-2026-0063
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/go-openapi/swag/yamlutils@v0.26.1
  │ OSGTV
  │ ✘✘✘✘✔ CVE-2026-85280         HIGH         8.7      -   ·  ↳ V:MEND:CVE-2026-85280
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/klauspost/compress@v1.18.6
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-63209         HIGH         7.5   0.6%   ·  ↳ O:GHSA-259r-337f-4rfw,GO-2026-5841 | S:GHSA-259r-337f-4rfw,GO-2026-5841 | V:MEND:CVE-2026-63209
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/moby/buildkit@v0.31.1
  │ OSGTV
  │ ✘✘✘✘✔ CVE-2026-15788         HIGH         7.5   0.4%   ·  ↳ V:MEND:CVE-2026-15788
  │ ✘✘✘✘✔ CVE-2026-15789         HIGH         7.5   0.3%   ·  ↳ V:MEND:CVE-2026-15789
  │ ✘✘✘✘✔ CVE-2026-15791         HIGH         7.5   0.2%   ·  ↳ V:MEND:CVE-2026-15791
  │ ✘✘✘✘✔ CVE-2026-15792         HIGH         7.5   0.2%   ·  ↳ V:MEND:CVE-2026-15792
  │ ✘✘✘✘✔ CVE-2026-15793         HIGH         7.5   0.2%   ·  ↳ V:MEND:CVE-2026-15793
  │ ✘✘✘✘✔ CVE-2026-75593         HIGH         7.2   0.5%   ·  ↳ V:MEND:CVE-2026-75593
  │ ✘✘✘✘✔ CVE-2026-93318         HIGH         7.5   0.2%   ·  ↳ V:MEND:CVE-2026-93318
  │ ✘✘✘✘✔ CVE-2026-93315         MEDIUM       5.8   0.1%   ·  ↳ V:MEND:CVE-2026-93315
  │ ✘✘✘✘✔ CVE-2026-93320         MEDIUM       6.0   0.1%   ·  ↳ V:MEND:CVE-2026-93320
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/moby/buildkit@v0.32.0
  │ OSGTV
  │ ✘✘✘✘✔ CVE-2026-93318         HIGH         7.5   0.2%   ·  ↳ V:MEND:CVE-2026-93318
  │ ✘✘✘✘✔ CVE-2026-93315         MEDIUM       5.8   0.1%   ·  ↳ V:MEND:CVE-2026-93315
  │ ✘✘✘✘✔ CVE-2026-93320         MEDIUM       6.0   0.1%   ·  ↳ V:MEND:CVE-2026-93320
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/moby/go-archive@v0.2.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-17106         HIGH         7.1   0.4%   ·  ↳ O:GHSA-hfg8-hc9c-6c3h,GO-2026-6253 | S:GHSA-hfg8-hc9c-6c3h,GO-2026-6253 | V:MEND:CVE-2026-17106
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/moby/go-archive@v0.2.1
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-17106         HIGH         7.1   0.4%   ·  ↳ O:GHSA-hfg8-hc9c-6c3h,GO-2026-6253 | S:GHSA-hfg8-hc9c-6c3h,GO-2026-6253 | V:MEND:CVE-2026-17106
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/pelletier/go-toml/v2@v2.3.1
  │ OSGTV
  │ ✘✘✘✘✔ WS-2026-0062           HIGH         8.7      -   ·  ↳ V:MEND:WS-2026-0062
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace@v1.44.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-81870         LOW          2.0   0.3%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | S:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:SNYK:GOLANG-GOOPENTELEMETRYIOOTELEXPORTERSOTLPOTLPTRACE-19883902
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc@v1.44.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-81870         LOW          2.0   0.3%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | S:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:SNYK:GOLANG-GOOPENTELEMETRYIOOTELEXPORTERSOTLPOTLPTRACEOTLPTRACEGRPC-19883903
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp@v1.44.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-81870         LOW          2.0   0.3%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | S:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:SNYK:GOLANG-GOOPENTELEMETRYIOOTELEXPORTERSOTLPOTLPTRACEOTLPTRACEHTTP-19883904
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/sdk@v1.44.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-81870         LOW          2.0   0.3%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | S:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:MEND:CVE-2026-81870
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/crypto@v0.53.0
  │ OSGTV
  │ ✘✘✘✘✔ CVE-2026-46595         CRITICAL    10.0   0.6%   ·  ↳ V:OSV:GO-2026-6303
  │ ✔✔✔✔✔ CVE-2026-56854         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6303 | S:GO-2026-6303 | V:MEND:CVE-2026-56854
  │ ✔✔✔✔✔ CVE-2026-56855         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6355 | S:GO-2026-6355 | V:MEND:CVE-2026-56855
  │ ✔✔✔✔✔ CVE-2026-78662         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6354 | S:GO-2026-6354 | V:MEND:CVE-2026-78662
  │ ✔✔✔✔✔ GO-2026-5932           ?            0.0      -   ·  ↳ V:OSV:GO-2026-5932
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/crypto@v0.54.0
  │ OSGTV
  │ ✘✘✘✘✔ CVE-2026-46595         CRITICAL    10.0   0.6%   ·  ↳ V:OSV:GO-2026-6303
  │ ✔✔✔✔✔ CVE-2026-56854         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6303 | S:GO-2026-6303 | V:MEND:CVE-2026-56854
  │ ✔✔✔✔✔ CVE-2026-56855         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6355 | S:GO-2026-6355 | V:MEND:CVE-2026-56855
  │ ✔✔✔✔✔ CVE-2026-78662         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6354 | S:GO-2026-6354 | V:MEND:CVE-2026-78662
  │ ✔✔✔✔✔ GO-2026-5932           ?            0.0      -   ·  ↳ V:OSV:GO-2026-5932
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/mod@v0.38.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-56864         HIGH         7.5   0.3%   ·  ↳ O:GO-2026-6180 | S:GO-2026-6180 | V:MEND:CVE-2026-56864
  │ ✔✔✔✔✔ CVE-2026-56865         HIGH         8.4   0.1%   ·  ↳ O:GO-2026-6179 | S:GO-2026-6179 | V:MEND:CVE-2026-56865
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/net@v0.56.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-78663         CRITICAL     9.1   0.6%   ·  ↳ O:GO-2026-6612 | S:GO-2026-6612 | V:MEND:CVE-2026-78663
  │ ✔✔✔✔✔ CVE-2026-78659         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6603 | S:GO-2026-6603 | V:MEND:CVE-2026-78659
  │ ✔✔✔✔✔ CVE-2026-78660         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6610 | S:GO-2026-6610 | V:MEND:CVE-2026-78660
  │ ✔✔✔✔✔ CVE-2026-78669         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6611 | S:GO-2026-6611 | V:MEND:CVE-2026-78669
  │ ✔✔✔✔✔ CVE-2026-97032         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6617 | S:GO-2026-6617 | V:MEND:CVE-2026-97032
  │ ✔✔✔✔✔ CVE-2026-78661         ?            0.0   0.2%   ·  ↳ O:GO-2026-6860 | S:GO-2026-6860 | V:OSV:GO-2026-6860
  │ ✔✔✔✔✔ CVE-2026-97045         ?            0.0   0.2%   ·  ↳ O:GO-2026-6866 | S:GO-2026-6866 | V:OSV:GO-2026-6866
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/net@v0.57.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-78663         CRITICAL     9.1   0.6%   ·  ↳ O:GO-2026-6612 | S:GO-2026-6612 | V:MEND:CVE-2026-78663
  │ ✔✔✔✔✔ CVE-2026-78659         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6603 | S:GO-2026-6603 | V:MEND:CVE-2026-78659
  │ ✔✔✔✔✔ CVE-2026-78660         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6610 | S:GO-2026-6610 | V:MEND:CVE-2026-78660
  │ ✔✔✔✔✔ CVE-2026-78669         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6611 | S:GO-2026-6611 | V:MEND:CVE-2026-78669
  │ ✔✔✔✔✔ CVE-2026-97032         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6617 | S:GO-2026-6617 | V:MEND:CVE-2026-97032
  │ ✔✔✔✔✔ CVE-2026-78661         ?            0.0   0.2%   ·  ↳ O:GO-2026-6860 | S:GO-2026-6860 | V:OSV:GO-2026-6860
  │ ✔✔✔✔✔ CVE-2026-97045         ?            0.0   0.2%   ·  ↳ O:GO-2026-6866 | S:GO-2026-6866 | V:OSV:GO-2026-6866
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/text@v0.38.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-56851         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6629 | S:GO-2026-6629 | V:MEND:CVE-2026-56851
  │ ✔✔✔✔✔ CVE-2026-56852         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-5970 | S:GO-2026-5970 | V:MEND:CVE-2026-56852
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/text@v0.40.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-56851         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6629 | S:GO-2026-6629 | V:MEND:CVE-2026-56851
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/google.golang.org/grpc@v1.81.1
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-84304         HIGH         8.7   0.6%   ·  ↳ O:GHSA-vp52-pcj8-j9qc,GO-2026-6348 | S:GHSA-vp52-pcj8-j9qc,GO-2026-6348 | V:OSV:GO-2026-6348
  │ ✔✔✔✔✔ CVE-2026-84445         HIGH         8.7   0.6%   ·  ↳ O:GHSA-2v4p-qf9q-27wj,GO-2026-6443 | S:GHSA-2v4p-qf9q-27wj,GO-2026-6443 | V:MEND:CVE-2026-84445
  │ ✔✔✔✔✔ CVE-2026-84303         MEDIUM       6.3   0.3%   ·  ↳ O:GHSA-qc2q-p7wx-3px3,GO-2026-6441 | S:GHSA-qc2q-p7wx-3px3,GO-2026-6441 | V:OSV:GO-2026-6441
  │ ✘✘✘✘✔ WS-2026-0025           CRITICAL     9.1      -   ·  ↳ V:MEND:WS-2026-0025
  │ ✔✔✔✔✔ GHSA-HRXH-6V49-42GF    HIGH         8.8      -   ·  ↳ O:GO-2026-6061 | S:GO-2026-6061 | V:GO-2026-6061,OSV:GO-2026-6061
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/google.golang.org/grpc@v1.82.1
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-84304         HIGH         8.7   0.6%   ·  ↳ O:GHSA-vp52-pcj8-j9qc,GO-2026-6348 | S:GHSA-vp52-pcj8-j9qc,GO-2026-6348 | V:OSV:GO-2026-6348
  │ ✔✔✔✔✔ CVE-2026-84445         HIGH         8.7   0.6%   ·  ↳ O:GHSA-2v4p-qf9q-27wj,GO-2026-6443 | S:GHSA-2v4p-qf9q-27wj,GO-2026-6443 | V:MEND:CVE-2026-84445
  │ ✔✔✔✔✔ CVE-2026-84303         MEDIUM       6.3   0.3%   ·  ↳ O:GHSA-qc2q-p7wx-3px3,GO-2026-6441 | S:GHSA-qc2q-p7wx-3px3,GO-2026-6441 | V:OSV:GO-2026-6441
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/stdlib@1.26.4
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-39821         CRITICAL     9.6   1.8%   ·  ↳ O:GO-2026-5026 | S:GO-2026-5026 | V:OSV:GO-2026-5026
  │ ✔✔✔✔✔ CVE-2026-56857         CRITICAL     9.8   0.6%   ·  ↳ O:GO-2026-6604 | S:GO-2026-6604 | V:OSV:GO-2026-6604
  │ ✔✔✔✔✔ CVE-2026-78663         CRITICAL     9.1   0.6%   ·  ↳ O:GO-2026-6612 | S:GO-2026-6612 | V:OSV:GO-2026-6612
  │ ✔✔✔✔✔ CVE-2026-33818         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-5972 | S:GO-2026-5972 | V:OSV:GO-2026-5972
  │ ✔✔✔✔✔ CVE-2026-39822         HIGH         7.8   0.2%   ·  ↳ O:GO-2026-4970 | S:GO-2026-4970 | V:OSV:GO-2026-4970
  │ ✔✔✔✔✔ CVE-2026-46600         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-5942 | S:GO-2026-5942 | V:OSV:GO-2026-5942
  │ ✔✔✔✔✔ CVE-2026-56853         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6089 | S:GO-2026-6089 | V:OSV:GO-2026-6089
  │ ✔✔✔✔✔ CVE-2026-56859         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6088 | S:GO-2026-6088 | V:OSV:GO-2026-6088
  │ ✔✔✔✔✔ CVE-2026-56862         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6090 | S:GO-2026-6090 | V:OSV:GO-2026-6090
  │ ✔✔✔✔✔ CVE-2026-56866         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6605 | S:GO-2026-6605 | V:OSV:GO-2026-6605
  │ ✔✔✔✔✔ CVE-2026-78659         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6603 | S:GO-2026-6603 | V:OSV:GO-2026-6603
  │ ✔✔✔✔✔ CVE-2026-78660         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6610 | S:GO-2026-6610 | V:OSV:GO-2026-6610
  │ ✔✔✔✔✔ CVE-2026-78667         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6609 | S:GO-2026-6609 | V:OSV:GO-2026-6609
  │ ✔✔✔✔✔ CVE-2026-78669         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6611 | S:GO-2026-6611 | V:OSV:GO-2026-6611
  │ ✔✔✔✔✔ CVE-2026-94439         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6613 | S:GO-2026-6613 | V:OSV:GO-2026-6613
  │ ✔✔✔✔✔ CVE-2026-94440         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6608 | S:GO-2026-6608 | V:OSV:GO-2026-6608
  │ ✔✔✔✔✔ CVE-2026-97031         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6607 | S:GO-2026-6607 | V:OSV:GO-2026-6607
  │ ✔✔✔✔✔ CVE-2026-97032         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6617 | S:GO-2026-6617 | V:OSV:GO-2026-6617
  │ ✔✔✔✔✔ CVE-2026-111943        MEDIUM       6.8   0.4%   ·  ↳ O:GO-2026-6809 | S:GO-2026-6809 | V:OSV:GO-2026-6809
  │ ✔✔✔✔✔ CVE-2026-42505         MEDIUM       5.3   0.4%   ·  ↳ O:GO-2026-5856 | S:GO-2026-5856 | V:OSV:GO-2026-5856
  │ ✔✔✔✔✔ CVE-2026-56858         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-6091 | S:GO-2026-6091 | V:OSV:GO-2026-6091
  │ ✔✔✔✔✔ CVE-2026-56860         MEDIUM       5.9   0.5%   ·  ↳ O:GO-2026-6218 | S:GO-2026-6218 | V:OSV:GO-2026-6218
  │ ✔✔✔✔✔ CVE-2026-94448         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-6599 | S:GO-2026-6599 | V:OSV:GO-2026-6599
  │ ✔✔✔✔✔ CVE-2026-97030         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-6600 | S:GO-2026-6600 | V:OSV:GO-2026-6600
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/stdlib@1.26.5
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-39821         CRITICAL     9.6   1.8%   ·  ↳ O:GO-2026-5026 | S:GO-2026-5026 | V:OSV:GO-2026-5026
  │ ✔✔✔✔✔ CVE-2026-56857         CRITICAL     9.8   0.6%   ·  ↳ O:GO-2026-6604 | S:GO-2026-6604 | V:OSV:GO-2026-6604
  │ ✔✔✔✔✔ CVE-2026-78663         CRITICAL     9.1   0.6%   ·  ↳ O:GO-2026-6612 | S:GO-2026-6612 | V:OSV:GO-2026-6612
  │ ✔✔✔✔✔ CVE-2026-33818         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-5972 | S:GO-2026-5972 | V:OSV:GO-2026-5972
  │ ✔✔✔✔✔ CVE-2026-46600         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-5942 | S:GO-2026-5942 | V:OSV:GO-2026-5942
  │ ✔✔✔✔✔ CVE-2026-56853         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6089 | S:GO-2026-6089 | V:OSV:GO-2026-6089
  │ ✔✔✔✔✔ CVE-2026-56859         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6088 | S:GO-2026-6088 | V:OSV:GO-2026-6088
  │ ✔✔✔✔✔ CVE-2026-56862         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6090 | S:GO-2026-6090 | V:OSV:GO-2026-6090
  │ ✔✔✔✔✔ CVE-2026-56866         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6605 | S:GO-2026-6605 | V:OSV:GO-2026-6605
  │ ✔✔✔✔✔ CVE-2026-78659         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6603 | S:GO-2026-6603 | V:OSV:GO-2026-6603
  │ ✔✔✔✔✔ CVE-2026-78660         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6610 | S:GO-2026-6610 | V:OSV:GO-2026-6610
  │ ✔✔✔✔✔ CVE-2026-78667         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6609 | S:GO-2026-6609 | V:OSV:GO-2026-6609
  │ ✔✔✔✔✔ CVE-2026-78669         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6611 | S:GO-2026-6611 | V:OSV:GO-2026-6611
  │ ✔✔✔✔✔ CVE-2026-94439         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6613 | S:GO-2026-6613 | V:OSV:GO-2026-6613
  │ ✔✔✔✔✔ CVE-2026-94440         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6608 | S:GO-2026-6608 | V:OSV:GO-2026-6608
  │ ✔✔✔✔✔ CVE-2026-97031         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6607 | S:GO-2026-6607 | V:OSV:GO-2026-6607
  │ ✔✔✔✔✔ CVE-2026-97032         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6617 | S:GO-2026-6617 | V:OSV:GO-2026-6617
  │ ✔✔✔✔✔ CVE-2026-111943        MEDIUM       6.8   0.4%   ·  ↳ O:GO-2026-6809 | S:GO-2026-6809 | V:OSV:GO-2026-6809
  │ ✔✔✔✔✔ CVE-2026-56858         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-6091 | S:GO-2026-6091 | V:OSV:GO-2026-6091
  │ ✔✔✔✔✔ CVE-2026-56860         MEDIUM       5.9   0.5%   ·  ↳ O:GO-2026-6218 | S:GO-2026-6218 | V:OSV:GO-2026-6218
  │ ✔✔✔✔✔ CVE-2026-94448         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-6599 | S:GO-2026-6599 | V:OSV:GO-2026-6599
  │ ✔✔✔✔✔ CVE-2026-97030         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-6600 | S:GO-2026-6600 | V:OSV:GO-2026-6600
  └────────────────────────────────────────────────────────────────────────────────────────────────────
