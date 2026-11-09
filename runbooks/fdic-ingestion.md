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
An `IncompleteResponseError` (rows received did not match what the API reported) or an `FDICAPIError` (network problem or bad response after 3 retries) stops the run and the CLI exits with code 1. Nothing is written for the failed quarter. **Just rerun the same command;** it resumes where it stopped. If it keeps failing on the same quarter, check whether the FDIC API is up before changing code.

## Tests
```
.venv/bin/pytest -v                    # everything (52 tests: 45 unit + 7 data checks)
.venv/bin/pytest -m "not data"         # unit tests only, no data files needed
.venv/bin/pytest -m data               # data checks on the real saved files
```
Data checks run against `data/raw` and skip if the files are absent. Set `CANARY_DATA_ROOT` to point them at another folder.
