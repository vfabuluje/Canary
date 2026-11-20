"""Fuzzy bank search for the dashboard: hand-written aliases, then rapidfuzz on bank names."""

import re
from typing import NamedTuple

import pandas as pd
from rapidfuzz import fuzz, process

ALIASES: dict[str, int] = {
    "svb": 24735, "silicon valley bank": 24735,
    "signature": 57053, "signature bank": 57053,
    "first republic": 59017, "first republic bank": 59017, "frb": 59017,
    "jpmorgan": 628, "jp morgan": 628, "chase": 628,
    "bank of america": 3510, "bofa": 3510,
    "citi": 7213, "citibank": 7213,
    "wells fargo": 3511,
    "goldman sachs": 33124,
    "us bank": 6548, "u.s. bank": 6548,
    "capital one": 4297,
    "pnc": 6384,
    "truist": 9846,
    "bny": 639, "bny mellon": 639, "bank of new york mellon": 639,
    "morgan stanley": 32992,
    "state street": 14,
    "td bank": 18409,
    "fifth third": 6672,
    "huntington": 6560,
    "bmo": 16571,
    "schwab": 57450, "charles schwab": 57450,
    "first citizens": 11063,
    "citizens": 57957,
    "m&t": 588, "m and t": 588,
}
DIRECT_MIN_SCORE = 90
DIRECT_MIN_LEAD = 10


class SearchResult(NamedTuple):
    direct: int | None
    suggestions: list[dict]


def _normalize(text: str) -> str:
    """Lower-case and turn punctuation into spaces so "M&T" and "m t" compare alike."""
    return " ".join(re.sub(r"[^a-z0-9]+", " ", text.lower()).split())


_NORMALIZED_ALIASES = {_normalize(k): v for k, v in ALIASES.items()}


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
    ahead of the next-best hit (a same-name twin counts, so it blocks); otherwise returns up to `limit` suggestions.
    """
    q = _normalize(query)
    if not q:
        return SearchResult(None, [])
    if q in _NORMALIZED_ALIASES:
        return SearchResult(_NORMALIZED_ALIASES[q], [])

    names = [_normalize(n) for n in banks["name"]]
    hits = process.extract(q, names, scorer=fuzz.WRatio, limit=limit + 1)
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
