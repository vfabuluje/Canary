# Canary: bank failure early-warning system

**Research tool, not financial advice.**

Silicon Valley Bank (SVB) failed in March 2023 after customers pulled about $42B in one day. Its public filings had shown the warning signs for months: huge unrealized losses on long-term bonds and mostly uninsured deposits. Canary asks whether a model built only on public regulatory data could have flagged SVB, Signature Bank and First Republic before they failed. The goal is to score every FDIC-insured US bank's risk of failing within the next 4 quarters.

The name comes from the canary in the coal mine: it reacts to danger before people do.

## Status
**Phase 1 (done): FDIC data pull.** Pulls quarterly financials for every FDIC-insured bank and the FDIC failed bank list to local Parquet files. There is no model yet and no results to report.

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

## Scale (measured)
- **Financials:** 710,691 rows over 102 quarters (2001-03-31 to 2026-06-30); 9,940 banks in the first quarter, 4,313 in the latest.
- **Failures:** 4,117 rows (3,524 FAILURE, 593 ASSISTANCE; 574 FAILURE since 2001).
- **On disk:** 172 MB. Full pull: 6 min 47 s (102 API calls). Rerun: about 7 s.
- **Tests:** 62 passing (55 unit, 7 data checks).

## Limitations
- **Amended data only.** The FDIC API serves current, corrected values, not what banks originally filed. The SVB replay will use numbers as corrected later, not exactly what an analyst saw at the time.
- **0 can mean "not reported."** Some fields did not exist in early years. Phase 1 keeps the 0; cleaning is a later, documented step.
- **Uninsured-deposit estimates** are mainly available for banks with $1B+ in assets.
- Dollar income fields are year-to-date and dollar amounts are in thousands.

See `decisions/` for the reasoning and `data-dictionary/` for every column.

## Roadmap
2. Call report pipeline to S3/Athena; dbt models and data tests
3. CAMELS-style features; train XGBoost; test on 2016-2024 (train 2001-2015, time-based only)
4. SVB / Signature / First Republic replay; error analysis
5. AI risk analyst agent that writes cited risk memos per bank
6. Streamlit dashboard; metrics and limitations; demo video
