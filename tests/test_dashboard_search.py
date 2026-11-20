from pathlib import Path

import pandas as pd
import pytest

from canary.dashboard.search import search


def _frame(rows):
    cols = ["cert", "name", "state", "city", "last_report", "failure_date"]
    df = pd.DataFrame(rows, columns=cols)
    df["last_report"] = pd.to_datetime(df["last_report"])
    df["failure_date"] = pd.to_datetime(df["failure_date"])
    return df


BANKS = _frame([
    (1, "Manufacturers&Traders Tr Co", "NY", "BUFFALO", "2026-06-30", None),
    (2, "First National Bank", "OH", "AKRON", "2026-06-30", None),
    (3, "First National Bank", "OH", "TOLEDO", "2010-03-31", None),
    (4, "Silicon Valley Bank", "CA", "SANTA CLARA", "2022-12-31", "2023-03-10"),
    (5, "Zebra Savings", "TX", "AUSTIN", "2026-06-30", None),
])


def test_alias_svb_direct():
    assert search("SVB", BANKS).direct == 24735


def test_alias_case_insensitive():
    assert search("  frb ", BANKS).direct == 59017


@pytest.mark.parametrize("q", ["", "   "])
def test_empty_query(q):
    r = search(q, BANKS)
    assert r.direct is None and r.suggestions == []


def test_one_letter():
    r = search("a", BANKS)
    assert len(r.suggestions) <= 8


def test_punctuation():
    r = search("Manufacturers & Traders", BANKS)
    assert 1 in [s["cert"] for s in r.suggestions]


def test_same_name_disambiguated():
    r = search("First National Bank", BANKS)
    labels = {s["cert"]: s["label"] for s in r.suggestions}
    assert "AKRON" in labels[2] and "cert 2" in labels[2]
    assert "TOLEDO" in labels[3] and "cert 3" in labels[3]
    assert r.direct is None


def test_direct_needs_clear_win():
    close = _frame([
        (1, "Citizens Bank", "PA", "A", "2026-06-30", None),
        (2, "Citizens Banks", "PA", "B", "2026-06-30", None),
    ])
    assert search("Citizens Bank", close).direct is None
    assert search("Zebra Savings", BANKS).direct == 5


def test_status_values():
    by = {s["cert"]: s["status"] for s in search("bank", BANKS, limit=8).suggestions}
    assert by[4] == "Failed Mar 10, 2023"
    assert by[3] == "Stopped reporting 2010"
    assert by[2] == "Active"


@pytest.mark.data
@pytest.mark.skipif(not Path("dashboard/data/banks.parquet").exists(), reason="banks.parquet not exported")
def test_real_banks_svb():
    banks = pd.read_parquet("dashboard/data/banks.parquet")
    assert search("silicon valley bank", banks).direct == 24735


@pytest.mark.parametrize("q", ["&", "!!!", "-"])
def test_no_alphanumerics_is_empty(q):
    r = search(q, BANKS)
    assert r.direct is None and r.suggestions == []


def test_alias_punctuation_insensitive():
    assert search("svb.", BANKS).direct == 24735
    assert search("U.S. Bank", BANKS).direct == 6548


_needs_parquet = pytest.mark.skipif(not Path("dashboard/data/banks.parquet").exists(),
                                    reason="banks.parquet not exported")


@pytest.mark.data
@_needs_parquet
@pytest.mark.parametrize("q,cert", [("M&T", 588), ("m and t", 588), ("chase", 628),
                                    ("first republic bank", 59017), ("Signature Bank", 57053)])
def test_real_alias_opens_directly(q, cert):
    banks = pd.read_parquet("dashboard/data/banks.parquet")
    assert search(q, banks).direct == cert


@pytest.mark.data
@_needs_parquet
def test_real_banks_empty_punctuation():
    banks = pd.read_parquet("dashboard/data/banks.parquet")
    r = search("!!!", banks)
    assert r.direct is None and r.suggestions == []


@pytest.mark.data
@_needs_parquet
def test_alias_certs_exist_with_expected_names():
    from canary.dashboard.search import ALIASES
    banks = pd.read_parquet("dashboard/data/banks.parquet").set_index("cert")
    assert set(ALIASES.values()) <= set(banks.index)
    expect = {588: "manufacturers", 628: "jpmorgan", 3510: "bank of america", 7213: "citibank",
              3511: "wells fargo", 33124: "goldman", 6548: "u s bank", 4297: "capital one",
              6384: "pnc", 9846: "truist", 639: "new york mellon", 32992: "morgan stanley",
              14: "state street", 18409: "td bank", 6672: "fifth third", 6560: "huntington",
              16571: "bmo", 57450: "schwab", 11063: "first-citizens", 57957: "citizens bank",
              24735: "silicon valley", 57053: "signature", 59017: "first republic"}
    for cert, frag in expect.items():
        assert frag in banks.loc[cert, "name"].lower(), cert
