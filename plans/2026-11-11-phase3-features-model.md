# Phase 3 Features + Model Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a tested dbt features table from `fct_bank_quarters`, export it locally, train XGBoost on 2001–2014 report dates, score 2016–2024 once, and report AUC / recall / lead time / false alarms / baseline / SVB-Signature-First Republic case studies honestly.

**Architecture:** A dbt model `canary_marts.fct_bank_features` computes ~31 CAMELS-style ratios in SQL with data tests. `python -m canary.export_features` runs an Athena `UNLOAD` (features joined to label columns) into `athena-results/exports/<run_id>/` and saves one local Parquet file. A `canary.model` package holds the label/split rules, the watchlist + metrics functions, and a `train` / `evaluate` CLI that writes model, scores, metrics and case studies to `data/model/`. Stage 1 (Tasks 1–5) uses no AWS; stage 2 (Task 6) is the live run, gated on Victor's yes.

**Tech Stack:** Python 3.12, pandas, pyarrow, boto3, xgboost, scikit-learn, moto (tests); dbt-core 1.10 + dbt-athena + dbt_utils; Athena engine v3.

**Spec:** `specs/2026-11-11-phase3-features-model-design.md` (approved 2026-11-11). Read it alongside this plan; it is the authority.

## Global Constraints

- Branch `phase3-model`. Never commit `data/`, `.env`, `~/.aws/` contents, or personal details. The repo is public.
- Never read `~/.aws/credentials`. No AWS deletes. `dbt build` / `dbt run` that builds a table needs Victor's explicit yes each time. `dbt parse` / `dbt compile` / `dbt test` are fine.
- Unit tests touch no network and no AWS (moto / fakes only). AWS CLI lives at `/usr/local/bin/aws`; profile `canary`, region `us-east-1`, workgroup `canary` (1 GB scan cap).
- Generic dbt tests use the dbt 1.10 `arguments:` / `config:` syntax (see `warehouse/models/marts/_marts.yml`). Run dbt from `warehouse/` with `--profiles-dir . --no-partial-parse` after `set -a; source ../.env; set +a`.
- Split by report date, exactly: train `2001-03-31`–`2014-12-31`; gap `2015-03-31`–`2015-12-31` (unused); test `2016-03-31`–`2024-12-31`; not scored `≥ 2025-03-31`. Inner validation: fit `≤ 2011-12-31`, validate `2012-03-31`–`2014-12-31`.
- Label `fails_within_4q = 1` iff `quarters_until_failure ∈ {1,2,3,4}`; else 0.
- Watchlist: per `report_date`, flag the top `ceil(0.02 × n_banks)` by score; ties broken by `cert` ascending. All banks reporting that quarter, no filter.
- Model inputs are exactly `FEATURE_COLUMNS` (Task 2). Never `failure_date`, `quarters_until_failure`, `institution_name`, `cert`, `report_date`, or `select *`.
- Nothing is tuned on test years. `evaluate` runs once; rerunning needs `--force` and is logged.
- Case-study certs: SVB `24735`, Signature `57053`, First Republic `59017`; window `report_date ≥ 2021-03-31`.
- New optional dependency group `model = ["xgboost>=2.1,<4", "scikit-learn>=1.5"]`. On macOS, if `import xgboost` fails with a libomp error, run `brew install libomp` (`/opt/homebrew/bin/brew`).
- Every new table/column documented in `data-dictionary/`; new decisions `0009`–`0012` in `decisions/` (plain English, Victor must be able to explain each); `daily-log.md` at session end.

## Review Focus

1. **A quarter with very few banks** (e.g. a synthetic quarter of 10) → at least 1 bank flagged (ceil), never 0. Test: Task 3 `test_flag_small_quarter_flags_at_least_one`.
2. **Tied scores at the watchlist cutoff** → exactly `k` flagged, chosen deterministically by lowest `cert`. Test: Task 3 `test_flag_ties_are_deterministic`.
3. **A label or ID column sneaking into the features** (export carries `quarters_until_failure`, `failure_date`, `institution_name`) → `select_features` uses the fixed list and raises if any listed column is missing. Tests: Task 2 `test_feature_columns_exclude_label_and_ids`, `test_select_features_missing_column_raises`.
4. **Running `evaluate` a second time** → refuses (exit 1, message) unless `--force`, so the test set is scored once. Test: Task 5 `test_evaluate_refuses_to_overwrite`.
5. **Athena `UNLOAD` fails or returns no files** → exit 1 with the reason, and no partial local Parquet left behind. Tests: Task 4 `test_export_failed_query_leaves_no_file`, `test_export_no_files_fails`.

