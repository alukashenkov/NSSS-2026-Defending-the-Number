# Vulnerability Comparison Report — insecureapp-20.04:latest

- **Image:** `insecureapp-20.04:latest`
- **Digest:** `sha256:ca3fa0cb11c0295b461fc4674d29bf9569df312c71dc62e468b85baab422102d`
- **SBOM:** `insecureapp-20.04.syft.cdx.json` — CycloneDX 1.7, syft 1.54.1, built 2026-10-16T12:38:24+02:00
- **Report generated:** 2026-10-16T12:40:38
- **Scanners:** OSV (api.osv.dev) · Grype (grype 0.120.1) · Trivy (trivy 0.76.0) · Vulners (vulners.com audit API v4)

## Summary

  SBOM Components (Raw):           685
  Deduplicated PURLs:              541
  Clean (0 vulns):                 335
  Vulnerable:                      206

  Scanner              |   Pkgs Scanned |  Pkgs w/ Vulns | Total Vuln IDs
  ---------------------+----------------+----------------+---------------
  OSV                  |            541 |             71 |            513
  Grype                |            541 |            201 |            688
  Trivy                |            541 |             43 |            222
  Vulners              |            541 |            169 |            533

  All 4 agree:       222     ≥2 agree:          616     Total:   755     (CVE:719 GHSA:8 Other:28)
  Exclusive to: OSV:33  Grype:77  Trivy:0  Vulners:29

