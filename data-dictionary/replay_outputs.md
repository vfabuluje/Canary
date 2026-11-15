# replay_outputs (Phase 4 files)

The files `python -m canary.replay` writes to `data/replay/` (on the owner's machine `data.nosync/replay/`). They are **local files, not warehouse tables**, and are git-ignored; this page exists so every number the README and [[analysis/phase4-replay]] cite has a defined column. Spec: [[specs/2026-11-11-phase4-replay-design]]. Runbook: [[runbooks/model-training]] ("Phase 4 replay").

| | |
|---|---|
| Inputs (read only) | `fct_bank_features` export, Phase 3 `model.json` |
| Built by | `src/canary/replay/` (`runrisk.py`, `analysis.py`, `probe.py`, `__main__.py`) |
| Deterministic | Yes: same inputs give the same files |
| Post-hoc | Every run-risk and corrected-baseline number ([[decisions/0013-run-risk-check]], [[decisions/0014-corrected-texas-baseline]]) |

## Read this first

- **Post-hoc vs clean.** The model columns (`model_*`, `score`, `top_*`, `best_percentile`) come from the Phase 3 model, untouched, and are as clean as the Phase 3 test. The run-risk and corrected-baseline columns were designed after seeing the 2023 failures.
- **Ranks.** Rank 1 is the riskiest bank that quarter. Ties are broken by `cert` ascending and a missing score ranks last, the same order as the 2% watchlist ([[decisions/0011-watchlist-flag-and-metrics]]), so `rank <= k` exactly when the row is flagged (`k = ceil(2% of banks)`).
- **Percentile** = `100 * (n_banks - rank + 1) / n_banks`, so rank 1 is 100.
- **Units.** Feature columns keep the units of [[fct_bank_features]]: some are percent (e.g. `tier1_risk_based_ratio` 15.0 = 15%), the ones computed in dbt are fractions (e.g. `uninsured_to_deposits` 0.86 = 86%).
- **Contribution strings** look like `afs_unrealized_loss_to_equity=+0.804, efficiency_ratio=+0.159`: XGBoost's per-feature contribution to the score in log-odds units (positive pushes toward "will fail").

## `posthoc_metrics.json`

One JSON object.

| Key | Meaning |
|---|---|
| `post_hoc` | Always `true`. |
| `note` | The sentence saying these checks were designed after seeing the 2023 failures. |
| `run_risk` | Metrics for the run-risk watchlist: `test_2016_2024` (comparable with Phase 3) and `train_era_2001_2014` (failures through 2015-12-31). Each is a metrics block (below). |
| `corrected_baseline` | Metrics for the corrected Texas-ratio watchlist on `test_2016_2024`. |
| `overlap_with_model_test` | On 2016-2024 rows: `rows_both` (flagged by run-risk and the model), `rows_a_only` (run-risk only), `rows_b_only` (model only), `banks_both` (distinct banks flagged by both on the same row). |
| `case_study_flags` | For SVB (24735), Signature (57053) and First Republic (59017): every report date (2001-2024) on which the run-risk check flagged the bank. |
| `failure_mix` | Counts from `training_mix.csv`: `training` and `2023` (profile counts), `training_by_year` (failure year x profile). |
| `false_alarm_rows` | `n_true_alarm_rows` and `n_false_alarm_rows`: the row counts behind `false_alarm_profile.csv`. |
| `model_sha256` | SHA-256 of the `model.json` that was read, so the files can be tied to the exact Phase 3 model. |

**Metrics block** (same keys and definitions as Phase 3 `metrics.json`, [[decisions/0011-watchlist-flag-and-metrics]]): `auc`, `recall`, `banks_caught`, `eligible_banks`, `caught_certs`, `recall_2q`, `banks_caught_2q`, `eligible_banks_2q`, `lead_time_median`, `lead_time_min`, `lead_time_max`, `false_alarm_rate`, `false_alarm_banks` (did not fail by the window's horizon: 2025-12-31 for the test, 2015-12-31 for the training era), `rows_flagged`, plus `n_null_scores` (rows with no score; for AUC they sit below every real score, and corrected-baseline +infinity rows sit just above the largest finite score).

## `replay_banks.csv`

One row per case-study bank per quarter from 2021-03-31 to its last report.

| Column | Meaning |
|---|---|
| `cert` | FDIC certificate number. |
| `institution_name` | Bank name. |
| `report_date` | Quarter-end report date. |
| `quarters_until_failure` | Quarters from this report to the failure quarter (1 = last report before failing). |
| `model_score` | Phase 3 model score (probability-like, 0-1). |
| `model_rank` | National rank of `model_score` among all test-window banks that quarter. |
| `model_percentile` | Percentile of `model_rank`. |
| `model_flagged` | On the model's 2% watchlist that quarter. |
| `run_risk_score` | Post-hoc. `clip(uninsured_to_deposits, 0, 1) x bond_loss_to_equity` ([[decisions/0013-run-risk-check]]). |
| `run_risk_rank` | Post-hoc. National rank of `run_risk_score` that quarter. |
| `run_risk_flagged` | Post-hoc. On the run-risk 2% watchlist that quarter. |
| `corrected_baseline_rank` | Post-hoc. National rank by the corrected Texas ratio (insolvent = worst, [[decisions/0014-corrected-texas-baseline]]). |
| `corrected_baseline_flagged` | Post-hoc. On the corrected-baseline 2% watchlist. |
| `htm_unrealized_loss_to_equity` | Held-to-maturity bonds: (amortized cost - fair value) / equity. Fraction. |
| `afs_unrealized_loss_to_equity` | Available-for-sale bonds: (amortized cost - fair value) / equity. Fraction. |
| `uninsured_to_deposits` | Estimated uninsured deposits / total deposits. Fraction. |
| `tier1_risk_based_ratio` | Tier 1 capital / risk-weighted assets. Percent. |
| `interest_expense_to_assets_ann` | Annualized interest expense / assets. Fraction. |
| `securities_to_assets` | Securities / assets. Fraction. |

## `contributions.csv`

The last two reports of each case-study bank: what pushed the model's score up and down.

| Column | Meaning |
|---|---|
| `cert` | FDIC certificate number. |
| `report_date` | Report date. |
| `top_positive` | Up to 5 features with a positive contribution (toward "will fail"), largest first. |
| `top_negative` | Up to 5 features with a negative contribution (toward "safe"), most negative first. |

## `what_if.csv`

Change one feature at a time on one bank-quarter, keep the rest as reported, and re-score with the saved model. Rows: SVB 2022-12-31, Signature 2022-12-31, First Republic 2023-03-31; HTM loss / equity 0 to 1.5, AFS loss / equity 0 to 1.0, uninsured / deposits 0 to 1.0, steps of 0.1.

| Column | Meaning |
|---|---|
| `cert` | Bank probed. |
| `report_date` | Quarter probed. |
| `feature` | The one feature that was changed. |
| `value` | The value it was set to. |
| `score` | Model score with that change. |
| `rank` | 1 + number of *other* banks that quarter with a higher real score (the bank's own row is left out). |
| `n_banks` | Banks that quarter, including the probed bank. |
| `percentile` | Percentile of `rank`. |
| `actual_value` | The bank's reported value for `feature`, for comparison. |

## `training_mix.csv`

One row per failed bank: its profile at its report closest to failure (1-4 quarters before). Rules: [[decisions/0015-failure-mix-profiles]].

| Column | Meaning |
|---|---|
| `era` | `training`: a report dated 2001-2014 was 1-4 quarters before failure. `2023`: SVB, Signature, First Republic at their last report. |
| `cert` | FDIC certificate number. |
| `institution_name` | Bank name. |
| `failure_date` | Date the FDIC closed the bank. |
| `failure_year` | Year of `failure_date`. |
| `report_date` | The report used (closest to failure). |
| `quarters_until_failure` | Quarters from that report to failure (1-4). |
| `credit_loss` | Credit-loss profile: noncurrent loans >= 5% of loans, or Texas ratio >= 100%, or Texas ratio negative (insolvent). |
| `run_risk` | Run-risk profile: on the run-risk 2% watchlist that quarter. |
| `profile` | `credit only`, `run-risk only`, `both` or `neither`. |
| `noncurrent_loans_to_loans` | Noncurrent loans / loans on that report. Fraction. |
| `texas_ratio` | Texas ratio on that report. Fraction (1.0 = 100%). |
| `bond_loss_to_equity` | HTM + AFS unrealized loss / equity (one null counts as 0; both null gives null). Fraction. |
| `uninsured_to_deposits` | Uninsured / deposits. Fraction. |
| `run_risk_score` | Post-hoc run-risk score on that report. |

## `distributions.csv`

How large bond losses and uninsured deposits were in the training years vs the 2023 banks.

| Column | Meaning |
|---|---|
| `variable` | `bond_loss_to_equity` or `uninsured_to_deposits`. |
| `group` | `train_positive_rows` (2001-2014 reports 1-4 quarters before a failure), `train_all_rows` (all 2001-2014 reports), or a 2023 bank's name (its last report, n = 1). |
| `n` | Non-null values in the group. |
| `median` | Median. |
| `p90` | 90th percentile. |
| `p99` | 99th percentile. |
| `share_above_0_3` | Share of the group above 0.3. |

## `test_misses.csv`

Failed banks with a 2016-2024 report 1-4 quarters before failure that the model never flagged on such a report.

| Column | Meaning |
|---|---|
| `cert` | FDIC certificate number. |
| `institution_name` | Bank name. |
| `failure_date` | Date the FDIC closed the bank. |
| `report_date` | The bank's highest-scoring eligible report (on a tie, the latest). |
| `quarters_until_failure` | Quarters from that report to failure. |
| `best_percentile` | Model percentile on that report. |
| `top_signals` | Up to 3 features pushing that score up. |
| `credit_loss` | Credit-loss profile on that report (same rule as `training_mix.csv`). |

## `false_alarm_profile.csv`

2016-2024 rows on the model's watchlist: true alarms (failed within 4 quarters) vs false alarms (did not). Row counts are in `posthoc_metrics.json` under `false_alarm_rows`.

| Column | Meaning |
|---|---|
| `feature` | One of the 31 model features. |
| `median_true_alarm` | Median on flagged rows that failed within 4 quarters. |
| `median_false_alarm` | Median on flagged rows that did not. |
| `difference` | `median_false_alarm - median_true_alarm`. |

## `top_false_alarm_banks.csv`

The 10 banks the model flagged most often in 2016-2024 that had not failed by 2025-12-31.

| Column | Meaning |
|---|---|
| `cert` | FDIC certificate number. |
| `institution_name` | Bank name (latest flagged report). |
| `quarters_flagged` | Number of quarters on the model's watchlist. |