---

### Task 1: dbt features model `fct_bank_features` + dictionary + decision 0009

**Files:**
- Create: `warehouse/models/marts/fct_bank_features.sql`
- Modify: `warehouse/models/marts/_marts.yml` (add model + tests)
- Create: `warehouse/tests/assert_features_row_count_matches_quarters.sql`, `warehouse/tests/assert_svb_2022q4_htm_loss_to_equity.sql`, `warehouse/tests/assert_growth_null_without_prior_year.sql`
- Create: `data-dictionary/fct_bank_features.md`, `decisions/0009-features-and-zero-handling.md`

**Interfaces:**
- Consumes: `ref('fct_bank_quarters')` columns (see `data-dictionary/fct_bank_quarters.md`).
- Produces: table `canary_marts.fct_bank_features` with keys `cert`, `report_date` and exactly these 31 feature columns (Task 2's `FEATURE_COLUMNS` must match this list and order):
  `equity_to_assets, leverage_ratio, tier1_risk_based_ratio, total_risk_based_ratio, noncurrent_loans_to_loans, nonaccrual_ore_to_assets, past_due_30_89_to_assets, allowance_to_loans, net_charge_offs_to_loans_ann, provision_to_assets_ann, construction_loans_to_loans, cre_loans_to_loans, texas_ratio, return_on_assets, return_on_equity, net_interest_margin, efficiency_ratio, interest_expense_to_assets_ann, loans_to_deposits, uninsured_to_deposits, brokered_to_deposits, core_deposits_to_assets, fhlb_to_assets, volatile_liabilities_to_assets, cash_to_assets, htm_unrealized_loss_to_equity, afs_unrealized_loss_to_equity, securities_to_assets, log_total_assets, asset_growth_4q, deposit_growth_4q`

Formula rules (pinned by the spec; the builder writes the SQL):
- FDIC-supplied ratios pass through unchanged, in percent: `equity_to_assets` ← `equity_to_assets_ratio`; `leverage_ratio`; `tier1_risk_based_ratio`; `total_risk_based_ratio`; `return_on_assets`; `return_on_equity`; `net_interest_margin`; `efficiency_ratio`; `loans_to_deposits` ← `net_loans_to_deposits_ratio`.
- Computed ratios are fractions (not percent); every denominator wrapped in `nullif(x, 0)`.
- `texas_ratio` = (`noncurrent_loans` + `other_real_estate_owned`) ÷ (`equity_capital` + `loan_loss_allowance`).
- `_ann` fields: year-to-date dollars × 4 ÷ `quarter(report_date)`, then ÷ the denominator.
- `htm_unrealized_loss_to_equity` = (`htm_securities_amortized_cost` − `htm_securities_fair_value`) ÷ `equity_capital`; 0 when cost = 0; **null when cost > 0 and fair value = 0**. AFS likewise.
- `log_total_assets` = `ln(total_assets)` (null if ≤ 0).
- Growth: (value ÷ value at the same `cert`'s row with `report_date = date_add('month', -12, report_date)`) − 1, via self-join on `cert` and that date (not a row offset); null when no such row.
- 0 → null for: `tier1_risk_based_ratio`, `total_risk_based_ratio` (2020 community bank leverage ratio option), `uninsured_deposits`. For every other input field, profile 0-shares by year from local `data/raw/financials` (read-only pandas) and apply 0 → null only where the data shows "not reported" behavior; record each rule and its evidence in decision 0009.

- [ ] **Step 1: Write the tests first.** In `_marts.yml`, add `fct_bank_features` with: `dbt_utils.unique_combination_of_columns` on (`cert`, `report_date`); `not_null` on `cert`, `report_date`; `dbt_utils.accepted_range` (`min_value: 0`, `max_value: 1`, `config: {severity: warn}`) on `uninsured_to_deposits`, `brokered_to_deposits`, `construction_loans_to_loans`, `cre_loans_to_loans`; every column with a description (meaning + units). Singular tests (each returns failing rows):
  - `assert_features_row_count_matches_quarters`: `count(*)` of `fct_bank_features` ≠ `count(*)` of `fct_bank_quarters` → one row.
  - `assert_svb_2022q4_htm_loss_to_equity`: row for `cert = 24735` and `report_date = date '2022-12-31'` missing, or `htm_unrealized_loss_to_equity` not between `0.90` and `1.05` → row.
  - `assert_growth_null_without_prior_year`: any row with `asset_growth_4q` or `deposit_growth_4q` non-null where no row exists for the same `cert` at `report_date − 12 months`.
- [ ] **Step 2: Write `data-dictionary/fct_bank_features.md`** in the existing dictionary format (grain, key, source, "read this first": units, null rules, not a label table), one `| \`<column>\` |` row per column.
- [ ] **Step 3: Run** `.venv/bin/pytest -q tests/test_data_dictionary.py` → PASS; `dbt parse` → succeeds with errors only for the missing model SQL.
- [ ] **Step 4: Profile 0-shares** and write `decisions/0009-features-and-zero-handling.md` (feature list by CAMELS group with one plain-English line each; units rule; every 0→null rule with its evidence; why `texas_ratio` is included).
- [ ] **Step 5: Write `fct_bank_features.sql`.** Run `dbt compile --select fct_bank_features` → compiles. Do NOT `dbt build`.
- [ ] **Step 6: Run** `.venv/bin/pytest -q` → all pass. Commit `"Add fct_bank_features dbt model, tests, dictionary, decision 0009"`.

### Task 2: Dataset rules — label, split, feature list (+ decision 0010)

**Files:**
- Create: `src/canary/model/__init__.py`, `src/canary/model/dataset.py`, `tests/test_model_dataset.py`, `decisions/0010-label-and-time-split.md`
- Modify: `pyproject.toml` (add `model` optional group; install with `.venv/bin/pip install -e '.[dev,model]'`)

**Interfaces:**
- Produces (`canary.model.dataset`):
  - `FEATURE_COLUMNS: tuple[str, ...]`: the 31 names from Task 1, same order.
  - `TRAIN_END = date(2014,12,31)`, `TEST_START = date(2016,3,31)`, `TEST_END = date(2024,12,31)`, `INNER_FIT_END = date(2011,12,31)`, `TRAINING_FAILURE_CUTOFF = date(2015,12,31)`.
  - `fails_within_4q(quarters_until_failure: pd.Series) -> pd.Series` (int 0/1).
  - `assign_split(report_date: pd.Series) -> pd.Series` with values `"train" | "gap" | "test" | "not_scored"`.
  - `select_features(df: pd.DataFrame) -> pd.DataFrame` returns `df[list(FEATURE_COLUMNS)]`; raises `KeyError` naming missing columns.
  - `load_dataset(path: Path) -> pd.DataFrame` reads the export, adds `label` and `split` columns.

- [ ] **Step 1: Write failing tests:**
  - `test_label_values`: `[1,2,3,4] → 1`; `[None, 5, 8] → 0`.
  - `test_split_boundaries`: `2014-12-31 → train`, `2015-03-31` and `2015-12-31 → gap`, `2016-03-31` and `2024-12-31 → test`, `2025-03-31 → not_scored`, `2001-03-31 → train`.
  - `test_training_labels_only_use_failures_through_2015`: on a synthetic frame, every train row with `label == 1` has `failure_date ≤ TRAINING_FAILURE_CUTOFF`.
  - `test_feature_columns_exclude_label_and_ids`: none of `cert, report_date, failure_date, quarters_until_failure, institution_name, label, split` in `FEATURE_COLUMNS`; `len(FEATURE_COLUMNS) == 31`.
  - `test_feature_columns_match_dbt_yml`: names equal the `fct_bank_features` columns in `_marts.yml` minus `cert`, `report_date`, in order.
  - `test_select_features_missing_column_raises`.
- [ ] **Step 2: Run** `pytest tests/test_model_dataset.py -v` → FAIL (module missing).
- [ ] **Step 3: Implement `dataset.py`.**
- [ ] **Step 4: Run** → PASS. Write decision 0010 (label, the four splits, why 2015 is a gap, the CLAUDE.md wording, inner validation). Commit `"Add label, time split and feature list rules"`.

### Task 3: Watchlist flags and metrics (+ decision 0011)

**Files:**
- Create: `src/canary/model/metrics.py`, `tests/test_model_metrics.py`, `decisions/0011-watchlist-flag-and-metrics.md`

**Interfaces:**
- Consumes: frames with columns `cert`, `report_date`, `quarters_until_failure`, `failure_date`, `label`, a score column.
- Produces (`canary.model.metrics`):
  - `WATCHLIST_SHARE = 0.02`
  - `flag_watchlist(df: pd.DataFrame, score_col: str, share: float = WATCHLIST_SHARE) -> pd.Series` (bool, aligned to `df.index`).
  - `@dataclass RecallResult(caught: int, eligible: int, recall: float, caught_certs: list[int])`
  - `bank_recall(df: pd.DataFrame, flag_col: str, min_quarters: int = 1) -> RecallResult`: eligible rows have `quarters_until_failure` in `[min_quarters, 4]`; a bank is eligible if it has ≥ 1 eligible row in `df`; caught if any eligible row is flagged. The caller passes test rows only.
  - `lead_times(df: pd.DataFrame, flag_col: str) -> pd.Series` (index `cert`; max `quarters_until_failure` among flagged rows with values 1–4).
  - `false_alarm_rate(df, flag_col) -> float` = flagged & `label == 0` ÷ flagged.
  - `false_alarm_banks(df, flag_col, horizon_end: date = date(2025,12,31)) -> int`: distinct flagged certs whose `failure_date` is null or > `horizon_end`.
  - `auc(df, score_col) -> float` (scikit-learn `roc_auc_score` on `label`).

- [ ] **Step 1: Write failing tests** on a hand-made frame (2 quarters, ~60 banks, 3 failures) with known answers:
  - `test_flag_rate_per_quarter`: 100 banks → exactly 2 flagged; 101 banks → 3.
  - `test_flag_small_quarter_flags_at_least_one`: 10 banks → 1.
  - `test_flag_ties_are_deterministic`: 5 equal top scores, k = 2 → the 2 lowest certs flagged.
  - `test_recall_counts_bank_once`; `test_recall_min_quarters_2`; `test_bank_with_no_eligible_rows_not_in_denominator` (its only 1–4 rows are absent from the frame, as for a gap-year bank).
  - `test_lead_time_is_max_flagged_quarters`; `test_false_alarm_rate`; `test_false_alarm_banks_excludes_later_failures`.
- [ ] **Step 2: Run** → FAIL. **Step 3: Implement.** **Step 4: Run** → PASS.
- [ ] **Step 5:** Write decision 0011 (why a 2% watchlist, the ceil and tie rule, each metric in one plain sentence, the reporting-lag caveat on lead time). Commit `"Add watchlist flag and evaluation metrics"`.

### Task 4: Export features from Athena (+ decision 0012)

**Files:**
- Create: `src/canary/export_features.py`, `tests/test_export_features.py`, `decisions/0012-feature-export-via-unload.md`

**Interfaces:**
- Consumes: `load_settings(env)`, `Settings` (`canary.config`); `run(statements, athena_client, workgroup)`, `AthenaError` (`canary.athena_ddl`); `log_profile(profile)` (`canary.upload`).
- Produces:
  - `export_sql(bucket: str, run_id: str) -> str`: `UNLOAD (SELECT f.*, q.quarters_until_failure, q.failure_date, q.institution_name FROM canary_marts.fct_bank_features f JOIN canary_marts.fct_bank_quarters q ON f.cert = q.cert AND f.report_date = q.report_date) TO 's3://<bucket>/athena-results/exports/<run_id>/' WITH (format = 'PARQUET', compression = 'SNAPPY')`.
  - `export(settings: Settings, athena_client, s3_client, out_path: Path, run_id: str) -> int` (rows written): runs the UNLOAD, lists and downloads every object under the prefix, concatenates them, writes `out_path` atomically (temp file then rename). It raises `AthenaError`, or `RuntimeError("no files under ...")` if the prefix is empty. On any error it leaves no `out_path`.
  - `main(argv=None, athena_client=None, s3_client=None, env=None) -> int` CLI `python -m canary.export_features [--out data/features/fct_bank_features.parquet]`; returns 1 on `ConfigError`, `AthenaError`, `ClientError`, `RuntimeError`; logs the profile via `log_profile`. `run_id` = UTC timestamp `YYYYMMDDTHHMMSSZ`.

- [ ] **Step 1: Write failing tests** (moto S3; a fake Athena client whose `start_query_execution` drops 2 small Parquet parts under the prefix and reports SUCCEEDED):
  - `test_export_sql_targets_athena_results_prefix` (contains `athena-results/exports/<run_id>/`, `PARQUET`, the join on both keys).
  - `test_export_writes_concatenated_parquet` (row count = sum of parts; columns include features + the 3 label/name columns).
  - `test_export_failed_query_leaves_no_file` (fake returns FAILED → `main` returns 1, `out_path` absent).
  - `test_export_no_files_fails` (SUCCEEDED but empty prefix → 1, no file).
  - `test_missing_bucket_env_fails` (`env={}` → 1, no client calls).
- [ ] **Step 2: Run** → FAIL. **Step 3: Implement.** **Step 4: Run** → PASS.
- [ ] **Step 5:** Write decision 0012 (UNLOAD vs downloading CSV results; why under `athena-results/`: auto-expiry and no new IAM delete rights; the scan stays under 1 GB). Commit `"Add Athena feature export"`.

### Task 5: Train, evaluate, baseline, case studies (CLI)

**Files:**
- Create: `src/canary/model/train.py`, `src/canary/model/__main__.py`, `tests/test_model_train.py`

**Interfaces:**
- Consumes: Task 2 (`load_dataset`, `select_features`, `FEATURE_COLUMNS`, split constants); Task 3 (all metrics, `flag_watchlist`).
- Produces (`canary.model.train`):
  - `SEED = 42`; `CASE_STUDY_CERTS = {24735: "Silicon Valley Bank", 57053: "Signature Bank", 59017: "First Republic Bank"}`; `CASE_STUDY_START = date(2021,3,31)`.
  - `train(df: pd.DataFrame) -> tuple[xgboost.XGBClassifier, dict]`: uses `split == "train"` rows only. It tries a grid of ≤ 8 combos (`max_depth`, `learning_rate`, `min_child_weight`), fitting on `report_date ≤ INNER_FIT_END` and early-stopping on `INNER_FIT_END < report_date ≤ TRAIN_END` by PR-AUC, with `scale_pos_weight` = negatives ÷ positives of the fit set. It then refits on all train rows with the best params and best number of trees. It returns the model and a config dict (params, n_trees, validation PR-AUC per combo, row and positive counts).
  - `evaluate(df, model) -> dict`: scores `split == "test"` rows and flags with `flag_watchlist`. It computes `auc`, `bank_recall` (min 1 and min 2), `lead_times` (median, min, max), `false_alarm_rate`, `false_alarm_banks`, and the same for the baseline (score = `texas_ratio`, nulls ranked lowest). It returns a metrics dict that includes the eligible-bank count.
  - `case_studies(df, model) -> pd.DataFrame`: for `CASE_STUDY_CERTS` rows with `report_date ≥ CASE_STUDY_START` (scored with the national rank and percentile of their own quarter), returns `cert, institution_name, report_date, quarters_until_failure, score, rank, n_banks, percentile, flagged, top_signals`, where `top_signals` is the 5 features with the largest positive contribution (`model.get_booster().predict(DMatrix, pred_contribs=True)`), formatted `name=+0.123`.
  - CLI: `python -m canary.model train --features PATH --out data/model` writes `model.json` and `run_config.json`. `python -m canary.model evaluate --features PATH --out data/model [--force]` writes `scores_test.parquet`, `metrics.json` and `case_studies.csv`. Evaluate returns 1 if `metrics.json` exists and `--force` is not given; with `--force` it logs a warning and appends `"rerun": true` to the metrics.

- [ ] **Step 1: Write failing tests** on a synthetic dataset from a fixture (~40 banks × quarters 2001–2026, a few failures in train and test years, one feature that strongly predicts failure):
  - `test_train_uses_only_train_rows` (config row counts match `split == "train"`; no test-year date in the fit set).
  - `test_train_is_deterministic` (two runs → identical predictions).
  - `test_evaluate_metrics_keys` (`auc`, `recall`, `recall_2q`, `eligible_banks`, `lead_time_median`, `false_alarm_rate`, `false_alarm_banks`, `baseline` present; the strong feature gives `auc > 0.8`).
  - `test_case_studies_columns_and_top_signals` (5 signals per row, names from `FEATURE_COLUMNS`).
  - `test_evaluate_refuses_to_overwrite` (second call → 1; with `--force` → 0 and `rerun` true).
  - `test_cli_end_to_end_smoke` (train then evaluate on the fixture via `main`; all 5 output files exist).
- [ ] **Step 2: Run** → FAIL. **Step 3: Implement.** **Step 4: Run** `pytest -q` → all pass, output pristine.
- [ ] **Step 5: Commit** `"Add XGBoost training, evaluation, baseline and case studies"`.

### Task 6: Live run (gated)

**Files:** none committed except `warehouse/` fixes if a dbt test exposes a real bug (fix in Task 1's files, re-reviewed).

- [ ] **Step 1: Ask Victor** before building. Then `dbt build --select fct_bank_features`. Expected: model built, all tests PASS (range tests may WARN; record counts and investigate any WARN rows before proceeding).
- [ ] **Step 2: Verify in Athena:** `count(*)` of `canary_marts.fct_bank_features` = 710,691; the SVB 2022-12-31 `htm_unrealized_loss_to_equity` ≈ 0.98.
- [ ] **Step 3:** `python -m canary.export_features` → 710,691 rows written to `data/features/fct_bank_features.parquet`.
- [ ] **Step 4:** `python -m canary.model train ...`; then `evaluate` **once**. Save the console output. Do not change features, parameters or the 2% after seeing the test metrics. If something must change, stop and ask Victor; the README must then say what changed.
- [ ] **Step 5:** Record in the ledger: metrics JSON, case-study table, baseline comparison, run_config.

### Task 7: Documentation and results

**Files:**
- Create: `runbooks/model-training.md`
- Modify: `README.md` (results section, roadmap, uninsured-deposits limitation recheck), `TOOLS.md` (XGBoost section: planned → what it does), `daily-log.md`

- [ ] **Step 1:** `runbooks/model-training.md`: build features (with Victor's yes), export, train, evaluate once; what to do if each fails; the "don't tune on test" rule.
- [ ] **Step 2:** README results section, from `metrics.json` exactly:
  - AUC, recall with its eligible-bank count, recall at 2+ quarters, lead time (with the reporting-lag caveat), false-alarm rate and banks.
  - Baseline vs. XGBoost side by side.
  - The case-study table, per quarter for each bank: score percentile, flagged, top signals.
  - One honest paragraph: what was caught, what wasn't, and why. For example, training years dominated by credit-loss failures.
- [ ] **Step 3:** Recheck the limitation "Uninsured-deposit estimates are mainly available for banks with $1B+ in assets" against the 0-share profiling from decision 0009, and correct or remove it.
- [ ] **Step 4:** TOOLS.md XGBoost section reflects what was built. Roadmap marks Phase 3 done. `daily-log.md` entry.
- [ ] **Step 5:** `.venv/bin/pytest -q` → all pass; `dbt test --no-partial-parse` → pass / known warns. Commit `"Phase 3 docs: results, runbook, tools"`.
