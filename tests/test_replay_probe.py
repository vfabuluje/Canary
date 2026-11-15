from datetime import date

import numpy as np
import pandas as pd
import pytest

from canary.model import train as train_mod
from canary.model.dataset import FEATURE_COLUMNS, assign_split, fails_within_4q, select_features
from canary.model.train import CASE_STUDY_CERTS, _score_test, train
from canary.replay.probe import (
    WHAT_IF_GRID,
    WHAT_IF_ROWS,
    contributions,
    replay_banks,
    test_misses as find_misses,
    what_if,
)
from canary.replay.runrisk import score_posthoc


@pytest.fixture(scope="module")
def frame(raw):
    out = raw.copy()
    rng = np.random.default_rng(1)
    n = len(out)
    out["htm_unrealized_loss_to_equity"] = rng.uniform(0, 1, n)
    out["afs_unrealized_loss_to_equity"] = rng.uniform(0, 0.5, n)
    out["uninsured_to_deposits"] = rng.uniform(0, 1, n)
    out["label"] = fails_within_4q(out["quarters_until_failure"])
    out["split"] = assign_split(out["report_date"])
    return out


@pytest.fixture(scope="module")
def model(frame):
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(train_mod, "GRID", [{"max_depth": 2, "learning_rate": 0.3, "min_child_weight": 1}])
        mp.setattr(train_mod, "MAX_TREES", 30)
        mp.setattr(train_mod, "EARLY_STOPPING_ROUNDS", 5)
        fitted, _ = train(frame)
    return fitted


@pytest.fixture(scope="module")
def test_scored(frame, model):
    return _score_test(frame, model)


def _parse(signals: str) -> list[float]:
    return [float(s.split("=")[1]) for s in signals.split(", ")] if signals else []


def test_contributions_signs_and_length(model, test_scored):
    rows = test_scored[test_scored["cert"].isin(CASE_STUDY_CERTS)].tail(6)
    before = rows.copy()
    out = contributions(model, rows)
    assert len(out) == len(rows)
    assert list(out.columns) == ["cert", "report_date", "top_positive", "top_negative"]
    for pos, neg in zip(out["top_positive"], out["top_negative"]):
        p, q = _parse(pos), _parse(neg)
        assert len(p) <= 5 and len(q) <= 5
        assert all(v > 0 for v in p) and all(v < 0 for v in q)
        assert p == sorted(p, reverse=True) and q == sorted(q)
    assert rows.equals(before)


def test_what_if_changes_one_feature(model, test_scored):
    before = test_scored.copy()
    cert, d = WHAT_IF_ROWS[0]
    out = what_if(model, test_scored, cert, d)
    original = test_scored[(test_scored["cert"] == cert) & (test_scored["report_date"] == d)]
    for _, r in out.sample(8, random_state=0).iterrows():
        probe = select_features(original).copy()
        probe[r["feature"]] = r["value"]
        assert model.predict_proba(probe)[0, 1] == pytest.approx(r["score"])
        assert r["actual_value"] == pytest.approx(original.iloc[0][r["feature"]])
    assert test_scored.equals(before)


def test_what_if_rank_excludes_self(model, test_scored):
    cert, d = WHAT_IF_ROWS[0]
    quarter = test_scored[test_scored["report_date"] == d].copy()
    own = quarter["cert"] == cert
    quarter.loc[~own, "score"] = 0.0  # every other bank scores below anything the model gives
    out = what_if(model, quarter, cert, d)
    assert (out["rank"] == 1).all()
    assert (out["n_banks"] == len(quarter)).all()
    assert (out["percentile"] == 100.0).all()


def test_what_if_rank_counts_higher_banks(model, test_scored):
    cert, d = WHAT_IF_ROWS[0]
    quarter = test_scored[test_scored["report_date"] == d].copy()
    own = quarter["cert"] == cert
    quarter.loc[~own, "score"] = 2.0  # above any probability
    out = what_if(model, quarter, cert, d)
    assert (out["rank"] == len(quarter)).all()


def test_what_if_grid_sizes(model, test_scored):
    out = what_if(model, test_scored, *WHAT_IF_ROWS[1])
    counts = out["feature"].value_counts().to_dict()
    assert counts == {
        "htm_unrealized_loss_to_equity": 16,
        "afs_unrealized_loss_to_equity": 11,
        "uninsured_to_deposits": 11,
    }
    assert set(WHAT_IF_GRID) == set(counts)


def test_what_if_missing_row_raises(model, test_scored):
    with pytest.raises(ValueError):
        what_if(model, test_scored, 999999, date(2022, 12, 31))


def _eligible(ts):
    q = pd.to_numeric(ts["quarters_until_failure"], errors="coerce")
    return ts[q.between(1, 4)]


def test_test_misses_only_unflagged_eligible(model, test_scored):
    ts = test_scored.copy()
    # Force one eligible bank to be missed so the output is not empty.
    ts.loc[ts["cert"] == 3, "flagged"] = False
    before = ts.copy()
    out = find_misses(model, ts)
    elig = _eligible(ts)
    caught = set(elig.loc[elig["flagged"], "cert"])
    missed = set(elig["cert"]) - caught
    assert set(out["cert"]) == missed and 3 in missed
    row = out.set_index("cert").loc[3]
    bank = elig[elig["cert"] == 3]
    best = bank["score"].max()
    # Highest score; on a tie, the row closest to failure (latest report date).
    assert row["report_date"] == bank.loc[bank["score"] == best, "report_date"].max()
    assert 0 < row["best_percentile"] <= 100
    assert len(_parse(row["top_signals"])) <= 3
    assert {"credit_loss", "failure_date", "quarters_until_failure", "institution_name"} <= set(out.columns)
    assert ts.equals(before)


def test_replay_banks_columns_and_window(frame, model, test_scored):
    scored = score_posthoc(frame)
    out = replay_banks(test_scored, scored)
    assert set(out["cert"]) == set(CASE_STUDY_CERTS)
    assert (pd.to_datetime(out["report_date"]) >= pd.Timestamp("2021-03-31")).all()
    expected = [
        "cert", "institution_name", "report_date", "quarters_until_failure", "model_score",
        "model_rank", "model_percentile", "model_flagged", "run_risk_score", "run_risk_rank",
        "run_risk_flagged", "corrected_baseline_rank", "corrected_baseline_flagged",
        "htm_unrealized_loss_to_equity", "afs_unrealized_loss_to_equity", "uninsured_to_deposits",
        "tier1_risk_based_ratio", "interest_expense_to_assets_ann", "securities_to_assets",
    ]
    assert list(out.columns) == expected
    # model rank 1 = highest score that quarter, against every test bank
    for _, r in out.iterrows():
        q = test_scored[test_scored["report_date"] == r["report_date"]]
        assert r["model_rank"] == 1 + int((q["score"] > r["model_score"]).sum()) + int(
            ((q["score"] == r["model_score"]) & (q["cert"] < r["cert"])).sum()
        )
        s = scored[scored["report_date"] == r["report_date"]]
        assert r["run_risk_rank"] == 1 + int((s["run_risk_score"] > r["run_risk_score"]).sum()) + int(
            ((s["run_risk_score"] == r["run_risk_score"]) & (s["cert"] < r["cert"])).sum()
        )
    assert (out["model_flagged"] == (out["model_rank"] <= 1)).all()  # 40 banks x 2% -> k = 1


def test_feature_columns_present():
    for col in ("tier1_risk_based_ratio", "interest_expense_to_assets_ann", "securities_to_assets"):
        assert col in FEATURE_COLUMNS
