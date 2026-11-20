import re
from pathlib import Path

import pytest

from canary.analyst.context import load_context
from canary.analyst.labels import PLAIN_NAMES
from canary.dashboard.cases import export_cases, phase_of
from canary.dashboard.copy import CASE_CAPTIONS

CASE_CSV = Path("data/model/case_studies.csv")
FEATURES = Path("data/features/fct_bank_features.parquet")
FAILURES = Path("data/raw/failures/failures.parquet")


@pytest.fixture(scope="module")
def cases():
    if not (CASE_CSV.exists() and FEATURES.exists() and FAILURES.exists()):
        pytest.skip("real data not present")
    ctx = load_context(FEATURES, Path("data/model"), FAILURES)
    return export_cases(ctx, CASE_CSV)


def test_case_quarter_counts(cases):
    assert len(cases[24735]) == 8
    assert len(cases[57053]) == 8
    assert len(cases[59017]) == 9
    assert cases[59017][-1]["q"] == "2023-03-31"


def test_svb_last_quarter(cases):
    last = cases[24735][-1]
    assert last["rank"] == 3494
    assert last["n"] == 4773
    assert last["weak"] == pytest.approx(98.1, abs=0.05)
    assert last["phase"] == "last"


def test_phases(cases):
    for rows in cases.values():
        for r in rows[:-1]:
            assert r["phase"] == ("before" if r["q"].startswith("2021") else "rising")
        assert rows[-1]["phase"] == "last"


def test_phase_of():
    from datetime import date
    last = date(2022, 12, 31)
    assert phase_of(date(2021, 6, 30), last) == "before"
    assert phase_of(date(2022, 6, 30), last) == "rising"
    assert phase_of(last, last) == "last"


def test_captions_have_no_digits():
    # The spec's verbatim SVB "last" caption says "2008-era", a year, not a data figure; years are allowed.
    for c in CASE_CAPTIONS.values():
        for text in c.values():
            assert not any(ch.isdigit() for ch in re.sub(r"\b(19|20)\d\d\b", "", text)), text


def test_case_signals_plain_names(cases):
    names = set(PLAIN_NAMES.values())
    for rows in cases.values():
        for r in rows:
            assert len(r["signals"]) == 3
            assert all(name in names for name, _ in r["signals"])


def test_honest_miss_matches_data(cases):
    assert all(r["pct"] < 98 for rows in cases.values() for r in rows)
