# 0002 — Save financials as one Parquet file per quarter

**Date:** 2026-11-09
**Status:** Accepted

## Decision
Each quarter of FDIC financials is saved as its own Parquet file: `data/raw/financials/repdte=YYYYMMDD/part.parquet` (about 100 files). The failed bank list is a single file, `data/raw/failures/failures.parquet`.

## Why
- **Resumable.** If the pull crashes at quarter 80, a rerun skips the quarters already saved and carries on. See [[runbooks/fdic-ingestion]].
- **Incremental.** When the FDIC publishes a new quarter, that is one new API call, not a re-download of 700k rows.
- **Ready for Phase 2.** The `repdte=YYYYMMDD` folder naming is the Hive-style partition layout that S3/Athena and pandas both understand, so the folder can be uploaded to S3 unchanged.
- Parquet keeps column types (dates, numbers) and is small: the full pull is 172 MB.

## Alternatives
1. **One big Parquet file rebuilt every run.** Least code, but any failure restarts everything and every refresh re-downloads all ~700k rows. Rejected.
2. **Save raw JSON first, convert to Parquet in a second step.** A textbook raw-then-clean pattern, but twice the code and storage, and the FDIC API can simply be called again. Rejected.

## Phase 2 notes
- **Case clash.** Athena and Glue are case-insensitive, so the partition key `repdte` (from the folder name) and the data column `REPDTE` collide. When defining the Athena table, declare `repdte` as the partition and leave `REPDTE` out of the column list (or rename one of them).
- **Date type.** Dates are stored as Parquet `timestamp[ns]` at midnight. Decide in Phase 2 whether to convert them to a date type for Athena.

Related: [[decisions/0003-curated-45-financial-fields]], [[decisions/0004-store-raw-values-unchanged]]. Full design: [[specs/2026-11-09-phase1-fdic-ingestion-design]].
