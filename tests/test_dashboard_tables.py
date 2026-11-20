import dataclasses
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from canary.dashboard import __main__ as cli
from canary.dashboard.tables import (
    WATCHLIST_SHARES,
    export_banks,
    export_concentration,
    export_scores_history,
    showcase_certs,
    threshold_table,
    write_tables,
)

SCORES_TEST = Path("data/model/scores_test.parquet")


def _synthetic_scores(n_dates=3, n_banks=100):
    rng = np.random.default_rng(0)
    rows = []
    for d in pd.date_range("2020-03-31", periods=n_dates, freq="QE"):
        for c in range(n_banks):
            rows.append({"cert": c, "report_date": d.date().isoformat(), "quarters_until_failure": np.nan,
                         "label": 0, "score": rng.random()})
    return pd.DataFrame(rows)


def test_threshold_shares_in_order():
    table = threshold_table(_synthetic_scores())
    assert [r["share"] for r in table] == list(WATCHLIST_SHARES)
    assert [r["rows"] for r in table] == sorted(r["rows"] for r in table)


@pytest.mark.data
def test_threshold_published_share_matches_metrics():
    if not SCORES_TEST.exists():
        pytest.skip("data/model/scores_test.parquet not present")
    table = {r["share"]: r for r in threshold_table(pd.read_parquet(SCORES_TEST))}
    pub = table[0.02]
    assert (pub["caught"], pub["eligible"], pub["rows"]) == (21, 29, 3783)
    assert pub["false_alarm"] == pytest.approx(0.9828178694158075)
    assert table[0.10]["caught_case_studies"] == [57053]


def test_banks_never_scored(analyst_ctx):
    b = export_banks(analyst_ctx, set()).set_index("cert")
    assert list(export_banks(analyst_ctx, set()).columns) == [
        "cert", "name", "state", "city", "first_report", "last_report", "failure_date", "scored",
        "latest_report_date", "latest_rank", "latest_n", "latest_percentile", "latest_flagged",
        "after_test_period", "has_report"]
    assert b.loc[1, "last_report"] < pd.Timestamp("2016-03-31")
    assert not b.loc[1, "scored"]
    for col in ("latest_report_date", "latest_rank", "latest_n", "latest_percentile", "latest_flagged"):
        assert pd.isna(b.loc[1, col])
    assert not b.loc[1, "after_test_period"]
    assert b.loc[100, "scored"]


def test_banks_after_test_period(analyst_ctx):
    b = export_banks(analyst_ctx, {100}).set_index("cert")
    assert b.loc[100, "latest_report_date"] > pd.Timestamp("2024-12-31")
    assert b.loc[100, "after_test_period"]
    assert b.loc[100, "has_report"] and not b.loc[101, "has_report"]
    assert b.loc[24735, "scored"] and not b.loc[24735, "after_test_period"]
    assert b.loc[100, "name"] == "Bank 100"


def test_scores_history(analyst_ctx):
    h = export_scores_history(analyst_ctx)
    assert list(h.columns) == ["cert", "report_date", "rank", "n_banks", "percentile", "flagged"]
    assert h["report_date"].min() >= pd.Timestamp("2016-03-31")


def test_concentration_reason_kept(analyst_ctx):
    conc = analyst_ctx.concentration
    bad = (conc["cert"] == 102) & (conc["report_date"] == pd.Timestamp(analyst_ctx.latest_quarter))
    conc = conc.copy()
    conc.loc[bad, ["RBC", "RBCT1J"]] = np.nan
    ctx = dataclasses.replace(analyst_ctx, concentration=conc)
    out = export_concentration(ctx)
    assert list(out.columns) == ["cert", "as_of", "measure", "construction_pct", "cre_pct", "growth_pct",
                                 "reason", "lines"]
    assert out["cert"].is_unique
    row = out.set_index("cert").loc[102]
    assert row["reason"] and pd.isna(row["cre_pct"])
    ok = out.set_index("cert").loc[103]
    assert pd.isna(ok["reason"]) and ok["cre_pct"] > 0
    assert isinstance(ok["lines"], str) and ok["lines"]


def test_showcase_certs_needs_note_and_ok_trace(tmp_path):
    notes, traces = tmp_path / "banks", tmp_path / "traces"
    notes.mkdir(), traces.mkdir()
    for cert, ok in ((1, True), (2, False), (3, True)):
        (notes / f"B{cert} ({cert}).md").write_text(f'---\ncert: {cert}\nname: "B"\nas_of: 2024-06-30\n---\n# x\n')
        (traces / f"{cert}_2024-06-30.json").write_text(json.dumps({"cert": cert, "ok": ok}))
    (traces / "4_2024-06-30.json").write_text(json.dumps({"cert": 4, "ok": True}))  # trace, no note
    (notes / "C5 (5).md").write_text('---\ncert: 5\nas_of: 2024-06-30\n---\n')  # note, no trace
    assert showcase_certs(notes, traces) == {1, 3}


def test_write_tables(analyst_ctx, tmp_path):
    model_dir, out = tmp_path / "m", tmp_path / "out"
    model_dir.mkdir()
    metrics = {"auc": 0.9, "recall": 0.7, "banks_caught": 21, "eligible_banks": 29, "lead_time_median": 4.0,
               "false_alarm_rate": 0.98, "rows_flagged": 3783, "baseline": {"auc": 0.77}, "extra": 1}
    (model_dir / "metrics.json").write_text(json.dumps(metrics))
    _synthetic_scores().to_parquet(model_dir / "scores_test.parquet")
    write_tables(analyst_ctx, model_dir, out, {100})
    assert sorted(p.name for p in out.iterdir()) == [
        "banks.parquet", "concentration.parquet", "metrics.json", "scores_history.parquet", "threshold.json"]
    m = json.loads((out / "metrics.json").read_text())
    assert set(m) == {"auc", "recall", "banks_caught", "eligible_banks", "lead_time_median",
                      "false_alarm_rate", "rows_flagged", "baseline"}
    assert len(json.loads((out / "threshold.json").read_text())) == len(WATCHLIST_SHARES)


def test_export_cli_size_guard(analyst_ctx, tmp_path, monkeypatch, capsys):
    out = tmp_path / "out"
    out.mkdir()
    (out / "big.bin").write_bytes(b"0" * (51 * 1024 * 1024))
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    monkeypatch.setattr(cli, "write_all", lambda *a, **k: None)
    assert cli.main(["export", "--out", str(out)]) == 1
    assert "50 MB" in capsys.readouterr().err


def test_export_cli_small_ok(analyst_ctx, tmp_path, monkeypatch, capsys):
    out = tmp_path / "out"
    out.mkdir()
    (out / "a.txt").write_text("hi")
    monkeypatch.setattr(cli, "load_context", lambda *a, **k: analyst_ctx)
    monkeypatch.setattr(cli, "write_all", lambda *a, **k: None)
    assert cli.main(["export", "--out", str(out)]) == 0
    assert "a.txt" in capsys.readouterr().out
