# Runbook: warehouse refresh

How to bring the warehouse up to date: pull new FDIC data, copy it to S3, refresh the Athena raw tables, rebuild the dbt models and run the tests. Design: [[specs/2026-11-09-phase2-warehouse-design]]. One-time AWS setup is in [[runbooks/aws-setup]]; the Phase 1 pull is in [[runbooks/fdic-ingestion]].

## Before you start
- Work from the repo root with the virtual environment (`.venv`) and a filled-in `.env` (`CANARY_BUCKET`, `AWS_PROFILE=canary`).
- AWS commands use the limited `canary` profile only.
- **Confirm-before-delete rule:** never delete anything in AWS (S3 files, tables, databases, keys) without the project owner's explicit yes first. Nothing in this runbook deletes.
- **`dbt build` and `dbt run` replace the mart tables.** They rewrite the files under `dbt/` in S3, and that counts as a delete-and-replace, so they also need the project owner's yes first. `dbt test` only reads and needs no approval.

## Steps (run in order)

### 1. Pull from the FDIC
```
.venv/bin/python -m canary.ingest financials
.venv/bin/python -m canary.ingest failures
```
- Does: downloads quarters not yet on disk, re-pulls the latest 2 quarters (banks amend recent filings), and re-pulls the failures list. Files land in `data/raw/`.
- If it fails: rerun the same command; it resumes. See [[runbooks/fdic-ingestion]] for each error type.

### 2. Upload to S3
```
.venv/bin/python -m canary.upload
```
- Does: copies new or changed files to `s3://<bucket>/raw/fdic/`. Skips files whose size and MD5 already match. Never deletes.
- If it fails: a missing-bucket error means `CANARY_BUCKET` is not set in `.env`. An access error means the `canary` profile or its key is wrong (see [[runbooks/aws-setup]]). Rerun after fixing; it is safe to repeat.

### 3. Refresh the Athena raw tables
```
.venv/bin/python -m canary.athena_ddl
```
- Does: creates the raw tables if missing, and rewrites the list of quarters the financials table knows about. **Rerun it after any new quarter is uploaded**, otherwise Athena does not see the new quarter. The list is spelled out quarter by quarter because Athena's date-based rule found only 1 of 102 quarters ([[decisions/0006-athena-handwritten-ddl-and-dbt]]).
- If it fails: an Athena error message is printed. Common causes are the wrong bucket name or a missing database (setup not run). It is safe to repeat.

### 4. Rebuild the models (needs the project owner's yes first)
```
cd warehouse
set -a; source ../.env; set +a
../.venv/bin/dbt build --no-partial-parse --profiles-dir .
```
- Does: builds the staging views and the two mart tables, then runs every data test.
- **Always use `--no-partial-parse`.** dbt keeps a cache of what it parsed last time. A stale cache once produced a build that ran zero tests and still reported success. The flag forces a fresh read of every file.
- **Expected result:** all tests pass except one warning. The `relationships` test on `dim_failed_banks.cert` warns about cert 34264 (First Alliance Bank and Trust Co), which failed on 2001-02-02, before the first quarter of financials. That warning is expected. Anything else (an ERROR, or a new warning) needs investigating.
- If a test fails: read the test name in the output. Row-count and missing-quarter tests usually mean steps 1 to 3 did not finish. A `unique` failure on `dim_failed_banks.cert` means a bank appears twice in the failures list; look at the rows, do not hide it.
- To only re-check without rebuilding (no approval needed): `../.venv/bin/dbt test --no-partial-parse --profiles-dir .`

### 5. Check the run
- Confirm the test summary shows no ERROR. Update the numbers in the README and the data dictionary if row counts changed.
