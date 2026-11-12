# Phase 4 Replay and Error Analysis Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Explain why the Phase 3 model missed SVB, Signature and First Republic, and evaluate a post-hoc run-risk check and a corrected Texas-ratio baseline, without touching the Phase 3 model or its outputs.

**Architecture:** A new local package `canary.replay` reads the Phase 3 feature export and saved model, computes post-hoc scores (`runrisk.py`), model-free analysis (`analysis.py`) and model probes (`probe.py`), and writes CSV/JSON to its own output folder through a CLI (`__main__.py`). Humans then write the report, decisions and README from those files.

**Tech Stack:** Python 3.12, pandas, xgboost, scikit-learn (all already installed). pytest. No AWS, no dbt changes.

**Spec:** `specs/2026-11-11-phase4-replay-design.md`

## Global Constraints

- Every run-risk and corrected-baseline number is labeled post-hoc: `posthoc_metrics.json` has top-level `"post_hoc": true` and a `"note"` string saying "designed after seeing the 2023 failures".
- Run-risk formula is fixed (spec §6): `bond_loss_to_equity = htm_unrealized_loss_to_equity + afs_unrealized_loss_to_equity` (both null → null, one null → the other); `run_risk_score = clip(uninsured_to_deposits, 0, 1) * bond_loss_to_equity`; null uninsured → null score. No variants.
- Watchlist share is `WATCHLIST_SHARE` (0.02) via the existing `flag_watchlist`. Do not change it.
- Credit-loss profile (spec §8.1): `noncurrent_loans_to_loans >= 0.05` or `texas_ratio >= 1.0` or `texas_ratio < 0`.
- Case-study certs: SVB 24735, Signature 57053, First Republic 59017 (`CASE_STUDY_CERTS`), replay from `CASE_STUDY_START` = 2021-03-31.
- Never write into the Phase 3 model folder; never modify `model.json`, `metrics.json`, `scores_test.parquet`.
- Local data lives at `data.nosync/` on Victor's machine; every path is a CLI argument.
- Run tests with `.venv.nosync/bin/python -m pytest`.
- No AWS calls. No credentials. Nothing about Victor personally in committed files.

## Review Focus

1. **NaN scores in AUC.** Run-risk is null for many early-year and small banks; `roc_auc_score` rejects NaN. Expected: the existing `_summary` fill-below-min rule is applied and the number of null-score rows is reported next to the AUC (Task 2 test `test_window_summary_reports_null_scores`).
2. **A bank missing from a quarter in what-if.** The what-if rank must be computed against the other banks' real scores that quarter, excluding the probed bank's own row, so the probed bank is not counted twice (Task 4 test `test_what_if_rank_excludes_self`).
3. **Input frame mutation.** Analysis functions get the shared loaded frame; mutating it would corrupt later outputs. Expected: inputs are unchanged after every public function (Tasks 2–4 tests assert `df.equals(before)`).
4. **Failure-mix window edge.** A bank whose only 1–4-quarter rows are in the 2015 gap must not be classified as a training-era failure (Task 3 test `test_failure_mix_ignores_gap_rows`).
5. **`--out` pointing at the model folder by another spelling** (trailing slash, `./data/model`). Expected: refused after `Path.resolve()` (Task 5 test `test_cli_refuses_model_folder_alias`).

---

### Task 1: Shared synthetic fixtures

Move the synthetic dataset out of `tests/test_model_train.py` so the replay tests can reuse it.

**Files:**
- Modify: `tests/conftest.py` (add fixtures)
- Modify: `tests/test_model_train.py` (remove moved fixtures; keep an autouse wrapper)

**Interfaces:**
- Produces (pytest fixtures in `tests/conftest.py`): `raw` (module scope, unchanged content), `df` (adds `label`, `split`), `features_path`, `small_grid` (not autouse; same monkeypatches as today), helper `_quarters`.
- `tests/test_model_train.py` keeps `@pytest.fixture(autouse=True) def _small(small_grid): pass`.

