import json

import pandas as pd
import pytest

from canary.analyst import context as ctx_mod
from canary.analyst.context import load_context
from canary.model.train import _score_test


def test_scored_only_from_2016(analyst_ctx):
    assert analyst_ctx.scored["report_date"].min() == pd.Timestamp("2016-03-31")


def test_scored_columns_and_percentile(analyst_ctx):
    s = analyst_ctx.scored
    assert {"score", "rank", "n_banks", "percentile", "flagged"} <= set(s.columns)
    top = s[s["rank"] == 1]
    assert (top["percentile"] == 100.0).all()
    assert analyst_ctx.model_run and len(analyst_ctx.model_run) == 12


def test_flags_match_phase3_for_test_rows(analyst_ctx, trained_model, df):
    p3 = _score_test(df, trained_model)
    p3["report_date"] = pd.to_datetime(p3["report_date"])
    phase3 = p3.set_index(["cert", "report_date"])["flagged"]
    ours = analyst_ctx.scored.set_index(["cert", "report_date"])["flagged"]
    assert ours.reindex(phase3.index).equals(phase3)


def test_banks_table(analyst_ctx):
    b = analyst_ctx.banks.set_index("cert")
    assert len(b) == analyst_ctx.features["cert"].nunique()
    assert b.loc[24735, "failure_date"] is not None and b.loc[24735, "city"] == "City24735"
    assert b.loc[100, "state"] == "PA"
    assert b.loc[100, "last_report"] == analyst_ctx.latest_quarter
    assert pd.isna(b.loc[100, "city"])
    assert analyst_ctx.failures["cert"].tolist().count(3) == 1


def test_cache_reused_then_invalidated(analyst_ctx, tmp_path, failures_path, financials_dir, monkeypatch):
    features, model_dir, cache = tmp_path / "features.parquet", tmp_path / "model", tmp_path / "cache"
    meta = json.loads((cache / "scores.json").read_text())
    assert set(meta) == {"model_run", "features_size", "features_mtime"}

    def boom(*a, **k):
        raise AssertionError("rescored")

    monkeypatch.setattr(ctx_mod, "score_rows", boom)
    again = load_context(features, model_dir, failures_path, financials_dir, cache)
    assert len(again.scored) == len(analyst_ctx.scored)

    features.touch()
    import os

    os.utime(features, (1, 1))
    with pytest.raises(AssertionError, match="rescored"):
        load_context(features, model_dir, failures_path, financials_dir, cache)