## VULNERABLE PACKAGES — [O]SV [G]rype [T]rivy [V]ulners findings

  ▸ Python (PyPI) (15 packages)
    ✔✔✔✔  pkg:pypi/aiohttp@3.9.1
    ✔✔✔✔  pkg:pypi/certifi@2019.11.28
    ✔✔✔✔  pkg:pypi/cryptography@3.3.2
    ✔✔✔✔  pkg:pypi/flask@3.0.2
    ✔✔✔✔  pkg:pypi/idna@2.7
    ✔✔✔✔  pkg:pypi/idna@2.8
    ✔✔✔✔  pkg:pypi/pip@20.0.2
    ✔✘✘✘  pkg:pypi/python-apt@2.0.1%2Bubuntu0.20.4.1
    ✔✔✔✔  pkg:pypi/requests@2.19.1
    ✔✔✔✔  pkg:pypi/requests@2.22.0
    ✔✔✔✔  pkg:pypi/setuptools@45.2.0
    ✔✔✔✔  pkg:pypi/urllib3@1.23
    ✔✔✔✔  pkg:pypi/urllib3@1.25.8
    ✔✔✔✔  pkg:pypi/werkzeug@3.0.6
    ✔✔✔✔  pkg:pypi/wheel@0.34.2

  ▸ Debian/Ubuntu (deb) (157 packages)
    ✔✔✘✔  pkg:deb/ubuntu/binutils@2.34-6ubuntu1.11
    ✘✔✘✔  pkg:deb/ubuntu/binutils-aarch64-linux-gnu@2.34-6ubuntu1.11
    ✘✔✘✔  pkg:deb/ubuntu/binutils-common@2.34-6ubuntu1.11
    ✘✔✘✔  pkg:deb/ubuntu/bsdutils@1%3A2.34-0.1ubuntu9.6
    ✔✔✘✔  pkg:deb/ubuntu/bzip2@1.0.8-2
    ✔✔✘✘  pkg:deb/ubuntu/coreutils@8.30-3ubuntu2
    ✘✔✘✘  pkg:deb/ubuntu/cpp@4%3A9.3.0-1ubuntu2
    ✘✔✘✔  pkg:deb/ubuntu/cpp-9@9.4.0-1ubuntu1~20.04.2
    ✔✔✘✔  pkg:deb/ubuntu/curl@7.68.0-1ubuntu2.25
    ✔✔✘✔  pkg:deb/ubuntu/dash@0.5.10.2-6
    ✔✔✘✔  pkg:deb/ubuntu/dbus@1.12.16-2ubuntu2.3
    ✘✔✘✔  pkg:deb/ubuntu/dbus-user-session@1.12.16-2ubuntu2.3
    ✔✔✘✔  pkg:deb/ubuntu/diffutils@1%3A3.7-3
    ✘✔✘✘  pkg:deb/ubuntu/dirmngr@2.2.19-3ubuntu2.5
    ✘✔✘✔  pkg:deb/ubuntu/dmsetup@2%3A1.02.167-1ubuntu1
    ✔✔✘✘  pkg:deb/ubuntu/dpkg@1.19.7ubuntu3.2
    ✘✔✘✘  pkg:deb/ubuntu/dpkg-dev@1.19.7ubuntu3.2
    ✘✔✘✔  pkg:deb/ubuntu/fdisk@2.34-0.1ubuntu9.6
    ✘✔✘✘  pkg:deb/ubuntu/g%2B%2B@4%3A9.3.0-1ubuntu2
    ✘✔✘✔  pkg:deb/ubuntu/g%2B%2B-9@9.4.0-1ubuntu1~20.04.2
    ✘✔✘✘  pkg:deb/ubuntu/gcc@4%3A9.3.0-1ubuntu2
    ✘✔✘✔  pkg:deb/ubuntu/gcc-10-base@10.5.0-1ubuntu1~20.04
    ✔✔✘✔  pkg:deb/ubuntu/gcc-9@9.4.0-1ubuntu1~20.04.2
    ✘✔✘✔  pkg:deb/ubuntu/gcc-9-base@9.4.0-1ubuntu1~20.04.2
    ✘✔✘✔  pkg:deb/ubuntu/gir1.2-packagekitglib-1.0@1.1.13-2ubuntu1.1
    ✔✔✘✔  pkg:deb/ubuntu/glib-networking@2.64.2-1ubuntu0.1
    ✘✔✘✔  pkg:deb/ubuntu/glib-networking-common@2.64.2-1ubuntu0.1
    ✘✔✘✔  pkg:deb/ubuntu/glib-networking-services@2.64.2-1ubuntu0.1
    ✘✔✘✔  pkg:deb/ubuntu/gnupg@2.2.19-3ubuntu2.5
    ✘✔✘✘  pkg:deb/ubuntu/gnupg-l10n@2.2.19-3ubuntu2.5
    ✘✔✘✘  pkg:deb/ubuntu/gnupg-utils@2.2.19-3ubuntu2.5
    ✘✔✘✔  pkg:deb/ubuntu/gpg@2.2.19-3ubuntu2.5
    ✘✔✘✘  pkg:deb/ubuntu/gpg-agent@2.2.19-3ubuntu2.5
    ✘✔✘✘  pkg:deb/ubuntu/gpg-wks-client@2.2.19-3ubuntu2.5
    ✘✔✘✘  pkg:deb/ubuntu/gpg-wks-server@2.2.19-3ubuntu2.5
    ✘✔✘✘  pkg:deb/ubuntu/gpgconf@2.2.19-3ubuntu2.5
    ✘✔✘✘  pkg:deb/ubuntu/gpgsm@2.2.19-3ubuntu2.5
    ✘✔✘✘  pkg:deb/ubuntu/gpgv@2.2.19-3ubuntu2.5
    ✔✔✘✔  pkg:deb/ubuntu/gzip@1.10-0ubuntu4.1
    ✘✔✘✘  pkg:deb/ubuntu/krb5-locales@1.17-6ubuntu4.11
    ✘✔✘✘  pkg:deb/ubuntu/libacl1@2.2.53-6
    ✘✔✘✔  pkg:deb/ubuntu/libasan5@9.4.0-1ubuntu1~20.04.2
    ✘✔✘✔  pkg:deb/ubuntu/libatomic1@10.5.0-1ubuntu1~20.04
    ✘✔✘✔  pkg:deb/ubuntu/libattr1@1%3A2.4.48-5
    ✘✔✘✔  pkg:deb/ubuntu/libbinutils@2.34-6ubuntu1.11
    ✘✔✘✔  pkg:deb/ubuntu/libblkid1@2.34-0.1ubuntu9.6
    ✘✔✘✘  pkg:deb/ubuntu/libbz2-1.0@1.0.8-2
    ✘✔✘✔  pkg:deb/ubuntu/libc-bin@2.31-0ubuntu9.17
    ✘✔✘✔  pkg:deb/ubuntu/libc-dev-bin@2.31-0ubuntu9.18
    ✘✔✘✔  pkg:deb/ubuntu/libc6@2.31-0ubuntu9.18
    ✘✔✘✔  pkg:deb/ubuntu/libc6-dev@2.31-0ubuntu9.18
    ✔✔✘✔  pkg:deb/ubuntu/libcap2@1%3A2.32-1ubuntu0.2
    ✘✔✘✔  pkg:deb/ubuntu/libcap2-bin@1%3A2.32-1ubuntu0.2
    ✘✔✘✔  pkg:deb/ubuntu/libcc1-0@10.5.0-1ubuntu1~20.04
    ✘✔✘✔  pkg:deb/ubuntu/libctf-nobfd0@2.34-6ubuntu1.11
    ✘✔✘✔  pkg:deb/ubuntu/libctf0@2.34-6ubuntu1.11
    ✘✔✘✔  pkg:deb/ubuntu/libcurl4@7.68.0-1ubuntu2.25
    ✘✔✘✔  pkg:deb/ubuntu/libdbus-1-3@1.12.16-2ubuntu2.3
    ✘✔✘✔  pkg:deb/ubuntu/libdevmapper1.02.1@2%3A1.02.167-1ubuntu1
    ✘✔✘✘  pkg:deb/ubuntu/libdpkg-perl@1.19.7ubuntu3.2
    ✘✔✘✔  pkg:deb/ubuntu/libelf1@0.176-1.1ubuntu0.1
    ✘✔✘✔  pkg:deb/ubuntu/libexpat1@2.2.9-1ubuntu0.8
    ✘✔✘✔  pkg:deb/ubuntu/libexpat1-dev@2.2.9-1ubuntu0.8
    ✘✔✘✔  pkg:deb/ubuntu/libfdisk1@2.34-0.1ubuntu9.6
    ✘✔✘✔  pkg:deb/ubuntu/libgcc-9-dev@9.4.0-1ubuntu1~20.04.2
    ✘✔✘✔  pkg:deb/ubuntu/libgcc-s1@10.5.0-1ubuntu1~20.04
    ✔✔✘✔  pkg:deb/ubuntu/libgcrypt20@1.8.5-5ubuntu1.1
    ✘✔✘✔  pkg:deb/ubuntu/libglib2.0-0@2.64.6-1~ubuntu20.04.9
    ✘✔✘✔  pkg:deb/ubuntu/libglib2.0-bin@2.64.6-1~ubuntu20.04.9
    ✘✔✘✔  pkg:deb/ubuntu/libglib2.0-data@2.64.6-1~ubuntu20.04.9
    ✘✔✘✔  pkg:deb/ubuntu/libgnutls30@3.6.13-2ubuntu1.12
    ✘✔✘✔  pkg:deb/ubuntu/libgomp1@10.5.0-1ubuntu1~20.04
    ✘✔✘✘  pkg:deb/ubuntu/libgssapi-krb5-2@1.17-6ubuntu4.11
    ✘✔✘✔  pkg:deb/ubuntu/libicu66@66.1-2ubuntu2.1
    ✘✔✘✘  pkg:deb/ubuntu/libip4tc2@1.8.4-3ubuntu2.1
    ✘✔✘✔  pkg:deb/ubuntu/libitm1@10.5.0-1ubuntu1~20.04
    ✘✔✘✘  pkg:deb/ubuntu/libk5crypto3@1.17-6ubuntu4.11
    ✘✔✘✘  pkg:deb/ubuntu/libkrb5-3@1.17-6ubuntu4.11
    ✘✔✘✘  pkg:deb/ubuntu/libkrb5support0@1.17-6ubuntu4.11
    ✘✔✘✔  pkg:deb/ubuntu/liblmdb0@0.9.24-1
    ✘✔✘✔  pkg:deb/ubuntu/liblsan0@10.5.0-1ubuntu1~20.04
    ✘✔✘✔  pkg:deb/ubuntu/liblzma5@5.2.4-1ubuntu1.1
    ✘✔✘✔  pkg:deb/ubuntu/libmount1@2.34-0.1ubuntu9.6
    ✘✔✘✔  pkg:deb/ubuntu/libncurses6@6.2-0ubuntu2.1
    ✘✔✘✔  pkg:deb/ubuntu/libncursesw6@6.2-0ubuntu2.1
    ✘✔✘✔  pkg:deb/ubuntu/libnghttp2-14@1.40.0-1ubuntu0.3
    ✘✔✘✔  pkg:deb/ubuntu/libnss-systemd@245.4-4ubuntu3.24
    ✘✔✘✔  pkg:deb/ubuntu/libp11-kit0@0.23.20-1ubuntu0.1
    ✘✔✘✔  pkg:deb/ubuntu/libpackagekit-glib2-18@1.1.13-2ubuntu1.1
    ✘✔✘✔  pkg:deb/ubuntu/libpam-cap@1%3A2.32-1ubuntu0.2
    ✘✔✘✘  pkg:deb/ubuntu/libpam-modules@1.3.1-5ubuntu4.7
    ✘✔✘✘  pkg:deb/ubuntu/libpam-modules-bin@1.3.1-5ubuntu4.7
    ✘✔✘✘  pkg:deb/ubuntu/libpam-runtime@1.3.1-5ubuntu4.7
    ✘✔✘✔  pkg:deb/ubuntu/libpam-systemd@245.4-4ubuntu3.24
    ✘✔✘✘  pkg:deb/ubuntu/libpam0g@1.3.1-5ubuntu4.7
    ✘✔✘✔  pkg:deb/ubuntu/libpcre2-8-0@10.34-7ubuntu0.1
    ✘✔✘✘  pkg:deb/ubuntu/libpcre3@2%3A8.39-12ubuntu0.1
    ✘✔✘✔  pkg:deb/ubuntu/libperl5.30@5.30.0-9ubuntu0.5
    ✘✔✘✔  pkg:deb/ubuntu/libpolkit-agent-1-0@0.105-26ubuntu1.3
    ✘✔✘✔  pkg:deb/ubuntu/libpolkit-gobject-1-0@0.105-26ubuntu1.3
    ✘✔✘✔  pkg:deb/ubuntu/libpython3.8@3.8.10-0ubuntu1~20.04.18
    ✘✔✘✔  pkg:deb/ubuntu/libpython3.8-dev@3.8.10-0ubuntu1~20.04.18
    ✘✔✘✔  pkg:deb/ubuntu/libpython3.8-minimal@3.8.10-0ubuntu1~20.04.18
    ✘✔✘✔  pkg:deb/ubuntu/libpython3.8-stdlib@3.8.10-0ubuntu1~20.04.18
    ✘✔✘✘  pkg:deb/ubuntu/libsasl2-2@2.1.27%2Bdfsg-2ubuntu0.1
    ✘✔✘✘  pkg:deb/ubuntu/libsasl2-modules@2.1.27%2Bdfsg-2ubuntu0.1
    ✘✔✘✘  pkg:deb/ubuntu/libsasl2-modules-db@2.1.27%2Bdfsg-2ubuntu0.1
    ✘✔✘✔  pkg:deb/ubuntu/libsmartcols1@2.34-0.1ubuntu9.6
    ✘✔✘✔  pkg:deb/ubuntu/libsoup2.4-1@2.70.0-1ubuntu0.5
    ✘✔✘✔  pkg:deb/ubuntu/libsqlite3-0@3.31.1-4ubuntu0.7
    ✘✔✘✔  pkg:deb/ubuntu/libssh-4@0.9.3-2ubuntu2.5
    ✘✔✘✔  pkg:deb/ubuntu/libssl1.1@1.1.1f-1ubuntu2.24
    ✘✔✘✔  pkg:deb/ubuntu/libstdc%2B%2B-9-dev@9.4.0-1ubuntu1~20.04.2
    ✘✔✘✔  pkg:deb/ubuntu/libstdc%2B%2B6@10.5.0-1ubuntu1~20.04
    ✘✔✘✔  pkg:deb/ubuntu/libsystemd0@245.4-4ubuntu3.24
    ✔✔✘✔  pkg:deb/ubuntu/libtasn1-6@4.16.0-2ubuntu0.1
    ✘✔✘✔  pkg:deb/ubuntu/libtinfo6@6.2-0ubuntu2.1
    ✘✔✘✔  pkg:deb/ubuntu/libtsan0@10.5.0-1ubuntu1~20.04
    ✘✔✘✔  pkg:deb/ubuntu/libubsan1@10.5.0-1ubuntu1~20.04
    ✘✔✘✔  pkg:deb/ubuntu/libudev1@245.4-4ubuntu3.24
    ✘✔✘✔  pkg:deb/ubuntu/libuuid1@2.34-0.1ubuntu9.6
    ✔✔✘✔  pkg:deb/ubuntu/libxml2@2.9.10%2Bdfsg-5ubuntu0.20.04.10
    ✘✔✘✔  pkg:deb/ubuntu/login@1%3A4.8.1-1ubuntu5.20.04.5
    ✘✔✘✔  pkg:deb/ubuntu/mount@2.34-0.1ubuntu9.6
    ✘✔✘✔  pkg:deb/ubuntu/ncurses-base@6.2-0ubuntu2.1
    ✘✔✘✔  pkg:deb/ubuntu/ncurses-bin@6.2-0ubuntu2.1
    ✔✔✘✔  pkg:deb/ubuntu/openssl@1.1.1f-1ubuntu2.24
    ✔✔✘✔  pkg:deb/ubuntu/packagekit@1.1.13-2ubuntu1.1
    ✘✔✘✔  pkg:deb/ubuntu/packagekit-tools@1.1.13-2ubuntu1.1
    ✘✔✘✔  pkg:deb/ubuntu/passwd@1%3A4.8.1-1ubuntu5.20.04.5
    ✔✔✘✔  pkg:deb/ubuntu/patch@2.7.6-6
    ✔✔✘✔  pkg:deb/ubuntu/perl@5.30.0-9ubuntu0.5
    ✘✔✘✔  pkg:deb/ubuntu/perl-base@5.30.0-9ubuntu0.5
    ✘✔✘✔  pkg:deb/ubuntu/perl-modules-5.30@5.30.0-9ubuntu0.5
    ✔✔✘✔  pkg:deb/ubuntu/policykit-1@0.105-26ubuntu1.3
    ✘✔✘✔  pkg:deb/ubuntu/python-apt-common@2.0.1ubuntu0.20.04.1
    ✘✔✘✔  pkg:deb/ubuntu/python-pip-whl@20.0.2-5ubuntu1.11
    ✘✔✘✔  pkg:deb/ubuntu/python3-apt@2.0.1ubuntu0.20.04.1
    ✘✔✘✘  pkg:deb/ubuntu/python3-certifi@2019.11.28-1
    ✘✔✘✘  pkg:deb/ubuntu/python3-idna@2.8-1ubuntu0.1
    ✘✔✘✔  pkg:deb/ubuntu/python3-pip@20.0.2-5ubuntu1.11
    ✘✔✘✘  pkg:deb/ubuntu/python3-pkg-resources@45.2.0-1ubuntu0.3
    ✘✔✘✔  pkg:deb/ubuntu/python3-requests@2.22.0-2ubuntu1.1
    ✘✔✘✘  pkg:deb/ubuntu/python3-setuptools@45.2.0-1ubuntu0.3
    ✘✔✘✔  pkg:deb/ubuntu/python3-urllib3@1.25.8-2ubuntu0.4
    ✔✔✘✔  pkg:deb/ubuntu/python3.8@3.8.10-0ubuntu1~20.04.18
    ✘✔✘✔  pkg:deb/ubuntu/python3.8-dev@3.8.10-0ubuntu1~20.04.18
    ✘✔✘✔  pkg:deb/ubuntu/python3.8-minimal@3.8.10-0ubuntu1~20.04.18
    ✔✔✘✔  pkg:deb/ubuntu/sed@4.7-1
    ✔✔✘✔  pkg:deb/ubuntu/systemd@245.4-4ubuntu3.24
    ✘✔✘✔  pkg:deb/ubuntu/systemd-sysv@245.4-4ubuntu3.24
    ✘✔✘✔  pkg:deb/ubuntu/systemd-timesyncd@245.4-4ubuntu3.24
    ✔✔✘✔  pkg:deb/ubuntu/tar@1.30%2Bdfsg-7ubuntu0.20.04.4
    ✔✔✘✔  pkg:deb/ubuntu/util-linux@2.34-0.1ubuntu9.6
    ✔✔✘✔  pkg:deb/ubuntu/xz-utils@5.2.4-1ubuntu1.1
    ✘✔✘✔  pkg:deb/ubuntu/zlib1g@1%3A1.2.11.dfsg-2ubuntu1.5
    ✘✔✘✔  pkg:deb/ubuntu/zlib1g-dev@1%3A1.2.11.dfsg-2ubuntu1.5

  ▸ Go (34 packages)
    ✘✘✘✔  pkg:golang/github.com/aws/aws-sdk-go-v2/service/sso@v1.22.4
    ✘✘✘✔  pkg:golang/github.com/aws/aws-sdk-go-v2/service/ssooidc@v1.26.4
    ✘✘✘✔  pkg:golang/github.com/aws/aws-sdk-go-v2/service/sts@v1.30.3
    ✔✔✔✔  pkg:golang/github.com/containerd/containerd/v2@v2.0.4
    ✘✘✘✔  pkg:golang/github.com/docker/buildx@v0.23.0
    ✔✔✔✔  pkg:golang/github.com/docker/cli@v28.0.4%2Bincompatible
    ✔✔✔✔  pkg:golang/github.com/docker/cli@v28.1.0%2Bincompatible
    ✔✔✔✔  pkg:golang/github.com/docker/compose/v2@v2.35.1
    ✔✔✔✔  pkg:golang/github.com/docker/distribution@v2.8.3%2Bincompatible
    ✔✔✔✔  pkg:golang/github.com/docker/docker@v28.0.4%2Bincompatible
    ✔✔✔✔  pkg:golang/github.com/docker/docker@v28.1.0%2Bincompatible
    ✔✔✔✔  pkg:golang/github.com/go-viper/mapstructure/v2@v2.0.0
    ✔✔✔✔  pkg:golang/github.com/gorilla/websocket@v1.5.0
    ✔✔✔✔  pkg:golang/github.com/in-toto/in-toto-golang@v0.5.0
    ✔✔✘✔  pkg:golang/github.com/klauspost/compress@v1.18.0
    ✔✔✔✔  pkg:golang/github.com/moby/buildkit@v0.21.0
    ✔✔✔✔  pkg:golang/github.com/moby/go-archive@v0.1.0
    ✔✔✔✔  pkg:golang/github.com/moby/spdystream@v0.4.0
    ✔✔✔✔  pkg:golang/github.com/moby/sys/user@v0.4.0
    ✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp@v1.31.0
    ✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace@v1.31.0
    ✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc@v1.31.0
    ✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp@v1.31.0
    ✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/sdk@v1.31.0
    ✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/sdk@v1.34.0
    ✔✔✔✔  pkg:golang/golang.org/x/crypto@v0.37.0
    ✔✔✔✔  pkg:golang/golang.org/x/net@v0.39.0
    ✔✔✔✔  pkg:golang/golang.org/x/oauth2@v0.23.0
    ✔✔✔✔  pkg:golang/golang.org/x/oauth2@v0.25.0
    ✔✔✔✔  pkg:golang/golang.org/x/sys@v0.32.0
    ✔✔✔✔  pkg:golang/golang.org/x/text@v0.24.0
    ✔✔✔✔  pkg:golang/google.golang.org/grpc@v1.69.4
    ✔✔✔✔  pkg:golang/google.golang.org/grpc@v1.71.1
    ✔✔✔✔  pkg:golang/stdlib@1.23.8

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
  ┌─ pkg:pypi/certifi@2019.11.28
  │ OGTV
  │ ✔✔✔✔ CVE-2023-37920         CRITICAL     9.8   0.6%   ·  ↳ O:GHSA-xqr8-7jwr-rhp7,PYSEC-2023-135 | V:GHSA-XQR8-7JWR-RHP7
  │ ✔✔✔✔ CVE-2022-23491         HIGH         7.5   0.5%   ·  ↳ O:GHSA-43fp-rhv2-5gv8,PYSEC-2022-42986 | V:GHSA-43FP-RHV2-5GV8
  │ ✔✘✘✔ CVE-2024-39689         HIGH         7.5   1.0%   ·  ↳ O:PYSEC-2024-230 | V:OSV:PYSEC-2024-230
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
  ┌─ pkg:pypi/idna@2.8
  │ OGTV
  │ ✔✔✔✔ CVE-2024-3651          HIGH         7.5   1.4%   ·  ↳ O:GHSA-jjg7-2v4v-x38h,PYSEC-2024-60 | V:MEND:CVE-2024-3651
  │ ✔✔✔✔ CVE-2026-45409         MEDIUM       6.9   0.5%   ·  ↳ O:GHSA-65pc-fj4g-8rjx,PYSEC-2026-215 | V:MEND:CVE-2026-45409
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/pip@20.0.2
  │ OGTV
  │ ✔✔✔✔ CVE-2026-8643          HIGH         8.0   0.5%   ·  ↳ O:GHSA-wf93-45jw-7689,PYSEC-2026-196 | V:MEND:CVE-2026-8643
  │ ✔✔✔✔ CVE-2021-3572          MEDIUM       5.7   1.8%   ·  ↳ O:GHSA-5xp3-jfq3-5q8x,PYSEC-2021-437 | V:MEND:CVE-2021-3572
  │ ✔✔✔✔ CVE-2023-5752          MEDIUM       5.5   0.5%   ·  ↳ O:GHSA-mq26-g339-26xf,PYSEC-2023-228 | V:MEND:CVE-2023-5752
  │ ✔✔✔✔ CVE-2025-8869          MEDIUM       5.9   0.5%   ·  ↳ O:GHSA-4xh5-x5gv-qwph,PYSEC-2026-1795 | V:MEND:CVE-2025-8869
  │ ✔✔✔✔ CVE-2026-13346         MEDIUM       6.5   0.3%   ·  ↳ O:GHSA-qwm4-qh6w-59xr,PYSEC-2026-3721 | V:MEND:CVE-2026-13346
  │ ✔✔✔✔ CVE-2026-3219          MEDIUM       4.6   0.2%   ·  ↳ O:GHSA-58qw-9mgm-455v,PYSEC-2026-2875 | V:MEND:CVE-2026-3219
  │ ✔✔✔✔ CVE-2026-6357          MEDIUM       5.3   0.2%   ·  ↳ O:GHSA-jp4c-xjxw-mgf9,PYSEC-2026-2876 | V:MEND:CVE-2026-6357
  │ ✔✔✔✔ CVE-2026-1703          LOW          2.0   0.4%   ·  ↳ O:GHSA-6vgw-5pg2-w6jp,PYSEC-2026-1796 | V:MEND:CVE-2026-1703
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/python-apt@2.0.1%2Bubuntu0.20.4.1
  │ OGTV
  │ ✔✘✘✘ CVE-2019-15795         MEDIUM       4.7   0.5%   ·  ↳ O:GHSA-rp8m-h266-53jh
  │ ✔✘✘✘ CVE-2019-15796         MEDIUM       4.7   0.5%   ·  ↳ O:GHSA-pj65-3pf6-c5q4
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/requests@2.19.1
  │ OGTV
  │ ✔✔✔✔ CVE-2018-18074         HIGH         7.5   7.4%   ·  ↳ O:GHSA-x84v-xcm2-53pg,PYSEC-2018-28 | V:OSV:PYSEC-2018-28
  │ ✔✔✔✔ CVE-2023-32681         MEDIUM       6.1   3.0%   ·  ↳ O:GHSA-j8r2-6x86-q33q,PYSEC-2023-74 | V:GHSA-J8R2-6X86-Q33Q
  │ ✔✔✔✔ CVE-2024-35195         MEDIUM       5.6   0.3%   ·  ↳ O:GHSA-9wx4-h78v-vm56,PYSEC-2026-1873 | V:GHSA-9WX4-H78V-VM56
  │ ✔✔✔✔ CVE-2024-47081         MEDIUM       5.3   1.0%   ·  ↳ O:GHSA-9hjg-9r4m-mvj7,PYSEC-2026-1872 | V:MEND:CVE-2024-47081
  │ ✔✔✔✔ CVE-2026-25645         MEDIUM       5.5   0.2%   ·  ↳ O:GHSA-gc5v-m9x4-r6x2,PYSEC-2026-2275 | V:GHSA-GC5V-M9X4-R6X2
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/requests@2.22.0
  │ OGTV
  │ ✔✔✔✔ CVE-2023-32681         MEDIUM       6.1   3.0%   ·  ↳ O:GHSA-j8r2-6x86-q33q,PYSEC-2023-74 | V:GHSA-J8R2-6X86-Q33Q
  │ ✔✔✔✔ CVE-2024-35195         MEDIUM       5.6   0.3%   ·  ↳ O:GHSA-9wx4-h78v-vm56,PYSEC-2026-1873 | V:GHSA-9WX4-H78V-VM56
  │ ✔✔✔✔ CVE-2024-47081         MEDIUM       5.3   1.0%   ·  ↳ O:GHSA-9hjg-9r4m-mvj7,PYSEC-2026-1872 | V:MEND:CVE-2024-47081
  │ ✔✔✔✔ CVE-2026-25645         MEDIUM       5.5   0.2%   ·  ↳ O:GHSA-gc5v-m9x4-r6x2,PYSEC-2026-2275 | V:GHSA-GC5V-M9X4-R6X2
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/setuptools@45.2.0
  │ OGTV
  │ ✔✔✔✔ CVE-2024-6345          HIGH         8.8   1.9%   ·  ↳ O:GHSA-cx63-2mw6-8hw5,PYSEC-2026-1918 | V:MEND:CVE-2024-6345
  │ ✔✔✔✔ CVE-2025-47273         HIGH         8.8   1.6%   ·  ↳ O:GHSA-5rjg-fvgr-3xxf,PYSEC-2025-49 | V:MEND:CVE-2025-47273
  │ ✔✔✔✔ CVE-2022-40897         MEDIUM       5.9   2.5%   ·  ↳ O:GHSA-r9hx-vwmv-q579,PYSEC-2022-43012 | V:MEND:CVE-2022-40897
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
  ┌─ pkg:pypi/urllib3@1.25.8
  │ OGTV
  │ ✔✔✔✔ CVE-2021-33503         HIGH         7.5   3.3%   ·  ↳ O:GHSA-q2q7-5pp4-w6pg,PYSEC-2021-108 | V:GHSA-Q2Q7-5PP4-W6PG
  │ ✔✔✔✔ CVE-2023-43804         HIGH         8.1   1.4%   ·  ↳ O:GHSA-v845-jxx5-vc9f,PYSEC-2023-192 | V:GHSA-V845-JXX5-VC9F
  │ ✔✔✔✔ CVE-2025-66418         HIGH         8.9   0.7%   ·  ↳ O:GHSA-gm62-xv2j-4w53,PYSEC-2026-1998 | V:MEND:CVE-2025-66418
  │ ✔✔✔✔ CVE-2025-66471         HIGH         8.9   0.7%   ·  ↳ O:GHSA-2xpw-w6gg-jr37,PYSEC-2026-1994 | V:MEND:CVE-2025-66471
  │ ✔✔✔✔ CVE-2026-21441         HIGH         8.9   2.9%   ·  ↳ O:GHSA-38jv-5279-wg99,PYSEC-2026-1996 | V:MEND:CVE-2026-21441
  │ ✔✔✔✔ CVE-2026-44431         HIGH         8.2   0.3%   ·  ↳ O:GHSA-qccp-gfcp-xxvc,PYSEC-2026-141 | V:MEND:CVE-2026-44431
  │ ✔✔✔✔ CVE-2026-97689         HIGH         8.9   0.3%   ·  ↳ O:GHSA-vxq7-64xx-v4gw,PYSEC-2026-4177 | V:MEND:CVE-2026-97689
  │ ✔✔✔✔ CVE-2020-26137         MEDIUM       6.5   2.3%   ·  ↳ O:GHSA-wqvq-5m8c-6g24,PYSEC-2020-148 | V:GHSA-WQVQ-5M8C-6G24
  │ ✔✔✔✔ CVE-2023-45803         MEDIUM       4.2   0.5%   ·  ↳ O:GHSA-g4mx-q9vg-27p4,PYSEC-2023-212 | V:OSV:PYSEC-2023-212
  │ ✔✔✔✔ CVE-2024-37891         MEDIUM       6.5   1.1%   ·  ↳ O:GHSA-34jh-p97f-mpxf,PYSEC-2026-1995 | V:GHSA-34JH-P97F-MPXF
  │ ✔✔✔✔ CVE-2025-50181         MEDIUM       6.1   0.5%   ·  ↳ O:GHSA-pq67-6m6q-mj2v,PYSEC-2026-1999 | V:MEND:CVE-2025-50181
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/werkzeug@3.0.6
  │ OGTV
  │ ✔✔✔✔ CVE-2025-66221         MEDIUM       6.3   0.5%   ·  ↳ O:GHSA-hgf8-39gv-g3f2,PYSEC-2026-2046 | V:SNYK:PYTHON-WERKZEUG-15322677
  │ ✔✔✔✔ CVE-2026-102598        MEDIUM       6.3   0.4%   ·  ↳ O:GHSA-g6x2-hccm-hh4m,PYSEC-2026-4312 | V:OSV:PYSEC-2026-4312
  │ ✔✔✔✔ CVE-2026-21860         MEDIUM       6.3   0.5%   ·  ↳ O:GHSA-87hc-h4r5-73f7,PYSEC-2026-2044 | V:GHSA-87HC-H4R5-73F7
  │ ✔✔✔✔ CVE-2026-27199         MEDIUM       6.3   0.6%   ·  ↳ O:GHSA-29vq-49wr-vm6x,PYSEC-2026-2320 | V:GHSA-29VQ-49WR-VM6X
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/wheel@0.34.2
  │ OGTV
  │ ✔✔✔✔ CVE-2022-40898         HIGH         7.5   2.7%   ·  ↳ O:GHSA-qwmp-2cf2-g9g6,PYSEC-2022-43017 | V:MEND:CVE-2022-40898
  │ ✘✘✘✔ CVE-2026-24049         HIGH         7.1   0.4%   ·  ↳ V:MEND:CVE-2026-24049
  └────────────────────────────────────────────────────────────────────────────────────────────────────

  ━━ Debian/Ubuntu (deb) ━━
  ┌─ pkg:deb/ubuntu/binutils@2.34-6ubuntu1.11
  │ OGTV
  │ ✔✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ O:UBUNTU-CVE-2017-13716 | V:UB:CVE-2017-13716
  │ ✔✘✘✘ CVE-2025-0840          HIGH         7.5   0.7%   ·  ↳ O:USN-7899-1
  │ ✔✔✘✔ CVE-2025-11082         HIGH         7.8   0.3%   ·  ↳ O:UBUNTU-CVE-2025-11082 | V:UB:CVE-2025-11082
  │ ✔✔✘✘ CVE-2025-11083         HIGH         7.8   0.3%   ·  ↳ O:UBUNTU-CVE-2025-11083
  │ ✔✔✘✔ CVE-2025-5244          HIGH         7.8   0.3%   ·  ↳ O:UBUNTU-CVE-2025-5244,USN-7899-1 | V:UB:CVE-2025-5244
  │ ✔✔✘✔ CVE-2025-5245          HIGH         7.8   0.3%   ·  ↳ O:UBUNTU-CVE-2025-5245,USN-7899-1 | V:UB:CVE-2025-5245
  │ ✔✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2025-66862
  │ ✔✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2025-66863
  │ ✔✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-66864
  │ ✔✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2025-66865
  │ ✔✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·  ↳ O:UBUNTU-CVE-2025-66866
  │ ✔✔✘✔ CVE-2025-7545          HIGH         7.8   0.3%   ·  ↳ O:UBUNTU-CVE-2025-7545,USN-7899-1 | V:UB:CVE-2025-7545
  │ ✔✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·  ↳ O:UBUNTU-CVE-2026-3441
  │ ✔✔✘✘ CVE-2026-3442          HIGH         7.1   0.2%   ·  ↳ O:UBUNTU-CVE-2026-3442
  │ ✔✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-6846
  │ ✔✔✘✔ CVE-2019-1010204       MEDIUM       5.5   1.1%   ·  ↳ O:UBUNTU-CVE-2019-1010204 | V:UB:CVE-2019-1010204
  │ ✔✔✘✘ CVE-2021-20197         MEDIUM       6.3   0.3%   ·  ↳ O:UBUNTU-CVE-2021-20197
  │ ✔✔✘✔ CVE-2022-48064         MEDIUM       5.5   0.6%   ·  ↳ O:UBUNTU-CVE-2022-48064 | V:UB:CVE-2022-48064
  │ ✔✔✘✔ CVE-2025-11412         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-11412 | V:UB:CVE-2025-11412
  │ ✔✔✘✔ CVE-2025-11413         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-11413 | V:UB:CVE-2025-11413
  │ ✔✔✘✔ CVE-2025-11414         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-11414 | V:UB:CVE-2025-11414
  │ ✔✔✘✔ CVE-2025-11494         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-11494 | V:UB:CVE-2025-11494
  │ ✔✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-11495
  │ ✔✘✘✘ CVE-2025-1153          MEDIUM       5.9   1.4%   ·  ↳ O:USN-7899-1
  │ ✔✘✘✘ CVE-2025-1178          MEDIUM       6.3   0.8%   ·  ↳ O:UBUNTU-CVE-2025-1178
  │ ✔✘✘✔ CVE-2025-1181          MEDIUM       5.1   0.7%   ·  ↳ O:UBUNTU-CVE-2025-1181,USN-7899-1 | V:UB:CVE-2025-1181
  │ ✔✘✘✘ CVE-2025-1182          MEDIUM       5.1   0.6%   ·  ↳ O:USN-7899-1
  │ ✔✔✘✔ CVE-2025-11839         MEDIUM       5.5   0.3%   ·  ↳ O:UBUNTU-CVE-2025-11839,USN-7899-1 | V:UB:CVE-2025-11839
  │ ✔✔✘✔ CVE-2025-11840         MEDIUM       5.5   0.3%   ·  ↳ O:UBUNTU-CVE-2025-11840,USN-7899-1 | V:UB:CVE-2025-11840
  │ ✔✔✘✔ CVE-2025-3198          MEDIUM       5.5   0.3%   ·  ↳ O:UBUNTU-CVE-2025-3198,USN-7899-1 | V:UB:CVE-2025-3198
  │ ✔✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-69645 | V:UB:CVE-2025-69645
  │ ✔✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-69651 | V:UB:CVE-2025-69651
  │ ✔✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ O:UBUNTU-CVE-2025-69652 | V:UB:CVE-2025-69652
  │ ✔✔✘✔ CVE-2025-8225          MEDIUM       4.8   0.2%   ·  ↳ O:UBUNTU-CVE-2025-8225,USN-7899-1 | V:UB:CVE-2025-8225
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
  │ ✔✔✘✔ CVE-2025-1148          LOW          3.1   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1148 | V:UB:CVE-2025-1148
  │ ✔✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1149
  │ ✔✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1150
  │ ✔✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1151
  │ ✔✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1152 | V:UB:CVE-2025-1152
  │ ✔✔✘✔ CVE-2025-1180          LOW          3.1   0.7%   ·  ↳ O:UBUNTU-CVE-2025-1180 | V:UB:CVE-2025-1180
  │ ✔✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·  ↳ O:UBUNTU-CVE-2025-66861
  │ ✔✘✘✘ USN-7919-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/binutils-aarch64-linux-gnu@2.34-6ubuntu1.11
  │ OGTV
  │ ✘✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✔✘✘ CVE-2025-11082         HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-11083         HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-5244          HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-5245          HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·
  │ ✘✔✘✘ CVE-2025-7545          HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-3442          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·
  │ ✘✔✘✔ CVE-2019-1010204       MEDIUM       5.5   1.1%   ·  ↳ V:UB:CVE-2019-1010204
  │ ✘✔✘✘ CVE-2021-20197         MEDIUM       6.3   0.3%   ·
  │ ✘✔✘✔ CVE-2022-48064         MEDIUM       5.5   0.6%   ·  ↳ V:UB:CVE-2022-48064
  │ ✘✔✘✘ CVE-2025-11412         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11413         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11414         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11494         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11839         MEDIUM       5.5   0.3%   ·
  │ ✘✔✘✘ CVE-2025-11840         MEDIUM       5.5   0.3%   ·
  │ ✘✔✘✘ CVE-2025-3198          MEDIUM       5.5   0.3%   ·
  │ ✘✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✔✘✘ CVE-2025-8225          MEDIUM       4.8   0.2%   ·
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
  │ ✘✔✘✔ CVE-2025-1148          LOW          3.1   0.6%   ·  ↳ V:UB:CVE-2025-1148
  │ ✘✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·
  │ ✘✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  │ ✘✔✘✔ CVE-2025-1180          LOW          3.1   0.7%   ·  ↳ V:UB:CVE-2025-1180
  │ ✘✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/binutils-common@2.34-6ubuntu1.11
  │ OGTV
  │ ✘✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✔✘✘ CVE-2025-11082         HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-11083         HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-5244          HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-5245          HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·
  │ ✘✔✘✘ CVE-2025-7545          HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-3442          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·
  │ ✘✔✘✔ CVE-2019-1010204       MEDIUM       5.5   1.1%   ·  ↳ V:UB:CVE-2019-1010204
  │ ✘✔✘✘ CVE-2021-20197         MEDIUM       6.3   0.3%   ·
  │ ✘✔✘✔ CVE-2022-48064         MEDIUM       5.5   0.6%   ·  ↳ V:UB:CVE-2022-48064
  │ ✘✔✘✘ CVE-2025-11412         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11413         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11414         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11494         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11839         MEDIUM       5.5   0.3%   ·
  │ ✘✔✘✘ CVE-2025-11840         MEDIUM       5.5   0.3%   ·
  │ ✘✔✘✘ CVE-2025-3198          MEDIUM       5.5   0.3%   ·
  │ ✘✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✔✘✘ CVE-2025-8225          MEDIUM       4.8   0.2%   ·
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
  │ ✘✔✘✔ CVE-2025-1148          LOW          3.1   0.6%   ·  ↳ V:UB:CVE-2025-1148
  │ ✘✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·
  │ ✘✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  │ ✘✔✘✔ CVE-2025-1180          LOW          3.1   0.7%   ·  ↳ V:UB:CVE-2025-1180
  │ ✘✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/bsdutils@1%3A2.34-0.1ubuntu9.6
  │ OGTV
  │ ✘✔✘✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✔ CVE-2026-27456         MEDIUM       4.7   0.1%   ·  ↳ V:UB:CVE-2026-27456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/bzip2@1.0.8-2
  │ OGTV
  │ ✔✔✘✔ CVE-2026-42250         MEDIUM       4.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-42250,USN-8685-1 | V:UB:CVE-2026-42250
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/coreutils@8.30-3ubuntu2
  │ OGTV
  │ ✔✔✘✘ CVE-2016-2781          MEDIUM       6.5   0.4%   ·  ↳ O:UBUNTU-CVE-2016-2781
  │ ✔✔✘✘ CVE-2025-5278          MEDIUM       4.4   0.3%   ·  ↳ O:UBUNTU-CVE-2025-5278
  │ ✘✔✘✘ CVE-2026-56392         MEDIUM       6.1   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/cpp@4%3A9.3.0-1ubuntu2
  │ OGTV
  │ ✘✔✘✘ CVE-2020-23026         HIGH         7.5   1.0%   ·
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/cpp-9@9.4.0-1ubuntu1~20.04.2
  │ OGTV
  │ ✘✔✘✘ CVE-2020-23026         HIGH         7.5   1.0%   ·
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  │ ✘✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/curl@7.68.0-1ubuntu2.25
  │ OGTV
  │ ✔✔✘✔ CVE-2026-11856         CRITICAL     9.8   0.7%   ·  ↳ O:UBUNTU-CVE-2026-11856 | V:UB:CVE-2026-11856
  │ ✔✔✘✔ CVE-2026-18924         CRITICAL     9.1   0.6%   ·  ↳ O:UBUNTU-CVE-2026-18924,USN-8820-1 | V:UB:CVE-2026-18924
  │ ✔✔✘✔ CVE-2026-8924          CRITICAL     9.1   0.7%   ·  ↳ O:UBUNTU-CVE-2026-8924 | V:UB:CVE-2026-8924
  │ ✔✔✘✔ CVE-2026-8927          CRITICAL     9.1   0.5%   ·  ↳ O:UBUNTU-CVE-2026-8927,USN-8820-1 | V:UB:CVE-2026-8927
  │ ✔✘✘✘ CVE-2026-13608         HIGH         7.4   0.5%   ·  ↳ O:USN-8820-1
  │ ✔✔✘✔ CVE-2026-5773          HIGH         7.5   0.7%   ·  ↳ O:UBUNTU-CVE-2026-5773 | V:UB:CVE-2026-5773
  │ ✔✘✘✘ CVE-2026-80229         HIGH         7.5   0.6%   ·  ↳ O:USN-8820-1
  │ ✔✔✘✔ CVE-2026-80230         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-80230,USN-8820-1 | V:UB:CVE-2026-80230
  │ ✔✘✘✘ CVE-2026-80255         HIGH         7.5   0.5%   ·  ↳ O:USN-8820-1
  │ ✔✔✘✔ CVE-2026-82209         HIGH         8.2   0.4%   ·  ↳ O:UBUNTU-CVE-2026-82209,USN-8820-1 | V:UB:CVE-2026-82209
  │ ✔✔✘✔ CVE-2026-8286          HIGH         8.1   0.3%   ·  ↳ O:UBUNTU-CVE-2026-8286 | V:UB:CVE-2026-8286
  │ ✔✔✘✔ CVE-2026-8932          HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-8932,USN-8670-2 | V:UB:CVE-2026-8932
  │ ✔✘✘✘ CVE-2026-9080          HIGH         7.3   0.5%   ·  ↳ O:USN-8820-1
  │ ✔✔✘✔ CVE-2025-14017         MEDIUM       6.3   0.1%   ·  ↳ O:UBUNTU-CVE-2025-14017 | V:UB:CVE-2025-14017
  │ ✔✔✘✘ CVE-2025-14524         MEDIUM       5.3   0.7%   ·  ↳ O:UBUNTU-CVE-2025-14524
  │ ✔✔✘✔ CVE-2025-15079         MEDIUM       5.3   0.5%   ·  ↳ O:UBUNTU-CVE-2025-15079 | V:UB:CVE-2025-15079
  │ ✔✔✘✔ CVE-2026-1965          MEDIUM       6.5   0.3%   ·  ↳ O:UBUNTU-CVE-2026-1965,USN-8099-1 | V:UB:CVE-2026-1965
  │ ✔✔✘✔ CVE-2026-3783          MEDIUM       5.3   0.5%   ·  ↳ O:UBUNTU-CVE-2026-3783,USN-8099-1 | V:UB:CVE-2026-3783
  │ ✔✔✘✔ CVE-2026-3784          MEDIUM       6.5   0.5%   ·  ↳ O:UBUNTU-CVE-2026-3784,USN-8099-1 | V:UB:CVE-2026-3784
  │ ✔✔✘✘ CVE-2026-4873          MEDIUM       5.9   0.4%   ·  ↳ O:UBUNTU-CVE-2026-4873
  │ ✔✔✘✔ CVE-2026-5545          MEDIUM       6.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-5545 | V:UB:CVE-2026-5545
  │ ✔✔✘✘ CVE-2026-6253          MEDIUM       5.9   0.7%   ·  ↳ O:UBUNTU-CVE-2026-6253
  │ ✔✔✘✘ CVE-2026-6429          MEDIUM       5.3   0.5%   ·  ↳ O:UBUNTU-CVE-2026-6429
  │ ✔✔✘✔ CVE-2026-7168          MEDIUM       5.3   0.5%   ·  ↳ O:UBUNTU-CVE-2026-7168 | V:UB:CVE-2026-7168
  │ ✔✔✘✔ CVE-2026-8458          MEDIUM       6.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-8458 | V:UB:CVE-2026-8458
  │ ✔✔✘✔ CVE-2025-15224         LOW          3.1   0.5%   ·  ↳ O:UBUNTU-CVE-2025-15224 | V:UB:CVE-2025-15224
  │ ✘✘✘✔ CVE-2026-86414         ?            0.0      -   ·  ↳ V:UB:CVE-2026-86414
  │ ✘✘✘✔ CVE-2026-87864         ?            0.0      -   ·  ↳ V:UB:CVE-2026-87864
  │ ✘✘✘✔ CVE-2026-92388         ?            0.0      -   ·  ↳ V:UB:CVE-2026-92388
  │ ✘✘✘✔ CVE-2026-92389         ?            0.0      -   ·  ↳ V:UB:CVE-2026-92389
  │ ✘✘✘✔ CVE-2026-92391         ?            0.0      -   ·  ↳ V:UB:CVE-2026-92391
  │ ✘✘✘✔ CVE-2026-94266         ?            0.0      -   ·  ↳ V:UB:CVE-2026-94266
  │ ✔✘✘✘ USN-8062-2             ?             -       -   ·
  │ ✔✘✘✘ USN-8487-1             ?             -       -   ·
  │ ✔✘✘✘ USN-8525-1             ?             -       -   ·
  │ ✔✘✘✘ USN-8651-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dash@0.5.10.2-6
  │ OGTV
  │ ✘✔✘✘ CVE-2026-91187         CRITICAL     9.3   0.3%   ·
  │ ✔✔✘✔ CVE-2026-102473        MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-102473 | V:UB:CVE-2026-102473
  │ ✔✔✘✔ CVE-2026-102474        MEDIUM       4.0   0.1%   ·  ↳ O:UBUNTU-CVE-2026-102474 | V:UB:CVE-2026-102474
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dbus@1.12.16-2ubuntu2.3
  │ OGTV
  │ ✔✔✘✔ CVE-2023-34969         MEDIUM       6.5   1.5%   ·  ↳ O:UBUNTU-CVE-2023-34969 | V:UB:CVE-2023-34969
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dbus-user-session@1.12.16-2ubuntu2.3
  │ OGTV
  │ ✘✔✘✔ CVE-2023-34969         MEDIUM       6.5   1.5%   ·  ↳ V:UB:CVE-2023-34969
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/diffutils@1%3A3.7-3
  │ OGTV
  │ ✔✔✘✔ CVE-2026-53910         LOW          2.1   0.3%   ·  ↳ O:UBUNTU-CVE-2026-53910,USN-8692-1 | V:UB:CVE-2026-53910
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dirmngr@2.2.19-3ubuntu2.5
  │ OGTV
  │ ✘✔✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dmsetup@2%3A1.02.167-1ubuntu1
  │ OGTV
  │ ✘✔✘✔ CVE-2026-19617         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-19617
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dpkg@1.19.7ubuntu3.2
  │ OGTV
  │ ✔✔✘✘ CVE-2025-6297          HIGH         8.2   0.4%   ·  ↳ O:UBUNTU-CVE-2025-6297
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dpkg-dev@1.19.7ubuntu3.2
  │ OGTV
  │ ✘✔✘✘ CVE-2025-6297          HIGH         8.2   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/fdisk@2.34-0.1ubuntu9.6
  │ OGTV
  │ ✘✔✘✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✔ CVE-2026-27456         MEDIUM       4.7   0.1%   ·  ↳ V:UB:CVE-2026-27456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/g%2B%2B@4%3A9.3.0-1ubuntu2
  │ OGTV
  │ ✘✔✘✘ CVE-2020-23026         HIGH         7.5   1.0%   ·
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/g%2B%2B-9@9.4.0-1ubuntu1~20.04.2
  │ OGTV
  │ ✘✔✘✘ CVE-2020-23026         HIGH         7.5   1.0%   ·
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  │ ✘✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc@4%3A9.3.0-1ubuntu2
  │ OGTV
  │ ✘✔✘✘ CVE-2020-23026         HIGH         7.5   1.0%   ·
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc-10-base@10.5.0-1ubuntu1~20.04
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  │ ✘✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc-9@9.4.0-1ubuntu1~20.04.2
  │ OGTV
  │ ✔✔✘✘ CVE-2020-23026         HIGH         7.5   1.0%   ·  ↳ O:UBUNTU-CVE-2020-23026
  │ ✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-102010
  │ ✔✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ O:UBUNTU-CVE-2026-95619
  │ ✔✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ O:UBUNTU-CVE-2023-4039 | V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc-9-base@9.4.0-1ubuntu1~20.04.2
  │ OGTV
  │ ✘✔✘✘ CVE-2020-23026         HIGH         7.5   1.0%   ·
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  │ ✘✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gir1.2-packagekitglib-1.0@1.1.13-2ubuntu1.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-41651         HIGH         8.8   0.5%   ·
  │ ✘✔✘✘ CVE-2026-10294         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✔ CVE-2022-0987          LOW          3.3   0.3%   ·  ↳ V:UB:CVE-2022-0987
  │ ✘✔✘✔ CVE-2024-0217          LOW          3.3   0.2%   ·  ↳ V:UB:CVE-2024-0217
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/glib-networking@2.64.2-1ubuntu0.1
  │ OGTV
  │ ✔✔✘✔ CVE-2026-10028         MEDIUM       4.3   0.2%   ·  ↳ O:UBUNTU-CVE-2026-10028 | V:UB:CVE-2026-10028
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/glib-networking-common@2.64.2-1ubuntu0.1
  │ OGTV
  │ ✘✔✘✔ CVE-2026-10028         MEDIUM       4.3   0.2%   ·  ↳ V:UB:CVE-2026-10028
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/glib-networking-services@2.64.2-1ubuntu0.1
  │ OGTV
  │ ✘✔✘✔ CVE-2026-10028         MEDIUM       4.3   0.2%   ·  ↳ V:UB:CVE-2026-10028
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gnupg@2.2.19-3ubuntu2.5
  │ OGTV
  │ ✘✔✘✔ CVE-2025-68973         HIGH         7.8   0.2%   ·  ↳ V:UB:CVE-2025-68973
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gnupg-l10n@2.2.19-3ubuntu2.5
  │ OGTV
  │ ✘✔✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gnupg-utils@2.2.19-3ubuntu2.5
  │ OGTV
  │ ✘✔✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg@2.2.19-3ubuntu2.5
  │ OGTV
  │ ✘✔✘✔ CVE-2025-68973         HIGH         7.8   0.2%   ·  ↳ V:UB:CVE-2025-68973
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg-agent@2.2.19-3ubuntu2.5
  │ OGTV
  │ ✘✔✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg-wks-client@2.2.19-3ubuntu2.5
  │ OGTV
  │ ✘✔✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg-wks-server@2.2.19-3ubuntu2.5
  │ OGTV
  │ ✘✔✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpgconf@2.2.19-3ubuntu2.5
  │ OGTV
  │ ✘✔✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpgsm@2.2.19-3ubuntu2.5
  │ OGTV
  │ ✘✔✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpgv@2.2.19-3ubuntu2.5
  │ OGTV
  │ ✘✔✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gzip@1.10-0ubuntu4.1
  │ OGTV
  │ ✔✔✘✔ CVE-2026-41992         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-41992,USN-8733-2 | V:UB:CVE-2026-41992
  │ ✔✔✘✔ CVE-2026-41991         MEDIUM       4.7   0.1%   ·  ↳ O:UBUNTU-CVE-2026-41991,USN-8733-2 | V:UB:CVE-2026-41991
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/krb5-locales@1.17-6ubuntu4.11
  │ OGTV
  │ ✘✔✘✘ CVE-2018-5709          HIGH         7.5   2.0%   ·
  │ ✘✔✘✘ CVE-2026-11850         MEDIUM       5.0   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libacl1@2.2.53-6
  │ OGTV
  │ ✘✔✘✘ CVE-2026-54369         HIGH         8.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-54370         HIGH         7.2   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libasan5@9.4.0-1ubuntu1~20.04.2
  │ OGTV
  │ ✘✔✘✘ CVE-2020-23026         HIGH         7.5   1.0%   ·
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  │ ✘✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libatomic1@10.5.0-1ubuntu1~20.04
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  │ ✘✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libattr1@1%3A2.4.48-5
  │ OGTV
  │ ✘✔✘✔ CVE-2026-54371         HIGH         8.4   0.1%   ·  ↳ V:UB:CVE-2026-54371
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libbinutils@2.34-6ubuntu1.11
  │ OGTV
  │ ✘✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✔✘✘ CVE-2025-11082         HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-11083         HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-5244          HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-5245          HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·
  │ ✘✔✘✘ CVE-2025-7545          HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-3442          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·
  │ ✘✔✘✔ CVE-2019-1010204       MEDIUM       5.5   1.1%   ·  ↳ V:UB:CVE-2019-1010204
  │ ✘✔✘✘ CVE-2021-20197         MEDIUM       6.3   0.3%   ·
  │ ✘✔✘✔ CVE-2022-48064         MEDIUM       5.5   0.6%   ·  ↳ V:UB:CVE-2022-48064
  │ ✘✔✘✘ CVE-2025-11412         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11413         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11414         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11494         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11839         MEDIUM       5.5   0.3%   ·
  │ ✘✔✘✘ CVE-2025-11840         MEDIUM       5.5   0.3%   ·
  │ ✘✔✘✘ CVE-2025-3198          MEDIUM       5.5   0.3%   ·
  │ ✘✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✔✘✘ CVE-2025-8225          MEDIUM       4.8   0.2%   ·
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
  │ ✘✔✘✔ CVE-2025-1148          LOW          3.1   0.6%   ·  ↳ V:UB:CVE-2025-1148
  │ ✘✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·
  │ ✘✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  │ ✘✔✘✔ CVE-2025-1180          LOW          3.1   0.7%   ·  ↳ V:UB:CVE-2025-1180
  │ ✘✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libblkid1@2.34-0.1ubuntu9.6
  │ OGTV
  │ ✘✔✘✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✔ CVE-2026-27456         MEDIUM       4.7   0.1%   ·  ↳ V:UB:CVE-2026-27456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libbz2-1.0@1.0.8-2
  │ OGTV
  │ ✘✔✘✘ CVE-2026-42250         MEDIUM       4.8   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc-bin@2.31-0ubuntu9.17
  │ OGTV
  │ ✘✔✘✘ CVE-2019-1010022       CRITICAL     9.8   3.2%   ·
  │ ✘✔✘✘ CVE-2021-33574         CRITICAL     9.8   3.5%   ·
  │ ✘✔✘✘ CVE-2026-5450          CRITICAL     9.8   0.7%   ·
  │ ✘✔✘✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·
  │ ✘✔✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·
  │ ✘✔✘✘ CVE-2018-20796         HIGH         7.5   5.8%   ·
  │ ✘✔✘✘ CVE-2019-1010023       HIGH         8.8   3.1%   ·
  │ ✘✔✘✘ CVE-2025-15281         HIGH         7.5   0.5%   ·
  │ ✘✔✘✘ CVE-2025-4802          HIGH         7.8   0.6%   ·
  │ ✘✔✘✘ CVE-2026-0861          HIGH         8.4   0.4%   ·
  │ ✘✔✘✘ CVE-2026-0915          HIGH         7.5   0.6%   ·
  │ ✘✔✘✔ CVE-2026-4046          HIGH         7.5   0.7%   ·  ↳ V:UB:CVE-2026-4046
  │ ✘✔✘✔ CVE-2026-5435          HIGH         7.3   0.4%   ·  ↳ V:UB:CVE-2026-5435
  │ ✘✔✘✘ CVE-2026-5928          HIGH         7.5   0.5%   ·
  │ ✘✔✘✘ CVE-2019-1010024       MEDIUM       5.3   3.2%   ·
  │ ✘✔✘✘ CVE-2025-8058          MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ V:UB:CVE-2026-18374
  │ ✘✔✘✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·
  │ ✘✔✘✔ CVE-2026-6238          MEDIUM       6.5   0.4%   ·  ↳ V:UB:CVE-2026-6238
  │ ✘✔✘✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·
  │ ✘✔✘✔ CVE-2026-89092         MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-89092
  │ ✘✔✘✘ CVE-2026-6368          LOW          2.1   0.1%   ·
  │ ✘✔✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc-dev-bin@2.31-0ubuntu9.18
  │ OGTV
  │ ✘✔✘✘ CVE-2019-1010022       CRITICAL     9.8   3.2%   ·
  │ ✘✔✘✘ CVE-2021-33574         CRITICAL     9.8   3.5%   ·
  │ ✘✔✘✘ CVE-2026-5450          CRITICAL     9.8   0.7%   ·
  │ ✘✔✘✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·
  │ ✘✔✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·
  │ ✘✔✘✘ CVE-2018-20796         HIGH         7.5   5.8%   ·
  │ ✘✔✘✘ CVE-2019-1010023       HIGH         8.8   3.1%   ·
  │ ✘✔✘✘ CVE-2025-15281         HIGH         7.5   0.5%   ·
  │ ✘✔✘✘ CVE-2026-0861          HIGH         8.4   0.4%   ·
  │ ✘✔✘✘ CVE-2026-0915          HIGH         7.5   0.6%   ·
  │ ✘✔✘✔ CVE-2026-4046          HIGH         7.5   0.7%   ·  ↳ V:UB:CVE-2026-4046
  │ ✘✔✘✔ CVE-2026-5435          HIGH         7.3   0.4%   ·  ↳ V:UB:CVE-2026-5435
  │ ✘✔✘✘ CVE-2026-5928          HIGH         7.5   0.5%   ·
  │ ✘✔✘✘ CVE-2019-1010024       MEDIUM       5.3   3.2%   ·
  │ ✘✔✘✘ CVE-2025-8058          MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ V:UB:CVE-2026-18374
  │ ✘✔✘✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·
  │ ✘✔✘✔ CVE-2026-6238          MEDIUM       6.5   0.4%   ·  ↳ V:UB:CVE-2026-6238
  │ ✘✔✘✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·
  │ ✘✔✘✔ CVE-2026-89092         MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-89092
  │ ✘✔✘✘ CVE-2026-6368          LOW          2.1   0.1%   ·
  │ ✘✔✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc6@2.31-0ubuntu9.18
  │ OGTV
  │ ✘✔✘✘ CVE-2019-1010022       CRITICAL     9.8   3.2%   ·
  │ ✘✔✘✘ CVE-2021-33574         CRITICAL     9.8   3.5%   ·
  │ ✘✔✘✘ CVE-2026-5450          CRITICAL     9.8   0.7%   ·
  │ ✘✔✘✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·
  │ ✘✔✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·
  │ ✘✔✘✘ CVE-2018-20796         HIGH         7.5   5.8%   ·
  │ ✘✔✘✘ CVE-2019-1010023       HIGH         8.8   3.1%   ·
  │ ✘✔✘✔ CVE-2025-15281         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2025-15281
  │ ✘✔✘✔ CVE-2026-0861          HIGH         8.4   0.4%   ·  ↳ V:UB:CVE-2026-0861
  │ ✘✔✘✔ CVE-2026-0915          HIGH         7.5   0.6%   ·  ↳ V:UB:CVE-2026-0915
  │ ✘✔✘✔ CVE-2026-4046          HIGH         7.5   0.7%   ·  ↳ V:UB:CVE-2026-4046
  │ ✘✔✘✔ CVE-2026-5435          HIGH         7.3   0.4%   ·  ↳ V:UB:CVE-2026-5435
  │ ✘✔✘✘ CVE-2026-5928          HIGH         7.5   0.5%   ·
  │ ✘✔✘✘ CVE-2019-1010024       MEDIUM       5.3   3.2%   ·
  │ ✘✔✘✔ CVE-2025-8058          MEDIUM       5.9   0.2%   ·  ↳ V:UB:CVE-2025-8058
  │ ✘✔✘✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ V:UB:CVE-2026-18374
  │ ✘✔✘✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·
  │ ✘✔✘✔ CVE-2026-6238          MEDIUM       6.5   0.4%   ·  ↳ V:UB:CVE-2026-6238
  │ ✘✔✘✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·
  │ ✘✔✘✔ CVE-2026-89092         MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-89092
  │ ✘✔✘✘ CVE-2026-6368          LOW          2.1   0.1%   ·
  │ ✘✔✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc6-dev@2.31-0ubuntu9.18
  │ OGTV
  │ ✘✔✘✘ CVE-2019-1010022       CRITICAL     9.8   3.2%   ·
  │ ✘✔✘✘ CVE-2021-33574         CRITICAL     9.8   3.5%   ·
  │ ✘✔✘✘ CVE-2026-5450          CRITICAL     9.8   0.7%   ·
  │ ✘✔✘✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·
  │ ✘✔✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·
  │ ✘✔✘✘ CVE-2018-20796         HIGH         7.5   5.8%   ·
  │ ✘✔✘✘ CVE-2019-1010023       HIGH         8.8   3.1%   ·
  │ ✘✔✘✘ CVE-2025-15281         HIGH         7.5   0.5%   ·
  │ ✘✔✘✘ CVE-2026-0861          HIGH         8.4   0.4%   ·
  │ ✘✔✘✘ CVE-2026-0915          HIGH         7.5   0.6%   ·
  │ ✘✔✘✔ CVE-2026-4046          HIGH         7.5   0.7%   ·  ↳ V:UB:CVE-2026-4046
  │ ✘✔✘✔ CVE-2026-5435          HIGH         7.3   0.4%   ·  ↳ V:UB:CVE-2026-5435
  │ ✘✔✘✘ CVE-2026-5928          HIGH         7.5   0.5%   ·
  │ ✘✔✘✘ CVE-2019-1010024       MEDIUM       5.3   3.2%   ·
  │ ✘✔✘✘ CVE-2025-8058          MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ V:UB:CVE-2026-18374
  │ ✘✔✘✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·
  │ ✘✔✘✔ CVE-2026-6238          MEDIUM       6.5   0.4%   ·  ↳ V:UB:CVE-2026-6238
  │ ✘✔✘✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·
  │ ✘✔✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·
  │ ✘✔✘✔ CVE-2026-89092         MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-89092
  │ ✘✔✘✘ CVE-2026-6368          LOW          2.1   0.1%   ·
  │ ✘✔✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·
  │ ✘✔✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libcap2@1%3A2.32-1ubuntu0.2
  │ OGTV
  │ ✔✔✘✔ CVE-2026-4878          HIGH         7.0   0.1%   ·  ↳ O:UBUNTU-CVE-2026-4878,USN-8193-2 | V:UB:CVE-2026-4878
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libcap2-bin@1%3A2.32-1ubuntu0.2
  │ OGTV
  │ ✘✔✘✔ CVE-2026-4878          HIGH         7.0   0.1%   ·  ↳ V:UB:CVE-2026-4878
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libcc1-0@10.5.0-1ubuntu1~20.04
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  │ ✘✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libctf-nobfd0@2.34-6ubuntu1.11
  │ OGTV
  │ ✘✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✔✘✘ CVE-2025-11082         HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-11083         HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-5244          HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-5245          HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·
  │ ✘✔✘✘ CVE-2025-7545          HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-3442          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·
  │ ✘✔✘✔ CVE-2019-1010204       MEDIUM       5.5   1.1%   ·  ↳ V:UB:CVE-2019-1010204
  │ ✘✔✘✘ CVE-2021-20197         MEDIUM       6.3   0.3%   ·
  │ ✘✔✘✔ CVE-2022-48064         MEDIUM       5.5   0.6%   ·  ↳ V:UB:CVE-2022-48064
  │ ✘✔✘✘ CVE-2025-11412         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11413         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11414         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11494         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11839         MEDIUM       5.5   0.3%   ·
  │ ✘✔✘✘ CVE-2025-11840         MEDIUM       5.5   0.3%   ·
  │ ✘✔✘✘ CVE-2025-3198          MEDIUM       5.5   0.3%   ·
  │ ✘✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✔✘✘ CVE-2025-8225          MEDIUM       4.8   0.2%   ·
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
  │ ✘✔✘✔ CVE-2025-1148          LOW          3.1   0.6%   ·  ↳ V:UB:CVE-2025-1148
  │ ✘✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·
  │ ✘✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  │ ✘✔✘✔ CVE-2025-1180          LOW          3.1   0.7%   ·  ↳ V:UB:CVE-2025-1180
  │ ✘✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libctf0@2.34-6ubuntu1.11
  │ OGTV
  │ ✘✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ V:UB:CVE-2017-13716
  │ ✘✔✘✘ CVE-2025-11082         HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-11083         HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-5244          HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-5245          HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·
  │ ✘✔✘✘ CVE-2025-7545          HIGH         7.8   0.3%   ·
  │ ✘✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-3442          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·
  │ ✘✔✘✔ CVE-2019-1010204       MEDIUM       5.5   1.1%   ·  ↳ V:UB:CVE-2019-1010204
  │ ✘✔✘✘ CVE-2021-20197         MEDIUM       6.3   0.3%   ·
  │ ✘✔✘✔ CVE-2022-48064         MEDIUM       5.5   0.6%   ·  ↳ V:UB:CVE-2022-48064
  │ ✘✔✘✘ CVE-2025-11412         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11413         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11414         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11494         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-11839         MEDIUM       5.5   0.3%   ·
  │ ✘✔✘✘ CVE-2025-11840         MEDIUM       5.5   0.3%   ·
  │ ✘✔✘✘ CVE-2025-3198          MEDIUM       5.5   0.3%   ·
  │ ✘✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69645
  │ ✘✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-69651
  │ ✘✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2025-69652
  │ ✘✔✘✘ CVE-2025-8225          MEDIUM       4.8   0.2%   ·
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
  │ ✘✔✘✔ CVE-2025-1148          LOW          3.1   0.6%   ·  ↳ V:UB:CVE-2025-1148
  │ ✘✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·
  │ ✘✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·
  │ ✘✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ V:UB:CVE-2025-1152
  │ ✘✔✘✔ CVE-2025-1180          LOW          3.1   0.7%   ·  ↳ V:UB:CVE-2025-1180
  │ ✘✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libcurl4@7.68.0-1ubuntu2.25
  │ OGTV
  │ ✘✔✘✔ CVE-2026-11856         CRITICAL     9.8   0.7%   ·  ↳ V:UB:CVE-2026-11856
  │ ✘✔✘✔ CVE-2026-18924         CRITICAL     9.1   0.6%   ·  ↳ V:UB:CVE-2026-18924
  │ ✘✔✘✔ CVE-2026-8924          CRITICAL     9.1   0.7%   ·  ↳ V:UB:CVE-2026-8924
  │ ✘✔✘✔ CVE-2026-8927          CRITICAL     9.1   0.5%   ·  ↳ V:UB:CVE-2026-8927
  │ ✘✔✘✔ CVE-2026-5773          HIGH         7.5   0.7%   ·  ↳ V:UB:CVE-2026-5773
  │ ✘✔✘✔ CVE-2026-80230         HIGH         7.5   0.4%   ·  ↳ V:UB:CVE-2026-80230
  │ ✘✔✘✔ CVE-2026-82209         HIGH         8.2   0.4%   ·  ↳ V:UB:CVE-2026-82209
  │ ✘✔✘✔ CVE-2026-8286          HIGH         8.1   0.3%   ·  ↳ V:UB:CVE-2026-8286
  │ ✘✔✘✔ CVE-2026-8932          HIGH         7.5   0.4%   ·  ↳ V:UB:CVE-2026-8932
  │ ✘✔✘✔ CVE-2025-14017         MEDIUM       6.3   0.1%   ·  ↳ V:UB:CVE-2025-14017
  │ ✘✔✘✘ CVE-2025-14524         MEDIUM       5.3   0.7%   ·
  │ ✘✔✘✔ CVE-2025-15079         MEDIUM       5.3   0.5%   ·  ↳ V:UB:CVE-2025-15079
  │ ✘✔✘✔ CVE-2026-1965          MEDIUM       6.5   0.3%   ·  ↳ V:UB:CVE-2026-1965
  │ ✘✔✘✔ CVE-2026-3783          MEDIUM       5.3   0.5%   ·  ↳ V:UB:CVE-2026-3783
  │ ✘✔✘✔ CVE-2026-3784          MEDIUM       6.5   0.5%   ·  ↳ V:UB:CVE-2026-3784
  │ ✘✔✘✘ CVE-2026-4873          MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✔ CVE-2026-5545          MEDIUM       6.5   0.4%   ·  ↳ V:UB:CVE-2026-5545
  │ ✘✔✘✘ CVE-2026-6253          MEDIUM       5.9   0.7%   ·
  │ ✘✔✘✘ CVE-2026-6429          MEDIUM       5.3   0.5%   ·
  │ ✘✔✘✔ CVE-2026-7168          MEDIUM       5.3   0.5%   ·  ↳ V:UB:CVE-2026-7168
  │ ✘✔✘✔ CVE-2026-8458          MEDIUM       6.5   0.4%   ·  ↳ V:UB:CVE-2026-8458
  │ ✘✔✘✔ CVE-2025-15224         LOW          3.1   0.5%   ·  ↳ V:UB:CVE-2025-15224
  │ ✘✘✘✔ CVE-2026-86414         ?            0.0      -   ·  ↳ V:UB:CVE-2026-86414
  │ ✘✘✘✔ CVE-2026-87864         ?            0.0      -   ·  ↳ V:UB:CVE-2026-87864
  │ ✘✘✘✔ CVE-2026-92388         ?            0.0      -   ·  ↳ V:UB:CVE-2026-92388
  │ ✘✘✘✔ CVE-2026-92389         ?            0.0      -   ·  ↳ V:UB:CVE-2026-92389
  │ ✘✘✘✔ CVE-2026-92391         ?            0.0      -   ·  ↳ V:UB:CVE-2026-92391
  │ ✘✘✘✔ CVE-2026-94266         ?            0.0      -   ·  ↳ V:UB:CVE-2026-94266
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libdbus-1-3@1.12.16-2ubuntu2.3
  │ OGTV
  │ ✘✔✘✔ CVE-2023-34969         MEDIUM       6.5   1.5%   ·  ↳ V:UB:CVE-2023-34969
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libdevmapper1.02.1@2%3A1.02.167-1ubuntu1
  │ OGTV
  │ ✘✔✘✔ CVE-2026-19617         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-19617
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libdpkg-perl@1.19.7ubuntu3.2
  │ OGTV
  │ ✘✔✘✘ CVE-2025-6297          HIGH         8.2   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libelf1@0.176-1.1ubuntu0.1
  │ OGTV
  │ ✘✔✘✔ CVE-2025-1352          HIGH         7.5   0.7%   ·  ↳ V:UB:CVE-2025-1352
  │ ✘✔✘✔ CVE-2025-1376          MEDIUM       4.7   0.3%   ·  ↳ V:UB:CVE-2025-1376
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libexpat1@2.2.9-1ubuntu0.8
  │ OGTV
  │ ✘✔✘✘ CVE-2023-52425         HIGH         7.5   2.1%   ·
  │ ✘✔✘✘ CVE-2024-28757         HIGH         7.5   2.0%   ·
  │ ✘✔✘✘ CVE-2024-8176          HIGH         7.5   1.4%   ·
  │ ✘✔✘✘ CVE-2025-59375         HIGH         7.5   1.3%   ·
  │ ✘✔✘✘ CVE-2026-102633        HIGH         8.2   0.3%   ·
  │ ✘✔✘✔ CVE-2026-25210         HIGH         7.8   0.2%   ·  ↳ V:UB:CVE-2026-25210
  │ ✘✔✘✘ CVE-2026-41080         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2026-45186         HIGH         7.5   0.5%   ·
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
  │ ✘✔✘✔ CVE-2026-24515         LOW          2.9   0.2%   ·  ↳ V:UB:CVE-2026-24515
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libexpat1-dev@2.2.9-1ubuntu0.8
  │ OGTV
  │ ✘✔✘✘ CVE-2023-52425         HIGH         7.5   2.1%   ·
  │ ✘✔✘✘ CVE-2024-28757         HIGH         7.5   2.0%   ·
  │ ✘✔✘✘ CVE-2024-8176          HIGH         7.5   1.4%   ·
  │ ✘✔✘✘ CVE-2025-59375         HIGH         7.5   1.3%   ·
  │ ✘✔✘✘ CVE-2026-102633        HIGH         8.2   0.3%   ·
  │ ✘✔✘✘ CVE-2026-25210         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-41080         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2026-45186         HIGH         7.5   0.5%   ·
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
  │ ✘✔✘✘ CVE-2026-24515         LOW          2.9   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libfdisk1@2.34-0.1ubuntu9.6
  │ OGTV
  │ ✘✔✘✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✔ CVE-2026-27456         MEDIUM       4.7   0.1%   ·  ↳ V:UB:CVE-2026-27456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgcc-9-dev@9.4.0-1ubuntu1~20.04.2
  │ OGTV
  │ ✘✔✘✘ CVE-2020-23026         HIGH         7.5   1.0%   ·
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  │ ✘✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgcc-s1@10.5.0-1ubuntu1~20.04
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  │ ✘✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgcrypt20@1.8.5-5ubuntu1.1
  │ OGTV
  │ ✔✔✘✔ CVE-2024-2236          MEDIUM       5.9   1.1%   ·  ↳ O:UBUNTU-CVE-2024-2236 | V:UB:CVE-2024-2236
  │ ✔✔✘✘ CVE-2026-41989         MEDIUM       6.7   0.2%   ·  ↳ O:UBUNTU-CVE-2026-41989
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libglib2.0-0@2.64.6-1~ubuntu20.04.9
  │ OGTV
  │ ✘✔✘✔ CVE-2025-14087         CRITICAL     9.8   0.8%   ·  ↳ V:UB:CVE-2025-14087
  │ ✘✔✘✔ CVE-2026-58016         CRITICAL     9.1   0.5%   ·  ↳ V:UB:CVE-2026-58016
  │ ✘✔✘✔ CVE-2025-13601         HIGH         7.7   0.3%   ·  ↳ V:UB:CVE-2025-13601
  │ ✘✔✘✔ CVE-2026-16118         HIGH         7.1   0.3%   ·  ↳ V:UB:CVE-2026-16118
  │ ✘✔✘✔ CVE-2026-58010         HIGH         8.2   0.5%   ·  ↳ V:UB:CVE-2026-58010
  │ ✘✔✘✔ CVE-2026-58011         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-58011
  │ ✘✔✘✔ CVE-2026-58012         HIGH         8.2   0.5%   ·  ↳ V:UB:CVE-2026-58012
  │ ✘✔✘✔ CVE-2026-58013         HIGH         8.2   0.5%   ·  ↳ V:UB:CVE-2026-58013
  │ ✘✔✘✔ CVE-2026-58014         HIGH         8.6   0.5%   ·  ↳ V:UB:CVE-2026-58014
  │ ✘✔✘✔ CVE-2026-58015         HIGH         7.5   0.8%   ·  ↳ V:UB:CVE-2026-58015
  │ ✘✔✘✘ CVE-2025-14512         MEDIUM       6.5   0.6%   ·
  │ ✘✔✘✔ CVE-2026-1484          MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-1484
  │ ✘✔✘✔ CVE-2026-1489          MEDIUM       5.4   0.4%   ·  ↳ V:UB:CVE-2026-1489
  │ ✘✔✘✔ CVE-2026-15588         MEDIUM       5.3   0.5%   ·  ↳ V:UB:CVE-2026-15588
  │ ✘✔✘✔ CVE-2026-86469         MEDIUM       5.3   0.1%   ·  ↳ V:UB:CVE-2026-86469
  │ ✘✔✘✔ CVE-2025-3360          LOW          3.7   0.5%   ·  ↳ V:UB:CVE-2025-3360
  │ ✘✔✘✔ CVE-2025-7039          LOW          3.7   0.4%   ·  ↳ V:UB:CVE-2025-7039
  │ ✘✔✘✔ CVE-2026-0988          LOW          3.7   0.4%   ·  ↳ V:UB:CVE-2026-0988
  │ ✘✔✘✔ CVE-2026-1485          LOW          2.8   0.2%   ·  ↳ V:UB:CVE-2026-1485
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libglib2.0-bin@2.64.6-1~ubuntu20.04.9
  │ OGTV
  │ ✘✔✘✘ CVE-2025-14087         CRITICAL     9.8   0.8%   ·
  │ ✘✔✘✔ CVE-2026-58016         CRITICAL     9.1   0.5%   ·  ↳ V:UB:CVE-2026-58016
  │ ✘✔✘✘ CVE-2025-13601         HIGH         7.7   0.3%   ·
  │ ✘✔✘✔ CVE-2026-16118         HIGH         7.1   0.3%   ·  ↳ V:UB:CVE-2026-16118
  │ ✘✔✘✔ CVE-2026-58010         HIGH         8.2   0.5%   ·  ↳ V:UB:CVE-2026-58010
  │ ✘✔✘✔ CVE-2026-58011         HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-58011
  │ ✘✔✘✔ CVE-2026-58012         HIGH         8.2   0.5%   ·  ↳ V:UB:CVE-2026-58012
  │ ✘✔✘✔ CVE-2026-58013         HIGH         8.2   0.5%   ·  ↳ V:UB:CVE-2026-58013
  │ ✘✔✘✔ CVE-2026-58014         HIGH         8.6   0.5%   ·  ↳ V:UB:CVE-2026-58014
  │ ✘✔✘✔ CVE-2026-58015         HIGH         7.5   0.8%   ·  ↳ V:UB:CVE-2026-58015
  │ ✘✔✘✘ CVE-2025-14512         MEDIUM       6.5   0.6%   ·
  │ ✘✔✘✔ CVE-2026-1484          MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-1484
  │ ✘✔✘✔ CVE-2026-1489          MEDIUM       5.4   0.4%   ·  ↳ V:UB:CVE-2026-1489
  │ ✘✔✘✔ CVE-2026-15588         MEDIUM       5.3   0.5%   ·  ↳ V:UB:CVE-2026-15588
  │ ✘✔✘✔ CVE-2026-86469         MEDIUM       5.3   0.1%   ·  ↳ V:UB:CVE-2026-86469
  │ ✘✔✘✘ CVE-2025-3360          LOW          3.7   0.5%   ·
  │ ✘✔✘✘ CVE-2025-7039          LOW          3.7   0.4%   ·
  │ ✘✔✘✔ CVE-2026-0988          LOW          3.7   0.4%   ·  ↳ V:UB:CVE-2026-0988
  │ ✘✔✘✔ CVE-2026-1485          LOW          2.8   0.2%   ·  ↳ V:UB:CVE-2026-1485
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libglib2.0-data@2.64.6-1~ubuntu20.04.9
  │ OGTV
  │ ✘✔✘✘ CVE-2025-14087         CRITICAL     9.8   0.8%   ·
  │ ✘✔✘✘ CVE-2026-58016         CRITICAL     9.1   0.5%   ·
  │ ✘✔✘✘ CVE-2025-13601         HIGH         7.7   0.3%   ·
  │ ✘✔✘✘ CVE-2026-16118         HIGH         7.1   0.3%   ·
  │ ✘✔✘✘ CVE-2026-58010         HIGH         8.2   0.5%   ·
  │ ✘✔✘✘ CVE-2026-58011         HIGH         7.5   0.5%   ·
  │ ✘✔✘✘ CVE-2026-58012         HIGH         8.2   0.5%   ·
  │ ✘✔✘✘ CVE-2026-58013         HIGH         8.2   0.5%   ·
  │ ✘✔✘✘ CVE-2026-58014         HIGH         8.6   0.5%   ·
  │ ✘✔✘✘ CVE-2026-58015         HIGH         7.5   0.8%   ·
  │ ✘✔✘✘ CVE-2025-14512         MEDIUM       6.5   0.6%   ·
  │ ✘✔✘✔ CVE-2026-1484          MEDIUM       4.2   0.3%   ·  ↳ V:UB:CVE-2026-1484
  │ ✘✔✘✔ CVE-2026-1489          MEDIUM       5.4   0.4%   ·  ↳ V:UB:CVE-2026-1489
  │ ✘✔✘✘ CVE-2026-15588         MEDIUM       5.3   0.5%   ·
  │ ✘✔✘✔ CVE-2026-86469         MEDIUM       5.3   0.1%   ·  ↳ V:UB:CVE-2026-86469
  │ ✘✔✘✘ CVE-2025-3360          LOW          3.7   0.5%   ·
  │ ✘✔✘✘ CVE-2025-7039          LOW          3.7   0.4%   ·
  │ ✘✔✘✔ CVE-2026-0988          LOW          3.7   0.4%   ·  ↳ V:UB:CVE-2026-0988
  │ ✘✔✘✔ CVE-2026-1485          LOW          2.8   0.2%   ·  ↳ V:UB:CVE-2026-1485
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgnutls30@3.6.13-2ubuntu1.12
  │ OGTV
  │ ✘✔✘✔ CVE-2026-33845         CRITICAL     9.1   0.9%   ·  ↳ V:UB:CVE-2026-33845
  │ ✘✔✘✔ CVE-2026-42010         CRITICAL     9.8   0.9%   ·  ↳ V:UB:CVE-2026-42010
  │ ✘✔✘✔ CVE-2026-88647         CRITICAL     9.1   0.2%   ·  ↳ V:UB:CVE-2026-88647
  │ ✘✔✘✔ CVE-2026-95210         CRITICAL     9.1   0.2%   ·  ↳ V:UB:CVE-2026-95210
  │ ✘✔✘✔ CVE-2025-32988         HIGH         8.2   1.5%   ·  ↳ V:UB:CVE-2025-32988
  │ ✘✔✘✔ CVE-2025-32990         HIGH         8.2   0.9%   ·  ↳ V:UB:CVE-2025-32990
  │ ✘✔✘✔ CVE-2026-33846         HIGH         7.5   1.1%   ·  ↳ V:UB:CVE-2026-33846
  │ ✘✔✘✔ CVE-2026-3833          HIGH         7.4   0.9%   ·  ↳ V:UB:CVE-2026-3833
  │ ✘✔✘✔ CVE-2026-42009         HIGH         7.5   1.1%   ·  ↳ V:UB:CVE-2026-42009
  │ ✘✔✘✔ CVE-2026-42011         HIGH         7.4   0.5%   ·  ↳ V:UB:CVE-2026-42011
  │ ✘✔✘✔ CVE-2026-42012         HIGH         7.1   0.5%   ·  ↳ V:UB:CVE-2026-42012
  │ ✘✔✘✔ CVE-2026-42013         HIGH         8.2   0.6%   ·  ↳ V:UB:CVE-2026-42013
  │ ✘✔✘✔ CVE-2026-5260          HIGH         8.2   0.9%   ·  ↳ V:UB:CVE-2026-5260
  │ ✘✔✘✔ CVE-2026-67693         HIGH         7.5   0.2%   ·  ↳ V:UB:CVE-2026-67693
  │ ✘✔✘✔ CVE-2026-95184         HIGH         7.5   0.2%   ·  ↳ V:UB:CVE-2026-95184
  │ ✘✔✘✔ CVE-2026-95209         HIGH         7.5   0.3%   ·  ↳ V:UB:CVE-2026-95209
  │ ✘✔✘✔ CVE-2025-14831         MEDIUM       5.3   0.7%   ·  ↳ V:UB:CVE-2025-14831
  │ ✘✔✘✔ CVE-2025-6395          MEDIUM       6.5   0.8%   ·  ↳ V:UB:CVE-2025-6395
  │ ✘✔✘✔ CVE-2025-9820          MEDIUM       4.0   0.2%   ·  ↳ V:UB:CVE-2025-9820
  │ ✘✔✘✔ CVE-2026-42014         MEDIUM       6.6   0.2%   ·  ↳ V:UB:CVE-2026-42014
  │ ✘✔✘✔ CVE-2026-42015         MEDIUM       5.3   0.9%   ·  ↳ V:UB:CVE-2026-42015
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgomp1@10.5.0-1ubuntu1~20.04
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  │ ✘✘✘✔ CVE-2020-13844         MEDIUM       5.5   0.5%   ·  ↳ V:UB:CVE-2020-13844
  │ ✘✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgssapi-krb5-2@1.17-6ubuntu4.11
  │ OGTV
  │ ✘✔✘✘ CVE-2018-5709          HIGH         7.5   2.0%   ·
  │ ✘✔✘✘ CVE-2026-11850         MEDIUM       5.0   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libicu66@66.1-2ubuntu2.1
  │ OGTV
  │ ✘✔✘✔ CVE-2025-5222          HIGH         7.0   0.4%   ·  ↳ V:UB:CVE-2025-5222
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libip4tc2@1.8.4-3ubuntu2.1
  │ OGTV
  │ ✘✔✘✘ CVE-2012-2663          HIGH         7.5   2.7%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libitm1@10.5.0-1ubuntu1~20.04
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  │ ✘✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libk5crypto3@1.17-6ubuntu4.11
  │ OGTV
  │ ✘✔✘✘ CVE-2018-5709          HIGH         7.5   2.0%   ·
  │ ✘✔✘✘ CVE-2026-11850         MEDIUM       5.0   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libkrb5-3@1.17-6ubuntu4.11
  │ OGTV
  │ ✘✔✘✘ CVE-2018-5709          HIGH         7.5   2.0%   ·
  │ ✘✔✘✘ CVE-2026-11850         MEDIUM       5.0   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libkrb5support0@1.17-6ubuntu4.11
  │ OGTV
  │ ✘✔✘✘ CVE-2018-5709          HIGH         7.5   2.0%   ·
  │ ✘✔✘✘ CVE-2026-11850         MEDIUM       5.0   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/liblmdb0@0.9.24-1
  │ OGTV
  │ ✘✔✘✔ CVE-2026-22185         MEDIUM       4.6   0.2%   ·  ↳ V:UB:CVE-2026-22185
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/liblsan0@10.5.0-1ubuntu1~20.04
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  │ ✘✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/liblzma5@5.2.4-1ubuntu1.1
  │ OGTV
  │ ✘✔✘✔ CVE-2026-34743         MEDIUM       6.3   0.5%   ·  ↳ V:UB:CVE-2026-34743
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libmount1@2.34-0.1ubuntu9.6
  │ OGTV
  │ ✘✔✘✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✔ CVE-2026-27456         MEDIUM       4.7   0.1%   ·  ↳ V:UB:CVE-2026-27456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libncurses6@6.2-0ubuntu2.1
  │ OGTV
  │ ✘✔✘✘ CVE-2025-69720         CRITICAL     9.8   0.4%   ·
  │ ✘✔✘✔ CVE-2023-50495         MEDIUM       6.5   1.0%   ·  ↳ V:UB:CVE-2023-50495
  │ ✘✔✘✔ CVE-2025-6141          MEDIUM       4.8   0.2%   ·  ↳ V:UB:CVE-2025-6141
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libncursesw6@6.2-0ubuntu2.1
  │ OGTV
  │ ✘✔✘✘ CVE-2025-69720         CRITICAL     9.8   0.4%   ·
  │ ✘✔✘✔ CVE-2023-50495         MEDIUM       6.5   1.0%   ·  ↳ V:UB:CVE-2023-50495
  │ ✘✔✘✘ CVE-2025-6141          MEDIUM       4.8   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libnghttp2-14@1.40.0-1ubuntu0.3
  │ OGTV
  │ ✘✔✘✔ CVE-2026-27135         HIGH         7.5   0.9%   ·  ↳ V:UB:CVE-2026-27135
  │ ✘✔✘✘ CVE-2026-58055         MEDIUM       6.3   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libnss-systemd@245.4-4ubuntu3.24
  │ OGTV
  │ ✘✔✘✔ CVE-2023-26604         HIGH         7.8   1.1%   ·  ↳ V:UB:CVE-2023-26604
  │ ✘✔✘✘ CVE-2020-13776         MEDIUM       6.7   0.5%   ·
  │ ✘✔✘✔ CVE-2023-7008          MEDIUM       5.9   0.8%   ·  ↳ V:UB:CVE-2023-7008
  │ ✘✔✘✘ CVE-2025-4598          MEDIUM       4.7   1.2%   ·
  │ ✘✔✘✘ CVE-2026-29111         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✔ CVE-2026-40225         MEDIUM       6.4   0.2%   ·  ↳ V:UB:CVE-2026-40225
  │ ✘✔✘✘ CVE-2026-40226         MEDIUM       6.4   0.1%   ·
  │ ✘✔✘✔ CVE-2026-40228         LOW          3.3   0.1%   ·  ↳ V:UB:CVE-2026-40228
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libp11-kit0@0.23.20-1ubuntu0.1
  │ OGTV
  │ ✘✔✘✔ CVE-2026-13757         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2026-13757
  │ ✘✔✘✔ CVE-2026-18938         MEDIUM       6.2   0.2%   ·  ↳ V:UB:CVE-2026-18938
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpackagekit-glib2-18@1.1.13-2ubuntu1.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-41651         HIGH         8.8   0.5%   ·
  │ ✘✔✘✘ CVE-2026-10294         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✔ CVE-2022-0987          LOW          3.3   0.3%   ·  ↳ V:UB:CVE-2022-0987
  │ ✘✔✘✔ CVE-2024-0217          LOW          3.3   0.2%   ·  ↳ V:UB:CVE-2024-0217
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-cap@1%3A2.32-1ubuntu0.2
  │ OGTV
  │ ✘✔✘✔ CVE-2026-4878          HIGH         7.0   0.1%   ·  ↳ V:UB:CVE-2026-4878
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-modules@1.3.1-5ubuntu4.7
  │ OGTV
  │ ✘✔✘✘ CVE-2025-6020          HIGH         7.8   0.5%   ·
  │ ✘✔✘✘ CVE-2026-54411         HIGH         8.2   0.5%   ·
  │ ✘✔✘✘ CVE-2024-10041         MEDIUM       4.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-modules-bin@1.3.1-5ubuntu4.7
  │ OGTV
  │ ✘✔✘✘ CVE-2025-6020          HIGH         7.8   0.5%   ·
  │ ✘✔✘✘ CVE-2026-54411         HIGH         8.2   0.5%   ·
  │ ✘✔✘✘ CVE-2024-10041         MEDIUM       4.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-runtime@1.3.1-5ubuntu4.7
  │ OGTV
  │ ✘✔✘✘ CVE-2025-6020          HIGH         7.8   0.5%   ·
  │ ✘✔✘✘ CVE-2026-54411         HIGH         8.2   0.5%   ·
  │ ✘✔✘✘ CVE-2024-10041         MEDIUM       4.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-systemd@245.4-4ubuntu3.24
  │ OGTV
  │ ✘✔✘✔ CVE-2023-26604         HIGH         7.8   1.1%   ·  ↳ V:UB:CVE-2023-26604
  │ ✘✔✘✘ CVE-2020-13776         MEDIUM       6.7   0.5%   ·
  │ ✘✔✘✔ CVE-2023-7008          MEDIUM       5.9   0.8%   ·  ↳ V:UB:CVE-2023-7008
  │ ✘✔✘✘ CVE-2025-4598          MEDIUM       4.7   1.2%   ·
  │ ✘✔✘✘ CVE-2026-29111         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✔ CVE-2026-40225         MEDIUM       6.4   0.2%   ·  ↳ V:UB:CVE-2026-40225
  │ ✘✔✘✘ CVE-2026-40226         MEDIUM       6.4   0.1%   ·
  │ ✘✔✘✔ CVE-2026-40228         LOW          3.3   0.1%   ·  ↳ V:UB:CVE-2026-40228
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam0g@1.3.1-5ubuntu4.7
  │ OGTV
  │ ✘✔✘✘ CVE-2025-6020          HIGH         7.8   0.5%   ·
  │ ✘✔✘✘ CVE-2026-54411         HIGH         8.2   0.5%   ·
  │ ✘✔✘✘ CVE-2024-10041         MEDIUM       4.7   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpcre2-8-0@10.34-7ubuntu0.1
  │ OGTV
  │ ✘✔✘✔ CVE-2022-41409         HIGH         7.5   1.1%   ·  ↳ V:UB:CVE-2022-41409
  │ ✘✔✘✔ CVE-2026-103111        HIGH         7.6   0.2%   ·  ↳ V:UB:CVE-2026-103111
  │ ✘✔✘✔ CVE-2026-86145         HIGH         8.2   0.4%   ·  ↳ V:UB:CVE-2026-86145
  │ ✘✔✘✔ CVE-2026-89157         HIGH         7.4   0.3%   ·  ↳ V:UB:CVE-2026-89157
  │ ✘✔✘✔ CVE-2026-89161         HIGH         7.8   0.1%   ·  ↳ V:UB:CVE-2026-89161
  │ ✘✔✘✔ CVE-2026-89156         MEDIUM       5.9   0.3%   ·  ↳ V:UB:CVE-2026-89156
  │ ✘✔✘✔ CVE-2026-89158         MEDIUM       6.5   0.2%   ·  ↳ V:UB:CVE-2026-89158
  │ ✘✔✘✔ CVE-2026-89160         MEDIUM       6.5   0.3%   ·  ↳ V:UB:CVE-2026-89160
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpcre3@2%3A8.39-12ubuntu0.1
  │ OGTV
  │ ✘✔✘✘ CVE-2017-11164         HIGH         7.8   3.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libperl5.30@5.30.0-9ubuntu0.5
  │ OGTV
  │ ✘✔✘✘ CVE-2011-10043         CRITICAL     9.8   0.8%   ·
  │ ✘✔✘✘ CVE-2017-20230         CRITICAL    10.0   0.6%   ·
  │ ✘✔✘✔ CVE-2026-12087         CRITICAL     9.1   0.4%   ·  ↳ V:UB:CVE-2026-12087
  │ ✘✔✘✔ CVE-2026-13221         CRITICAL     9.1   0.4%   ·  ↳ V:UB:CVE-2026-13221
  │ ✘✔✘✘ CVE-2026-4176          CRITICAL     9.8   0.8%   ·
  │ ✘✔✘✔ CVE-2026-42496         CRITICAL     9.1   0.4%   ·  ↳ V:UB:CVE-2026-42496
  │ ✘✔✘✔ CVE-2026-57433         CRITICAL     9.8   0.4%   ·  ↳ V:UB:CVE-2026-57433
  │ ✘✔✘✔ CVE-2026-8376          CRITICAL     9.8   0.5%   ·  ↳ V:UB:CVE-2026-8376
  │ ✘✔✘✘ CVE-2023-31486         HIGH         8.1   1.7%   ·
  │ ✘✔✘✘ CVE-2023-47039         HIGH         7.8   0.4%   ·
  │ ✘✔✘✘ CVE-2026-42497         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2026-48959         HIGH         7.5   0.6%   ·
  │ ✘✔✘✘ CVE-2026-48961         HIGH         7.3   0.4%   ·
  │ ✘✔✘✘ CVE-2026-48962         HIGH         7.8   0.5%   ·
  │ ✘✔✘✔ CVE-2026-57432         HIGH         8.4   0.2%   ·  ↳ V:UB:CVE-2026-57432
  │ ✘✔✘✘ CVE-2026-7017          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-82560         HIGH         7.5   0.6%   ·
  │ ✘✔✘✘ CVE-2026-9538          HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15649         MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2025-40909         MEDIUM       5.9   0.5%   ·
  │ ✘✔✘✔ CVE-2026-15534         MEDIUM       5.7   0.3%   ·  ↳ V:UB:CVE-2026-15534
  │ ✘✔✘✔ CVE-2026-19487         MEDIUM       5.3   0.4%   ·  ↳ V:UB:CVE-2026-19487
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpolkit-agent-1-0@0.105-26ubuntu1.3
  │ OGTV
  │ ✘✔✘✔ CVE-2016-2568          HIGH         7.8   0.4%   ·  ↳ V:UB:CVE-2016-2568
  │ ✘✔✘✘ CVE-2025-7519          MEDIUM       6.7   0.2%   ·
  │ ✘✔✘✘ CVE-2026-4897          MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-85498         ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpolkit-gobject-1-0@0.105-26ubuntu1.3
  │ OGTV
  │ ✘✔✘✔ CVE-2016-2568          HIGH         7.8   0.4%   ·  ↳ V:UB:CVE-2016-2568
  │ ✘✔✘✘ CVE-2025-7519          MEDIUM       6.7   0.2%   ·
  │ ✘✔✘✘ CVE-2026-4897          MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-85498         ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.8@3.8.10-0ubuntu1~20.04.18
  │ OGTV
  │ ✘✔✘✘ CVE-2007-4559          CRITICAL     9.8  27.1%   ·
  │ ✘✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.4%   ·
  │ ✘✔✘✘ CVE-2026-6100          CRITICAL     9.1   0.8%   ·
  │ ✘✔✘✘ CVE-2020-10735         HIGH         7.5   4.5%   ·
  │ ✘✔✘✔ CVE-2025-13836         HIGH         7.5   1.6%   ·  ↳ V:UB:CVE-2025-13836
  │ ✘✔✘✘ CVE-2025-69534         HIGH         8.2   0.6%   ·
  │ ✘✔✘✔ CVE-2025-8194          HIGH         7.5   0.7%   ·  ↳ V:UB:CVE-2025-8194
  │ ✘✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·
  │ ✘✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·
  │ ✘✔✘✔ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ V:UB:CVE-2026-15308
  │ ✘✔✘✘ CVE-2026-19553         HIGH         7.6   0.4%   ·
  │ ✘✔✘✔ CVE-2026-3644          HIGH         7.5   0.5%   ·  ↳ V:UB:CVE-2026-3644
  │ ✘✔✘✔ CVE-2026-4224          HIGH         7.5   0.7%   ·  ↳ V:UB:CVE-2026-4224
  │ ✘✔✘✘ CVE-2026-4519          HIGH         7.1   0.4%   ·
  │ ✘✔✘✘ CVE-2026-4786          HIGH         7.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·
  │ ✘✔✘✘ CVE-2026-9669          HIGH         8.2   0.4%   ·
  │ ✘✔✘✘ CVE-2021-23336         MEDIUM       5.9  40.7%   ·
  │ ✘✔✘✔ CVE-2025-11468         MEDIUM       5.7   0.6%   ·  ↳ V:UB:CVE-2025-11468
  │ ✘✔✘✔ CVE-2025-12084         MEDIUM       6.3   0.8%   ·  ↳ V:UB:CVE-2025-12084
  │ ✘✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.6%   ·
  │ ✘✔✘✔ CVE-2025-13837         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2025-13837
  │ ✘✔✘✔ CVE-2025-15282         MEDIUM       6.0   0.5%   ·  ↳ V:UB:CVE-2025-15282
  │ ✘✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✔ CVE-2025-4516          MEDIUM       5.9   0.2%   ·  ↳ V:UB:CVE-2025-4516
  │ ✘✔✘✔ CVE-2025-6069          MEDIUM       4.3   0.6%   ·  ↳ V:UB:CVE-2025-6069
  │ ✘✔✘✔ CVE-2025-6075          MEDIUM       5.5   0.1%   ·  ↳ V:UB:CVE-2025-6075
  │ ✘✔✘✔ CVE-2025-8291          MEDIUM       4.3   0.5%   ·  ↳ V:UB:CVE-2025-8291
  │ ✘✔✘✔ CVE-2026-0672          MEDIUM       6.0   0.5%   ·  ↳ V:UB:CVE-2026-0672
  │ ✘✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✔ CVE-2026-0865          MEDIUM       5.9   0.5%   ·  ↳ V:UB:CVE-2026-0865
  │ ✘✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-1299          MEDIUM       6.0   0.6%   ·
  │ ✘✔✘✘ CVE-2026-1502          MEDIUM       5.7   0.6%   ·
  │ ✘✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·
  │ ✘✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✔ CVE-2026-2297          MEDIUM       5.7   0.2%   ·  ↳ V:UB:CVE-2026-2297
  │ ✘✔✘✘ CVE-2026-3276          MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·
  │ ✘✔✘✔ CVE-2026-6019          MEDIUM       6.1   0.2%   ·  ↳ V:UB:CVE-2026-6019
  │ ✘✔✘✘ CVE-2026-8328          MEDIUM       5.9   0.5%   ·
  │ ✘✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.5%   ·
  │ ✘✔✘✘ CVE-2025-13462         LOW          3.3   0.2%   ·
  │ ✘✔✘✔ CVE-2025-1795          LOW          2.3   0.6%   ·  ↳ V:UB:CVE-2025-1795
  │ ✘✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.8-dev@3.8.10-0ubuntu1~20.04.18
  │ OGTV
  │ ✘✔✘✘ CVE-2007-4559          CRITICAL     9.8  27.1%   ·
  │ ✘✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.4%   ·
  │ ✘✔✘✘ CVE-2026-6100          CRITICAL     9.1   0.8%   ·
  │ ✘✔✘✘ CVE-2020-10735         HIGH         7.5   4.5%   ·
  │ ✘✔✘✘ CVE-2025-13836         HIGH         7.5   1.6%   ·
  │ ✘✔✘✘ CVE-2025-69534         HIGH         8.2   0.6%   ·
  │ ✘✔✘✘ CVE-2025-8194          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·
  │ ✘✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·
  │ ✘✔✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·
  │ ✘✔✘✘ CVE-2026-19553         HIGH         7.6   0.4%   ·
  │ ✘✔✘✘ CVE-2026-3644          HIGH         7.5   0.5%   ·
  │ ✘✔✘✘ CVE-2026-4224          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-4519          HIGH         7.1   0.4%   ·
  │ ✘✔✘✘ CVE-2026-4786          HIGH         7.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·
  │ ✘✔✘✘ CVE-2026-9669          HIGH         8.2   0.4%   ·
  │ ✘✔✘✘ CVE-2021-23336         MEDIUM       5.9  40.7%   ·
  │ ✘✔✘✘ CVE-2025-11468         MEDIUM       5.7   0.6%   ·
  │ ✘✔✘✘ CVE-2025-12084         MEDIUM       6.3   0.8%   ·
  │ ✘✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.6%   ·
  │ ✘✔✘✘ CVE-2025-13837         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-15282         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2025-4516          MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✘ CVE-2025-6069          MEDIUM       4.3   0.6%   ·
  │ ✘✔✘✘ CVE-2025-6075          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2025-8291          MEDIUM       4.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-0672          MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-0865          MEDIUM       5.9   0.5%   ·
  │ ✘✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-1299          MEDIUM       6.0   0.6%   ·
  │ ✘✔✘✘ CVE-2026-1502          MEDIUM       5.7   0.6%   ·
  │ ✘✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·
  │ ✘✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✔ CVE-2026-2297          MEDIUM       5.7   0.2%   ·  ↳ V:UB:CVE-2026-2297
  │ ✘✔✘✘ CVE-2026-3276          MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6019          MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-8328          MEDIUM       5.9   0.5%   ·
  │ ✘✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.5%   ·
  │ ✘✔✘✘ CVE-2025-13462         LOW          3.3   0.2%   ·
  │ ✘✔✘✘ CVE-2025-1795          LOW          2.3   0.6%   ·
  │ ✘✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.8-minimal@3.8.10-0ubuntu1~20.04.18
  │ OGTV
  │ ✘✔✘✘ CVE-2007-4559          CRITICAL     9.8  27.1%   ·
  │ ✘✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.4%   ·
  │ ✘✔✘✘ CVE-2026-6100          CRITICAL     9.1   0.8%   ·
  │ ✘✔✘✘ CVE-2020-10735         HIGH         7.5   4.5%   ·
  │ ✘✔✘✘ CVE-2025-13836         HIGH         7.5   1.6%   ·
  │ ✘✔✘✘ CVE-2025-69534         HIGH         8.2   0.6%   ·
  │ ✘✔✘✘ CVE-2025-8194          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·
  │ ✘✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·
  │ ✘✔✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·
  │ ✘✔✘✘ CVE-2026-19553         HIGH         7.6   0.4%   ·
  │ ✘✔✘✘ CVE-2026-3644          HIGH         7.5   0.5%   ·
  │ ✘✔✘✘ CVE-2026-4224          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-4519          HIGH         7.1   0.4%   ·
  │ ✘✔✘✘ CVE-2026-4786          HIGH         7.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·
  │ ✘✔✘✘ CVE-2026-9669          HIGH         8.2   0.4%   ·
  │ ✘✔✘✘ CVE-2021-23336         MEDIUM       5.9  40.7%   ·
  │ ✘✔✘✘ CVE-2025-11468         MEDIUM       5.7   0.6%   ·
  │ ✘✔✘✘ CVE-2025-12084         MEDIUM       6.3   0.8%   ·
  │ ✘✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.6%   ·
  │ ✘✔✘✘ CVE-2025-13837         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-15282         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✔ CVE-2025-4516          MEDIUM       5.9   0.2%   ·  ↳ V:UB:CVE-2025-4516
  │ ✘✔✘✘ CVE-2025-6069          MEDIUM       4.3   0.6%   ·
  │ ✘✔✘✘ CVE-2025-6075          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2025-8291          MEDIUM       4.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-0672          MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-0865          MEDIUM       5.9   0.5%   ·
  │ ✘✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-1299          MEDIUM       6.0   0.6%   ·
  │ ✘✔✘✘ CVE-2026-1502          MEDIUM       5.7   0.6%   ·
  │ ✘✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·
  │ ✘✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✔ CVE-2026-2297          MEDIUM       5.7   0.2%   ·  ↳ V:UB:CVE-2026-2297
  │ ✘✔✘✘ CVE-2026-3276          MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6019          MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-8328          MEDIUM       5.9   0.5%   ·
  │ ✘✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.5%   ·
  │ ✘✔✘✘ CVE-2025-13462         LOW          3.3   0.2%   ·
  │ ✘✔✘✔ CVE-2025-1795          LOW          2.3   0.6%   ·  ↳ V:UB:CVE-2025-1795
  │ ✘✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.8-stdlib@3.8.10-0ubuntu1~20.04.18
  │ OGTV
  │ ✘✔✘✘ CVE-2007-4559          CRITICAL     9.8  27.1%   ·
  │ ✘✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.4%   ·
  │ ✘✔✘✘ CVE-2026-6100          CRITICAL     9.1   0.8%   ·
  │ ✘✔✘✘ CVE-2020-10735         HIGH         7.5   4.5%   ·
  │ ✘✔✘✘ CVE-2025-13836         HIGH         7.5   1.6%   ·
  │ ✘✔✘✘ CVE-2025-69534         HIGH         8.2   0.6%   ·
  │ ✘✔✘✘ CVE-2025-8194          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·
  │ ✘✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·
  │ ✘✔✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·
  │ ✘✔✘✘ CVE-2026-19553         HIGH         7.6   0.4%   ·
  │ ✘✔✘✘ CVE-2026-3644          HIGH         7.5   0.5%   ·
  │ ✘✔✘✘ CVE-2026-4224          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-4519          HIGH         7.1   0.4%   ·
  │ ✘✔✘✘ CVE-2026-4786          HIGH         7.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·
  │ ✘✔✘✘ CVE-2026-9669          HIGH         8.2   0.4%   ·
  │ ✘✔✘✘ CVE-2021-23336         MEDIUM       5.9  40.7%   ·
  │ ✘✔✘✘ CVE-2025-11468         MEDIUM       5.7   0.6%   ·
  │ ✘✔✘✘ CVE-2025-12084         MEDIUM       6.3   0.8%   ·
  │ ✘✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.6%   ·
  │ ✘✔✘✘ CVE-2025-13837         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-15282         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2025-4516          MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✘ CVE-2025-6069          MEDIUM       4.3   0.6%   ·
  │ ✘✔✘✘ CVE-2025-6075          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2025-8291          MEDIUM       4.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-0672          MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-0865          MEDIUM       5.9   0.5%   ·
  │ ✘✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-1299          MEDIUM       6.0   0.6%   ·
  │ ✘✔✘✘ CVE-2026-1502          MEDIUM       5.7   0.6%   ·
  │ ✘✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·
  │ ✘✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✔ CVE-2026-2297          MEDIUM       5.7   0.2%   ·  ↳ V:UB:CVE-2026-2297
  │ ✘✔✘✘ CVE-2026-3276          MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6019          MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-8328          MEDIUM       5.9   0.5%   ·
  │ ✘✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.5%   ·
  │ ✘✔✘✘ CVE-2025-13462         LOW          3.3   0.2%   ·
  │ ✘✔✘✘ CVE-2025-1795          LOW          2.3   0.6%   ·
  │ ✘✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsasl2-2@2.1.27%2Bdfsg-2ubuntu0.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-107161        HIGH         7.5   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsasl2-modules@2.1.27%2Bdfsg-2ubuntu0.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-107161        HIGH         7.5   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsasl2-modules-db@2.1.27%2Bdfsg-2ubuntu0.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-107161        HIGH         7.5   0.3%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsmartcols1@2.34-0.1ubuntu9.6
  │ OGTV
  │ ✘✔✘✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✔ CVE-2026-27456         MEDIUM       4.7   0.1%   ·  ↳ V:UB:CVE-2026-27456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsoup2.4-1@2.70.0-1ubuntu0.5
  │ OGTV
  │ ✘✔✘✔ CVE-2026-2369          CRITICAL     9.1   0.4%   ·  ↳ V:UB:CVE-2026-2369
  │ ✘✔✘✔ CVE-2025-11021         HIGH         7.5   0.6%   ·  ↳ V:UB:CVE-2025-11021
  │ ✘✔✘✔ CVE-2025-14523         HIGH         8.2   0.5%   ·  ↳ V:UB:CVE-2025-14523
  │ ✘✔✘✔ CVE-2025-32049         HIGH         7.5   0.9%   ·  ↳ V:UB:CVE-2025-32049
  │ ✘✔✘✔ CVE-2025-4948          HIGH         7.5   0.8%   ·  ↳ V:UB:CVE-2025-4948
  │ ✘✔✘✔ CVE-2026-0719          HIGH         8.6   0.6%   ·  ↳ V:UB:CVE-2026-0719
  │ ✘✔✘✘ CVE-2026-102555        HIGH         8.2   0.3%   ·
  │ ✘✔✘✘ CVE-2026-102556        HIGH         8.6   0.3%   ·
  │ ✘✔✘✘ CVE-2026-102557        HIGH         8.6   0.3%   ·
  │ ✘✔✘✘ CVE-2026-102558        HIGH         8.6   0.4%   ·
  │ ✘✔✘✘ CVE-2026-102559        HIGH         8.6   0.4%   ·
  │ ✘✔✘✘ CVE-2026-102560        HIGH         8.6   0.4%   ·
  │ ✘✔✘✘ CVE-2026-15709         HIGH         7.5   0.9%   ·
  │ ✘✔✘✘ CVE-2026-15711         HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-1761          HIGH         8.6   1.1%   ·
  │ ✘✔✘✔ CVE-2026-3099          HIGH         7.3   0.5%   ·  ↳ V:UB:CVE-2026-3099
  │ ✘✔✘✔ CVE-2026-5119          HIGH         8.2   0.3%   ·  ↳ V:UB:CVE-2026-5119
  │ ✘✔✘✔ CVE-2026-66338         HIGH         7.2   0.3%   ·  ↳ V:UB:CVE-2026-66338
  │ ✘✔✘✔ CVE-2025-32907         MEDIUM       5.3   0.7%   ·  ↳ V:UB:CVE-2025-32907
  │ ✘✔✘✔ CVE-2025-4035          MEDIUM       4.3   0.4%   ·  ↳ V:UB:CVE-2025-4035
  │ ✘✔✘✔ CVE-2025-4969          MEDIUM       6.5   0.9%   ·  ↳ V:UB:CVE-2025-4969
  │ ✘✔✘✔ CVE-2025-9901          MEDIUM       5.9   0.5%   ·  ↳ V:UB:CVE-2025-9901
  │ ✘✔✘✔ CVE-2026-0716          MEDIUM       4.8   0.4%   ·  ↳ V:UB:CVE-2026-0716
  │ ✘✔✘✘ CVE-2026-103399        MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-12548         MEDIUM       4.2   0.3%   ·
  │ ✘✔✘✘ CVE-2026-12549         MEDIUM       4.8   0.4%   ·
  │ ✘✔✘✔ CVE-2026-1467          MEDIUM       5.8   0.4%   ·  ↳ V:UB:CVE-2026-1467
  │ ✘✔✘✔ CVE-2026-1539          MEDIUM       5.8   0.3%   ·  ↳ V:UB:CVE-2026-1539
  │ ✘✔✘✘ CVE-2026-15714         MEDIUM       6.5   0.4%   ·
  │ ✘✔✘✘ CVE-2026-1760          MEDIUM       5.3   0.5%   ·
  │ ✘✔✘✔ CVE-2026-1801          MEDIUM       6.5   0.4%   ·  ↳ V:UB:CVE-2026-1801
  │ ✘✔✘✘ CVE-2026-2443          MEDIUM       5.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-2708          MEDIUM       5.3   0.3%   ·
  │ ✘✔✘✔ CVE-2026-3632          MEDIUM       5.5   0.4%   ·  ↳ V:UB:CVE-2026-3632
  │ ✘✔✘✔ CVE-2026-3633          MEDIUM       6.5   0.4%   ·  ↳ V:UB:CVE-2026-3633
  │ ✘✔✘✔ CVE-2026-3634          MEDIUM       6.5   0.3%   ·  ↳ V:UB:CVE-2026-3634
  │ ✘✔✘✘ CVE-2026-6324          MEDIUM       4.8   0.9%   ·
  │ ✘✔✘✔ CVE-2026-66337         MEDIUM       6.5   0.2%   ·  ↳ V:UB:CVE-2026-66337
  │ ✘✔✘✔ CVE-2026-66339         MEDIUM       6.5   0.2%   ·  ↳ V:UB:CVE-2026-66339
  │ ✘✔✘✔ CVE-2026-77014         MEDIUM       5.3   0.2%   ·  ↳ V:UB:CVE-2026-77014
  │ ✘✔✘✔ CVE-2026-77680         MEDIUM       5.3   0.3%   ·  ↳ V:UB:CVE-2026-77680
  │ ✘✔✘✔ CVE-2025-4945          LOW          3.7   0.7%   ·  ↳ V:UB:CVE-2025-4945
  │ ✘✔✘✘ CVE-2026-12547         LOW          3.4   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsqlite3-0@3.31.1-4ubuntu0.7
  │ OGTV
  │ ✘✔✘✔ CVE-2025-6965          HIGH         7.7  71.4%   ·  ↳ V:UB:CVE-2025-6965
  │ ✘✔✘✘ CVE-2026-11822         HIGH         8.5   0.3%   ·
  │ ✘✔✘✘ CVE-2026-11824         HIGH         8.5   0.2%   ·
  │ ✘✔✘✔ CVE-2026-39113         MEDIUM       4.0   0.2%   ·  ↳ V:UB:CVE-2026-39113
  │ ✘✔✘✘ CVE-2026-50812         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-50813         MEDIUM       6.1   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libssh-4@0.9.3-2ubuntu2.5
  │ OGTV
  │ ✘✔✘✔ CVE-2025-5318          HIGH         8.1   1.8%   ·  ↳ V:UB:CVE-2025-5318
  │ ✘✔✘✘ CVE-2025-5372          HIGH         8.8   0.5%   ·
  │ ✘✔✘✔ CVE-2026-0966          HIGH         8.2   0.6%   ·  ↳ V:UB:CVE-2026-0966
  │ ✘✔✘✔ CVE-2026-3731          HIGH         7.5   1.2%   ·  ↳ V:UB:CVE-2026-3731
  │ ✘✔✘✘ CVE-2026-59847         HIGH         7.5   0.3%   ·
  │ ✘✔✘✘ CVE-2026-59850         HIGH         7.5   0.3%   ·
  │ ✘✔✘✔ CVE-2025-4877          MEDIUM       4.5   0.2%   ·  ↳ V:UB:CVE-2025-4877
  │ ✘✔✘✔ CVE-2025-8114          MEDIUM       4.7   0.2%   ·  ↳ V:UB:CVE-2025-8114
  │ ✘✔✘✔ CVE-2026-0964          MEDIUM       6.3   0.4%   ·  ↳ V:UB:CVE-2026-0964
  │ ✘✔✘✔ CVE-2026-0967          MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-0967
  │ ✘✔✘✘ CVE-2026-59843         MEDIUM       6.5   0.7%   ·
  │ ✘✔✘✔ CVE-2026-59845         MEDIUM       5.9   0.1%   ·  ↳ V:UB:CVE-2026-59845
  │ ✘✔✘✘ CVE-2026-59848         MEDIUM       5.3   0.3%   ·
  │ ✘✔✘✔ CVE-2025-4878          LOW          3.6   0.2%   ·  ↳ V:UB:CVE-2025-4878
  │ ✘✔✘✔ CVE-2025-8277          LOW          3.1   0.4%   ·  ↳ V:UB:CVE-2025-8277
  │ ✘✔✘✔ CVE-2026-0965          LOW          3.3   0.2%   ·  ↳ V:UB:CVE-2026-0965
  │ ✘✔✘✔ CVE-2026-0968          LOW          3.1   0.4%   ·  ↳ V:UB:CVE-2026-0968
  │ ✘✔✘✘ CVE-2026-59846         LOW          3.9   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libssl1.1@1.1.1f-1ubuntu2.24
  │ OGTV
  │ ✘✔✘✔ CVE-2025-69419         HIGH         7.4   0.6%   ·  ↳ V:UB:CVE-2025-69419
  │ ✘✔✘✔ CVE-2025-69420         HIGH         7.5   0.9%   ·  ↳ V:UB:CVE-2025-69420
  │ ✘✔✘✔ CVE-2025-69421         HIGH         7.5   1.0%   ·  ↳ V:UB:CVE-2025-69421
  │ ✘✔✘✔ CVE-2025-9230          HIGH         7.5   1.6%   ·  ↳ V:UB:CVE-2025-9230
  │ ✘✔✘✔ CVE-2026-28387         HIGH         8.1   0.7%   ·  ↳ V:UB:CVE-2026-28387
  │ ✘✔✘✔ CVE-2026-28388         HIGH         7.5   0.9%   ·  ↳ V:UB:CVE-2026-28388
  │ ✘✔✘✔ CVE-2026-28389         HIGH         7.5   0.8%   ·  ↳ V:UB:CVE-2026-28389
  │ ✘✔✘✔ CVE-2026-28390         HIGH         7.5   0.8%   ·  ↳ V:UB:CVE-2026-28390
  │ ✘✔✘✘ CVE-2026-34180         HIGH         7.5   1.0%   ·
  │ ✘✔✘✘ CVE-2026-45447         HIGH         8.8   4.0%   ·
  │ ✘✔✘✔ CVE-2026-54874         HIGH         7.5   0.6%   ·  ↳ V:UB:CVE-2026-54874
  │ ✘✔✘✔ CVE-2026-63072         HIGH         7.5   0.9%   ·  ↳ V:UB:CVE-2026-63072
  │ ✘✔✘✘ CVE-2026-7383          HIGH         8.1   0.8%   ·
  │ ✘✔✘✔ CVE-2026-84782         HIGH         8.2   0.4%   ·  ↳ V:UB:CVE-2026-84782
  │ ✘✔✘✘ CVE-2026-9076          HIGH         7.5   0.7%   ·
  │ ✘✔✘✔ CVE-2025-68160         MEDIUM       4.7   0.2%   ·  ↳ V:UB:CVE-2025-68160
  │ ✘✔✘✔ CVE-2025-69418         MEDIUM       4.0   0.1%   ·  ↳ V:UB:CVE-2025-69418
  │ ✘✔✘✔ CVE-2026-22795         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-22795
  │ ✘✔✘✔ CVE-2026-22796         MEDIUM       5.3   0.6%   ·  ↳ V:UB:CVE-2026-22796
  │ ✘✔✘✔ CVE-2026-35189         MEDIUM       5.3   0.3%   ·  ↳ V:UB:CVE-2026-35189
  │ ✘✔✘✘ CVE-2026-42766         MEDIUM       5.9   1.1%   ·
  │ ✘✔✘✘ CVE-2026-75806         MEDIUM       5.3   0.4%   ·
  │ ✘✔✘✔ CVE-2026-54872         LOW          3.7   0.3%   ·  ↳ V:UB:CVE-2026-54872
  │ ✘✔✘✔ CVE-2026-77696         LOW          3.7   0.2%   ·  ↳ V:UB:CVE-2026-77696
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libstdc%2B%2B-9-dev@9.4.0-1ubuntu1~20.04.2
  │ OGTV
  │ ✘✔✘✘ CVE-2020-23026         HIGH         7.5   1.0%   ·
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  │ ✘✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libstdc%2B%2B6@10.5.0-1ubuntu1~20.04
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  │ ✘✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsystemd0@245.4-4ubuntu3.24
  │ OGTV
  │ ✘✔✘✔ CVE-2023-26604         HIGH         7.8   1.1%   ·  ↳ V:UB:CVE-2023-26604
  │ ✘✔✘✘ CVE-2020-13776         MEDIUM       6.7   0.5%   ·
  │ ✘✔✘✔ CVE-2023-7008          MEDIUM       5.9   0.8%   ·  ↳ V:UB:CVE-2023-7008
  │ ✘✔✘✘ CVE-2025-4598          MEDIUM       4.7   1.2%   ·
  │ ✘✔✘✔ CVE-2026-29111         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-29111
  │ ✘✔✘✔ CVE-2026-40225         MEDIUM       6.4   0.2%   ·  ↳ V:UB:CVE-2026-40225
  │ ✘✔✘✘ CVE-2026-40226         MEDIUM       6.4   0.1%   ·
  │ ✘✔✘✔ CVE-2026-40228         LOW          3.3   0.1%   ·  ↳ V:UB:CVE-2026-40228
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libtasn1-6@4.16.0-2ubuntu0.1
  │ OGTV
  │ ✔✔✘✔ CVE-2021-46848         CRITICAL     9.1   2.3%   ·  ↳ O:UBUNTU-CVE-2021-46848 | V:UB:CVE-2021-46848
  │ ✔✔✘✔ CVE-2025-13151         HIGH         7.5   1.2%   ·  ↳ O:UBUNTU-CVE-2025-13151 | V:UB:CVE-2025-13151
  │ ✔✘✘✘ USN-7954-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libtinfo6@6.2-0ubuntu2.1
  │ OGTV
  │ ✘✔✘✘ CVE-2025-69720         CRITICAL     9.8   0.4%   ·
  │ ✘✔✘✔ CVE-2023-50495         MEDIUM       6.5   1.0%   ·  ↳ V:UB:CVE-2023-50495
  │ ✘✔✘✔ CVE-2025-6141          MEDIUM       4.8   0.2%   ·  ↳ V:UB:CVE-2025-6141
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libtsan0@10.5.0-1ubuntu1~20.04
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  │ ✘✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libubsan1@10.5.0-1ubuntu1~20.04
  │ OGTV
  │ ✘✔✘✘ CVE-2026-102010        HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·
  │ ✘✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ V:UB:CVE-2023-4039
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libudev1@245.4-4ubuntu3.24
  │ OGTV
  │ ✘✔✘✔ CVE-2023-26604         HIGH         7.8   1.1%   ·  ↳ V:UB:CVE-2023-26604
  │ ✘✔✘✘ CVE-2020-13776         MEDIUM       6.7   0.5%   ·
  │ ✘✔✘✔ CVE-2023-7008          MEDIUM       5.9   0.8%   ·  ↳ V:UB:CVE-2023-7008
  │ ✘✔✘✘ CVE-2025-4598          MEDIUM       4.7   1.2%   ·
  │ ✘✔✘✔ CVE-2026-29111         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-29111
  │ ✘✔✘✔ CVE-2026-40225         MEDIUM       6.4   0.2%   ·  ↳ V:UB:CVE-2026-40225
  │ ✘✔✘✘ CVE-2026-40226         MEDIUM       6.4   0.1%   ·
  │ ✘✔✘✔ CVE-2026-40228         LOW          3.3   0.1%   ·  ↳ V:UB:CVE-2026-40228
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libuuid1@2.34-0.1ubuntu9.6
  │ OGTV
  │ ✘✔✘✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✔ CVE-2026-27456         MEDIUM       4.7   0.1%   ·  ↳ V:UB:CVE-2026-27456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libxml2@2.9.10%2Bdfsg-5ubuntu0.20.04.10
  │ OGTV
  │ ✔✔✘✔ CVE-2025-49794         CRITICAL     9.1   0.8%   ·  ↳ O:UBUNTU-CVE-2025-49794,USN-7694-1 | V:UB:CVE-2025-49794
  │ ✔✔✘✔ CVE-2025-49796         CRITICAL     9.1   1.6%   ·  ↳ O:UBUNTU-CVE-2025-49796,USN-7694-1 | V:UB:CVE-2025-49796
  │ ✔✔✘✔ CVE-2025-6021          HIGH         7.5   1.4%   ·  ↳ O:UBUNTU-CVE-2025-6021,USN-7694-1 | V:UB:CVE-2025-6021
  │ ✔✔✘✔ CVE-2025-7425          HIGH         7.8   0.4%   ·  ↳ O:UBUNTU-CVE-2025-7425,USN-7852-2 | V:UB:CVE-2025-7425
  │ ✔✔✘✘ CVE-2026-11979         HIGH         7.8   0.1%   ·  ↳ O:UBUNTU-CVE-2026-11979
  │ ✔✔✘✔ CVE-2026-74860         HIGH         8.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-74860,USN-8787-1 | V:UB:CVE-2026-74860
  │ ✔✔✘✔ CVE-2026-86138         HIGH         7.8   0.1%   ·  ↳ O:UBUNTU-CVE-2026-86138,USN-8910-1 | V:UB:CVE-2026-86138
  │ ✔✘✘✘ CVE-2026-86139         HIGH         7.8   0.2%   ·  ↳ O:USN-8910-1
  │ ✔✔✘✔ CVE-2026-86140         HIGH         8.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-86140,USN-8787-1 | V:UB:CVE-2026-86140
  │ ✔✔✘✔ CVE-2026-86142         HIGH         7.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-86142,USN-8910-1 | V:UB:CVE-2026-86142
  │ ✔✔✘✔ CVE-2026-86143         HIGH         7.3   0.2%   ·  ↳ O:UBUNTU-CVE-2026-86143,USN-8910-1 | V:UB:CVE-2026-86143
  │ ✔✔✘✔ CVE-2026-86144         HIGH         7.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-86144,USN-8910-1 | V:UB:CVE-2026-86144
  │ ✔✘✘✘ CVE-2025-26434         MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2025-26434
  │ ✔✔✘✔ CVE-2025-8732          MEDIUM       4.8   0.2%   ·  ↳ O:UBUNTU-CVE-2025-8732 | V:UB:CVE-2025-8732
  │ ✔✔✘✔ CVE-2025-9714          MEDIUM       6.2   0.2%   ·  ↳ O:UBUNTU-CVE-2025-9714,USN-7743-1 | V:UB:CVE-2025-9714
  │ ✔✔✘✔ CVE-2026-0990          MEDIUM       5.9   1.0%   ·  ↳ O:UBUNTU-CVE-2026-0990 | V:UB:CVE-2026-0990
  │ ✔✔✘✔ CVE-2026-76781         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2026-76781,USN-8910-1 | V:UB:CVE-2026-76781
  │ ✔✔✘✔ CVE-2025-6170          LOW          2.5   0.3%   ·  ↳ O:UBUNTU-CVE-2025-6170,USN-7694-1 | V:UB:CVE-2025-6170
  │ ✔✔✘✔ CVE-2026-0989          LOW          3.7   0.5%   ·  ↳ O:UBUNTU-CVE-2026-0989 | V:UB:CVE-2026-0989
  │ ✔✔✘✔ CVE-2026-0992          LOW          2.9   0.5%   ·  ↳ O:UBUNTU-CVE-2026-0992 | V:UB:CVE-2026-0992
  │ ✔✘✘✘ USN-7974-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/login@1%3A4.8.1-1ubuntu5.20.04.5
  │ OGTV
  │ ✘✔✘✘ CVE-2013-4235          MEDIUM       4.7   0.3%   ·
  │ ✘✔✘✔ CVE-2023-29383         LOW          3.3   0.4%   ·  ↳ V:UB:CVE-2023-29383
  │ ✘✔✘✔ CVE-2024-56433         LOW          3.6   0.4%   ·  ↳ V:UB:CVE-2024-56433
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/mount@2.34-0.1ubuntu9.6
  │ OGTV
  │ ✘✔✘✘ CVE-2026-53613         HIGH         7.0   0.1%   ·
  │ ✘✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·
  │ ✘✔✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✔ CVE-2026-27456         MEDIUM       4.7   0.1%   ·  ↳ V:UB:CVE-2026-27456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/ncurses-base@6.2-0ubuntu2.1
  │ OGTV
  │ ✘✔✘✘ CVE-2025-69720         CRITICAL     9.8   0.4%   ·
  │ ✘✔✘✔ CVE-2023-50495         MEDIUM       6.5   1.0%   ·  ↳ V:UB:CVE-2023-50495
  │ ✘✔✘✘ CVE-2025-6141          MEDIUM       4.8   0.2%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/ncurses-bin@6.2-0ubuntu2.1
  │ OGTV
  │ ✘✔✘✔ CVE-2025-69720         CRITICAL     9.8   0.4%   ·  ↳ V:UB:CVE-2025-69720
  │ ✘✔✘✔ CVE-2023-50495         MEDIUM       6.5   1.0%   ·  ↳ V:UB:CVE-2023-50495
  │ ✘✔✘✔ CVE-2025-6141          MEDIUM       4.8   0.2%   ·  ↳ V:UB:CVE-2025-6141
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/openssl@1.1.1f-1ubuntu2.24
  │ OGTV
  │ ✔✘✘✘ CVE-2024-5535          CRITICAL     9.1   5.6%   ·  ↳ O:USN-8678-2
  │ ✔✔✘✔ CVE-2025-69419         HIGH         7.4   0.6%   ·  ↳ O:UBUNTU-CVE-2025-69419 | V:UB:CVE-2025-69419
  │ ✔✔✘✔ CVE-2025-69420         HIGH         7.5   0.9%   ·  ↳ O:UBUNTU-CVE-2025-69420 | V:UB:CVE-2025-69420
  │ ✔✔✘✔ CVE-2025-69421         HIGH         7.5   1.0%   ·  ↳ O:UBUNTU-CVE-2025-69421 | V:UB:CVE-2025-69421
  │ ✔✔✘✔ CVE-2025-9230          HIGH         7.5   1.6%   ·  ↳ O:UBUNTU-CVE-2025-9230,USN-7786-1 | V:UB:CVE-2025-9230
  │ ✔✔✘✔ CVE-2026-28387         HIGH         8.1   0.7%   ·  ↳ O:UBUNTU-CVE-2026-28387 | V:UB:CVE-2026-28387
  │ ✔✔✘✔ CVE-2026-28388         HIGH         7.5   0.9%   ·  ↳ O:UBUNTU-CVE-2026-28388 | V:UB:CVE-2026-28388
  │ ✔✔✘✔ CVE-2026-28389         HIGH         7.5   0.8%   ·  ↳ O:UBUNTU-CVE-2026-28389 | V:UB:CVE-2026-28389
  │ ✔✔✘✔ CVE-2026-28390         HIGH         7.5   0.8%   ·  ↳ O:UBUNTU-CVE-2026-28390 | V:UB:CVE-2026-28390
  │ ✔✔✘✔ CVE-2026-34180         HIGH         7.5   1.0%   ·  ↳ O:UBUNTU-CVE-2026-34180 | V:UB:CVE-2026-34180
  │ ✔✔✘✔ CVE-2026-45447         HIGH         8.8   4.0%   ·  ↳ O:UBUNTU-CVE-2026-45447 | V:UB:CVE-2026-45447
  │ ✔✔✘✔ CVE-2026-54874         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-54874,USN-8678-2 | V:UB:CVE-2026-54874
  │ ✔✔✘✔ CVE-2026-63072         HIGH         7.5   0.9%   ·  ↳ O:UBUNTU-CVE-2026-63072,USN-8678-2 | V:UB:CVE-2026-63072
  │ ✔✔✘✔ CVE-2026-7383          HIGH         8.1   0.8%   ·  ↳ O:UBUNTU-CVE-2026-7383 | V:UB:CVE-2026-7383
  │ ✔✔✘✔ CVE-2026-84782         HIGH         8.2   0.4%   ·  ↳ O:UBUNTU-CVE-2026-84782,USN-8847-2 | V:UB:CVE-2026-84782
  │ ✔✔✘✔ CVE-2026-9076          HIGH         7.5   0.7%   ·  ↳ O:UBUNTU-CVE-2026-9076 | V:UB:CVE-2026-9076
  │ ✔✘✘✘ CVE-2024-2511          MEDIUM       5.9  52.4%   ·  ↳ O:USN-8678-2
  │ ✔✔✘✔ CVE-2025-68160         MEDIUM       4.7   0.2%   ·  ↳ O:UBUNTU-CVE-2025-68160 | V:UB:CVE-2025-68160
  │ ✔✔✘✔ CVE-2025-69418         MEDIUM       4.0   0.1%   ·  ↳ O:UBUNTU-CVE-2025-69418 | V:UB:CVE-2025-69418
  │ ✔✘✘✘ CVE-2025-9231          MEDIUM       6.5   2.2%   ·  ↳ O:USN-7786-1
  │ ✔✘✘✘ CVE-2025-9232          MEDIUM       5.9   2.0%   ·  ↳ O:USN-7786-1
  │ ✔✔✘✔ CVE-2026-22795         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2026-22795 | V:UB:CVE-2026-22795
  │ ✔✔✘✔ CVE-2026-22796         MEDIUM       5.3   0.6%   ·  ↳ O:UBUNTU-CVE-2026-22796 | V:UB:CVE-2026-22796
  │ ✔✔✘✔ CVE-2026-35189         MEDIUM       5.3   0.3%   ·  ↳ O:UBUNTU-CVE-2026-35189,USN-8847-2 | V:UB:CVE-2026-35189
  │ ✔✔✘✔ CVE-2026-42766         MEDIUM       5.9   1.1%   ·  ↳ O:UBUNTU-CVE-2026-42766 | V:UB:CVE-2026-42766
  │ ✔✔✘✘ CVE-2026-75806         MEDIUM       5.3   0.4%   ·  ↳ O:UBUNTU-CVE-2026-75806
  │ ✔✔✘✔ CVE-2026-54872         LOW          3.7   0.3%   ·  ↳ O:UBUNTU-CVE-2026-54872,USN-8847-2 | V:UB:CVE-2026-54872
  │ ✔✔✘✔ CVE-2026-77696         LOW          3.7   0.2%   ·  ↳ O:UBUNTU-CVE-2026-77696,USN-8847-2 | V:UB:CVE-2026-77696
  │ ✔✘✘✘ USN-7980-2             ?             -       -   ·
  │ ✔✘✘✘ USN-8155-2             ?             -       -   ·
  │ ✔✘✘✘ USN-8414-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/packagekit@1.1.13-2ubuntu1.1
  │ OGTV
  │ ✔✔✘✔ CVE-2026-41651         HIGH         8.8   0.5%   ·  ↳ O:UBUNTU-CVE-2026-41651 | V:UB:CVE-2026-41651
  │ ✔✔✘✘ CVE-2026-10294         MEDIUM       5.3   0.2%   ·  ↳ O:UBUNTU-CVE-2026-10294
  │ ✔✔✘✔ CVE-2022-0987          LOW          3.3   0.3%   ·  ↳ O:UBUNTU-CVE-2022-0987 | V:UB:CVE-2022-0987
  │ ✔✔✘✔ CVE-2024-0217          LOW          3.3   0.2%   ·  ↳ O:UBUNTU-CVE-2024-0217 | V:UB:CVE-2024-0217
  │ ✔✘✘✘ USN-8195-3             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/packagekit-tools@1.1.13-2ubuntu1.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-41651         HIGH         8.8   0.5%   ·
  │ ✘✔✘✘ CVE-2026-10294         MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✔ CVE-2022-0987          LOW          3.3   0.3%   ·  ↳ V:UB:CVE-2022-0987
  │ ✘✔✘✔ CVE-2024-0217          LOW          3.3   0.2%   ·  ↳ V:UB:CVE-2024-0217
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/passwd@1%3A4.8.1-1ubuntu5.20.04.5
  │ OGTV
  │ ✘✔✘✘ CVE-2013-4235          MEDIUM       4.7   0.3%   ·
  │ ✘✔✘✔ CVE-2023-29383         LOW          3.3   0.4%   ·  ↳ V:UB:CVE-2023-29383
  │ ✘✔✘✔ CVE-2024-56433         LOW          3.6   0.4%   ·  ↳ V:UB:CVE-2024-56433
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/patch@2.7.6-6
  │ OGTV
  │ ✔✔✘✔ CVE-2018-6952          HIGH         7.5   8.2%   ·  ↳ O:UBUNTU-CVE-2018-6952 | V:UB:CVE-2018-6952
  │ ✔✔✘✔ CVE-2019-20633         MEDIUM       5.5   1.0%   ·  ↳ O:UBUNTU-CVE-2019-20633 | V:UB:CVE-2019-20633
  │ ✔✔✘✔ CVE-2021-45261         MEDIUM       5.5   0.8%   ·  ↳ O:UBUNTU-CVE-2021-45261 | V:UB:CVE-2021-45261
  │ ✔✔✘✔ CVE-2026-56288         MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-56288 | V:UB:CVE-2026-56289
  │ ✔✔✘✔ CVE-2026-56289         MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-56289 | V:UB:CVE-2026-56289
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/perl@5.30.0-9ubuntu0.5
  │ OGTV
  │ ✔✔✘✘ CVE-2011-10043         CRITICAL     9.8   0.8%   ·  ↳ O:UBUNTU-CVE-2011-10043
  │ ✔✔✘✘ CVE-2017-20230         CRITICAL    10.0   0.6%   ·  ↳ O:UBUNTU-CVE-2017-20230
  │ ✔✔✘✘ CVE-2026-12087         CRITICAL     9.1   0.4%   ·  ↳ O:UBUNTU-CVE-2026-12087,USN-8675-1
  │ ✔✔✘✘ CVE-2026-13221         CRITICAL     9.1   0.4%   ·  ↳ O:UBUNTU-CVE-2026-13221,USN-8675-1
  │ ✔✔✘✘ CVE-2026-4176          CRITICAL     9.8   0.8%   ·  ↳ O:UBUNTU-CVE-2026-4176
  │ ✔✔✘✔ CVE-2026-42496         CRITICAL     9.1   0.4%   ·  ↳ O:UBUNTU-CVE-2026-42496,USN-8467-1 | V:UB:CVE-2026-42496
  │ ✔✔✘✘ CVE-2026-57433         CRITICAL     9.8   0.4%   ·  ↳ O:UBUNTU-CVE-2026-57433,USN-8675-1
  │ ✔✔✘✔ CVE-2026-8376          CRITICAL     9.8   0.5%   ·  ↳ O:UBUNTU-CVE-2026-8376,USN-8467-1 | V:UB:CVE-2026-8376
  │ ✔✔✘✘ CVE-2023-31486         HIGH         8.1   1.7%   ·  ↳ O:UBUNTU-CVE-2023-31486
  │ ✔✔✘✘ CVE-2023-47039         HIGH         7.8   0.4%   ·  ↳ O:UBUNTU-CVE-2023-47039
  │ ✔✔✘✘ CVE-2026-42497         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-42497
  │ ✔✔✘✘ CVE-2026-48959         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-48959
  │ ✔✔✘✘ CVE-2026-48961         HIGH         7.3   0.4%   ·  ↳ O:UBUNTU-CVE-2026-48961
  │ ✔✔✘✘ CVE-2026-48962         HIGH         7.8   0.5%   ·  ↳ O:UBUNTU-CVE-2026-48962
  │ ✔✔✘✘ CVE-2026-57432         HIGH         8.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57432,USN-8675-1
  │ ✔✔✘✘ CVE-2026-7017          HIGH         7.1   0.2%   ·  ↳ O:UBUNTU-CVE-2026-7017
  │ ✔✔✘✘ CVE-2026-82560         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-82560
  │ ✔✔✘✘ CVE-2026-9538          HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-9538
  │ ✔✔✘✘ CVE-2025-15649         MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2025-15649
  │ ✔✔✘✘ CVE-2025-40909         MEDIUM       5.9   0.5%   ·  ↳ O:UBUNTU-CVE-2025-40909
  │ ✔✔✘✘ CVE-2026-15534         MEDIUM       5.7   0.3%   ·  ↳ O:UBUNTU-CVE-2026-15534,USN-8736-1
  │ ✔✔✘✘ CVE-2026-19487         MEDIUM       5.3   0.4%   ·  ↳ O:UBUNTU-CVE-2026-19487,USN-8736-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/perl-base@5.30.0-9ubuntu0.5
  │ OGTV
  │ ✘✔✘✘ CVE-2011-10043         CRITICAL     9.8   0.8%   ·
  │ ✘✔✘✘ CVE-2017-20230         CRITICAL    10.0   0.6%   ·
  │ ✘✔✘✔ CVE-2026-12087         CRITICAL     9.1   0.4%   ·  ↳ V:UB:CVE-2026-12087
  │ ✘✔✘✔ CVE-2026-13221         CRITICAL     9.1   0.4%   ·  ↳ V:UB:CVE-2026-13221
  │ ✘✔✘✘ CVE-2026-4176          CRITICAL     9.8   0.8%   ·
  │ ✘✔✘✔ CVE-2026-42496         CRITICAL     9.1   0.4%   ·  ↳ V:UB:CVE-2026-42496
  │ ✘✔✘✔ CVE-2026-57433         CRITICAL     9.8   0.4%   ·  ↳ V:UB:CVE-2026-57433
  │ ✘✔✘✔ CVE-2026-8376          CRITICAL     9.8   0.5%   ·  ↳ V:UB:CVE-2026-8376
  │ ✘✔✘✘ CVE-2023-31486         HIGH         8.1   1.7%   ·
  │ ✘✔✘✘ CVE-2023-47039         HIGH         7.8   0.4%   ·
  │ ✘✔✘✘ CVE-2026-42497         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2026-48959         HIGH         7.5   0.6%   ·
  │ ✘✔✘✘ CVE-2026-48961         HIGH         7.3   0.4%   ·
  │ ✘✔✘✘ CVE-2026-48962         HIGH         7.8   0.5%   ·
  │ ✘✔✘✔ CVE-2026-57432         HIGH         8.4   0.2%   ·  ↳ V:UB:CVE-2026-57432
  │ ✘✔✘✘ CVE-2026-7017          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-82560         HIGH         7.5   0.6%   ·
  │ ✘✔✘✘ CVE-2026-9538          HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15649         MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2025-40909         MEDIUM       5.9   0.5%   ·
  │ ✘✔✘✔ CVE-2026-15534         MEDIUM       5.7   0.3%   ·  ↳ V:UB:CVE-2026-15534
  │ ✘✔✘✔ CVE-2026-19487         MEDIUM       5.3   0.4%   ·  ↳ V:UB:CVE-2026-19487
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/perl-modules-5.30@5.30.0-9ubuntu0.5
  │ OGTV
  │ ✘✔✘✘ CVE-2011-10043         CRITICAL     9.8   0.8%   ·
  │ ✘✔✘✘ CVE-2017-20230         CRITICAL    10.0   0.6%   ·
  │ ✘✔✘✔ CVE-2026-12087         CRITICAL     9.1   0.4%   ·  ↳ V:UB:CVE-2026-12087
  │ ✘✔✘✔ CVE-2026-13221         CRITICAL     9.1   0.4%   ·  ↳ V:UB:CVE-2026-13221
  │ ✘✔✘✘ CVE-2026-4176          CRITICAL     9.8   0.8%   ·
  │ ✘✔✘✔ CVE-2026-42496         CRITICAL     9.1   0.4%   ·  ↳ V:UB:CVE-2026-42496
  │ ✘✔✘✔ CVE-2026-57433         CRITICAL     9.8   0.4%   ·  ↳ V:UB:CVE-2026-57433
  │ ✘✔✘✔ CVE-2026-8376          CRITICAL     9.8   0.5%   ·  ↳ V:UB:CVE-2026-8376
  │ ✘✔✘✘ CVE-2023-31486         HIGH         8.1   1.7%   ·
  │ ✘✔✘✘ CVE-2023-47039         HIGH         7.8   0.4%   ·
  │ ✘✔✘✘ CVE-2026-42497         HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2026-48959         HIGH         7.5   0.6%   ·
  │ ✘✔✘✘ CVE-2026-48961         HIGH         7.3   0.4%   ·
  │ ✘✔✘✘ CVE-2026-48962         HIGH         7.8   0.5%   ·
  │ ✘✔✘✔ CVE-2026-57432         HIGH         8.4   0.2%   ·  ↳ V:UB:CVE-2026-57432
  │ ✘✔✘✘ CVE-2026-7017          HIGH         7.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-82560         HIGH         7.5   0.6%   ·
  │ ✘✔✘✘ CVE-2026-9538          HIGH         7.5   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15649         MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2025-40909         MEDIUM       5.9   0.5%   ·
  │ ✘✔✘✘ CVE-2026-15534         MEDIUM       5.7   0.3%   ·
  │ ✘✔✘✘ CVE-2026-19487         MEDIUM       5.3   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/policykit-1@0.105-26ubuntu1.3
  │ OGTV
  │ ✔✔✘✔ CVE-2016-2568          HIGH         7.8   0.4%   ·  ↳ O:UBUNTU-CVE-2016-2568 | V:UB:CVE-2016-2568
  │ ✔✔✘✘ CVE-2025-7519          MEDIUM       6.7   0.2%   ·  ↳ O:UBUNTU-CVE-2025-7519
  │ ✔✔✘✘ CVE-2026-4897          MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2026-4897
  │ ✔✔✘✘ CVE-2026-85498         ?             -       -   ·  ↳ O:UBUNTU-CVE-2026-85498
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python-apt-common@2.0.1ubuntu0.20.04.1
  │ OGTV
  │ ✘✔✘✔ CVE-2025-6966          MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2025-6966
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python-pip-whl@20.0.2-5ubuntu1.11
  │ OGTV
  │ ✘✔✘✘ CVE-2023-37920         CRITICAL     9.8   0.6%   ·
  │ ✘✔✘✘ CVE-2018-20225         HIGH         7.8   1.8%   ·
  │ ✘✔✘✘ CVE-2024-3651          HIGH         7.5   1.4%   ·
  │ ✘✔✘✘ CVE-2024-6345          HIGH         8.8   1.9%   ·
  │ ✘✔✘✔ CVE-2025-47273         HIGH         8.8   1.6%   ·  ↳ V:UB:CVE-2025-47273
  │ ✘✘✘✔ CVE-2025-66418         HIGH         8.9   0.7%   ·  ↳ V:UB:CVE-2025-66418
  │ ✘✔✘✘ CVE-2025-66471         HIGH         8.9   0.7%   ·
  │ ✘✘✘✔ CVE-2026-21441         HIGH         8.9   2.9%   ·  ↳ V:UB:CVE-2026-21441
  │ ✘✔✘✘ CVE-2026-24049         HIGH         7.1   0.4%   ·
  │ ✘✔✘✘ CVE-2026-44431         HIGH         8.2   0.3%   ·
  │ ✘✔✘✘ CVE-2026-44432         HIGH         8.9   0.9%   ·
  │ ✘✔✘✘ CVE-2026-57585         HIGH         7.5   0.5%   ·
  │ ✘✔✘✘ CVE-2026-8643          HIGH         8.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-97687         HIGH         8.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-97689         HIGH         8.9   0.3%   ·
  │ ✘✔✘✘ CVE-2024-35195         MEDIUM       5.6   0.3%   ·
  │ ✘✔✘✔ CVE-2025-8869          MEDIUM       5.9   0.5%   ·  ↳ V:UB:CVE-2025-8869
  │ ✘✔✘✘ CVE-2026-13346         MEDIUM       6.5   0.3%   ·
  │ ✘✔✘✘ CVE-2026-25645         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-3219          MEDIUM       4.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-45409         MEDIUM       6.9   0.5%   ·
  │ ✘✔✘✘ CVE-2026-6357          MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-97688         MEDIUM       6.9   0.3%   ·
  │ ✘✔✘✔ CVE-2026-1703          LOW          2.0   0.4%   ·  ↳ V:UB:CVE-2026-1703
  │ ✘✘✘✔ CVE-2026-9375          ?            0.0   0.3%   ·  ↳ V:UB:CVE-2026-9375
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-apt@2.0.1ubuntu0.20.04.1
  │ OGTV
  │ ✘✔✘✔ CVE-2025-6966          MEDIUM       6.9   0.1%   ·  ↳ V:UB:CVE-2025-6966
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-certifi@2019.11.28-1
  │ OGTV
  │ ✘✔✘✘ CVE-2023-37920         CRITICAL     9.8   0.6%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-idna@2.8-1ubuntu0.1
  │ OGTV
  │ ✘✔✘✘ CVE-2026-45409         MEDIUM       6.9   0.5%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-pip@20.0.2-5ubuntu1.11
  │ OGTV
  │ ✘✔✘✘ CVE-2023-37920         CRITICAL     9.8   0.6%   ·
  │ ✘✔✘✘ CVE-2018-20225         HIGH         7.8   1.8%   ·
  │ ✘✔✘✘ CVE-2024-3651          HIGH         7.5   1.4%   ·
  │ ✘✔✘✘ CVE-2024-6345          HIGH         8.8   1.9%   ·
  │ ✘✔✘✔ CVE-2025-47273         HIGH         8.8   1.6%   ·  ↳ V:UB:CVE-2025-47273
  │ ✘✘✘✔ CVE-2025-66418         HIGH         8.9   0.7%   ·  ↳ V:UB:CVE-2025-66418
  │ ✘✔✘✘ CVE-2025-66471         HIGH         8.9   0.7%   ·
  │ ✘✘✘✔ CVE-2026-21441         HIGH         8.9   2.9%   ·  ↳ V:UB:CVE-2026-21441
  │ ✘✔✘✘ CVE-2026-24049         HIGH         7.1   0.4%   ·
  │ ✘✔✘✘ CVE-2026-44431         HIGH         8.2   0.3%   ·
  │ ✘✔✘✘ CVE-2026-44432         HIGH         8.9   0.9%   ·
  │ ✘✔✘✘ CVE-2026-57585         HIGH         7.5   0.5%   ·
  │ ✘✔✘✘ CVE-2026-8643          HIGH         8.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-97687         HIGH         8.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-97689         HIGH         8.9   0.3%   ·
  │ ✘✔✘✘ CVE-2024-35195         MEDIUM       5.6   0.3%   ·
  │ ✘✔✘✔ CVE-2025-8869          MEDIUM       5.9   0.5%   ·  ↳ V:UB:CVE-2025-8869
  │ ✘✔✘✘ CVE-2026-13346         MEDIUM       6.5   0.3%   ·
  │ ✘✔✘✘ CVE-2026-25645         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2026-3219          MEDIUM       4.6   0.2%   ·
  │ ✘✔✘✘ CVE-2026-45409         MEDIUM       6.9   0.5%   ·
  │ ✘✔✘✘ CVE-2026-6357          MEDIUM       5.3   0.2%   ·
  │ ✘✔✘✘ CVE-2026-97688         MEDIUM       6.9   0.3%   ·
  │ ✘✔✘✔ CVE-2026-1703          LOW          2.0   0.4%   ·  ↳ V:UB:CVE-2026-1703
  │ ✘✘✘✔ CVE-2026-9375          ?            0.0   0.3%   ·  ↳ V:UB:CVE-2026-9375
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-pkg-resources@45.2.0-1ubuntu0.3
  │ OGTV
  │ ✘✔✘✘ CVE-2026-59890         MEDIUM       6.1   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-requests@2.22.0-2ubuntu1.1
  │ OGTV
  │ ✘✔✘✘ CVE-2024-35195         MEDIUM       5.6   0.3%   ·
  │ ✘✔✘✔ CVE-2024-47081         MEDIUM       5.3   1.0%   ·  ↳ V:UB:CVE-2024-47081
  │ ✘✔✘✔ CVE-2026-25645         MEDIUM       5.5   0.2%   ·  ↳ V:UB:CVE-2026-25645
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-setuptools@45.2.0-1ubuntu0.3
  │ OGTV
  │ ✘✔✘✘ CVE-2026-59890         MEDIUM       6.1   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-urllib3@1.25.8-2ubuntu0.4
  │ OGTV
  │ ✘✔✘✔ CVE-2025-66418         HIGH         8.9   0.7%   ·  ↳ V:UB:CVE-2025-66418
  │ ✘✔✘✘ CVE-2025-66471         HIGH         8.9   0.7%   ·
  │ ✘✔✘✔ CVE-2026-21441         HIGH         8.9   2.9%   ·  ↳ V:UB:CVE-2026-21441
  │ ✘✔✘✔ CVE-2026-44431         HIGH         8.2   0.3%   ·  ↳ V:UB:CVE-2026-44431
  │ ✘✔✘✘ CVE-2026-97687         HIGH         8.1   0.2%   ·
  │ ✘✔✘✔ CVE-2026-97689         HIGH         8.9   0.3%   ·  ↳ V:UB:CVE-2026-97689
  │ ✘✔✘✔ CVE-2025-50181         MEDIUM       6.1   0.5%   ·  ↳ V:UB:CVE-2025-50181
  │ ✘✔✘✘ CVE-2026-97688         MEDIUM       6.9   0.3%   ·
  │ ✘✘✘✔ CVE-2026-9375          ?            0.0   0.3%   ·  ↳ V:UB:CVE-2026-9375
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3.8@3.8.10-0ubuntu1~20.04.18
  │ OGTV
  │ ✔✔✘✘ CVE-2007-4559          CRITICAL     9.8  27.1%   ·  ↳ O:UBUNTU-CVE-2007-4559
  │ ✔✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.4%   ·  ↳ O:UBUNTU-CVE-2026-19445
  │ ✔✔✘✘ CVE-2026-6100          CRITICAL     9.1   0.8%   ·  ↳ O:UBUNTU-CVE-2026-6100
  │ ✔✔✘✘ CVE-2020-10735         HIGH         7.5   4.5%   ·  ↳ O:UBUNTU-CVE-2020-10735
  │ ✔✔✘✔ CVE-2025-13836         HIGH         7.5   1.6%   ·  ↳ O:UBUNTU-CVE-2025-13836,USN-7951-1 | V:UB:CVE-2025-13836
  │ ✔✔✘✘ CVE-2025-69534         HIGH         8.2   0.6%   ·  ↳ O:UBUNTU-CVE-2025-69534
  │ ✔✔✘✔ CVE-2025-8194          HIGH         7.5   0.7%   ·  ↳ O:UBUNTU-CVE-2025-8194,USN-7710-1 | V:UB:CVE-2025-8194
  │ ✔✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·  ↳ O:UBUNTU-CVE-2026-11940
  │ ✔✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·  ↳ O:UBUNTU-CVE-2026-11972
  │ ✔✔✘✔ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ O:UBUNTU-CVE-2026-15308,USN-8744-1 | V:UB:CVE-2026-15308
  │ ✔✔✘✘ CVE-2026-19553         HIGH         7.6   0.4%   ·  ↳ O:UBUNTU-CVE-2026-19553
  │ ✔✔✘✔ CVE-2026-3644          HIGH         7.5   0.5%   ·  ↳ O:UBUNTU-CVE-2026-3644,USN-8744-1 | V:UB:CVE-2026-3644
  │ ✔✔✘✔ CVE-2026-4224          HIGH         7.5   0.7%   ·  ↳ O:UBUNTU-CVE-2026-4224,USN-8744-1 | V:UB:CVE-2026-4224
  │ ✔✔✘✘ CVE-2026-4519          HIGH         7.1   0.4%   ·  ↳ O:UBUNTU-CVE-2026-4519
  │ ✔✔✘✘ CVE-2026-4786          HIGH         7.1   0.5%   ·  ↳ O:UBUNTU-CVE-2026-4786
  │ ✔✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57178
  │ ✔✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·  ↳ O:UBUNTU-CVE-2026-7210
  │ ✔✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-82049
  │ ✔✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·  ↳ O:UBUNTU-CVE-2026-84366
  │ ✔✔✘✘ CVE-2026-9669          HIGH         8.2   0.4%   ·  ↳ O:UBUNTU-CVE-2026-9669
  │ ✔✔✘✘ CVE-2021-23336         MEDIUM       5.9  40.7%   ·  ↳ O:UBUNTU-CVE-2021-23336
  │ ✔✔✘✔ CVE-2025-11468         MEDIUM       5.7   0.6%   ·  ↳ O:UBUNTU-CVE-2025-11468 | V:UB:CVE-2025-11468
  │ ✔✔✘✔ CVE-2025-12084         MEDIUM       6.3   0.8%   ·  ↳ O:UBUNTU-CVE-2025-12084 | V:UB:CVE-2025-12084
  │ ✔✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.6%   ·  ↳ O:UBUNTU-CVE-2025-12781
  │ ✔✔✘✔ CVE-2025-13837         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-13837 | V:UB:CVE-2025-13837
  │ ✔✔✘✔ CVE-2025-15282         MEDIUM       6.0   0.5%   ·  ↳ O:UBUNTU-CVE-2025-15282 | V:UB:CVE-2025-15282
  │ ✔✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·  ↳ O:UBUNTU-CVE-2025-15366
  │ ✔✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·  ↳ O:UBUNTU-CVE-2025-15367
  │ ✔✔✘✔ CVE-2025-4516          MEDIUM       5.9   0.2%   ·  ↳ O:UBUNTU-CVE-2025-4516,USN-7570-1 | V:UB:CVE-2025-4516
  │ ✔✔✘✔ CVE-2025-6069          MEDIUM       4.3   0.6%   ·  ↳ O:UBUNTU-CVE-2025-6069,USN-7710-1 | V:UB:CVE-2025-6069
  │ ✔✔✘✔ CVE-2025-6075          MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2025-6075,USN-7886-1 | V:UB:CVE-2025-6075
  │ ✔✔✘✔ CVE-2025-8291          MEDIUM       4.3   0.5%   ·  ↳ O:UBUNTU-CVE-2025-8291,USN-7886-1 | V:UB:CVE-2025-8291
  │ ✔✔✘✔ CVE-2026-0672          MEDIUM       6.0   0.5%   ·  ↳ O:UBUNTU-CVE-2026-0672 | V:UB:CVE-2026-0672
  │ ✔✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-0864
  │ ✔✔✘✔ CVE-2026-0865          MEDIUM       5.9   0.5%   ·  ↳ O:UBUNTU-CVE-2026-0865 | V:UB:CVE-2026-0865
  │ ✔✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.2%   ·  ↳ O:UBUNTU-CVE-2026-12345
  │ ✔✔✘✘ CVE-2026-1299          MEDIUM       6.0   0.6%   ·  ↳ O:UBUNTU-CVE-2026-1299
  │ ✔✔✘✘ CVE-2026-1502          MEDIUM       5.7   0.6%   ·  ↳ O:UBUNTU-CVE-2026-1502
  │ ✔✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·  ↳ O:UBUNTU-CVE-2026-15806
  │ ✔✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·  ↳ O:UBUNTU-CVE-2026-17084
  │ ✔✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·  ↳ O:UBUNTU-CVE-2026-19672
  │ ✔✔✘✔ CVE-2026-2297          MEDIUM       5.7   0.2%   ·  ↳ O:UBUNTU-CVE-2026-2297 | V:UB:CVE-2026-2297
  │ ✔✔✘✘ CVE-2026-3276          MEDIUM       6.3   0.5%   ·  ↳ O:UBUNTU-CVE-2026-3276
  │ ✔✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-3446
  │ ✔✘✘✘ CVE-2026-4360          MEDIUM       5.3   0.5%   ·  ↳ O:USN-8744-1
  │ ✔✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57175
  │ ✔✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57176
  │ ✔✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·  ↳ O:UBUNTU-CVE-2026-57177
  │ ✔✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57179
  │ ✔✔✘✔ CVE-2026-6019          MEDIUM       6.1   0.2%   ·  ↳ O:UBUNTU-CVE-2026-6019,USN-8744-1 | V:UB:CVE-2026-6019
  │ ✔✔✘✘ CVE-2026-8328          MEDIUM       5.9   0.5%   ·  ↳ O:UBUNTU-CVE-2026-8328
  │ ✔✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.5%   ·  ↳ O:UBUNTU-CVE-2026-87910
  │ ✔✔✘✘ CVE-2025-13462         LOW          3.3   0.2%   ·  ↳ O:UBUNTU-CVE-2025-13462
  │ ✔✔✘✔ CVE-2025-1795          LOW          2.3   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1795,USN-7570-1 | V:UB:CVE-2025-1795
  │ ✔✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·  ↳ O:UBUNTU-CVE-2026-15310
  │ ✔✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·  ↳ O:UBUNTU-CVE-2026-18503
  │ ✔✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·  ↳ O:UBUNTU-CVE-2026-6879
  │ ✔✘✘✘ USN-8018-1             ?             -       -   ·
  │ ✔✘✘✘ USN-8018-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3.8-dev@3.8.10-0ubuntu1~20.04.18
  │ OGTV
  │ ✘✔✘✘ CVE-2007-4559          CRITICAL     9.8  27.1%   ·
  │ ✘✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.4%   ·
  │ ✘✔✘✘ CVE-2026-6100          CRITICAL     9.1   0.8%   ·
  │ ✘✔✘✘ CVE-2020-10735         HIGH         7.5   4.5%   ·
  │ ✘✔✘✘ CVE-2025-13836         HIGH         7.5   1.6%   ·
  │ ✘✔✘✘ CVE-2025-69534         HIGH         8.2   0.6%   ·
  │ ✘✔✘✘ CVE-2025-8194          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·
  │ ✘✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·
  │ ✘✔✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·
  │ ✘✔✘✘ CVE-2026-19553         HIGH         7.6   0.4%   ·
  │ ✘✔✘✘ CVE-2026-3644          HIGH         7.5   0.5%   ·
  │ ✘✔✘✘ CVE-2026-4224          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-4519          HIGH         7.1   0.4%   ·
  │ ✘✔✘✘ CVE-2026-4786          HIGH         7.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·
  │ ✘✔✘✘ CVE-2026-9669          HIGH         8.2   0.4%   ·
  │ ✘✔✘✘ CVE-2021-23336         MEDIUM       5.9  40.7%   ·
  │ ✘✔✘✘ CVE-2025-11468         MEDIUM       5.7   0.6%   ·
  │ ✘✔✘✘ CVE-2025-12084         MEDIUM       6.3   0.8%   ·
  │ ✘✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.6%   ·
  │ ✘✔✘✘ CVE-2025-13837         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-15282         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2025-4516          MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✘ CVE-2025-6069          MEDIUM       4.3   0.6%   ·
  │ ✘✔✘✘ CVE-2025-6075          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2025-8291          MEDIUM       4.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-0672          MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-0865          MEDIUM       5.9   0.5%   ·
  │ ✘✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-1299          MEDIUM       6.0   0.6%   ·
  │ ✘✔✘✘ CVE-2026-1502          MEDIUM       5.7   0.6%   ·
  │ ✘✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·
  │ ✘✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✔ CVE-2026-2297          MEDIUM       5.7   0.2%   ·  ↳ V:UB:CVE-2026-2297
  │ ✘✔✘✘ CVE-2026-3276          MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6019          MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-8328          MEDIUM       5.9   0.5%   ·
  │ ✘✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.5%   ·
  │ ✘✔✘✘ CVE-2025-13462         LOW          3.3   0.2%   ·
  │ ✘✔✘✘ CVE-2025-1795          LOW          2.3   0.6%   ·
  │ ✘✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3.8-minimal@3.8.10-0ubuntu1~20.04.18
  │ OGTV
  │ ✘✔✘✘ CVE-2007-4559          CRITICAL     9.8  27.1%   ·
  │ ✘✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.4%   ·
  │ ✘✔✘✘ CVE-2026-6100          CRITICAL     9.1   0.8%   ·
  │ ✘✔✘✘ CVE-2020-10735         HIGH         7.5   4.5%   ·
  │ ✘✔✘✘ CVE-2025-13836         HIGH         7.5   1.6%   ·
  │ ✘✔✘✘ CVE-2025-69534         HIGH         8.2   0.6%   ·
  │ ✘✔✘✘ CVE-2025-8194          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·
  │ ✘✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·
  │ ✘✔✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·
  │ ✘✔✘✘ CVE-2026-19553         HIGH         7.6   0.4%   ·
  │ ✘✔✘✘ CVE-2026-3644          HIGH         7.5   0.5%   ·
  │ ✘✔✘✘ CVE-2026-4224          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-4519          HIGH         7.1   0.4%   ·
  │ ✘✔✘✘ CVE-2026-4786          HIGH         7.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·
  │ ✘✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·
  │ ✘✔✘✘ CVE-2026-9669          HIGH         8.2   0.4%   ·
  │ ✘✔✘✘ CVE-2021-23336         MEDIUM       5.9  40.7%   ·
  │ ✘✔✘✘ CVE-2025-11468         MEDIUM       5.7   0.6%   ·
  │ ✘✔✘✘ CVE-2025-12084         MEDIUM       6.3   0.8%   ·
  │ ✘✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.6%   ·
  │ ✘✔✘✘ CVE-2025-13837         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✘ CVE-2025-15282         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·
  │ ✘✔✘✔ CVE-2025-4516          MEDIUM       5.9   0.2%   ·  ↳ V:UB:CVE-2025-4516
  │ ✘✔✘✘ CVE-2025-6069          MEDIUM       4.3   0.6%   ·
  │ ✘✔✘✘ CVE-2025-6075          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2025-8291          MEDIUM       4.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-0672          MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·
  │ ✘✔✘✘ CVE-2026-0865          MEDIUM       5.9   0.5%   ·
  │ ✘✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.2%   ·
  │ ✘✔✘✘ CVE-2026-1299          MEDIUM       6.0   0.6%   ·
  │ ✘✔✘✘ CVE-2026-1502          MEDIUM       5.7   0.6%   ·
  │ ✘✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·
  │ ✘✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·
  │ ✘✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✔ CVE-2026-2297          MEDIUM       5.7   0.2%   ·  ↳ V:UB:CVE-2026-2297
  │ ✘✔✘✘ CVE-2026-3276          MEDIUM       6.3   0.5%   ·
  │ ✘✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·
  │ ✘✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·
  │ ✘✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·
  │ ✘✔✘✘ CVE-2026-6019          MEDIUM       6.1   0.2%   ·
  │ ✘✔✘✘ CVE-2026-8328          MEDIUM       5.9   0.5%   ·
  │ ✘✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.5%   ·
  │ ✘✔✘✘ CVE-2025-13462         LOW          3.3   0.2%   ·
  │ ✘✔✘✔ CVE-2025-1795          LOW          2.3   0.6%   ·  ↳ V:UB:CVE-2025-1795
  │ ✘✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·
  │ ✘✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·
  │ ✘✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/sed@4.7-1
  │ OGTV
  │ ✔✔✘✔ CVE-2026-5958          LOW          2.1   0.1%   ·  ↳ O:UBUNTU-CVE-2026-5958,USN-8229-2 | V:UB:CVE-2026-5958
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/systemd@245.4-4ubuntu3.24
  │ OGTV
  │ ✔✔✘✔ CVE-2023-26604         HIGH         7.8   1.1%   ·  ↳ O:UBUNTU-CVE-2023-26604 | V:UB:CVE-2023-26604
  │ ✔✔✘✘ CVE-2020-13776         MEDIUM       6.7   0.5%   ·  ↳ O:UBUNTU-CVE-2020-13776
  │ ✔✔✘✔ CVE-2023-7008          MEDIUM       5.9   0.8%   ·  ↳ O:UBUNTU-CVE-2023-7008 | V:UB:CVE-2023-7008
  │ ✔✔✘✘ CVE-2025-4598          MEDIUM       4.7   1.2%   ·  ↳ O:UBUNTU-CVE-2025-4598,USN-7559-1
  │ ✔✔✘✔ CVE-2026-29111         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2026-29111 | V:UB:CVE-2026-29111
  │ ✔✔✘✔ CVE-2026-40225         MEDIUM       6.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-40225 | V:UB:CVE-2026-40225
  │ ✔✔✘✘ CVE-2026-40226         MEDIUM       6.4   0.1%   ·  ↳ O:UBUNTU-CVE-2026-40226
  │ ✔✔✘✔ CVE-2026-40228         LOW          3.3   0.1%   ·  ↳ O:UBUNTU-CVE-2026-40228 | V:UB:CVE-2026-40228
  │ ✔✘✘✘ USN-8119-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/systemd-sysv@245.4-4ubuntu3.24
  │ OGTV
  │ ✘✔✘✔ CVE-2023-26604         HIGH         7.8   1.1%   ·  ↳ V:UB:CVE-2023-26604
  │ ✘✔✘✘ CVE-2020-13776         MEDIUM       6.7   0.5%   ·
  │ ✘✔✘✔ CVE-2023-7008          MEDIUM       5.9   0.8%   ·  ↳ V:UB:CVE-2023-7008
  │ ✘✔✘✘ CVE-2025-4598          MEDIUM       4.7   1.2%   ·
  │ ✘✔✘✘ CVE-2026-29111         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✔ CVE-2026-40225         MEDIUM       6.4   0.2%   ·  ↳ V:UB:CVE-2026-40225
  │ ✘✔✘✘ CVE-2026-40226         MEDIUM       6.4   0.1%   ·
  │ ✘✔✘✔ CVE-2026-40228         LOW          3.3   0.1%   ·  ↳ V:UB:CVE-2026-40228
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/systemd-timesyncd@245.4-4ubuntu3.24
  │ OGTV
  │ ✘✔✘✔ CVE-2023-26604         HIGH         7.8   1.1%   ·  ↳ V:UB:CVE-2023-26604
  │ ✘✔✘✘ CVE-2020-13776         MEDIUM       6.7   0.5%   ·
  │ ✘✔✘✔ CVE-2023-7008          MEDIUM       5.9   0.8%   ·  ↳ V:UB:CVE-2023-7008
  │ ✘✔✘✘ CVE-2025-4598          MEDIUM       4.7   1.2%   ·
  │ ✘✔✘✘ CVE-2026-29111         MEDIUM       5.5   0.2%   ·
  │ ✘✔✘✔ CVE-2026-40225         MEDIUM       6.4   0.2%   ·  ↳ V:UB:CVE-2026-40225
  │ ✘✔✘✘ CVE-2026-40226         MEDIUM       6.4   0.1%   ·
  │ ✘✔✘✔ CVE-2026-40228         LOW          3.3   0.1%   ·  ↳ V:UB:CVE-2026-40228
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/tar@1.30%2Bdfsg-7ubuntu0.20.04.4
  │ OGTV
  │ ✔✔✘✔ CVE-2025-45582         MEDIUM       4.1   0.5%   ·  ↳ O:UBUNTU-CVE-2025-45582 | V:UB:CVE-2025-45582
  │ ✔✔✘✔ CVE-2026-18477         MEDIUM       4.4   0.1%   ·  ↳ O:UBUNTU-CVE-2026-18477 | V:UB:CVE-2026-18477
  │ ✔✔✘✔ CVE-2026-18508         MEDIUM       4.4   0.1%   ·  ↳ O:UBUNTU-CVE-2026-18508 | V:UB:CVE-2026-18508
  │ ✔✔✘✔ CVE-2026-5704          MEDIUM       5.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-5704,USN-8477-2,USN-8477-3 | V:UB:CVE-2026-5704
  │ ✔✘✘✘ USN-8477-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/util-linux@2.34-0.1ubuntu9.6
  │ OGTV
  │ ✔✔✘✘ CVE-2026-53613         HIGH         7.0   0.1%   ·  ↳ O:UBUNTU-CVE-2026-53613
  │ ✔✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-53615
  │ ✔✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ O:UBUNTU-CVE-2026-76642
  │ ✔✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ O:UBUNTU-CVE-2026-78408
  │ ✔✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-78409
  │ ✔✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-78410
  │ ✔✔✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·  ↳ O:UBUNTU-CVE-2025-14104
  │ ✔✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-13595
  │ ✔✔✘✔ CVE-2026-27456         MEDIUM       4.7   0.1%   ·  ↳ O:UBUNTU-CVE-2026-27456 | V:UB:CVE-2026-27456
  │ ✔✘✘✘ USN-8091-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/xz-utils@5.2.4-1ubuntu1.1
  │ OGTV
  │ ✔✔✘✔ CVE-2026-34743         MEDIUM       6.3   0.5%   ·  ↳ O:UBUNTU-CVE-2026-34743,USN-8362-1 | V:UB:CVE-2026-34743
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/zlib1g@1%3A1.2.11.dfsg-2ubuntu1.5
  │ OGTV
  │ ✘✔✘✔ CVE-2026-85091         HIGH         8.3   0.4%   ·  ↳ V:UB:CVE-2026-85091
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/zlib1g-dev@1%3A1.2.11.dfsg-2ubuntu1.5
  │ OGTV
  │ ✘✔✘✔ CVE-2026-85091         HIGH         8.3   0.4%   ·  ↳ V:UB:CVE-2026-85091
  └────────────────────────────────────────────────────────────────────────────────────────────────────

  ━━ Go ━━
  ┌─ pkg:golang/github.com/aws/aws-sdk-go-v2/service/sso@v1.22.4
  │ OGTV
  │ ✘✘✘✔ WS-2026-0065           MEDIUM       6.3      -   ·  ↳ V:MEND:WS-2026-0065
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/aws/aws-sdk-go-v2/service/ssooidc@v1.26.4
  │ OGTV
  │ ✘✘✘✔ WS-2026-0065           MEDIUM       6.3      -   ·  ↳ V:MEND:WS-2026-0065
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/aws/aws-sdk-go-v2/service/sts@v1.30.3
  │ OGTV
  │ ✘✘✘✔ WS-2026-0065           MEDIUM       6.3      -   ·  ↳ V:MEND:WS-2026-0065
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/containerd/containerd/v2@v2.0.4
  │ OGTV
  │ ✔✔✔✔ CVE-2026-53488         CRITICAL     9.4   0.2%   ·  ↳ O:GHSA-xhf5-7wjv-pqxp,GO-2026-5758 | V:MEND:CVE-2026-53488
  │ ✔✔✔✔ CVE-2024-25621         HIGH         7.8   0.2%   ·  ↳ O:GHSA-pwhc-rpq9-4c8w,GO-2025-4100 | V:GHSA-PWHC-RPQ9-4C8W
  │ ✔✔✔✔ CVE-2025-47291         HIGH         7.5   0.3%   ·  ↳ O:GHSA-cxfp-7pvr-95ff,GO-2025-3701 | V:MEND:CVE-2025-47291
  │ ✔✔✔✔ CVE-2026-46680         HIGH         7.8   0.2%   ·  ↳ O:GHSA-fqw6-gf59-qr4w,GO-2026-5378 | V:MEND:CVE-2026-46680
  │ ✔✔✔✔ CVE-2025-64329         MEDIUM       6.9   0.2%   ·  ↳ O:GHSA-m6hq-p25p-ffr2,GO-2025-4108 | V:MEND:CVE-2025-64329
  │ ✔✔✔✔ CVE-2026-47262         MEDIUM       5.5   0.3%   ·  ↳ O:GHSA-jpcc-p29g-p8mq,GO-2026-5475 | V:MEND:CVE-2026-47262
  │ ✔✔✔✔ CVE-2026-53493         MEDIUM       6.9   0.4%   ·  ↳ O:GHSA-pg57-6jwg-q645,GO-2026-6597 | V:MEND:CVE-2026-53493
  │ ✔✔✔✔ CVE-2026-53495         MEDIUM       6.8   0.2%   ·  ↳ O:GHSA-7jxh-36q5-gcqv,GO-2026-6444 | V:GHSA-7JXH-36Q5-GCQV
  │ ✔✔✔✔ CVE-2026-95838         MEDIUM       4.6   0.2%   ·  ↳ O:GHSA-rp3h-jf77-q9p4 | V:MEND:CVE-2026-95838
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/buildx@v0.23.0
  │ OGTV
  │ ✘✘✘✔ CVE-2026-103433        MEDIUM       6.9   0.3%   ·  ↳ V:MEND:CVE-2026-103433
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/cli@v28.0.4%2Bincompatible
  │ OGTV
  │ ✔✔✔✔ CVE-2025-15558         HIGH         8.0   0.5%   ·  ↳ O:GHSA-p436-gjf2-799p,GO-2026-4610 | V:GHSA-P436-GJF2-799P
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/cli@v28.1.0%2Bincompatible
  │ OGTV
  │ ✔✔✔✔ CVE-2025-15558         HIGH         8.0   0.5%   ·  ↳ O:GHSA-p436-gjf2-799p,GO-2026-4610 | V:GHSA-P436-GJF2-799P
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/compose/v2@v2.35.1
  │ OGTV
  │ ✔✔✘✔ CVE-2025-15558         HIGH         8.0   0.5%   ·  ↳ O:GO-2026-4610 | V:OSV:GO-2026-4610
  │ ✔✔✔✔ CVE-2025-62725         HIGH         8.9  13.7%   ·  ↳ O:GHSA-gv8h-7v7w-r22q,GO-2025-4077 | V:MEND:CVE-2025-62725
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/distribution@v2.8.3%2Bincompatible
  │ OGTV
  │ ✔✔✔✔ CVE-2026-85747         MEDIUM       6.8   0.2%   ·  ↳ O:GHSA-685w-q87j-wqw3 | V:OSV:GHSA-685W-Q87J-WQW3
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/docker@v28.0.4%2Bincompatible
  │ OGTV
  │ ✔✔✔✔ CVE-2026-33997         HIGH         8.4   0.5%   ·  ↳ O:GHSA-pxq6-2prw-chj9,GO-2026-4883 | V:OSV:GO-2026-4883
  │ ✔✔✘✔ CVE-2026-34040         HIGH         8.8   0.2%   ·  ↳ O:GO-2026-4887 | V:OSV:GO-2026-4887
  │ ✔✔✔✔ CVE-2026-41567         HIGH         7.5   0.2%   ·  ↳ O:GHSA-x86f-5xw2-fm2r,GO-2026-5746 | V:OSV:GO-2026-5746
  │ ✔✔✔✔ CVE-2026-42306         HIGH         7.2   0.1%   ·  ↳ O:GHSA-rg2x-37c3-w2rh,GO-2026-5617 | V:OSV:GO-2026-5617
  │ ✔✔✔✔ CVE-2026-41568         MEDIUM       6.1   0.1%   ·  ↳ O:GHSA-vp62-88p7-qqf5,GO-2026-5668 | V:OSV:GO-2026-5668
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/docker@v28.1.0%2Bincompatible
  │ OGTV
  │ ✔✔✔✔ CVE-2026-33997         HIGH         8.4   0.5%   ·  ↳ O:GHSA-pxq6-2prw-chj9,GO-2026-4883 | V:OSV:GO-2026-4883
  │ ✔✔✘✔ CVE-2026-34040         HIGH         8.8   0.2%   ·  ↳ O:GO-2026-4887 | V:OSV:GO-2026-4887
  │ ✔✔✔✔ CVE-2026-41567         HIGH         7.5   0.2%   ·  ↳ O:GHSA-x86f-5xw2-fm2r,GO-2026-5746 | V:OSV:GO-2026-5746
  │ ✔✔✔✔ CVE-2026-42306         HIGH         7.2   0.1%   ·  ↳ O:GHSA-rg2x-37c3-w2rh,GO-2026-5617 | V:OSV:GO-2026-5617
  │ ✔✔✔✔ CVE-2026-41568         MEDIUM       6.1   0.1%   ·  ↳ O:GHSA-vp62-88p7-qqf5,GO-2026-5668 | V:OSV:GO-2026-5668
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/go-viper/mapstructure/v2@v2.0.0
  │ OGTV
  │ ✔✔✔✔ CVE-2025-11065         MEDIUM       5.3   0.4%   ·  ↳ O:GHSA-2464-8j7c-4cjm,GO-2025-3900 | V:SNYK:GOLANG-GITHUBCOMGOVIPERMAPSTRUCTUREV2-12177854
  │ ✘✘✘✔ CVE-2025-52893         MEDIUM       4.5   0.3%   ·  ↳ V:SNYK:GOLANG-GITHUBCOMGOVIPERMAPSTRUCTUREV2-10558294
  │ ✔✔✔✔ GHSA-FV92-FJC5-JJ9H    MEDIUM       5.3      -   ·  ↳ O:GO-2025-3787 | V:GO-2025-3787,OSV:GO-2025-3787
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/gorilla/websocket@v1.5.0
  │ OGTV
  │ ✔✔✔✔ GHSA-W67G-5RQW-F597    MEDIUM       6.9      -   ·  ↳ O:GO-2026-6278 | V:GO-2026-6278,OSV:GO-2026-6278
  │ ✘✘✘✔ GOLANG-GITHUBCOMGORILLAWEBSOCKET-19256866 MEDIUM       6.9      -   ·  ↳ V:SNYK:GOLANG-GITHUBCOMGORILLAWEBSOCKET-19256866
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/in-toto/in-toto-golang@v0.5.0
  │ OGTV
  │ ✔✔✔✔ GHSA-PMWQ-PJRM-6P5R    MEDIUM       4.1      -   ·  ↳ O:GO-2026-5547 | V:GO-2026-5547,OSV:GO-2026-5547
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/klauspost/compress@v1.18.0
  │ OGTV
  │ ✔✔✘✔ CVE-2026-63209         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-5841 | G:GO-2026-5841 | V:MEND:CVE-2026-63209
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/moby/buildkit@v0.21.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-33747         CRITICAL     9.8   0.6%   ·  ↳ O:GHSA-4c29-8rgm-jvjj,GO-2026-4858 | V:GHSA-4C29-8RGM-JVJJ
  │ ✘✘✘✔ CVE-2026-15788         HIGH         7.5   0.4%   ·  ↳ V:MEND:CVE-2026-15788
  │ ✘✘✘✔ CVE-2026-15789         HIGH         7.5   0.3%   ·  ↳ V:MEND:CVE-2026-15789
  │ ✘✘✘✔ CVE-2026-15791         HIGH         7.5   0.2%   ·  ↳ V:MEND:CVE-2026-15791
  │ ✘✘✘✔ CVE-2026-15792         HIGH         7.5   0.2%   ·  ↳ V:MEND:CVE-2026-15792
  │ ✔✔✔✔ CVE-2026-33748         HIGH         8.2   0.5%   ·  ↳ O:GHSA-4vrq-3vrq-g6gg,GO-2026-4859 | V:GHSA-4VRQ-3VRQ-G6GG
  │ ✘✘✘✔ CVE-2026-75593         HIGH         7.2   0.5%   ·  ↳ V:MEND:CVE-2026-75593
  │ ✘✘✘✔ CVE-2026-93318         HIGH         7.5   0.2%   ·  ↳ V:MEND:CVE-2026-93318
  │ ✔✔✔✔ CVE-2026-61711         MEDIUM       5.3   0.4%   ·  ↳ O:GHSA-7236-3392-c5c6,GO-2026-6255 | V:MEND:CVE-2026-61711
  │ ✘✘✘✔ CVE-2026-93320         MEDIUM       6.0   0.1%   ·  ↳ V:MEND:CVE-2026-93320
  │ ✔✔✔✔ CVE-2026-61712         LOW          2.3   0.4%   ·  ↳ O:GHSA-72x6-4j93-7w86,GO-2026-6256 | V:MEND:CVE-2026-61712
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/moby/go-archive@v0.1.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-17106         HIGH         7.1   0.4%   ·  ↳ O:GHSA-hfg8-hc9c-6c3h,GO-2026-6253 | V:MEND:CVE-2026-17106
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/moby/spdystream@v0.4.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-35469         HIGH         8.7   0.8%   ·  ↳ O:GHSA-pc3f-x583-g7j2,GO-2026-4958 | V:MEND:CVE-2026-35469
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/moby/sys/user@v0.4.0
  │ OGTV
  │ ✘✘✘✔ CVE-2026-47262         MEDIUM       5.5   0.3%   ·  ↳ V:GHSA-MJCV-P78Q-W5FW
  │ ✔✔✔✔ CVE-2026-61801         MEDIUM       5.5   0.1%   ·  ↳ O:GHSA-mjcv-p78q-w5fw | V:MEND:CVE-2026-61801
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp@v1.31.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-39882         MEDIUM       5.3   0.2%   ·  ↳ O:GHSA-w8rr-5gcm-pp58,GO-2026-4985 | V:GHSA-W8RR-5GCM-PP58
  │ ✔✘✘✔ CVE-2026-44967         MEDIUM       5.3   0.3%   ·  ↳ O:GHSA-w8rr-5gcm-pp58 | V:OSV:GHSA-W8RR-5GCM-PP58
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace@v1.31.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-81870         LOW          2.0   0.2%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:SNYK:GOLANG-GOOPENTELEMETRYIOOTELEXPORTERSOTLPOTLPTRACE-19883902
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc@v1.31.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-81870         LOW          2.0   0.2%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:SNYK:GOLANG-GOOPENTELEMETRYIOOTELEXPORTERSOTLPOTLPTRACEOTLPTRACEGRPC-19883903
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp@v1.31.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-39882         MEDIUM       5.3   0.2%   ·  ↳ O:GHSA-w8rr-5gcm-pp58,GO-2026-4985 | V:GHSA-W8RR-5GCM-PP58
  │ ✔✘✘✔ CVE-2026-44967         MEDIUM       5.3   0.3%   ·  ↳ O:GHSA-w8rr-5gcm-pp58 | V:OSV:GHSA-W8RR-5GCM-PP58
  │ ✔✔✔✔ CVE-2026-81870         LOW          2.0   0.2%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:SNYK:GOLANG-GOOPENTELEMETRYIOOTELEXPORTERSOTLPOTLPTRACEOTLPTRACEHTTP-19883904
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/sdk@v1.31.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-24051         HIGH         7.0   0.2%   ·  ↳ O:GHSA-9h8m-3fm2-qjrq,GO-2026-4394 | V:GHSA-HFVC-G4FC-PQHX
  │ ✔✔✔✔ CVE-2026-39883         HIGH         8.8   0.2%   ·  ↳ O:GHSA-hfvc-g4fc-pqhx,GO-2026-5426 | V:MEND:CVE-2026-39883
  │ ✔✔✔✔ CVE-2026-81869         MEDIUM       5.1   0.2%   ·  ↳ O:GHSA-p9f8-wvj8-2fg8,GO-2026-6616 | V:MEND:CVE-2026-81869
  │ ✔✔✔✔ CVE-2026-81870         LOW          2.0   0.2%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:MEND:CVE-2026-81870
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/sdk@v1.34.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-24051         HIGH         7.0   0.2%   ·  ↳ O:GHSA-9h8m-3fm2-qjrq,GO-2026-4394 | V:GHSA-HFVC-G4FC-PQHX
  │ ✔✔✔✔ CVE-2026-39883         HIGH         8.8   0.2%   ·  ↳ O:GHSA-hfvc-g4fc-pqhx,GO-2026-5426 | V:MEND:CVE-2026-39883
  │ ✔✔✔✔ CVE-2026-81870         LOW          2.0   0.2%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:MEND:CVE-2026-81870
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/crypto@v0.37.0
  │ OGTV
  │ ✘✘✘✔ CVE-2024-45337         CRITICAL     9.1   3.2%   ·  ↳ V:MEND:CVE-2026-46595
  │ ✔✔✔✔ CVE-2026-39830         CRITICAL     9.1   0.6%   ·  ↳ O:GHSA-vgwf-h737-ff37,GO-2026-5017 | V:MEND:CVE-2026-39830
  │ ✔✔✔✔ CVE-2026-39831         CRITICAL     9.1   0.5%   ·  ↳ O:GHSA-89gr-r52h-f8rx,GO-2026-5019 | V:MEND:CVE-2026-39831
  │ ✔✔✔✔ CVE-2026-39832         CRITICAL     9.1   0.7%   ·  ↳ O:GHSA-f5wc-c3c7-36mc,GO-2026-5006 | V:MEND:CVE-2026-39832
  │ ✔✔✔✔ CVE-2026-39833         CRITICAL     9.1   0.5%   ·  ↳ O:GHSA-jppx-rxg9-jmrx,GO-2026-5005 | V:MEND:CVE-2026-39833
  │ ✔✔✔✔ CVE-2026-39834         CRITICAL     9.1   0.6%   ·  ↳ O:GHSA-rm3j-f69w-wqmq,GO-2026-5020 | V:MEND:CVE-2026-39834
  │ ✔✔✔✔ CVE-2026-42508         CRITICAL     9.1   0.7%   ·  ↳ O:GHSA-5cgq-3rg8-m6cv,GO-2026-5021 | V:MEND:CVE-2026-42508
  │ ✔✔✔✔ CVE-2026-46595         CRITICAL    10.0   0.5%   ·  ↳ O:GHSA-x527-x647-q7gg,GO-2026-5023 | V:MEND:CVE-2026-46595
  │ ✔✔✔✔ CVE-2025-47913         HIGH         7.5   0.7%   ·  ↳ O:GO-2025-4116 | V:OSV:GO-2025-4116
  │ ✔✔✔✔ CVE-2026-39828         HIGH         8.8   0.5%   ·  ↳ O:GHSA-45gg-vh54-h5m9,GO-2026-5014 | V:MEND:CVE-2026-39828
  │ ✔✔✔✔ CVE-2026-39829         HIGH         7.5   0.6%   ·  ↳ O:GHSA-w879-237q-wc7r,GO-2026-5018 | V:MEND:CVE-2026-39829
  │ ✔✔✔✔ CVE-2026-39835         HIGH         7.5   0.5%   ·  ↳ O:GHSA-78mq-xcr3-xm33,GO-2026-5015 | V:MEND:CVE-2026-39835
  │ ✔✔✔✔ CVE-2026-46597         HIGH         7.5   0.6%   ·  ↳ O:GHSA-q4h4-gmj2-qvw2,GO-2026-5013 | V:MEND:CVE-2026-46597
  │ ✔✔✔✔ CVE-2026-56854         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6303 | V:MEND:CVE-2026-56854
  │ ✔✔✔✔ CVE-2026-56855         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6355 | V:MEND:CVE-2026-56855
  │ ✔✔✔✔ CVE-2026-78662         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6354 | V:MEND:CVE-2026-78662
  │ ✔✔✔✔ CVE-2025-47914         MEDIUM       5.3   0.5%   ·  ↳ O:GHSA-f6x5-jh6r-wrfv,GO-2025-4135 | V:MEND:CVE-2025-47914
  │ ✔✔✔✔ CVE-2025-58181         MEDIUM       5.3   0.6%   ·  ↳ O:GHSA-j5w8-q4qc-rx2x,GO-2025-4134 | V:MEND:CVE-2025-58181
  │ ✔✔✔✔ CVE-2026-39827         MEDIUM       6.5   0.3%   ·  ↳ O:GHSA-qpw4-5x99-6vjp,GO-2026-5016 | V:MEND:CVE-2026-39827
  │ ✔✔✔✔ CVE-2026-46598         MEDIUM       5.3   0.5%   ·  ↳ O:GHSA-9m57-25v3-79x9,GO-2026-5033 | V:MEND:CVE-2026-46598
  │ ✔✔✔✔ GO-2026-5932           ?            0.0      -   ·  ↳ V:OSV:GO-2026-5932
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/net@v0.39.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-39821         CRITICAL     9.6   0.7%   ·  ↳ O:GO-2026-5026 | V:MEND:CVE-2026-39821
  │ ✔✔✔✔ CVE-2026-78663         CRITICAL     9.1   0.6%   ·  ↳ O:GO-2026-6612 | V:MEND:CVE-2026-78663
  │ ✔✔✔✔ CVE-2026-33814         HIGH         7.5   0.8%   ·  ↳ O:GO-2026-4918 | V:MEND:CVE-2026-33814
  │ ✔✔✔✔ CVE-2026-46600         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-5942 | V:MEND:CVE-2026-46600
  │ ✔✔✔✔ CVE-2026-78659         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6603 | V:MEND:CVE-2026-78659
  │ ✔✔✔✔ CVE-2026-78660         HIGH         7.5   0.3%   ·  ↳ O:GO-2026-6610 | V:MEND:CVE-2026-78660
  │ ✔✔✔✔ CVE-2026-78669         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6611 | V:MEND:CVE-2026-78669
  │ ✔✔✔✔ CVE-2026-97032         HIGH         7.5   0.2%   ·  ↳ O:GO-2026-6617 | V:MEND:CVE-2026-97032
  │ ✔✔✔✔ CVE-2025-47911         MEDIUM       5.3   0.6%   ·  ↳ O:GO-2026-4440 | V:OSV:GO-2026-4440
  │ ✔✔✔✔ CVE-2025-58190         MEDIUM       5.3   0.5%   ·  ↳ O:GO-2026-4441 | V:OSV:GO-2026-4441
  │ ✔✔✔✔ CVE-2026-25680         MEDIUM       6.5   0.5%   ·  ↳ O:GHSA-5cv4-jp36-h3mw,GO-2026-5028 | V:GHSA-5CV4-JP36-H3MW
  │ ✔✔✔✔ CVE-2026-25681         MEDIUM       6.1   0.2%   ·  ↳ O:GO-2026-5029 | V:MEND:CVE-2026-25681
  │ ✔✔✔✔ CVE-2026-27136         MEDIUM       6.1   0.2%   ·  ↳ O:GO-2026-5030 | V:MEND:CVE-2026-27136
  │ ✔✔✔✔ CVE-2026-42502         MEDIUM       6.1   0.2%   ·  ↳ O:GO-2026-5027 | V:MEND:CVE-2026-42502
  │ ✔✔✔✔ CVE-2026-42506         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-5025 | V:MEND:CVE-2026-42506
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/oauth2@v0.23.0
  │ OGTV
  │ ✔✔✔✔ CVE-2025-22868         HIGH         7.5   0.9%   ·  ↳ O:GHSA-6v2p-p543-phr9,GO-2025-3488 | V:MEND:CVE-2025-22868
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/oauth2@v0.25.0
  │ OGTV
  │ ✔✔✔✔ CVE-2025-22868         HIGH         7.5   0.9%   ·  ↳ O:GHSA-6v2p-p543-phr9,GO-2025-3488 | V:MEND:CVE-2025-22868
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/sys@v0.32.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-39824         LOW          3.3   0.2%   ·  ↳ O:GO-2026-5024 | V:MEND:CVE-2026-39824
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/text@v0.24.0
  │ OGTV
  │ ✔✔✔✔ CVE-2026-56851         HIGH         7.5   0.3%   ·  ↳ O:GO-2026-6629 | V:MEND:CVE-2026-56851
  │ ✔✔✔✔ CVE-2026-56852         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-5970 | V:MEND:CVE-2026-56852
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/google.golang.org/grpc@v1.69.4
  │ OGTV
  │ ✔✔✔✔ CVE-2026-33186         CRITICAL     9.1   1.6%   ·  ↳ O:GHSA-p77j-4mvh-x3m3,GO-2026-4762 | V:GHSA-P77J-4MVH-X3M3
  │ ✔✔✔✔ CVE-2026-84304         HIGH         8.7   0.6%   ·  ↳ O:GHSA-vp52-pcj8-j9qc,GO-2026-6348 | V:OSV:GO-2026-6348
  │ ✔✔✔✔ CVE-2026-84445         HIGH         8.7   0.6%   ·  ↳ O:GHSA-2v4p-qf9q-27wj,GO-2026-6443 | V:MEND:CVE-2026-84445
  │ ✔✔✔✔ CVE-2026-84303         MEDIUM       6.3   0.3%   ·  ↳ O:GHSA-qc2q-p7wx-3px3,GO-2026-6441 | V:OSV:GO-2026-6441
  │ ✘✘✘✔ WS-2026-0025           CRITICAL     9.1      -   ·  ↳ V:MEND:WS-2026-0025
  │ ✔✔✔✔ GHSA-HRXH-6V49-42GF    HIGH         8.8      -   ·  ↳ O:GO-2026-6061 | V:GO-2026-6061,OSV:GO-2026-6061
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/google.golang.org/grpc@v1.71.1
  │ OGTV
  │ ✔✔✔✔ CVE-2026-33186         CRITICAL     9.1   1.6%   ·  ↳ O:GHSA-p77j-4mvh-x3m3,GO-2026-4762 | V:GHSA-P77J-4MVH-X3M3
  │ ✔✔✔✔ CVE-2026-84304         HIGH         8.7   0.6%   ·  ↳ O:GHSA-vp52-pcj8-j9qc,GO-2026-6348 | V:OSV:GO-2026-6348
  │ ✔✔✔✔ CVE-2026-84445         HIGH         8.7   0.6%   ·  ↳ O:GHSA-2v4p-qf9q-27wj,GO-2026-6443 | V:MEND:CVE-2026-84445
  │ ✔✔✔✔ CVE-2026-84303         MEDIUM       6.3   0.3%   ·  ↳ O:GHSA-qc2q-p7wx-3px3,GO-2026-6441 | V:OSV:GO-2026-6441
  │ ✘✘✘✔ WS-2026-0025           CRITICAL     9.1      -   ·  ↳ V:MEND:WS-2026-0025
  │ ✔✔✔✔ GHSA-HRXH-6V49-42GF    HIGH         8.8      -   ·  ↳ O:GO-2026-6061 | V:GO-2026-6061,OSV:GO-2026-6061
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/stdlib@1.23.8
  │ OGTV
  │ ✔✔✔✔ CVE-2025-68121         CRITICAL    10.0   0.9%   ·  ↳ O:GO-2026-4337 | V:OSV:GO-2026-4337
  │ ✔✔✔✔ CVE-2026-39821         CRITICAL     9.6   0.7%   ·  ↳ O:GO-2026-5026 | V:OSV:GO-2026-5026
  │ ✔✔✔✔ CVE-2026-56857         CRITICAL     9.8   0.5%   ·  ↳ O:GO-2026-6604 | V:OSV:GO-2026-6604
  │ ✔✔✔✔ CVE-2026-78663         CRITICAL     9.1   0.6%   ·  ↳ O:GO-2026-6612 | V:OSV:GO-2026-6612
  │ ✔✔✔✔ CVE-2025-47907         HIGH         7.0   0.4%   ·  ↳ O:GO-2025-3849 | V:OSV:GO-2025-3849
  │ ✔✔✔✔ CVE-2025-58187         HIGH         7.5   0.4%   ·  ↳ O:GO-2025-4007 | V:OSV:GO-2025-4007
  │ ✔✔✔✔ CVE-2025-58188         HIGH         7.5   0.4%   ·  ↳ O:GO-2025-4013 | V:OSV:GO-2025-4013
  │ ✔✔✔✔ CVE-2025-61723         HIGH         7.5   0.7%   ·  ↳ O:GO-2025-4009 | V:OSV:GO-2025-4009
  │ ✔✔✔✔ CVE-2025-61725         HIGH         7.5   0.6%   ·  ↳ O:GO-2025-4006 | V:OSV:GO-2025-4006
  │ ✔✔✔✔ CVE-2025-61726         HIGH         7.5   2.3%   ·  ↳ O:GO-2026-4341 | V:OSV:GO-2026-4341
  │ ✔✔✔✔ CVE-2025-61729         HIGH         7.5   0.5%   ·  ↳ O:GO-2025-4155 | V:OSV:GO-2025-4155
  │ ✔✔✔✔ CVE-2026-25679         HIGH         7.5   0.8%   ·  ↳ O:GO-2026-4601 | V:OSV:GO-2026-4601
  │ ✔✔✔✔ CVE-2026-27145         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-5037 | V:OSV:GO-2026-5037
  │ ✔✔✔✔ CVE-2026-32280         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-4947 | V:OSV:GO-2026-4947
  │ ✔✔✔✔ CVE-2026-32281         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-4946 | V:OSV:GO-2026-4946
  │ ✔✔✔✔ CVE-2026-32283         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-4870 | V:OSV:GO-2026-4870
  │ ✔✔✔✔ CVE-2026-33811         HIGH         7.5   0.8%   ·  ↳ O:GO-2026-4981 | V:OSV:GO-2026-4981
  │ ✔✔✔✔ CVE-2026-33814         HIGH         7.5   0.8%   ·  ↳ O:GO-2026-4918 | V:OSV:GO-2026-4918
  │ ✔✔✔✔ CVE-2026-33818         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-5972 | V:OSV:GO-2026-5972
  │ ✔✔✔✔ CVE-2026-39820         HIGH         7.5   0.8%   ·  ↳ O:GO-2026-4986 | V:OSV:GO-2026-4986
  │ ✔✔✔✔ CVE-2026-39822         HIGH         7.8   0.2%   ·  ↳ O:GO-2026-4970 | V:OSV:GO-2026-4970
  │ ✔✔✔✔ CVE-2026-39836         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-4971 | V:OSV:GO-2026-4971
  │ ✔✔✔✔ CVE-2026-42499         HIGH         7.5   0.8%   ·  ↳ O:GO-2026-4977 | V:OSV:GO-2026-4977
  │ ✔✔✔✔ CVE-2026-42504         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-5038 | V:OSV:GO-2026-5038
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
  │ ✔✔✔✔ CVE-2025-0913          MEDIUM       5.5   0.3%   ·  ↳ O:GO-2025-3750 | V:OSV:GO-2025-3750
  │ ✔✔✔✔ CVE-2025-4673          MEDIUM       6.8   0.7%   ·  ↳ O:GO-2025-3751 | V:OSV:GO-2025-3751
  │ ✔✔✔✔ CVE-2025-47906         MEDIUM       6.5   0.5%   ·  ↳ O:GO-2025-3956 | V:OSV:GO-2025-3956
  │ ✔✔✔✔ CVE-2025-47912         MEDIUM       5.3   0.5%   ·  ↳ O:GO-2025-4010 | V:OSV:GO-2025-4010
  │ ✔✔✔✔ CVE-2025-58183         MEDIUM       4.3   0.4%   ·  ↳ O:GO-2025-4014 | V:OSV:GO-2025-4014
  │ ✔✔✔✔ CVE-2025-58185         MEDIUM       5.3   0.6%   ·  ↳ O:GO-2025-4011 | V:OSV:GO-2025-4011
  │ ✔✔✔✔ CVE-2025-58186         MEDIUM       5.3   0.6%   ·  ↳ O:GO-2025-4012 | V:OSV:GO-2025-4012
  │ ✔✔✔✔ CVE-2025-58189         MEDIUM       5.3   0.5%   ·  ↳ O:GO-2025-4008 | V:OSV:GO-2025-4008
  │ ✔✔✔✔ CVE-2025-61724         MEDIUM       5.3   0.6%   ·  ↳ O:GO-2025-4015 | V:OSV:GO-2025-4015
  │ ✔✔✔✔ CVE-2025-61727         MEDIUM       6.5   0.3%   ·  ↳ O:GO-2025-4175 | V:OSV:GO-2025-4175
  │ ✔✔✔✔ CVE-2025-61728         MEDIUM       6.5   0.7%   ·  ↳ O:GO-2026-4342 | V:OSV:GO-2026-4342
  │ ✔✔✔✔ CVE-2025-61730         MEDIUM       5.3   0.3%   ·  ↳ O:GO-2026-4340 | V:OSV:GO-2026-4340
  │ ✔✔✔✔ CVE-2026-27142         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-4603 | V:OSV:GO-2026-4603
  │ ✔✔✔✔ CVE-2026-32282         MEDIUM       6.4   0.3%   ·  ↳ O:GO-2026-4864 | V:OSV:GO-2026-4864
  │ ✔✔✔✔ CVE-2026-32288         MEDIUM       5.5   0.2%   ·  ↳ O:GO-2026-4869 | V:OSV:GO-2026-4869
  │ ✔✔✔✔ CVE-2026-32289         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-4865 | V:OSV:GO-2026-4865
  │ ✔✔✔✔ CVE-2026-39823         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-4982 | V:OSV:GO-2026-4982
  │ ✔✔✔✔ CVE-2026-39825         MEDIUM       5.3   0.4%   ·  ↳ O:GO-2026-4976 | V:OSV:GO-2026-4976
  │ ✔✔✔✔ CVE-2026-39826         MEDIUM       6.1   0.4%   ·  ↳ O:GO-2026-4980 | V:OSV:GO-2026-4980
  │ ✔✔✔✔ CVE-2026-42505         MEDIUM       5.3   0.4%   ·  ↳ O:GO-2026-5856 | V:OSV:GO-2026-5856
  │ ✔✔✔✔ CVE-2026-42507         MEDIUM       5.3   0.4%   ·  ↳ O:GO-2026-5039 | V:OSV:GO-2026-5039
  │ ✔✔✔✔ CVE-2026-56858         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-6091 | V:OSV:GO-2026-6091
  │ ✔✔✔✔ CVE-2026-56860         MEDIUM       5.9   0.5%   ·  ↳ O:GO-2026-6218 | V:OSV:GO-2026-6218
  │ ✔✔✔✔ CVE-2026-94448         MEDIUM       6.1   0.2%   ·  ↳ O:GO-2026-6599 | V:OSV:GO-2026-6599
  │ ✔✔✔✔ CVE-2026-97030         MEDIUM       6.1   0.2%   ·  ↳ O:GO-2026-6600 | V:OSV:GO-2026-6600
  │ ✔✔✔✔ CVE-2025-22873         LOW          3.8   0.2%   ·  ↳ O:GO-2026-4403 | V:OSV:GO-2026-4403
  │ ✔✔✔✔ CVE-2026-27139         LOW          2.5   0.1%   ·  ↳ O:GO-2026-4602 | V:OSV:GO-2026-4602
  └────────────────────────────────────────────────────────────────────────────────────────────────────
