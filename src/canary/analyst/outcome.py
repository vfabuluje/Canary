"""Outcome classification and as-of rules for one bank (spec 5.1, 5.3)."""

from dataclasses import dataclass
from datetime import date
from typing import Literal

import pandas as pd

from canary.analyst.context import Context
from canary.model.dataset import TEST_START
from canary.model.metrics import lead_times

TEST_END = date(2025, 12, 31)


@dataclass
class Outcome:
    kind: Literal["caught", "missed", "false_alarm", "quiet", "open_watchlist"]
    after_test_window: bool
    failure_date: date | None
    first_flag: date | None
    lead_quarters: int | None
    still_reporting: bool
    last_report: date


def _bank(ctx: Context, cert: int) -> pd.Series:
    rows = ctx.banks[ctx.banks["cert"] == cert]
    if rows.empty:
        raise ValueError(f"cert {cert} is not in the data")
    return rows.iloc[0]


def _date_or_none(value) -> date | None:
    return None if pd.isna(value) else pd.Timestamp(value).date()


def default_as_of(ctx: Context, cert: int) -> date:
    bank = _bank(ctx, cert)
    if pd.isna(bank["failure_date"]):
        return ctx.latest_quarter
    return pd.Timestamp(bank["last_report"]).date()


def validate_as_of(ctx: Context, cert: int, as_of: date) -> None:
    bank = _bank(ctx, cert)
    first = max(pd.Timestamp(TEST_START), pd.Timestamp(bank["first_report"]))
    last = pd.Timestamp(bank["last_report"])
    reported = set(ctx.features.loc[ctx.features["cert"] == cert, "report_date"])
    ts = pd.Timestamp(as_of)
    if ts < pd.Timestamp(TEST_START) or ts > last or ts not in reported:
        raise ValueError(
            f"as-of {as_of} is not a quarter cert {cert} reported; "
            f"valid range is {first.date()} to {last.date()} (quarter-end dates it filed)"
        )


def classify(ctx: Context, cert: int, as_of: date) -> Outcome:
    bank = _bank(ctx, cert)
    failure = _date_or_none(bank["failure_date"])
    last_report = pd.Timestamp(bank["last_report"]).date()
    rows = ctx.scored[ctx.scored["cert"] == cert]
    first_flag = lead = None
    if failure is not None:
        leads = lead_times(rows, "flagged")
        if cert in leads.index:
            kind = "caught"
            lead = int(leads[cert])
            hit = rows[rows["flagged"].astype(bool) & (rows["quarters_until_failure"] == lead)]
            first_flag = pd.Timestamp(hit["report_date"].min()).date()
        else:
            kind = "missed"
    else:
        at = rows[rows["report_date"] == pd.Timestamp(as_of)]
        flagged = bool(at["flagged"].astype(bool).any())
        if flagged and as_of == ctx.latest_quarter:
            kind = "open_watchlist"
        elif flagged:
            kind = "false_alarm"
        else:
            kind = "quiet"
    return Outcome(
        kind=kind,
        after_test_window=failure is not None and failure > TEST_END,
        failure_date=failure,
        first_flag=first_flag,
        lead_quarters=lead,
        still_reporting=last_report == ctx.latest_quarter,
        last_report=last_report,
    )
