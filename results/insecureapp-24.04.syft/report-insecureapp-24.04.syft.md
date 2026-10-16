# Vulnerability Comparison Report — insecureapp-24.04:latest

- **Image:** `insecureapp-24.04:latest`
- **Digest:** `sha256:18a28020dd5cf4d3243ac372e7860ddca3e32fd2caa79aa7c541cb860db27952`
- **SBOM:** `insecureapp-24.04.syft.cdx.json` — CycloneDX 1.7, syft 1.54.1, built 2026-10-16T12:38:30+02:00
- **Report generated:** 2026-10-16T12:40:38
- **Scanners:** OSV (api.osv.dev) · Grype (grype 0.120.1) · Trivy (trivy 0.76.0) · Vulners (vulners.com audit API v4)

## Summary

  SBOM Components (Raw):           617
  Deduplicated PURLs:              535
  Clean (0 vulns):                 383
  Vulnerable:                      152

  Scanner              |   Pkgs Scanned |  Pkgs w/ Vulns | Total Vuln IDs
  ---------------------+----------------+----------------+---------------
  OSV                  |            535 |             47 |            275
  Grype                |            535 |            144 |            360
  Trivy                |            535 |             45 |            197
  Vulners              |            535 |            102 |            311

  All 4 agree:       188     ≥2 agree:          343     Total:   422     (CVE:403 GHSA:5 Other:14)
  Exclusive to: OSV:21  Grype:28  Trivy:0  Vulners:30

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

  ▸ Debian/Ubuntu (deb) (113 packages)
    ✔✔✔✔  pkg:deb/ubuntu/binutils@2.42-4ubuntu2.10
    ✘✔✘✔  pkg:deb/ubuntu/binutils-aarch64-linux-gnu@2.42-4ubuntu2.10
    ✘✔✘✔  pkg:deb/ubuntu/binutils-common@2.42-4ubuntu2.10
    ✘✔✘✘  pkg:deb/ubuntu/bsdutils@1%3A2.39.3-9ubuntu6.5
    ✔✔✔✔  pkg:deb/ubuntu/bzip2@1.0.8-5.1build0.1
    ✔✔✔✔  pkg:deb/ubuntu/coreutils@9.4-3ubuntu6.2
    ✘✔✘✘  pkg:deb/ubuntu/cpp@4%3A13.2.0-7ubuntu1
    ✘✔✘✘  pkg:deb/ubuntu/cpp-13@13.3.0-6ubuntu2~24.04.1
    ✘✔✘✘  pkg:deb/ubuntu/cpp-13-aarch64-linux-gnu@13.3.0-6ubuntu2~24.04.1
    ✘✔✘✘  pkg:deb/ubuntu/cpp-aarch64-linux-gnu@4%3A13.2.0-7ubuntu1
    ✔✔✔✔  pkg:deb/ubuntu/curl@8.5.0-2ubuntu10.11
    ✔✔✔✔  pkg:deb/ubuntu/dash@0.5.12-6ubuntu5
    ✔✔✔✔  pkg:deb/ubuntu/diffutils@1%3A3.10-1build1
    ✘✔✘✘  pkg:deb/ubuntu/dirmngr@2.4.4-2ubuntu17.4
    ✘✔✘✘  pkg:deb/ubuntu/g%2B%2B@4%3A13.2.0-7ubuntu1
    ✘✔✘✘  pkg:deb/ubuntu/g%2B%2B-13@13.3.0-6ubuntu2~24.04.1
    ✘✔✘✘  pkg:deb/ubuntu/g%2B%2B-13-aarch64-linux-gnu@13.3.0-6ubuntu2~24.04.1
    ✘✔✘✘  pkg:deb/ubuntu/g%2B%2B-aarch64-linux-gnu@4%3A13.2.0-7ubuntu1
    ✘✔✘✘  pkg:deb/ubuntu/gcc@4%3A13.2.0-7ubuntu1
    ✔✔✘✘  pkg:deb/ubuntu/gcc-13@13.3.0-6ubuntu2~24.04.1
    ✘✔✘✘  pkg:deb/ubuntu/gcc-13-aarch64-linux-gnu@13.3.0-6ubuntu2~24.04.1
    ✘✔✘✘  pkg:deb/ubuntu/gcc-13-base@13.3.0-6ubuntu2~24.04.1
    ✘✔✘✘  pkg:deb/ubuntu/gcc-aarch64-linux-gnu@4%3A13.2.0-7ubuntu1
    ✘✔✘✘  pkg:deb/ubuntu/gnupg@2.4.4-2ubuntu17.4
    ✘✔✘✘  pkg:deb/ubuntu/gnupg-l10n@2.4.4-2ubuntu17.4
    ✘✔✘✘  pkg:deb/ubuntu/gnupg-utils@2.4.4-2ubuntu17.4
    ✘✔✘✘  pkg:deb/ubuntu/gpg@2.4.4-2ubuntu17.4
    ✘✔✘✘  pkg:deb/ubuntu/gpg-agent@2.4.4-2ubuntu17.4
    ✘✔✘✘  pkg:deb/ubuntu/gpg-wks-client@2.4.4-2ubuntu17.4
    ✘✔✘✘  pkg:deb/ubuntu/gpgconf@2.4.4-2ubuntu17.4
    ✘✔✘✔  pkg:deb/ubuntu/gpgsm@2.4.4-2ubuntu17.4
    ✘✔✘✘  pkg:deb/ubuntu/gpgv@2.4.4-2ubuntu17.4
    ✔✔✔✔  pkg:deb/ubuntu/gzip@1.12-1ubuntu3.1
    ✘✔✘✘  pkg:deb/ubuntu/keyboxd@2.4.4-2ubuntu17.4
    ✘✔✘✘  pkg:deb/ubuntu/libacl1@2.3.2-1build1.1
    ✘✔✘✔  pkg:deb/ubuntu/libaom3@3.8.2-2ubuntu0.1
    ✘✔✘✔  pkg:deb/ubuntu/libattr1@1%3A2.5.2-1build1.1
    ✘✔✘✔  pkg:deb/ubuntu/libbinutils@2.42-4ubuntu2.10
    ✘✔✘✘  pkg:deb/ubuntu/libblkid1@2.39.3-9ubuntu6.5
    ✘✔✘✘  pkg:deb/ubuntu/libbz2-1.0@1.0.8-5.1build0.1
    ✘✔✘✔  pkg:deb/ubuntu/libc-bin@2.39-0ubuntu8.8
    ✘✔✘✔  pkg:deb/ubuntu/libc-dev-bin@2.39-0ubuntu8.8
    ✘✔✘✔  pkg:deb/ubuntu/libc-devtools@2.39-0ubuntu8.8
    ✘✔✘✔  pkg:deb/ubuntu/libc6@2.39-0ubuntu8.8
    ✘✔✘✔  pkg:deb/ubuntu/libc6-dev@2.39-0ubuntu8.8
    ✘✔✘✔  pkg:deb/ubuntu/libctf-nobfd0@2.42-4ubuntu2.10
    ✘✔✘✔  pkg:deb/ubuntu/libctf0@2.42-4ubuntu2.10
    ✘✔✘✔  pkg:deb/ubuntu/libcurl4t64@8.5.0-2ubuntu10.11
    ✘✔✘✔  pkg:deb/ubuntu/libexpat1@2.6.1-2ubuntu0.4
    ✘✔✘✔  pkg:deb/ubuntu/libexpat1-dev@2.6.1-2ubuntu0.4
    ✘✔✘✔  pkg:deb/ubuntu/libfreetype6@2.13.2%2Bdfsg-1ubuntu0.1
    ✘✔✘✘  pkg:deb/ubuntu/libgcc-13-dev@13.3.0-6ubuntu2~24.04.1
    ✔✔✔✔  pkg:deb/ubuntu/libgcrypt20@1.10.3-2ubuntu0.1
    ✘✔✘✘  pkg:deb/ubuntu/libgd3@2.3.3-9ubuntu5
    ✘✔✘✔  pkg:deb/ubuntu/libgnutls30t64@3.8.3-1.1ubuntu3.6
    ✘✔✘✔  pkg:deb/ubuntu/libgprofng0@2.42-4ubuntu2.10
    ✘✔✘✔  pkg:deb/ubuntu/libheif-plugin-aomdec@1.17.6-1ubuntu4.6
    ✘✔✘✔  pkg:deb/ubuntu/libheif-plugin-aomenc@1.17.6-1ubuntu4.6
    ✘✔✘✔  pkg:deb/ubuntu/libheif1@1.17.6-1ubuntu4.6
    ✘✘✘✔  pkg:deb/ubuntu/libhwasan0@14.2.0-4ubuntu2~24.04.1
    ✘✔✘✘  pkg:deb/ubuntu/libjpeg-turbo8@2.1.5-2ubuntu2
    ✘✔✘✘  pkg:deb/ubuntu/libmount1@2.39.3-9ubuntu6.5
    ✘✔✘✔  pkg:deb/ubuntu/libncursesw6@6.4%2B20240113-1ubuntu2
    ✘✔✘✔  pkg:deb/ubuntu/libp11-kit0@0.25.3-4ubuntu2.1
    ✘✔✘✔  pkg:deb/ubuntu/libpam-modules@1.5.3-5ubuntu5.5
    ✘✔✘✘  pkg:deb/ubuntu/libpam-modules-bin@1.5.3-5ubuntu5.5
    ✘✔✘✘  pkg:deb/ubuntu/libpam-runtime@1.5.3-5ubuntu5.5
    ✘✔✘✘  pkg:deb/ubuntu/libpam0g@1.5.3-5ubuntu5.5
    ✘✔✘✔  pkg:deb/ubuntu/libpcre2-8-0@10.42-4ubuntu2.1
    ✘✔✘✔  pkg:deb/ubuntu/libperl5.38t64@5.38.2-3.2ubuntu0.3
    ✘✔✘✔  pkg:deb/ubuntu/libpng16-16t64@1.6.43-5ubuntu0.6
    ✘✔✘✘  pkg:deb/ubuntu/libpython3.12-dev@3.12.3-1ubuntu0.15
    ✘✔✘✘  pkg:deb/ubuntu/libpython3.12-minimal@3.12.3-1ubuntu0.15
    ✘✔✘✘  pkg:deb/ubuntu/libpython3.12-stdlib@3.12.3-1ubuntu0.15
    ✘✔✘✔  pkg:deb/ubuntu/libpython3.12t64@3.12.3-1ubuntu0.15
    ✘✔✘✘  pkg:deb/ubuntu/libsasl2-2@2.1.28%2Bdfsg1-5ubuntu3.1
    ✘✔✘✘  pkg:deb/ubuntu/libsasl2-modules@2.1.28%2Bdfsg1-5ubuntu3.1
    ✘✔✘✘  pkg:deb/ubuntu/libsasl2-modules-db@2.1.28%2Bdfsg1-5ubuntu3.1
    ✘✔✘✔  pkg:deb/ubuntu/libsframe1@2.42-4ubuntu2.10
    ✘✔✘✘  pkg:deb/ubuntu/libsmartcols1@2.39.3-9ubuntu6.5
    ✘✔✘✔  pkg:deb/ubuntu/libsqlite3-0@3.45.1-1ubuntu2.7
    ✘✔✘✔  pkg:deb/ubuntu/libssh-4@0.10.6-2ubuntu0.4
    ✘✔✘✔  pkg:deb/ubuntu/libssl3t64@3.0.13-0ubuntu3.12
    ✘✔✘✘  pkg:deb/ubuntu/libstdc%2B%2B-13-dev@13.3.0-6ubuntu2~24.04.1
    ✘✔✘✔  pkg:deb/ubuntu/libsystemd0@255.4-1ubuntu8.16
    ✘✔✘✘  pkg:deb/ubuntu/libtiff6@4.5.1%2Bgit230720-4ubuntu2.5
    ✘✔✘✔  pkg:deb/ubuntu/libtinfo6@6.4%2B20240113-1ubuntu2
    ✘✔✘✔  pkg:deb/ubuntu/libudev1@255.4-1ubuntu8.16
    ✘✔✘✘  pkg:deb/ubuntu/libuuid1@2.39.3-9ubuntu6.5
    ✘✔✘✔  pkg:deb/ubuntu/libx11-6@2%3A1.8.7-1build1
    ✘✔✘✘  pkg:deb/ubuntu/libx11-data@2%3A1.8.7-1build1
    ✘✔✘✔  pkg:deb/ubuntu/libxpm4@1%3A3.5.17-1ubuntu0.24.04.1
    ✘✔✘✔  pkg:deb/ubuntu/login@1%3A4.13%2Bdfsg1-4ubuntu3.2
    ✘✔✘✘  pkg:deb/ubuntu/mount@2.39.3-9ubuntu6.5
    ✘✔✘✔  pkg:deb/ubuntu/ncurses-base@6.4%2B20240113-1ubuntu2
    ✘✔✘✔  pkg:deb/ubuntu/ncurses-bin@6.4%2B20240113-1ubuntu2
    ✔✔✔✔  pkg:deb/ubuntu/openssl@3.0.13-0ubuntu3.12
    ✘✔✘✔  pkg:deb/ubuntu/passwd@1%3A4.13%2Bdfsg1-4ubuntu3.2
    ✔✔✔✔  pkg:deb/ubuntu/patch@2.7.6-7build3
    ✔✔✔✔  pkg:deb/ubuntu/perl@5.38.2-3.2ubuntu0.3
    ✘✔✘✔  pkg:deb/ubuntu/perl-base@5.38.2-3.2ubuntu0.3
    ✘✔✘✔  pkg:deb/ubuntu/perl-modules-5.38@5.38.2-3.2ubuntu0.3
    ✘✔✘✔  pkg:deb/ubuntu/python3-pip@24.0%2Bdfsg-1ubuntu1.3
    ✘✔✘✘  pkg:deb/ubuntu/python3-pkg-resources@68.1.2-2ubuntu1.2
    ✘✔✘✘  pkg:deb/ubuntu/python3-setuptools@68.1.2-2ubuntu1.2
    ✘✔✘✔  pkg:deb/ubuntu/python3-wheel@0.42.0-2
    ✔✔✔✔  pkg:deb/ubuntu/python3.12@3.12.3-1ubuntu0.15
    ✘✔✘✘  pkg:deb/ubuntu/python3.12-dev@3.12.3-1ubuntu0.15
    ✘✔✘✘  pkg:deb/ubuntu/python3.12-minimal@3.12.3-1ubuntu0.15
    ✔✔✔✔  pkg:deb/ubuntu/tar@1.35%2Bdfsg-3build1
    ✔✔✔✔  pkg:deb/ubuntu/util-linux@2.39.3-9ubuntu6.5
    ✘✔✘✔  pkg:deb/ubuntu/zlib1g@1%3A1.3.dfsg-3.1ubuntu2.1
    ✘✔✘✔  pkg:deb/ubuntu/zlib1g-dev@1%3A1.3.dfsg-3.1ubuntu2.1

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
    ✔✔✔✔  pkg:golang/stdlib@1.26.4
    ✔✔✔✔  pkg:golang/stdlib@1.26.5

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
  │ ✘✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·
  │ ✘✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-3442          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ V:UB:CVE-2025-69644
  │ ✘✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✔✘✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69646
  │ ✘✔✘✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69647
  │ ✘✔✘✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69648
  │ ✘✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✔✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·
  │ ✘✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  │ ✘✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/binutils-common@2.42-4ubuntu2.10
  │ OGTV
  │ ✘✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·
  │ ✘✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-3442          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ V:UB:CVE-2025-69644
  │ ✘✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✔✘✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69646
  │ ✘✔✘✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69647
  │ ✘✔✘✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69648
  │ ✘✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✔✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·
  │ ✘✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  │ ✘✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/bsdutils@1%3A2.39.3-9ubuntu6.5
  │ OGTV
  │ ✘✔✘✘ CVE-2026-53612         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53614         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-27456         MEDIUM       4.7   0.1%   ·
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
  ┌─ pkg:deb/ubuntu/cpp@4%3A13.2.0-7ubuntu1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/cpp-13@13.3.0-6ubuntu2~24.04.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/cpp-13-aarch64-linux-gnu@13.3.0-6ubuntu2~24.04.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/cpp-aarch64-linux-gnu@4%3A13.2.0-7ubuntu1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
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
  │ ✔✔✔✔ CVE-2026-53910         LOW          2.1   0.3%   ·  ↳ O:UBUNTU-CVE-2026-53910,USN-8692-1 | V:UB:CVE-2026-53910
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dirmngr@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/g%2B%2B@4%3A13.2.0-7ubuntu1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/g%2B%2B-13@13.3.0-6ubuntu2~24.04.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/g%2B%2B-13-aarch64-linux-gnu@13.3.0-6ubuntu2~24.04.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/g%2B%2B-aarch64-linux-gnu@4%3A13.2.0-7ubuntu1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc@4%3A13.2.0-7ubuntu1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc-13@13.3.0-6ubuntu2~24.04.1
  │ OGTV
  │ ✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-102010
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc-13-aarch64-linux-gnu@13.3.0-6ubuntu2~24.04.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc-13-base@13.3.0-6ubuntu2~24.04.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc-aarch64-linux-gnu@4%3A13.2.0-7ubuntu1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gnupg@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gnupg-l10n@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gnupg-utils@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg-agent@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg-wks-client@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpgconf@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpgsm@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  │ ✘✔✘✔ CVE-2026-57062         LOW          2.9   0.1%   ·  ↳ V:UB:CVE-2026-57062
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpgv@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gzip@1.12-1ubuntu3.1
  │ OGTV
  │ ✔✔✔✔ CVE-2026-41992         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-41992,USN-8512-1 | V:UB:CVE-2026-41992
  │ ✔✔✔✔ CVE-2026-41991         MEDIUM       4.7   0.1%   ·  ↳ O:UBUNTU-CVE-2026-41991,USN-8512-1 | V:UB:CVE-2026-41991
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/keyboxd@2.4.4-2ubuntu17.4
  │ OGTV
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57062         LOW          2.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libacl1@2.3.2-1build1.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-54369         HIGH         8.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-54370         HIGH         7.2   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libaom3@3.8.2-2ubuntu0.1
  │ OGTV
  │ ✘✔✘✔ CVE-2026-56208         HIGH         7.6   0.4%   ·  ↳ V:UB:CVE-2026-56208
  │ ✘✔✘✔ CVE-2026-56209         HIGH         7.1   0.6%   ·  ↳ V:UB:CVE-2026-56209
  │ ✘✔✘✔ CVE-2026-56210         HIGH         7.1   0.6%   ·  ↳ V:UB:CVE-2026-56210
  │ ✘✔✘✔ CVE-2026-56211         HIGH         7.1   0.9%   ·  ↳ V:UB:CVE-2026-56211
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libattr1@1%3A2.5.2-1build1.1
  │ OGTV
  │ ✘✔✘✔ CVE-2026-54371         HIGH         8.4   0.1%   ·  ↳ V:UB:CVE-2026-54371
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libbinutils@2.42-4ubuntu2.10
  │ OGTV
  │ ✘✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·
  │ ✘✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-3442          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ V:UB:CVE-2025-69644
  │ ✘✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✔✘✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69646
  │ ✘✔✘✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69647
  │ ✘✔✘✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69648
  │ ✘✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✔✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·
  │ ✘✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  │ ✘✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libblkid1@2.39.3-9ubuntu6.5
  │ OGTV
  │ ✘✔✘✘ CVE-2026-53612         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53614         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-27456         MEDIUM       4.7   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libbz2-1.0@1.0.8-5.1build0.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-42250         MEDIUM       4.8   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc-bin@2.39-0ubuntu8.8
  │ OGTV
  │ ✘✔✘✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·
  │ ✘✔✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·
  │ ✘✔✘✘ CVE-2026-19499         HIGH         7.7   0.3%   ·
  │ ✘✔✘✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ V:UB:CVE-2026-18374
  │ ✘✔✘✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·
  │ ✘✔✘✔ CVE-2026-89092         MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-89092
  │ ✘✔✘✘ CVE-2026-6368          LOW          2.1   0.1%   ·
  │ ✘✔✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc-dev-bin@2.39-0ubuntu8.8
  │ OGTV
  │ ✘✔✘✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·
  │ ✘✔✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·
  │ ✘✔✘✘ CVE-2026-19499         HIGH         7.7   0.3%   ·
  │ ✘✔✘✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ V:UB:CVE-2026-18374
  │ ✘✔✘✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·
  │ ✘✔✘✔ CVE-2026-89092         MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-89092
  │ ✘✔✘✘ CVE-2026-6368          LOW          2.1   0.1%   ·
  │ ✘✔✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc-devtools@2.39-0ubuntu8.8
  │ OGTV
  │ ✘✔✘✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·
  │ ✘✔✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·
  │ ✘✔✘✘ CVE-2026-19499         HIGH         7.7   0.3%   ·
  │ ✘✔✘✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ V:UB:CVE-2026-18374
  │ ✘✔✘✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·
  │ ✘✔✘✔ CVE-2026-89092         MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-89092
  │ ✘✔✘✘ CVE-2026-6368          LOW          2.1   0.1%   ·
  │ ✘✔✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc6@2.39-0ubuntu8.8
  │ OGTV
  │ ✘✔✘✔ CVE-2026-6791          CRITICAL     9.0   0.2%   ·  ↳ V:UB:CVE-2026-6791
  │ ✘✔✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·
  │ ✘✔✘✔ CVE-2026-19499         HIGH         7.7   0.3%   ·  ↳ V:UB:CVE-2026-19499
  │ ✘✔✘✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ V:UB:CVE-2026-18374
  │ ✘✔✘✔ CVE-2026-19542         MEDIUM       5.6   0.2%   ·  ↳ V:UB:CVE-2026-19542
  │ ✘✔✘✔ CVE-2026-77117         MEDIUM       5.9   0.4%   ·  ↳ V:UB:CVE-2026-77117
  │ ✘✔✘✔ CVE-2026-80489         MEDIUM       5.9   0.4%   ·  ↳ V:UB:CVE-2026-80489
  │ ✘✔✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·
  │ ✘✔✘✔ CVE-2026-89092         MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-89092
  │ ✘✔✘✔ CVE-2026-6368          LOW          2.1   0.1%   ·  ↳ V:UB:CVE-2026-6368
  │ ✘✔✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc6-dev@2.39-0ubuntu8.8
  │ OGTV
  │ ✘✔✘✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·
  │ ✘✔✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·
  │ ✘✔✘✘ CVE-2026-19499         HIGH         7.7   0.3%   ·
  │ ✘✔✘✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ V:UB:CVE-2026-18374
  │ ✘✔✘✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·
  │ ✘✔✘✔ CVE-2026-89092         MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-89092
  │ ✘✔✘✘ CVE-2026-6368          LOW          2.1   0.1%   ·
  │ ✘✔✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libctf-nobfd0@2.42-4ubuntu2.10
  │ OGTV
  │ ✘✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·
  │ ✘✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-3442          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ V:UB:CVE-2025-69644
  │ ✘✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✔✘✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69646
  │ ✘✔✘✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69647
  │ ✘✔✘✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69648
  │ ✘✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✔✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·
  │ ✘✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  │ ✘✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libctf0@2.42-4ubuntu2.10
  │ OGTV
  │ ✘✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·
  │ ✘✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-3442          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ V:UB:CVE-2025-69644
  │ ✘✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✔✘✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69646
  │ ✘✔✘✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69647
  │ ✘✔✘✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69648
  │ ✘✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✔✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·
  │ ✘✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  │ ✘✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libcurl4t64@8.5.0-2ubuntu10.11
  │ OGTV
  │ ✘✔✘✔ CVE-2026-11856         CRITICAL     9.8   0.7%   ·  ↳ V:UB:CVE-2026-11856
  │ ✘✔✘✔ CVE-2026-18924         CRITICAL     9.1   0.6%   ·  ↳ V:UB:CVE-2026-18924
  │ ✘✔✘✔ CVE-2026-13608         HIGH         7.4   0.5%   ·  ↳ V:UB:CVE-2026-13608
  │ ✘✔✘✔ CVE-2026-80230         HIGH         7.5   0.4%   ·  ↳ V:UB:CVE-2026-80230
  │ ✘✔✘✔ CVE-2026-82209         HIGH         8.2   0.4%   ·  ↳ V:UB:CVE-2026-82209
  │ ✘✔✘✔ CVE-2026-8932          HIGH         7.5   0.4%   ·  ↳ V:UB:CVE-2026-8932
  │ ✘✘✘✔ CVE-2026-86409         ?            0.0      -   ·  ↳ V:UB:CVE-2026-86409
  │ ✘✘✘✔ CVE-2026-86414         ?            0.0      -   ·  ↳ V:UB:CVE-2026-86414
  │ ✘✘✘✔ CVE-2026-87862         ?            0.0      -   ·  ↳ V:UB:CVE-2026-87862
  │ ✘✘✘✔ CVE-2026-87863         ?            0.0      -   ·  ↳ V:UB:CVE-2026-87863
  │ ✘✘✘✔ CVE-2026-87864         ?            0.0      -   ·  ↳ V:UB:CVE-2026-87864
  │ ✘✘✘✔ CVE-2026-92388         ?            0.0      -   ·  ↳ V:UB:CVE-2026-92388
  │ ✘✘✘✔ CVE-2026-92389         ?            0.0      -   ·  ↳ V:UB:CVE-2026-92389
  │ ✘✘✘✔ CVE-2026-92391         ?            0.0      -   ·  ↳ V:UB:CVE-2026-92391
  │ ✘✘✘✔ CVE-2026-94266         ?            0.0      -   ·  ↳ V:UB:CVE-2026-94266
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libexpat1@2.6.1-2ubuntu0.4
  │ OGTV
  │ ✘✔✘✔ CVE-2025-59375         HIGH         7.5   1.3%   ·  ↳ V:UB:CVE-2025-59375
  │ ✘✔✘✘ CVE-2026-102633        HIGH         8.2   0.3%   ·
  │ ✘✔✘✔ CVE-2026-41080         HIGH         7.5   0.4%   ·  ↳ V:UB:CVE-2026-41080
  │ ✘✔✘✔ CVE-2026-45186         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-45186
  │ ✘✔✘✔ CVE-2026-66046         HIGH         8.7   0.7%   ·  ↳ V:UB:CVE-2026-66046
  │ ✘✔✘✔ CVE-2026-76641         HIGH         8.7   0.4%   ·  ↳ V:UB:CVE-2026-76641
  │ ✘✔✘✔ CVE-2026-76957         HIGH         7.8   0.1%   ·  ↳ V:UB:CVE-2026-76957
  │ ✘✔✘✘ CVE-2026-77214         HIGH         8.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-93990         HIGH         8.7   0.4%   ·
  │ ✘✔✘✔ CVE-2025-66382         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-66382
  │ ✘✔✘✔ CVE-2026-32776         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-32776
  │ ✘✔✘✔ CVE-2026-32777         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-32777
  │ ✘✔✘✔ CVE-2026-32778         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-32778
  │ ✘✔✘✔ CVE-2026-50219         MEDIUM       5.9   0.2%   ·  ↳ V:UB:CVE-2026-50219
  │ ✘✔✘✔ CVE-2026-56131         MEDIUM       4.9   0.2%   ·  ↳ V:UB:CVE-2026-56131
  │ ✘✔✘✔ CVE-2026-56132         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56132
  │ ✘✔✘✔ CVE-2026-56403         MEDIUM       6.9   0.2%   ·  ↳ V:UB:CVE-2026-56403
  │ ✘✔✘✔ CVE-2026-56404         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56404
  │ ✘✔✘✔ CVE-2026-56405         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56405
  │ ✘✔✘✔ CVE-2026-56406         MEDIUM       6.9   0.2%   ·  ↳ V:UB:CVE-2026-56406
  │ ✘✔✘✔ CVE-2026-56407         MEDIUM       6.9   0.2%   ·  ↳ V:UB:CVE-2026-56407
  │ ✘✔✘✔ CVE-2026-56408         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56408
  │ ✘✔✘✔ CVE-2026-56409         MEDIUM       6.5   0.1%   ·  ↳ V:UB:CVE-2026-56409
  │ ✘✔✘✔ CVE-2026-56410         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56410
  │ ✘✔✘✔ CVE-2026-56411         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56411
  │ ✘✔✘✔ CVE-2026-56412         MEDIUM       5.9   0.2%   ·  ↳ V:UB:CVE-2026-56412
  │ ✘✔✘✔ CVE-2026-72522         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2026-72522
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libexpat1-dev@2.6.1-2ubuntu0.4
  │ OGTV
  │ ✘✔✘✔ CVE-2025-59375         HIGH         7.5   1.3%   ·  ↳ V:UB:CVE-2025-59375
  │ ✘✔✘✘ CVE-2026-102633        HIGH         8.2   0.3%   ·
  │ ✘✔✘✔ CVE-2026-41080         HIGH         7.5   0.4%   ·  ↳ V:UB:CVE-2026-41080
  │ ✘✔✘✔ CVE-2026-45186         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-45186
  │ ✘✔✘✔ CVE-2026-66046         HIGH         8.7   0.7%   ·  ↳ V:UB:CVE-2026-66046
  │ ✘✔✘✔ CVE-2026-76641         HIGH         8.7   0.4%   ·  ↳ V:UB:CVE-2026-76641
  │ ✘✔✘✔ CVE-2026-76957         HIGH         7.8   0.1%   ·  ↳ V:UB:CVE-2026-76957
  │ ✘✔✘✘ CVE-2026-77214         HIGH         8.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-93990         HIGH         8.7   0.4%   ·
  │ ✘✔✘✔ CVE-2025-66382         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-66382
  │ ✘✔✘✔ CVE-2026-32776         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-32776
  │ ✘✔✘✔ CVE-2026-32777         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-32777
  │ ✘✔✘✔ CVE-2026-32778         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-32778
  │ ✘✔✘✔ CVE-2026-50219         MEDIUM       5.9   0.2%   ·  ↳ V:UB:CVE-2026-50219
  │ ✘✔✘✔ CVE-2026-56131         MEDIUM       4.9   0.2%   ·  ↳ V:UB:CVE-2026-56131
  │ ✘✔✘✔ CVE-2026-56132         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56132
  │ ✘✔✘✔ CVE-2026-56403         MEDIUM       6.9   0.2%   ·  ↳ V:UB:CVE-2026-56403
  │ ✘✔✘✔ CVE-2026-56404         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56404
  │ ✘✔✘✔ CVE-2026-56405         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56405
  │ ✘✔✘✔ CVE-2026-56406         MEDIUM       6.9   0.2%   ·  ↳ V:UB:CVE-2026-56406
  │ ✘✔✘✔ CVE-2026-56407         MEDIUM       6.9   0.2%   ·  ↳ V:UB:CVE-2026-56407
  │ ✘✔✘✔ CVE-2026-56408         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56408
  │ ✘✔✘✔ CVE-2026-56409         MEDIUM       6.5   0.1%   ·  ↳ V:UB:CVE-2026-56409
  │ ✘✔✘✔ CVE-2026-56410         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56410
  │ ✘✔✘✔ CVE-2026-56411         MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2026-56411
  │ ✘✔✘✔ CVE-2026-56412         MEDIUM       5.9   0.2%   ·  ↳ V:UB:CVE-2026-56412
  │ ✘✔✘✔ CVE-2026-72522         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2026-72522
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libfreetype6@2.13.2%2Bdfsg-1ubuntu0.1
  │ OGTV
  │ ✘✔✘✔ CVE-2026-95512         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-95512
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgcc-13-dev@13.3.0-6ubuntu2~24.04.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgcrypt20@1.10.3-2ubuntu0.1
  │ OGTV
  │ ✔✔✔✔ CVE-2024-2236          MEDIUM       5.9   1.1%   ·  ↳ O:UBUNTU-CVE-2024-2236,USN-8711-1 | V:UB:CVE-2024-2236
  │ ✘✘✘✔ CVE-2026-41990         MEDIUM       4.0   0.2%   ·  ↳ V:UB:CVE-2026-41990
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgd3@2.3.3-9ubuntu5
  │ OGTV
  │ ✘✔✘✘ CVE-2026-9672          ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgnutls30t64@3.8.3-1.1ubuntu3.6
  │ OGTV
  │ ✘✔✘✔ CVE-2026-88647         CRITICAL     9.1   0.2%   ·  ↳ V:UB:CVE-2026-88647
  │ ✘✔✘✔ CVE-2026-95210         CRITICAL     9.1   0.2%   ·  ↳ V:UB:CVE-2026-95210
  │ ✘✔✘✔ CVE-2026-67693         HIGH         7.5   0.2%   ·  ↳ V:UB:CVE-2026-67693
  │ ✘✔✘✔ CVE-2026-95184         HIGH         7.5   0.2%   ·  ↳ V:UB:CVE-2026-95184
  │ ✘✔✘✔ CVE-2026-95209         HIGH         7.5   0.3%   ·  ↳ V:UB:CVE-2026-95209
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgprofng0@2.42-4ubuntu2.10
  │ OGTV
  │ ✘✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·
  │ ✘✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-3442          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ V:UB:CVE-2025-69644
  │ ✘✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✔✘✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69646
  │ ✘✔✘✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69647
  │ ✘✔✘✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69648
  │ ✘✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✔✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·
  │ ✘✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  │ ✘✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libheif-plugin-aomdec@1.17.6-1ubuntu4.6
  │ OGTV
  │ ✘✔✘✔ CVE-2026-84384         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-84384
  │ ✘✔✘✔ CVE-2026-84447         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-84447
  │ ✘✔✘✔ CVE-2026-62289         MEDIUM       4.3   0.3%   ·  ↳ V:UB:CVE-2026-62289
  │ ✘✔✘✔ CVE-2026-62291         MEDIUM       5.3   0.2%   ·  ↳ V:UB:CVE-2026-62291
  │ ✘✔✘✔ CVE-2026-84448         MEDIUM       4.0   0.2%   ·  ↳ V:UB:CVE-2026-84448
  │ ✘✔✘✔ CVE-2026-84449         LOW          3.7   0.4%   ·  ↳ V:UB:CVE-2026-84449
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libheif-plugin-aomenc@1.17.6-1ubuntu4.6
  │ OGTV
  │ ✘✔✘✔ CVE-2026-84384         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-84384
  │ ✘✔✘✔ CVE-2026-84447         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-84447
  │ ✘✔✘✔ CVE-2026-62289         MEDIUM       4.3   0.3%   ·  ↳ V:UB:CVE-2026-62289
  │ ✘✔✘✔ CVE-2026-62291         MEDIUM       5.3   0.2%   ·  ↳ V:UB:CVE-2026-62291
  │ ✘✔✘✔ CVE-2026-84448         MEDIUM       4.0   0.2%   ·  ↳ V:UB:CVE-2026-84448
  │ ✘✔✘✔ CVE-2026-84449         LOW          3.7   0.4%   ·  ↳ V:UB:CVE-2026-84449
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libheif1@1.17.6-1ubuntu4.6
  │ OGTV
  │ ✘✔✘✔ CVE-2026-84384         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-84384
  │ ✘✔✘✔ CVE-2026-84447         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-84447
  │ ✘✔✘✔ CVE-2026-62289         MEDIUM       4.3   0.3%   ·  ↳ V:UB:CVE-2026-62289
  │ ✘✔✘✔ CVE-2026-62291         MEDIUM       5.3   0.2%   ·  ↳ V:UB:CVE-2026-62291
  │ ✘✔✘✔ CVE-2026-84448         MEDIUM       4.0   0.2%   ·  ↳ V:UB:CVE-2026-84448
  │ ✘✔✘✔ CVE-2026-84449         LOW          3.7   0.4%   ·  ↳ V:UB:CVE-2026-84449
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libhwasan0@14.2.0-4ubuntu2~24.04.1
  │ OGTV
  │ ✘✘✘✔ CVE-2021-3826          MEDIUM       6.5   1.4%   ·  ↳ V:UB:CVE-2021-3826
  │ ✘✘✘✔ CVE-2021-46195         MEDIUM       5.5   0.8%   ·  ↳ V:UB:CVE-2021-46195
  │ ✘✘✘✔ CVE-2022-27943         MEDIUM       5.5   1.0%   ·  ↳ V:UB:CVE-2022-27943
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libjpeg-turbo8@2.1.5-2ubuntu2
  │ OGTV
  │ ✘✔✘✘ CVE-2018-10126         MEDIUM       6.5   1.8%   ·
  │ ✘✔✘✘ CVE-2026-75466         MEDIUM       6.5   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libmount1@2.39.3-9ubuntu6.5
  │ OGTV
  │ ✘✔✘✘ CVE-2026-53612         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53614         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-27456         MEDIUM       4.7   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libncursesw6@6.4%2B20240113-1ubuntu2
  │ OGTV
  │ ✘✔✘✔ CVE-2025-69720         CRITICAL     9.8   0.4%   ·  ↳ V:UB:CVE-2025-69720
  │ ✘✔✘✘ CVE-2025-6141          MEDIUM       4.8   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libp11-kit0@0.25.3-4ubuntu2.1
  │ OGTV
  │ ✘✔✘✔ CVE-2026-13757         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2026-13757
  │ ✘✔✘✔ CVE-2026-18938         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2026-18938
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-modules@1.5.3-5ubuntu5.5
  │ OGTV
  │ ✘✔✘✔ CVE-2026-54411         HIGH         8.2   0.5%   ·  ↳ V:UB:CVE-2026-54411
  │ ✘✔✘✘ CVE-2024-10041         MEDIUM       4.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-modules-bin@1.5.3-5ubuntu5.5
  │ OGTV
  │ ✘✔✘✘ CVE-2026-54411         HIGH         8.2   0.5%   ·
  │ ✘✔✘✘ CVE-2024-10041         MEDIUM       4.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-runtime@1.5.3-5ubuntu5.5
  │ OGTV
  │ ✘✔✘✘ CVE-2026-54411         HIGH         8.2   0.5%   ·
  │ ✘✔✘✘ CVE-2024-10041         MEDIUM       4.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam0g@1.5.3-5ubuntu5.5
  │ OGTV
  │ ✘✔✘✘ CVE-2026-54411         HIGH         8.2   0.5%   ·
  │ ✘✔✘✘ CVE-2024-10041         MEDIUM       4.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpcre2-8-0@10.42-4ubuntu2.1
  │ OGTV
  │ ✘✔✘✔ CVE-2026-103111        HIGH         7.6   0.2%   ·  ↳ V:UB:CVE-2026-103111
  │ ✘✔✘✔ CVE-2026-86145         HIGH         8.2   0.4%   ·  ↳ V:UB:CVE-2026-86145
  │ ✘✔✘✔ CVE-2026-89157         HIGH         7.4   0.3%   ·  ↳ V:UB:CVE-2026-89157
  │ ✘✔✘✔ CVE-2026-89161         HIGH         7.8   0.1%   ·  ↳ V:UB:CVE-2026-89161
  │ ✘✔✘✔ CVE-2026-89156         MEDIUM       5.9   0.3%   ·  ↳ V:UB:CVE-2026-89156
  │ ✘✔✘✔ CVE-2026-89158         MEDIUM       6.5   0.2%   ·  ↳ V:UB:CVE-2026-89158
  │ ✘✔✘✔ CVE-2026-89160         MEDIUM       6.5   0.3%   ·  ↳ V:UB:CVE-2026-89160
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libperl5.38t64@5.38.2-3.2ubuntu0.3
  │ OGTV
  │ ✘✔✘✘ CVE-2026-12087         CRITICAL     9.1   0.4%   ·
  │ ✘✔✘✘ CVE-2026-13221         CRITICAL     9.1   0.4%   ·
  │ ✘✔✘✘ CVE-2026-57433         CRITICAL     9.8   0.4%   ·
  │ ✘✔✘✘ CVE-2026-48959         HIGH         7.5   0.6%   ·
  │ ✘✔✘✘ CVE-2026-48962         HIGH         7.8   0.5%   ·
  │ ✘✔✘✘ CVE-2026-57432         HIGH         8.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-7017          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-82560         HIGH         7.5   0.6%   ·
  │ ✘✔✘✘ CVE-2026-9538          HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15649         MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✔ CVE-2026-15534         MEDIUM       5.7   0.3%   ·  ↳ V:UB:CVE-2026-15534
  │ ✘✔✘✔ CVE-2026-19487         MEDIUM       5.3   0.4%   ·  ↳ V:UB:CVE-2026-19487
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpng16-16t64@1.6.43-5ubuntu0.6
  │ OGTV
  │ ✘✔✘✔ CVE-2026-46675         ?            0.0      -   ·  ↳ V:UB:CVE-2026-46675
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.12-dev@3.12.3-1ubuntu0.15
  │ OGTV
  │ ✘✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.4%   ·
  │ ✘✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·
  │ ✘✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·
  │ ✘✔✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·
  │ ✘✔✘✘ CVE-2026-19553         HIGH         7.6   0.4%   ·
  │ ✘✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·
  │ ✘✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.6%   ·
  │ ✘✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·
  │ ✘✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-4360          MEDIUM       5.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·
  │ ✘✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.5%   ·
  │ ✘✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.12-minimal@3.12.3-1ubuntu0.15
  │ OGTV
  │ ✘✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.4%   ·
  │ ✘✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·
  │ ✘✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·
  │ ✘✔✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·
  │ ✘✔✘✘ CVE-2026-19553         HIGH         7.6   0.4%   ·
  │ ✘✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·
  │ ✘✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.6%   ·
  │ ✘✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·
  │ ✘✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-4360          MEDIUM       5.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·
  │ ✘✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.5%   ·
  │ ✘✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.12-stdlib@3.12.3-1ubuntu0.15
  │ OGTV
  │ ✘✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.4%   ·
  │ ✘✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·
  │ ✘✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·
  │ ✘✔✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·
  │ ✘✔✘✘ CVE-2026-19553         HIGH         7.6   0.4%   ·
  │ ✘✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·
  │ ✘✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.6%   ·
  │ ✘✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·
  │ ✘✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-4360          MEDIUM       5.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·
  │ ✘✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.5%   ·
  │ ✘✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.12t64@3.12.3-1ubuntu0.15
  │ OGTV
  │ ✘✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.4%   ·
  │ ✘✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·
  │ ✘✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·
  │ ✘✔✘✔ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ V:UB:CVE-2026-15308
  │ ✘✔✘✘ CVE-2026-19553         HIGH         7.6   0.4%   ·
  │ ✘✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·
  │ ✘✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.6%   ·
  │ ✘✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·
  │ ✘✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·
  │ ✘✔✘✔ CVE-2026-4360          MEDIUM       5.3   0.5%   ·  ↳ V:UB:CVE-2026-4360
  │ ✘✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·
  │ ✘✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.5%   ·
  │ ✘✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsasl2-2@2.1.28%2Bdfsg1-5ubuntu3.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-107161        HIGH         7.5   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsasl2-modules@2.1.28%2Bdfsg1-5ubuntu3.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-107161        HIGH         7.5   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsasl2-modules-db@2.1.28%2Bdfsg1-5ubuntu3.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-107161        HIGH         7.5   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsframe1@2.42-4ubuntu2.10
  │ OGTV
  │ ✘✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·
  │ ✘✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-3442          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✔ CVE-2025-69644         MEDIUM       5.0   0.1%   ·  ↳ V:UB:CVE-2025-69644
  │ ✘✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✔✘✔ CVE-2025-69646         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69646
  │ ✘✔✘✔ CVE-2025-69647         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69647
  │ ✘✔✘✔ CVE-2025-69648         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69648
  │ ✘✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✔✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·
  │ ✘✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  │ ✘✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsmartcols1@2.39.3-9ubuntu6.5
  │ OGTV
  │ ✘✔✘✘ CVE-2026-53612         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53614         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-27456         MEDIUM       4.7   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsqlite3-0@3.45.1-1ubuntu2.7
  │ OGTV
  │ ✘✔✘✔ CVE-2026-39113         MEDIUM       4.0   0.2%   ·  ↳ V:UB:CVE-2026-39113
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libssh-4@0.10.6-2ubuntu0.4
  │ OGTV
  │ ✘✔✘✔ CVE-2026-59847         HIGH         7.5   0.3%   ·  ↳ V:UB:CVE-2026-59847
  │ ✘✔✘✔ CVE-2026-59850         HIGH         7.5   0.3%   ·  ↳ V:UB:CVE-2026-59850
  │ ✘✔✘✔ CVE-2026-59843         MEDIUM       6.5   0.7%   ·  ↳ V:UB:CVE-2026-59843
  │ ✘✔✘✔ CVE-2026-59845         MEDIUM       5.9   0.1%   ·  ↳ V:UB:CVE-2026-59845
  │ ✘✔✘✔ CVE-2026-59848         MEDIUM       5.3   0.3%   ·  ↳ V:UB:CVE-2026-59848
  │ ✘✔✘✔ CVE-2026-59846         LOW          3.9   0.1%   ·  ↳ V:UB:CVE-2026-59846
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libssl3t64@3.0.13-0ubuntu3.12
  │ OGTV
  │ ✘✔✘✔ CVE-2026-75803         CRITICAL     9.1   0.2%   ·  ↳ V:UB:CVE-2026-75803
  │ ✘✔✘✔ CVE-2026-54874         HIGH         7.5   0.6%   ·  ↳ V:UB:CVE-2026-54874
  │ ✘✔✘✔ CVE-2026-63072         HIGH         7.5   0.9%   ·  ↳ V:UB:CVE-2026-63072
  │ ✘✔✘✔ CVE-2026-63076         HIGH         7.5   1.6%   ·  ↳ V:UB:CVE-2026-63076
  │ ✘✔✘✔ CVE-2026-84782         HIGH         8.2   0.4%   ·  ↳ V:UB:CVE-2026-84782
  │ ✘✔✘✔ CVE-2026-35189         MEDIUM       5.3   0.3%   ·  ↳ V:UB:CVE-2026-35189
  │ ✘✔✘✔ CVE-2026-63074         MEDIUM       5.9   0.6%   ·  ↳ V:UB:CVE-2026-63074
  │ ✘✔✘✔ CVE-2026-75805         MEDIUM       5.3   0.2%   ·  ↳ V:UB:CVE-2026-75805
  │ ✘✔✘✔ CVE-2026-75806         MEDIUM       5.3   0.4%   ·  ↳ V:UB:CVE-2026-75806
  │ ✘✔✘✔ CVE-2026-54872         LOW          3.7   0.3%   ·  ↳ V:UB:CVE-2026-54872
  │ ✘✔✘✔ CVE-2026-77696         LOW          3.7   0.2%   ·  ↳ V:UB:CVE-2026-77696
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libstdc%2B%2B-13-dev@13.3.0-6ubuntu2~24.04.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsystemd0@255.4-1ubuntu8.16
  │ OGTV
  │ ✘✔✘✘ CVE-2026-15059         MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-16742         MEDIUM       6.7   0.1%   ·
  │ ✘✔✘✔ CVE-2026-40228         LOW          3.3   0.1%   ·  ↳ V:UB:CVE-2026-40228
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libtiff6@4.5.1%2Bgit230720-4ubuntu2.5
  │ OGTV
  │ ✘✔✘✘ CVE-2026-12912         HIGH         7.3   0.4%   ·
  │ ✘✔✘✘ CVE-2026-4775          HIGH         7.8   0.4%   ·
  │ ✘✔✘✘ CVE-2026-18495         MEDIUM       6.1   0.1%   ·
  │ ✘✔✘✘ CVE-2026-36849         ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libtinfo6@6.4%2B20240113-1ubuntu2
  │ OGTV
  │ ✘✔✘✔ CVE-2025-69720         CRITICAL     9.8   0.4%   ·  ↳ V:UB:CVE-2025-69720
  │ ✘✔✘✔ CVE-2025-6141          MEDIUM       4.8   0.2%   ·  ↳ V:UB:CVE-2025-6141
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libudev1@255.4-1ubuntu8.16
  │ OGTV
  │ ✘✔✘✘ CVE-2026-15059         MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-16742         MEDIUM       6.7   0.1%   ·
  │ ✘✔✘✔ CVE-2026-40228         LOW          3.3   0.1%   ·  ↳ V:UB:CVE-2026-40228
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libuuid1@2.39.3-9ubuntu6.5
  │ OGTV
  │ ✘✔✘✘ CVE-2026-53612         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53614         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-27456         MEDIUM       4.7   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libx11-6@2%3A1.8.7-1build1
  │ OGTV
  │ ✘✔✘✔ CVE-2026-88806         HIGH         7.5   0.2%   ·  ↳ V:UB:CVE-2026-88806
  │ ✘✔✘✔ CVE-2026-94283         MEDIUM       6.5   0.2%   ·  ↳ V:UB:CVE-2026-94283
  │ ✘✔✘✔ CVE-2026-94284         MEDIUM       5.5   0.1%   ·  ↳ V:UB:CVE-2026-94284
  │ ✘✔✘✔ CVE-2026-94285         MEDIUM       5.1   0.1%   ·  ↳ V:UB:CVE-2026-94285
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libx11-data@2%3A1.8.7-1build1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-88806         HIGH         7.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-94283         MEDIUM       6.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-94284         MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-94285         MEDIUM       5.1   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libxpm4@1%3A3.5.17-1ubuntu0.24.04.1
  │ OGTV
  │ ✘✔✘✔ CVE-2026-94287         MEDIUM       5.5   0.1%   ·  ↳ V:UB:CVE-2026-94287
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/login@1%3A4.13%2Bdfsg1-4ubuntu3.2
  │ OGTV
  │ ✘✔✘✔ CVE-2024-56433         LOW          3.6   0.4%   ·  ↳ V:UB:CVE-2024-56433
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/mount@2.39.3-9ubuntu6.5
  │ OGTV
  │ ✘✔✘✘ CVE-2026-53612         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53614         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-27456         MEDIUM       4.7   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/ncurses-base@6.4%2B20240113-1ubuntu2
  │ OGTV
  │ ✘✔✘✔ CVE-2025-69720         CRITICAL     9.8   0.4%   ·  ↳ V:UB:CVE-2025-69720
  │ ✘✔✘✘ CVE-2025-6141          MEDIUM       4.8   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/ncurses-bin@6.4%2B20240113-1ubuntu2
  │ OGTV
  │ ✘✔✘✔ CVE-2025-69720         CRITICAL     9.8   0.4%   ·  ↳ V:UB:CVE-2025-69720
  │ ✘✔✘✔ CVE-2025-6141          MEDIUM       4.8   0.2%   ·  ↳ V:UB:CVE-2025-6141
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
  │ ✘✔✘✔ CVE-2024-56433         LOW          3.6   0.4%   ·  ↳ V:UB:CVE-2024-56433
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
  │ ✘✔✘✘ CVE-2026-12087         CRITICAL     9.1   0.4%   ·
  │ ✘✔✘✘ CVE-2026-13221         CRITICAL     9.1   0.4%   ·
  │ ✘✔✘✘ CVE-2026-57433         CRITICAL     9.8   0.4%   ·
  │ ✘✔✘✘ CVE-2026-48959         HIGH         7.5   0.6%   ·
  │ ✘✔✘✘ CVE-2026-48962         HIGH         7.8   0.5%   ·
  │ ✘✔✘✘ CVE-2026-57432         HIGH         8.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-7017          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-82560         HIGH         7.5   0.6%   ·
  │ ✘✔✘✘ CVE-2026-9538          HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15649         MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✔ CVE-2026-15534         MEDIUM       5.7   0.3%   ·  ↳ V:UB:CVE-2026-15534
  │ ✘✔✘✔ CVE-2026-19487         MEDIUM       5.3   0.4%   ·  ↳ V:UB:CVE-2026-19487
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/perl-modules-5.38@5.38.2-3.2ubuntu0.3
  │ OGTV
  │ ✘✔✘✔ CVE-2026-12087         CRITICAL     9.1   0.4%   ·  ↳ V:UB:CVE-2026-12087
  │ ✘✔✘✔ CVE-2026-13221         CRITICAL     9.1   0.4%   ·  ↳ V:UB:CVE-2026-13221
  │ ✘✔✘✔ CVE-2026-57433         CRITICAL     9.8   0.4%   ·  ↳ V:UB:CVE-2026-57433
  │ ✘✔✘✔ CVE-2026-48959         HIGH         7.5   0.6%   ·  ↳ V:UB:CVE-2026-48959
  │ ✘✔✘✔ CVE-2026-48962         HIGH         7.8   0.5%   ·  ↳ V:UB:CVE-2026-48962
  │ ✘✔✘✔ CVE-2026-57432         HIGH         8.4   0.2%   ·  ↳ V:UB:CVE-2026-57432
  │ ✘✔✘✔ CVE-2026-7017          HIGH         7.1   0.2%   ·  ↳ V:UB:CVE-2026-7017
  │ ✘✔✘✘ CVE-2026-82560         HIGH         7.5   0.6%   ·
  │ ✘✔✘✔ CVE-2026-9538          HIGH         7.5   0.4%   ·  ↳ V:UB:CVE-2026-9538
  │ ✘✔✘✔ CVE-2025-15649         MEDIUM       5.5   0.1%   ·  ↳ V:UB:CVE-2025-15649
  │ ✘✔✘✘ CVE-2026-15534         MEDIUM       5.7   0.3%   ·
  │ ✘✔✘✘ CVE-2026-19487         MEDIUM       5.3   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-pip@24.0%2Bdfsg-1ubuntu1.3
  │ OGTV
  │ ✘✔✘✔ CVE-2025-66418         HIGH         8.9   0.7%   ·  ↳ V:UB:CVE-2025-66418
  │ ✘✔✘✔ CVE-2025-66471         HIGH         8.9   0.7%   ·  ↳ V:UB:CVE-2025-66471
  │ ✘✔✘✔ CVE-2026-21441         HIGH         8.9   2.9%   ·  ↳ V:UB:CVE-2026-21441
  │ ✘✔✘✘ CVE-2026-44431         HIGH         8.2   0.3%   ·
  │ ✘✔✘✘ CVE-2026-44432         HIGH         8.9   0.9%   ·
  │ ✘✔✘✘ CVE-2026-57585         HIGH         7.5   0.5%   ·
  │ ✘✔✘✘ CVE-2026-8643          HIGH         8.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-97687         HIGH         8.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-97689         HIGH         8.9   0.3%   ·
  │ ✘✔✘✔ CVE-2024-35195         MEDIUM       5.6   0.3%   ·  ↳ V:UB:CVE-2024-35195
  │ ✘✔✘✘ CVE-2026-13346         MEDIUM       6.5   0.3%   ·
  │ ✘✔✘✘ CVE-2026-25645         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-3219          MEDIUM       4.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-45409         MEDIUM       6.9   0.5%   ·
  │ ✘✔✘✘ CVE-2026-6357          MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-97688         MEDIUM       6.9   0.3%   ·
  │ ✘✔✘✔ CVE-2026-1703          LOW          2.0   0.4%   ·  ↳ V:UB:CVE-2026-1703
  │ ✘✘✘✔ CVE-2026-9375          ?            0.0   0.3%   ·  ↳ V:UB:CVE-2026-9375
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-pkg-resources@68.1.2-2ubuntu1.2
  │ OGTV
  │ ✘✔✘✘ CVE-2026-59890         MEDIUM       6.1   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-setuptools@68.1.2-2ubuntu1.2
  │ OGTV
  │ ✘✔✘✘ CVE-2026-59890         MEDIUM       6.1   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-wheel@0.42.0-2
  │ OGTV
  │ ✘✔✘✔ CVE-2026-24049         HIGH         7.1   0.4%   ·  ↳ V:UB:CVE-2026-24049
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
  │ ✘✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.4%   ·
  │ ✘✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·
  │ ✘✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·
  │ ✘✔✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·
  │ ✘✔✘✘ CVE-2026-19553         HIGH         7.6   0.4%   ·
  │ ✘✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·
  │ ✘✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.6%   ·
  │ ✘✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·
  │ ✘✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-4360          MEDIUM       5.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·
  │ ✘✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.5%   ·
  │ ✘✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3.12-minimal@3.12.3-1ubuntu0.15
  │ OGTV
  │ ✘✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.4%   ·
  │ ✘✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·
  │ ✘✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·
  │ ✘✔✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·
  │ ✘✔✘✘ CVE-2026-19553         HIGH         7.6   0.4%   ·
  │ ✘✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·
  │ ✘✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.6%   ·
  │ ✘✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·
  │ ✘✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-4360          MEDIUM       5.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·
  │ ✘✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.5%   ·
  │ ✘✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·
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
  │ ✘✔✘✔ CVE-2026-85091         HIGH         8.3   0.4%   ·  ↳ V:UB:CVE-2026-85091
  │ ✘✔✘✔ CVE-2026-27171         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-27171
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/zlib1g-dev@1%3A1.3.dfsg-3.1ubuntu2.1
  │ OGTV
  │ ✘✔✘✔ CVE-2026-85091         HIGH         8.3   0.4%   ·  ↳ V:UB:CVE-2026-85091
  │ ✘✔✘✔ CVE-2026-27171         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-27171
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
  ┌─ pkg:golang/stdlib@1.26.4
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
  ┌─ pkg:golang/stdlib@1.26.5
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
