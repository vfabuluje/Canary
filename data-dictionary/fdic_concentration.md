# fdic_concentration

FDIC commercial real estate (CRE) loan and capital fields for every FDIC-insured bank, per quarter. Used by the Phase 5d real-estate concentration section (2006 regulator thresholds).

| | |
|---|---|
| Grain | One row per bank (`CERT`) per quarter (`REPDTE`) |
| Primary key | (`CERT`, `REPDTE`) |
| Source | `GET https://api.fdic.gov/banks/financials` (FDIC BankFind), fields `CERT,REPDTE,LNRECONS,LNREMULT,LNRENROT,LNCOMRE,RBC,RBCT1J,LNATRES` |
| File | `data/raw/concentration/repdte=YYYYMMDD/part.parquet` (one file per quarter) |
| Pull | `python -m canary.ingest concentration [--force] [--root data/raw]` |

Design and reasoning: [[specs/2026-11-19-phase5d-concentration-design]] section 4. This is a separate table from [[fdic_financials]] and [[fdic_specialty]] on purpose: extending the 45-field pull would replace the raw values the warehouse and features were built from, so adding these fields cannot change any existing number or model input. `LNRECONS` is pulled again here so every number in the test comes from the same pull. Values are stored exactly as published; the only conversion is blank to null. A quarter with 0 rows or a duplicate `CERT` is an error, not a written file. The latest 2 quarters are re-pulled on every run; `--force` re-pulls all.

## Columns

All dollar fields are in $ thousands, as published.

| Column | Type | FDIC title | Meaning (plain English) | Call Report item / caveats |
|---|---|---|---|---|
| `CERT` | int64 | FDIC Certificate # | The bank's unique FDIC ID number; joins to the financials table. | Never null. |
| `REPDTE` | date (Parquet `date32`) | Report Date | The quarter-end date this row describes. | e.g. 2022-12-31. |
| `LNRECONS` | float64 | RE CONSTRUCTION & LAND DEVELOP | Construction, land development and other land loans (1-4 family construction plus other construction and land). | Call Report F158 + F159. $ thousands. |
| `LNREMULT` | float64 | RE MULTIFAMILY | Loans secured by multifamily property. | Call Report 1460. $ thousands. |
| `LNRENROT` | float64 | RE NONFARM NONRES OTHER (NON-OWNER-OCCUPIED) | Loans secured by other (non-owner-occupied) nonfarm nonresidential property. | Call Report F161; reported from 2007. $ thousands. |
| `LNCOMRE` | float64 | LOANS TO FINANCE CRE NOT SECURED BY RE | Loans to finance commercial real estate, construction and land development that are not secured by real estate. | Call Report 2746. 0 for most small banks (3,817 of 4,773 at 2022-12-31); used as reported. $ thousands. |
| `RBC` | float64 | TOTAL RISK-BASED CAPITAL | Total risk-based capital (Tier 1 plus Tier 2). | Call Report 3792. Used as the capital denominator before 2020-03-31. 0 for 1,669 of 4,773 banks at 2022-12-31 (banks on the community bank leverage ratio framework do not report Tier 2). $ thousands. |
| `RBCT1J` | float64 | TIER 1 CAPITAL | Tier 1 capital. | Used with `LNATRES` as the capital denominator from 2020-03-31. $ thousands. |
| `LNATRES` | float64 | ALLOWANCE FOR LOAN AND LEASE LOSSES | Loan-loss allowance (for CECL adopters, the allowance for credit losses on loans and leases). | Added to `RBCT1J` from 2020-03-31. $ thousands. |
| `ingested_at` | timestamp (UTC) | (added by Canary) | When Canary pulled the row. | Not an FDIC field. |

## Coverage notes (checked 2026-11-19)

- All fields were present for each quarter checked.
- Any field can be null for a bank-quarter; a null is kept as null, never filled. A reported 0 is a real zero for the loan fields; for `RBC` see the next notes.
- Total CRE for the test is `LNRECONS + LNREMULT + LNRENROT + LNCOMRE`; a null component makes it missing.
- `RBC` of 0 for banks on the community bank leverage ratio framework (from 2020) means Tier 2 capital was not reported, not that capital is zero. No quarter from 2014 to 2019 has `RBC` of 0.
- Negative `RBC` or `RBCT1J` appears in 6 insolvent memo-era bank-quarters (certs 9956, 19328, 57564, 58302 twice, 17719); the section reports capital as zero or negative.
- Negative `LNATRES` appears in 4 bank-quarters (cert 30746 in 2020Q1-Q3; cert 4134 at 2024-09-30, where it cuts capital from 11,170 to 3,743); it is used as reported.
- In the memo era, capital and `LNRENROT`/`LNCOMRE` are null together in 714 rows.
- `RBC` being 0 for many banks at 2022-12-31 does not matter to the test: from 2020-03-31 the denominator is `RBCT1J + LNATRES` for every bank.
