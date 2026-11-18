"""Tools for the `ask` agent (spec 6). Plain functions that return JSON strings.

User errors (bad cert, bad as-of, no match) come back as {"error": "..."}; they are never raised,
so Claude can read the message and recover. Dates are "YYYY-MM-DD" strings, nulls are null.
"""

import json
import math
from datetime import date

import pandas as pd

from canary.analyst.context import Context
from canary.analyst.facts import build_fact_sheet
from canary.analyst.writer import RefusalError, TruncatedError, write_memo
from canary.model.metrics import WATCHLIST_SHARE

MAX_MATCHES = 10


def _dumps(obj) -> str:
    return json.dumps(obj)


def _error(msg: str) -> str:
    return _dumps({"error": msg})


def _day(value) -> str | None:
    return None if pd.isna(value) else pd.Timestamp(value).date().isoformat()


def _text(value) -> str | None:
    return None if pd.isna(value) else str(value)


def _parse_date(value: str | None, what: str) -> date | None:
    if value is None or value == "":
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        raise ValueError(f"{what} must be YYYY-MM-DD, got {value!r}") from None


def find_bank(ctx: Context, query: str, state: str | None = None, failed_year: int | None = None) -> str:
    q = query.strip()
    banks = ctx.banks
    if not q:
        return _error("query is empty")
    if q.isdigit():
        hit = banks[banks["cert"] == int(q)]
    else:
        low = q.lower()
        by_name = banks["name"].fillna("").str.lower().str.contains(low, regex=False)
        failed = banks["failure_date"].notna()
        by_city = failed & banks["city"].fillna("").str.lower().str.contains(low, regex=False)
        hit = banks[by_name | by_city]
    if state:
        hit = hit[hit["state"].fillna("").str.upper() == state.strip().upper()]
    if failed_year is not None:
        hit = hit[hit["failure_date"].dt.year == failed_year]
    rows = [
        {
            "cert": int(r.cert),
            "name": _text(r.name),
            "state": _text(r.state),
            "city": _text(r.city),
            "first_report": _day(r.first_report),
            "last_report": _day(r.last_report),
            "failure_date": _day(r.failure_date),
        }
        for r in hit.sort_values("cert").head(MAX_MATCHES).itertuples()
    ]
    return _dumps(rows)


def get_bank_facts(ctx: Context, cert: int, as_of: str | None = None) -> str:
    try:
        sheet = build_fact_sheet(ctx, int(cert), _parse_date(as_of, "as_of"))
    except (ValueError, KeyError) as exc:
        return _error(str(exc))
    return _dumps(
        {
            "cert": sheet.cert,
            "name": sheet.name,
            "as_of": sheet.as_of.isoformat(),
            "outcome": sheet.outcome.kind,
            "facts": [
                {"id": f.id, "label": f.label, "quarter": f.quarter.isoformat() if f.quarter else None,
                 "display": f.display}
                for f in sheet.facts
            ],
        }
    )


def list_watchlist(ctx: Context, quarter: str | None = None) -> str:
    try:
        q = _parse_date(quarter, "quarter") or ctx.latest_quarter
    except ValueError as exc:
        return _error(str(exc))
    rows = ctx.scored[ctx.scored["report_date"] == pd.Timestamp(q)]
    if rows.empty:
        return _error(f"no scores for quarter {q}; scores run from 2016-03-31 to {ctx.latest_quarter}")
    k = math.ceil(round(len(rows) * WATCHLIST_SHARE, 9))
    top = rows.sort_values(["rank", "cert"]).head(k)
    names = ctx.banks.set_index("cert")["name"]
    return _dumps(
        [{"cert": int(r.cert), "name": _text(names.get(r.cert)), "rank": int(r.rank)} for r in top.itertuples()]
    )


def write_memo_tool(ctx: Context, client, model: str, cert: int, as_of: str | None = None) -> str:
    try:
        res = write_memo(ctx, int(cert), _parse_date(as_of, "as_of"), client=client, model=model)
    except (RefusalError, TruncatedError, ValueError, KeyError, json.JSONDecodeError) as exc:
        return _error(str(exc))
    return _dumps(
        {"path": str(res.path) if res.path else None, "ok": res.ok, "errors": res.errors,
         "attempts": res.attempts}
    )
