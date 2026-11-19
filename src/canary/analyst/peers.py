"""Peer comparison core: the fixed peer rule (spec section 6), pure functions.

Descriptive only. An unusual figure is not a prediction of failure.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, replace
from datetime import date
from typing import Literal

import pandas as pd

from canary.analyst import sections as sections_mod
from canary.analyst.facts import (
    SPELLED_SPAN,
    Fact,
    _count_forms,
    _ordinal,
    date_forms,
    decimal_ordinal_forms,
    spelled_norm,
)
from canary.analyst.labels import PLAIN_NAMES, display_forms
from canary.analyst.sections import Section
from canary.analyst.trends import TREND_RATIOS, _nz

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
    if pd.isna(log_total_assets):
        raise ValueError("log_total_assets is missing; cannot assign a size tier")
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
    mine = quarter[quarter["cert"] == cert]
    if mine.empty:
        raise ValueError(f"cert {cert} is not in the quarter's rows at {as_of}")
    me = mine.iloc[0]
    missing = [f for f in TREND_RATIOS if f not in quarter.columns]
    if missing:
        raise KeyError(f"quarter is missing ratio column(s): {missing}")
    tier = size_tier(float(me["log_total_assets"]))
    sg = me["specgrp"]
    specgrp = None if pd.isna(sg) else int(sg)

    peer_set: pd.DataFrame | None = None
    n_peers = 0
    if specgrp is None:
        basis = "no_specialty"
    else:
        in_spec = quarter[quarter["specgrp"] == specgrp]
        # banks with no assets figure belong to no tier group
        known = in_spec[in_spec["log_total_assets"].notna()]
        in_tier = known[known["log_total_assets"].map(size_tier) == tier]
        if len(in_tier) >= MIN_PEERS:
            basis, peer_set, n_peers = "specialty_tier", in_tier, len(in_tier)
        elif len(in_spec) >= MIN_PEERS:
            basis, peer_set, n_peers = "specialty", in_spec, len(in_spec)
        else:
            basis, n_peers = "too_few", len(in_spec)

    rows: list[PeerRow] = []
    for f in TREND_RATIOS:
        if pd.isna(me[f]):
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


PEER_KEY = "peers"
PEER_SENTENCE = (
    "This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a "
    "prediction of failure, and the comparison has not been tested as a warning signal."
)
SPECIALTY_LINE = "The FDIC's specialty group for this bank at {as_of}: {name}."
GENERAL_LINE = "This is a general group: the FDIC did not record a lending specialty for this bank."
TIER_LINE = "Peers: {n} banks in the same specialty group and size tier ({tier})."
SPECIALTY_ONLY_LINE = ("Peers: {n} banks in the same specialty group (all sizes), because fewer than "
                       f"{MIN_PEERS} shared its size tier.")
TOO_FEW_LINE = ("There are not enough comparable banks ({n} in its specialty group) for a reliable "
                "comparison, so none is shown.")
NO_SPECIALTY_LINE = "The FDIC recorded no specialty group for this bank at {as_of}, so no peer comparison is shown."
NONE_UNUSUAL = "None of this bank's ratios were in the national top or bottom 10% at {as_of}."
_FEATURES_SRC = "data/features/fct_bank_features.parquet"
_SPECIALTY_SRC = "data/raw/specialty/: SPECGRP"
_RULE_SRC = "canary.analyst.peers: peer rule (fixed)"


def _basis_line(r: PeerResult) -> str:
    if r.basis == "no_specialty":
        return NO_SPECIALTY_LINE.format(as_of=r.as_of)
    if r.basis == "too_few":
        return TOO_FEW_LINE.format(n=r.n_peers)
    if r.basis == "specialty":
        return SPECIALTY_ONLY_LINE.format(n=r.n_peers)
    return TIER_LINE.format(n=r.n_peers, tier=r.tier)


def render_peer_lines(sheet) -> list[str]:
    """Code lines placed before the AI text: specialty, general-group note, basis (paragraph per line)."""
    r: PeerResult | None = sheet.extras.get(PEER_KEY)
    if r is None:
        return []
    lines: list[str] = []
    if r.specgrp is not None:
        lines.append(SPECIALTY_LINE.format(as_of=r.as_of, name=r.specialty_name))
        if r.specgrp in GENERAL_GROUPS:
            lines.append(GENERAL_LINE)
    lines.append(_basis_line(r))
    out: list[str] = []
    for ln in lines:
        out += [ln, ""]
    return out[:-1]


def _pct_text(p: float) -> str:
    return decimal_ordinal_forms(p)[-1]


def _first(feature: str, v: float) -> str:
    return _nz(display_forms(feature, v)[0])


def render_peer_table(sheet) -> list[str]:
    r: PeerResult | None = sheet.extras.get(PEER_KEY)
    if r is None:
        return []
    if r.basis in ("too_few", "no_specialty"):
        return [PEER_SENTENCE]
    if not r.shown:
        return [NONE_UNUSUAL.format(as_of=r.as_of), "", PEER_SENTENCE]
    lines = ["| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |",
             "|---|---|---|---|---|---|"]
    for row in r.shown:
        nat_word = NATIONAL_HIGH if row.nat_side == "high" else NATIONAL_LOW
        peer_pct = "n/a" if row.peer_pct is None else _pct_text(row.peer_pct)
        med = "n/a" if row.peer_median is None else _first(row.feature, row.peer_median)
        lines.append(f"| {PLAIN_NAMES[row.feature]} | {_first(row.feature, row.value)} | "
                     f"{_pct_text(row.nat_pct)} ({nat_word}) | {med} | {peer_pct} | {row.reading} |")
    return lines + ["", PEER_SENTENCE]


PEER_SECTION = Section(
    PEER_KEY, "Compared with similar banks", "as_of",
    "Cite only the peer facts (labels starting \"Peers\") and the as-of rank facts. For each ratio you "
    "discuss, give the bank's value, its national percentile with the national word, and, where the "
    "fact exists, the peer percentile and the peer median, with the reading. Give one ratio per sentence "
    "whenever you state its peer reading or peer percentile. Use the reading and the national word with "
    "the same meaning, no stronger or weaker claim; say \"unusually high\" or \"unusually low\", never "
    "\"risky\". Write each reading exactly as given (for example \"typical for its peer group\" or "
    "\"unusually high among its peers\"); don't paraphrase it (no \"not unusual among its peers\", no "
    "\"relative to its peers\"). Code adds the specialty and peer-group lines before your text, so don't repeat them. "
    "Don't write a disclaimer; code adds one after your text. In this section don't use the words risky, "
    "warning, predict or forecast at all, even negated, and do not mention the outcome. End with one "
    "sentence on the overall picture using the count of ratios in the national top or bottom 10% and the "
    "count of those that are also unusual among peers. If you mention the 10% cut-off or the minimum peer "
    "group size, cite the facts \"Peers: cut-off for unusual\" or \"Peers: minimum peer group size\".",
    True,
    render=render_peer_table,
    render_before=render_peer_lines,
)


def _ok(x: float | None) -> bool:
    return x is not None and math.isfinite(x)


def _clean(result: PeerResult) -> PeerResult:
    """No NaN reaches a fact or the table: a row with a non-finite value or national percentile is
    dropped; a non-finite peer percentile or median is treated as missing."""
    rows = []
    for r in result.rows:
        if not (_ok(r.value) and _ok(r.nat_pct)):
            continue
        ok = _ok(r.peer_pct) and _ok(r.peer_median)
        rows.append(replace(r, peer_pct=r.peer_pct if ok else None,
                            peer_median=r.peer_median if ok else None,
                            reading=r.reading if ok else READING_TOO_FEW))
    return replace(result, rows=rows)


def _value_forms(feature: str, v: float) -> list[str]:
    return list(dict.fromkeys(_nz(x) for x in display_forms(feature, v)))


def _pct_forms(p: float) -> list[str]:
    return [f"{p:.1f}", f"{p:.0f}", f"{p:.1f}%", f"{p:.0f}%", _ordinal(round(p)), *decimal_ordinal_forms(p)]


def _fact(label, value, display, forms, source, quarter, feature=None, kind=None) -> Fact:
    forms = list(forms) + (date_forms(quarter) if quarter else [])
    forms += [spelled_norm(m["sw"], m["su"]) for m in SPELLED_SPAN.finditer(f"{label} {display}")]
    return Fact("", label, quarter, value, display, list(dict.fromkeys(forms)), False, source, feature, kind)


def _quarter_rows(ctx, as_of: date) -> pd.DataFrame:
    ts = pd.Timestamp(as_of)
    q = ctx.features[ctx.features["report_date"] == ts].drop(columns=["specgrp"], errors="ignore")
    spec = ctx.specialty[ctx.specialty["report_date"] == ts][["cert", "specgrp"]]
    spec = spec.drop_duplicates("cert", keep="last")
    return q.merge(spec, on="cert", how="left")


class PeerSpecialist:
    key = PEER_KEY
    sections = [PEER_SECTION]

    def build_facts(self, ctx, sheet) -> list[Fact]:
        as_of = sheet.as_of
        result = _clean(compute_peers(_quarter_rows(ctx, as_of), sheet.cert, as_of))
        sheet.extras[PEER_KEY] = result
        comparing = result.basis in ("specialty_tier", "specialty")
        if not comparing or not result.shown:
            sheet.code_only.add(PEER_KEY)

        out: list[Fact] = []
        if result.specgrp is not None:
            disp = f"{result.specialty_name} (group {result.specgrp})"
            out.append(_fact("Peers: the FDIC specialty group at the as-of quarter", disp, disp,
                             [str(result.specgrp)], _SPECIALTY_SRC, as_of, None, "peer_specialty"))
        out.append(_fact("Peers: size tier used", result.tier, result.tier, [], _FEATURES_SRC, as_of,
                         None, "peer_tier"))
        line = _basis_line(result)
        out.append(_fact("Peers: how the peer group was formed", line, line, [], _SPECIALTY_SRC, as_of,
                         None, "peer_basis"))
        if comparing:
            for r in result.shown:
                name = PLAIN_NAMES[r.feature]
                src = f"{_FEATURES_SRC}: {r.feature}"
                v = _value_forms(r.feature, r.value)
                out.append(_fact(f"Peers: {name}, bank value at the as-of quarter", r.value, v[0], v, src,
                                 as_of, r.feature, "peer_value"))
                nat = _pct_forms(r.nat_pct)
                out.append(_fact(f"Peers: {name}, national percentile (100 = highest value among all banks)",
                                 r.nat_pct, _pct_text(r.nat_pct), nat, src, as_of, r.feature, "peer_nat_pct"))
                word = NATIONAL_HIGH if r.nat_side == "high" else NATIONAL_LOW
                out.append(_fact(f"Peers: {name}, national reading", word, word, [], src, as_of,
                                 r.feature, "peer_nat_dir"))
                if r.peer_pct is not None and r.peer_median is not None:
                    pf = _pct_forms(r.peer_pct)
                    out.append(_fact(f"Peers: {name}, percentile among its peers (100 = highest value)",
                                     r.peer_pct, _pct_text(r.peer_pct), pf, src, as_of, r.feature,
                                     "peer_pct"))
                    mf = _value_forms(r.feature, r.peer_median)
                    out.append(_fact(f"Peers: {name}, peer median", r.peer_median, mf[0], mf, src, as_of,
                                     r.feature, "peer_median"))
                out.append(_fact(f"Peers: {name}, reading against its peers", r.reading, r.reading, [], src,
                                 as_of, r.feature, "peer_reading"))
        counts = [
            ("Peers: banks in the peer group (including this bank)", result.n_peers, "peer_count", _SPECIALTY_SRC),
            ("Peers: ratios in the national top or bottom 10%", len(result.rows), "peer_count_unusual",
             _FEATURES_SRC),
            ("Peers: those ratios also unusual among peers", result.n_unusual_peers,
             "peer_count_unusual_peers", _FEATURES_SRC),
            ("Peers: ratios shown in the table (the furthest from the middle nationally)",
             len(result.shown) if comparing else 0, "peer_count_shown", _FEATURES_SRC),
        ]
        for label, n, kind, src in counts:
            out.append(_fact(label, n, str(n), _count_forms(n), src, as_of, None, kind))
        out.append(_fact("Peers: cut-off for unusual (top or bottom share of banks)", "10%", "10%",
                         ["10%", "10", "10 percent"], _FEATURES_SRC, as_of, None, "peer_cutoff"))
        out.append(_fact("Peers: minimum peer group size", "15", "15", ["15", "fifteen"], _SPECIALTY_SRC,
                         as_of, None, "peer_min"))
        return out


sections_mod.register(PeerSpecialist())
