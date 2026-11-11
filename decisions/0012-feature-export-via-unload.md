# 0012 — Export features with Athena UNLOAD under athena-results/

**Date:** 2026-11-11
**Status:** Accepted

## Decision
**The model reads a local Parquet file, produced by an Athena `UNLOAD` query.** `python -m canary.export_features` joins `fct_bank_features` to `fct_bank_quarters` (to get `quarters_until_failure`, `failure_date`, `institution_name`), writes Parquet parts to S3, downloads them, and writes one file at `data/features/fct_bank_features.parquet` (git-ignored). The write is atomic: a temp file is written first and renamed, so a failed run never leaves a half-written file or overwrites a good one.

**Why UNLOAD and not downloading the CSV result.** A normal Athena result is one untyped CSV, so dates and integers must be guessed again on load and nulls become empty strings. UNLOAD keeps the column types in Parquet, is compressed, and is much smaller. UNLOAD needs an empty target prefix, so each run uses a new UTC timestamp `run_id`.

**Why under `athena-results/exports/`.** The IAM user `canary-dev` may delete only under `athena-results/` and `dbt/`, and `athena-results/` objects expire after 7 days. Putting exports there means they clean themselves up and we need no new delete permission. The files are a temporary copy; the local Parquet is the thing we keep.

**Cost.** The query scans only the two mart tables, well under 1 GB, so the cost is a fraction of a cent, within the $5/month budget.

## Alternatives
1. **Download the CSV query result.** Rejected: loses types, bigger.
2. **Export under a new `exports/` prefix.** Rejected: would need a new delete right or manual cleanup.
3. **Query Athena directly from the training code.** Rejected: slow, repeated cost, and no frozen copy of the training data.

Related: [[decisions/0009-features-and-zero-handling]].
