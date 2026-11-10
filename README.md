# Canary: bank failure early-warning system

**Research tool, not financial advice.**

Silicon Valley Bank (SVB) failed in March 2023 after customers pulled about $42B in one day. Its public filings had shown the warning signs for months: huge unrealized losses on long-term bonds and mostly uninsured deposits. Canary asks whether a model built only on public regulatory data could have flagged SVB, Signature Bank and First Republic before they failed. The goal is to score every FDIC-insured US bank's risk of failing within the next 4 quarters.

The name comes from the canary in the coal mine: it reacts to danger before people do.

## Status
**Phase 1 (done): FDIC data pull.** Pulls quarterly financials for every FDIC-insured bank and the FDIC failed bank list to local Parquet files.

**Phase 2 (done): warehouse.** The raw files are copied to S3, exposed as Athena tables, and cleaned into dbt models with data tests. There is no model yet and no results to report; Phase 3 trains it.

What the data already shows for SVB's last filing (2022 Q4):

| Signal | Value |
|---|---|
| Held-to-maturity bonds, cost vs fair value | $91.3B vs $76.2B ($15.2B unrealized loss) |
| Equity | $15.5B, so the bond loss was about all of it |
| Uninsured deposits | 86% ($151.6B of $175.4B) |

## Quickstart
```
python3.12 -m venv .venv
.venv/bin/pip install -e ".[dev]"
.venv/bin/python -m canary.ingest financials
.venv/bin/python -m canary.ingest failures
.venv/bin/pytest -v
```
More detail, including what to do if a pull fails: `runbooks/fdic-ingestion.md`.

## Architecture
```
FDIC BankFind API
      |  python -m canary.ingest            (Phase 1)
      v
local Parquet  data/raw/            one folder per quarter
      |  python -m canary.upload            (skips unchanged files, never deletes)
      v
S3  raw/fdic/
      |  python -m canary.athena_ddl        (raw tables; rerun after a new quarter)
      v
Athena raw tables   canary_raw
      |  dbt build                          (needs the owner's yes: replaces mart tables)
      v
stg_fdic__financials, stg_fdic__failures    views      canary_staging
dim_failed_banks, fct_bank_quarters         tables     canary_marts  -> Phase 3
```

## How to run the warehouse
One-time AWS setup (bucket, Athena, budget, limited IAM user): [runbooks/aws-setup.md](runbooks/aws-setup.md). Copy `.env.example` to `.env` and set `CANARY_BUCKET`.

Each refresh, in order: `canary.ingest`, `canary.upload`, `canary.athena_ddl`, then `dbt build --no-partial-parse` from `warehouse/`. Details and what to do if a step fails: [runbooks/warehouse-refresh.md](runbooks/warehouse-refresh.md). To re-run only the dbt tests (read-only): `dbt test --no-partial-parse --profiles-dir .` from `warehouse/`.

## Scale (measured)
- **Financials:** 710,691 rows over 102 quarters (2001-03-31 to 2026-06-30); 9,940 banks in the first quarter, 4,313 in the latest.
- **Failures:** 4,117 rows (3,524 FAILURE, 593 ASSISTANCE; 574 FAILURE since 2001).
- **On disk:** 172 MB. Full pull: 6 min 47 s (102 API calls). Rerun: about 7 s.
- **Warehouse:** `fct_bank_quarters` 710,691 rows; `dim_failed_banks` 574 rows.
- **Tests:** 100 pytest tests passing (93 unit, 7 data checks on local files). dbt: 19 data tests, 18 pass and 1 expected warning (cert 34264, First Alliance Bank and Trust Co, failed 2001-02-02, before the first quarter of financials).
- **AWS cost so far:** not yet recorded (budget cap: $5/month)
  <!-- TODO(owner): fill in from Billing console -->
- **Case-study label check:** SVB and Signature at 2022-12-31 and First Republic at 2023-03-31 each show 1 quarter until failure.

## Limitations
- **Amended data only.** The FDIC API serves current, corrected values, not what banks originally filed. The SVB replay will use numbers as corrected later, not exactly what an analyst saw at the time.
- **0 can mean "not reported."** Some fields did not exist in early years. Phase 1 keeps the 0; cleaning is a later, documented step.
- **FDIC API only.** Bulk FFIEC call reports are deferred ([decision 0005](decisions/0005-fdic-api-only-no-bulk-call-reports.md)); they appear to hold amended values too, so they would likely not fix the limitation above.
- **Uninsured-deposit estimates** are mainly available for banks with $1B+ in assets.
- Dollar income fields are year-to-date and dollar amounts are in thousands.

See `decisions/` for the reasoning and `data-dictionary/` for every column.

## Roadmap
2. (done) FDIC data to S3/Athena; dbt models and data tests
3. CAMELS-style features; train XGBoost; test on 2016-2024 (train 2001-2015, time-based only)
4. SVB / Signature / First Republic replay; error analysis
5. AI risk analyst agent that writes cited risk memos per bank
6. Streamlit dashboard; metrics and limitations; demo video