- [ ] **Step 1:** Move `_quarters`, `STRONG`, `raw`, `df`, `features_path`, and the `small_grid` body into `tests/conftest.py` (`small_grid` without `autouse`). Add the autouse wrapper in `test_model_train.py`.
- [ ] **Step 2:** Run `.venv.nosync/bin/python -m pytest -q`. Expected: same pass count as before the move (142 passed).
- [ ] **Step 3:** Commit: `git commit -m "Move synthetic model fixtures to conftest for reuse"`

---

### Task 2: Post-hoc scores and metrics (`runrisk.py`)

**Files:**
- Create: `src/canary/replay/__init__.py` (empty docstring), `src/canary/replay/runrisk.py`
- Modify: `src/canary/model/train.py` — `_summary` gains keyword `horizon_end: date = date(2025, 12, 31)`, passed to `false_alarm_banks`. Default keeps Phase 3 behavior.
- Test: `tests/test_replay_runrisk.py`

**Interfaces:**
- Consumes: `flag_watchlist`, `bank_recall`, `_summary` (canary.model), `assign_split`.
- Produces:
  - `bond_loss_to_equity(df) -> pd.Series`
  - `run_risk_score(df) -> pd.Series`
  - `corrected_texas_score(df) -> pd.Series` — `texas_ratio`, with every negative value replaced by `+inf`; null stays null.
  - `score_posthoc(df) -> pd.DataFrame` — copy of rows with `split in {"train", "gap", "test"}` (report dates 2001-03-31..2024-12-31), adding `bond_loss_to_equity`, `run_risk_score`, `run_risk_flagged`, `corrected_baseline_score`, `corrected_baseline_flagged`; flags computed per report date over all those rows; index reset.
  - `window_summary(rows, score_col, flag_col, horizon_end) -> dict` — `_summary(...)` plus `"n_null_scores": int`.
  - `watchlist_overlap(rows, flag_a, flag_b) -> dict` with keys `rows_both`, `rows_a_only`, `rows_b_only`, `banks_both`.
  - `posthoc_metrics(scored, model_flagged) -> dict` — `model_flagged` is a bool Series aligned to the test-window rows of `scored`; returns `{"post_hoc": True, "note": ..., "run_risk": {"test_2016_2024": ..., "train_era_2001_2014": ...}, "corrected_baseline": {"test_2016_2024": ...}, "overlap_with_model_test": ..., "case_study_flags": {cert: [report_date strings where run_risk_flagged]}}`. Train-era horizon is 2015-12-31.

- [ ] **Step 1: Write failing tests** in `tests/test_replay_runrisk.py`:

```python
def test_run_risk_score_cases():
    df = pd.DataFrame({
        "htm_unrealized_loss_to_equity": [0.5, np.nan, 0.5, np.nan, -0.2, 0.4],
        "afs_unrealized_loss_to_equity": [0.1, 0.3, np.nan, np.nan, 0.0, 0.0],
        "uninsured_to_deposits":         [0.5, 0.5, 0.5, 0.5, 0.9, 1.7],
    })
    before = df.copy()
    s = run_risk_score(df)
    assert s.tolist()[:3] == pytest.approx([0.3, 0.15, 0.25])
    assert np.isnan(s[3])                 # both losses null
    assert s[4] == pytest.approx(-0.18)   # gains kept, rank low
    assert s[5] == pytest.approx(0.4)     # uninsured clipped to 1
    assert df.equals(before)

def test_run_risk_null_uninsured_is_null(): ...  # uninsured NaN -> NaN

def test_corrected_texas_insolvent_ranks_worst():
    df = pd.DataFrame({"texas_ratio": [0.2, -3.0, 5.0, np.nan]})
    s = corrected_texas_score(df)
    assert s[1] == np.inf and s[0] < s[2] and np.isnan(s[3])

def test_score_posthoc_window_and_flags(df):
    scored = score_posthoc(df)
    d = pd.to_datetime(scored["report_date"])
    assert d.min() == pd.Timestamp("2001-03-31") and d.max() == pd.Timestamp("2024-12-31")
    per_q = scored.groupby("report_date")["run_risk_flagged"].sum()
    assert (per_q >= 1).all()

def test_window_summary_reports_null_scores(df):  # some NaN run-risk -> finite auc, n_null_scores counted
def test_watchlist_overlap_counts(): ...           # hand-made 4-row frame, known counts
def test_posthoc_metrics_labeled(df):
    m = posthoc_metrics(...)
    assert m["post_hoc"] is True and "2023" in m["note"]
    assert set(m["case_study_flags"]) == {24735, 57053, 59017}
def test_summary_default_horizon_unchanged(df):    # _summary without horizon_end == Phase 3 result
```

