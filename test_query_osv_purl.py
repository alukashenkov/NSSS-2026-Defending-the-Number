#!/usr/bin/env python3
"""
Tests for query_osv_purl: dedupe_vulns' handling of Ubuntu notices, the epoch
spelling of binary-mode queries, and the slim record cache.

    python3 -m unittest test_query_osv_purl
"""

import datetime as dt
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import query_osv_purl
from query_osv_purl import binary_purl, cached_is_current, dedupe_vulns, slim_record


def ids(result):
    """{canonical_id: [source advisories]} from dedupe_vulns' output."""
    return {canon: sources for canon, sources, _ in result}


# The gnutls28 3.6.13-2ubuntu1.12 case: USN-8502-1 lists CVE-2024-0553 and
# CVE-2025-9820 in `upstream`, but OSV returned only the second one's record.
USN = {"id": "USN-8502-1", "upstream": ["CVE-2024-0553", "CVE-2025-9820",
                                       "UBUNTU-CVE-2024-0553", "UBUNTU-CVE-2025-9820"]}
OWN = {"id": "UBUNTU-CVE-2025-9820", "upstream": ["CVE-2025-9820"]}


class NoticeTests(unittest.TestCase):
    def test_notice_cve_with_own_record_is_kept(self):
        details = {r["id"]: r for r in (USN, OWN)}
        result = ids(dedupe_vulns(["USN-8502-1", "UBUNTU-CVE-2025-9820"], details))
        self.assertIn("CVE-2025-9820", result)
        self.assertEqual(result["CVE-2025-9820"], ["UBUNTU-CVE-2025-9820", "USN-8502-1"])

    def test_notice_cve_without_own_record_is_dropped(self):
        details = {r["id"]: r for r in (USN, OWN)}
        result = ids(dedupe_vulns(["USN-8502-1", "UBUNTU-CVE-2025-9820"], details))
        self.assertNotIn("CVE-2024-0553", result)
        self.assertNotIn("USN-8502-1", result)

    def test_notice_alone_adds_nothing(self):
        self.assertEqual(dedupe_vulns(["USN-8502-1"], {"USN-8502-1": USN}), [])

    def test_lsn_is_a_notice_too(self):
        lsn = {"id": "LSN-0122-1", "upstream": ["CVE-2026-1", "CVE-2026-2"]}
        own = {"id": "UBUNTU-CVE-2026-1", "upstream": ["CVE-2026-1"]}
        details = {r["id"]: r for r in (lsn, own)}
        result = ids(dedupe_vulns(["LSN-0122-1", "UBUNTU-CVE-2026-1"], details))
        self.assertEqual(result, {"CVE-2026-1": ["LSN-0122-1", "UBUNTU-CVE-2026-1"]})

    def test_notice_without_cves_stays_its_own_finding(self):
        bare = {"id": "USN-7919-1", "summary": "regression fix"}
        self.assertEqual(ids(dedupe_vulns(["USN-7919-1"], {"USN-7919-1": bare})),
                         {"USN-7919-1": []})


class RegressionTests(unittest.TestCase):
    def test_ubuntu_cve_record_carries_its_cve_in_upstream(self):
        self.assertEqual(ids(dedupe_vulns(["UBUNTU-CVE-2025-9820"], {OWN["id"]: OWN})),
                         {"CVE-2025-9820": ["UBUNTU-CVE-2025-9820"]})

    def test_related_is_not_identity(self):
        ghsa = {"id": "GHSA-w8rr-5gcm-pp58", "aliases": ["CVE-2026-39882", "GO-2026-4985"],
                "related": ["CVE-2026-44967"]}
        self.assertEqual(ids(dedupe_vulns([ghsa["id"]], {ghsa["id"]: ghsa})),
                         {"CVE-2026-39882": ["GHSA-w8rr-5gcm-pp58"]})

    def test_non_notice_with_several_cves_expands(self):
        go = {"id": "GO-2026-6303", "aliases": ["CVE-2026-1", "CVE-2026-2"]}
        self.assertEqual(set(ids(dedupe_vulns([go["id"]], {go["id"]: go}))),
                         {"CVE-2026-1", "CVE-2026-2"})


