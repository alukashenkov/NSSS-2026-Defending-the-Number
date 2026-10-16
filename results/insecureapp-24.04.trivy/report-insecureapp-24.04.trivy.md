# Vulnerability Comparison Report — insecureapp-24.04:latest

- **Image:** `insecureapp-24.04:latest`
- **Digest:** `sha256:f1856a1c91c32175c95e4f48586b100a389fd104e0c209d82a0f5a0c4d5fe9f3`
- **SBOM:** `insecureapp-24.04.trivy.cdx.json` — CycloneDX 1.7, trivy 0.76.0, built 2026-10-16T10:38:31+00:00
- **Report generated:** 2026-10-16T12:55:49
- **Scanners:** OSV (api.osv.dev) · Grype (grype 0.120.1) · Trivy (trivy 0.76.0) · Vulners (vulners.com audit API v4)

## Summary

  SBOM Components (Raw):           619
  Deduplicated PURLs:              534
  Clean (0 vulns):                 401
  Vulnerable:                      133

  Scanner              |   Pkgs Scanned |  Pkgs w/ Vulns | Total Vuln IDs
  ---------------------+----------------+----------------+---------------
  OSV                  |            534 |             46 |            274
  Grype                |            534 |             47 |            252
  Trivy                |            534 |            123 |           4381
  Vulners              |            534 |            102 |            311

  All 4 agree:       187     ≥2 agree:          342     Total:   4499    (CVE:4480 GHSA:5 Other:14)
  Exclusive to: OSV:21  Grype:0  Trivy:4105  Vulners:31

## VULNERABLE PACKAGES — [O]SV [G]rype [T]rivy [V]ulners findings

  ▸ Python (PyPI) (11 packages)
    ✔✔✔✔  pkg:pypi/aiohttp@3.9.1
    ✔✔✔✔  pkg:pypi/cryptography@3.3.2
    ✔✔✔✔  pkg:pypi/flask@3.0.2
    ✔✔✔✔  pkg:pypi/idna@2.7
    ✔✔✔✔  pkg:pypi/multidict@6.7.1
    ✔✔✔✔  pkg:pypi/pip@24.0
    ✔✔✔✔  pkg:pypi/requests@2.19.1
    ✔✔✔✔  pkg:pypi/setuptools@68.1.2
    ✔✔✔✔  pkg:pypi/urllib3@1.23
    ✔✔✔✔  pkg:pypi/werkzeug@3.1.8
    ✔✔✔✔  pkg:pypi/wheel@0.42.0

  ▸ Debian/Ubuntu (deb) (94 packages)
    ✔✔✔✔  pkg:deb/ubuntu/binutils@2.42-4ubuntu2.10
    ✘✘✔✔  pkg:deb/ubuntu/binutils-aarch64-linux-gnu@2.42-4ubuntu2.10
    ✘✘✔✔  pkg:deb/ubuntu/binutils-common@2.42-4ubuntu2.10
    ✘✘✔✘  pkg:deb/ubuntu/bsdutils@1%3A2.39.3-9ubuntu6.5
    ✔✔✔✔  pkg:deb/ubuntu/bzip2@1.0.8-5.1build0.1
    ✔✔✔✔  pkg:deb/ubuntu/coreutils@9.4-3ubuntu6.2
    ✔✔✔✔  pkg:deb/ubuntu/curl@8.5.0-2ubuntu10.11
    ✔✔✔✔  pkg:deb/ubuntu/dash@0.5.12-6ubuntu5
    ✘✔✔✔  pkg:deb/ubuntu/diffutils@1%3A3.10-1build1
    ✘✘✔✘  pkg:deb/ubuntu/dirmngr@2.4.4-2ubuntu17.4
    ✔✔✘✘  pkg:deb/ubuntu/gcc-13@13.3.0-6ubuntu2~24.04.1
    ✘✘✔✘  pkg:deb/ubuntu/gnupg@2.4.4-2ubuntu17.4
    ✘✘✔✘  pkg:deb/ubuntu/gnupg-l10n@2.4.4-2ubuntu17.4
    ✘✘✔✘  pkg:deb/ubuntu/gnupg-utils@2.4.4-2ubuntu17.4
    ✘✘✔✘  pkg:deb/ubuntu/gpg@2.4.4-2ubuntu17.4
    ✘✘✔✘  pkg:deb/ubuntu/gpg-agent@2.4.4-2ubuntu17.4
    ✘✘✔✘  pkg:deb/ubuntu/gpg-wks-client@2.4.4-2ubuntu17.4
    ✘✘✔✘  pkg:deb/ubuntu/gpgconf@2.4.4-2ubuntu17.4
    ✘✘✔✔  pkg:deb/ubuntu/gpgsm@2.4.4-2ubuntu17.4
    ✘✘✔✘  pkg:deb/ubuntu/gpgv@2.4.4-2ubuntu17.4
    ✔✔✔✔  pkg:deb/ubuntu/gzip@1.12-1ubuntu3.1
    ✘✘✔✘  pkg:deb/ubuntu/keyboxd@2.4.4-2ubuntu17.4
    ✘✘✔✔  pkg:deb/ubuntu/libaom3@3.8.2-2ubuntu0.1
    ✘✘✔✔  pkg:deb/ubuntu/libattr1@1%3A2.5.2-1build1.1
    ✘✘✔✔  pkg:deb/ubuntu/libbinutils@2.42-4ubuntu2.10
    ✘✘✔✘  pkg:deb/ubuntu/libblkid1@2.39.3-9ubuntu6.5
    ✘✘✔✘  pkg:deb/ubuntu/libbz2-1.0@1.0.8-5.1build0.1
    ✘✘✔✔  pkg:deb/ubuntu/libc-bin@2.39-0ubuntu8.8
    ✘✘✔✔  pkg:deb/ubuntu/libc-dev-bin@2.39-0ubuntu8.8
    ✘✘✔✔  pkg:deb/ubuntu/libc-devtools@2.39-0ubuntu8.8
    ✘✘✔✔  pkg:deb/ubuntu/libc6@2.39-0ubuntu8.8
    ✘✘✔✔  pkg:deb/ubuntu/libc6-dev@2.39-0ubuntu8.8
    ✘✘✔✔  pkg:deb/ubuntu/libctf-nobfd0@2.42-4ubuntu2.10
    ✘✘✔✔  pkg:deb/ubuntu/libctf0@2.42-4ubuntu2.10
    ✘✘✔✔  pkg:deb/ubuntu/libcurl4t64@8.5.0-2ubuntu10.11
    ✘✘✔✔  pkg:deb/ubuntu/libexpat1@2.6.1-2ubuntu0.4
    ✘✘✔✔  pkg:deb/ubuntu/libexpat1-dev@2.6.1-2ubuntu0.4
    ✘✘✔✔  pkg:deb/ubuntu/libfreetype6@2.13.2%2Bdfsg-1ubuntu0.1
    ✔✔✔✔  pkg:deb/ubuntu/libgcrypt20@1.10.3-2ubuntu0.1
    ✘✘✔✔  pkg:deb/ubuntu/libgnutls30t64@3.8.3-1.1ubuntu3.6
    ✘✘✔✔  pkg:deb/ubuntu/libgprofng0@2.42-4ubuntu2.10
    ✘✘✔✔  pkg:deb/ubuntu/libheif-plugin-aomdec@1.17.6-1ubuntu4.6
    ✘✘✔✔  pkg:deb/ubuntu/libheif-plugin-aomenc@1.17.6-1ubuntu4.6
    ✘✘✔✔  pkg:deb/ubuntu/libheif1@1.17.6-1ubuntu4.6
    ✘✘✘✔  pkg:deb/ubuntu/libhwasan0@14.2.0-4ubuntu2~24.04.1
    ✘✘✔✘  pkg:deb/ubuntu/libmount1@2.39.3-9ubuntu6.5
    ✘✘✔✔  pkg:deb/ubuntu/libncursesw6@6.4%2B20240113-1ubuntu2
    ✘✘✔✔  pkg:deb/ubuntu/libp11-kit0@0.25.3-4ubuntu2.1
    ✘✘✔✔  pkg:deb/ubuntu/libpam-modules@1.5.3-5ubuntu5.5
    ✘✘✔✘  pkg:deb/ubuntu/libpam-modules-bin@1.5.3-5ubuntu5.5
    ✘✘✔✘  pkg:deb/ubuntu/libpam-runtime@1.5.3-5ubuntu5.5
    ✘✘✔✘  pkg:deb/ubuntu/libpam0g@1.5.3-5ubuntu5.5
    ✘✘✔✔  pkg:deb/ubuntu/libpcre2-8-0@10.42-4ubuntu2.1
    ✘✘✔✔  pkg:deb/ubuntu/libperl5.38t64@5.38.2-3.2ubuntu0.3
    ✘✘✔✔  pkg:deb/ubuntu/libpng16-16t64@1.6.43-5ubuntu0.6
    ✘✘✔✘  pkg:deb/ubuntu/libpython3.12-dev@3.12.3-1ubuntu0.15
    ✘✘✔✘  pkg:deb/ubuntu/libpython3.12-minimal@3.12.3-1ubuntu0.15
    ✘✘✔✘  pkg:deb/ubuntu/libpython3.12-stdlib@3.12.3-1ubuntu0.15
    ✘✘✔✔  pkg:deb/ubuntu/libpython3.12t64@3.12.3-1ubuntu0.15
    ✘✘✔✘  pkg:deb/ubuntu/libsasl2-2@2.1.28%2Bdfsg1-5ubuntu3.1
    ✘✘✔✘  pkg:deb/ubuntu/libsasl2-modules@2.1.28%2Bdfsg1-5ubuntu3.1
    ✘✘✔✘  pkg:deb/ubuntu/libsasl2-modules-db@2.1.28%2Bdfsg1-5ubuntu3.1
    ✘✘✔✔  pkg:deb/ubuntu/libsframe1@2.42-4ubuntu2.10
    ✘✘✔✘  pkg:deb/ubuntu/libsmartcols1@2.39.3-9ubuntu6.5
    ✘✘✔✔  pkg:deb/ubuntu/libsqlite3-0@3.45.1-1ubuntu2.7
    ✘✘✔✔  pkg:deb/ubuntu/libssh-4@0.10.6-2ubuntu0.4
    ✘✘✔✔  pkg:deb/ubuntu/libssl3t64@3.0.13-0ubuntu3.12
    ✘✘✔✔  pkg:deb/ubuntu/libsystemd0@255.4-1ubuntu8.16
    ✘✘✔✔  pkg:deb/ubuntu/libtinfo6@6.4%2B20240113-1ubuntu2
    ✘✘✔✔  pkg:deb/ubuntu/libudev1@255.4-1ubuntu8.16
    ✘✘✔✘  pkg:deb/ubuntu/libuuid1@2.39.3-9ubuntu6.5
    ✘✘✔✔  pkg:deb/ubuntu/libx11-6@2%3A1.8.7-1build1
    ✘✘✔✘  pkg:deb/ubuntu/libx11-data@2%3A1.8.7-1build1
    ✘✘✔✔  pkg:deb/ubuntu/libxpm4@1%3A3.5.17-1ubuntu0.24.04.1
    ✘✘✔✘  pkg:deb/ubuntu/linux-libc-dev@6.8.0-136.136
    ✘✘✔✔  pkg:deb/ubuntu/login@1%3A4.13%2Bdfsg1-4ubuntu3.2
    ✘✘✔✘  pkg:deb/ubuntu/mount@2.39.3-9ubuntu6.5
    ✘✘✔✔  pkg:deb/ubuntu/ncurses-base@6.4%2B20240113-1ubuntu2
    ✘✘✔✔  pkg:deb/ubuntu/ncurses-bin@6.4%2B20240113-1ubuntu2
    ✔✔✔✔  pkg:deb/ubuntu/openssl@3.0.13-0ubuntu3.12
    ✘✘✔✔  pkg:deb/ubuntu/passwd@1%3A4.13%2Bdfsg1-4ubuntu3.2
    ✔✔✔✔  pkg:deb/ubuntu/patch@2.7.6-7build3
    ✔✔✔✔  pkg:deb/ubuntu/perl@5.38.2-3.2ubuntu0.3
    ✘✘✔✔  pkg:deb/ubuntu/perl-base@5.38.2-3.2ubuntu0.3
    ✘✘✔✔  pkg:deb/ubuntu/perl-modules-5.38@5.38.2-3.2ubuntu0.3
    ✘✘✔✔  pkg:deb/ubuntu/python3-pip@24.0%2Bdfsg-1ubuntu1.3
    ✘✘✔✔  pkg:deb/ubuntu/python3-wheel@0.42.0-2
    ✔✔✔✔  pkg:deb/ubuntu/python3.12@3.12.3-1ubuntu0.15
    ✘✘✔✘  pkg:deb/ubuntu/python3.12-dev@3.12.3-1ubuntu0.15
    ✘✘✔✘  pkg:deb/ubuntu/python3.12-minimal@3.12.3-1ubuntu0.15
    ✔✔✔✔  pkg:deb/ubuntu/tar@1.35%2Bdfsg-3build1
    ✔✔✔✔  pkg:deb/ubuntu/util-linux@2.39.3-9ubuntu6.5
    ✘✘✔✔  pkg:deb/ubuntu/zlib1g@1%3A1.3.dfsg-3.1ubuntu2.1
    ✘✘✔✔  pkg:deb/ubuntu/zlib1g-dev@1%3A1.3.dfsg-3.1ubuntu2.1

  ▸ Go (28 packages)
    ✔✔✔✔  pkg:golang/github.com/containerd/containerd/v2@v2.2.5
    ✔✔✔✔  pkg:golang/github.com/containerd/containerd/v2@v2.3.3
    ✘✘✘✔  pkg:golang/github.com/docker/buildx@v0.35.0
    ✘✘✘✔  pkg:golang/github.com/docker/buildx@v0.36.0
    ✔✔✔✔  pkg:golang/github.com/docker/docker@v28.5.2%2Bincompatible
    ✘✘✘✔  pkg:golang/github.com/go-openapi/swag/jsonutils@v0.26.1
    ✘✘✘✔  pkg:golang/github.com/go-openapi/swag/yamlutils@v0.26.1
    ✔✔✘✔  pkg:golang/github.com/klauspost/compress@v1.18.6
    ✘✘✘✔  pkg:golang/github.com/moby/buildkit@v0.31.1
    ✘✘✘✔  pkg:golang/github.com/moby/buildkit@v0.32.0
    ✔✔✔✔  pkg:golang/github.com/moby/go-archive@v0.2.0
    ✔✔✔✔  pkg:golang/github.com/moby/go-archive@v0.2.1
    ✘✘✘✔  pkg:golang/github.com/pelletier/go-toml/v2@v2.3.1
    ✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace@v1.44.0
    ✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc@v1.44.0
    ✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp@v1.44.0
    ✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/sdk@v1.44.0
    ✔✔✔✔  pkg:golang/golang.org/x/crypto@v0.53.0
    ✔✔✔✔  pkg:golang/golang.org/x/crypto@v0.54.0
    ✔✔✔✔  pkg:golang/golang.org/x/mod@v0.38.0
    ✔✔✔✔  pkg:golang/golang.org/x/net@v0.56.0
    ✔✔✔✔  pkg:golang/golang.org/x/net@v0.57.0
    ✔✔✔✔  pkg:golang/golang.org/x/text@v0.38.0
    ✔✔✔✔  pkg:golang/golang.org/x/text@v0.40.0
    ✔✔✔✔  pkg:golang/google.golang.org/grpc@v1.81.1
    ✔✔✔✔  pkg:golang/google.golang.org/grpc@v1.82.1
    ✔✔✔✔  pkg:golang/stdlib@v1.26.4
    ✔✔✔✔  pkg:golang/stdlib@v1.26.5

