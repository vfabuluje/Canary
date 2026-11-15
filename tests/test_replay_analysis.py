from datetime import date

import numpy as np
import pandas as pd
import pytest

from canary.model.dataset import FEATURE_COLUMNS, assign_split, fails_within_4q
from canary.replay.analysis import (
    PROFILES,
    credit_loss_profile,
    distribution_table,
    failure_mix,
    false_alarm_profile,
    mix_summary,
    top_false_alarm_banks,
)
from canary.replay.runrisk import score_posthoc


def _with_signal(df, seed=1):
    out = df.copy()
    rng = np.random.default_rng(seed)
    n = len(out)
    out["htm_unrealized_loss_to_equity"] = rng.uniform(0, 1, n)
    out["afs_unrealized_loss_to_equity"] = rng.uniform(0, 0.5, n)
    out["uninsured_to_deposits"] = rng.uniform(0, 1, n)
    return out


@pytest.fixture
def scored(df):
    return score_posthoc(_with_signal(df))


def _bank_rows(cert, fail, report_dates, **cols):
    """Hand-made rows for one bank; quarters_until_failure counted from the failure quarter."""
    quarters = pd.date_range("2000-03-31", "2026-12-31", freq="QE").date.tolist()
    rows = []
    for d in report_dates:
        qtf = quarters.index(fail) - quarters.index(d) if fail else None
        row = {
            "cert": cert, "institution_name": f"Bank {cert}", "report_date": d,
            "failure_date": fail, "quarters_until_failure": qtf,
            "noncurrent_loans_to_loans": 0.01, "texas_ratio": 0.2,
            "run_risk_flagged": False, "run_risk_score": 0.0,
            "bond_loss_to_equity": 0.0, "uninsured_to_deposits": 0.1,
        }
        row.update(cols)
        rows.append(row)
    return rows


def _frame(rows):
    out = pd.DataFrame(rows)
    out["label"] = fails_within_4q(out["quarters_until_failure"])
    out["split"] = assign_split(out["report_date"])
    return out


def test_credit_loss_profile_rules():
    rows = pd.DataFrame({
        "noncurrent_loans_to_loans": [0.06, 0.01, 0.01, 0.01, np.nan],
        "texas_ratio":               [0.2, 1.2, -2.0, 0.5, np.nan],
    })
    before = rows.copy()
    assert credit_loss_profile(rows).tolist() == [True, True, True, False, False]
    assert rows.equals(before)


def test_failure_mix_one_row_per_bank_closest_to_failure(scored):
    before = scored.copy()
    mix = failure_mix(scored)
    training = mix[mix["era"] == "training"]
    assert training["cert"].tolist().count(1) == 1
    assert training["cert"].tolist().count(2) == 1
    assert (training.set_index("cert").loc[[1, 2], "quarters_until_failure"] == 1).all()
    assert 3 not in training["cert"].tolist()  # failed 2019: a test-era failure
    assert scored.equals(before)


def test_failure_mix_profiles():
    fail = date(2010, 6, 30)
    last = [date(2010, 3, 31)]
    rows = (
        _bank_rows(10, fail, last, noncurrent_loans_to_loans=0.08)
        + _bank_rows(11, fail, last, run_risk_flagged=True)
        + _bank_rows(12, fail, last, texas_ratio=1.5, run_risk_flagged=True)
        + _bank_rows(13, fail, last)
        + _bank_rows(500, None, last)  # never failed: not in the mix
    )
    frame = _frame(rows)
    before = frame.copy()
    mix = failure_mix(frame).set_index("cert")
    assert mix.loc[10, "profile"] == "credit only"
    assert mix.loc[11, "profile"] == "run-risk only"
    assert mix.loc[12, "profile"] == "both"
    assert mix.loc[13, "profile"] == "neither"
    assert 500 not in mix.index
    assert (mix["failure_year"] == 2010).all()
    assert frame.equals(before)


def test_failure_mix_uses_row_closest_to_failure():
    fail = date(2010, 6, 30)
    rows = _bank_rows(10, fail, [date(2009, 9, 30)], noncurrent_loans_to_loans=0.08) + _bank_rows(
        10, fail, [date(2010, 3, 31)]
    )
    mix = failure_mix(_frame(rows))
    assert len(mix) == 1
    assert mix.iloc[0]["quarters_until_failure"] == 1
    assert mix.iloc[0]["profile"] == "neither"


