from pathlib import Path

import pandas as pd
import pytest

from canary.dashboard.suggest import BIGGEST, COLLAPSES, starter_groups, status_line

Q = pd.Timestamp("2026-06-30")


def _banks(rows):
    cols = ["cert", "has_report", "failure_date", "latest_report_date", "latest_rank", "latest_n", "latest_flagged"]
    df = pd.DataFrame(rows, columns=cols)
    df["failure_date"] = pd.to_datetime(df["failure_date"])
    df["latest_flagged"] = df["latest_flagged"].astype("boolean")
    return df


def test_groups_only_reported_banks_and_skip_empty_ones():
    df = _banks([
        (24735, True, "2023-03-10", pd.Timestamp("2022-12-31"), 3494, 4773, False),
        (628, True, None, Q, 1315, 4313, False),
        (3510, False, None, Q, 900, 4313, False),           # no report: not suggested
        (500, True, None, Q, 3, 4313, True),
        (501, True, None, Q, 1, 4313, True),
        (502, True, None, pd.Timestamp("2025-12-31"), 2, 4300, True),  # flagged, but not the latest quarter
        (503, False, None, Q, 2, 4313, True),               # flagged, no report
    ])
    groups = dict(starter_groups(df))
    assert [int(r["cert"]) for r in groups["The 2023 collapses"]] == [24735]
    assert [int(r["cert"]) for r in groups["Biggest US banks"]] == [628]
    assert [int(r["cert"]) for r in groups["On the watchlist now"]] == [501, 500]


def test_status_lines():
    df = _banks([(1, True, "2023-03-10", None, None, None, None), (2, True, None, Q, 1580, 4313, False),
                 (3, True, None, Q, 7, 4313, True)])
    assert [status_line(r) for _, r in df.iterrows()] == [
        "Failed Mar 10, 2023", "Rank #1,580 of 4,313", "Rank #7 of 4,313 · on the watchlist"]


@pytest.mark.data
@pytest.mark.skipif(not Path("dashboard/data/banks.parquet").exists(), reason="banks.parquet not exported")
def test_real_groups_are_full_and_distinct():
    groups = starter_groups(pd.read_parquet("dashboard/data/banks.parquet"))
    certs = [int(r["cert"]) for _, rows in groups for r in rows]
    assert [t for t, _ in groups] == ["The 2023 collapses", "Biggest US banks", "On the watchlist now"]
    assert certs[:7] == COLLAPSES + BIGGEST and len(certs) == 11 == len(set(certs))
