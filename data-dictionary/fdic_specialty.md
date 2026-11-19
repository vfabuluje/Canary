# fdic_specialty

FDIC specialty group and city for every FDIC-insured bank, per quarter. Used by the Phase 5c peer comparison.

| | |
|---|---|
| Grain | One row per bank (`CERT`) per quarter (`REPDTE`) |
| Primary key | (`CERT`, `REPDTE`) |
| Source | `GET https://api.fdic.gov/banks/financials` (FDIC BankFind), fields `CERT,REPDTE,SPECGRP,CITY` |
| File | `data/raw/specialty/repdte=YYYYMMDD/part.parquet` (one file per quarter) |
| Pull | `python -m canary.ingest specialty [--force] [--root data/raw]` |

Design and reasoning: [[specs/2026-11-18-phase5c-peers-design]] section 5. This is a separate table from [[fdic_financials]] on purpose: the 45-field financials files stay untouched, so adding these two fields cannot change any existing number or model input. Values are stored exactly as published; the only conversion is blank to null. The specialty group is read at the quarter being analysed, from this table, never from the `institutions` endpoint.

## Columns

| Column | Type | FDIC title | Meaning (plain English) | Units / caveats |
|---|---|---|---|---|
| `CERT` | int64 | FDIC Certificate # | The bank's unique FDIC ID number; joins to the financials table. | Never null. |
| `REPDTE` | date (Parquet `date32`) | Report Date | The quarter-end date this row describes. | e.g. 2022-12-31. |
| `SPECGRP` | Int64 (nullable) | Asset concentration specialty group | The FDIC's specialty group code for the bank in that quarter (codes below). | Can be null; a null means no specialty group was recorded. |
| `CITY` | string | City | The city of the bank's main office. | Can change over time. |
| `ingested_at` | timestamp (UTC) | (added by Canary) | When Canary pulled the row. | Not an FDIC field. |

## Specialty group codes

| Code | Name |
|---|---|
| 1 | International Specialization |
| 2 | Agricultural Specialization |
| 3 | Credit-card Specialization |
| 4 | Commercial Lending Specialization |
| 5 | Mortgage Lending Specialization |
| 6 | Consumer Lending Specialization |
| 7 | Other Specialized Under 1 Billion |
| 8 | All Other Under 1 Billion |
| 9 | All Other Over 1 Billion |

Codes 8 and 9 are general groups: the FDIC did not record a lending specialty for the bank.
