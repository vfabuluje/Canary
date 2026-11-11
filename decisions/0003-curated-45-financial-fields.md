# 0003 — Pull 45 hand-picked financial fields

**Date:** 2026-11-09
**Status:** Accepted

## Decision
Pull 45 fields from the FDIC financials API, chosen by hand and grouped as: identity, size, capital, asset quality, loan mix, earnings, liquidity and funding, and securities / interest-rate risk. The list lives in one Python file (`src/canary/schema.py`); every field is documented in [[data-dictionary/fdic_financials]].

## Why
- The fields map onto the CAMELS-style features planned for Phase 3 (capital, asset quality, earnings, liquidity, sensitivity to rates). CAMELS and the other acronyms here (HTM, `SCHA`/`SCHF`, etc.) are defined in [reference/GLOSSARY.md](../reference/GLOSSARY.md), added 2026-11-11.
- They include the SVB warning signs: held-to-maturity bond cost and fair value (`SCHA`, `SCHF`), equity (`EQ`), and uninsured deposits (`DEPUNINS`).
- Small enough that I can document and explain every column. Pulls stay fast (the full pull took 6 min 47 s).
- All 45 were checked against the FDIC field catalog and returned values for SVB in 2022 Q4.

## Alternatives
- **The API's default ~160 fields.** More to document and store, most not useful for the model yet.
- **All 2,378 fields.** Huge pulls, impossible to document properly, and most are empty for most banks.

## How to add a field later
1. Add one line to the field list in `src/canary/schema.py` (name and type).
2. Add its row to [[data-dictionary/fdic_financials]]. The dictionary test fails if you forget.
3. Re-pull everything with `python -m canary.ingest financials --force` (about 7 minutes), because old quarter files don't have the new column.

Related: [[decisions/0002-parquet-partitioned-by-quarter]].