(The synthetic `raw` fixture has no loss/uninsured signal tied to failure; tests that need run-risk columns set them with `rng.uniform` inside the test.)

- [ ] **Step 2:** Run `.venv.nosync/bin/python -m pytest tests/test_replay_runrisk.py -q`. Expected: FAIL (module not found).
- [ ] **Step 3:** Implement the functions above.
- [ ] **Step 4:** Run the replay tests and the full suite. Expected: all pass.
- [ ] **Step 5:** Commit: `git commit -m "Add post-hoc run-risk check and corrected Texas baseline"`

---

### Task 3: Model-free analysis (`analysis.py`)

**Files:**
- Create: `src/canary/replay/analysis.py`
- Test: `tests/test_replay_analysis.py`

**Interfaces:**
- Consumes: `score_posthoc` output (`scored`) from Task 2.
- Produces:
  - `CREDIT_NONCURRENT = 0.05`, `CREDIT_TEXAS = 1.0`
  - `credit_loss_profile(rows) -> pd.Series[bool]` — spec §8.1 rule (negative Texas counts as insolvent → True).
  - `failure_mix(scored) -> pd.DataFrame` — one row per failed bank with ≥1 row where `split == "train"` and `quarters_until_failure` in 1..4; uses the row with the smallest `quarters_until_failure`. Columns: `cert, institution_name, failure_date, failure_year, report_date, quarters_until_failure, credit_loss, run_risk, profile` (`profile` ∈ `"credit only", "run-risk only", "both", "neither"`), plus the same row for each case-study cert at its last pre-failure row (`era = "2023"` vs `"training"` column).
  - `mix_summary(mix) -> dict` — counts by `profile` for each era, and by `failure_year` × `profile` for training.
  - `distribution_table(scored) -> pd.DataFrame` — for `bond_loss_to_equity` and `uninsured_to_deposits`: median, p90, p99, and share > 0.3 for groups `train_positive_rows`, `train_all_rows`, and each case-study bank's last pre-failure row value.
  - `false_alarm_profile(test_scored) -> pd.DataFrame` — `test_scored` has model `flagged`, `label`, `failure_date` and features; median of each `FEATURE_COLUMNS` feature for flagged & label 1 vs flagged & label 0, plus a `difference` column.
  - `top_false_alarm_banks(test_scored, n=10) -> pd.DataFrame` — banks flagged most often that did not fail by 2025-12-31: `cert, institution_name, quarters_flagged`.

- [ ] **Step 1: Write failing tests**, asserting:
  - `test_credit_loss_profile_rules`: rows (noncurrent 0.06, texas 0.2) → True; (0.01, 1.2) → True; (0.01, -2.0) → True; (0.01, 0.5) → False; (NaN, NaN) → False.
  - `test_failure_mix_one_row_per_bank_closest_to_failure`: in the `df` fixture with run-risk columns set, cert 1 appears once with `quarters_until_failure == 1`; cert 2 likewise; cert 3 (test-era failure) absent from the training era.
  - `test_failure_mix_profiles`: hand-made frame with four banks hitting each profile → expected labels.
  - `test_failure_mix_ignores_gap_rows`: a bank failing 2016-03-31 whose 1–4 rows are all in 2015 is not in the training era.
  - `test_failure_mix_includes_case_studies`: the three certs appear with `era == "2023"`.
  - `test_false_alarm_profile_medians`: tiny frame with known medians.
  - `test_top_false_alarm_banks_excludes_failed`: a bank failing 2020 is not listed.
  - Each test asserts the input frame is unchanged.
- [ ] **Step 2:** Run `pytest tests/test_replay_analysis.py -q`. Expected: FAIL.
- [ ] **Step 3:** Implement.
- [ ] **Step 4:** Run tests. Expected: PASS.
- [ ] **Step 5:** Commit: `git commit -m "Add failure-mix, distribution and false-alarm analysis"`

---

### Task 4: Model probes (`probe.py`)

