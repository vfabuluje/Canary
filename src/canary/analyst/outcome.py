"""Outcome classification and as-of rules for one bank (spec 5.1, 5.3)."""

from dataclasses import dataclass
from datetime import date
from typing import Literal

import pandas as pd

from canary.analyst.context import Context
from canary.model.dataset import TEST_END, TEST_START
from canary.model.metrics import lead_times

# "After the test window": failure_date > this. Failures up to this date belong to the reported
# 2016-2024 test (their last test-period rows are scored by metrics.json).
AFTER_WINDOW_START = date(2025, 12, 31)


@dataclass
class Outcome:
    kind: Literal["caught", "missed", "false_alarm", "quiet", "open_watchlist"]
    after_test_window: bool
    failure_date: date | None
    first_flag: date | None
    lead_quarters: int | None
    still_reporting: bool
    last_report: date
    late_flag: date | None = None  # first flag after TEST_END for a test-window failure (hindsight only)


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
    first_flag = lead = late_flag = None
    if failure is not None:
        after_window = failure > AFTER_WINDOW_START
        # Test-window failures are judged on test-period rows only, as in metrics.json (ruling R11).
        judged = rows if after_window else rows[rows["report_date"] <= pd.Timestamp(TEST_END)]
        leads = lead_times(judged, "flagged")
        if cert in leads.index:
            kind = "caught"
            lead = int(leads[cert])
            hit = judged[judged["flagged"].astype(bool) & (judged["quarters_until_failure"] == lead)]
            first_flag = pd.Timestamp(hit["report_date"].min()).date()
        else:
            kind = "missed"
            if not after_window:
                late = rows[(rows["report_date"] > pd.Timestamp(TEST_END)) & rows["flagged"].astype(bool)
                            & pd.to_numeric(rows["quarters_until_failure"], errors="coerce").between(1, 4)]
                if len(late):
                    late_flag = pd.Timestamp(late["report_date"].min()).date()
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
        after_test_window=failure is not None and failure > AFTER_WINDOW_START,
        failure_date=failure,
        first_flag=first_flag,
        lead_quarters=lead,
        still_reporting=last_report == ctx.latest_quarter,
        last_report=last_report,
        late_flag=late_flag,
    )
