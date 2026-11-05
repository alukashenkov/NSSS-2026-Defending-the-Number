# Vulnerability Comparison Report — insecureapp-20.04:latest

- **Image:** `insecureapp-20.04:latest`
- **Digest:** `sha256:3893236509066ada26fdab52594be25cd0a487c02832119fdf1a6738c09c58bd`
- **SBOM:** `insecureapp-20.04.trivy.cdx.json` — CycloneDX 1.7, trivy 0.76.0, built 2026-10-16T10:38:24+00:00
- **Report generated:** 2026-11-02T15:42:18
- **Scanners:** OSV (api.osv.dev) · Src OSV (api.osv.dev, by source package) · Grype (grype 0.121.0) · Trivy (trivy 0.76.1) · Vulners (vulners.com audit API v4)

## Summary

  SBOM Components (Raw):   687
  Deduplicated PURLs:      540
    by ecosystem:          pypi 39 · deb 293 · golang 208
  Clean (0 vulns):         328
  Vulnerable:              212

  Scanner              |   Pkgs Scanned |  Pkgs w/ Vulns | Total Vuln IDs
  ---------------------+----------------+----------------+---------------
  OSV                  |            540 |             72 |            529
  Src OSV              |            540 |            208 |           6193
  Grype                |            540 |             70 |            500
  Trivy                |            540 |             45 |            237
  Vulners              |            540 |            165 |            565

  All 5 agree: 236     ≥2 agree:  679     Total: 6225    (CVE:6165 GHSA:11 Other:49)
  Exclusive to: OSV:0  Src OSV:5514  Grype:2  Trivy:0  Vulners:30

## VULNERABLE PACKAGES — [O]SV [S]rc OSV [G]rype [T]rivy [V]ulners findings

  ▸ Python (PyPI) (15 packages)
    ✔✔✔✔✔  pkg:pypi/aiohttp@3.9.1
    ✔✔✔✔✔  pkg:pypi/certifi@2019.11.28
    ✔✔✔✔✔  pkg:pypi/cryptography@3.3.2
    ✔✔✔✔✔  pkg:pypi/flask@3.0.2
    ✔✔✔✔✔  pkg:pypi/idna@2.7
    ✔✔✔✔✔  pkg:pypi/idna@2.8
    ✔✔✔✔✔  pkg:pypi/pip@20.0.2
    ✔✔✘✘✘  pkg:pypi/python-apt@2.0.1%2Bubuntu0.20.4.1
    ✔✔✔✔✔  pkg:pypi/requests@2.19.1
    ✔✔✔✔✔  pkg:pypi/requests@2.22.0
    ✔✔✔✔✔  pkg:pypi/setuptools@45.2.0
    ✔✔✔✔✔  pkg:pypi/urllib3@1.23
    ✔✔✔✔✔  pkg:pypi/urllib3@1.25.8
    ✔✔✔✔✔  pkg:pypi/werkzeug@3.0.6
    ✔✔✔✔✔  pkg:pypi/wheel@0.34.2

  ▸ Debian/Ubuntu (deb) (163 packages)
    ✔✔✔✘✔  pkg:deb/ubuntu/binutils@2.34-6ubuntu1.11
    ✘✔✘✘✔  pkg:deb/ubuntu/binutils-aarch64-linux-gnu@2.34-6ubuntu1.11
    ✘✔✘✘✔  pkg:deb/ubuntu/binutils-common@2.34-6ubuntu1.11
    ✘✔✘✘✔  pkg:deb/ubuntu/bsdutils@1%3A2.34-0.1ubuntu9.6
    ✔✔✔✘✔  pkg:deb/ubuntu/bzip2@1.0.8-2
    ✔✔✘✘✘  pkg:deb/ubuntu/ca-certificates@20240203~20.04.1
    ✔✔✔✘✘  pkg:deb/ubuntu/coreutils@8.30-3ubuntu2
    ✘✔✘✘✘  pkg:deb/ubuntu/cpp@4%3A9.3.0-1ubuntu2
    ✘✔✘✘✔  pkg:deb/ubuntu/cpp-9@9.4.0-1ubuntu1~20.04.2
    ✔✔✔✘✔  pkg:deb/ubuntu/curl@7.68.0-1ubuntu2.25
    ✔✔✔✘✔  pkg:deb/ubuntu/dash@0.5.10.2-6
    ✔✔✔✘✔  pkg:deb/ubuntu/dbus@1.12.16-2ubuntu2.3
    ✘✔✘✘✔  pkg:deb/ubuntu/dbus-user-session@1.12.16-2ubuntu2.3
    ✔✔✔✘✔  pkg:deb/ubuntu/diffutils@1%3A3.7-3
    ✘✔✘✘✘  pkg:deb/ubuntu/dirmngr@2.2.19-3ubuntu2.5
    ✘✔✘✘✔  pkg:deb/ubuntu/dmsetup@2%3A1.02.167-1ubuntu1
    ✔✔✔✘✘  pkg:deb/ubuntu/dpkg@1.19.7ubuntu3.2
    ✘✔✘✘✘  pkg:deb/ubuntu/dpkg-dev@1.19.7ubuntu3.2
    ✘✔✘✘✔  pkg:deb/ubuntu/fdisk@2.34-0.1ubuntu9.6
    ✘✔✘✘✘  pkg:deb/ubuntu/g%2B%2B@4%3A9.3.0-1ubuntu2
    ✘✔✘✘✔  pkg:deb/ubuntu/g%2B%2B-9@9.4.0-1ubuntu1~20.04.2
    ✘✔✘✘✘  pkg:deb/ubuntu/gcc@4%3A9.3.0-1ubuntu2
    ✘✔✘✘✔  pkg:deb/ubuntu/gcc-10-base@10.5.0-1ubuntu1~20.04
    ✔✔✔✘✔  pkg:deb/ubuntu/gcc-9@9.4.0-1ubuntu1~20.04.2
    ✘✔✘✘✔  pkg:deb/ubuntu/gcc-9-base@9.4.0-1ubuntu1~20.04.2
    ✘✔✘✘✔  pkg:deb/ubuntu/gir1.2-packagekitglib-1.0@1.1.13-2ubuntu1.1
    ✔✔✔✘✔  pkg:deb/ubuntu/glib-networking@2.64.2-1ubuntu0.1
    ✘✔✘✘✔  pkg:deb/ubuntu/glib-networking-common@2.64.2-1ubuntu0.1
    ✘✔✘✘✔  pkg:deb/ubuntu/glib-networking-services@2.64.2-1ubuntu0.1
    ✘✔✘✘✔  pkg:deb/ubuntu/gnupg@2.2.19-3ubuntu2.5
    ✘✔✘✘✘  pkg:deb/ubuntu/gnupg-l10n@2.2.19-3ubuntu2.5
    ✘✔✘✘✘  pkg:deb/ubuntu/gnupg-utils@2.2.19-3ubuntu2.5
    ✘✔✘✘✔  pkg:deb/ubuntu/gpg@2.2.19-3ubuntu2.5
    ✘✔✘✘✘  pkg:deb/ubuntu/gpg-agent@2.2.19-3ubuntu2.5
    ✘✔✘✘✘  pkg:deb/ubuntu/gpg-wks-client@2.2.19-3ubuntu2.5
    ✘✔✘✘✘  pkg:deb/ubuntu/gpg-wks-server@2.2.19-3ubuntu2.5
    ✘✔✘✘✘  pkg:deb/ubuntu/gpgconf@2.2.19-3ubuntu2.5
    ✘✔✘✘✘  pkg:deb/ubuntu/gpgsm@2.2.19-3ubuntu2.5
    ✘✔✘✘✘  pkg:deb/ubuntu/gpgv@2.2.19-3ubuntu2.5
    ✔✔✔✘✔  pkg:deb/ubuntu/gzip@1.10-0ubuntu4.1
    ✘✔✘✘✘  pkg:deb/ubuntu/krb5-locales@1.17-6ubuntu4.11
    ✘✔✘✘✘  pkg:deb/ubuntu/libacl1@2.2.53-6
    ✘✔✘✘✔  pkg:deb/ubuntu/libasan5@9.4.0-1ubuntu1~20.04.2
    ✘✔✘✘✔  pkg:deb/ubuntu/libatomic1@10.5.0-1ubuntu1~20.04
    ✘✔✘✘✔  pkg:deb/ubuntu/libattr1@1%3A2.4.48-5
    ✘✔✘✘✔  pkg:deb/ubuntu/libbinutils@2.34-6ubuntu1.11
    ✘✔✘✘✔  pkg:deb/ubuntu/libblkid1@2.34-0.1ubuntu9.6
    ✘✔✘✘✔  pkg:deb/ubuntu/libbrotli1@1.0.7-6ubuntu0.1
    ✘✔✘✘✘  pkg:deb/ubuntu/libbz2-1.0@1.0.8-2
    ✘✔✘✔✔  pkg:deb/ubuntu/libc-bin@2.31-0ubuntu9.17
    ✘✔✘✘✔  pkg:deb/ubuntu/libc-dev-bin@2.31-0ubuntu9.18
    ✘✔✘✘✔  pkg:deb/ubuntu/libc6@2.31-0ubuntu9.18
    ✘✔✘✘✘  pkg:deb/ubuntu/libc6-dev@2.31-0ubuntu9.18
    ✔✔✔✘✔  pkg:deb/ubuntu/libcap2@1%3A2.32-1ubuntu0.2
    ✘✔✘✘✔  pkg:deb/ubuntu/libcap2-bin@1%3A2.32-1ubuntu0.2
    ✘✔✘✘✔  pkg:deb/ubuntu/libcc1-0@10.5.0-1ubuntu1~20.04
    ✘✔✘✘✔  pkg:deb/ubuntu/libctf-nobfd0@2.34-6ubuntu1.11
    ✘✔✘✘✔  pkg:deb/ubuntu/libctf0@2.34-6ubuntu1.11
    ✘✔✘✘✔  pkg:deb/ubuntu/libcurl4@7.68.0-1ubuntu2.25
    ✘✔✘✘✔  pkg:deb/ubuntu/libdbus-1-3@1.12.16-2ubuntu2.3
    ✘✔✘✘✔  pkg:deb/ubuntu/libdevmapper1.02.1@2%3A1.02.167-1ubuntu1
    ✘✔✘✘✘  pkg:deb/ubuntu/libdpkg-perl@1.19.7ubuntu3.2
    ✘✔✘✘✔  pkg:deb/ubuntu/libelf1@0.176-1.1ubuntu0.1
    ✘✔✘✘✔  pkg:deb/ubuntu/libexpat1@2.2.9-1ubuntu0.8
    ✘✔✘✘✔  pkg:deb/ubuntu/libexpat1-dev@2.2.9-1ubuntu0.8
    ✘✔✘✘✔  pkg:deb/ubuntu/libfdisk1@2.34-0.1ubuntu9.6
    ✘✔✘✘✘  pkg:deb/ubuntu/libgcc-9-dev@9.4.0-1ubuntu1~20.04.2
    ✘✔✘✘✔  pkg:deb/ubuntu/libgcc-s1@10.5.0-1ubuntu1~20.04
    ✔✔✔✘✔  pkg:deb/ubuntu/libgcrypt20@1.8.5-5ubuntu1.1
    ✘✔✘✘✔  pkg:deb/ubuntu/libglib2.0-0@2.64.6-1~ubuntu20.04.9
    ✘✔✘✘✔  pkg:deb/ubuntu/libglib2.0-bin@2.64.6-1~ubuntu20.04.9
    ✘✔✘✘✘  pkg:deb/ubuntu/libglib2.0-data@2.64.6-1~ubuntu20.04.9
    ✘✔✘✘✔  pkg:deb/ubuntu/libgnutls30@3.6.13-2ubuntu1.12
    ✘✔✘✘✔  pkg:deb/ubuntu/libgomp1@10.5.0-1ubuntu1~20.04
    ✘✔✘✘✘  pkg:deb/ubuntu/libgssapi-krb5-2@1.17-6ubuntu4.11
    ✘✔✘✘✔  pkg:deb/ubuntu/libicu66@66.1-2ubuntu2.1
    ✘✔✘✘✘  pkg:deb/ubuntu/libip4tc2@1.8.4-3ubuntu2.1
    ✘✔✘✘✔  pkg:deb/ubuntu/libitm1@10.5.0-1ubuntu1~20.04
    ✘✔✘✘✘  pkg:deb/ubuntu/libk5crypto3@1.17-6ubuntu4.11
    ✘✔✘✘✘  pkg:deb/ubuntu/libkmod2@27-1ubuntu2.1
    ✘✔✘✘✘  pkg:deb/ubuntu/libkrb5-3@1.17-6ubuntu4.11
    ✘✔✘✘✘  pkg:deb/ubuntu/libkrb5support0@1.17-6ubuntu4.11
    ✘✔✘✘✔  pkg:deb/ubuntu/liblmdb0@0.9.24-1
    ✘✔✘✘✔  pkg:deb/ubuntu/liblsan0@10.5.0-1ubuntu1~20.04
    ✘✔✘✘✘  pkg:deb/ubuntu/liblz4-1@1.9.2-2ubuntu0.20.04.1
    ✘✔✘✘✔  pkg:deb/ubuntu/liblzma5@5.2.4-1ubuntu1.1
    ✘✔✘✘✔  pkg:deb/ubuntu/libmount1@2.34-0.1ubuntu9.6
    ✘✔✘✘✔  pkg:deb/ubuntu/libncurses6@6.2-0ubuntu2.1
    ✘✔✘✘✔  pkg:deb/ubuntu/libncursesw6@6.2-0ubuntu2.1
    ✘✔✘✘✔  pkg:deb/ubuntu/libnghttp2-14@1.40.0-1ubuntu0.3
    ✘✔✘✘✔  pkg:deb/ubuntu/libnss-systemd@245.4-4ubuntu3.24
    ✘✔✘✘✔  pkg:deb/ubuntu/libp11-kit0@0.23.20-1ubuntu0.1
    ✘✔✘✘✔  pkg:deb/ubuntu/libpackagekit-glib2-18@1.1.13-2ubuntu1.1
    ✘✔✘✘✔  pkg:deb/ubuntu/libpam-cap@1%3A2.32-1ubuntu0.2
    ✘✔✘✘✘  pkg:deb/ubuntu/libpam-modules@1.3.1-5ubuntu4.7
    ✘✔✘✘✘  pkg:deb/ubuntu/libpam-modules-bin@1.3.1-5ubuntu4.7
    ✘✔✘✘✘  pkg:deb/ubuntu/libpam-runtime@1.3.1-5ubuntu4.7
    ✘✔✘✘✔  pkg:deb/ubuntu/libpam-systemd@245.4-4ubuntu3.24
    ✘✔✘✘✘  pkg:deb/ubuntu/libpam0g@1.3.1-5ubuntu4.7
    ✘✔✘✘✔  pkg:deb/ubuntu/libpcre2-8-0@10.34-7ubuntu0.1
    ✘✔✘✘✘  pkg:deb/ubuntu/libpcre3@2%3A8.39-12ubuntu0.1
    ✘✔✘✘✔  pkg:deb/ubuntu/libperl5.30@5.30.0-9ubuntu0.5
    ✘✔✘✘✔  pkg:deb/ubuntu/libpolkit-agent-1-0@0.105-26ubuntu1.3
    ✘✔✘✘✔  pkg:deb/ubuntu/libpolkit-gobject-1-0@0.105-26ubuntu1.3
    ✘✔✘✘✔  pkg:deb/ubuntu/libpython3.8@3.8.10-0ubuntu1~20.04.18
    ✘✔✘✘✘  pkg:deb/ubuntu/libpython3.8-dev@3.8.10-0ubuntu1~20.04.18
    ✘✔✘✘✔  pkg:deb/ubuntu/libpython3.8-minimal@3.8.10-0ubuntu1~20.04.18
    ✘✔✘✘✔  pkg:deb/ubuntu/libpython3.8-stdlib@3.8.10-0ubuntu1~20.04.18
    ✘✔✘✘✘  pkg:deb/ubuntu/librtmp1@2.4%2B20151223.gitfa8646d.1-2build1
    ✘✔✘✘✔  pkg:deb/ubuntu/libsasl2-2@2.1.27%2Bdfsg-2ubuntu0.1
    ✘✔✘✘✔  pkg:deb/ubuntu/libsasl2-modules@2.1.27%2Bdfsg-2ubuntu0.1
    ✘✔✘✘✔  pkg:deb/ubuntu/libsasl2-modules-db@2.1.27%2Bdfsg-2ubuntu0.1
    ✘✔✘✘✔  pkg:deb/ubuntu/libsmartcols1@2.34-0.1ubuntu9.6
    ✘✔✘✘✔  pkg:deb/ubuntu/libsoup2.4-1@2.70.0-1ubuntu0.5
    ✘✔✘✘✔  pkg:deb/ubuntu/libsqlite3-0@3.31.1-4ubuntu0.7
    ✘✔✘✘✔  pkg:deb/ubuntu/libssh-4@0.9.3-2ubuntu2.5
    ✘✔✘✘✔  pkg:deb/ubuntu/libssl1.1@1.1.1f-1ubuntu2.24
    ✘✔✘✘✘  pkg:deb/ubuntu/libstdc%2B%2B-9-dev@9.4.0-1ubuntu1~20.04.2
    ✘✔✘✘✔  pkg:deb/ubuntu/libstdc%2B%2B6@10.5.0-1ubuntu1~20.04
    ✘✔✘✘✔  pkg:deb/ubuntu/libsystemd0@245.4-4ubuntu3.24
    ✔✔✔✘✔  pkg:deb/ubuntu/libtasn1-6@4.16.0-2ubuntu0.1
    ✘✔✘✘✔  pkg:deb/ubuntu/libtinfo6@6.2-0ubuntu2.1
    ✘✔✘✘✔  pkg:deb/ubuntu/libtsan0@10.5.0-1ubuntu1~20.04
    ✘✔✘✘✔  pkg:deb/ubuntu/libubsan1@10.5.0-1ubuntu1~20.04
    ✘✔✘✘✔  pkg:deb/ubuntu/libudev1@245.4-4ubuntu3.24
    ✘✔✘✘✔  pkg:deb/ubuntu/libuuid1@2.34-0.1ubuntu9.6
    ✔✔✔✘✔  pkg:deb/ubuntu/libxml2@2.9.10%2Bdfsg-5ubuntu0.20.04.10
    ✘✔✘✘✘  pkg:deb/ubuntu/linux-libc-dev@5.4.0-216.236
    ✘✔✘✘✔  pkg:deb/ubuntu/login@1%3A4.8.1-1ubuntu5.20.04.5
    ✘✔✘✘✔  pkg:deb/ubuntu/mount@2.34-0.1ubuntu9.6
    ✘✔✘✘✔  pkg:deb/ubuntu/ncurses-base@6.2-0ubuntu2.1
    ✘✔✘✘✔  pkg:deb/ubuntu/ncurses-bin@6.2-0ubuntu2.1
    ✔✔✔✘✔  pkg:deb/ubuntu/openssl@1.1.1f-1ubuntu2.24
    ✔✔✔✘✔  pkg:deb/ubuntu/packagekit@1.1.13-2ubuntu1.1
    ✘✔✘✘✔  pkg:deb/ubuntu/packagekit-tools@1.1.13-2ubuntu1.1
    ✘✔✘✘✔  pkg:deb/ubuntu/passwd@1%3A4.8.1-1ubuntu5.20.04.5
    ✔✔✔✘✔  pkg:deb/ubuntu/patch@2.7.6-6
    ✔✔✔✘✔  pkg:deb/ubuntu/perl@5.30.0-9ubuntu0.5
    ✘✔✘✘✔  pkg:deb/ubuntu/perl-base@5.30.0-9ubuntu0.5
    ✘✔✘✘✔  pkg:deb/ubuntu/perl-modules-5.30@5.30.0-9ubuntu0.5
    ✔✔✔✘✔  pkg:deb/ubuntu/policykit-1@0.105-26ubuntu1.3
    ✘✔✘✘✔  pkg:deb/ubuntu/python-apt-common@2.0.1ubuntu0.20.04.1
    ✘✔✘✘✔  pkg:deb/ubuntu/python-pip-whl@20.0.2-5ubuntu1.11
    ✘✔✘✘✔  pkg:deb/ubuntu/python3-apt@2.0.1ubuntu0.20.04.1
    ✘✔✘✘✘  pkg:deb/ubuntu/python3-certifi@2019.11.28-1
    ✘✔✘✘✘  pkg:deb/ubuntu/python3-idna@2.8-1ubuntu0.1
    ✘✔✘✘✔  pkg:deb/ubuntu/python3-pip@20.0.2-5ubuntu1.11
    ✘✔✘✘✘  pkg:deb/ubuntu/python3-pkg-resources@45.2.0-1ubuntu0.3
    ✘✔✘✘✔  pkg:deb/ubuntu/python3-requests@2.22.0-2ubuntu1.1
    ✘✔✘✘✘  pkg:deb/ubuntu/python3-setuptools@45.2.0-1ubuntu0.3
    ✘✔✘✘✔  pkg:deb/ubuntu/python3-urllib3@1.25.8-2ubuntu0.4
    ✔✔✔✘✔  pkg:deb/ubuntu/python3.8@3.8.10-0ubuntu1~20.04.18
    ✘✔✘✘✘  pkg:deb/ubuntu/python3.8-dev@3.8.10-0ubuntu1~20.04.18
    ✘✔✘✘✔  pkg:deb/ubuntu/python3.8-minimal@3.8.10-0ubuntu1~20.04.18
    ✔✔✔✘✔  pkg:deb/ubuntu/sed@4.7-1
    ✔✔✔✘✔  pkg:deb/ubuntu/systemd@245.4-4ubuntu3.24
    ✘✔✘✘✔  pkg:deb/ubuntu/systemd-sysv@245.4-4ubuntu3.24
    ✘✔✘✘✔  pkg:deb/ubuntu/systemd-timesyncd@245.4-4ubuntu3.24
    ✔✔✔✘✔  pkg:deb/ubuntu/tar@1.30%2Bdfsg-7ubuntu0.20.04.4
    ✔✔✔✘✔  pkg:deb/ubuntu/util-linux@2.34-0.1ubuntu9.6
    ✔✔✔✘✔  pkg:deb/ubuntu/xz-utils@5.2.4-1ubuntu1.1
    ✘✔✘✘✘  pkg:deb/ubuntu/zlib1g@1%3A1.2.11.dfsg-2ubuntu1.5
    ✘✔✘✘✘  pkg:deb/ubuntu/zlib1g-dev@1%3A1.2.11.dfsg-2ubuntu1.5

  ▸ Go (34 packages)
    ✘✘✘✘✔  pkg:golang/github.com/aws/aws-sdk-go-v2/service/sso@v1.22.4
    ✘✘✘✘✔  pkg:golang/github.com/aws/aws-sdk-go-v2/service/ssooidc@v1.26.4
    ✘✘✘✘✔  pkg:golang/github.com/aws/aws-sdk-go-v2/service/sts@v1.30.3
    ✔✔✔✔✔  pkg:golang/github.com/containerd/containerd/v2@v2.0.4
    ✘✘✘✘✔  pkg:golang/github.com/docker/buildx@v0.23.0
    ✔✔✔✔✔  pkg:golang/github.com/docker/cli@v28.0.4%2Bincompatible
    ✔✔✔✔✔  pkg:golang/github.com/docker/cli@v28.1.0%2Bincompatible
    ✔✔✔✔✔  pkg:golang/github.com/docker/compose/v2@v2.35.1
    ✔✔✔✔✔  pkg:golang/github.com/docker/distribution@v2.8.3%2Bincompatible
    ✔✔✔✔✔  pkg:golang/github.com/docker/docker@v28.0.4%2Bincompatible
    ✔✔✔✔✔  pkg:golang/github.com/docker/docker@v28.1.0%2Bincompatible
    ✔✔✔✔✔  pkg:golang/github.com/go-viper/mapstructure/v2@v2.0.0
    ✔✔✔✔✔  pkg:golang/github.com/gorilla/websocket@v1.5.0
    ✔✔✔✔✔  pkg:golang/github.com/in-toto/in-toto-golang@v0.5.0
    ✔✔✔✔✔  pkg:golang/github.com/klauspost/compress@v1.18.0
    ✔✔✔✔✔  pkg:golang/github.com/moby/buildkit@v0.21.0
    ✔✔✔✔✔  pkg:golang/github.com/moby/go-archive@v0.1.0
    ✔✔✔✔✔  pkg:golang/github.com/moby/spdystream@v0.4.0
    ✔✔✔✔✔  pkg:golang/github.com/moby/sys/user@v0.4.0
    ✔✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp@v1.31.0
    ✔✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace@v1.31.0
    ✔✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc@v1.31.0
    ✔✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp@v1.31.0
    ✔✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/sdk@v1.31.0
    ✔✔✔✔✔  pkg:golang/go.opentelemetry.io/otel/sdk@v1.34.0
    ✔✔✔✔✔  pkg:golang/golang.org/x/crypto@v0.37.0
    ✔✔✔✔✔  pkg:golang/golang.org/x/net@v0.39.0
    ✔✔✔✔✔  pkg:golang/golang.org/x/oauth2@v0.23.0
    ✔✔✔✔✔  pkg:golang/golang.org/x/oauth2@v0.25.0
    ✔✔✔✔✔  pkg:golang/golang.org/x/sys@v0.32.0
    ✔✔✔✔✔  pkg:golang/golang.org/x/text@v0.24.0
    ✔✔✔✔✔  pkg:golang/google.golang.org/grpc@v1.69.4
    ✔✔✔✔✔  pkg:golang/google.golang.org/grpc@v1.71.1
    ✔✔✔✔✔  pkg:golang/stdlib@v1.23.8

## VULNERABILITY DETAIL — All Scanner Findings

  Every vulnerability found, and which scanners agree on it.
  CVSS, EPSS and KEV come from Vulners where it knows the CVE, otherwise from the scanner that reported it.
  Vulners CVE data: 6165 of 6165 CVEs known, CVSS+EPSS on 6129 (99.4%).
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
  ┌─ pkg:pypi/certifi@2019.11.28
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2023-37920         CRITICAL     9.8   0.6%   ·  ↳ O:GHSA-xqr8-7jwr-rhp7,PYSEC-2023-135 | S:GHSA-xqr8-7jwr-rhp7,PYSEC-2023-135 | V:GHSA-XQR8-7JWR-RHP7
  │ ✔✔✔✔✔ CVE-2022-23491         HIGH         7.5   0.5%   ·  ↳ O:GHSA-43fp-rhv2-5gv8,PYSEC-2022-42986 | S:GHSA-43fp-rhv2-5gv8,PYSEC-2022-42986 | V:GHSA-43FP-RHV2-5GV8
  │ ✔✔✘✘✔ CVE-2024-39689         HIGH         7.5   1.0%   ·  ↳ O:PYSEC-2024-230 | S:PYSEC-2024-230 | V:OSV:PYSEC-2024-230
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
  ┌─ pkg:pypi/idna@2.8
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2024-3651          HIGH         7.5   1.4%   ·  ↳ O:GHSA-jjg7-2v4v-x38h,PYSEC-2024-60 | S:GHSA-jjg7-2v4v-x38h,PYSEC-2024-60 | V:MEND:CVE-2024-3651
  │ ✔✔✔✔✔ CVE-2026-45409         MEDIUM       6.9   0.4%   ·  ↳ O:GHSA-65pc-fj4g-8rjx,PYSEC-2026-215 | S:GHSA-65pc-fj4g-8rjx,PYSEC-2026-215 | V:MEND:CVE-2026-45409
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/pip@20.0.2
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-8643          HIGH         8.0   0.3%   ·  ↳ O:GHSA-wf93-45jw-7689,PYSEC-2026-196 | S:GHSA-wf93-45jw-7689,PYSEC-2026-196 | V:MEND:CVE-2026-8643
  │ ✔✔✔✔✔ CVE-2021-3572          MEDIUM       5.7   1.8%   ·  ↳ O:GHSA-5xp3-jfq3-5q8x,PYSEC-2021-437 | S:GHSA-5xp3-jfq3-5q8x,PYSEC-2021-437 | V:MEND:CVE-2021-3572
  │ ✔✔✔✔✔ CVE-2023-5752          MEDIUM       5.5   0.5%   ·  ↳ O:GHSA-mq26-g339-26xf,PYSEC-2023-228 | S:GHSA-mq26-g339-26xf,PYSEC-2023-228 | V:MEND:CVE-2023-5752
  │ ✔✔✔✔✔ CVE-2025-8869          MEDIUM       5.9   0.5%   ·  ↳ O:GHSA-4xh5-x5gv-qwph,PYSEC-2026-1795 | S:GHSA-4xh5-x5gv-qwph,PYSEC-2026-1795 | V:MEND:CVE-2025-8869
  │ ✔✔✔✔✔ CVE-2026-13346         MEDIUM       6.5   0.3%   ·  ↳ O:GHSA-qwm4-qh6w-59xr,PYSEC-2026-3721 | S:GHSA-qwm4-qh6w-59xr,PYSEC-2026-3721 | V:MEND:CVE-2026-13346
  │ ✔✔✔✔✔ CVE-2026-3219          MEDIUM       4.6   0.1%   ·  ↳ O:GHSA-58qw-9mgm-455v,PYSEC-2026-2875 | S:GHSA-58qw-9mgm-455v,PYSEC-2026-2875 | V:MEND:CVE-2026-3219
  │ ✔✔✔✔✔ CVE-2026-6357          MEDIUM       5.3   0.1%   ·  ↳ O:GHSA-jp4c-xjxw-mgf9,PYSEC-2026-2876 | S:GHSA-jp4c-xjxw-mgf9,PYSEC-2026-2876 | V:MEND:CVE-2026-6357
  │ ✔✔✔✔✔ CVE-2026-1703          LOW          2.0   0.4%   ·  ↳ O:GHSA-6vgw-5pg2-w6jp,PYSEC-2026-1796 | S:GHSA-6vgw-5pg2-w6jp,PYSEC-2026-1796 | V:MEND:CVE-2026-1703
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/python-apt@2.0.1%2Bubuntu0.20.4.1
  │ OSGTV
  │ ✔✔✘✘✘ CVE-2019-15795         MEDIUM       4.7   0.5%   ·  ↳ O:GHSA-rp8m-h266-53jh | S:GHSA-rp8m-h266-53jh
  │ ✔✔✘✘✘ CVE-2019-15796         MEDIUM       4.7   0.5%   ·  ↳ O:GHSA-pj65-3pf6-c5q4 | S:GHSA-pj65-3pf6-c5q4
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/requests@2.19.1
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2018-18074         HIGH         7.5   6.9%   ·  ↳ O:GHSA-x84v-xcm2-53pg,PYSEC-2018-28 | S:GHSA-x84v-xcm2-53pg,PYSEC-2018-28 | V:OSV:PYSEC-2018-28
  │ ✔✔✔✔✔ CVE-2023-32681         MEDIUM       6.1   3.0%   ·  ↳ O:GHSA-j8r2-6x86-q33q,PYSEC-2023-74 | S:GHSA-j8r2-6x86-q33q,PYSEC-2023-74 | V:GHSA-J8R2-6X86-Q33Q
  │ ✔✔✔✔✔ CVE-2024-35195         MEDIUM       5.6   0.3%   ·  ↳ O:GHSA-9wx4-h78v-vm56,PYSEC-2026-1873 | S:GHSA-9wx4-h78v-vm56,PYSEC-2026-1873 | V:GHSA-9WX4-H78V-VM56
  │ ✔✔✔✔✔ CVE-2024-47081         MEDIUM       5.3   1.0%   ·  ↳ O:GHSA-9hjg-9r4m-mvj7,PYSEC-2026-1872 | S:GHSA-9hjg-9r4m-mvj7,PYSEC-2026-1872 | V:MEND:CVE-2024-47081
  │ ✔✔✔✔✔ CVE-2026-25645         MEDIUM       5.5   0.2%   ·  ↳ O:GHSA-gc5v-m9x4-r6x2,PYSEC-2026-2275 | S:GHSA-gc5v-m9x4-r6x2,PYSEC-2026-2275 | V:GHSA-GC5V-M9X4-R6X2
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/requests@2.22.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2023-32681         MEDIUM       6.1   3.0%   ·  ↳ O:GHSA-j8r2-6x86-q33q,PYSEC-2023-74 | S:GHSA-j8r2-6x86-q33q,PYSEC-2023-74 | V:GHSA-J8R2-6X86-Q33Q
  │ ✔✔✔✔✔ CVE-2024-35195         MEDIUM       5.6   0.3%   ·  ↳ O:GHSA-9wx4-h78v-vm56,PYSEC-2026-1873 | S:GHSA-9wx4-h78v-vm56,PYSEC-2026-1873 | V:GHSA-9WX4-H78V-VM56
  │ ✔✔✔✔✔ CVE-2024-47081         MEDIUM       5.3   1.0%   ·  ↳ O:GHSA-9hjg-9r4m-mvj7,PYSEC-2026-1872 | S:GHSA-9hjg-9r4m-mvj7,PYSEC-2026-1872 | V:MEND:CVE-2024-47081
  │ ✔✔✔✔✔ CVE-2026-25645         MEDIUM       5.5   0.2%   ·  ↳ O:GHSA-gc5v-m9x4-r6x2,PYSEC-2026-2275 | S:GHSA-gc5v-m9x4-r6x2,PYSEC-2026-2275 | V:GHSA-GC5V-M9X4-R6X2
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/setuptools@45.2.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2024-6345          HIGH         8.8   1.9%   ·  ↳ O:GHSA-cx63-2mw6-8hw5,PYSEC-2026-1918 | S:GHSA-cx63-2mw6-8hw5,PYSEC-2026-1918 | V:MEND:CVE-2024-6345
  │ ✔✔✔✔✔ CVE-2025-47273         HIGH         8.8   1.6%   ·  ↳ O:GHSA-5rjg-fvgr-3xxf,PYSEC-2025-49 | S:GHSA-5rjg-fvgr-3xxf,PYSEC-2025-49 | V:MEND:CVE-2025-47273
  │ ✔✔✔✔✔ CVE-2022-40897         MEDIUM       5.9   2.6%   ·  ↳ O:GHSA-r9hx-vwmv-q579,PYSEC-2022-43012 | S:GHSA-r9hx-vwmv-q579,PYSEC-2022-43012 | V:MEND:CVE-2022-40897
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
  ┌─ pkg:pypi/urllib3@1.25.8
  │ OSGTV
  │ ✘✘✘✘✔ CVE-2020-26116         HIGH         7.2   6.4%   ·  ↳ V:OSV:PYSEC-2020-148
  │ ✔✔✔✔✔ CVE-2021-33503         HIGH         7.5   3.3%   ·  ↳ O:GHSA-q2q7-5pp4-w6pg,PYSEC-2021-108 | S:GHSA-q2q7-5pp4-w6pg,PYSEC-2021-108 | V:GHSA-Q2Q7-5PP4-W6PG
  │ ✔✔✔✔✔ CVE-2023-43804         HIGH         8.1   1.4%   ·  ↳ O:GHSA-v845-jxx5-vc9f,PYSEC-2023-192 | S:GHSA-v845-jxx5-vc9f,PYSEC-2023-192 | V:GHSA-V845-JXX5-VC9F
  │ ✔✔✔✔✔ CVE-2025-66418         HIGH         8.9   0.7%   ·  ↳ O:GHSA-gm62-xv2j-4w53,PYSEC-2026-1998 | S:GHSA-gm62-xv2j-4w53,PYSEC-2026-1998 | V:MEND:CVE-2025-66418
  │ ✔✔✔✔✔ CVE-2025-66471         HIGH         8.9   0.7%   ·  ↳ O:GHSA-2xpw-w6gg-jr37,PYSEC-2026-1994 | S:GHSA-2xpw-w6gg-jr37,PYSEC-2026-1994 | V:MEND:CVE-2025-66471
  │ ✔✔✔✔✔ CVE-2026-21441         HIGH         8.9   2.9%   ·  ↳ O:GHSA-38jv-5279-wg99,PYSEC-2026-1996 | S:GHSA-38jv-5279-wg99,PYSEC-2026-1996 | V:MEND:CVE-2026-21441
  │ ✔✔✔✔✔ CVE-2026-44431         HIGH         8.2   0.3%   ·  ↳ O:GHSA-qccp-gfcp-xxvc,PYSEC-2026-141 | S:GHSA-qccp-gfcp-xxvc,PYSEC-2026-141 | V:MEND:CVE-2026-44431
  │ ✔✔✔✔✔ CVE-2026-97689         HIGH         8.9   0.3%   ·  ↳ O:GHSA-vxq7-64xx-v4gw,PYSEC-2026-4177 | S:GHSA-vxq7-64xx-v4gw,PYSEC-2026-4177 | V:MEND:CVE-2026-97689
  │ ✔✔✔✔✔ CVE-2020-26137         MEDIUM       6.5   2.3%   ·  ↳ O:GHSA-wqvq-5m8c-6g24,PYSEC-2020-148 | S:GHSA-wqvq-5m8c-6g24,PYSEC-2020-148 | V:OSV:PYSEC-2020-148
  │ ✔✔✔✔✔ CVE-2023-45803         MEDIUM       4.2   0.6%   ·  ↳ O:GHSA-g4mx-q9vg-27p4,PYSEC-2023-212 | S:GHSA-g4mx-q9vg-27p4,PYSEC-2023-212 | V:OSV:PYSEC-2023-212
  │ ✔✔✔✔✔ CVE-2024-37891         MEDIUM       6.5   1.1%   ·  ↳ O:GHSA-34jh-p97f-mpxf,PYSEC-2026-1995 | S:GHSA-34jh-p97f-mpxf,PYSEC-2026-1995 | V:GHSA-34JH-P97F-MPXF
  │ ✔✔✔✔✔ CVE-2025-50181         MEDIUM       6.1   0.5%   ·  ↳ O:GHSA-pq67-6m6q-mj2v,PYSEC-2026-1999 | S:GHSA-pq67-6m6q-mj2v,PYSEC-2026-1999 | V:MEND:CVE-2025-50181
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/werkzeug@3.0.6
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2025-66221         MEDIUM       6.3   0.5%   ·  ↳ O:GHSA-hgf8-39gv-g3f2,PYSEC-2026-2046 | S:GHSA-hgf8-39gv-g3f2,PYSEC-2026-2046 | V:SNYK:PYTHON-WERKZEUG-15322677
  │ ✔✔✔✔✔ CVE-2026-102598        MEDIUM       6.3   0.4%   ·  ↳ O:GHSA-g6x2-hccm-hh4m,PYSEC-2026-4312 | S:GHSA-g6x2-hccm-hh4m,PYSEC-2026-4312 | V:OSV:PYSEC-2026-4312
  │ ✔✔✔✔✔ CVE-2026-21860         MEDIUM       6.3   0.5%   ·  ↳ O:GHSA-87hc-h4r5-73f7,PYSEC-2026-2044 | S:GHSA-87hc-h4r5-73f7,PYSEC-2026-2044 | V:GHSA-87HC-H4R5-73F7
  │ ✔✔✔✔✔ CVE-2026-27199         MEDIUM       6.3   0.6%   ·  ↳ O:GHSA-29vq-49wr-vm6x,PYSEC-2026-2320 | S:GHSA-29vq-49wr-vm6x,PYSEC-2026-2320 | V:GHSA-29VQ-49WR-VM6X
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:pypi/wheel@0.34.2
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2022-40898         HIGH         7.5   2.8%   ·  ↳ O:GHSA-qwmp-2cf2-g9g6,PYSEC-2022-43017 | S:GHSA-qwmp-2cf2-g9g6,PYSEC-2022-43017 | V:MEND:CVE-2022-40898
  │ ✘✘✘✘✔ CVE-2026-24049         HIGH         7.1   0.4%   ·  ↳ V:MEND:CVE-2026-24049
  └────────────────────────────────────────────────────────────────────────────────────────────────────

  ━━ Debian/Ubuntu (deb) ━━
  ┌─ pkg:deb/ubuntu/binutils@2.34-6ubuntu1.11
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ O:UBUNTU-CVE-2017-13716 | S:UBUNTU-CVE-2017-13716 | V:UB:CVE-2017-13716
  │ ✔✔✔✘✔ CVE-2025-11082         HIGH         7.8   0.3%   ·  ↳ O:UBUNTU-CVE-2025-11082 | S:UBUNTU-CVE-2025-11082 | V:UB:CVE-2025-11082
  │ ✔✔✔✘✘ CVE-2025-11083         HIGH         7.8   0.3%   ·  ↳ O:UBUNTU-CVE-2025-11083 | S:UBUNTU-CVE-2025-11083
  │ ✔✔✔✘✔ CVE-2025-5244          HIGH         7.8   0.3%   ·  ↳ O:UBUNTU-CVE-2025-5244,USN-7899-1 | S:UBUNTU-CVE-2025-5244,USN-7899-1 | V:UB:CVE-2025-5244
  │ ✔✔✔✘✔ CVE-2025-5245          HIGH         7.8   0.3%   ·  ↳ O:UBUNTU-CVE-2025-5245,USN-7899-1 | S:UBUNTU-CVE-2025-5245,USN-7899-1 | V:UB:CVE-2025-5245
  │ ✔✔✔✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2025-66862 | S:UBUNTU-CVE-2025-66862
  │ ✔✔✔✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2025-66863 | S:UBUNTU-CVE-2025-66863
  │ ✔✔✔✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-66864 | S:UBUNTU-CVE-2025-66864
  │ ✔✔✔✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2025-66865 | S:UBUNTU-CVE-2025-66865
  │ ✔✔✔✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·  ↳ O:UBUNTU-CVE-2025-66866 | S:UBUNTU-CVE-2025-66866
  │ ✔✔✔✘✔ CVE-2025-7545          HIGH         7.8   0.3%   ·  ↳ O:UBUNTU-CVE-2025-7545,USN-7899-1 | S:UBUNTU-CVE-2025-7545,USN-7899-1 | V:UB:CVE-2025-7545
  │ ✔✔✔✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·  ↳ O:UBUNTU-CVE-2026-3441 | S:UBUNTU-CVE-2026-3441
  │ ✔✔✔✘✘ CVE-2026-3442          HIGH         7.1   0.3%   ·  ↳ O:UBUNTU-CVE-2026-3442 | S:UBUNTU-CVE-2026-3442
  │ ✔✔✔✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-6846 | S:UBUNTU-CVE-2026-6846
  │ ✔✔✔✘✔ CVE-2019-1010204       MEDIUM       5.5   1.1%   ·  ↳ O:UBUNTU-CVE-2019-1010204 | S:UBUNTU-CVE-2019-1010204 | V:UB:CVE-2019-1010204
  │ ✔✔✔✘✘ CVE-2021-20197         MEDIUM       6.3   0.3%   ·  ↳ O:UBUNTU-CVE-2021-20197 | S:UBUNTU-CVE-2021-20197
  │ ✔✔✔✘✔ CVE-2022-48064         MEDIUM       5.5   0.6%   ·  ↳ O:UBUNTU-CVE-2022-48064 | S:UBUNTU-CVE-2022-48064 | V:UB:CVE-2022-48064
  │ ✔✔✔✘✔ CVE-2025-11412         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-11412 | S:UBUNTU-CVE-2025-11412 | V:UB:CVE-2025-11412
  │ ✔✔✔✘✔ CVE-2025-11413         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-11413 | S:UBUNTU-CVE-2025-11413 | V:UB:CVE-2025-11413
  │ ✔✔✔✘✔ CVE-2025-11414         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-11414 | S:UBUNTU-CVE-2025-11414 | V:UB:CVE-2025-11414
  │ ✔✔✔✘✔ CVE-2025-11494         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-11494 | S:UBUNTU-CVE-2025-11494 | V:UB:CVE-2025-11494
  │ ✔✔✔✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-11495 | S:UBUNTU-CVE-2025-11495
  │ ✔✔✘✘✘ CVE-2025-1178          MEDIUM       6.3   0.8%   ·  ↳ O:UBUNTU-CVE-2025-1178 | S:UBUNTU-CVE-2025-1178
  │ ✔✔✘✘✔ CVE-2025-1181          MEDIUM       5.1   0.7%   ·  ↳ O:UBUNTU-CVE-2025-1181,USN-7899-1 | S:UBUNTU-CVE-2025-1181,USN-7899-1 | V:UB:CVE-2025-1181
  │ ✔✔✔✘✔ CVE-2025-11839         MEDIUM       5.5   0.3%   ·  ↳ O:UBUNTU-CVE-2025-11839,USN-7899-1 | S:UBUNTU-CVE-2025-11839,USN-7899-1 | V:UB:CVE-2025-11839
  │ ✔✔✔✘✔ CVE-2025-11840         MEDIUM       5.5   0.3%   ·  ↳ O:UBUNTU-CVE-2025-11840,USN-7899-1 | S:UBUNTU-CVE-2025-11840,USN-7899-1 | V:UB:CVE-2025-11840
  │ ✔✔✔✘✔ CVE-2025-3198          MEDIUM       5.5   0.3%   ·  ↳ O:UBUNTU-CVE-2025-3198,USN-7899-1 | S:UBUNTU-CVE-2025-3198,USN-7899-1 | V:UB:CVE-2025-3198
  │ ✔✔✔✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-69645 | S:UBUNTU-CVE-2025-69645 | V:UB:CVE-2025-69645
  │ ✔✔✔✘✔ CVE-2025-69651         MEDIUM       5.5   0.3%   ·  ↳ O:UBUNTU-CVE-2025-69651 | S:UBUNTU-CVE-2025-69651 | V:UB:CVE-2025-69651
  │ ✔✔✔✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ O:UBUNTU-CVE-2025-69652 | S:UBUNTU-CVE-2025-69652 | V:UB:CVE-2025-69652
  │ ✔✔✔✘✔ CVE-2025-8225          MEDIUM       4.8   0.3%   ·  ↳ O:UBUNTU-CVE-2025-8225,USN-7899-1 | S:UBUNTU-CVE-2025-8225,USN-7899-1 | V:UB:CVE-2025-8225
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
  │ ✔✔✔✘✔ CVE-2025-1148          LOW          3.1   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1148 | S:UBUNTU-CVE-2025-1148 | V:UB:CVE-2025-1148
  │ ✔✔✔✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1149 | S:UBUNTU-CVE-2025-1149
  │ ✔✔✔✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1150 | S:UBUNTU-CVE-2025-1150
  │ ✔✔✔✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1151 | S:UBUNTU-CVE-2025-1151
  │ ✔✔✔✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1152 | S:UBUNTU-CVE-2025-1152 | V:UB:CVE-2025-1152
  │ ✔✔✔✘✔ CVE-2025-1180          LOW          3.1   0.7%   ·  ↳ O:UBUNTU-CVE-2025-1180 | S:UBUNTU-CVE-2025-1180 | V:UB:CVE-2025-1180
  │ ✔✔✔✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·  ↳ O:UBUNTU-CVE-2025-66861 | S:UBUNTU-CVE-2025-66861
  │ ✔✔✘✘✘ USN-7919-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/binutils-aarch64-linux-gnu@2.34-6ubuntu1.11
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ S:UBUNTU-CVE-2017-13716 | V:UB:CVE-2017-13716
  │ ✘✔✘✘✘ CVE-2025-11082         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11082
  │ ✘✔✘✘✘ CVE-2025-11083         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11083
  │ ✘✔✘✘✘ CVE-2025-5244          HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-5244,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-5245          HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-5245,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66862
  │ ✘✔✘✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66863
  │ ✘✔✘✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-66864
  │ ✘✔✘✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66865
  │ ✘✔✘✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-66866
  │ ✘✔✘✘✘ CVE-2025-7545          HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-7545,USN-7899-1
  │ ✘✔✘✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3441
  │ ✘✔✘✘✘ CVE-2026-3442          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-3442
  │ ✘✔✘✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6846
  │ ✘✔✘✘✔ CVE-2019-1010204       MEDIUM       5.5   1.1%   ·  ↳ S:UBUNTU-CVE-2019-1010204 | V:UB:CVE-2019-1010204
  │ ✘✔✘✘✘ CVE-2021-20197         MEDIUM       6.3   0.3%   ·  ↳ S:UBUNTU-CVE-2021-20197
  │ ✘✔✘✘✔ CVE-2022-48064         MEDIUM       5.5   0.6%   ·  ↳ S:UBUNTU-CVE-2022-48064 | V:UB:CVE-2022-48064
  │ ✘✔✘✘✘ CVE-2025-11412         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11412
  │ ✘✔✘✘✘ CVE-2025-11413         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11413
  │ ✘✔✘✘✘ CVE-2025-11414         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11414
  │ ✘✔✘✘✘ CVE-2025-11494         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11494
  │ ✘✔✘✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11495
  │ ✘✔✘✘✘ CVE-2025-1178          MEDIUM       6.3   0.8%   ·  ↳ S:UBUNTU-CVE-2025-1178
  │ ✘✔✘✘✘ CVE-2025-1181          MEDIUM       5.1   0.7%   ·  ↳ S:UBUNTU-CVE-2025-1181,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-11839         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11839,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-11840         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11840,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-3198          MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-3198,USN-7899-1
  │ ✘✔✘✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69645 | V:UB:CVE-2025-69645
  │ ✘✔✘✘✔ CVE-2025-69651         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-69651 | V:UB:CVE-2025-69651
  │ ✘✔✘✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69652 | V:UB:CVE-2025-69652
  │ ✘✔✘✘✘ CVE-2025-8225          MEDIUM       4.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-8225,USN-7899-1
  │ ✘✔✘✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15003
  │ ✘✔✘✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19548
  │ ✘✔✘✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-4647
  │ ✘✔✘✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6844
  │ ✘✔✘✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6845
  │ ✘✔✘✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90801
  │ ✘✔✘✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90802
  │ ✘✔✘✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90803
  │ ✘✔✘✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90804
  │ ✘✔✘✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90828
  │ ✘✔✘✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90829
  │ ✘✔✘✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90830
  │ ✘✔✘✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90831
  │ ✘✔✘✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91779
  │ ✘✔✘✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91780
  │ ✘✔✘✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91781
  │ ✘✔✘✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91782
  │ ✘✔✘✘✔ CVE-2025-1148          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1148 | V:UB:CVE-2025-1148
  │ ✘✔✘✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1149
  │ ✘✔✘✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1150
  │ ✘✔✘✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1151
  │ ✘✔✘✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1152 | V:UB:CVE-2025-1152
  │ ✘✔✘✘✔ CVE-2025-1180          LOW          3.1   0.7%   ·  ↳ S:UBUNTU-CVE-2025-1180 | V:UB:CVE-2025-1180
  │ ✘✔✘✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-66861
  │ ✘✔✘✘✘ USN-7919-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/binutils-common@2.34-6ubuntu1.11
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ S:UBUNTU-CVE-2017-13716 | V:UB:CVE-2017-13716
  │ ✘✔✘✘✘ CVE-2025-11082         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11082
  │ ✘✔✘✘✘ CVE-2025-11083         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11083
  │ ✘✔✘✘✘ CVE-2025-5244          HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-5244,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-5245          HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-5245,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66862
  │ ✘✔✘✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66863
  │ ✘✔✘✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-66864
  │ ✘✔✘✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66865
  │ ✘✔✘✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-66866
  │ ✘✔✘✘✘ CVE-2025-7545          HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-7545,USN-7899-1
  │ ✘✔✘✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3441
  │ ✘✔✘✘✘ CVE-2026-3442          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-3442
  │ ✘✔✘✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6846
  │ ✘✔✘✘✔ CVE-2019-1010204       MEDIUM       5.5   1.1%   ·  ↳ S:UBUNTU-CVE-2019-1010204 | V:UB:CVE-2019-1010204
  │ ✘✔✘✘✘ CVE-2021-20197         MEDIUM       6.3   0.3%   ·  ↳ S:UBUNTU-CVE-2021-20197
  │ ✘✔✘✘✔ CVE-2022-48064         MEDIUM       5.5   0.6%   ·  ↳ S:UBUNTU-CVE-2022-48064 | V:UB:CVE-2022-48064
  │ ✘✔✘✘✘ CVE-2025-11412         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11412
  │ ✘✔✘✘✘ CVE-2025-11413         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11413
  │ ✘✔✘✘✘ CVE-2025-11414         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11414
  │ ✘✔✘✘✘ CVE-2025-11494         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11494
  │ ✘✔✘✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11495
  │ ✘✔✘✘✘ CVE-2025-1178          MEDIUM       6.3   0.8%   ·  ↳ S:UBUNTU-CVE-2025-1178
  │ ✘✔✘✘✘ CVE-2025-1181          MEDIUM       5.1   0.7%   ·  ↳ S:UBUNTU-CVE-2025-1181,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-11839         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11839,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-11840         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11840,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-3198          MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-3198,USN-7899-1
  │ ✘✔✘✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69645 | V:UB:CVE-2025-69645
  │ ✘✔✘✘✔ CVE-2025-69651         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-69651 | V:UB:CVE-2025-69651
  │ ✘✔✘✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69652 | V:UB:CVE-2025-69652
  │ ✘✔✘✘✘ CVE-2025-8225          MEDIUM       4.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-8225,USN-7899-1
  │ ✘✔✘✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15003
  │ ✘✔✘✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19548
  │ ✘✔✘✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-4647
  │ ✘✔✘✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6844
  │ ✘✔✘✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6845
  │ ✘✔✘✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90801
  │ ✘✔✘✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90802
  │ ✘✔✘✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90803
  │ ✘✔✘✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90804
  │ ✘✔✘✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90828
  │ ✘✔✘✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90829
  │ ✘✔✘✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90830
  │ ✘✔✘✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90831
  │ ✘✔✘✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91779
  │ ✘✔✘✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91780
  │ ✘✔✘✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91781
  │ ✘✔✘✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91782
  │ ✘✔✘✘✔ CVE-2025-1148          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1148 | V:UB:CVE-2025-1148
  │ ✘✔✘✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1149
  │ ✘✔✘✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1150
  │ ✘✔✘✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1151
  │ ✘✔✘✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1152 | V:UB:CVE-2025-1152
  │ ✘✔✘✘✔ CVE-2025-1180          LOW          3.1   0.7%   ·  ↳ S:UBUNTU-CVE-2025-1180 | V:UB:CVE-2025-1180
  │ ✘✔✘✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-66861
  │ ✘✔✘✘✘ USN-7919-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/bsdutils@1%3A2.34-0.1ubuntu9.6
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-53613         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53613
  │ ✘✔✘✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53615
  │ ✘✔✘✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-76642
  │ ✘✔✘✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78408
  │ ✘✔✘✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78409
  │ ✘✔✘✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78410
  │ ✘✔✘✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-14104
  │ ✘✔✘✘✘ CVE-2026-13595         MEDIUM       6.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-13595
  │ ✘✔✘✘✔ CVE-2026-27456         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-27456 | V:UB:CVE-2026-27456
  │ ✘✔✘✘✘ USN-8091-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/bzip2@1.0.8-2
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2026-42250         MEDIUM       4.8   0.1%   ·  ↳ O:UBUNTU-CVE-2026-42250,USN-8685-1 | S:UBUNTU-CVE-2026-42250,USN-8685-1 | V:UB:CVE-2026-42250
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/ca-certificates@20240203~20.04.1
  │ OSGTV
  │ ✔✔✘✘✘ USN-8944-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/coreutils@8.30-3ubuntu2
  │ OSGTV
  │ ✔✔✔✘✘ CVE-2016-2781          MEDIUM       6.5   0.4%   ·  ↳ O:UBUNTU-CVE-2016-2781 | S:UBUNTU-CVE-2016-2781
  │ ✔✔✔✘✘ CVE-2025-5278          MEDIUM       4.4   0.3%   ·  ↳ O:UBUNTU-CVE-2025-5278 | S:UBUNTU-CVE-2025-5278
  │ ✘✘✔✘✘ CVE-2026-56392         MEDIUM       6.1   0.1%   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/cpp@4%3A9.3.0-1ubuntu2
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2020-23026         HIGH         7.5   1.1%   ·  ↳ S:UBUNTU-CVE-2020-23026
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/cpp-9@9.4.0-1ubuntu1~20.04.2
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2020-23026         HIGH         7.5   1.1%   ·  ↳ S:UBUNTU-CVE-2020-23026
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ S:UBUNTU-CVE-2023-4039 | V:UB:CVE-2023-4039
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/curl@7.68.0-1ubuntu2.25
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2026-11856         CRITICAL     9.8   0.7%   ·  ↳ O:UBUNTU-CVE-2026-11856 | S:UBUNTU-CVE-2026-11856 | V:UB:CVE-2026-11856
  │ ✔✔✔✘✔ CVE-2026-18924         CRITICAL     9.1   0.6%   ·  ↳ O:UBUNTU-CVE-2026-18924,USN-8820-1 | S:UBUNTU-CVE-2026-18924,USN-8820-1 | V:UB:CVE-2026-18924
  │ ✔✔✔✘✔ CVE-2026-86414         CRITICAL     9.1   0.7%   ·  ↳ O:UBUNTU-CVE-2026-86414,USN-8932-1 | S:UBUNTU-CVE-2026-86414,USN-8932-1 | V:UB:CVE-2026-86414
  │ ✔✔✔✘✔ CVE-2026-8924          CRITICAL     9.1   0.7%   ·  ↳ O:UBUNTU-CVE-2026-8924 | S:UBUNTU-CVE-2026-8924 | V:UB:CVE-2026-8924
  │ ✔✔✔✘✔ CVE-2026-8927          CRITICAL     9.1   0.5%   ·  ↳ O:UBUNTU-CVE-2026-8927,USN-8820-1 | S:UBUNTU-CVE-2026-8927,USN-8820-1 | V:UB:CVE-2026-8927
  │ ✔✔✔✘✔ CVE-2026-92388         CRITICAL     9.1   0.7%   ·  ↳ O:UBUNTU-CVE-2026-92388,USN-8932-1 | S:UBUNTU-CVE-2026-92388,USN-8932-1 | V:UB:CVE-2026-92388
  │ ✔✔✔✘✔ CVE-2026-5773          HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-5773 | S:UBUNTU-CVE-2026-5773 | V:UB:CVE-2026-5773
  │ ✔✔✔✘✔ CVE-2026-80230         HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-80230,USN-8820-1 | S:UBUNTU-CVE-2026-80230,USN-8820-1 | V:UB:CVE-2026-80230
  │ ✔✔✔✘✔ CVE-2026-82209         HIGH         8.2   0.4%   ·  ↳ O:UBUNTU-CVE-2026-82209,USN-8820-1 | S:UBUNTU-CVE-2026-82209,USN-8820-1 | V:UB:CVE-2026-82209
  │ ✔✔✔✘✔ CVE-2026-8286          HIGH         8.1   0.3%   ·  ↳ O:UBUNTU-CVE-2026-8286 | S:UBUNTU-CVE-2026-8286 | V:UB:CVE-2026-8286
  │ ✔✔✔✘✔ CVE-2026-87864         HIGH         8.1   0.8%   ·  ↳ O:UBUNTU-CVE-2026-87864,USN-8932-1 | S:UBUNTU-CVE-2026-87864,USN-8932-1 | V:UB:CVE-2026-87864
  │ ✔✔✔✘✔ CVE-2026-8932          HIGH         7.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-8932,USN-8670-2 | S:UBUNTU-CVE-2026-8932,USN-8670-2 | V:UB:CVE-2026-8932
  │ ✔✔✔✘✔ CVE-2026-92389         HIGH         8.1   0.7%   ·  ↳ O:UBUNTU-CVE-2026-92389,USN-8932-1 | S:UBUNTU-CVE-2026-92389,USN-8932-1 | V:UB:CVE-2026-92389
  │ ✔✔✔✘✘ CVE-2026-92390         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-92390 | S:UBUNTU-CVE-2026-92390
  │ ✔✔✔✘✔ CVE-2026-92391         HIGH         7.5   1.2%   ·  ↳ O:UBUNTU-CVE-2026-92391,USN-8932-1 | S:UBUNTU-CVE-2026-92391,USN-8932-1 | V:UB:CVE-2026-92391
  │ ✔✔✔✘✔ CVE-2026-94266         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-94266,USN-8932-1 | S:UBUNTU-CVE-2026-94266,USN-8932-1 | V:UB:CVE-2026-94266
  │ ✔✔✔✘✔ CVE-2025-14017         MEDIUM       6.3   0.1%   ·  ↳ O:UBUNTU-CVE-2025-14017 | S:UBUNTU-CVE-2025-14017 | V:UB:CVE-2025-14017
  │ ✔✔✔✘✘ CVE-2025-14524         MEDIUM       5.3   0.7%   ·  ↳ O:UBUNTU-CVE-2025-14524 | S:UBUNTU-CVE-2025-14524
  │ ✔✔✔✘✔ CVE-2025-15079         MEDIUM       5.3   0.5%   ·  ↳ O:UBUNTU-CVE-2025-15079 | S:UBUNTU-CVE-2025-15079 | V:UB:CVE-2025-15079
  │ ✔✔✔✘✔ CVE-2026-1965          MEDIUM       6.5   0.3%   ·  ↳ O:UBUNTU-CVE-2026-1965,USN-8099-1 | S:UBUNTU-CVE-2026-1965,USN-8099-1 | V:UB:CVE-2026-1965
  │ ✔✔✔✘✔ CVE-2026-3783          MEDIUM       5.3   0.5%   ·  ↳ O:UBUNTU-CVE-2026-3783,USN-8099-1 | S:UBUNTU-CVE-2026-3783,USN-8099-1 | V:UB:CVE-2026-3783
  │ ✔✔✔✘✔ CVE-2026-3784          MEDIUM       6.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-3784,USN-8099-1 | S:UBUNTU-CVE-2026-3784,USN-8099-1 | V:UB:CVE-2026-3784
  │ ✔✔✔✘✘ CVE-2026-4873          MEDIUM       5.9   0.3%   ·  ↳ O:UBUNTU-CVE-2026-4873 | S:UBUNTU-CVE-2026-4873
  │ ✔✔✔✘✔ CVE-2026-5545          MEDIUM       6.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-5545 | S:UBUNTU-CVE-2026-5545 | V:UB:CVE-2026-5545
  │ ✔✔✔✘✘ CVE-2026-6253          MEDIUM       5.9   0.7%   ·  ↳ O:UBUNTU-CVE-2026-6253 | S:UBUNTU-CVE-2026-6253
  │ ✔✔✔✘✘ CVE-2026-6429          MEDIUM       5.3   0.5%   ·  ↳ O:UBUNTU-CVE-2026-6429 | S:UBUNTU-CVE-2026-6429
  │ ✔✔✔✘✔ CVE-2026-7168          MEDIUM       5.3   0.5%   ·  ↳ O:UBUNTU-CVE-2026-7168 | S:UBUNTU-CVE-2026-7168 | V:UB:CVE-2026-7168
  │ ✔✔✔✘✔ CVE-2026-8458          MEDIUM       6.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-8458 | S:UBUNTU-CVE-2026-8458 | V:UB:CVE-2026-8458
  │ ✔✔✔✘✔ CVE-2025-15224         LOW          3.1   0.5%   ·  ↳ O:UBUNTU-CVE-2025-15224 | S:UBUNTU-CVE-2025-15224 | V:UB:CVE-2025-15224
  │ ✔✔✘✘✘ USN-8062-2             ?             -       -   ·
  │ ✔✔✘✘✘ USN-8487-1             ?             -       -   ·
  │ ✔✔✘✘✘ USN-8525-1             ?             -       -   ·
  │ ✔✔✘✘✘ USN-8651-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dash@0.5.10.2-6
  │ OSGTV
  │ ✘✘✔✘✘ CVE-2026-91187         CRITICAL     9.3   0.3%   ·
  │ ✔✔✔✘✔ CVE-2026-102473        MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-102473 | S:UBUNTU-CVE-2026-102473 | V:UB:CVE-2026-102473
  │ ✔✔✔✘✔ CVE-2026-102474        MEDIUM       4.0   0.1%   ·  ↳ O:UBUNTU-CVE-2026-102474 | S:UBUNTU-CVE-2026-102474 | V:UB:CVE-2026-102474
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dbus@1.12.16-2ubuntu2.3
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2023-34969         MEDIUM       6.5   1.5%   ·  ↳ O:UBUNTU-CVE-2023-34969 | S:UBUNTU-CVE-2023-34969 | V:UB:CVE-2023-34969
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dbus-user-session@1.12.16-2ubuntu2.3
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2023-34969         MEDIUM       6.5   1.5%   ·  ↳ S:UBUNTU-CVE-2023-34969 | V:UB:CVE-2023-34969
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/diffutils@1%3A3.7-3
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2026-53910         LOW          2.1   0.3%   ·  ↳ O:UBUNTU-CVE-2026-53910,USN-8692-1 | S:UBUNTU-CVE-2026-53910,USN-8692-1 | V:UB:CVE-2026-53910
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dirmngr@2.2.19-3ubuntu2.5
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68973
  │ ✘✔✘✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✘✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✘✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  │ ✘✔✘✘✘ USN-7946-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dmsetup@2%3A1.02.167-1ubuntu1
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2026-19617         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19617 | V:UB:CVE-2026-19617
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dpkg@1.19.7ubuntu3.2
  │ OSGTV
  │ ✔✔✔✘✘ CVE-2025-6297          HIGH         8.2   0.5%   ·  ↳ O:UBUNTU-CVE-2025-6297 | S:UBUNTU-CVE-2025-6297
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/dpkg-dev@1.19.7ubuntu3.2
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-6297          HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2025-6297
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/fdisk@2.34-0.1ubuntu9.6
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-53613         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53613
  │ ✘✔✘✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53615
  │ ✘✔✘✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-76642
  │ ✘✔✘✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78408
  │ ✘✔✘✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78409
  │ ✘✔✘✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78410
  │ ✘✔✘✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-14104
  │ ✘✔✘✘✘ CVE-2026-13595         MEDIUM       6.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-13595
  │ ✘✔✘✘✔ CVE-2026-27456         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-27456 | V:UB:CVE-2026-27456
  │ ✘✔✘✘✘ USN-8091-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/g%2B%2B@4%3A9.3.0-1ubuntu2
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2020-23026         HIGH         7.5   1.1%   ·  ↳ S:UBUNTU-CVE-2020-23026
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/g%2B%2B-9@9.4.0-1ubuntu1~20.04.2
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2020-23026         HIGH         7.5   1.1%   ·  ↳ S:UBUNTU-CVE-2020-23026
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ S:UBUNTU-CVE-2023-4039 | V:UB:CVE-2023-4039
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc@4%3A9.3.0-1ubuntu2
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2020-23026         HIGH         7.5   1.1%   ·  ↳ S:UBUNTU-CVE-2020-23026
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc-10-base@10.5.0-1ubuntu1~20.04
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ S:UBUNTU-CVE-2023-4039,USN-7700-1 | V:UB:CVE-2023-4039
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc-9@9.4.0-1ubuntu1~20.04.2
  │ OSGTV
  │ ✔✔✔✘✘ CVE-2020-23026         HIGH         7.5   1.1%   ·  ↳ O:UBUNTU-CVE-2020-23026 | S:UBUNTU-CVE-2020-23026
  │ ✔✔✔✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ O:UBUNTU-CVE-2026-102010 | S:UBUNTU-CVE-2026-102010
  │ ✔✔✔✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ O:UBUNTU-CVE-2026-95619 | S:UBUNTU-CVE-2026-95619
  │ ✔✔✔✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ O:UBUNTU-CVE-2023-4039 | S:UBUNTU-CVE-2023-4039 | V:UB:CVE-2023-4039
  │ ✔✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ O:UBUNTU-CVE-2026-114690 | S:UBUNTU-CVE-2026-114690
  │ ✔✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ O:UBUNTU-CVE-2026-114691 | S:UBUNTU-CVE-2026-114691
  │ ✔✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ O:UBUNTU-CVE-2026-115455 | S:UBUNTU-CVE-2026-115455
  │ ✔✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ O:UBUNTU-CVE-2026-115456 | S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gcc-9-base@9.4.0-1ubuntu1~20.04.2
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2020-23026         HIGH         7.5   1.1%   ·  ↳ S:UBUNTU-CVE-2020-23026
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ S:UBUNTU-CVE-2023-4039 | V:UB:CVE-2023-4039
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gir1.2-packagekitglib-1.0@1.1.13-2ubuntu1.1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-41651         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-41651
  │ ✘✔✘✘✘ CVE-2026-10294         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-10294
  │ ✘✔✘✘✔ CVE-2022-0987          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-0987 | V:UB:CVE-2022-0987
  │ ✘✔✘✘✔ CVE-2024-0217          LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2024-0217 | V:UB:CVE-2024-0217
  │ ✘✔✘✘✘ USN-8195-3             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/glib-networking@2.64.2-1ubuntu0.1
  │ OSGTV
  │ ✔✔✘✘✘ CVE-2026-103963        HIGH         7.5   0.3%   ·  ↳ O:UBUNTU-CVE-2026-103963 | S:UBUNTU-CVE-2026-103963
  │ ✔✔✔✘✔ CVE-2026-10028         MEDIUM       4.3   0.2%   ·  ↳ O:UBUNTU-CVE-2026-10028 | S:UBUNTU-CVE-2026-10028 | V:UB:CVE-2026-10028
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/glib-networking-common@2.64.2-1ubuntu0.1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-103963        HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-103963
  │ ✘✔✘✘✔ CVE-2026-10028         MEDIUM       4.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-10028 | V:UB:CVE-2026-10028
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/glib-networking-services@2.64.2-1ubuntu0.1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-103963        HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-103963
  │ ✘✔✘✘✔ CVE-2026-10028         MEDIUM       4.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-10028 | V:UB:CVE-2026-10028
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gnupg@2.2.19-3ubuntu2.5
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2025-68973         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68973 | V:UB:CVE-2025-68973
  │ ✘✔✘✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✘✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✘✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  │ ✘✔✘✘✘ USN-7946-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gnupg-l10n@2.2.19-3ubuntu2.5
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68973
  │ ✘✔✘✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✘✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✘✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  │ ✘✔✘✘✘ USN-7946-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gnupg-utils@2.2.19-3ubuntu2.5
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68973
  │ ✘✔✘✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✘✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✘✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  │ ✘✔✘✘✘ USN-7946-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg@2.2.19-3ubuntu2.5
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2025-68973         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68973 | V:UB:CVE-2025-68973
  │ ✘✔✘✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✘✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✘✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  │ ✘✔✘✘✘ USN-7946-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg-agent@2.2.19-3ubuntu2.5
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68973
  │ ✘✔✘✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✘✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✘✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  │ ✘✔✘✘✘ USN-7946-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg-wks-client@2.2.19-3ubuntu2.5
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68973
  │ ✘✔✘✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✘✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✘✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  │ ✘✔✘✘✘ USN-7946-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpg-wks-server@2.2.19-3ubuntu2.5
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68973
  │ ✘✔✘✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✘✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✘✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  │ ✘✔✘✘✘ USN-7946-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpgconf@2.2.19-3ubuntu2.5
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68973
  │ ✘✔✘✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✘✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✘✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  │ ✘✔✘✘✘ USN-7946-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpgsm@2.2.19-3ubuntu2.5
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68973
  │ ✘✔✘✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✘✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✘✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  │ ✘✔✘✘✘ USN-7946-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gpgv@2.2.19-3ubuntu2.5
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-68973         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68973
  │ ✘✔✘✘✘ CVE-2022-3219          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-3219
  │ ✘✔✘✘✘ CVE-2026-105712        LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-105712
  │ ✘✔✘✘✘ CVE-2026-118131        ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-118131
  │ ✘✔✘✘✘ USN-7946-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/gzip@1.10-0ubuntu4.1
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2026-41992         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-41992,USN-8733-2 | S:UBUNTU-CVE-2026-41992,USN-8733-2 | V:UB:CVE-2026-41992
  │ ✔✔✔✘✔ CVE-2026-41991         MEDIUM       4.7   0.1%   ·  ↳ O:UBUNTU-CVE-2026-41991,USN-8733-2 | S:UBUNTU-CVE-2026-41991,USN-8733-2 | V:UB:CVE-2026-41991
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/krb5-locales@1.17-6ubuntu4.11
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2018-5709          HIGH         7.5   2.0%   ·  ↳ S:UBUNTU-CVE-2018-5709
  │ ✘✔✘✘✘ CVE-2026-107778        HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-107778
  │ ✘✔✘✘✘ CVE-2026-107708        MEDIUM       6.9   0.5%   ·  ↳ S:UBUNTU-CVE-2026-107708
  │ ✘✔✘✘✘ CVE-2026-11850         MEDIUM       5.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-11850
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libacl1@2.2.53-6
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-54369         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-54369
  │ ✘✔✘✘✘ CVE-2026-54370         HIGH         7.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-54370
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libasan5@9.4.0-1ubuntu1~20.04.2
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2020-23026         HIGH         7.5   1.1%   ·  ↳ S:UBUNTU-CVE-2020-23026
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ S:UBUNTU-CVE-2023-4039 | V:UB:CVE-2023-4039
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libatomic1@10.5.0-1ubuntu1~20.04
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ S:UBUNTU-CVE-2023-4039,USN-7700-1 | V:UB:CVE-2023-4039
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libattr1@1%3A2.4.48-5
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2026-54371         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-54371,USN-8691-1 | V:UB:CVE-2026-54371
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libbinutils@2.34-6ubuntu1.11
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ S:UBUNTU-CVE-2017-13716 | V:UB:CVE-2017-13716
  │ ✘✔✘✘✘ CVE-2025-11082         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11082
  │ ✘✔✘✘✘ CVE-2025-11083         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11083
  │ ✘✔✘✘✘ CVE-2025-5244          HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-5244,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-5245          HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-5245,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66862
  │ ✘✔✘✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66863
  │ ✘✔✘✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-66864
  │ ✘✔✘✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66865
  │ ✘✔✘✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-66866
  │ ✘✔✘✘✘ CVE-2025-7545          HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-7545,USN-7899-1
  │ ✘✔✘✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3441
  │ ✘✔✘✘✘ CVE-2026-3442          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-3442
  │ ✘✔✘✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6846
  │ ✘✔✘✘✔ CVE-2019-1010204       MEDIUM       5.5   1.1%   ·  ↳ S:UBUNTU-CVE-2019-1010204 | V:UB:CVE-2019-1010204
  │ ✘✔✘✘✘ CVE-2021-20197         MEDIUM       6.3   0.3%   ·  ↳ S:UBUNTU-CVE-2021-20197
  │ ✘✔✘✘✔ CVE-2022-48064         MEDIUM       5.5   0.6%   ·  ↳ S:UBUNTU-CVE-2022-48064 | V:UB:CVE-2022-48064
  │ ✘✔✘✘✘ CVE-2025-11412         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11412
  │ ✘✔✘✘✘ CVE-2025-11413         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11413
  │ ✘✔✘✘✘ CVE-2025-11414         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11414
  │ ✘✔✘✘✘ CVE-2025-11494         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11494
  │ ✘✔✘✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11495
  │ ✘✔✘✘✘ CVE-2025-1178          MEDIUM       6.3   0.8%   ·  ↳ S:UBUNTU-CVE-2025-1178
  │ ✘✔✘✘✘ CVE-2025-1181          MEDIUM       5.1   0.7%   ·  ↳ S:UBUNTU-CVE-2025-1181,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-11839         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11839,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-11840         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11840,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-3198          MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-3198,USN-7899-1
  │ ✘✔✘✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69645 | V:UB:CVE-2025-69645
  │ ✘✔✘✘✔ CVE-2025-69651         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-69651 | V:UB:CVE-2025-69651
  │ ✘✔✘✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69652 | V:UB:CVE-2025-69652
  │ ✘✔✘✘✘ CVE-2025-8225          MEDIUM       4.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-8225,USN-7899-1
  │ ✘✔✘✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15003
  │ ✘✔✘✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19548
  │ ✘✔✘✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-4647
  │ ✘✔✘✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6844
  │ ✘✔✘✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6845
  │ ✘✔✘✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90801
  │ ✘✔✘✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90802
  │ ✘✔✘✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90803
  │ ✘✔✘✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90804
  │ ✘✔✘✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90828
  │ ✘✔✘✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90829
  │ ✘✔✘✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90830
  │ ✘✔✘✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90831
  │ ✘✔✘✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91779
  │ ✘✔✘✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91780
  │ ✘✔✘✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91781
  │ ✘✔✘✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91782
  │ ✘✔✘✘✔ CVE-2025-1148          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1148 | V:UB:CVE-2025-1148
  │ ✘✔✘✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1149
  │ ✘✔✘✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1150
  │ ✘✔✘✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1151
  │ ✘✔✘✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1152 | V:UB:CVE-2025-1152
  │ ✘✔✘✘✔ CVE-2025-1180          LOW          3.1   0.7%   ·  ↳ S:UBUNTU-CVE-2025-1180 | V:UB:CVE-2025-1180
  │ ✘✔✘✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-66861
  │ ✘✔✘✘✘ USN-7919-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libblkid1@2.34-0.1ubuntu9.6
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-53613         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53613
  │ ✘✔✘✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53615
  │ ✘✔✘✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-76642
  │ ✘✔✘✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78408
  │ ✘✔✘✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78409
  │ ✘✔✘✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78410
  │ ✘✔✘✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-14104
  │ ✘✔✘✘✘ CVE-2026-13595         MEDIUM       6.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-13595
  │ ✘✔✘✘✔ CVE-2026-27456         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-27456 | V:UB:CVE-2026-27456
  │ ✘✔✘✘✘ USN-8091-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libbrotli1@1.0.7-6ubuntu0.1
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2026-111497        CRITICAL     9.8  82.6% KEV  ↳ S:UBUNTU-CVE-2026-111497,USN-8956-2 | V:UB:CVE-2026-111497
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libbz2-1.0@1.0.8-2
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-42250         MEDIUM       4.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-42250,USN-8685-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc-bin@2.31-0ubuntu9.17
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2019-1010022       CRITICAL     9.8   3.2%   ·  ↳ S:UBUNTU-CVE-2019-1010022
  │ ✘✔✘✘✘ CVE-2021-33574         CRITICAL     9.8   3.5%   ·  ↳ S:UBUNTU-CVE-2021-33574
  │ ✘✔✘✘✘ CVE-2026-5450          CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-5450
  │ ✘✔✘✘✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6791
  │ ✘✔✘✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·  ↳ S:UBUNTU-CVE-2016-20013
  │ ✘✔✘✘✘ CVE-2018-20796         HIGH         7.5   5.8%   ·  ↳ S:UBUNTU-CVE-2018-20796
  │ ✘✔✘✘✘ CVE-2019-1010023       HIGH         8.8   3.1%   ·  ↳ S:UBUNTU-CVE-2019-1010023
  │ ✘✔✘✘✘ CVE-2025-15281         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2025-15281
  │ ✘✔✘✔✘ CVE-2025-4802          HIGH         7.8   0.6%   ·  ↳ S:UBUNTU-CVE-2025-4802,USN-7541-1
  │ ✘✔✘✘✘ CVE-2026-0861          HIGH         8.4   0.4%   ·  ↳ S:UBUNTU-CVE-2026-0861
  │ ✘✔✘✘✘ CVE-2026-0915          HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-0915
  │ ✘✔✘✘✔ CVE-2026-4046          HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-4046 | V:UB:CVE-2026-4046
  │ ✘✔✘✘✔ CVE-2026-5435          HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-5435 | V:UB:CVE-2026-5435
  │ ✘✔✘✘✘ CVE-2026-5928          HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-5928
  │ ✘✔✘✘✘ CVE-2019-1010024       MEDIUM       5.3   3.2%   ·  ↳ S:UBUNTU-CVE-2019-1010024
  │ ✘✔✘✘✘ CVE-2025-8058          MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2025-8058
  │ ✘✔✘✘✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18374 | V:UB:CVE-2026-18374
  │ ✘✔✘✘✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19542
  │ ✘✔✘✘✔ CVE-2026-6238          MEDIUM       6.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-6238 | V:UB:CVE-2026-6238
  │ ✘✔✘✘✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-77117
  │ ✘✔✘✘✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80489
  │ ✘✔✘✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-8674
  │ ✘✔✘✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-86805
  │ ✘✔✘✘✔ CVE-2026-89092         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89092 | V:UB:CVE-2026-89092
  │ ✘✔✘✘✘ CVE-2026-6368          LOW          2.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6368
  │ ✘✔✘✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-95818
  │ ✘✔✘✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97399
  │ ✘✔✘✘✘ USN-8005-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc-dev-bin@2.31-0ubuntu9.18
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2019-1010022       CRITICAL     9.8   3.2%   ·  ↳ S:UBUNTU-CVE-2019-1010022
  │ ✘✔✘✘✘ CVE-2021-33574         CRITICAL     9.8   3.5%   ·  ↳ S:UBUNTU-CVE-2021-33574
  │ ✘✔✘✘✘ CVE-2026-5450          CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-5450
  │ ✘✔✘✘✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6791
  │ ✘✔✘✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·  ↳ S:UBUNTU-CVE-2016-20013
  │ ✘✔✘✘✘ CVE-2018-20796         HIGH         7.5   5.8%   ·  ↳ S:UBUNTU-CVE-2018-20796
  │ ✘✔✘✘✘ CVE-2019-1010023       HIGH         8.8   3.1%   ·  ↳ S:UBUNTU-CVE-2019-1010023
  │ ✘✔✘✘✘ CVE-2025-15281         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2025-15281
  │ ✘✔✘✘✘ CVE-2026-0861          HIGH         8.4   0.4%   ·  ↳ S:UBUNTU-CVE-2026-0861
  │ ✘✔✘✘✘ CVE-2026-0915          HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-0915
  │ ✘✔✘✘✔ CVE-2026-4046          HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-4046 | V:UB:CVE-2026-4046
  │ ✘✔✘✘✔ CVE-2026-5435          HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-5435 | V:UB:CVE-2026-5435
  │ ✘✔✘✘✘ CVE-2026-5928          HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-5928
  │ ✘✔✘✘✘ CVE-2019-1010024       MEDIUM       5.3   3.2%   ·  ↳ S:UBUNTU-CVE-2019-1010024
  │ ✘✔✘✘✘ CVE-2025-8058          MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2025-8058
  │ ✘✔✘✘✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18374 | V:UB:CVE-2026-18374
  │ ✘✔✘✘✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19542
  │ ✘✔✘✘✔ CVE-2026-6238          MEDIUM       6.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-6238 | V:UB:CVE-2026-6238
  │ ✘✔✘✘✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-77117
  │ ✘✔✘✘✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80489
  │ ✘✔✘✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-8674
  │ ✘✔✘✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-86805
  │ ✘✔✘✘✔ CVE-2026-89092         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89092 | V:UB:CVE-2026-89092
  │ ✘✔✘✘✘ CVE-2026-6368          LOW          2.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6368
  │ ✘✔✘✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-95818
  │ ✘✔✘✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97399
  │ ✘✔✘✘✘ USN-8005-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc6@2.31-0ubuntu9.18
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2019-1010022       CRITICAL     9.8   3.2%   ·  ↳ S:UBUNTU-CVE-2019-1010022
  │ ✘✔✘✘✘ CVE-2021-33574         CRITICAL     9.8   3.5%   ·  ↳ S:UBUNTU-CVE-2021-33574
  │ ✘✔✘✘✘ CVE-2026-5450          CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-5450
  │ ✘✔✘✘✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6791
  │ ✘✔✘✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·  ↳ S:UBUNTU-CVE-2016-20013
  │ ✘✔✘✘✘ CVE-2018-20796         HIGH         7.5   5.8%   ·  ↳ S:UBUNTU-CVE-2018-20796
  │ ✘✔✘✘✘ CVE-2019-1010023       HIGH         8.8   3.1%   ·  ↳ S:UBUNTU-CVE-2019-1010023
  │ ✘✔✘✘✔ CVE-2025-15281         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2025-15281 | V:UB:CVE-2025-15281
  │ ✘✔✘✘✔ CVE-2026-0861          HIGH         8.4   0.4%   ·  ↳ S:UBUNTU-CVE-2026-0861 | V:UB:CVE-2026-0861
  │ ✘✔✘✘✔ CVE-2026-0915          HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-0915 | V:UB:CVE-2026-0915
  │ ✘✔✘✘✔ CVE-2026-4046          HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-4046 | V:UB:CVE-2026-4046
  │ ✘✔✘✘✔ CVE-2026-5435          HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-5435 | V:UB:CVE-2026-5435
  │ ✘✔✘✘✘ CVE-2026-5928          HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-5928
  │ ✘✔✘✘✘ CVE-2019-1010024       MEDIUM       5.3   3.2%   ·  ↳ S:UBUNTU-CVE-2019-1010024
  │ ✘✔✘✘✔ CVE-2025-8058          MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2025-8058 | V:UB:CVE-2025-8058
  │ ✘✔✘✘✔ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18374 | V:UB:CVE-2026-18374
  │ ✘✔✘✘✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19542
  │ ✘✔✘✘✔ CVE-2026-6238          MEDIUM       6.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-6238 | V:UB:CVE-2026-6238
  │ ✘✔✘✘✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-77117
  │ ✘✔✘✘✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80489
  │ ✘✔✘✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-8674
  │ ✘✔✘✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-86805
  │ ✘✔✘✘✔ CVE-2026-89092         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89092 | V:UB:CVE-2026-89092
  │ ✘✔✘✘✘ CVE-2026-6368          LOW          2.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6368
  │ ✘✔✘✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-95818
  │ ✘✔✘✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97399
  │ ✘✔✘✘✘ USN-8005-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libc6-dev@2.31-0ubuntu9.18
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2019-1010022       CRITICAL     9.8   3.2%   ·  ↳ S:UBUNTU-CVE-2019-1010022
  │ ✘✔✘✘✘ CVE-2021-33574         CRITICAL     9.8   3.5%   ·  ↳ S:UBUNTU-CVE-2021-33574
  │ ✘✔✘✘✘ CVE-2026-5450          CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-5450
  │ ✘✔✘✘✘ CVE-2026-6791          CRITICAL     9.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6791
  │ ✘✔✘✘✘ CVE-2016-20013         HIGH         7.5   2.2%   ·  ↳ S:UBUNTU-CVE-2016-20013
  │ ✘✔✘✘✘ CVE-2018-20796         HIGH         7.5   5.8%   ·  ↳ S:UBUNTU-CVE-2018-20796
  │ ✘✔✘✘✘ CVE-2019-1010023       HIGH         8.8   3.1%   ·  ↳ S:UBUNTU-CVE-2019-1010023
  │ ✘✔✘✘✘ CVE-2025-15281         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2025-15281
  │ ✘✔✘✘✘ CVE-2026-0861          HIGH         8.4   0.4%   ·  ↳ S:UBUNTU-CVE-2026-0861
  │ ✘✔✘✘✘ CVE-2026-0915          HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-0915
  │ ✘✔✘✘✘ CVE-2026-4046          HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-4046
  │ ✘✔✘✘✘ CVE-2026-5435          HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-5435
  │ ✘✔✘✘✘ CVE-2026-5928          HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-5928
  │ ✘✔✘✘✘ CVE-2019-1010024       MEDIUM       5.3   3.2%   ·  ↳ S:UBUNTU-CVE-2019-1010024
  │ ✘✔✘✘✘ CVE-2025-8058          MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2025-8058
  │ ✘✔✘✘✘ CVE-2026-18374         MEDIUM       4.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18374
  │ ✘✔✘✘✘ CVE-2026-19542         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19542
  │ ✘✔✘✘✘ CVE-2026-6238          MEDIUM       6.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-6238
  │ ✘✔✘✘✘ CVE-2026-77117         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-77117
  │ ✘✔✘✘✘ CVE-2026-80489         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80489
  │ ✘✔✘✘✘ CVE-2026-8674          MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-8674
  │ ✘✔✘✘✘ CVE-2026-86805         MEDIUM       6.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-86805
  │ ✘✔✘✘✘ CVE-2026-89092         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89092
  │ ✘✔✘✘✘ CVE-2026-6368          LOW          2.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6368
  │ ✘✔✘✘✘ CVE-2026-95818         LOW          3.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-95818
  │ ✘✔✘✘✘ CVE-2026-97399         LOW          3.7   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97399
  │ ✘✔✘✘✘ USN-8005-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libcap2@1%3A2.32-1ubuntu0.2
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2026-4878          HIGH         7.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-4878,USN-8193-2 | S:UBUNTU-CVE-2026-4878,USN-8193-2 | V:UB:CVE-2026-4878
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libcap2-bin@1%3A2.32-1ubuntu0.2
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2026-4878          HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-4878,USN-8193-2 | V:UB:CVE-2026-4878
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libcc1-0@10.5.0-1ubuntu1~20.04
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ S:UBUNTU-CVE-2023-4039,USN-7700-1 | V:UB:CVE-2023-4039
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libctf-nobfd0@2.34-6ubuntu1.11
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ S:UBUNTU-CVE-2017-13716 | V:UB:CVE-2017-13716
  │ ✘✔✘✘✘ CVE-2025-11082         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11082
  │ ✘✔✘✘✘ CVE-2025-11083         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11083
  │ ✘✔✘✘✘ CVE-2025-5244          HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-5244,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-5245          HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-5245,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66862
  │ ✘✔✘✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66863
  │ ✘✔✘✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-66864
  │ ✘✔✘✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66865
  │ ✘✔✘✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-66866
  │ ✘✔✘✘✘ CVE-2025-7545          HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-7545,USN-7899-1
  │ ✘✔✘✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3441
  │ ✘✔✘✘✘ CVE-2026-3442          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-3442
  │ ✘✔✘✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6846
  │ ✘✔✘✘✔ CVE-2019-1010204       MEDIUM       5.5   1.1%   ·  ↳ S:UBUNTU-CVE-2019-1010204 | V:UB:CVE-2019-1010204
  │ ✘✔✘✘✘ CVE-2021-20197         MEDIUM       6.3   0.3%   ·  ↳ S:UBUNTU-CVE-2021-20197
  │ ✘✔✘✘✔ CVE-2022-48064         MEDIUM       5.5   0.6%   ·  ↳ S:UBUNTU-CVE-2022-48064 | V:UB:CVE-2022-48064
  │ ✘✔✘✘✘ CVE-2025-11412         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11412
  │ ✘✔✘✘✘ CVE-2025-11413         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11413
  │ ✘✔✘✘✘ CVE-2025-11414         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11414
  │ ✘✔✘✘✘ CVE-2025-11494         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11494
  │ ✘✔✘✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11495
  │ ✘✔✘✘✘ CVE-2025-1178          MEDIUM       6.3   0.8%   ·  ↳ S:UBUNTU-CVE-2025-1178
  │ ✘✔✘✘✘ CVE-2025-1181          MEDIUM       5.1   0.7%   ·  ↳ S:UBUNTU-CVE-2025-1181,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-11839         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11839,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-11840         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11840,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-3198          MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-3198,USN-7899-1
  │ ✘✔✘✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69645 | V:UB:CVE-2025-69645
  │ ✘✔✘✘✔ CVE-2025-69651         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-69651 | V:UB:CVE-2025-69651
  │ ✘✔✘✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69652 | V:UB:CVE-2025-69652
  │ ✘✔✘✘✘ CVE-2025-8225          MEDIUM       4.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-8225,USN-7899-1
  │ ✘✔✘✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15003
  │ ✘✔✘✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19548
  │ ✘✔✘✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-4647
  │ ✘✔✘✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6844
  │ ✘✔✘✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6845
  │ ✘✔✘✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90801
  │ ✘✔✘✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90802
  │ ✘✔✘✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90803
  │ ✘✔✘✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90804
  │ ✘✔✘✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90828
  │ ✘✔✘✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90829
  │ ✘✔✘✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90830
  │ ✘✔✘✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90831
  │ ✘✔✘✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91779
  │ ✘✔✘✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91780
  │ ✘✔✘✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91781
  │ ✘✔✘✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91782
  │ ✘✔✘✘✔ CVE-2025-1148          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1148 | V:UB:CVE-2025-1148
  │ ✘✔✘✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1149
  │ ✘✔✘✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1150
  │ ✘✔✘✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1151
  │ ✘✔✘✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1152 | V:UB:CVE-2025-1152
  │ ✘✔✘✘✔ CVE-2025-1180          LOW          3.1   0.7%   ·  ↳ S:UBUNTU-CVE-2025-1180 | V:UB:CVE-2025-1180
  │ ✘✔✘✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-66861
  │ ✘✔✘✘✘ USN-7919-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libctf0@2.34-6ubuntu1.11
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2017-13716         HIGH         7.1   1.4%   ·  ↳ S:UBUNTU-CVE-2017-13716 | V:UB:CVE-2017-13716
  │ ✘✔✘✘✘ CVE-2025-11082         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11082
  │ ✘✔✘✘✘ CVE-2025-11083         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11083
  │ ✘✔✘✘✘ CVE-2025-5244          HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-5244,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-5245          HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-5245,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-66862         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66862
  │ ✘✔✘✘✘ CVE-2025-66863         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66863
  │ ✘✔✘✘✘ CVE-2025-66864         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-66864
  │ ✘✔✘✘✘ CVE-2025-66865         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-66865
  │ ✘✔✘✘✘ CVE-2025-66866         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-66866
  │ ✘✔✘✘✘ CVE-2025-7545          HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-7545,USN-7899-1
  │ ✘✔✘✘✘ CVE-2026-3441          HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3441
  │ ✘✔✘✘✘ CVE-2026-3442          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-3442
  │ ✘✔✘✘✘ CVE-2026-6846          HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6846
  │ ✘✔✘✘✔ CVE-2019-1010204       MEDIUM       5.5   1.1%   ·  ↳ S:UBUNTU-CVE-2019-1010204 | V:UB:CVE-2019-1010204
  │ ✘✔✘✘✘ CVE-2021-20197         MEDIUM       6.3   0.3%   ·  ↳ S:UBUNTU-CVE-2021-20197
  │ ✘✔✘✘✔ CVE-2022-48064         MEDIUM       5.5   0.6%   ·  ↳ S:UBUNTU-CVE-2022-48064 | V:UB:CVE-2022-48064
  │ ✘✔✘✘✘ CVE-2025-11412         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11412
  │ ✘✔✘✘✘ CVE-2025-11413         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11413
  │ ✘✔✘✘✘ CVE-2025-11414         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11414
  │ ✘✔✘✘✘ CVE-2025-11494         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11494
  │ ✘✔✘✘✘ CVE-2025-11495         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-11495
  │ ✘✔✘✘✘ CVE-2025-1178          MEDIUM       6.3   0.8%   ·  ↳ S:UBUNTU-CVE-2025-1178
  │ ✘✔✘✘✘ CVE-2025-1181          MEDIUM       5.1   0.7%   ·  ↳ S:UBUNTU-CVE-2025-1181,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-11839         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11839,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-11840         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-11840,USN-7899-1
  │ ✘✔✘✘✘ CVE-2025-3198          MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-3198,USN-7899-1
  │ ✘✔✘✘✔ CVE-2025-69645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69645 | V:UB:CVE-2025-69645
  │ ✘✔✘✘✔ CVE-2025-69651         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-69651 | V:UB:CVE-2025-69651
  │ ✘✔✘✘✔ CVE-2025-69652         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-69652 | V:UB:CVE-2025-69652
  │ ✘✔✘✘✘ CVE-2025-8225          MEDIUM       4.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-8225,USN-7899-1
  │ ✘✔✘✘✘ CVE-2026-15003         MEDIUM       5.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15003
  │ ✘✔✘✘✘ CVE-2026-19548         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19548
  │ ✘✔✘✘✘ CVE-2026-4647          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-4647
  │ ✘✔✘✘✘ CVE-2026-6844          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6844
  │ ✘✔✘✘✘ CVE-2026-6845          MEDIUM       5.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6845
  │ ✘✔✘✘✘ CVE-2026-90801         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90801
  │ ✘✔✘✘✘ CVE-2026-90802         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90802
  │ ✘✔✘✘✘ CVE-2026-90803         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90803
  │ ✘✔✘✘✘ CVE-2026-90804         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90804
  │ ✘✔✘✘✘ CVE-2026-90828         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90828
  │ ✘✔✘✘✘ CVE-2026-90829         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90829
  │ ✘✔✘✘✘ CVE-2026-90830         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90830
  │ ✘✔✘✘✘ CVE-2026-90831         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90831
  │ ✘✔✘✘✘ CVE-2026-91779         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91779
  │ ✘✔✘✘✘ CVE-2026-91780         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91780
  │ ✘✔✘✘✘ CVE-2026-91781         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91781
  │ ✘✔✘✘✘ CVE-2026-91782         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-91782
  │ ✘✔✘✘✔ CVE-2025-1148          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1148 | V:UB:CVE-2025-1148
  │ ✘✔✘✘✘ CVE-2025-1149          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1149
  │ ✘✔✘✘✘ CVE-2025-1150          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1150
  │ ✘✔✘✘✘ CVE-2025-1151          LOW          3.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1151
  │ ✘✔✘✘✔ CVE-2025-1152          LOW          3.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1152 | V:UB:CVE-2025-1152
  │ ✘✔✘✘✔ CVE-2025-1180          LOW          3.1   0.7%   ·  ↳ S:UBUNTU-CVE-2025-1180 | V:UB:CVE-2025-1180
  │ ✘✔✘✘✘ CVE-2025-66861         LOW          2.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-66861
  │ ✘✔✘✘✘ USN-7919-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libcurl4@7.68.0-1ubuntu2.25
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2026-11856         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-11856 | V:UB:CVE-2026-11856
  │ ✘✔✘✘✔ CVE-2026-18924         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-18924,USN-8820-1 | V:UB:CVE-2026-18924
  │ ✘✔✘✘✔ CVE-2026-86414         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-86414,USN-8932-1 | V:UB:CVE-2026-86414
  │ ✘✔✘✘✔ CVE-2026-8924          CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-8924 | V:UB:CVE-2026-8924
  │ ✘✔✘✘✔ CVE-2026-8927          CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-8927,USN-8820-1 | V:UB:CVE-2026-8927
  │ ✘✔✘✘✔ CVE-2026-92388         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-92388,USN-8932-1 | V:UB:CVE-2026-92388
  │ ✘✔✘✘✔ CVE-2026-5773          HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-5773 | V:UB:CVE-2026-5773
  │ ✘✔✘✘✔ CVE-2026-80230         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80230,USN-8820-1 | V:UB:CVE-2026-80230
  │ ✘✔✘✘✔ CVE-2026-82209         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-82209,USN-8820-1 | V:UB:CVE-2026-82209
  │ ✘✔✘✘✔ CVE-2026-8286          HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-8286 | V:UB:CVE-2026-8286
  │ ✘✔✘✘✔ CVE-2026-87864         HIGH         8.1   0.8%   ·  ↳ S:UBUNTU-CVE-2026-87864,USN-8932-1 | V:UB:CVE-2026-87864
  │ ✘✔✘✘✔ CVE-2026-8932          HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-8932,USN-8670-2 | V:UB:CVE-2026-8932
  │ ✘✔✘✘✔ CVE-2026-92389         HIGH         8.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-92389,USN-8932-1 | V:UB:CVE-2026-92389
  │ ✘✔✘✘✘ CVE-2026-92390         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-92390
  │ ✘✔✘✘✔ CVE-2026-92391         HIGH         7.5   1.2%   ·  ↳ S:UBUNTU-CVE-2026-92391,USN-8932-1 | V:UB:CVE-2026-92391
  │ ✘✔✘✘✔ CVE-2026-94266         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-94266,USN-8932-1 | V:UB:CVE-2026-94266
  │ ✘✔✘✘✔ CVE-2025-14017         MEDIUM       6.3   0.1%   ·  ↳ S:UBUNTU-CVE-2025-14017 | V:UB:CVE-2025-14017
  │ ✘✔✘✘✘ CVE-2025-14524         MEDIUM       5.3   0.7%   ·  ↳ S:UBUNTU-CVE-2025-14524
  │ ✘✔✘✘✔ CVE-2025-15079         MEDIUM       5.3   0.5%   ·  ↳ S:UBUNTU-CVE-2025-15079 | V:UB:CVE-2025-15079
  │ ✘✔✘✘✔ CVE-2026-1965          MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-1965,USN-8099-1 | V:UB:CVE-2026-1965
  │ ✘✔✘✘✔ CVE-2026-3783          MEDIUM       5.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-3783,USN-8099-1 | V:UB:CVE-2026-3783
  │ ✘✔✘✘✔ CVE-2026-3784          MEDIUM       6.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-3784,USN-8099-1 | V:UB:CVE-2026-3784
  │ ✘✔✘✘✘ CVE-2026-4873          MEDIUM       5.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-4873
  │ ✘✔✘✘✔ CVE-2026-5545          MEDIUM       6.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-5545 | V:UB:CVE-2026-5545
  │ ✘✔✘✘✘ CVE-2026-6253          MEDIUM       5.9   0.7%   ·  ↳ S:UBUNTU-CVE-2026-6253
  │ ✘✔✘✘✘ CVE-2026-6429          MEDIUM       5.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-6429
  │ ✘✔✘✘✔ CVE-2026-7168          MEDIUM       5.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-7168 | V:UB:CVE-2026-7168
  │ ✘✔✘✘✔ CVE-2026-8458          MEDIUM       6.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-8458 | V:UB:CVE-2026-8458
  │ ✘✔✘✘✔ CVE-2025-15224         LOW          3.1   0.5%   ·  ↳ S:UBUNTU-CVE-2025-15224 | V:UB:CVE-2025-15224
  │ ✘✔✘✘✘ USN-8062-2             ?             -       -   ·
  │ ✘✔✘✘✘ USN-8487-1             ?             -       -   ·
  │ ✘✔✘✘✘ USN-8525-1             ?             -       -   ·
  │ ✘✔✘✘✘ USN-8651-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libdbus-1-3@1.12.16-2ubuntu2.3
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2023-34969         MEDIUM       6.5   1.5%   ·  ↳ S:UBUNTU-CVE-2023-34969 | V:UB:CVE-2023-34969
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libdevmapper1.02.1@2%3A1.02.167-1ubuntu1
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2026-19617         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-19617 | V:UB:CVE-2026-19617
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libdpkg-perl@1.19.7ubuntu3.2
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-6297          HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2025-6297
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libelf1@0.176-1.1ubuntu0.1
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2025-1352          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2025-1352 | V:UB:CVE-2025-1352
  │ ✘✔✘✘✔ CVE-2025-1376          MEDIUM       4.7   0.3%   ·  ↳ S:UBUNTU-CVE-2025-1376 | V:UB:CVE-2025-1376
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libexpat1@2.2.9-1ubuntu0.8
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2023-52425         HIGH         7.5   2.1%   ·  ↳ S:UBUNTU-CVE-2023-52425
  │ ✘✔✘✘✘ CVE-2024-28757         HIGH         7.5   2.0%   ·  ↳ S:UBUNTU-CVE-2024-28757
  │ ✘✔✘✘✘ CVE-2024-8176          HIGH         7.5   1.4%   ·  ↳ S:UBUNTU-CVE-2024-8176
  │ ✘✔✘✘✘ CVE-2025-59375         HIGH         7.5   1.4%   ·  ↳ S:UBUNTU-CVE-2025-59375,USN-8790-1
  │ ✘✔✘✘✘ CVE-2026-102633        HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-102633
  │ ✘✔✘✘✘ CVE-2026-113351        HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-113351
  │ ✘✔✘✘✘ CVE-2026-115506        HIGH         8.7   0.5%   ·  ↳ S:UBUNTU-CVE-2026-115506
  │ ✘✔✘✘✘ CVE-2026-117610        HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-117610
  │ ✘✔✘✘✘ CVE-2026-118370        HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-118370
  │ ✘✔✘✘✔ CVE-2026-25210         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-25210 | V:UB:CVE-2026-25210
  │ ✘✔✘✘✘ CVE-2026-41080         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-41080,USN-8790-1
  │ ✘✔✘✘✘ CVE-2026-45186         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-45186,USN-8790-1
  │ ✘✔✘✘✔ CVE-2026-66046         HIGH         8.7   0.7%   ·  ↳ S:UBUNTU-CVE-2026-66046,USN-8813-1 | V:UB:CVE-2026-66046
  │ ✘✔✘✘✔ CVE-2026-76641         HIGH         8.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-76641,USN-8813-1 | V:UB:CVE-2026-76641
  │ ✘✔✘✘✔ CVE-2026-76957         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-76957,USN-8813-1 | V:UB:CVE-2026-76957
  │ ✘✔✘✘✘ CVE-2026-77214         HIGH         8.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-77214
  │ ✘✔✘✘✘ CVE-2026-93990         HIGH         8.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-93990
  │ ✘✔✘✘✔ CVE-2025-66382         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-66382 | V:UB:CVE-2025-66382
  │ ✘✔✘✘✔ CVE-2026-32776         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-32776,USN-8790-1 | V:UB:CVE-2026-32776
  │ ✘✔✘✘✔ CVE-2026-32777         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-32777,USN-8790-1 | V:UB:CVE-2026-32777
  │ ✘✔✘✘✔ CVE-2026-32778         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-32778,USN-8790-1 | V:UB:CVE-2026-32778
  │ ✘✔✘✘✔ CVE-2026-50219         MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-50219,USN-8790-1 | V:UB:CVE-2026-50219
  │ ✘✔✘✘✔ CVE-2026-56131         MEDIUM       4.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56131,USN-8813-1 | V:UB:CVE-2026-56131
  │ ✘✔✘✘✔ CVE-2026-56132         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56132,USN-8813-1 | V:UB:CVE-2026-56132
  │ ✘✔✘✘✔ CVE-2026-56403         MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56403,USN-8790-1 | V:UB:CVE-2026-56403
  │ ✘✔✘✘✔ CVE-2026-56404         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56404,USN-8790-1 | V:UB:CVE-2026-56404
  │ ✘✔✘✘✔ CVE-2026-56405         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56405,USN-8790-1 | V:UB:CVE-2026-56405
  │ ✘✔✘✘✔ CVE-2026-56406         MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56406,USN-8813-1 | V:UB:CVE-2026-56406
  │ ✘✔✘✘✔ CVE-2026-56407         MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56407,USN-8813-1 | V:UB:CVE-2026-56407
  │ ✘✔✘✘✔ CVE-2026-56408         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56408,USN-8790-1 | V:UB:CVE-2026-56408
  │ ✘✔✘✘✔ CVE-2026-56409         MEDIUM       6.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56409,USN-8813-1 | V:UB:CVE-2026-56409
  │ ✘✔✘✘✔ CVE-2026-56410         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56410,USN-8813-1 | V:UB:CVE-2026-56410
  │ ✘✔✘✘✔ CVE-2026-56411         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56411,USN-8813-1 | V:UB:CVE-2026-56411
  │ ✘✔✘✘✔ CVE-2026-56412         MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56412,USN-8790-1 | V:UB:CVE-2026-56412
  │ ✘✔✘✘✔ CVE-2026-72522         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72522,USN-8813-1 | V:UB:CVE-2026-72522
  │ ✘✔✘✘✔ CVE-2026-24515         LOW          2.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-24515 | V:UB:CVE-2026-24515
  │ ✘✔✘✘✘ USN-8022-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libexpat1-dev@2.2.9-1ubuntu0.8
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2023-52425         HIGH         7.5   2.1%   ·  ↳ S:UBUNTU-CVE-2023-52425
  │ ✘✔✘✘✘ CVE-2024-28757         HIGH         7.5   2.0%   ·  ↳ S:UBUNTU-CVE-2024-28757
  │ ✘✔✘✘✘ CVE-2024-8176          HIGH         7.5   1.4%   ·  ↳ S:UBUNTU-CVE-2024-8176
  │ ✘✔✘✘✘ CVE-2025-59375         HIGH         7.5   1.4%   ·  ↳ S:UBUNTU-CVE-2025-59375,USN-8790-1
  │ ✘✔✘✘✘ CVE-2026-102633        HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-102633
  │ ✘✔✘✘✘ CVE-2026-113351        HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-113351
  │ ✘✔✘✘✘ CVE-2026-115506        HIGH         8.7   0.5%   ·  ↳ S:UBUNTU-CVE-2026-115506
  │ ✘✔✘✘✘ CVE-2026-117610        HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-117610
  │ ✘✔✘✘✘ CVE-2026-118370        HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-118370
  │ ✘✔✘✘✘ CVE-2026-25210         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-25210
  │ ✘✔✘✘✘ CVE-2026-41080         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-41080,USN-8790-1
  │ ✘✔✘✘✘ CVE-2026-45186         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-45186,USN-8790-1
  │ ✘✔✘✘✔ CVE-2026-66046         HIGH         8.7   0.7%   ·  ↳ S:UBUNTU-CVE-2026-66046,USN-8813-1 | V:UB:CVE-2026-66046
  │ ✘✔✘✘✔ CVE-2026-76641         HIGH         8.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-76641,USN-8813-1 | V:UB:CVE-2026-76641
  │ ✘✔✘✘✔ CVE-2026-76957         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-76957,USN-8813-1 | V:UB:CVE-2026-76957
  │ ✘✔✘✘✘ CVE-2026-77214         HIGH         8.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-77214
  │ ✘✔✘✘✘ CVE-2026-93990         HIGH         8.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-93990
  │ ✘✔✘✘✘ CVE-2025-66382         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-66382
  │ ✘✔✘✘✔ CVE-2026-32776         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-32776,USN-8790-1 | V:UB:CVE-2026-32776
  │ ✘✔✘✘✔ CVE-2026-32777         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-32777,USN-8790-1 | V:UB:CVE-2026-32777
  │ ✘✔✘✘✔ CVE-2026-32778         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-32778,USN-8790-1 | V:UB:CVE-2026-32778
  │ ✘✔✘✘✔ CVE-2026-50219         MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-50219,USN-8790-1 | V:UB:CVE-2026-50219
  │ ✘✔✘✘✔ CVE-2026-56131         MEDIUM       4.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56131,USN-8813-1 | V:UB:CVE-2026-56131
  │ ✘✔✘✘✔ CVE-2026-56132         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56132,USN-8813-1 | V:UB:CVE-2026-56132
  │ ✘✔✘✘✔ CVE-2026-56403         MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56403,USN-8790-1 | V:UB:CVE-2026-56403
  │ ✘✔✘✘✔ CVE-2026-56404         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56404,USN-8790-1 | V:UB:CVE-2026-56404
  │ ✘✔✘✘✔ CVE-2026-56405         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56405,USN-8790-1 | V:UB:CVE-2026-56405
  │ ✘✔✘✘✔ CVE-2026-56406         MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56406,USN-8813-1 | V:UB:CVE-2026-56406
  │ ✘✔✘✘✔ CVE-2026-56407         MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56407,USN-8813-1 | V:UB:CVE-2026-56407
  │ ✘✔✘✘✔ CVE-2026-56408         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56408,USN-8790-1 | V:UB:CVE-2026-56408
  │ ✘✔✘✘✔ CVE-2026-56409         MEDIUM       6.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56409,USN-8813-1 | V:UB:CVE-2026-56409
  │ ✘✔✘✘✔ CVE-2026-56410         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56410,USN-8813-1 | V:UB:CVE-2026-56410
  │ ✘✔✘✘✔ CVE-2026-56411         MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-56411,USN-8813-1 | V:UB:CVE-2026-56411
  │ ✘✔✘✘✔ CVE-2026-56412         MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-56412,USN-8790-1 | V:UB:CVE-2026-56412
  │ ✘✔✘✘✔ CVE-2026-72522         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72522,USN-8813-1 | V:UB:CVE-2026-72522
  │ ✘✔✘✘✘ CVE-2026-24515         LOW          2.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-24515
  │ ✘✔✘✘✘ USN-8022-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libfdisk1@2.34-0.1ubuntu9.6
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-53613         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53613
  │ ✘✔✘✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53615
  │ ✘✔✘✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-76642
  │ ✘✔✘✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78408
  │ ✘✔✘✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78409
  │ ✘✔✘✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78410
  │ ✘✔✘✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-14104
  │ ✘✔✘✘✘ CVE-2026-13595         MEDIUM       6.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-13595
  │ ✘✔✘✘✔ CVE-2026-27456         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-27456 | V:UB:CVE-2026-27456
  │ ✘✔✘✘✘ USN-8091-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgcc-9-dev@9.4.0-1ubuntu1~20.04.2
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2020-23026         HIGH         7.5   1.1%   ·  ↳ S:UBUNTU-CVE-2020-23026
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✘ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ S:UBUNTU-CVE-2023-4039
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgcc-s1@10.5.0-1ubuntu1~20.04
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ S:UBUNTU-CVE-2023-4039,USN-7700-1 | V:UB:CVE-2023-4039
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgcrypt20@1.8.5-5ubuntu1.1
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2024-2236          MEDIUM       5.9   1.1%   ·  ↳ O:UBUNTU-CVE-2024-2236 | S:UBUNTU-CVE-2024-2236 | V:UB:CVE-2024-2236
  │ ✔✔✔✘✘ CVE-2026-41989         MEDIUM       6.7   0.2%   ·  ↳ O:UBUNTU-CVE-2026-41989 | S:UBUNTU-CVE-2026-41989
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libglib2.0-0@2.64.6-1~ubuntu20.04.9
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2025-14087         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2025-14087 | V:UB:CVE-2025-14087
  │ ✘✔✘✘✔ CVE-2026-58016         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-58016,USN-8794-1 | V:UB:CVE-2026-58016
  │ ✘✔✘✘✔ CVE-2025-13601         HIGH         7.7   0.3%   ·  ↳ S:UBUNTU-CVE-2025-13601 | V:UB:CVE-2025-13601
  │ ✘✔✘✘✔ CVE-2026-16118         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-16118,USN-8794-1 | V:UB:CVE-2026-16118
  │ ✘✔✘✘✔ CVE-2026-58010         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-58010,USN-8794-1 | V:UB:CVE-2026-58010
  │ ✘✔✘✘✔ CVE-2026-58011         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-58011,USN-8794-1 | V:UB:CVE-2026-58011
  │ ✘✔✘✘✔ CVE-2026-58012         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-58012,USN-8794-1 | V:UB:CVE-2026-58012
  │ ✘✔✘✘✔ CVE-2026-58013         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-58013,USN-8794-1 | V:UB:CVE-2026-58013
  │ ✘✔✘✘✔ CVE-2026-58014         HIGH         8.6   0.6%   ·  ↳ S:UBUNTU-CVE-2026-58014,USN-8794-1 | V:UB:CVE-2026-58014
  │ ✘✔✘✘✔ CVE-2026-58015         HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2026-58015,USN-8794-1 | V:UB:CVE-2026-58015
  │ ✘✔✘✘✘ CVE-2025-14512         MEDIUM       6.5   0.6%   ·  ↳ S:UBUNTU-CVE-2025-14512
  │ ✘✔✘✘✔ CVE-2026-1484          MEDIUM       4.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-1484 | V:UB:CVE-2026-1484
  │ ✘✔✘✘✔ CVE-2026-1489          MEDIUM       5.4   0.4%   ·  ↳ S:UBUNTU-CVE-2026-1489 | V:UB:CVE-2026-1489
  │ ✘✔✘✘✔ CVE-2026-15588         MEDIUM       5.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15588,USN-8794-1 | V:UB:CVE-2026-15588
  │ ✘✔✘✘✔ CVE-2026-86469         MEDIUM       5.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-86469 | V:UB:CVE-2026-86469
  │ ✘✔✘✘✔ CVE-2025-3360          LOW          3.7   0.7%   ·  ↳ S:UBUNTU-CVE-2025-3360 | V:UB:CVE-2025-3360
  │ ✘✔✘✘✔ CVE-2025-7039          LOW          3.7   0.4%   ·  ↳ S:UBUNTU-CVE-2025-7039 | V:UB:CVE-2025-7039
  │ ✘✔✘✘✔ CVE-2026-0988          LOW          3.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-0988 | V:UB:CVE-2026-0988
  │ ✘✔✘✘✔ CVE-2026-1485          LOW          2.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-1485 | V:UB:CVE-2026-1485
  │ ✘✔✘✘✘ USN-7942-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libglib2.0-bin@2.64.6-1~ubuntu20.04.9
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-14087         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2025-14087
  │ ✘✔✘✘✔ CVE-2026-58016         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-58016,USN-8794-1 | V:UB:CVE-2026-58016
  │ ✘✔✘✘✘ CVE-2025-13601         HIGH         7.7   0.3%   ·  ↳ S:UBUNTU-CVE-2025-13601
  │ ✘✔✘✘✔ CVE-2026-16118         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-16118,USN-8794-1 | V:UB:CVE-2026-16118
  │ ✘✔✘✘✔ CVE-2026-58010         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-58010,USN-8794-1 | V:UB:CVE-2026-58010
  │ ✘✔✘✘✔ CVE-2026-58011         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-58011,USN-8794-1 | V:UB:CVE-2026-58011
  │ ✘✔✘✘✔ CVE-2026-58012         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-58012,USN-8794-1 | V:UB:CVE-2026-58012
  │ ✘✔✘✘✔ CVE-2026-58013         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-58013,USN-8794-1 | V:UB:CVE-2026-58013
  │ ✘✔✘✘✔ CVE-2026-58014         HIGH         8.6   0.6%   ·  ↳ S:UBUNTU-CVE-2026-58014,USN-8794-1 | V:UB:CVE-2026-58014
  │ ✘✔✘✘✔ CVE-2026-58015         HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2026-58015,USN-8794-1 | V:UB:CVE-2026-58015
  │ ✘✔✘✘✘ CVE-2025-14512         MEDIUM       6.5   0.6%   ·  ↳ S:UBUNTU-CVE-2025-14512
  │ ✘✔✘✘✔ CVE-2026-1484          MEDIUM       4.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-1484 | V:UB:CVE-2026-1484
  │ ✘✔✘✘✔ CVE-2026-1489          MEDIUM       5.4   0.4%   ·  ↳ S:UBUNTU-CVE-2026-1489 | V:UB:CVE-2026-1489
  │ ✘✔✘✘✔ CVE-2026-15588         MEDIUM       5.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15588,USN-8794-1 | V:UB:CVE-2026-15588
  │ ✘✔✘✘✔ CVE-2026-86469         MEDIUM       5.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-86469 | V:UB:CVE-2026-86469
  │ ✘✔✘✘✘ CVE-2025-3360          LOW          3.7   0.7%   ·  ↳ S:UBUNTU-CVE-2025-3360
  │ ✘✔✘✘✘ CVE-2025-7039          LOW          3.7   0.4%   ·  ↳ S:UBUNTU-CVE-2025-7039
  │ ✘✔✘✘✔ CVE-2026-0988          LOW          3.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-0988 | V:UB:CVE-2026-0988
  │ ✘✔✘✘✔ CVE-2026-1485          LOW          2.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-1485 | V:UB:CVE-2026-1485
  │ ✘✔✘✘✘ USN-7942-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libglib2.0-data@2.64.6-1~ubuntu20.04.9
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-14087         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2025-14087
  │ ✘✔✘✘✘ CVE-2026-58016         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-58016,USN-8794-1
  │ ✘✔✘✘✘ CVE-2025-13601         HIGH         7.7   0.3%   ·  ↳ S:UBUNTU-CVE-2025-13601
  │ ✘✔✘✘✘ CVE-2026-16118         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-16118,USN-8794-1
  │ ✘✔✘✘✘ CVE-2026-58010         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-58010,USN-8794-1
  │ ✘✔✘✘✘ CVE-2026-58011         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-58011,USN-8794-1
  │ ✘✔✘✘✘ CVE-2026-58012         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-58012,USN-8794-1
  │ ✘✔✘✘✘ CVE-2026-58013         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-58013,USN-8794-1
  │ ✘✔✘✘✘ CVE-2026-58014         HIGH         8.6   0.6%   ·  ↳ S:UBUNTU-CVE-2026-58014,USN-8794-1
  │ ✘✔✘✘✘ CVE-2026-58015         HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2026-58015,USN-8794-1
  │ ✘✔✘✘✘ CVE-2025-14512         MEDIUM       6.5   0.6%   ·  ↳ S:UBUNTU-CVE-2025-14512
  │ ✘✔✘✘✘ CVE-2026-1484          MEDIUM       4.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-1484
  │ ✘✔✘✘✘ CVE-2026-1489          MEDIUM       5.4   0.4%   ·  ↳ S:UBUNTU-CVE-2026-1489
  │ ✘✔✘✘✘ CVE-2026-15588         MEDIUM       5.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15588,USN-8794-1
  │ ✘✔✘✘✘ CVE-2026-86469         MEDIUM       5.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-86469
  │ ✘✔✘✘✘ CVE-2025-3360          LOW          3.7   0.7%   ·  ↳ S:UBUNTU-CVE-2025-3360
  │ ✘✔✘✘✘ CVE-2025-7039          LOW          3.7   0.4%   ·  ↳ S:UBUNTU-CVE-2025-7039
  │ ✘✔✘✘✘ CVE-2026-0988          LOW          3.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-0988
  │ ✘✔✘✘✘ CVE-2026-1485          LOW          2.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-1485
  │ ✘✔✘✘✘ USN-7942-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgnutls30@3.6.13-2ubuntu1.12
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2026-33845         CRITICAL     9.1   2.1%   ·  ↳ S:UBUNTU-CVE-2026-33845,USN-8502-1 | V:UB:CVE-2026-33845
  │ ✘✔✘✘✔ CVE-2026-42010         CRITICAL     9.8   1.1%   ·  ↳ S:UBUNTU-CVE-2026-42010,USN-8502-1 | V:UB:CVE-2026-42010
  │ ✘✔✘✘✔ CVE-2025-32988         HIGH         8.2   1.5%   ·  ↳ S:UBUNTU-CVE-2025-32988,USN-7742-1 | V:UB:CVE-2025-32988
  │ ✘✔✘✘✔ CVE-2025-32990         HIGH         8.2   0.9%   ·  ↳ S:UBUNTU-CVE-2025-32990,USN-7742-1 | V:UB:CVE-2025-32990
  │ ✘✔✘✘✔ CVE-2026-33846         HIGH         7.5   1.3%   ·  ↳ S:UBUNTU-CVE-2026-33846,USN-8502-1 | V:UB:CVE-2026-33846
  │ ✘✔✘✘✔ CVE-2026-3833          HIGH         7.4   0.6%   ·  ↳ S:UBUNTU-CVE-2026-3833,USN-8502-1 | V:UB:CVE-2026-3833
  │ ✘✔✘✘✔ CVE-2026-42009         HIGH         7.5   1.3%   ·  ↳ S:UBUNTU-CVE-2026-42009,USN-8502-1 | V:UB:CVE-2026-42009
  │ ✘✔✘✘✔ CVE-2026-42011         HIGH         7.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-42011,USN-8539-1 | V:UB:CVE-2026-42011
  │ ✘✔✘✘✔ CVE-2026-42012         HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-42012,USN-8539-1 | V:UB:CVE-2026-42012
  │ ✘✔✘✘✔ CVE-2026-42013         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-42013,USN-8539-1 | V:UB:CVE-2026-42013
  │ ✘✔✘✘✔ CVE-2026-5260          HIGH         8.2   0.8%   ·  ↳ S:UBUNTU-CVE-2026-5260,USN-8502-1 | V:UB:CVE-2026-5260
  │ ✘✔✘✘✔ CVE-2025-14831         MEDIUM       5.3   0.7%   ·  ↳ S:UBUNTU-CVE-2025-14831,USN-8502-1 | V:UB:CVE-2025-14831
  │ ✘✔✘✘✔ CVE-2025-6395          MEDIUM       6.5   0.8%   ·  ↳ S:UBUNTU-CVE-2025-6395,USN-7742-1 | V:UB:CVE-2025-6395
  │ ✘✔✘✘✔ CVE-2025-9820          MEDIUM       4.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-9820,USN-8502-1 | V:UB:CVE-2025-9820
  │ ✘✔✘✘✔ CVE-2026-42014         MEDIUM       6.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-42014,USN-8539-1 | V:UB:CVE-2026-42014
  │ ✘✔✘✘✔ CVE-2026-42015         MEDIUM       5.3   0.7%   ·  ↳ S:UBUNTU-CVE-2026-42015,USN-8539-1 | V:UB:CVE-2026-42015
  │ ✘✔✘✘✔ CVE-2026-88647         MEDIUM       6.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-88647 | V:UB:CVE-2026-88647
  │ ✘✔✘✘✔ CVE-2026-95184         MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-95184 | V:UB:CVE-2026-95184
  │ ✘✔✘✘✔ CVE-2026-95209         MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-95209 | V:UB:CVE-2026-95209
  │ ✘✔✘✘✔ CVE-2026-95210         MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-95210 | V:UB:CVE-2026-95210
  │ ✘✔✘✘✔ CVE-2026-67693         LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-67693 | V:UB:CVE-2026-67693
  │ ✘✔✘✘✔ CVE-2026-88648         LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-88648 | V:UB:CVE-2026-88648
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgomp1@10.5.0-1ubuntu1~20.04
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✘✘✘✔ CVE-2020-13844         MEDIUM       5.5   0.5%   ·  ↳ V:UB:CVE-2020-13844
  │ ✘✔✘✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ S:UBUNTU-CVE-2023-4039,USN-7700-1 | V:UB:CVE-2023-4039
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libgssapi-krb5-2@1.17-6ubuntu4.11
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2018-5709          HIGH         7.5   2.0%   ·  ↳ S:UBUNTU-CVE-2018-5709
  │ ✘✔✘✘✘ CVE-2026-107778        HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-107778
  │ ✘✔✘✘✘ CVE-2026-107708        MEDIUM       6.9   0.5%   ·  ↳ S:UBUNTU-CVE-2026-107708
  │ ✘✔✘✘✘ CVE-2026-11850         MEDIUM       5.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-11850
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libicu66@66.1-2ubuntu2.1
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2025-5222          HIGH         7.0   0.4%   ·  ↳ S:UBUNTU-CVE-2025-5222 | V:UB:CVE-2025-5222
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libip4tc2@1.8.4-3ubuntu2.1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2012-2663          HIGH         7.5   2.7%   ·  ↳ S:UBUNTU-CVE-2012-2663
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libitm1@10.5.0-1ubuntu1~20.04
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ S:UBUNTU-CVE-2023-4039,USN-7700-1 | V:UB:CVE-2023-4039
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libk5crypto3@1.17-6ubuntu4.11
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2018-5709          HIGH         7.5   2.0%   ·  ↳ S:UBUNTU-CVE-2018-5709
  │ ✘✔✘✘✘ CVE-2026-107778        HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-107778
  │ ✘✔✘✘✘ CVE-2026-107708        MEDIUM       6.9   0.5%   ·  ↳ S:UBUNTU-CVE-2026-107708
  │ ✘✔✘✘✘ CVE-2026-11850         MEDIUM       5.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-11850
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libkmod2@27-1ubuntu2.1
  │ OSGTV
  │ ✘✔✘✘✘ USN-8226-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libkrb5-3@1.17-6ubuntu4.11
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2018-5709          HIGH         7.5   2.0%   ·  ↳ S:UBUNTU-CVE-2018-5709
  │ ✘✔✘✘✘ CVE-2026-107778        HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-107778
  │ ✘✔✘✘✘ CVE-2026-107708        MEDIUM       6.9   0.5%   ·  ↳ S:UBUNTU-CVE-2026-107708
  │ ✘✔✘✘✘ CVE-2026-11850         MEDIUM       5.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-11850
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libkrb5support0@1.17-6ubuntu4.11
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2018-5709          HIGH         7.5   2.0%   ·  ↳ S:UBUNTU-CVE-2018-5709
  │ ✘✔✘✘✘ CVE-2026-107778        HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-107778
  │ ✘✔✘✘✘ CVE-2026-107708        MEDIUM       6.9   0.5%   ·  ↳ S:UBUNTU-CVE-2026-107708
  │ ✘✔✘✘✘ CVE-2026-11850         MEDIUM       5.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-11850
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/liblmdb0@0.9.24-1
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2026-22185         MEDIUM       4.6   0.2%   ·  ↳ S:UBUNTU-CVE-2026-22185 | V:UB:CVE-2026-22185
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/liblsan0@10.5.0-1ubuntu1~20.04
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ S:UBUNTU-CVE-2023-4039,USN-7700-1 | V:UB:CVE-2023-4039
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/liblz4-1@1.9.2-2ubuntu0.20.04.1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-62813         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2025-62813
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/liblzma5@5.2.4-1ubuntu1.1
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2026-34743         MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-34743,USN-8362-1 | V:UB:CVE-2026-34743
  │ ✘✔✘✘✘ USN-8945-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libmount1@2.34-0.1ubuntu9.6
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-53613         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53613
  │ ✘✔✘✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53615
  │ ✘✔✘✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-76642
  │ ✘✔✘✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78408
  │ ✘✔✘✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78409
  │ ✘✔✘✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78410
  │ ✘✔✘✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-14104
  │ ✘✔✘✘✘ CVE-2026-13595         MEDIUM       6.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-13595
  │ ✘✔✘✘✔ CVE-2026-27456         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-27456 | V:UB:CVE-2026-27456
  │ ✘✔✘✘✘ USN-8091-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libncurses6@6.2-0ubuntu2.1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-69720         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-69720,USN-8503-1
  │ ✘✔✘✘✔ CVE-2023-50495         MEDIUM       6.5   1.0%   ·  ↳ S:UBUNTU-CVE-2023-50495 | V:UB:CVE-2023-50495
  │ ✘✔✘✘✔ CVE-2025-6141          MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-6141,USN-8709-1 | V:UB:CVE-2025-6141
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libncursesw6@6.2-0ubuntu2.1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-69720         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-69720,USN-8503-1
  │ ✘✔✘✘✔ CVE-2023-50495         MEDIUM       6.5   1.0%   ·  ↳ S:UBUNTU-CVE-2023-50495 | V:UB:CVE-2023-50495
  │ ✘✔✘✘✘ CVE-2025-6141          MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-6141,USN-8709-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libnghttp2-14@1.40.0-1ubuntu0.3
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2026-27135         HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2026-27135 | V:UB:CVE-2026-27135
  │ ✘✔✘✘✘ CVE-2026-58055         MEDIUM       6.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-58055
  │ ✘✔✘✘✘ USN-8233-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libnss-systemd@245.4-4ubuntu3.24
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2023-26604         HIGH         7.8   1.1%   ·  ↳ S:UBUNTU-CVE-2023-26604 | V:UB:CVE-2023-26604
  │ ✘✔✘✘✘ CVE-2020-13776         MEDIUM       6.7   0.5%   ·  ↳ S:UBUNTU-CVE-2020-13776
  │ ✘✔✘✘✔ CVE-2023-7008          MEDIUM       5.9   0.8%   ·  ↳ S:UBUNTU-CVE-2023-7008 | V:UB:CVE-2023-7008
  │ ✘✔✘✘✘ CVE-2025-4598          MEDIUM       4.7   1.3%   ·  ↳ S:UBUNTU-CVE-2025-4598,USN-7559-1
  │ ✘✔✘✘✘ CVE-2026-29111         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-29111
  │ ✘✔✘✘✔ CVE-2026-40225         MEDIUM       6.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-40225 | V:UB:CVE-2026-40225
  │ ✘✔✘✘✘ CVE-2026-40226         MEDIUM       6.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-40226
  │ ✘✔✘✘✔ CVE-2026-40228         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-40228 | V:UB:CVE-2026-40228
  │ ✘✔✘✘✘ USN-8119-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libp11-kit0@0.23.20-1ubuntu0.1
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2026-13757         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-13757,USN-8687-1 | V:UB:CVE-2026-13757
  │ ✘✔✘✘✔ CVE-2026-18938         MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18938,USN-8687-1 | V:UB:CVE-2026-18938
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpackagekit-glib2-18@1.1.13-2ubuntu1.1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-41651         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-41651
  │ ✘✔✘✘✘ CVE-2026-10294         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-10294
  │ ✘✔✘✘✔ CVE-2022-0987          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-0987 | V:UB:CVE-2022-0987
  │ ✘✔✘✘✔ CVE-2024-0217          LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2024-0217 | V:UB:CVE-2024-0217
  │ ✘✔✘✘✘ USN-8195-3             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-cap@1%3A2.32-1ubuntu0.2
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2026-4878          HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-4878,USN-8193-2 | V:UB:CVE-2026-4878
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-modules@1.3.1-5ubuntu4.7
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-6020          HIGH         7.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-6020
  │ ✘✔✘✘✘ CVE-2026-54411         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-54411
  │ ✘✔✘✘✘ CVE-2024-10041         MEDIUM       4.7   0.3%   ·  ↳ S:UBUNTU-CVE-2024-10041
  │ ✘✔✘✘✘ USN-8688-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-modules-bin@1.3.1-5ubuntu4.7
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-6020          HIGH         7.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-6020
  │ ✘✔✘✘✘ CVE-2026-54411         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-54411
  │ ✘✔✘✘✘ CVE-2024-10041         MEDIUM       4.7   0.3%   ·  ↳ S:UBUNTU-CVE-2024-10041
  │ ✘✔✘✘✘ USN-8688-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-runtime@1.3.1-5ubuntu4.7
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-6020          HIGH         7.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-6020
  │ ✘✔✘✘✘ CVE-2026-54411         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-54411
  │ ✘✔✘✘✘ CVE-2024-10041         MEDIUM       4.7   0.3%   ·  ↳ S:UBUNTU-CVE-2024-10041
  │ ✘✔✘✘✘ USN-8688-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam-systemd@245.4-4ubuntu3.24
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2023-26604         HIGH         7.8   1.1%   ·  ↳ S:UBUNTU-CVE-2023-26604 | V:UB:CVE-2023-26604
  │ ✘✔✘✘✘ CVE-2020-13776         MEDIUM       6.7   0.5%   ·  ↳ S:UBUNTU-CVE-2020-13776
  │ ✘✔✘✘✔ CVE-2023-7008          MEDIUM       5.9   0.8%   ·  ↳ S:UBUNTU-CVE-2023-7008 | V:UB:CVE-2023-7008
  │ ✘✔✘✘✘ CVE-2025-4598          MEDIUM       4.7   1.3%   ·  ↳ S:UBUNTU-CVE-2025-4598,USN-7559-1
  │ ✘✔✘✘✘ CVE-2026-29111         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-29111
  │ ✘✔✘✘✔ CVE-2026-40225         MEDIUM       6.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-40225 | V:UB:CVE-2026-40225
  │ ✘✔✘✘✘ CVE-2026-40226         MEDIUM       6.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-40226
  │ ✘✔✘✘✔ CVE-2026-40228         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-40228 | V:UB:CVE-2026-40228
  │ ✘✔✘✘✘ USN-8119-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpam0g@1.3.1-5ubuntu4.7
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-6020          HIGH         7.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-6020
  │ ✘✔✘✘✘ CVE-2026-54411         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-54411
  │ ✘✔✘✘✘ CVE-2024-10041         MEDIUM       4.7   0.3%   ·  ↳ S:UBUNTU-CVE-2024-10041
  │ ✘✔✘✘✘ USN-8688-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpcre2-8-0@10.34-7ubuntu0.1
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2022-41409         HIGH         7.5   1.1%   ·  ↳ S:UBUNTU-CVE-2022-41409 | V:UB:CVE-2022-41409
  │ ✘✔✘✘✔ CVE-2026-103111        HIGH         7.6   0.3%   ·  ↳ S:UBUNTU-CVE-2026-103111 | V:UB:CVE-2026-103111
  │ ✘✔✘✘✔ CVE-2026-86145         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-86145 | V:UB:CVE-2026-86145
  │ ✘✔✘✘✔ CVE-2026-89157         HIGH         7.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89157 | V:UB:CVE-2026-89157
  │ ✘✔✘✘✔ CVE-2026-89161         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89161 | V:UB:CVE-2026-89161
  │ ✘✔✘✘✔ CVE-2026-89156         MEDIUM       5.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89156 | V:UB:CVE-2026-89156
  │ ✘✔✘✘✔ CVE-2026-89158         MEDIUM       6.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89158 | V:UB:CVE-2026-89158
  │ ✘✔✘✘✔ CVE-2026-89160         MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89160 | V:UB:CVE-2026-89160
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpcre3@2%3A8.39-12ubuntu0.1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2017-11164         HIGH         7.8   3.1%   ·  ↳ S:UBUNTU-CVE-2017-11164
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libperl5.30@5.30.0-9ubuntu0.5
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2011-10043         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2011-10043
  │ ✘✔✘✘✘ CVE-2017-20230         CRITICAL    10.0   0.6%   ·  ↳ S:UBUNTU-CVE-2017-20230
  │ ✘✔✘✘✔ CVE-2026-12087         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-12087,USN-8675-1 | V:UB:CVE-2026-12087
  │ ✘✔✘✘✔ CVE-2026-13221         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-13221,USN-8675-1 | V:UB:CVE-2026-13221
  │ ✘✔✘✘✘ CVE-2026-4176          CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-4176
  │ ✘✔✘✘✔ CVE-2026-42496         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-42496,USN-8467-1 | V:UB:CVE-2026-42496
  │ ✘✔✘✘✔ CVE-2026-57433         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-57433,USN-8675-1 | V:UB:CVE-2026-57433
  │ ✘✔✘✘✔ CVE-2026-8376          CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-8376,USN-8467-1 | V:UB:CVE-2026-8376
  │ ✘✔✘✘✘ CVE-2023-31486         HIGH         8.1   1.7%   ·  ↳ S:UBUNTU-CVE-2023-31486
  │ ✘✔✘✘✘ CVE-2023-47039         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2023-47039
  │ ✘✔✘✘✘ CVE-2026-42497         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-42497
  │ ✘✔✘✘✘ CVE-2026-48959         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-48959
  │ ✘✔✘✘✘ CVE-2026-48961         HIGH         7.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-48961
  │ ✘✔✘✘✘ CVE-2026-48962         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-48962
  │ ✘✔✘✘✔ CVE-2026-57432         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57432,USN-8675-1 | V:UB:CVE-2026-57432
  │ ✘✔✘✘✘ CVE-2026-7017          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-7017
  │ ✘✔✘✘✘ CVE-2026-82560         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-82560
  │ ✘✔✘✘✘ CVE-2026-9538          HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-9538
  │ ✘✔✘✘✘ CVE-2025-15649         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-15649
  │ ✘✔✘✘✘ CVE-2025-40909         MEDIUM       5.9   0.5%   ·  ↳ S:UBUNTU-CVE-2025-40909
  │ ✘✔✘✘✔ CVE-2026-15534         MEDIUM       5.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15534,USN-8736-1 | V:UB:CVE-2026-15534
  │ ✘✔✘✘✔ CVE-2026-19487         MEDIUM       5.3   0.4%   ·  ↳ S:UBUNTU-CVE-2026-19487,USN-8736-1 | V:UB:CVE-2026-19487
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpolkit-agent-1-0@0.105-26ubuntu1.3
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2016-2568          HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2016-2568 | V:UB:CVE-2016-2568
  │ ✘✔✘✘✘ CVE-2025-7519          MEDIUM       6.7   0.2%   ·  ↳ S:UBUNTU-CVE-2025-7519
  │ ✘✔✘✘✘ CVE-2026-4897          MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-4897
  │ ✘✔✘✘✘ CVE-2026-85498         LOW          3.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-85498
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpolkit-gobject-1-0@0.105-26ubuntu1.3
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2016-2568          HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2016-2568 | V:UB:CVE-2016-2568
  │ ✘✔✘✘✘ CVE-2025-7519          MEDIUM       6.7   0.2%   ·  ↳ S:UBUNTU-CVE-2025-7519
  │ ✘✔✘✘✘ CVE-2026-4897          MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-4897
  │ ✘✔✘✘✘ CVE-2026-85498         LOW          3.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-85498
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.8@3.8.10-0ubuntu1~20.04.18
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2007-4559          CRITICAL     9.8  27.1%   ·  ↳ S:UBUNTU-CVE-2007-4559
  │ ✘✔✘✘✘ CVE-2026-115557        CRITICAL     9.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-115557
  │ ✘✔✘✘✘ CVE-2026-19445         CRITICAL     9.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19445
  │ ✘✔✘✘✘ CVE-2026-6100          CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-6100
  │ ✘✔✘✘✘ CVE-2020-10735         HIGH         7.5   4.5%   ·  ↳ S:UBUNTU-CVE-2020-10735
  │ ✘✔✘✘✔ CVE-2025-13836         HIGH         7.5   1.7%   ·  ↳ S:UBUNTU-CVE-2025-13836,USN-7951-1 | V:UB:CVE-2025-13836
  │ ✘✔✘✘✘ CVE-2025-69534         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2025-69534
  │ ✘✔✘✘✔ CVE-2025-8194          HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2025-8194,USN-7710-1 | V:UB:CVE-2025-8194
  │ ✘✔✘✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-11940
  │ ✘✔✘✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2026-11972
  │ ✘✔✘✘✔ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-15308,USN-8744-1 | V:UB:CVE-2026-15308
  │ ✘✔✘✘✘ CVE-2026-19553         HIGH         7.6   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19553
  │ ✘✔✘✘✔ CVE-2026-3644          HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-3644,USN-8744-1 | V:UB:CVE-2026-3644
  │ ✘✔✘✘✔ CVE-2026-4224          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-4224,USN-8744-1 | V:UB:CVE-2026-4224
  │ ✘✔✘✘✘ CVE-2026-4519          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-4519
  │ ✘✔✘✘✘ CVE-2026-4786          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-4786
  │ ✘✔✘✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57178
  │ ✘✔✘✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-7210
  │ ✘✔✘✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-82049
  │ ✘✔✘✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-84366
  │ ✘✔✘✘✘ CVE-2026-9669          HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-9669
  │ ✘✔✘✘✘ CVE-2021-23336         MEDIUM       5.9  40.7%   ·  ↳ S:UBUNTU-CVE-2021-23336
  │ ✘✔✘✘✔ CVE-2025-11468         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-11468 | V:UB:CVE-2025-11468
  │ ✘✔✘✘✔ CVE-2025-12084         MEDIUM       6.3   0.8%   ·  ↳ S:UBUNTU-CVE-2025-12084 | V:UB:CVE-2025-12084
  │ ✘✔✘✘✘ CVE-2025-12781         MEDIUM       6.3   0.9%   ·  ↳ S:UBUNTU-CVE-2025-12781
  │ ✘✔✘✘✔ CVE-2025-13837         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-13837 | V:UB:CVE-2025-13837
  │ ✘✔✘✘✔ CVE-2025-15282         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2025-15282 | V:UB:CVE-2025-15282
  │ ✘✔✘✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15366
  │ ✘✔✘✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15367
  │ ✘✔✘✘✔ CVE-2025-4516          MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2025-4516,USN-7570-1 | V:UB:CVE-2025-4516
  │ ✘✔✘✘✔ CVE-2025-6069          MEDIUM       4.3   0.6%   ·  ↳ S:UBUNTU-CVE-2025-6069,USN-7710-1 | V:UB:CVE-2025-6069
  │ ✘✔✘✘✔ CVE-2025-6075          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-6075,USN-7886-1 | V:UB:CVE-2025-6075
  │ ✘✔✘✘✔ CVE-2025-8291          MEDIUM       4.3   0.5%   ·  ↳ S:UBUNTU-CVE-2025-8291,USN-7886-1 | V:UB:CVE-2025-8291
  │ ✘✔✘✘✔ CVE-2026-0672          MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-0672 | V:UB:CVE-2026-0672
  │ ✘✔✘✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-0864
  │ ✘✔✘✘✔ CVE-2026-0865          MEDIUM       5.9   0.6%   ·  ↳ S:UBUNTU-CVE-2026-0865 | V:UB:CVE-2026-0865
  │ ✘✔✘✘✘ CVE-2026-114583        MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-114583
  │ ✘✔✘✘✘ CVE-2026-12345         MEDIUM       5.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-12345
  │ ✘✔✘✘✘ CVE-2026-1299          MEDIUM       6.0   0.6%   ·  ↳ S:UBUNTU-CVE-2026-1299
  │ ✘✔✘✘✘ CVE-2026-1502          MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-1502
  │ ✘✔✘✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15806
  │ ✘✔✘✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·  ↳ S:UBUNTU-CVE-2026-17084
  │ ✘✔✘✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19672
  │ ✘✔✘✘✔ CVE-2026-2297          MEDIUM       5.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-2297 | V:UB:CVE-2026-2297
  │ ✘✔✘✘✘ CVE-2026-3276          MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-3276
  │ ✘✔✘✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3446
  │ ✘✔✘✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57175
  │ ✘✔✘✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57176
  │ ✘✔✘✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57177
  │ ✘✔✘✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57179
  │ ✘✔✘✘✔ CVE-2026-6019          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6019,USN-8744-1 | V:UB:CVE-2026-6019
  │ ✘✔✘✘✘ CVE-2026-8328          MEDIUM       5.9   0.5%   ·  ↳ S:UBUNTU-CVE-2026-8328
  │ ✘✔✘✘✘ CVE-2026-87910         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-87910
  │ ✘✔✘✘✘ CVE-2025-13462         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2025-13462
  │ ✘✔✘✘✔ CVE-2025-1795          LOW          2.3   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1795,USN-7570-1 | V:UB:CVE-2025-1795
  │ ✘✔✘✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15310
  │ ✘✔✘✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18503
  │ ✘✔✘✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-6879
  │ ✘✔✘✘✘ USN-8018-1             ?             -       -   ·
  │ ✘✔✘✘✘ USN-8018-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.8-dev@3.8.10-0ubuntu1~20.04.18
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2007-4559          CRITICAL     9.8  27.1%   ·  ↳ S:UBUNTU-CVE-2007-4559
  │ ✘✔✘✘✘ CVE-2026-115557        CRITICAL     9.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-115557
  │ ✘✔✘✘✘ CVE-2026-19445         CRITICAL     9.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19445
  │ ✘✔✘✘✘ CVE-2026-6100          CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-6100
  │ ✘✔✘✘✘ CVE-2020-10735         HIGH         7.5   4.5%   ·  ↳ S:UBUNTU-CVE-2020-10735
  │ ✘✔✘✘✘ CVE-2025-13836         HIGH         7.5   1.7%   ·  ↳ S:UBUNTU-CVE-2025-13836,USN-7951-1
  │ ✘✔✘✘✘ CVE-2025-69534         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2025-69534
  │ ✘✔✘✘✘ CVE-2025-8194          HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2025-8194,USN-7710-1
  │ ✘✔✘✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-11940
  │ ✘✔✘✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2026-11972
  │ ✘✔✘✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-15308,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-19553         HIGH         7.6   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19553
  │ ✘✔✘✘✘ CVE-2026-3644          HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-3644,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-4224          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-4224,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-4519          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-4519
  │ ✘✔✘✘✘ CVE-2026-4786          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-4786
  │ ✘✔✘✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57178
  │ ✘✔✘✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-7210
  │ ✘✔✘✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-82049
  │ ✘✔✘✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-84366
  │ ✘✔✘✘✘ CVE-2026-9669          HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-9669
  │ ✘✔✘✘✘ CVE-2021-23336         MEDIUM       5.9  40.7%   ·  ↳ S:UBUNTU-CVE-2021-23336
  │ ✘✔✘✘✘ CVE-2025-11468         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-11468
  │ ✘✔✘✘✘ CVE-2025-12084         MEDIUM       6.3   0.8%   ·  ↳ S:UBUNTU-CVE-2025-12084
  │ ✘✔✘✘✘ CVE-2025-12781         MEDIUM       6.3   0.9%   ·  ↳ S:UBUNTU-CVE-2025-12781
  │ ✘✔✘✘✘ CVE-2025-13837         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-13837
  │ ✘✔✘✘✘ CVE-2025-15282         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2025-15282
  │ ✘✔✘✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15366
  │ ✘✔✘✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15367
  │ ✘✔✘✘✘ CVE-2025-4516          MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2025-4516,USN-7570-1
  │ ✘✔✘✘✘ CVE-2025-6069          MEDIUM       4.3   0.6%   ·  ↳ S:UBUNTU-CVE-2025-6069,USN-7710-1
  │ ✘✔✘✘✘ CVE-2025-6075          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-6075,USN-7886-1
  │ ✘✔✘✘✘ CVE-2025-8291          MEDIUM       4.3   0.5%   ·  ↳ S:UBUNTU-CVE-2025-8291,USN-7886-1
  │ ✘✔✘✘✘ CVE-2026-0672          MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-0672
  │ ✘✔✘✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-0864
  │ ✘✔✘✘✘ CVE-2026-0865          MEDIUM       5.9   0.6%   ·  ↳ S:UBUNTU-CVE-2026-0865
  │ ✘✔✘✘✘ CVE-2026-114583        MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-114583
  │ ✘✔✘✘✘ CVE-2026-12345         MEDIUM       5.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-12345
  │ ✘✔✘✘✘ CVE-2026-1299          MEDIUM       6.0   0.6%   ·  ↳ S:UBUNTU-CVE-2026-1299
  │ ✘✔✘✘✘ CVE-2026-1502          MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-1502
  │ ✘✔✘✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15806
  │ ✘✔✘✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·  ↳ S:UBUNTU-CVE-2026-17084
  │ ✘✔✘✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19672
  │ ✘✔✘✘✘ CVE-2026-2297          MEDIUM       5.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-2297
  │ ✘✔✘✘✘ CVE-2026-3276          MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-3276
  │ ✘✔✘✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3446
  │ ✘✔✘✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57175
  │ ✘✔✘✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57176
  │ ✘✔✘✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57177
  │ ✘✔✘✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57179
  │ ✘✔✘✘✘ CVE-2026-6019          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6019,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-8328          MEDIUM       5.9   0.5%   ·  ↳ S:UBUNTU-CVE-2026-8328
  │ ✘✔✘✘✘ CVE-2026-87910         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-87910
  │ ✘✔✘✘✘ CVE-2025-13462         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2025-13462
  │ ✘✔✘✘✘ CVE-2025-1795          LOW          2.3   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1795,USN-7570-1
  │ ✘✔✘✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15310
  │ ✘✔✘✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18503
  │ ✘✔✘✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-6879
  │ ✘✔✘✘✘ USN-8018-1             ?             -       -   ·
  │ ✘✔✘✘✘ USN-8018-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.8-minimal@3.8.10-0ubuntu1~20.04.18
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2007-4559          CRITICAL     9.8  27.1%   ·  ↳ S:UBUNTU-CVE-2007-4559
  │ ✘✔✘✘✘ CVE-2026-115557        CRITICAL     9.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-115557
  │ ✘✔✘✘✘ CVE-2026-19445         CRITICAL     9.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19445
  │ ✘✔✘✘✘ CVE-2026-6100          CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-6100
  │ ✘✔✘✘✘ CVE-2020-10735         HIGH         7.5   4.5%   ·  ↳ S:UBUNTU-CVE-2020-10735
  │ ✘✔✘✘✘ CVE-2025-13836         HIGH         7.5   1.7%   ·  ↳ S:UBUNTU-CVE-2025-13836,USN-7951-1
  │ ✘✔✘✘✘ CVE-2025-69534         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2025-69534
  │ ✘✔✘✘✘ CVE-2025-8194          HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2025-8194,USN-7710-1
  │ ✘✔✘✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-11940
  │ ✘✔✘✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2026-11972
  │ ✘✔✘✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-15308,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-19553         HIGH         7.6   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19553
  │ ✘✔✘✘✘ CVE-2026-3644          HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-3644,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-4224          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-4224,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-4519          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-4519
  │ ✘✔✘✘✘ CVE-2026-4786          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-4786
  │ ✘✔✘✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57178
  │ ✘✔✘✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-7210
  │ ✘✔✘✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-82049
  │ ✘✔✘✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-84366
  │ ✘✔✘✘✘ CVE-2026-9669          HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-9669
  │ ✘✔✘✘✘ CVE-2021-23336         MEDIUM       5.9  40.7%   ·  ↳ S:UBUNTU-CVE-2021-23336
  │ ✘✔✘✘✘ CVE-2025-11468         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-11468
  │ ✘✔✘✘✘ CVE-2025-12084         MEDIUM       6.3   0.8%   ·  ↳ S:UBUNTU-CVE-2025-12084
  │ ✘✔✘✘✘ CVE-2025-12781         MEDIUM       6.3   0.9%   ·  ↳ S:UBUNTU-CVE-2025-12781
  │ ✘✔✘✘✘ CVE-2025-13837         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-13837
  │ ✘✔✘✘✘ CVE-2025-15282         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2025-15282
  │ ✘✔✘✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15366
  │ ✘✔✘✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15367
  │ ✘✔✘✘✔ CVE-2025-4516          MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2025-4516,USN-7570-1 | V:UB:CVE-2025-4516
  │ ✘✔✘✘✘ CVE-2025-6069          MEDIUM       4.3   0.6%   ·  ↳ S:UBUNTU-CVE-2025-6069,USN-7710-1
  │ ✘✔✘✘✘ CVE-2025-6075          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-6075,USN-7886-1
  │ ✘✔✘✘✘ CVE-2025-8291          MEDIUM       4.3   0.5%   ·  ↳ S:UBUNTU-CVE-2025-8291,USN-7886-1
  │ ✘✔✘✘✘ CVE-2026-0672          MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-0672
  │ ✘✔✘✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-0864
  │ ✘✔✘✘✘ CVE-2026-0865          MEDIUM       5.9   0.6%   ·  ↳ S:UBUNTU-CVE-2026-0865
  │ ✘✔✘✘✘ CVE-2026-114583        MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-114583
  │ ✘✔✘✘✘ CVE-2026-12345         MEDIUM       5.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-12345
  │ ✘✔✘✘✘ CVE-2026-1299          MEDIUM       6.0   0.6%   ·  ↳ S:UBUNTU-CVE-2026-1299
  │ ✘✔✘✘✘ CVE-2026-1502          MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-1502
  │ ✘✔✘✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15806
  │ ✘✔✘✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·  ↳ S:UBUNTU-CVE-2026-17084
  │ ✘✔✘✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19672
  │ ✘✔✘✘✔ CVE-2026-2297          MEDIUM       5.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-2297 | V:UB:CVE-2026-2297
  │ ✘✔✘✘✘ CVE-2026-3276          MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-3276
  │ ✘✔✘✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3446
  │ ✘✔✘✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57175
  │ ✘✔✘✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57176
  │ ✘✔✘✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57177
  │ ✘✔✘✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57179
  │ ✘✔✘✘✘ CVE-2026-6019          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6019,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-8328          MEDIUM       5.9   0.5%   ·  ↳ S:UBUNTU-CVE-2026-8328
  │ ✘✔✘✘✘ CVE-2026-87910         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-87910
  │ ✘✔✘✘✘ CVE-2025-13462         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2025-13462
  │ ✘✔✘✘✔ CVE-2025-1795          LOW          2.3   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1795,USN-7570-1 | V:UB:CVE-2025-1795
  │ ✘✔✘✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15310
  │ ✘✔✘✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18503
  │ ✘✔✘✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-6879
  │ ✘✔✘✘✘ USN-8018-1             ?             -       -   ·
  │ ✘✔✘✘✘ USN-8018-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libpython3.8-stdlib@3.8.10-0ubuntu1~20.04.18
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2007-4559          CRITICAL     9.8  27.1%   ·  ↳ S:UBUNTU-CVE-2007-4559
  │ ✘✔✘✘✘ CVE-2026-115557        CRITICAL     9.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-115557
  │ ✘✔✘✘✘ CVE-2026-19445         CRITICAL     9.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19445
  │ ✘✔✘✘✘ CVE-2026-6100          CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-6100
  │ ✘✔✘✘✘ CVE-2020-10735         HIGH         7.5   4.5%   ·  ↳ S:UBUNTU-CVE-2020-10735
  │ ✘✔✘✘✘ CVE-2025-13836         HIGH         7.5   1.7%   ·  ↳ S:UBUNTU-CVE-2025-13836,USN-7951-1
  │ ✘✔✘✘✘ CVE-2025-69534         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2025-69534
  │ ✘✔✘✘✘ CVE-2025-8194          HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2025-8194,USN-7710-1
  │ ✘✔✘✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-11940
  │ ✘✔✘✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2026-11972
  │ ✘✔✘✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-15308,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-19553         HIGH         7.6   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19553
  │ ✘✔✘✘✘ CVE-2026-3644          HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-3644,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-4224          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-4224,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-4519          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-4519
  │ ✘✔✘✘✘ CVE-2026-4786          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-4786
  │ ✘✔✘✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57178
  │ ✘✔✘✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-7210
  │ ✘✔✘✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-82049
  │ ✘✔✘✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-84366
  │ ✘✔✘✘✘ CVE-2026-9669          HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-9669
  │ ✘✔✘✘✘ CVE-2021-23336         MEDIUM       5.9  40.7%   ·  ↳ S:UBUNTU-CVE-2021-23336
  │ ✘✔✘✘✘ CVE-2025-11468         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-11468
  │ ✘✔✘✘✘ CVE-2025-12084         MEDIUM       6.3   0.8%   ·  ↳ S:UBUNTU-CVE-2025-12084
  │ ✘✔✘✘✘ CVE-2025-12781         MEDIUM       6.3   0.9%   ·  ↳ S:UBUNTU-CVE-2025-12781
  │ ✘✔✘✘✘ CVE-2025-13837         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-13837
  │ ✘✔✘✘✘ CVE-2025-15282         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2025-15282
  │ ✘✔✘✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15366
  │ ✘✔✘✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15367
  │ ✘✔✘✘✘ CVE-2025-4516          MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2025-4516,USN-7570-1
  │ ✘✔✘✘✘ CVE-2025-6069          MEDIUM       4.3   0.6%   ·  ↳ S:UBUNTU-CVE-2025-6069,USN-7710-1
  │ ✘✔✘✘✘ CVE-2025-6075          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-6075,USN-7886-1
  │ ✘✔✘✘✘ CVE-2025-8291          MEDIUM       4.3   0.5%   ·  ↳ S:UBUNTU-CVE-2025-8291,USN-7886-1
  │ ✘✔✘✘✘ CVE-2026-0672          MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-0672
  │ ✘✔✘✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-0864
  │ ✘✔✘✘✘ CVE-2026-0865          MEDIUM       5.9   0.6%   ·  ↳ S:UBUNTU-CVE-2026-0865
  │ ✘✔✘✘✘ CVE-2026-114583        MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-114583
  │ ✘✔✘✘✘ CVE-2026-12345         MEDIUM       5.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-12345
  │ ✘✔✘✘✘ CVE-2026-1299          MEDIUM       6.0   0.6%   ·  ↳ S:UBUNTU-CVE-2026-1299
  │ ✘✔✘✘✘ CVE-2026-1502          MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-1502
  │ ✘✔✘✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15806
  │ ✘✔✘✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·  ↳ S:UBUNTU-CVE-2026-17084
  │ ✘✔✘✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19672
  │ ✘✔✘✘✔ CVE-2026-2297          MEDIUM       5.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-2297 | V:UB:CVE-2026-2297
  │ ✘✔✘✘✘ CVE-2026-3276          MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-3276
  │ ✘✔✘✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3446
  │ ✘✔✘✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57175
  │ ✘✔✘✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57176
  │ ✘✔✘✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57177
  │ ✘✔✘✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57179
  │ ✘✔✘✘✘ CVE-2026-6019          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6019,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-8328          MEDIUM       5.9   0.5%   ·  ↳ S:UBUNTU-CVE-2026-8328
  │ ✘✔✘✘✘ CVE-2026-87910         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-87910
  │ ✘✔✘✘✘ CVE-2025-13462         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2025-13462
  │ ✘✔✘✘✘ CVE-2025-1795          LOW          2.3   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1795,USN-7570-1
  │ ✘✔✘✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15310
  │ ✘✔✘✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18503
  │ ✘✔✘✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-6879
  │ ✘✔✘✘✘ USN-8018-1             ?             -       -   ·
  │ ✘✔✘✘✘ USN-8018-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/librtmp1@2.4%2B20151223.gitfa8646d.1-2build1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-112060        MEDIUM       6.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-112060
  │ ✘✔✘✘✘ CVE-2026-112061        MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-112061
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsasl2-2@2.1.27%2Bdfsg-2ubuntu0.1
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2026-107161        HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-107161 | V:UB:CVE-2026-107161
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsasl2-modules@2.1.27%2Bdfsg-2ubuntu0.1
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2026-107161        HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-107161 | V:UB:CVE-2026-107161
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsasl2-modules-db@2.1.27%2Bdfsg-2ubuntu0.1
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2026-107161        HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-107161 | V:UB:CVE-2026-107161
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsmartcols1@2.34-0.1ubuntu9.6
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-53613         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53613
  │ ✘✔✘✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53615
  │ ✘✔✘✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-76642
  │ ✘✔✘✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78408
  │ ✘✔✘✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78409
  │ ✘✔✘✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78410
  │ ✘✔✘✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-14104
  │ ✘✔✘✘✘ CVE-2026-13595         MEDIUM       6.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-13595
  │ ✘✔✘✘✔ CVE-2026-27456         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-27456 | V:UB:CVE-2026-27456
  │ ✘✔✘✘✘ USN-8091-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsoup2.4-1@2.70.0-1ubuntu0.5
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2026-102560        CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-102560 | V:UB:CVE-2026-102560
  │ ✘✔✘✘✔ CVE-2026-2369          CRITICAL     9.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-2369,USN-8523-1 | V:UB:CVE-2026-2369
  │ ✘✔✘✘✔ CVE-2025-11021         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2025-11021 | V:UB:CVE-2025-11021
  │ ✘✔✘✘✔ CVE-2025-14523         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2025-14523 | V:UB:CVE-2025-14523
  │ ✘✔✘✘✔ CVE-2025-32049         HIGH         7.5   0.9%   ·  ↳ S:UBUNTU-CVE-2025-32049 | V:UB:CVE-2025-32049
  │ ✘✔✘✘✔ CVE-2025-4948          HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2025-4948,USN-7643-1 | V:UB:CVE-2025-4948
  │ ✘✔✘✘✔ CVE-2026-0719          HIGH         8.6   0.6%   ·  ↳ S:UBUNTU-CVE-2026-0719 | V:UB:CVE-2026-0719
  │ ✘✔✘✘✔ CVE-2026-102555        HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-102555 | V:UB:CVE-2026-102555
  │ ✘✔✘✘✔ CVE-2026-102556        HIGH         8.6   0.4%   ·  ↳ S:UBUNTU-CVE-2026-102556 | V:UB:CVE-2026-102556
  │ ✘✔✘✘✔ CVE-2026-102557        HIGH         8.6   0.4%   ·  ↳ S:UBUNTU-CVE-2026-102557 | V:UB:CVE-2026-102557
  │ ✘✔✘✘✔ CVE-2026-102558        HIGH         8.6   0.5%   ·  ↳ S:UBUNTU-CVE-2026-102558 | V:UB:CVE-2026-102558
  │ ✘✔✘✘✔ CVE-2026-102559        HIGH         8.6   0.5%   ·  ↳ S:UBUNTU-CVE-2026-102559 | V:UB:CVE-2026-102559
  │ ✘✔✘✘✘ CVE-2026-15709         HIGH         7.5   0.9%   ·  ↳ S:UBUNTU-CVE-2026-15709
  │ ✘✔✘✘✘ CVE-2026-15711         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-15711
  │ ✘✔✘✘✘ CVE-2026-1761          HIGH         8.6   1.1%   ·  ↳ S:UBUNTU-CVE-2026-1761
  │ ✘✔✘✘✔ CVE-2026-3099          HIGH         7.3   0.4%   ·  ↳ S:UBUNTU-CVE-2026-3099 | V:UB:CVE-2026-3099
  │ ✘✔✘✘✔ CVE-2026-5119          HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-5119,USN-8523-1,USN-8890-1 | V:UB:CVE-2026-5119
  │ ✘✔✘✘✔ CVE-2026-66338         HIGH         7.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-66338 | V:UB:CVE-2026-66338
  │ ✘✔✘✘✔ CVE-2025-32907         MEDIUM       5.3   0.7%   ·  ↳ S:UBUNTU-CVE-2025-32907,USN-7643-1 | V:UB:CVE-2025-32907
  │ ✘✔✘✘✔ CVE-2025-4035          MEDIUM       4.3   0.4%   ·  ↳ S:UBUNTU-CVE-2025-4035 | V:UB:CVE-2025-4035
  │ ✘✔✘✘✔ CVE-2025-4969          MEDIUM       6.5   0.9%   ·  ↳ S:UBUNTU-CVE-2025-4969,USN-7643-1 | V:UB:CVE-2025-4969
  │ ✘✔✘✘✔ CVE-2025-9901          MEDIUM       5.9   0.5%   ·  ↳ S:UBUNTU-CVE-2025-9901 | V:UB:CVE-2025-9901
  │ ✘✔✘✘✔ CVE-2026-0716          MEDIUM       4.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-0716 | V:UB:CVE-2026-0716
  │ ✘✔✘✘✔ CVE-2026-103399        MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-103399 | V:UB:CVE-2026-103399
  │ ✘✔✘✘✔ CVE-2026-12548         MEDIUM       4.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-12548 | V:UB:CVE-2026-12548
  │ ✘✔✘✘✔ CVE-2026-12549         MEDIUM       4.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-12549 | V:UB:CVE-2026-12549
  │ ✘✔✘✘✔ CVE-2026-1467          MEDIUM       5.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-1467,USN-8780-1 | V:UB:CVE-2026-1467
  │ ✘✔✘✘✔ CVE-2026-1539          MEDIUM       5.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-1539,USN-8780-1 | V:UB:CVE-2026-1539
  │ ✘✔✘✘✘ CVE-2026-15714         MEDIUM       6.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-15714
  │ ✘✔✘✘✘ CVE-2026-1760          MEDIUM       5.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-1760
  │ ✘✔✘✘✔ CVE-2026-1801          MEDIUM       6.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-1801,USN-8780-1 | V:UB:CVE-2026-1801
  │ ✘✔✘✘✘ CVE-2026-2443          MEDIUM       5.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-2443
  │ ✘✔✘✘✘ CVE-2026-2708          MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-2708
  │ ✘✔✘✘✔ CVE-2026-3632          MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3632 | V:UB:CVE-2026-3632
  │ ✘✔✘✘✔ CVE-2026-3633          MEDIUM       6.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3633 | V:UB:CVE-2026-3633
  │ ✘✔✘✘✔ CVE-2026-3634          MEDIUM       6.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3634 | V:UB:CVE-2026-3634
  │ ✘✔✘✘✘ CVE-2026-6324          MEDIUM       4.8   0.9%   ·  ↳ S:UBUNTU-CVE-2026-6324,USN-8890-1
  │ ✘✔✘✘✔ CVE-2026-66337         MEDIUM       6.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-66337 | V:UB:CVE-2026-66337
  │ ✘✔✘✘✔ CVE-2026-66339         MEDIUM       6.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-66339,USN-8890-1 | V:UB:CVE-2026-66339
  │ ✘✔✘✘✔ CVE-2026-77014         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-77014,USN-8890-1 | V:UB:CVE-2026-77014
  │ ✘✔✘✘✔ CVE-2026-77680         MEDIUM       5.3   0.7%   ·  ↳ S:UBUNTU-CVE-2026-77680,USN-8890-1 | V:UB:CVE-2026-77680
  │ ✘✔✘✘✔ CVE-2025-4945          LOW          3.7   0.7%   ·  ↳ S:UBUNTU-CVE-2025-4945,USN-7643-1 | V:UB:CVE-2025-4945
  │ ✘✔✘✘✔ CVE-2026-12547         LOW          3.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-12547 | V:UB:CVE-2026-12547
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsqlite3-0@3.31.1-4ubuntu0.7
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2025-6965          HIGH         7.7  73.5%   ·  ↳ S:UBUNTU-CVE-2025-6965,USN-7679-1 | V:UB:CVE-2025-6965
  │ ✘✔✘✘✘ CVE-2026-11824         HIGH         8.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-11824
  │ ✘✔✘✘✘ CVE-2026-11822         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-11822
  │ ✘✔✘✘✔ CVE-2026-39113         MEDIUM       4.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-39113,USN-8775-1 | V:UB:CVE-2026-39113
  │ ✘✔✘✘✘ CVE-2026-50812         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-50812
  │ ✘✔✘✘✘ CVE-2026-50813         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-50813
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libssh-4@0.9.3-2ubuntu2.5
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2025-5318          HIGH         8.1   1.9%   ·  ↳ S:UBUNTU-CVE-2025-5318,USN-7696-1 | V:UB:CVE-2025-5318
  │ ✘✔✘✘✘ CVE-2025-5372          HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-5372
  │ ✘✔✘✘✔ CVE-2026-0966          HIGH         8.2   0.6%   ·  ↳ S:UBUNTU-CVE-2026-0966 | V:UB:CVE-2026-0966
  │ ✘✔✘✘✔ CVE-2026-3731          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-3731,USN-8093-1 | V:UB:CVE-2026-3731
  │ ✘✔✘✘✘ CVE-2026-59847         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-59847
  │ ✘✔✘✘✘ CVE-2026-59850         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-59850
  │ ✘✔✘✘✔ CVE-2025-4877          MEDIUM       4.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-4877,USN-7696-1 | V:UB:CVE-2025-4877
  │ ✘✔✘✘✔ CVE-2025-8114          MEDIUM       4.7   0.3%   ·  ↳ S:UBUNTU-CVE-2025-8114,USN-7849-1 | V:UB:CVE-2025-8114
  │ ✘✔✘✘✔ CVE-2026-0964          MEDIUM       6.3   0.4%   ·  ↳ S:UBUNTU-CVE-2026-0964 | V:UB:CVE-2026-0964
  │ ✘✔✘✘✔ CVE-2026-0967          MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-0967 | V:UB:CVE-2026-0967
  │ ✘✔✘✘✘ CVE-2026-59843         MEDIUM       6.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-59843
  │ ✘✔✘✘✔ CVE-2026-59845         MEDIUM       5.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-59845 | V:UB:CVE-2026-59845
  │ ✘✔✘✘✘ CVE-2026-59848         MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-59848
  │ ✘✔✘✘✔ CVE-2025-4878          LOW          3.6   0.2%   ·  ↳ S:UBUNTU-CVE-2025-4878,USN-7696-1 | V:UB:CVE-2025-4878
  │ ✘✔✘✘✔ CVE-2025-8277          LOW          3.1   0.4%   ·  ↳ S:UBUNTU-CVE-2025-8277 | V:UB:CVE-2025-8277
  │ ✘✔✘✘✔ CVE-2026-0965          LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-0965 | V:UB:CVE-2026-0965
  │ ✘✔✘✘✔ CVE-2026-0968          LOW          3.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-0968 | V:UB:CVE-2026-0968
  │ ✘✔✘✘✘ CVE-2026-59846         LOW          3.9   0.1%   ·  ↳ S:UBUNTU-CVE-2026-59846
  │ ✘✔✘✘✘ USN-8051-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libssl1.1@1.1.1f-1ubuntu2.24
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2025-69419         HIGH         7.4   0.6%   ·  ↳ S:UBUNTU-CVE-2025-69419 | V:UB:CVE-2025-69419
  │ ✘✔✘✘✔ CVE-2025-69420         HIGH         7.5   0.9%   ·  ↳ S:UBUNTU-CVE-2025-69420 | V:UB:CVE-2025-69420
  │ ✘✔✘✘✔ CVE-2025-69421         HIGH         7.5   0.9%   ·  ↳ S:UBUNTU-CVE-2025-69421 | V:UB:CVE-2025-69421
  │ ✘✔✘✘✔ CVE-2025-9230          HIGH         7.5   1.6%   ·  ↳ S:UBUNTU-CVE-2025-9230,USN-7786-1 | V:UB:CVE-2025-9230
  │ ✘✔✘✘✔ CVE-2026-28387         HIGH         8.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-28387 | V:UB:CVE-2026-28387
  │ ✘✔✘✘✔ CVE-2026-28388         HIGH         7.5   0.9%   ·  ↳ S:UBUNTU-CVE-2026-28388 | V:UB:CVE-2026-28388
  │ ✘✔✘✘✔ CVE-2026-28389         HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2026-28389 | V:UB:CVE-2026-28389
  │ ✘✔✘✘✔ CVE-2026-28390         HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2026-28390 | V:UB:CVE-2026-28390
  │ ✘✔✘✘✘ CVE-2026-34180         HIGH         7.5   1.0%   ·  ↳ S:UBUNTU-CVE-2026-34180
  │ ✘✔✘✘✘ CVE-2026-45447         HIGH         8.8   4.0%   ·  ↳ S:UBUNTU-CVE-2026-45447
  │ ✘✔✘✘✔ CVE-2026-54874         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-54874,USN-8678-2 | V:UB:CVE-2026-54874
  │ ✘✔✘✘✔ CVE-2026-63072         HIGH         7.5   0.9%   ·  ↳ S:UBUNTU-CVE-2026-63072,USN-8678-2 | V:UB:CVE-2026-63072
  │ ✘✔✘✘✘ CVE-2026-7383          HIGH         8.1   0.8%   ·  ↳ S:UBUNTU-CVE-2026-7383
  │ ✘✔✘✘✔ CVE-2026-84782         HIGH         8.2   0.8%   ·  ↳ S:UBUNTU-CVE-2026-84782,USN-8847-2 | V:UB:CVE-2026-84782
  │ ✘✔✘✘✘ CVE-2026-9076          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-9076
  │ ✘✔✘✘✔ CVE-2025-68160         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68160 | V:UB:CVE-2025-68160
  │ ✘✔✘✘✔ CVE-2025-69418         MEDIUM       4.0   0.1%   ·  ↳ S:UBUNTU-CVE-2025-69418 | V:UB:CVE-2025-69418
  │ ✘✔✘✘✔ CVE-2026-22795         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-22795 | V:UB:CVE-2026-22795
  │ ✘✔✘✘✔ CVE-2026-22796         MEDIUM       5.3   0.6%   ·  ↳ S:UBUNTU-CVE-2026-22796 | V:UB:CVE-2026-22796
  │ ✘✔✘✘✔ CVE-2026-35189         MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-35189,USN-8847-2 | V:UB:CVE-2026-35189
  │ ✘✔✘✘✘ CVE-2026-42766         MEDIUM       5.9   1.1%   ·  ↳ S:UBUNTU-CVE-2026-42766
  │ ✘✔✘✘✘ CVE-2026-75806         MEDIUM       5.3   1.1%   ·  ↳ S:UBUNTU-CVE-2026-75806
  │ ✘✔✘✘✔ CVE-2026-54872         LOW          3.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-54872,USN-8847-2 | V:UB:CVE-2026-54872
  │ ✘✔✘✘✔ CVE-2026-77696         LOW          3.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-77696,USN-8847-2 | V:UB:CVE-2026-77696
  │ ✘✔✘✘✘ USN-7980-2             ?             -       -   ·
  │ ✘✔✘✘✘ USN-8155-2             ?             -       -   ·
  │ ✘✔✘✘✘ USN-8414-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libstdc%2B%2B-9-dev@9.4.0-1ubuntu1~20.04.2
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2020-23026         HIGH         7.5   1.1%   ·  ↳ S:UBUNTU-CVE-2020-23026
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✘ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ S:UBUNTU-CVE-2023-4039
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libstdc%2B%2B6@10.5.0-1ubuntu1~20.04
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ S:UBUNTU-CVE-2023-4039,USN-7700-1 | V:UB:CVE-2023-4039
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libsystemd0@245.4-4ubuntu3.24
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2023-26604         HIGH         7.8   1.1%   ·  ↳ S:UBUNTU-CVE-2023-26604 | V:UB:CVE-2023-26604
  │ ✘✔✘✘✘ CVE-2020-13776         MEDIUM       6.7   0.5%   ·  ↳ S:UBUNTU-CVE-2020-13776
  │ ✘✔✘✘✔ CVE-2023-7008          MEDIUM       5.9   0.8%   ·  ↳ S:UBUNTU-CVE-2023-7008 | V:UB:CVE-2023-7008
  │ ✘✔✘✘✘ CVE-2025-4598          MEDIUM       4.7   1.3%   ·  ↳ S:UBUNTU-CVE-2025-4598,USN-7559-1
  │ ✘✔✘✘✔ CVE-2026-29111         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-29111 | V:UB:CVE-2026-29111
  │ ✘✔✘✘✔ CVE-2026-40225         MEDIUM       6.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-40225 | V:UB:CVE-2026-40225
  │ ✘✔✘✘✘ CVE-2026-40226         MEDIUM       6.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-40226
  │ ✘✔✘✘✔ CVE-2026-40228         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-40228 | V:UB:CVE-2026-40228
  │ ✘✔✘✘✘ USN-8119-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libtasn1-6@4.16.0-2ubuntu0.1
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2021-46848         CRITICAL     9.1   2.8%   ·  ↳ O:UBUNTU-CVE-2021-46848 | S:UBUNTU-CVE-2021-46848 | V:UB:CVE-2021-46848
  │ ✔✔✔✘✔ CVE-2025-13151         HIGH         7.5   1.4%   ·  ↳ O:UBUNTU-CVE-2025-13151 | S:UBUNTU-CVE-2025-13151 | V:UB:CVE-2025-13151
  │ ✔✔✘✘✘ USN-7954-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libtinfo6@6.2-0ubuntu2.1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-69720         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-69720,USN-8503-1
  │ ✘✔✘✘✔ CVE-2023-50495         MEDIUM       6.5   1.0%   ·  ↳ S:UBUNTU-CVE-2023-50495 | V:UB:CVE-2023-50495
  │ ✘✔✘✘✔ CVE-2025-6141          MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-6141,USN-8709-1 | V:UB:CVE-2025-6141
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libtsan0@10.5.0-1ubuntu1~20.04
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ S:UBUNTU-CVE-2023-4039,USN-7700-1 | V:UB:CVE-2023-4039
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libubsan1@10.5.0-1ubuntu1~20.04
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-102010        HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-102010
  │ ✘✔✘✘✘ CVE-2026-95619         HIGH         7.7   0.4%   ·  ↳ S:UBUNTU-CVE-2026-95619
  │ ✘✔✘✘✔ CVE-2023-4039          MEDIUM       4.8   1.0%   ·  ↳ S:UBUNTU-CVE-2023-4039,USN-7700-1 | V:UB:CVE-2023-4039
  │ ✘✔✘✘✘ CVE-2026-114690        MEDIUM       6.2   0.1%   ·  ↳ S:UBUNTU-CVE-2026-114690
  │ ✘✔✘✘✘ CVE-2026-114691        MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-114691
  │ ✘✔✘✘✘ CVE-2026-115455        MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-115455
  │ ✘✔✘✘✘ CVE-2026-115456        LOW          3.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-115456
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libudev1@245.4-4ubuntu3.24
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2023-26604         HIGH         7.8   1.1%   ·  ↳ S:UBUNTU-CVE-2023-26604 | V:UB:CVE-2023-26604
  │ ✘✔✘✘✘ CVE-2020-13776         MEDIUM       6.7   0.5%   ·  ↳ S:UBUNTU-CVE-2020-13776
  │ ✘✔✘✘✔ CVE-2023-7008          MEDIUM       5.9   0.8%   ·  ↳ S:UBUNTU-CVE-2023-7008 | V:UB:CVE-2023-7008
  │ ✘✔✘✘✘ CVE-2025-4598          MEDIUM       4.7   1.3%   ·  ↳ S:UBUNTU-CVE-2025-4598,USN-7559-1
  │ ✘✔✘✘✔ CVE-2026-29111         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-29111 | V:UB:CVE-2026-29111
  │ ✘✔✘✘✔ CVE-2026-40225         MEDIUM       6.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-40225 | V:UB:CVE-2026-40225
  │ ✘✔✘✘✘ CVE-2026-40226         MEDIUM       6.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-40226
  │ ✘✔✘✘✔ CVE-2026-40228         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-40228 | V:UB:CVE-2026-40228
  │ ✘✔✘✘✘ USN-8119-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libuuid1@2.34-0.1ubuntu9.6
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-53613         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53613
  │ ✘✔✘✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53615
  │ ✘✔✘✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-76642
  │ ✘✔✘✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78408
  │ ✘✔✘✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78409
  │ ✘✔✘✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78410
  │ ✘✔✘✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-14104
  │ ✘✔✘✘✘ CVE-2026-13595         MEDIUM       6.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-13595
  │ ✘✔✘✘✔ CVE-2026-27456         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-27456 | V:UB:CVE-2026-27456
  │ ✘✔✘✘✘ USN-8091-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/libxml2@2.9.10%2Bdfsg-5ubuntu0.20.04.10
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2025-49794         CRITICAL     9.1   0.8%   ·  ↳ O:UBUNTU-CVE-2025-49794,USN-7694-1 | S:UBUNTU-CVE-2025-49794,USN-7694-1 | V:UB:CVE-2025-49794
  │ ✔✔✔✘✔ CVE-2025-49796         CRITICAL     9.1   1.6%   ·  ↳ O:UBUNTU-CVE-2025-49796,USN-7694-1 | S:UBUNTU-CVE-2025-49796,USN-7694-1 | V:UB:CVE-2025-49796
  │ ✔✔✔✘✔ CVE-2025-6021          HIGH         7.5   1.4%   ·  ↳ O:UBUNTU-CVE-2025-6021,USN-7694-1 | S:UBUNTU-CVE-2025-6021,USN-7694-1 | V:UB:CVE-2025-6021
  │ ✔✔✔✘✔ CVE-2025-7425          HIGH         7.8   0.4%   ·  ↳ O:UBUNTU-CVE-2025-7425,USN-7852-2 | S:UBUNTU-CVE-2025-7425,USN-7852-2 | V:UB:CVE-2025-7425
  │ ✔✔✔✘✘ CVE-2026-11979         HIGH         7.8   0.1%   ·  ↳ O:UBUNTU-CVE-2026-11979 | S:UBUNTU-CVE-2026-11979
  │ ✔✔✔✘✔ CVE-2026-74860         HIGH         8.5   0.7%   ·  ↳ O:UBUNTU-CVE-2026-74860,USN-8787-1 | S:UBUNTU-CVE-2026-74860,USN-8787-1 | V:UB:CVE-2026-74860
  │ ✔✔✔✘✔ CVE-2026-86138         HIGH         7.8   0.1%   ·  ↳ O:UBUNTU-CVE-2026-86138,USN-8910-1 | S:UBUNTU-CVE-2026-86138,USN-8910-1 | V:UB:CVE-2026-86138
  │ ✔✔✔✘✔ CVE-2026-86140         HIGH         8.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-86140,USN-8787-1 | S:UBUNTU-CVE-2026-86140,USN-8787-1 | V:UB:CVE-2026-86140
  │ ✔✔✔✘✔ CVE-2026-86142         HIGH         7.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-86142,USN-8910-1 | S:UBUNTU-CVE-2026-86142,USN-8910-1 | V:UB:CVE-2026-86142
  │ ✔✔✔✘✔ CVE-2026-86143         HIGH         7.3   0.2%   ·  ↳ O:UBUNTU-CVE-2026-86143,USN-8910-1 | S:UBUNTU-CVE-2026-86143,USN-8910-1 | V:UB:CVE-2026-86143
  │ ✔✔✔✘✔ CVE-2026-86144         HIGH         7.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-86144,USN-8910-1 | S:UBUNTU-CVE-2026-86144,USN-8910-1 | V:UB:CVE-2026-86144
  │ ✔✔✘✘✘ CVE-2025-26434         MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2025-26434 | S:UBUNTU-CVE-2025-26434
  │ ✔✔✔✘✔ CVE-2025-8732          MEDIUM       4.8   0.2%   ·  ↳ O:UBUNTU-CVE-2025-8732 | S:UBUNTU-CVE-2025-8732 | V:UB:CVE-2025-8732
  │ ✔✔✔✘✔ CVE-2025-9714          MEDIUM       6.2   0.2%   ·  ↳ O:UBUNTU-CVE-2025-9714,USN-7743-1 | S:UBUNTU-CVE-2025-9714,USN-7743-1 | V:UB:CVE-2025-9714
  │ ✔✔✔✘✔ CVE-2026-0990          MEDIUM       5.9   1.0%   ·  ↳ O:UBUNTU-CVE-2026-0990 | S:UBUNTU-CVE-2026-0990 | V:UB:CVE-2026-0990
  │ ✔✔✔✘✔ CVE-2026-76781         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2026-76781,USN-8910-1 | S:UBUNTU-CVE-2026-76781,USN-8910-1 | V:UB:CVE-2026-76781
  │ ✔✔✔✘✔ CVE-2025-6170          LOW          2.5   0.3%   ·  ↳ O:UBUNTU-CVE-2025-6170,USN-7694-1 | S:UBUNTU-CVE-2025-6170,USN-7694-1 | V:UB:CVE-2025-6170
  │ ✔✔✔✘✔ CVE-2026-0989          LOW          3.7   0.5%   ·  ↳ O:UBUNTU-CVE-2026-0989 | S:UBUNTU-CVE-2026-0989 | V:UB:CVE-2026-0989
  │ ✔✔✔✘✔ CVE-2026-0992          LOW          2.9   0.5%   ·  ↳ O:UBUNTU-CVE-2026-0992 | S:UBUNTU-CVE-2026-0992 | V:UB:CVE-2026-0992
  │ ✔✔✘✘✘ USN-7974-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/linux-libc-dev@5.4.0-216.236
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2021-3773          CRITICAL     9.8   5.3%   ·  ↳ S:UBUNTU-CVE-2021-3773
  │ ✘✔✘✘✘ CVE-2021-47378         CRITICAL     9.8   1.2%   ·  ↳ S:UBUNTU-CVE-2021-47378,USN-8666-1
  │ ✘✔✘✘✘ CVE-2021-47544         CRITICAL     9.8   0.9%   ·  ↳ S:UBUNTU-CVE-2021-47544
  │ ✘✔✘✘✘ CVE-2022-48673         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2022-48673
  │ ✘✔✘✘✘ CVE-2022-48828         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2022-48828
  │ ✘✔✘✘✘ CVE-2022-48829         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2022-48829
  │ ✘✔✘✘✘ CVE-2022-49149         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2022-49149,USN-8919-1
  │ ✘✔✘✘✘ CVE-2022-49194         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2022-49194
  │ ✘✔✘✘✘ CVE-2022-49201         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2022-49201,USN-8919-1
  │ ✘✔✘✘✘ CVE-2022-50335         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2022-50335
  │ ✘✔✘✘✘ CVE-2022-50350         CRITICAL     9.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-50350
  │ ✘✔✘✘✘ CVE-2022-50410         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2022-50410
  │ ✘✔✘✘✘ CVE-2022-50666         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2022-50666
  │ ✘✔✘✘✘ CVE-2023-52515         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2023-52515
  │ ✘✔✘✘✘ CVE-2023-52732         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2023-52732
  │ ✘✔✘✘✘ CVE-2023-52735         CRITICAL     9.1   1.2%   ·  ↳ S:UBUNTU-CVE-2023-52735
  │ ✘✔✘✘✘ CVE-2023-53517         CRITICAL     9.8   0.3%   ·  ↳ S:UBUNTU-CVE-2023-53517
  │ ✘✔✘✘✘ CVE-2023-53751         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2023-53751
  │ ✘✔✘✘✘ CVE-2023-53794         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2023-53794
  │ ✘✔✘✘✘ CVE-2023-53867         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2023-53867
  │ ✘✔✘✘✘ CVE-2024-35865         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2024-35865
  │ ✘✔✘✘✘ CVE-2024-35870         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2024-35870
  │ ✘✔✘✘✘ CVE-2024-38541         CRITICAL     9.8   0.9%   ·  ↳ S:UBUNTU-CVE-2024-38541,USN-7701-1
  │ ✘✔✘✘✘ CVE-2024-40999         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2024-40999
  │ ✘✔✘✘✘ CVE-2024-46695         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2024-46695
  │ ✘✔✘✘✘ CVE-2024-47678         CRITICAL     9.4   0.6%   ·  ↳ S:UBUNTU-CVE-2024-47678
  │ ✘✔✘✘✘ CVE-2024-49571         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2024-49571
  │ ✘✔✘✘✘ CVE-2024-49855         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2024-49855
  │ ✘✔✘✘✘ CVE-2024-50047         CRITICAL     9.8   0.5%   ·  ↳ S:LSN-0113-1,LSN-0115-1,UBUNTU-CVE-2024-50047,USN-7671-1
  │ ✘✔✘✘✘ CVE-2024-50106         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2024-50106
  │ ✘✔✘✘✘ CVE-2024-50154         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2024-50154
  │ ✘✔✘✘✘ CVE-2024-53058         CRITICAL     9.4   0.6%   ·  ↳ S:UBUNTU-CVE-2024-53058
  │ ✘✔✘✘✘ CVE-2024-53095         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2024-53095
  │ ✘✔✘✘✘ CVE-2024-53179         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2024-53179
  │ ✘✔✘✘✘ CVE-2024-56640         CRITICAL     9.8   0.6%   ·  ↳ S:LSN-0119-1,UBUNTU-CVE-2024-56640,USN-8098-1
  │ ✘✔✘✘✘ CVE-2025-10263         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2025-10263
  │ ✘✔✘✘✘ CVE-2025-21796         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2025-21796,USN-7795-1
  │ ✘✔✘✘✘ CVE-2025-21927         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2025-21927
  │ ✘✔✘✘✘ CVE-2025-22021         CRITICAL    10.0   0.5%   ·  ↳ S:UBUNTU-CVE-2025-22021,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-27558         CRITICAL     9.1   0.3%   ·  ↳ S:UBUNTU-CVE-2025-27558,USN-8666-1
  │ ✘✔✘✘✘ CVE-2025-37879         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2025-37879
  │ ✘✔✘✘✘ CVE-2025-38075         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-38075
  │ ✘✔✘✘✘ CVE-2025-38211         CRITICAL     9.8   0.4%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-38211
  │ ✘✔✘✘✘ CVE-2025-38264         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2025-38264
  │ ✘✔✘✘✘ CVE-2025-38430         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2025-38430
  │ ✘✔✘✘✘ CVE-2025-38439         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2025-38439
  │ ✘✔✘✘✘ CVE-2025-38488         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2025-38488
  │ ✘✔✘✘✘ CVE-2025-38527         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2025-38527
  │ ✘✔✘✘✘ CVE-2025-38708         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2025-38708
  │ ✘✔✘✘✘ CVE-2025-38724         CRITICAL     9.8   0.4%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-38724,USN-8851-1
  │ ✘✔✘✘✘ CVE-2025-38728         CRITICAL     9.1   0.3%   ·  ↳ S:UBUNTU-CVE-2025-38728
  │ ✘✔✘✘✘ CVE-2025-39702         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2025-39702
  │ ✘✔✘✘✘ CVE-2025-39726         CRITICAL     9.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39726
  │ ✘✔✘✘✘ CVE-2025-39841         CRITICAL     9.8   0.5%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-39841
  │ ✘✔✘✘✘ CVE-2025-39932         CRITICAL     9.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-39932
  │ ✘✔✘✘✘ CVE-2025-39933         CRITICAL     9.4   0.3%   ·  ↳ S:UBUNTU-CVE-2025-39933
  │ ✘✔✘✘✘ CVE-2025-40074         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-40074
  │ ✘✔✘✘✘ CVE-2025-40099         CRITICAL     9.4   0.4%   ·  ↳ S:UBUNTU-CVE-2025-40099
  │ ✘✔✘✘✘ CVE-2025-40252         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2025-40252
  │ ✘✔✘✘✘ CVE-2025-40343         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2025-40343
  │ ✘✔✘✘✘ CVE-2025-68192         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2025-68192
  │ ✘✔✘✘✘ CVE-2025-68285         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2025-68285
  │ ✘✔✘✘✘ CVE-2025-68315         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2025-68315
  │ ✘✔✘✘✘ CVE-2025-68745         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-68745
  │ ✘✔✘✘✘ CVE-2025-68794         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2025-68794
  │ ✘✔✘✘✘ CVE-2025-71093         CRITICAL     9.1   0.3%   ·  ↳ S:UBUNTU-CVE-2025-71093
  │ ✘✔✘✘✘ CVE-2025-71116         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2025-71116
  │ ✘✔✘✘✘ CVE-2025-71183         CRITICAL     9.1   0.3%   ·  ↳ S:UBUNTU-CVE-2025-71183
  │ ✘✔✘✘✘ CVE-2026-100075        CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-100075
  │ ✘✔✘✘✘ CVE-2026-23112         CRITICAL     9.8   0.5%   ·  ↳ S:LSN-120-1,UBUNTU-CVE-2026-23112,USN-8273-1
  │ ✘✔✘✘✘ CVE-2026-23240         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-23240
  │ ✘✔✘✘✘ CVE-2026-23455         CRITICAL     9.1   1.6%   ·  ↳ S:LSN-0121-1,LSN-0122-1,UBUNTU-CVE-2026-23455,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-25702         CRITICAL     9.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-25702
  │ ✘✔✘✘✘ CVE-2026-31402         CRITICAL     9.8   1.2%   ·  ↳ S:LSN-0121-1,LSN-0122-1,UBUNTU-CVE-2026-31402,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-31405         CRITICAL     9.8   0.5%   ·  ↳ S:LSN-0121-1,LSN-0122-1,UBUNTU-CVE-2026-31405,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-31414         CRITICAL     9.8   0.6%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-31414,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-31448         CRITICAL     9.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-31448,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-31533         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-31533
  │ ✘✔✘✘✘ CVE-2026-31607         CRITICAL     9.8   0.3%   ·  ↳ S:LSN-0121-1,UBUNTU-CVE-2026-31607,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-31637         CRITICAL     9.8   0.6%   ·  ↳ S:LSN-0121-1,UBUNTU-CVE-2026-31637,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-31649         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-31649,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-31657         CRITICAL     9.8   0.4%   ·  ↳ S:LSN-0121-1,LSN-0122-1,UBUNTU-CVE-2026-31657,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-31659         CRITICAL     9.8   0.4%   ·  ↳ S:LSN-0121-1,UBUNTU-CVE-2026-31659,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-31668         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-31668,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-31682         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-31682,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-31685         CRITICAL     9.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-31685,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-43011         CRITICAL     9.8   0.6%   ·  ↳ S:LSN-0121-1,UBUNTU-CVE-2026-43011,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-43037         CRITICAL     9.8   0.7%   ·  ↳ S:LSN-0121-1,UBUNTU-CVE-2026-43037,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-43038         CRITICAL     9.8   0.3%   ·  ↳ S:LSN-0121-1,LSN-0122-1,UBUNTU-CVE-2026-43038,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-43071         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-43071,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-43117         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-43117,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-43198         CRITICAL     9.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-43198,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-43383         CRITICAL     9.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-43383,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-43407         CRITICAL     9.1   0.7%   ·  ↳ S:LSN-0121-1,UBUNTU-CVE-2026-43407,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-43414         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-43414,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-43493         CRITICAL     9.8   0.7%   ·  ↳ S:LSN-0121-1,LSN-0122-1,UBUNTU-CVE-2026-43493,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-45988         CRITICAL     9.8   0.5%   ·  ↳ S:LSN-0121-1,UBUNTU-CVE-2026-45988,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-46043         CRITICAL     9.1   0.5%   ·  ↳ S:LSN-0121-1,UBUNTU-CVE-2026-46043,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-46119         CRITICAL     9.1   0.5%   ·  ↳ S:LSN-0121-1,UBUNTU-CVE-2026-46119,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-46135         CRITICAL     9.8   0.4%   ·  ↳ S:LSN-0121-1,UBUNTU-CVE-2026-46135,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-46266         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-46266,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-52914         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-52914,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-52924         CRITICAL     9.8   0.7%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-52924,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-52931         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-52931,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-52955         CRITICAL     9.8   0.4%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-52955,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-52958         CRITICAL     9.1   0.7%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-52958,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-52982         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-52982,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-52986         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-52986,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-52989         CRITICAL     9.8   0.4%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-52989,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-52993         CRITICAL     9.8   0.4%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-52993,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-52999         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-52999,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-53002         CRITICAL     9.8   0.4%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-53002,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-53006         CRITICAL     9.8   0.4%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-53006,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-53043         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53043,USN-8714-1
  │ ✘✔✘✘✘ CVE-2026-53045         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53045,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-53086         CRITICAL     9.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53086
  │ ✘✔✘✘✘ CVE-2026-53088         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-53088,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-53131         CRITICAL     9.4   0.4%   ·  ↳ S:UBUNTU-CVE-2026-53131,USN-8851-1
  │ ✘✔✘✘✘ CVE-2026-53176         CRITICAL     9.8   0.8%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-53176,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-53186         CRITICAL     9.1   0.5%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-53186
  │ ✘✔✘✘✘ CVE-2026-53221         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-53221,USN-8851-1
  │ ✘✔✘✘✘ CVE-2026-53224         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-53224,USN-8714-1
  │ ✘✔✘✘✘ CVE-2026-53225         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-53225,USN-8714-1
  │ ✘✔✘✘✘ CVE-2026-53228         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-53228,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-53246         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-53246,USN-8714-1
  │ ✘✔✘✘✘ CVE-2026-53309         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-53309,USN-8714-1
  │ ✘✔✘✘✘ CVE-2026-53355         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-53355
  │ ✘✔✘✘✘ CVE-2026-53399         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-53399
  │ ✘✔✘✘✘ CVE-2026-63800         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-63800
  │ ✘✔✘✘✘ CVE-2026-63825         CRITICAL     9.8   0.9%   ·  ↳ S:UBUNTU-CVE-2026-63825
  │ ✘✔✘✘✘ CVE-2026-63830         CRITICAL     9.4   0.4%   ·  ↳ S:UBUNTU-CVE-2026-63830
  │ ✘✔✘✘✘ CVE-2026-63887         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-63887
  │ ✘✔✘✘✘ CVE-2026-63888         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-63888
  │ ✘✔✘✘✘ CVE-2026-63912         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-63912
  │ ✘✔✘✘✘ CVE-2026-63922         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-63922
  │ ✘✔✘✘✘ CVE-2026-63924         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-63924
  │ ✘✔✘✘✘ CVE-2026-64007         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64007
  │ ✘✔✘✘✘ CVE-2026-64046         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64046
  │ ✘✔✘✘✘ CVE-2026-64047         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64047
  │ ✘✔✘✘✘ CVE-2026-64055         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64055
  │ ✘✔✘✘✘ CVE-2026-64056         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-64056
  │ ✘✔✘✘✘ CVE-2026-64089         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-64089
  │ ✘✔✘✘✘ CVE-2026-64091         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64091
  │ ✘✔✘✘✘ CVE-2026-64102         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64102
  │ ✘✔✘✘✘ CVE-2026-64106         CRITICAL     9.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64106
  │ ✘✔✘✘✘ CVE-2026-64113         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64113
  │ ✘✔✘✘✘ CVE-2026-64125         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-64125
  │ ✘✔✘✘✘ CVE-2026-64268         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-64268
  │ ✘✔✘✘✘ CVE-2026-64303         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-64303
  │ ✘✔✘✘✘ CVE-2026-64320         CRITICAL     9.1   0.8%   ·  ↳ S:UBUNTU-CVE-2026-64320
  │ ✘✔✘✘✘ CVE-2026-64541         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-64541
  │ ✘✔✘✘✘ CVE-2026-64551         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64551
  │ ✘✔✘✘✘ CVE-2026-64564         CRITICAL     9.8   1.4%   ·  ↳ S:UBUNTU-CVE-2026-64564
  │ ✘✔✘✘✘ CVE-2026-68082         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68082
  │ ✘✔✘✘✘ CVE-2026-68117         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68117
  │ ✘✔✘✘✘ CVE-2026-68123         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-68123
  │ ✘✔✘✘✘ CVE-2026-68127         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68127
  │ ✘✔✘✘✘ CVE-2026-68137         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68137
  │ ✘✔✘✘✘ CVE-2026-68144         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68144
  │ ✘✔✘✘✘ CVE-2026-68154         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68154
  │ ✘✔✘✘✘ CVE-2026-68156         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68156
  │ ✘✔✘✘✘ CVE-2026-68158         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68158
  │ ✘✔✘✘✘ CVE-2026-68159         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68159
  │ ✘✔✘✘✘ CVE-2026-68160         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-68160
  │ ✘✔✘✘✘ CVE-2026-68300         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-68300
  │ ✘✔✘✘✘ CVE-2026-68343         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68343
  │ ✘✔✘✘✘ CVE-2026-68426         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68426
  │ ✘✔✘✘✘ CVE-2026-68476         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68476
  │ ✘✔✘✘✘ CVE-2026-68477         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68477
  │ ✘✔✘✘✘ CVE-2026-72014         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72014
  │ ✘✔✘✘✘ CVE-2026-72020         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72020
  │ ✘✔✘✘✘ CVE-2026-72033         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-72033
  │ ✘✔✘✘✘ CVE-2026-72083         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72083
  │ ✘✔✘✘✘ CVE-2026-72084         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72084
  │ ✘✔✘✘✘ CVE-2026-72085         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72085
  │ ✘✔✘✘✘ CVE-2026-72098         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72098
  │ ✘✔✘✘✘ CVE-2026-72129         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72129
  │ ✘✔✘✘✘ CVE-2026-72200         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72200
  │ ✘✔✘✘✘ CVE-2026-72226         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-72226
  │ ✘✔✘✘✘ CVE-2026-72234         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72234
  │ ✘✔✘✘✘ CVE-2026-72251         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72251
  │ ✘✔✘✘✘ CVE-2026-72288         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72288
  │ ✘✔✘✘✘ CVE-2026-72289         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72289
  │ ✘✔✘✘✘ CVE-2026-72296         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72296
  │ ✘✔✘✘✘ CVE-2026-72299         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72299
  │ ✘✔✘✘✘ CVE-2026-72318         CRITICAL     9.4   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72318
  │ ✘✔✘✘✘ CVE-2026-72319         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72319
  │ ✘✔✘✘✘ CVE-2026-72322         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72322
  │ ✘✔✘✘✘ CVE-2026-72323         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72323
  │ ✘✔✘✘✘ CVE-2026-72329         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72329
  │ ✘✔✘✘✘ CVE-2026-72339         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72339
  │ ✘✔✘✘✘ CVE-2026-72348         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72348
  │ ✘✔✘✘✘ CVE-2026-72351         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72351
  │ ✘✔✘✘✘ CVE-2026-72398         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-72398
  │ ✘✔✘✘✘ CVE-2026-72421         CRITICAL    10.0   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72421
  │ ✘✔✘✘✘ CVE-2026-72436         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72436
  │ ✘✔✘✘✘ CVE-2026-72466         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72466
  │ ✘✔✘✘✘ CVE-2026-72472         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72472
  │ ✘✔✘✘✘ CVE-2026-72473         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72473
  │ ✘✔✘✘✘ CVE-2026-72491         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72491
  │ ✘✔✘✘✘ CVE-2026-72493         CRITICAL     9.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-72493
  │ ✘✔✘✘✘ CVE-2026-74255         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74255
  │ ✘✔✘✘✘ CVE-2026-74267         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-74267
  │ ✘✔✘✘✘ CVE-2026-74268         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-74268
  │ ✘✔✘✘✘ CVE-2026-74279         CRITICAL    10.0   0.8%   ·  ↳ S:UBUNTU-CVE-2026-74279
  │ ✘✔✘✘✘ CVE-2026-74287         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-74287
  │ ✘✔✘✘✘ CVE-2026-74310         CRITICAL     9.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74310
  │ ✘✔✘✘✘ CVE-2026-74345         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74345
  │ ✘✔✘✘✘ CVE-2026-74350         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-74350
  │ ✘✔✘✘✘ CVE-2026-74376         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74376
  │ ✘✔✘✘✘ CVE-2026-74384         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74384
  │ ✘✔✘✘✘ CVE-2026-74394         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74394
  │ ✘✔✘✘✘ CVE-2026-74398         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74398
  │ ✘✔✘✘✘ CVE-2026-74406         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74406
  │ ✘✔✘✘✘ CVE-2026-74427         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-74427
  │ ✘✔✘✘✘ CVE-2026-74436         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74436
  │ ✘✔✘✘✘ CVE-2026-74473         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74473
  │ ✘✔✘✘✘ CVE-2026-74474         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74474
  │ ✘✔✘✘✘ CVE-2026-74475         CRITICAL    10.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74475
  │ ✘✔✘✘✘ CVE-2026-74478         CRITICAL     9.8   0.9%   ·  ↳ S:UBUNTU-CVE-2026-74478
  │ ✘✔✘✘✘ CVE-2026-74480         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-74480
  │ ✘✔✘✘✘ CVE-2026-74495         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74495
  │ ✘✔✘✘✘ CVE-2026-74556         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74556
  │ ✘✔✘✘✘ CVE-2026-74569         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74569
  │ ✘✔✘✘✘ CVE-2026-74581         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74581
  │ ✘✔✘✘✘ CVE-2026-74586         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74586
  │ ✘✔✘✘✘ CVE-2026-74587         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74587
  │ ✘✔✘✘✘ CVE-2026-74588         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74588
  │ ✘✔✘✘✘ CVE-2026-74597         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74597
  │ ✘✔✘✘✘ CVE-2026-74628         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74628
  │ ✘✔✘✘✘ CVE-2026-74662         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74662
  │ ✘✔✘✘✘ CVE-2026-74669         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74669
  │ ✘✔✘✘✘ CVE-2026-74688         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74688
  │ ✘✔✘✘✘ CVE-2026-74705         CRITICAL    10.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74705
  │ ✘✔✘✘✘ CVE-2026-74723         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74723
  │ ✘✔✘✘✘ CVE-2026-74730         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74730
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
  │ ✘✔✘✘✘ CVE-2026-80600         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-80600
  │ ✘✔✘✘✘ CVE-2026-80603         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-80603
  │ ✘✔✘✘✘ CVE-2026-80630         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-80630
  │ ✘✔✘✘✘ CVE-2026-80670         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-80670
  │ ✘✔✘✘✘ CVE-2026-80671         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80671
  │ ✘✔✘✘✘ CVE-2026-80681         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-80681
  │ ✘✔✘✘✘ CVE-2026-80694         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-80694
  │ ✘✔✘✘✘ CVE-2026-80714         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-80714
  │ ✘✔✘✘✘ CVE-2026-80976         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-80976
  │ ✘✔✘✘✘ CVE-2026-81002         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-81002
  │ ✘✔✘✘✘ CVE-2026-89448         CRITICAL     9.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89448
  │ ✘✔✘✘✘ CVE-2026-89478         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89478
  │ ✘✔✘✘✘ CVE-2026-89479         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89479
  │ ✘✔✘✘✘ CVE-2026-89482         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89482
  │ ✘✔✘✘✘ CVE-2026-89485         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89485
  │ ✘✔✘✘✘ CVE-2026-89492         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89492
  │ ✘✔✘✘✘ CVE-2026-89494         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89494
  │ ✘✔✘✘✘ CVE-2026-89495         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89495
  │ ✘✔✘✘✘ CVE-2026-89530         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89530
  │ ✘✔✘✘✘ CVE-2026-89537         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89537
  │ ✘✔✘✘✘ CVE-2026-89538         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89538
  │ ✘✔✘✘✘ CVE-2026-89541         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89541
  │ ✘✔✘✘✘ CVE-2026-89542         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89542
  │ ✘✔✘✘✘ CVE-2026-89550         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89550
  │ ✘✔✘✘✘ CVE-2026-89551         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89551
  │ ✘✔✘✘✘ CVE-2026-89555         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89555
  │ ✘✔✘✘✘ CVE-2026-89631         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89631
  │ ✘✔✘✘✘ CVE-2026-89633         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89633
  │ ✘✔✘✘✘ CVE-2026-89636         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89636
  │ ✘✔✘✘✘ CVE-2026-89637         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89637
  │ ✘✔✘✘✘ CVE-2026-89643         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89643
  │ ✘✔✘✘✘ CVE-2026-89649         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89649
  │ ✘✔✘✘✘ CVE-2026-89650         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89650
  │ ✘✔✘✘✘ CVE-2026-89652         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89652
  │ ✘✔✘✘✘ CVE-2026-89654         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89654
  │ ✘✔✘✘✘ CVE-2026-89655         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89655
  │ ✘✔✘✘✘ CVE-2026-89656         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89656
  │ ✘✔✘✘✘ CVE-2026-89659         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89659
  │ ✘✔✘✘✘ CVE-2026-89662         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89662
  │ ✘✔✘✘✘ CVE-2026-89671         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89671
  │ ✘✔✘✘✘ CVE-2026-89672         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89672
  │ ✘✔✘✘✘ CVE-2026-89674         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89674
  │ ✘✔✘✘✘ CVE-2026-89675         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89675
  │ ✘✔✘✘✘ CVE-2026-89676         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89676
  │ ✘✔✘✘✘ CVE-2026-89686         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89686
  │ ✘✔✘✘✘ CVE-2026-89697         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89697
  │ ✘✔✘✘✘ CVE-2026-89708         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89708
  │ ✘✔✘✘✘ CVE-2026-89713         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89713
  │ ✘✔✘✘✘ CVE-2026-89778         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89778
  │ ✘✔✘✘✘ CVE-2026-89783         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89783
  │ ✘✔✘✘✘ CVE-2026-89786         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89786
  │ ✘✔✘✘✘ CVE-2026-89846         CRITICAL     9.1   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89846
  │ ✘✔✘✘✘ CVE-2026-89847         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89847
  │ ✘✔✘✘✘ CVE-2026-89930         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89930
  │ ✘✔✘✘✘ CVE-2026-89969         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89969
  │ ✘✔✘✘✘ CVE-2026-89972         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89972
  │ ✘✔✘✘✘ CVE-2026-90011         CRITICAL     9.1   0.8%   ·  ↳ S:UBUNTU-CVE-2026-90011
  │ ✘✔✘✘✘ CVE-2026-90036         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-90036
  │ ✘✔✘✘✘ CVE-2026-90037         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-90037
  │ ✘✔✘✘✘ CVE-2026-90049         CRITICAL     9.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90049
  │ ✘✔✘✘✘ CVE-2026-90104         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90104
  │ ✘✔✘✘✘ CVE-2026-90110         CRITICAL     9.4   0.6%   ·  ↳ S:UBUNTU-CVE-2026-90110
  │ ✘✔✘✘✘ CVE-2026-90151         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90151
  │ ✘✔✘✘✘ CVE-2026-90235         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90235
  │ ✘✔✘✘✘ CVE-2026-90413         CRITICAL     9.1   0.8%   ·  ↳ S:UBUNTU-CVE-2026-90413
  │ ✘✔✘✘✘ CVE-2026-90414         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-90414
  │ ✘✔✘✘✘ CVE-2026-97413         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-97413
  │ ✘✔✘✘✘ CVE-2026-98323         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-98323
  │ ✘✔✘✘✘ CVE-2026-98365         CRITICAL     9.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-98365
  │ ✘✔✘✘✘ CVE-2026-98432         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-98432
  │ ✘✔✘✘✘ CVE-2026-98490         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-98490
  │ ✘✔✘✘✘ CVE-2026-98548         CRITICAL     9.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-98548
  │ ✘✔✘✘✘ CVE-2026-98549         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-98549
  │ ✘✔✘✘✘ CVE-2026-98959         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-98959
  │ ✘✔✘✘✘ CVE-2026-99153         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-99153
  │ ✘✔✘✘✘ CVE-2026-99154         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-99154
  │ ✘✔✘✘✘ CVE-2026-99999         CRITICAL     9.3   0.8% KEV  ↳ S:UBUNTU-CVE-2026-99999
  │ ✘✔✘✘✘ CVE-2013-7445          HIGH         7.8   2.8%   ·  ↳ S:UBUNTU-CVE-2013-7445
  │ ✘✔✘✘✘ CVE-2017-13165         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2017-13165
  │ ✘✔✘✘✘ CVE-2018-12930         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2018-12930
  │ ✘✔✘✘✘ CVE-2018-12931         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2018-12931
  │ ✘✔✘✘✘ CVE-2019-14899         HIGH         7.4   0.8%   ·  ↳ S:UBUNTU-CVE-2019-14899
  │ ✘✔✘✘✘ CVE-2019-19378         HIGH         7.8   2.3%   ·  ↳ S:UBUNTU-CVE-2019-19378
  │ ✘✔✘✘✘ CVE-2019-19814         HIGH         9.3   3.3%   ·  ↳ S:UBUNTU-CVE-2019-19814
  │ ✘✔✘✘✘ CVE-2020-12362         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2020-12362
  │ ✘✔✘✘✘ CVE-2020-14356         HIGH         7.8   1.0%   ·  ↳ S:UBUNTU-CVE-2020-14356
  │ ✘✔✘✘✘ CVE-2020-26556         HIGH         7.5   0.9%   ·  ↳ S:UBUNTU-CVE-2020-26556
  │ ✘✔✘✘✘ CVE-2020-26557         HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2020-26557
  │ ✘✔✘✘✘ CVE-2020-26559         HIGH         8.8   0.9%   ·  ↳ S:UBUNTU-CVE-2020-26559
  │ ✘✔✘✘✘ CVE-2020-26560         HIGH         8.1   0.9%   ·  ↳ S:UBUNTU-CVE-2020-26560
  │ ✘✔✘✘✘ CVE-2020-36788         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2020-36788
  │ ✘✔✘✘✘ CVE-2021-26934         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2021-26934
  │ ✘✔✘✘✘ CVE-2021-32078         HIGH         7.1   0.6%   ·  ↳ S:UBUNTU-CVE-2021-32078
  │ ✘✔✘✘✘ CVE-2021-34981         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-34981
  │ ✘✔✘✘✘ CVE-2021-3847          HIGH         7.8   0.5%   ·  ↳ S:UBUNTU-CVE-2021-3847
  │ ✘✔✘✘✘ CVE-2021-3864          HIGH         7.0   0.8%   ·  ↳ S:UBUNTU-CVE-2021-3864
  │ ✘✔✘✘✘ CVE-2021-39801         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2021-39801
  │ ✘✔✘✘✘ CVE-2021-46925         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2021-46925
  │ ✘✔✘✘✘ CVE-2021-47004         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47004
  │ ✘✔✘✘✘ CVE-2021-47049         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47049
  │ ✘✔✘✘✘ CVE-2021-47061         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47061
  │ ✘✔✘✘✘ CVE-2021-47113         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2021-47113
  │ ✘✔✘✘✘ CVE-2021-47158         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47158
  │ ✘✔✘✘✘ CVE-2021-47183         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2021-47183
  │ ✘✔✘✘✘ CVE-2021-47226         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47226
  │ ✘✔✘✘✘ CVE-2021-47247         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47247
  │ ✘✔✘✘✘ CVE-2021-47281         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47281
  │ ✘✔✘✘✘ CVE-2021-47352         HIGH         8.4   0.3%   ·  ↳ S:UBUNTU-CVE-2021-47352
  │ ✘✔✘✘✘ CVE-2021-47366         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47366
  │ ✘✔✘✘✘ CVE-2021-47391         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47391
  │ ✘✔✘✘✘ CVE-2021-47412         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47412
  │ ✘✔✘✘✘ CVE-2021-47438         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47438
  │ ✘✔✘✘✘ CVE-2021-47479         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47479
  │ ✘✔✘✘✘ CVE-2021-47492         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47492
  │ ✘✔✘✘✘ CVE-2021-47493         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47493
  │ ✘✔✘✘✘ CVE-2021-47552         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47552
  │ ✘✔✘✘✘ CVE-2021-47559         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2021-47559
  │ ✘✔✘✘✘ CVE-2021-47635         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2021-47635
  │ ✘✔✘✘✘ CVE-2022-0400          HIGH         7.5   1.9%   ·  ↳ S:UBUNTU-CVE-2022-0400
  │ ✘✔✘✘✘ CVE-2022-0995          HIGH         7.8   8.9% KEV  ↳ S:LSN-0112-1,UBUNTU-CVE-2022-0995
  │ ✘✔✘✘✘ CVE-2022-1247          HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2022-1247
  │ ✘✔✘✘✘ CVE-2022-21546         HIGH         7.8   0.5%   ·  ↳ S:UBUNTU-CVE-2022-21546
  │ ✘✔✘✘✘ CVE-2022-25265         HIGH         7.8   1.1%   ·  ↳ S:UBUNTU-CVE-2022-25265
  │ ✘✔✘✘✘ CVE-2022-25836         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2022-25836
  │ ✘✔✘✘✘ CVE-2022-25837         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2022-25837
  │ ✘✔✘✘✘ CVE-2022-2961          HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2022-2961
  │ ✘✔✘✘✘ CVE-2022-39189         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-39189
  │ ✘✔✘✘✘ CVE-2022-45885         HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2022-45885
  │ ✘✔✘✘✘ CVE-2022-47518         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-47518
  │ ✘✔✘✘✘ CVE-2022-47519         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-47519
  │ ✘✔✘✘✘ CVE-2022-48721         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48721
  │ ✘✔✘✘✘ CVE-2022-48744         HIGH         7.8   0.6%   ·  ↳ S:UBUNTU-CVE-2022-48744
  │ ✘✔✘✘✘ CVE-2022-48751         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48751
  │ ✘✔✘✘✘ CVE-2022-48771         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48771
  │ ✘✔✘✘✘ CVE-2022-48792         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48792
  │ ✘✔✘✘✘ CVE-2022-48827         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2022-48827
  │ ✘✔✘✘✘ CVE-2022-48887         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48887
  │ ✘✔✘✘✘ CVE-2022-49026         HIGH         7.8   0.2%   ·  ↳ S:LSN-0117-1,UBUNTU-CVE-2022-49026,USN-7922-1
  │ ✘✔✘✘✘ CVE-2022-49065         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2022-49065
  │ ✘✔✘✘✘ CVE-2022-49082         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49082
  │ ✘✔✘✘✘ CVE-2022-49110         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2022-49110
  │ ✘✔✘✘✘ CVE-2022-49138         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2022-49138
  │ ✘✔✘✘✘ CVE-2022-49142         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2022-49142
  │ ✘✔✘✘✘ CVE-2022-49154         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49154
  │ ✘✔✘✘✘ CVE-2022-49159         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49159
  │ ✘✔✘✘✘ CVE-2022-49168         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49168
  │ ✘✔✘✘✘ CVE-2022-49170         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49170,USN-8919-1
  │ ✘✔✘✘✘ CVE-2022-49172         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49172
  │ ✘✔✘✘✘ CVE-2022-49178         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49178
  │ ✘✔✘✘✘ CVE-2022-49182         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49182,USN-8919-1
  │ ✘✔✘✘✘ CVE-2022-49196         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49196
  │ ✘✔✘✘✘ CVE-2022-49215         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49215
  │ ✘✔✘✘✘ CVE-2022-49234         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49234
  │ ✘✔✘✘✘ CVE-2022-49258         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49258
  │ ✘✔✘✘✘ CVE-2022-49289         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49289
  │ ✘✔✘✘✘ CVE-2022-49325         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2022-49325
  │ ✘✔✘✘✘ CVE-2022-49328         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2022-49328
  │ ✘✔✘✘✘ CVE-2022-49390         HIGH         7.8   0.3%   ·  ↳ S:LSN-0117-1,UBUNTU-CVE-2022-49390,USN-7922-1
  │ ✘✔✘✘✘ CVE-2022-49444         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49444
  │ ✘✔✘✘✘ CVE-2022-49465         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49465
  │ ✘✔✘✘✘ CVE-2022-49470         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49470
  │ ✘✔✘✘✘ CVE-2022-49519         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49519
  │ ✘✔✘✘✘ CVE-2022-49531         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49531
  │ ✘✔✘✘✘ CVE-2022-49545         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49545
  │ ✘✔✘✘✘ CVE-2022-49555         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49555
  │ ✘✔✘✘✘ CVE-2022-49562         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49562
  │ ✘✔✘✘✘ CVE-2022-49563         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49563
  │ ✘✔✘✘✘ CVE-2022-49564         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49564
  │ ✘✔✘✘✘ CVE-2022-49622         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49622
  │ ✘✔✘✘✘ CVE-2022-49623         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49623
  │ ✘✔✘✘✘ CVE-2022-49635         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49635
  │ ✘✔✘✘✘ CVE-2022-49651         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49651
  │ ✘✔✘✘✘ CVE-2022-49664         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2022-49664
  │ ✘✔✘✘✘ CVE-2022-49696         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49696
  │ ✘✔✘✘✘ CVE-2022-49698         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49698,USN-7990-1
  │ ✘✔✘✘✘ CVE-2022-49711         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49711
  │ ✘✔✘✘✘ CVE-2022-49720         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49720
  │ ✘✔✘✘✘ CVE-2022-49761         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49761
  │ ✘✔✘✘✘ CVE-2022-49799         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49799
  │ ✘✔✘✘✘ CVE-2022-49851         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49851
  │ ✘✔✘✘✘ CVE-2022-49892         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49892
  │ ✘✔✘✘✘ CVE-2022-49898         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49898
  │ ✘✔✘✘✘ CVE-2022-49899         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49899
  │ ✘✔✘✘✘ CVE-2022-49900         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49900
  │ ✘✔✘✘✘ CVE-2022-49910         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49910
  │ ✘✔✘✘✘ CVE-2022-49935         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49935
  │ ✘✔✘✘✘ CVE-2022-49980         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49980
  │ ✘✔✘✘✘ CVE-2022-49997         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2022-49997
  │ ✘✔✘✘✘ CVE-2022-49998         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49998
  │ ✘✔✘✘✘ CVE-2022-50021         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50021
  │ ✘✔✘✘✘ CVE-2022-50026         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50026
  │ ✘✔✘✘✘ CVE-2022-50066         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50066
  │ ✘✔✘✘✘ CVE-2022-50082         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50082
  │ ✘✔✘✘✘ CVE-2022-50090         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50090
  │ ✘✔✘✘✘ CVE-2022-50098         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-50098
  │ ✘✔✘✘✘ CVE-2022-50103         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50103
  │ ✘✔✘✘✘ CVE-2022-50129         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50129
  │ ✘✔✘✘✘ CVE-2022-50163         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-50163
  │ ✘✔✘✘✘ CVE-2022-50167         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2022-50167
  │ ✘✔✘✘✘ CVE-2022-50171         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2022-50171
  │ ✘✔✘✘✘ CVE-2022-50213         HIGH         7.8  10.2%   ·  ↳ S:UBUNTU-CVE-2022-50213
  │ ✘✔✘✘✘ CVE-2022-50234         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50234
  │ ✘✔✘✘✘ CVE-2022-50240         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50240
  │ ✘✔✘✘✘ CVE-2022-50256         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50256
  │ ✘✔✘✘✘ CVE-2022-50300         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50300
  │ ✘✔✘✘✘ CVE-2022-50306         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50306
  │ ✘✔✘✘✘ CVE-2022-50362         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50362
  │ ✘✔✘✘✘ CVE-2022-50378         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50378
  │ ✘✔✘✘✘ CVE-2022-50399         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50399
  │ ✘✔✘✘✘ CVE-2022-50406         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50406
  │ ✘✔✘✘✘ CVE-2022-50412         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50412
  │ ✘✔✘✘✘ CVE-2022-50417         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50417
  │ ✘✔✘✘✘ CVE-2022-50472         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2022-50472
  │ ✘✔✘✘✘ CVE-2022-50488         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50488
  │ ✘✔✘✘✘ CVE-2022-50492         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50492
  │ ✘✔✘✘✘ CVE-2022-50493         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50493
  │ ✘✔✘✘✘ CVE-2022-50518         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2022-50518
  │ ✘✔✘✘✘ CVE-2022-50551         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50551
  │ ✘✔✘✘✘ CVE-2022-50552         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50552
  │ ✘✔✘✘✘ CVE-2022-50630         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50630
  │ ✘✔✘✘✘ CVE-2022-50700         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-50700
  │ ✘✔✘✘✘ CVE-2022-50746         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50746
  │ ✘✔✘✘✘ CVE-2022-50756         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50756
  │ ✘✔✘✘✘ CVE-2022-50860         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50860
  │ ✘✔✘✘✘ CVE-2023-0030          HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-0030
  │ ✘✔✘✘✘ CVE-2023-2007          HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2023-2007
  │ ✘✔✘✘✘ CVE-2023-26242         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-26242
  │ ✘✔✘✘✘ CVE-2023-2640          HIGH         7.8  15.2% KEV  ↳ S:UBUNTU-CVE-2023-2640
  │ ✘✔✘✘✘ CVE-2023-32256         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2023-32256
  │ ✘✔✘✘✘ CVE-2023-33053         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2023-33053
  │ ✘✔✘✘✘ CVE-2023-3397          HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-3397
  │ ✘✔✘✘✘ CVE-2023-3640          HIGH         7.8   0.8%   ·  ↳ S:UBUNTU-CVE-2023-3640
  │ ✘✔✘✘✘ CVE-2023-39176         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2023-39176
  │ ✘✔✘✘✘ CVE-2023-39198         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2023-39198
  │ ✘✔✘✘✘ CVE-2023-52474         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2023-52474
  │ ✘✔✘✘✘ CVE-2023-52572         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52572
  │ ✘✔✘✘✘ CVE-2023-52586         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52586
  │ ✘✔✘✘✘ CVE-2023-52588         HIGH         7.3   0.3%   ·  ↳ S:UBUNTU-CVE-2023-52588
  │ ✘✔✘✘✘ CVE-2023-52590         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52590
  │ ✘✔✘✘✘ CVE-2023-52591         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2023-52591
  │ ✘✔✘✘✘ CVE-2023-52610         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2023-52610
  │ ✘✔✘✘✘ CVE-2023-52624         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2023-52624
  │ ✘✔✘✘✘ CVE-2023-52642         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52642
  │ ✘✔✘✘✘ CVE-2023-52669         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2023-52669
  │ ✘✔✘✘✘ CVE-2023-52757         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52757,USN-7701-1
  │ ✘✔✘✘✘ CVE-2023-52761         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2023-52761
  │ ✘✔✘✘✘ CVE-2023-52834         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2023-52834
  │ ✘✔✘✘✘ CVE-2023-52854         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52854,USN-7874-1
  │ ✘✔✘✘✘ CVE-2023-52879         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52879
  │ ✘✔✘✘✘ CVE-2023-52903         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52903
  │ ✘✔✘✘✘ CVE-2023-52916         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52916
  │ ✘✔✘✘✘ CVE-2023-52920         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2023-52920
  │ ✘✔✘✘✘ CVE-2023-52926         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52926
  │ ✘✔✘✘✘ CVE-2023-52935         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52935
  │ ✘✔✘✘✘ CVE-2023-52975         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2023-52975,USN-7701-1
  │ ✘✔✘✘✘ CVE-2023-53034         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2023-53034,USN-7585-1
  │ ✘✔✘✘✘ CVE-2023-53039         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53039
  │ ✘✔✘✘✘ CVE-2023-53052         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53052
  │ ✘✔✘✘✘ CVE-2023-53080         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53080
  │ ✘✔✘✘✘ CVE-2023-53094         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53094
  │ ✘✔✘✘✘ CVE-2023-53111         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53111
  │ ✘✔✘✘✘ CVE-2023-53178         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53178
  │ ✘✔✘✘✘ CVE-2023-53217         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53217
  │ ✘✔✘✘✘ CVE-2023-53218         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53218
  │ ✘✔✘✘✘ CVE-2023-53254         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53254
  │ ✘✔✘✘✘ CVE-2023-53257         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53257
  │ ✘✔✘✘✘ CVE-2023-53259         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53259
  │ ✘✔✘✘✘ CVE-2023-53272         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53272
  │ ✘✔✘✘✘ CVE-2023-53282         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53282
  │ ✘✔✘✘✘ CVE-2023-53335         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2023-53335
  │ ✘✔✘✘✘ CVE-2023-53399         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2023-53399
  │ ✘✔✘✘✘ CVE-2023-53429         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53429
  │ ✘✔✘✘✘ CVE-2023-53432         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53432
  │ ✘✔✘✘✘ CVE-2023-53463         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2023-53463
  │ ✘✔✘✘✘ CVE-2023-53473         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53473
  │ ✘✔✘✘✘ CVE-2023-53491         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2023-53491
  │ ✘✔✘✘✘ CVE-2023-53494         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53494
  │ ✘✔✘✘✘ CVE-2023-53499         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53499
  │ ✘✔✘✘✘ CVE-2023-53510         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53510
  │ ✘✔✘✘✘ CVE-2023-53539         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53539
  │ ✘✔✘✘✘ CVE-2023-53540         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53540
  │ ✘✔✘✘✘ CVE-2023-53544         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53544
  │ ✘✔✘✘✘ CVE-2023-53545         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53545
  │ ✘✔✘✘✘ CVE-2023-53577         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53577
  │ ✘✔✘✘✘ CVE-2023-53586         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2023-53586
  │ ✘✔✘✘✘ CVE-2023-53596         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53596
  │ ✘✔✘✘✘ CVE-2023-53606         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2023-53606
  │ ✘✔✘✘✘ CVE-2023-53627         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53627
  │ ✘✔✘✘✘ CVE-2023-53635         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2023-53635
  │ ✘✔✘✘✘ CVE-2023-53651         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53651
  │ ✘✔✘✘✘ CVE-2023-53680         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2023-53680
  │ ✘✔✘✘✘ CVE-2023-53707         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53707
  │ ✘✔✘✘✘ CVE-2023-53718         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53718
  │ ✘✔✘✘✘ CVE-2023-53733         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53733
  │ ✘✔✘✘✘ CVE-2023-53748         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53748
  │ ✘✔✘✘✘ CVE-2023-53753         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53753
  │ ✘✔✘✘✘ CVE-2023-53781         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53781
  │ ✘✔✘✘✘ CVE-2023-53806         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53806
  │ ✘✔✘✘✘ CVE-2023-53816         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53816
  │ ✘✔✘✘✘ CVE-2023-53819         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53819
  │ ✘✔✘✘✘ CVE-2023-53824         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53824
  │ ✘✔✘✘✘ CVE-2023-53829         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53829
  │ ✘✔✘✘✘ CVE-2023-53846         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53846
  │ ✘✔✘✘✘ CVE-2023-54019         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2023-54019
  │ ✘✔✘✘✘ CVE-2023-54035         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2023-54035
  │ ✘✔✘✘✘ CVE-2023-54048         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54048
  │ ✘✔✘✘✘ CVE-2023-54067         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54067
  │ ✘✔✘✘✘ CVE-2023-54088         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54088
  │ ✘✔✘✘✘ CVE-2023-54098         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54098
  │ ✘✔✘✘✘ CVE-2023-54121         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54121
  │ ✘✔✘✘✘ CVE-2023-54129         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2023-54129
  │ ✘✔✘✘✘ CVE-2023-54153         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54153
  │ ✘✔✘✘✘ CVE-2023-54157         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2023-54157
  │ ✘✔✘✘✘ CVE-2023-54182         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2023-54182
  │ ✘✔✘✘✘ CVE-2023-54187         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54187
  │ ✘✔✘✘✘ CVE-2023-54202         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2023-54202
  │ ✘✔✘✘✘ CVE-2023-54207         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54207
  │ ✘✔✘✘✘ CVE-2023-54243         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2023-54243
  │ ✘✔✘✘✘ CVE-2023-6610          HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2023-6610
  │ ✘✔✘✘✘ CVE-2023-7356          HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2023-7356
  │ ✘✔✘✘✘ CVE-2024-21823         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-21823
  │ ✘✔✘✘✘ CVE-2024-25743         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2024-25743
  │ ✘✔✘✘✘ CVE-2024-25744         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-25744
  │ ✘✔✘✘✘ CVE-2024-26656         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26656
  │ ✘✔✘✘✘ CVE-2024-26659         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26659
  │ ✘✔✘✘✘ CVE-2024-26672         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26672
  │ ✘✔✘✘✘ CVE-2024-26739         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-26739
  │ ✘✔✘✘✘ CVE-2024-26759         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-26759
  │ ✘✔✘✘✘ CVE-2024-26769         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2024-26769
  │ ✘✔✘✘✘ CVE-2024-26795         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26795
  │ ✘✔✘✘✘ CVE-2024-26807         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26807
  │ ✘✔✘✘✘ CVE-2024-26869         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26869
  │ ✘✔✘✘✘ CVE-2024-26872         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26872
  │ ✘✔✘✘✘ CVE-2024-26958         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26958
  │ ✘✔✘✘✘ CVE-2024-26961         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26961
  │ ✘✔✘✘✘ CVE-2024-26988         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-26988
  │ ✘✔✘✘✘ CVE-2024-27052         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-27052
  │ ✘✔✘✘✘ CVE-2024-27056         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-27056
  │ ✘✔✘✘✘ CVE-2024-27062         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-27062
  │ ✘✔✘✘✘ CVE-2024-27403         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-27403
  │ ✘✔✘✘✘ CVE-2024-27408         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-27408
  │ ✘✔✘✘✘ CVE-2024-27415         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-27415
  │ ✘✔✘✘✘ CVE-2024-35791         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35791
  │ ✘✔✘✘✘ CVE-2024-35808         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35808
  │ ✘✔✘✘✘ CVE-2024-35839         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35839
  │ ✘✔✘✘✘ CVE-2024-35867         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-35867,USN-7874-1
  │ ✘✔✘✘✘ CVE-2024-35868         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35868
  │ ✘✔✘✘✘ CVE-2024-35871         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2024-35871
  │ ✘✔✘✘✘ CVE-2024-35875         HIGH         8.4   0.3%   ·  ↳ S:UBUNTU-CVE-2024-35875
  │ ✘✔✘✘✘ CVE-2024-35931         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35931
  │ ✘✔✘✘✘ CVE-2024-35932         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35932
  │ ✘✔✘✘✘ CVE-2024-36009         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-36009
  │ ✘✔✘✘✘ CVE-2024-36013         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2024-36013
  │ ✘✔✘✘✘ CVE-2024-36880         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-36880
  │ ✘✔✘✘✘ CVE-2024-36908         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2024-36908
  │ ✘✔✘✘✘ CVE-2024-36914         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-36914
  │ ✘✔✘✘✘ CVE-2024-36915         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2024-36915
  │ ✘✔✘✘✘ CVE-2024-36922         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-36922
  │ ✘✔✘✘✘ CVE-2024-37354         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-37354
  │ ✘✔✘✘✘ CVE-2024-38545         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-38545
  │ ✘✔✘✘✘ CVE-2024-38556         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-38556
  │ ✘✔✘✘✘ CVE-2024-38580         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-38580
  │ ✘✔✘✘✘ CVE-2024-39507         HIGH         7.0   0.3%   ·  ↳ S:UBUNTU-CVE-2024-39507
  │ ✘✔✘✘✘ CVE-2024-39508         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-39508
  │ ✘✔✘✘✘ CVE-2024-40927         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-40927
  │ ✘✔✘✘✘ CVE-2024-40947         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-40947
  │ ✘✔✘✘✘ CVE-2024-40971         HIGH         7.3   0.3%   ·  ↳ S:UBUNTU-CVE-2024-40971
  │ ✘✔✘✘✘ CVE-2024-40990         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-40990
  │ ✘✔✘✘✘ CVE-2024-41000         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-41000
  │ ✘✔✘✘✘ CVE-2024-41008         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-41008
  │ ✘✔✘✘✘ CVE-2024-41013         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2024-41013
  │ ✘✔✘✘✘ CVE-2024-41014         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2024-41014
  │ ✘✔✘✘✘ CVE-2024-41048         HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2024-41048
  │ ✘✔✘✘✘ CVE-2024-41060         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-41060
  │ ✘✔✘✘✘ CVE-2024-41062         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-41062
  │ ✘✔✘✘✘ CVE-2024-41069         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-41069
  │ ✘✔✘✘✘ CVE-2024-41079         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2024-41079
  │ ✘✔✘✘✘ CVE-2024-41935         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2024-41935
  │ ✘✔✘✘✘ CVE-2024-42110         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2024-42110
  │ ✘✔✘✘✘ CVE-2024-42118         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-42118
  │ ✘✔✘✘✘ CVE-2024-42120         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-42120
  │ ✘✔✘✘✘ CVE-2024-42121         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-42121
  │ ✘✔✘✘✘ CVE-2024-42147         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-42147
  │ ✘✔✘✘✘ CVE-2024-42253         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-42253
  │ ✘✔✘✘✘ CVE-2024-42296         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-42296
  │ ✘✔✘✘✘ CVE-2024-43832         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-43832
  │ ✘✔✘✘✘ CVE-2024-43872         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2024-43872
  │ ✘✔✘✘✘ CVE-2024-44939         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-44939
  │ ✘✔✘✘✘ CVE-2024-44950         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2024-44950
  │ ✘✔✘✘✘ CVE-2024-44986         HIGH         8.1   0.7%   ·  ↳ S:UBUNTU-CVE-2024-44986
  │ ✘✔✘✘✘ CVE-2024-46713         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-46713
  │ ✘✔✘✘✘ CVE-2024-46716         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46716
  │ ✘✔✘✘✘ CVE-2024-46729         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46729
  │ ✘✔✘✘✘ CVE-2024-46730         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46730
  │ ✘✔✘✘✘ CVE-2024-46751         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-46751
  │ ✘✔✘✘✘ CVE-2024-46754         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46754
  │ ✘✔✘✘✘ CVE-2024-46763         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2024-46763
  │ ✘✔✘✘✘ CVE-2024-46774         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2024-46774
  │ ✘✔✘✘✘ CVE-2024-46787         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46787,USN-7671-1
  │ ✘✔✘✘✘ CVE-2024-46811         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46811
  │ ✘✔✘✘✘ CVE-2024-46812         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-46812
  │ ✘✔✘✘✘ CVE-2024-46813         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-46813
  │ ✘✔✘✘✘ CVE-2024-46816         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-46816,USN-8200-1
  │ ✘✔✘✘✘ CVE-2024-46821         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-46821
  │ ✘✔✘✘✘ CVE-2024-46834         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-46834
  │ ✘✔✘✘✘ CVE-2024-46855         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2024-46855
  │ ✘✔✘✘✘ CVE-2024-46859         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46859
  │ ✘✔✘✘✘ CVE-2024-46871         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46871
  │ ✘✔✘✘✘ CVE-2024-47658         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2024-47658
  │ ✘✔✘✘✘ CVE-2024-47690         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-47690
  │ ✘✔✘✘✘ CVE-2024-47691         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-47691,USN-7922-1
  │ ✘✔✘✘✘ CVE-2024-47718         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-47718
  │ ✘✔✘✘✘ CVE-2024-47726         HIGH         7.8   0.7%   ·  ↳ S:UBUNTU-CVE-2024-47726
  │ ✘✔✘✘✘ CVE-2024-47739         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2024-47739
  │ ✘✔✘✘✘ CVE-2024-47745         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-47745
  │ ✘✔✘✘✘ CVE-2024-49569         HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2024-49569
  │ ✘✔✘✘✘ CVE-2024-49854         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49854
  │ ✘✔✘✘✘ CVE-2024-49859         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49859
  │ ✘✔✘✘✘ CVE-2024-49861         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49861
  │ ✘✔✘✘✘ CVE-2024-49875         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2024-49875
  │ ✘✔✘✘✘ CVE-2024-49889         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-49889
  │ ✘✔✘✘✘ CVE-2024-49895         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-49895
  │ ✘✔✘✘✘ CVE-2024-49932         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49932
  │ ✘✔✘✘✘ CVE-2024-49934         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2024-49934
  │ ✘✔✘✘✘ CVE-2024-49940         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-49940
  │ ✘✔✘✘✘ CVE-2024-49950         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2024-49950,USN-7701-1
  │ ✘✔✘✘✘ CVE-2024-49989         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-49989
  │ ✘✔✘✘✘ CVE-2024-49991         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-49991
  │ ✘✔✘✘✘ CVE-2024-49992         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49992
  │ ✘✔✘✘✘ CVE-2024-50036         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50036
  │ ✘✔✘✘✘ CVE-2024-50061         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50061,USN-7874-1
  │ ✘✔✘✘✘ CVE-2024-50067         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50067,USN-7922-1
  │ ✘✔✘✘✘ CVE-2024-50073         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-50073,USN-7701-1
  │ ✘✔✘✘✘ CVE-2024-50095         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2024-50095,USN-7922-1
  │ ✘✔✘✘✘ CVE-2024-50115         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50115
  │ ✘✔✘✘✘ CVE-2024-50125         HIGH         8.0   0.3%   ·  ↳ S:UBUNTU-CVE-2024-50125
  │ ✘✔✘✘✘ CVE-2024-50187         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50187
  │ ✘✔✘✘✘ CVE-2024-50211         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50211
  │ ✘✔✘✘✘ CVE-2024-50217         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-50217
  │ ✘✔✘✘✘ CVE-2024-50241         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2024-50241
  │ ✘✔✘✘✘ CVE-2024-50280         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-50280
  │ ✘✔✘✘✘ CVE-2024-52559         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-52559
  │ ✘✔✘✘✘ CVE-2024-53073         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2024-53073
  │ ✘✔✘✘✘ CVE-2024-53079         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53079
  │ ✘✔✘✘✘ CVE-2024-53088         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53088
  │ ✘✔✘✘✘ CVE-2024-53090         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2024-53090,USN-7922-1
  │ ✘✔✘✘✘ CVE-2024-53093         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2024-53093
  │ ✘✔✘✘✘ CVE-2024-53144         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2024-53144
  │ ✘✔✘✘✘ CVE-2024-53168         HIGH         7.8   0.3%   ·  ↳ S:LSN-0112-1,UBUNTU-CVE-2024-53168,USN-7585-1
  │ ✘✔✘✘✘ CVE-2024-53216         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53216
  │ ✘✔✘✘✘ CVE-2024-53218         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53218,USN-7922-1
  │ ✘✔✘✘✘ CVE-2024-53220         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53220
  │ ✘✔✘✘✘ CVE-2024-53224         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-53224
  │ ✘✔✘✘✘ CVE-2024-54458         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-54458
  │ ✘✔✘✘✘ CVE-2024-56551         HIGH         7.8   0.2%   ·  ↳ S:LSN-0112-1,LSN-0113-1,UBUNTU-CVE-2024-56551,USN-7585-1
  │ ✘✔✘✘✘ CVE-2024-56590         HIGH         7.6   0.3%   ·  ↳ S:UBUNTU-CVE-2024-56590
  │ ✘✔✘✘✘ CVE-2024-56591         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-56591
  │ ✘✔✘✘✘ CVE-2024-56604         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56604
  │ ✘✔✘✘✘ CVE-2024-56609         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56609
  │ ✘✔✘✘✘ CVE-2024-56616         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56616
  │ ✘✔✘✘✘ CVE-2024-56623         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56623
  │ ✘✔✘✘✘ CVE-2024-56641         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2024-56641
  │ ✘✔✘✘✘ CVE-2024-56662         HIGH         7.8   0.6%   ·  ↳ S:UBUNTU-CVE-2024-56662,USN-7671-1
  │ ✘✔✘✘✘ CVE-2024-56664         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56664,USN-7874-1
  │ ✘✔✘✘✘ CVE-2024-56692         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56692
  │ ✘✔✘✘✘ CVE-2024-56703         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2024-56703
  │ ✘✔✘✘✘ CVE-2024-56759         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56759
  │ ✘✔✘✘✘ CVE-2024-57791         HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2024-57791
  │ ✘✔✘✘✘ CVE-2024-57795         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-57795
  │ ✘✔✘✘✘ CVE-2024-57857         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-57857
  │ ✘✔✘✘✘ CVE-2024-57883         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-57883
  │ ✘✔✘✘✘ CVE-2024-57887         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-57887
  │ ✘✔✘✘✘ CVE-2024-57893         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-57893
  │ ✘✔✘✘✘ CVE-2024-57896         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-57896
  │ ✘✔✘✘✘ CVE-2024-57975         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-57975
  │ ✘✔✘✘✘ CVE-2024-57976         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-57976
  │ ✘✔✘✘✘ CVE-2024-57982         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-57982
  │ ✘✔✘✘✘ CVE-2024-57996         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2024-57996,USN-7754-1
  │ ✘✔✘✘✘ CVE-2024-58034         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-58034
  │ ✘✔✘✘✘ CVE-2024-58053         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2024-58053
  │ ✘✔✘✘✘ CVE-2024-58089         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-58089
  │ ✘✔✘✘✘ CVE-2024-58093         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-58093,USN-7585-1
  │ ✘✔✘✘✘ CVE-2024-58094         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-58094
  │ ✘✔✘✘✘ CVE-2024-58241         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2024-58241
  │ ✘✔✘✘✘ CVE-2024-8805          HIGH         8.8   2.0%   ·  ↳ S:UBUNTU-CVE-2024-8805
  │ ✘✔✘✘✘ CVE-2025-1272          HIGH         7.7   0.3%   ·  ↳ S:UBUNTU-CVE-2025-1272
  │ ✘✔✘✘✘ CVE-2025-21629         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2025-21629
  │ ✘✔✘✘✘ CVE-2025-21682         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21682
  │ ✘✔✘✘✘ CVE-2025-21712         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21712
  │ ✘✔✘✘✘ CVE-2025-21726         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21726,USN-7990-1
  │ ✘✔✘✘✘ CVE-2025-21727         HIGH         7.8   0.2%   ·  ↳ S:LSN-0116-1,LSN-0122-1,UBUNTU-CVE-2025-21727,USN-7874-1
  │ ✘✔✘✘✘ CVE-2025-21734         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21734
  │ ✘✔✘✘✘ CVE-2025-21738         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21738
  │ ✘✔✘✘✘ CVE-2025-21758         HIGH         7.8  16.9%   ·  ↳ S:UBUNTU-CVE-2025-21758
  │ ✘✔✘✘✘ CVE-2025-21759         HIGH         7.8   7.8%   ·  ↳ S:UBUNTU-CVE-2025-21759
  │ ✘✔✘✘✘ CVE-2025-21766         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-21766
  │ ✘✔✘✘✘ CVE-2025-21780         HIGH         7.8   0.3%   ·  ↳ S:LSN-0119-1,UBUNTU-CVE-2025-21780,USN-8098-1
  │ ✘✔✘✘✘ CVE-2025-21792         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21792
  │ ✘✔✘✘✘ CVE-2025-21801         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-21801
  │ ✘✔✘✘✘ CVE-2025-21812         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21812
  │ ✘✔✘✘✘ CVE-2025-21844         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2025-21844
  │ ✘✔✘✘✘ CVE-2025-21855         HIGH         8.6   0.4%   ·  ↳ S:UBUNTU-CVE-2025-21855,USN-7922-1
  │ ✘✔✘✘✘ CVE-2025-21899         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21899
  │ ✘✔✘✘✘ CVE-2025-21959         HIGH         7.3   0.4%   ·  ↳ S:UBUNTU-CVE-2025-21959,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-21976         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-21976
  │ ✘✔✘✘✘ CVE-2025-21985         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21985
  │ ✘✔✘✘✘ CVE-2025-21991         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21991,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-21993         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21993,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-21999         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21999
  │ ✘✔✘✘✘ CVE-2025-22004         HIGH         8.6   0.4%   ·  ↳ S:UBUNTU-CVE-2025-22004,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-22020         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22020,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-22022         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22022
  │ ✘✔✘✘✘ CVE-2025-22025         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2025-22025
  │ ✘✔✘✘✘ CVE-2025-22035         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-22035,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-22045         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22045,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-22055         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2025-22055
  │ ✘✔✘✘✘ CVE-2025-22057         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22057
  │ ✘✔✘✘✘ CVE-2025-22072         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22072
  │ ✘✔✘✘✘ CVE-2025-22079         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22079,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-22083         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22083
  │ ✘✔✘✘✘ CVE-2025-22086         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-22086,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-22090         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22090
  │ ✘✔✘✘✘ CVE-2025-22104         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22104
  │ ✘✔✘✘✘ CVE-2025-22107         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22107
  │ ✘✔✘✘✘ CVE-2025-22109         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-22109
  │ ✘✔✘✘✘ CVE-2025-22121         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22121
  │ ✘✔✘✘✘ CVE-2025-23132         HIGH         7.0   0.4%   ·  ↳ S:UBUNTU-CVE-2025-23132
  │ ✘✔✘✘✘ CVE-2025-23142         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-23142
  │ ✘✔✘✘✘ CVE-2025-23150         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-23150
  │ ✘✔✘✘✘ CVE-2025-23156         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-23156
  │ ✘✔✘✘✘ CVE-2025-23157         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-23157
  │ ✘✔✘✘✘ CVE-2025-23158         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-23158
  │ ✘✔✘✘✘ CVE-2025-23159         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2025-23159
  │ ✘✔✘✘✘ CVE-2025-37738         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-37738
  │ ✘✔✘✘✘ CVE-2025-37739         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37739
  │ ✘✔✘✘✘ CVE-2025-37741         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37741
  │ ✘✔✘✘✘ CVE-2025-37749         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2025-37749
  │ ✘✔✘✘✘ CVE-2025-37756         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37756
  │ ✘✔✘✘✘ CVE-2025-37757         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2025-37757
  │ ✘✔✘✘✘ CVE-2025-37765         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37765
  │ ✘✔✘✘✘ CVE-2025-37780         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37780
  │ ✘✔✘✘✘ CVE-2025-37785         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37785,USN-7795-1
  │ ✘✔✘✘✘ CVE-2025-37789         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37789
  │ ✘✔✘✘✘ CVE-2025-37796         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37796
  │ ✘✔✘✘✘ CVE-2025-37797         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37797,USN-7701-1
  │ ✘✔✘✘✘ CVE-2025-37798         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37798,USN-7671-1
  │ ✘✔✘✘✘ CVE-2025-37800         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37800
  │ ✘✔✘✘✘ CVE-2025-37810         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37810
  │ ✘✔✘✘✘ CVE-2025-37817         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37817
  │ ✘✔✘✘✘ CVE-2025-37819         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37819
  │ ✘✔✘✘✘ CVE-2025-37823         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-37823
  │ ✘✔✘✘✘ CVE-2025-37838         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37838,USN-7874-1
  │ ✘✔✘✘✘ CVE-2025-37839         HIGH         7.8   0.3%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-37839
  │ ✘✔✘✘✘ CVE-2025-37840         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37840
  │ ✘✔✘✘✘ CVE-2025-37849         HIGH         8.8   0.3%   ·  ↳ S:LSN-120-1,UBUNTU-CVE-2025-37849,USN-8200-1
  │ ✘✔✘✘✘ CVE-2025-37885         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37885
  │ ✘✔✘✘✘ CVE-2025-37890         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37890,USN-7671-1
  │ ✘✔✘✘✘ CVE-2025-37892         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37892
  │ ✘✔✘✘✘ CVE-2025-37911         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37911
  │ ✘✔✘✘✘ CVE-2025-37913         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-37913
  │ ✘✔✘✘✘ CVE-2025-37914         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-37914
  │ ✘✔✘✘✘ CVE-2025-37915         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37915
  │ ✘✔✘✘✘ CVE-2025-37920         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37920
  │ ✘✔✘✘✘ CVE-2025-37923         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37923
  │ ✘✔✘✘✘ CVE-2025-37927         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37927
  │ ✘✔✘✘✘ CVE-2025-37928         HIGH         7.8   0.7%   ·  ↳ S:UBUNTU-CVE-2025-37928
  │ ✘✔✘✘✘ CVE-2025-37949         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37949
  │ ✘✔✘✘✘ CVE-2025-37991         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37991
  │ ✘✔✘✘✘ CVE-2025-37997         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37997,USN-7671-1
  │ ✘✔✘✘✘ CVE-2025-37998         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37998
  │ ✘✔✘✘✘ CVE-2025-38000         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38000,USN-7671-1
  │ ✘✔✘✘✘ CVE-2025-38001         HIGH         7.8   0.6%   ·  ↳ S:UBUNTU-CVE-2025-38001,USN-7671-1
  │ ✘✔✘✘✘ CVE-2025-38003         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-38003
  │ ✘✔✘✘✘ CVE-2025-38004         HIGH         7.3   0.3%   ·  ↳ S:UBUNTU-CVE-2025-38004
  │ ✘✔✘✘✘ CVE-2025-38022         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38022
  │ ✘✔✘✘✘ CVE-2025-38024         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-38024
  │ ✘✔✘✘✘ CVE-2025-38035         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2025-38035
  │ ✘✔✘✘✘ CVE-2025-38051         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38051
  │ ✘✔✘✘✘ CVE-2025-38058         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38058
  │ ✘✔✘✘✘ CVE-2025-38062         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38062
  │ ✘✔✘✘✘ CVE-2025-38064         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-38064
  │ ✘✔✘✘✘ CVE-2025-38065         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38065
  │ ✘✔✘✘✘ CVE-2025-38068         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38068
  │ ✘✔✘✘✘ CVE-2025-38069         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38069
  │ ✘✔✘✘✘ CVE-2025-38074         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38074
  │ ✘✔✘✘✘ CVE-2025-38078         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38078
  │ ✘✔✘✘✘ CVE-2025-38079         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-38079
  │ ✘✔✘✘✘ CVE-2025-38080         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38080
  │ ✘✔✘✘✘ CVE-2025-38083         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38083,USN-7701-1
  │ ✘✔✘✘✘ CVE-2025-38084         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38084
  │ ✘✔✘✘✘ CVE-2025-38085         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38085
  │ ✘✔✘✘✘ CVE-2025-38090         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38090
  │ ✘✔✘✘✘ CVE-2025-38095         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38095
  │ ✘✔✘✘✘ CVE-2025-38102         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38102
  │ ✘✔✘✘✘ CVE-2025-38103         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38103
  │ ✘✔✘✘✘ CVE-2025-38107         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38107
  │ ✘✔✘✘✘ CVE-2025-38108         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38108
  │ ✘✔✘✘✘ CVE-2025-38115         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38115
  │ ✘✔✘✘✘ CVE-2025-38117         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38117
  │ ✘✔✘✘✘ CVE-2025-38129         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-38129
  │ ✘✔✘✘✘ CVE-2025-38153         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38153
  │ ✘✔✘✘✘ CVE-2025-38157         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38157
  │ ✘✔✘✘✘ CVE-2025-38159         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38159
  │ ✘✔✘✘✘ CVE-2025-38161         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38161
  │ ✘✔✘✘✘ CVE-2025-38166         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38166
  │ ✘✔✘✘✘ CVE-2025-38173         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38173
  │ ✘✔✘✘✘ CVE-2025-38174         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-38174
  │ ✘✔✘✘✘ CVE-2025-38177         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38177,USN-7671-1
  │ ✘✔✘✘✘ CVE-2025-38180         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38180
  │ ✘✔✘✘✘ CVE-2025-38181         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2025-38181
  │ ✘✔✘✘✘ CVE-2025-38184         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38184
  │ ✘✔✘✘✘ CVE-2025-38192         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38192
  │ ✘✔✘✘✘ CVE-2025-38193         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38193
  │ ✘✔✘✘✘ CVE-2025-38204         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38204
  │ ✘✔✘✘✘ CVE-2025-38212         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-38212
  │ ✘✔✘✘✘ CVE-2025-38218         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38218
  │ ✘✔✘✘✘ CVE-2025-38226         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-38226
  │ ✘✔✘✘✘ CVE-2025-38230         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38230
  │ ✘✔✘✘✘ CVE-2025-38232         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38232
  │ ✘✔✘✘✘ CVE-2025-38234         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38234
  │ ✘✔✘✘✘ CVE-2025-38239         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38239
  │ ✘✔✘✘✘ CVE-2025-38245         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38245
  │ ✘✔✘✘✘ CVE-2025-38249         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38249
  │ ✘✔✘✘✘ CVE-2025-38250         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38250
  │ ✘✔✘✘✘ CVE-2025-38257         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-38257
  │ ✘✔✘✘✘ CVE-2025-38259         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38259
  │ ✘✔✘✘✘ CVE-2025-38261         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38261
  │ ✘✔✘✘✘ CVE-2025-38262         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38262
  │ ✘✔✘✘✘ CVE-2025-38280         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38280
  │ ✘✔✘✘✘ CVE-2025-38286         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38286
  │ ✘✔✘✘✘ CVE-2025-38298         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38298
  │ ✘✔✘✘✘ CVE-2025-38313         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38313
  │ ✘✔✘✘✘ CVE-2025-38320         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38320
  │ ✘✔✘✘✘ CVE-2025-38323         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38323
  │ ✘✔✘✘✘ CVE-2025-38331         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-38331
  │ ✘✔✘✘✘ CVE-2025-38333         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38333
  │ ✘✔✘✘✘ CVE-2025-38342         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38342
  │ ✘✔✘✘✘ CVE-2025-38346         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38346
  │ ✘✔✘✘✘ CVE-2025-38348         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38348
  │ ✘✔✘✘✘ CVE-2025-38350         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-38350,USN-7754-1
  │ ✘✔✘✘✘ CVE-2025-38352         HIGH         7.8   1.4% KEV  ↳ S:LSN-0116-1,LSN-0122-1,UBUNTU-CVE-2025-38352,USN-7874-1
  │ ✘✔✘✘✘ CVE-2025-38361         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38361
  │ ✘✔✘✘✘ CVE-2025-38375         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38375
  │ ✘✔✘✘✘ CVE-2025-38377         HIGH         8.8   0.3%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-38377
  │ ✘✔✘✘✘ CVE-2025-38386         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38386
  │ ✘✔✘✘✘ CVE-2025-38389         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38389
  │ ✘✔✘✘✘ CVE-2025-38395         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38395
  │ ✘✔✘✘✘ CVE-2025-38399         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2025-38399
  │ ✘✔✘✘✘ CVE-2025-38401         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-38401
  │ ✘✔✘✘✘ CVE-2025-38403         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38403
  │ ✘✔✘✘✘ CVE-2025-38415         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38415
  │ ✘✔✘✘✘ CVE-2025-38416         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-38416
  │ ✘✔✘✘✘ CVE-2025-38422         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38422
  │ ✘✔✘✘✘ CVE-2025-38424         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38424
  │ ✘✔✘✘✘ CVE-2025-38428         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38428
  │ ✘✔✘✘✘ CVE-2025-38445         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38445
  │ ✘✔✘✘✘ CVE-2025-38449         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38449
  │ ✘✔✘✘✘ CVE-2025-38459         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38459
  │ ✘✔✘✘✘ CVE-2025-38460         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38460
  │ ✘✔✘✘✘ CVE-2025-38464         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-38464
  │ ✘✔✘✘✘ CVE-2025-38470         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38470
  │ ✘✔✘✘✘ CVE-2025-38477         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-38477,USN-7795-1
  │ ✘✔✘✘✘ CVE-2025-38478         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38478
  │ ✘✔✘✘✘ CVE-2025-38482         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38482
  │ ✘✔✘✘✘ CVE-2025-38483         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38483
  │ ✘✔✘✘✘ CVE-2025-38494         HIGH         7.8   0.3%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-38494
  │ ✘✔✘✘✘ CVE-2025-38495         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2025-38495
  │ ✘✔✘✘✘ CVE-2025-38497         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38497
  │ ✘✔✘✘✘ CVE-2025-38498         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38498
  │ ✘✔✘✘✘ CVE-2025-38499         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38499
  │ ✘✔✘✘✘ CVE-2025-38514         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-38514
  │ ✘✔✘✘✘ CVE-2025-38524         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-38524
  │ ✘✔✘✘✘ CVE-2025-38529         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38529
  │ ✘✔✘✘✘ CVE-2025-38530         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38530
  │ ✘✔✘✘✘ CVE-2025-38538         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38538
  │ ✘✔✘✘✘ CVE-2025-38539         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38539
  │ ✘✔✘✘✘ CVE-2025-38542         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38542
  │ ✘✔✘✘✘ CVE-2025-38555         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38555
  │ ✘✔✘✘✘ CVE-2025-38556         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38556
  │ ✘✔✘✘✘ CVE-2025-38563         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2025-38563
  │ ✘✔✘✘✘ CVE-2025-38565         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38565
  │ ✘✔✘✘✘ CVE-2025-38572         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38572
  │ ✘✔✘✘✘ CVE-2025-38574         HIGH         8.6   0.4%   ·  ↳ S:UBUNTU-CVE-2025-38574
  │ ✘✔✘✘✘ CVE-2025-38577         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38577
  │ ✘✔✘✘✘ CVE-2025-38578         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38578
  │ ✘✔✘✘✘ CVE-2025-38584         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38584
  │ ✘✔✘✘✘ CVE-2025-38595         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38595
  │ ✘✔✘✘✘ CVE-2025-38604         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38604
  │ ✘✔✘✘✘ CVE-2025-38608         HIGH         8.6   0.4%   ·  ↳ S:UBUNTU-CVE-2025-38608
  │ ✘✔✘✘✘ CVE-2025-38614         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38614
  │ ✘✔✘✘✘ CVE-2025-38617         HIGH         7.8   0.4%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-38617,USN-7795-1
  │ ✘✔✘✘✘ CVE-2025-38618         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38618,USN-7795-1
  │ ✘✔✘✘✘ CVE-2025-38639         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38639
  │ ✘✔✘✘✘ CVE-2025-38643         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38643
  │ ✘✔✘✘✘ CVE-2025-38652         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38652
  │ ✘✔✘✘✘ CVE-2025-38666         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38666,USN-7922-1
  │ ✘✔✘✘✘ CVE-2025-38676         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2025-38676
  │ ✘✔✘✘✘ CVE-2025-38677         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38677
  │ ✘✔✘✘✘ CVE-2025-38679         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38679
  │ ✘✔✘✘✘ CVE-2025-38680         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38680
  │ ✘✔✘✘✘ CVE-2025-38685         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38685
  │ ✘✔✘✘✘ CVE-2025-38687         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2025-38687
  │ ✘✔✘✘✘ CVE-2025-38697         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-38697
  │ ✘✔✘✘✘ CVE-2025-38699         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38699
  │ ✘✔✘✘✘ CVE-2025-38702         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38702
  │ ✘✔✘✘✘ CVE-2025-38710         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38710
  │ ✘✔✘✘✘ CVE-2025-38713         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38713
  │ ✘✔✘✘✘ CVE-2025-38714         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38714
  │ ✘✔✘✘✘ CVE-2025-38715         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38715
  │ ✘✔✘✘✘ CVE-2025-38717         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-38717
  │ ✘✔✘✘✘ CVE-2025-38718         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38718
  │ ✘✔✘✘✘ CVE-2025-38729         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38729
  │ ✘✔✘✘✘ CVE-2025-39677         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39677
  │ ✘✔✘✘✘ CVE-2025-39683         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39683
  │ ✘✔✘✘✘ CVE-2025-39685         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39685
  │ ✘✔✘✘✘ CVE-2025-39686         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39686
  │ ✘✔✘✘✘ CVE-2025-39689         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39689
  │ ✘✔✘✘✘ CVE-2025-39691         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39691
  │ ✘✔✘✘✘ CVE-2025-39697         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39697
  │ ✘✔✘✘✘ CVE-2025-39710         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39710
  │ ✘✔✘✘✘ CVE-2025-39714         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39714
  │ ✘✔✘✘✘ CVE-2025-39730         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-39730
  │ ✘✔✘✘✘ CVE-2025-39735         HIGH         7.1   0.3%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-39735,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-39743         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-39743
  │ ✘✔✘✘✘ CVE-2025-39744         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39744
  │ ✘✔✘✘✘ CVE-2025-39749         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39749
  │ ✘✔✘✘✘ CVE-2025-39757         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39757
  │ ✘✔✘✘✘ CVE-2025-39759         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39759
  │ ✘✔✘✘✘ CVE-2025-39760         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39760
  │ ✘✔✘✘✘ CVE-2025-39766         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39766
  │ ✘✔✘✘✘ CVE-2025-39770         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-39770
  │ ✘✔✘✘✘ CVE-2025-39783         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39783
  │ ✘✔✘✘✘ CVE-2025-39787         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39787
  │ ✘✔✘✘✘ CVE-2025-39789         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39789
  │ ✘✔✘✘✘ CVE-2025-39797         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39797
  │ ✘✔✘✘✘ CVE-2025-39798         HIGH         7.3   0.3%   ·  ↳ S:UBUNTU-CVE-2025-39798
  │ ✘✔✘✘✘ CVE-2025-39800         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39800
  │ ✘✔✘✘✘ CVE-2025-39810         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39810
  │ ✘✔✘✘✘ CVE-2025-39817         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39817
  │ ✘✔✘✘✘ CVE-2025-39823         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39823
  │ ✘✔✘✘✘ CVE-2025-39824         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-39824
  │ ✘✔✘✘✘ CVE-2025-39826         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39826
  │ ✘✔✘✘✘ CVE-2025-39827         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39827
  │ ✘✔✘✘✘ CVE-2025-39828         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39828
  │ ✘✔✘✘✘ CVE-2025-39839         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-39839
  │ ✘✔✘✘✘ CVE-2025-39848         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39848
  │ ✘✔✘✘✘ CVE-2025-39853         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39853
  │ ✘✔✘✘✘ CVE-2025-39860         HIGH         8.0   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-39860
  │ ✘✔✘✘✘ CVE-2025-39863         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-39863
  │ ✘✔✘✘✘ CVE-2025-39864         HIGH         8.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-39864
  │ ✘✔✘✘✘ CVE-2025-39866         HIGH         7.8   0.3%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-39866
  │ ✘✔✘✘✘ CVE-2025-39869         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39869
  │ ✘✔✘✘✘ CVE-2025-39873         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39873
  │ ✘✔✘✘✘ CVE-2025-39883         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39883
  │ ✘✔✘✘✘ CVE-2025-39891         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39891
  │ ✘✔✘✘✘ CVE-2025-39901         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39901
  │ ✘✔✘✘✘ CVE-2025-39902         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39902
  │ ✘✔✘✘✘ CVE-2025-39911         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39911
  │ ✘✔✘✘✘ CVE-2025-39913         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39913
  │ ✘✔✘✘✘ CVE-2025-39927         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39927
  │ ✘✔✘✘✘ CVE-2025-39929         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-39929
  │ ✘✔✘✘✘ CVE-2025-39931         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39931
  │ ✘✔✘✘✘ CVE-2025-39945         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39945
  │ ✘✔✘✘✘ CVE-2025-39949         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39949
  │ ✘✔✘✘✘ CVE-2025-39952         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-39952
  │ ✘✔✘✘✘ CVE-2025-39955         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39955
  │ ✘✔✘✘✘ CVE-2025-39961         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39961
  │ ✘✔✘✘✘ CVE-2025-39964         HIGH         7.8   1.6% KEV  ↳ S:UBUNTU-CVE-2025-39964,USN-7922-1
  │ ✘✔✘✘✘ CVE-2025-39967         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39967
  │ ✘✔✘✘✘ CVE-2025-39968         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39968
  │ ✘✔✘✘✘ CVE-2025-39969         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39969
  │ ✘✔✘✘✘ CVE-2025-39970         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39970
  │ ✘✔✘✘✘ CVE-2025-39971         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39971
  │ ✘✔✘✘✘ CVE-2025-39972         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39972
  │ ✘✔✘✘✘ CVE-2025-39973         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39973
  │ ✘✔✘✘✘ CVE-2025-39985         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39985
  │ ✘✔✘✘✘ CVE-2025-39986         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39986
  │ ✘✔✘✘✘ CVE-2025-39987         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39987
  │ ✘✔✘✘✘ CVE-2025-39993         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39993,USN-7922-1
  │ ✘✔✘✘✘ CVE-2025-39994         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39994
  │ ✘✔✘✘✘ CVE-2025-39998         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39998
  │ ✘✔✘✘✘ CVE-2025-40006         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40006
  │ ✘✔✘✘✘ CVE-2025-40018         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40018,USN-7922-1
  │ ✘✔✘✘✘ CVE-2025-40025         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40025
  │ ✘✔✘✘✘ CVE-2025-40026         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40026
  │ ✘✔✘✘✘ CVE-2025-40027         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40027
  │ ✘✔✘✘✘ CVE-2025-40043         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-40043
  │ ✘✔✘✘✘ CVE-2025-40044         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40044
  │ ✘✔✘✘✘ CVE-2025-40048         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2025-40048
  │ ✘✔✘✘✘ CVE-2025-40053         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2025-40053
  │ ✘✔✘✘✘ CVE-2025-40064         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40064
  │ ✘✔✘✘✘ CVE-2025-40075         HIGH         8.1   0.5%   ·  ↳ S:UBUNTU-CVE-2025-40075
  │ ✘✔✘✘✘ CVE-2025-40081         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40081
  │ ✘✔✘✘✘ CVE-2025-40087         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2025-40087
  │ ✘✔✘✘✘ CVE-2025-40088         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40088
  │ ✘✔✘✘✘ CVE-2025-40092         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40092
  │ ✘✔✘✘✘ CVE-2025-40093         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40093
  │ ✘✔✘✘✘ CVE-2025-40094         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40094
  │ ✘✔✘✘✘ CVE-2025-40095         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40095
  │ ✘✔✘✘✘ CVE-2025-40104         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40104
  │ ✘✔✘✘✘ CVE-2025-40105         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40105
  │ ✘✔✘✘✘ CVE-2025-40111         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40111
  │ ✘✔✘✘✘ CVE-2025-40112         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40112
  │ ✘✔✘✘✘ CVE-2025-40123         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40123
  │ ✘✔✘✘✘ CVE-2025-40124         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40124
  │ ✘✔✘✘✘ CVE-2025-40135         HIGH         8.1   0.7%   ·  ↳ S:UBUNTU-CVE-2025-40135
  │ ✘✔✘✘✘ CVE-2025-40139         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40139
  │ ✘✔✘✘✘ CVE-2025-40140         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-40140
  │ ✘✔✘✘✘ CVE-2025-40149         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40149
  │ ✘✔✘✘✘ CVE-2025-40158         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2025-40158
  │ ✘✔✘✘✘ CVE-2025-40167         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40167
  │ ✘✔✘✘✘ CVE-2025-40168         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2025-40168
  │ ✘✔✘✘✘ CVE-2025-40170         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40170
  │ ✘✔✘✘✘ CVE-2025-40173         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40173
  │ ✘✔✘✘✘ CVE-2025-40187         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2025-40187
  │ ✘✔✘✘✘ CVE-2025-40190         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40190
  │ ✘✔✘✘✘ CVE-2025-40198         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40198
  │ ✘✔✘✘✘ CVE-2025-40204         HIGH         8.1   0.5%   ·  ↳ S:UBUNTU-CVE-2025-40204
  │ ✘✔✘✘✘ CVE-2025-40205         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40205
  │ ✘✔✘✘✘ CVE-2025-40206         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40206
  │ ✘✔✘✘✘ CVE-2025-40215         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40215,USN-8098-1
  │ ✘✔✘✘✘ CVE-2025-40233         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40233
  │ ✘✔✘✘✘ CVE-2025-40240         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2025-40240
  │ ✘✔✘✘✘ CVE-2025-40242         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40242
  │ ✘✔✘✘✘ CVE-2025-40243         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40243
  │ ✘✔✘✘✘ CVE-2025-40244         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40244
  │ ✘✔✘✘✘ CVE-2025-40248         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40248
  │ ✘✔✘✘✘ CVE-2025-40253         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-40253
  │ ✘✔✘✘✘ CVE-2025-40266         HIGH         8.2   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40266
  │ ✘✔✘✘✘ CVE-2025-40269         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40269
  │ ✘✔✘✘✘ CVE-2025-40271         HIGH         7.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-40271
  │ ✘✔✘✘✘ CVE-2025-40277         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40277
  │ ✘✔✘✘✘ CVE-2025-40280         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40280
  │ ✘✔✘✘✘ CVE-2025-40282         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-40282
  │ ✘✔✘✘✘ CVE-2025-40283         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40283
  │ ✘✔✘✘✘ CVE-2025-40303         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40303
  │ ✘✔✘✘✘ CVE-2025-40304         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40304
  │ ✘✔✘✘✘ CVE-2025-40306         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40306
  │ ✘✔✘✘✘ CVE-2025-40317         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40317
  │ ✘✔✘✘✘ CVE-2025-40322         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40322
  │ ✘✔✘✘✘ CVE-2025-40323         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40323
  │ ✘✔✘✘✘ CVE-2025-40331         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40331
  │ ✘✔✘✘✘ CVE-2025-40337         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2025-40337
  │ ✘✔✘✘✘ CVE-2025-40342         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2025-40342
  │ ✘✔✘✘✘ CVE-2025-40349         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40349
  │ ✘✔✘✘✘ CVE-2025-40354         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40354
  │ ✘✔✘✘✘ CVE-2025-40358         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2025-40358
  │ ✘✔✘✘✘ CVE-2025-54518         HIGH         7.3   0.3%   ·  ↳ S:UBUNTU-CVE-2025-54518
  │ ✘✔✘✘✘ CVE-2025-62626         HIGH         7.2   0.2%   ·  ↳ S:UBUNTU-CVE-2025-62626
  │ ✘✔✘✘✘ CVE-2025-68168         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68168
  │ ✘✔✘✘✘ CVE-2025-68206         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2025-68206
  │ ✘✔✘✘✘ CVE-2025-68241         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2025-68241
  │ ✘✔✘✘✘ CVE-2025-68254         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2025-68254
  │ ✘✔✘✘✘ CVE-2025-68255         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2025-68255
  │ ✘✔✘✘✘ CVE-2025-68256         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-68256
  │ ✘✔✘✘✘ CVE-2025-68261         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2025-68261
  │ ✘✔✘✘✘ CVE-2025-68283         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2025-68283
  │ ✘✔✘✘✘ CVE-2025-68286         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68286
  │ ✘✔✘✘✘ CVE-2025-68302         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2025-68302
  │ ✘✔✘✘✘ CVE-2025-68303         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-68303
  │ ✘✔✘✘✘ CVE-2025-68321         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2025-68321
  │ ✘✔✘✘✘ CVE-2025-68336         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2025-68336
  │ ✘✔✘✘✘ CVE-2025-68337         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2025-68337
  │ ✘✔✘✘✘ CVE-2025-68340         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-68340
  │ ✘✔✘✘✘ CVE-2025-68349         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2025-68349
  │ ✘✔✘✘✘ CVE-2025-68379         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-68379
  │ ✘✔✘✘✘ CVE-2025-68724         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-68724
  │ ✘✔✘✘✘ CVE-2025-68774         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2025-68774
  │ ✘✔✘✘✘ CVE-2025-68785         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68785
  │ ✘✔✘✘✘ CVE-2025-68795         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68795
  │ ✘✔✘✘✘ CVE-2025-68799         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2025-68799
  │ ✘✔✘✘✘ CVE-2025-68801         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68801
  │ ✘✔✘✘✘ CVE-2025-68818         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2025-68818
  │ ✘✔✘✘✘ CVE-2025-68819         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68819
  │ ✘✔✘✘✘ CVE-2025-68822         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68822
  │ ✘✔✘✘✘ CVE-2025-71073         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71073
  │ ✘✔✘✘✘ CVE-2025-71074         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71074
  │ ✘✔✘✘✘ CVE-2025-71075         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71075
  │ ✘✔✘✘✘ CVE-2025-71078         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71078
  │ ✘✔✘✘✘ CVE-2025-71082         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-71082
  │ ✘✔✘✘✘ CVE-2025-71085         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-71085
  │ ✘✔✘✘✘ CVE-2025-71086         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71086
  │ ✘✔✘✘✘ CVE-2025-71089         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-71089
  │ ✘✔✘✘✘ CVE-2025-71091         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71091
  │ ✘✔✘✘✘ CVE-2025-71109         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71109
  │ ✘✔✘✘✘ CVE-2025-71112         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71112
  │ ✘✔✘✘✘ CVE-2025-71120         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2025-71120
  │ ✘✔✘✘✘ CVE-2025-71131         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-71131
  │ ✘✔✘✘✘ CVE-2025-71136         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71136
  │ ✘✔✘✘✘ CVE-2025-71150         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-71150
  │ ✘✔✘✘✘ CVE-2025-71152         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71152
  │ ✘✔✘✘✘ CVE-2025-71161         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2025-71161
  │ ✘✔✘✘✘ CVE-2025-71162         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2025-71162
  │ ✘✔✘✘✘ CVE-2025-71192         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71192
  │ ✘✔✘✘✘ CVE-2025-71202         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71202
  │ ✘✔✘✘✘ CVE-2025-71221         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71221
  │ ✘✔✘✘✘ CVE-2025-71236         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-71236
  │ ✘✔✘✘✘ CVE-2025-71268         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-71268
  │ ✘✔✘✘✘ CVE-2025-71269         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71269
  │ ✘✔✘✘✘ CVE-2025-71274         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71274
  │ ✘✔✘✘✘ CVE-2025-71292         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-71292
  │ ✘✔✘✘✘ CVE-2026-100072        HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-100072
  │ ✘✔✘✘✘ CVE-2026-22980         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-22980
  │ ✘✔✘✘✘ CVE-2026-22990         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-22990
  │ ✘✔✘✘✘ CVE-2026-22991         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-22991
  │ ✘✔✘✘✘ CVE-2026-22997         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-22997
  │ ✘✔✘✘✘ CVE-2026-22998         HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2026-22998
  │ ✘✔✘✘✘ CVE-2026-22999         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-22999
  │ ✘✔✘✘✘ CVE-2026-23001         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23001
  │ ✘✔✘✘✘ CVE-2026-23003         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-23003
  │ ✘✔✘✘✘ CVE-2026-23004         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23004
  │ ✘✔✘✘✘ CVE-2026-23066         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23066
  │ ✘✔✘✘✘ CVE-2026-23068         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23068
  │ ✘✔✘✘✘ CVE-2026-23073         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23073
  │ ✘✔✘✘✘ CVE-2026-23074         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-23074,USN-8200-1
  │ ✘✔✘✘✘ CVE-2026-23076         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23076
  │ ✘✔✘✘✘ CVE-2026-23083         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23083
  │ ✘✔✘✘✘ CVE-2026-23089         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23089
  │ ✘✔✘✘✘ CVE-2026-23095         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-23095
  │ ✘✔✘✘✘ CVE-2026-23098         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23098
  │ ✘✔✘✘✘ CVE-2026-23099         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23099
  │ ✘✔✘✘✘ CVE-2026-23103         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23103
  │ ✘✔✘✘✘ CVE-2026-23105         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-23105
  │ ✘✔✘✘✘ CVE-2026-23191         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23191
  │ ✘✔✘✘✘ CVE-2026-23193         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-23193
  │ ✘✔✘✘✘ CVE-2026-23198         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23198
  │ ✘✔✘✘✘ CVE-2026-23204         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23204
  │ ✘✔✘✘✘ CVE-2026-23208         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23208
  │ ✘✔✘✘✘ CVE-2026-23209         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-23209,USN-8273-1
  │ ✘✔✘✘✘ CVE-2026-23216         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-23216
  │ ✘✔✘✘✘ CVE-2026-23222         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-23222
  │ ✘✔✘✘✘ CVE-2026-23227         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23227
  │ ✘✔✘✘✘ CVE-2026-23234         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23234
  │ ✘✔✘✘✘ CVE-2026-23235         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23235
  │ ✘✔✘✘✘ CVE-2026-23236         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23236
  │ ✘✔✘✘✘ CVE-2026-23242         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-23242
  │ ✘✔✘✘✘ CVE-2026-23243         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23243
  │ ✘✔✘✘✘ CVE-2026-23253         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-23253
  │ ✘✔✘✘✘ CVE-2026-23268         HIGH         7.8   0.1%   ·  ↳ S:LSN-0119-1,UBUNTU-CVE-2026-23268
  │ ✘✔✘✘✘ CVE-2026-23269         HIGH         7.1   0.1%   ·  ↳ S:LSN-0119-1,UBUNTU-CVE-2026-23269
  │ ✘✔✘✘✘ CVE-2026-23271         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23271
  │ ✘✔✘✘✘ CVE-2026-23272         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23272,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-23278         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23278
  │ ✘✔✘✘✘ CVE-2026-23281         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23281
  │ ✘✔✘✘✘ CVE-2026-23318         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23318
  │ ✘✔✘✘✘ CVE-2026-23336         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23336
  │ ✘✔✘✘✘ CVE-2026-23340         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23340
  │ ✘✔✘✘✘ CVE-2026-23361         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23361
  │ ✘✔✘✘✘ CVE-2026-23372         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-23372
  │ ✘✔✘✘✘ CVE-2026-23378         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23378
  │ ✘✔✘✘✘ CVE-2026-23388         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23388
  │ ✘✔✘✘✘ CVE-2026-23391         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-23391
  │ ✘✔✘✘✘ CVE-2026-23392         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-23392,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-23397         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23397
  │ ✘✔✘✘✘ CVE-2026-23406         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23406
  │ ✘✔✘✘✘ CVE-2026-23407         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23407
  │ ✘✔✘✘✘ CVE-2026-23410         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23410
  │ ✘✔✘✘✘ CVE-2026-23411         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23411
  │ ✘✔✘✘✘ CVE-2026-23444         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23444
  │ ✘✔✘✘✘ CVE-2026-23447         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23447
  │ ✘✔✘✘✘ CVE-2026-23448         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23448
  │ ✘✔✘✘✘ CVE-2026-23449         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23449
  │ ✘✔✘✘✘ CVE-2026-23456         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-23456
  │ ✘✔✘✘✘ CVE-2026-23457         HIGH         8.6   0.4%   ·  ↳ S:UBUNTU-CVE-2026-23457
  │ ✘✔✘✘✘ CVE-2026-23458         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23458
  │ ✘✔✘✘✘ CVE-2026-23462         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-23462
  │ ✘✔✘✘✘ CVE-2026-31392         HIGH         8.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31392
  │ ✘✔✘✘✘ CVE-2026-31393         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-31393
  │ ✘✔✘✘✘ CVE-2026-31396         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31396
  │ ✘✔✘✘✘ CVE-2026-31399         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31399
  │ ✘✔✘✘✘ CVE-2026-31403         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31403
  │ ✘✔✘✘✘ CVE-2026-31407         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31407
  │ ✘✔✘✘✘ CVE-2026-31408         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-31408
  │ ✘✔✘✘✘ CVE-2026-31417         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-31417
  │ ✘✔✘✘✘ CVE-2026-31426         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31426
  │ ✘✔✘✘✘ CVE-2026-31431         HIGH         7.8  98.1% KEV  ↳ S:LSN-0121-1,LSN-120-1,UBUNTU-CVE-2026-31431
  │ ✘✔✘✘✘ CVE-2026-31447         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-31447
  │ ✘✔✘✘✘ CVE-2026-31449         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31449
  │ ✘✔✘✘✘ CVE-2026-31450         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-31450
  │ ✘✔✘✘✘ CVE-2026-31452         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31452
  │ ✘✔✘✘✘ CVE-2026-31464         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-31464
  │ ✘✔✘✘✘ CVE-2026-31467         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-31467
  │ ✘✔✘✘✘ CVE-2026-31469         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-31469
  │ ✘✔✘✘✘ CVE-2026-31473         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-31473
  │ ✘✔✘✘✘ CVE-2026-31485         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31485
  │ ✘✔✘✘✘ CVE-2026-31486         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31486
  │ ✘✔✘✘✘ CVE-2026-31489         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31489
  │ ✘✔✘✘✘ CVE-2026-31494         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31494
  │ ✘✔✘✘✘ CVE-2026-31500         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31500
  │ ✘✔✘✘✘ CVE-2026-31502         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31502
  │ ✘✔✘✘✘ CVE-2026-31504         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-31504
  │ ✘✔✘✘✘ CVE-2026-31507         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31507
  │ ✘✔✘✘✘ CVE-2026-31516         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31516
  │ ✘✔✘✘✘ CVE-2026-31527         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31527
  │ ✘✔✘✘✘ CVE-2026-31532         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-31532
  │ ✘✔✘✘✘ CVE-2026-31548         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31548
  │ ✘✔✘✘✘ CVE-2026-31568         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31568
  │ ✘✔✘✘✘ CVE-2026-31570         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-31570
  │ ✘✔✘✘✘ CVE-2026-31576         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31576
  │ ✘✔✘✘✘ CVE-2026-31578         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31578
  │ ✘✔✘✘✘ CVE-2026-31580         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31580
  │ ✘✔✘✘✘ CVE-2026-31581         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31581
  │ ✘✔✘✘✘ CVE-2026-31583         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31583
  │ ✘✔✘✘✘ CVE-2026-31586         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-31586
  │ ✘✔✘✘✘ CVE-2026-31588         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31588
  │ ✘✔✘✘✘ CVE-2026-31597         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31597
  │ ✘✔✘✘✘ CVE-2026-31598         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-31598
  │ ✘✔✘✘✘ CVE-2026-31602         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31602
  │ ✘✔✘✘✘ CVE-2026-31622         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-31622
  │ ✘✔✘✘✘ CVE-2026-31626         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-31626
  │ ✘✔✘✘✘ CVE-2026-31627         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-31627
  │ ✘✔✘✘✘ CVE-2026-31629         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-31629
  │ ✘✔✘✘✘ CVE-2026-31630         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31630
  │ ✘✔✘✘✘ CVE-2026-31662         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-31662
  │ ✘✔✘✘✘ CVE-2026-31663         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31663
  │ ✘✔✘✘✘ CVE-2026-31665         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31665
  │ ✘✔✘✘✘ CVE-2026-31667         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31667
  │ ✘✔✘✘✘ CVE-2026-31673         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-31673
  │ ✘✔✘✘✘ CVE-2026-31674         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31674
  │ ✘✔✘✘✘ CVE-2026-31675         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31675
  │ ✘✔✘✘✘ CVE-2026-31676         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-31676
  │ ✘✔✘✘✘ CVE-2026-31678         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31678
  │ ✘✔✘✘✘ CVE-2026-31680         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-31680
  │ ✘✔✘✘✘ CVE-2026-31683         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31683
  │ ✘✔✘✘✘ CVE-2026-31686         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31686
  │ ✘✔✘✘✘ CVE-2026-31694         HIGH         7.8   0.3%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-31694
  │ ✘✔✘✘✘ CVE-2026-31696         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31696
  │ ✘✔✘✘✘ CVE-2026-31697         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31697
  │ ✘✔✘✘✘ CVE-2026-31698         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31698
  │ ✘✔✘✘✘ CVE-2026-31699         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31699
  │ ✘✔✘✘✘ CVE-2026-31700         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31700
  │ ✘✔✘✘✘ CVE-2026-31708         HIGH         8.1   0.4%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-31708
  │ ✘✔✘✘✘ CVE-2026-31715         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31715
  │ ✘✔✘✘✘ CVE-2026-31720         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-31720
  │ ✘✔✘✘✘ CVE-2026-31747         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31747
  │ ✘✔✘✘✘ CVE-2026-31748         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31748
  │ ✘✔✘✘✘ CVE-2026-31758         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-31758
  │ ✘✔✘✘✘ CVE-2026-31759         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-31759
  │ ✘✔✘✘✘ CVE-2026-31761         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31761
  │ ✘✔✘✘✘ CVE-2026-31768         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31768
  │ ✘✔✘✘✘ CVE-2026-31773         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-31773
  │ ✘✔✘✘✘ CVE-2026-31778         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31778
  │ ✘✔✘✘✘ CVE-2026-31780         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-31780
  │ ✘✔✘✘✘ CVE-2026-31786         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31786
  │ ✘✔✘✘✘ CVE-2026-31787         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31787
  │ ✘✔✘✘✘ CVE-2026-31788         HIGH         8.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31788
  │ ✘✔✘✘✘ CVE-2026-43015         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43015
  │ ✘✔✘✘✘ CVE-2026-43020         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43020
  │ ✘✔✘✘✘ CVE-2026-43025         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43025
  │ ✘✔✘✘✘ CVE-2026-43027         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43027
  │ ✘✔✘✘✘ CVE-2026-43028         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43028
  │ ✘✔✘✘✘ CVE-2026-43033         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43033
  │ ✘✔✘✘✘ CVE-2026-43040         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43040
  │ ✘✔✘✘✘ CVE-2026-43042         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43042
  │ ✘✔✘✘✘ CVE-2026-43047         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-43047
  │ ✘✔✘✘✘ CVE-2026-43048         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-43048
  │ ✘✔✘✘✘ CVE-2026-43049         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-43049
  │ ✘✔✘✘✘ CVE-2026-43050         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43050
  │ ✘✔✘✘✘ CVE-2026-43051         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-43051
  │ ✘✔✘✘✘ CVE-2026-43052         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43052
  │ ✘✔✘✘✘ CVE-2026-43060         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43060
  │ ✘✔✘✘✘ CVE-2026-43075         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43075
  │ ✘✔✘✘✘ CVE-2026-43076         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43076
  │ ✘✔✘✘✘ CVE-2026-43078         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43078
  │ ✘✔✘✘✘ CVE-2026-43091         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-43091
  │ ✘✔✘✘✘ CVE-2026-43093         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-43093
  │ ✘✔✘✘✘ CVE-2026-43110         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-43110
  │ ✘✔✘✘✘ CVE-2026-43111         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-43111
  │ ✘✔✘✘✘ CVE-2026-43113         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43113
  │ ✘✔✘✘✘ CVE-2026-43116         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43116
  │ ✘✔✘✘✘ CVE-2026-43126         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43126
  │ ✘✔✘✘✘ CVE-2026-43134         HIGH         8.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43134
  │ ✘✔✘✘✘ CVE-2026-43139         HIGH         8.6   0.4%   ·  ↳ S:UBUNTU-CVE-2026-43139
  │ ✘✔✘✘✘ CVE-2026-43141         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43141
  │ ✘✔✘✘✘ CVE-2026-43158         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-43158
  │ ✘✔✘✘✘ CVE-2026-43180         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43180
  │ ✘✔✘✘✘ CVE-2026-43184         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-43184
  │ ✘✔✘✘✘ CVE-2026-43187         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-43187
  │ ✘✔✘✘✘ CVE-2026-43190         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-43190
  │ ✘✔✘✘✘ CVE-2026-43194         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-43194
  │ ✘✔✘✘✘ CVE-2026-43203         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-43203
  │ ✘✔✘✘✘ CVE-2026-43206         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-43206
  │ ✘✔✘✘✘ CVE-2026-43207         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43207
  │ ✘✔✘✘✘ CVE-2026-43211         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43211
  │ ✘✔✘✘✘ CVE-2026-43226         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-43226
  │ ✘✔✘✘✘ CVE-2026-43230         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-43230
  │ ✘✔✘✘✘ CVE-2026-43232         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-43232
  │ ✘✔✘✘✘ CVE-2026-43233         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-43233
  │ ✘✔✘✘✘ CVE-2026-43236         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-43236
  │ ✘✔✘✘✘ CVE-2026-43241         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43241
  │ ✘✔✘✘✘ CVE-2026-43249         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-43249
  │ ✘✔✘✘✘ CVE-2026-43250         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43250
  │ ✘✔✘✘✘ CVE-2026-43253         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-43253
  │ ✘✔✘✘✘ CVE-2026-43279         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43279
  │ ✘✔✘✘✘ CVE-2026-43281         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43281
  │ ✘✔✘✘✘ CVE-2026-43283         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43283
  │ ✘✔✘✘✘ CVE-2026-43284         HIGH         8.8  94.2% KEV  ↳ S:UBUNTU-CVE-2026-43284
  │ ✘✔✘✘✘ CVE-2026-43296         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-43296
  │ ✘✔✘✘✘ CVE-2026-43328         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43328
  │ ✘✔✘✘✘ CVE-2026-43334         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-43334
  │ ✘✔✘✘✘ CVE-2026-43336         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-43336
  │ ✘✔✘✘✘ CVE-2026-43339         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43339
  │ ✘✔✘✘✘ CVE-2026-43350         HIGH         7.6   0.3%   ·  ↳ S:UBUNTU-CVE-2026-43350
  │ ✘✔✘✘✘ CVE-2026-43362         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-43362
  │ ✘✔✘✘✘ CVE-2026-43370         HIGH         7.8   0.1%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-43370
  │ ✘✔✘✘✘ CVE-2026-43373         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-43373
  │ ✘✔✘✘✘ CVE-2026-43386         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43386
  │ ✘✔✘✘✘ CVE-2026-43405         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-43405
  │ ✘✔✘✘✘ CVE-2026-43426         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43426
  │ ✘✔✘✘✘ CVE-2026-43427         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43427
  │ ✘✔✘✘✘ CVE-2026-43437         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43437
  │ ✘✔✘✘✘ CVE-2026-43449         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43449
  │ ✘✔✘✘✘ CVE-2026-43450         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43450
  │ ✘✔✘✘✘ CVE-2026-43452         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-43452
  │ ✘✔✘✘✘ CVE-2026-43456         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43456,USN-8919-1
  │ ✘✔✘✘✘ CVE-2026-43458         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43458
  │ ✘✔✘✘✘ CVE-2026-43459         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43459
  │ ✘✔✘✘✘ CVE-2026-43466         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-43466
  │ ✘✔✘✘✘ CVE-2026-43494         HIGH         7.8   0.4% KEV  ↳ S:UBUNTU-CVE-2026-43494
  │ ✘✔✘✘✘ CVE-2026-43497         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43497
  │ ✘✔✘✘✘ CVE-2026-43499         HIGH         7.8   0.9%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-43499,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-43500         HIGH         7.8  94.1% KEV  ↳ S:UBUNTU-CVE-2026-43500
  │ ✘✔✘✘✘ CVE-2026-43502         HIGH         7.8   0.3%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-43502
  │ ✘✔✘✘✘ CVE-2026-43503         HIGH         8.8   2.0%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-43503,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-45839         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45839
  │ ✘✔✘✘✘ CVE-2026-45843         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-45843
  │ ✘✔✘✘✘ CVE-2026-45852         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-45852
  │ ✘✔✘✘✘ CVE-2026-45856         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45856
  │ ✘✔✘✘✘ CVE-2026-45862         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45862
  │ ✘✔✘✘✘ CVE-2026-45866         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45866
  │ ✘✔✘✘✘ CVE-2026-45867         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45867
  │ ✘✔✘✘✘ CVE-2026-45885         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45885
  │ ✘✔✘✘✘ CVE-2026-45893         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45893
  │ ✘✔✘✘✘ CVE-2026-45894         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45894
  │ ✘✔✘✘✘ CVE-2026-45916         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45916
  │ ✘✔✘✘✘ CVE-2026-45920         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45920
  │ ✘✔✘✘✘ CVE-2026-45936         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45936
  │ ✘✔✘✘✘ CVE-2026-45942         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45942
  │ ✘✔✘✘✘ CVE-2026-45944         HIGH         7.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45944
  │ ✘✔✘✘✘ CVE-2026-45956         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45956
  │ ✘✔✘✘✘ CVE-2026-45958         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45958
  │ ✘✔✘✘✘ CVE-2026-45970         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45970
  │ ✘✔✘✘✘ CVE-2026-45984         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45984
  │ ✘✔✘✘✘ CVE-2026-45991         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45991
  │ ✘✔✘✘✘ CVE-2026-45994         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45994
  │ ✘✔✘✘✘ CVE-2026-46004         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46004
  │ ✘✔✘✘✘ CVE-2026-46006         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46006
  │ ✘✔✘✘✘ CVE-2026-46022         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46022
  │ ✘✔✘✘✘ CVE-2026-46024         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-46024
  │ ✘✔✘✘✘ CVE-2026-46027         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-46027
  │ ✘✔✘✘✘ CVE-2026-46033         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46033
  │ ✘✔✘✘✘ CVE-2026-46052         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-46052
  │ ✘✔✘✘✘ CVE-2026-46054         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46054
  │ ✘✔✘✘✘ CVE-2026-46056         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-46056
  │ ✘✔✘✘✘ CVE-2026-46064         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46064
  │ ✘✔✘✘✘ CVE-2026-46065         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46065
  │ ✘✔✘✘✘ CVE-2026-46068         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46068
  │ ✘✔✘✘✘ CVE-2026-46069         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46069
  │ ✘✔✘✘✘ CVE-2026-46070         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46070
  │ ✘✔✘✘✘ CVE-2026-46075         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46075
  │ ✘✔✘✘✘ CVE-2026-46078         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46078
  │ ✘✔✘✘✘ CVE-2026-46090         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46090
  │ ✘✔✘✘✘ CVE-2026-46099         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-46099
  │ ✘✔✘✘✘ CVE-2026-46102         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-46102
  │ ✘✔✘✘✘ CVE-2026-46107         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46107
  │ ✘✔✘✘✘ CVE-2026-46112         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46112
  │ ✘✔✘✘✘ CVE-2026-46113         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-46113
  │ ✘✔✘✘✘ CVE-2026-46116         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46116
  │ ✘✔✘✘✘ CVE-2026-46120         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46120
  │ ✘✔✘✘✘ CVE-2026-46122         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46122
  │ ✘✔✘✘✘ CVE-2026-46133         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-46133
  │ ✘✔✘✘✘ CVE-2026-46149         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46149
  │ ✘✔✘✘✘ CVE-2026-46150         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46150
  │ ✘✔✘✘✘ CVE-2026-46157         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46157
  │ ✘✔✘✘✘ CVE-2026-46163         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46163
  │ ✘✔✘✘✘ CVE-2026-46174         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-46174
  │ ✘✔✘✘✘ CVE-2026-46175         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46175
  │ ✘✔✘✘✘ CVE-2026-46177         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-46177
  │ ✘✔✘✘✘ CVE-2026-46178         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46178
  │ ✘✔✘✘✘ CVE-2026-46180         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46180
  │ ✘✔✘✘✘ CVE-2026-46181         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46181
  │ ✘✔✘✘✘ CVE-2026-46189         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46189
  │ ✘✔✘✘✘ CVE-2026-46191         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46191
  │ ✘✔✘✘✘ CVE-2026-46198         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-46198
  │ ✘✔✘✘✘ CVE-2026-46205         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46205
  │ ✘✔✘✘✘ CVE-2026-46206         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46206
  │ ✘✔✘✘✘ CVE-2026-46208         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46208
  │ ✘✔✘✘✘ CVE-2026-46209         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46209
  │ ✘✔✘✘✘ CVE-2026-46212         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-46212
  │ ✘✔✘✘✘ CVE-2026-46218         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46218
  │ ✘✔✘✘✘ CVE-2026-46219         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46219
  │ ✘✔✘✘✘ CVE-2026-46227         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46227
  │ ✘✔✘✘✘ CVE-2026-46238         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-46238
  │ ✘✔✘✘✘ CVE-2026-46241         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46241
  │ ✘✔✘✘✘ CVE-2026-46243         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-46243,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-46250         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46250
  │ ✘✔✘✘✘ CVE-2026-46253         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-46253
  │ ✘✔✘✘✘ CVE-2026-46259         HIGH         7.8   0.1%   ·  ↳ S:LSN-0121-1,LSN-0122-1,UBUNTU-CVE-2026-46259
  │ ✘✔✘✘✘ CVE-2026-46265         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-46265
  │ ✘✔✘✘✘ CVE-2026-46267         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46267
  │ ✘✔✘✘✘ CVE-2026-46270         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46270
  │ ✘✔✘✘✘ CVE-2026-46273         HIGH         8.6   0.4%   ·  ↳ S:UBUNTU-CVE-2026-46273
  │ ✘✔✘✘✘ CVE-2026-46275         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-46275
  │ ✘✔✘✘✘ CVE-2026-46294         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46294
  │ ✘✔✘✘✘ CVE-2026-46299         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46299
  │ ✘✔✘✘✘ CVE-2026-46301         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46301
  │ ✘✔✘✘✘ CVE-2026-46303         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-46303
  │ ✘✔✘✘✘ CVE-2026-46304         HIGH         7.5   0.3%   ·  ↳ S:LSN-0121-1,UBUNTU-CVE-2026-46304
  │ ✘✔✘✘✘ CVE-2026-46307         HIGH         8.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-46307
  │ ✘✔✘✘✘ CVE-2026-46320         HIGH         7.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-46320
  │ ✘✔✘✘✘ CVE-2026-46321         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46321
  │ ✘✔✘✘✘ CVE-2026-46322         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46322
  │ ✘✔✘✘✘ CVE-2026-46324         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46324
  │ ✘✔✘✘✘ CVE-2026-46328         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46328
  │ ✘✔✘✘✘ CVE-2026-46331         HIGH         7.8   0.6% KEV  ↳ S:UBUNTU-CVE-2026-46331,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-52909         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52909
  │ ✘✔✘✘✘ CVE-2026-52910         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52910,USN-8919-1
  │ ✘✔✘✘✘ CVE-2026-52912         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-52912
  │ ✘✔✘✘✘ CVE-2026-52915         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52915
  │ ✘✔✘✘✘ CVE-2026-52917         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52917
  │ ✘✔✘✘✘ CVE-2026-52918         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-52918
  │ ✘✔✘✘✘ CVE-2026-52919         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52919
  │ ✘✔✘✘✘ CVE-2026-52920         HIGH         8.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-52920
  │ ✘✔✘✘✘ CVE-2026-52922         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-52922
  │ ✘✔✘✘✘ CVE-2026-52923         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-52923
  │ ✘✔✘✘✘ CVE-2026-52927         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52927
  │ ✘✔✘✘✘ CVE-2026-52929         HIGH         7.5   0.9%   ·  ↳ S:UBUNTU-CVE-2026-52929
  │ ✘✔✘✘✘ CVE-2026-52934         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-52934
  │ ✘✔✘✘✘ CVE-2026-52942         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52942
  │ ✘✔✘✘✘ CVE-2026-52943         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-52943
  │ ✘✔✘✘✘ CVE-2026-52946         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-52946
  │ ✘✔✘✘✘ CVE-2026-52947         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52947
  │ ✘✔✘✘✘ CVE-2026-52954         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-52954
  │ ✘✔✘✘✘ CVE-2026-52956         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-52956
  │ ✘✔✘✘✘ CVE-2026-52957         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-52957
  │ ✘✔✘✘✘ CVE-2026-52962         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52962
  │ ✘✔✘✘✘ CVE-2026-52975         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52975
  │ ✘✔✘✘✘ CVE-2026-52981         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-52981
  │ ✘✔✘✘✘ CVE-2026-52991         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52991
  │ ✘✔✘✘✘ CVE-2026-52998         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-52998
  │ ✘✔✘✘✘ CVE-2026-53003         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-53003
  │ ✘✔✘✘✘ CVE-2026-53004         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53004
  │ ✘✔✘✘✘ CVE-2026-53009         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53009
  │ ✘✔✘✘✘ CVE-2026-53011         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53011
  │ ✘✔✘✘✘ CVE-2026-53016         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53016
  │ ✘✔✘✘✘ CVE-2026-53024         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53024
  │ ✘✔✘✘✘ CVE-2026-53025         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53025
  │ ✘✔✘✘✘ CVE-2026-53036         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53036
  │ ✘✔✘✘✘ CVE-2026-53040         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53040
  │ ✘✔✘✘✘ CVE-2026-53041         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53041
  │ ✘✔✘✘✘ CVE-2026-53050         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53050
  │ ✘✔✘✘✘ CVE-2026-53053         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53053
  │ ✘✔✘✘✘ CVE-2026-53059         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53059
  │ ✘✔✘✘✘ CVE-2026-53062         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53062
  │ ✘✔✘✘✘ CVE-2026-53068         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53068
  │ ✘✔✘✘✘ CVE-2026-53072         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53072
  │ ✘✔✘✘✘ CVE-2026-53075         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53075
  │ ✘✔✘✘✘ CVE-2026-53076         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53076
  │ ✘✔✘✘✘ CVE-2026-53077         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53077
  │ ✘✔✘✘✘ CVE-2026-53078         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53078
  │ ✘✔✘✘✘ CVE-2026-53089         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53089
  │ ✘✔✘✘✘ CVE-2026-53091         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53091
  │ ✘✔✘✘✘ CVE-2026-53112         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53112
  │ ✘✔✘✘✘ CVE-2026-53117         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53117
  │ ✘✔✘✘✘ CVE-2026-53120         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53120
  │ ✘✔✘✘✘ CVE-2026-53129         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53129
  │ ✘✔✘✘✘ CVE-2026-53130         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53130
  │ ✘✔✘✘✘ CVE-2026-53133         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53133
  │ ✘✔✘✘✘ CVE-2026-53136         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53136
  │ ✘✔✘✘✘ CVE-2026-53138         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53138
  │ ✘✔✘✘✘ CVE-2026-53146         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53146
  │ ✘✔✘✘✘ CVE-2026-53147         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53147
  │ ✘✔✘✘✘ CVE-2026-53148         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53148
  │ ✘✔✘✘✘ CVE-2026-53149         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53149
  │ ✘✔✘✘✘ CVE-2026-53156         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53156
  │ ✘✔✘✘✘ CVE-2026-53157         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53157
  │ ✘✔✘✘✘ CVE-2026-53159         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53159
  │ ✘✔✘✘✘ CVE-2026-53161         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53161
  │ ✘✔✘✘✘ CVE-2026-53185         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53185
  │ ✘✔✘✘✘ CVE-2026-53189         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53189
  │ ✘✔✘✘✘ CVE-2026-53194         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53194
  │ ✘✔✘✘✘ CVE-2026-53195         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53195
  │ ✘✔✘✘✘ CVE-2026-53199         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53199
  │ ✘✔✘✘✘ CVE-2026-53212         HIGH         7.8   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-53212,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-53223         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53223
  │ ✘✔✘✘✘ CVE-2026-53229         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53229
  │ ✘✔✘✘✘ CVE-2026-53230         HIGH         8.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53230
  │ ✘✔✘✘✘ CVE-2026-53239         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53239
  │ ✘✔✘✘✘ CVE-2026-53253         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53253
  │ ✘✔✘✘✘ CVE-2026-53254         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53254
  │ ✘✔✘✘✘ CVE-2026-53255         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53255
  │ ✘✔✘✘✘ CVE-2026-53256         HIGH         8.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53256
  │ ✘✔✘✘✘ CVE-2026-53262         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53262
  │ ✘✔✘✘✘ CVE-2026-53264         HIGH         7.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53264
  │ ✘✔✘✘✘ CVE-2026-53266         HIGH         8.8   0.9% KEV  ↳ S:UBUNTU-CVE-2026-53266
  │ ✘✔✘✘✘ CVE-2026-53267         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53267
  │ ✘✔✘✘✘ CVE-2026-53268         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53268
  │ ✘✔✘✘✘ CVE-2026-53270         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53270
  │ ✘✔✘✘✘ CVE-2026-53273         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53273
  │ ✘✔✘✘✘ CVE-2026-53275         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53275
  │ ✘✔✘✘✘ CVE-2026-53284         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53284
  │ ✘✔✘✘✘ CVE-2026-53294         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53294
  │ ✘✔✘✘✘ CVE-2026-53296         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53296
  │ ✘✔✘✘✘ CVE-2026-53303         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53303
  │ ✘✔✘✘✘ CVE-2026-53329         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53329
  │ ✘✔✘✘✘ CVE-2026-53354         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53354
  │ ✘✔✘✘✘ CVE-2026-53356         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53356
  │ ✘✔✘✘✘ CVE-2026-53358         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53358
  │ ✘✔✘✘✘ CVE-2026-53359         HIGH         8.8   1.4%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-53359,USN-8666-1
  │ ✘✔✘✘✘ CVE-2026-53368         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53368
  │ ✘✔✘✘✘ CVE-2026-53369         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53369
  │ ✘✔✘✘✘ CVE-2026-53374         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53374
  │ ✘✔✘✘✘ CVE-2026-53375         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53375
  │ ✘✔✘✘✘ CVE-2026-53388         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53388
  │ ✘✔✘✘✘ CVE-2026-53391         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53391
  │ ✘✔✘✘✘ CVE-2026-53392         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53392
  │ ✘✔✘✘✘ CVE-2026-53397         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-53397
  │ ✘✔✘✘✘ CVE-2026-53400         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53400
  │ ✘✔✘✘✘ CVE-2026-53401         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53401
  │ ✘✔✘✘✘ CVE-2026-63794         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63794
  │ ✘✔✘✘✘ CVE-2026-63796         HIGH         8.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-63796
  │ ✘✔✘✘✘ CVE-2026-63803         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63803
  │ ✘✔✘✘✘ CVE-2026-63806         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63806
  │ ✘✔✘✘✘ CVE-2026-63814         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63814
  │ ✘✔✘✘✘ CVE-2026-63815         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63815
  │ ✘✔✘✘✘ CVE-2026-63818         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63818
  │ ✘✔✘✘✘ CVE-2026-63819         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63819
  │ ✘✔✘✘✘ CVE-2026-63823         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63823
  │ ✘✔✘✘✘ CVE-2026-63824         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63824
  │ ✘✔✘✘✘ CVE-2026-63827         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63827
  │ ✘✔✘✘✘ CVE-2026-63828         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63828
  │ ✘✔✘✘✘ CVE-2026-63829         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63829
  │ ✘✔✘✘✘ CVE-2026-63831         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-63831
  │ ✘✔✘✘✘ CVE-2026-63833         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63833
  │ ✘✔✘✘✘ CVE-2026-63855         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63855
  │ ✘✔✘✘✘ CVE-2026-63856         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63856
  │ ✘✔✘✘✘ CVE-2026-63860         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63860
  │ ✘✔✘✘✘ CVE-2026-63870         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63870
  │ ✘✔✘✘✘ CVE-2026-63893         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-63893
  │ ✘✔✘✘✘ CVE-2026-63898         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63898
  │ ✘✔✘✘✘ CVE-2026-63899         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63899
  │ ✘✔✘✘✘ CVE-2026-63901         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63901
  │ ✘✔✘✘✘ CVE-2026-63902         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63902
  │ ✘✔✘✘✘ CVE-2026-63903         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63903
  │ ✘✔✘✘✘ CVE-2026-63904         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63904
  │ ✘✔✘✘✘ CVE-2026-63905         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63905
  │ ✘✔✘✘✘ CVE-2026-63913         HIGH         8.2   1.0%   ·  ↳ S:UBUNTU-CVE-2026-63913
  │ ✘✔✘✘✘ CVE-2026-63914         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63914
  │ ✘✔✘✘✘ CVE-2026-63915         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-63915
  │ ✘✔✘✘✘ CVE-2026-63916         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-63916
  │ ✘✔✘✘✘ CVE-2026-63917         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63917
  │ ✘✔✘✘✘ CVE-2026-63920         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63920
  │ ✘✔✘✘✘ CVE-2026-63921         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63921
  │ ✘✔✘✘✘ CVE-2026-63926         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63926
  │ ✘✔✘✘✘ CVE-2026-63927         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63927
  │ ✘✔✘✘✘ CVE-2026-63928         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63928
  │ ✘✔✘✘✘ CVE-2026-63930         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63930
  │ ✘✔✘✘✘ CVE-2026-63934         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63934
  │ ✘✔✘✘✘ CVE-2026-63942         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63942
  │ ✘✔✘✘✘ CVE-2026-63947         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-63947
  │ ✘✔✘✘✘ CVE-2026-63954         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63954
  │ ✘✔✘✘✘ CVE-2026-63956         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63956
  │ ✘✔✘✘✘ CVE-2026-63957         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63957
  │ ✘✔✘✘✘ CVE-2026-63971         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63971
  │ ✘✔✘✘✘ CVE-2026-64001         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64001
  │ ✘✔✘✘✘ CVE-2026-64002         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64002
  │ ✘✔✘✘✘ CVE-2026-64004         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64004
  │ ✘✔✘✘✘ CVE-2026-64005         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64005
  │ ✘✔✘✘✘ CVE-2026-64009         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64009
  │ ✘✔✘✘✘ CVE-2026-64010         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64010
  │ ✘✔✘✘✘ CVE-2026-64011         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64011
  │ ✘✔✘✘✘ CVE-2026-64014         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64014
  │ ✘✔✘✘✘ CVE-2026-64015         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64015
  │ ✘✔✘✘✘ CVE-2026-64026         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64026
  │ ✘✔✘✘✘ CVE-2026-64088         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64088
  │ ✘✔✘✘✘ CVE-2026-64093         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64093
  │ ✘✔✘✘✘ CVE-2026-64095         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64095
  │ ✘✔✘✘✘ CVE-2026-64096         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64096
  │ ✘✔✘✘✘ CVE-2026-64097         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64097
  │ ✘✔✘✘✘ CVE-2026-64103         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64103
  │ ✘✔✘✘✘ CVE-2026-64109         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64109
  │ ✘✔✘✘✘ CVE-2026-64112         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64112
  │ ✘✔✘✘✘ CVE-2026-64114         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64114
  │ ✘✔✘✘✘ CVE-2026-64115         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64115
  │ ✘✔✘✘✘ CVE-2026-64118         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64118
  │ ✘✔✘✘✘ CVE-2026-64123         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64123
  │ ✘✔✘✘✘ CVE-2026-64133         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64133
  │ ✘✔✘✘✘ CVE-2026-64178         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64178
  │ ✘✔✘✘✘ CVE-2026-64188         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64188
  │ ✘✔✘✘✘ CVE-2026-64189         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64189
  │ ✘✔✘✘✘ CVE-2026-64191         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64191
  │ ✘✔✘✘✘ CVE-2026-64206         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64206
  │ ✘✔✘✘✘ CVE-2026-64210         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64210
  │ ✘✔✘✘✘ CVE-2026-64218         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64218
  │ ✘✔✘✘✘ CVE-2026-64219         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64219
  │ ✘✔✘✘✘ CVE-2026-64221         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64221
  │ ✘✔✘✘✘ CVE-2026-64225         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64225
  │ ✘✔✘✘✘ CVE-2026-64237         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64237
  │ ✘✔✘✘✘ CVE-2026-64249         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64249
  │ ✘✔✘✘✘ CVE-2026-64266         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64266
  │ ✘✔✘✘✘ CVE-2026-64270         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64270
  │ ✘✔✘✘✘ CVE-2026-64271         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64271
  │ ✘✔✘✘✘ CVE-2026-64273         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64273
  │ ✘✔✘✘✘ CVE-2026-64274         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64274
  │ ✘✔✘✘✘ CVE-2026-64276         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64276
  │ ✘✔✘✘✘ CVE-2026-64279         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64279
  │ ✘✔✘✘✘ CVE-2026-64280         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64280
  │ ✘✔✘✘✘ CVE-2026-64298         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64298
  │ ✘✔✘✘✘ CVE-2026-64299         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64299
  │ ✘✔✘✘✘ CVE-2026-64304         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64304
  │ ✘✔✘✘✘ CVE-2026-64305         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64305
  │ ✘✔✘✘✘ CVE-2026-64312         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64312
  │ ✘✔✘✘✘ CVE-2026-64313         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64313
  │ ✘✔✘✘✘ CVE-2026-64315         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64315
  │ ✘✔✘✘✘ CVE-2026-64317         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64317
  │ ✘✔✘✘✘ CVE-2026-64318         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64318
  │ ✘✔✘✘✘ CVE-2026-64322         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64322
  │ ✘✔✘✘✘ CVE-2026-64323         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64323
  │ ✘✔✘✘✘ CVE-2026-64324         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64324
  │ ✘✔✘✘✘ CVE-2026-64330         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64330
  │ ✘✔✘✘✘ CVE-2026-64333         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64333
  │ ✘✔✘✘✘ CVE-2026-64340         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64340
  │ ✘✔✘✘✘ CVE-2026-64341         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64341
  │ ✘✔✘✘✘ CVE-2026-64342         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64342
  │ ✘✔✘✘✘ CVE-2026-64343         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64343
  │ ✘✔✘✘✘ CVE-2026-64344         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64344
  │ ✘✔✘✘✘ CVE-2026-64346         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64346
  │ ✘✔✘✘✘ CVE-2026-64348         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64348
  │ ✘✔✘✘✘ CVE-2026-64363         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64363
  │ ✘✔✘✘✘ CVE-2026-64372         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64372
  │ ✘✔✘✘✘ CVE-2026-64374         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-64374
  │ ✘✔✘✘✘ CVE-2026-64375         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64375
  │ ✘✔✘✘✘ CVE-2026-64378         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64378
  │ ✘✔✘✘✘ CVE-2026-64379         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64379
  │ ✘✔✘✘✘ CVE-2026-64381         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64381
  │ ✘✔✘✘✘ CVE-2026-64388         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64388
  │ ✘✔✘✘✘ CVE-2026-64403         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64403
  │ ✘✔✘✘✘ CVE-2026-64408         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64408
  │ ✘✔✘✘✘ CVE-2026-64411         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64411
  │ ✘✔✘✘✘ CVE-2026-64412         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64412
  │ ✘✔✘✘✘ CVE-2026-64413         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64413
  │ ✘✔✘✘✘ CVE-2026-64420         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64420
  │ ✘✔✘✘✘ CVE-2026-64422         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64422
  │ ✘✔✘✘✘ CVE-2026-64423         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64423
  │ ✘✔✘✘✘ CVE-2026-64424         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64424
  │ ✘✔✘✘✘ CVE-2026-64435         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64435
  │ ✘✔✘✘✘ CVE-2026-64436         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64436
  │ ✘✔✘✘✘ CVE-2026-64438         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64438
  │ ✘✔✘✘✘ CVE-2026-64440         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64440
  │ ✘✔✘✘✘ CVE-2026-64441         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64441
  │ ✘✔✘✘✘ CVE-2026-64442         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64442
  │ ✘✔✘✘✘ CVE-2026-64443         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64443
  │ ✘✔✘✘✘ CVE-2026-64444         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64444
  │ ✘✔✘✘✘ CVE-2026-64445         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64445
  │ ✘✔✘✘✘ CVE-2026-64446         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64446
  │ ✘✔✘✘✘ CVE-2026-64448         HIGH         8.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64448
  │ ✘✔✘✘✘ CVE-2026-64449         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64449
  │ ✘✔✘✘✘ CVE-2026-64452         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64452
  │ ✘✔✘✘✘ CVE-2026-64456         HIGH         7.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64456
  │ ✘✔✘✘✘ CVE-2026-64463         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64463
  │ ✘✔✘✘✘ CVE-2026-64468         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64468
  │ ✘✔✘✘✘ CVE-2026-64469         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64469
  │ ✘✔✘✘✘ CVE-2026-64496         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64496
  │ ✘✔✘✘✘ CVE-2026-64510         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64510
  │ ✘✔✘✘✘ CVE-2026-64529         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64529
  │ ✘✔✘✘✘ CVE-2026-64536         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64536
  │ ✘✔✘✘✘ CVE-2026-64539         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64539
  │ ✘✔✘✘✘ CVE-2026-64540         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64540
  │ ✘✔✘✘✘ CVE-2026-64543         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64543
  │ ✘✔✘✘✘ CVE-2026-64546         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64546
  │ ✘✔✘✘✘ CVE-2026-64547         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64547
  │ ✘✔✘✘✘ CVE-2026-64548         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64548
  │ ✘✔✘✘✘ CVE-2026-64550         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64550
  │ ✘✔✘✘✘ CVE-2026-64554         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64554
  │ ✘✔✘✘✘ CVE-2026-64557         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-64557
  │ ✘✔✘✘✘ CVE-2026-64562         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64562
  │ ✘✔✘✘✘ CVE-2026-64563         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64563
  │ ✘✔✘✘✘ CVE-2026-64567         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64567
  │ ✘✔✘✘✘ CVE-2026-64580         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64580
  │ ✘✔✘✘✘ CVE-2026-64581         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64581
  │ ✘✔✘✘✘ CVE-2026-64582         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64582
  │ ✘✔✘✘✘ CVE-2026-64583         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64583
  │ ✘✔✘✘✘ CVE-2026-64584         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64584
  │ ✘✔✘✘✘ CVE-2026-64585         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64585
  │ ✘✔✘✘✘ CVE-2026-64586         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64586
  │ ✘✔✘✘✘ CVE-2026-64587         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64587
  │ ✘✔✘✘✘ CVE-2026-64600         HIGH         7.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-64600
  │ ✘✔✘✘✘ CVE-2026-68091         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68091
  │ ✘✔✘✘✘ CVE-2026-68096         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68096
  │ ✘✔✘✘✘ CVE-2026-68097         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68097
  │ ✘✔✘✘✘ CVE-2026-68098         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68098
  │ ✘✔✘✘✘ CVE-2026-68100         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68100
  │ ✘✔✘✘✘ CVE-2026-68103         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68103
  │ ✘✔✘✘✘ CVE-2026-68104         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68104
  │ ✘✔✘✘✘ CVE-2026-68106         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68106
  │ ✘✔✘✘✘ CVE-2026-68107         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68107
  │ ✘✔✘✘✘ CVE-2026-68108         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68108
  │ ✘✔✘✘✘ CVE-2026-68118         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68118
  │ ✘✔✘✘✘ CVE-2026-68121         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68121
  │ ✘✔✘✘✘ CVE-2026-68125         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68125
  │ ✘✔✘✘✘ CVE-2026-68131         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68131
  │ ✘✔✘✘✘ CVE-2026-68138         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68138
  │ ✘✔✘✘✘ CVE-2026-68140         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68140
  │ ✘✔✘✘✘ CVE-2026-68141         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68141
  │ ✘✔✘✘✘ CVE-2026-68142         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68142
  │ ✘✔✘✘✘ CVE-2026-68143         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68143
  │ ✘✔✘✘✘ CVE-2026-68153         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68153
  │ ✘✔✘✘✘ CVE-2026-68155         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68155
  │ ✘✔✘✘✘ CVE-2026-68162         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68162
  │ ✘✔✘✘✘ CVE-2026-68192         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68192
  │ ✘✔✘✘✘ CVE-2026-68196         HIGH         8.3   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68196
  │ ✘✔✘✘✘ CVE-2026-68198         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68198
  │ ✘✔✘✘✘ CVE-2026-68199         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68199
  │ ✘✔✘✘✘ CVE-2026-68202         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68202
  │ ✘✔✘✘✘ CVE-2026-68204         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68204
  │ ✘✔✘✘✘ CVE-2026-68209         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68209
  │ ✘✔✘✘✘ CVE-2026-68210         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68210
  │ ✘✔✘✘✘ CVE-2026-68213         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68213
  │ ✘✔✘✘✘ CVE-2026-68216         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68216
  │ ✘✔✘✘✘ CVE-2026-68222         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68222
  │ ✘✔✘✘✘ CVE-2026-68236         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68236
  │ ✘✔✘✘✘ CVE-2026-68245         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68245
  │ ✘✔✘✘✘ CVE-2026-68255         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68255
  │ ✘✔✘✘✘ CVE-2026-68257         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68257
  │ ✘✔✘✘✘ CVE-2026-68258         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68258
  │ ✘✔✘✘✘ CVE-2026-68284         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68284
  │ ✘✔✘✘✘ CVE-2026-68287         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-68287
  │ ✘✔✘✘✘ CVE-2026-68294         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68294
  │ ✘✔✘✘✘ CVE-2026-68297         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68297
  │ ✘✔✘✘✘ CVE-2026-68299         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68299
  │ ✘✔✘✘✘ CVE-2026-68315         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-68315
  │ ✘✔✘✘✘ CVE-2026-68320         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68320
  │ ✘✔✘✘✘ CVE-2026-68323         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68323
  │ ✘✔✘✘✘ CVE-2026-68326         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68326
  │ ✘✔✘✘✘ CVE-2026-68329         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68329
  │ ✘✔✘✘✘ CVE-2026-68335         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68335
  │ ✘✔✘✘✘ CVE-2026-68338         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68338
  │ ✘✔✘✘✘ CVE-2026-68340         HIGH         7.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68340
  │ ✘✔✘✘✘ CVE-2026-68352         HIGH         8.3   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68352
  │ ✘✔✘✘✘ CVE-2026-68353         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68353
  │ ✘✔✘✘✘ CVE-2026-68354         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68354
  │ ✘✔✘✘✘ CVE-2026-68370         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68370
  │ ✘✔✘✘✘ CVE-2026-68373         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68373
  │ ✘✔✘✘✘ CVE-2026-68374         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68374
  │ ✘✔✘✘✘ CVE-2026-68376         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-68376
  │ ✘✔✘✘✘ CVE-2026-68377         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68377
  │ ✘✔✘✘✘ CVE-2026-68397         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68397
  │ ✘✔✘✘✘ CVE-2026-68398         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68398
  │ ✘✔✘✘✘ CVE-2026-68399         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68399
  │ ✘✔✘✘✘ CVE-2026-68402         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68402
  │ ✘✔✘✘✘ CVE-2026-68404         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68404
  │ ✘✔✘✘✘ CVE-2026-68414         HIGH         7.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68414
  │ ✘✔✘✘✘ CVE-2026-68417         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68417
  │ ✘✔✘✘✘ CVE-2026-68425         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68425
  │ ✘✔✘✘✘ CVE-2026-68427         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68427
  │ ✘✔✘✘✘ CVE-2026-68432         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68432
  │ ✘✔✘✘✘ CVE-2026-68433         HIGH         8.6   0.4%   ·  ↳ S:UBUNTU-CVE-2026-68433
  │ ✘✔✘✘✘ CVE-2026-68445         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68445
  │ ✘✔✘✘✘ CVE-2026-68447         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68447
  │ ✘✔✘✘✘ CVE-2026-68452         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68452
  │ ✘✔✘✘✘ CVE-2026-68453         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68453
  │ ✘✔✘✘✘ CVE-2026-68466         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68466
  │ ✘✔✘✘✘ CVE-2026-68467         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68467
  │ ✘✔✘✘✘ CVE-2026-68474         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68474
  │ ✘✔✘✘✘ CVE-2026-68479         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68479
  │ ✘✔✘✘✘ CVE-2026-72005         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72005
  │ ✘✔✘✘✘ CVE-2026-72019         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72019
  │ ✘✔✘✘✘ CVE-2026-72021         HIGH         8.2   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72021
  │ ✘✔✘✘✘ CVE-2026-72024         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-72024
  │ ✘✔✘✘✘ CVE-2026-72035         HIGH         8.2   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72035
  │ ✘✔✘✘✘ CVE-2026-72036         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72036
  │ ✘✔✘✘✘ CVE-2026-72049         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-72049
  │ ✘✔✘✘✘ CVE-2026-72051         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72051
  │ ✘✔✘✘✘ CVE-2026-72052         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72052
  │ ✘✔✘✘✘ CVE-2026-72053         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72053
  │ ✘✔✘✘✘ CVE-2026-72054         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72054
  │ ✘✔✘✘✘ CVE-2026-72055         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72055
  │ ✘✔✘✘✘ CVE-2026-72061         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72061
  │ ✘✔✘✘✘ CVE-2026-72066         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72066
  │ ✘✔✘✘✘ CVE-2026-72067         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72067
  │ ✘✔✘✘✘ CVE-2026-72102         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72102
  │ ✘✔✘✘✘ CVE-2026-72107         HIGH         8.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72107
  │ ✘✔✘✘✘ CVE-2026-72108         HIGH         7.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-72108
  │ ✘✔✘✘✘ CVE-2026-72113         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72113
  │ ✘✔✘✘✘ CVE-2026-72114         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72114
  │ ✘✔✘✘✘ CVE-2026-72115         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-72115
  │ ✘✔✘✘✘ CVE-2026-72116         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72116
  │ ✘✔✘✘✘ CVE-2026-72122         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72122
  │ ✘✔✘✘✘ CVE-2026-72123         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72123
  │ ✘✔✘✘✘ CVE-2026-72133         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72133
  │ ✘✔✘✘✘ CVE-2026-72135         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72135
  │ ✘✔✘✘✘ CVE-2026-72136         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72136
  │ ✘✔✘✘✘ CVE-2026-72144         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72144
  │ ✘✔✘✘✘ CVE-2026-72148         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-72148
  │ ✘✔✘✘✘ CVE-2026-72157         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-72157
  │ ✘✔✘✘✘ CVE-2026-72160         HIGH         8.8   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72160
  │ ✘✔✘✘✘ CVE-2026-72162         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72162
  │ ✘✔✘✘✘ CVE-2026-72164         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72164
  │ ✘✔✘✘✘ CVE-2026-72165         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72165
  │ ✘✔✘✘✘ CVE-2026-72170         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72170
  │ ✘✔✘✘✘ CVE-2026-72171         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72171
  │ ✘✔✘✘✘ CVE-2026-72181         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72181
  │ ✘✔✘✘✘ CVE-2026-72198         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72198
  │ ✘✔✘✘✘ CVE-2026-72203         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72203
  │ ✘✔✘✘✘ CVE-2026-72231         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72231
  │ ✘✔✘✘✘ CVE-2026-72232         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72232
  │ ✘✔✘✘✘ CVE-2026-72233         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-72233
  │ ✘✔✘✘✘ CVE-2026-72235         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-72235
  │ ✘✔✘✘✘ CVE-2026-72242         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72242
  │ ✘✔✘✘✘ CVE-2026-72243         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72243
  │ ✘✔✘✘✘ CVE-2026-72247         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72247
  │ ✘✔✘✘✘ CVE-2026-72250         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72250
  │ ✘✔✘✘✘ CVE-2026-72253         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72253
  │ ✘✔✘✘✘ CVE-2026-72255         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72255
  │ ✘✔✘✘✘ CVE-2026-72282         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72282
  │ ✘✔✘✘✘ CVE-2026-72284         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72284
  │ ✘✔✘✘✘ CVE-2026-72297         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72297
  │ ✘✔✘✘✘ CVE-2026-72298         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72298
  │ ✘✔✘✘✘ CVE-2026-72310         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72310
  │ ✘✔✘✘✘ CVE-2026-72314         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72314
  │ ✘✔✘✘✘ CVE-2026-72338         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72338
  │ ✘✔✘✘✘ CVE-2026-72342         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72342
  │ ✘✔✘✘✘ CVE-2026-72347         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72347
  │ ✘✔✘✘✘ CVE-2026-72350         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72350
  │ ✘✔✘✘✘ CVE-2026-72374         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72374
  │ ✘✔✘✘✘ CVE-2026-72375         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72375
  │ ✘✔✘✘✘ CVE-2026-72378         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72378
  │ ✘✔✘✘✘ CVE-2026-72380         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-72380
  │ ✘✔✘✘✘ CVE-2026-72383         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72383
  │ ✘✔✘✘✘ CVE-2026-72389         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72389
  │ ✘✔✘✘✘ CVE-2026-72390         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72390
  │ ✘✔✘✘✘ CVE-2026-72397         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72397
  │ ✘✔✘✘✘ CVE-2026-72400         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72400
  │ ✘✔✘✘✘ CVE-2026-72404         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72404
  │ ✘✔✘✘✘ CVE-2026-72406         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72406
  │ ✘✔✘✘✘ CVE-2026-72409         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72409
  │ ✘✔✘✘✘ CVE-2026-72416         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72416
  │ ✘✔✘✘✘ CVE-2026-72420         HIGH         8.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-72420
  │ ✘✔✘✘✘ CVE-2026-72434         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72434
  │ ✘✔✘✘✘ CVE-2026-72435         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72435
  │ ✘✔✘✘✘ CVE-2026-72444         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-72444
  │ ✘✔✘✘✘ CVE-2026-72450         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72450
  │ ✘✔✘✘✘ CVE-2026-72459         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-72459
  │ ✘✔✘✘✘ CVE-2026-72460         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-72460
  │ ✘✔✘✘✘ CVE-2026-72464         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72464
  │ ✘✔✘✘✘ CVE-2026-72476         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72476
  │ ✘✔✘✘✘ CVE-2026-72483         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72483
  │ ✘✔✘✘✘ CVE-2026-72487         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72487
  │ ✘✔✘✘✘ CVE-2026-72489         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72489
  │ ✘✔✘✘✘ CVE-2026-72502         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-72502
  │ ✘✔✘✘✘ CVE-2026-74256         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74256
  │ ✘✔✘✘✘ CVE-2026-74262         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74262
  │ ✘✔✘✘✘ CVE-2026-74281         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-74281
  │ ✘✔✘✘✘ CVE-2026-74282         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-74282
  │ ✘✔✘✘✘ CVE-2026-74283         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74283
  │ ✘✔✘✘✘ CVE-2026-74288         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74288
  │ ✘✔✘✘✘ CVE-2026-74289         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74289
  │ ✘✔✘✘✘ CVE-2026-74293         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74293
  │ ✘✔✘✘✘ CVE-2026-74295         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74295
  │ ✘✔✘✘✘ CVE-2026-74296         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74296
  │ ✘✔✘✘✘ CVE-2026-74297         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74297
  │ ✘✔✘✘✘ CVE-2026-74302         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74302
  │ ✘✔✘✘✘ CVE-2026-74317         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74317
  │ ✘✔✘✘✘ CVE-2026-74321         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-74321
  │ ✘✔✘✘✘ CVE-2026-74330         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74330
  │ ✘✔✘✘✘ CVE-2026-74334         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74334
  │ ✘✔✘✘✘ CVE-2026-74340         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74340
  │ ✘✔✘✘✘ CVE-2026-74341         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74341
  │ ✘✔✘✘✘ CVE-2026-74347         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74347
  │ ✘✔✘✘✘ CVE-2026-74349         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74349
  │ ✘✔✘✘✘ CVE-2026-74359         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74359
  │ ✘✔✘✘✘ CVE-2026-74365         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74365
  │ ✘✔✘✘✘ CVE-2026-74374         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-74374
  │ ✘✔✘✘✘ CVE-2026-74377         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74377
  │ ✘✔✘✘✘ CVE-2026-74378         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74378
  │ ✘✔✘✘✘ CVE-2026-74387         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74387
  │ ✘✔✘✘✘ CVE-2026-74388         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74388
  │ ✘✔✘✘✘ CVE-2026-74397         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74397
  │ ✘✔✘✘✘ CVE-2026-74405         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74405
  │ ✘✔✘✘✘ CVE-2026-74408         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74408
  │ ✘✔✘✘✘ CVE-2026-74410         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74410
  │ ✘✔✘✘✘ CVE-2026-74417         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74417
  │ ✘✔✘✘✘ CVE-2026-74438         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74438
  │ ✘✔✘✘✘ CVE-2026-74443         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74443
  │ ✘✔✘✘✘ CVE-2026-74444         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74444
  │ ✘✔✘✘✘ CVE-2026-74450         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74450
  │ ✘✔✘✘✘ CVE-2026-74453         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74453
  │ ✘✔✘✘✘ CVE-2026-74454         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74454
  │ ✘✔✘✘✘ CVE-2026-74456         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74456
  │ ✘✔✘✘✘ CVE-2026-74469         HIGH         8.8   1.5%   ·  ↳ S:UBUNTU-CVE-2026-74469
  │ ✘✔✘✘✘ CVE-2026-74471         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74471
  │ ✘✔✘✘✘ CVE-2026-74479         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74479
  │ ✘✔✘✘✘ CVE-2026-74482         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74482
  │ ✘✔✘✘✘ CVE-2026-74485         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74485
  │ ✘✔✘✘✘ CVE-2026-74488         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74488
  │ ✘✔✘✘✘ CVE-2026-74490         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74490
  │ ✘✔✘✘✘ CVE-2026-74492         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74492
  │ ✘✔✘✘✘ CVE-2026-74496         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74496
  │ ✘✔✘✘✘ CVE-2026-74497         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74497
  │ ✘✔✘✘✘ CVE-2026-74507         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74507
  │ ✘✔✘✘✘ CVE-2026-74508         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74508
  │ ✘✔✘✘✘ CVE-2026-74510         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74510
  │ ✘✔✘✘✘ CVE-2026-74512         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74512
  │ ✘✔✘✘✘ CVE-2026-74519         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74519
  │ ✘✔✘✘✘ CVE-2026-74527         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74527
  │ ✘✔✘✘✘ CVE-2026-74540         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74540
  │ ✘✔✘✘✘ CVE-2026-74544         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74544
  │ ✘✔✘✘✘ CVE-2026-74548         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74548
  │ ✘✔✘✘✘ CVE-2026-74549         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74549
  │ ✘✔✘✘✘ CVE-2026-74550         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74550
  │ ✘✔✘✘✘ CVE-2026-74557         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74557
  │ ✘✔✘✘✘ CVE-2026-74563         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74563
  │ ✘✔✘✘✘ CVE-2026-74564         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74564
  │ ✘✔✘✘✘ CVE-2026-74565         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74565
  │ ✘✔✘✘✘ CVE-2026-74567         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74567
  │ ✘✔✘✘✘ CVE-2026-74575         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74575
  │ ✘✔✘✘✘ CVE-2026-74578         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74578
  │ ✘✔✘✘✘ CVE-2026-74580         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74580
  │ ✘✔✘✘✘ CVE-2026-74582         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74582
  │ ✘✔✘✘✘ CVE-2026-74583         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74583
  │ ✘✔✘✘✘ CVE-2026-74584         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74584
  │ ✘✔✘✘✘ CVE-2026-74589         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74589
  │ ✘✔✘✘✘ CVE-2026-74592         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74592
  │ ✘✔✘✘✘ CVE-2026-74598         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74598
  │ ✘✔✘✘✘ CVE-2026-74601         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74601
  │ ✘✔✘✘✘ CVE-2026-74609         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74609
  │ ✘✔✘✘✘ CVE-2026-74613         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74613
  │ ✘✔✘✘✘ CVE-2026-74615         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74615
  │ ✘✔✘✘✘ CVE-2026-74625         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74625
  │ ✘✔✘✘✘ CVE-2026-74626         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74626
  │ ✘✔✘✘✘ CVE-2026-74630         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74630
  │ ✘✔✘✘✘ CVE-2026-74631         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74631
  │ ✘✔✘✘✘ CVE-2026-74632         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74632
  │ ✘✔✘✘✘ CVE-2026-74637         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74637
  │ ✘✔✘✘✘ CVE-2026-74641         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74641
  │ ✘✔✘✘✘ CVE-2026-74648         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74648
  │ ✘✔✘✘✘ CVE-2026-74649         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74649
  │ ✘✔✘✘✘ CVE-2026-74651         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74651
  │ ✘✔✘✘✘ CVE-2026-74656         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74656
  │ ✘✔✘✘✘ CVE-2026-74660         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74660
  │ ✘✔✘✘✘ CVE-2026-74663         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74663
  │ ✘✔✘✘✘ CVE-2026-74666         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74666
  │ ✘✔✘✘✘ CVE-2026-74667         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74667
  │ ✘✔✘✘✘ CVE-2026-74668         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74668
  │ ✘✔✘✘✘ CVE-2026-74675         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74675
  │ ✘✔✘✘✘ CVE-2026-74684         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74684
  │ ✘✔✘✘✘ CVE-2026-74687         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74687
  │ ✘✔✘✘✘ CVE-2026-74689         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74689
  │ ✘✔✘✘✘ CVE-2026-74690         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74690
  │ ✘✔✘✘✘ CVE-2026-74691         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-74691
  │ ✘✔✘✘✘ CVE-2026-74692         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74692
  │ ✘✔✘✘✘ CVE-2026-74695         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74695
  │ ✘✔✘✘✘ CVE-2026-74697         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74697
  │ ✘✔✘✘✘ CVE-2026-74700         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74700
  │ ✘✔✘✘✘ CVE-2026-74701         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74701
  │ ✘✔✘✘✘ CVE-2026-74704         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-74704
  │ ✘✔✘✘✘ CVE-2026-74717         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-74717
  │ ✘✔✘✘✘ CVE-2026-74720         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74720
  │ ✘✔✘✘✘ CVE-2026-74724         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74724
  │ ✘✔✘✘✘ CVE-2026-74725         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74725
  │ ✘✔✘✘✘ CVE-2026-74726         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74726
  │ ✘✔✘✘✘ CVE-2026-74739         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74739
  │ ✘✔✘✘✘ CVE-2026-74747         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74747
  │ ✘✔✘✘✘ CVE-2026-74748         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-74748
  │ ✘✔✘✘✘ CVE-2026-80536         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80536
  │ ✘✔✘✘✘ CVE-2026-80540         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80540
  │ ✘✔✘✘✘ CVE-2026-80541         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80541
  │ ✘✔✘✘✘ CVE-2026-80548         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80548
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
  │ ✘✔✘✘✘ CVE-2026-80579         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80579
  │ ✘✔✘✘✘ CVE-2026-80580         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80580
  │ ✘✔✘✘✘ CVE-2026-80584         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80584
  │ ✘✔✘✘✘ CVE-2026-80590         HIGH         8.6   0.6%   ·  ↳ S:UBUNTU-CVE-2026-80590
  │ ✘✔✘✘✘ CVE-2026-80591         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80591
  │ ✘✔✘✘✘ CVE-2026-80593         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80593
  │ ✘✔✘✘✘ CVE-2026-80599         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80599
  │ ✘✔✘✘✘ CVE-2026-80601         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80601
  │ ✘✔✘✘✘ CVE-2026-80619         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80619
  │ ✘✔✘✘✘ CVE-2026-80622         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80622
  │ ✘✔✘✘✘ CVE-2026-80628         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80628
  │ ✘✔✘✘✘ CVE-2026-80635         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80635
  │ ✘✔✘✘✘ CVE-2026-80637         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-80637
  │ ✘✔✘✘✘ CVE-2026-80645         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80645
  │ ✘✔✘✘✘ CVE-2026-80646         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-80646
  │ ✘✔✘✘✘ CVE-2026-80649         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80649
  │ ✘✔✘✘✘ CVE-2026-80664         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80664
  │ ✘✔✘✘✘ CVE-2026-80680         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80680
  │ ✘✔✘✘✘ CVE-2026-80706         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80706
  │ ✘✔✘✘✘ CVE-2026-80707         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-80707
  │ ✘✔✘✘✘ CVE-2026-80710         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80710
  │ ✘✔✘✘✘ CVE-2026-80716         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80716
  │ ✘✔✘✘✘ CVE-2026-80717         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-80717
  │ ✘✔✘✘✘ CVE-2026-80718         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80718
  │ ✘✔✘✘✘ CVE-2026-80731         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80731
  │ ✘✔✘✘✘ CVE-2026-80732         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80732
  │ ✘✔✘✘✘ CVE-2026-80737         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80737
  │ ✘✔✘✘✘ CVE-2026-80738         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80738
  │ ✘✔✘✘✘ CVE-2026-80747         HIGH         8.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80747
  │ ✘✔✘✘✘ CVE-2026-80752         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80752
  │ ✘✔✘✘✘ CVE-2026-80754         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80754
  │ ✘✔✘✘✘ CVE-2026-80921         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80921
  │ ✘✔✘✘✘ CVE-2026-80928         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80928
  │ ✘✔✘✘✘ CVE-2026-80931         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80931
  │ ✘✔✘✘✘ CVE-2026-80932         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80932
  │ ✘✔✘✘✘ CVE-2026-80944         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80944
  │ ✘✔✘✘✘ CVE-2026-80947         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80947
  │ ✘✔✘✘✘ CVE-2026-80952         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80952
  │ ✘✔✘✘✘ CVE-2026-80967         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80967
  │ ✘✔✘✘✘ CVE-2026-80971         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80971
  │ ✘✔✘✘✘ CVE-2026-80977         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80977
  │ ✘✔✘✘✘ CVE-2026-80978         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-80978
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
  │ ✘✔✘✘✘ CVE-2026-89440         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89440
  │ ✘✔✘✘✘ CVE-2026-89441         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89441
  │ ✘✔✘✘✘ CVE-2026-89452         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89452
  │ ✘✔✘✘✘ CVE-2026-89456         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89456
  │ ✘✔✘✘✘ CVE-2026-89465         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89465
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
  │ ✘✔✘✘✘ CVE-2026-89504         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89504
  │ ✘✔✘✘✘ CVE-2026-89508         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89508
  │ ✘✔✘✘✘ CVE-2026-89510         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89510
  │ ✘✔✘✘✘ CVE-2026-89511         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89511
  │ ✘✔✘✘✘ CVE-2026-89524         HIGH         8.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89524
  │ ✘✔✘✘✘ CVE-2026-89528         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89528
  │ ✘✔✘✘✘ CVE-2026-89540         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89540
  │ ✘✔✘✘✘ CVE-2026-89544         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89544
  │ ✘✔✘✘✘ CVE-2026-89545         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89545
  │ ✘✔✘✘✘ CVE-2026-89548         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89548
  │ ✘✔✘✘✘ CVE-2026-89549         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89549
  │ ✘✔✘✘✘ CVE-2026-89553         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89553
  │ ✘✔✘✘✘ CVE-2026-89557         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89557
  │ ✘✔✘✘✘ CVE-2026-89559         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89559
  │ ✘✔✘✘✘ CVE-2026-89562         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89562
  │ ✘✔✘✘✘ CVE-2026-89563         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89563
  │ ✘✔✘✘✘ CVE-2026-89569         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89569
  │ ✘✔✘✘✘ CVE-2026-89573         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89573
  │ ✘✔✘✘✘ CVE-2026-89574         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89574
  │ ✘✔✘✘✘ CVE-2026-89580         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89580
  │ ✘✔✘✘✘ CVE-2026-89585         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89585
  │ ✘✔✘✘✘ CVE-2026-89586         HIGH         8.2   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89586
  │ ✘✔✘✘✘ CVE-2026-89596         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89596
  │ ✘✔✘✘✘ CVE-2026-89597         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89597
  │ ✘✔✘✘✘ CVE-2026-89599         HIGH         8.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89599
  │ ✘✔✘✘✘ CVE-2026-89601         HIGH         8.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89601
  │ ✘✔✘✘✘ CVE-2026-89605         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89605
  │ ✘✔✘✘✘ CVE-2026-89606         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89606
  │ ✘✔✘✘✘ CVE-2026-89607         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89607
  │ ✘✔✘✘✘ CVE-2026-89608         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89608
  │ ✘✔✘✘✘ CVE-2026-89609         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89609
  │ ✘✔✘✘✘ CVE-2026-89626         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89626
  │ ✘✔✘✘✘ CVE-2026-89632         HIGH         8.2   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89632
  │ ✘✔✘✘✘ CVE-2026-89638         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89638
  │ ✘✔✘✘✘ CVE-2026-89640         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89640
  │ ✘✔✘✘✘ CVE-2026-89647         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89647
  │ ✘✔✘✘✘ CVE-2026-89665         HIGH         8.2   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89665
  │ ✘✔✘✘✘ CVE-2026-89699         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-89699
  │ ✘✔✘✘✘ CVE-2026-89707         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-89707
  │ ✘✔✘✘✘ CVE-2026-89709         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89709
  │ ✘✔✘✘✘ CVE-2026-89711         HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89711
  │ ✘✔✘✘✘ CVE-2026-89720         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89720
  │ ✘✔✘✘✘ CVE-2026-89723         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89723
  │ ✘✔✘✘✘ CVE-2026-89724         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89724
  │ ✘✔✘✘✘ CVE-2026-89725         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89725
  │ ✘✔✘✘✘ CVE-2026-89729         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89729
  │ ✘✔✘✘✘ CVE-2026-89733         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89733
  │ ✘✔✘✘✘ CVE-2026-89736         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89736
  │ ✘✔✘✘✘ CVE-2026-89738         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89738
  │ ✘✔✘✘✘ CVE-2026-89742         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89742
  │ ✘✔✘✘✘ CVE-2026-89761         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89761
  │ ✘✔✘✘✘ CVE-2026-89762         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89762
  │ ✘✔✘✘✘ CVE-2026-89763         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-89763
  │ ✘✔✘✘✘ CVE-2026-89777         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89777
  │ ✘✔✘✘✘ CVE-2026-89789         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89789
  │ ✘✔✘✘✘ CVE-2026-89795         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89795
  │ ✘✔✘✘✘ CVE-2026-89799         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89799
  │ ✘✔✘✘✘ CVE-2026-89823         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89823
  │ ✘✔✘✘✘ CVE-2026-89832         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89832
  │ ✘✔✘✘✘ CVE-2026-89838         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89838
  │ ✘✔✘✘✘ CVE-2026-89840         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89840
  │ ✘✔✘✘✘ CVE-2026-89848         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89848
  │ ✘✔✘✘✘ CVE-2026-89854         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89854
  │ ✘✔✘✘✘ CVE-2026-89856         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89856
  │ ✘✔✘✘✘ CVE-2026-89860         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89860
  │ ✘✔✘✘✘ CVE-2026-89861         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89861
  │ ✘✔✘✘✘ CVE-2026-89877         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89877
  │ ✘✔✘✘✘ CVE-2026-89880         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89880
  │ ✘✔✘✘✘ CVE-2026-89883         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89883
  │ ✘✔✘✘✘ CVE-2026-89887         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89887
  │ ✘✔✘✘✘ CVE-2026-89890         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89890
  │ ✘✔✘✘✘ CVE-2026-89893         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89893
  │ ✘✔✘✘✘ CVE-2026-89897         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-89897
  │ ✘✔✘✘✘ CVE-2026-89899         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89899
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
  │ ✘✔✘✘✘ CVE-2026-89965         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89965
  │ ✘✔✘✘✘ CVE-2026-89968         HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2026-89968
  │ ✘✔✘✘✘ CVE-2026-89973         HIGH         8.2   0.6%   ·  ↳ S:UBUNTU-CVE-2026-89973
  │ ✘✔✘✘✘ CVE-2026-89979         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89979
  │ ✘✔✘✘✘ CVE-2026-89988         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89988
  │ ✘✔✘✘✘ CVE-2026-89997         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89997
  │ ✘✔✘✘✘ CVE-2026-89999         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-89999
  │ ✘✔✘✘✘ CVE-2026-90000         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90000
  │ ✘✔✘✘✘ CVE-2026-90002         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90002
  │ ✘✔✘✘✘ CVE-2026-90007         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90007
  │ ✘✔✘✘✘ CVE-2026-90013         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90013
  │ ✘✔✘✘✘ CVE-2026-90016         HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90016
  │ ✘✔✘✘✘ CVE-2026-90017         HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90017
  │ ✘✔✘✘✘ CVE-2026-90018         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90018
  │ ✘✔✘✘✘ CVE-2026-90025         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90025
  │ ✘✔✘✘✘ CVE-2026-90032         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90032
  │ ✘✔✘✘✘ CVE-2026-90041         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-90041
  │ ✘✔✘✘✘ CVE-2026-90044         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90044
  │ ✘✔✘✘✘ CVE-2026-90045         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90045
  │ ✘✔✘✘✘ CVE-2026-90057         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90057
  │ ✘✔✘✘✘ CVE-2026-90062         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90062
  │ ✘✔✘✘✘ CVE-2026-90067         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90067
  │ ✘✔✘✘✘ CVE-2026-90102         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90102
  │ ✘✔✘✘✘ CVE-2026-90103         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90103
  │ ✘✔✘✘✘ CVE-2026-90111         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90111
  │ ✘✔✘✘✘ CVE-2026-90141         HIGH         7.3   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90141
  │ ✘✔✘✘✘ CVE-2026-90143         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90143
  │ ✘✔✘✘✘ CVE-2026-90149         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90149
  │ ✘✔✘✘✘ CVE-2026-90203         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90203
  │ ✘✔✘✘✘ CVE-2026-90204         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90204
  │ ✘✔✘✘✘ CVE-2026-90205         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90205
  │ ✘✔✘✘✘ CVE-2026-90207         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90207
  │ ✘✔✘✘✘ CVE-2026-90223         HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90223
  │ ✘✔✘✘✘ CVE-2026-90225         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90225
  │ ✘✔✘✘✘ CVE-2026-90227         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90227
  │ ✘✔✘✘✘ CVE-2026-90234         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90234
  │ ✘✔✘✘✘ CVE-2026-90237         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90237
  │ ✘✔✘✘✘ CVE-2026-90286         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90286
  │ ✘✔✘✘✘ CVE-2026-90292         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90292
  │ ✘✔✘✘✘ CVE-2026-90293         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90293
  │ ✘✔✘✘✘ CVE-2026-90294         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-90294
  │ ✘✔✘✘✘ CVE-2026-90301         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-90301
  │ ✘✔✘✘✘ CVE-2026-90316         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90316
  │ ✘✔✘✘✘ CVE-2026-90320         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90320
  │ ✘✔✘✘✘ CVE-2026-90321         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90321
  │ ✘✔✘✘✘ CVE-2026-90329         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-90329
  │ ✘✔✘✘✘ CVE-2026-90341         HIGH         7.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90341
  │ ✘✔✘✘✘ CVE-2026-90343         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90343
  │ ✘✔✘✘✘ CVE-2026-90347         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90347
  │ ✘✔✘✘✘ CVE-2026-90379         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-90379
  │ ✘✔✘✘✘ CVE-2026-90383         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90383
  │ ✘✔✘✘✘ CVE-2026-90403         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-90403
  │ ✘✔✘✘✘ CVE-2026-90419         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90419
  │ ✘✔✘✘✘ CVE-2026-90435         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-90435
  │ ✘✔✘✘✘ CVE-2026-92511         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-92511
  │ ✘✔✘✘✘ CVE-2026-92522         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-92522
  │ ✘✔✘✘✘ CVE-2026-92525         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92525
  │ ✘✔✘✘✘ CVE-2026-93037         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93037
  │ ✘✔✘✘✘ CVE-2026-93039         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93039
  │ ✘✔✘✘✘ CVE-2026-93042         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-93042
  │ ✘✔✘✘✘ CVE-2026-93054         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-93054
  │ ✘✔✘✘✘ CVE-2026-93095         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93095
  │ ✘✔✘✘✘ CVE-2026-93105         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93105
  │ ✘✔✘✘✘ CVE-2026-93151         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-93151
  │ ✘✔✘✘✘ CVE-2026-93170         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93170
  │ ✘✔✘✘✘ CVE-2026-93175         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93175
  │ ✘✔✘✘✘ CVE-2026-93177         HIGH         7.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93177
  │ ✘✔✘✘✘ CVE-2026-93178         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93178
  │ ✘✔✘✘✘ CVE-2026-93189         HIGH         8.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-93189
  │ ✘✔✘✘✘ CVE-2026-93192         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93192
  │ ✘✔✘✘✘ CVE-2026-93196         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93196
  │ ✘✔✘✘✘ CVE-2026-93203         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-93203
  │ ✘✔✘✘✘ CVE-2026-93221         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-93221
  │ ✘✔✘✘✘ CVE-2026-93237         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93237
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
  │ ✘✔✘✘✘ CVE-2026-97531         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97531
  │ ✘✔✘✘✘ CVE-2026-97536         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97536
  │ ✘✔✘✘✘ CVE-2026-97557         HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-97557
  │ ✘✔✘✘✘ CVE-2026-97608         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97608
  │ ✘✔✘✘✘ CVE-2026-97612         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97612
  │ ✘✔✘✘✘ CVE-2026-97910         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97910
  │ ✘✔✘✘✘ CVE-2026-97926         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97926
  │ ✘✔✘✘✘ CVE-2026-97931         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-97931
  │ ✘✔✘✘✘ CVE-2026-97940         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97940
  │ ✘✔✘✘✘ CVE-2026-97953         HIGH         7.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-97953
  │ ✘✔✘✘✘ CVE-2026-98017         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98017
  │ ✘✔✘✘✘ CVE-2026-98027         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98027
  │ ✘✔✘✘✘ CVE-2026-98030         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98030
  │ ✘✔✘✘✘ CVE-2026-98056         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-98056
  │ ✘✔✘✘✘ CVE-2026-98069         HIGH         8.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-98069
  │ ✘✔✘✘✘ CVE-2026-98070         HIGH         8.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-98070
  │ ✘✔✘✘✘ CVE-2026-98096         HIGH         7.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-98096
  │ ✘✔✘✘✘ CVE-2026-98116         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98116
  │ ✘✔✘✘✘ CVE-2026-98130         HIGH         8.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-98130
  │ ✘✔✘✘✘ CVE-2026-98156         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98156
  │ ✘✔✘✘✘ CVE-2026-98164         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98164
  │ ✘✔✘✘✘ CVE-2026-98169         HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-98169
  │ ✘✔✘✘✘ CVE-2026-98171         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-98171
  │ ✘✔✘✘✘ CVE-2026-98174         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-98174
  │ ✘✔✘✘✘ CVE-2026-98175         HIGH         7.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-98175
  │ ✘✔✘✘✘ CVE-2026-98197         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98197
  │ ✘✔✘✘✘ CVE-2026-98229         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98229
  │ ✘✔✘✘✘ CVE-2026-98241         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98241
  │ ✘✔✘✘✘ CVE-2026-98251         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98251
  │ ✘✔✘✘✘ CVE-2026-98252         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98252
  │ ✘✔✘✘✘ CVE-2026-98257         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-98257
  │ ✘✔✘✘✘ CVE-2026-98276         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98276
  │ ✘✔✘✘✘ CVE-2026-98282         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98282
  │ ✘✔✘✘✘ CVE-2026-98283         HIGH         8.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98283
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
  │ ✘✔✘✘✘ CVE-2026-98364         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98364
  │ ✘✔✘✘✘ CVE-2026-98367         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98367
  │ ✘✔✘✘✘ CVE-2026-98383         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98383
  │ ✘✔✘✘✘ CVE-2026-98401         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-98401
  │ ✘✔✘✘✘ CVE-2026-98419         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98419
  │ ✘✔✘✘✘ CVE-2026-98436         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98436
  │ ✘✔✘✘✘ CVE-2026-98451         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-98451
  │ ✘✔✘✘✘ CVE-2026-98454         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-98454
  │ ✘✔✘✘✘ CVE-2026-98456         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98456
  │ ✘✔✘✘✘ CVE-2026-98479         HIGH         7.5   0.4%   ·  ↳ S:UBUNTU-CVE-2026-98479
  │ ✘✔✘✘✘ CVE-2026-98485         HIGH         7.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98485
  │ ✘✔✘✘✘ CVE-2026-98491         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98491
  │ ✘✔✘✘✘ CVE-2026-98499         HIGH         8.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-98499
  │ ✘✔✘✘✘ CVE-2026-98501         HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-98501
  │ ✘✔✘✘✘ CVE-2026-98507         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98507
  │ ✘✔✘✘✘ CVE-2026-98515         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98515
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
  │ ✘✔✘✘✘ CVE-2026-98975         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98975
  │ ✘✔✘✘✘ CVE-2026-98978         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98978
  │ ✘✔✘✘✘ CVE-2026-98980         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98980
  │ ✘✔✘✘✘ CVE-2026-98981         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98981
  │ ✘✔✘✘✘ CVE-2026-98993         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98993
  │ ✘✔✘✘✘ CVE-2026-99002         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99002
  │ ✘✔✘✘✘ CVE-2026-99032         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99032
  │ ✘✔✘✘✘ CVE-2026-99053         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99053
  │ ✘✔✘✘✘ CVE-2026-99054         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99054
  │ ✘✔✘✘✘ CVE-2026-99077         HIGH         7.4   0.4%   ·  ↳ S:UBUNTU-CVE-2026-99077
  │ ✘✔✘✘✘ CVE-2026-99081         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-99081
  │ ✘✔✘✘✘ CVE-2026-99082         HIGH         8.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99082
  │ ✘✔✘✘✘ CVE-2026-99083         HIGH         8.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-99083
  │ ✘✔✘✘✘ CVE-2026-99109         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99109
  │ ✘✔✘✘✘ CVE-2026-99122         HIGH         7.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99122
  │ ✘✔✘✘✘ CVE-2026-99123         HIGH         7.1   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99123
  │ ✘✔✘✘✘ CVE-2026-99136         HIGH         7.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99136
  │ ✘✔✘✘✘ CVE-2026-99152         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-99152
  │ ✘✔✘✘✘ CVE-2026-99156         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99156
  │ ✘✔✘✘✘ CVE-2026-99167         HIGH         7.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-99167
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
  │ ✘✔✘✘✘ CVE-2018-7191          MEDIUM       5.5   0.7%   ·  ↳ S:UBUNTU-CVE-2018-7191
  │ ✘✔✘✘✘ CVE-2019-15213         MEDIUM       4.9   0.7%   ·  ↳ S:UBUNTU-CVE-2019-15213
  │ ✘✔✘✘✘ CVE-2019-20794         MEDIUM       4.7   0.5%   ·  ↳ S:UBUNTU-CVE-2019-20794
  │ ✘✔✘✘✘ CVE-2020-12363         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2020-12363
  │ ✘✔✘✘✘ CVE-2020-12364         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2020-12364
  │ ✘✔✘✘✘ CVE-2020-14304         MEDIUM       4.4   0.4%   ·  ↳ S:UBUNTU-CVE-2020-14304
  │ ✘✔✘✘✘ CVE-2020-15802         MEDIUM       5.9   7.1%   ·  ↳ S:UBUNTU-CVE-2020-15802
  │ ✘✔✘✘✘ CVE-2020-24504         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2020-24504
  │ ✘✔✘✘✘ CVE-2020-26140         MEDIUM       6.5   2.9%   ·  ↳ S:UBUNTU-CVE-2020-26140
  │ ✘✔✘✘✘ CVE-2020-26142         MEDIUM       5.3   2.1%   ·  ↳ S:UBUNTU-CVE-2020-26142
  │ ✘✔✘✘✘ CVE-2020-26143         MEDIUM       6.5   4.2%   ·  ↳ S:UBUNTU-CVE-2020-26143
  │ ✘✔✘✘✘ CVE-2020-26144         MEDIUM       6.5   4.9%   ·  ↳ S:UBUNTU-CVE-2020-26144
  │ ✘✔✘✘✘ CVE-2020-26146         MEDIUM       5.3   5.6%   ·  ↳ S:UBUNTU-CVE-2020-26146
  │ ✘✔✘✘✘ CVE-2020-27835         MEDIUM       4.9   0.3%   ·  ↳ S:UBUNTU-CVE-2020-27835
  │ ✘✔✘✘✘ CVE-2020-36310         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2020-36310
  │ ✘✔✘✘✘ CVE-2020-36776         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2020-36776
  │ ✘✔✘✘✘ CVE-2020-36784         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2020-36784
  │ ✘✔✘✘✘ CVE-2021-20320         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2021-20320
  │ ✘✔✘✘✘ CVE-2021-31615         MEDIUM       5.3   0.4%   ·  ↳ S:UBUNTU-CVE-2021-31615
  │ ✘✔✘✘✘ CVE-2021-33096         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2021-33096
  │ ✘✔✘✘✘ CVE-2021-3714          MEDIUM       5.9   1.6%   ·  ↳ S:UBUNTU-CVE-2021-3714
  │ ✘✔✘✘✘ CVE-2021-4148          MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2021-4148
  │ ✘✔✘✘✘ CVE-2021-46941         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-46941
  │ ✘✔✘✘✘ CVE-2021-46987         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-46987
  │ ✘✔✘✘✘ CVE-2021-47024         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47024
  │ ✘✔✘✘✘ CVE-2021-47074         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47074
  │ ✘✔✘✘✘ CVE-2021-47077         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47077
  │ ✘✔✘✘✘ CVE-2021-47139         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47139
  │ ✘✔✘✘✘ CVE-2021-47143         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47143
  │ ✘✔✘✘✘ CVE-2021-47182         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47182
  │ ✘✔✘✘✘ CVE-2021-47205         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47205
  │ ✘✔✘✘✘ CVE-2021-47211         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47211,USN-7585-1
  │ ✘✔✘✘✘ CVE-2021-47234         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47234
  │ ✘✔✘✘✘ CVE-2021-47265         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47265
  │ ✘✔✘✘✘ CVE-2021-47275         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47275
  │ ✘✔✘✘✘ CVE-2021-47335         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47335
  │ ✘✔✘✘✘ CVE-2021-47362         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47362
  │ ✘✔✘✘✘ CVE-2021-47381         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47381
  │ ✘✔✘✘✘ CVE-2021-47399         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47399
  │ ✘✔✘✘✘ CVE-2021-47407         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47407
  │ ✘✔✘✘✘ CVE-2021-47408         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2021-47408
  │ ✘✔✘✘✘ CVE-2021-47414         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47414
  │ ✘✔✘✘✘ CVE-2021-47428         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47428
  │ ✘✔✘✘✘ CVE-2021-47432         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2021-47432
  │ ✘✔✘✘✘ CVE-2021-47452         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47452
  │ ✘✔✘✘✘ CVE-2021-47455         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47455
  │ ✘✔✘✘✘ CVE-2021-47473         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47473
  │ ✘✔✘✘✘ CVE-2021-47491         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47491
  │ ✘✔✘✘✘ CVE-2021-47498         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47498
  │ ✘✔✘✘✘ CVE-2021-47508         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47508
  │ ✘✔✘✘✘ CVE-2021-47523         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47523
  │ ✘✔✘✘✘ CVE-2021-47560         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47560
  │ ✘✔✘✘✘ CVE-2021-47582         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47582
  │ ✘✔✘✘✘ CVE-2021-47599         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2021-47599,USN-8098-1
  │ ✘✔✘✘✘ CVE-2021-47618         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47618
  │ ✘✔✘✘✘ CVE-2021-47622         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2021-47622
  │ ✘✔✘✘✘ CVE-2021-47644         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2021-47644
  │ ✘✔✘✘✘ CVE-2021-47648         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2021-47648
  │ ✘✔✘✘✘ CVE-2022-0480          MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-0480
  │ ✘✔✘✘✘ CVE-2022-1205          MEDIUM       4.7   0.4%   ·  ↳ S:UBUNTU-CVE-2022-1205
  │ ✘✔✘✘✘ CVE-2022-1280          MEDIUM       6.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-1280
  │ ✘✔✘✘✘ CVE-2022-23825         MEDIUM       6.5   0.8%   ·  ↳ S:UBUNTU-CVE-2022-23825
  │ ✘✔✘✘✘ CVE-2022-29900         MEDIUM       6.5   3.9%   ·  ↳ S:UBUNTU-CVE-2022-29900
  │ ✘✔✘✘✘ CVE-2022-3344          MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-3344
  │ ✘✔✘✘✘ CVE-2022-3523          MEDIUM       5.3   1.1%   ·  ↳ S:UBUNTU-CVE-2022-3523
  │ ✘✔✘✘✘ CVE-2022-38457         MEDIUM       6.3   0.6%   ·  ↳ S:UBUNTU-CVE-2022-38457
  │ ✘✔✘✘✘ CVE-2022-40133         MEDIUM       6.3   0.6%   ·  ↳ S:UBUNTU-CVE-2022-40133
  │ ✘✔✘✘✘ CVE-2022-41848         MEDIUM       4.2   0.3%   ·  ↳ S:UBUNTU-CVE-2022-41848
  │ ✘✔✘✘✘ CVE-2022-44032         MEDIUM       6.4   0.4%   ·  ↳ S:UBUNTU-CVE-2022-44032
  │ ✘✔✘✘✘ CVE-2022-44033         MEDIUM       6.4   0.4%   ·  ↳ S:UBUNTU-CVE-2022-44033
  │ ✘✔✘✘✘ CVE-2022-44034         MEDIUM       6.4   0.3%   ·  ↳ S:UBUNTU-CVE-2022-44034
  │ ✘✔✘✘✘ CVE-2022-4543          MEDIUM       5.5   1.0%   ·  ↳ S:UBUNTU-CVE-2022-4543
  │ ✘✔✘✘✘ CVE-2022-48628         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48628
  │ ✘✔✘✘✘ CVE-2022-48642         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48642
  │ ✘✔✘✘✘ CVE-2022-48664         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48664
  │ ✘✔✘✘✘ CVE-2022-48755         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48755
  │ ✘✔✘✘✘ CVE-2022-48761         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48761
  │ ✘✔✘✘✘ CVE-2022-48763         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48763
  │ ✘✔✘✘✘ CVE-2022-48765         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48765
  │ ✘✔✘✘✘ CVE-2022-48769         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48769
  │ ✘✔✘✘✘ CVE-2022-48802         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-48802
  │ ✘✔✘✘✘ CVE-2022-48811         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-48811
  │ ✘✔✘✘✘ CVE-2022-48818         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-48818
  │ ✘✔✘✘✘ CVE-2022-48833         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48833
  │ ✘✔✘✘✘ CVE-2022-48865         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-48865
  │ ✘✔✘✘✘ CVE-2022-48875         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48875,USN-8098-1
  │ ✘✔✘✘✘ CVE-2022-48893         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-48893
  │ ✘✔✘✘✘ CVE-2022-48901         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48901
  │ ✘✔✘✘✘ CVE-2022-48909         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48909
  │ ✘✔✘✘✘ CVE-2022-48920         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48920
  │ ✘✔✘✘✘ CVE-2022-48952         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48952
  │ ✘✔✘✘✘ CVE-2022-48953         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48953
  │ ✘✔✘✘✘ CVE-2022-48961         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48961
  │ ✘✔✘✘✘ CVE-2022-48975         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-48975
  │ ✘✔✘✘✘ CVE-2022-49000         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49000
  │ ✘✔✘✘✘ CVE-2022-49027         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49027
  │ ✘✔✘✘✘ CVE-2022-49028         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49028
  │ ✘✔✘✘✘ CVE-2022-49046         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49046,USN-8200-1
  │ ✘✔✘✘✘ CVE-2022-49072         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49072,USN-8098-1
  │ ✘✔✘✘✘ CVE-2022-49097         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49097
  │ ✘✔✘✘✘ CVE-2022-49106         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49106
  │ ✘✔✘✘✘ CVE-2022-49107         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49107
  │ ✘✔✘✘✘ CVE-2022-49113         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49113
  │ ✘✔✘✘✘ CVE-2022-49118         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49118
  │ ✘✔✘✘✘ CVE-2022-49119         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49119
  │ ✘✔✘✘✘ CVE-2022-49120         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49120
  │ ✘✔✘✘✘ CVE-2022-49121         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49121
  │ ✘✔✘✘✘ CVE-2022-49124         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49124
  │ ✘✔✘✘✘ CVE-2022-49134         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49134
  │ ✘✔✘✘✘ CVE-2022-49135         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49135
  │ ✘✔✘✘✘ CVE-2022-49156         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49156
  │ ✘✔✘✘✘ CVE-2022-49157         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49157
  │ ✘✔✘✘✘ CVE-2022-49158         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49158
  │ ✘✔✘✘✘ CVE-2022-49161         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49161
  │ ✘✔✘✘✘ CVE-2022-49164         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49164
  │ ✘✔✘✘✘ CVE-2022-49169         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49169
  │ ✘✔✘✘✘ CVE-2022-49188         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49188
  │ ✘✔✘✘✘ CVE-2022-49190         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49190
  │ ✘✔✘✘✘ CVE-2022-49219         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49219
  │ ✘✔✘✘✘ CVE-2022-49226         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49226
  │ ✘✔✘✘✘ CVE-2022-49241         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49241
  │ ✘✔✘✘✘ CVE-2022-49246         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49246
  │ ✘✔✘✘✘ CVE-2022-49285         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49285
  │ ✘✔✘✘✘ CVE-2022-49311         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49311
  │ ✘✔✘✘✘ CVE-2022-49312         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49312
  │ ✘✔✘✘✘ CVE-2022-49317         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49317
  │ ✘✔✘✘✘ CVE-2022-49319         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49319
  │ ✘✔✘✘✘ CVE-2022-49323         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49323
  │ ✘✔✘✘✘ CVE-2022-49327         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49327
  │ ✘✔✘✘✘ CVE-2022-49342         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49342
  │ ✘✔✘✘✘ CVE-2022-49360         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49360
  │ ✘✔✘✘✘ CVE-2022-49361         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49361
  │ ✘✔✘✘✘ CVE-2022-49376         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49376
  │ ✘✔✘✘✘ CVE-2022-49398         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49398
  │ ✘✔✘✘✘ CVE-2022-49420         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49420
  │ ✘✔✘✘✘ CVE-2022-49428         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49428
  │ ✘✔✘✘✘ CVE-2022-49437         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49437
  │ ✘✔✘✘✘ CVE-2022-49440         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49440
  │ ✘✔✘✘✘ CVE-2022-49443         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49443
  │ ✘✔✘✘✘ CVE-2022-49445         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49445
  │ ✘✔✘✘✘ CVE-2022-49449         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49449
  │ ✘✔✘✘✘ CVE-2022-49468         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49468
  │ ✘✔✘✘✘ CVE-2022-49497         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49497
  │ ✘✔✘✘✘ CVE-2022-49502         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49502
  │ ✘✔✘✘✘ CVE-2022-49504         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49504
  │ ✘✔✘✘✘ CVE-2022-49512         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49512
  │ ✘✔✘✘✘ CVE-2022-49513         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49513
  │ ✘✔✘✘✘ CVE-2022-49521         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49521
  │ ✘✔✘✘✘ CVE-2022-49534         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49534
  │ ✘✔✘✘✘ CVE-2022-49536         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49536
  │ ✘✔✘✘✘ CVE-2022-49546         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49546
  │ ✘✔✘✘✘ CVE-2022-49566         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49566
  │ ✘✔✘✘✘ CVE-2022-49578         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49578
  │ ✘✔✘✘✘ CVE-2022-49579         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49579
  │ ✘✔✘✘✘ CVE-2022-49585         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49585
  │ ✘✔✘✘✘ CVE-2022-49599         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49599
  │ ✘✔✘✘✘ CVE-2022-49603         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49603
  │ ✘✔✘✘✘ CVE-2022-49610         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49610
  │ ✘✔✘✘✘ CVE-2022-49630         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49630
  │ ✘✔✘✘✘ CVE-2022-49632         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49632
  │ ✘✔✘✘✘ CVE-2022-49636         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49636,USN-7585-1
  │ ✘✔✘✘✘ CVE-2022-49640         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49640
  │ ✘✔✘✘✘ CVE-2022-49641         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49641
  │ ✘✔✘✘✘ CVE-2022-49650         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49650
  │ ✘✔✘✘✘ CVE-2022-49658         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49658
  │ ✘✔✘✘✘ CVE-2022-49666         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49666
  │ ✘✔✘✘✘ CVE-2022-49723         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49723
  │ ✘✔✘✘✘ CVE-2022-49728         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49728
  │ ✘✔✘✘✘ CVE-2022-49749         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49749
  │ ✘✔✘✘✘ CVE-2022-49758         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49758
  │ ✘✔✘✘✘ CVE-2022-49764         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49764
  │ ✘✔✘✘✘ CVE-2022-49765         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49765
  │ ✘✔✘✘✘ CVE-2022-49766         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49766
  │ ✘✔✘✘✘ CVE-2022-49812         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49812
  │ ✘✔✘✘✘ CVE-2022-49813         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49813
  │ ✘✔✘✘✘ CVE-2022-49822         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49822
  │ ✘✔✘✘✘ CVE-2022-49823         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49823
  │ ✘✔✘✘✘ CVE-2022-49824         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49824
  │ ✘✔✘✘✘ CVE-2022-49825         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49825
  │ ✘✔✘✘✘ CVE-2022-49828         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49828
  │ ✘✔✘✘✘ CVE-2022-49829         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49829
  │ ✘✔✘✘✘ CVE-2022-49837         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49837
  │ ✘✔✘✘✘ CVE-2022-49838         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49838
  │ ✘✔✘✘✘ CVE-2022-49839         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49839
  │ ✘✔✘✘✘ CVE-2022-49873         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49873
  │ ✘✔✘✘✘ CVE-2022-49885         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49885
  │ ✘✔✘✘✘ CVE-2022-49901         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49901
  │ ✘✔✘✘✘ CVE-2022-49923         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49923
  │ ✘✔✘✘✘ CVE-2022-49924         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49924
  │ ✘✔✘✘✘ CVE-2022-49932         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49932
  │ ✘✔✘✘✘ CVE-2022-49938         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49938
  │ ✘✔✘✘✘ CVE-2022-49940         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49940
  │ ✘✔✘✘✘ CVE-2022-49966         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-49966
  │ ✘✔✘✘✘ CVE-2022-49967         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2022-49967
  │ ✘✔✘✘✘ CVE-2022-49989         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-49989
  │ ✘✔✘✘✘ CVE-2022-50011         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50011
  │ ✘✔✘✘✘ CVE-2022-50023         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50023
  │ ✘✔✘✘✘ CVE-2022-50024         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50024
  │ ✘✔✘✘✘ CVE-2022-50027         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50027
  │ ✘✔✘✘✘ CVE-2022-50036         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50036
  │ ✘✔✘✘✘ CVE-2022-50044         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2022-50044
  │ ✘✔✘✘✘ CVE-2022-50053         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2022-50053
  │ ✘✔✘✘✘ CVE-2022-50060         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50060
  │ ✘✔✘✘✘ CVE-2022-50065         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50065
  │ ✘✔✘✘✘ CVE-2022-50068         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50068
  │ ✘✔✘✘✘ CVE-2022-50073         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50073
  │ ✘✔✘✘✘ CVE-2022-50086         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50086
  │ ✘✔✘✘✘ CVE-2022-50114         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50114
  │ ✘✔✘✘✘ CVE-2022-50116         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2022-50116
  │ ✘✔✘✘✘ CVE-2022-50120         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50120
  │ ✘✔✘✘✘ CVE-2022-50132         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50132
  │ ✘✔✘✘✘ CVE-2022-50138         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-50138
  │ ✘✔✘✘✘ CVE-2022-50144         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50144
  │ ✘✔✘✘✘ CVE-2022-50146         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50146
  │ ✘✔✘✘✘ CVE-2022-50159         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50159
  │ ✘✔✘✘✘ CVE-2022-50166         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50166
  │ ✘✔✘✘✘ CVE-2022-50172         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50172
  │ ✘✔✘✘✘ CVE-2022-50174         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50174
  │ ✘✔✘✘✘ CVE-2022-50175         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50175
  │ ✘✔✘✘✘ CVE-2022-50181         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-50181
  │ ✘✔✘✘✘ CVE-2022-50201         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50201
  │ ✘✔✘✘✘ CVE-2022-50204         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2022-50204
  │ ✘✔✘✘✘ CVE-2022-50224         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50224
  │ ✘✔✘✘✘ CVE-2022-50226         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50226
  │ ✘✔✘✘✘ CVE-2022-50236         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50236
  │ ✘✔✘✘✘ CVE-2022-50260         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50260
  │ ✘✔✘✘✘ CVE-2022-50262         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50262
  │ ✘✔✘✘✘ CVE-2022-50266         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50266
  │ ✘✔✘✘✘ CVE-2022-50267         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50267
  │ ✘✔✘✘✘ CVE-2022-50293         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50293
  │ ✘✔✘✘✘ CVE-2022-50304         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50304
  │ ✘✔✘✘✘ CVE-2022-50316         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50316
  │ ✘✔✘✘✘ CVE-2022-50327         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50327
  │ ✘✔✘✘✘ CVE-2022-50336         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50336
  │ ✘✔✘✘✘ CVE-2022-50340         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50340
  │ ✘✔✘✘✘ CVE-2022-50356         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50356
  │ ✘✔✘✘✘ CVE-2022-50364         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50364
  │ ✘✔✘✘✘ CVE-2022-50369         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50369
  │ ✘✔✘✘✘ CVE-2022-50374         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50374
  │ ✘✔✘✘✘ CVE-2022-50380         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50380
  │ ✘✔✘✘✘ CVE-2022-50385         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50385
  │ ✘✔✘✘✘ CVE-2022-50388         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50388
  │ ✘✔✘✘✘ CVE-2022-50392         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50392
  │ ✘✔✘✘✘ CVE-2022-50400         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2022-50400
  │ ✘✔✘✘✘ CVE-2022-50420         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50420
  │ ✘✔✘✘✘ CVE-2022-50443         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50443
  │ ✘✔✘✘✘ CVE-2022-50445         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50445
  │ ✘✔✘✘✘ CVE-2022-50451         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50451
  │ ✘✔✘✘✘ CVE-2022-50453         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50453
  │ ✘✔✘✘✘ CVE-2022-50469         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50469
  │ ✘✔✘✘✘ CVE-2022-50471         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50471
  │ ✘✔✘✘✘ CVE-2022-50500         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2022-50500
  │ ✘✔✘✘✘ CVE-2022-50512         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50512
  │ ✘✔✘✘✘ CVE-2022-50516         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50516
  │ ✘✔✘✘✘ CVE-2022-50539         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50539
  │ ✘✔✘✘✘ CVE-2022-50541         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50541
  │ ✘✔✘✘✘ CVE-2022-50550         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50550
  │ ✘✔✘✘✘ CVE-2022-50554         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50554
  │ ✘✔✘✘✘ CVE-2023-0160          MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2023-0160
  │ ✘✔✘✘✘ CVE-2023-1582          MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2023-1582
  │ ✘✔✘✘✘ CVE-2023-20569         MEDIUM       4.7   7.3%   ·  ↳ S:UBUNTU-CVE-2023-20569
  │ ✘✔✘✘✘ CVE-2023-31082         MEDIUM       5.5   0.4%   ·  ↳ S:UBUNTU-CVE-2023-31082
  │ ✘✔✘✘✘ CVE-2023-32246         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-32246
  │ ✘✔✘✘✘ CVE-2023-32253         MEDIUM       5.9   0.3%   ·  ↳ S:UBUNTU-CVE-2023-32253
  │ ✘✔✘✘✘ CVE-2023-32255         MEDIUM       5.3   0.5%   ·  ↳ S:UBUNTU-CVE-2023-32255
  │ ✘✔✘✘✘ CVE-2023-33288         MEDIUM       4.7   0.3%   ·  ↳ S:UBUNTU-CVE-2023-33288
  │ ✘✔✘✘✘ CVE-2023-4133          MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-4133
  │ ✘✔✘✘✘ CVE-2023-4134          MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-4134
  │ ✘✔✘✘✘ CVE-2023-52481         MEDIUM       4.7   0.6%   ·  ↳ S:UBUNTU-CVE-2023-52481
  │ ✘✔✘✘✘ CVE-2023-52489         MEDIUM       4.7   0.3%   ·  ↳ S:UBUNTU-CVE-2023-52489
  │ ✘✔✘✘✘ CVE-2023-52500         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52500
  │ ✘✔✘✘✘ CVE-2023-52516         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52516
  │ ✘✔✘✘✘ CVE-2023-52561         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52561
  │ ✘✔✘✘✘ CVE-2023-52635         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52635
  │ ✘✔✘✘✘ CVE-2023-52652         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2023-52652
  │ ✘✔✘✘✘ CVE-2023-52653         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2023-52653
  │ ✘✔✘✘✘ CVE-2023-52671         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52671
  │ ✘✔✘✘✘ CVE-2023-52674         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52674
  │ ✘✔✘✘✘ CVE-2023-52680         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52680
  │ ✘✔✘✘✘ CVE-2023-52700         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52700
  │ ✘✔✘✘✘ CVE-2023-52736         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52736
  │ ✘✔✘✘✘ CVE-2023-52749         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52749
  │ ✘✔✘✘✘ CVE-2023-52750         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52750
  │ ✘✔✘✘✘ CVE-2023-52754         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52754
  │ ✘✔✘✘✘ CVE-2023-52762         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52762
  │ ✘✔✘✘✘ CVE-2023-52763         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52763
  │ ✘✔✘✘✘ CVE-2023-52781         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52781
  │ ✘✔✘✘✘ CVE-2023-52808         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52808
  │ ✘✔✘✘✘ CVE-2023-52811         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52811
  │ ✘✔✘✘✘ CVE-2023-52826         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52826
  │ ✘✔✘✘✘ CVE-2023-52828         MEDIUM       6.6   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52828
  │ ✘✔✘✘✘ CVE-2023-52833         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52833
  │ ✘✔✘✘✘ CVE-2023-52878         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52878
  │ ✘✔✘✘✘ CVE-2023-52888         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52888
  │ ✘✔✘✘✘ CVE-2023-52925         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52925
  │ ✘✔✘✘✘ CVE-2023-52939         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-52939
  │ ✘✔✘✘✘ CVE-2023-53008         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53008
  │ ✘✔✘✘✘ CVE-2023-53010         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53010
  │ ✘✔✘✘✘ CVE-2023-53020         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53020
  │ ✘✔✘✘✘ CVE-2023-53042         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53042
  │ ✘✔✘✘✘ CVE-2023-53054         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53054
  │ ✘✔✘✘✘ CVE-2023-53068         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53068
  │ ✘✔✘✘✘ CVE-2023-53079         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53079
  │ ✘✔✘✘✘ CVE-2023-53091         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53091
  │ ✘✔✘✘✘ CVE-2023-53093         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53093
  │ ✘✔✘✘✘ CVE-2023-53103         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53103
  │ ✘✔✘✘✘ CVE-2023-53105         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53105
  │ ✘✔✘✘✘ CVE-2023-53131         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53131
  │ ✘✔✘✘✘ CVE-2023-53133         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53133
  │ ✘✔✘✘✘ CVE-2023-53149         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53149
  │ ✘✔✘✘✘ CVE-2023-53152         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53152
  │ ✘✔✘✘✘ CVE-2023-53171         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53171
  │ ✘✔✘✘✘ CVE-2023-53173         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53173
  │ ✘✔✘✘✘ CVE-2023-53188         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53188
  │ ✘✔✘✘✘ CVE-2023-53197         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53197
  │ ✘✔✘✘✘ CVE-2023-53200         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53200
  │ ✘✔✘✘✘ CVE-2023-53201         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53201
  │ ✘✔✘✘✘ CVE-2023-53202         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53202
  │ ✘✔✘✘✘ CVE-2023-53225         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53225
  │ ✘✔✘✘✘ CVE-2023-53230         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53230
  │ ✘✔✘✘✘ CVE-2023-53231         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53231
  │ ✘✔✘✘✘ CVE-2023-53241         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53241
  │ ✘✔✘✘✘ CVE-2023-53244         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53244
  │ ✘✔✘✘✘ CVE-2023-53248         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53248
  │ ✘✔✘✘✘ CVE-2023-53249         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53249
  │ ✘✔✘✘✘ CVE-2023-53250         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53250
  │ ✘✔✘✘✘ CVE-2023-53261         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53261
  │ ✘✔✘✘✘ CVE-2023-53270         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53270
  │ ✘✔✘✘✘ CVE-2023-53279         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53279
  │ ✘✔✘✘✘ CVE-2023-53287         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53287
  │ ✘✔✘✘✘ CVE-2023-53326         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53326
  │ ✘✔✘✘✘ CVE-2023-53328         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53328
  │ ✘✔✘✘✘ CVE-2023-53332         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53332
  │ ✘✔✘✘✘ CVE-2023-53334         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53334
  │ ✘✔✘✘✘ CVE-2023-53347         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53347
  │ ✘✔✘✘✘ CVE-2023-53348         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53348
  │ ✘✔✘✘✘ CVE-2023-53353         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53353
  │ ✘✔✘✘✘ CVE-2023-53355         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53355
  │ ✘✔✘✘✘ CVE-2023-53359         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53359
  │ ✘✔✘✘✘ CVE-2023-53367         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53367
  │ ✘✔✘✘✘ CVE-2023-53370         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53370
  │ ✘✔✘✘✘ CVE-2023-53383         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53383
  │ ✘✔✘✘✘ CVE-2023-53390         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53390
  │ ✘✔✘✘✘ CVE-2023-53391         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53391
  │ ✘✔✘✘✘ CVE-2023-53393         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53393
  │ ✘✔✘✘✘ CVE-2023-53402         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53402
  │ ✘✔✘✘✘ CVE-2023-53403         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53403
  │ ✘✔✘✘✘ CVE-2023-53404         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53404
  │ ✘✔✘✘✘ CVE-2023-53405         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53405
  │ ✘✔✘✘✘ CVE-2023-53406         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53406
  │ ✘✔✘✘✘ CVE-2023-53407         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53407
  │ ✘✔✘✘✘ CVE-2023-53408         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53408
  │ ✘✔✘✘✘ CVE-2023-53409         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53409
  │ ✘✔✘✘✘ CVE-2023-53411         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53411
  │ ✘✔✘✘✘ CVE-2023-53412         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53412
  │ ✘✔✘✘✘ CVE-2023-53413         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53413
  │ ✘✔✘✘✘ CVE-2023-53414         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53414
  │ ✘✔✘✘✘ CVE-2023-53415         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53415
  │ ✘✔✘✘✘ CVE-2023-53416         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53416
  │ ✘✔✘✘✘ CVE-2023-53417         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53417
  │ ✘✔✘✘✘ CVE-2023-53418         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53418
  │ ✘✔✘✘✘ CVE-2023-53419         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53419
  │ ✘✔✘✘✘ CVE-2023-53438         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53438
  │ ✘✔✘✘✘ CVE-2023-53441         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53441
  │ ✘✔✘✘✘ CVE-2023-53447         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53447
  │ ✘✔✘✘✘ CVE-2023-53458         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53458
  │ ✘✔✘✘✘ CVE-2023-53460         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53460
  │ ✘✔✘✘✘ CVE-2023-53461         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53461
  │ ✘✔✘✘✘ CVE-2023-53470         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53470
  │ ✘✔✘✘✘ CVE-2023-53476         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53476
  │ ✘✔✘✘✘ CVE-2023-53482         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53482
  │ ✘✔✘✘✘ CVE-2023-53503         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53503
  │ ✘✔✘✘✘ CVE-2023-53509         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53509
  │ ✘✔✘✘✘ CVE-2023-53512         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53512
  │ ✘✔✘✘✘ CVE-2023-53513         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53513
  │ ✘✔✘✘✘ CVE-2023-53529         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53529
  │ ✘✔✘✘✘ CVE-2023-53530         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53530
  │ ✘✔✘✘✘ CVE-2023-53538         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53538
  │ ✘✔✘✘✘ CVE-2023-53562         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53562
  │ ✘✔✘✘✘ CVE-2023-53574         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53574
  │ ✘✔✘✘✘ CVE-2023-53576         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53576
  │ ✘✔✘✘✘ CVE-2023-53579         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53579
  │ ✘✔✘✘✘ CVE-2023-53581         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53581
  │ ✘✔✘✘✘ CVE-2023-53584         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53584
  │ ✘✔✘✘✘ CVE-2023-53588         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53588
  │ ✘✔✘✘✘ CVE-2023-53594         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53594
  │ ✘✔✘✘✘ CVE-2023-53603         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53603
  │ ✘✔✘✘✘ CVE-2023-53605         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53605
  │ ✘✔✘✘✘ CVE-2023-53607         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53607
  │ ✘✔✘✘✘ CVE-2023-53618         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53618
  │ ✘✔✘✘✘ CVE-2023-53620         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53620
  │ ✘✔✘✘✘ CVE-2023-53624         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53624
  │ ✘✔✘✘✘ CVE-2023-53625         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53625
  │ ✘✔✘✘✘ CVE-2023-53647         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53647
  │ ✘✔✘✘✘ CVE-2023-53661         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53661
  │ ✘✔✘✘✘ CVE-2023-53682         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53682
  │ ✘✔✘✘✘ CVE-2023-53684         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53684
  │ ✘✔✘✘✘ CVE-2023-53685         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2023-53685
  │ ✘✔✘✘✘ CVE-2023-54321         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54321
  │ ✘✔✘✘✘ CVE-2023-6240          MEDIUM       6.5   1.0%   ·  ↳ S:UBUNTU-CVE-2023-6240
  │ ✘✔✘✘✘ CVE-2024-0564          MEDIUM       6.5   0.6%   ·  ↳ S:UBUNTU-CVE-2024-0564
  │ ✘✔✘✘✘ CVE-2024-1151          MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-1151
  │ ✘✔✘✘✘ CVE-2024-2193          MEDIUM       5.7   1.3%   ·  ↳ S:UBUNTU-CVE-2024-2193
  │ ✘✔✘✘✘ CVE-2024-24864         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2024-24864
  │ ✘✔✘✘✘ CVE-2024-25740         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-25740
  │ ✘✔✘✘✘ CVE-2024-26595         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26595
  │ ✘✔✘✘✘ CVE-2024-26629         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26629
  │ ✘✔✘✘✘ CVE-2024-26644         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26644
  │ ✘✔✘✘✘ CVE-2024-26686         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26686
  │ ✘✔✘✘✘ CVE-2024-26691         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26691
  │ ✘✔✘✘✘ CVE-2024-26700         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26700
  │ ✘✔✘✘✘ CVE-2024-26715         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-26715
  │ ✘✔✘✘✘ CVE-2024-26726         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-26726
  │ ✘✔✘✘✘ CVE-2024-26740         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26740
  │ ✘✔✘✘✘ CVE-2024-26743         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26743
  │ ✘✔✘✘✘ CVE-2024-26744         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-26744
  │ ✘✔✘✘✘ CVE-2024-26747         MEDIUM       4.4   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26747
  │ ✘✔✘✘✘ CVE-2024-26756         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26756
  │ ✘✔✘✘✘ CVE-2024-26757         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26757
  │ ✘✔✘✘✘ CVE-2024-26758         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26758
  │ ✘✔✘✘✘ CVE-2024-26771         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26771
  │ ✘✔✘✘✘ CVE-2024-26776         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26776
  │ ✘✔✘✘✘ CVE-2024-26844         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26844
  │ ✘✔✘✘✘ CVE-2024-26846         MEDIUM       4.4   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26846
  │ ✘✔✘✘✘ CVE-2024-26866         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26866
  │ ✘✔✘✘✘ CVE-2024-26876         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26876
  │ ✘✔✘✘✘ CVE-2024-26900         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-26900
  │ ✘✔✘✘✘ CVE-2024-26948         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-26948
  │ ✘✔✘✘✘ CVE-2024-27002         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-27002
  │ ✘✔✘✘✘ CVE-2024-27010         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-27010
  │ ✘✔✘✘✘ CVE-2024-27011         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-27011
  │ ✘✔✘✘✘ CVE-2024-27014         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-27014
  │ ✘✔✘✘✘ CVE-2024-27025         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-27025
  │ ✘✔✘✘✘ CVE-2024-27032         MEDIUM       6.3   0.3%   ·  ↳ S:UBUNTU-CVE-2024-27032
  │ ✘✔✘✘✘ CVE-2024-27037         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-27037
  │ ✘✔✘✘✘ CVE-2024-27054         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-27054
  │ ✘✔✘✘✘ CVE-2024-27072         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-27072
  │ ✘✔✘✘✘ CVE-2024-27402         MEDIUM       5.8   0.2%   ·  ↳ S:UBUNTU-CVE-2024-27402
  │ ✘✔✘✘✘ CVE-2024-28956         MEDIUM       5.7   0.4%   ·  ↳ S:UBUNTU-CVE-2024-28956
  │ ✘✔✘✘✘ CVE-2024-35247         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35247
  │ ✘✔✘✘✘ CVE-2024-35784         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35784
  │ ✘✔✘✘✘ CVE-2024-35790         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35790
  │ ✘✔✘✘✘ CVE-2024-35794         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35794
  │ ✘✔✘✘✘ CVE-2024-35799         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35799
  │ ✘✔✘✘✘ CVE-2024-35803         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35803
  │ ✘✔✘✘✘ CVE-2024-35826         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35826
  │ ✘✔✘✘✘ CVE-2024-35837         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35837
  │ ✘✔✘✘✘ CVE-2024-35945         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35945
  │ ✘✔✘✘✘ CVE-2024-35995         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-35995
  │ ✘✔✘✘✘ CVE-2024-36024         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2024-36024
  │ ✘✔✘✘✘ CVE-2024-36029         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-36029
  │ ✘✔✘✘✘ CVE-2024-36244         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-36244
  │ ✘✔✘✘✘ CVE-2024-36347         MEDIUM       6.4   0.1%   ·  ↳ S:UBUNTU-CVE-2024-36347
  │ ✘✔✘✘✘ CVE-2024-36350         MEDIUM       5.6   0.5%   ·  ↳ S:UBUNTU-CVE-2024-36350
  │ ✘✔✘✘✘ CVE-2024-36357         MEDIUM       5.6   0.4%   ·  ↳ S:UBUNTU-CVE-2024-36357
  │ ✘✔✘✘✘ CVE-2024-36479         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-36479
  │ ✘✔✘✘✘ CVE-2024-36903         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-36903
  │ ✘✔✘✘✘ CVE-2024-36917         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-36917
  │ ✘✔✘✘✘ CVE-2024-36924         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-36924
  │ ✘✔✘✘✘ CVE-2024-36927         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2024-36927
  │ ✘✔✘✘✘ CVE-2024-36949         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2024-36949
  │ ✘✔✘✘✘ CVE-2024-36951         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-36951
  │ ✘✔✘✘✘ CVE-2024-36969         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-36969
  │ ✘✔✘✘✘ CVE-2024-37021         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-37021
  │ ✘✔✘✘✘ CVE-2024-38546         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-38546
  │ ✘✔✘✘✘ CVE-2024-38547         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-38547
  │ ✘✔✘✘✘ CVE-2024-38554         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-38554
  │ ✘✔✘✘✘ CVE-2024-38591         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-38591
  │ ✘✔✘✘✘ CVE-2024-38608         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-38608
  │ ✘✔✘✘✘ CVE-2024-38632         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-38632
  │ ✘✔✘✘✘ CVE-2024-38662         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2024-38662
  │ ✘✔✘✘✘ CVE-2024-39490         MEDIUM       6.2   0.2%   ·  ↳ S:UBUNTU-CVE-2024-39490
  │ ✘✔✘✘✘ CVE-2024-39497         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-39497
  │ ✘✔✘✘✘ CVE-2024-40966         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-40966
  │ ✘✔✘✘✘ CVE-2024-40972         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-40972
  │ ✘✔✘✘✘ CVE-2024-40976         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-40976
  │ ✘✔✘✘✘ CVE-2024-40977         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-40977
  │ ✘✔✘✘✘ CVE-2024-40998         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-40998
  │ ✘✔✘✘✘ CVE-2024-41001         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-41001
  │ ✘✔✘✘✘ CVE-2024-41005         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2024-41005
  │ ✘✔✘✘✘ CVE-2024-41023         MEDIUM       5.5   0.4%   ·  ↳ S:UBUNTU-CVE-2024-41023
  │ ✘✔✘✘✘ CVE-2024-41077         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-41077
  │ ✘✔✘✘✘ CVE-2024-41078         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-41078
  │ ✘✔✘✘✘ CVE-2024-41082         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-41082
  │ ✘✔✘✘✘ CVE-2024-42080         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-42080
  │ ✘✔✘✘✘ CVE-2024-42082         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-42082
  │ ✘✔✘✘✘ CVE-2024-42098         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-42098
  │ ✘✔✘✘✘ CVE-2024-42114         MEDIUM       4.4   0.2%   ·  ↳ S:UBUNTU-CVE-2024-42114
  │ ✘✔✘✘✘ CVE-2024-42128         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-42128
  │ ✘✔✘✘✘ CVE-2024-42129         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-42129
  │ ✘✔✘✘✘ CVE-2024-42267         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-42267
  │ ✘✔✘✘✘ CVE-2024-42312         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-42312
  │ ✘✔✘✘✘ CVE-2024-42319         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-42319
  │ ✘✔✘✘✘ CVE-2024-42321         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-42321
  │ ✘✔✘✘✘ CVE-2024-42322         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-42322
  │ ✘✔✘✘✘ CVE-2024-43817         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-43817
  │ ✘✔✘✘✘ CVE-2024-43831         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-43831
  │ ✘✔✘✘✘ CVE-2024-43834         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-43834
  │ ✘✔✘✘✘ CVE-2024-43866         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2024-43866
  │ ✘✔✘✘✘ CVE-2024-43899         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-43899
  │ ✘✔✘✘✘ CVE-2024-43902         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-43902
  │ ✘✔✘✘✘ CVE-2024-43905         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-43905
  │ ✘✔✘✘✘ CVE-2024-43907         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-43907
  │ ✘✔✘✘✘ CVE-2024-43912         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-43912
  │ ✘✔✘✘✘ CVE-2024-44958         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-44958
  │ ✘✔✘✘✘ CVE-2024-44963         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-44963
  │ ✘✔✘✘✘ CVE-2024-44982         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-44982
  │ ✘✔✘✘✘ CVE-2024-45015         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-45015
  │ ✘✔✘✘✘ CVE-2024-45828         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-45828
  │ ✘✔✘✘✘ CVE-2024-46681         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-46681
  │ ✘✔✘✘✘ CVE-2024-46702         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46702
  │ ✘✔✘✘✘ CVE-2024-46707         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46707
  │ ✘✔✘✘✘ CVE-2024-46715         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46715
  │ ✘✔✘✘✘ CVE-2024-46720         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46720
  │ ✘✔✘✘✘ CVE-2024-46726         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46726
  │ ✘✔✘✘✘ CVE-2024-46727         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46727
  │ ✘✔✘✘✘ CVE-2024-46728         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46728
  │ ✘✔✘✘✘ CVE-2024-46732         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46732
  │ ✘✔✘✘✘ CVE-2024-46752         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46752
  │ ✘✔✘✘✘ CVE-2024-46753         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-46753
  │ ✘✔✘✘✘ CVE-2024-46770         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46770
  │ ✘✔✘✘✘ CVE-2024-46775         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46775
  │ ✘✔✘✘✘ CVE-2024-46802         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46802
  │ ✘✔✘✘✘ CVE-2024-46806         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46806
  │ ✘✔✘✘✘ CVE-2024-46807         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46807
  │ ✘✔✘✘✘ CVE-2024-46808         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-46808
  │ ✘✔✘✘✘ CVE-2024-46809         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46809
  │ ✘✔✘✘✘ CVE-2024-46810         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46810
  │ ✘✔✘✘✘ CVE-2024-46819         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46819
  │ ✘✔✘✘✘ CVE-2024-46832         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46832
  │ ✘✔✘✘✘ CVE-2024-46841         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46841
  │ ✘✔✘✘✘ CVE-2024-46848         MEDIUM       5.5   1.1%   ·  ↳ S:UBUNTU-CVE-2024-46848
  │ ✘✔✘✘✘ CVE-2024-46857         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46857
  │ ✘✔✘✘✘ CVE-2024-46860         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-46860
  │ ✘✔✘✘✘ CVE-2024-46870         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2024-46870
  │ ✘✔✘✘✘ CVE-2024-47141         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-47141
  │ ✘✔✘✘✘ CVE-2024-47143         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-47143
  │ ✘✔✘✘✘ CVE-2024-47660         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2024-47660
  │ ✘✔✘✘✘ CVE-2024-47661         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-47661
  │ ✘✔✘✘✘ CVE-2024-47665         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-47665
  │ ✘✔✘✘✘ CVE-2024-47666         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-47666
  │ ✘✔✘✘✘ CVE-2024-47673         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-47673
  │ ✘✔✘✘✘ CVE-2024-47683         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-47683
  │ ✘✔✘✘✘ CVE-2024-47693         MEDIUM       6.5   1.0%   ·  ↳ S:UBUNTU-CVE-2024-47693
  │ ✘✔✘✘✘ CVE-2024-47704         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-47704
  │ ✘✔✘✘✘ CVE-2024-47728         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-47728
  │ ✘✔✘✘✘ CVE-2024-47735         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-47735
  │ ✘✔✘✘✘ CVE-2024-47809         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-47809
  │ ✘✔✘✘✘ CVE-2024-49858         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49858
  │ ✘✔✘✘✘ CVE-2024-49863         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-49863
  │ ✘✔✘✘✘ CVE-2024-49881         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49881
  │ ✘✔✘✘✘ CVE-2024-49890         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49890
  │ ✘✔✘✘✘ CVE-2024-49891         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49891
  │ ✘✔✘✘✘ CVE-2024-49893         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49893
  │ ✘✔✘✘✘ CVE-2024-49898         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49898
  │ ✘✔✘✘✘ CVE-2024-49899         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-49899
  │ ✘✔✘✘✘ CVE-2024-49901         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49901
  │ ✘✔✘✘✘ CVE-2024-49905         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49905
  │ ✘✔✘✘✘ CVE-2024-49906         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49906
  │ ✘✔✘✘✘ CVE-2024-49907         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49907
  │ ✘✔✘✘✘ CVE-2024-49908         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49908
  │ ✘✔✘✘✘ CVE-2024-49910         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49910
  │ ✘✔✘✘✘ CVE-2024-49911         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49911
  │ ✘✔✘✘✘ CVE-2024-49912         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49912
  │ ✘✔✘✘✘ CVE-2024-49913         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49913
  │ ✘✔✘✘✘ CVE-2024-49914         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49914
  │ ✘✔✘✘✘ CVE-2024-49915         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49915
  │ ✘✔✘✘✘ CVE-2024-49916         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49916
  │ ✘✔✘✘✘ CVE-2024-49917         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49917
  │ ✘✔✘✘✘ CVE-2024-49918         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-49918
  │ ✘✔✘✘✘ CVE-2024-49919         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49919
  │ ✘✔✘✘✘ CVE-2024-49920         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-49920
  │ ✘✔✘✘✘ CVE-2024-49921         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-49921
  │ ✘✔✘✘✘ CVE-2024-49922         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49922
  │ ✘✔✘✘✘ CVE-2024-49923         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49923
  │ ✘✔✘✘✘ CVE-2024-49927         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49927,USN-8098-1
  │ ✘✔✘✘✘ CVE-2024-49929         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49929
  │ ✘✔✘✘✘ CVE-2024-49935         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-49935,USN-7922-1
  │ ✘✔✘✘✘ CVE-2024-49945         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-49945
  │ ✘✔✘✘✘ CVE-2024-49970         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-49970
  │ ✘✔✘✘✘ CVE-2024-50015         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50015
  │ ✘✔✘✘✘ CVE-2024-50017         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50017
  │ ✘✔✘✘✘ CVE-2024-50038         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50038
  │ ✘✔✘✘✘ CVE-2024-50058         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50058
  │ ✘✔✘✘✘ CVE-2024-50135         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50135
  │ ✘✔✘✘✘ CVE-2024-50166         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50166
  │ ✘✔✘✘✘ CVE-2024-50196         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50196,USN-7922-1
  │ ✘✔✘✘✘ CVE-2024-50258         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50258
  │ ✘✔✘✘✘ CVE-2024-50272         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-50272
  │ ✘✔✘✘✘ CVE-2024-50289         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50289
  │ ✘✔✘✘✘ CVE-2024-50298         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50298
  │ ✘✔✘✘✘ CVE-2024-50304         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50304,USN-8273-1
  │ ✘✔✘✘✘ CVE-2024-53051         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-53051,USN-7671-1
  │ ✘✔✘✘✘ CVE-2024-53052         MEDIUM       4.4   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53052
  │ ✘✔✘✘✘ CVE-2024-53128         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53128
  │ ✘✔✘✘✘ CVE-2024-53187         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-53187,USN-8919-1
  │ ✘✔✘✘✘ CVE-2024-53190         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53190
  │ ✘✔✘✘✘ CVE-2024-53195         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53195
  │ ✘✔✘✘✘ CVE-2024-53210         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53210,USN-8919-1
  │ ✘✔✘✘✘ CVE-2024-53219         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-53219
  │ ✘✔✘✘✘ CVE-2024-53234         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53234
  │ ✘✔✘✘✘ CVE-2024-53241         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-53241
  │ ✘✔✘✘✘ CVE-2024-53685         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-53685
  │ ✘✔✘✘✘ CVE-2024-54683         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-54683
  │ ✘✔✘✘✘ CVE-2024-56369         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-56369
  │ ✘✔✘✘✘ CVE-2024-56533         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56533
  │ ✘✔✘✘✘ CVE-2024-56544         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-56544
  │ ✘✔✘✘✘ CVE-2024-56565         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56565
  │ ✘✔✘✘✘ CVE-2024-56566         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56566
  │ ✘✔✘✘✘ CVE-2024-56568         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56568
  │ ✘✔✘✘✘ CVE-2024-56583         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56583
  │ ✘✔✘✘✘ CVE-2024-56584         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56584
  │ ✘✔✘✘✘ CVE-2024-56588         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56588
  │ ✘✔✘✘✘ CVE-2024-56589         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56589
  │ ✘✔✘✘✘ CVE-2024-56592         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56592
  │ ✘✔✘✘✘ CVE-2024-56611         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56611
  │ ✘✔✘✘✘ CVE-2024-56636         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-56636
  │ ✘✔✘✘✘ CVE-2024-56647         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56647
  │ ✘✔✘✘✘ CVE-2024-56698         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56698
  │ ✘✔✘✘✘ CVE-2024-56701         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56701
  │ ✘✔✘✘✘ CVE-2024-56705         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-56705
  │ ✘✔✘✘✘ CVE-2024-56712         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56712
  │ ✘✔✘✘✘ CVE-2024-56722         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56722
  │ ✘✔✘✘✘ CVE-2024-56751         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56751
  │ ✘✔✘✘✘ CVE-2024-56763         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56763,USN-8919-1
  │ ✘✔✘✘✘ CVE-2024-56776         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56776
  │ ✘✔✘✘✘ CVE-2024-56777         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56777
  │ ✘✔✘✘✘ CVE-2024-56778         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56778
  │ ✘✔✘✘✘ CVE-2024-56787         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-56787
  │ ✘✔✘✘✘ CVE-2024-57809         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-57809
  │ ✘✔✘✘✘ CVE-2024-57872         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-57872
  │ ✘✔✘✘✘ CVE-2024-57888         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-57888
  │ ✘✔✘✘✘ CVE-2024-57897         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-57897
  │ ✘✔✘✘✘ CVE-2024-57903         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-57903
  │ ✘✔✘✘✘ CVE-2024-57924         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-57924
  │ ✘✔✘✘✘ CVE-2024-57939         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-57939
  │ ✘✔✘✘✘ CVE-2024-57974         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2024-57974
  │ ✘✔✘✘✘ CVE-2024-58005         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2024-58005
  │ ✘✔✘✘✘ CVE-2024-58016         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-58016
  │ ✘✔✘✘✘ CVE-2024-58095         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2024-58095
  │ ✘✔✘✘✘ CVE-2025-12801         MEDIUM       6.5   0.5%   ·  ↳ S:UBUNTU-CVE-2025-12801
  │ ✘✔✘✘✘ CVE-2025-21634         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-21634
  │ ✘✔✘✘✘ CVE-2025-21635         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-21635
  │ ✘✔✘✘✘ CVE-2025-21648         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21648
  │ ✘✔✘✘✘ CVE-2025-21651         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21651
  │ ✘✔✘✘✘ CVE-2025-21690         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21690
  │ ✘✔✘✘✘ CVE-2025-21711         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21711
  │ ✘✔✘✘✘ CVE-2025-21768         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-21768
  │ ✘✔✘✘✘ CVE-2025-21779         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-21779
  │ ✘✔✘✘✘ CVE-2025-21802         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21802
  │ ✘✔✘✘✘ CVE-2025-21816         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21816
  │ ✘✔✘✘✘ CVE-2025-21820         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21820
  │ ✘✔✘✘✘ CVE-2025-21831         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21831
  │ ✘✔✘✘✘ CVE-2025-21838         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21838
  │ ✘✔✘✘✘ CVE-2025-21861         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21861
  │ ✘✔✘✘✘ CVE-2025-21872         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21872
  │ ✘✔✘✘✘ CVE-2025-21881         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21881
  │ ✘✔✘✘✘ CVE-2025-21891         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21891
  │ ✘✔✘✘✘ CVE-2025-21894         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21894
  │ ✘✔✘✘✘ CVE-2025-21912         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21912
  │ ✘✔✘✘✘ CVE-2025-21931         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21931
  │ ✘✔✘✘✘ CVE-2025-21941         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21941
  │ ✘✔✘✘✘ CVE-2025-21956         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21956,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-21957         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21957,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-21996         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-21996,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-22005         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22005,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-22007         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22007,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-22010         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22010
  │ ✘✔✘✘✘ CVE-2025-22018         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22018,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-22027         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22027
  │ ✘✔✘✘✘ CVE-2025-22028         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22028
  │ ✘✔✘✘✘ CVE-2025-22053         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22053
  │ ✘✔✘✘✘ CVE-2025-22054         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22054,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-22058         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22058
  │ ✘✔✘✘✘ CVE-2025-22060         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22060
  │ ✘✔✘✘✘ CVE-2025-22063         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-22063,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-22071         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22071,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-22073         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22073,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-22103         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22103
  │ ✘✔✘✘✘ CVE-2025-22125         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-22125
  │ ✘✔✘✘✘ CVE-2025-2312          MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2025-2312,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-23131         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-23131
  │ ✘✔✘✘✘ CVE-2025-23136         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-23136,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-23140         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-23140
  │ ✘✔✘✘✘ CVE-2025-23143         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-23143
  │ ✘✔✘✘✘ CVE-2025-23147         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-23147
  │ ✘✔✘✘✘ CVE-2025-23148         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-23148
  │ ✘✔✘✘✘ CVE-2025-23161         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-23161
  │ ✘✔✘✘✘ CVE-2025-23163         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-23163
  │ ✘✔✘✘✘ CVE-2025-37740         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37740
  │ ✘✔✘✘✘ CVE-2025-37742         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37742
  │ ✘✔✘✘✘ CVE-2025-37758         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37758
  │ ✘✔✘✘✘ CVE-2025-37766         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37766
  │ ✘✔✘✘✘ CVE-2025-37768         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37768
  │ ✘✔✘✘✘ CVE-2025-37770         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37770
  │ ✘✔✘✘✘ CVE-2025-37773         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37773
  │ ✘✔✘✘✘ CVE-2025-37781         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37781
  │ ✘✔✘✘✘ CVE-2025-37792         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37792
  │ ✘✔✘✘✘ CVE-2025-37794         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37794
  │ ✘✔✘✘✘ CVE-2025-37807         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37807
  │ ✘✔✘✘✘ CVE-2025-37808         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37808
  │ ✘✔✘✘✘ CVE-2025-37812         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37812
  │ ✘✔✘✘✘ CVE-2025-37824         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37824
  │ ✘✔✘✘✘ CVE-2025-37829         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37829
  │ ✘✔✘✘✘ CVE-2025-37830         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37830
  │ ✘✔✘✘✘ CVE-2025-37833         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37833
  │ ✘✔✘✘✘ CVE-2025-37834         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37834
  │ ✘✔✘✘✘ CVE-2025-37836         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37836
  │ ✘✔✘✘✘ CVE-2025-37841         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37841
  │ ✘✔✘✘✘ CVE-2025-37842         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37842
  │ ✘✔✘✘✘ CVE-2025-37850         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37850
  │ ✘✔✘✘✘ CVE-2025-37851         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37851
  │ ✘✔✘✘✘ CVE-2025-37852         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37852
  │ ✘✔✘✘✘ CVE-2025-37853         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37853
  │ ✘✔✘✘✘ CVE-2025-37857         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37857
  │ ✘✔✘✘✘ CVE-2025-37858         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37858
  │ ✘✔✘✘✘ CVE-2025-37859         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37859
  │ ✘✔✘✘✘ CVE-2025-37862         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37862
  │ ✘✔✘✘✘ CVE-2025-37867         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37867
  │ ✘✔✘✘✘ CVE-2025-37880         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37880
  │ ✘✔✘✘✘ CVE-2025-37881         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37881
  │ ✘✔✘✘✘ CVE-2025-37883         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37883
  │ ✘✔✘✘✘ CVE-2025-37909         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37909
  │ ✘✔✘✘✘ CVE-2025-37925         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-37925
  │ ✘✔✘✘✘ CVE-2025-37932         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37932,USN-7671-1
  │ ✘✔✘✘✘ CVE-2025-37937         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37937,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-37940         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37940
  │ ✘✔✘✘✘ CVE-2025-37948         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37948
  │ ✘✔✘✘✘ CVE-2025-37951         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37951
  │ ✘✔✘✘✘ CVE-2025-37958         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37958,USN-7922-1
  │ ✘✔✘✘✘ CVE-2025-37961         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37961
  │ ✘✔✘✘✘ CVE-2025-37963         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37963
  │ ✘✔✘✘✘ CVE-2025-37967         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37967
  │ ✘✔✘✘✘ CVE-2025-37968         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37968
  │ ✘✔✘✘✘ CVE-2025-37969         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37969
  │ ✘✔✘✘✘ CVE-2025-37970         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37970
  │ ✘✔✘✘✘ CVE-2025-37980         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37980
  │ ✘✔✘✘✘ CVE-2025-37982         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37982
  │ ✘✔✘✘✘ CVE-2025-37983         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37983
  │ ✘✔✘✘✘ CVE-2025-37989         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37989
  │ ✘✔✘✘✘ CVE-2025-37990         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37990
  │ ✘✔✘✘✘ CVE-2025-37992         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37992
  │ ✘✔✘✘✘ CVE-2025-37994         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37994
  │ ✘✔✘✘✘ CVE-2025-37995         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-37995
  │ ✘✔✘✘✘ CVE-2025-38009         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38009
  │ ✘✔✘✘✘ CVE-2025-38023         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38023
  │ ✘✔✘✘✘ CVE-2025-38034         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38034
  │ ✘✔✘✘✘ CVE-2025-38037         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38037
  │ ✘✔✘✘✘ CVE-2025-38040         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38040
  │ ✘✔✘✘✘ CVE-2025-38043         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38043
  │ ✘✔✘✘✘ CVE-2025-38044         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38044
  │ ✘✔✘✘✘ CVE-2025-38048         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2025-38048
  │ ✘✔✘✘✘ CVE-2025-38061         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38061
  │ ✘✔✘✘✘ CVE-2025-38063         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38063
  │ ✘✔✘✘✘ CVE-2025-38066         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38066
  │ ✘✔✘✘✘ CVE-2025-38067         MEDIUM       5.5   0.6%   ·  ↳ S:UBUNTU-CVE-2025-38067
  │ ✘✔✘✘✘ CVE-2025-38072         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38072
  │ ✘✔✘✘✘ CVE-2025-38086         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38086
  │ ✘✔✘✘✘ CVE-2025-38094         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38094
  │ ✘✔✘✘✘ CVE-2025-38096         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38096
  │ ✘✔✘✘✘ CVE-2025-38105         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38105
  │ ✘✔✘✘✘ CVE-2025-38112         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2025-38112
  │ ✘✔✘✘✘ CVE-2025-38119         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38119
  │ ✘✔✘✘✘ CVE-2025-38126         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38126
  │ ✘✔✘✘✘ CVE-2025-38135         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38135
  │ ✘✔✘✘✘ CVE-2025-38136         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38136
  │ ✘✔✘✘✘ CVE-2025-38143         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38143
  │ ✘✔✘✘✘ CVE-2025-38145         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38145
  │ ✘✔✘✘✘ CVE-2025-38147         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38147
  │ ✘✔✘✘✘ CVE-2025-38163         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38163
  │ ✘✔✘✘✘ CVE-2025-38185         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38185
  │ ✘✔✘✘✘ CVE-2025-38190         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38190
  │ ✘✔✘✘✘ CVE-2025-38194         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38194
  │ ✘✔✘✘✘ CVE-2025-38200         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38200
  │ ✘✔✘✘✘ CVE-2025-38203         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38203
  │ ✘✔✘✘✘ CVE-2025-38207         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38207
  │ ✘✔✘✘✘ CVE-2025-38214         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38214
  │ ✘✔✘✘✘ CVE-2025-38215         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38215
  │ ✘✔✘✘✘ CVE-2025-38219         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38219
  │ ✘✔✘✘✘ CVE-2025-38222         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38222
  │ ✘✔✘✘✘ CVE-2025-38229         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38229
  │ ✘✔✘✘✘ CVE-2025-38237         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38237
  │ ✘✔✘✘✘ CVE-2025-38263         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38263
  │ ✘✔✘✘✘ CVE-2025-38272         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38272
  │ ✘✔✘✘✘ CVE-2025-38285         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38285
  │ ✘✔✘✘✘ CVE-2025-38305         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38305
  │ ✘✔✘✘✘ CVE-2025-38310         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38310
  │ ✘✔✘✘✘ CVE-2025-38312         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38312
  │ ✘✔✘✘✘ CVE-2025-38319         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38319
  │ ✘✔✘✘✘ CVE-2025-38324         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38324
  │ ✘✔✘✘✘ CVE-2025-38326         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38326
  │ ✘✔✘✘✘ CVE-2025-38328         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38328
  │ ✘✔✘✘✘ CVE-2025-38332         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38332
  │ ✘✔✘✘✘ CVE-2025-38336         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38336
  │ ✘✔✘✘✘ CVE-2025-38337         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38337
  │ ✘✔✘✘✘ CVE-2025-38344         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38344
  │ ✘✔✘✘✘ CVE-2025-38345         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38345
  │ ✘✔✘✘✘ CVE-2025-38347         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38347
  │ ✘✔✘✘✘ CVE-2025-38359         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38359
  │ ✘✔✘✘✘ CVE-2025-38363         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38363
  │ ✘✔✘✘✘ CVE-2025-38371         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38371
  │ ✘✔✘✘✘ CVE-2025-38384         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38384
  │ ✘✔✘✘✘ CVE-2025-38387         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38387
  │ ✘✔✘✘✘ CVE-2025-38391         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38391
  │ ✘✔✘✘✘ CVE-2025-38400         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38400
  │ ✘✔✘✘✘ CVE-2025-38406         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38406
  │ ✘✔✘✘✘ CVE-2025-38409         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38409
  │ ✘✔✘✘✘ CVE-2025-38410         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38410
  │ ✘✔✘✘✘ CVE-2025-38420         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38420
  │ ✘✔✘✘✘ CVE-2025-38426         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38426
  │ ✘✔✘✘✘ CVE-2025-38436         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38436
  │ ✘✔✘✘✘ CVE-2025-38438         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38438
  │ ✘✔✘✘✘ CVE-2025-38448         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2025-38448
  │ ✘✔✘✘✘ CVE-2025-38457         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38457
  │ ✘✔✘✘✘ CVE-2025-38458         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38458
  │ ✘✔✘✘✘ CVE-2025-38465         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38465
  │ ✘✔✘✘✘ CVE-2025-38467         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38467
  │ ✘✔✘✘✘ CVE-2025-38468         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38468
  │ ✘✔✘✘✘ CVE-2025-38473         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38473
  │ ✘✔✘✘✘ CVE-2025-38474         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38474
  │ ✘✔✘✘✘ CVE-2025-38480         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38480
  │ ✘✔✘✘✘ CVE-2025-38481         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38481
  │ ✘✔✘✘✘ CVE-2025-38487         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38487
  │ ✘✔✘✘✘ CVE-2025-38513         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38513
  │ ✘✔✘✘✘ CVE-2025-38515         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38515
  │ ✘✔✘✘✘ CVE-2025-38516         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38516
  │ ✘✔✘✘✘ CVE-2025-38540         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38540
  │ ✘✔✘✘✘ CVE-2025-38544         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38544
  │ ✘✔✘✘✘ CVE-2025-38546         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38546
  │ ✘✔✘✘✘ CVE-2025-38562         MEDIUM       5.5  13.0%   ·  ↳ S:UBUNTU-CVE-2025-38562
  │ ✘✔✘✘✘ CVE-2025-38569         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38569
  │ ✘✔✘✘✘ CVE-2025-38576         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38576
  │ ✘✔✘✘✘ CVE-2025-38581         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38581
  │ ✘✔✘✘✘ CVE-2025-38591         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38591
  │ ✘✔✘✘✘ CVE-2025-38602         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38602
  │ ✘✔✘✘✘ CVE-2025-38612         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38612
  │ ✘✔✘✘✘ CVE-2025-38622         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38622
  │ ✘✔✘✘✘ CVE-2025-38623         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38623
  │ ✘✔✘✘✘ CVE-2025-38624         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38624
  │ ✘✔✘✘✘ CVE-2025-38626         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38626
  │ ✘✔✘✘✘ CVE-2025-38630         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38630
  │ ✘✔✘✘✘ CVE-2025-38635         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38635
  │ ✘✔✘✘✘ CVE-2025-38637         MEDIUM       5.5   0.3%   ·  ↳ S:UBUNTU-CVE-2025-38637,USN-7585-1
  │ ✘✔✘✘✘ CVE-2025-38644         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38644
  │ ✘✔✘✘✘ CVE-2025-38645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38645
  │ ✘✔✘✘✘ CVE-2025-38650         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-38650
  │ ✘✔✘✘✘ CVE-2025-38663         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38663
  │ ✘✔✘✘✘ CVE-2025-38664         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38664
  │ ✘✔✘✘✘ CVE-2025-38665         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38665
  │ ✘✔✘✘✘ CVE-2025-38668         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38668
  │ ✘✔✘✘✘ CVE-2025-38671         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38671
  │ ✘✔✘✘✘ CVE-2025-38683         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38683
  │ ✘✔✘✘✘ CVE-2025-38684         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38684
  │ ✘✔✘✘✘ CVE-2025-38691         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38691
  │ ✘✔✘✘✘ CVE-2025-38693         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38693
  │ ✘✔✘✘✘ CVE-2025-38694         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38694
  │ ✘✔✘✘✘ CVE-2025-38695         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38695
  │ ✘✔✘✘✘ CVE-2025-38696         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38696
  │ ✘✔✘✘✘ CVE-2025-38698         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38698
  │ ✘✔✘✘✘ CVE-2025-38700         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38700
  │ ✘✔✘✘✘ CVE-2025-38701         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38701
  │ ✘✔✘✘✘ CVE-2025-38705         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38705
  │ ✘✔✘✘✘ CVE-2025-38706         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38706
  │ ✘✔✘✘✘ CVE-2025-38709         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-38709
  │ ✘✔✘✘✘ CVE-2025-38711         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-38711
  │ ✘✔✘✘✘ CVE-2025-38712         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38712
  │ ✘✔✘✘✘ CVE-2025-38716         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-38716
  │ ✘✔✘✘✘ CVE-2025-38721         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-38721
  │ ✘✔✘✘✘ CVE-2025-39676         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39676
  │ ✘✔✘✘✘ CVE-2025-39684         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39684
  │ ✘✔✘✘✘ CVE-2025-39693         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39693
  │ ✘✔✘✘✘ CVE-2025-39705         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39705
  │ ✘✔✘✘✘ CVE-2025-39706         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39706
  │ ✘✔✘✘✘ CVE-2025-39707         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39707
  │ ✘✔✘✘✘ CVE-2025-39709         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39709
  │ ✘✔✘✘✘ CVE-2025-39713         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39713
  │ ✘✔✘✘✘ CVE-2025-39716         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39716
  │ ✘✔✘✘✘ CVE-2025-39724         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39724
  │ ✘✔✘✘✘ CVE-2025-39736         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39736
  │ ✘✔✘✘✘ CVE-2025-39737         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39737
  │ ✘✔✘✘✘ CVE-2025-39742         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39742
  │ ✘✔✘✘✘ CVE-2025-39746         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39746
  │ ✘✔✘✘✘ CVE-2025-39747         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39747
  │ ✘✔✘✘✘ CVE-2025-39748         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39748
  │ ✘✔✘✘✘ CVE-2025-39752         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39752
  │ ✘✔✘✘✘ CVE-2025-39754         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39754
  │ ✘✔✘✘✘ CVE-2025-39756         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39756
  │ ✘✔✘✘✘ CVE-2025-39762         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39762
  │ ✘✔✘✘✘ CVE-2025-39763         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39763
  │ ✘✔✘✘✘ CVE-2025-39764         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39764
  │ ✘✔✘✘✘ CVE-2025-39772         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39772
  │ ✘✔✘✘✘ CVE-2025-39773         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39773
  │ ✘✔✘✘✘ CVE-2025-39782         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39782
  │ ✘✔✘✘✘ CVE-2025-39794         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39794
  │ ✘✔✘✘✘ CVE-2025-39795         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39795
  │ ✘✔✘✘✘ CVE-2025-39801         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39801
  │ ✘✔✘✘✘ CVE-2025-39808         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39808
  │ ✘✔✘✘✘ CVE-2025-39812         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39812
  │ ✘✔✘✘✘ CVE-2025-39813         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39813
  │ ✘✔✘✘✘ CVE-2025-39829         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39829
  │ ✘✔✘✘✘ CVE-2025-39833         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39833
  │ ✘✔✘✘✘ CVE-2025-39846         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39846
  │ ✘✔✘✘✘ CVE-2025-39847         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39847
  │ ✘✔✘✘✘ CVE-2025-39865         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39865
  │ ✘✔✘✘✘ CVE-2025-39876         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39876
  │ ✘✔✘✘✘ CVE-2025-39885         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39885
  │ ✘✔✘✘✘ CVE-2025-39907         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39907
  │ ✘✔✘✘✘ CVE-2025-39920         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39920
  │ ✘✔✘✘✘ CVE-2025-39923         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39923
  │ ✘✔✘✘✘ CVE-2025-39925         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39925
  │ ✘✔✘✘✘ CVE-2025-39937         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-39937
  │ ✘✔✘✘✘ CVE-2025-39940         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39940
  │ ✘✔✘✘✘ CVE-2025-39953         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39953
  │ ✘✔✘✘✘ CVE-2025-40005         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40005
  │ ✘✔✘✘✘ CVE-2025-40164         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40164
  │ ✘✔✘✘✘ CVE-2025-40300         MEDIUM       5.5   0.4%   ·  ↳ S:UBUNTU-CVE-2025-40300,USN-7874-1
  │ ✘✔✘✘✘ CVE-2025-68211         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-68211
  │ ✘✔✘✘✘ CVE-2025-68214         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2025-68214
  │ ✘✔✘✘✘ CVE-2025-68223         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-68223
  │ ✘✔✘✘✘ CVE-2025-68358         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68358
  │ ✘✔✘✘✘ CVE-2025-71077         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71077
  │ ✘✔✘✘✘ CVE-2025-71079         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71079
  │ ✘✔✘✘✘ CVE-2025-71081         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71081
  │ ✘✔✘✘✘ CVE-2025-71083         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71083
  │ ✘✔✘✘✘ CVE-2025-71087         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71087
  │ ✘✔✘✘✘ CVE-2025-71096         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71096
  │ ✘✔✘✘✘ CVE-2025-71097         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71097
  │ ✘✔✘✘✘ CVE-2025-71098         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71098
  │ ✘✔✘✘✘ CVE-2025-71104         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71104
  │ ✘✔✘✘✘ CVE-2025-71105         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71105
  │ ✘✔✘✘✘ CVE-2025-71108         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71108
  │ ✘✔✘✘✘ CVE-2025-71111         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71111
  │ ✘✔✘✘✘ CVE-2025-71113         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71113
  │ ✘✔✘✘✘ CVE-2025-71114         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71114
  │ ✘✔✘✘✘ CVE-2025-71118         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71118
  │ ✘✔✘✘✘ CVE-2025-71121         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71121
  │ ✘✔✘✘✘ CVE-2025-71125         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71125
  │ ✘✔✘✘✘ CVE-2025-71154         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71154
  │ ✘✔✘✘✘ CVE-2025-71160         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71160
  │ ✘✔✘✘✘ CVE-2025-71180         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71180
  │ ✘✔✘✘✘ CVE-2025-71182         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71182
  │ ✘✔✘✘✘ CVE-2025-71184         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71184
  │ ✘✔✘✘✘ CVE-2025-71185         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71185
  │ ✘✔✘✘✘ CVE-2025-71186         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71186
  │ ✘✔✘✘✘ CVE-2025-71188         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71188
  │ ✘✔✘✘✘ CVE-2025-71190         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71190
  │ ✘✔✘✘✘ CVE-2025-71191         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71191
  │ ✘✔✘✘✘ CVE-2025-71222         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71222
  │ ✘✔✘✘✘ CVE-2025-71225         MEDIUM       5.3   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71225
  │ ✘✔✘✘✘ CVE-2025-71227         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71227
  │ ✘✔✘✘✘ CVE-2025-71232         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71232
  │ ✘✔✘✘✘ CVE-2025-71235         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71235
  │ ✘✔✘✘✘ CVE-2025-71237         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71237
  │ ✘✔✘✘✘ CVE-2025-71239         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71239
  │ ✘✔✘✘✘ CVE-2025-71265         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71265
  │ ✘✔✘✘✘ CVE-2025-71266         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71266
  │ ✘✔✘✘✘ CVE-2025-71267         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71267
  │ ✘✔✘✘✘ CVE-2025-71273         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71273
  │ ✘✔✘✘✘ CVE-2025-71287         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71287
  │ ✘✔✘✘✘ CVE-2025-71304         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71304
  │ ✘✔✘✘✘ CVE-2025-71315         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-71315
  │ ✘✔✘✘✘ CVE-2026-100070        MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-100070
  │ ✘✔✘✘✘ CVE-2026-100071        MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-100071
  │ ✘✔✘✘✘ CVE-2026-100076        MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-100076
  │ ✘✔✘✘✘ CVE-2026-100077        MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-100077
  │ ✘✔✘✘✘ CVE-2026-22976         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-22976
  │ ✘✔✘✘✘ CVE-2026-22977         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-22977
  │ ✘✔✘✘✘ CVE-2026-23011         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23011
  │ ✘✔✘✘✘ CVE-2026-23020         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23020
  │ ✘✔✘✘✘ CVE-2026-23021         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23021
  │ ✘✔✘✘✘ CVE-2026-23060         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23060,USN-8200-1
  │ ✘✔✘✘✘ CVE-2026-23061         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23061
  │ ✘✔✘✘✘ CVE-2026-23064         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23064
  │ ✘✔✘✘✘ CVE-2026-23069         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23069
  │ ✘✔✘✘✘ CVE-2026-23071         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23071
  │ ✘✔✘✘✘ CVE-2026-23075         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23075
  │ ✘✔✘✘✘ CVE-2026-23080         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23080
  │ ✘✔✘✘✘ CVE-2026-23084         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23084
  │ ✘✔✘✘✘ CVE-2026-23085         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23085
  │ ✘✔✘✘✘ CVE-2026-23086         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23086
  │ ✘✔✘✘✘ CVE-2026-23087         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23087
  │ ✘✔✘✘✘ CVE-2026-23090         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23090
  │ ✘✔✘✘✘ CVE-2026-23091         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23091
  │ ✘✔✘✘✘ CVE-2026-23101         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23101
  │ ✘✔✘✘✘ CVE-2026-23108         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23108
  │ ✘✔✘✘✘ CVE-2026-23113         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23113
  │ ✘✔✘✘✘ CVE-2026-23118         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23118
  │ ✘✔✘✘✘ CVE-2026-23120         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23120
  │ ✘✔✘✘✘ CVE-2026-23121         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23121
  │ ✘✔✘✘✘ CVE-2026-23125         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23125
  │ ✘✔✘✘✘ CVE-2026-23126         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23126
  │ ✘✔✘✘✘ CVE-2026-23128         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23128
  │ ✘✔✘✘✘ CVE-2026-23133         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23133
  │ ✘✔✘✘✘ CVE-2026-23137         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23137
  │ ✘✔✘✘✘ CVE-2026-23141         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23141
  │ ✘✔✘✘✘ CVE-2026-23150         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23150
  │ ✘✔✘✘✘ CVE-2026-23157         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23157
  │ ✘✔✘✘✘ CVE-2026-23164         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23164
  │ ✘✔✘✘✘ CVE-2026-23167         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23167
  │ ✘✔✘✘✘ CVE-2026-23170         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23170
  │ ✘✔✘✘✘ CVE-2026-23190         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23190
  │ ✘✔✘✘✘ CVE-2026-23212         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23212
  │ ✘✔✘✘✘ CVE-2026-23220         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23220
  │ ✘✔✘✘✘ CVE-2026-23229         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23229
  │ ✘✔✘✘✘ CVE-2026-23237         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23237
  │ ✘✔✘✘✘ CVE-2026-23238         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23238
  │ ✘✔✘✘✘ CVE-2026-23241         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23241
  │ ✘✔✘✘✘ CVE-2026-23247         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23247
  │ ✘✔✘✘✘ CVE-2026-23255         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23255
  │ ✘✔✘✘✘ CVE-2026-23256         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23256
  │ ✘✔✘✘✘ CVE-2026-23257         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23257
  │ ✘✔✘✘✘ CVE-2026-23258         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23258
  │ ✘✔✘✘✘ CVE-2026-23265         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23265
  │ ✘✔✘✘✘ CVE-2026-23266         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23266
  │ ✘✔✘✘✘ CVE-2026-23267         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23267
  │ ✘✔✘✘✘ CVE-2026-23276         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23276
  │ ✘✔✘✘✘ CVE-2026-23277         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23277
  │ ✘✔✘✘✘ CVE-2026-23279         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23279
  │ ✘✔✘✘✘ CVE-2026-23286         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23286
  │ ✘✔✘✘✘ CVE-2026-23287         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23287
  │ ✘✔✘✘✘ CVE-2026-23289         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23289
  │ ✘✔✘✘✘ CVE-2026-23290         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23290
  │ ✘✔✘✘✘ CVE-2026-23291         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23291
  │ ✘✔✘✘✘ CVE-2026-23292         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23292
  │ ✘✔✘✘✘ CVE-2026-23293         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23293
  │ ✘✔✘✘✘ CVE-2026-23298         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23298
  │ ✘✔✘✘✘ CVE-2026-23300         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23300
  │ ✘✔✘✘✘ CVE-2026-23302         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23302
  │ ✘✔✘✘✘ CVE-2026-23303         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23303
  │ ✘✔✘✘✘ CVE-2026-23304         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23304
  │ ✘✔✘✘✘ CVE-2026-23307         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23307
  │ ✘✔✘✘✘ CVE-2026-23312         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23312
  │ ✘✔✘✘✘ CVE-2026-23330         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23330
  │ ✘✔✘✘✘ CVE-2026-23339         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23339
  │ ✘✔✘✘✘ CVE-2026-23352         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23352
  │ ✘✔✘✘✘ CVE-2026-23356         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23356
  │ ✘✔✘✘✘ CVE-2026-23357         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23357
  │ ✘✔✘✘✘ CVE-2026-23365         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23365
  │ ✘✔✘✘✘ CVE-2026-23367         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23367
  │ ✘✔✘✘✘ CVE-2026-23368         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23368
  │ ✘✔✘✘✘ CVE-2026-23371         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23371
  │ ✘✔✘✘✘ CVE-2026-23374         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23374
  │ ✘✔✘✘✘ CVE-2026-23381         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23381
  │ ✘✔✘✘✘ CVE-2026-23382         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23382
  │ ✘✔✘✘✘ CVE-2026-23389         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23389
  │ ✘✔✘✘✘ CVE-2026-23396         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23396
  │ ✘✔✘✘✘ CVE-2026-23398         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23398
  │ ✘✔✘✘✘ CVE-2026-23403         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23403
  │ ✘✔✘✘✘ CVE-2026-23404         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23404
  │ ✘✔✘✘✘ CVE-2026-23405         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23405
  │ ✘✔✘✘✘ CVE-2026-23409         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23409
  │ ✘✔✘✘✘ CVE-2026-23420         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23420
  │ ✘✔✘✘✘ CVE-2026-23439         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23439
  │ ✘✔✘✘✘ CVE-2026-23442         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23442
  │ ✘✔✘✘✘ CVE-2026-23446         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23446
  │ ✘✔✘✘✘ CVE-2026-23452         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23452
  │ ✘✔✘✘✘ CVE-2026-23460         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23460
  │ ✘✔✘✘✘ CVE-2026-23463         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23463
  │ ✘✔✘✘✘ CVE-2026-23465         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23465
  │ ✘✔✘✘✘ CVE-2026-23468         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23468
  │ ✘✔✘✘✘ CVE-2026-23472         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23472
  │ ✘✔✘✘✘ CVE-2026-23474         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-23474
  │ ✘✔✘✘✘ CVE-2026-31391         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31391
  │ ✘✔✘✘✘ CVE-2026-31400         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31400
  │ ✘✔✘✘✘ CVE-2026-31411         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31411
  │ ✘✔✘✘✘ CVE-2026-31412         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31412
  │ ✘✔✘✘✘ CVE-2026-31415         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31415
  │ ✘✔✘✘✘ CVE-2026-31416         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31416
  │ ✘✔✘✘✘ CVE-2026-31418         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31418,USN-8615-1
  │ ✘✔✘✘✘ CVE-2026-31421         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31421
  │ ✘✔✘✘✘ CVE-2026-31422         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31422
  │ ✘✔✘✘✘ CVE-2026-31423         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31423
  │ ✘✔✘✘✘ CVE-2026-31424         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31424
  │ ✘✔✘✘✘ CVE-2026-31425         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31425
  │ ✘✔✘✘✘ CVE-2026-31427         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31427
  │ ✘✔✘✘✘ CVE-2026-31428         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31428
  │ ✘✔✘✘✘ CVE-2026-31451         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31451
  │ ✘✔✘✘✘ CVE-2026-31462         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31462
  │ ✘✔✘✘✘ CVE-2026-31466         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31466
  │ ✘✔✘✘✘ CVE-2026-31487         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31487
  │ ✘✔✘✘✘ CVE-2026-31495         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31495
  │ ✘✔✘✘✘ CVE-2026-31496         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31496
  │ ✘✔✘✘✘ CVE-2026-31498         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31498
  │ ✘✔✘✘✘ CVE-2026-31503         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31503
  │ ✘✔✘✘✘ CVE-2026-31509         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31509
  │ ✘✔✘✘✘ CVE-2026-31510         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31510
  │ ✘✔✘✘✘ CVE-2026-31512         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31512
  │ ✘✔✘✘✘ CVE-2026-31515         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31515
  │ ✘✔✘✘✘ CVE-2026-31519         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31519
  │ ✘✔✘✘✘ CVE-2026-31521         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31521
  │ ✘✔✘✘✘ CVE-2026-31522         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31522
  │ ✘✔✘✘✘ CVE-2026-31523         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31523
  │ ✘✔✘✘✘ CVE-2026-31524         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31524
  │ ✘✔✘✘✘ CVE-2026-31531         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31531
  │ ✘✔✘✘✘ CVE-2026-31540         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31540
  │ ✘✔✘✘✘ CVE-2026-31545         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31545
  │ ✘✔✘✘✘ CVE-2026-31546         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31546
  │ ✘✔✘✘✘ CVE-2026-31550         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31550
  │ ✘✔✘✘✘ CVE-2026-31555         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31555
  │ ✘✔✘✘✘ CVE-2026-31577         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31577
  │ ✘✔✘✘✘ CVE-2026-31592         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31592
  │ ✘✔✘✘✘ CVE-2026-31596         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31596
  │ ✘✔✘✘✘ CVE-2026-31603         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31603
  │ ✘✔✘✘✘ CVE-2026-31605         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31605
  │ ✘✔✘✘✘ CVE-2026-31606         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31606
  │ ✘✔✘✘✘ CVE-2026-31610         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31610
  │ ✘✔✘✘✘ CVE-2026-31615         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31615
  │ ✘✔✘✘✘ CVE-2026-31616         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31616
  │ ✘✔✘✘✘ CVE-2026-31617         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31617
  │ ✘✔✘✘✘ CVE-2026-31618         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31618
  │ ✘✔✘✘✘ CVE-2026-31619         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31619
  │ ✘✔✘✘✘ CVE-2026-31623         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31623
  │ ✘✔✘✘✘ CVE-2026-31624         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31624
  │ ✘✔✘✘✘ CVE-2026-31625         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31625
  │ ✘✔✘✘✘ CVE-2026-31628         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31628
  │ ✘✔✘✘✘ CVE-2026-31634         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31634
  │ ✘✔✘✘✘ CVE-2026-31642         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31642
  │ ✘✔✘✘✘ CVE-2026-31651         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31651
  │ ✘✔✘✘✘ CVE-2026-31658         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31658
  │ ✘✔✘✘✘ CVE-2026-31661         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31661
  │ ✘✔✘✘✘ CVE-2026-31664         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31664
  │ ✘✔✘✘✘ CVE-2026-31670         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31670
  │ ✘✔✘✘✘ CVE-2026-31671         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31671
  │ ✘✔✘✘✘ CVE-2026-31672         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31672
  │ ✘✔✘✘✘ CVE-2026-31677         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31677
  │ ✘✔✘✘✘ CVE-2026-31681         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31681
  │ ✘✔✘✘✘ CVE-2026-31684         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31684
  │ ✘✔✘✘✘ CVE-2026-31687         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31687
  │ ✘✔✘✘✘ CVE-2026-31692         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31692
  │ ✘✔✘✘✘ CVE-2026-31701         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31701
  │ ✘✔✘✘✘ CVE-2026-31721         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31721
  │ ✘✔✘✘✘ CVE-2026-31722         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31722
  │ ✘✔✘✘✘ CVE-2026-31723         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31723
  │ ✘✔✘✘✘ CVE-2026-31724         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31724
  │ ✘✔✘✘✘ CVE-2026-31725         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-31725
  │ ✘✔✘✘✘ CVE-2026-31728         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31728
  │ ✘✔✘✘✘ CVE-2026-31737         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31737
  │ ✘✔✘✘✘ CVE-2026-31738         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31738
  │ ✘✔✘✘✘ CVE-2026-31749         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31749
  │ ✘✔✘✘✘ CVE-2026-31751         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31751
  │ ✘✔✘✘✘ CVE-2026-31752         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31752
  │ ✘✔✘✘✘ CVE-2026-31754         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31754
  │ ✘✔✘✘✘ CVE-2026-31755         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31755
  │ ✘✔✘✘✘ CVE-2026-31762         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31762
  │ ✘✔✘✘✘ CVE-2026-31763         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31763
  │ ✘✔✘✘✘ CVE-2026-31770         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31770
  │ ✘✔✘✘✘ CVE-2026-31777         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31777
  │ ✘✔✘✘✘ CVE-2026-31781         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-31781
  │ ✘✔✘✘✘ CVE-2026-43014         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43014
  │ ✘✔✘✘✘ CVE-2026-43024         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43024
  │ ✘✔✘✘✘ CVE-2026-43026         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43026
  │ ✘✔✘✘✘ CVE-2026-43035         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43035
  │ ✘✔✘✘✘ CVE-2026-43036         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43036
  │ ✘✔✘✘✘ CVE-2026-43043         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43043
  │ ✘✔✘✘✘ CVE-2026-43046         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43046
  │ ✘✔✘✘✘ CVE-2026-43053         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43053
  │ ✘✔✘✘✘ CVE-2026-43061         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43061
  │ ✘✔✘✘✘ CVE-2026-43068         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43068
  │ ✘✔✘✘✘ CVE-2026-43069         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43069
  │ ✘✔✘✘✘ CVE-2026-43073         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43073
  │ ✘✔✘✘✘ CVE-2026-43077         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43077
  │ ✘✔✘✘✘ CVE-2026-43080         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43080
  │ ✘✔✘✘✘ CVE-2026-43085         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43085
  │ ✘✔✘✘✘ CVE-2026-43088         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43088
  │ ✘✔✘✘✘ CVE-2026-43089         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43089
  │ ✘✔✘✘✘ CVE-2026-43103         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43103
  │ ✘✔✘✘✘ CVE-2026-43104         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43104
  │ ✘✔✘✘✘ CVE-2026-43105         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43105
  │ ✘✔✘✘✘ CVE-2026-43107         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43107
  │ ✘✔✘✘✘ CVE-2026-43115         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43115
  │ ✘✔✘✘✘ CVE-2026-43118         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43118
  │ ✘✔✘✘✘ CVE-2026-43119         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43119
  │ ✘✔✘✘✘ CVE-2026-43123         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43123
  │ ✘✔✘✘✘ CVE-2026-43124         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43124
  │ ✘✔✘✘✘ CVE-2026-43130         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43130
  │ ✘✔✘✘✘ CVE-2026-43132         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43132
  │ ✘✔✘✘✘ CVE-2026-43135         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43135
  │ ✘✔✘✘✘ CVE-2026-43136         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43136
  │ ✘✔✘✘✘ CVE-2026-43140         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43140
  │ ✘✔✘✘✘ CVE-2026-43149         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43149
  │ ✘✔✘✘✘ CVE-2026-43152         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43152
  │ ✘✔✘✘✘ CVE-2026-43156         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43156
  │ ✘✔✘✘✘ CVE-2026-43159         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43159
  │ ✘✔✘✘✘ CVE-2026-43163         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43163
  │ ✘✔✘✘✘ CVE-2026-43167         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43167
  │ ✘✔✘✘✘ CVE-2026-43168         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43168
  │ ✘✔✘✘✘ CVE-2026-43171         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43171
  │ ✘✔✘✘✘ CVE-2026-43182         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43182
  │ ✘✔✘✘✘ CVE-2026-43183         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43183
  │ ✘✔✘✘✘ CVE-2026-43202         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43202
  │ ✘✔✘✘✘ CVE-2026-43204         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43204
  │ ✘✔✘✘✘ CVE-2026-43209         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43209
  │ ✘✔✘✘✘ CVE-2026-43216         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43216
  │ ✘✔✘✘✘ CVE-2026-43218         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43218
  │ ✘✔✘✘✘ CVE-2026-43223         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43223
  │ ✘✔✘✘✘ CVE-2026-43225         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43225
  │ ✘✔✘✘✘ CVE-2026-43227         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43227
  │ ✘✔✘✘✘ CVE-2026-43231         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43231
  │ ✘✔✘✘✘ CVE-2026-43234         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43234
  │ ✘✔✘✘✘ CVE-2026-43244         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43244
  │ ✘✔✘✘✘ CVE-2026-43246         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43246
  │ ✘✔✘✘✘ CVE-2026-43251         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43251
  │ ✘✔✘✘✘ CVE-2026-43255         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43255
  │ ✘✔✘✘✘ CVE-2026-43257         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43257
  │ ✘✔✘✘✘ CVE-2026-43261         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43261
  │ ✘✔✘✘✘ CVE-2026-43262         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43262
  │ ✘✔✘✘✘ CVE-2026-43264         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43264
  │ ✘✔✘✘✘ CVE-2026-43266         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43266
  │ ✘✔✘✘✘ CVE-2026-43268         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43268
  │ ✘✔✘✘✘ CVE-2026-43269         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43269
  │ ✘✔✘✘✘ CVE-2026-43270         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43270
  │ ✘✔✘✘✘ CVE-2026-43271         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43271
  │ ✘✔✘✘✘ CVE-2026-43273         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43273
  │ ✘✔✘✘✘ CVE-2026-43275         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43275
  │ ✘✔✘✘✘ CVE-2026-43277         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43277
  │ ✘✔✘✘✘ CVE-2026-43287         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43287
  │ ✘✔✘✘✘ CVE-2026-43288         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43288
  │ ✘✔✘✘✘ CVE-2026-43289         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43289
  │ ✘✔✘✘✘ CVE-2026-43295         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43295
  │ ✘✔✘✘✘ CVE-2026-43299         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43299
  │ ✘✔✘✘✘ CVE-2026-43302         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43302
  │ ✘✔✘✘✘ CVE-2026-43308         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43308
  │ ✘✔✘✘✘ CVE-2026-43309         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43309
  │ ✘✔✘✘✘ CVE-2026-43313         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43313
  │ ✘✔✘✘✘ CVE-2026-43314         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43314
  │ ✘✔✘✘✘ CVE-2026-43316         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43316
  │ ✘✔✘✘✘ CVE-2026-43327         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43327
  │ ✘✔✘✘✘ CVE-2026-43338         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43338
  │ ✘✔✘✘✘ CVE-2026-43340         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43340
  │ ✘✔✘✘✘ CVE-2026-43342         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43342
  │ ✘✔✘✘✘ CVE-2026-43343         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43343
  │ ✘✔✘✘✘ CVE-2026-43355         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43355
  │ ✘✔✘✘✘ CVE-2026-43357         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43357
  │ ✘✔✘✘✘ CVE-2026-43359         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43359
  │ ✘✔✘✘✘ CVE-2026-43361         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43361
  │ ✘✔✘✘✘ CVE-2026-43363         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43363
  │ ✘✔✘✘✘ CVE-2026-43381         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43381
  │ ✘✔✘✘✘ CVE-2026-43382         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43382
  │ ✘✔✘✘✘ CVE-2026-43387         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43387
  │ ✘✔✘✘✘ CVE-2026-43409         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43409
  │ ✘✔✘✘✘ CVE-2026-43411         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43411
  │ ✘✔✘✘✘ CVE-2026-43413         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43413
  │ ✘✔✘✘✘ CVE-2026-43416         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43416
  │ ✘✔✘✘✘ CVE-2026-43421         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43421
  │ ✘✔✘✘✘ CVE-2026-43424         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43424
  │ ✘✔✘✘✘ CVE-2026-43425         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43425
  │ ✘✔✘✘✘ CVE-2026-43428         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43428
  │ ✘✔✘✘✘ CVE-2026-43429         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43429
  │ ✘✔✘✘✘ CVE-2026-43430         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43430
  │ ✘✔✘✘✘ CVE-2026-43432         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43432
  │ ✘✔✘✘✘ CVE-2026-43439         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43439
  │ ✘✔✘✘✘ CVE-2026-43445         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43445
  │ ✘✔✘✘✘ CVE-2026-43448         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43448
  │ ✘✔✘✘✘ CVE-2026-43451         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43451
  │ ✘✔✘✘✘ CVE-2026-43472         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43472
  │ ✘✔✘✘✘ CVE-2026-43473         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43473
  │ ✘✔✘✘✘ CVE-2026-43475         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43475
  │ ✘✔✘✘✘ CVE-2026-43483         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43483
  │ ✘✔✘✘✘ CVE-2026-43484         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43484
  │ ✘✔✘✘✘ CVE-2026-43492         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-43492
  │ ✘✔✘✘✘ CVE-2026-43496         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-43496
  │ ✘✔✘✘✘ CVE-2026-45834         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45834
  │ ✘✔✘✘✘ CVE-2026-45835         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45835
  │ ✘✔✘✘✘ CVE-2026-45836         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45836
  │ ✘✔✘✘✘ CVE-2026-45838         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45838
  │ ✘✔✘✘✘ CVE-2026-45840         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45840
  │ ✘✔✘✘✘ CVE-2026-45841         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45841
  │ ✘✔✘✘✘ CVE-2026-45842         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45842
  │ ✘✔✘✘✘ CVE-2026-45844         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45844
  │ ✘✔✘✘✘ CVE-2026-45848         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45848
  │ ✘✔✘✘✘ CVE-2026-45850         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45850
  │ ✘✔✘✘✘ CVE-2026-45857         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45857
  │ ✘✔✘✘✘ CVE-2026-45858         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45858
  │ ✘✔✘✘✘ CVE-2026-45868         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45868
  │ ✘✔✘✘✘ CVE-2026-45869         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45869
  │ ✘✔✘✘✘ CVE-2026-45870         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45870
  │ ✘✔✘✘✘ CVE-2026-45871         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45871
  │ ✘✔✘✘✘ CVE-2026-45873         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45873
  │ ✘✔✘✘✘ CVE-2026-45875         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45875
  │ ✘✔✘✘✘ CVE-2026-45877         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45877
  │ ✘✔✘✘✘ CVE-2026-45883         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45883
  │ ✘✔✘✘✘ CVE-2026-45890         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45890
  │ ✘✔✘✘✘ CVE-2026-45899         MEDIUM       5.5   0.2%   ·  ↳ S:LSN-0122-1,UBUNTU-CVE-2026-45899
  │ ✘✔✘✘✘ CVE-2026-45905         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45905
  │ ✘✔✘✘✘ CVE-2026-45912         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45912
  │ ✘✔✘✘✘ CVE-2026-45915         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45915
  │ ✘✔✘✘✘ CVE-2026-45917         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45917
  │ ✘✔✘✘✘ CVE-2026-45919         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45919
  │ ✘✔✘✘✘ CVE-2026-45923         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45923
  │ ✘✔✘✘✘ CVE-2026-45934         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45934
  │ ✘✔✘✘✘ CVE-2026-45940         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45940
  │ ✘✔✘✘✘ CVE-2026-45941         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45941
  │ ✘✔✘✘✘ CVE-2026-45948         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45948
  │ ✘✔✘✘✘ CVE-2026-45949         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45949
  │ ✘✔✘✘✘ CVE-2026-45954         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45954
  │ ✘✔✘✘✘ CVE-2026-45960         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45960
  │ ✘✔✘✘✘ CVE-2026-45964         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45964
  │ ✘✔✘✘✘ CVE-2026-45965         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-45965
  │ ✘✔✘✘✘ CVE-2026-45968         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45968
  │ ✘✔✘✘✘ CVE-2026-45978         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45978
  │ ✘✔✘✘✘ CVE-2026-45981         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45981
  │ ✘✔✘✘✘ CVE-2026-45983         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45983
  │ ✘✔✘✘✘ CVE-2026-45985         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45985
  │ ✘✔✘✘✘ CVE-2026-45986         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45986
  │ ✘✔✘✘✘ CVE-2026-45997         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-45997
  │ ✘✔✘✘✘ CVE-2026-46000         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-46000
  │ ✘✔✘✘✘ CVE-2026-46002         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46002
  │ ✘✔✘✘✘ CVE-2026-46014         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46014
  │ ✘✔✘✘✘ CVE-2026-46018         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-46018
  │ ✘✔✘✘✘ CVE-2026-46019         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-46019
  │ ✘✔✘✘✘ CVE-2026-46021         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46021
  │ ✘✔✘✘✘ CVE-2026-46023         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46023
  │ ✘✔✘✘✘ CVE-2026-46028         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46028
  │ ✘✔✘✘✘ CVE-2026-46040         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46040
  │ ✘✔✘✘✘ CVE-2026-46044         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46044
  │ ✘✔✘✘✘ CVE-2026-46049         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46049
  │ ✘✔✘✘✘ CVE-2026-46051         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46051
  │ ✘✔✘✘✘ CVE-2026-46077         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46077
  │ ✘✔✘✘✘ CVE-2026-46080         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46080
  │ ✘✔✘✘✘ CVE-2026-46082         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46082
  │ ✘✔✘✘✘ CVE-2026-46083         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46083
  │ ✘✔✘✘✘ CVE-2026-46086         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46086
  │ ✘✔✘✘✘ CVE-2026-46088         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46088
  │ ✘✔✘✘✘ CVE-2026-46091         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46091
  │ ✘✔✘✘✘ CVE-2026-46098         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46098
  │ ✘✔✘✘✘ CVE-2026-46103         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46103
  │ ✘✔✘✘✘ CVE-2026-46108         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46108
  │ ✘✔✘✘✘ CVE-2026-46127         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46127
  │ ✘✔✘✘✘ CVE-2026-46128         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46128
  │ ✘✔✘✘✘ CVE-2026-46132         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46132
  │ ✘✔✘✘✘ CVE-2026-46147         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46147
  │ ✘✔✘✘✘ CVE-2026-46151         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46151
  │ ✘✔✘✘✘ CVE-2026-46153         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46153
  │ ✘✔✘✘✘ CVE-2026-46159         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46159
  │ ✘✔✘✘✘ CVE-2026-46160         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46160
  │ ✘✔✘✘✘ CVE-2026-46161         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46161
  │ ✘✔✘✘✘ CVE-2026-46167         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46167
  │ ✘✔✘✘✘ CVE-2026-46169         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46169
  │ ✘✔✘✘✘ CVE-2026-46184         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46184
  │ ✘✔✘✘✘ CVE-2026-46187         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46187
  │ ✘✔✘✘✘ CVE-2026-46193         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46193
  │ ✘✔✘✘✘ CVE-2026-46196         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46196
  │ ✘✔✘✘✘ CVE-2026-46200         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46200
  │ ✘✔✘✘✘ CVE-2026-46220         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46220
  │ ✘✔✘✘✘ CVE-2026-46225         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46225
  │ ✘✔✘✘✘ CVE-2026-46226         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46226
  │ ✘✔✘✘✘ CVE-2026-46229         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46229
  │ ✘✔✘✘✘ CVE-2026-46231         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46231
  │ ✘✔✘✘✘ CVE-2026-46233         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46233
  │ ✘✔✘✘✘ CVE-2026-46235         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46235
  │ ✘✔✘✘✘ CVE-2026-46236         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46236
  │ ✘✔✘✘✘ CVE-2026-46245         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-46245
  │ ✘✔✘✘✘ CVE-2026-46247         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46247
  │ ✘✔✘✘✘ CVE-2026-46249         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46249
  │ ✘✔✘✘✘ CVE-2026-46252         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46252
  │ ✘✔✘✘✘ CVE-2026-46254         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-46254
  │ ✘✔✘✘✘ CVE-2026-46291         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46291
  │ ✘✔✘✘✘ CVE-2026-46292         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46292
  │ ✘✔✘✘✘ CVE-2026-46302         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46302
  │ ✘✔✘✘✘ CVE-2026-46312         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-46312
  │ ✘✔✘✘✘ CVE-2026-52913         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52913
  │ ✘✔✘✘✘ CVE-2026-52916         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52916
  │ ✘✔✘✘✘ CVE-2026-52921         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52921
  │ ✘✔✘✘✘ CVE-2026-52925         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52925
  │ ✘✔✘✘✘ CVE-2026-52926         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52926
  │ ✘✔✘✘✘ CVE-2026-52930         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52930
  │ ✘✔✘✘✘ CVE-2026-52936         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52936
  │ ✘✔✘✘✘ CVE-2026-52937         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52937
  │ ✘✔✘✘✘ CVE-2026-52939         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52939
  │ ✘✔✘✘✘ CVE-2026-52948         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52948
  │ ✘✔✘✘✘ CVE-2026-52963         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-52963
  │ ✘✔✘✘✘ CVE-2026-52970         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52970
  │ ✘✔✘✘✘ CVE-2026-52972         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52972
  │ ✘✔✘✘✘ CVE-2026-52984         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52984
  │ ✘✔✘✘✘ CVE-2026-52985         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52985
  │ ✘✔✘✘✘ CVE-2026-52995         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-52995
  │ ✘✔✘✘✘ CVE-2026-53001         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53001
  │ ✘✔✘✘✘ CVE-2026-53012         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53012
  │ ✘✔✘✘✘ CVE-2026-53015         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53015
  │ ✘✔✘✘✘ CVE-2026-53017         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53017
  │ ✘✔✘✘✘ CVE-2026-53018         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53018
  │ ✘✔✘✘✘ CVE-2026-53021         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53021
  │ ✘✔✘✘✘ CVE-2026-53037         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53037
  │ ✘✔✘✘✘ CVE-2026-53039         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53039
  │ ✘✔✘✘✘ CVE-2026-53047         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53047
  │ ✘✔✘✘✘ CVE-2026-53060         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53060
  │ ✘✔✘✘✘ CVE-2026-53061         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53061
  │ ✘✔✘✘✘ CVE-2026-53063         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53063
  │ ✘✔✘✘✘ CVE-2026-53064         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53064
  │ ✘✔✘✘✘ CVE-2026-53065         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53065
  │ ✘✔✘✘✘ CVE-2026-53066         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53066
  │ ✘✔✘✘✘ CVE-2026-53080         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53080
  │ ✘✔✘✘✘ CVE-2026-53082         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53082
  │ ✘✔✘✘✘ CVE-2026-53093         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53093
  │ ✘✔✘✘✘ CVE-2026-53111         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53111
  │ ✘✔✘✘✘ CVE-2026-53128         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53128
  │ ✘✔✘✘✘ CVE-2026-53134         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53134
  │ ✘✔✘✘✘ CVE-2026-53135         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53135
  │ ✘✔✘✘✘ CVE-2026-53139         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53139
  │ ✘✔✘✘✘ CVE-2026-53150         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53150
  │ ✘✔✘✘✘ CVE-2026-53158         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53158
  │ ✘✔✘✘✘ CVE-2026-53167         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53167
  │ ✘✔✘✘✘ CVE-2026-53168         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53168
  │ ✘✔✘✘✘ CVE-2026-53177         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53177
  │ ✘✔✘✘✘ CVE-2026-53181         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53181
  │ ✘✔✘✘✘ CVE-2026-53196         MEDIUM       6.8   0.3%   ·  ↳ S:UBUNTU-CVE-2026-53196
  │ ✘✔✘✘✘ CVE-2026-53208         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53208
  │ ✘✔✘✘✘ CVE-2026-53213         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53213
  │ ✘✔✘✘✘ CVE-2026-53218         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53218
  │ ✘✔✘✘✘ CVE-2026-53219         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53219
  │ ✘✔✘✘✘ CVE-2026-53220         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53220
  │ ✘✔✘✘✘ CVE-2026-53227         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53227
  │ ✘✔✘✘✘ CVE-2026-53236         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53236
  │ ✘✔✘✘✘ CVE-2026-53237         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53237
  │ ✘✔✘✘✘ CVE-2026-53238         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53238
  │ ✘✔✘✘✘ CVE-2026-53245         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53245
  │ ✘✔✘✘✘ CVE-2026-53249         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53249
  │ ✘✔✘✘✘ CVE-2026-53263         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53263
  │ ✘✔✘✘✘ CVE-2026-53269         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53269
  │ ✘✔✘✘✘ CVE-2026-53287         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53287
  │ ✘✔✘✘✘ CVE-2026-53292         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53292
  │ ✘✔✘✘✘ CVE-2026-53295         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53295
  │ ✘✔✘✘✘ CVE-2026-53304         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53304
  │ ✘✔✘✘✘ CVE-2026-53306         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53306
  │ ✘✔✘✘✘ CVE-2026-53314         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53314
  │ ✘✔✘✘✘ CVE-2026-53320         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53320
  │ ✘✔✘✘✘ CVE-2026-53325         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53325
  │ ✘✔✘✘✘ CVE-2026-53332         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53332
  │ ✘✔✘✘✘ CVE-2026-53337         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53337
  │ ✘✔✘✘✘ CVE-2026-53349         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53349
  │ ✘✔✘✘✘ CVE-2026-53352         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53352
  │ ✘✔✘✘✘ CVE-2026-53353         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53353
  │ ✘✔✘✘✘ CVE-2026-53376         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53376
  │ ✘✔✘✘✘ CVE-2026-53379         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53379
  │ ✘✔✘✘✘ CVE-2026-53385         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53385
  │ ✘✔✘✘✘ CVE-2026-53403         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-53403
  │ ✘✔✘✘✘ CVE-2026-63798         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63798
  │ ✘✔✘✘✘ CVE-2026-63868         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63868
  │ ✘✔✘✘✘ CVE-2026-63897         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63897
  │ ✘✔✘✘✘ CVE-2026-63900         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63900
  │ ✘✔✘✘✘ CVE-2026-63908         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63908
  │ ✘✔✘✘✘ CVE-2026-63933         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63933
  │ ✘✔✘✘✘ CVE-2026-63948         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63948
  │ ✘✔✘✘✘ CVE-2026-63958         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63958
  │ ✘✔✘✘✘ CVE-2026-63960         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63960
  │ ✘✔✘✘✘ CVE-2026-63961         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63961
  │ ✘✔✘✘✘ CVE-2026-63962         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63962
  │ ✘✔✘✘✘ CVE-2026-63963         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63963
  │ ✘✔✘✘✘ CVE-2026-63964         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63964
  │ ✘✔✘✘✘ CVE-2026-63990         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63990
  │ ✘✔✘✘✘ CVE-2026-63991         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-63991
  │ ✘✔✘✘✘ CVE-2026-64012         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64012
  │ ✘✔✘✘✘ CVE-2026-64090         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64090
  │ ✘✔✘✘✘ CVE-2026-64094         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64094
  │ ✘✔✘✘✘ CVE-2026-64144         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64144
  │ ✘✔✘✘✘ CVE-2026-64164         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64164
  │ ✘✔✘✘✘ CVE-2026-64165         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64165
  │ ✘✔✘✘✘ CVE-2026-64168         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64168
  │ ✘✔✘✘✘ CVE-2026-64170         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64170
  │ ✘✔✘✘✘ CVE-2026-64173         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64173
  │ ✘✔✘✘✘ CVE-2026-64174         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64174
  │ ✘✔✘✘✘ CVE-2026-64177         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64177
  │ ✘✔✘✘✘ CVE-2026-64185         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64185
  │ ✘✔✘✘✘ CVE-2026-64187         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64187
  │ ✘✔✘✘✘ CVE-2026-64190         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64190
  │ ✘✔✘✘✘ CVE-2026-64213         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64213
  │ ✘✔✘✘✘ CVE-2026-64234         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64234
  │ ✘✔✘✘✘ CVE-2026-64275         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64275
  │ ✘✔✘✘✘ CVE-2026-64306         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64306
  │ ✘✔✘✘✘ CVE-2026-64316         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64316
  │ ✘✔✘✘✘ CVE-2026-64331         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64331
  │ ✘✔✘✘✘ CVE-2026-64332         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64332
  │ ✘✔✘✘✘ CVE-2026-64334         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64334
  │ ✘✔✘✘✘ CVE-2026-64335         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64335
  │ ✘✔✘✘✘ CVE-2026-64337         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64337
  │ ✘✔✘✘✘ CVE-2026-64338         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64338
  │ ✘✔✘✘✘ CVE-2026-64345         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64345
  │ ✘✔✘✘✘ CVE-2026-64347         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64347
  │ ✘✔✘✘✘ CVE-2026-64351         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64351
  │ ✘✔✘✘✘ CVE-2026-64359         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64359
  │ ✘✔✘✘✘ CVE-2026-64370         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64370
  │ ✘✔✘✘✘ CVE-2026-64371         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64371
  │ ✘✔✘✘✘ CVE-2026-64373         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64373
  │ ✘✔✘✘✘ CVE-2026-64405         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64405
  │ ✘✔✘✘✘ CVE-2026-64429         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-64429
  │ ✘✔✘✘✘ CVE-2026-98078         MEDIUM       4.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98078
  │ ✘✔✘✘✘ CVE-2026-98080         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98080
  │ ✘✔✘✘✘ CVE-2026-98091         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98091
  │ ✘✔✘✘✘ CVE-2026-98094         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98094
  │ ✘✔✘✘✘ CVE-2026-98095         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98095
  │ ✘✔✘✘✘ CVE-2026-98097         MEDIUM       5.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-98097
  │ ✘✔✘✘✘ CVE-2026-98098         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98098
  │ ✘✔✘✘✘ CVE-2026-98099         MEDIUM       4.7   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98099
  │ ✘✔✘✘✘ CVE-2026-98123         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98123
  │ ✘✔✘✘✘ CVE-2026-98124         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98124
  │ ✘✔✘✘✘ CVE-2026-98126         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98126
  │ ✘✔✘✘✘ CVE-2026-98131         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98131
  │ ✘✔✘✘✘ CVE-2026-98142         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98142
  │ ✘✔✘✘✘ CVE-2026-98157         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98157
  │ ✘✔✘✘✘ CVE-2026-98158         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98158
  │ ✘✔✘✘✘ CVE-2026-98160         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98160
  │ ✘✔✘✘✘ CVE-2026-98161         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98161
  │ ✘✔✘✘✘ CVE-2020-35501         LOW          3.6   0.2%   ·  ↳ S:UBUNTU-CVE-2020-35501
  │ ✘✔✘✘✘ CVE-2023-32251         LOW          3.7   0.5%   ·  ↳ S:UBUNTU-CVE-2023-32251
  │ ✘✔✘✘✘ CVE-2024-39286         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2024-39286
  │ ✘✔✘✘✘ CVE-2024-42155         LOW          1.9   0.3%   ·  ↳ S:UBUNTU-CVE-2024-42155
  │ ✘✔✘✘✘ CVE-2024-50057         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2024-50057
  │ ✘✔✘✘✘ CVE-2025-54505         LOW          2.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-54505
  │ ✘✔✘✘✘ CVE-2026-22978         LOW          3.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-22978
  │ ✘✔✘✘✘ CVE-2021-47488         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2021-47488
  │ ✘✔✘✘✘ CVE-2022-2209          ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-2209
  │ ✘✔✘✘✘ CVE-2022-48700         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-48700
  │ ✘✔✘✘✘ CVE-2022-49267         ?            0.0   0.0%   ·  ↳ S:UBUNTU-CVE-2022-49267,USN-8098-1
  │ ✘✔✘✘✘ CVE-2022-49933         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-49933
  │ ✘✔✘✘✘ CVE-2022-4994          ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-4994
  │ ✘✔✘✘✘ CVE-2022-49941         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-49941
  │ ✘✔✘✘✘ CVE-2022-50018         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-50018
  │ ✘✔✘✘✘ CVE-2022-50081         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-50081
  │ ✘✔✘✘✘ CVE-2022-50128         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-50128
  │ ✘✔✘✘✘ CVE-2022-50150         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-50150
  │ ✘✔✘✘✘ CVE-2022-50180         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-50180
  │ ✘✔✘✘✘ CVE-2022-50216         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-50216
  │ ✘✔✘✘✘ CVE-2022-50290         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-50290
  │ ✘✔✘✘✘ CVE-2022-50338         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-50338
  │ ✘✔✘✘✘ CVE-2022-50345         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-50345
  │ ✘✔✘✘✘ CVE-2022-50397         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-50397
  │ ✘✔✘✘✘ CVE-2022-50455         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-50455
  │ ✘✔✘✘✘ CVE-2022-50487         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-50487
  │ ✘✔✘✘✘ CVE-2022-50502         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2022-50502
  │ ✘✔✘✘✘ CVE-2022-50556         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50556
  │ ✘✔✘✘✘ CVE-2022-50560         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50560
  │ ✘✔✘✘✘ CVE-2022-50562         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50562
  │ ✘✔✘✘✘ CVE-2022-50580         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50580
  │ ✘✔✘✘✘ CVE-2022-50582         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50582
  │ ✘✔✘✘✘ CVE-2022-50614         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50614
  │ ✘✔✘✘✘ CVE-2022-50615         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50615
  │ ✘✔✘✘✘ CVE-2022-50616         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50616
  │ ✘✔✘✘✘ CVE-2022-50622         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50622
  │ ✘✔✘✘✘ CVE-2022-50699         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50699
  │ ✘✔✘✘✘ CVE-2022-50704         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50704
  │ ✘✔✘✘✘ CVE-2022-50708         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50708
  │ ✘✔✘✘✘ CVE-2022-50710         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50710
  │ ✘✔✘✘✘ CVE-2022-50720         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50720
  │ ✘✔✘✘✘ CVE-2022-50735         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50735
  │ ✘✔✘✘✘ CVE-2022-50739         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50739
  │ ✘✔✘✘✘ CVE-2022-50741         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50741
  │ ✘✔✘✘✘ CVE-2022-50744         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50744
  │ ✘✔✘✘✘ CVE-2022-50764         ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2022-50764
  │ ✘✔✘✘✘ CVE-2022-50766         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50766
  │ ✘✔✘✘✘ CVE-2022-50768         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50768
  │ ✘✔✘✘✘ CVE-2022-50772         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50772
  │ ✘✔✘✘✘ CVE-2022-50774         ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2022-50774
  │ ✘✔✘✘✘ CVE-2022-50812         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50812
  │ ✘✔✘✘✘ CVE-2022-50814         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50814
  │ ✘✔✘✘✘ CVE-2022-50815         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50815
  │ ✘✔✘✘✘ CVE-2022-50817         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50817
  │ ✘✔✘✘✘ CVE-2022-50819         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50819
  │ ✘✔✘✘✘ CVE-2022-50835         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50835
  │ ✘✔✘✘✘ CVE-2022-50839         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50839
  │ ✘✔✘✘✘ CVE-2022-50842         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50842
  │ ✘✔✘✘✘ CVE-2022-50844         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50844
  │ ✘✔✘✘✘ CVE-2022-50864         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50864
  │ ✘✔✘✘✘ CVE-2022-50878         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50878
  │ ✘✔✘✘✘ CVE-2022-50881         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2022-50881
  │ ✘✔✘✘✘ CVE-2023-4010          ?            0.0   0.6%   ·  ↳ S:UBUNTU-CVE-2023-4010
  │ ✘✔✘✘✘ CVE-2023-53001         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2023-53001
  │ ✘✔✘✘✘ CVE-2023-53293         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2023-53293
  │ ✘✔✘✘✘ CVE-2023-53693         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53693
  │ ✘✔✘✘✘ CVE-2023-53696         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53696
  │ ✘✔✘✘✘ CVE-2023-53699         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53699
  │ ✘✔✘✘✘ CVE-2023-53708         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53708
  │ ✘✔✘✘✘ CVE-2023-53709         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53709
  │ ✘✔✘✘✘ CVE-2023-53712         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53712
  │ ✘✔✘✘✘ CVE-2023-53732         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53732
  │ ✘✔✘✘✘ CVE-2023-53744         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53744
  │ ✘✔✘✘✘ CVE-2023-53749         ?            0.0   0.0%   ·  ↳ S:UBUNTU-CVE-2023-53749
  │ ✘✔✘✘✘ CVE-2023-53756         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53756
  │ ✘✔✘✘✘ CVE-2023-53765         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53765
  │ ✘✔✘✘✘ CVE-2023-53780         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53780
  │ ✘✔✘✘✘ CVE-2023-53799         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53799
  │ ✘✔✘✘✘ CVE-2023-53801         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53801
  │ ✘✔✘✘✘ CVE-2023-53815         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53815
  │ ✘✔✘✘✘ CVE-2023-53834         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53834
  │ ✘✔✘✘✘ CVE-2023-53840         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53840
  │ ✘✔✘✘✘ CVE-2023-53849         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53849
  │ ✘✔✘✘✘ CVE-2023-53850         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53850
  │ ✘✔✘✘✘ CVE-2023-53856         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53856
  │ ✘✔✘✘✘ CVE-2023-53859         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53859
  │ ✘✔✘✘✘ CVE-2023-53992         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-53992
  │ ✘✔✘✘✘ CVE-2023-54001         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54001
  │ ✘✔✘✘✘ CVE-2023-54013         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54013
  │ ✘✔✘✘✘ CVE-2023-54023         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54023
  │ ✘✔✘✘✘ CVE-2023-54028         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54028
  │ ✘✔✘✘✘ CVE-2023-54036         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54036
  │ ✘✔✘✘✘ CVE-2023-54047         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54047
  │ ✘✔✘✘✘ CVE-2023-54066         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54066
  │ ✘✔✘✘✘ CVE-2023-54081         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54081
  │ ✘✔✘✘✘ CVE-2023-54086         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54086
  │ ✘✔✘✘✘ CVE-2023-54105         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54105
  │ ✘✔✘✘✘ CVE-2023-54118         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54118
  │ ✘✔✘✘✘ CVE-2023-54145         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54145
  │ ✘✔✘✘✘ CVE-2023-54150         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54150
  │ ✘✔✘✘✘ CVE-2023-54180         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54180
  │ ✘✔✘✘✘ CVE-2023-54185         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54185
  │ ✘✔✘✘✘ CVE-2023-54194         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54194
  │ ✘✔✘✘✘ CVE-2023-54196         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54196
  │ ✘✔✘✘✘ CVE-2023-54229         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54229
  │ ✘✔✘✘✘ CVE-2023-54245         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54245
  │ ✘✔✘✘✘ CVE-2023-54246         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54246
  │ ✘✔✘✘✘ CVE-2023-54251         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54251
  │ ✘✔✘✘✘ CVE-2023-54267         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54267
  │ ✘✔✘✘✘ CVE-2023-54271         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54271
  │ ✘✔✘✘✘ CVE-2023-54272         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54272
  │ ✘✔✘✘✘ CVE-2023-54274         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54274
  │ ✘✔✘✘✘ CVE-2023-54281         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54281
  │ ✘✔✘✘✘ CVE-2023-54287         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54287
  │ ✘✔✘✘✘ CVE-2023-54295         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54295
  │ ✘✔✘✘✘ CVE-2023-54322         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54322
  │ ✘✔✘✘✘ CVE-2023-54324         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2023-54324
  │ ✘✔✘✘✘ CVE-2024-26720         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2024-26720
  │ ✘✔✘✘✘ CVE-2024-35923         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2024-35923
  │ ✘✔✘✘✘ CVE-2024-35928         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2024-35928
  │ ✘✔✘✘✘ CVE-2024-36022         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2024-36022
  │ ✘✔✘✘✘ CVE-2024-36885         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2024-36885
  │ ✘✔✘✘✘ CVE-2024-36907         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2024-36907
  │ ✘✔✘✘✘ CVE-2024-44955         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2024-44955
  │ ✘✔✘✘✘ CVE-2024-56786         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2024-56786
  │ ✘✔✘✘✘ CVE-2025-37753         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2025-37753
  │ ✘✔✘✘✘ CVE-2025-37782         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2025-37782
  │ ✘✔✘✘✘ CVE-2025-37804         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2025-37804
  │ ✘✔✘✘✘ CVE-2025-37976         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2025-37976
  │ ✘✔✘✘✘ CVE-2025-38611         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2025-38611
  │ ✘✔✘✘✘ CVE-2025-39751         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2025-39751
  │ ✘✔✘✘✘ CVE-2025-39898         ?            0.0      -   ·  ↳ S:UBUNTU-CVE-2025-39898
  │ ✘✔✘✘✘ CVE-2025-39995         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39995
  │ ✘✔✘✘✘ CVE-2025-39996         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-39996
  │ ✘✔✘✘✘ CVE-2025-40001         ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2025-40001
  │ ✘✔✘✘✘ CVE-2025-40003         ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2025-40003
  │ ✘✔✘✘✘ CVE-2025-40011         ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2025-40011
  │ ✘✔✘✘✘ CVE-2025-40019         ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2025-40019,USN-7990-1
  │ ✘✔✘✘✘ CVE-2025-40020         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40020
  │ ✘✔✘✘✘ CVE-2025-40021         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40021
  │ ✘✔✘✘✘ CVE-2025-40030         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40030
  │ ✘✔✘✘✘ CVE-2025-40035         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40035
  │ ✘✔✘✘✘ CVE-2025-40036         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40036
  │ ✘✔✘✘✘ CVE-2025-40042         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40042
  │ ✘✔✘✘✘ CVE-2025-40049         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40049
  │ ✘✔✘✘✘ CVE-2025-40055         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40055
  │ ✘✔✘✘✘ CVE-2025-40070         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40070
  │ ✘✔✘✘✘ CVE-2025-40078         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40078
  │ ✘✔✘✘✘ CVE-2025-40080         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40080
  │ ✘✔✘✘✘ CVE-2025-40083         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40083
  │ ✘✔✘✘✘ CVE-2025-40100         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40100
  │ ✘✔✘✘✘ CVE-2025-40102         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40102
  │ ✘✔✘✘✘ CVE-2025-40103         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40103
  │ ✘✔✘✘✘ CVE-2025-40106         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40106
  │ ✘✔✘✘✘ CVE-2025-40107         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40107
  │ ✘✔✘✘✘ CVE-2025-40110         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40110
  │ ✘✔✘✘✘ CVE-2025-40115         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40115
  │ ✘✔✘✘✘ CVE-2025-40116         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40116
  │ ✘✔✘✘✘ CVE-2025-40121         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40121
  │ ✘✔✘✘✘ CVE-2025-40125         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40125
  │ ✘✔✘✘✘ CVE-2025-40126         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40126
  │ ✘✔✘✘✘ CVE-2025-40134         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40134
  │ ✘✔✘✘✘ CVE-2025-40137         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40137
  │ ✘✔✘✘✘ CVE-2025-40146         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40146
  │ ✘✔✘✘✘ CVE-2025-40153         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40153
  │ ✘✔✘✘✘ CVE-2025-40154         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40154
  │ ✘✔✘✘✘ CVE-2025-40160         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40160
  │ ✘✔✘✘✘ CVE-2025-40178         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40178
  │ ✘✔✘✘✘ CVE-2025-40180         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40180
  │ ✘✔✘✘✘ CVE-2025-40188         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40188
  │ ✘✔✘✘✘ CVE-2025-40193         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40193
  │ ✘✔✘✘✘ CVE-2025-40194         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40194
  │ ✘✔✘✘✘ CVE-2025-40196         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40196
  │ ✘✔✘✘✘ CVE-2025-40200         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40200
  │ ✘✔✘✘✘ CVE-2025-40211         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40211
  │ ✘✔✘✘✘ CVE-2025-40219         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40219
  │ ✘✔✘✘✘ CVE-2025-40220         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40220
  │ ✘✔✘✘✘ CVE-2025-40247         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40247
  │ ✘✔✘✘✘ CVE-2025-40254         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40254
  │ ✘✔✘✘✘ CVE-2025-40259         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40259
  │ ✘✔✘✘✘ CVE-2025-40263         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40263
  │ ✘✔✘✘✘ CVE-2025-40264         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40264
  │ ✘✔✘✘✘ CVE-2025-40275         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40275
  │ ✘✔✘✘✘ CVE-2025-40278         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40278
  │ ✘✔✘✘✘ CVE-2025-40279         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40279
  │ ✘✔✘✘✘ CVE-2025-40281         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40281
  │ ✘✔✘✘✘ CVE-2025-40288         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40288
  │ ✘✔✘✘✘ CVE-2025-40289         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40289
  │ ✘✔✘✘✘ CVE-2025-40308         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40308
  │ ✘✔✘✘✘ CVE-2025-40312         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40312
  │ ✘✔✘✘✘ CVE-2025-40313         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40313
  │ ✘✔✘✘✘ CVE-2025-40314         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40314
  │ ✘✔✘✘✘ CVE-2025-40315         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40315
  │ ✘✔✘✘✘ CVE-2025-40321         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40321
  │ ✘✔✘✘✘ CVE-2025-40333         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40333
  │ ✘✔✘✘✘ CVE-2025-40339         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40339
  │ ✘✔✘✘✘ CVE-2025-40341         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40341
  │ ✘✔✘✘✘ CVE-2025-40345         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40345
  │ ✘✔✘✘✘ CVE-2025-40351         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40351
  │ ✘✔✘✘✘ CVE-2025-40355         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40355
  │ ✘✔✘✘✘ CVE-2025-40363         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-40363
  │ ✘✔✘✘✘ CVE-2025-68173         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68173
  │ ✘✔✘✘✘ CVE-2025-68176         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68176
  │ ✘✔✘✘✘ CVE-2025-68177         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68177
  │ ✘✔✘✘✘ CVE-2025-68185         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68185
  │ ✘✔✘✘✘ CVE-2025-68188         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68188
  │ ✘✔✘✘✘ CVE-2025-68190         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68190
  │ ✘✔✘✘✘ CVE-2025-68191         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68191
  │ ✘✔✘✘✘ CVE-2025-68194         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68194
  │ ✘✔✘✘✘ CVE-2025-68204         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68204
  │ ✘✔✘✘✘ CVE-2025-68217         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68217
  │ ✘✔✘✘✘ CVE-2025-68220         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68220
  │ ✘✔✘✘✘ CVE-2025-68227         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68227
  │ ✘✔✘✘✘ CVE-2025-68229         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68229
  │ ✘✔✘✘✘ CVE-2025-68231         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68231
  │ ✘✔✘✘✘ CVE-2025-68239         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68239
  │ ✘✔✘✘✘ CVE-2025-68245         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68245
  │ ✘✔✘✘✘ CVE-2025-68258         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68258
  │ ✘✔✘✘✘ CVE-2025-68264         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68264
  │ ✘✔✘✘✘ CVE-2025-68266         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68266
  │ ✘✔✘✘✘ CVE-2025-68282         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68282
  │ ✘✔✘✘✘ CVE-2025-68287         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68287
  │ ✘✔✘✘✘ CVE-2025-68288         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68288
  │ ✘✔✘✘✘ CVE-2025-68289         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68289
  │ ✘✔✘✘✘ CVE-2025-68295         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68295
  │ ✘✔✘✘✘ CVE-2025-68296         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68296
  │ ✘✔✘✘✘ CVE-2025-68307         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68307
  │ ✘✔✘✘✘ CVE-2025-68308         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68308
  │ ✘✔✘✘✘ CVE-2025-68312         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68312
  │ ✘✔✘✘✘ CVE-2025-68322         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68322
  │ ✘✔✘✘✘ CVE-2025-68324         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68324
  │ ✘✔✘✘✘ CVE-2025-68327         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68327
  │ ✘✔✘✘✘ CVE-2025-68328         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68328
  │ ✘✔✘✘✘ CVE-2025-68330         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68330
  │ ✘✔✘✘✘ CVE-2025-68332         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68332
  │ ✘✔✘✘✘ CVE-2025-68335         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68335
  │ ✘✔✘✘✘ CVE-2025-68339         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68339
  │ ✘✔✘✘✘ CVE-2025-68342         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68342
  │ ✘✔✘✘✘ CVE-2025-68343         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68343
  │ ✘✔✘✘✘ CVE-2025-68344         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68344
  │ ✘✔✘✘✘ CVE-2025-68346         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68346
  │ ✘✔✘✘✘ CVE-2025-68354         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68354
  │ ✘✔✘✘✘ CVE-2025-68362         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68362
  │ ✘✔✘✘✘ CVE-2025-68364         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68364
  │ ✘✔✘✘✘ CVE-2025-68366         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68366
  │ ✘✔✘✘✘ CVE-2025-68367         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68367
  │ ✘✔✘✘✘ CVE-2025-68372         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68372
  │ ✘✔✘✘✘ CVE-2025-68733         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68733
  │ ✘✔✘✘✘ CVE-2025-68734         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68734
  │ ✘✔✘✘✘ CVE-2025-68740         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68740
  │ ✘✔✘✘✘ CVE-2025-68742         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68742
  │ ✘✔✘✘✘ CVE-2025-68750         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68750
  │ ✘✔✘✘✘ CVE-2025-68757         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68757
  │ ✘✔✘✘✘ CVE-2025-68759         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68759
  │ ✘✔✘✘✘ CVE-2025-68767         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68767
  │ ✘✔✘✘✘ CVE-2025-68768         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68768
  │ ✘✔✘✘✘ CVE-2025-68769         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68769
  │ ✘✔✘✘✘ CVE-2025-68771         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68771
  │ ✘✔✘✘✘ CVE-2025-68776         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68776
  │ ✘✔✘✘✘ CVE-2025-68777         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68777
  │ ✘✔✘✘✘ CVE-2025-68778         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68778
  │ ✘✔✘✘✘ CVE-2025-68780         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68780
  │ ✘✔✘✘✘ CVE-2025-68781         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68781
  │ ✘✔✘✘✘ CVE-2025-68783         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68783
  │ ✘✔✘✘✘ CVE-2025-68787         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68787
  │ ✘✔✘✘✘ CVE-2025-68788         ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2025-68788
  │ ✘✔✘✘✘ CVE-2025-68796         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68796
  │ ✘✔✘✘✘ CVE-2025-68797         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68797
  │ ✘✔✘✘✘ CVE-2025-68804         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68804
  │ ✘✔✘✘✘ CVE-2025-68813         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68813
  │ ✘✔✘✘✘ CVE-2025-68816         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-68816
  │ ✘✔✘✘✘ CVE-2025-71064         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71064
  │ ✘✔✘✘✘ CVE-2025-71069         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71069
  │ ✘✔✘✘✘ CVE-2025-71193         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71193
  │ ✘✔✘✘✘ CVE-2025-71194         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71194
  │ ✘✔✘✘✘ CVE-2025-71196         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71196
  │ ✘✔✘✘✘ CVE-2025-71199         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71199
  │ ✘✔✘✘✘ CVE-2025-71224         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2025-71224
  │ ✘✔✘✘✘ CVE-2026-23031         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23031
  │ ✘✔✘✘✘ CVE-2026-23033         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23033
  │ ✘✔✘✘✘ CVE-2026-23038         ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-23038
  │ ✘✔✘✘✘ CVE-2026-23047         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23047
  │ ✘✔✘✘✘ CVE-2026-23049         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23049
  │ ✘✔✘✘✘ CVE-2026-23050         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23050
  │ ✘✔✘✘✘ CVE-2026-23054         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23054
  │ ✘✔✘✘✘ CVE-2026-23058         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23058
  │ ✘✔✘✘✘ CVE-2026-23176         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-23176
  │ ✘✔✘✘✘ CVE-2026-63810         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63810
  │ ✘✔✘✘✘ CVE-2026-63826         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63826
  │ ✘✔✘✘✘ CVE-2026-63834         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63834
  │ ✘✔✘✘✘ CVE-2026-63835         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63835
  │ ✘✔✘✘✘ CVE-2026-63836         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63836
  │ ✘✔✘✘✘ CVE-2026-63890         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63890
  │ ✘✔✘✘✘ CVE-2026-63891         ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-63891
  │ ✘✔✘✘✘ CVE-2026-63892         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63892
  │ ✘✔✘✘✘ CVE-2026-63895         ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-63895
  │ ✘✔✘✘✘ CVE-2026-63983         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-63983
  │ ✘✔✘✘✘ CVE-2026-64455         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64455
  │ ✘✔✘✘✘ CVE-2026-64461         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64461
  │ ✘✔✘✘✘ CVE-2026-64465         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64465
  │ ✘✔✘✘✘ CVE-2026-64470         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64470
  │ ✘✔✘✘✘ CVE-2026-64471         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64471
  │ ✘✔✘✘✘ CVE-2026-64483         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64483
  │ ✘✔✘✘✘ CVE-2026-64484         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64484
  │ ✘✔✘✘✘ CVE-2026-64487         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64487
  │ ✘✔✘✘✘ CVE-2026-64488         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64488
  │ ✘✔✘✘✘ CVE-2026-64495         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64495
  │ ✘✔✘✘✘ CVE-2026-64500         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64500
  │ ✘✔✘✘✘ CVE-2026-64503         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64503
  │ ✘✔✘✘✘ CVE-2026-64504         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64504
  │ ✘✔✘✘✘ CVE-2026-64505         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64505
  │ ✘✔✘✘✘ CVE-2026-64513         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64513
  │ ✘✔✘✘✘ CVE-2026-64514         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64514
  │ ✘✔✘✘✘ CVE-2026-64528         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64528
  │ ✘✔✘✘✘ CVE-2026-64538         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64538
  │ ✘✔✘✘✘ CVE-2026-64544         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64544
  │ ✘✔✘✘✘ CVE-2026-64549         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64549
  │ ✘✔✘✘✘ CVE-2026-64553         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64553
  │ ✘✔✘✘✘ CVE-2026-64565         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64565
  │ ✘✔✘✘✘ CVE-2026-64569         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64569
  │ ✘✔✘✘✘ CVE-2026-64571         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64571
  │ ✘✔✘✘✘ CVE-2026-64579         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64579
  │ ✘✔✘✘✘ CVE-2026-64593         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64593
  │ ✘✔✘✘✘ CVE-2026-64594         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64594
  │ ✘✔✘✘✘ CVE-2026-64602         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64602
  │ ✘✔✘✘✘ CVE-2026-64604         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-64604
  │ ✘✔✘✘✘ CVE-2026-68081         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68081
  │ ✘✔✘✘✘ CVE-2026-68084         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68084
  │ ✘✔✘✘✘ CVE-2026-68086         ?            0.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-68086
  │ ✘✔✘✘✘ CVE-2026-68088         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68088
  │ ✘✔✘✘✘ CVE-2026-68090         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68090
  │ ✘✔✘✘✘ CVE-2026-68093         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68093
  │ ✘✔✘✘✘ CVE-2026-68105         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68105
  │ ✘✔✘✘✘ CVE-2026-68109         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68109
  │ ✘✔✘✘✘ CVE-2026-68110         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68110
  │ ✘✔✘✘✘ CVE-2026-68111         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68111
  │ ✘✔✘✘✘ CVE-2026-68112         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68112
  │ ✘✔✘✘✘ CVE-2026-68113         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68113
  │ ✘✔✘✘✘ CVE-2026-68114         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68114
  │ ✘✔✘✘✘ CVE-2026-68115         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68115
  │ ✘✔✘✘✘ CVE-2026-68132         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68132
  │ ✘✔✘✘✘ CVE-2026-68135         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68135
  │ ✘✔✘✘✘ CVE-2026-68146         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68146
  │ ✘✔✘✘✘ CVE-2026-68151         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68151
  │ ✘✔✘✘✘ CVE-2026-68175         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68175
  │ ✘✔✘✘✘ CVE-2026-68176         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68176
  │ ✘✔✘✘✘ CVE-2026-68182         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68182
  │ ✘✔✘✘✘ CVE-2026-68183         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68183
  │ ✘✔✘✘✘ CVE-2026-68184         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68184
  │ ✘✔✘✘✘ CVE-2026-68187         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68187
  │ ✘✔✘✘✘ CVE-2026-68188         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68188
  │ ✘✔✘✘✘ CVE-2026-68190         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68190
  │ ✘✔✘✘✘ CVE-2026-68197         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68197
  │ ✘✔✘✘✘ CVE-2026-68203         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68203
  │ ✘✔✘✘✘ CVE-2026-68205         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68205
  │ ✘✔✘✘✘ CVE-2026-68212         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68212
  │ ✘✔✘✘✘ CVE-2026-68214         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68214
  │ ✘✔✘✘✘ CVE-2026-68215         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68215
  │ ✘✔✘✘✘ CVE-2026-68217         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68217
  │ ✘✔✘✘✘ CVE-2026-68218         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68218
  │ ✘✔✘✘✘ CVE-2026-68223         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68223
  │ ✘✔✘✘✘ CVE-2026-68226         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68226
  │ ✘✔✘✘✘ CVE-2026-68227         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68227
  │ ✘✔✘✘✘ CVE-2026-68231         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68231
  │ ✘✔✘✘✘ CVE-2026-68233         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68233
  │ ✘✔✘✘✘ CVE-2026-68234         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68234
  │ ✘✔✘✘✘ CVE-2026-68235         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68235
  │ ✘✔✘✘✘ CVE-2026-68238         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68238
  │ ✘✔✘✘✘ CVE-2026-68246         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68246
  │ ✘✔✘✘✘ CVE-2026-68249         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68249
  │ ✘✔✘✘✘ CVE-2026-68250         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68250
  │ ✘✔✘✘✘ CVE-2026-68251         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68251
  │ ✘✔✘✘✘ CVE-2026-68252         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68252
  │ ✘✔✘✘✘ CVE-2026-68259         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68259
  │ ✘✔✘✘✘ CVE-2026-68277         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68277
  │ ✘✔✘✘✘ CVE-2026-68278         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68278
  │ ✘✔✘✘✘ CVE-2026-68279         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68279
  │ ✘✔✘✘✘ CVE-2026-68280         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68280
  │ ✘✔✘✘✘ CVE-2026-68286         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68286
  │ ✘✔✘✘✘ CVE-2026-68288         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68288
  │ ✘✔✘✘✘ CVE-2026-68289         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68289
  │ ✘✔✘✘✘ CVE-2026-68303         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68303
  │ ✘✔✘✘✘ CVE-2026-68304         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68304
  │ ✘✔✘✘✘ CVE-2026-68313         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68313
  │ ✘✔✘✘✘ CVE-2026-68322         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68322
  │ ✘✔✘✘✘ CVE-2026-68325         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68325
  │ ✘✔✘✘✘ CVE-2026-68327         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68327
  │ ✘✔✘✘✘ CVE-2026-68328         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68328
  │ ✘✔✘✘✘ CVE-2026-68349         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68349
  │ ✘✔✘✘✘ CVE-2026-68350         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68350
  │ ✘✔✘✘✘ CVE-2026-68351         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68351
  │ ✘✔✘✘✘ CVE-2026-68357         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68357
  │ ✘✔✘✘✘ CVE-2026-68363         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68363
  │ ✘✔✘✘✘ CVE-2026-68365         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68365
  │ ✘✔✘✘✘ CVE-2026-68366         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68366
  │ ✘✔✘✘✘ CVE-2026-68367         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68367
  │ ✘✔✘✘✘ CVE-2026-68368         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68368
  │ ✘✔✘✘✘ CVE-2026-68369         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68369
  │ ✘✔✘✘✘ CVE-2026-68395         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68395
  │ ✘✔✘✘✘ CVE-2026-68403         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68403
  │ ✘✔✘✘✘ CVE-2026-68405         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68405
  │ ✘✔✘✘✘ CVE-2026-68406         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68406
  │ ✘✔✘✘✘ CVE-2026-68410         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68410
  │ ✘✔✘✘✘ CVE-2026-68412         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68412
  │ ✘✔✘✘✘ CVE-2026-68413         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68413
  │ ✘✔✘✘✘ CVE-2026-68428         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68428
  │ ✘✔✘✘✘ CVE-2026-68430         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68430
  │ ✘✔✘✘✘ CVE-2026-68436         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68436
  │ ✘✔✘✘✘ CVE-2026-68441         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68441
  │ ✘✔✘✘✘ CVE-2026-68448         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68448
  │ ✘✔✘✘✘ CVE-2026-68449         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68449
  │ ✘✔✘✘✘ CVE-2026-68456         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68456
  │ ✘✔✘✘✘ CVE-2026-68459         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68459
  │ ✘✔✘✘✘ CVE-2026-68460         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68460
  │ ✘✔✘✘✘ CVE-2026-68469         ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-68469
  │ ✘✔✘✘✘ CVE-2026-68475         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68475
  │ ✘✔✘✘✘ CVE-2026-68478         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68478
  │ ✘✔✘✘✘ CVE-2026-68480         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-68480
  │ ✘✔✘✘✘ CVE-2026-72004         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72004
  │ ✘✔✘✘✘ CVE-2026-72010         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72010
  │ ✘✔✘✘✘ CVE-2026-72015         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72015
  │ ✘✔✘✘✘ CVE-2026-72017         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72017
  │ ✘✔✘✘✘ CVE-2026-72022         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72022
  │ ✘✔✘✘✘ CVE-2026-72025         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72025
  │ ✘✔✘✘✘ CVE-2026-72038         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72038
  │ ✘✔✘✘✘ CVE-2026-72039         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72039
  │ ✘✔✘✘✘ CVE-2026-72047         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72047
  │ ✘✔✘✘✘ CVE-2026-72048         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72048
  │ ✘✔✘✘✘ CVE-2026-72056         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72056
  │ ✘✔✘✘✘ CVE-2026-72062         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72062
  │ ✘✔✘✘✘ CVE-2026-72063         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72063
  │ ✘✔✘✘✘ CVE-2026-72068         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72068
  │ ✘✔✘✘✘ CVE-2026-72070         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72070
  │ ✘✔✘✘✘ CVE-2026-72073         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72073
  │ ✘✔✘✘✘ CVE-2026-72074         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72074
  │ ✘✔✘✘✘ CVE-2026-72075         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72075
  │ ✘✔✘✘✘ CVE-2026-72076         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72076
  │ ✘✔✘✘✘ CVE-2026-72077         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72077
  │ ✘✔✘✘✘ CVE-2026-72078         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72078
  │ ✘✔✘✘✘ CVE-2026-72079         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72079
  │ ✘✔✘✘✘ CVE-2026-72086         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72086
  │ ✘✔✘✘✘ CVE-2026-72087         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72087
  │ ✘✔✘✘✘ CVE-2026-72088         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72088
  │ ✘✔✘✘✘ CVE-2026-72096         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72096
  │ ✘✔✘✘✘ CVE-2026-72106         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72106
  │ ✘✔✘✘✘ CVE-2026-72117         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72117
  │ ✘✔✘✘✘ CVE-2026-72118         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72118
  │ ✘✔✘✘✘ CVE-2026-72138         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72138
  │ ✘✔✘✘✘ CVE-2026-72142         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72142
  │ ✘✔✘✘✘ CVE-2026-72147         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72147
  │ ✘✔✘✘✘ CVE-2026-72152         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72152
  │ ✘✔✘✘✘ CVE-2026-72153         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72153
  │ ✘✔✘✘✘ CVE-2026-72155         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72155
  │ ✘✔✘✘✘ CVE-2026-72159         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72159
  │ ✘✔✘✘✘ CVE-2026-72163         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72163
  │ ✘✔✘✘✘ CVE-2026-72166         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72166
  │ ✘✔✘✘✘ CVE-2026-72168         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72168
  │ ✘✔✘✘✘ CVE-2026-72179         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72179
  │ ✘✔✘✘✘ CVE-2026-72215         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72215
  │ ✘✔✘✘✘ CVE-2026-72223         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72223
  │ ✘✔✘✘✘ CVE-2026-72224         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72224
  │ ✘✔✘✘✘ CVE-2026-72228         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72228
  │ ✘✔✘✘✘ CVE-2026-72229         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72229
  │ ✘✔✘✘✘ CVE-2026-72230         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72230
  │ ✘✔✘✘✘ CVE-2026-72236         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72236
  │ ✘✔✘✘✘ CVE-2026-72238         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72238
  │ ✘✔✘✘✘ CVE-2026-72240         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72240
  │ ✘✔✘✘✘ CVE-2026-72241         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72241
  │ ✘✔✘✘✘ CVE-2026-72245         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72245
  │ ✘✔✘✘✘ CVE-2026-72256         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72256
  │ ✘✔✘✘✘ CVE-2026-72264         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72264
  │ ✘✔✘✘✘ CVE-2026-72265         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72265
  │ ✘✔✘✘✘ CVE-2026-72267         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72267
  │ ✘✔✘✘✘ CVE-2026-72268         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72268
  │ ✘✔✘✘✘ CVE-2026-72269         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72269
  │ ✘✔✘✘✘ CVE-2026-72270         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72270
  │ ✘✔✘✘✘ CVE-2026-72271         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72271
  │ ✘✔✘✘✘ CVE-2026-72272         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72272
  │ ✘✔✘✘✘ CVE-2026-72307         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72307
  │ ✘✔✘✘✘ CVE-2026-72308         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72308
  │ ✘✔✘✘✘ CVE-2026-72316         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72316
  │ ✘✔✘✘✘ CVE-2026-72321         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72321
  │ ✘✔✘✘✘ CVE-2026-72324         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72324
  │ ✘✔✘✘✘ CVE-2026-72326         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72326
  │ ✘✔✘✘✘ CVE-2026-72336         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72336
  │ ✘✔✘✘✘ CVE-2026-72337         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72337
  │ ✘✔✘✘✘ CVE-2026-72349         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72349
  │ ✘✔✘✘✘ CVE-2026-72384         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72384
  │ ✘✔✘✘✘ CVE-2026-72392         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72392
  │ ✘✔✘✘✘ CVE-2026-72396         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72396
  │ ✘✔✘✘✘ CVE-2026-72413         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72413
  │ ✘✔✘✘✘ CVE-2026-72428         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72428
  │ ✘✔✘✘✘ CVE-2026-72433         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72433
  │ ✘✔✘✘✘ CVE-2026-72441         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72441
  │ ✘✔✘✘✘ CVE-2026-72447         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72447
  │ ✘✔✘✘✘ CVE-2026-72479         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72479
  │ ✘✔✘✘✘ CVE-2026-72481         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72481
  │ ✘✔✘✘✘ CVE-2026-72484         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-72484
  │ ✘✔✘✘✘ CVE-2026-74261         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74261
  │ ✘✔✘✘✘ CVE-2026-74271         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74271
  │ ✘✔✘✘✘ CVE-2026-74276         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74276
  │ ✘✔✘✘✘ CVE-2026-74278         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74278
  │ ✘✔✘✘✘ CVE-2026-74284         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74284
  │ ✘✔✘✘✘ CVE-2026-74290         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74290
  │ ✘✔✘✘✘ CVE-2026-74291         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74291
  │ ✘✔✘✘✘ CVE-2026-74307         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74307
  │ ✘✔✘✘✘ CVE-2026-74308         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74308
  │ ✘✔✘✘✘ CVE-2026-74320         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74320
  │ ✘✔✘✘✘ CVE-2026-74331         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74331
  │ ✘✔✘✘✘ CVE-2026-74337         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74337
  │ ✘✔✘✘✘ CVE-2026-74339         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74339
  │ ✘✔✘✘✘ CVE-2026-74342         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74342
  │ ✘✔✘✘✘ CVE-2026-74348         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74348
  │ ✘✔✘✘✘ CVE-2026-74351         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74351
  │ ✘✔✘✘✘ CVE-2026-74382         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74382
  │ ✘✔✘✘✘ CVE-2026-74386         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74386
  │ ✘✔✘✘✘ CVE-2026-74389         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74389
  │ ✘✔✘✘✘ CVE-2026-74391         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74391
  │ ✘✔✘✘✘ CVE-2026-74395         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74395
  │ ✘✔✘✘✘ CVE-2026-74399         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74399
  │ ✘✔✘✘✘ CVE-2026-74402         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74402
  │ ✘✔✘✘✘ CVE-2026-74416         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74416
  │ ✘✔✘✘✘ CVE-2026-74424         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74424
  │ ✘✔✘✘✘ CVE-2026-74426         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74426
  │ ✘✔✘✘✘ CVE-2026-74445         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74445
  │ ✘✔✘✘✘ CVE-2026-74455         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74455
  │ ✘✔✘✘✘ CVE-2026-74457         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74457
  │ ✘✔✘✘✘ CVE-2026-74458         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74458
  │ ✘✔✘✘✘ CVE-2026-74460         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74460
  │ ✘✔✘✘✘ CVE-2026-74463         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74463
  │ ✘✔✘✘✘ CVE-2026-74464         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74464
  │ ✘✔✘✘✘ CVE-2026-74468         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74468
  │ ✘✔✘✘✘ CVE-2026-74484         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74484
  │ ✘✔✘✘✘ CVE-2026-74487         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74487
  │ ✘✔✘✘✘ CVE-2026-74498         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74498
  │ ✘✔✘✘✘ CVE-2026-74499         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74499
  │ ✘✔✘✘✘ CVE-2026-74505         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74505
  │ ✘✔✘✘✘ CVE-2026-74525         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74525
  │ ✘✔✘✘✘ CVE-2026-74547         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74547
  │ ✘✔✘✘✘ CVE-2026-74553         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74553
  │ ✘✔✘✘✘ CVE-2026-74566         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74566
  │ ✘✔✘✘✘ CVE-2026-74577         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74577
  │ ✘✔✘✘✘ CVE-2026-74585         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74585
  │ ✘✔✘✘✘ CVE-2026-74599         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74599
  │ ✘✔✘✘✘ CVE-2026-74620         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74620
  │ ✘✔✘✘✘ CVE-2026-74622         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74622
  │ ✘✔✘✘✘ CVE-2026-74623         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74623
  │ ✘✔✘✘✘ CVE-2026-74650         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74650
  │ ✘✔✘✘✘ CVE-2026-74653         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74653
  │ ✘✔✘✘✘ CVE-2026-74654         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74654
  │ ✘✔✘✘✘ CVE-2026-74657         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74657
  │ ✘✔✘✘✘ CVE-2026-74658         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74658
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
  │ ✘✔✘✘✘ CVE-2026-74694         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74694
  │ ✘✔✘✘✘ CVE-2026-74729         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74729
  │ ✘✔✘✘✘ CVE-2026-74735         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74735
  │ ✘✔✘✘✘ CVE-2026-74740         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74740
  │ ✘✔✘✘✘ CVE-2026-74754         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-74754
  │ ✘✔✘✘✘ CVE-2026-80534         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80534
  │ ✘✔✘✘✘ CVE-2026-80539         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80539
  │ ✘✔✘✘✘ CVE-2026-80562         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80562
  │ ✘✔✘✘✘ CVE-2026-80567         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80567
  │ ✘✔✘✘✘ CVE-2026-80573         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80573
  │ ✘✔✘✘✘ CVE-2026-80594         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80594
  │ ✘✔✘✘✘ CVE-2026-80595         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80595
  │ ✘✔✘✘✘ CVE-2026-80597         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80597
  │ ✘✔✘✘✘ CVE-2026-80605         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80605
  │ ✘✔✘✘✘ CVE-2026-80611         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80611
  │ ✘✔✘✘✘ CVE-2026-80616         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80616
  │ ✘✔✘✘✘ CVE-2026-80626         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80626
  │ ✘✔✘✘✘ CVE-2026-80627         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80627
  │ ✘✔✘✘✘ CVE-2026-80644         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80644
  │ ✘✔✘✘✘ CVE-2026-80647         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80647
  │ ✘✔✘✘✘ CVE-2026-80650         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80650
  │ ✘✔✘✘✘ CVE-2026-80652         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80652
  │ ✘✔✘✘✘ CVE-2026-80659         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80659
  │ ✘✔✘✘✘ CVE-2026-80676         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80676
  │ ✘✔✘✘✘ CVE-2026-80679         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80679
  │ ✘✔✘✘✘ CVE-2026-80689         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80689
  │ ✘✔✘✘✘ CVE-2026-80695         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80695
  │ ✘✔✘✘✘ CVE-2026-80704         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80704
  │ ✘✔✘✘✘ CVE-2026-80708         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80708
  │ ✘✔✘✘✘ CVE-2026-80733         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80733
  │ ✘✔✘✘✘ CVE-2026-80739         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80739
  │ ✘✔✘✘✘ CVE-2026-80742         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80742
  │ ✘✔✘✘✘ CVE-2026-80743         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80743
  │ ✘✔✘✘✘ CVE-2026-80755         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80755
  │ ✘✔✘✘✘ CVE-2026-80757         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80757
  │ ✘✔✘✘✘ CVE-2026-80764         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80764
  │ ✘✔✘✘✘ CVE-2026-80765         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80765
  │ ✘✔✘✘✘ CVE-2026-80766         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80766
  │ ✘✔✘✘✘ CVE-2026-80767         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80767
  │ ✘✔✘✘✘ CVE-2026-80781         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80781
  │ ✘✔✘✘✘ CVE-2026-80782         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80782
  │ ✘✔✘✘✘ CVE-2026-80783         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80783
  │ ✘✔✘✘✘ CVE-2026-80785         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80785
  │ ✘✔✘✘✘ CVE-2026-80786         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80786
  │ ✘✔✘✘✘ CVE-2026-80788         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80788
  │ ✘✔✘✘✘ CVE-2026-80789         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80789
  │ ✘✔✘✘✘ CVE-2026-80790         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80790
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
  │ ✘✔✘✘✘ CVE-2026-80807         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80807
  │ ✘✔✘✘✘ CVE-2026-80808         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80808
  │ ✘✔✘✘✘ CVE-2026-80809         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80809
  │ ✘✔✘✘✘ CVE-2026-80812         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80812
  │ ✘✔✘✘✘ CVE-2026-80814         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80814
  │ ✘✔✘✘✘ CVE-2026-80819         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80819
  │ ✘✔✘✘✘ CVE-2026-80820         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80820
  │ ✘✔✘✘✘ CVE-2026-80823         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80823
  │ ✘✔✘✘✘ CVE-2026-80824         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80824
  │ ✘✔✘✘✘ CVE-2026-80826         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80826
  │ ✘✔✘✘✘ CVE-2026-80827         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80827
  │ ✘✔✘✘✘ CVE-2026-80828         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80828
  │ ✘✔✘✘✘ CVE-2026-80829         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80829
  │ ✘✔✘✘✘ CVE-2026-80830         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80830
  │ ✘✔✘✘✘ CVE-2026-80831         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80831
  │ ✘✔✘✘✘ CVE-2026-80840         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80840
  │ ✘✔✘✘✘ CVE-2026-80841         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80841
  │ ✘✔✘✘✘ CVE-2026-80843         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80843
  │ ✘✔✘✘✘ CVE-2026-80844         ?            0.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-80844
  │ ✘✔✘✘✘ CVE-2026-80847         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80847
  │ ✘✔✘✘✘ CVE-2026-80851         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80851
  │ ✘✔✘✘✘ CVE-2026-80852         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80852
  │ ✘✔✘✘✘ CVE-2026-80854         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80854
  │ ✘✔✘✘✘ CVE-2026-80861         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80861
  │ ✘✔✘✘✘ CVE-2026-80863         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80863
  │ ✘✔✘✘✘ CVE-2026-80864         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80864
  │ ✘✔✘✘✘ CVE-2026-80866         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80866
  │ ✘✔✘✘✘ CVE-2026-80867         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80867
  │ ✘✔✘✘✘ CVE-2026-80875         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80875
  │ ✘✔✘✘✘ CVE-2026-80876         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80876
  │ ✘✔✘✘✘ CVE-2026-80877         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80877
  │ ✘✔✘✘✘ CVE-2026-80879         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80879
  │ ✘✔✘✘✘ CVE-2026-80881         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80881
  │ ✘✔✘✘✘ CVE-2026-80883         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80883
  │ ✘✔✘✘✘ CVE-2026-80884         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80884
  │ ✘✔✘✘✘ CVE-2026-80886         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80886
  │ ✘✔✘✘✘ CVE-2026-80888         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80888
  │ ✘✔✘✘✘ CVE-2026-80890         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80890
  │ ✘✔✘✘✘ CVE-2026-80901         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80901
  │ ✘✔✘✘✘ CVE-2026-80902         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80902
  │ ✘✔✘✘✘ CVE-2026-80905         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80905
  │ ✘✔✘✘✘ CVE-2026-80906         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80906
  │ ✘✔✘✘✘ CVE-2026-80907         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80907
  │ ✘✔✘✘✘ CVE-2026-80908         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80908
  │ ✘✔✘✘✘ CVE-2026-80909         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80909
  │ ✘✔✘✘✘ CVE-2026-80912         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80912
  │ ✘✔✘✘✘ CVE-2026-80913         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80913
  │ ✘✔✘✘✘ CVE-2026-80918         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80918
  │ ✘✔✘✘✘ CVE-2026-80925         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80925
  │ ✘✔✘✘✘ CVE-2026-80930         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80930
  │ ✘✔✘✘✘ CVE-2026-80948         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80948
  │ ✘✔✘✘✘ CVE-2026-80949         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80949
  │ ✘✔✘✘✘ CVE-2026-80963         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80963
  │ ✘✔✘✘✘ CVE-2026-80964         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80964
  │ ✘✔✘✘✘ CVE-2026-80965         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80965
  │ ✘✔✘✘✘ CVE-2026-80966         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80966
  │ ✘✔✘✘✘ CVE-2026-80968         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80968
  │ ✘✔✘✘✘ CVE-2026-80969         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80969
  │ ✘✔✘✘✘ CVE-2026-80972         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80972
  │ ✘✔✘✘✘ CVE-2026-80973         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80973
  │ ✘✔✘✘✘ CVE-2026-80974         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80974
  │ ✘✔✘✘✘ CVE-2026-80988         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80988
  │ ✘✔✘✘✘ CVE-2026-80996         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80996
  │ ✘✔✘✘✘ CVE-2026-80999         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-80999
  │ ✘✔✘✘✘ CVE-2026-81005         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-81005
  │ ✘✔✘✘✘ CVE-2026-89457         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89457
  │ ✘✔✘✘✘ CVE-2026-89458         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89458
  │ ✘✔✘✘✘ CVE-2026-89461         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89461
  │ ✘✔✘✘✘ CVE-2026-89462         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89462
  │ ✘✔✘✘✘ CVE-2026-89464         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89464
  │ ✘✔✘✘✘ CVE-2026-89468         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89468
  │ ✘✔✘✘✘ CVE-2026-89475         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89475
  │ ✘✔✘✘✘ CVE-2026-89484         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89484
  │ ✘✔✘✘✘ CVE-2026-89490         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89490
  │ ✘✔✘✘✘ CVE-2026-89491         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89491
  │ ✘✔✘✘✘ CVE-2026-89496         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89496
  │ ✘✔✘✘✘ CVE-2026-89498         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89498
  │ ✘✔✘✘✘ CVE-2026-89515         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89515
  │ ✘✔✘✘✘ CVE-2026-89525         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89525
  │ ✘✔✘✘✘ CVE-2026-89527         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89527
  │ ✘✔✘✘✘ CVE-2026-89531         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89531
  │ ✘✔✘✘✘ CVE-2026-89539         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89539
  │ ✘✔✘✘✘ CVE-2026-89543         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89543
  │ ✘✔✘✘✘ CVE-2026-89552         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89552
  │ ✘✔✘✘✘ CVE-2026-89565         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89565
  │ ✘✔✘✘✘ CVE-2026-89575         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89575
  │ ✘✔✘✘✘ CVE-2026-89576         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89576
  │ ✘✔✘✘✘ CVE-2026-89582         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89582
  │ ✘✔✘✘✘ CVE-2026-89595         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89595
  │ ✘✔✘✘✘ CVE-2026-89598         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89598
  │ ✘✔✘✘✘ CVE-2026-89623         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89623
  │ ✘✔✘✘✘ CVE-2026-89627         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89627
  │ ✘✔✘✘✘ CVE-2026-89628         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89628
  │ ✘✔✘✘✘ CVE-2026-89642         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89642
  │ ✘✔✘✘✘ CVE-2026-89644         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89644
  │ ✘✔✘✘✘ CVE-2026-89666         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89666
  │ ✘✔✘✘✘ CVE-2026-89673         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89673
  │ ✘✔✘✘✘ CVE-2026-89718         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89718
  │ ✘✔✘✘✘ CVE-2026-89719         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89719
  │ ✘✔✘✘✘ CVE-2026-89722         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89722
  │ ✘✔✘✘✘ CVE-2026-89726         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89726
  │ ✘✔✘✘✘ CVE-2026-89730         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89730
  │ ✘✔✘✘✘ CVE-2026-89732         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89732
  │ ✘✔✘✘✘ CVE-2026-89740         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89740
  │ ✘✔✘✘✘ CVE-2026-89749         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89749
  │ ✘✔✘✘✘ CVE-2026-89752         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89752
  │ ✘✔✘✘✘ CVE-2026-89753         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89753
  │ ✘✔✘✘✘ CVE-2026-89756         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89756
  │ ✘✔✘✘✘ CVE-2026-89765         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89765
  │ ✘✔✘✘✘ CVE-2026-89780         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89780
  │ ✘✔✘✘✘ CVE-2026-89784         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89784
  │ ✘✔✘✘✘ CVE-2026-89797         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89797
  │ ✘✔✘✘✘ CVE-2026-89813         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89813
  │ ✘✔✘✘✘ CVE-2026-89816         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89816
  │ ✘✔✘✘✘ CVE-2026-89821         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89821
  │ ✘✔✘✘✘ CVE-2026-89822         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89822
  │ ✘✔✘✘✘ CVE-2026-89833         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89833
  │ ✘✔✘✘✘ CVE-2026-89843         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89843
  │ ✘✔✘✘✘ CVE-2026-89845         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89845
  │ ✘✔✘✘✘ CVE-2026-89850         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89850
  │ ✘✔✘✘✘ CVE-2026-89852         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89852
  │ ✘✔✘✘✘ CVE-2026-89855         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89855
  │ ✘✔✘✘✘ CVE-2026-89858         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89858
  │ ✘✔✘✘✘ CVE-2026-89859         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89859
  │ ✘✔✘✘✘ CVE-2026-89864         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89864
  │ ✘✔✘✘✘ CVE-2026-89865         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89865
  │ ✘✔✘✘✘ CVE-2026-89871         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89871
  │ ✘✔✘✘✘ CVE-2026-89872         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89872
  │ ✘✔✘✘✘ CVE-2026-89876         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89876
  │ ✘✔✘✘✘ CVE-2026-89878         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89878
  │ ✘✔✘✘✘ CVE-2026-89879         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89879
  │ ✘✔✘✘✘ CVE-2026-89881         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89881
  │ ✘✔✘✘✘ CVE-2026-89891         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89891
  │ ✘✔✘✘✘ CVE-2026-89892         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89892
  │ ✘✔✘✘✘ CVE-2026-89895         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89895
  │ ✘✔✘✘✘ CVE-2026-89896         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89896
  │ ✘✔✘✘✘ CVE-2026-89901         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89901
  │ ✘✔✘✘✘ CVE-2026-89921         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89921
  │ ✘✔✘✘✘ CVE-2026-89923         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89923
  │ ✘✔✘✘✘ CVE-2026-89924         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89924
  │ ✘✔✘✘✘ CVE-2026-89925         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89925
  │ ✘✔✘✘✘ CVE-2026-89926         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89926
  │ ✘✔✘✘✘ CVE-2026-89936         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89936
  │ ✘✔✘✘✘ CVE-2026-89937         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89937
  │ ✘✔✘✘✘ CVE-2026-89944         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89944
  │ ✘✔✘✘✘ CVE-2026-89945         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89945
  │ ✘✔✘✘✘ CVE-2026-89946         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89946
  │ ✘✔✘✘✘ CVE-2026-89948         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89948
  │ ✘✔✘✘✘ CVE-2026-89949         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89949
  │ ✘✔✘✘✘ CVE-2026-89952         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89952
  │ ✘✔✘✘✘ CVE-2026-89953         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89953
  │ ✘✔✘✘✘ CVE-2026-89964         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89964
  │ ✘✔✘✘✘ CVE-2026-89982         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89982
  │ ✘✔✘✘✘ CVE-2026-89987         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89987
  │ ✘✔✘✘✘ CVE-2026-89993         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-89993
  │ ✘✔✘✘✘ CVE-2026-90015         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90015
  │ ✘✔✘✘✘ CVE-2026-90019         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90019
  │ ✘✔✘✘✘ CVE-2026-90020         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90020
  │ ✘✔✘✘✘ CVE-2026-90021         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90021
  │ ✘✔✘✘✘ CVE-2026-90023         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90023
  │ ✘✔✘✘✘ CVE-2026-90029         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90029
  │ ✘✔✘✘✘ CVE-2026-90031         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90031
  │ ✘✔✘✘✘ CVE-2026-90033         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90033
  │ ✘✔✘✘✘ CVE-2026-90034         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90034
  │ ✘✔✘✘✘ CVE-2026-90053         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90053
  │ ✘✔✘✘✘ CVE-2026-90054         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90054
  │ ✘✔✘✘✘ CVE-2026-90055         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90055
  │ ✘✔✘✘✘ CVE-2026-90056         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90056
  │ ✘✔✘✘✘ CVE-2026-90058         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90058
  │ ✘✔✘✘✘ CVE-2026-90063         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90063
  │ ✘✔✘✘✘ CVE-2026-90068         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90068
  │ ✘✔✘✘✘ CVE-2026-90070         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90070
  │ ✘✔✘✘✘ CVE-2026-90072         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90072
  │ ✘✔✘✘✘ CVE-2026-90073         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90073
  │ ✘✔✘✘✘ CVE-2026-90075         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90075
  │ ✘✔✘✘✘ CVE-2026-90076         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90076
  │ ✘✔✘✘✘ CVE-2026-90081         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90081
  │ ✘✔✘✘✘ CVE-2026-90083         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90083
  │ ✘✔✘✘✘ CVE-2026-90088         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90088
  │ ✘✔✘✘✘ CVE-2026-90090         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90090
  │ ✘✔✘✘✘ CVE-2026-90099         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90099
  │ ✘✔✘✘✘ CVE-2026-90105         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90105
  │ ✘✔✘✘✘ CVE-2026-90106         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90106
  │ ✘✔✘✘✘ CVE-2026-90109         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90109
  │ ✘✔✘✘✘ CVE-2026-90112         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90112
  │ ✘✔✘✘✘ CVE-2026-90116         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90116
  │ ✘✔✘✘✘ CVE-2026-90125         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90125
  │ ✘✔✘✘✘ CVE-2026-90126         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90126
  │ ✘✔✘✘✘ CVE-2026-90138         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90138
  │ ✘✔✘✘✘ CVE-2026-90150         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90150
  │ ✘✔✘✘✘ CVE-2026-90160         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90160
  │ ✘✔✘✘✘ CVE-2026-90180         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90180
  │ ✘✔✘✘✘ CVE-2026-90182         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90182
  │ ✘✔✘✘✘ CVE-2026-90183         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90183
  │ ✘✔✘✘✘ CVE-2026-90184         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90184
  │ ✘✔✘✘✘ CVE-2026-90187         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90187
  │ ✘✔✘✘✘ CVE-2026-90188         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90188
  │ ✘✔✘✘✘ CVE-2026-90189         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90189
  │ ✘✔✘✘✘ CVE-2026-90194         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90194
  │ ✘✔✘✘✘ CVE-2026-90196         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90196
  │ ✘✔✘✘✘ CVE-2026-90202         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90202
  │ ✘✔✘✘✘ CVE-2026-90208         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90208
  │ ✘✔✘✘✘ CVE-2026-90209         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90209
  │ ✘✔✘✘✘ CVE-2026-90213         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90213
  │ ✘✔✘✘✘ CVE-2026-90214         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90214
  │ ✘✔✘✘✘ CVE-2026-90216         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90216
  │ ✘✔✘✘✘ CVE-2026-90219         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90219
  │ ✘✔✘✘✘ CVE-2026-90222         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90222
  │ ✘✔✘✘✘ CVE-2026-90226         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90226
  │ ✘✔✘✘✘ CVE-2026-90245         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90245
  │ ✘✔✘✘✘ CVE-2026-90247         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90247
  │ ✘✔✘✘✘ CVE-2026-90248         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90248
  │ ✘✔✘✘✘ CVE-2026-90259         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90259
  │ ✘✔✘✘✘ CVE-2026-90263         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90263
  │ ✘✔✘✘✘ CVE-2026-90267         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90267
  │ ✘✔✘✘✘ CVE-2026-90274         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90274
  │ ✘✔✘✘✘ CVE-2026-90283         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90283
  │ ✘✔✘✘✘ CVE-2026-90284         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90284
  │ ✘✔✘✘✘ CVE-2026-90285         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90285
  │ ✘✔✘✘✘ CVE-2026-90295         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90295
  │ ✘✔✘✘✘ CVE-2026-90296         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90296
  │ ✘✔✘✘✘ CVE-2026-90297         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90297
  │ ✘✔✘✘✘ CVE-2026-90298         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90298
  │ ✘✔✘✘✘ CVE-2026-90302         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90302
  │ ✘✔✘✘✘ CVE-2026-90303         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90303
  │ ✘✔✘✘✘ CVE-2026-90307         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90307
  │ ✘✔✘✘✘ CVE-2026-90311         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90311
  │ ✘✔✘✘✘ CVE-2026-90314         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90314
  │ ✘✔✘✘✘ CVE-2026-90315         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90315
  │ ✘✔✘✘✘ CVE-2026-90318         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90318
  │ ✘✔✘✘✘ CVE-2026-90319         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90319
  │ ✘✔✘✘✘ CVE-2026-90322         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90322
  │ ✘✔✘✘✘ CVE-2026-90327         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90327
  │ ✘✔✘✘✘ CVE-2026-90328         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90328
  │ ✘✔✘✘✘ CVE-2026-90330         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90330
  │ ✘✔✘✘✘ CVE-2026-90334         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90334
  │ ✘✔✘✘✘ CVE-2026-90335         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90335
  │ ✘✔✘✘✘ CVE-2026-90336         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90336
  │ ✘✔✘✘✘ CVE-2026-90337         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90337
  │ ✘✔✘✘✘ CVE-2026-90345         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90345
  │ ✘✔✘✘✘ CVE-2026-90360         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90360
  │ ✘✔✘✘✘ CVE-2026-90382         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90382
  │ ✘✔✘✘✘ CVE-2026-90386         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90386
  │ ✘✔✘✘✘ CVE-2026-90394         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90394
  │ ✘✔✘✘✘ CVE-2026-90395         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90395
  │ ✘✔✘✘✘ CVE-2026-90410         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90410
  │ ✘✔✘✘✘ CVE-2026-90411         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90411
  │ ✘✔✘✘✘ CVE-2026-90415         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90415
  │ ✘✔✘✘✘ CVE-2026-90416         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90416
  │ ✘✔✘✘✘ CVE-2026-90417         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90417
  │ ✘✔✘✘✘ CVE-2026-90418         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90418
  │ ✘✔✘✘✘ CVE-2026-90420         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90420
  │ ✘✔✘✘✘ CVE-2026-90421         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90421
  │ ✘✔✘✘✘ CVE-2026-90431         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90431
  │ ✘✔✘✘✘ CVE-2026-90433         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90433
  │ ✘✔✘✘✘ CVE-2026-90434         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-90434
  │ ✘✔✘✘✘ CVE-2026-92480         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92480
  │ ✘✔✘✘✘ CVE-2026-92481         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92481
  │ ✘✔✘✘✘ CVE-2026-92482         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92482
  │ ✘✔✘✘✘ CVE-2026-92498         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92498
  │ ✘✔✘✘✘ CVE-2026-92499         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92499
  │ ✘✔✘✘✘ CVE-2026-92500         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92500
  │ ✘✔✘✘✘ CVE-2026-92509         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92509
  │ ✘✔✘✘✘ CVE-2026-92520         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92520
  │ ✘✔✘✘✘ CVE-2026-92521         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92521
  │ ✘✔✘✘✘ CVE-2026-92524         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-92524
  │ ✘✔✘✘✘ CVE-2026-93040         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93040
  │ ✘✔✘✘✘ CVE-2026-93041         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93041
  │ ✘✔✘✘✘ CVE-2026-93047         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93047
  │ ✘✔✘✘✘ CVE-2026-93048         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93048
  │ ✘✔✘✘✘ CVE-2026-93049         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93049
  │ ✘✔✘✘✘ CVE-2026-93050         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93050
  │ ✘✔✘✘✘ CVE-2026-93051         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93051
  │ ✘✔✘✘✘ CVE-2026-93053         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93053
  │ ✘✔✘✘✘ CVE-2026-93055         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93055
  │ ✘✔✘✘✘ CVE-2026-93056         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93056
  │ ✘✔✘✘✘ CVE-2026-93061         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93061
  │ ✘✔✘✘✘ CVE-2026-93067         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93067
  │ ✘✔✘✘✘ CVE-2026-93072         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93072
  │ ✘✔✘✘✘ CVE-2026-93099         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93099
  │ ✘✔✘✘✘ CVE-2026-93100         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93100
  │ ✘✔✘✘✘ CVE-2026-93103         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93103
  │ ✘✔✘✘✘ CVE-2026-93104         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93104
  │ ✘✔✘✘✘ CVE-2026-93108         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93108
  │ ✘✔✘✘✘ CVE-2026-93110         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93110
  │ ✘✔✘✘✘ CVE-2026-93117         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93117
  │ ✘✔✘✘✘ CVE-2026-93120         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93120
  │ ✘✔✘✘✘ CVE-2026-93140         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93140
  │ ✘✔✘✘✘ CVE-2026-93141         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93141
  │ ✘✔✘✘✘ CVE-2026-93145         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93145
  │ ✘✔✘✘✘ CVE-2026-93149         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93149
  │ ✘✔✘✘✘ CVE-2026-93159         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93159
  │ ✘✔✘✘✘ CVE-2026-93160         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93160
  │ ✘✔✘✘✘ CVE-2026-93163         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93163
  │ ✘✔✘✘✘ CVE-2026-93167         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93167
  │ ✘✔✘✘✘ CVE-2026-93168         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93168
  │ ✘✔✘✘✘ CVE-2026-93172         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93172
  │ ✘✔✘✘✘ CVE-2026-93179         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93179
  │ ✘✔✘✘✘ CVE-2026-93183         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93183
  │ ✘✔✘✘✘ CVE-2026-93184         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93184
  │ ✘✔✘✘✘ CVE-2026-93188         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93188
  │ ✘✔✘✘✘ CVE-2026-93191         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93191
  │ ✘✔✘✘✘ CVE-2026-93199         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93199
  │ ✘✔✘✘✘ CVE-2026-93200         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93200
  │ ✘✔✘✘✘ CVE-2026-93202         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93202
  │ ✘✔✘✘✘ CVE-2026-93204         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93204
  │ ✘✔✘✘✘ CVE-2026-93205         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93205
  │ ✘✔✘✘✘ CVE-2026-93206         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93206
  │ ✘✔✘✘✘ CVE-2026-93210         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93210
  │ ✘✔✘✘✘ CVE-2026-93213         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93213
  │ ✘✔✘✘✘ CVE-2026-93214         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93214
  │ ✘✔✘✘✘ CVE-2026-93219         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93219
  │ ✘✔✘✘✘ CVE-2026-93222         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93222
  │ ✘✔✘✘✘ CVE-2026-93226         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93226
  │ ✘✔✘✘✘ CVE-2026-93231         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93231
  │ ✘✔✘✘✘ CVE-2026-93235         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93235
  │ ✘✔✘✘✘ CVE-2026-93236         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93236
  │ ✘✔✘✘✘ CVE-2026-93239         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93239
  │ ✘✔✘✘✘ CVE-2026-93240         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93240
  │ ✘✔✘✘✘ CVE-2026-93241         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93241
  │ ✘✔✘✘✘ CVE-2026-93245         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93245
  │ ✘✔✘✘✘ CVE-2026-93251         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93251
  │ ✘✔✘✘✘ CVE-2026-93252         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93252
  │ ✘✔✘✘✘ CVE-2026-93256         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93256
  │ ✘✔✘✘✘ CVE-2026-93261         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93261
  │ ✘✔✘✘✘ CVE-2026-93264         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93264
  │ ✘✔✘✘✘ CVE-2026-93268         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93268
  │ ✘✔✘✘✘ CVE-2026-93269         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93269
  │ ✘✔✘✘✘ CVE-2026-93274         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93274
  │ ✘✔✘✘✘ CVE-2026-93275         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-93275
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
  │ ✘✔✘✘✘ CVE-2026-97529         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97529
  │ ✘✔✘✘✘ CVE-2026-97532         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97532
  │ ✘✔✘✘✘ CVE-2026-97535         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97535
  │ ✘✔✘✘✘ CVE-2026-97537         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97537
  │ ✘✔✘✘✘ CVE-2026-97539         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97539
  │ ✘✔✘✘✘ CVE-2026-97540         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97540
  │ ✘✔✘✘✘ CVE-2026-97541         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97541
  │ ✘✔✘✘✘ CVE-2026-97554         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97554
  │ ✘✔✘✘✘ CVE-2026-97561         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97561
  │ ✘✔✘✘✘ CVE-2026-97563         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97563
  │ ✘✔✘✘✘ CVE-2026-97564         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97564
  │ ✘✔✘✘✘ CVE-2026-97565         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97565
  │ ✘✔✘✘✘ CVE-2026-97572         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97572
  │ ✘✔✘✘✘ CVE-2026-97582         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97582
  │ ✘✔✘✘✘ CVE-2026-97596         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97596
  │ ✘✔✘✘✘ CVE-2026-97597         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97597
  │ ✘✔✘✘✘ CVE-2026-97598         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97598
  │ ✘✔✘✘✘ CVE-2026-97599         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97599
  │ ✘✔✘✘✘ CVE-2026-97600         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97600
  │ ✘✔✘✘✘ CVE-2026-97601         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97601
  │ ✘✔✘✘✘ CVE-2026-97604         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97604
  │ ✘✔✘✘✘ CVE-2026-97616         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97616
  │ ✘✔✘✘✘ CVE-2026-97904         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97904
  │ ✘✔✘✘✘ CVE-2026-97905         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97905
  │ ✘✔✘✘✘ CVE-2026-97908         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97908
  │ ✘✔✘✘✘ CVE-2026-97909         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97909
  │ ✘✔✘✘✘ CVE-2026-97918         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97918
  │ ✘✔✘✘✘ CVE-2026-97922         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97922
  │ ✘✔✘✘✘ CVE-2026-97923         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97923
  │ ✘✔✘✘✘ CVE-2026-97925         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97925
  │ ✘✔✘✘✘ CVE-2026-97927         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97927
  │ ✘✔✘✘✘ CVE-2026-97929         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97929
  │ ✘✔✘✘✘ CVE-2026-97930         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97930
  │ ✘✔✘✘✘ CVE-2026-97933         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97933
  │ ✘✔✘✘✘ CVE-2026-97935         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97935
  │ ✘✔✘✘✘ CVE-2026-97938         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97938
  │ ✘✔✘✘✘ CVE-2026-97939         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97939
  │ ✘✔✘✘✘ CVE-2026-97949         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97949
  │ ✘✔✘✘✘ CVE-2026-97950         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97950
  │ ✘✔✘✘✘ CVE-2026-97951         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97951
  │ ✘✔✘✘✘ CVE-2026-97954         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97954
  │ ✘✔✘✘✘ CVE-2026-97958         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97958
  │ ✘✔✘✘✘ CVE-2026-97959         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97959
  │ ✘✔✘✘✘ CVE-2026-97965         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97965
  │ ✘✔✘✘✘ CVE-2026-97975         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97975
  │ ✘✔✘✘✘ CVE-2026-97981         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97981
  │ ✘✔✘✘✘ CVE-2026-97982         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97982
  │ ✘✔✘✘✘ CVE-2026-97986         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97986
  │ ✘✔✘✘✘ CVE-2026-97987         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97987
  │ ✘✔✘✘✘ CVE-2026-97988         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97988
  │ ✘✔✘✘✘ CVE-2026-97995         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97995
  │ ✘✔✘✘✘ CVE-2026-97997         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97997
  │ ✘✔✘✘✘ CVE-2026-97998         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97998
  │ ✘✔✘✘✘ CVE-2026-98006         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98006
  │ ✘✔✘✘✘ CVE-2026-98010         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98010
  │ ✘✔✘✘✘ CVE-2026-98011         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98011
  │ ✘✔✘✘✘ CVE-2026-98015         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98015
  │ ✘✔✘✘✘ CVE-2026-98019         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98019
  │ ✘✔✘✘✘ CVE-2026-98021         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98021
  │ ✘✔✘✘✘ CVE-2026-98022         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98022
  │ ✘✔✘✘✘ CVE-2026-98025         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98025
  │ ✘✔✘✘✘ CVE-2026-98026         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98026
  │ ✘✔✘✘✘ CVE-2026-98068         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98068
  │ ✘✔✘✘✘ CVE-2026-98071         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98071
  │ ✘✔✘✘✘ CVE-2026-98072         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98072
  │ ✘✔✘✘✘ CVE-2026-98074         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98074
  │ ✘✔✘✘✘ CVE-2026-98076         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98076
  │ ✘✔✘✘✘ CVE-2026-98077         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98077
  │ ✘✔✘✘✘ CVE-2026-98079         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98079
  │ ✘✔✘✘✘ CVE-2026-98088         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98088
  │ ✘✔✘✘✘ CVE-2026-98103         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98103
  │ ✘✔✘✘✘ CVE-2026-98104         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98104
  │ ✘✔✘✘✘ CVE-2026-98167         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98167
  │ ✘✔✘✘✘ CVE-2026-98170         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98170
  │ ✘✔✘✘✘ CVE-2026-98172         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98172
  │ ✘✔✘✘✘ CVE-2026-98176         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98176
  │ ✘✔✘✘✘ CVE-2026-98177         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98177
  │ ✘✔✘✘✘ CVE-2026-98182         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98182
  │ ✘✔✘✘✘ CVE-2026-98185         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98185
  │ ✘✔✘✘✘ CVE-2026-98186         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98186
  │ ✘✔✘✘✘ CVE-2026-98187         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98187
  │ ✘✔✘✘✘ CVE-2026-98188         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98188
  │ ✘✔✘✘✘ CVE-2026-98189         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98189
  │ ✘✔✘✘✘ CVE-2026-98191         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98191
  │ ✘✔✘✘✘ CVE-2026-98193         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98193
  │ ✘✔✘✘✘ CVE-2026-98194         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98194
  │ ✘✔✘✘✘ CVE-2026-98195         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98195
  │ ✘✔✘✘✘ CVE-2026-98196         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98196
  │ ✘✔✘✘✘ CVE-2026-98201         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98201
  │ ✘✔✘✘✘ CVE-2026-98202         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98202
  │ ✘✔✘✘✘ CVE-2026-98203         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98203
  │ ✘✔✘✘✘ CVE-2026-98204         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98204
  │ ✘✔✘✘✘ CVE-2026-98205         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98205
  │ ✘✔✘✘✘ CVE-2026-98207         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98207
  │ ✘✔✘✘✘ CVE-2026-98208         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98208
  │ ✘✔✘✘✘ CVE-2026-98209         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98209
  │ ✘✔✘✘✘ CVE-2026-98210         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98210
  │ ✘✔✘✘✘ CVE-2026-98213         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98213
  │ ✘✔✘✘✘ CVE-2026-98217         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98217
  │ ✘✔✘✘✘ CVE-2026-98222         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98222
  │ ✘✔✘✘✘ CVE-2026-98227         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98227
  │ ✘✔✘✘✘ CVE-2026-98233         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98233
  │ ✘✔✘✘✘ CVE-2026-98234         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98234
  │ ✘✔✘✘✘ CVE-2026-98248         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98248
  │ ✘✔✘✘✘ CVE-2026-98255         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98255
  │ ✘✔✘✘✘ CVE-2026-98262         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98262
  │ ✘✔✘✘✘ CVE-2026-98266         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98266
  │ ✘✔✘✘✘ CVE-2026-98269         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98269
  │ ✘✔✘✘✘ CVE-2026-98271         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98271
  │ ✘✔✘✘✘ CVE-2026-98272         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98272
  │ ✘✔✘✘✘ CVE-2026-98275         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98275
  │ ✘✔✘✘✘ CVE-2026-98284         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98284
  │ ✘✔✘✘✘ CVE-2026-98285         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98285
  │ ✘✔✘✘✘ CVE-2026-98288         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98288
  │ ✘✔✘✘✘ CVE-2026-98292         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98292
  │ ✘✔✘✘✘ CVE-2026-98294         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98294
  │ ✘✔✘✘✘ CVE-2026-98298         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98298
  │ ✘✔✘✘✘ CVE-2026-98299         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98299
  │ ✘✔✘✘✘ CVE-2026-98300         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98300
  │ ✘✔✘✘✘ CVE-2026-98302         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98302
  │ ✘✔✘✘✘ CVE-2026-98303         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98303
  │ ✘✔✘✘✘ CVE-2026-98306         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98306
  │ ✘✔✘✘✘ CVE-2026-98308         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98308
  │ ✘✔✘✘✘ CVE-2026-98309         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98309
  │ ✘✔✘✘✘ CVE-2026-98312         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98312
  │ ✘✔✘✘✘ CVE-2026-98314         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98314
  │ ✘✔✘✘✘ CVE-2026-98319         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98319
  │ ✘✔✘✘✘ CVE-2026-98321         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98321
  │ ✘✔✘✘✘ CVE-2026-98325         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98325
  │ ✘✔✘✘✘ CVE-2026-98326         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98326
  │ ✘✔✘✘✘ CVE-2026-98327         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98327
  │ ✘✔✘✘✘ CVE-2026-98329         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98329
  │ ✘✔✘✘✘ CVE-2026-98332         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98332
  │ ✘✔✘✘✘ CVE-2026-98333         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98333
  │ ✘✔✘✘✘ CVE-2026-98334         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98334
  │ ✘✔✘✘✘ CVE-2026-98335         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98335
  │ ✘✔✘✘✘ CVE-2026-98337         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98337
  │ ✘✔✘✘✘ CVE-2026-98338         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98338
  │ ✘✔✘✘✘ CVE-2026-98340         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98340
  │ ✘✔✘✘✘ CVE-2026-98342         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98342
  │ ✘✔✘✘✘ CVE-2026-98345         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98345
  │ ✘✔✘✘✘ CVE-2026-98347         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98347
  │ ✘✔✘✘✘ CVE-2026-98351         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98351
  │ ✘✔✘✘✘ CVE-2026-98354         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98354
  │ ✘✔✘✘✘ CVE-2026-98358         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98358
  │ ✘✔✘✘✘ CVE-2026-98362         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98362
  │ ✘✔✘✘✘ CVE-2026-98363         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98363
  │ ✘✔✘✘✘ CVE-2026-98375         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98375
  │ ✘✔✘✘✘ CVE-2026-98377         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98377
  │ ✘✔✘✘✘ CVE-2026-98379         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98379
  │ ✘✔✘✘✘ CVE-2026-98380         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98380
  │ ✘✔✘✘✘ CVE-2026-98386         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98386
  │ ✘✔✘✘✘ CVE-2026-98389         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98389
  │ ✘✔✘✘✘ CVE-2026-98393         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98393
  │ ✘✔✘✘✘ CVE-2026-98398         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98398
  │ ✘✔✘✘✘ CVE-2026-98399         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98399
  │ ✘✔✘✘✘ CVE-2026-98400         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98400
  │ ✘✔✘✘✘ CVE-2026-98404         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98404
  │ ✘✔✘✘✘ CVE-2026-98406         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98406
  │ ✘✔✘✘✘ CVE-2026-98407         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98407
  │ ✘✔✘✘✘ CVE-2026-98409         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98409
  │ ✘✔✘✘✘ CVE-2026-98413         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98413
  │ ✘✔✘✘✘ CVE-2026-98421         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98421
  │ ✘✔✘✘✘ CVE-2026-98422         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98422
  │ ✘✔✘✘✘ CVE-2026-98423         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98423
  │ ✘✔✘✘✘ CVE-2026-98424         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98424
  │ ✘✔✘✘✘ CVE-2026-98425         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98425
  │ ✘✔✘✘✘ CVE-2026-98426         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98426
  │ ✘✔✘✘✘ CVE-2026-98427         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98427
  │ ✘✔✘✘✘ CVE-2026-98428         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98428
  │ ✘✔✘✘✘ CVE-2026-98430         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98430
  │ ✘✔✘✘✘ CVE-2026-98435         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98435
  │ ✘✔✘✘✘ CVE-2026-98439         ?            0.0   0.1%   ·  ↳ S:UBUNTU-CVE-2026-98439
  │ ✘✔✘✘✘ CVE-2026-98449         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98449
  │ ✘✔✘✘✘ CVE-2026-98450         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98450
  │ ✘✔✘✘✘ CVE-2026-98452         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98452
  │ ✘✔✘✘✘ CVE-2026-98453         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98453
  │ ✘✔✘✘✘ CVE-2026-98455         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98455
  │ ✘✔✘✘✘ CVE-2026-98457         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98457
  │ ✘✔✘✘✘ CVE-2026-98460         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98460
  │ ✘✔✘✘✘ CVE-2026-98461         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98461
  │ ✘✔✘✘✘ CVE-2026-98476         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98476
  │ ✘✔✘✘✘ CVE-2026-98481         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98481
  │ ✘✔✘✘✘ CVE-2026-98482         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98482
  │ ✘✔✘✘✘ CVE-2026-98483         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98483
  │ ✘✔✘✘✘ CVE-2026-98486         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98486
  │ ✘✔✘✘✘ CVE-2026-98488         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98488
  │ ✘✔✘✘✘ CVE-2026-98489         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98489
  │ ✘✔✘✘✘ CVE-2026-98493         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98493
  │ ✘✔✘✘✘ CVE-2026-98494         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98494
  │ ✘✔✘✘✘ CVE-2026-98502         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98502
  │ ✘✔✘✘✘ CVE-2026-98503         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98503
  │ ✘✔✘✘✘ CVE-2026-98511         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98511
  │ ✘✔✘✘✘ CVE-2026-98514         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98514
  │ ✘✔✘✘✘ CVE-2026-98516         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98516
  │ ✘✔✘✘✘ CVE-2026-98526         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98526
  │ ✘✔✘✘✘ CVE-2026-98527         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98527
  │ ✘✔✘✘✘ CVE-2026-98529         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98529
  │ ✘✔✘✘✘ CVE-2026-98531         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98531
  │ ✘✔✘✘✘ CVE-2026-98535         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98535
  │ ✘✔✘✘✘ CVE-2026-98537         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98537
  │ ✘✔✘✘✘ CVE-2026-98541         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98541
  │ ✘✔✘✘✘ CVE-2026-98544         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98544
  │ ✘✔✘✘✘ CVE-2026-98547         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98547
  │ ✘✔✘✘✘ CVE-2026-98553         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98553
  │ ✘✔✘✘✘ CVE-2026-98554         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98554
  │ ✘✔✘✘✘ CVE-2026-98565         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98565
  │ ✘✔✘✘✘ CVE-2026-98567         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98567
  │ ✘✔✘✘✘ CVE-2026-98568         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98568
  │ ✘✔✘✘✘ CVE-2026-98569         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98569
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
  │ ✘✔✘✘✘ CVE-2026-98589         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98589
  │ ✘✔✘✘✘ CVE-2026-98594         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98594
  │ ✘✔✘✘✘ CVE-2026-98597         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98597
  │ ✘✔✘✘✘ CVE-2026-98598         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98598
  │ ✘✔✘✘✘ CVE-2026-98602         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98602
  │ ✘✔✘✘✘ CVE-2026-98608         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98608
  │ ✘✔✘✘✘ CVE-2026-98609         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98609
  │ ✘✔✘✘✘ CVE-2026-98610         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98610
  │ ✘✔✘✘✘ CVE-2026-98612         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98612
  │ ✘✔✘✘✘ CVE-2026-98614         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98614
  │ ✘✔✘✘✘ CVE-2026-98620         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98620
  │ ✘✔✘✘✘ CVE-2026-98621         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98621
  │ ✘✔✘✘✘ CVE-2026-98623         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98623
  │ ✘✔✘✘✘ CVE-2026-98624         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98624
  │ ✘✔✘✘✘ CVE-2026-98628         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98628
  │ ✘✔✘✘✘ CVE-2026-98634         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98634
  │ ✘✔✘✘✘ CVE-2026-98636         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98636
  │ ✘✔✘✘✘ CVE-2026-98643         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98643
  │ ✘✔✘✘✘ CVE-2026-98652         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98652
  │ ✘✔✘✘✘ CVE-2026-98657         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98657
  │ ✘✔✘✘✘ CVE-2026-98662         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98662
  │ ✘✔✘✘✘ CVE-2026-98663         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98663
  │ ✘✔✘✘✘ CVE-2026-98665         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98665
  │ ✘✔✘✘✘ CVE-2026-98666         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98666
  │ ✘✔✘✘✘ CVE-2026-98671         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98671
  │ ✘✔✘✘✘ CVE-2026-98679         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98679
  │ ✘✔✘✘✘ CVE-2026-98681         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98681
  │ ✘✔✘✘✘ CVE-2026-98686         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98686
  │ ✘✔✘✘✘ CVE-2026-98687         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98687
  │ ✘✔✘✘✘ CVE-2026-98694         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98694
  │ ✘✔✘✘✘ CVE-2026-98695         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98695
  │ ✘✔✘✘✘ CVE-2026-98696         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98696
  │ ✘✔✘✘✘ CVE-2026-98697         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98697
  │ ✘✔✘✘✘ CVE-2026-98698         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98698
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
  │ ✘✔✘✘✘ CVE-2026-98722         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98722
  │ ✘✔✘✘✘ CVE-2026-98726         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98726
  │ ✘✔✘✘✘ CVE-2026-98732         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98732
  │ ✘✔✘✘✘ CVE-2026-98734         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98734
  │ ✘✔✘✘✘ CVE-2026-98735         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98735
  │ ✘✔✘✘✘ CVE-2026-98738         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98738
  │ ✘✔✘✘✘ CVE-2026-98739         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98739
  │ ✘✔✘✘✘ CVE-2026-98740         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98740
  │ ✘✔✘✘✘ CVE-2026-98741         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98741
  │ ✘✔✘✘✘ CVE-2026-98742         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98742
  │ ✘✔✘✘✘ CVE-2026-98749         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98749
  │ ✘✔✘✘✘ CVE-2026-98750         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98750
  │ ✘✔✘✘✘ CVE-2026-98751         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98751
  │ ✘✔✘✘✘ CVE-2026-98752         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98752
  │ ✘✔✘✘✘ CVE-2026-98753         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98753
  │ ✘✔✘✘✘ CVE-2026-98754         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98754
  │ ✘✔✘✘✘ CVE-2026-98755         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98755
  │ ✘✔✘✘✘ CVE-2026-98756         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98756
  │ ✘✔✘✘✘ CVE-2026-98757         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98757
  │ ✘✔✘✘✘ CVE-2026-98760         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98760
  │ ✘✔✘✘✘ CVE-2026-98762         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98762
  │ ✘✔✘✘✘ CVE-2026-98763         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98763
  │ ✘✔✘✘✘ CVE-2026-98764         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98764
  │ ✘✔✘✘✘ CVE-2026-98765         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98765
  │ ✘✔✘✘✘ CVE-2026-98766         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98766
  │ ✘✔✘✘✘ CVE-2026-98769         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98769
  │ ✘✔✘✘✘ CVE-2026-98771         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98771
  │ ✘✔✘✘✘ CVE-2026-98772         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98772
  │ ✘✔✘✘✘ CVE-2026-98779         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98779
  │ ✘✔✘✘✘ CVE-2026-98784         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98784
  │ ✘✔✘✘✘ CVE-2026-98794         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98794
  │ ✘✔✘✘✘ CVE-2026-98796         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98796
  │ ✘✔✘✘✘ CVE-2026-98798         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98798
  │ ✘✔✘✘✘ CVE-2026-98802         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98802
  │ ✘✔✘✘✘ CVE-2026-98803         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98803
  │ ✘✔✘✘✘ CVE-2026-98808         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98808
  │ ✘✔✘✘✘ CVE-2026-98810         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98810
  │ ✘✔✘✘✘ CVE-2026-98811         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98811
  │ ✘✔✘✘✘ CVE-2026-98815         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98815
  │ ✘✔✘✘✘ CVE-2026-98816         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98816
  │ ✘✔✘✘✘ CVE-2026-98819         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98819
  │ ✘✔✘✘✘ CVE-2026-98822         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98822
  │ ✘✔✘✘✘ CVE-2026-98823         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98823
  │ ✘✔✘✘✘ CVE-2026-98824         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98824
  │ ✘✔✘✘✘ CVE-2026-98826         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98826
  │ ✘✔✘✘✘ CVE-2026-98827         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98827
  │ ✘✔✘✘✘ CVE-2026-98828         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98828
  │ ✘✔✘✘✘ CVE-2026-98829         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98829
  │ ✘✔✘✘✘ CVE-2026-98831         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98831
  │ ✘✔✘✘✘ CVE-2026-98836         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98836
  │ ✘✔✘✘✘ CVE-2026-98838         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98838
  │ ✘✔✘✘✘ CVE-2026-98839         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98839
  │ ✘✔✘✘✘ CVE-2026-98846         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98846
  │ ✘✔✘✘✘ CVE-2026-98847         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98847
  │ ✘✔✘✘✘ CVE-2026-98850         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98850
  │ ✘✔✘✘✘ CVE-2026-98851         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98851
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
  │ ✘✔✘✘✘ CVE-2026-98924         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98924
  │ ✘✔✘✘✘ CVE-2026-98926         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98926
  │ ✘✔✘✘✘ CVE-2026-98929         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98929
  │ ✘✔✘✘✘ CVE-2026-98930         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98930
  │ ✘✔✘✘✘ CVE-2026-98934         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98934
  │ ✘✔✘✘✘ CVE-2026-98935         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98935
  │ ✘✔✘✘✘ CVE-2026-98937         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98937
  │ ✘✔✘✘✘ CVE-2026-98942         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98942
  │ ✘✔✘✘✘ CVE-2026-98947         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98947
  │ ✘✔✘✘✘ CVE-2026-98950         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98950
  │ ✘✔✘✘✘ CVE-2026-98954         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98954
  │ ✘✔✘✘✘ CVE-2026-98955         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98955
  │ ✘✔✘✘✘ CVE-2026-98969         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98969
  │ ✘✔✘✘✘ CVE-2026-98970         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98970
  │ ✘✔✘✘✘ CVE-2026-98972         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98972
  │ ✘✔✘✘✘ CVE-2026-98977         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98977
  │ ✘✔✘✘✘ CVE-2026-98984         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98984
  │ ✘✔✘✘✘ CVE-2026-98985         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98985
  │ ✘✔✘✘✘ CVE-2026-98989         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98989
  │ ✘✔✘✘✘ CVE-2026-98990         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98990
  │ ✘✔✘✘✘ CVE-2026-98992         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98992
  │ ✘✔✘✘✘ CVE-2026-98996         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-98996
  │ ✘✔✘✘✘ CVE-2026-99007         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99007
  │ ✘✔✘✘✘ CVE-2026-99008         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99008
  │ ✘✔✘✘✘ CVE-2026-99010         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99010
  │ ✘✔✘✘✘ CVE-2026-99015         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99015
  │ ✘✔✘✘✘ CVE-2026-99019         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99019
  │ ✘✔✘✘✘ CVE-2026-99022         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99022
  │ ✘✔✘✘✘ CVE-2026-99024         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99024
  │ ✘✔✘✘✘ CVE-2026-99025         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99025
  │ ✘✔✘✘✘ CVE-2026-99026         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99026
  │ ✘✔✘✘✘ CVE-2026-99027         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99027
  │ ✘✔✘✘✘ CVE-2026-99034         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99034
  │ ✘✔✘✘✘ CVE-2026-99035         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99035
  │ ✘✔✘✘✘ CVE-2026-99036         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99036
  │ ✘✔✘✘✘ CVE-2026-99037         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99037
  │ ✘✔✘✘✘ CVE-2026-99038         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99038
  │ ✘✔✘✘✘ CVE-2026-99039         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99039
  │ ✘✔✘✘✘ CVE-2026-99040         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99040
  │ ✘✔✘✘✘ CVE-2026-99041         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99041
  │ ✘✔✘✘✘ CVE-2026-99045         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99045
  │ ✘✔✘✘✘ CVE-2026-99052         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99052
  │ ✘✔✘✘✘ CVE-2026-99057         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99057
  │ ✘✔✘✘✘ CVE-2026-99058         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99058
  │ ✘✔✘✘✘ CVE-2026-99061         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99061
  │ ✘✔✘✘✘ CVE-2026-99063         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99063
  │ ✘✔✘✘✘ CVE-2026-99067         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99067
  │ ✘✔✘✘✘ CVE-2026-99076         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99076
  │ ✘✔✘✘✘ CVE-2026-99080         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99080
  │ ✘✔✘✘✘ CVE-2026-99087         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99087
  │ ✘✔✘✘✘ CVE-2026-99088         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99088
  │ ✘✔✘✘✘ CVE-2026-99089         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99089
  │ ✘✔✘✘✘ CVE-2026-99090         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99090
  │ ✘✔✘✘✘ CVE-2026-99095         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99095
  │ ✘✔✘✘✘ CVE-2026-99100         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99100
  │ ✘✔✘✘✘ CVE-2026-99101         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99101
  │ ✘✔✘✘✘ CVE-2026-99118         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99118
  │ ✘✔✘✘✘ CVE-2026-99121         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99121
  │ ✘✔✘✘✘ CVE-2026-99124         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99124
  │ ✘✔✘✘✘ CVE-2026-99126         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99126
  │ ✘✔✘✘✘ CVE-2026-99128         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99128
  │ ✘✔✘✘✘ CVE-2026-99132         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99132
  │ ✘✔✘✘✘ CVE-2026-99133         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99133
  │ ✘✔✘✘✘ CVE-2026-99161         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99161
  │ ✘✔✘✘✘ CVE-2026-99165         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99165
  │ ✘✔✘✘✘ CVE-2026-99166         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99166
  │ ✘✔✘✘✘ CVE-2026-99175         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99175
  │ ✘✔✘✘✘ CVE-2026-99176         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99176
  │ ✘✔✘✘✘ CVE-2026-99178         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99178
  │ ✘✔✘✘✘ CVE-2026-99181         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99181
  │ ✘✔✘✘✘ CVE-2026-99192         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99192
  │ ✘✔✘✘✘ CVE-2026-99201         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99201
  │ ✘✔✘✘✘ CVE-2026-99204         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99204
  │ ✘✔✘✘✘ CVE-2026-99206         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99206
  │ ✘✔✘✘✘ CVE-2026-99211         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99211
  │ ✘✔✘✘✘ CVE-2026-99215         ?            0.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-99215
  │ ✘✔✘✘✘ LSN-0118-1             ?             -       -   ·
  │ ✘✔✘✘✘ USN-8280-1             ?             -       -   ·
  │ ✘✔✘✘✘ USN-8389-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/login@1%3A4.8.1-1ubuntu5.20.04.5
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2013-4235          MEDIUM       4.7   0.3%   ·  ↳ S:UBUNTU-CVE-2013-4235
  │ ✘✔✘✘✔ CVE-2023-29383         LOW          3.3   0.4%   ·  ↳ S:UBUNTU-CVE-2023-29383 | V:UB:CVE-2023-29383
  │ ✘✔✘✘✔ CVE-2024-56433         LOW          3.6   0.4%   ·  ↳ S:UBUNTU-CVE-2024-56433 | V:UB:CVE-2024-56433
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/mount@2.34-0.1ubuntu9.6
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-53613         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53613
  │ ✘✔✘✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-53615
  │ ✘✔✘✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-76642
  │ ✘✔✘✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78408
  │ ✘✔✘✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78409
  │ ✘✔✘✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-78410
  │ ✘✔✘✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2025-14104
  │ ✘✔✘✘✘ CVE-2026-13595         MEDIUM       6.8   0.1%   ·  ↳ S:UBUNTU-CVE-2026-13595
  │ ✘✔✘✘✔ CVE-2026-27456         MEDIUM       4.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-27456 | V:UB:CVE-2026-27456
  │ ✘✔✘✘✘ USN-8091-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/ncurses-base@6.2-0ubuntu2.1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2025-69720         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-69720,USN-8503-1
  │ ✘✔✘✘✔ CVE-2023-50495         MEDIUM       6.5   1.0%   ·  ↳ S:UBUNTU-CVE-2023-50495 | V:UB:CVE-2023-50495
  │ ✘✔✘✘✘ CVE-2025-6141          MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-6141,USN-8709-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/ncurses-bin@6.2-0ubuntu2.1
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2025-69720         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2025-69720,USN-8503-1 | V:UB:CVE-2025-69720
  │ ✘✔✘✘✔ CVE-2023-50495         MEDIUM       6.5   1.0%   ·  ↳ S:UBUNTU-CVE-2023-50495 | V:UB:CVE-2023-50495
  │ ✘✔✘✘✔ CVE-2025-6141          MEDIUM       4.8   0.2%   ·  ↳ S:UBUNTU-CVE-2025-6141,USN-8709-1 | V:UB:CVE-2025-6141
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/openssl@1.1.1f-1ubuntu2.24
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2025-69419         HIGH         7.4   0.6%   ·  ↳ O:UBUNTU-CVE-2025-69419 | S:UBUNTU-CVE-2025-69419 | V:UB:CVE-2025-69419
  │ ✔✔✔✘✔ CVE-2025-69420         HIGH         7.5   0.9%   ·  ↳ O:UBUNTU-CVE-2025-69420 | S:UBUNTU-CVE-2025-69420 | V:UB:CVE-2025-69420
  │ ✔✔✔✘✔ CVE-2025-69421         HIGH         7.5   0.9%   ·  ↳ O:UBUNTU-CVE-2025-69421 | S:UBUNTU-CVE-2025-69421 | V:UB:CVE-2025-69421
  │ ✔✔✔✘✔ CVE-2025-9230          HIGH         7.5   1.6%   ·  ↳ O:UBUNTU-CVE-2025-9230,USN-7786-1 | S:UBUNTU-CVE-2025-9230,USN-7786-1 | V:UB:CVE-2025-9230
  │ ✔✔✔✘✔ CVE-2026-28387         HIGH         8.1   0.7%   ·  ↳ O:UBUNTU-CVE-2026-28387 | S:UBUNTU-CVE-2026-28387 | V:UB:CVE-2026-28387
  │ ✔✔✔✘✔ CVE-2026-28388         HIGH         7.5   0.9%   ·  ↳ O:UBUNTU-CVE-2026-28388 | S:UBUNTU-CVE-2026-28388 | V:UB:CVE-2026-28388
  │ ✔✔✔✘✔ CVE-2026-28389         HIGH         7.5   0.8%   ·  ↳ O:UBUNTU-CVE-2026-28389 | S:UBUNTU-CVE-2026-28389 | V:UB:CVE-2026-28389
  │ ✔✔✔✘✔ CVE-2026-28390         HIGH         7.5   0.8%   ·  ↳ O:UBUNTU-CVE-2026-28390 | S:UBUNTU-CVE-2026-28390 | V:UB:CVE-2026-28390
  │ ✔✔✔✘✔ CVE-2026-34180         HIGH         7.5   1.0%   ·  ↳ O:UBUNTU-CVE-2026-34180 | S:UBUNTU-CVE-2026-34180 | V:UB:CVE-2026-34180
  │ ✔✔✔✘✔ CVE-2026-45447         HIGH         8.8   4.0%   ·  ↳ O:UBUNTU-CVE-2026-45447 | S:UBUNTU-CVE-2026-45447 | V:UB:CVE-2026-45447
  │ ✔✔✔✘✔ CVE-2026-54874         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-54874,USN-8678-2 | S:UBUNTU-CVE-2026-54874,USN-8678-2 | V:UB:CVE-2026-54874
  │ ✔✔✔✘✔ CVE-2026-63072         HIGH         7.5   0.9%   ·  ↳ O:UBUNTU-CVE-2026-63072,USN-8678-2 | S:UBUNTU-CVE-2026-63072,USN-8678-2 | V:UB:CVE-2026-63072
  │ ✔✔✔✘✔ CVE-2026-7383          HIGH         8.1   0.8%   ·  ↳ O:UBUNTU-CVE-2026-7383 | S:UBUNTU-CVE-2026-7383 | V:UB:CVE-2026-7383
  │ ✔✔✔✘✔ CVE-2026-84782         HIGH         8.2   0.8%   ·  ↳ O:UBUNTU-CVE-2026-84782,USN-8847-2 | S:UBUNTU-CVE-2026-84782,USN-8847-2 | V:UB:CVE-2026-84782
  │ ✔✔✔✘✔ CVE-2026-9076          HIGH         7.5   0.7%   ·  ↳ O:UBUNTU-CVE-2026-9076 | S:UBUNTU-CVE-2026-9076 | V:UB:CVE-2026-9076
  │ ✔✔✔✘✔ CVE-2025-68160         MEDIUM       4.7   0.2%   ·  ↳ O:UBUNTU-CVE-2025-68160 | S:UBUNTU-CVE-2025-68160 | V:UB:CVE-2025-68160
  │ ✔✔✔✘✔ CVE-2025-69418         MEDIUM       4.0   0.1%   ·  ↳ O:UBUNTU-CVE-2025-69418 | S:UBUNTU-CVE-2025-69418 | V:UB:CVE-2025-69418
  │ ✔✔✔✘✔ CVE-2026-22795         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2026-22795 | S:UBUNTU-CVE-2026-22795 | V:UB:CVE-2026-22795
  │ ✔✔✔✘✔ CVE-2026-22796         MEDIUM       5.3   0.6%   ·  ↳ O:UBUNTU-CVE-2026-22796 | S:UBUNTU-CVE-2026-22796 | V:UB:CVE-2026-22796
  │ ✔✔✔✘✔ CVE-2026-35189         MEDIUM       5.3   0.3%   ·  ↳ O:UBUNTU-CVE-2026-35189,USN-8847-2 | S:UBUNTU-CVE-2026-35189,USN-8847-2 | V:UB:CVE-2026-35189
  │ ✔✔✔✘✔ CVE-2026-42766         MEDIUM       5.9   1.1%   ·  ↳ O:UBUNTU-CVE-2026-42766 | S:UBUNTU-CVE-2026-42766 | V:UB:CVE-2026-42766
  │ ✔✔✔✘✘ CVE-2026-75806         MEDIUM       5.3   1.1%   ·  ↳ O:UBUNTU-CVE-2026-75806 | S:UBUNTU-CVE-2026-75806
  │ ✔✔✔✘✔ CVE-2026-54872         LOW          3.7   0.4%   ·  ↳ O:UBUNTU-CVE-2026-54872,USN-8847-2 | S:UBUNTU-CVE-2026-54872,USN-8847-2 | V:UB:CVE-2026-54872
  │ ✔✔✔✘✔ CVE-2026-77696         LOW          3.7   0.4%   ·  ↳ O:UBUNTU-CVE-2026-77696,USN-8847-2 | S:UBUNTU-CVE-2026-77696,USN-8847-2 | V:UB:CVE-2026-77696
  │ ✔✔✘✘✘ USN-7980-2             ?             -       -   ·
  │ ✔✔✘✘✘ USN-8155-2             ?             -       -   ·
  │ ✔✔✘✘✘ USN-8414-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/packagekit@1.1.13-2ubuntu1.1
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2026-41651         HIGH         8.8   0.5%   ·  ↳ O:UBUNTU-CVE-2026-41651 | S:UBUNTU-CVE-2026-41651 | V:UB:CVE-2026-41651
  │ ✔✔✔✘✘ CVE-2026-10294         MEDIUM       5.3   0.2%   ·  ↳ O:UBUNTU-CVE-2026-10294 | S:UBUNTU-CVE-2026-10294
  │ ✔✔✔✘✔ CVE-2022-0987          LOW          3.3   0.3%   ·  ↳ O:UBUNTU-CVE-2022-0987 | S:UBUNTU-CVE-2022-0987 | V:UB:CVE-2022-0987
  │ ✔✔✔✘✔ CVE-2024-0217          LOW          3.3   0.2%   ·  ↳ O:UBUNTU-CVE-2024-0217 | S:UBUNTU-CVE-2024-0217 | V:UB:CVE-2024-0217
  │ ✔✔✘✘✘ USN-8195-3             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/packagekit-tools@1.1.13-2ubuntu1.1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-41651         HIGH         8.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-41651
  │ ✘✔✘✘✘ CVE-2026-10294         MEDIUM       5.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-10294
  │ ✘✔✘✘✔ CVE-2022-0987          LOW          3.3   0.3%   ·  ↳ S:UBUNTU-CVE-2022-0987 | V:UB:CVE-2022-0987
  │ ✘✔✘✘✔ CVE-2024-0217          LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2024-0217 | V:UB:CVE-2024-0217
  │ ✘✔✘✘✘ USN-8195-3             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/passwd@1%3A4.8.1-1ubuntu5.20.04.5
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2013-4235          MEDIUM       4.7   0.3%   ·  ↳ S:UBUNTU-CVE-2013-4235
  │ ✘✔✘✘✔ CVE-2023-29383         LOW          3.3   0.4%   ·  ↳ S:UBUNTU-CVE-2023-29383 | V:UB:CVE-2023-29383
  │ ✘✔✘✘✔ CVE-2024-56433         LOW          3.6   0.4%   ·  ↳ S:UBUNTU-CVE-2024-56433 | V:UB:CVE-2024-56433
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/patch@2.7.6-6
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2018-6952          HIGH         7.5   8.2%   ·  ↳ O:UBUNTU-CVE-2018-6952 | S:UBUNTU-CVE-2018-6952 | V:UB:CVE-2018-6952
  │ ✔✔✔✘✔ CVE-2019-20633         MEDIUM       5.5   1.0%   ·  ↳ O:UBUNTU-CVE-2019-20633 | S:UBUNTU-CVE-2019-20633 | V:UB:CVE-2019-20633
  │ ✔✔✔✘✔ CVE-2021-45261         MEDIUM       5.5   0.8%   ·  ↳ O:UBUNTU-CVE-2021-45261 | S:UBUNTU-CVE-2021-45261 | V:UB:CVE-2021-45261
  │ ✔✔✔✘✘ CVE-2026-115207        MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-115207 | S:UBUNTU-CVE-2026-115207
  │ ✔✔✔✘✔ CVE-2026-56288         MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-56288 | S:UBUNTU-CVE-2026-56288 | V:UB:CVE-2026-56289
  │ ✔✔✔✘✔ CVE-2026-56289         MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-56289 | S:UBUNTU-CVE-2026-56289 | V:UB:CVE-2026-56289
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/perl@5.30.0-9ubuntu0.5
  │ OSGTV
  │ ✔✔✔✘✘ CVE-2011-10043         CRITICAL     9.8   0.8%   ·  ↳ O:UBUNTU-CVE-2011-10043 | S:UBUNTU-CVE-2011-10043
  │ ✔✔✔✘✘ CVE-2017-20230         CRITICAL    10.0   0.6%   ·  ↳ O:UBUNTU-CVE-2017-20230 | S:UBUNTU-CVE-2017-20230
  │ ✔✔✔✘✘ CVE-2026-12087         CRITICAL     9.1   0.6%   ·  ↳ O:UBUNTU-CVE-2026-12087,USN-8675-1 | S:UBUNTU-CVE-2026-12087,USN-8675-1
  │ ✔✔✔✘✘ CVE-2026-13221         CRITICAL     9.1   0.5%   ·  ↳ O:UBUNTU-CVE-2026-13221,USN-8675-1 | S:UBUNTU-CVE-2026-13221,USN-8675-1
  │ ✔✔✔✘✘ CVE-2026-4176          CRITICAL     9.8   0.6%   ·  ↳ O:UBUNTU-CVE-2026-4176 | S:UBUNTU-CVE-2026-4176
  │ ✔✔✔✘✔ CVE-2026-42496         CRITICAL     9.1   0.5%   ·  ↳ O:UBUNTU-CVE-2026-42496,USN-8467-1 | S:UBUNTU-CVE-2026-42496,USN-8467-1 | V:UB:CVE-2026-42496
  │ ✔✔✔✘✘ CVE-2026-57433         CRITICAL     9.8   0.5%   ·  ↳ O:UBUNTU-CVE-2026-57433,USN-8675-1 | S:UBUNTU-CVE-2026-57433,USN-8675-1
  │ ✔✔✔✘✔ CVE-2026-8376          CRITICAL     9.8   0.5%   ·  ↳ O:UBUNTU-CVE-2026-8376,USN-8467-1 | S:UBUNTU-CVE-2026-8376,USN-8467-1 | V:UB:CVE-2026-8376
  │ ✔✔✔✘✘ CVE-2023-31486         HIGH         8.1   1.7%   ·  ↳ O:UBUNTU-CVE-2023-31486 | S:UBUNTU-CVE-2023-31486
  │ ✔✔✔✘✘ CVE-2023-47039         HIGH         7.8   0.4%   ·  ↳ O:UBUNTU-CVE-2023-47039 | S:UBUNTU-CVE-2023-47039
  │ ✔✔✔✘✘ CVE-2026-42497         HIGH         7.5   0.5%   ·  ↳ O:UBUNTU-CVE-2026-42497 | S:UBUNTU-CVE-2026-42497
  │ ✔✔✔✘✘ CVE-2026-48959         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-48959 | S:UBUNTU-CVE-2026-48959
  │ ✔✔✔✘✘ CVE-2026-48961         HIGH         7.3   0.3%   ·  ↳ O:UBUNTU-CVE-2026-48961 | S:UBUNTU-CVE-2026-48961
  │ ✔✔✔✘✘ CVE-2026-48962         HIGH         7.8   0.4%   ·  ↳ O:UBUNTU-CVE-2026-48962 | S:UBUNTU-CVE-2026-48962
  │ ✔✔✔✘✘ CVE-2026-57432         HIGH         8.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57432,USN-8675-1 | S:UBUNTU-CVE-2026-57432,USN-8675-1
  │ ✔✔✔✘✘ CVE-2026-7017          HIGH         7.1   0.3%   ·  ↳ O:UBUNTU-CVE-2026-7017 | S:UBUNTU-CVE-2026-7017
  │ ✔✔✔✘✘ CVE-2026-82560         HIGH         7.5   0.6%   ·  ↳ O:UBUNTU-CVE-2026-82560 | S:UBUNTU-CVE-2026-82560
  │ ✔✔✔✘✘ CVE-2026-9538          HIGH         7.5   0.5%   ·  ↳ O:UBUNTU-CVE-2026-9538 | S:UBUNTU-CVE-2026-9538
  │ ✔✔✔✘✘ CVE-2025-15649         MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2025-15649 | S:UBUNTU-CVE-2025-15649
  │ ✔✔✔✘✘ CVE-2025-40909         MEDIUM       5.9   0.5%   ·  ↳ O:UBUNTU-CVE-2025-40909 | S:UBUNTU-CVE-2025-40909
  │ ✔✔✔✘✘ CVE-2026-15534         MEDIUM       5.7   0.2%   ·  ↳ O:UBUNTU-CVE-2026-15534,USN-8736-1 | S:UBUNTU-CVE-2026-15534,USN-8736-1
  │ ✔✔✔✘✘ CVE-2026-19487         MEDIUM       5.3   0.4%   ·  ↳ O:UBUNTU-CVE-2026-19487,USN-8736-1 | S:UBUNTU-CVE-2026-19487,USN-8736-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/perl-base@5.30.0-9ubuntu0.5
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2011-10043         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2011-10043
  │ ✘✔✘✘✘ CVE-2017-20230         CRITICAL    10.0   0.6%   ·  ↳ S:UBUNTU-CVE-2017-20230
  │ ✘✔✘✘✔ CVE-2026-12087         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-12087,USN-8675-1 | V:UB:CVE-2026-12087
  │ ✘✔✘✘✔ CVE-2026-13221         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-13221,USN-8675-1 | V:UB:CVE-2026-13221
  │ ✘✔✘✘✘ CVE-2026-4176          CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-4176
  │ ✘✔✘✘✔ CVE-2026-42496         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-42496,USN-8467-1 | V:UB:CVE-2026-42496
  │ ✘✔✘✘✔ CVE-2026-57433         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-57433,USN-8675-1 | V:UB:CVE-2026-57433
  │ ✘✔✘✘✔ CVE-2026-8376          CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-8376,USN-8467-1 | V:UB:CVE-2026-8376
  │ ✘✔✘✘✘ CVE-2023-31486         HIGH         8.1   1.7%   ·  ↳ S:UBUNTU-CVE-2023-31486
  │ ✘✔✘✘✘ CVE-2023-47039         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2023-47039
  │ ✘✔✘✘✘ CVE-2026-42497         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-42497
  │ ✘✔✘✘✘ CVE-2026-48959         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-48959
  │ ✘✔✘✘✘ CVE-2026-48961         HIGH         7.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-48961
  │ ✘✔✘✘✘ CVE-2026-48962         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-48962
  │ ✘✔✘✘✔ CVE-2026-57432         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57432,USN-8675-1 | V:UB:CVE-2026-57432
  │ ✘✔✘✘✘ CVE-2026-7017          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-7017
  │ ✘✔✘✘✘ CVE-2026-82560         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-82560
  │ ✘✔✘✘✘ CVE-2026-9538          HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-9538
  │ ✘✔✘✘✘ CVE-2025-15649         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-15649
  │ ✘✔✘✘✘ CVE-2025-40909         MEDIUM       5.9   0.5%   ·  ↳ S:UBUNTU-CVE-2025-40909
  │ ✘✔✘✘✔ CVE-2026-15534         MEDIUM       5.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15534,USN-8736-1 | V:UB:CVE-2026-15534
  │ ✘✔✘✘✔ CVE-2026-19487         MEDIUM       5.3   0.4%   ·  ↳ S:UBUNTU-CVE-2026-19487,USN-8736-1 | V:UB:CVE-2026-19487
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/perl-modules-5.30@5.30.0-9ubuntu0.5
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2011-10043         CRITICAL     9.8   0.8%   ·  ↳ S:UBUNTU-CVE-2011-10043
  │ ✘✔✘✘✘ CVE-2017-20230         CRITICAL    10.0   0.6%   ·  ↳ S:UBUNTU-CVE-2017-20230
  │ ✘✔✘✘✔ CVE-2026-12087         CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-12087,USN-8675-1 | V:UB:CVE-2026-12087
  │ ✘✔✘✘✔ CVE-2026-13221         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-13221,USN-8675-1 | V:UB:CVE-2026-13221
  │ ✘✔✘✘✘ CVE-2026-4176          CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2026-4176
  │ ✘✔✘✘✔ CVE-2026-42496         CRITICAL     9.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-42496,USN-8467-1 | V:UB:CVE-2026-42496
  │ ✘✔✘✘✔ CVE-2026-57433         CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-57433,USN-8675-1 | V:UB:CVE-2026-57433
  │ ✘✔✘✘✔ CVE-2026-8376          CRITICAL     9.8   0.5%   ·  ↳ S:UBUNTU-CVE-2026-8376,USN-8467-1 | V:UB:CVE-2026-8376
  │ ✘✔✘✘✘ CVE-2023-31486         HIGH         8.1   1.7%   ·  ↳ S:UBUNTU-CVE-2023-31486
  │ ✘✔✘✘✘ CVE-2023-47039         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2023-47039
  │ ✘✔✘✘✘ CVE-2026-42497         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-42497
  │ ✘✔✘✘✘ CVE-2026-48959         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-48959
  │ ✘✔✘✘✘ CVE-2026-48961         HIGH         7.3   0.3%   ·  ↳ S:UBUNTU-CVE-2026-48961
  │ ✘✔✘✘✘ CVE-2026-48962         HIGH         7.8   0.4%   ·  ↳ S:UBUNTU-CVE-2026-48962
  │ ✘✔✘✘✔ CVE-2026-57432         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57432,USN-8675-1 | V:UB:CVE-2026-57432
  │ ✘✔✘✘✘ CVE-2026-7017          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-7017
  │ ✘✔✘✘✘ CVE-2026-82560         HIGH         7.5   0.6%   ·  ↳ S:UBUNTU-CVE-2026-82560
  │ ✘✔✘✘✘ CVE-2026-9538          HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-9538
  │ ✘✔✘✘✘ CVE-2025-15649         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-15649
  │ ✘✔✘✘✘ CVE-2025-40909         MEDIUM       5.9   0.5%   ·  ↳ S:UBUNTU-CVE-2025-40909
  │ ✘✔✘✘✘ CVE-2026-15534         MEDIUM       5.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-15534,USN-8736-1
  │ ✘✔✘✘✘ CVE-2026-19487         MEDIUM       5.3   0.4%   ·  ↳ S:UBUNTU-CVE-2026-19487,USN-8736-1
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/policykit-1@0.105-26ubuntu1.3
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2016-2568          HIGH         7.8   0.4%   ·  ↳ O:UBUNTU-CVE-2016-2568 | S:UBUNTU-CVE-2016-2568 | V:UB:CVE-2016-2568
  │ ✔✔✔✘✘ CVE-2025-7519          MEDIUM       6.7   0.2%   ·  ↳ O:UBUNTU-CVE-2025-7519 | S:UBUNTU-CVE-2025-7519
  │ ✔✔✔✘✘ CVE-2026-4897          MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2026-4897 | S:UBUNTU-CVE-2026-4897
  │ ✔✔✔✘✘ CVE-2026-85498         LOW          3.5   0.3%   ·  ↳ O:UBUNTU-CVE-2026-85498 | S:UBUNTU-CVE-2026-85498
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python-apt-common@2.0.1ubuntu0.20.04.1
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2025-6966          MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2025-6966,USN-7916-2 | V:UB:CVE-2025-6966
  │ ✘✔✘✘✘ USN-7916-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python-pip-whl@20.0.2-5ubuntu1.11
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2023-37920         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2023-37920
  │ ✘✔✘✘✘ CVE-2018-20225         HIGH         7.8   1.8%   ·  ↳ S:UBUNTU-CVE-2018-20225
  │ ✘✔✘✘✘ CVE-2024-39689         HIGH         7.5   1.0%   ·  ↳ S:UBUNTU-CVE-2024-39689
  │ ✘✘✘✘✔ CVE-2025-47273         HIGH         8.8   1.6%   ·  ↳ V:UB:CVE-2025-47273
  │ ✘✘✘✘✔ CVE-2025-66418         HIGH         8.9   0.7%   ·  ↳ V:UB:CVE-2025-66418
  │ ✘✔✘✘✘ CVE-2025-66471         HIGH         8.9   0.7%   ·  ↳ S:UBUNTU-CVE-2025-66471
  │ ✘✘✘✘✔ CVE-2026-21441         HIGH         8.9   2.9%   ·  ↳ V:UB:CVE-2026-21441
  │ ✘✔✘✘✘ CVE-2026-24049         HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-24049
  │ ✘✔✘✘✘ CVE-2026-44431         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-44431
  │ ✘✔✘✘✘ CVE-2026-44432         HIGH         8.9   0.7%   ·  ↳ S:UBUNTU-CVE-2026-44432
  │ ✘✔✘✘✘ CVE-2026-57585         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-57585
  │ ✘✔✘✘✘ CVE-2026-8643          HIGH         8.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-8643
  │ ✘✔✘✘✘ CVE-2026-97687         HIGH         8.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97687
  │ ✘✔✘✘✘ CVE-2026-97689         HIGH         8.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97689
  │ ✘✔✘✘✘ CVE-2024-35195         MEDIUM       5.6   0.3%   ·  ↳ S:UBUNTU-CVE-2024-35195
  │ ✘✔✘✘✔ CVE-2025-8869          MEDIUM       5.9   0.5%   ·  ↳ S:UBUNTU-CVE-2025-8869 | V:UB:CVE-2025-8869
  │ ✘✔✘✘✘ CVE-2026-13346         MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-13346
  │ ✘✔✘✘✘ CVE-2026-25645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-25645
  │ ✘✔✘✘✘ CVE-2026-3219          MEDIUM       4.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-3219
  │ ✘✔✘✘✘ CVE-2026-45409         MEDIUM       6.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-45409
  │ ✘✔✘✘✘ CVE-2026-6357          MEDIUM       5.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6357
  │ ✘✔✘✘✘ CVE-2026-97688         MEDIUM       6.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97688
  │ ✘✔✘✘✔ CVE-2026-1703          LOW          2.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-1703 | V:UB:CVE-2026-1703
  │ ✘✔✘✘✔ CVE-2026-9375          ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-9375 | V:UB:CVE-2026-9375
  │ ✘✔✘✘✘ USN-8010-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-apt@2.0.1ubuntu0.20.04.1
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2025-6966          MEDIUM       6.9   0.1%   ·  ↳ S:UBUNTU-CVE-2025-6966,USN-7916-2 | V:UB:CVE-2025-6966
  │ ✘✔✘✘✘ USN-7916-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-certifi@2019.11.28-1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2023-37920         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2023-37920
  │ ✘✔✘✘✘ CVE-2024-39689         HIGH         7.5   1.0%   ·  ↳ S:UBUNTU-CVE-2024-39689
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-idna@2.8-1ubuntu0.1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-45409         MEDIUM       6.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-45409
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-pip@20.0.2-5ubuntu1.11
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2023-37920         CRITICAL     9.8   0.6%   ·  ↳ S:UBUNTU-CVE-2023-37920
  │ ✘✔✘✘✘ CVE-2018-20225         HIGH         7.8   1.8%   ·  ↳ S:UBUNTU-CVE-2018-20225
  │ ✘✔✘✘✘ CVE-2024-39689         HIGH         7.5   1.0%   ·  ↳ S:UBUNTU-CVE-2024-39689
  │ ✘✘✘✘✔ CVE-2025-47273         HIGH         8.8   1.6%   ·  ↳ V:UB:CVE-2025-47273
  │ ✘✘✘✘✔ CVE-2025-66418         HIGH         8.9   0.7%   ·  ↳ V:UB:CVE-2025-66418
  │ ✘✔✘✘✘ CVE-2025-66471         HIGH         8.9   0.7%   ·  ↳ S:UBUNTU-CVE-2025-66471
  │ ✘✘✘✘✔ CVE-2026-21441         HIGH         8.9   2.9%   ·  ↳ V:UB:CVE-2026-21441
  │ ✘✔✘✘✘ CVE-2026-24049         HIGH         7.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-24049
  │ ✘✔✘✘✘ CVE-2026-44431         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-44431
  │ ✘✔✘✘✘ CVE-2026-44432         HIGH         8.9   0.7%   ·  ↳ S:UBUNTU-CVE-2026-44432
  │ ✘✔✘✘✘ CVE-2026-57585         HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-57585
  │ ✘✔✘✘✘ CVE-2026-8643          HIGH         8.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-8643
  │ ✘✔✘✘✘ CVE-2026-97687         HIGH         8.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-97687
  │ ✘✔✘✘✘ CVE-2026-97689         HIGH         8.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97689
  │ ✘✔✘✘✘ CVE-2024-35195         MEDIUM       5.6   0.3%   ·  ↳ S:UBUNTU-CVE-2024-35195
  │ ✘✔✘✘✔ CVE-2025-8869          MEDIUM       5.9   0.5%   ·  ↳ S:UBUNTU-CVE-2025-8869 | V:UB:CVE-2025-8869
  │ ✘✔✘✘✘ CVE-2026-13346         MEDIUM       6.5   0.3%   ·  ↳ S:UBUNTU-CVE-2026-13346
  │ ✘✔✘✘✘ CVE-2026-25645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-25645
  │ ✘✔✘✘✘ CVE-2026-3219          MEDIUM       4.6   0.1%   ·  ↳ S:UBUNTU-CVE-2026-3219
  │ ✘✔✘✘✘ CVE-2026-45409         MEDIUM       6.9   0.4%   ·  ↳ S:UBUNTU-CVE-2026-45409
  │ ✘✔✘✘✘ CVE-2026-6357          MEDIUM       5.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-6357
  │ ✘✔✘✘✘ CVE-2026-97688         MEDIUM       6.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97688
  │ ✘✔✘✘✔ CVE-2026-1703          LOW          2.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-1703 | V:UB:CVE-2026-1703
  │ ✘✔✘✘✔ CVE-2026-9375          ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-9375 | V:UB:CVE-2026-9375
  │ ✘✔✘✘✘ USN-8010-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-pkg-resources@45.2.0-1ubuntu0.3
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-59890         MEDIUM       6.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-59890
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-requests@2.22.0-2ubuntu1.1
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2024-35195         MEDIUM       5.6   0.3%   ·  ↳ S:UBUNTU-CVE-2024-35195
  │ ✘✔✘✘✔ CVE-2024-47081         MEDIUM       5.3   1.0%   ·  ↳ S:UBUNTU-CVE-2024-47081,USN-7568-1 | V:UB:CVE-2024-47081
  │ ✘✔✘✘✔ CVE-2026-25645         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2026-25645,USN-8825-1 | V:UB:CVE-2026-25645
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-setuptools@45.2.0-1ubuntu0.3
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-59890         MEDIUM       6.1   0.4%   ·  ↳ S:UBUNTU-CVE-2026-59890
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3-urllib3@1.25.8-2ubuntu0.4
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2025-66418         HIGH         8.9   0.7%   ·  ↳ S:UBUNTU-CVE-2025-66418,USN-7927-1 | V:UB:CVE-2025-66418
  │ ✘✔✘✘✘ CVE-2025-66471         HIGH         8.9   0.7%   ·  ↳ S:UBUNTU-CVE-2025-66471,USN-7927-1
  │ ✘✔✘✘✔ CVE-2026-21441         HIGH         8.9   2.9%   ·  ↳ S:UBUNTU-CVE-2026-21441 | V:UB:CVE-2026-21441
  │ ✘✔✘✘✔ CVE-2026-44431         HIGH         8.2   0.3%   ·  ↳ S:UBUNTU-CVE-2026-44431,USN-8811-1 | V:UB:CVE-2026-44431
  │ ✘✔✘✘✔ CVE-2026-97689         HIGH         8.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-97689,USN-8926-1 | V:UB:CVE-2026-97689
  │ ✘✔✘✘✔ CVE-2025-50181         MEDIUM       6.1   0.5%   ·  ↳ S:UBUNTU-CVE-2025-50181,USN-7599-1 | V:UB:CVE-2025-50181
  │ ✘✔✘✘✔ CVE-2026-9375          ?            0.0   0.3%   ·  ↳ S:UBUNTU-CVE-2026-9375 | V:UB:CVE-2026-9375
  │ ✘✔✘✘✘ USN-7955-1             ?             -       -   ·
  │ ✘✔✘✘✘ USN-7955-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3.8@3.8.10-0ubuntu1~20.04.18
  │ OSGTV
  │ ✔✔✔✘✘ CVE-2007-4559          CRITICAL     9.8  27.1%   ·  ↳ O:UBUNTU-CVE-2007-4559 | S:UBUNTU-CVE-2007-4559
  │ ✔✔✔✘✘ CVE-2026-115557        CRITICAL     9.4   0.5%   ·  ↳ O:UBUNTU-CVE-2026-115557 | S:UBUNTU-CVE-2026-115557
  │ ✔✔✔✘✘ CVE-2026-19445         CRITICAL     9.2   0.5%   ·  ↳ O:UBUNTU-CVE-2026-19445 | S:UBUNTU-CVE-2026-19445
  │ ✔✔✔✘✘ CVE-2026-6100          CRITICAL     9.1   0.6%   ·  ↳ O:UBUNTU-CVE-2026-6100 | S:UBUNTU-CVE-2026-6100
  │ ✔✔✔✘✘ CVE-2020-10735         HIGH         7.5   4.5%   ·  ↳ O:UBUNTU-CVE-2020-10735 | S:UBUNTU-CVE-2020-10735
  │ ✔✔✔✘✔ CVE-2025-13836         HIGH         7.5   1.7%   ·  ↳ O:UBUNTU-CVE-2025-13836,USN-7951-1 | S:UBUNTU-CVE-2025-13836,USN-7951-1 | V:UB:CVE-2025-13836
  │ ✔✔✔✘✘ CVE-2025-69534         HIGH         8.2   0.7%   ·  ↳ O:UBUNTU-CVE-2025-69534 | S:UBUNTU-CVE-2025-69534
  │ ✔✔✔✘✔ CVE-2025-8194          HIGH         7.5   0.8%   ·  ↳ O:UBUNTU-CVE-2025-8194,USN-7710-1 | S:UBUNTU-CVE-2025-8194,USN-7710-1 | V:UB:CVE-2025-8194
  │ ✔✔✔✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·  ↳ O:UBUNTU-CVE-2026-11940 | S:UBUNTU-CVE-2026-11940
  │ ✔✔✔✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·  ↳ O:UBUNTU-CVE-2026-11972 | S:UBUNTU-CVE-2026-11972
  │ ✔✔✔✘✔ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ O:UBUNTU-CVE-2026-15308,USN-8744-1 | S:UBUNTU-CVE-2026-15308,USN-8744-1 | V:UB:CVE-2026-15308
  │ ✔✔✔✘✘ CVE-2026-19553         HIGH         7.6   0.5%   ·  ↳ O:UBUNTU-CVE-2026-19553 | S:UBUNTU-CVE-2026-19553
  │ ✔✔✔✘✔ CVE-2026-3644          HIGH         7.5   0.5%   ·  ↳ O:UBUNTU-CVE-2026-3644,USN-8744-1 | S:UBUNTU-CVE-2026-3644,USN-8744-1 | V:UB:CVE-2026-3644
  │ ✔✔✔✘✔ CVE-2026-4224          HIGH         7.5   0.7%   ·  ↳ O:UBUNTU-CVE-2026-4224,USN-8744-1 | S:UBUNTU-CVE-2026-4224,USN-8744-1 | V:UB:CVE-2026-4224
  │ ✔✔✔✘✘ CVE-2026-4519          HIGH         7.1   0.3%   ·  ↳ O:UBUNTU-CVE-2026-4519 | S:UBUNTU-CVE-2026-4519
  │ ✔✔✔✘✘ CVE-2026-4786          HIGH         7.1   0.3%   ·  ↳ O:UBUNTU-CVE-2026-4786 | S:UBUNTU-CVE-2026-4786
  │ ✔✔✔✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57178 | S:UBUNTU-CVE-2026-57178
  │ ✔✔✔✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·  ↳ O:UBUNTU-CVE-2026-7210 | S:UBUNTU-CVE-2026-7210
  │ ✔✔✔✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-82049 | S:UBUNTU-CVE-2026-82049
  │ ✔✔✔✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·  ↳ O:UBUNTU-CVE-2026-84366 | S:UBUNTU-CVE-2026-84366
  │ ✔✔✔✘✘ CVE-2026-9669          HIGH         8.2   0.4%   ·  ↳ O:UBUNTU-CVE-2026-9669 | S:UBUNTU-CVE-2026-9669
  │ ✔✔✔✘✘ CVE-2021-23336         MEDIUM       5.9  40.7%   ·  ↳ O:UBUNTU-CVE-2021-23336 | S:UBUNTU-CVE-2021-23336
  │ ✔✔✔✘✔ CVE-2025-11468         MEDIUM       5.7   0.6%   ·  ↳ O:UBUNTU-CVE-2025-11468 | S:UBUNTU-CVE-2025-11468 | V:UB:CVE-2025-11468
  │ ✔✔✔✘✔ CVE-2025-12084         MEDIUM       6.3   0.8%   ·  ↳ O:UBUNTU-CVE-2025-12084 | S:UBUNTU-CVE-2025-12084 | V:UB:CVE-2025-12084
  │ ✔✔✔✘✘ CVE-2025-12781         MEDIUM       6.3   0.9%   ·  ↳ O:UBUNTU-CVE-2025-12781 | S:UBUNTU-CVE-2025-12781
  │ ✔✔✔✘✔ CVE-2025-13837         MEDIUM       5.5   0.2%   ·  ↳ O:UBUNTU-CVE-2025-13837 | S:UBUNTU-CVE-2025-13837 | V:UB:CVE-2025-13837
  │ ✔✔✔✘✔ CVE-2025-15282         MEDIUM       6.0   0.5%   ·  ↳ O:UBUNTU-CVE-2025-15282 | S:UBUNTU-CVE-2025-15282 | V:UB:CVE-2025-15282
  │ ✔✔✔✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·  ↳ O:UBUNTU-CVE-2025-15366 | S:UBUNTU-CVE-2025-15366
  │ ✔✔✔✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·  ↳ O:UBUNTU-CVE-2025-15367 | S:UBUNTU-CVE-2025-15367
  │ ✔✔✔✘✔ CVE-2025-4516          MEDIUM       5.9   0.2%   ·  ↳ O:UBUNTU-CVE-2025-4516,USN-7570-1 | S:UBUNTU-CVE-2025-4516,USN-7570-1 | V:UB:CVE-2025-4516
  │ ✔✔✔✘✔ CVE-2025-6069          MEDIUM       4.3   0.6%   ·  ↳ O:UBUNTU-CVE-2025-6069,USN-7710-1 | S:UBUNTU-CVE-2025-6069,USN-7710-1 | V:UB:CVE-2025-6069
  │ ✔✔✔✘✔ CVE-2025-6075          MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2025-6075,USN-7886-1 | S:UBUNTU-CVE-2025-6075,USN-7886-1 | V:UB:CVE-2025-6075
  │ ✔✔✔✘✔ CVE-2025-8291          MEDIUM       4.3   0.5%   ·  ↳ O:UBUNTU-CVE-2025-8291,USN-7886-1 | S:UBUNTU-CVE-2025-8291,USN-7886-1 | V:UB:CVE-2025-8291
  │ ✔✔✔✘✔ CVE-2026-0672          MEDIUM       6.0   0.5%   ·  ↳ O:UBUNTU-CVE-2026-0672 | S:UBUNTU-CVE-2026-0672 | V:UB:CVE-2026-0672
  │ ✔✔✔✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-0864 | S:UBUNTU-CVE-2026-0864
  │ ✔✔✔✘✔ CVE-2026-0865          MEDIUM       5.9   0.6%   ·  ↳ O:UBUNTU-CVE-2026-0865 | S:UBUNTU-CVE-2026-0865 | V:UB:CVE-2026-0865
  │ ✔✔✔✘✘ CVE-2026-114583        MEDIUM       6.9   0.2%   ·  ↳ O:UBUNTU-CVE-2026-114583 | S:UBUNTU-CVE-2026-114583
  │ ✔✔✔✘✘ CVE-2026-12345         MEDIUM       5.9   0.3%   ·  ↳ O:UBUNTU-CVE-2026-12345 | S:UBUNTU-CVE-2026-12345
  │ ✔✔✔✘✘ CVE-2026-1299          MEDIUM       6.0   0.6%   ·  ↳ O:UBUNTU-CVE-2026-1299 | S:UBUNTU-CVE-2026-1299
  │ ✔✔✔✘✘ CVE-2026-1502          MEDIUM       5.7   0.6%   ·  ↳ O:UBUNTU-CVE-2026-1502 | S:UBUNTU-CVE-2026-1502
  │ ✔✔✔✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·  ↳ O:UBUNTU-CVE-2026-15806 | S:UBUNTU-CVE-2026-15806
  │ ✔✔✔✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·  ↳ O:UBUNTU-CVE-2026-17084 | S:UBUNTU-CVE-2026-17084
  │ ✔✔✔✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·  ↳ O:UBUNTU-CVE-2026-19672 | S:UBUNTU-CVE-2026-19672
  │ ✔✔✔✘✔ CVE-2026-2297          MEDIUM       5.7   0.2%   ·  ↳ O:UBUNTU-CVE-2026-2297 | S:UBUNTU-CVE-2026-2297 | V:UB:CVE-2026-2297
  │ ✔✔✔✘✘ CVE-2026-3276          MEDIUM       6.3   0.5%   ·  ↳ O:UBUNTU-CVE-2026-3276 | S:UBUNTU-CVE-2026-3276
  │ ✔✔✔✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-3446 | S:UBUNTU-CVE-2026-3446
  │ ✔✔✔✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57175 | S:UBUNTU-CVE-2026-57175
  │ ✔✔✔✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57176 | S:UBUNTU-CVE-2026-57176
  │ ✔✔✔✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·  ↳ O:UBUNTU-CVE-2026-57177 | S:UBUNTU-CVE-2026-57177
  │ ✔✔✔✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·  ↳ O:UBUNTU-CVE-2026-57179 | S:UBUNTU-CVE-2026-57179
  │ ✔✔✔✘✔ CVE-2026-6019          MEDIUM       6.1   0.2%   ·  ↳ O:UBUNTU-CVE-2026-6019,USN-8744-1 | S:UBUNTU-CVE-2026-6019,USN-8744-1 | V:UB:CVE-2026-6019
  │ ✔✔✔✘✘ CVE-2026-8328          MEDIUM       5.9   0.5%   ·  ↳ O:UBUNTU-CVE-2026-8328 | S:UBUNTU-CVE-2026-8328
  │ ✔✔✔✘✘ CVE-2026-87910         MEDIUM       5.7   0.6%   ·  ↳ O:UBUNTU-CVE-2026-87910 | S:UBUNTU-CVE-2026-87910
  │ ✔✔✔✘✘ CVE-2025-13462         LOW          3.3   0.2%   ·  ↳ O:UBUNTU-CVE-2025-13462 | S:UBUNTU-CVE-2025-13462
  │ ✔✔✔✘✔ CVE-2025-1795          LOW          2.3   0.6%   ·  ↳ O:UBUNTU-CVE-2025-1795,USN-7570-1 | S:UBUNTU-CVE-2025-1795,USN-7570-1 | V:UB:CVE-2025-1795
  │ ✔✔✔✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·  ↳ O:UBUNTU-CVE-2026-15310 | S:UBUNTU-CVE-2026-15310
  │ ✔✔✔✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·  ↳ O:UBUNTU-CVE-2026-18503 | S:UBUNTU-CVE-2026-18503
  │ ✔✔✔✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·  ↳ O:UBUNTU-CVE-2026-6879 | S:UBUNTU-CVE-2026-6879
  │ ✔✔✘✘✘ USN-8018-1             ?             -       -   ·
  │ ✔✔✘✘✘ USN-8018-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3.8-dev@3.8.10-0ubuntu1~20.04.18
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2007-4559          CRITICAL     9.8  27.1%   ·  ↳ S:UBUNTU-CVE-2007-4559
  │ ✘✔✘✘✘ CVE-2026-115557        CRITICAL     9.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-115557
  │ ✘✔✘✘✘ CVE-2026-19445         CRITICAL     9.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19445
  │ ✘✔✘✘✘ CVE-2026-6100          CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-6100
  │ ✘✔✘✘✘ CVE-2020-10735         HIGH         7.5   4.5%   ·  ↳ S:UBUNTU-CVE-2020-10735
  │ ✘✔✘✘✘ CVE-2025-13836         HIGH         7.5   1.7%   ·  ↳ S:UBUNTU-CVE-2025-13836,USN-7951-1
  │ ✘✔✘✘✘ CVE-2025-69534         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2025-69534
  │ ✘✔✘✘✘ CVE-2025-8194          HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2025-8194,USN-7710-1
  │ ✘✔✘✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-11940
  │ ✘✔✘✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2026-11972
  │ ✘✔✘✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-15308,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-19553         HIGH         7.6   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19553
  │ ✘✔✘✘✘ CVE-2026-3644          HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-3644,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-4224          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-4224,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-4519          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-4519
  │ ✘✔✘✘✘ CVE-2026-4786          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-4786
  │ ✘✔✘✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57178
  │ ✘✔✘✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-7210
  │ ✘✔✘✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-82049
  │ ✘✔✘✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-84366
  │ ✘✔✘✘✘ CVE-2026-9669          HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-9669
  │ ✘✔✘✘✘ CVE-2021-23336         MEDIUM       5.9  40.7%   ·  ↳ S:UBUNTU-CVE-2021-23336
  │ ✘✔✘✘✘ CVE-2025-11468         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-11468
  │ ✘✔✘✘✘ CVE-2025-12084         MEDIUM       6.3   0.8%   ·  ↳ S:UBUNTU-CVE-2025-12084
  │ ✘✔✘✘✘ CVE-2025-12781         MEDIUM       6.3   0.9%   ·  ↳ S:UBUNTU-CVE-2025-12781
  │ ✘✔✘✘✘ CVE-2025-13837         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-13837
  │ ✘✔✘✘✘ CVE-2025-15282         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2025-15282
  │ ✘✔✘✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15366
  │ ✘✔✘✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15367
  │ ✘✔✘✘✘ CVE-2025-4516          MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2025-4516,USN-7570-1
  │ ✘✔✘✘✘ CVE-2025-6069          MEDIUM       4.3   0.6%   ·  ↳ S:UBUNTU-CVE-2025-6069,USN-7710-1
  │ ✘✔✘✘✘ CVE-2025-6075          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-6075,USN-7886-1
  │ ✘✔✘✘✘ CVE-2025-8291          MEDIUM       4.3   0.5%   ·  ↳ S:UBUNTU-CVE-2025-8291,USN-7886-1
  │ ✘✔✘✘✘ CVE-2026-0672          MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-0672
  │ ✘✔✘✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-0864
  │ ✘✔✘✘✘ CVE-2026-0865          MEDIUM       5.9   0.6%   ·  ↳ S:UBUNTU-CVE-2026-0865
  │ ✘✔✘✘✘ CVE-2026-114583        MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-114583
  │ ✘✔✘✘✘ CVE-2026-12345         MEDIUM       5.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-12345
  │ ✘✔✘✘✘ CVE-2026-1299          MEDIUM       6.0   0.6%   ·  ↳ S:UBUNTU-CVE-2026-1299
  │ ✘✔✘✘✘ CVE-2026-1502          MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-1502
  │ ✘✔✘✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15806
  │ ✘✔✘✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·  ↳ S:UBUNTU-CVE-2026-17084
  │ ✘✔✘✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19672
  │ ✘✔✘✘✘ CVE-2026-2297          MEDIUM       5.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-2297
  │ ✘✔✘✘✘ CVE-2026-3276          MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-3276
  │ ✘✔✘✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3446
  │ ✘✔✘✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57175
  │ ✘✔✘✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57176
  │ ✘✔✘✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57177
  │ ✘✔✘✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57179
  │ ✘✔✘✘✘ CVE-2026-6019          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6019,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-8328          MEDIUM       5.9   0.5%   ·  ↳ S:UBUNTU-CVE-2026-8328
  │ ✘✔✘✘✘ CVE-2026-87910         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-87910
  │ ✘✔✘✘✘ CVE-2025-13462         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2025-13462
  │ ✘✔✘✘✘ CVE-2025-1795          LOW          2.3   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1795,USN-7570-1
  │ ✘✔✘✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15310
  │ ✘✔✘✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18503
  │ ✘✔✘✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-6879
  │ ✘✔✘✘✘ USN-8018-1             ?             -       -   ·
  │ ✘✔✘✘✘ USN-8018-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/python3.8-minimal@3.8.10-0ubuntu1~20.04.18
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2007-4559          CRITICAL     9.8  27.1%   ·  ↳ S:UBUNTU-CVE-2007-4559
  │ ✘✔✘✘✘ CVE-2026-115557        CRITICAL     9.4   0.5%   ·  ↳ S:UBUNTU-CVE-2026-115557
  │ ✘✔✘✘✘ CVE-2026-19445         CRITICAL     9.2   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19445
  │ ✘✔✘✘✘ CVE-2026-6100          CRITICAL     9.1   0.6%   ·  ↳ S:UBUNTU-CVE-2026-6100
  │ ✘✔✘✘✘ CVE-2020-10735         HIGH         7.5   4.5%   ·  ↳ S:UBUNTU-CVE-2020-10735
  │ ✘✔✘✘✘ CVE-2025-13836         HIGH         7.5   1.7%   ·  ↳ S:UBUNTU-CVE-2025-13836,USN-7951-1
  │ ✘✔✘✘✘ CVE-2025-69534         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2025-69534
  │ ✘✔✘✘✘ CVE-2025-8194          HIGH         7.5   0.8%   ·  ↳ S:UBUNTU-CVE-2025-8194,USN-7710-1
  │ ✘✔✘✘✘ CVE-2026-11940         HIGH         7.8   0.8%   ·  ↳ S:UBUNTU-CVE-2026-11940
  │ ✘✔✘✘✘ CVE-2026-11972         HIGH         8.2   0.7%   ·  ↳ S:UBUNTU-CVE-2026-11972
  │ ✘✔✘✘✘ CVE-2026-15308         HIGH         8.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-15308,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-19553         HIGH         7.6   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19553
  │ ✘✔✘✘✘ CVE-2026-3644          HIGH         7.5   0.5%   ·  ↳ S:UBUNTU-CVE-2026-3644,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-4224          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-4224,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-4519          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-4519
  │ ✘✔✘✘✘ CVE-2026-4786          HIGH         7.1   0.3%   ·  ↳ S:UBUNTU-CVE-2026-4786
  │ ✘✔✘✘✘ CVE-2026-57178         HIGH         7.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57178
  │ ✘✔✘✘✘ CVE-2026-7210          HIGH         7.5   0.7%   ·  ↳ S:UBUNTU-CVE-2026-7210
  │ ✘✔✘✘✘ CVE-2026-82049         HIGH         8.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-82049
  │ ✘✔✘✘✘ CVE-2026-84366         HIGH         7.4   0.3%   ·  ↳ S:UBUNTU-CVE-2026-84366
  │ ✘✔✘✘✘ CVE-2026-9669          HIGH         8.2   0.4%   ·  ↳ S:UBUNTU-CVE-2026-9669
  │ ✘✔✘✘✘ CVE-2021-23336         MEDIUM       5.9  40.7%   ·  ↳ S:UBUNTU-CVE-2021-23336
  │ ✘✔✘✘✘ CVE-2025-11468         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2025-11468
  │ ✘✔✘✘✘ CVE-2025-12084         MEDIUM       6.3   0.8%   ·  ↳ S:UBUNTU-CVE-2025-12084
  │ ✘✔✘✘✘ CVE-2025-12781         MEDIUM       6.3   0.9%   ·  ↳ S:UBUNTU-CVE-2025-12781
  │ ✘✔✘✘✘ CVE-2025-13837         MEDIUM       5.5   0.2%   ·  ↳ S:UBUNTU-CVE-2025-13837
  │ ✘✔✘✘✘ CVE-2025-15282         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2025-15282
  │ ✘✔✘✘✘ CVE-2025-15366         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15366
  │ ✘✔✘✘✘ CVE-2025-15367         MEDIUM       5.9   0.4%   ·  ↳ S:UBUNTU-CVE-2025-15367
  │ ✘✔✘✘✔ CVE-2025-4516          MEDIUM       5.9   0.2%   ·  ↳ S:UBUNTU-CVE-2025-4516,USN-7570-1 | V:UB:CVE-2025-4516
  │ ✘✔✘✘✘ CVE-2025-6069          MEDIUM       4.3   0.6%   ·  ↳ S:UBUNTU-CVE-2025-6069,USN-7710-1
  │ ✘✔✘✘✘ CVE-2025-6075          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2025-6075,USN-7886-1
  │ ✘✔✘✘✘ CVE-2025-8291          MEDIUM       4.3   0.5%   ·  ↳ S:UBUNTU-CVE-2025-8291,USN-7886-1
  │ ✘✔✘✘✘ CVE-2026-0672          MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-0672
  │ ✘✔✘✘✘ CVE-2026-0864          MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-0864
  │ ✘✔✘✘✘ CVE-2026-0865          MEDIUM       5.9   0.6%   ·  ↳ S:UBUNTU-CVE-2026-0865
  │ ✘✔✘✘✘ CVE-2026-114583        MEDIUM       6.9   0.2%   ·  ↳ S:UBUNTU-CVE-2026-114583
  │ ✘✔✘✘✘ CVE-2026-12345         MEDIUM       5.9   0.3%   ·  ↳ S:UBUNTU-CVE-2026-12345
  │ ✘✔✘✘✘ CVE-2026-1299          MEDIUM       6.0   0.6%   ·  ↳ S:UBUNTU-CVE-2026-1299
  │ ✘✔✘✘✘ CVE-2026-1502          MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-1502
  │ ✘✔✘✘✘ CVE-2026-15806         MEDIUM       6.0   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15806
  │ ✘✔✘✘✘ CVE-2026-17084         MEDIUM       6.0   0.7%   ·  ↳ S:UBUNTU-CVE-2026-17084
  │ ✘✔✘✘✘ CVE-2026-19672         MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-19672
  │ ✘✔✘✘✔ CVE-2026-2297          MEDIUM       5.7   0.2%   ·  ↳ S:UBUNTU-CVE-2026-2297 | V:UB:CVE-2026-2297
  │ ✘✔✘✘✘ CVE-2026-3276          MEDIUM       6.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-3276
  │ ✘✔✘✘✘ CVE-2026-3446          MEDIUM       6.0   0.2%   ·  ↳ S:UBUNTU-CVE-2026-3446
  │ ✘✔✘✘✘ CVE-2026-57175         MEDIUM       6.4   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57175
  │ ✘✔✘✘✘ CVE-2026-57176         MEDIUM       6.8   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57176
  │ ✘✔✘✘✘ CVE-2026-57177         MEDIUM       4.3   0.1%   ·  ↳ S:UBUNTU-CVE-2026-57177
  │ ✘✔✘✘✘ CVE-2026-57179         MEDIUM       4.2   0.2%   ·  ↳ S:UBUNTU-CVE-2026-57179
  │ ✘✔✘✘✘ CVE-2026-6019          MEDIUM       6.1   0.2%   ·  ↳ S:UBUNTU-CVE-2026-6019,USN-8744-1
  │ ✘✔✘✘✘ CVE-2026-8328          MEDIUM       5.9   0.5%   ·  ↳ S:UBUNTU-CVE-2026-8328
  │ ✘✔✘✘✘ CVE-2026-87910         MEDIUM       5.7   0.6%   ·  ↳ S:UBUNTU-CVE-2026-87910
  │ ✘✔✘✘✘ CVE-2025-13462         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2025-13462
  │ ✘✔✘✘✔ CVE-2025-1795          LOW          2.3   0.6%   ·  ↳ S:UBUNTU-CVE-2025-1795,USN-7570-1 | V:UB:CVE-2025-1795
  │ ✘✔✘✘✘ CVE-2026-15310         LOW          2.1   0.5%   ·  ↳ S:UBUNTU-CVE-2026-15310
  │ ✘✔✘✘✘ CVE-2026-18503         LOW          2.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-18503
  │ ✘✔✘✘✘ CVE-2026-6879          LOW          2.0   0.4%   ·  ↳ S:UBUNTU-CVE-2026-6879
  │ ✘✔✘✘✘ USN-8018-1             ?             -       -   ·
  │ ✘✔✘✘✘ USN-8018-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/sed@4.7-1
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2026-5958          LOW          2.1   0.1%   ·  ↳ O:UBUNTU-CVE-2026-5958,USN-8229-2 | S:UBUNTU-CVE-2026-5958,USN-8229-2 | V:UB:CVE-2026-5958
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/systemd@245.4-4ubuntu3.24
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2023-26604         HIGH         7.8   1.1%   ·  ↳ O:UBUNTU-CVE-2023-26604 | S:UBUNTU-CVE-2023-26604 | V:UB:CVE-2023-26604
  │ ✔✔✔✘✘ CVE-2020-13776         MEDIUM       6.7   0.5%   ·  ↳ O:UBUNTU-CVE-2020-13776 | S:UBUNTU-CVE-2020-13776
  │ ✔✔✔✘✔ CVE-2023-7008          MEDIUM       5.9   0.8%   ·  ↳ O:UBUNTU-CVE-2023-7008 | S:UBUNTU-CVE-2023-7008 | V:UB:CVE-2023-7008
  │ ✔✔✔✘✘ CVE-2025-4598          MEDIUM       4.7   1.3%   ·  ↳ O:UBUNTU-CVE-2025-4598,USN-7559-1 | S:UBUNTU-CVE-2025-4598,USN-7559-1
  │ ✔✔✔✘✔ CVE-2026-29111         MEDIUM       5.5   0.1%   ·  ↳ O:UBUNTU-CVE-2026-29111 | S:UBUNTU-CVE-2026-29111 | V:UB:CVE-2026-29111
  │ ✔✔✔✘✔ CVE-2026-40225         MEDIUM       6.4   0.1%   ·  ↳ O:UBUNTU-CVE-2026-40225 | S:UBUNTU-CVE-2026-40225 | V:UB:CVE-2026-40225
  │ ✔✔✔✘✘ CVE-2026-40226         MEDIUM       6.4   0.1%   ·  ↳ O:UBUNTU-CVE-2026-40226 | S:UBUNTU-CVE-2026-40226
  │ ✔✔✔✘✔ CVE-2026-40228         LOW          3.3   0.2%   ·  ↳ O:UBUNTU-CVE-2026-40228 | S:UBUNTU-CVE-2026-40228 | V:UB:CVE-2026-40228
  │ ✔✔✘✘✘ USN-8119-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/systemd-sysv@245.4-4ubuntu3.24
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2023-26604         HIGH         7.8   1.1%   ·  ↳ S:UBUNTU-CVE-2023-26604 | V:UB:CVE-2023-26604
  │ ✘✔✘✘✘ CVE-2020-13776         MEDIUM       6.7   0.5%   ·  ↳ S:UBUNTU-CVE-2020-13776
  │ ✘✔✘✘✔ CVE-2023-7008          MEDIUM       5.9   0.8%   ·  ↳ S:UBUNTU-CVE-2023-7008 | V:UB:CVE-2023-7008
  │ ✘✔✘✘✘ CVE-2025-4598          MEDIUM       4.7   1.3%   ·  ↳ S:UBUNTU-CVE-2025-4598,USN-7559-1
  │ ✘✔✘✘✘ CVE-2026-29111         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-29111
  │ ✘✔✘✘✔ CVE-2026-40225         MEDIUM       6.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-40225 | V:UB:CVE-2026-40225
  │ ✘✔✘✘✘ CVE-2026-40226         MEDIUM       6.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-40226
  │ ✘✔✘✘✔ CVE-2026-40228         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-40228 | V:UB:CVE-2026-40228
  │ ✘✔✘✘✘ USN-8119-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/systemd-timesyncd@245.4-4ubuntu3.24
  │ OSGTV
  │ ✘✔✘✘✔ CVE-2023-26604         HIGH         7.8   1.1%   ·  ↳ S:UBUNTU-CVE-2023-26604 | V:UB:CVE-2023-26604
  │ ✘✔✘✘✘ CVE-2020-13776         MEDIUM       6.7   0.5%   ·  ↳ S:UBUNTU-CVE-2020-13776
  │ ✘✔✘✘✔ CVE-2023-7008          MEDIUM       5.9   0.8%   ·  ↳ S:UBUNTU-CVE-2023-7008 | V:UB:CVE-2023-7008
  │ ✘✔✘✘✘ CVE-2025-4598          MEDIUM       4.7   1.3%   ·  ↳ S:UBUNTU-CVE-2025-4598,USN-7559-1
  │ ✘✔✘✘✘ CVE-2026-29111         MEDIUM       5.5   0.1%   ·  ↳ S:UBUNTU-CVE-2026-29111
  │ ✘✔✘✘✔ CVE-2026-40225         MEDIUM       6.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-40225 | V:UB:CVE-2026-40225
  │ ✘✔✘✘✘ CVE-2026-40226         MEDIUM       6.4   0.1%   ·  ↳ S:UBUNTU-CVE-2026-40226
  │ ✘✔✘✘✔ CVE-2026-40228         LOW          3.3   0.2%   ·  ↳ S:UBUNTU-CVE-2026-40228 | V:UB:CVE-2026-40228
  │ ✘✔✘✘✘ USN-8119-2             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/tar@1.30%2Bdfsg-7ubuntu0.20.04.4
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2025-45582         MEDIUM       4.1   0.5%   ·  ↳ O:UBUNTU-CVE-2025-45582 | S:UBUNTU-CVE-2025-45582 | V:UB:CVE-2025-45582
  │ ✔✔✔✘✔ CVE-2026-18477         MEDIUM       4.4   0.1%   ·  ↳ O:UBUNTU-CVE-2026-18477 | S:UBUNTU-CVE-2026-18477 | V:UB:CVE-2026-18477
  │ ✔✔✔✘✔ CVE-2026-18508         MEDIUM       4.4   0.1%   ·  ↳ O:UBUNTU-CVE-2026-18508 | S:UBUNTU-CVE-2026-18508 | V:UB:CVE-2026-18508
  │ ✔✔✔✘✔ CVE-2026-5704          MEDIUM       5.5   0.4%   ·  ↳ O:UBUNTU-CVE-2026-5704,USN-8477-2,USN-8477-3 | S:UBUNTU-CVE-2026-5704,USN-8477-2,USN-8477-3 | V:UB:CVE-2026-5704
  │ ✔✔✘✘✘ USN-8477-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/util-linux@2.34-0.1ubuntu9.6
  │ OSGTV
  │ ✔✔✔✘✘ CVE-2026-53613         HIGH         7.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-53613 | S:UBUNTU-CVE-2026-53613
  │ ✔✔✔✘✘ CVE-2026-53615         HIGH         8.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-53615 | S:UBUNTU-CVE-2026-53615
  │ ✔✔✔✘✘ CVE-2026-76642         HIGH         8.5   0.2%   ·  ↳ O:UBUNTU-CVE-2026-76642 | S:UBUNTU-CVE-2026-76642
  │ ✔✔✔✘✘ CVE-2026-78408         HIGH         7.9   0.2%   ·  ↳ O:UBUNTU-CVE-2026-78408 | S:UBUNTU-CVE-2026-78408
  │ ✔✔✔✘✘ CVE-2026-78409         HIGH         7.0   0.2%   ·  ↳ O:UBUNTU-CVE-2026-78409 | S:UBUNTU-CVE-2026-78409
  │ ✔✔✔✘✘ CVE-2026-78410         HIGH         7.8   0.2%   ·  ↳ O:UBUNTU-CVE-2026-78410 | S:UBUNTU-CVE-2026-78410
  │ ✔✔✔✘✘ CVE-2025-14104         MEDIUM       6.1   0.2%   ·  ↳ O:UBUNTU-CVE-2025-14104 | S:UBUNTU-CVE-2025-14104
  │ ✔✔✔✘✘ CVE-2026-13595         MEDIUM       6.8   0.1%   ·  ↳ O:UBUNTU-CVE-2026-13595 | S:UBUNTU-CVE-2026-13595
  │ ✔✔✔✘✔ CVE-2026-27456         MEDIUM       4.7   0.2%   ·  ↳ O:UBUNTU-CVE-2026-27456 | S:UBUNTU-CVE-2026-27456 | V:UB:CVE-2026-27456
  │ ✔✔✘✘✘ USN-8091-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/xz-utils@5.2.4-1ubuntu1.1
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2026-34743         MEDIUM       6.3   0.5%   ·  ↳ O:UBUNTU-CVE-2026-34743,USN-8362-1 | S:UBUNTU-CVE-2026-34743,USN-8362-1 | V:UB:CVE-2026-34743
  │ ✔✔✘✘✘ USN-8945-1             ?             -       -   ·
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/zlib1g@1%3A1.2.11.dfsg-2ubuntu1.5
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-85091         HIGH         8.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-85091
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:deb/ubuntu/zlib1g-dev@1%3A1.2.11.dfsg-2ubuntu1.5
  │ OSGTV
  │ ✘✔✘✘✘ CVE-2026-85091         HIGH         8.3   0.5%   ·  ↳ S:UBUNTU-CVE-2026-85091
  └────────────────────────────────────────────────────────────────────────────────────────────────────

  ━━ Go ━━
  ┌─ pkg:golang/github.com/aws/aws-sdk-go-v2/service/sso@v1.22.4
  │ OSGTV
  │ ✘✘✘✘✔ WS-2026-0065           MEDIUM       6.3      -   ·  ↳ V:MEND:WS-2026-0065
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/aws/aws-sdk-go-v2/service/ssooidc@v1.26.4
  │ OSGTV
  │ ✘✘✘✘✔ WS-2026-0065           MEDIUM       6.3      -   ·  ↳ V:MEND:WS-2026-0065
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/aws/aws-sdk-go-v2/service/sts@v1.30.3
  │ OSGTV
  │ ✘✘✘✘✔ WS-2026-0065           MEDIUM       6.3      -   ·  ↳ V:MEND:WS-2026-0065
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/containerd/containerd/v2@v2.0.4
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-53488         CRITICAL     9.4   0.2%   ·  ↳ O:GHSA-xhf5-7wjv-pqxp,GO-2026-5758 | S:GHSA-xhf5-7wjv-pqxp,GO-2026-5758 | V:MEND:CVE-2026-53488
  │ ✔✔✔✔✔ CVE-2024-25621         HIGH         7.8   0.2%   ·  ↳ O:GHSA-pwhc-rpq9-4c8w,GO-2025-4100 | S:GHSA-pwhc-rpq9-4c8w,GO-2025-4100 | V:GHSA-PWHC-RPQ9-4C8W
  │ ✔✔✔✔✔ CVE-2025-47291         HIGH         7.5   0.3%   ·  ↳ O:GHSA-cxfp-7pvr-95ff,GO-2025-3701 | S:GHSA-cxfp-7pvr-95ff,GO-2025-3701 | V:MEND:CVE-2025-47291
  │ ✔✔✔✔✔ CVE-2026-46680         HIGH         7.8   0.2%   ·  ↳ O:GHSA-fqw6-gf59-qr4w,GO-2026-5378 | S:GHSA-fqw6-gf59-qr4w,GO-2026-5378 | V:MEND:CVE-2026-46680
  │ ✔✔✔✔✔ CVE-2025-64329         MEDIUM       6.9   0.2%   ·  ↳ O:GHSA-m6hq-p25p-ffr2,GO-2025-4108 | S:GHSA-m6hq-p25p-ffr2,GO-2025-4108 | V:MEND:CVE-2025-64329
  │ ✔✔✔✔✔ CVE-2026-47262         MEDIUM       5.5   0.3%   ·  ↳ O:GHSA-jpcc-p29g-p8mq,GO-2026-5475 | S:GHSA-jpcc-p29g-p8mq,GO-2026-5475 | V:MEND:CVE-2026-47262
  │ ✔✔✔✔✔ CVE-2026-53493         MEDIUM       6.9   0.4%   ·  ↳ O:GHSA-pg57-6jwg-q645,GO-2026-6597 | S:GHSA-pg57-6jwg-q645,GO-2026-6597 | V:MEND:CVE-2026-53493
  │ ✔✔✔✔✔ CVE-2026-53495         MEDIUM       6.8   0.2%   ·  ↳ O:GHSA-7jxh-36q5-gcqv,GO-2026-6444 | S:GHSA-7jxh-36q5-gcqv,GO-2026-6444 | V:GHSA-7JXH-36Q5-GCQV
  │ ✔✔✔✔✔ CVE-2026-95838         MEDIUM       4.6   0.2%   ·  ↳ O:GHSA-rp3h-jf77-q9p4,GO-2026-6796 | S:GHSA-rp3h-jf77-q9p4,GO-2026-6796 | V:MEND:CVE-2026-95838
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/buildx@v0.23.0
  │ OSGTV
  │ ✘✘✘✘✔ CVE-2026-103433        MEDIUM       6.9   0.3%   ·  ↳ V:MEND:CVE-2026-103433
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/cli@v28.0.4%2Bincompatible
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2025-15558         HIGH         8.0   0.5%   ·  ↳ O:GHSA-p436-gjf2-799p,GO-2026-4610 | S:GHSA-p436-gjf2-799p,GO-2026-4610 | V:GHSA-P436-GJF2-799P
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/cli@v28.1.0%2Bincompatible
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2025-15558         HIGH         8.0   0.5%   ·  ↳ O:GHSA-p436-gjf2-799p,GO-2026-4610 | S:GHSA-p436-gjf2-799p,GO-2026-4610 | V:GHSA-P436-GJF2-799P
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/compose/v2@v2.35.1
  │ OSGTV
  │ ✔✔✔✘✔ CVE-2025-15558         HIGH         8.0   0.5%   ·  ↳ O:GO-2026-4610 | S:GO-2026-4610 | V:OSV:GO-2026-4610
  │ ✔✔✔✔✔ CVE-2025-62725         HIGH         8.9  13.7%   ·  ↳ O:GHSA-gv8h-7v7w-r22q,GO-2025-4077 | S:GHSA-gv8h-7v7w-r22q,GO-2025-4077 | V:MEND:CVE-2025-62725
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/distribution@v2.8.3%2Bincompatible
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-85747         MEDIUM       6.8   0.2%   ·  ↳ O:GHSA-685w-q87j-wqw3 | S:GHSA-685w-q87j-wqw3 | V:OSV:GHSA-685W-Q87J-WQW3
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/docker@v28.0.4%2Bincompatible
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-33997         HIGH         8.4   0.4%   ·  ↳ O:GHSA-pxq6-2prw-chj9,GO-2026-4883 | S:GHSA-pxq6-2prw-chj9,GO-2026-4883 | V:OSV:GO-2026-4883
  │ ✔✔✔✘✔ CVE-2026-34040         HIGH         8.8   9.3%   ·  ↳ O:GO-2026-4887 | S:GO-2026-4887 | V:OSV:GO-2026-4887
  │ ✔✔✔✔✔ CVE-2026-41567         HIGH         7.5   0.2%   ·  ↳ O:GHSA-x86f-5xw2-fm2r,GO-2026-5746 | S:GHSA-x86f-5xw2-fm2r,GO-2026-5746 | V:OSV:GO-2026-5746
  │ ✔✔✔✔✔ CVE-2026-42306         HIGH         7.2   0.1%   ·  ↳ O:GHSA-rg2x-37c3-w2rh,GO-2026-5617 | S:GHSA-rg2x-37c3-w2rh,GO-2026-5617 | V:OSV:GO-2026-5617
  │ ✔✔✔✔✔ CVE-2026-41568         MEDIUM       6.1   0.1%   ·  ↳ O:GHSA-vp62-88p7-qqf5,GO-2026-5668 | S:GHSA-vp62-88p7-qqf5,GO-2026-5668 | V:OSV:GO-2026-5668
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/docker/docker@v28.1.0%2Bincompatible
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-33997         HIGH         8.4   0.4%   ·  ↳ O:GHSA-pxq6-2prw-chj9,GO-2026-4883 | S:GHSA-pxq6-2prw-chj9,GO-2026-4883 | V:OSV:GO-2026-4883
  │ ✔✔✔✘✔ CVE-2026-34040         HIGH         8.8   9.3%   ·  ↳ O:GO-2026-4887 | S:GO-2026-4887 | V:OSV:GO-2026-4887
  │ ✔✔✔✔✔ CVE-2026-41567         HIGH         7.5   0.2%   ·  ↳ O:GHSA-x86f-5xw2-fm2r,GO-2026-5746 | S:GHSA-x86f-5xw2-fm2r,GO-2026-5746 | V:OSV:GO-2026-5746
  │ ✔✔✔✔✔ CVE-2026-42306         HIGH         7.2   0.1%   ·  ↳ O:GHSA-rg2x-37c3-w2rh,GO-2026-5617 | S:GHSA-rg2x-37c3-w2rh,GO-2026-5617 | V:OSV:GO-2026-5617
  │ ✔✔✔✔✔ CVE-2026-41568         MEDIUM       6.1   0.1%   ·  ↳ O:GHSA-vp62-88p7-qqf5,GO-2026-5668 | S:GHSA-vp62-88p7-qqf5,GO-2026-5668 | V:OSV:GO-2026-5668
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/go-viper/mapstructure/v2@v2.0.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2025-11065         MEDIUM       5.3   0.4%   ·  ↳ O:GHSA-2464-8j7c-4cjm,GO-2025-3900 | S:GHSA-2464-8j7c-4cjm,GO-2025-3900 | V:SNYK:GOLANG-GITHUBCOMGOVIPERMAPSTRUCTUREV2-12177854
  │ ✘✘✘✘✔ CVE-2025-52893         MEDIUM       4.5   0.3%   ·  ↳ V:SNYK:GOLANG-GITHUBCOMGOVIPERMAPSTRUCTUREV2-10558294
  │ ✔✔✔✔✔ GHSA-FV92-FJC5-JJ9H    MEDIUM       5.3      -   ·  ↳ O:GO-2025-3787 | S:GO-2025-3787 | V:GO-2025-3787,OSV:GO-2025-3787
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/gorilla/websocket@v1.5.0
  │ OSGTV
  │ ✔✔✔✔✔ GHSA-W67G-5RQW-F597    MEDIUM       6.9      -   ·  ↳ O:GO-2026-6278 | S:GO-2026-6278 | V:GO-2026-6278,OSV:GO-2026-6278
  │ ✘✘✘✘✔ GOLANG-GITHUBCOMGORILLAWEBSOCKET-19256866 MEDIUM       6.9      -   ·  ↳ V:SNYK:GOLANG-GITHUBCOMGORILLAWEBSOCKET-19256866
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/in-toto/in-toto-golang@v0.5.0
  │ OSGTV
  │ ✔✔✔✔✔ GHSA-PMWQ-PJRM-6P5R    MEDIUM       4.1      -   ·  ↳ O:GO-2026-5547 | S:GO-2026-5547 | V:GO-2026-5547,OSV:GO-2026-5547
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/klauspost/compress@v1.18.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-63209         HIGH         7.5   0.6%   ·  ↳ O:GHSA-259r-337f-4rfw,GO-2026-5841 | S:GHSA-259r-337f-4rfw,GO-2026-5841 | V:MEND:CVE-2026-63209
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/moby/buildkit@v0.21.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-33747         CRITICAL     9.8   0.5%   ·  ↳ O:GHSA-4c29-8rgm-jvjj,GO-2026-4858 | S:GHSA-4c29-8rgm-jvjj,GO-2026-4858 | V:GHSA-4C29-8RGM-JVJJ
  │ ✘✘✘✘✔ CVE-2026-15788         HIGH         7.5   0.4%   ·  ↳ V:MEND:CVE-2026-15788
  │ ✘✘✘✘✔ CVE-2026-15789         HIGH         7.5   0.3%   ·  ↳ V:MEND:CVE-2026-15789
  │ ✘✘✘✘✔ CVE-2026-15791         HIGH         7.5   0.2%   ·  ↳ V:MEND:CVE-2026-15791
  │ ✘✘✘✘✔ CVE-2026-15792         HIGH         7.5   0.2%   ·  ↳ V:MEND:CVE-2026-15792
  │ ✔✔✔✔✔ CVE-2026-33748         HIGH         8.2   0.5%   ·  ↳ O:GHSA-4vrq-3vrq-g6gg,GO-2026-4859 | S:GHSA-4vrq-3vrq-g6gg,GO-2026-4859 | V:GHSA-4VRQ-3VRQ-G6GG
  │ ✘✘✘✘✔ CVE-2026-75593         HIGH         7.2   0.5%   ·  ↳ V:MEND:CVE-2026-75593
  │ ✘✘✘✘✔ CVE-2026-93318         HIGH         7.5   0.2%   ·  ↳ V:MEND:CVE-2026-93318
  │ ✔✔✔✔✔ CVE-2026-61711         MEDIUM       5.3   0.4%   ·  ↳ O:GHSA-7236-3392-c5c6,GO-2026-6255 | S:GHSA-7236-3392-c5c6,GO-2026-6255 | V:MEND:CVE-2026-61711
  │ ✘✘✘✘✔ CVE-2026-93320         MEDIUM       6.0   0.1%   ·  ↳ V:MEND:CVE-2026-93320
  │ ✔✔✔✔✔ CVE-2026-61712         LOW          2.3   0.4%   ·  ↳ O:GHSA-72x6-4j93-7w86,GO-2026-6256 | S:GHSA-72x6-4j93-7w86,GO-2026-6256 | V:MEND:CVE-2026-61712
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/moby/go-archive@v0.1.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-17106         HIGH         7.1   0.4%   ·  ↳ O:GHSA-hfg8-hc9c-6c3h,GO-2026-6253 | S:GHSA-hfg8-hc9c-6c3h,GO-2026-6253 | V:MEND:CVE-2026-17106
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/moby/spdystream@v0.4.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-35469         HIGH         8.7   0.7%   ·  ↳ O:GHSA-pc3f-x583-g7j2,GO-2026-4958 | S:GHSA-pc3f-x583-g7j2,GO-2026-4958 | V:MEND:CVE-2026-35469
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/github.com/moby/sys/user@v0.4.0
  │ OSGTV
  │ ✘✘✘✘✔ CVE-2026-47262         MEDIUM       5.5   0.3%   ·  ↳ V:GHSA-MJCV-P78Q-W5FW
  │ ✔✔✔✔✔ CVE-2026-61801         MEDIUM       5.5   0.1%   ·  ↳ O:GHSA-mjcv-p78q-w5fw,GO-2026-6686 | S:GHSA-mjcv-p78q-w5fw,GO-2026-6686 | V:MEND:CVE-2026-61801
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp@v1.31.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-39882         MEDIUM       5.3   0.2%   ·  ↳ O:GHSA-w8rr-5gcm-pp58,GO-2026-4985 | S:GHSA-w8rr-5gcm-pp58,GO-2026-4985 | V:GHSA-W8RR-5GCM-PP58
  │ ✘✘✘✘✔ CVE-2026-44967         MEDIUM       5.3   0.2%   ·  ↳ V:OSV:GHSA-W8RR-5GCM-PP58
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace@v1.31.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-81870         LOW          2.0   0.3%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | S:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:SNYK:GOLANG-GOOPENTELEMETRYIOOTELEXPORTERSOTLPOTLPTRACE-19883902
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc@v1.31.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-81870         LOW          2.0   0.3%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | S:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:SNYK:GOLANG-GOOPENTELEMETRYIOOTELEXPORTERSOTLPOTLPTRACEOTLPTRACEGRPC-19883903
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp@v1.31.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-39882         MEDIUM       5.3   0.2%   ·  ↳ O:GHSA-w8rr-5gcm-pp58,GO-2026-4985 | S:GHSA-w8rr-5gcm-pp58,GO-2026-4985 | V:GHSA-W8RR-5GCM-PP58
  │ ✘✘✘✘✔ CVE-2026-44967         MEDIUM       5.3   0.2%   ·  ↳ V:OSV:GHSA-W8RR-5GCM-PP58
  │ ✔✔✔✔✔ CVE-2026-81870         LOW          2.0   0.3%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | S:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:SNYK:GOLANG-GOOPENTELEMETRYIOOTELEXPORTERSOTLPOTLPTRACEOTLPTRACEHTTP-19883904
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/sdk@v1.31.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-24051         HIGH         7.0   0.2%   ·  ↳ O:GHSA-9h8m-3fm2-qjrq,GO-2026-4394 | S:GHSA-9h8m-3fm2-qjrq,GO-2026-4394 | V:GHSA-HFVC-G4FC-PQHX
  │ ✔✔✔✔✔ CVE-2026-39883         HIGH         8.8   0.3%   ·  ↳ O:GHSA-hfvc-g4fc-pqhx,GO-2026-5426 | S:GHSA-hfvc-g4fc-pqhx,GO-2026-5426 | V:MEND:CVE-2026-39883
  │ ✔✔✔✔✔ CVE-2026-81869         MEDIUM       5.1   0.2%   ·  ↳ O:GHSA-p9f8-wvj8-2fg8,GO-2026-6616 | S:GHSA-p9f8-wvj8-2fg8,GO-2026-6616 | V:MEND:CVE-2026-81869
  │ ✔✔✔✔✔ CVE-2026-81870         LOW          2.0   0.3%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | S:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:MEND:CVE-2026-81870
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/go.opentelemetry.io/otel/sdk@v1.34.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-24051         HIGH         7.0   0.2%   ·  ↳ O:GHSA-9h8m-3fm2-qjrq,GO-2026-4394 | S:GHSA-9h8m-3fm2-qjrq,GO-2026-4394 | V:GHSA-HFVC-G4FC-PQHX
  │ ✔✔✔✔✔ CVE-2026-39883         HIGH         8.8   0.3%   ·  ↳ O:GHSA-hfvc-g4fc-pqhx,GO-2026-5426 | S:GHSA-hfvc-g4fc-pqhx,GO-2026-5426 | V:MEND:CVE-2026-39883
  │ ✔✔✔✔✔ CVE-2026-81870         LOW          2.0   0.3%   ·  ↳ O:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | S:GHSA-8wmf-6v46-5gfg,GO-2026-6505 | V:MEND:CVE-2026-81870
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/crypto@v0.37.0
  │ OSGTV
  │ ✘✘✘✘✔ CVE-2024-45337         CRITICAL     9.1   3.2%   ·  ↳ V:MEND:CVE-2026-46595
  │ ✔✔✔✔✔ CVE-2026-39830         CRITICAL     9.1   0.7%   ·  ↳ O:GHSA-vgwf-h737-ff37,GO-2026-5017 | S:GHSA-vgwf-h737-ff37,GO-2026-5017 | V:MEND:CVE-2026-39830
  │ ✔✔✔✔✔ CVE-2026-39831         CRITICAL     9.1   0.5%   ·  ↳ O:GHSA-89gr-r52h-f8rx,GO-2026-5019 | S:GHSA-89gr-r52h-f8rx,GO-2026-5019 | V:MEND:CVE-2026-39831
  │ ✔✔✔✔✔ CVE-2026-39832         CRITICAL     9.1   0.7%   ·  ↳ O:GHSA-f5wc-c3c7-36mc,GO-2026-5006 | S:GHSA-f5wc-c3c7-36mc,GO-2026-5006 | V:MEND:CVE-2026-39832
  │ ✔✔✔✔✔ CVE-2026-39833         CRITICAL     9.1   0.5%   ·  ↳ O:GHSA-jppx-rxg9-jmrx,GO-2026-5005 | S:GHSA-jppx-rxg9-jmrx,GO-2026-5005 | V:MEND:CVE-2026-39833
  │ ✔✔✔✔✔ CVE-2026-39834         CRITICAL     9.1   0.6%   ·  ↳ O:GHSA-rm3j-f69w-wqmq,GO-2026-5020 | S:GHSA-rm3j-f69w-wqmq,GO-2026-5020 | V:MEND:CVE-2026-39834
  │ ✔✔✔✔✔ CVE-2026-42508         CRITICAL     9.1   6.9%   ·  ↳ O:GHSA-5cgq-3rg8-m6cv,GO-2026-5021 | S:GHSA-5cgq-3rg8-m6cv,GO-2026-5021 | V:MEND:CVE-2026-42508
  │ ✔✔✔✔✔ CVE-2026-46595         CRITICAL    10.0   0.6%   ·  ↳ O:GHSA-x527-x647-q7gg,GO-2026-5023 | S:GHSA-x527-x647-q7gg,GO-2026-5023 | V:OSV:GO-2026-6303
  │ ✔✔✔✔✔ CVE-2025-47913         HIGH         7.5   0.7%   ·  ↳ O:GO-2025-4116 | S:GO-2025-4116 | V:OSV:GO-2025-4116
  │ ✔✔✔✔✔ CVE-2026-39828         HIGH         8.8   0.4%   ·  ↳ O:GHSA-45gg-vh54-h5m9,GO-2026-5014 | S:GHSA-45gg-vh54-h5m9,GO-2026-5014 | V:MEND:CVE-2026-39828
  │ ✔✔✔✔✔ CVE-2026-39829         HIGH         7.5   0.5%   ·  ↳ O:GHSA-w879-237q-wc7r,GO-2026-5018 | S:GHSA-w879-237q-wc7r,GO-2026-5018 | V:MEND:CVE-2026-39829
  │ ✔✔✔✔✔ CVE-2026-39835         HIGH         7.5   0.5%   ·  ↳ O:GHSA-78mq-xcr3-xm33,GO-2026-5015 | S:GHSA-78mq-xcr3-xm33,GO-2026-5015 | V:MEND:CVE-2026-39835
  │ ✔✔✔✔✔ CVE-2026-46597         HIGH         7.5   0.5%   ·  ↳ O:GHSA-q4h4-gmj2-qvw2,GO-2026-5013 | S:GHSA-q4h4-gmj2-qvw2,GO-2026-5013 | V:MEND:CVE-2026-46597
  │ ✔✔✔✔✔ CVE-2026-56854         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6303 | S:GO-2026-6303 | V:MEND:CVE-2026-56854
  │ ✔✔✔✔✔ CVE-2026-56855         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6355 | S:GO-2026-6355 | V:MEND:CVE-2026-56855
  │ ✔✔✔✔✔ CVE-2026-78662         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6354 | S:GO-2026-6354 | V:MEND:CVE-2026-78662
  │ ✔✔✔✔✔ CVE-2025-47914         MEDIUM       5.3   0.5%   ·  ↳ O:GHSA-f6x5-jh6r-wrfv,GO-2025-4135 | S:GHSA-f6x5-jh6r-wrfv,GO-2025-4135 | V:MEND:CVE-2025-47914
  │ ✔✔✔✔✔ CVE-2025-58181         MEDIUM       5.3   0.6%   ·  ↳ O:GHSA-j5w8-q4qc-rx2x,GO-2025-4134 | S:GHSA-j5w8-q4qc-rx2x,GO-2025-4134 | V:MEND:CVE-2025-58181
  │ ✔✔✔✔✔ CVE-2026-39827         MEDIUM       6.5   0.3%   ·  ↳ O:GHSA-qpw4-5x99-6vjp,GO-2026-5016 | S:GHSA-qpw4-5x99-6vjp,GO-2026-5016 | V:MEND:CVE-2026-39827
  │ ✔✔✔✔✔ CVE-2026-46598         MEDIUM       5.3   0.4%   ·  ↳ O:GHSA-9m57-25v3-79x9,GO-2026-5033 | S:GHSA-9m57-25v3-79x9,GO-2026-5033 | V:MEND:CVE-2026-46598
  │ ✔✔✔✔✔ GO-2026-5932           ?            0.0      -   ·  ↳ V:OSV:GO-2026-5932
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/net@v0.39.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-39821         CRITICAL     9.6   1.8%   ·  ↳ O:GO-2026-5026 | S:GO-2026-5026 | V:MEND:CVE-2026-39821
  │ ✔✔✔✔✔ CVE-2026-78663         CRITICAL     9.1   0.6%   ·  ↳ O:GO-2026-6612 | S:GO-2026-6612 | V:MEND:CVE-2026-78663
  │ ✔✔✔✔✔ CVE-2026-33814         HIGH         7.5   0.8%   ·  ↳ O:GO-2026-4918 | S:GO-2026-4918 | V:MEND:CVE-2026-33814
  │ ✔✔✔✔✔ CVE-2026-46600         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-5942 | S:GO-2026-5942 | V:MEND:CVE-2026-46600
  │ ✔✔✔✔✔ CVE-2026-78659         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6603 | S:GO-2026-6603 | V:MEND:CVE-2026-78659
  │ ✔✔✔✔✔ CVE-2026-78660         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-6610 | S:GO-2026-6610 | V:MEND:CVE-2026-78660
  │ ✔✔✔✔✔ CVE-2026-78669         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-6611 | S:GO-2026-6611 | V:MEND:CVE-2026-78669
  │ ✔✔✔✔✔ CVE-2026-97032         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6617 | S:GO-2026-6617 | V:MEND:CVE-2026-97032
  │ ✔✔✔✔✔ CVE-2025-47911         MEDIUM       5.3   0.6%   ·  ↳ O:GO-2026-4440 | S:GO-2026-4440 | V:OSV:GO-2026-4440
  │ ✔✔✔✔✔ CVE-2025-58190         MEDIUM       5.3   0.5%   ·  ↳ O:GO-2026-4441 | S:GO-2026-4441 | V:OSV:GO-2026-4441
  │ ✔✔✔✔✔ CVE-2026-25680         MEDIUM       6.5   0.3%   ·  ↳ O:GHSA-5cv4-jp36-h3mw,GO-2026-5028 | S:GHSA-5cv4-jp36-h3mw,GO-2026-5028 | V:GHSA-5CV4-JP36-H3MW
  │ ✔✔✔✔✔ CVE-2026-25681         MEDIUM       6.1   0.2%   ·  ↳ O:GO-2026-5029 | S:GO-2026-5029 | V:MEND:CVE-2026-25681
  │ ✔✔✔✔✔ CVE-2026-27136         MEDIUM       6.1   0.2%   ·  ↳ O:GO-2026-5030 | S:GO-2026-5030 | V:MEND:CVE-2026-27136
  │ ✔✔✔✔✔ CVE-2026-42502         MEDIUM       6.1   0.2%   ·  ↳ O:GO-2026-5027 | S:GO-2026-5027 | V:MEND:CVE-2026-42502
  │ ✔✔✔✔✔ CVE-2026-42506         MEDIUM       6.1   0.2%   ·  ↳ O:GO-2026-5025 | S:GO-2026-5025 | V:MEND:CVE-2026-42506
  │ ✔✔✔✔✔ CVE-2026-78661         ?            0.0   0.2%   ·  ↳ O:GO-2026-6860 | S:GO-2026-6860 | V:OSV:GO-2026-6860
  │ ✔✔✔✔✔ CVE-2026-97045         ?            0.0   0.2%   ·  ↳ O:GO-2026-6866 | S:GO-2026-6866 | V:OSV:GO-2026-6866
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/oauth2@v0.23.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2025-22868         HIGH         7.5   0.9%   ·  ↳ O:GHSA-6v2p-p543-phr9,GO-2025-3488 | S:GHSA-6v2p-p543-phr9,GO-2025-3488 | V:MEND:CVE-2025-22868
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/oauth2@v0.25.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2025-22868         HIGH         7.5   0.9%   ·  ↳ O:GHSA-6v2p-p543-phr9,GO-2025-3488 | S:GHSA-6v2p-p543-phr9,GO-2025-3488 | V:MEND:CVE-2025-22868
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/sys@v0.32.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-39824         LOW          3.3   0.1%   ·  ↳ O:GO-2026-5024 | S:GO-2026-5024 | V:MEND:CVE-2026-39824
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/golang.org/x/text@v0.24.0
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-56851         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-6629 | S:GO-2026-6629 | V:MEND:CVE-2026-56851
  │ ✔✔✔✔✔ CVE-2026-56852         HIGH         7.5   0.5%   ·  ↳ O:GO-2026-5970 | S:GO-2026-5970 | V:MEND:CVE-2026-56852
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/google.golang.org/grpc@v1.69.4
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-33186         CRITICAL     9.1   1.6%   ·  ↳ O:GHSA-p77j-4mvh-x3m3,GO-2026-4762 | S:GHSA-p77j-4mvh-x3m3,GO-2026-4762 | V:GHSA-P77J-4MVH-X3M3
  │ ✔✔✔✔✔ CVE-2026-84304         HIGH         8.7   0.6%   ·  ↳ O:GHSA-vp52-pcj8-j9qc,GO-2026-6348 | S:GHSA-vp52-pcj8-j9qc,GO-2026-6348 | V:OSV:GO-2026-6348
  │ ✔✔✔✔✔ CVE-2026-84445         HIGH         8.7   0.6%   ·  ↳ O:GHSA-2v4p-qf9q-27wj,GO-2026-6443 | S:GHSA-2v4p-qf9q-27wj,GO-2026-6443 | V:MEND:CVE-2026-84445
  │ ✔✔✔✔✔ CVE-2026-84303         MEDIUM       6.3   0.3%   ·  ↳ O:GHSA-qc2q-p7wx-3px3,GO-2026-6441 | S:GHSA-qc2q-p7wx-3px3,GO-2026-6441 | V:OSV:GO-2026-6441
  │ ✘✘✘✘✔ WS-2026-0025           CRITICAL     9.1      -   ·  ↳ V:MEND:WS-2026-0025
  │ ✔✔✔✔✔ GHSA-HRXH-6V49-42GF    HIGH         8.8      -   ·  ↳ O:GO-2026-6061 | S:GO-2026-6061 | V:GO-2026-6061,OSV:GO-2026-6061
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/google.golang.org/grpc@v1.71.1
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2026-33186         CRITICAL     9.1   1.6%   ·  ↳ O:GHSA-p77j-4mvh-x3m3,GO-2026-4762 | S:GHSA-p77j-4mvh-x3m3,GO-2026-4762 | V:GHSA-P77J-4MVH-X3M3
  │ ✔✔✔✔✔ CVE-2026-84304         HIGH         8.7   0.6%   ·  ↳ O:GHSA-vp52-pcj8-j9qc,GO-2026-6348 | S:GHSA-vp52-pcj8-j9qc,GO-2026-6348 | V:OSV:GO-2026-6348
  │ ✔✔✔✔✔ CVE-2026-84445         HIGH         8.7   0.6%   ·  ↳ O:GHSA-2v4p-qf9q-27wj,GO-2026-6443 | S:GHSA-2v4p-qf9q-27wj,GO-2026-6443 | V:MEND:CVE-2026-84445
  │ ✔✔✔✔✔ CVE-2026-84303         MEDIUM       6.3   0.3%   ·  ↳ O:GHSA-qc2q-p7wx-3px3,GO-2026-6441 | S:GHSA-qc2q-p7wx-3px3,GO-2026-6441 | V:OSV:GO-2026-6441
  │ ✘✘✘✘✔ WS-2026-0025           CRITICAL     9.1      -   ·  ↳ V:MEND:WS-2026-0025
  │ ✔✔✔✔✔ GHSA-HRXH-6V49-42GF    HIGH         8.8      -   ·  ↳ O:GO-2026-6061 | S:GO-2026-6061 | V:GO-2026-6061,OSV:GO-2026-6061
  └────────────────────────────────────────────────────────────────────────────────────────────────────
  ┌─ pkg:golang/stdlib@v1.23.8
  │ OSGTV
  │ ✔✔✔✔✔ CVE-2025-68121         CRITICAL    10.0   0.9%   ·  ↳ O:GO-2026-4337 | S:GO-2026-4337 | V:OSV:GO-2026-4337
  │ ✔✔✔✔✔ CVE-2026-39821         CRITICAL     9.6   1.8%   ·  ↳ O:GO-2026-5026 | S:GO-2026-5026 | V:OSV:GO-2026-5026
  │ ✔✔✔✔✔ CVE-2026-56857         CRITICAL     9.8   0.6%   ·  ↳ O:GO-2026-6604 | S:GO-2026-6604 | V:OSV:GO-2026-6604
  │ ✔✔✔✔✔ CVE-2026-78663         CRITICAL     9.1   0.6%   ·  ↳ O:GO-2026-6612 | S:GO-2026-6612 | V:OSV:GO-2026-6612
  │ ✔✔✔✔✔ CVE-2025-47907         HIGH         7.0   0.4%   ·  ↳ O:GO-2025-3849 | S:GO-2025-3849 | V:OSV:GO-2025-3849
  │ ✔✔✔✔✔ CVE-2025-58187         HIGH         7.5   0.4%   ·  ↳ O:GO-2025-4007 | S:GO-2025-4007 | V:OSV:GO-2025-4007
  │ ✔✔✔✔✔ CVE-2025-58188         HIGH         7.5   0.4%   ·  ↳ O:GO-2025-4013 | S:GO-2025-4013 | V:OSV:GO-2025-4013
  │ ✔✔✔✔✔ CVE-2025-61723         HIGH         7.5   0.7%   ·  ↳ O:GO-2025-4009 | S:GO-2025-4009 | V:OSV:GO-2025-4009
  │ ✔✔✔✔✔ CVE-2025-61725         HIGH         7.5   0.6%   ·  ↳ O:GO-2025-4006 | S:GO-2025-4006 | V:OSV:GO-2025-4006
  │ ✔✔✔✔✔ CVE-2025-61726         HIGH         7.5   2.3%   ·  ↳ O:GO-2026-4341 | S:GO-2026-4341 | V:OSV:GO-2026-4341
  │ ✔✔✔✔✔ CVE-2025-61729         HIGH         7.5   0.5%   ·  ↳ O:GO-2025-4155 | S:GO-2025-4155 | V:OSV:GO-2025-4155
  │ ✔✔✔✔✔ CVE-2026-25679         HIGH         7.5   0.8%   ·  ↳ O:GO-2026-4601 | S:GO-2026-4601 | V:OSV:GO-2026-4601
  │ ✔✔✔✔✔ CVE-2026-27145         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-5037 | S:GO-2026-5037 | V:OSV:GO-2026-5037
  │ ✔✔✔✔✔ CVE-2026-32280         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-4947 | S:GO-2026-4947 | V:OSV:GO-2026-4947
  │ ✔✔✔✔✔ CVE-2026-32281         HIGH         7.5   0.4%   ·  ↳ O:GO-2026-4946 | S:GO-2026-4946 | V:OSV:GO-2026-4946
  │ ✔✔✔✔✔ CVE-2026-32283         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-4870 | S:GO-2026-4870 | V:OSV:GO-2026-4870
  │ ✔✔✔✔✔ CVE-2026-33811         HIGH         7.5   0.9%   ·  ↳ O:GO-2026-4981 | S:GO-2026-4981 | V:OSV:GO-2026-4981
  │ ✔✔✔✔✔ CVE-2026-33814         HIGH         7.5   0.8%   ·  ↳ O:GO-2026-4918 | S:GO-2026-4918 | V:OSV:GO-2026-4918
  │ ✔✔✔✔✔ CVE-2026-33818         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-5972 | S:GO-2026-5972 | V:OSV:GO-2026-5972
  │ ✔✔✔✔✔ CVE-2026-39820         HIGH         7.5   0.8%   ·  ↳ O:GO-2026-4986 | S:GO-2026-4986 | V:OSV:GO-2026-4986
  │ ✔✔✔✔✔ CVE-2026-39822         HIGH         7.8   0.2%   ·  ↳ O:GO-2026-4970 | S:GO-2026-4970 | V:OSV:GO-2026-4970
  │ ✔✔✔✔✔ CVE-2026-39836         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-4971 | S:GO-2026-4971 | V:OSV:GO-2026-4971
  │ ✔✔✔✔✔ CVE-2026-42499         HIGH         7.5   0.8%   ·  ↳ O:GO-2026-4977 | S:GO-2026-4977 | V:OSV:GO-2026-4977
  │ ✔✔✔✔✔ CVE-2026-42504         HIGH         7.5   0.6%   ·  ↳ O:GO-2026-5038 | S:GO-2026-5038 | V:OSV:GO-2026-5038
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
  │ ✔✔✔✔✔ CVE-2025-0913          MEDIUM       5.5   0.3%   ·  ↳ O:GO-2025-3750 | S:GO-2025-3750 | V:OSV:GO-2025-3750
  │ ✔✔✔✔✔ CVE-2025-4673          MEDIUM       6.8   0.7%   ·  ↳ O:GO-2025-3751 | S:GO-2025-3751 | V:OSV:GO-2025-3751
  │ ✔✔✔✔✔ CVE-2025-47906         MEDIUM       6.5   0.5%   ·  ↳ O:GO-2025-3956 | S:GO-2025-3956 | V:OSV:GO-2025-3956
  │ ✔✔✔✔✔ CVE-2025-47912         MEDIUM       5.3   0.5%   ·  ↳ O:GO-2025-4010 | S:GO-2025-4010 | V:OSV:GO-2025-4010
  │ ✔✔✔✔✔ CVE-2025-58183         MEDIUM       4.3   0.4%   ·  ↳ O:GO-2025-4014 | S:GO-2025-4014 | V:OSV:GO-2025-4014
  │ ✔✔✔✔✔ CVE-2025-58185         MEDIUM       5.3   0.6%   ·  ↳ O:GO-2025-4011 | S:GO-2025-4011 | V:OSV:GO-2025-4011
  │ ✔✔✔✔✔ CVE-2025-58186         MEDIUM       5.3   0.6%   ·  ↳ O:GO-2025-4012 | S:GO-2025-4012 | V:OSV:GO-2025-4012
  │ ✔✔✔✔✔ CVE-2025-58189         MEDIUM       5.3   0.5%   ·  ↳ O:GO-2025-4008 | S:GO-2025-4008 | V:OSV:GO-2025-4008
  │ ✔✔✔✔✔ CVE-2025-61724         MEDIUM       5.3   0.6%   ·  ↳ O:GO-2025-4015 | S:GO-2025-4015 | V:OSV:GO-2025-4015
  │ ✔✔✔✔✔ CVE-2025-61727         MEDIUM       6.5   0.3%   ·  ↳ O:GO-2025-4175 | S:GO-2025-4175 | V:OSV:GO-2025-4175
  │ ✔✔✔✔✔ CVE-2025-61728         MEDIUM       6.5   0.7%   ·  ↳ O:GO-2026-4342 | S:GO-2026-4342 | V:OSV:GO-2026-4342
  │ ✔✔✔✔✔ CVE-2025-61730         MEDIUM       5.3   0.3%   ·  ↳ O:GO-2026-4340 | S:GO-2026-4340 | V:OSV:GO-2026-4340
  │ ✔✔✔✔✔ CVE-2026-111943        MEDIUM       6.8   0.4%   ·  ↳ O:GO-2026-6809 | S:GO-2026-6809 | V:OSV:GO-2026-6809
  │ ✔✔✔✔✔ CVE-2026-27142         MEDIUM       6.1   0.4%   ·  ↳ O:GO-2026-4603 | S:GO-2026-4603 | V:OSV:GO-2026-4982
  │ ✔✔✔✔✔ CVE-2026-32282         MEDIUM       6.4   0.3%   ·  ↳ O:GO-2026-4864 | S:GO-2026-4864 | V:OSV:GO-2026-4864
  │ ✔✔✔✔✔ CVE-2026-32288         MEDIUM       5.5   0.3%   ·  ↳ O:GO-2026-4869 | S:GO-2026-4869 | V:OSV:GO-2026-4869
  │ ✔✔✔✔✔ CVE-2026-32289         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-4865 | S:GO-2026-4865 | V:OSV:GO-2026-4865
  │ ✔✔✔✔✔ CVE-2026-39823         MEDIUM       6.1   0.4%   ·  ↳ O:GO-2026-4982 | S:GO-2026-4982 | V:OSV:GO-2026-4982
  │ ✔✔✔✔✔ CVE-2026-39825         MEDIUM       5.3   0.4%   ·  ↳ O:GO-2026-4976 | S:GO-2026-4976 | V:OSV:GO-2026-4976
  │ ✔✔✔✔✔ CVE-2026-39826         MEDIUM       6.1   0.4%   ·  ↳ O:GO-2026-4980 | S:GO-2026-4980 | V:OSV:GO-2026-4980
  │ ✔✔✔✔✔ CVE-2026-42505         MEDIUM       5.3   0.4%   ·  ↳ O:GO-2026-5856 | S:GO-2026-5856 | V:OSV:GO-2026-5856
  │ ✔✔✔✔✔ CVE-2026-42507         MEDIUM       5.3   0.4%   ·  ↳ O:GO-2026-5039 | S:GO-2026-5039 | V:OSV:GO-2026-5039
  │ ✔✔✔✔✔ CVE-2026-56858         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-6091 | S:GO-2026-6091 | V:OSV:GO-2026-6091
  │ ✔✔✔✔✔ CVE-2026-56860         MEDIUM       5.9   0.5%   ·  ↳ O:GO-2026-6218 | S:GO-2026-6218 | V:OSV:GO-2026-6218
  │ ✔✔✔✔✔ CVE-2026-94448         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-6599 | S:GO-2026-6599 | V:OSV:GO-2026-6599
  │ ✔✔✔✔✔ CVE-2026-97030         MEDIUM       6.1   0.3%   ·  ↳ O:GO-2026-6600 | S:GO-2026-6600 | V:OSV:GO-2026-6600
  │ ✔✔✔✔✔ CVE-2025-22873         LOW          3.8   0.2%   ·  ↳ O:GO-2026-4403 | S:GO-2026-4403 | V:OSV:GO-2026-4403
  │ ✔✔✔✔✔ CVE-2026-27139         LOW          2.5   0.2%   ·  ↳ O:GO-2026-4602 | S:GO-2026-4602 | V:OSV:GO-2026-4602
  └────────────────────────────────────────────────────────────────────────────────────────────────────
