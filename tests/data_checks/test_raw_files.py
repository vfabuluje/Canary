"""Data checks on the real saved FDIC files (skipped when no local data)."""
import os
from datetime import date
from pathlib import Path

import pandas as pd
import pytest

from canary.quarters import quarter_ends

ROOT = Path(os.environ.get("CANARY_DATA_ROOT", Path(__file__).resolve().parents[2] / "data" / "raw"))

pytestmark = [
    pytest.mark.data,
    pytest.mark.skipif(not (ROOT / "financials").is_dir(), reason="no local data"),
]


@pytest.fixture(scope="module")
def fin():
    df = pd.read_parquet(ROOT / "financials", columns=["CERT", "REPDTE", "ASSET"])
    df["REPDTE"] = pd.to_datetime(df["REPDTE"])
    return df


@pytest.fixture(scope="module")
def failures():
    return pd.read_parquet(ROOT / "failures" / "failures.parquet")


def test_cert_repdte_unique(fin):
    assert not fin.duplicated(["CERT", "REPDTE"]).any()


def test_cert_never_null_financials(fin):
    assert fin["CERT"].notna().all()


def test_no_missing_quarters(fin):
    last = fin["REPDTE"].max().date()
    expected = set(quarter_ends(date(2001, 3, 31), last))
    assert {d.date() for d in fin["REPDTE"].unique()} == expected


def test_rows_per_quarter_in_range(fin):
    counts = fin.groupby("REPDTE").size()
    assert counts.between(3_000, 12_000).all(), counts[~counts.between(3_000, 12_000)]


def test_svb_2022q4_assets(fin):
    row = fin[(fin["CERT"] == 24735) & (fin["REPDTE"] == pd.Timestamp("2022-12-31"))]
    assert len(row) == 1
    assert row["ASSET"].iloc[0] == 209_026_000


def test_2023_failures_present(failures):
    expected = {24735: "2023-03-10", 57053: "2023-03-12", 59017: "2023-05-01"}
    got = {
        int(r.CERT): pd.Timestamp(r.FAILDATE).strftime("%Y-%m-%d")
        for r in failures.dropna(subset=["CERT"]).itertuples()
        if int(r.CERT) in expected
    }
    assert got == expected


def test_failures_cert_present_since_2001(failures):
    recent = failures[failures["FAILYR"] >= 2001]
    assert len(recent) > 0
    assert recent["CERT"].notna().all()
