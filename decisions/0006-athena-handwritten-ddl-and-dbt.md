# 0006 — Hand-written Athena table definitions, explicit partition list

**Date:** 2026-11-10
**Status:** Accepted

## Decision
The two raw Athena tables (`canary_raw.fdic_financials`, `canary_raw.fdic_failures`) are defined by SQL files we write ourselves (`warehouse/ddl/`) and run with `python -m canary.athena_ddl`. dbt then builds on top of them. The financials table lists its quarters explicitly (partition projection of type `enum`), and `REPDTE` is left out of the column list.

## Why
- **Readable and explainable.** Every column and type is visible in a file in the repo, and a unit test checks that the file matches `FINANCIAL_FIELDS` / `FAILURE_FIELDS`.
- **Safe to repeat.** Every statement is `CREATE ... IF NOT EXISTS` or `ALTER ... SET TBLPROPERTIES`. Nothing is dropped.
- **Partition projection** means Athena works out the partition folders (`repdte=YYYYMMDD`) from a rule instead of us registering 102 partitions one by one or running a crawler.
- **`REPDTE` vs `repdte` clash.** Athena column names are case-insensitive, and the folder name already gives a partition column `repdte`. The Parquet files also contain `REPDTE`, so declaring both would be a duplicate. We declare only the partition column; Athena ignores the extra file column. The partition value is the same text (`20221231`), and dbt converts it to a date later.

## Spike: which projection type?
I created a throwaway table `canary_raw.tmp_projection_check` (one column, `cert bigint`) with a `date` projection (`range=20010331,NOW`, `interval=3 MONTHS`, format `yyyyMMdd`) and ran `SELECT count(DISTINCT repdte) FROM canary_raw.tmp_projection_check`.
- Expected: 102 (the number of local quarter folders). Got: **1**. A scanning query showed only `20010331` was found.
- Cause not determined: possibly how the date stepping or the date format interacted. The explicit list in the `enum` approach avoids the question entirely.
- So I used the **`enum` branch**: `athena_ddl.py` writes the exact list of quarter ends (2001-03-31 up to the newest local quarter) into `projection.repdte.values`. Re-running after a new quarter is uploaded extends the list.
- The temp table was dropped on 2026-11-10 with the owner's approval.

## Alternatives
1. **Glue crawler.** Rejected: it guesses types, can trip on the `repdte`/`REPDTE` clash, costs money per run, and is hard to explain.
2. **DuckDB locally.** Rejected: different SQL dialect from Athena, so everything would be debugged twice.
3. **Date-range projection.** Rejected: failed the spike above.
4. **Register partitions with `MSCK REPAIR TABLE`.** Not chosen: slower and needs a re-scan of S3 each time.

Related: [[decisions/0002-parquet-partitioned-by-quarter]], [[decisions/0007-dates-stored-as-date32]], [[decisions/0008-aws-setup-and-cost-guardrails]].
