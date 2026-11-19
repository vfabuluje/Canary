"""Peer comparison core: the fixed peer rule (spec section 6), pure functions.

Descriptive only. An unusual figure is not a prediction of failure.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import date
from typing import Literal

import pandas as pd

from canary.analyst.labels import PLAIN_NAMES
from canary.analyst.trends import TREND_RATIOS

SPECIALTY_NAMES: dict[int, str] = {
    1: "International Specialization",
    2: "Agricultural Specialization",
    3: "Credit-card Specialization",
    4: "Commercial Lending Specialization",
    5: "Mortgage Lending Specialization",
    6: "Consumer Lending Specialization",
    7: "Other Specialized Under 1 Billion",
    8: "All Other Under 1 Billion",
    9: "All Other Over 1 Billion",
}
GENERAL_GROUPS = frozenset({8, 9})

# (upper bound in dollars, exclusive; label). Lower bounds are inclusive.
TIERS: list[tuple[float, str]] = [
    (1e8, "under $100 million"),
    (1e9, "$100 million to $1 billion"),
    (1e10, "$1 billion to $10 billion"),
    (math.inf, "over $10 billion"),
]
MIN_PEERS = 15
UNUSUAL_SHARE = 0.10
MAX_SHOWN_PEERS = 8

NATIONAL_HIGH = "unusually high"
NATIONAL_LOW = "unusually low"
READING_HIGH_TOO = "unusually high among its peers too"
READING_HIGH = "unusually high among its peers"
READING_LOW_TOO = "unusually low among its peers too"
READING_LOW = "unusually low among its peers"
READING_TYPICAL = "typical for its peer group"
READING_TOO_FEW = "too few peers with this figure"

Side = Literal["high", "low"]


def size_tier(log_total_assets: float) -> str:
    # log_total_assets is ln(assets in $ thousands); round away float noise
    dollars = round(math.exp(log_total_assets) * 1000, 6)
    for upper, label in TIERS:
        if dollars < upper:
            return label
    return TIERS[-1][1]


def midrank_pct(values: pd.Series, v: float) -> float:
    """Mid-rank percentile (0-100) of v among values (v is one of them)."""
    below = (values < v).sum()
    equal = (values == v).sum()
    return float((below + 0.5 * equal) / len(values) * 100)


def unusual_side(values: pd.Series, v: float) -> Side | None:
    n = len(values)
    if (values <= v).sum() / n <= UNUSUAL_SHARE:
        return "low"
    if (values >= v).sum() / n <= UNUSUAL_SHARE:
        return "high"
    return None


@dataclass
class PeerRow:
    feature: str
    value: float
    nat_pct: float
    nat_side: Side
    peer_pct: float | None
    peer_median: float | None
    reading: str


@dataclass
class PeerResult:
    as_of: date
    specgrp: int | None
    specialty_name: str | None
    tier: str
    basis: Literal["specialty_tier", "specialty", "too_few", "no_specialty"]
    n_peers: int
    rows: list[PeerRow]

    @property
    def shown(self) -> list[PeerRow]:
        return self.rows[:MAX_SHOWN_PEERS]

    @property
    def n_unusual_peers(self) -> int:
        return sum(r.reading.startswith("unusually") for r in self.rows)


def _reading(peer_side: Side | None, nat_side: Side) -> str:
    if peer_side == "high":
        return READING_HIGH_TOO if nat_side == "high" else READING_HIGH
    if peer_side == "low":
        return READING_LOW_TOO if nat_side == "low" else READING_LOW
    return READING_TYPICAL


def compute_peers(quarter: pd.DataFrame, cert: int, as_of: date) -> PeerResult:
    me = quarter[quarter["cert"] == cert].iloc[0]
    tier = size_tier(float(me["log_total_assets"]))
    sg = me["specgrp"]
    specgrp = None if pd.isna(sg) else int(sg)

    peer_set: pd.DataFrame | None = None
    n_peers = 0
    if specgrp is None:
        basis = "no_specialty"
    else:
        in_spec = quarter[quarter["specgrp"] == specgrp]
        in_tier = in_spec[in_spec["log_total_assets"].map(size_tier) == tier]
        if len(in_tier) >= MIN_PEERS:
            basis, peer_set, n_peers = "specialty_tier", in_tier, len(in_tier)
        elif len(in_spec) >= MIN_PEERS:
            basis, peer_set, n_peers = "specialty", in_spec, len(in_spec)
        else:
            basis, n_peers = "too_few", len(in_spec)

    rows: list[PeerRow] = []
    for f in TREND_RATIOS:
        if f not in quarter.columns or pd.isna(me[f]):
            continue
        v = float(me[f])
        nat = quarter[f].dropna().astype(float)
        side = unusual_side(nat, v)
        if side is None:
            continue
        nat_pct = midrank_pct(nat, v)
        peer_pct = peer_median = None
        reading = ""
        if peer_set is not None:
            pv = peer_set[f].dropna().astype(float)
            if len(pv) < MIN_PEERS:
                reading = READING_TOO_FEW
            else:
                peer_pct = midrank_pct(pv, v)
                peer_median = float(pv.median())
                reading = _reading(unusual_side(pv, v), side)
        rows.append(PeerRow(f, v, nat_pct, side, peer_pct, peer_median, reading))
    rows.sort(key=lambda r: (-abs(r.nat_pct - 50), PLAIN_NAMES[r.feature]))
    return PeerResult(
        as_of=as_of, specgrp=specgrp,
        specialty_name=SPECIALTY_NAMES.get(specgrp) if specgrp is not None else None,
        tier=tier, basis=basis, n_peers=n_peers, rows=rows,
    )
