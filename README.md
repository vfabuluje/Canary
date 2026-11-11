# Canary

**An early-warning system for US bank failures.**

> **The question:** from public quarterly data alone, can a model trained only on 2001–2015 pick out the banks that failed in 2016–2024, and in particular Silicon Valley Bank, Signature Bank and First Republic, before they failed?

**Research tool, not financial advice.**

Silicon Valley Bank (SVB) failed in March 2023 after customers pulled about $42B in one day. Its public filings had shown the warning signs for months: huge unrealized losses on long-term bonds and mostly uninsured deposits. The goal is to score every FDIC-insured US bank's risk of failing within the next 4 quarters.

**Why "Canary"?** Coal miners once carried canaries underground. The birds reacted to toxic gas before people did, so a sick canary was the signal to get out. Canary aims to be that early signal for banks.

## Status
**Phase 1 (done): FDIC data pull.** Pulls quarterly financials for every FDIC-insured bank and the FDIC failed bank list to local Parquet files.

**Phase 2 (done): warehouse.** The raw files are copied to S3, exposed as Athena tables, and cleaned into dbt models with data tests.

**Phase 3 (done): features and model.** 31 CAMELS-style ratios per bank per quarter, an XGBoost model trained on report dates 2001-2014 and tested once on 2016-2024. Results are below. Short version: it has a higher AUC than a simple baseline (0.902 vs 0.774) with similar recall at the 2% flag, but **it did not flag SVB, Signature or First Republic.** Phase 4 investigates why.

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
dim_failed_banks, fct_bank_quarters         tables     canary_marts
fct_bank_features                           table      canary_marts  (Phase 3)
      |  python -m canary.export_features   (Athena UNLOAD to local Parquet)
      v