**Files:**
- Create: `src/canary/replay/probe.py`
- Test: `tests/test_replay_probe.py`

**Interfaces:**
- Consumes: an `xgboost.XGBClassifier`; `_score_test` (canary.model.train) output `test_scored` (has `score`, `flagged`); `select_features`, `FEATURE_COLUMNS`.
- Produces:
  - `contributions(model, rows, n=5) -> pd.DataFrame` — per row: `cert, report_date, top_positive, top_negative` (strings formatted like Phase 3's `format_signals`: `name=+0.123`, positive largest first; negative most negative first; each ≤ n items, only strictly positive / strictly negative).
  - `WHAT_IF_GRID = {"htm_unrealized_loss_to_equity": 0.0..1.5 step 0.1, "afs_unrealized_loss_to_equity": 0.0..1.0 step 0.1, "uninsured_to_deposits": 0.0..1.0 step 0.1}` (use `np.round(np.arange(...), 2)`).
  - `what_if(model, test_scored, cert, report_date, grid=WHAT_IF_GRID) -> pd.DataFrame` — columns `cert, report_date, feature, value, score, rank, n_banks, percentile, actual_value`. Rank = 1 + number of *other* banks that quarter with score > new score; `n_banks` = number of banks that quarter; percentile as in Phase 3 (`100 * (n - rank + 1) / n`).
  - `WHAT_IF_ROWS = [(24735, date(2022,12,31)), (57053, date(2022,12,31)), (59017, date(2023,3,31))]`
  - `test_misses(model, test_scored) -> pd.DataFrame` — eligible failed banks (any test row with `quarters_until_failure` 1..4) never flagged on such a row; per bank its highest-scoring eligible row: `cert, institution_name, failure_date, report_date, quarters_until_failure, best_percentile, top_signals` (top 3 positive), plus `credit_loss` from `credit_loss_profile`.
  - `replay_banks(test_scored, scored) -> pd.DataFrame` — case-study certs from 2021-03-31: `cert, institution_name, report_date, quarters_until_failure, model_score, model_rank, model_percentile, model_flagged, run_risk_score, run_risk_rank, run_risk_flagged, corrected_baseline_rank, corrected_baseline_flagged, htm_unrealized_loss_to_equity, afs_unrealized_loss_to_equity, uninsured_to_deposits, tier1_risk_based_ratio, interest_expense_to_assets_ann, securities_to_assets`. Ranks are national within the quarter, ties by cert, NaN last (same ordering as `flag_watchlist`).

- [ ] **Step 1: Write failing tests** (use `small_grid` + `train(df)` from the conftest fixtures; scope the trained model per module):
  - `test_contributions_signs_and_length`: every listed positive value > 0, negatives < 0, ≤ 5 each, sorted.
  - `test_what_if_changes_one_feature`: for each output row, re-scoring the original row with only that feature replaced reproduces `score`; `test_scored` unchanged.
  - `test_what_if_rank_excludes_self`: if the new score equals the bank's own original score and it is the quarter's maximum, rank == 1.
  - `test_what_if_grid_sizes`: 16 + 11 + 11 rows per probed bank-quarter.
  - `test_test_misses_only_unflagged_eligible`: on the synthetic test set, no cert in the output has any flagged eligible row, and every eligible unflagged bank appears.
  - `test_replay_banks_columns_and_window`: only the three certs, report dates ≥ 2021-03-31, model rank 1 = highest score.
- [ ] **Step 2:** Run `pytest tests/test_replay_probe.py -q`. Expected: FAIL.
- [ ] **Step 3:** Implement.
- [ ] **Step 4:** Run tests. Expected: PASS.
- [ ] **Step 5:** Commit: `git commit -m "Add contributions, what-if, misses and replay tables"`

---

### Task 5: CLI (`python -m canary.replay`)

**Files:**
- Create: `src/canary/replay/__main__.py`
- Test: `tests/test_replay_cli.py`

**Interfaces:**
- Consumes: everything above; `load_dataset`; `_score_test`; `_jsonable`.
- Produces: `main(argv) -> int` with arguments `--features PATH` (required), `--model-dir PATH` (default `data/model`), `--out PATH` (default `data/replay`). Writes to `--out`: `posthoc_metrics.json` (also contains `mix_summary` under `"failure_mix"`), `replay_banks.csv`, `contributions.csv` (last two reports of each case-study bank), `what_if.csv` (all `WHAT_IF_ROWS`), `training_mix.csv`, `distributions.csv`, `test_misses.csv`, `false_alarm_profile.csv`, `top_false_alarm_banks.csv`. Overwriting its own outputs is allowed (it is deterministic).
- Returns 1 with a logged error if `--out` resolves to the same path as `--model-dir`, or if `model.json` is missing.

- [ ] **Step 1: Write failing tests:**
  - `test_cli_writes_every_output(features_path, tmp_path)`: train with the synthetic data, save `model.json` to `tmp_path/"model"`, run `main([...])` → 0 and each of the nine files exists; `posthoc_metrics.json["post_hoc"] is True`.
  - `test_cli_refuses_model_folder(...)`: `--out` == `--model-dir` → 1, nothing written.
  - `test_cli_refuses_model_folder_alias(...)`: `--out f"{model_dir}/"` and `--out model_dir/"."` → 1.
  - `test_cli_does_not_touch_model_folder(...)`: model folder listing and file hashes identical before and after a run.
- [ ] **Step 2:** Run. Expected: FAIL.
- [ ] **Step 3:** Implement.
- [ ] **Step 4:** Run the full suite. Expected: all pass.
- [ ] **Step 5:** Commit: `git commit -m "Add canary.replay CLI"`

---

### Task 6: Live run (local, no AWS)

- [ ] **Step 1:** Run:
```bash
.venv.nosync/bin/python -m canary.replay --features data.nosync/features/fct_bank_features.parquet --model-dir data.nosync/model --out data.nosync/replay
```
Expected: exit 0, nine files in `data.nosync/replay/`.
- [ ] **Step 2: Sanity checks** (print and compare):
  - `replay_banks.csv` model ranks for SVB match Phase 3 `data.nosync/model/case_studies.csv` ranks for the same quarters.
  - SVB run-risk ranks at 2021-12-31..2022-12-31 match the spec §5 pre-look (3, 9, 63, 70, 54) — this checks the formula, not the result.
  - `what_if.csv` row for SVB HTM at the actual value reproduces the 2022-12-31 score 0.0023 (to 4 decimals).
  - `shasum data.nosync/model/*` unchanged from before the run.
- [ ] **Step 3:** Record any mismatch as a finding; do not change the formula to remove one.

---

### Task 7: Documentation from the results

**Files:**
- Create: `analysis/phase4-replay.md`, `decisions/0013-run-risk-check.md`, `decisions/0014-corrected-texas-baseline.md`, `decisions/0015-failure-mix-profiles.md`, `data-dictionary/replay_outputs.md`
- Modify: `runbooks/model-training.md` (add "Phase 4 replay" section: command, inputs, outputs, failure modes), `reference/GLOSSARY.md` (post-hoc, run-risk score, what-if analysis), `README.md`, `daily-log.md`

- [ ] **Step 1:** Decisions 0013–0015 in the existing decision format (Date, Status, Decision, Why, Alternatives), content from spec §5–§8 and the alternatives rejected there.
- [ ] **Step 2:** `data-dictionary/replay_outputs.md`: every column of every output file (Task 5 list), with meaning and units.
- [ ] **Step 3:** `analysis/phase4-replay.md`: per spec §8 and §11 — the three questions, replay tables, failure mix, what-if, contributions, misses, false alarms, First Republic data limit (no loan fair-value figure unless verified from a cited source), and "post-hoc" on every post-hoc number. Every number cites bank, quarter and source file.
- [ ] **Step 4:** README: keep the clean Phase 3 result as the headline; add a "Post-hoc (Phase 4)" section and link the report; update roadmap and limitations. Keep "Research tool, not financial advice."
- [ ] **Step 5:** Runbook, glossary, daily log.
- [ ] **Step 6:** Run `.venv.nosync/bin/python -m pytest -q`. Expected: all pass (data-dictionary test included).
- [ ] **Step 7:** Commit: `git commit -m "Phase 4 docs: replay report, decisions 0013-0015, dictionary, README"`
