"""Fuzzy bank search for the dashboard: hand-written aliases, then rapidfuzz on bank names."""

import re
from typing import NamedTuple

import pandas as pd
from rapidfuzz import fuzz, process

ALIASES: dict[str, int] = {
    "svb": 24735, "silicon valley bank": 24735, "silicon valley": 24735,
    "signature": 57053, "signature bank": 57053,
    "first republic": 59017, "first republic bank": 59017, "frb": 59017,
    "jpmorgan": 628, "jp morgan": 628, "chase": 628, "jpmorgan chase": 628, "jp morgan chase": 628,
    "chase bank": 628,
    "bank of america": 3510, "bofa": 3510,
    "citi": 7213, "citibank": 7213,
    "wells fargo": 3511, "wells": 3511,
    "goldman sachs": 33124, "goldman": 33124,
    "us bank": 6548, "u.s. bank": 6548,
    "capital one": 4297,
    "pnc": 6384,
    "truist": 9846,
    "bny": 639, "bny mellon": 639, "bank of new york mellon": 639, "bank of ny mellon": 639,
    "bank of new york": 639,
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
DIRECT_MIN_WHOLE = 80  # whole-name similarity, so a fragment ("chse" in "sachse") doesn't open a bank
CLOSE_SCORE = 90       # below this, no name is a close match (for example a credit union)
MIN_SCORE = 60         # weaker hits aren't suggested at all
CANDIDATES = 40
ALIAS_TYPO_SCORE = 85  # "chse" is close enough to "chase" to suggest JPMorgan Chase first


class SearchResult(NamedTuple):
    direct: int | None
    suggestions: list[dict]
    close: bool = True  # False when no name is a close match: the suggestions are only the nearest names


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

    Opens directly only when the top score is at least 90, at least 10 points ahead of the next-best hit
    (a same-name twin counts, so it blocks) and the whole name is similar (not just a fragment); otherwise
    returns up to `limit` suggestions. Among equally good names, banks with a written report and banks still
    reporting come first, so "wells farg" lists today's Wells Fargo before branches that closed in 2003.
    """
    q = _normalize(query)
    if not q:
        return SearchResult(None, [])
    if q in _NORMALIZED_ALIASES:
        return SearchResult(_NORMALIZED_ALIASES[q], [])

    names = [_normalize(n) for n in banks["name"]]
    hits = [h for h in process.extract(q, names, scorer=fuzz.WRatio, limit=CANDIDATES) if h[1] >= MIN_SCORE]
    latest_quarter = banks["last_report"].max()
    direct = None
    if hits and hits[0][1] >= DIRECT_MIN_SCORE and fuzz.ratio(q, hits[0][0]) >= DIRECT_MIN_WHOLE:
        runner_up = hits[1][1] if len(hits) > 1 else 0
        if hits[0][1] - runner_up >= DIRECT_MIN_LEAD:
            direct = int(banks.iloc[hits[0][2]]["cert"])
    close = bool(hits) and hits[0][1] >= CLOSE_SCORE

    def rank(hit):
        row = banks.iloc[hit[2]]
        has_report = bool(row["has_report"]) if "has_report" in row.index else False
        return -(round(hit[1]) + 4 * has_report + 2 * (row["last_report"] == latest_quarter))

    top = sorted(hits, key=rank)  # stable: equal ranks keep rapidfuzz's order
    order = [i for _, _, i in top]
    typo_certs = {cert for key, cert in _NORMALIZED_ALIASES.items()
                  if len(key) >= 4 and fuzz.ratio(q, key) >= ALIAS_TYPO_SCORE}
    typo_rows = [int(i) for i in banks["cert"].isin(typo_certs).to_numpy().nonzero()[0]]
    order = (typo_rows + [i for i in order if i not in typo_rows])[:limit]
    rows = [banks.iloc[i] for i in order]
    suggestions = []
    for row in rows:
        twin = any(o["cert"] != row["cert"] and o["name"] == row["name"] and o["state"] == row["state"]
                   for o in rows)
        label = f"{row['name']} — {row['city']}, cert {row['cert']}" if twin else row["name"]
        suggestions.append({"cert": int(row["cert"]), "name": row["name"], "state": row["state"],
                            "status": _status(row, latest_quarter), "label": label,
                            "website": row["website"] if "website" in row.index and pd.notna(row["website"]) else None})
    return SearchResult(direct, suggestions, close)
