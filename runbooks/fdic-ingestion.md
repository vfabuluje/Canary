# Runbook: FDIC ingestion

How to pull the FDIC financials and failed bank list to local Parquet. Design: [[specs/2026-11-09-phase1-fdic-ingestion-design]]. Why the layout is what it is: [[decisions/0002-parquet-partitioned-by-quarter]].

## Setup (once)
```
python3.12 -m venv .venv
.venv/bin/pip install -e ".[dev]"
```
No API key is needed; the FDIC API is public.

## Commands
```
.venv/bin/python -m canary.ingest financials            # resume + refresh latest 2 quarters
.venv/bin/python -m canary.ingest financials --force    # re-pull every quarter
.venv/bin/python -m canary.ingest failures              # always re-pull (one call)
```
Both accept `--root DIR` (default `data/raw`).

## Expected runtime
- First full financials pull: 102 API calls, about 6 min 47 s. Output is about 172 MB in `data/raw`.
- Rerun with nothing new: about 7 s (100 quarters skipped, the latest 2 re-pulled).
- Failures: a single call.

## What resume and `--force` do
- **Resume (default):** a quarter is skipped if its `part.parquet` already exists. Files are written to a temporary name and renamed, so a crash never leaves a half-written file that resume would trust.
- **Latest 2 quarters** are always re-pulled and overwritten, because banks amend recent filings ([[decisions/0004-store-raw-values-unchanged]]).
- **`--force`** re-pulls every quarter. Use it after adding a field ([[decisions/0003-curated-45-financial-fields]]).

## If it fails
Any failure stops the run and the CLI exits with code 1. Nothing is written for the failed quarter (or the failures file), and earlier files are untouched.

- **Network errors** (timeouts, refused or dropped connections, HTTP 429/5xx): each request is retried 3 times with waits of 1, 2 and 4 seconds, then raises `FDICAPIError`. **Rerun the same command;** it resumes where it stopped. If it keeps failing, check whether the FDIC API is up.
- **0 rows returned** (`IncompleteResponseError`): the API answered but sent no data. Nothing is written, so an existing good file is never replaced by an empty one. Check the API, then rerun.
- **Row count or duplicate mismatch** (`IncompleteResponseError`): we received a different number of rows than the API reported, or the same CERT twice. Duplicates mean the paging drifted while we downloaded, so the quarter is not trustworthy and is not written. Rerun.
- **`SchemaError`**: FDIC changed a column or sent a non-numeric value where a number belongs. Rerunning will not fix it; inspect the named field in the API response.

## Upload to S3
After ingesting, copy the raw files to the warehouse bucket:
```
.venv/bin/python -m canary.upload          # --root DIR to change the source (default data/raw)
```
- Needs `CANARY_BUCKET` (and `AWS_PROFILE=canary`) in `.env`.
- Files land under `raw/fdic/` (e.g. `raw/fdic/financials/repdte=20221231/part.parquet`).
- Safe to rerun: a file is skipped when S3 already has the same size and MD5 (stored as object metadata). Changed or new files are uploaded. It never deletes anything in S3.
- First full upload: 103 files (102 quarters + failures). Rerun with nothing new: 0 uploaded.

## Tests
```
.venv/bin/pytest -v                    # everything (100 tests: 93 unit + 7 data checks)
.venv/bin/pytest -m "not data"         # unit tests only, no data files needed
.venv/bin/pytest -m data               # data checks on the real saved files
```
Data checks run against `data/raw` and skip if the files are absent. Set `CANARY_DATA_ROOT` to point them at another folder.
