---
cert: 30003
name: "Guaranty Bank"
as_of: 2017-03-31
rank: 33
n_banks: 5925
percentile: 99.45991561181434
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-05-05
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:48"
writer_model: "claude-opus-5-5"
checked: true
---

# Guaranty Bank (cert 30003)

*Hindsight: failed 2017-05-05. Canary flagged it 4 quarters ahead.*

## Summary

As of 2017-03-31, Guaranty Bank of Wisconsin ranked 33 out of 5,925 banks nationally on Canary's risk score, placing it in the 99.5th percentile, where higher means riskier. That put it on Canary's watchlist that quarter. Its capital cushion, the owners' money that absorbs losses, was 2.1% of assets, far below the national median of 10.7%. Troubled loans (90+ days late or no longer paying interest) were 4.5% of loans, well above the national median of 0.6%.

## Warning signs in the data

Capital was the clearest weak spot: equity was 2.1% of assets against a national median of 10.7%, and the leverage ratio (core capital as a share of average assets) was 2.1% against a median of 10.5%. The Tier 1 risk-based capital ratio, which measures core capital against assets weighted by their riskiness, was 3.1% versus a median of 15.1%, and the total risk-based capital ratio was 4.4% versus 16.2%.

Credit quality was also poor: nonaccrual assets and foreclosed property were 3.4% of assets, well above the median of 0.5%. The Texas ratio, which compares troubled assets with the capital and reserves available to cover them, stood at 109.7%, far above the national median of 4.8%. Net loan write-offs were 0.4% of loans against a median of 0.0%, and operating costs ate up 93.9% of revenue compared with a median of 69.8%.

Funding looked stable rather than risky: core deposits, the steady everyday deposits, funded 97.0% of assets versus a median of 79.0%, and uninsured deposits were only 1.3% of deposits versus 17.3%. Cash was 14.9% of assets, above the median of 6.9%. Bond losses were small, at -0.2% of equity on bonds held to maturity and 0.4% on bonds available for sale, close to the medians of 0.0% and 0.3%.

## Understanding the score

In Q1 2017, Guaranty Bank ranked 33 of 5,925 banks, the 99.5th percentile on a scale of 0 to 100 where higher means riskier. The bank was flagged on the watchlist, which covers the top 2% of banks and held 119 banks that quarter.

The five factors pushing the score up most were the Tier 1 risk-based capital ratio at 3.1%, the Texas ratio at 109.7%, and the total risk-based capital ratio at 4.4%. Also pushing it up were core deposits as a share of assets at 97.0% and commercial real estate loans as a share of loans at 0.2%.

The five factors pulling the score down most were interest expense as a share of assets at 0.0%, return on equity (profit relative to the owners' stake) at 21.5%, and loans 30-89 days past due at 0.3% of assets. Return on assets at 0.4% and total assets of $1.0 billion also lowered the score.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 20 | 6,193 | ▲ watchlist |
| 2016-06-30 | 21 | 6,129 | ▲ watchlist (first flag) |
| 2016-09-30 | 11 | 6,051 | ▲ watchlist |
| 2016-12-31 | 17 | 5,983 | ▲ watchlist |
| 2017-03-31 | 33 | 5,925 | ▲ watchlist |

## How early Canary caught it

In hindsight, Canary first flagged Guaranty Bank in the quarter ending 2016-06-30, 4 quarters before it failed on 2017-05-05. At that first flag, the top drivers were already capital and troubled assets: a Tier 1 risk-based capital ratio of 3.3% and a Texas ratio of 125.6%. The total risk-based capital ratio was 4.5% at that time.

## What happened next

In hindsight, the bank failed on 2017-05-05. Its last report was for the quarter ending 2017-03-31, so there are no later ranks or flags. Our data shows only that the bank stopped reporting, which can mean a merger or a closure.

## Sources

- F1 · Bank name · n/a · Guaranty Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WI · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2017-03-31 · 33 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2017-03-31 · 5,925 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2017-03-31 · 99.5% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2017-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2017-03-31 · 119 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2017-03-31 · 2.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2017-03-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · 2.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2017-03-31 · 3.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2017-03-31 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2017-03-31 · 4.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2017-03-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 4.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 3.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2017-03-31 · 0.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2017-03-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 109.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 4.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2017-03-31 · 93.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2017-03-31 · 69.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2017-03-31 · 1.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2017-03-31 · 17.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2017-03-31 · 97.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2017-03-31 · 79.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2017-03-31 · 14.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2017-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2017-03-31 · -0.2% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2017-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2017-03-31 · 0.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2017-03-31 · 0.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 3.1%; contribution to the score · 2017-03-31 · +1.350 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 109.7%; contribution to the score · 2017-03-31 · +0.604 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: the total risk-based capital ratio, value 4.4%; contribution to the score · 2017-03-31 · +0.518 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F78 · Driver up #4: core deposits as a share of assets, value 97.0%; contribution to the score · 2017-03-31 · +0.318 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F79 · Driver up #5: commercial real estate loans as a share of loans, value 0.2%; contribution to the score · 2017-03-31 · +0.281 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.0%; contribution to the score · 2017-03-31 · -1.410 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 21.5%; contribution to the score · 2017-03-31 · -0.861 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: loans 30-89 days past due, as a share of assets, value 0.3%; contribution to the score · 2017-03-31 · -0.619 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F83 · Driver down #4: return on assets (profit as a share of assets), value 0.4%; contribution to the score · 2017-03-31 · -0.558 · data/analyst/scores.parquet: feature return_on_assets contribution
- F84 · Driver down #5: total assets, value $1.0 billion; contribution to the score · 2017-03-31 · -0.340 · data/analyst/scores.parquet: feature log_total_assets contribution
- F85 · Failure date · 2017-05-05 · 2017-05-05 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-06-30 · 2016-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-06-30: the Tier 1 risk-based capital ratio, value 3.3%; contribution to the score · 2016-06-30 · +1.814 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2016-06-30: the Texas ratio (troubled assets against capital plus reserves), value 125.6%; contribution to the score · 2016-06-30 · +1.083 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2016-06-30: the total risk-based capital ratio, value 4.5%; contribution to the score · 2016-06-30 · +0.426 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
