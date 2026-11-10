# 0007 — Store report and failure dates as Parquet date32

**Date:** 2026-11-09
**Status:** Accepted

## Decision
`REPDTE`, `FAILDATE` and `RESDATE` are saved in Parquet as `date32` (a calendar date, no time of day). `ingested_at` is saved as a millisecond timestamp in UTC (`timestamp[ms, tz=UTC]`). The Phase 1 files were re-pulled to use these types.

## Why
- **They are dates, not times.** A report date like 2022-12-31 has no time of day. Storing it as a timestamp at midnight says something untrue and invites time-zone bugs.
- **Athena misreads nanosecond timestamps.** Phase 1 wrote `timestamp[ns]`, which Athena cannot read as a normal `timestamp` column. A `date32` column maps cleanly to Athena's `date` type, and the millisecond `ingested_at` maps to `timestamp`.
- **Fix it once at the source.** Every later step (Athena table, dbt models) then just declares `date` and `timestamp` and needs no conversions.

## Alternatives
1. **Keep the nanosecond timestamps and cast to dates in dbt.** Rejected: the Athena table could not even be declared cleanly over those files, and every model would repeat the cast.
2. **Store dates as text such as `20221231`.** Rejected: loses date comparisons and date math.

Related: [[decisions/0002-parquet-partitioned-by-quarter]], [[decisions/0004-store-raw-values-unchanged]].