def test_failure_mix_ignores_gap_rows():
    fail = date(2016, 3, 31)  # 1-4 quarters before are all 2015 (gap year)
    rows = _bank_rows(20, fail, [date(2014, 12, 31), date(2015, 3, 31), date(2015, 12, 31)])
    frame = _frame(rows)
    mix = failure_mix(frame)
    assert 20 not in mix["cert"].tolist()


def test_failure_mix_includes_case_studies(scored):
    mix = failure_mix(scored)
    cases = mix[mix["era"] == "2023"]
    assert sorted(cases["cert"]) == [24735, 57053, 59017]
    assert (cases["quarters_until_failure"] == 1).all()


def test_mix_summary_counts():
    fail = date(2010, 6, 30)
    last = [date(2010, 3, 31)]
    rows = _bank_rows(10, fail, last, noncurrent_loans_to_loans=0.08) + _bank_rows(13, fail, last)
    summary = mix_summary(failure_mix(_frame(rows)))
    assert summary["training"] == {"credit only": 1, "run-risk only": 0, "both": 0, "neither": 1}
    assert summary["2023"] == {p: 0 for p in PROFILES}
    assert summary["training_by_year"] == {2010: {"credit only": 1, "run-risk only": 0, "both": 0, "neither": 1}}


def test_distribution_table_groups(scored):
    before = scored.copy()
    table = distribution_table(scored)
    assert set(table["variable"]) == {"bond_loss_to_equity", "uninsured_to_deposits"}
    groups = set(table["group"])
    assert {"train_positive_rows", "train_all_rows"} <= groups
    assert {"Silicon Valley Bank", "Signature Bank", "First Republic Bank"} <= groups
    pos = table[(table["variable"] == "bond_loss_to_equity") & (table["group"] == "train_positive_rows")].iloc[0]
    train_pos = scored[(scored["split"] == "train") & (scored["label"] == 1)]["bond_loss_to_equity"]
    assert pos["median"] == pytest.approx(train_pos.median())
    assert pos["p90"] == pytest.approx(train_pos.quantile(0.9))
    assert pos["share_above_0_3"] == pytest.approx((train_pos > 0.3).mean())
    assert scored.equals(before)


def _alarm_frame():
    feats = {c: [0.0, 0.0, 0.0, 0.0, 0.0] for c in FEATURE_COLUMNS}
    feats["noncurrent_loans_to_loans"] = [0.10, 0.20, 0.01, 0.03, 9.0]
    return pd.DataFrame({
        "cert": [1, 2, 3, 4, 5],
        "institution_name": ["A", "B", "C", "D", "E"],
        "report_date": [date(2018, 3, 31)] * 5,
        "flagged": [True, True, True, True, False],
        "label": [1, 1, 0, 0, 0],
        "failure_date": [date(2018, 9, 30), date(2018, 12, 31), None, date(2020, 6, 30), None],
        **feats,
    })


def test_false_alarm_profile_medians():
    frame = _alarm_frame()
    before = frame.copy()
    out = false_alarm_profile(frame).set_index("feature")
    row = out.loc["noncurrent_loans_to_loans"]
    assert row["median_true_alarm"] == pytest.approx(0.15)
    assert row["median_false_alarm"] == pytest.approx(0.02)  # unflagged row (9.0) excluded
    assert row["difference"] == pytest.approx(0.02 - 0.15)
    assert set(out.index) == set(FEATURE_COLUMNS)
    assert frame.equals(before)


def test_top_false_alarm_banks_excludes_failed():
    frame = _alarm_frame()
    extra = frame.iloc[[2]].assign(report_date=date(2018, 6, 30))
    frame = pd.concat([frame, extra], ignore_index=True)
    before = frame.copy()
    out = top_false_alarm_banks(frame)
    assert out["cert"].tolist() == [3]  # bank 4 failed in 2020; banks 1-2 failed; bank 5 never flagged
    assert out.iloc[0]["quarters_flagged"] == 2
    assert list(out.columns) == ["cert", "institution_name", "quarters_flagged"]
    assert frame.equals(before)
