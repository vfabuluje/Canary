"""Starter banks for the empty Find page: famous failures, the biggest banks and today's watchlist.

Only banks with a written report are suggested, so every pick opens the full replay and report.
"""

import pandas as pd

from canary.dashboard.copy import (FIND_START_BIG, FIND_START_COLLAPSES, FIND_START_WATCHLIST)

COLLAPSES = [24735, 57053, 59017]  # SVB, Signature, First Republic
BIGGEST = [628, 3510, 7213, 3511]  # JPMorgan Chase, Bank of America, Citibank, Wells Fargo
WATCHLIST_COUNT = 4


def status_line(row: pd.Series) -> str:
    """'Failed Mar 10, 2023', or 'Rank #1,580 of 4,313' (+ ' · on the watchlist')."""
    if pd.notna(row["failure_date"]):
        d = row["failure_date"]
        return f"Failed {d.strftime('%b')} {d.day}, {d.year}"
    if pd.notna(row["latest_rank"]) and pd.notna(row["latest_n"]):
        flagged = " · on the watchlist" if row["latest_flagged"] is True or row["latest_flagged"] == True else ""  # noqa: E712
        return f"Rank #{int(row['latest_rank']):,} of {int(row['latest_n']):,}{flagged}"
    return ""


def starter_groups(banks: pd.DataFrame) -> list[tuple[str, list[pd.Series]]]:
    """(title, rows) for each group that has at least one bank with a report; no bank appears twice."""
    reported = banks[banks["has_report"]].set_index("cert", drop=False)
    used: set[int] = set()

    def pick(certs) -> list[pd.Series]:
        rows = [reported.loc[c] for c in certs if c in reported.index and c not in used]
        used.update(int(r["cert"]) for r in rows)
        return rows

    latest = banks["latest_report_date"].max()
    on_list = reported[(reported["latest_flagged"] == True) & (reported["latest_report_date"] == latest)  # noqa: E712
                       & reported["failure_date"].isna()].sort_values("latest_rank")
    groups = [(FIND_START_COLLAPSES, pick(COLLAPSES)), (FIND_START_BIG, pick(BIGGEST)),
              (FIND_START_WATCHLIST, pick([c for c in on_list["cert"] if c not in used][:WATCHLIST_COUNT]))]
    return [(title, rows) for title, rows in groups if rows]
