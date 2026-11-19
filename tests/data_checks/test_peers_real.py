"""Data check on SVB's peer group (skipped when no local data).
Asserts only the group, tier and basis; nothing about readings."""
from datetime import date
from pathlib import Path

import pandas as pd
import pytest

from canary.analyst.peers import compute_peers

ROOT = Path(__file__).resolve().parents[2]
FEATURES = ROOT / "data" / "features" / "fct_bank_features.parquet"
SPECIALTY = ROOT / "data" / "raw" / "specialty"
SVB_CERT = 24735

pytestmark = [
    pytest.mark.data,
    pytest.mark.skipif(
        not (FEATURES.exists() and SPECIALTY.exists()), reason="no local data"
    ),
]


def test_svb_2022q4_peer_group():
    f = pd.read_parquet(FEATURES)
    f["report_date"] = pd.to_datetime(f["report_date"])
    q = f[f["report_date"] == pd.Timestamp("2022-12-31")].copy()
    s = pd.read_parquet(SPECIALTY, columns=["CERT", "REPDTE", "SPECGRP"])
    s = s[pd.to_datetime(s["REPDTE"]) == pd.Timestamp("2022-12-31")]
    s = s.drop_duplicates("CERT").rename(columns={"CERT": "cert", "SPECGRP": "specgrp"})
    q = q.merge(s[["cert", "specgrp"]], on="cert", how="left")
    q["specgrp"] = pd.to_numeric(q["specgrp"], errors="coerce").astype("Int64")
    r = compute_peers(q, SVB_CERT, date(2022, 12, 31))
    assert r.specgrp == 9
    assert r.tier == "over $10 billion"
    assert r.basis in {"specialty_tier", "specialty"}
