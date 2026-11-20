"""Fuzzy bank search for the dashboard: hand-written aliases, then rapidfuzz on bank names."""

import re
from typing import NamedTuple

import pandas as pd
from rapidfuzz import fuzz, process

ALIASES: dict[str, int] = {
    "svb": 24735,
    "signature": 57053,
    "first republic": 59017,
    "frb": 59017,
}
DIRECT_MIN_SCORE = 90
DIRECT_MIN_LEAD = 10


class SearchResult(NamedTuple):
    direct: int | None
    suggestions: list[dict]


def _normalize(text: str) -> str:
    """Lower-case and turn punctuation into spaces so "M&T" and "m t" compare alike."""
    return " ".join(re.sub(r"[^a-z0-9]+", " ", text.lower()).split())


def _status(row: pd.Series, latest_quarter: pd.Timestamp) -> str:
    if pd.notna(row["failure_date"]):
        d = row["failure_date"]
        return f"Failed {d.strftime('%b')} {d.day}, {d.year}"
    if row["last_report"] == latest_quarter:
        return "Active"
    return f"Stopped reporting {row['last_report'].year}"


def search(query: str, banks: pd.DataFrame, limit: int = 8) -> SearchResult:
    """Alias match opens a bank directly; otherwise fuzzy-match names.

    Opens directly only when the top score is at least 90 and at least 10 points
    ahead of the next different bank; otherwise returns up to `limit` suggestions.
    """
    q = query.strip().lower()
    if not q:
        return SearchResult(None, [])
    if q in ALIASES:
        return SearchResult(ALIASES[q], [])

    names = [_normalize(n) for n in banks["name"]]
    hits = process.extract(_normalize(q), names, scorer=fuzz.WRatio, limit=limit + 1)
    top = hits[:limit]
    direct = None
    if top and top[0][1] >= DIRECT_MIN_SCORE:
        runner_up = hits[1][1] if len(hits) > 1 else 0
        if top[0][1] - runner_up >= DIRECT_MIN_LEAD:
            direct = int(banks.iloc[top[0][2]]["cert"])

    latest_quarter = banks["last_report"].max()
    rows = [banks.iloc[i] for _, _, i in top]
    suggestions = []
    for row in rows:
        twin = any(o["cert"] != row["cert"] and o["name"] == row["name"] and o["state"] == row["state"]
                   for o in rows)
        label = f"{row['name']} — {row['city']}, cert {row['cert']}" if twin else row["name"]
        suggestions.append({"cert": int(row["cert"]), "name": row["name"], "state": row["state"],
                            "status": _status(row, latest_quarter), "label": label})
    return SearchResult(direct, suggestions)
