from datetime import date

import numpy as np
import pandas as pd
import pytest

from canary.analyst import peers
from canary.analyst.peers import (
    compute_peers, midrank_pct, size_tier, unusual_side,
)
from canary.analyst.trends import TREND_RATIOS

LOG_MID = float(np.log(5e5))  # $500M -> middle tier
LOG_BIG = float(np.log(5e6))  # $5B
AS_OF = date(2022, 12, 31)


def test_size_tier_bounds():
    assert size_tier(float(np.log(9.99e4))) == "under $100 million"
    assert size_tier(float(np.log(1e5))) == "$100 million to $1 billion"
    assert size_tier(float(np.log(209e6))) == "over $10 billion"
    assert size_tier(float(np.log(5e6))) == "$1 billion to $10 billion"


def test_unusual_side_ties():
    s = pd.Series([0.0] * 15 + list(np.arange(1, 86, dtype=float)))
    assert unusual_side(s, 0.0) is None
    assert unusual_side(s, 85.0) == "high"
    d = pd.Series(np.arange(100, dtype=float))
    assert unusual_side(d, 9.0) == "low"   # 10 of 100 at or below
    assert unusual_side(d, 10.0) is None   # 11 of 100


def test_midrank_pct():
    assert midrank_pct(pd.Series([1.0, 2, 3, 4]), 4.0) == 87.5


def _quarter(n_bank_group, n_tier_other=0, n_other_spec=0, bank_spec=4,
             bank_log=LOG_MID, feat_value=None):
    """Bank cert 1 plus peers. Group: same spec & tier; other tier same spec;
    other specialty."""
    rows = []
    def add(cert, spec, lta):
        r = {"cert": cert, "log_total_assets": lta, "specgrp": spec}
        for i, f in enumerate(TREND_RATIOS):
            r[f] = float(cert % 50)
        rows.append(r)
    add(1, bank_spec, bank_log)
    c = 2
    for _ in range(n_bank_group - 1):
        add(c, bank_spec, bank_log); c += 1
    for _ in range(n_tier_other):
        add(c, bank_spec, LOG_BIG); c += 1
    for _ in range(n_other_spec):
        add(c, 7, bank_log); c += 1
    df = pd.DataFrame(rows)
    df["specgrp"] = df["specgrp"].astype("Int64")
    return df


def test_group_order_and_counting():
    r = compute_peers(_quarter(15), 1, AS_OF)
    assert (r.basis, r.n_peers, r.specgrp) == ("specialty_tier", 15, 4)
    assert r.specialty_name == "Commercial Lending Specialization"
    assert r.tier == "$100 million to $1 billion"
    r = compute_peers(_quarter(14, n_tier_other=6), 1, AS_OF)
    assert (r.basis, r.n_peers) == ("specialty", 20)
    r = compute_peers(_quarter(7, n_tier_other=7, n_other_spec=30), 1, AS_OF)
    assert (r.basis, r.n_peers) == ("too_few", 14)
    q = _quarter(15)
    q["specgrp"] = pd.array([pd.NA] * len(q), dtype="Int64")
    r = compute_peers(q, 1, AS_OF)
    assert r.basis == "no_specialty" and r.specgrp is None


def test_bank_counted_in_its_group():
    # 14 others + bank = 15 -> used; with bank excluded it would be 14
    r = compute_peers(_quarter(15), 1, AS_OF)
    assert r.basis == "specialty_tier"


def _readings_quarter(bank_val, peer_vals, nat_others, feature="return_on_assets"):
    """Bank (cert 1) + peers with given values in the group; plus national others."""
    q = _quarter(len(peer_vals) + 1, n_other_spec=len(nat_others))
    for f in TREND_RATIOS:
        q[f] = 50.0
    q[feature] = [bank_val] + list(peer_vals) + list(nat_others)
    return q


def test_readings():
    f = "return_on_assets"
    # national high, peer high (bank top of group too)
    others = list(np.linspace(0, 10, 200))
    peer = list(np.linspace(0, 10, 14))
    q = _readings_quarter(100.0, peer, others)
    row = next(x for x in compute_peers(q, 1, AS_OF).rows if x.feature == f)
    assert row.nat_side == "high"
    assert row.reading == "unusually high among its peers too"
    # national high, peer low: peers all much higher, others low
    q = _readings_quarter(5.0, [1000.0 + i for i in range(14)], [float(i) / 50 for i in range(200)])
    row = next(x for x in compute_peers(q, 1, AS_OF).rows if x.feature == f)
    assert row.nat_side == "high" and row.peer_pct < 50
    assert row.reading == "unusually low among its peers"
    # national low, peer neither
    q = _readings_quarter(5.0, list(np.arange(1, 15) * 1.0) + [], [float(i) + 6 for i in range(200)])
    q.loc[1:7, f] = 1.0  # some peers lower
    q.loc[8:14, f] = 10.0
    row = next(x for x in compute_peers(q, 1, AS_OF).rows if x.feature == f)
    assert row.nat_side == "low"
    assert row.reading == "typical for its peer group"
    # 14 peers with a value
    q = _readings_quarter(100.0, list(np.linspace(0, 10, 14)), list(np.linspace(0, 10, 200)))
    q.loc[2, f] = np.nan
    row = next(x for x in compute_peers(q, 1, AS_OF).rows if x.feature == f)
    assert row.reading == "too few peers with this figure"
    assert row.peer_pct is None and row.peer_median is None


def test_nan_excluded():
    f = "return_on_assets"
    q = _readings_quarter(100.0, list(np.linspace(0, 10, 20)), list(np.linspace(0, 10, 200)))
    q[f] = q[f].astype(float)
    q.loc[1, f] = np.nan
    q.loc[2:4, f] = np.nan
    r = compute_peers(q, 1, AS_OF)
    row = next(x for x in r.rows if x.feature == f)
    assert row.feature == f  # peer NaNs excluded, still enough (17)
    peers_vals = q.loc[(q["specgrp"] == 4), f].dropna()
    assert row.peer_median == pytest.approx(float(peers_vals.median()))
    # bank NaN -> skipped
    q.loc[0, f] = np.nan
    r = compute_peers(q, 1, AS_OF)
    assert f not in [x.feature for x in r.rows]


def test_order_and_cap():
    q = _quarter(20)
    feats = list(TREND_RATIOS)[:10]
    for f in TREND_RATIOS:
        q[f] = np.linspace(0, 1, len(q))
    for i, f in enumerate(feats):
        q[f] = np.linspace(0, 1, len(q))
        q.loc[0, f] = 10.0 + i  # top of group, all share top percentile
    r = compute_peers(q, 1, AS_OF)
    assert len(r.rows) >= 10
    assert len(r.shown) == 8
    from canary.analyst.labels import PLAIN_NAMES
    keys = [(-abs(x.nat_pct - 50), PLAIN_NAMES[x.feature]) for x in r.rows]
    assert keys == sorted(keys)


def test_log_total_assets_not_a_ratio():
    q = _quarter(20)
    q.loc[0, "log_total_assets"] = 30.0
    r = compute_peers(q, 1, AS_OF)
    assert "log_total_assets" not in [x.feature for x in r.rows]
