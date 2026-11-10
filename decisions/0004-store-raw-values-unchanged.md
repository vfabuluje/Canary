# 0004 — Store raw FDIC values unchanged

**Date:** 2026-11-09
**Status:** Accepted

## Decision
Phase 1 saves what the FDIC published, with no cleaning:
- **No imputation.** Blanks stay null; nothing is filled in.
- **Keep 0s.** A 0 is not turned into null, even where it probably means "not reported".
- **Keep FDIC column names** (`ASSET`, `DEPUNINS`, ...) so each can be looked up in FDIC docs. Friendlier names come later in dbt (Phase 2).
- **Latest 2 quarters are re-pulled and overwritten on every run**, because banks amend recent filings. No snapshots are kept. `--force` re-pulls everything.
- Only changes: types are set (dates as dates, dollars as numbers) and an `ingested_at` timestamp is added.

## Why
Cleaning choices (what to do with a 0, how to fill gaps) affect model results, so they should be made on purpose, in Phase 3, and written down. If the raw layer is untouched, we can always redo them differently.

## Known limitations
- **The API serves amended values only.** It returns the current, corrected numbers for every quarter, not what the bank originally filed. The SVB replay therefore uses numbers as corrected later, not exactly what an analyst saw in early 2023. This is a point-in-time limitation and must be stated wherever results are reported.
- **0 can mean "not reported".** Some fields did not exist in early years (SVB's `SCHF` is 0 in 2001).
- **Uninsured-deposit estimates** (`DEPUNINS`) are mainly available for banks with $1B+ in assets.
- Dollar income fields (`NETINC`, `EINTEXP`, `ELNATR`, `NTLNLS`) are year-to-date; Phase 3 must convert them to per-quarter.

Related: [[decisions/0002-parquet-partitioned-by-quarter]], [[decisions/0003-curated-45-financial-fields]], [[data-dictionary/fdic_financials]].
