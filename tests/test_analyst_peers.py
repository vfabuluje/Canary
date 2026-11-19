from datetime import date

import numpy as np
import pandas as pd
import pytest

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
        for f in TREND_RATIOS:
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
    # 20 in the group (bank + 19), 180 elsewhere; bank is the top value
    q = _quarter(20, n_other_spec=180)
    q[f] = np.arange(len(q), dtype=float)
    q.loc[0, f] = 1000.0
    q.loc[1:3, f] = np.nan        # 3 peers without a value
    q.loc[30:49, f] = np.nan      # 20 national (non-peer) NaNs
    row = next(x for x in compute_peers(q, 1, AS_OF).rows if x.feature == f)
    n_nat = 200 - 3 - 20
    assert row.nat_pct == pytest.approx((n_nat - 0.5) / n_nat * 100)
    assert row.peer_pct == pytest.approx((17 - 0.5) / 17 * 100)
    pv = q.loc[q["specgrp"] == 4, f].dropna()
    assert row.peer_median == pytest.approx(float(pv.median()))
    # bank NaN -> ratio skipped
    q.loc[0, f] = np.nan
    assert f not in [x.feature for x in compute_peers(q, 1, AS_OF).rows]


def test_order_and_cap():
    q = _quarter(100)
    feats = list(TREND_RATIOS)
    # (feature index, side, rank from that extreme among 100); distance = 50.5 - rank
    spec = [(0, "high", 1), (1, "low", 2), (2, "high", 3), (3, "low", 3),
            (4, "high", 5), (5, "low", 6), (6, "high", 7), (7, "low", 8),
            (8, "high", 9), (9, "high", 10)]
    for f in feats:
        q[f] = np.arange(100, dtype=float)
        q.loc[0, f] = 50.0  # mid-pack: not unusual
    for idx, side, rank in spec:
        target = float(100 - rank) if side == "high" else float(rank - 1)
        col = list(range(100))
        col[0], col[int(target)] = int(target), 0
        q[feats[idx]] = np.array(col, dtype=float)
    r = compute_peers(q, 1, AS_OF)
    from canary.analyst.labels import PLAIN_NAMES
    tie = sorted([feats[2], feats[3]], key=PLAIN_NAMES.get)
    expected = [feats[0], feats[1], *tie, feats[4], feats[5], feats[6],
                feats[7], feats[8], feats[9]]
    assert [x.feature for x in r.rows] == expected
    assert len(r.rows) == 10 and len(r.shown) == 8
    assert [x.feature for x in r.shown] == expected[:8]


def test_nan_assets_not_in_tier_group():
    q = _quarter(15, n_other_spec=0)
    extra = q.iloc[[1]].copy()
    extra["cert"] = 999
    extra["log_total_assets"] = np.nan
    q = pd.concat([q, extra], ignore_index=True)
    r = compute_peers(q, 1, AS_OF)
    # 15 in tier only if the NaN-assets bank counted; it must not
    assert (r.basis, r.n_peers) == ("specialty_tier", 15)
    q2 = _quarter(14)
    q2 = pd.concat([q2, extra], ignore_index=True)
    r2 = compute_peers(q2, 1, AS_OF)
    assert (r2.basis, r2.n_peers) == ("specialty", 15)
    with pytest.raises(ValueError):
        size_tier(float("nan"))


def test_input_errors():
    q = _quarter(15)
    with pytest.raises(ValueError, match="12345"):
        compute_peers(q, 12345, AS_OF)
    with pytest.raises(KeyError, match="return_on_assets"):
        compute_peers(q.drop(columns=["return_on_assets"]), 1, AS_OF)


def test_log_total_assets_not_a_ratio():
    q = _quarter(20)
    q.loc[0, "log_total_assets"] = 30.0
    r = compute_peers(q, 1, AS_OF)
    assert "log_total_assets" not in [x.feature for x in r.rows]
