"""Real-estate concentration core: the 2006 interagency screens (spec sections 5 and 6).

Pure functions. Crossing a line is a supervisory screen, not a prediction.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Literal

import pandas as pd

NEW_MEASURE_FROM = date(2020, 3, 31)
LINE1_PCT = 100.0
LINE2_PCT = 300.0
GROWTH_PCT = 50.0
GROWTH_QUARTERS = 12

LEAD = (
    "This section checks a different, more common way banks have failed than SVB's: heavy lending "
    "tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set "
    "in 2006 to flag a bank for closer supervisory review; they are not lending limits."
)
CAPITAL_2006 = "Capital measure: total risk-based capital, as the 2006 guidance specifies."
CAPITAL_2020 = (
    "Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used "
    "for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). "
    "The 2006 thresholds were not restated for this measure."
)
TABLE_HEADER = "| Test | Bank | Line | Meets it? |"
TABLE_RULE = "|---|---|---|---|"
ROW_CONSTRUCTION = "Construction and land loans ÷ capital"
ROW_CRE = "Total commercial real estate loans ÷ capital"
ROW_GROWTH = "Growth in commercial real estate loans over the prior 36 months"
LINE_CONSTRUCTION = "100% or more"
LINE_CRE = "300% or more"
LINE_GROWTH = "50% or more"
YES, NO, NA = "yes", "no", "n/a"

L1_CROSSED = "It crossed the construction line (100% or more of capital)."
L1_NOT_CROSSED = "It did not cross the construction line."
L1_CANT = "The construction line can't be checked: {reason}."
L2_CROSSED = ("It crossed the total commercial real estate line (300% or more of capital, with 50% "
              "or more growth over 36 months).")
L2_NOT_CROSSED = "It did not cross the total commercial real estate line."
L2_GROWTH_LOW = ("Its commercial real estate loans reached 300% of capital, but grew less than 50% "
                 "over 36 months, so it did not cross the second line.")
L2_GROWTH_UNKNOWN = ("Its commercial real estate loans reached 300% of capital, but the growth part "
                     "can't be checked: {growth_reason}.")
L2_CANT = "The total commercial real estate line can't be checked: {reason}."
BOTH_NOT_CROSSED = "It did not cross either line."
BOTH_CROSSED = "It crossed both lines: construction loans and total commercial real estate loans."

REASON_CAPITAL = "the bank reported no usable capital figure for this quarter"
REASON_LOAN = "a loan figure the test needs is missing for this quarter"
REASON_NO_DATA = "there is no concentration data for this bank this quarter"
GROWTH_NO_FIGURE = "there is no figure from 12 quarters earlier"
GROWTH_ZERO_BASE = "it reported no commercial real estate loans 12 quarters earlier"

DEFINITIONS = (
    "Total commercial real estate here means construction and land, multifamily, and "
    "non-owner-occupied commercial property loans, plus loans to finance commercial real estate "
    "not secured by real estate (FDIC call report data)."
)
CLOSING = ("Crossing a line is a supervisory screen, not a prediction: it has not been tested as a "
           "warning signal in Canary.")

_CRE_PARTS = ["LNRECONS", "LNREMULT", "LNRENROT", "LNCOMRE"]


@dataclass
class ConcentrationResult:
    as_of: date
    measure: Literal["rbc_2006", "t1_allowance_2020"]
    construction_pct: float | None
    cre_pct: float | None
    growth_pct: float | None
    reason: str | None = None
    cre_reason: str | None = None
    growth_reason: str | None = None


def _num(v) -> float | None:
    return None if v is None or pd.isna(v) else float(v)


def _cre_total(row) -> float | None:
    vals = [_num(row.get(c)) for c in _CRE_PARTS]
    return None if any(v is None for v in vals) else sum(vals)


def _row_at(rows: pd.DataFrame, d: date):
    if rows is None or len(rows) == 0 or "report_date" not in rows.columns:
        return None
    hit = rows[pd.to_datetime(rows["report_date"]).dt.date == d]
    return None if hit.empty else hit.iloc[0]


def compute_concentration(rows: pd.DataFrame, as_of: date) -> ConcentrationResult:
    measure = "t1_allowance_2020" if as_of >= NEW_MEASURE_FROM else "rbc_2006"
    res = ConcentrationResult(as_of, measure, None, None, None)
    row = _row_at(rows, as_of)
    if row is None:
        res.reason = REASON_NO_DATA
        return res
    if measure == "rbc_2006":
        capital = _num(row.get("RBC"))
    else:
        t1, allow = _num(row.get("RBCT1J")), _num(row.get("LNATRES"))
        capital = None if t1 is None or allow is None else t1 + allow
    if capital is None or capital <= 0:
        res.reason = REASON_CAPITAL
        return res
    construction = _num(row.get("LNRECONS"))
    if construction is None:
        res.reason = REASON_LOAN
        return res
    res.construction_pct = construction / capital * 100
    total = _cre_total(row)
    if total is None:
        res.cre_reason = REASON_LOAN
        return res
    res.cre_pct = total / capital * 100
    earlier_d = date(as_of.year - GROWTH_QUARTERS // 4, as_of.month, as_of.day)
    earlier_row = _row_at(rows, earlier_d)
    earlier = None if earlier_row is None else _cre_total(earlier_row)
    if earlier is None:
        res.growth_reason = GROWTH_NO_FIGURE
    elif earlier == 0:
        res.growth_reason = GROWTH_ZERO_BASE
    else:
        res.growth_pct = (total / earlier - 1) * 100
    return res


def _pct(v: float | None) -> str:
    if v is None:
        return NA
    text = f"{v:,.1f}"
    if text == "-0.0":
        text = "0.0"
    return text + "%"


def _meets(v: float | None, line: float) -> str:
    return NA if v is None else (YES if v >= line else NO)


def _summary(r: ConcentrationResult) -> list[str]:
    reason1 = r.reason
    reason2 = r.reason or r.cre_reason
    c1 = None if r.construction_pct is None else r.construction_pct >= LINE1_PCT
    if r.cre_pct is None:
        c2 = None
    elif r.cre_pct < LINE2_PCT:
        c2 = False
    elif r.growth_pct is None:
        c2 = None
    else:
        c2 = r.growth_pct >= GROWTH_PCT
    if c1 is False and r.cre_pct is not None and r.cre_pct < LINE2_PCT:
        return [BOTH_NOT_CROSSED]
    if c1 is True and c2 is True:
        return [BOTH_CROSSED]
    out = [L1_CANT.format(reason=reason1) if c1 is None else (L1_CROSSED if c1 else L1_NOT_CROSSED)]
    if r.cre_pct is None:
        out.append(L2_CANT.format(reason=reason2))
    elif r.cre_pct < LINE2_PCT:
        out.append(L2_NOT_CROSSED)
    elif r.growth_pct is None:
        out.append(L2_GROWTH_UNKNOWN.format(growth_reason=r.growth_reason))
    else:
        out.append(L2_CROSSED if c2 else L2_GROWTH_LOW)
    return out


def render_concentration(result: ConcentrationResult) -> list[str]:
    r = result
    return [
        LEAD, "",
        CAPITAL_2006 if r.measure == "rbc_2006" else CAPITAL_2020, "",
        TABLE_HEADER, TABLE_RULE,
        f"| {ROW_CONSTRUCTION} | {_pct(r.construction_pct)} | {LINE_CONSTRUCTION} | "
        f"{_meets(r.construction_pct, LINE1_PCT)} |",
        f"| {ROW_CRE} | {_pct(r.cre_pct)} | {LINE_CRE} | {_meets(r.cre_pct, LINE2_PCT)} |",
        f"| {ROW_GROWTH} | {_pct(r.growth_pct)} | {LINE_GROWTH} | {_meets(r.growth_pct, GROWTH_PCT)} |",
        "",
        *_summary(r), "",
        DEFINITIONS, "",
        CLOSING,
    ]
