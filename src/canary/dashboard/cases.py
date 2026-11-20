"""The 2023 case studies: one record per bank-quarter for the dashboard's quarter slider."""
from datetime import date
from pathlib import Path
from typing import Literal

import pandas as pd

from canary.analyst.labels import PLAIN_NAMES

WEAK_SPOT: dict[int, str] = {
    24735: "htm_unrealized_loss_to_equity",
    57053: "afs_unrealized_loss_to_equity",
    59017: "uninsured_to_deposits",
}

N_SIGNALS = 3


def phase_of(report_date: date, last: date) -> Literal["before", "rising", "last"]:
    if report_date == last:
        return "last"
    return "before" if report_date.year == 2021 else "rising"


def _signals(text: str) -> list[list]:
    out = []
    for part in text.split(",")[:N_SIGNALS]:
        name, value = part.strip().split("=")
        out.append([PLAIN_NAMES[name], float(value)])
    return out


def export_cases(ctx, case_csv: Path) -> dict[int, list[dict]]:
    cases = pd.read_csv(case_csv, parse_dates=["report_date"])
    feats = ctx.features.assign(report_date=pd.to_datetime(ctx.features["report_date"]))
    result: dict[int, list[dict]] = {}
    for cert, column in WEAK_SPOT.items():
        rows = cases[cases["cert"] == cert].sort_values("report_date")
        weak = feats[feats["cert"] == cert].set_index("report_date")[column]
        last = rows["report_date"].iloc[-1].date()
        result[cert] = [
            {
                "q": r.report_date.date().isoformat(),
                "pct": float(r.percentile),
                "rank": int(r.rank),
                "n": int(r.n_banks),
                "weak": float(weak.loc[r.report_date]) * 100,
                "signals": _signals(r.top_signals),
                "phase": phase_of(r.report_date.date(), last),
            }
            for r in rows.itertuples()
        ]
    return result
