"""Data check on SVB's 2022Q4 concentration measures (skipped when no local data).
Asserts only which measure is used and that the ratios compute; nothing about crossing."""
import math
from datetime import date
from pathlib import Path

import pandas as pd
import pytest

from canary.analyst.concentration import compute_concentration

ROOT = Path(__file__).resolve().parents[2]
FEATURES = ROOT / "data" / "features" / "fct_bank_features.parquet"
CONC = ROOT / "data" / "raw" / "concentration"
SVB_CERT = 24735

pytestmark = [
    pytest.mark.data,
    pytest.mark.skipif(not (FEATURES.exists() and CONC.exists()), reason="no local data"),
]


def test_svb_2022q4_concentration_computes():
    raw = pd.read_parquet(CONC)
    raw = raw[raw["CERT"] == SVB_CERT].copy()
    rows = pd.DataFrame({"report_date": pd.to_datetime(raw["REPDTE"]),
                         **{c: raw[c].astype("float64") for c in
                            ["LNRECONS", "LNREMULT", "LNRENROT", "LNCOMRE", "RBC", "RBCT1J", "LNATRES"]}})
    last = rows[rows["report_date"] == pd.Timestamp("2022-12-31")].iloc[0]
    assert last["RBCT1J"] == 16_995_000 and last["LNATRES"] == 636_000
    r = compute_concentration(rows, date(2022, 12, 31))
    assert r.measure == "t1_allowance_2020"
    assert r.reason is None
    assert math.isfinite(r.construction_pct) and math.isfinite(r.cre_pct)