class BinaryQueryTests(unittest.TestCase):
    """OSV ignores ?epoch=, so Trivy's spelling must be moved inline to match."""

    def test_trivy_epoch_moves_inline(self):
        self.assertEqual(
            binary_purl("pkg:deb/ubuntu/diffutils@3.7-3?arch=arm64&distro=ubuntu-20.04&epoch=1"),
            "pkg:deb/ubuntu/diffutils@1%3A3.7-3?arch=arm64&distro=ubuntu-20.04")

    def test_syft_inline_epoch_is_unchanged(self):
        purl = ("pkg:deb/ubuntu/bsdutils@1%3A2.34-0.1ubuntu9.6?arch=arm64"
                "&distro=ubuntu-20.04&upstream=util-linux%402.34-0.1ubuntu9.6")
        self.assertEqual(binary_purl(purl), purl)

    def test_no_epoch_and_non_deb_are_unchanged(self):
        for purl in ("pkg:deb/ubuntu/bash@5.0-6ubuntu1.2?arch=arm64&distro=ubuntu-20.04",
                     "pkg:pypi/requests@2.19.1"):
            self.assertEqual(binary_purl(purl), purl)


class CacheTests(unittest.TestCase):
    KERNEL = {"id": "UBUNTU-CVE-2026-1", "modified": "2026-08-31T22:15:27.568721235Z",
              "upstream": ["CVE-2026-1"],
              "database_specific": {"severity": "high", "cves": ["…"]},
              "affected": [{"versions": ["5.15.0-1"] * 1000}], "details": "x" * 5000}

    def test_slim_record_keeps_only_what_dedupe_reads(self):
        slim = slim_record(self.KERNEL)
        self.assertEqual(slim, {"id": "UBUNTU-CVE-2026-1",
                                "modified": "2026-08-31T22:15:27.568721235Z", "aliases": [],
                                "upstream": ["CVE-2026-1"],
                                "database_specific": {"severity": "high"}})
        self.assertEqual(ids(dedupe_vulns([slim["id"]], {slim["id"]: slim})),
                         ids(dedupe_vulns([slim["id"]], {slim["id"]: self.KERNEL})))

    def test_slim_record_is_never_a_failure_stub(self):
        # fetch_vuln_details refetches cached entries with a single key.
        self.assertGreater(len(slim_record({"id": "PYSEC-2026-1"})), 1)

    def test_cached_record_is_reused_only_while_unchanged(self):
        cached = {**slim_record({"id": "GHSA-x"}), "modified": "2026-01-01T00:00:00Z"}
        self.assertTrue(cached_is_current(cached, "2026-01-01T00:00:00Z"))
        self.assertFalse(cached_is_current(cached, "2026-02-01T00:00:00Z"))
        self.assertTrue(cached_is_current(cached, None))       # nothing to compare
        self.assertFalse(cached_is_current({"id": "GHSA-x"}, None))  # failure stub
        self.assertFalse(cached_is_current(None, None))

    def _load(self, document):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "cache.json"
            path.write_text(json.dumps(document))
            with mock.patch.object(query_osv_purl, "CACHE_PATH", path), \
                 mock.patch.object(query_osv_purl, "_cache", {"loaded": False, "vulns": {}}):
                return query_osv_purl._load_cache()  # pylint: disable=protected-access

    def test_cache_of_current_format_is_used_whatever_its_age(self):
        doc = {"format": query_osv_purl.CACHE_FORMAT, "vulns": {"A": {"id": "A"}}}
        self.assertEqual(self._load(doc), {"A": {"id": "A"}})

    def test_older_formats_are_discarded(self):
        today = dt.date.today().isoformat()
        for doc in ({"date": today, "vulns": {"A": {}}},               # format 1
                    {"format": 2, "date": today, "vulns": {"A": {}}}):  # format 2
            self.assertEqual(self._load(doc), {})


if __name__ == "__main__":
    unittest.main()