python -m canary.model train / evaluate     XGBoost, metrics.json, case_studies.csv
```
What each tool is, why Canary uses it, and what it does here: [TOOLS.md](TOOLS.md).

## How to run the warehouse
One-time AWS setup (bucket, Athena, budget, limited IAM user): [runbooks/aws-setup.md](runbooks/aws-setup.md). Copy `.env.example` to `.env` and set `CANARY_BUCKET`.

Each refresh, in order: `canary.ingest`, `canary.upload`, `canary.athena_ddl`, then `dbt build --no-partial-parse` from `warehouse/`. Details and what to do if a step fails: [runbooks/warehouse-refresh.md](runbooks/warehouse-refresh.md). Features, training and the one-time test: [runbooks/model-training.md](runbooks/model-training.md). To re-run only the dbt tests (read-only): `dbt test --no-partial-parse --profiles-dir .` from `warehouse/`.

## Scale (measured)
- **Financials:** 710,691 rows over 102 quarters (2001-03-31 to 2026-06-30); 9,940 banks in the first quarter, 4,313 in the latest.
- **Failures:** 4,117 rows (3,524 FAILURE, 593 ASSISTANCE; 574 FAILURE since 2001).
- **On disk:** 172 MB. Full pull: 6 min 47 s (102 API calls). Rerun: about 7 s.
- **Warehouse:** `fct_bank_quarters` 710,691 rows; `dim_failed_banks` 574 rows; `fct_bank_features` 710,691 rows with 31 features.
- **Model data:** 470,361 training rows (2,134 positive), 188,250 test rows (102 positive).
- **Tests:** 142 pytest tests passing. dbt: 29 data tests, 24 pass and 5 warnings, 0 errors. The warnings are the known ones: cert 34264 (First Alliance Bank and Trust Co, failed 2001-02-02, before the first quarter of financials) and four range checks on `fct_bank_features` (see [data-dictionary/fct_bank_features.md](data-dictionary/fct_bank_features.md)).
- **AWS cost so far:** $0.02 as of 2026-11-11, per the AWS Billing console (budget cap: $5/month)
- **Case-study label check:** SVB and Signature at 2022-12-31 and First Republic at 2023-03-31 each show 1 quarter until failure, meaning that report was the last one before the bank closed.

## Results (2016-2024 test, run once)
The model was trained on report dates 2001-03-31 to 2014-12-31 (2015 is dropped; see [decision 0010](decisions/0010-label-and-time-split.md)). A row is "positive" if the bank failed 1 to 4 quarters after that report. Each quarter the 2% of banks with the highest score are flagged ([decision 0011](decisions/0011-watchlist-flag-and-metrics.md)). The test set has 188,250 bank-quarters, 102 of them positive. The baseline is the Texas ratio, a classic rule of thumb (bad loans and foreclosed property divided by equity plus loan-loss reserve), flagged the same way. Numbers come from `metrics.json` of the single evaluation run.

| Metric | XGBoost | Texas-ratio baseline |
|---|---|---|
| AUC (2016-2024) | 0.902 | 0.774 |
| Recall: failed banks flagged at least once 1-4 quarters before failing | 21 of 29 (72%) | 19 of 29 (66%) |
| Recall with 2+ quarters notice | 18 of 27 (67%) | 17 of 27 (63%) |
| Lead time (first flag, quarters before failure): median, range | 4, 1-4 | 4, 1-4 |
| False-alarm rate (flagged rows not within 4 quarters of failing) | 98.3% | 98.4% |
| Never-failed banks flagged at least once in 9 years | 746 | 544 |

**Reading the numbers.**
- The 29 "eligible" banks are the failed banks with at least one report 1-4 quarters before failure from 2016 on. Only 29 banks, so one bank moves recall by about 3 points. The gap between 21 and 19 is two banks, not strong evidence.
- **The 98.3% false-alarm rate is mostly built in, not a sign the model is useless.** The watchlist flags 2% of about 5,200 banks on average, about 105 per quarter (3,783 flagged rows over 36 quarters), while only about 3 banks fail per year. Even a good ranking cannot avoid flagging many banks that survive. Precision is about 1.7% against a base rate of 102 / 188,250 = 0.054%, so a flagged bank is about 32 times more likely to be a near-term failure than a random one. Still, 746 different banks that did not fail within the window were flagged at least once over 9 years; a supervisor would call that a lot of wasted attention.
- **Lead time is capped at 4 by the label window**, so a median of 4 means most caught banks were already flagged at the earliest point the label can show. It is counted from the report date. Reports become public about a month after quarter-end, so the real warning is about a month shorter than the numbers above.
- The Texas-ratio baseline is hard to beat on recall; the model's clearer advantage is the overall ranking (AUC).
- The settings were chosen on a 2012-2014 validation block, not on the test years. Settings: max depth 5, learning rate 0.1, min child weight 10, 79 trees, seed 42 (`run_config.json`).

### Case studies: SVB, Signature, First Republic
**None of the three was flagged in any quarter.** Percentile is the bank's score rank among all banks that quarter (99 = riskier than 99% of banks; the flag needs about the top 2%, so roughly 98 or higher). The top signal is the feature that pushed the bank's score up most.

**Silicon Valley Bank**

| Report | Qtrs before failure | Percentile | Rank / banks | Flagged | Top 3 signals |
|---|---|---|---|---|---|
| 2021-03-31 | 8 | 75.0 | 1263 / 5044 | no | deposit_growth_4q=+0.327, cre_loans_to_loans=+0.229, efficiency_ratio=+0.133 |
| 2021-06-30 | 7 | 79.7 | 1018 / 5015 | no | deposit_growth_4q=+0.364, cre_loans_to_loans=+0.196, efficiency_ratio=+0.100 |
| 2021-09-30 | 6 | 77.1 | 1142 / 4979 | no | deposit_growth_4q=+0.350, cre_loans_to_loans=+0.230, leverage_ratio=+0.081 |
| 2021-12-31 | 5 | 56.0 | 2160 / 4904 | no | deposit_growth_4q=+0.333, cre_loans_to_loans=+0.163, efficiency_ratio=+0.107 |
| 2022-03-31 | 4 | 25.2 | 3638 / 4861 | no | deposit_growth_4q=+0.281, cre_loans_to_loans=+0.180, afs_unrealized_loss_to_equity=+0.169 |
| 2022-06-30 | 3 | 7.2 | 4489 / 4838 | no | efficiency_ratio=+0.190, cre_loans_to_loans=+0.163, afs_unrealized_loss_to_equity=+0.156 |
| 2022-09-30 | 2 | 24.4 | 3640 / 4813 | no | afs_unrealized_loss_to_equity=+0.798, efficiency_ratio=+0.167, cre_loans_to_loans=+0.123 |
| 2022-12-31 | 1 | 26.8 | 3494 / 4773 | no | afs_unrealized_loss_to_equity=+0.804, efficiency_ratio=+0.159, cre_loans_to_loans=+0.118 |

**Signature Bank**

| Report | Qtrs before failure | Percentile | Rank / banks | Flagged | Top 3 signals |
|---|---|---|---|---|---|
| 2021-03-31 | 8 | 79.8 | 1022 / 5044 | no | deposit_growth_4q=+0.325, efficiency_ratio=+0.291, loans_to_deposits=+0.149 |
| 2021-06-30 | 7 | 83.4 | 831 / 5015 | no | deposit_growth_4q=+0.308, efficiency_ratio=+0.256, loans_to_deposits=+0.155 |
| 2021-09-30 | 6 | 81.7 | 913 / 4979 | no | deposit_growth_4q=+0.299, efficiency_ratio=+0.214, loans_to_deposits=+0.155 |
| 2021-12-31 | 5 | 79.9 | 986 / 4904 | no | deposit_growth_4q=+0.294, efficiency_ratio=+0.215, loans_to_deposits=+0.158 |
| 2022-03-31 | 4 | 49.5 | 2456 / 4861 | no | efficiency_ratio=+0.333, afs_unrealized_loss_to_equity=+0.290, deposit_growth_4q=+0.190 |
| 2022-06-30 | 3 | 55.3 | 2162 / 4838 | no | afs_unrealized_loss_to_equity=+0.848, efficiency_ratio=+0.333, loans_to_deposits=+0.146 |
| 2022-09-30 | 2 | 91.3 | 420 / 4813 | no | afs_unrealized_loss_to_equity=+1.999, efficiency_ratio=+0.268, core_deposits_to_assets=+0.042 |
| 2022-12-31 | 1 | 94.9 | 246 / 4773 | no | afs_unrealized_loss_to_equity=+2.063, efficiency_ratio=+0.186, asset_growth_4q=+0.101 |

**First Republic Bank**

| Report | Qtrs before failure | Percentile | Rank / banks | Flagged | Top 3 signals |
|---|---|---|---|---|---|
| 2021-03-31 | 9 | 80.3 | 995 / 5044 | no | cre_loans_to_loans=+0.274, deposit_growth_4q=+0.227, past_due_30_89_to_assets=+0.074 |
| 2021-06-30 | 8 | 73.6 | 1327 / 5015 | no | cre_loans_to_loans=+0.302, deposit_growth_4q=+0.220, leverage_ratio=+0.061 |
| 2021-09-30 | 7 | 88.7 | 566 / 4979 | no | cre_loans_to_loans=+0.328, deposit_growth_4q=+0.250, past_due_30_89_to_assets=+0.083 |
| 2021-12-31 | 6 | 80.7 | 948 / 4904 | no | cre_loans_to_loans=+0.350, deposit_growth_4q=+0.236, afs_unrealized_loss_to_equity=+0.056 |
| 2022-03-31 | 5 | 28.0 | 3502 / 4861 | no | cre_loans_to_loans=+0.242, deposit_growth_4q=+0.050, afs_unrealized_loss_to_equity=+0.049 |
| 2022-06-30 | 4 | 32.6 | 3262 / 4838 | no | cre_loans_to_loans=+0.317, afs_unrealized_loss_to_equity=+0.055, deposit_growth_4q=+0.049 |
| 2022-09-30 | 3 | 35.7 | 3095 / 4813 | no | cre_loans_to_loans=+0.308, past_due_30_89_to_assets=+0.074, afs_unrealized_loss_to_equity=+0.051 |
| 2022-12-31 | 2 | 29.7 | 3355 / 4773 | no | cre_loans_to_loans=+0.308, afs_unrealized_loss_to_equity=+0.051, equity_to_assets=+0.043 |
| 2023-03-31 | 1 | 83.0 | 809 / 4740 | no | volatile_liabilities_to_assets=+0.357, cre_loans_to_loans=+0.306, core_deposits_to_assets=+0.090 |

Every case-study quarter is shown (26 rows, from 2021-03-31). Rank 1 is the riskiest bank; the flag needs rank within the top 2% (rank 96 or better for 4,773 banks, about the 98th percentile). Signals are the features that pushed the score up most (the CSV, `case_studies.csv`, lists up to 5); values are in the model's score units (log-odds contributions), not percentages. None of the three was flagged by the model or by the Texas-ratio baseline in any test quarter 2016-2024.

### What was caught, what wasn't, and why
The model caught 21 of 29 eligible failed banks at least once with 1-4 quarters of notice, but none of the three famous 2023 failures. Signature came closest (94.9th percentile at 2022-12-31: rank 246; the cutoff was rank 96, about the 98th percentile). First Republic reached the 83rd percentile in its last report. SVB was in the 80th percentile in mid-2021 and then **fell** to the 27th percentile by 2022-12-31: right before it failed, the model rated it safer than most banks. The model did react to bond losses: unrealized losses on available-for-sale bonds were the top push for SVB and Signature in the second half of 2022. It was not enough to reach the top 2%. SVB's much bigger held-to-maturity loss (about 98% of its equity) did not show up in its top 5 signals, and its clean loans and profits pulled its score down.

One hypothesis, not proven: the training years (2001-2014) are dominated by credit-loss failures of 2008-2012, banks that failed because their loans went bad, and perhaps few training-era banks failed from bond losses or a run by uninsured depositors, so the model may have learned that clean loans plus profits mean safe. Another possibility is that the signals were present but too weak relative to thousands of other banks. This is a limit of learning from past failures, and it is the honest result: **a model trained only on pre-2015 data did not catch SVB.** Phase 4 (replay and error analysis) tests these hypotheses and asks what signal would have caught them. Any model change made after seeing the 2023 results means 2016-2024 is no longer a clean out-of-sample test, so Phase 4 reports such changes separately.

## Limitations
- **Amended data only.** The FDIC API serves current, corrected values, not what banks originally filed. The SVB replay will use numbers as corrected later, not exactly what an analyst saw at the time.
- **0 can mean "not reported."** Some fields did not exist in early years. Phase 1 keeps the 0; cleaning is a later, documented step.
- **FDIC API only.** Bulk FFIEC call reports are deferred ([decision 0005](decisions/0005-fdic-api-only-no-bulk-call-reports.md)); they appear to hold amended values too, so they would likely not fix the limitation above.
- **The real warning window is shorter than the label suggests.** Banks file each quarter's report about a month after the quarter ends. SVB's December 31, 2022 numbers became public around late January 2023, roughly six weeks before it closed on March 10, not a full quarter earlier. Any lead time Canary reports is counted from the report date, so the time an analyst would really have had is about a month less.
- **Small test, rare events.** 29 eligible failed banks and 102 positive rows: results are noisy, and no confidence intervals are reported.
- **Validation is slightly optimistic.** The inner validation split (fit through 2011, validate 2012-2014) has no gap: fit rows from late 2011 carry labels from 2012 failures, which fall inside the validation block. This slightly flatters the validation score used to pick settings. It does not affect the test result.
- **Outliers kept in the features.** About 183 of 710,691 feature rows fall outside their expected 0-1 range (reporting errors); they were kept as-is ([data dictionary](data-dictionary/fct_bank_features.md)). Tree models are robust to them.
- **Uninsured-deposit estimates** are filled in for about 99% of banks every year, so they are not limited to large banks ([decision 0009](decisions/0009-features-and-zero-handling.md)). Reported 0s are treated as missing in the feature. The estimate is a regulatory one, not an exact count.
- Dollar income fields are year-to-date and dollar amounts are in thousands.

See `decisions/` for the reasoning and `data-dictionary/` for every column.

## Roadmap
2. (done) FDIC data to S3/Athena; dbt models and data tests
3. (done) CAMELS-style features; train XGBoost; test on 2016-2024 (time-based only)
4. SVB / Signature / First Republic replay; error analysis
5. AI risk analyst agent that writes cited risk memos per bank
6. Streamlit dashboard; metrics and limitations; demo video
