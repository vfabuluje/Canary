"""Tests for watchlist flags and metrics. Every expected value is worked out by hand."""

from datetime import date

import numpy as np
import pandas as pd

from canary.model.metrics import (
    auc,
    bank_recall,
    false_alarm_banks,
    false_alarm_rate,
    flag_watchlist,
    lead_times,
)

Q1 = date(2020, 3, 31)
Q2 = date(2020, 6, 30)


def _scores(n: int, quarter=Q1, start_cert: int = 1) -> pd.DataFrame:
    """n banks with distinct scores; cert i has score i (higher cert = higher score)."""
    certs = list(range(start_cert, start_cert + n))
    return pd.DataFrame({"cert": certs, "report_date": quarter, "score": [float(c) for c in certs]})


def test_flag_rate_per_quarter():
    # ceil(100 * 0.02) = 2 ; ceil(101 * 0.02) = ceil(2.02) = 3
    assert flag_watchlist(_scores(100), "score").sum() == 2
    assert flag_watchlist(_scores(101), "score").sum() == 3


def test_flag_is_per_report_date():
    df = pd.concat([_scores(100, Q1), _scores(10, Q2, start_cert=1000)], ignore_index=True)
    flags = flag_watchlist(df, "score")
    assert flags[df["report_date"] == Q1].sum() == 2  # ceil(2.0)
    assert flags[df["report_date"] == Q2].sum() == 1  # ceil(0.2)
    assert flags.index.equals(df.index)
    assert flags.dtype == bool


def test_flag_small_quarter_flags_at_least_one():
    assert flag_watchlist(_scores(10), "score").sum() == 1


def test_flag_picks_highest_scores():
    df = _scores(100)
    flagged = df.loc[flag_watchlist(df, "score"), "cert"].tolist()
    assert sorted(flagged) == [99, 100]


def test_flag_ties_are_deterministic():
    # 5 equal top scores, 100 banks -> k = 2 -> the 2 lowest certs among the tied.
    df = _scores(100)
    df["score"] = 0.0
    top = [50, 20, 70, 30, 60]  # shuffled order on purpose
    df.loc[df["cert"].isin(top), "score"] = 1.0
    df = df.sample(frac=1, random_state=0)
    flagged = df.loc[flag_watchlist(df, "score"), "cert"].tolist()
    assert sorted(flagged) == [20, 30]


def test_flag_nan_scores_rank_lowest():
    df = _scores(100)
    df.loc[df["cert"] == 100, "score"] = np.nan  # would be top if NaN sorted first
    flagged = df.loc[flag_watchlist(df, "score"), "cert"].tolist()
    assert sorted(flagged) == [98, 99]


def test_flag_float_drift_guard():
    # 50 * 0.06 = 3.0000000000000004 in floats; ceil would wrongly give 4.
    assert flag_watchlist(_scores(50), "score", share=0.06).sum() == 3


def _eval_frame() -> pd.DataFrame:
    """Hand-made frame. Banks A=1, B=2, C=3 fail; D=4 never fails; E=5 fails in 2030.

    cert 1: rows at 4q, 3q, 1q before failure; flagged at 3q and 1q only
    cert 2: rows at 2q, 1q; flagged at 1q only
    cert 3: rows at 4q, 3q; never flagged
    cert 4: healthy, flagged once and once not
    cert 5: fails in 2030 (after horizon), flagged once, row has null quarters_until_failure
    """
    rows = [
        # cert, qtf, failure_date, flagged
        (1, 4, date(2021, 3, 31), False),
        (1, 3, date(2021, 3, 31), True),
        (1, 1, date(2021, 3, 31), True),
        (2, 2, date(2021, 6, 30), False),
        (2, 1, date(2021, 6, 30), True),
        (3, 4, date(2022, 3, 31), False),
        (3, 3, date(2022, 3, 31), False),
        (4, None, None, True),
        (4, None, None, False),
        (5, None, date(2030, 1, 31), True),
    ]
    df = pd.DataFrame(rows, columns=["cert", "quarters_until_failure", "failure_date", "flag"])
    df["quarters_until_failure"] = df["quarters_until_failure"].astype("Int64")
    df["failure_date"] = pd.to_datetime(df["failure_date"])
    df["report_date"] = Q1
    df["label"] = df["quarters_until_failure"].between(1, 4).fillna(False).astype(int)
    return df


def test_recall_counts_bank_once():
    # cert 1 is flagged on two rows but counts once. Eligible: 1, 2, 3. Caught: 1, 2.
    r = bank_recall(_eval_frame(), "flag")
    assert (r.caught, r.eligible) == (2, 3)
    assert r.recall == 2 / 3
    assert sorted(r.caught_certs) == [1, 2]


def test_recall_min_quarters_2():
    # Rows with qtf in [2,4]: cert 1 (4,3), cert 2 (2), cert 3 (4,3). Flagged: only cert 1 at 3q.
    # cert 2's flagged row is 1q, which no longer counts. Caught 1 of 3.
    r = bank_recall(_eval_frame(), "flag", min_quarters=2)
    assert (r.caught, r.eligible) == (1, 3)
    assert r.caught_certs == [1]


def test_bank_with_no_eligible_rows_not_in_denominator():
    # Drop cert 3's only 1-4 rows (as for a gap-year bank): denominator falls to 2.
    df = _eval_frame()
    df = df[df["cert"] != 3]
    r = bank_recall(df, "flag")
    assert (r.caught, r.eligible) == (2, 2)
    assert r.recall == 1.0


def test_recall_with_no_eligible_banks_is_nan():
    df = _eval_frame()
    df = df[df["label"] == 0]
    r = bank_recall(df, "flag")
    assert r.eligible == 0 and np.isnan(r.recall)


def test_lead_time_is_max_flagged_quarters():
    # cert 1 flagged at 3q and 1q -> 3. cert 2 flagged at 1q -> 1. cert 3 never flagged -> absent.
    # Healthy / null rows are ignored.
    lt = lead_times(_eval_frame(), "flag")
    assert lt.to_dict() == {1: 3, 2: 1}
    assert lt.index.name == "cert"


def test_false_alarm_rate():
    # Flagged rows: cert1 x2 (label 1), cert2 x1 (label 1), cert4 x1 (0), cert5 x1 (0) = 5.
    # False = 2 -> 0.4.
    assert false_alarm_rate(_eval_frame(), "flag") == 2 / 5


def test_false_alarm_rate_nothing_flagged_is_nan():
    df = _eval_frame()
    df["flag"] = False
    assert np.isnan(false_alarm_rate(df, "flag"))


def test_false_alarm_banks_excludes_later_failures():
    # Flagged certs: 1, 2, 4, 5. Failure date null for 4 (counts); 5 fails 2030 > horizon (counts);
    # 1 and 2 failed in 2021 (do not count) -> 2.
    assert false_alarm_banks(_eval_frame(), "flag") == 2
    # Horizon pushed past 2030: cert 5 now is a real failure inside the horizon -> only cert 4.
    assert false_alarm_banks(_eval_frame(), "flag", horizon_end=date(2031, 1, 1)) == 1


def test_auc():
    df = pd.DataFrame({"label": [0, 0, 1, 1], "score": [0.1, 0.4, 0.35, 0.8]})
    # Pairs: (0.35>0.1) y, (0.35>0.4) n, (0.8>0.1) y, (0.8>0.4) y -> 3/4
    assert auc(df, "score") == 0.75