## VULNERABILITY DETAIL — All Scanner Findings

  Every vulnerability found, and which scanners agree on it.
  CVSS, EPSS and KEV come from Vulners where it knows the CVE, otherwise from the scanner that reported it.
  OSV Grype Trivy Vulners   SEVERITY   CVSS   EPSS  KEV   ↳ provenance
  ━━ Python (PyPI) ━━
  ┌─ pkg:pypi/aiohttp@3.9.1
  │ OGTV
  │ ✔✔✔✔ CVE-2026-34520         CRITICAL     9.1   0.7%   ·  ↳ O:GHSA-63hf-3vf5-4wqf,PYSEC-2026-2102 | V:SNYK:PYTHON-AIOHTTP-15873704
  │ ✔✔✔✔ CVE-2024-23334         HIGH         7.5  76.9% KEV  ↳ O:GHSA-5h86-8mv2-jq9f,PYSEC-2024-24 | V:GHSA-5H86-8MV2-JQ9F
  │ ✔✔✔✔ CVE-2024-30251         HIGH         7.5   1.1%   ·  ↳ O:GHSA-5m98-qgg9-wh84,PYSEC-2026-1098 | V:GHSA-5M98-QGG9-WH84
  │ ✔✔✔✔ CVE-2024-52304         HIGH         7.5   0.6%   ·  ↳ O:GHSA-8495-4g3g-x7pr,PYSEC-2026-1103 | V:SNYK:PYTHON-AIOHTTP-8383923
  │ ✔✔✔✔ CVE-2025-53643         HIGH         7.5   0.4%   ·  ↳ O:GHSA-9548-qrrj-x5pj,PYSEC-2026-1104 | V:GHSA-9548-QRRJ-X5PJ
  │ ✔✔✔✔ CVE-2025-69223         HIGH         7.5   0.6%   ·  ↳ O:GHSA-6mq8-rvhq-8wgg,PYSEC-2026-1101 | V:SNYK:PYTHON-AIOHTTP-14871876
  │ ✔✔✔✔ CVE-2025-69227         HIGH         8.7   0.4%   ·  ↳ O:GHSA-jj3x-wxrx-4x23,PYSEC-2026-1107 | V:SNYK:PYTHON-AIOHTTP-14871979
  │ ✔✔✔✔ CVE-2025-69228         HIGH         8.7   0.4%   ·  ↳ O:GHSA-6jhg-hg63-jvvf,PYSEC-2026-1100 | V:SNYK:PYTHON-AIOHTTP-14871877
  │ ✔✔✔✔ CVE-2025-69229         HIGH         8.7   0.4%   ·  ↳ O:GHSA-g84x-mcqj-x9qq,PYSEC-2026-1106 | V:SNYK:PYTHON-AIOHTTP-14871954
  │ ✔✔✔✔ CVE-2026-22815         HIGH         7.5   0.4%   ·  ↳ O:GHSA-w2fm-2cpv-w7v5,PYSEC-2026-2094 | V:SNYK:PYTHON-AIOHTTP-15873739
  │ ✔✔✔✔ CVE-2026-34513         HIGH         7.5   0.6%   ·  ↳ O:GHSA-hcc4-c3v8-rx92,PYSEC-2026-2095 | V:SNYK:PYTHON-AIOHTTP-15873737
  │ ✔✔✔✔ CVE-2026-34515         HIGH         8.7   0.5%   ·  ↳ O:GHSA-p998-jp59-783m,PYSEC-2026-2097 | V:SNYK:PYTHON-AIOHTTP-15873738
  │ ✔✔✔✔ CVE-2026-34516         HIGH         8.7   0.6%   ·  ↳ O:GHSA-m5qp-6w8w-w647,PYSEC-2026-2098 | V:SNYK:PYTHON-AIOHTTP-15873732
  │ ✔✔✔✔ CVE-2026-34993         HIGH         7.3   0.5%   ·  ↳ O:GHSA-jg22-mg44-37j8,PYSEC-2026-2104 | V:GHSA-JG22-MG44-37J8
  │ ✔✔✔✔ CVE-2026-47265         HIGH         8.7   0.2%   ·  ↳ O:GHSA-hg6j-4rv6-33pg,PYSEC-2026-2105 | V:GHSA-HG6J-4RV6-33PG
  │ ✔✔✔✔ CVE-2026-50269         HIGH         7.5   0.5%   ·  ↳ O:GHSA-m6qw-4cw2-hm4m,PYSEC-2026-2106 | V:SNYK:PYTHON-AIOHTTP-17342380
  │ ✔✔✔✔ CVE-2026-54273         HIGH         8.7   0.5%   ·  ↳ O:GHSA-4fvr-rgm6-gqmc,PYSEC-2026-2107 | V:SNYK:PYTHON-AIOHTTP-17342416
  │ ✔✔✔✔ CVE-2026-54274         HIGH         8.7   0.5%   ·  ↳ O:GHSA-xcgm-r5h9-7989,PYSEC-2026-2108 | V:SNYK:PYTHON-AIOHTTP-17342364
  │ ✔✔✔✔ CVE-2026-54275         HIGH         7.5   0.5%   ·  ↳ O:GHSA-4m7w-qmgq-4wj5,PYSEC-2026-237 | V:SNYK:PYTHON-AIOHTTP-17342400
  │ ✔✔✔✔ CVE-2026-54277         HIGH         8.7   0.6%   ·  ↳ O:GHSA-63hw-fmq6-xxg2,PYSEC-2026-2110 | V:SNYK:PYTHON-AIOHTTP-17342401
  │ ✔✔✔✔ CVE-2026-54278         HIGH         8.7   0.5%   ·  ↳ O:GHSA-g3cq-j2xw-wf74,PYSEC-2026-2111 | V:SNYK:PYTHON-AIOHTTP-17342413
  │ ✔✔✔✔ CVE-2026-54279         HIGH         7.5   0.5%   ·  ↳ O:GHSA-2fqr-mr3j-6wp8,PYSEC-2026-2112 | V:SNYK:PYTHON-AIOHTTP-17342393
  │ ✔✔✔✔ CVE-2026-54280         HIGH         7.5   0.5%   ·  ↳ O:GHSA-9x8q-7h8h-wcw9,PYSEC-2026-2113 | V:SNYK:PYTHON-AIOHTTP-17342415
  │ ✔✔✔✔ CVE-2026-69244         HIGH         7.1   0.5%   ·  ↳ O:GHSA-cq5v-8q36-5273,PYSEC-2026-3545 | V:SNYK:PYTHON-AIOHTTP-18517003
  │ ✔✔✔✔ CVE-2024-23829         MEDIUM       6.5   1.0%   ·  ↳ O:GHSA-8qpw-xqxj-h4r2,PYSEC-2024-26 | V:GHSA-8QPW-XQXJ-H4R2
  │ ✔✔✔✔ CVE-2024-27306         MEDIUM       6.1   0.7%   ·  ↳ O:GHSA-7gpw-8wmc-pm8g,PYSEC-2026-1102 | V:GHSA-7GPW-8WMC-PM8G
  │ ✔✔✔✔ CVE-2025-69224         MEDIUM       6.5   0.2%   ·  ↳ O:GHSA-69f9-5gxw-wvc2,PYSEC-2026-1099 | V:SNYK:PYTHON-AIOHTTP-14871873
  │ ✔✔✔✔ CVE-2025-69225         MEDIUM       6.9   0.3%   ·  ↳ O:GHSA-mqqc-3gqh-h2x8,PYSEC-2026-1109 | V:SNYK:PYTHON-AIOHTTP-14871929
  │ ✔✔✔✔ CVE-2025-69226         MEDIUM       6.3   0.4%   ·  ↳ O:GHSA-54jq-c3m8-4m76,PYSEC-2026-1097 | V:SNYK:PYTHON-AIOHTTP-14871888
  │ ✔✔✔✔ CVE-2025-69230         MEDIUM       6.9   0.4%   ·  ↳ O:GHSA-fh55-r93g-j68g,PYSEC-2026-1105 | V:SNYK:PYTHON-AIOHTTP-14872000
  │ ✔✔✔✔ CVE-2026-34514         MEDIUM       6.9   0.4%   ·  ↳ O:GHSA-2vrm-gr82-f7m5,PYSEC-2026-2096 | V:SNYK:PYTHON-AIOHTTP-15873736
  │ ✔✔✔✔ CVE-2026-34517         MEDIUM       6.9   0.5%   ·  ↳ O:GHSA-3wq7-rqq7-wx6j,PYSEC-2026-2099 | V:SNYK:PYTHON-AIOHTTP-15873734
  │ ✔✔✔✔ CVE-2026-34518         MEDIUM       6.9   0.4%   ·  ↳ O:GHSA-966j-vmvw-g2g9,PYSEC-2026-2100 | V:SNYK:PYTHON-AIOHTTP-15873735
  │ ✔✔✔✔ CVE-2026-34519         MEDIUM       6.9   0.4%   ·  ↳ O:GHSA-mwh4-6h8g-pg8w,PYSEC-2026-2101 | V:SNYK:PYTHON-AIOHTTP-15873731
  │ ✔✔✔✔ CVE-2026-34525         MEDIUM       6.3   0.4%   ·  ↳ O:GHSA-c427-h43c-vf67,PYSEC-2026-2103 | V:SNYK:PYTHON-AIOHTTP-15873733
  │ ✔✔✔✔ CVE-2026-54276         MEDIUM       6.3   0.3%   ·  ↳ O:GHSA-hpj7-wq8m-9hgp,PYSEC-2026-2109 | V:SNYK:PYTHON-AIOHTTP-17342365
  │ ✔✔✔✔ CVE-2026-59881         MEDIUM       6.9   0.5%   ·  ↳ O:GHSA-mq44-7p77-q5h7,PYSEC-2026-3547 | V:SNYK:PYTHON-AIOHTTP-18517004
  │ ✔✔✔✔ CVE-2026-69243         MEDIUM       6.3   0.4%   ·  ↳ O:GHSA-mfx4-hv73-q22v,PYSEC-2026-3546 | V:SNYK:PYTHON-AIOHTTP-18517005
  │ ✘✘✘✔ WS-2026-0114           MEDIUM       6.3      -   ·  ↳ V:MEND:WS-2026-0114
  │ ✘✘✘✔ WS-2026-0116           MEDIUM       6.3      -   ·  ↳ V:MEND:WS-2026-0116
  │ ✘✘✘✔ WS-2026-0119           MEDIUM       6.3      -   ·  ↳ V:MEND:WS-2026-0119
  │ ✘✘✘✔ WS-2026-0120           MEDIUM       6.9      -   ·  ↳ V:MEND:WS-2026-0120
  │ ✘✘✘✔ WS-2026-0121           MEDIUM       6.9      -   ·  ↳ V:MEND:WS-2026-0121
  │ ✘✘✘✔ WS-2026-0115           LOW          3.1      -   ·  ↳ V:MEND:WS-2026-0115
  │ ✘✘✘✔ WS-2026-0117           LOW          3.1      -   ·  ↳ V:MEND:WS-2026-0117
  │ ✘✘✘✔ WS-2026-0118           LOW          3.1      -   ·  ↳ V:MEND:WS-2026-0118
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/cryptography@3.3.2
  │ OGTV
  │ ✔✔✔✔ CVE-2023-0286          HIGH         7.4  71.2%   ·  ↳ O:GHSA-x4qr-2fvf-3mr5,PYSEC-2026-800 | V:GHSA-X4QR-2FVF-3MR5
  │ ✔✔✔✔ CVE-2023-49083         HIGH         7.5   1.0%   ·  ↳ O:GHSA-jfhm-5ghh-2f97,PYSEC-2023-254 | V:GHSA-JFHM-5GHH-2F97
  │ ✔✔✔✔ CVE-2023-50782         HIGH         7.5   1.1%   ·  ↳ O:GHSA-3ww4-gg4f-jr7f,PYSEC-2026-1283 | V:MEND:CVE-2023-50782
  │ ✔✔✔✔ CVE-2026-26007         HIGH         8.2   0.4%   ·  ↳ O:GHSA-r6ph-v2qm-q3c2,PYSEC-2026-2141 | V:MEND:CVE-2026-26007
  │ ✘✘✘✔ CVE-2026-34180         HIGH         7.5   1.0%   ·  ↳ V:SNYK:PYTHON-CRYPTOGRAPHY-17344551
  │ ✔✘✘✔ CVE-2026-69248         HIGH         8.3   0.3%   ·  ↳ O:PYSEC-2026-3554 | V:OSV:PYSEC-2026-3554
  │ ✔✘✘✔ CVE-2026-69249         HIGH         8.7   0.3%   ·  ↳ O:PYSEC-2026-3553 | V:OSV:PYSEC-2026-3553
  │ ✔✔✔✔ CVE-2023-23931         MEDIUM       6.5   1.3%   ·  ↳ O:GHSA-w7pp-m8wf-vj6r,PYSEC-2023-11 | V:GHSA-W7PP-M8WF-VJ6R
  │ ✔✔✔✔ CVE-2024-0727          MEDIUM       5.5   3.2%   ·  ↳ O:GHSA-9v9h-cgj8-h64p,PYSEC-2026-1285 | V:MEND:CVE-2024-0727
  │ ✔✔✔✔ CVE-2026-34073         MEDIUM       6.3   0.2%   ·  ↳ O:GHSA-m959-cc7f-wv43,PYSEC-2026-35 | V:MEND:CVE-2026-34073
  │ ✔✔✔✔ GHSA-537C-GMF6-5CCF    HIGH         7.5      -   ·
  │ ✔✔✔✔ GHSA-5CPQ-8WJ7-HF2V    LOW          0.0      -   ·  ↳ V:OSV:GHSA-5CPQ-8WJ7-HF2V
  │ ✔✔✔✔ GHSA-JM77-QPHF-C4W8    LOW          0.0      -   ·
  │ ✔✔✔✔ GHSA-V8GR-M533-GHJ9    LOW          0.0      -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/flask@3.0.2
  │ OGTV
  │ ✔✔✔✔ CVE-2026-27205         MEDIUM       4.3   0.4%   ·  ↳ O:GHSA-68rp-wp8r-4726,PYSEC-2026-2151 | V:GHSA-68RP-WP8R-4726
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/idna@2.7
  │ OGTV
  │ ✔✔✔✔ CVE-2024-3651          HIGH         7.5   1.4%   ·  ↳ O:GHSA-jjg7-2v4v-x38h,PYSEC-2024-60 | V:MEND:CVE-2024-3651
  │ ✔✔✔✔ CVE-2026-45409         MEDIUM       6.9   0.5%   ·  ↳ O:GHSA-65pc-fj4g-8rjx,PYSEC-2026-215 | V:MEND:CVE-2026-45409
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/multidict@6.7.1
  │ OGTV
  │ ✔✔✔✔ CVE-2026-104874        MEDIUM       5.3   0.3%   ·  ↳ O:GHSA-54p9-h82j-f925,PYSEC-2026-4244 | V:OSV:PYSEC-2026-4244
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/pip@24.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-8643          HIGH         8.0   0.5%   ·  ↳ O:GHSA-wf93-45jw-7689,PYSEC-2026-196 | V:MEND:CVE-2026-8643
  │ ✔✔✔✔ CVE-2025-8869          MEDIUM       5.9   0.5%   ·  ↳ O:GHSA-4xh5-x5gv-qwph,PYSEC-2026-1795 | V:MEND:CVE-2025-8869
  │ ✔✔✔✔ CVE-2026-13346         MEDIUM       6.5   0.3%   ·  ↳ O:GHSA-qwm4-qh6w-59xr,PYSEC-2026-3721 | V:MEND:CVE-2026-13346
  │ ✔✔✔✔ CVE-2026-3219          MEDIUM       4.6   0.2%   ·  ↳ O:GHSA-58qw-9mgm-455v,PYSEC-2026-2875 | V:MEND:CVE-2026-3219
  │ ✔✔✔✔ CVE-2026-6357          MEDIUM       5.3   0.2%   ·  ↳ O:GHSA-jp4c-xjxw-mgf9,PYSEC-2026-2876 | V:SNYK:PYTHON-PIP-16316401
  │ ✔✔✔✔ CVE-2026-1703          LOW          2.0   0.4%   ·  ↳ O:GHSA-6vgw-5pg2-w6jp,PYSEC-2026-1796 | V:MEND:CVE-2026-1703
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/requests@2.19.1
  │ OGTV
  │ ✔✔✔✔ CVE-2018-18074         HIGH         7.5   7.4%   ·  ↳ O:GHSA-x84v-xcm2-53pg,PYSEC-2018-28 | V:OSV:PYSEC-2018-28
  │ ✔✔✔✔ CVE-2023-32681         MEDIUM       6.1   3.0%   ·  ↳ O:GHSA-j8r2-6x86-q33q,PYSEC-2023-74 | V:GHSA-J8R2-6X86-Q33Q
  │ ✔✔✔✔ CVE-2024-35195         MEDIUM       5.6   0.3%   ·  ↳ O:GHSA-9wx4-h78v-vm56,PYSEC-2026-1873 | V:GHSA-9WX4-H78V-VM56
  │ ✔✔✔✔ CVE-2024-47081         MEDIUM       5.3   1.0%   ·  ↳ O:GHSA-9hjg-9r4m-mvj7,PYSEC-2026-1872 | V:MEND:CVE-2024-47081
  │ ✔✔✔✔ CVE-2026-25645         MEDIUM       5.5   0.2%   ·  ↳ O:GHSA-gc5v-m9x4-r6x2,PYSEC-2026-2275 | V:GHSA-GC5V-M9X4-R6X2
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/setuptools@68.1.2
  │ OGTV
  │ ✔✔✔✔ CVE-2024-6345          HIGH         8.8   1.9%   ·  ↳ O:GHSA-cx63-2mw6-8hw5,PYSEC-2026-1918 | V:MEND:CVE-2024-6345
  │ ✔✔✔✔ CVE-2025-47273         HIGH         8.8   1.6%   ·  ↳ O:GHSA-5rjg-fvgr-3xxf,PYSEC-2025-49 | V:MEND:CVE-2025-47273
  │ ✔✔✔✔ CVE-2026-59890         MEDIUM       6.1   0.4%   ·  ↳ O:GHSA-h35f-9h28-mq5c,PYSEC-2026-3447 | V:MEND:CVE-2026-59890
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/urllib3@1.23
  │ OGTV
  │ ✔✔✔✔ CVE-2019-11324         HIGH         7.5   2.9%   ·  ↳ O:GHSA-mh33-7rrq-662w,PYSEC-2019-133 | V:GHSA-MH33-7RRQ-662W
  │ ✔✔✔✔ CVE-2023-43804         HIGH         8.1   1.4%   ·  ↳ O:GHSA-v845-jxx5-vc9f,PYSEC-2023-192 | V:GHSA-V845-JXX5-VC9F
  │ ✔✔✔✔ CVE-2025-66471         HIGH         8.9   0.7%   ·  ↳ O:GHSA-2xpw-w6gg-jr37,PYSEC-2026-1994 | V:MEND:CVE-2025-66471
  │ ✔✔✔✔ CVE-2026-21441         HIGH         8.9   2.9%   ·  ↳ O:GHSA-38jv-5279-wg99,PYSEC-2026-1996 | V:MEND:CVE-2026-21441
  │ ✔✔✔✔ CVE-2026-44431         HIGH         8.2   0.3%   ·  ↳ O:GHSA-qccp-gfcp-xxvc,PYSEC-2026-141 | V:MEND:CVE-2026-44431
  │ ✔✔✔✔ CVE-2026-97689         HIGH         8.9   0.3%   ·  ↳ O:GHSA-vxq7-64xx-v4gw,PYSEC-2026-4177 | V:MEND:CVE-2026-97689
  │ ✔✔✔✔ CVE-2018-25091         MEDIUM       6.1   0.5%   ·  ↳ O:GHSA-gwvm-45gx-3cf8,PYSEC-2023-207 | V:GHSA-GWVM-45GX-3CF8
  │ ✔✔✔✔ CVE-2019-11236         MEDIUM       6.1   2.1%   ·  ↳ O:GHSA-r64q-w8jr-g9qp,PYSEC-2019-132 | V:OSV:PYSEC-2019-132
  │ ✔✔✔✔ CVE-2020-26137         MEDIUM       6.5   2.3%   ·  ↳ O:GHSA-wqvq-5m8c-6g24,PYSEC-2020-148 | V:GHSA-WQVQ-5M8C-6G24
  │ ✔✔✔✔ CVE-2023-45803         MEDIUM       4.2   0.5%   ·  ↳ O:GHSA-g4mx-q9vg-27p4,PYSEC-2023-212 | V:OSV:PYSEC-2023-212
  │ ✔✔✔✔ CVE-2024-37891         MEDIUM       6.5   1.1%   ·  ↳ O:GHSA-34jh-p97f-mpxf,PYSEC-2026-1995 | V:GHSA-34JH-P97F-MPXF
  │ ✔✔✔✔ CVE-2025-50181         MEDIUM       6.1   0.5%   ·  ↳ O:GHSA-pq67-6m6q-mj2v,PYSEC-2026-1999 | V:MEND:CVE-2025-50181
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/werkzeug@3.1.8
  │ OGTV
  │ ✔✔✔✔ CVE-2026-102598        MEDIUM       6.3   0.4%   ·  ↳ O:GHSA-g6x2-hccm-hh4m,PYSEC-2026-4312 | V:OSV:PYSEC-2026-4312
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/wheel@0.42.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-24049         HIGH         7.1   0.4%   ·  ↳ O:GHSA-8rrh-rw8j-w5fx,PYSEC-2026-2047 | V:OSV:PYSEC-2026-2047
  └────────────────────────────────────────────────────────────────────────────────────────────────────

  ━━ Debian/Ubuntu (deb) ━━
  ┌─ pkg:deb/ubuntu/binutils@2.42-4ubuntu2.10
  │ OGTV
  │ ✔✔✔✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ O:UBUNTU-CVE-2017-13716 | V:UB:CVE-2017-13716
  │ ✔✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2025-66862
  │ ✔✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2025-66863
  │ ✔✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-66864
  │ ✔✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2025-66865
  │ ✔✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·  ↳ O:UBUNTU-CVE-2025-66866
  │ ✔✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·  ↳ O:UBUNTU-CVE-2026-3441
  │ ✔✔✘✘ CVE-2026-3442          HIGH         7.1   0.2%   ·  ↳ O:UBUNTU-CVE-2026-3442
  │ ✔✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-6846
  │ ✔✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-11495
  │ ✔✔✔✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ O:UBUNTU-CVE-2025-69644 | V:UB:CVE-2025-69644
  │ ✔✔✔✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-69645 | V:UB:CVE-2025-69645
  │ ✔✔✔✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-69646 | V:UB:CVE-2025-69646
  │ ✔✔✔✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ O:UBUNTU-CVE-2025-69647 | V:UB:CVE-2025-69647
  │ ✔✔✔✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ O:UBUNTU-CVE-2025-69648 | V:UB:CVE-2025-69648
  │ ✔✔✔✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-69651 | V:UB:CVE-2025-69651
  │ ✔✔✔✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ O:UBUNTU-CVE-2025-69652 | V:UB:CVE-2025-69652
  │ ✔✔✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·  ↳ O:UBUNTU-CVE-2026-15003
  │ ✔✔✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2026-19548
  │ ✔✔✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·  ↳ O:UBUNTU-CVE-2026-4647
  │ ✔✔✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-6844
  │ ✔✔✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·  ↳ O:UBUNTU-CVE-2026-6845
  │ ✔✔✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·  ↳ O:UBUNTU-CVE-2026-90801
  │ ✔✔✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-90802
  │ ✔✔✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-90803
  │ ✔✔✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·  ↳ O:UBUNTU-CVE-2026-90804
  │ ✔✔✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·  ↳ O:UBUNTU-CVE-2026-90828
  │ ✔✔✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·  ↳ O:UBUNTU-CVE-2026-90829
  │ ✔✔✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·  ↳ O:UBUNTU-CVE-2026-90830
  │ ✔✔✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·  ↳ O:UBUNTU-CVE-2026-90831
  │ ✔✔✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-91779
  │ ✔✔✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-91780
  │ ✔✔✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-91781
  │ ✔✔✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-91782
  │ ✔✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1149
  │ ✔✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1150
  │ ✔✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1151
  │ ✔✔✔✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1152 | V:UB:CVE-2025-1152
  │ ✔✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·  ↳ O:UBUNTU-CVE-2025-66861
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/binutils-aarch64-linux-gnu@2.42-4ubuntu2.10
  │ OGTV
  │ ✘✘✔✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✘✔✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ V:UB:CVE-2025-69644
  │ ✘✘✔✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✘✔✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69646
  │ ✘✘✔✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69647
  │ ✘✘✔✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69648
  │ ✘✘✔✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✘✔✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✘✔✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/binutils-common@2.42-4ubuntu2.10
  │ OGTV
  │ ✘✘✔✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✘✔✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ V:UB:CVE-2025-69644
  │ ✘✘✔✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✘✔✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69646
  │ ✘✘✔✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69647
  │ ✘✘✔✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69648
  │ ✘✘✔✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✘✔✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✘✔✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/bsdutils@1%3A2.39.3-9ubuntu6.5
  │ OGTV
  │ ✘✘✔✘ CVE-2026-53612         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53614         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-27456         MEDIUM       4.7   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/bzip2@1.0.8-5.1build0.1
  │ OGTV
  │ ✔✔✔✔ CVE-2026-42250         MEDIUM       4.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-42250,USN-8685-1 | V:UB:CVE-2026-42250
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/coreutils@9.4-3ubuntu6.2
  │ OGTV
  │ ✔✔✘✘ CVE-2016-2781          MEDIUM       6.5   0.4%   ·  ↳ O:UBUNTU-CVE-2016-2781
  │ ✔✔✔✔ CVE-2025-5278          MEDIUM       4.4   0.3%   ·  ↳ O:UBUNTU-CVE-2025-5278,USN-8697-1 | V:UB:CVE-2025-5278
  │ ✔✘✘✘ CVE-2026-56391         MEDIUM       6.1   0.2%   ·  ↳ O:USN-8697-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/curl@8.5.0-2ubuntu10.11
  │ OGTV
  │ ✔✔✔✔ CVE-2026-11856         CRITICAL     9.8   0.7%   ·  ↳ O:UBUNTU-CVE-2026-11856 | V:UB:CVE-2026-11856
  │ ✔✔✔✔ CVE-2026-18924         CRITICAL     9.1   0.6%   ·  ↳ O:UBUNTU-CVE-2026-18924,USN-8820-1 | V:UB:CVE-2026-18924
  │ ✔✘✘✘ CVE-2026-8927          CRITICAL     9.1   0.5%   ·  ↳ O:USN-8820-1
  │ ✔✔✔✔ CVE-2026-13608         HIGH         7.4   0.5%   ·  ↳ O:UBUNTU-CVE-2026-13608,USN-8820-1 | V:UB:CVE-2026-13608
  │ ✔✘✘✘ CVE-2026-80229         HIGH         7.5   0.6%   ·  ↳ O:USN-8820-1
  │ ✔✔✔✔ CVE-2026-80230         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-80230,USN-8820-1 | V:UB:CVE-2026-80230
  │ ✔✘✘✘ CVE-2026-80255         HIGH         7.5   0.5%   ·  ↳ O:USN-8820-1
  │ ✔✔✔✔ CVE-2026-82209         HIGH         8.2   0.4%   ·  ↳ O:UBUNTU-CVE-2026-82209,USN-8820-1 | V:UB:CVE-2026-82209
  │ ✔✔✔✔ CVE-2026-8932          HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-8932,USN-8670-1 | V:UB:CVE-2026-8932
  │ ✔✘✘✘ CVE-2026-9080          HIGH         7.3   0.5%   ·  ↳ O:USN-8820-1
  │ ✘✘✔✔ CVE-2026-86409         LOW          0.0      -   ·  ↳ V:UB:CVE-2026-86409
  │ ✘✘✔✔ CVE-2026-86414         LOW          6.5      -   ·  ↳ V:UB:CVE-2026-86414
  │ ✘✘✔✔ CVE-2026-87862         LOW          0.0      -   ·  ↳ V:UB:CVE-2026-87862
  │ ✘✘✔✔ CVE-2026-87863         LOW          0.0      -   ·  ↳ V:UB:CVE-2026-87863
  │ ✘✘✔✔ CVE-2026-87864         LOW          0.0      -   ·  ↳ V:UB:CVE-2026-87864
  │ ✘✘✔✔ CVE-2026-92388         LOW          6.5      -   ·  ↳ V:UB:CVE-2026-92388
  │ ✘✘✔✔ CVE-2026-92389         LOW          0.0      -   ·  ↳ V:UB:CVE-2026-92389
  │ ✘✘✔✔ CVE-2026-92391         LOW          0.0      -   ·  ↳ V:UB:CVE-2026-92391
  │ ✘✘✔✔ CVE-2026-94266         LOW          0.0      -   ·  ↳ V:UB:CVE-2026-94266
  │ ✔✘✘✘ USN-8651-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dash@0.5.12-6ubuntu5
  │ OGTV
  │ ✔✔✔✔ CVE-2026-102473        MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-102473 | V:UB:CVE-2026-102473
  │ ✔✔✔✔ CVE-2026-102474        MEDIUM       4.0   0.1%   ·  ↳ O:UBUNTU-CVE-2026-102474 | V:UB:CVE-2026-102474
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/diffutils@1%3A3.10-1build1
  │ OGTV
  │ ✘✔✔✔ CVE-2026-53910         LOW          2.1   0.3%   ·  ↳ V:UB:CVE-2026-53910
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dirmngr@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✘✔✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc-13@13.3.0-6ubuntu2~24.04.1
  │ OGTV
  │ ✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-102010
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gnupg@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✘✔✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gnupg-l10n@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✘✔✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gnupg-utils@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✘✔✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✘✔✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg-agent@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✘✔✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg-wks-client@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✘✔✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpgconf@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✘✔✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpgsm@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✘✔✔ CVE-2026-57062         LOW          2.9   0.1%   ·  ↳ V:UB:CVE-2026-57062
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpgv@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✘✔✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gzip@1.12-1ubuntu3.1
  │ OGTV
  │ ✔✔✔✔ CVE-2026-41992         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-41992,USN-8512-1 | V:UB:CVE-2026-41992
  │ ✔✔✔✔ CVE-2026-41991         MEDIUM       4.7   0.1%   ·  ↳ O:UBUNTU-CVE-2026-41991,USN-8512-1 | V:UB:CVE-2026-41991
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/keyboxd@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✘✔✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libaom3@3.8.2-2ubuntu0.1
  │ OGTV
  │ ✘✘✔✔ CVE-2026-56208         HIGH         7.6   0.4%   ·  ↳ V:UB:CVE-2026-56208
  │ ✘✘✔✔ CVE-2026-56209         HIGH         7.1   0.6%   ·  ↳ V:UB:CVE-2026-56209
  │ ✘✘✔✔ CVE-2026-56210         HIGH         7.1   0.6%   ·  ↳ V:UB:CVE-2026-56210
  │ ✘✘✔✔ CVE-2026-56211         HIGH         7.1   0.9%   ·  ↳ V:UB:CVE-2026-56211
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libattr1@1%3A2.5.2-1build1.1
  │ OGTV
  │ ✘✘✔✔ CVE-2026-54371         HIGH         8.4   0.1%   ·  ↳ V:UB:CVE-2026-54371
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libbinutils@2.42-4ubuntu2.10
  │ OGTV
  │ ✘✘✔✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✘✔✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ V:UB:CVE-2025-69644
  │ ✘✘✔✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✘✔✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69646
  │ ✘✘✔✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69647
  │ ✘✘✔✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69648
  │ ✘✘✔✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✘✔✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✘✔✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libblkid1@2.39.3-9ubuntu6.5
  │ OGTV
  │ ✘✘✔✘ CVE-2026-53612         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53614         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-27456         MEDIUM       4.7   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libbz2-1.0@1.0.8-5.1build0.1
  │ OGTV
  │ ✘✘✔✘ CVE-2026-42250         MEDIUM       4.8   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc-bin@2.39-0ubuntu8.8
  │ OGTV
  │ ✘✘✔✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-19499         HIGH         7.7   0.3%   ·
  │ ✘✘✔✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ V:UB:CVE-2026-18374
  │ ✘✘✔✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·
  │ ✘✘✔✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·
  │ ✘✘✔✔ CVE-2026-89092         MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-89092
  │ ✘✘✔✘ CVE-2026-6368          LOW          2.1   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc-dev-bin@2.39-0ubuntu8.8
  │ OGTV
  │ ✘✘✔✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-19499         HIGH         7.7   0.3%   ·
  │ ✘✘✔✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ V:UB:CVE-2026-18374
  │ ✘✘✔✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·
  │ ✘✘✔✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·
  │ ✘✘✔✔ CVE-2026-89092         MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-89092
  │ ✘✘✔✘ CVE-2026-6368          LOW          2.1   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc-devtools@2.39-0ubuntu8.8
  │ OGTV
  │ ✘✘✔✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-19499         HIGH         7.7   0.3%   ·
  │ ✘✘✔✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ V:UB:CVE-2026-18374
  │ ✘✘✔✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·
  │ ✘✘✔✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·
  │ ✘✘✔✔ CVE-2026-89092         MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-89092
  │ ✘✘✔✘ CVE-2026-6368          LOW          2.1   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc6@2.39-0ubuntu8.8
  │ OGTV
  │ ✘✘✔✔ CVE-2026-6791          CRITICAL     9.0   0.2%   ·  ↳ V:UB:CVE-2026-6791
  │ ✘✘✔✔ CVE-2026-19499         HIGH         7.7   0.3%   ·  ↳ V:UB:CVE-2026-19499
  │ ✘✘✔✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ V:UB:CVE-2026-18374
  │ ✘✘✔✔ CVE-2026-19542         MEDIUM       5.6   0.2%   ·  ↳ V:UB:CVE-2026-19542
  │ ✘✘✔✔ CVE-2026-77117         MEDIUM       5.9   0.4%   ·  ↳ V:UB:CVE-2026-77117
  │ ✘✘✔✔ CVE-2026-80489         MEDIUM       5.9   0.4%   ·  ↳ V:UB:CVE-2026-80489
  │ ✘✘✔✔ CVE-2026-89092         MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-89092
  │ ✘✘✔✔ CVE-2026-6368          LOW          2.1   0.1%   ·  ↳ V:UB:CVE-2026-6368
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc6-dev@2.39-0ubuntu8.8
  │ OGTV
  │ ✘✘✔✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-19499         HIGH         7.7   0.3%   ·
  │ ✘✘✔✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ V:UB:CVE-2026-18374
  │ ✘✘✔✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·
  │ ✘✘✔✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·
  │ ✘✘✔✔ CVE-2026-89092         MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-89092
  │ ✘✘✔✘ CVE-2026-6368          LOW          2.1   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libctf-nobfd0@2.42-4ubuntu2.10
  │ OGTV
  │ ✘✘✔✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✘✔✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ V:UB:CVE-2025-69644
  │ ✘✘✔✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✘✔✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69646
  │ ✘✘✔✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69647
  │ ✘✘✔✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69648
  │ ✘✘✔✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✘✔✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✘✔✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libctf0@2.42-4ubuntu2.10
  │ OGTV
  │ ✘✘✔✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✘✔✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ V:UB:CVE-2025-69644
  │ ✘✘✔✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✘✔✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69646
  │ ✘✘✔✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69647
  │ ✘✘✔✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69648
  │ ✘✘✔✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✘✔✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✘✔✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libcurl4t64@8.5.0-2ubuntu10.11
  │ OGTV
  │ ✘✘✔✔ CVE-2026-11856         CRITICAL     9.8   0.7%   ·  ↳ V:UB:CVE-2026-11856
  │ ✘✘✔✔ CVE-2026-18924         CRITICAL     9.1   0.6%   ·  ↳ V:UB:CVE-2026-18924
  │ ✘✘✔✔ CVE-2026-13608         HIGH         7.4   0.5%   ·  ↳ V:UB:CVE-2026-13608
  │ ✘✘✔✔ CVE-2026-80230         HIGH         7.5   0.4%   ·  ↳ V:UB:CVE-2026-80230
  │ ✘✘✔✔ CVE-2026-82209         HIGH         8.2   0.4%   ·  ↳ V:UB:CVE-2026-82209
  │ ✘✘✔✔ CVE-2026-8932          HIGH         7.5   0.4%   ·  ↳ V:UB:CVE-2026-8932
  │ ✘✘✔✔ CVE-2026-86409         LOW          0.0      -   ·  ↳ V:UB:CVE-2026-86409
  │ ✘✘✔✔ CVE-2026-86414         LOW          6.5      -   ·  ↳ V:UB:CVE-2026-86414
  │ ✘✘✔✔ CVE-2026-87862         LOW          0.0      -   ·  ↳ V:UB:CVE-2026-87862
  │ ✘✘✔✔ CVE-2026-87863         LOW          0.0      -   ·  ↳ V:UB:CVE-2026-87863
  │ ✘✘✔✔ CVE-2026-87864         LOW          0.0      -   ·  ↳ V:UB:CVE-2026-87864
  │ ✘✘✔✔ CVE-2026-92388         LOW          6.5      -   ·  ↳ V:UB:CVE-2026-92388
  │ ✘✘✔✔ CVE-2026-92389         LOW          0.0      -   ·  ↳ V:UB:CVE-2026-92389
  │ ✘✘✔✔ CVE-2026-92391         LOW          0.0      -   ·  ↳ V:UB:CVE-2026-92391
  │ ✘✘✔✔ CVE-2026-94266         LOW          0.0      -   ·  ↳ V:UB:CVE-2026-94266
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libexpat1@2.6.1-2ubuntu0.4
  │ OGTV
  │ ✘✘✔✔ CVE-2025-59375         HIGH         7.5   1.3%   ·  ↳ V:UB:CVE-2025-59375
  │ ✘✘✔✔ CVE-2026-41080         HIGH         7.5   0.4%   ·  ↳ V:UB:CVE-2026-41080
  │ ✘✘✔✔ CVE-2026-45186         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-45186
  │ ✘✘✔✔ CVE-2026-66046         HIGH         8.7   0.7%   ·  ↳ V:UB:CVE-2026-66046
  │ ✘✘✔✔ CVE-2026-76641         HIGH         8.7   0.4%   ·  ↳ V:UB:CVE-2026-76641
  │ ✘✘✔✔ CVE-2026-76957         HIGH         7.8   0.1%   ·  ↳ V:UB:CVE-2026-76957
  │ ✘✘✔✔ CVE-2025-66382         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-66382
  │ ✘✘✔✔ CVE-2026-32776         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-32776
  │ ✘✘✔✔ CVE-2026-32777         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-32777
  │ ✘✘✔✔ CVE-2026-32778         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-32778
  │ ✘✘✔✔ CVE-2026-50219         MEDIUM       5.9   0.2%   ·  ↳ V:UB:CVE-2026-50219
  │ ✘✘✔✔ CVE-2026-56131         MEDIUM       4.9   0.2%   ·  ↳ V:UB:CVE-2026-56131
  │ ✘✘✔✔ CVE-2026-56132         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56132
  │ ✘✘✔✔ CVE-2026-56403         MEDIUM       6.9   0.2%   ·  ↳ V:UB:CVE-2026-56403
  │ ✘✘✔✔ CVE-2026-56404         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56404
  │ ✘✘✔✔ CVE-2026-56405         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56405
  │ ✘✘✔✔ CVE-2026-56406         MEDIUM       6.9   0.2%   ·  ↳ V:UB:CVE-2026-56406
  │ ✘✘✔✔ CVE-2026-56407         MEDIUM       6.9   0.2%   ·  ↳ V:UB:CVE-2026-56407
  │ ✘✘✔✔ CVE-2026-56408         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56408
  │ ✘✘✔✔ CVE-2026-56409         MEDIUM       6.5   0.1%   ·  ↳ V:UB:CVE-2026-56409
  │ ✘✘✔✔ CVE-2026-56410         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56410
  │ ✘✘✔✔ CVE-2026-56411         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56411
  │ ✘✘✔✔ CVE-2026-56412         MEDIUM       5.9   0.2%   ·  ↳ V:UB:CVE-2026-56412
  │ ✘✘✔✔ CVE-2026-72522         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2026-72522
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libexpat1-dev@2.6.1-2ubuntu0.4
  │ OGTV
  │ ✘✘✔✔ CVE-2025-59375         HIGH         7.5   1.3%   ·  ↳ V:UB:CVE-2025-59375
  │ ✘✘✔✔ CVE-2026-41080         HIGH         7.5   0.4%   ·  ↳ V:UB:CVE-2026-41080
  │ ✘✘✔✔ CVE-2026-45186         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-45186
  │ ✘✘✔✔ CVE-2026-66046         HIGH         8.7   0.7%   ·  ↳ V:UB:CVE-2026-66046
  │ ✘✘✔✔ CVE-2026-76641         HIGH         8.7   0.4%   ·  ↳ V:UB:CVE-2026-76641
  │ ✘✘✔✔ CVE-2026-76957         HIGH         7.8   0.1%   ·  ↳ V:UB:CVE-2026-76957
  │ ✘✘✔✔ CVE-2025-66382         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-66382
  │ ✘✘✔✔ CVE-2026-32776         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-32776
  │ ✘✘✔✔ CVE-2026-32777         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-32777
  │ ✘✘✔✔ CVE-2026-32778         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-32778
  │ ✘✘✔✔ CVE-2026-50219         MEDIUM       5.9   0.2%   ·  ↳ V:UB:CVE-2026-50219
  │ ✘✘✔✔ CVE-2026-56131         MEDIUM       4.9   0.2%   ·  ↳ V:UB:CVE-2026-56131
  │ ✘✘✔✔ CVE-2026-56132         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56132
  │ ✘✘✔✔ CVE-2026-56403         MEDIUM       6.9   0.2%   ·  ↳ V:UB:CVE-2026-56403
  │ ✘✘✔✔ CVE-2026-56404         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56404
  │ ✘✘✔✔ CVE-2026-56405         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56405
  │ ✘✘✔✔ CVE-2026-56406         MEDIUM       6.9   0.2%   ·  ↳ V:UB:CVE-2026-56406
  │ ✘✘✔✔ CVE-2026-56407         MEDIUM       6.9   0.2%   ·  ↳ V:UB:CVE-2026-56407
  │ ✘✘✔✔ CVE-2026-56408         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56408
  │ ✘✘✔✔ CVE-2026-56409         MEDIUM       6.5   0.1%   ·  ↳ V:UB:CVE-2026-56409
  │ ✘✘✔✔ CVE-2026-56410         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56410
  │ ✘✘✔✔ CVE-2026-56411         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56411
  │ ✘✘✔✔ CVE-2026-56412         MEDIUM       5.9   0.2%   ·  ↳ V:UB:CVE-2026-56412
  │ ✘✘✔✔ CVE-2026-72522         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2026-72522
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libfreetype6@2.13.2%2Bdfsg-1ubuntu0.1
  │ OGTV
  │ ✘✘✔✔ CVE-2026-95512         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-95512
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgcrypt20@1.10.3-2ubuntu0.1
  │ OGTV
  │ ✔✔✔✔ CVE-2024-2236          MEDIUM       5.9   1.1%   ·  ↳ O:UBUNTU-CVE-2024-2236,USN-8711-1 | V:UB:CVE-2024-2236
  │ ✘✘✘✔ CVE-2026-41990         MEDIUM       4.0   0.2%   ·  ↳ V:UB:CVE-2026-41990
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgnutls30t64@3.8.3-1.1ubuntu3.6
  │ OGTV
  │ ✘✘✔✔ CVE-2026-88647         CRITICAL     9.1   0.2%   ·  ↳ V:UB:CVE-2026-88647
  │ ✘✘✔✔ CVE-2026-95210         CRITICAL     9.1   0.2%   ·  ↳ V:UB:CVE-2026-95210
  │ ✘✘✔✔ CVE-2026-67693         HIGH         7.5   0.2%   ·  ↳ V:UB:CVE-2026-67693
  │ ✘✘✔✔ CVE-2026-95184         HIGH         7.5   0.2%   ·  ↳ V:UB:CVE-2026-95184
  │ ✘✘✔✔ CVE-2026-95209         HIGH         7.5   0.3%   ·  ↳ V:UB:CVE-2026-95209
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgprofng0@2.42-4ubuntu2.10
  │ OGTV
  │ ✘✘✔✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✘✔✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ V:UB:CVE-2025-69644
  │ ✘✘✔✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✘✔✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69646
  │ ✘✘✔✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69647
  │ ✘✘✔✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69648
  │ ✘✘✔✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✘✔✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✘✔✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libheif-plugin-aomdec@1.17.6-1ubuntu4.6
  │ OGTV
  │ ✘✘✔✔ CVE-2026-84384         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-84384
  │ ✘✘✘✔ CVE-2026-84447         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-84447
  │ ✘✘✔✔ CVE-2026-62289         MEDIUM       4.3   0.3%   ·  ↳ V:UB:CVE-2026-62289
  │ ✘✘✔✔ CVE-2026-62291         MEDIUM       5.3   0.2%   ·  ↳ V:UB:CVE-2026-62291
  │ ✘✘✔✔ CVE-2026-84448         MEDIUM       4.0   0.2%   ·  ↳ V:UB:CVE-2026-84448
  │ ✘✘✔✔ CVE-2026-84449         LOW          3.7   0.4%   ·  ↳ V:UB:CVE-2026-84449
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libheif-plugin-aomenc@1.17.6-1ubuntu4.6
  │ OGTV
  │ ✘✘✔✔ CVE-2026-84384         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-84384
  │ ✘✘✘✔ CVE-2026-84447         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-84447
  │ ✘✘✔✔ CVE-2026-62289         MEDIUM       4.3   0.3%   ·  ↳ V:UB:CVE-2026-62289
  │ ✘✘✔✔ CVE-2026-62291         MEDIUM       5.3   0.2%   ·  ↳ V:UB:CVE-2026-62291
  │ ✘✘✔✔ CVE-2026-84448         MEDIUM       4.0   0.2%   ·  ↳ V:UB:CVE-2026-84448
  │ ✘✘✔✔ CVE-2026-84449         LOW          3.7   0.4%   ·  ↳ V:UB:CVE-2026-84449
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libheif1@1.17.6-1ubuntu4.6
  │ OGTV
  │ ✘✘✔✔ CVE-2026-84384         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-84384
  │ ✘✘✘✔ CVE-2026-84447         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-84447
  │ ✘✘✔✔ CVE-2026-62289         MEDIUM       4.3   0.3%   ·  ↳ V:UB:CVE-2026-62289
  │ ✘✘✔✔ CVE-2026-62291         MEDIUM       5.3   0.2%   ·  ↳ V:UB:CVE-2026-62291
  │ ✘✘✔✔ CVE-2026-84448         MEDIUM       4.0   0.2%   ·  ↳ V:UB:CVE-2026-84448
  │ ✘✘✔✔ CVE-2026-84449         LOW          3.7   0.4%   ·  ↳ V:UB:CVE-2026-84449
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libhwasan0@14.2.0-4ubuntu2~24.04.1
  │ OGTV
  │ ✘✘✘✔ CVE-2021-3826          MEDIUM       6.5   1.4%   ·  ↳ V:UB:CVE-2021-3826
  │ ✘✘✘✔ CVE-2021-46195         MEDIUM       5.5   0.8%   ·  ↳ V:UB:CVE-2021-46195
  │ ✘✘✘✔ CVE-2022-27943         MEDIUM       5.5   1.0%   ·  ↳ V:UB:CVE-2022-27943
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libmount1@2.39.3-9ubuntu6.5
  │ OGTV
  │ ✘✘✔✘ CVE-2026-53612         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53614         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-27456         MEDIUM       4.7   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libncursesw6@6.4%2B20240113-1ubuntu2
  │ OGTV
  │ ✘✘✔✔ CVE-2025-69720         CRITICAL     9.8   0.4%   ·  ↳ V:UB:CVE-2025-69720
  │ ✘✘✔✘ CVE-2025-6141          MEDIUM       4.8   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libp11-kit0@0.25.3-4ubuntu2.1
  │ OGTV
  │ ✘✘✔✔ CVE-2026-13757         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2026-13757
  │ ✘✘✔✔ CVE-2026-18938         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2026-18938
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-modules@1.5.3-5ubuntu5.5
  │ OGTV
  │ ✘✘✔✔ CVE-2026-54411         HIGH         8.2   0.5%   ·  ↳ V:UB:CVE-2026-54411
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-modules-bin@1.5.3-5ubuntu5.5
  │ OGTV
  │ ✘✘✔✘ CVE-2026-54411         HIGH         8.2   0.5%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-runtime@1.5.3-5ubuntu5.5
  │ OGTV
  │ ✘✘✔✘ CVE-2026-54411         HIGH         8.2   0.5%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam0g@1.5.3-5ubuntu5.5
  │ OGTV
  │ ✘✘✔✘ CVE-2026-54411         HIGH         8.2   0.5%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpcre2-8-0@10.42-4ubuntu2.1
  │ OGTV
  │ ✘✘✔✔ CVE-2026-103111        HIGH         7.6   0.2%   ·  ↳ V:UB:CVE-2026-103111
  │ ✘✘✔✔ CVE-2026-86145         HIGH         8.2   0.4%   ·  ↳ V:UB:CVE-2026-86145
  │ ✘✘✔✔ CVE-2026-89157         HIGH         7.4   0.3%   ·  ↳ V:UB:CVE-2026-89157
  │ ✘✘✔✔ CVE-2026-89161         HIGH         7.8   0.1%   ·  ↳ V:UB:CVE-2026-89161
  │ ✘✘✔✔ CVE-2026-89156         MEDIUM       5.9   0.3%   ·  ↳ V:UB:CVE-2026-89156
  │ ✘✘✔✔ CVE-2026-89158         MEDIUM       6.5   0.2%   ·  ↳ V:UB:CVE-2026-89158
  │ ✘✘✔✔ CVE-2026-89160         MEDIUM       6.5   0.3%   ·  ↳ V:UB:CVE-2026-89160
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libperl5.38t64@5.38.2-3.2ubuntu0.3
  │ OGTV
  │ ✘✘✔✘ CVE-2026-12087         CRITICAL     9.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-13221         CRITICAL     9.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-57433         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-48959         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-48962         HIGH         7.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-57432         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-7017          HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-9538          HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2025-15649         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✔ CVE-2026-15534         MEDIUM       5.7   0.3%   ·  ↳ V:UB:CVE-2026-15534
  │ ✘✘✔✔ CVE-2026-19487         MEDIUM       5.3   0.4%   ·  ↳ V:UB:CVE-2026-19487
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpng16-16t64@1.6.43-5ubuntu0.6
  │ OGTV
  │ ✘✘✔✔ CVE-2026-46675         MEDIUM       0.0      -   ·  ↳ V:UB:CVE-2026-46675
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.12-dev@3.12.3-1ubuntu0.15
  │ OGTV
  │ ✘✘✔✘ CVE-2026-15308         HIGH         8.7   0.6%   ·
  │ ✘✘✔✘ CVE-2026-4360          MEDIUM       5.3   0.5%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.12-minimal@3.12.3-1ubuntu0.15
  │ OGTV
  │ ✘✘✔✘ CVE-2026-15308         HIGH         8.7   0.6%   ·
  │ ✘✘✔✘ CVE-2026-4360          MEDIUM       5.3   0.5%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.12-stdlib@3.12.3-1ubuntu0.15
  │ OGTV
  │ ✘✘✔✘ CVE-2026-15308         HIGH         8.7   0.6%   ·
  │ ✘✘✔✘ CVE-2026-4360          MEDIUM       5.3   0.5%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.12t64@3.12.3-1ubuntu0.15
  │ OGTV
  │ ✘✘✔✔ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ V:UB:CVE-2026-15308
  │ ✘✘✔✔ CVE-2026-4360          MEDIUM       5.3   0.5%   ·  ↳ V:UB:CVE-2026-4360
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsasl2-2@2.1.28%2Bdfsg1-5ubuntu3.1
  │ OGTV
  │ ✘✘✔✘ CVE-2026-107161        HIGH         7.5   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsasl2-modules@2.1.28%2Bdfsg1-5ubuntu3.1
  │ OGTV
  │ ✘✘✔✘ CVE-2026-107161        HIGH         7.5   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsasl2-modules-db@2.1.28%2Bdfsg1-5ubuntu3.1
  │ OGTV
  │ ✘✘✔✘ CVE-2026-107161        HIGH         7.5   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsframe1@2.42-4ubuntu2.10
  │ OGTV
  │ ✘✘✔✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✘✔✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ V:UB:CVE-2025-69644
  │ ✘✘✔✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✘✔✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69646
  │ ✘✘✔✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69647
  │ ✘✘✔✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69648
  │ ✘✘✔✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✘✔✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✘✔✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsmartcols1@2.39.3-9ubuntu6.5
  │ OGTV
  │ ✘✘✔✘ CVE-2026-53612         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53614         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-27456         MEDIUM       4.7   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsqlite3-0@3.45.1-1ubuntu2.7
  │ OGTV
  │ ✘✘✔✔ CVE-2026-39113         MEDIUM       4.0   0.2%   ·  ↳ V:UB:CVE-2026-39113
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libssh-4@0.10.6-2ubuntu0.4
  │ OGTV
  │ ✘✘✔✔ CVE-2026-59847         HIGH         7.5   0.3%   ·  ↳ V:UB:CVE-2026-59847
  │ ✘✘✔✔ CVE-2026-59850         HIGH         7.5   0.3%   ·  ↳ V:UB:CVE-2026-59850
  │ ✘✘✔✔ CVE-2026-59843         MEDIUM       6.5   0.7%   ·  ↳ V:UB:CVE-2026-59843
  │ ✘✘✔✔ CVE-2026-59845         MEDIUM       5.9   0.1%   ·  ↳ V:UB:CVE-2026-59845
  │ ✘✘✔✔ CVE-2026-59848         MEDIUM       5.3   0.3%   ·  ↳ V:UB:CVE-2026-59848
  │ ✘✘✔✔ CVE-2026-59846         LOW          3.9   0.1%   ·  ↳ V:UB:CVE-2026-59846
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libssl3t64@3.0.13-0ubuntu3.12
  │ OGTV
  │ ✘✘✔✔ CVE-2026-75803         CRITICAL     9.1   0.2%   ·  ↳ V:UB:CVE-2026-75803
  │ ✘✘✔✔ CVE-2026-54874         HIGH         7.5   0.6%   ·  ↳ V:UB:CVE-2026-54874
  │ ✘✘✔✔ CVE-2026-63072         HIGH         7.5   0.9%   ·  ↳ V:UB:CVE-2026-63072
  │ ✘✘✔✔ CVE-2026-63076         HIGH         7.5   1.6%   ·  ↳ V:UB:CVE-2026-63076
  │ ✘✘✔✔ CVE-2026-84782         HIGH         8.2   0.4%   ·  ↳ V:UB:CVE-2026-84782
  │ ✘✘✔✔ CVE-2026-35189         MEDIUM       5.3   0.3%   ·  ↳ V:UB:CVE-2026-35189
  │ ✘✘✔✔ CVE-2026-63074         MEDIUM       5.9   0.6%   ·  ↳ V:UB:CVE-2026-63074
  │ ✘✘✔✔ CVE-2026-75805         MEDIUM       5.3   0.2%   ·  ↳ V:UB:CVE-2026-75805
  │ ✘✘✔✔ CVE-2026-75806         MEDIUM       5.3   0.4%   ·  ↳ V:UB:CVE-2026-75806
  │ ✘✘✔✔ CVE-2026-54872         LOW          3.7   0.3%   ·  ↳ V:UB:CVE-2026-54872
  │ ✘✘✔✔ CVE-2026-77696         LOW          3.7   0.2%   ·  ↳ V:UB:CVE-2026-77696
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsystemd0@255.4-1ubuntu8.16
  │ OGTV
  │ ✘✘✔✘ CVE-2026-15059         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-16742         MEDIUM       6.7   0.1%   ·
  │ ✘✘✔✔ CVE-2026-40228         LOW          3.3   0.1%   ·  ↳ V:UB:CVE-2026-40228
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libtinfo6@6.4%2B20240113-1ubuntu2
  │ OGTV
  │ ✘✘✔✔ CVE-2025-69720         CRITICAL     9.8   0.4%   ·  ↳ V:UB:CVE-2025-69720
  │ ✘✘✔✔ CVE-2025-6141          MEDIUM       4.8   0.2%   ·  ↳ V:UB:CVE-2025-6141
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libudev1@255.4-1ubuntu8.16
  │ OGTV
  │ ✘✘✔✘ CVE-2026-15059         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-16742         MEDIUM       6.7   0.1%   ·
  │ ✘✘✔✔ CVE-2026-40228         LOW          3.3   0.1%   ·  ↳ V:UB:CVE-2026-40228
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libuuid1@2.39.3-9ubuntu6.5
  │ OGTV
  │ ✘✘✔✘ CVE-2026-53612         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53614         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-27456         MEDIUM       4.7   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libx11-6@2%3A1.8.7-1build1
  │ OGTV
  │ ✘✘✔✔ CVE-2026-88806         HIGH         7.5   0.2%   ·  ↳ V:UB:CVE-2026-88806
  │ ✘✘✔✔ CVE-2026-94283         MEDIUM       6.5   0.2%   ·  ↳ V:UB:CVE-2026-94283
  │ ✘✘✔✔ CVE-2026-94284         MEDIUM       5.5   0.1%   ·  ↳ V:UB:CVE-2026-94284
  │ ✘✘✔✔ CVE-2026-94285         MEDIUM       5.1   0.1%   ·  ↳ V:UB:CVE-2026-94285
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libx11-data@2%3A1.8.7-1build1
  │ OGTV
  │ ✘✘✔✘ CVE-2026-88806         HIGH         7.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-94283         MEDIUM       6.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-94284         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-94285         MEDIUM       5.1   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libxpm4@1%3A3.5.17-1ubuntu0.24.04.1
  │ OGTV
  │ ✘✘✔✔ CVE-2026-94287         MEDIUM       5.5   0.1%   ·  ↳ V:UB:CVE-2026-94287
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/linux-libc-dev@6.8.0-136.136
  │ OGTV
  │ ✘✘✔✘ CVE-2024-50106         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2025-10263         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2025-22077         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2025-39933         CRITICAL     9.4   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40074         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2025-68745         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-100075        CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-23240         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-31536         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-43083         CRITICAL     9.1   0.6%   ·
  │ ✘✘✔✘ CVE-2026-43197         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-43198         CRITICAL     9.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-43379         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-43465         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-46325         CRITICAL     9.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-52914         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-52924         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-52931         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-53131         CRITICAL     9.4   0.4%   ·
  │ ✘✘✔✘ CVE-2026-53151         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-53176         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-53186         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-53215         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-53216         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-53221         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-53224         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-53225         CRITICAL     9.1   0.6%   ·
  │ ✘✘✔✘ CVE-2026-53228         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-53246         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-53247         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-53355         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-53384         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-53398         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-53399         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-63795         CRITICAL    10.0   0.5%   ·
  │ ✘✘✔✘ CVE-2026-63800         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-63808         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-63825         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-63830         CRITICAL     9.4   0.4%   ·
  │ ✘✘✔✘ CVE-2026-63886         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-63887         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-63888         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-63912         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-63922         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-63924         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-63940         CRITICAL     9.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63978         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-63979         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-63984         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-63992         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-63993         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-63994         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64000         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64007         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64018         CRITICAL     9.3   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64025         CRITICAL     9.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64033         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64034         CRITICAL     9.3   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64046         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64047         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64055         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64056         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-64089         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-64091         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-64102         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64106         CRITICAL     9.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64113         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64125         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-64136         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64160         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-64268         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-64269         CRITICAL     9.1   0.7%   ·
  │ ✘✘✔✘ CVE-2026-64303         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-64319         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64320         CRITICAL     9.1   0.7%   ·
  │ ✘✘✔✘ CVE-2026-64355         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64383         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64384         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64385         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64386         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64387         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64391         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64392         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64393         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64397         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64399         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64450         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64523         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-64530         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64534         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-64535         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64541         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-64551         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64564         CRITICAL     9.8   1.4%   ·
  │ ✘✘✔✘ CVE-2026-64597         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-68082         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-68083         CRITICAL     9.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-68117         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68123         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-68124         CRITICAL     9.6   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68127         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68136         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68137         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68144         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68154         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-68156         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-68158         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-68159         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-68160         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-68161         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-68300         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-68302         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68343         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68381         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68388         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68426         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-68431         CRITICAL     9.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-68457         CRITICAL     9.1   0.7%   ·
  │ ✘✘✔✘ CVE-2026-68476         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-68477         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-72014         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72020         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72033         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-72041         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-72065         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72069         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72083         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72084         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72085         CRITICAL     9.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72098         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72129         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72130         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72191         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72192         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72194         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-72200         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72217         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72221         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72222         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72226         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-72234         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72251         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72288         CRITICAL     9.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72289         CRITICAL     9.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72296         CRITICAL     9.1   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72299         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72317         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72318         CRITICAL     9.4   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72319         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-72320         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-72322         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72323         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72329         CRITICAL     9.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72339         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72348         CRITICAL     9.1   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72351         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-72398         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72399         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72421         CRITICAL    10.0   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72422         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72436         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72451         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72463         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-72466         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72472         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72473         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72491         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72493         CRITICAL     9.9   0.3%   ·
  │ ✘✘✔✘ CVE-2026-72494         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72495         CRITICAL     9.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72496         CRITICAL     9.2   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74255         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-74267         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-74268         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-74269         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-74279         CRITICAL    10.0   0.8%   ·
  │ ✘✘✔✘ CVE-2026-74280         CRITICAL    10.0   0.8%   ·
  │ ✘✘✔✘ CVE-2026-74287         CRITICAL     9.1   0.7%   ·
  │ ✘✘✔✘ CVE-2026-74310         CRITICAL     9.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74345         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74350         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-74376         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-74384         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-74394         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74398         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-74401         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-74406         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-74427         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-74436         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74439         CRITICAL     9.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74473         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74474         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74475         CRITICAL    10.0   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74476         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74478         CRITICAL     9.8   0.9%   ·
  │ ✘✘✔✘ CVE-2026-74480         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-74493         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-74495         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74521         CRITICAL     9.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74556         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74569         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74581         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74586         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74587         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74588         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74597         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74608         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74611         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-74612         CRITICAL    10.0   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74616         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74628         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74662         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74669         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74688         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74705         CRITICAL    10.0   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74723         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-74730         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74737         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-74743         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74744         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74746         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74752         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80528         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-80551         CRITICAL     9.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80554         CRITICAL     9.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80557         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-80558         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-80561         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-80585         CRITICAL     9.4   0.3%   ·
  │ ✘✘✔✘ CVE-2026-80586         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80587         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80589         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80600         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-80603         CRITICAL     9.1   0.6%   ·
  │ ✘✘✔✘ CVE-2026-80609         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-80630         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-80634         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-80668         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-80670         CRITICAL     9.1   0.7%   ·
  │ ✘✘✔✘ CVE-2026-80671         CRITICAL     9.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80681         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-80684         CRITICAL     9.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80693         CRITICAL     9.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80694         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-80714         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-80725         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-80726         CRITICAL     9.3   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80945         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-80976         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-80980         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-81002         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89448         CRITICAL     9.3   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89478         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89479         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89482         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89485         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89492         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89494         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89495         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89526         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89530         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89532         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89533         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89536         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89537         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89538         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89541         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89542         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89550         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89551         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89555         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89631         CRITICAL     9.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-89633         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89634         CRITICAL     9.1   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89636         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89637         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89643         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89649         CRITICAL     9.1   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89650         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89652         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89653         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89654         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89655         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89656         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89659         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-89662         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89669         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89671         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89672         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89674         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89675         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-89676         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89686         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89697         CRITICAL     9.1   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89702         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89708         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-89712         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89713         CRITICAL     9.1   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89778         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89779         CRITICAL     9.1   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89783         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89786         CRITICAL     9.1   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89788         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89846         CRITICAL     9.1   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89847         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89857         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89930         CRITICAL     9.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89969         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89970         CRITICAL     9.8   0.8%   ·
  │ ✘✘✔✘ CVE-2026-89972         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-90011         CRITICAL     9.1   0.8%   ·
  │ ✘✘✔✘ CVE-2026-90036         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-90037         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-90042         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-90048         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-90049         CRITICAL     9.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90104         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-90110         CRITICAL     9.4   0.6%   ·
  │ ✘✘✔✘ CVE-2026-90151         CRITICAL     9.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-90230         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-90235         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-90413         CRITICAL     9.1   0.8%   ·
  │ ✘✘✔✘ CVE-2026-90414         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-92489         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-93207         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-93228         CRITICAL     9.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-97413         CRITICAL     9.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-98323         CRITICAL     9.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-98365         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2013-7445          HIGH         7.8   2.8%   ·
  │ ✘✘✔✘ CVE-2017-13165         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2018-12930         HIGH         7.8   0.4%   ·
  │ ✘✘✔✘ CVE-2018-12931         HIGH         7.8   0.4%   ·
  │ ✘✘✔✘ CVE-2019-14899         HIGH         7.4   0.8%   ·
  │ ✘✘✔✘ CVE-2019-15794         HIGH         7.2   1.2%   ·
  │ ✘✘✔✘ CVE-2019-19378         HIGH         7.8   2.4%   ·
  │ ✘✘✔✘ CVE-2019-19814         HIGH         9.3   3.3%   ·
  │ ✘✘✔✘ CVE-2019-20426         HIGH         7.8   1.9%   ·
  │ ✘✘✔✘ CVE-2020-14356         HIGH         7.8   1.0%   ·
  │ ✘✘✔✘ CVE-2021-26934         HIGH         7.8   0.3%   ·
  │ ✘✘✔✘ CVE-2021-3864          HIGH         7.0   0.8%   ·
  │ ✘✘✔✘ CVE-2022-0400          HIGH         7.5   1.8%   ·
  │ ✘✘✔✘ CVE-2022-1247          HIGH         7.0   0.3%   ·
  │ ✘✘✔✘ CVE-2022-25836         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2022-2961          HIGH         7.0   0.3%   ·
  │ ✘✘✔✘ CVE-2022-3238          HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2022-45885         HIGH         7.0   0.3%   ·
  │ ✘✘✔✘ CVE-2022-50090         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2022-50240         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2022-50551         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2023-0030          HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2023-26242         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2023-33053         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2023-52879         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2023-54187         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-14040         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2024-27022         HIGH         7.8   0.3%   ·
  │ ✘✘✔✘ CVE-2024-35948         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2024-38581         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-40954         HIGH         7.8   0.3%   ·
  │ ✘✘✔✘ CVE-2024-41008         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-43872         HIGH         7.5   0.3%   ·
  │ ✘✘✔✘ CVE-2024-44932         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-44951         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-44964         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-46833         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-49932         HIGH         7.0   0.2%   ·
  │ ✘✘✔✘ CVE-2024-49940         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-50217         HIGH         7.8   0.3%   ·
  │ ✘✘✔✘ CVE-2024-52560         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-53098         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-53207         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-53216         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-56552         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2024-56591         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2024-57857         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-57976         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-58015         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2024-58089         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-58094         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-58098         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-58100         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2024-58241         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-21687         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-21693         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-21984         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-21985         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-22043         HIGH         8.1   0.5%   ·
  │ ✘✘✔✘ CVE-2025-22104         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2025-22108         HIGH         8.6   0.4%   ·
  │ ✘✘✔✘ CVE-2025-22109         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-23132         HIGH         7.0   0.3%   ·
  │ ✘✘✔✘ CVE-2025-37776         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2025-37876         HIGH         7.0   0.3%   ·
  │ ✘✘✔✘ CVE-2025-37906         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-38064         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38069         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38187         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38189         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38204         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38206         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38242         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-38261         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38372         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38421         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38498         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38525         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2025-38563         HIGH         7.8   0.4%   ·
  │ ✘✘✔✘ CVE-2025-38565         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38636         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38717         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-39677         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-39789         HIGH         7.3   0.1%   ·
  │ ✘✘✔✘ CVE-2025-39859         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-39862         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-39896         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-39958         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-39990         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40014         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40025         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-40040         HIGH         7.8   0.4%   ·
  │ ✘✘✔✘ CVE-2025-40054         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40064         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-40075         HIGH         8.1   0.4%   ·
  │ ✘✘✔✘ CVE-2025-40139         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40158         HIGH         8.1   0.5%   ·
  │ ✘✘✔✘ CVE-2025-40168         HIGH         8.1   0.4%   ·
  │ ✘✘✔✘ CVE-2025-40170         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40190         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40203         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40274         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-40334         HIGH         7.3   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40344         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40354         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68174         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-68212         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-68304         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68360         HIGH         8.2   0.5%   ·
  │ ✘✘✔✘ CVE-2025-68730         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-68822         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-71073         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-71074         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-71080         HIGH         7.5   0.3%   ·
  │ ✘✘✔✘ CVE-2025-71202         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2025-71204         HIGH         7.5   0.3%   ·
  │ ✘✘✔✘ CVE-2025-71289         HIGH         7.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-23208         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23239         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23327         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23393         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23459         HIGH         8.2   0.4%   ·
  │ ✘✘✔✘ CVE-2026-31479         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-31486         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-31493         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-31568         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-31614         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-31630         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-31663         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-31771         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-43009         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43029         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-43042         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43048         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-43101         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-43116         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43126         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43172         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-43213         HIGH         7.5   0.3%   ·
  │ ✘✘✔✘ CVE-2026-43263         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43303         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43352         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43353         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43464         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-45894         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-45932         HIGH         7.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-45944         HIGH         7.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46054         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46130         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-46140         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46175         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-46181         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46203         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46242         HIGH         7.8   4.4%   ·
  │ ✘✘✔✘ CVE-2026-46275         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-46320         HIGH         7.4   0.3%   ·
  │ ✘✘✔✘ CVE-2026-46321         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46322         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46324         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46330         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46331         HIGH         7.8   0.6% KEV
  │ ✘✘✔✘ CVE-2026-52908         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52909         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52910         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52912         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-52915         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52917         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52918         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-52919         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52922         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-52923         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-52927         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52929         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-52934         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-52935         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52942         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52943         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-52945         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-52946         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-52947         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52953         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52956         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-52960         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-52988         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52991         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53000         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53005         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53009         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53024         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53025         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53053         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53070         HIGH         7.5   0.3%   ·
  │ ✘✘✔✘ CVE-2026-53078         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53089         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53090         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53091         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53109         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53118         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53120         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53129         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53132         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53133         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53136         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53137         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53138         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53143         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53146         HIGH         7.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-53147         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-53148         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53149         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53156         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53157         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53159         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53160         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53161         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53178         HIGH         8.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53179         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53182         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53183         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-53184         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-53185         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53189         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53194         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53195         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53198         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-53199         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-53202         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53205         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53209         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53212         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53217         HIGH         8.6   0.4%   ·
  │ ✘✘✔✘ CVE-2026-53223         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53229         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-53230         HIGH         8.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53232         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-53239         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53242         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53250         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53253         HIGH         7.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-53254         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-53255         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53256         HIGH         8.0   0.3%   ·
  │ ✘✘✔✘ CVE-2026-53262         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53264         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53265         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53266         HIGH         8.8   0.8% KEV
  │ ✘✘✔✘ CVE-2026-53267         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53268         HIGH         8.2   0.4%   ·
  │ ✘✘✔✘ CVE-2026-53270         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53272         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53273         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53275         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-53281         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53284         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-53329         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53330         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53354         HIGH         8.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-53356         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53357         HIGH         8.0   0.3%   ·
  │ ✘✘✔✘ CVE-2026-53358         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53359         HIGH         8.8   1.0%   ·
  │ ✘✘✔✘ CVE-2026-53361         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53362         HIGH         7.8   0.7% KEV
  │ ✘✘✔✘ CVE-2026-53365         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53366         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53368         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53381         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53383         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-53387         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53388         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53389         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53390         HIGH         8.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-53391         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-53392         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-53397         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-53400         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53401         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53402         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63794         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63796         HIGH         8.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-63797         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63801         HIGH         8.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-63802         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63803         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63804         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63805         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63806         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63807         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63809         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63812         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63814         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63815         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63816         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63817         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63818         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63819         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63823         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63824         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63827         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63828         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63829         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63831         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-63833         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63853         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63858         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63867         HIGH         8.2   0.3%   ·
  │ ✘✘✔✘ CVE-2026-63869         HIGH         7.6   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63870         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63875         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63879         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63881         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63883         HIGH         7.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63884         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63889         HIGH         8.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-63893         HIGH         8.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-63906         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63909         HIGH         8.1   0.6%   ·
  │ ✘✘✔✘ CVE-2026-63913         HIGH         8.2   1.0%   ·
  │ ✘✘✔✘ CVE-2026-63914         HIGH         7.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63915         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-63916         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-63917         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63919         HIGH         8.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-63920         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63921         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63925         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-63926         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63927         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63930         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63942         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63944         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-63945         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63946         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-63947         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-63952         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63954         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63968         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-63970         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63971         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63974         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-63975         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-63976         HIGH         8.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-63980         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-63985         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64001         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64002         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64003         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-64004         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64005         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64009         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64010         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64011         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64014         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64015         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64017         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64023         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64026         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64029         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64032         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64036         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64039         HIGH         7.7   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64048         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64051         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64073         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64076         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64077         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64078         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64082         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64084         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64085         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64086         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64088         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64093         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64095         HIGH         7.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64096         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64097         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64098         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64099         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64103         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64108         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64109         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64111         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64112         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64114         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64115         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64116         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64117         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64118         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64121         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64123         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64126         HIGH         7.3   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64133         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64134         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64137         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64138         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-64148         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64153         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64178         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64188         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64189         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64191         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64206         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64210         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64217         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64218         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64219         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64221         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64222         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64225         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64237         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64239         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64242         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64243         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64245         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64246         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64247         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64249         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64255         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64266         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64270         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64271         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64272         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64273         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64274         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64276         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64277         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64279         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64280         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64283         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64286         HIGH         8.2   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64287         HIGH         8.2   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64296         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64298         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64299         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64304         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64305         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64312         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64313         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-64315         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64317         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64318         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64322         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64323         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64324         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64329         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64330         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64333         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64340         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64341         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64342         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64343         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64344         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64346         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64348         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64352         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64361         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64362         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64363         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64364         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-64365         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64368         HIGH         8.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-64372         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64374         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-64375         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64377         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64378         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64379         HIGH         7.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64380         HIGH         8.2   0.4%   ·
  │ ✘✘✔✘ CVE-2026-64381         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64382         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-64388         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64389         HIGH         8.2   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64390         HIGH         8.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64394         HIGH         8.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64395         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-64396         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-64398         HIGH         8.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64400         HIGH         8.6   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64401         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64402         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64403         HIGH         7.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64406         HIGH         8.0   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64407         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64408         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64411         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64412         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64413         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64418         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64420         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64421         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64422         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64423         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64424         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64430         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64432         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64433         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64434         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64435         HIGH         8.2   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64436         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64437         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-64438         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64440         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64441         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64442         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64443         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64444         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64445         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64446         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64448         HIGH         8.2   0.5%   ·
  │ ✘✘✔✘ CVE-2026-64449         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64452         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64456         HIGH         7.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64463         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64468         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64469         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64475         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64481         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64496         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64510         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64524         HIGH         7.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64529         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64531         HIGH         7.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-64532         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64533         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64536         HIGH         8.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64539         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64540         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64543         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64545         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-64546         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64547         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64548         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64550         HIGH         7.3   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64552         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64554         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64555         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64556         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64557         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64560         HIGH         7.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-64561         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64562         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64563         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64567         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64568         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64570         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64574         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64576         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64577         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-64578         HIGH         8.2   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64580         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64581         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64582         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64583         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64584         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64585         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64586         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64598         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-64599         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64600         HIGH         7.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68085         HIGH         8.0   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68091         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68096         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68097         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-68098         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-68100         HIGH         8.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-68103         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68104         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68106         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68107         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68108         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68116         HIGH         7.9   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68118         HIGH         8.2   0.4%   ·
  │ ✘✘✔✘ CVE-2026-68119         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-68121         HIGH         7.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68125         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68129         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68131         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68138         HIGH         7.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68140         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68141         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68142         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68143         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68145         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68147         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68148         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68149         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68152         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68153         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68155         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-68157         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-68162         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68178         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68179         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68189         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68192         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-68196         HIGH         8.3   0.4%   ·
  │ ✘✘✔✘ CVE-2026-68198         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68199         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-68202         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68204         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68206         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68209         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68210         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68213         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68216         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68219         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68222         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68228         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68229         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68236         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68245         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68253         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68255         HIGH         7.7   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68257         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68258         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68260         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68262         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68263         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68266         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68273         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68284         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68287         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-68290         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68293         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68294         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68297         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68299         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68314         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68315         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68320         HIGH         7.3   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68323         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68326         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68329         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68335         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68338         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68340         HIGH         7.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68348         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68352         HIGH         8.3   0.4%   ·
  │ ✘✘✔✘ CVE-2026-68353         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68354         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68370         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68371         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68373         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68374         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68376         HIGH         8.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-68377         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68382         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68383         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68389         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68391         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68392         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68397         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68398         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68399         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68400         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68401         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68402         HIGH         7.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68404         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68409         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68414         HIGH         7.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68417         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68419         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68425         HIGH         7.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68427         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68432         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68433         HIGH         8.6   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68442         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68445         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68446         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68447         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68451         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68452         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68453         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68454         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68461         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68466         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68467         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68470         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68471         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68474         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68479         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72005         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72009         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72012         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72019         HIGH         7.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72021         HIGH         8.2   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72024         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72029         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-72035         HIGH         8.2   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72036         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72042         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72045         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72049         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72051         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72052         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72053         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72054         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72055         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72057         HIGH         8.2   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72061         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72066         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72067         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72071         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72072         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72089         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72099         HIGH         7.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-72102         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72105         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72107         HIGH         8.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72108         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72109         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72110         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72111         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72113         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72114         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72115         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-72116         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72119         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72120         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72121         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-72122         HIGH         7.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72123         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72124         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-72125         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72126         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72133         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72135         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72136         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72144         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72146         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72148         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-72149         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72157         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-72160         HIGH         8.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72162         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72164         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72165         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72170         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72171         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72172         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72175         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72181         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72195         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72196         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72197         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72198         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72202         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-72203         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72213         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72225         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72227         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-72231         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72232         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72233         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-72235         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-72242         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72243         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72244         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72247         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72250         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72252         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72253         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72254         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72255         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72261         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72262         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72282         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72284         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72297         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72298         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72301         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72302         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72304         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72310         HIGH         8.1   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72312         HIGH         7.9   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72314         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72315         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72330         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72334         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-72335         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72338         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72340         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72342         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72343         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72347         HIGH         7.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72350         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72352         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72369         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72371         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72373         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72374         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72375         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72378         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72380         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-72382         HIGH         8.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72383         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72389         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72390         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72395         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72397         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72400         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72404         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72405         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72406         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72409         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72410         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72416         HIGH         7.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72418         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72419         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72420         HIGH         8.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72423         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72425         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72427         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72434         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72435         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72438         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-72440         HIGH         7.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-72444         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72449         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72450         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72454         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72459         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72460         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72464         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-72469         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-72470         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72476         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72478         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72480         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72483         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72485         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72487         HIGH         7.7   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72488         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72489         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72492         HIGH         8.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-72499         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72502         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-74256         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74257         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74258         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74262         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74264         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74270         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74281         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-74282         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-74283         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74288         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74289         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74292         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74293         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74294         HIGH         7.3   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74295         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74296         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74297         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74300         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74302         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74305         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74312         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74313         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74314         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74317         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74321         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-74330         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74334         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74338         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74340         HIGH         8.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74341         HIGH         8.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74344         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74347         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74349         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74356         HIGH         7.4   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74359         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74363         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74365         HIGH         7.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74374         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74377         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74378         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74380         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74385         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-74387         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74388         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74390         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74397         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74405         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74407         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74408         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74410         HIGH         8.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74411         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74417         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74435         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-74438         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74440         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74443         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74444         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74446         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74450         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74453         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74454         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74456         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74461         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74465         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74467         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74469         HIGH         8.8   1.5%   ·
  │ ✘✘✔✘ CVE-2026-74470         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74471         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74479         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74481         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74482         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74485         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74488         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-74490         HIGH         8.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74492         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74496         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74497         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74506         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74507         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74508         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-74509         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74510         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74512         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74515         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74516         HIGH         8.2   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74518         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74519         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74522         HIGH         8.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-74523         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74527         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74530         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-74531         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-74533         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-74534         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74535         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74537         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74538         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74540         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-74541         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74544         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74548         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74549         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74550         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74551         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74557         HIGH         7.5   0.3%   ·
  │ ✘✘✔✘ CVE-2026-74563         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74564         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74565         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74567         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74572         HIGH         7.5   0.3%   ·
  │ ✘✘✔✘ CVE-2026-74574         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74575         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74578         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74579         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74580         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74582         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74583         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74584         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74589         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74590         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74592         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-74594         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74595         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74598         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74601         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74603         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74604         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74605         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74606         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74607         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74609         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74610         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74613         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74614         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74615         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74621         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74624         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74625         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74626         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74630         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74631         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74632         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74634         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74635         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74637         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74641         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74646         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74647         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74648         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74649         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-74651         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-74655         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74656         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74660         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74661         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74663         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74666         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74667         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74668         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74670         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74675         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74678         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74684         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74687         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74689         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74690         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74691         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-74692         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-74695         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74696         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74697         HIGH         8.2   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74700         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74701         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74704         HIGH         8.2   0.4%   ·
  │ ✘✘✔✘ CVE-2026-74710         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74711         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74713         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74714         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74715         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74717         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-74720         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74724         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74725         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74726         HIGH         7.3   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74733         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74736         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74739         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-74747         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74748         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80521         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80526         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80527         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-80536         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80540         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80541         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80547         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80548         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80549         HIGH         8.2   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80550         HIGH         7.9   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80552         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80553         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80555         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80556         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80559         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80560         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80565         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80568         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80569         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80570         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80572         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80574         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80576         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80578         HIGH         7.3   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80579         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80580         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80583         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80584         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80590         HIGH         8.6   0.6%   ·
  │ ✘✘✔✘ CVE-2026-80591         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80593         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80598         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80599         HIGH         8.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80601         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80613         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80619         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80622         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80628         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80631         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-80635         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80637         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-80644         HIGH         0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80645         HIGH         8.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80646         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-80649         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80653         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80662         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80663         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80664         HIGH         7.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80677         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80678         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80680         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80691         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80692         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-80700         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80702         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80706         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80707         HIGH         7.5   0.3%   ·
  │ ✘✘✔✘ CVE-2026-80709         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80710         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80716         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80717         HIGH         7.5   0.3%   ·
  │ ✘✘✔✘ CVE-2026-80718         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80721         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80722         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80731         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80732         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80737         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80738         HIGH         7.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80747         HIGH         8.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80752         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80754         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80914         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80921         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80928         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80931         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80932         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80933         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80935         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80937         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80944         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80947         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80952         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80967         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80971         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80977         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80978         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80979         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-80982         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80987         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-80989         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-80991         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80992         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80994         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-81000         HIGH         7.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-81001         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-81003         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-81007         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-81008         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-81010         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-81011         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-81012         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-81016         HIGH         7.7   0.2%   ·
  │ ✘✘✔✘ CVE-2026-81017         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89440         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89441         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89442         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89443         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89452         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89456         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89465         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89466         HIGH         7.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89469         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89470         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89471         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89472         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89476         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89477         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89480         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-89481         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-89483         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89487         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89488         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89489         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89493         HIGH         8.8   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89497         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89500         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89501         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89503         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89504         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89508         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89510         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89511         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89520         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89524         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-89528         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89540         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89544         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89545         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89547         HIGH         8.1   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89548         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89549         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89553         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89554         HIGH         8.2   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89557         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89559         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89560         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89561         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-89562         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89563         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89564         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89569         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-89573         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89574         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89579         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89580         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89583         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-89585         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89586         HIGH         8.2   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89587         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89588         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89594         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89596         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89597         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89599         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89601         HIGH         8.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89605         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89606         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89607         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89608         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89609         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89615         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89616         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-89617         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89622         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89624         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89626         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-89632         HIGH         8.2   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89638         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89640         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89647         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89648         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89657         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89663         HIGH         8.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89665         HIGH         8.2   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89680         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89682         HIGH         8.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89684         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89685         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-89690         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89691         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89696         HIGH         7.5   0.8%   ·
  │ ✘✘✔✘ CVE-2026-89699         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89704         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89705         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89706         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89707         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89709         HIGH         8.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89711         HIGH         8.2   0.4%   ·
  │ ✘✘✔✘ CVE-2026-89720         HIGH         7.7   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89723         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89724         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89725         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-89729         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-89731         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89733         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89736         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89738         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89741         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89742         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89743         HIGH         7.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89744         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89746         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89747         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89750         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89755         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89761         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89762         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89763         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89771         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89774         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-89777         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89781         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89782         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89789         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89792         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89793         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89795         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89799         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89801         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89803         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89806         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89808         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89810         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89811         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89814         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89818         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89819         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89823         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89832         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89838         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89840         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89844         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-89848         HIGH         8.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-89849         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-89854         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89856         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89860         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-89861         HIGH         8.1   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89863         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-89870         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89877         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89880         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89883         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89887         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89888         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89890         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89893         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89894         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89897         HIGH         7.5   0.3%   ·
  │ ✘✘✔✘ CVE-2026-89899         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89902         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89903         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89904         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89906         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89908         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89912         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89913         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89920         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89922         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89927         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89929         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89932         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89938         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89947         HIGH         8.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89951         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-89954         HIGH         8.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89957         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89959         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89960         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89961         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89965         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89968         HIGH         7.5   0.8%   ·
  │ ✘✘✔✘ CVE-2026-89973         HIGH         8.2   0.6%   ·
  │ ✘✘✔✘ CVE-2026-89979         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89988         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89992         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89995         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-89997         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89998         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89999         HIGH         8.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-90000         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-90002         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90003         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90007         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90013         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90016         HIGH         7.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-90017         HIGH         7.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-90018         HIGH         8.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-90022         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90025         HIGH         7.7   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90026         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90027         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90030         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90032         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90041         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-90044         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90045         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90057         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90062         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90067         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-90071         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90091         HIGH         8.0   0.4%   ·
  │ ✘✘✔✘ CVE-2026-90092         HIGH         8.0   0.4%   ·
  │ ✘✘✔✘ CVE-2026-90093         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90102         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-90103         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-90111         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90137         HIGH         7.7   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90141         HIGH         7.3   0.4%   ·
  │ ✘✘✔✘ CVE-2026-90143         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90146         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90149         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-90153         HIGH         8.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-90161         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90162         HIGH         8.8   0.6%   ·
  │ ✘✘✔✘ CVE-2026-90174         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90176         HIGH         8.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-90199         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90203         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90204         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90205         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90207         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90217         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90223         HIGH         7.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-90224         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-90225         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90227         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90228         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-90229         HIGH         7.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90231         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90234         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-90237         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90255         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-90256         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-90260         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90286         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90289         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90291         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90292         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90293         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-90294         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-90301         HIGH         8.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-90308         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90309         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90316         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90317         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90320         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90321         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90324         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90325         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90326         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90329         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-90341         HIGH         7.7   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90343         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90347         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90353         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-90357         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-90358         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90367         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-90372         HIGH         7.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-90379         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-90380         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-90383         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90387         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90388         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90392         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90398         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-90399         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90401         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90403         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-90407         HIGH         7.7   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90408         HIGH         7.7   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90419         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90435         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-92485         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92488         HIGH         7.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92504         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-92507         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92508         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92510         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-92511         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-92522         HIGH         7.3   0.1%   ·
  │ ✘✘✔✘ CVE-2026-92525         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93037         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93039         HIGH         7.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93042         HIGH         8.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-93046         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93054         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93063         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93095         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93105         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93107         HIGH         8.2   0.5%   ·
  │ ✘✘✔✘ CVE-2026-93116         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93122         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93125         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93137         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93138         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93144         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93148         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93151         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-93154         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93165         HIGH         7.7   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93170         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93175         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93176         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93177         HIGH         7.3   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93178         HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93189         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-93190         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93192         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93196         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93203         HIGH         7.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-93221         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-93229         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93237         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93250         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93260         HIGH         7.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93262         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93280         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-93282         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-93287         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93288         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93782         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93786         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-93787         HIGH         8.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-93790         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93793         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93796         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93798         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93799         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93801         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93806         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-93810         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93813         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93816         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93817         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93826         HIGH         7.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93827         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-93830         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-97409         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97415         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97417         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-97421         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97428         HIGH         7.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97429         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97433         HIGH         8.2   0.3%   ·
  │ ✘✘✔✘ CVE-2026-97437         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97438         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97442         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-97444         HIGH         7.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97445         HIGH         7.7   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97448         HIGH         7.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97450         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97451         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97452         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97454         HIGH         7.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97455         HIGH         8.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97474         HIGH         7.4   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97478         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97496         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97497         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97508         HIGH         7.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97509         HIGH         8.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97513         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97520         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97523         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-97524         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-97527         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-97528         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-97531         HIGH         7.5   0.3%   ·
  │ ✘✘✔✘ CVE-2026-97536         HIGH         7.5   0.3%   ·
  │ ✘✘✔✘ CVE-2026-97555         HIGH         8.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-97557         HIGH         7.5   0.7%   ·
  │ ✘✘✔✘ CVE-2026-97562         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-97573         HIGH         8.1   0.6%   ·
  │ ✘✘✔✘ CVE-2026-97575         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97576         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97577         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97578         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97579         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97583         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-97584         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97594         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97595         HIGH         7.5   0.3%   ·
  │ ✘✘✔✘ CVE-2026-97602         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97608         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97609         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97611         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97612         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97910         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97926         HIGH         7.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97931         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97940         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97953         HIGH         7.0   0.4%   ·
  │ ✘✘✔✘ CVE-2026-97957         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97990         HIGH         7.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97991         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98017         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98023         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98027         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98029         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98030         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98041         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98052         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98056         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-98069         HIGH         8.1   0.6%   ·
  │ ✘✘✔✘ CVE-2026-98070         HIGH         8.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-98073         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98083         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98096         HIGH         7.4   0.5%   ·
  │ ✘✘✔✘ CVE-2026-98108         HIGH         7.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98115         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-98116         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98122         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98130         HIGH         8.1   0.6%   ·
  │ ✘✘✔✘ CVE-2026-98154         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98156         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98164         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98169         HIGH         7.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-98171         HIGH         8.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-98173         HIGH         7.5   0.3%   ·
  │ ✘✘✔✘ CVE-2026-98174         HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2026-98175         HIGH         7.5   0.3%   ·
  │ ✘✘✔✘ CVE-2026-98180         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98197         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98216         HIGH         7.1   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98229         HIGH         7.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98230         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98239         HIGH         8.1   0.5%   ·
  │ ✘✘✔✘ CVE-2026-98241         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98251         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98252         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98253         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98254         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98257         HIGH         7.5   0.5%   ·
  │ ✘✘✔✘ CVE-2026-98260         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98261         HIGH         8.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-98276         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98282         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98283         HIGH         8.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98290         HIGH         7.5   0.3%   ·
  │ ✘✘✔✘ CVE-2026-98311         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98320         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98330         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98331         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98339         HIGH         8.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-98341         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98348         HIGH         7.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-98349         HIGH         7.1   0.3%   ·
  │ ✘✘✔✘ CVE-2026-98357         HIGH         8.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-98359         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98360         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98364         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98366         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98367         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98368         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98369         HIGH         7.8   0.1%   ·
  │ ✘✘✔✘ CVE-2015-7837          MEDIUM       5.5   0.4%   ·
  │ ✘✘✔✘ CVE-2016-8660          MEDIUM       5.5   0.4%   ·
  │ ✘✘✔✘ CVE-2017-0537          MEDIUM       4.7   1.0%   ·
  │ ✘✘✔✘ CVE-2017-13693         MEDIUM       5.5   0.4%   ·
  │ ✘✘✔✘ CVE-2018-1121          MEDIUM       5.9   4.2%   ·
  │ ✘✘✔✘ CVE-2018-12928         MEDIUM       5.5   0.4%   ·
  │ ✘✘✔✘ CVE-2018-12929         MEDIUM       5.5   0.4%   ·
  │ ✘✘✔✘ CVE-2018-17977         MEDIUM       4.9   0.4%   ·
  │ ✘✘✔✘ CVE-2019-15213         MEDIUM       4.9   0.7%   ·
  │ ✘✘✔✘ CVE-2020-14304         MEDIUM       4.4   0.4%   ·
  │ ✘✘✔✘ CVE-2021-3714          MEDIUM       5.9   1.5%   ·
  │ ✘✘✔✘ CVE-2022-0480          MEDIUM       5.5   0.3%   ·
  │ ✘✘✔✘ CVE-2022-41848         MEDIUM       4.2   0.3%   ·
  │ ✘✘✔✘ CVE-2022-44034         MEDIUM       6.4   0.3%   ·
  │ ✘✘✔✘ CVE-2022-4543          MEDIUM       5.5   1.0%   ·
  │ ✘✘✔✘ CVE-2022-48846         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2022-48929         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2022-49940         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2022-50230         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2022-50232         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2022-50380         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2023-0160          MEDIUM       5.5   0.3%   ·
  │ ✘✘✔✘ CVE-2023-1193          MEDIUM       6.5   1.0%   ·
  │ ✘✘✔✘ CVE-2023-20585         MEDIUM       5.6   0.1%   ·
  │ ✘✘✔✘ CVE-2023-31082         MEDIUM       5.5   0.4%   ·
  │ ✘✘✔✘ CVE-2023-53642         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2023-54105         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2023-54190         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2023-6238          MEDIUM       6.7   0.3%   ·
  │ ✘✘✔✘ CVE-2024-0564          MEDIUM       6.5   0.6%   ·
  │ ✘✘✔✘ CVE-2024-14027         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-27025         MEDIUM       5.5   0.3%   ·
  │ ✘✘✔✘ CVE-2024-35895         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-35995         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-42107         MEDIUM       4.7   0.2%   ·
  │ ✘✘✔✘ CVE-2024-42139         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-46742         MEDIUM       5.5   0.3%   ·
  │ ✘✘✔✘ CVE-2024-47729         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-49908         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-49910         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-49916         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-49970         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-49990         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-50003         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-50102         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-53056         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-53064         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-56544         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-56617         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-56702         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-56712         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-57809         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-57922         MEDIUM       5.5   0.3%   ·
  │ ✘✘✔✘ CVE-2024-58012         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2024-58095         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-21696         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-21752         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-21907         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-22002         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-22127         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-23131         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-23135         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-23162         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-37743         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-37746         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-37747         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-37806         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-37807         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-37833         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-37834         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-37870         MEDIUM       5.5   0.3%   ·
  │ ✘✘✔✘ CVE-2025-37880         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-37907         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-38029         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38036         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38038         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38041         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38042         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38096         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38132         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38140         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38188         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38199         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-38203         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38205         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38207         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38237         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38272         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38311         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-38353         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-38359         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-38360         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38438         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38597         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-38605         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-38621         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-39754         MEDIUM       4.7   0.1%   ·
  │ ✘✘✔✘ CVE-2025-39762         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2025-39833         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-39910         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-39925         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-40086         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40098         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40102         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40247         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40332         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40335         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40338         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40340         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40355         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68188         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68193         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68196         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68209         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68211         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-68230         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68236         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68251         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68281         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68296         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68309         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68318         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68324         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68333         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-68338         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68353         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68356         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68376         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68729         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68768         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68781         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-68802         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-71115         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-71223         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-71227         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-71285         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-71290         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-71293         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-71299         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-71313         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2025-71315         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-100070        MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-100071        MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-100072        MEDIUM       0.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-100074        MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-100076        MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-100077        MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-100078        MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-100079        MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23017         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-23137         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23152         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23181         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-23196         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23201         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23217         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23247         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23259         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23265         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23346         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23348         MEDIUM       4.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23371         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23377         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23385         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23469         MEDIUM       4.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-23472         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-31410         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-31420         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-31461         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-31462         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-31526         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-31531         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-31537         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-31560         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-31579         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-31592         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-31692         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-31777         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43010         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43021         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43022         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43034         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43045         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43053         MEDIUM       4.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43115         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43118         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43127         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43131         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43161         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43165         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43191         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43195         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43204         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43216         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43219         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43220         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43228         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43229         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43234         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43240         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43243         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43267         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43292         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43294         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43298         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43299         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43301         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43305         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43306         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43308         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43309         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43310         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43311         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43331         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43344         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43398         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43400         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43410         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43416         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43443         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-43463         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43474         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-43485         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-45850         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-45897         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-45901         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-45930         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-45934         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-45940         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-45949         MEDIUM       4.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-45961         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-45963         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46014         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46032         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-46059         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-46066         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-46071         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-46147         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-46148         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-46153         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46158         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46170         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46171         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-46245         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46252         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46272         MEDIUM       4.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46302         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-46315         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52913         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52916         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52921         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52926         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52928         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52930         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52937         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52939         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52941         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52944         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52948         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52972         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-52994         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53017         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53018         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53027         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53080         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53102         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53103         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53104         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53106         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53107         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53108         MEDIUM       4.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53113         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53134         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53135         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53139         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53140         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53142         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53144         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53150         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53154         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53158         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53163         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53167         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53168         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53177         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53181         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53190         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53196         MEDIUM       6.8   0.3%   ·
  │ ✘✘✔✘ CVE-2026-53207         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53208         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53210         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53213         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53214         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53218         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53219         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53220         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53226         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53227         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53236         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53237         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53238         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53245         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53249         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53251         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53252         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53258         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53261         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53263         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53269         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53274         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53285         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53292         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53297         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53313         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53317         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53325         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53327         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53331         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53332         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53336         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53337         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53339         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53343         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53345         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53347         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53349         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53350         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53352         MEDIUM       4.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53353         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53377         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-53382         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53385         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53393         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53403         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63798         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63810         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63811         MEDIUM       0.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63821         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63822         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63826         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63834         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63835         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63836         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63868         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63871         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63876         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63877         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63882         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63890         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63891         MEDIUM       0.0   0.3%   ·
  │ ✘✘✔✘ CVE-2026-63892         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63895         MEDIUM       0.0   0.3%   ·
  │ ✘✘✔✘ CVE-2026-63896         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63897         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63898         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63899         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63900         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63901         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63902         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63903         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63904         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63905         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63908         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63928         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63931         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63933         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63934         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63943         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63948         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63949         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63956         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63957         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63958         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63959         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63960         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63961         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63962         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63963         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63964         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63967         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63969         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63973         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63983         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-63990         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63991         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-63999         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64006         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64012         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64022         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64038         MEDIUM       4.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64052         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64060         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64064         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64070         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64079         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64083         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64087         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64090         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64092         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64094         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64127         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64128         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64131         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64135         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64144         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64146         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64147         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64154         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64155         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64163         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64165         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64166         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64168         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64170         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64173         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64174         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64177         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64179         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64180         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64182         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64183         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64184         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64185         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64187         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64190         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64192         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64205         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64212         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64213         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64214         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64220         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64227         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64231         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64233         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64234         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64240         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64241         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64244         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64254         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64256         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64275         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64289         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64294         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64297         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64301         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64306         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64316         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64321         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64326         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64331         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64332         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64334         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64335         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64336         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64337         MEDIUM       5.5   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64338         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64345         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64347         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64350         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64351         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64358         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64359         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64360         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64369         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64370         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64371         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64373         MEDIUM       4.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64376         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64404         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64405         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64409         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64417         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64419         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64425         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64428         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64429         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-64454         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64455         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64458         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64461         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64462         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64465         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64470         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64471         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64472         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64473         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64474         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64476         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64478         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64479         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64480         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64482         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64483         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64484         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64486         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64487         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64488         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64489         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64493         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64494         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64495         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64497         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64500         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64503         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64504         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64505         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64507         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64508         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64511         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64512         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64513         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64514         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64518         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64525         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64527         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64528         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64537         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64538         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64542         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64544         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64549         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64553         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64565         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64569         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64571         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64572         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64573         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64579         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64590         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64593         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64594         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64602         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64603         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-64604         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68081         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68084         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68086         MEDIUM       0.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68088         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68090         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68093         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68099         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68102         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68105         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68109         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68110         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68111         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68112         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68113         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68114         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68115         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68126         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68130         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68132         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68135         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68139         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68146         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68150         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68151         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68164         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68165         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68166         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68169         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68175         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68176         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68180         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68181         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68182         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68183         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68184         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68186         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68187         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68188         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68190         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68193         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68194         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68195         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68197         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68203         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68205         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68207         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68211         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68212         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68214         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68215         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68217         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68218         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68220         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68221         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68223         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68225         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68226         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68227         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68231         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68233         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68234         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68235         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68238         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68241         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68242         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68243         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68244         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68246         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68247         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68248         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68249         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68250         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68251         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68252         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68254         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68256         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68259         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68261         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68269         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68271         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68272         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68277         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68278         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68279         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68280         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68281         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68286         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68288         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68289         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68291         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68301         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68303         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68304         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68306         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68308         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68309         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68310         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68312         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68313         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68317         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68318         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68319         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68322         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68324         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68325         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68327         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68328         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68331         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68333         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68336         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68337         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68339         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68346         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68349         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68350         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68351         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68355         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68357         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68359         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68360         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68361         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68362         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68363         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68365         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68366         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68367         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68368         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68369         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68372         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68386         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68395         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68396         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68403         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68405         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68406         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68407         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68408         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68410         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68411         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68412         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68413         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68416         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68418         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68422         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68428         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68429         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68430         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68436         MEDIUM       0.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68437         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68439         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68441         MEDIUM       0.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-68443         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68444         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68448         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68449         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68450         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68456         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68459         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68460         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68469         MEDIUM       0.0   0.3%   ·
  │ ✘✘✔✘ CVE-2026-68475         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68478         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-68480         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72004         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72007         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72010         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72013         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72015         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72017         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72022         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72023         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72025         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72028         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72030         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72031         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72037         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72038         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72039         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72040         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72047         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72048         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72056         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72058         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72059         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72062         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72063         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72068         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72070         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72073         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72074         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72075         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72076         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72077         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72078         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72079         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72081         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72082         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72086         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72087         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72088         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72096         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72097         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72106         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72117         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72118         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72127         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72132         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72138         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72140         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72142         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72147         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72150         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72152         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72153         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72155         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72156         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72158         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72159         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72161         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72163         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72166         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72167         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72168         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72174         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72176         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72177         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72179         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72182         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72193         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72205         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72212         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72214         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72215         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72216         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72218         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72219         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72223         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72224         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72228         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72229         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72230         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72236         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72237         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72238         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72240         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72241         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72245         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72256         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72257         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72258         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72259         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72260         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72264         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72265         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72266         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72267         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72268         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72269         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72270         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72271         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72272         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72273         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72274         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72275         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72276         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72290         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72300         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72305         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72306         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72307         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72308         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72316         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72321         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72324         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72325         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72326         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72327         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72336         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72337         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72341         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72349         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72361         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72362         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72376         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72379         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72384         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72391         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72392         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72396         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72402         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72413         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72414         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72424         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72428         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72430         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72433         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72437         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72439         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72441         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72443         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72447         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72448         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72467         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72474         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72479         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72481         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72484         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72486         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-72501         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74261         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74263         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74265         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74271         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74272         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74273         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74276         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74278         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74284         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74290         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74291         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74303         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74307         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74308         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74318         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74320         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74324         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74327         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74329         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74331         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74337         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74339         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74342         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74346         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74348         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74351         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74362         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74368         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74373         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74375         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74379         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74381         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74382         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74386         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74389         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74391         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74395         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74399         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74402         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74416         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74424         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74426         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74432         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74441         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74445         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74448         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74455         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74457         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74458         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74459         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74460         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74463         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74464         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74466         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74468         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74472         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74483         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74484         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74487         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74494         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74498         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74499         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74500         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74501         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74502         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74505         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74514         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74525         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74532         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74536         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74543         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74546         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74547         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74552         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74553         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74555         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74558         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74559         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74560         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74566         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74571         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74577         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74585         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74599         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74600         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74602         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74618         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74619         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74620         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74622         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74623         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74636         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74638         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74650         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74653         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74654         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74657         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74658         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74659         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74664         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74671         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74672         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74673         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74676         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74677         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74679         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74680         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74682         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74683         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74693         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74694         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74718         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74719         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74722         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74729         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74734         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74735         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74740         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-74754         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80529         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80534         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80539         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80542         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80562         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80566         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80567         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80573         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80581         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80594         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80595         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80597         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80602         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80605         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80607         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80611         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80616         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80618         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80620         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80626         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80659         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80667         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80669         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80686         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80695         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80703         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80715         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80727         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80730         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80733         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80739         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80742         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80743         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80744         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80755         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80756         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80757         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80761         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80762         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80763         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80764         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80765         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80766         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80767         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80768         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80770         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80771         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80772         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80774         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80780         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80781         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80782         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80783         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80784         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80785         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80786         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80788         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80789         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80790         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80791         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80792         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80793         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80794         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80795         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80796         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80797         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80798         MEDIUM       0.0   0.3%   ·
  │ ✘✘✔✘ CVE-2026-80799         MEDIUM       0.0   0.3%   ·
  │ ✘✘✔✘ CVE-2026-80800         MEDIUM       0.0   0.3%   ·
  │ ✘✘✔✘ CVE-2026-80801         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80802         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80803         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80805         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80806         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80807         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80808         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80809         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80812         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80814         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80815         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80817         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80819         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80820         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80822         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80823         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80824         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80825         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80826         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80827         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80828         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80829         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80830         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80831         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80832         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80833         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80834         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80835         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80836         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80837         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80838         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80839         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80840         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80841         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80842         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80843         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80844         MEDIUM       0.0   0.4%   ·
  │ ✘✘✔✘ CVE-2026-80846         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80847         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80848         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80849         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80850         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80851         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80852         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80854         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80855         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80856         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80861         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80863         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80864         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80865         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80866         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80867         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80870         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80872         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80875         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80876         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80877         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80878         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80879         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80880         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80881         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80883         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80884         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80886         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80887         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80888         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80889         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80890         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80891         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80892         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80893         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80899         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80901         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80902         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80904         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80905         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80906         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80907         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80908         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80909         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80910         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80911         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80912         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80913         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80916         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80917         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80918         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80920         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80922         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80923         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80925         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80930         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80938         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80939         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80941         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80948         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80949         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80951         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80963         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80964         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80965         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80966         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80968         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80969         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80972         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80973         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80974         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80983         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80984         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80988         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80990         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80996         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80999         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-81005         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-81013         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-81014         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89437         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89438         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89439         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89444         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89451         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89457         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89458         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89460         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89461         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89462         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89463         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89464         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89467         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89468         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89473         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89474         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89475         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89484         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89490         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89491         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89496         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89498         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89502         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89512         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89515         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89525         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89527         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89531         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89539         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89543         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89552         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89556         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89565         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89566         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89567         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89572         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89575         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89576         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89582         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89595         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89598         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89603         MEDIUM       0.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-89604         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89618         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89621         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89623         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89625         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89627         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89628         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89642         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89644         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89645         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89666         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89673         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89693         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89694         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89698         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89710         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89717         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89718         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89719         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89722         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89726         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89730         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89732         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89735         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89740         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89749         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89751         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89752         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89753         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89756         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89757         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89759         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89765         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89773         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89776         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89780         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89784         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89785         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89787         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89794         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89796         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89797         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89800         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89802         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89809         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89812         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89813         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89816         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89817         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89821         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89822         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89824         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89827         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89830         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89833         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89834         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89835         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89837         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89839         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89842         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89843         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89845         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89850         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89851         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89852         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89853         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89855         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89858         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89859         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89862         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89864         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89865         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89866         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89868         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89871         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89872         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89874         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89876         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89878         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89879         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89881         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89884         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89891         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89892         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89895         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89896         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89900         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89901         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89909         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89921         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89923         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89924         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89925         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89926         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89931         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89933         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89934         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89936         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89937         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89939         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89944         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89945         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89946         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89948         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89949         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89950         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89952         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89953         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89955         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89956         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89958         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89962         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89964         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89975         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89982         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89983         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89984         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89987         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89989         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89993         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-89996         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90015         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90019         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90020         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90021         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90023         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90024         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90029         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90031         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90033         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90034         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90035         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90053         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90054         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90055         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90056         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90058         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90060         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90061         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90063         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90066         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90068         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90070         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90072         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90073         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90074         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90075         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90076         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90078         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90081         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90083         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90084         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90086         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90087         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90088         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90090         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90097         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90098         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90099         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90101         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90105         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90106         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90107         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90108         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90109         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90112         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90114         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90115         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90116         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90119         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90122         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90124         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90125         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90126         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90128         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90130         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90135         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90138         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90139         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90140         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90144         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90148         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90150         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90152         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90154         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90155         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90156         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90157         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90158         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90159         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90160         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90166         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90167         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90169         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90170         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90175         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90178         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90179         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90180         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90182         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90183         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90184         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90185         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90186         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90187         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90188         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90189         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90190         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90194         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90196         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90198         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90200         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90202         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90206         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90208         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90209         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90213         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90214         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90216         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90218         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90219         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90220         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90221         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90222         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90226         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90232         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90245         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90247         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90248         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90249         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90250         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90251         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90253         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90254         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90257         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90259         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90261         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90262         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90263         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90264         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90265         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90267         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90273         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90274         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90275         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90279         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90280         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90281         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90282         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90283         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90284         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90285         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90287         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90290         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90295         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90296         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90297         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90298         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90300         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90302         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90303         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90307         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90311         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90313         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90314         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90315         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90318         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90319         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90322         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90327         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90328         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90330         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90333         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90334         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90335         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90336         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90337         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90345         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90346         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90348         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90351         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90352         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90354         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90359         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90360         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90361         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90362         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90363         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90364         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90365         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90366         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90368         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90370         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90374         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90375         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90378         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90382         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90385         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90386         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90389         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90390         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90391         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90393         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90394         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90395         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90397         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90400         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90404         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90410         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90411         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90415         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90416         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90417         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90418         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90420         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90421         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90422         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90431         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90433         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-90434         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92476         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92477         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92480         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92481         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92482         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92484         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92490         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92493         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92494         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92495         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92496         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92497         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92498         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92499         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92500         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92501         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92502         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92503         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92506         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92509         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92512         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92514         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92519         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92520         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92521         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92523         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-92524         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93040         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93041         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93047         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93048         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93049         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93050         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93051         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93052         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93053         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93055         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93056         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93058         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93061         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93062         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93064         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93065         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93067         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93072         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93073         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93081         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93083         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93084         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93085         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93086         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93089         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93090         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93091         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93092         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93093         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93097         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93098         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93099         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93100         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93101         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93102         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93103         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93104         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93108         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93109         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93110         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93113         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93114         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93115         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93117         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93118         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93119         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93120         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93123         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93126         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93128         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93129         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93130         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93131         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93136         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93140         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93141         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93142         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93145         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93146         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93149         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93150         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93152         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93155         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93156         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93158         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93159         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93160         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93161         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93162         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93163         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93167         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93168         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93172         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93174         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93179         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93180         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93181         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93182         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93183         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93184         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93185         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93186         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93188         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93191         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93199         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93200         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93202         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93204         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93205         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93206         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93208         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93209         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93210         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93211         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93213         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93214         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93215         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93216         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93219         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93222         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93223         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93226         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93230         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93231         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93234         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93235         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93236         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93238         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93239         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93240         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93241         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93242         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93243         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93244         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93245         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93247         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93251         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93252         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93256         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93259         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93261         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93264         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93268         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93269         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93271         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93272         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93273         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93274         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93275         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93278         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93279         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93281         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93283         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93285         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93286         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93781         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93783         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93784         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93785         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93788         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93789         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93791         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93792         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93794         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93795         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93797         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93800         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93802         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93803         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93804         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93805         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93807         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93808         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93809         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93811         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93812         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93814         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93815         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93818         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93819         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93820         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93821         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93822         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93823         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93824         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93825         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93828         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-93829         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97407         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97408         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97410         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97411         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97412         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97414         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97416         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97418         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97419         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97420         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97422         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97423         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97424         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97425         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97426         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97427         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97430         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97431         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97432         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97434         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97435         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97436         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97439         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97440         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97441         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97443         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97446         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97447         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97449         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97453         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97456         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97472         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97473         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97475         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97476         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97477         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97479         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97480         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97481         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97482         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97483         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97484         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97485         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97486         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97487         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97488         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97489         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97490         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97491         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97492         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97493         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97494         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97495         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97498         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97499         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97500         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97501         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97502         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97503         MEDIUM       0.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97504         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97505         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97506         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97507         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97510         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97511         MEDIUM       0.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97512         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97514         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97515         MEDIUM       0.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97516         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97517         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97518         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97519         MEDIUM       0.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-97521         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97522         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97529         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97530         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97532         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97534         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97535         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97537         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97539         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97540         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97541         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97542         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97545         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97552         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97554         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97556         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97558         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97559         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97560         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97561         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97563         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97564         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97565         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97566         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97567         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97568         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97572         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97581         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97582         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97587         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97592         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97596         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97597         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97598         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97599         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97600         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97601         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97603         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97604         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97605         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97606         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97607         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97613         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97615         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97616         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97619         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97620         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97899         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97900         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97901         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97902         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97904         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97905         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97906         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97907         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97908         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97909         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97915         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97916         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97917         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97918         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97919         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97920         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97921         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97922         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97923         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97924         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97925         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97927         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97929         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97930         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97933         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97934         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97935         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97936         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97938         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97939         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97945         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97948         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97949         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97950         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97951         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97952         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97954         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97958         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97959         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97960         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97961         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97962         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97963         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97964         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97965         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97966         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97969         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97970         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97973         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97975         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97977         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97978         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97979         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97981         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97982         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97984         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97985         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97986         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97987         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97988         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97989         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97992         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97993         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97994         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97995         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97997         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-97998         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98003         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98006         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98007         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98008         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98009         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98010         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98011         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98012         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98013         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98014         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98015         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98016         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98018         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98019         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98020         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98021         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98022         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98024         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98025         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98026         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98028         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98031         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98032         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98033         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98034         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98037         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98038         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98039         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98043         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98044         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98046         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98051         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98054         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98055         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98058         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98063         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98064         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98066         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98067         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98068         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98071         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98072         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98074         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98075         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98076         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98077         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98078         MEDIUM       4.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98079         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98080         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98081         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98082         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98084         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98085         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98086         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98087         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98088         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98089         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98090         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98091         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98092         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98094         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98095         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98097         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98098         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98099         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98101         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98102         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98103         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98104         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98107         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98109         MEDIUM       4.7   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98111         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98113         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98114         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98121         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98123         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98124         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98125         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98126         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98127         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98128         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98129         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98131         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98134         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98142         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98148         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98151         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98152         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98155         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98157         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98158         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98159         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98160         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98161         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98162         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✘ CVE-2026-98167         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98168         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98170         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98172         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98176         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98177         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98179         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98181         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98182         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98185         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98186         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98187         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98188         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98189         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98190         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98191         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98192         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98193         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98194         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98195         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98196         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98198         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98199         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98200         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98201         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98202         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98203         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98204         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98205         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98206         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98207         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98208         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98209         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98210         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98211         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98212         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98213         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98217         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98218         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98221         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98222         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98227         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98231         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98232         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98233         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98234         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98235         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98236         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98237         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98238         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98245         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98246         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98247         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98248         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98249         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98255         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98262         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98263         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98264         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98265         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98266         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98269         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98270         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98271         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98272         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98273         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98275         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98279         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98284         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98285         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98286         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98287         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98288         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98289         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98292         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98293         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98294         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98295         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98297         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98298         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98299         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98300         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98301         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98302         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98303         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98304         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98306         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98307         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98308         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98309         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98312         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98313         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98314         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98316         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98317         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98319         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98321         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98322         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98325         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98326         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98327         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98328         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98329         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98332         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98333         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98334         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98335         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98336         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98337         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98338         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98340         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98342         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98343         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98344         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98345         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98347         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98351         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98352         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98353         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98354         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98355         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98358         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98362         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98363         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98370         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98373         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98374         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98375         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98377         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98378         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98379         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98380         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98381         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98382         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98383         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98384         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98386         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98387         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98388         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98389         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98393         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98394         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98398         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98399         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98400         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98401         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98402         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98403         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98404         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98406         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98407         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98409         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98410         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98413         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98416         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98417         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98419         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98420         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98421         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98422         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98423         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98424         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98425         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98426         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98427         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98428         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98429         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98430         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-98431         MEDIUM       0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2020-35501         LOW          3.6   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40003         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40065         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40097         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40136         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2025-40146         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80623         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80624         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80627         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80629         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80636         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80643         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80647         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80650         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80652         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80654         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80660         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80676         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80679         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80689         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80698         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80704         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80708         LOW          0.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-80711         LOW          0.0   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/login@1%3A4.13%2Bdfsg1-4ubuntu3.2
  │ OGTV
  │ ✘✘✔✔ CVE-2024-56433         LOW          3.6   0.4%   ·  ↳ V:UB:CVE-2024-56433
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/mount@2.39.3-9ubuntu6.5
  │ OGTV
  │ ✘✘✔✘ CVE-2026-53612         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53614         HIGH         7.0   0.1%   ·
  │ ✘✘✔✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✘✔✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✘✔✘ CVE-2026-27456         MEDIUM       4.7   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/ncurses-base@6.4%2B20240113-1ubuntu2
  │ OGTV
  │ ✘✘✔✔ CVE-2025-69720         CRITICAL     9.8   0.4%   ·  ↳ V:UB:CVE-2025-69720
  │ ✘✘✔✘ CVE-2025-6141          MEDIUM       4.8   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/ncurses-bin@6.4%2B20240113-1ubuntu2
  │ OGTV
  │ ✘✘✔✔ CVE-2025-69720         CRITICAL     9.8   0.4%   ·  ↳ V:UB:CVE-2025-69720
  │ ✘✘✔✔ CVE-2025-6141          MEDIUM       4.8   0.2%   ·  ↳ V:UB:CVE-2025-6141
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/openssl@3.0.13-0ubuntu3.12
  │ OGTV
  │ ✔✘✘✘ CVE-2026-63073         CRITICAL     9.8   1.2%   ·  ↳ O:USN-8678-1
  │ ✔✔✔✔ CVE-2026-75803         CRITICAL     9.1   0.2%   ·  ↳ O:UBUNTU-CVE-2026-75803,USN-8678-1 | V:UB:CVE-2026-75803
  │ ✔✘✘✘ CVE-2026-14456         HIGH         7.5   0.7%   ·  ↳ O:USN-8678-1
  │ ✔✘✘✘ CVE-2026-14457         HIGH         7.5   1.0%   ·  ↳ O:USN-8678-1
  │ ✔✘✘✘ CVE-2026-18798         HIGH         7.5   1.5%   ·  ↳ O:USN-8678-1
  │ ✔✔✔✔ CVE-2026-54874         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-54874,USN-8678-1 | V:UB:CVE-2026-54874
  │ ✔✔✔✔ CVE-2026-63072         HIGH         7.5   0.9%   ·  ↳ O:UBUNTU-CVE-2026-63072,USN-8678-1 | V:UB:CVE-2026-63072
  │ ✔✘✘✘ CVE-2026-63075         HIGH         7.5   0.8%   ·  ↳ O:USN-8678-1
  │ ✔✔✔✔ CVE-2026-63076         HIGH         7.5   1.6%   ·  ↳ O:UBUNTU-CVE-2026-63076,USN-8678-1 | V:UB:CVE-2026-63076
  │ ✔✘✘✘ CVE-2026-72897         HIGH         7.5   0.3%   ·  ↳ O:USN-8847-1
  │ ✔✔✔✘ CVE-2026-84782         HIGH         8.2   0.4%   ·  ↳ O:UBUNTU-CVE-2026-84782,USN-8847-1
  │ ✔✘✘✘ CVE-2026-84784         HIGH         7.5   0.4%   ·  ↳ O:USN-8847-1
  │ ✔✔✔✘ CVE-2026-35189         MEDIUM       5.3   0.3%   ·  ↳ O:UBUNTU-CVE-2026-35189,USN-8847-1
  │ ✔✔✔✔ CVE-2026-63074         MEDIUM       5.9   0.6%   ·  ↳ O:UBUNTU-CVE-2026-63074,USN-8678-1 | V:UB:CVE-2026-63074
  │ ✔✘✘✘ CVE-2026-75804         MEDIUM       5.3   0.4%   ·  ↳ O:USN-8847-1
  │ ✔✔✔✘ CVE-2026-75805         MEDIUM       5.3   0.2%   ·  ↳ O:UBUNTU-CVE-2026-75805,USN-8847-1
  │ ✔✔✔✘ CVE-2026-75806         MEDIUM       5.3   0.4%   ·  ↳ O:UBUNTU-CVE-2026-75806,USN-8847-1
  │ ✔✘✘✘ CVE-2026-35191         LOW          3.7   0.4%   ·  ↳ O:USN-8847-1
  │ ✔✔✔✘ CVE-2026-54872         LOW          3.7   0.3%   ·  ↳ O:UBUNTU-CVE-2026-54872,USN-8847-1
  │ ✔✘✘✘ CVE-2026-54875         LOW          3.7   0.3%   ·  ↳ O:USN-8847-1
  │ ✔✔✔✘ CVE-2026-77696         LOW          3.7   0.2%   ·  ↳ O:UBUNTU-CVE-2026-77696,USN-8847-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/passwd@1%3A4.13%2Bdfsg1-4ubuntu3.2
  │ OGTV
  │ ✘✘✔✔ CVE-2024-56433         LOW          3.6   0.4%   ·  ↳ V:UB:CVE-2024-56433
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/patch@2.7.6-7build3
  │ OGTV
  │ ✔✔✔✔ CVE-2018-6952          HIGH         7.5   8.2%   ·  ↳ O:UBUNTU-CVE-2018-6952 | V:UB:CVE-2018-6952
  │ ✔✔✔✔ CVE-2019-20633         MEDIUM       5.5   1.0%   ·  ↳ O:UBUNTU-CVE-2019-20633 | V:UB:CVE-2019-20633
  │ ✔✔✔✔ CVE-2021-45261         MEDIUM       5.5   0.8%   ·  ↳ O:UBUNTU-CVE-2021-45261 | V:UB:CVE-2021-45261
  │ ✔✔✔✔ CVE-2026-56288         MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-56288 | V:UB:CVE-2026-56289
  │ ✔✔✔✔ CVE-2026-56289         MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-56289 | V:UB:CVE-2026-56289
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/perl@5.38.2-3.2ubuntu0.3
  │ OGTV
  │ ✔✔✔✔ CVE-2026-12087         CRITICAL     9.1   0.4%   ·  ↳ O:UBUNTU-CVE-2026-12087,USN-8684-1 | V:UB:CVE-2026-12087
  │ ✔✔✔✔ CVE-2026-13221         CRITICAL     9.1   0.4%   ·  ↳ O:UBUNTU-CVE-2026-13221,USN-8684-1 | V:UB:CVE-2026-13221
  │ ✔✔✔✔ CVE-2026-57433         CRITICAL     9.8   0.4%   ·  ↳ O:UBUNTU-CVE-2026-57433,USN-8684-1 | V:UB:CVE-2026-57433
  │ ✔✔✔✔ CVE-2026-48959         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-48959,USN-8684-1 | V:UB:CVE-2026-48959
  │ ✔✔✔✔ CVE-2026-48962         HIGH         7.8   0.5%   ·  ↳ O:UBUNTU-CVE-2026-48962,USN-8684-1 | V:UB:CVE-2026-48962
  │ ✔✔✔✔ CVE-2026-57432         HIGH         8.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57432,USN-8684-1 | V:UB:CVE-2026-57432
  │ ✔✔✔✔ CVE-2026-7017          HIGH         7.1   0.2%   ·  ↳ O:UBUNTU-CVE-2026-7017,USN-8684-1 | V:UB:CVE-2026-7017
  │ ✔✔✘✘ CVE-2026-82560         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-82560
  │ ✔✔✔✔ CVE-2026-9538          HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-9538,USN-8684-1 | V:UB:CVE-2026-9538
  │ ✔✔✔✔ CVE-2025-15649         MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2025-15649,USN-8684-1 | V:UB:CVE-2025-15649
  │ ✔✔✔✘ CVE-2026-15534         MEDIUM       5.7   0.3%   ·  ↳ O:UBUNTU-CVE-2026-15534,USN-8736-2
  │ ✔✔✔✘ CVE-2026-19487         MEDIUM       5.3   0.4%   ·  ↳ O:UBUNTU-CVE-2026-19487,USN-8736-2
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/perl-base@5.38.2-3.2ubuntu0.3
  │ OGTV
  │ ✘✘✔✘ CVE-2026-12087         CRITICAL     9.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-13221         CRITICAL     9.1   0.4%   ·
  │ ✘✘✔✘ CVE-2026-57433         CRITICAL     9.8   0.4%   ·
  │ ✘✘✔✘ CVE-2026-48959         HIGH         7.5   0.6%   ·
  │ ✘✘✔✘ CVE-2026-48962         HIGH         7.8   0.5%   ·
  │ ✘✘✔✘ CVE-2026-57432         HIGH         8.4   0.2%   ·
  │ ✘✘✔✘ CVE-2026-7017          HIGH         7.1   0.2%   ·
  │ ✘✘✔✘ CVE-2026-9538          HIGH         7.5   0.4%   ·
  │ ✘✘✔✘ CVE-2025-15649         MEDIUM       5.5   0.1%   ·
  │ ✘✘✔✔ CVE-2026-15534         MEDIUM       5.7   0.3%   ·  ↳ V:UB:CVE-2026-15534
  │ ✘✘✔✔ CVE-2026-19487         MEDIUM       5.3   0.4%   ·  ↳ V:UB:CVE-2026-19487
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/perl-modules-5.38@5.38.2-3.2ubuntu0.3
  │ OGTV
  │ ✘✘✔✔ CVE-2026-12087         CRITICAL     9.1   0.4%   ·  ↳ V:UB:CVE-2026-12087
  │ ✘✘✔✔ CVE-2026-13221         CRITICAL     9.1   0.4%   ·  ↳ V:UB:CVE-2026-13221
  │ ✘✘✔✔ CVE-2026-57433         CRITICAL     9.8   0.4%   ·  ↳ V:UB:CVE-2026-57433
  │ ✘✘✔✔ CVE-2026-48959         HIGH         7.5   0.6%   ·  ↳ V:UB:CVE-2026-48959
  │ ✘✘✔✔ CVE-2026-48962         HIGH         7.8   0.5%   ·  ↳ V:UB:CVE-2026-48962
  │ ✘✘✔✔ CVE-2026-57432         HIGH         8.4   0.2%   ·  ↳ V:UB:CVE-2026-57432
  │ ✘✘✔✔ CVE-2026-7017          HIGH         7.1   0.2%   ·  ↳ V:UB:CVE-2026-7017
  │ ✘✘✔✔ CVE-2026-9538          HIGH         7.5   0.4%   ·  ↳ V:UB:CVE-2026-9538
  │ ✘✘✔✔ CVE-2025-15649         MEDIUM       5.5   0.1%   ·  ↳ V:UB:CVE-2025-15649
  │ ✘✘✔✘ CVE-2026-15534         MEDIUM       5.7   0.3%   ·
  │ ✘✘✔✘ CVE-2026-19487         MEDIUM       5.3   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-pip@24.0%2Bdfsg-1ubuntu1.3
  │ OGTV
  │ ✘✘✔✔ CVE-2025-66418         HIGH         8.9   0.7%   ·  ↳ V:UB:CVE-2025-66418
  │ ✘✘✔✔ CVE-2025-66471         HIGH         8.9   0.7%   ·  ↳ V:UB:CVE-2025-66471
  │ ✘✘✔✔ CVE-2026-21441         HIGH         8.9   2.9%   ·  ↳ V:UB:CVE-2026-21441
  │ ✘✘✔✔ CVE-2024-35195         MEDIUM       5.6   0.3%   ·  ↳ V:UB:CVE-2024-35195
  │ ✘✘✔✔ CVE-2026-1703          LOW          2.0   0.4%   ·  ↳ V:UB:CVE-2026-1703
  │ ✘✘✘✔ CVE-2026-9375          ?            0.0   0.3%   ·  ↳ V:UB:CVE-2026-9375
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-wheel@0.42.0-2
  │ OGTV
  │ ✘✘✔✔ CVE-2026-24049         HIGH         7.1   0.4%   ·  ↳ V:UB:CVE-2026-24049
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3.12@3.12.3-1ubuntu0.15
  │ OGTV
  │ ✔✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.4%   ·  ↳ O:UBUNTU-CVE-2026-19445
  │ ✔✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·  ↳ O:UBUNTU-CVE-2026-11940
  │ ✔✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·  ↳ O:UBUNTU-CVE-2026-11972
  │ ✔✔✔✔ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ O:UBUNTU-CVE-2026-15308,USN-8744-1 | V:UB:CVE-2026-15308
  │ ✔✔✘✘ CVE-2026-19553         HIGH         7.6   0.4%   ·  ↳ O:UBUNTU-CVE-2026-19553
  │ ✔✘✘✘ CVE-2026-3644          HIGH         7.5   0.5%   ·  ↳ O:USN-8744-1
  │ ✔✘✘✘ CVE-2026-4224          HIGH         7.5   0.7%   ·  ↳ O:USN-8744-1
  │ ✔✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57178
  │ ✔✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·  ↳ O:UBUNTU-CVE-2026-7210
  │ ✔✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-82049
  │ ✔✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·  ↳ O:UBUNTU-CVE-2026-84366
  │ ✔✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.6%   ·  ↳ O:UBUNTU-CVE-2025-12781
  │ ✔✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·  ↳ O:UBUNTU-CVE-2025-15366
  │ ✔✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·  ↳ O:UBUNTU-CVE-2025-15367
  │ ✔✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-0864
  │ ✔✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.2%   ·  ↳ O:UBUNTU-CVE-2026-12345
  │ ✔✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·  ↳ O:UBUNTU-CVE-2026-15806
  │ ✔✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·  ↳ O:UBUNTU-CVE-2026-17084
  │ ✔✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·  ↳ O:UBUNTU-CVE-2026-19672
  │ ✔✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-3446
  │ ✔✔✔✔ CVE-2026-4360          MEDIUM       5.3   0.5%   ·  ↳ O:UBUNTU-CVE-2026-4360,USN-8744-1 | V:UB:CVE-2026-4360
  │ ✔✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57175
  │ ✔✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57176
  │ ✔✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·  ↳ O:UBUNTU-CVE-2026-57177
  │ ✔✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57179
  │ ✔✘✘✘ CVE-2026-6019          MEDIUM       6.1   0.2%   ·  ↳ O:USN-8744-1
  │ ✔✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.5%   ·  ↳ O:UBUNTU-CVE-2026-87910
  │ ✔✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·  ↳ O:UBUNTU-CVE-2026-15310
  │ ✔✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·  ↳ O:UBUNTU-CVE-2026-18503
  │ ✔✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·  ↳ O:UBUNTU-CVE-2026-6879
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3.12-dev@3.12.3-1ubuntu0.15
  │ OGTV
  │ ✘✘✔✘ CVE-2026-15308         HIGH         8.7   0.6%   ·
  │ ✘✘✔✘ CVE-2026-4360          MEDIUM       5.3   0.5%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3.12-minimal@3.12.3-1ubuntu0.15
  │ OGTV
  │ ✘✘✔✘ CVE-2026-15308         HIGH         8.7   0.6%   ·
  │ ✘✘✔✘ CVE-2026-4360          MEDIUM       5.3   0.5%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/tar@1.35%2Bdfsg-3build1
  │ OGTV
  │ ✔✔✔✔ CVE-2025-45582         MEDIUM       4.1   0.5%   ·  ↳ O:UBUNTU-CVE-2025-45582,USN-8510-1 | V:UB:CVE-2025-45582
  │ ✔✔✔✔ CVE-2026-18477         MEDIUM       4.4   0.1%   ·  ↳ O:UBUNTU-CVE-2026-18477 | V:UB:CVE-2026-18477
  │ ✔✔✔✔ CVE-2026-18508         MEDIUM       4.4   0.1%   ·  ↳ O:UBUNTU-CVE-2026-18508 | V:UB:CVE-2026-18508
  │ ✔✔✔✔ CVE-2026-5704          MEDIUM       5.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-5704,USN-8477-2,USN-8477-3 | V:UB:CVE-2026-5704
  │ ✔✘✘✘ USN-8477-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/util-linux@2.39.3-9ubuntu6.5
  │ OGTV
  │ ✔✔✔✔ CVE-2026-53612         HIGH         7.0   0.1%   ·  ↳ O:UBUNTU-CVE-2026-53612,USN-8702-1 | V:UB:CVE-2026-53612
  │ ✔✔✔✔ CVE-2026-53613         HIGH         7.0   0.1%   ·  ↳ O:UBUNTU-CVE-2026-53613,USN-8702-1 | V:UB:CVE-2026-53613
  │ ✔✔✔✔ CVE-2026-53614         HIGH         7.0   0.1%   ·  ↳ O:UBUNTU-CVE-2026-53614,USN-8702-1 | V:UB:CVE-2026-53614
  │ ✔✔✔✔ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-53615,USN-8702-1 | V:UB:CVE-2026-53615
  │ ✔✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ O:UBUNTU-CVE-2026-76642
  │ ✔✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ O:UBUNTU-CVE-2026-78408
  │ ✔✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-78409
  │ ✔✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-78410
  │ ✔✔✔✔ CVE-2026-13595         MEDIUM       6.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-13595,USN-8702-1 | V:UB:CVE-2026-13595
  │ ✔✔✔✔ CVE-2026-27456         MEDIUM       4.7   0.1%   ·  ↳ O:UBUNTU-CVE-2026-27456,USN-8702-1 | V:UB:CVE-2026-27456
  │ ✔✘✘✘ CVE-2026-3184          MEDIUM       5.3   0.4%   ·  ↳ O:USN-8702-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/zlib1g@1%3A1.3.dfsg-3.1ubuntu2.1
  │ OGTV
  │ ✘✘✔✔ CVE-2026-85091         HIGH         8.3   0.4%   ·  ↳ V:UB:CVE-2026-85091
  │ ✘✘✔✔ CVE-2026-27171         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-27171
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/zlib1g-dev@1%3A1.3.dfsg-3.1ubuntu2.1
  │ OGTV
  │ ✘✘✔✔ CVE-2026-85091         HIGH         8.3   0.4%   ·  ↳ V:UB:CVE-2026-85091
  │ ✘✘✔✔ CVE-2026-27171         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-27171
  └────────────────────────────────────────────────────────────────────────────────────────────────────

  ━━ Go ━━
  ┌─ pkg:golang/github.com/containerd/containerd/v2@v2.2.5
  │ OGTV
  │ ✔✔✔✔ CVE-2026-95837         HIGH         7.8   0.1%   ·  ↳ O:GHSA-p7v4-vr35-mj6f | V:OSV:GHSA-P7V4-VR35-MJ6F
  │ ✘✘✘✔ CVE-2026-95839         HIGH         7.1      -   ·  ↳ V:MEND:CVE-2026-95839
  │ ✔✔✔✔ CVE-2026-53493         MEDIUM       6.9   0.4%   ·  ↳ O:GHSA-pg57-6jwg-q645,GO-2026-6597 | V:MEND:CVE-2026-53493
  │ ✔✔✔✔ CVE-2026-53495         MEDIUM       6.8   0.2%   ·  ↳ O:GHSA-7jxh-36q5-gcqv,GO-2026-6444 | V:MEND:CVE-2026-53495
  │ ✔✔✔✔ CVE-2026-95838         MEDIUM       4.6   0.2%   ·  ↳ O:GHSA-rp3h-jf77-q9p4 | V:OSV:GHSA-RP3H-JF77-Q9P4
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/containerd/containerd/v2@v2.3.3
  │ OGTV
  │ ✔✔✔✔ CVE-2026-95837         HIGH         7.8   0.1%   ·  ↳ O:GHSA-p7v4-vr35-mj6f | V:MEND:CVE-2026-95837
  │ ✘✘✘✔ CVE-2026-95839         HIGH         7.1      -   ·  ↳ V:MEND:CVE-2026-95839
  │ ✔✔✔✔ CVE-2026-53493         MEDIUM       6.9   0.4%   ·  ↳ O:GHSA-pg57-6jwg-q645,GO-2026-6597 | V:MEND:CVE-2026-53493
  │ ✔✔✔✔ CVE-2026-53495         MEDIUM       6.8   0.2%   ·  ↳ O:GHSA-7jxh-36q5-gcqv,GO-2026-6444 | V:MEND:CVE-2026-53495
  │ ✔✔✔✔ CVE-2026-95838         MEDIUM       4.6   0.2%   ·  ↳ O:GHSA-rp3h-jf77-q9p4 | V:OSV:GHSA-RP3H-JF77-Q9P4
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/buildx@v0.35.0
  │ OGTV
  │ ✘✘✘✔ CVE-2026-103433        MEDIUM       6.9   0.3%   ·  ↳ V:MEND:CVE-2026-103433
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/buildx@v0.36.0
  │ OGTV
  │ ✘✘✘✔ CVE-2026-103433        MEDIUM       6.9   0.3%   ·  ↳ V:MEND:CVE-2026-103433
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/docker@v28.5.2%2Bincompatible
  │ OGTV
  │ ✔✔✔✔ CVE-2026-33997         HIGH         8.4   0.5%   ·  ↳ O:GHSA-pxq6-2prw-chj9,GO-2026-4883 | V:OSV:GO-2026-4883
  │ ✔✔✘✔ CVE-2026-34040         HIGH         8.8   0.2%   ·  ↳ O:GO-2026-4887 | V:OSV:GO-2026-4887
  │ ✔✔✔✔ CVE-2026-41567         HIGH         7.5   0.2%   ·  ↳ O:GHSA-x86f-5xw2-fm2r,GO-2026-5746 | V:OSV:GO-2026-5746
  │ ✔✔✔✔ CVE-2026-42306         HIGH         7.2   0.1%   ·  ↳ O:GHSA-rg2x-37c3-w2rh,GO-2026-5617 | V:OSV:GO-2026-5617
  │ ✔✔✔✔ CVE-2026-41568         MEDIUM       6.1   0.1%   ·  ↳ O:GHSA-vp62-88p7-qqf5,GO-2026-5668 | V:OSV:GO-2026-5668
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/go-openapi/swag/jsonutils@v0.26.1
  │ OGTV
  │ ✘✘✘✔ CVE-2026-93450         HIGH         8.7   0.9%   ·  ↳ V:MEND:CVE-2026-93450
  │ ✘✘✘✔ WS-2026-0063           HIGH         8.7      -   ·  ↳ V:MEND:WS-2026-0063
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/go-openapi/swag/yamlutils@v0.26.1
  │ OGTV
  │ ✘✘✘✔ CVE-2026-85280         HIGH         8.7      -   ·  ↳ V:MEND:CVE-2026-85280
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/klauspost/compress@v1.18.6
  │ OGTV
  │ ✔✔✘✔ CVE-2026-63209         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-5841 | G:GO-2026-5841 | V:MEND:CVE-2026-63209
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/moby/buildkit@v0.31.1
  │ OGTV
  │ ✘✘✘✔ CVE-2026-15788         HIGH         7.5   0.4%   ·  ↳ V:MEND:CVE-2026-15788
  │ ✘✘✘✔ CVE-2026-15789         HIGH         7.5   0.3%   ·  ↳ V:MEND:CVE-2026-15789
  │ ✘✘✘✔ CVE-2026-15791         HIGH         7.5   0.2%   ·  ↳ V:MEND:CVE-2026-15791
  │ ✘✘✘✔ CVE-2026-15792         HIGH         7.5   0.2%   ·  ↳ V:MEND:CVE-2026-15792
  │ ✘✘✘✔ CVE-2026-15793         HIGH         7.5   0.2%   ·  ↳ V:MEND:CVE-2026-15793
  │ ✘✘✘✔ CVE-2026-75593         HIGH         7.2   0.5%   ·  ↳ V:MEND:CVE-2026-75593
  │ ✘✘✘✔ CVE-2026-93318         HIGH         7.5   0.2%   ·  ↳ V:MEND:CVE-2026-93318
  │ ✘✘✘✔ CVE-2026-93315         MEDIUM       5.8   0.1%   ·  ↳ V:MEND:CVE-2026-93315
  │ ✘✘✘✔ CVE-2026-93320         MEDIUM       6.0   0.1%   ·  ↳ V:MEND:CVE-2026-93320
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/moby/buildkit@v0.32.0
  │ OGTV
  │ ✘✘✘✔ CVE-2026-93318         HIGH         7.5   0.2%   ·  ↳ V:MEND:CVE-2026-93318
  │ ✘✘✘✔ CVE-2026-93315         MEDIUM       5.8   0.1%   ·  ↳ V:MEND:CVE-2026-93315
  │ ✘✘✘✔ CVE-2026-93320         MEDIUM       6.0   0.1%   ·  ↳ V:MEND:CVE-2026-93320
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/moby/go-archive@v0.2.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-17106         HIGH         7.1   0.4%   ·  ↳ O:GHSA-hfg8-hc9c-6c3h,GO-2026-6253 | V:MEND:CVE-2026-17106
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/moby/go-archive@v0.2.1
  │ OGTV
  │ ✔✔✔✔ CVE-2026-17106         HIGH         7.1   0.4%   ·  ↳ O:GHSA-hfg8-hc9c-6c3h,GO-2026-6253 | V:MEND:CVE-2026-17106
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/pelletier/go-toml/v2@v2.3.1
  │ OGTV
  │ ✘✘✘✔ WS-2026-0062           HIGH         8.7      -   ·  ↳ V:MEND:WS-2026-0062
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace@v1.44.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-81870         LOW          2.0   0.2%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:SNYK:GOLANG-GOOPENTELEMETRYIOOTELEXPORTERSOTLPOTLPTRACE-19883902
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc@v1.44.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-81870         LOW          2.0   0.2%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:SNYK:GOLANG-GOOPENTELEMETRYIOOTELEXPORTERSOTLPOTLPTRACEOTLPTRACEGRPC-19883903
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp@v1.44.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-81870         LOW          2.0   0.2%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:SNYK:GOLANG-GOOPENTELEMETRYIOOTELEXPORTERSOTLPOTLPTRACEOTLPTRACEHTTP-19883904
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/sdk@v1.44.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-81870         LOW          2.0   0.2%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:MEND:CVE-2026-81870
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/crypto@v0.53.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-56854         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6303 | V:MEND:CVE-2026-56854
  │ ✔✔✔✔ CVE-2026-56855         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6355 | V:MEND:CVE-2026-56855
  │ ✔✔✔✔ CVE-2026-78662         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6354 | V:MEND:CVE-2026-78662
  │ ✔✔✔✔ GO-2026-5932           ?            0.0      -   ·  ↳ V:OSV:GO-2026-5932
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/crypto@v0.54.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-56854         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6303 | V:MEND:CVE-2026-56854
  │ ✔✔✔✔ CVE-2026-56855         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6355 | V:MEND:CVE-2026-56855
  │ ✔✔✔✔ CVE-2026-78662         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6354 | V:MEND:CVE-2026-78662
  │ ✔✔✔✔ GO-2026-5932           ?            0.0      -   ·  ↳ V:OSV:GO-2026-5932
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/mod@v0.38.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-56864         HIGH         7.5   0.3%   ·  ↳ O:GO-2026-6180 | V:MEND:CVE-2026-56864
  │ ✔✔✔✔ CVE-2026-56865         HIGH         8.4   0.1%   ·  ↳ O:GO-2026-6179 | V:MEND:CVE-2026-56865
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/net@v0.56.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-78663         CRITICAL     9.1   0.6%   ·  ↳ O:GO-2026-6612 | V:MEND:CVE-2026-78663
  │ ✔✔✔✔ CVE-2026-78659         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6603 | V:MEND:CVE-2026-78659
  │ ✔✔✔✔ CVE-2026-78660         HIGH         7.5   0.3%   ·  ↳ O:GO-2026-6610 | V:MEND:CVE-2026-78660
  │ ✔✔✔✔ CVE-2026-78669         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6611 | V:MEND:CVE-2026-78669
  │ ✔✔✔✔ CVE-2026-97032         HIGH         7.5   0.2%   ·  ↳ O:GO-2026-6617 | V:MEND:CVE-2026-97032
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/net@v0.57.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-78663         CRITICAL     9.1   0.6%   ·  ↳ O:GO-2026-6612 | V:MEND:CVE-2026-78663
  │ ✔✔✔✔ CVE-2026-78659         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6603 | V:MEND:CVE-2026-78659
  │ ✔✔✔✔ CVE-2026-78660         HIGH         7.5   0.3%   ·  ↳ O:GO-2026-6610 | V:MEND:CVE-2026-78660
  │ ✔✔✔✔ CVE-2026-78669         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6611 | V:MEND:CVE-2026-78669
  │ ✔✔✔✔ CVE-2026-97032         HIGH         7.5   0.2%   ·  ↳ O:GO-2026-6617 | V:MEND:CVE-2026-97032
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/text@v0.38.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-56851         HIGH         7.5   0.3%   ·  ↳ O:GO-2026-6629 | V:MEND:CVE-2026-56851
  │ ✔✔✔✔ CVE-2026-56852         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-5970 | V:MEND:CVE-2026-56852
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/text@v0.40.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-56851         HIGH         7.5   0.3%   ·  ↳ O:GO-2026-6629 | V:MEND:CVE-2026-56851
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/google.golang.org/grpc@v1.81.1
  │ OGTV
  │ ✔✔✔✔ CVE-2026-84304         HIGH         8.7   0.6%   ·  ↳ O:GHSA-vp52-pcj8-j9qc,GO-2026-6348 | V:OSV:GO-2026-6348
  │ ✔✔✔✔ CVE-2026-84445         HIGH         8.7   0.6%   ·  ↳ O:GHSA-2v4p-qf9q-27wj,GO-2026-6443 | V:MEND:CVE-2026-84445
  │ ✔✔✔✔ CVE-2026-84303         MEDIUM       6.3   0.3%   ·  ↳ O:GHSA-qc2q-p7wx-3px3,GO-2026-6441 | V:OSV:GO-2026-6441
  │ ✘✘✘✔ WS-2026-0025           CRITICAL     9.1      -   ·  ↳ V:MEND:WS-2026-0025
  │ ✔✔✔✔ GHSA-HRXH-6V49-42GF    HIGH         8.8      -   ·  ↳ O:GO-2026-6061 | V:GO-2026-6061,OSV:GO-2026-6061
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/google.golang.org/grpc@v1.82.1
  │ OGTV
  │ ✔✔✔✔ CVE-2026-84304         HIGH         8.7   0.6%   ·  ↳ O:GHSA-vp52-pcj8-j9qc,GO-2026-6348 | V:OSV:GO-2026-6348
  │ ✔✔✔✔ CVE-2026-84445         HIGH         8.7   0.6%   ·  ↳ O:GHSA-2v4p-qf9q-27wj,GO-2026-6443 | V:MEND:CVE-2026-84445
  │ ✔✔✔✔ CVE-2026-84303         MEDIUM       6.3   0.3%   ·  ↳ O:GHSA-qc2q-p7wx-3px3,GO-2026-6441 | V:OSV:GO-2026-6441
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/stdlib@v1.26.4
  │ OGTV
  │ ✔✔✔✔ CVE-2026-39821         CRITICAL     9.6   0.7%   ·  ↳ O:GO-2026-5026 | V:OSV:GO-2026-5026
  │ ✔✔✔✔ CVE-2026-56857         CRITICAL     9.8   0.5%   ·  ↳ O:GO-2026-6604 | V:OSV:GO-2026-6604
  │ ✔✔✔✔ CVE-2026-78663         CRITICAL     9.1   0.6%   ·  ↳ O:GO-2026-6612 | V:OSV:GO-2026-6612
  │ ✔✔✔✔ CVE-2026-33818         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-5972 | V:OSV:GO-2026-5972
  │ ✔✔✔✔ CVE-2026-39822         HIGH         7.8   0.2%   ·  ↳ O:GO-2026-4970 | V:OSV:GO-2026-4970
  │ ✔✔✔✔ CVE-2026-46600         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-5942 | V:OSV:GO-2026-5942
  │ ✔✔✔✔ CVE-2026-56853         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6089 | V:OSV:GO-2026-6089
  │ ✔✔✔✔ CVE-2026-56859         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6088 | V:OSV:GO-2026-6088
  │ ✔✔✔✔ CVE-2026-56862         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6090 | V:OSV:GO-2026-6090
  │ ✔✔✔✔ CVE-2026-56866         HIGH         7.5   0.3%   ·  ↳ O:GO-2026-6605 | V:OSV:GO-2026-6605
  │ ✔✔✔✔ CVE-2026-78659         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6603 | V:OSV:GO-2026-6603
  │ ✔✔✔✔ CVE-2026-78660         HIGH         7.5   0.3%   ·  ↳ O:GO-2026-6610 | V:OSV:GO-2026-6610
  │ ✔✔✔✔ CVE-2026-78667         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6609 | V:OSV:GO-2026-6609
  │ ✔✔✔✔ CVE-2026-78669         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6611 | V:OSV:GO-2026-6611
  │ ✔✔✔✔ CVE-2026-94439         HIGH         7.5   0.3%   ·  ↳ O:GO-2026-6613 | V:OSV:GO-2026-6613
  │ ✔✔✔✔ CVE-2026-94440         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6608 | V:OSV:GO-2026-6608
  │ ✔✔✔✔ CVE-2026-97031         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6607 | V:OSV:GO-2026-6607
  │ ✔✔✔✔ CVE-2026-97032         HIGH         7.5   0.2%   ·  ↳ O:GO-2026-6617 | V:OSV:GO-2026-6617
  │ ✔✔✔✔ CVE-2026-42505         MEDIUM       5.3   0.4%   ·  ↳ O:GO-2026-5856 | V:OSV:GO-2026-5856
  │ ✔✔✔✔ CVE-2026-56858         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-6091 | V:OSV:GO-2026-6091
  │ ✔✔✔✔ CVE-2026-56860         MEDIUM       5.9   0.5%   ·  ↳ O:GO-2026-6218 | V:OSV:GO-2026-6218
  │ ✔✔✔✔ CVE-2026-94448         MEDIUM       6.1   0.2%   ·  ↳ O:GO-2026-6599 | V:OSV:GO-2026-6599
  │ ✔✔✔✔ CVE-2026-97030         MEDIUM       6.1   0.2%   ·  ↳ O:GO-2026-6600 | V:OSV:GO-2026-6600
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/stdlib@v1.26.5
  │ OGTV
  │ ✔✔✔✔ CVE-2026-39821         CRITICAL     9.6   0.7%   ·  ↳ O:GO-2026-5026 | V:OSV:GO-2026-5026
  │ ✔✔✔✔ CVE-2026-56857         CRITICAL     9.8   0.5%   ·  ↳ O:GO-2026-6604 | V:OSV:GO-2026-6604
  │ ✔✔✔✔ CVE-2026-78663         CRITICAL     9.1   0.6%   ·  ↳ O:GO-2026-6612 | V:OSV:GO-2026-6612
  │ ✔✔✔✔ CVE-2026-33818         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-5972 | V:OSV:GO-2026-5972
  │ ✔✔✔✔ CVE-2026-46600         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-5942 | V:OSV:GO-2026-5942
  │ ✔✔✔✔ CVE-2026-56853         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6089 | V:OSV:GO-2026-6089
  │ ✔✔✔✔ CVE-2026-56859         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6088 | V:OSV:GO-2026-6088
  │ ✔✔✔✔ CVE-2026-56862         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6090 | V:OSV:GO-2026-6090
  │ ✔✔✔✔ CVE-2026-56866         HIGH         7.5   0.3%   ·  ↳ O:GO-2026-6605 | V:OSV:GO-2026-6605
  │ ✔✔✔✔ CVE-2026-78659         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6603 | V:OSV:GO-2026-6603
  │ ✔✔✔✔ CVE-2026-78660         HIGH         7.5   0.3%   ·  ↳ O:GO-2026-6610 | V:OSV:GO-2026-6610
  │ ✔✔✔✔ CVE-2026-78667         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6609 | V:OSV:GO-2026-6609
  │ ✔✔✔✔ CVE-2026-78669         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6611 | V:OSV:GO-2026-6611
  │ ✔✔✔✔ CVE-2026-94439         HIGH         7.5   0.3%   ·  ↳ O:GO-2026-6613 | V:OSV:GO-2026-6613
  │ ✔✔✔✔ CVE-2026-94440         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6608 | V:OSV:GO-2026-6608
  │ ✔✔✔✔ CVE-2026-97031         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6607 | V:OSV:GO-2026-6607
  │ ✔✔✔✔ CVE-2026-97032         HIGH         7.5   0.2%   ·  ↳ O:GO-2026-6617 | V:OSV:GO-2026-6617
  │ ✔✔✔✔ CVE-2026-56858         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-6091 | V:OSV:GO-2026-6091
  │ ✔✔✔✔ CVE-2026-56860         MEDIUM       5.9   0.5%   ·  ↳ O:GO-2026-6218 | V:OSV:GO-2026-6218
  │ ✔✔✔✔ CVE-2026-94448         MEDIUM       6.1   0.2%   ·  ↳ O:GO-2026-6599 | V:OSV:GO-2026-6599
  │ ✔✔✔✔ CVE-2026-97030         MEDIUM       6.1   0.2%   ·  ↳ O:GO-2026-6600 | V:OSV:GO-2026-6600
  └────────────────────────────────────────────────────────────────────────────────────────────────────
