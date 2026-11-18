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


# ---- final-review fixes ----------------------------------------------------------------

def test_history_and_front_matter_with_shuffled_scores(analyst_ctx, tmp_path):
    import yaml

    from canary.analyst.render import render_note
    from test_analyst_writer import _memo

    analyst_ctx.scored = analyst_ctx.scored.sample(frac=1.0, random_state=7).reset_index(drop=True)
    sheet = build_fact_sheet(analyst_ctx, 24735, replay_dir=tmp_path / "none")
    h = sheet.history
    assert len(h) == 8 and h["report_date"].iloc[-1] == pd.Timestamp(sheet.as_of)
    assert h["report_date"].is_monotonic_increasing
    assert sheet.after_history.empty or sheet.after_history["report_date"].is_monotonic_increasing
    meta = {"model_run": "r", "written_at": "t", "writer_model": "m"}
    fm = yaml.safe_load(render_note(sheet, _memo(sheet), sections.all_sections(sheet.outcome.kind), meta)
                        .split("---\n")[1])
    s = analyst_ctx.scored
    row = s[(s["cert"] == 24735) & (s["report_date"] == pd.Timestamp(sheet.as_of))].iloc[0]
    assert fm["rank"] == int(row["rank"]) and fm["n_banks"] == int(row["n_banks"])
    assert fm["flagged"] is bool(row["flagged"]) and fm["percentile"] == pytest.approx(float(row["percentile"]))


def test_driver_facts_accept_value_forms(analyst_ctx):
    from canary.analyst.labels import display_forms

    sheet = build_fact_sheet(analyst_ctx, 3)
    d = next(f for f in sheet.facts if f.label.startswith("Driver up #1") and not f.hindsight)
    feature = d.source.split("feature ")[1].split(" ")[0]
    s = analyst_ctx.features
    v = s[(s["cert"] == 3) & (s["report_date"] == pd.Timestamp(sheet.as_of))].iloc[0][feature]
    for form in display_forms(feature, float(v)):
        assert form in d.forms
    assert display_forms(feature, float(v))[0] in d.label


def test_later_rank_facts_say_flagged(analyst_ctx):
    s = analyst_ctx.scored
    later = s[(s["cert"] == 3) & (s["report_date"] > pd.Timestamp(date(2018, 3, 31)))].sort_values("report_date")
    s.loc[later.index, "flagged"] = False
    s.loc[later.index[0], "flagged"] = True
    sheet = build_fact_sheet(analyst_ctx, 3, as_of=date(2018, 3, 31))
    rk = [f for f in sheet.facts if f.label.startswith("Rank in a later quarter")]
    assert "flagged (on the watchlist)" in rk[0].label and "(flagged)" in rk[0].display
    assert all("not flagged" in f.label and "not flagged" in f.display for f in rk[1:])


def _what_if_dir(tmp_path, cert, report_date):
    d = tmp_path / "wi"
    d.mkdir(exist_ok=True)
    pd.DataFrame({"cert": cert, "report_date": report_date, "feature": "htm_unrealized_loss_to_equity",
                  "value": [0.0, 0.5, 1.0], "score": 0.1, "rank": [300, 120, 200], "n_banks": 4773,
                  "percentile": 50.0, "actual_value": 0.98}).to_csv(d / "what_if.csv", index=False)
    return d


def test_what_if_facts_for_missed_bank(analyst_ctx, tmp_path):
    s = analyst_ctx.scored
    s.loc[s["cert"] == 3, "flagged"] = False
    d = _what_if_dir(tmp_path, 3, "2019-09-30")
    sheet = build_fact_sheet(analyst_ctx, 3, replay_dir=d)
    assert sheet.outcome.kind == "missed"
    wi = [f for f in sheet.facts if f.label.startswith("What-if")]
    assert len(wi) == 1 and wi[0].hindsight and POSTHOC_LABEL in wi[0].label
    assert wi[0].value == 120 and "120" in wi[0].forms and "50%" in wi[0].forms and "4,773" in wi[0].forms
    assert wi[0].quarter == date(2019, 9, 30)


def test_no_what_if_facts_for_caught_bank(analyst_ctx, tmp_path):
    d = _what_if_dir(tmp_path, 3, "2019-09-30")
    sheet = build_fact_sheet(analyst_ctx, 3, replay_dir=d)
    assert sheet.outcome.kind == "caught"
    assert not any(f.label.startswith("What-if") for f in sheet.facts)


def test_late_flag_hindsight_fact(analyst_ctx, tmp_path):
    from test_analyst_outcome import _fail_in_2025

    _fail_in_2025(analyst_ctx, flag="2025-03-31")
    sheet = build_fact_sheet(analyst_ctx, 101, replay_dir=tmp_path / "none")
    assert sheet.outcome.kind == "missed"
    late = [f for f in sheet.facts if f.label.startswith("Flagged at Q1 2025, after the 2016-2024 test period")]
    assert late and late[0].hindsight and late[0].quarter == date(2025, 3, 31)
    assert "not counted in the reported results" in late[0].label
