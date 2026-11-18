import json
from datetime import date

import numpy as np
import pandas as pd
import pytest

from canary.analyst import sections
from canary.analyst.facts import POSTHOC_LABEL, build_fact_sheet
from canary.model.dataset import select_features
from canary.replay import probe
from canary.replay.probe import contributions


@pytest.fixture
def tmp_replay_dir(analyst_ctx, tmp_path):
    d = tmp_path / "replay"
    d.mkdir()
    s = analyst_ctx.scored
    row = s[s["cert"] == 3].iloc[-1]
    pd.DataFrame(
        {"cert": [3], "report_date": [row["report_date"].date().isoformat()], "run_risk_rank": [42], "run_risk_flagged": [True]}
    ).to_csv(d / "replay_banks.csv", index=False)
    mix = {"credit only": 462, "run-risk only": 1, "both": 53, "neither": 23}
    (d / "posthoc_metrics.json").write_text(json.dumps({"failure_mix": {"training": mix}}))
    return d


def test_fact_ids_unique_and_sequential(analyst_ctx):
    sheet = build_fact_sheet(analyst_ctx, 3)
    assert [f.id for f in sheet.facts] == [f"F{i}" for i in range(1, len(sheet.facts) + 1)]
    assert sheet.by_id("F1") is sheet.facts[0]


def test_no_nan_facts(analyst_ctx):
    s = analyst_ctx.scored
    from canary.analyst.outcome import default_as_of

    as_of = default_as_of(analyst_ctx, 100)
    analyst_ctx.features.loc[
        (analyst_ctx.features["cert"] == 100) & (analyst_ctx.features["report_date"] == pd.Timestamp(as_of)),
        "tier1_risk_based_ratio",
    ] = np.nan
    sheet = build_fact_sheet(analyst_ctx, 100)
    assert all(f.display != "nan" and "nan" not in f.forms for f in sheet.facts)
    assert not any("tier 1" in f.label.lower() and f.quarter == sheet.as_of for f in sheet.facts)


def test_as_of_facts_not_after_as_of(analyst_ctx):
    sheet = build_fact_sheet(analyst_ctx, 3)
    assert all(f.quarter is None or f.quarter <= sheet.as_of for f in sheet.facts if not f.hindsight)


def test_drivers_match_phase4_contributions(analyst_ctx):
    sheet = build_fact_sheet(analyst_ctx, 3)
    s = analyst_ctx.scored
    row = s[(s["cert"] == 3) & (s["report_date"] == pd.Timestamp(sheet.as_of))]
    top = contributions(analyst_ctx.model, row).iloc[0]["top_positive"].split(",")[0].split("=")[0]
    up = [f for f in sheet.facts if f.label.startswith("Driver up #1")]
    assert up and top in up[0].source


def test_posthoc_fact_labeled(analyst_ctx, tmp_replay_dir):
    from canary.analyst.outcome import default_as_of

    sheet = build_fact_sheet(analyst_ctx, 3, replay_dir=tmp_replay_dir)
    rr = [f for f in sheet.facts if "run-risk" in f.label.lower() and "rank" in f.label.lower()]
    assert rr and POSTHOC_LABEL in rr[0].label and rr[0].value == 42
    assert rr[0].hindsight


def test_missing_replay_skips_facts(analyst_ctx, tmp_path):
    sheet = build_fact_sheet(analyst_ctx, 3, replay_dir=tmp_path / "none")
    assert not any("run-risk" in f.label.lower() or "training" in f.label.lower() for f in sheet.facts)


def test_training_mix_facts_and_cant_see(analyst_ctx, tmp_replay_dir):
    ctx = analyst_ctx
    ctx.features["noncurrent_loans_to_loans"] = 0.0
    ctx.features["texas_ratio"] = 0.1
    sheet = build_fact_sheet(ctx, 3, replay_dir=tmp_replay_dir)
    share = [f for f in sheet.facts if "credit-loss" in f.label.lower()]
    assert share and "96%" in share[0].forms and "96%" in sheet.cant_see
    assert "depositor" in sheet.cant_see


def test_credit_loss_bank_has_no_training_mix(analyst_ctx, tmp_replay_dir):
    ctx = analyst_ctx
    ctx.features["noncurrent_loans_to_loans"] = 0.5
    sheet = build_fact_sheet(ctx, 3, replay_dir=tmp_replay_dir)
    assert not any("credit-loss" in f.label.lower() for f in sheet.facts)
    assert "96%" not in sheet.cant_see and "depositor" in sheet.cant_see


def test_date_forms(analyst_ctx):
    sheet = build_fact_sheet(analyst_ctx, 3)
    f = next(f for f in sheet.facts if f.quarter == sheet.as_of)
    d = sheet.as_of
    for form in (d.isoformat(), f"Q{(d.month - 1) // 3 + 1} {d.year}", f"{d:%B} {d.day}, {d.year}", str(d.year)):
        assert form in f.forms


def test_outcome_facts_hindsight(analyst_ctx):
    sheet = build_fact_sheet(analyst_ctx, 3, as_of=date(2018, 3, 31))
    assert sheet.outcome.kind == "caught"
    hs = [f for f in sheet.facts if f.hindsight]
    assert any("failure" in f.label.lower() for f in hs)
    assert any("lead" in f.label.lower() for f in hs)
    assert (sheet.after_history["report_date"] > pd.Timestamp(sheet.as_of)).all()
    assert len(sheet.history) <= 8


def test_bad_as_of_raises(analyst_ctx):
    with pytest.raises(ValueError):
        build_fact_sheet(analyst_ctx, 3, as_of=date(2015, 12, 31))


def test_quiet_bank_has_no_outcome_section():
    assert "outcome" not in [s.key for s in sections.all_sections("quiet")]
    assert sections.all_sections("missed")[4].title == "Why the model missed it"


def test_section_order_and_specialists():
    keys = [s.key for s in sections.all_sections("caught")]
    assert keys == ["summary", "warning_signs", "score", "score_history", "outcome", "what_next", "sources"]

    class Spec:
        key = "x"
        sections = [sections.Section("x", "X", "as_of", "", True)]

        def build_facts(self, ctx, sheet):
            return []

    sections.register(Spec())
    try:
        keys = [s.key for s in sections.all_sections("caught")]
        assert keys[4] == "x" and keys[3] == "score_history"
    finally:
        sections.SPECIALISTS.clear()


def test_contribution_matrix_alias():
    assert probe._contribs is probe.contribution_matrix
