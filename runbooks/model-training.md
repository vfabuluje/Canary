# Runbook: build features, train and evaluate the model

How to go from the warehouse to a trained model and the one honest test result. Design: [[specs/2026-11-11-phase3-features-model-design]]. Warehouse steps are in [[runbooks/warehouse-refresh]]; AWS setup is in [[runbooks/aws-setup]].

## Before you start
- Work from the repo root with `.venv` and a filled-in `.env` (`CANARY_BUCKET`, `AWS_PROFILE=canary`).
- AWS commands use the limited `canary` profile only.
- **Confirm-before-delete rule:** never delete anything in AWS without the project owner's explicit yes.
- **`dbt build` replaces the feature table** (it rewrites files under `dbt/` in S3), so step 1 needs the owner's yes first.

## The "don't tune on test" rule
The test period (report dates 2016-03-31 to 2024-12-31) is looked at **once**. All choices (settings, early stopping) are made on a validation block inside the training years (2012-2014). If a result looks disappointing, do not change the model and rerun until the test number improves: that turns the test set into a second training set, and the reported number stops meaning anything. `evaluate` refuses to overwrite an existing `metrics.json`. `--force` exists only for a genuine rerun (for example after fixing a bug), and it marks the file as rerun. Anything learned from the test results goes to Phase 4 as a written finding, not into a tuned model.

## Steps (run in order)

### 1. Build the feature table (needs the project owner's yes first)
```
cd warehouse
set -a; source ../.env; set +a
../.venv/bin/dbt build --no-partial-parse --profiles-dir . --select fct_bank_features
```
- Does: builds `fct_bank_features` (710,691 rows, 31 features) and runs its tests.
- **Expected result:** the unique and not-null tests and the three singular tests pass. Four range tests warn (`uninsured_to_deposits` 144 rows, `brokered_to_deposits` 28, `cre_loans_to_loans` 5, `construction_loans_to_loans` 6, about 183 of 710,691 rows). These are known and kept as-is; see [[data-dictionary/fct_bank_features]].
- If a test ERRORs: read the test name. A row-count mismatch against `fct_bank_quarters` means the upstream tables are stale; do the [[runbooks/warehouse-refresh]] first. Do not loosen a test to make it pass.

### 2. Export the features to a local file
```
.venv/bin/python -m canary.export_features
```
- Does: runs an Athena `UNLOAD` and downloads the Parquet parts into one file, `data/features/fct_bank_features.parquet` (about 168 MB; git-ignored). See [[decisions/0012-feature-export-via-unload]].
- If it fails: an access error means the `canary` profile is wrong; a missing-bucket error means `CANARY_BUCKET` is not set. Safe to repeat. If the row count is not 710,691, the table was not rebuilt; go back to step 1.

### 3. Train
```
.venv/bin/python -m canary.model train --features data/features/fct_bank_features.parquet
```
- Does: tries 8 small settings combinations on the 2012-2014 validation block, then refits on all training rows (report dates through 2014) and writes `data/model/model.json` and `run_config.json`.
- If it fails: a "missing column" error means the export is out of date with the model (rerun step 1 and 2). It never touches the test period, so it is safe to repeat before evaluate. After evaluate has run, retraining overwrites `model.json` and needs the owner's yes; `metrics.json` records `model_sha256`, so a mismatch between the model file and the metrics is detectable. Phase 4 experiments go to a new `--out` directory.

### 4. Evaluate (once)
```
.venv/bin/python -m canary.model evaluate --features data/features/fct_bank_features.parquet
```
- Does: scores the test period, compares with the Texas-ratio baseline, and writes `metrics.json` and `case_studies.csv` (SVB, Signature, First Republic per quarter) under `data/model/`.
- If it says `metrics.json` already exists: that is the guard working. Read the existing file. Use `--force` only with the owner's yes and a written reason.
- Then copy the numbers into the README from `metrics.json` exactly, with their denominators.
