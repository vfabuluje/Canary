---
cert: 1802
name: "Fayette County Bank"
as_of: 2017-03-31
rank: 1
n_banks: 5925
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-05-26
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:11"
writer_model: "claude-opus-5-5"
checked: true
---

# Fayette County Bank (cert 1802)

*Hindsight: failed 2017-05-26. Canary flagged it 4 quarters ahead.*

## Summary

As of 2017-03-31, Fayette County Bank (certificate 1802, based in IL) ranked 1 out of 5,925 banks on Canary's risk score, placing it at the 100.0th percentile, where higher means riskier. It was flagged on Canary's watchlist that quarter, one of 119 banks. Its capital cushion was very thin, with equity, meaning the owners' stake, at 1.0% of assets against a national median of 10.7%. Problem loans and losses were also far worse than at a typical bank.

## Warning signs in the data

Capital, the bank's buffer for absorbing losses, was far below normal: equity was 1.0% of assets versus a national median of 10.7%, and the leverage ratio (core capital as a share of average assets) was 0.9% versus 10.5%. The Tier 1 risk-based capital ratio, which weighs capital against riskier assets, was 1.3% versus a median of 15.1%, and the total risk-based capital ratio was 2.6% versus 16.2%.

Credit quality was weak: loans 90 or more days past due or no longer earning interest made up 13.3% of loans, against a national median of 0.6%. Loans that were overdue but not yet seriously late were 5.0% of assets versus 0.3%, and nonaccrual assets plus foreclosed property were 9.7% of assets versus 0.5%. The Texas ratio, which compares troubled assets with the capital and reserves available to cover them, stood at 247.7% against a median of 4.8%. The bank was losing money, with a return on assets of -1.3% and a return on equity of -118.2%, compared with medians of 0.9% and 8.0%.

On funding, brokered deposits, money gathered through third-party brokers rather than local customers, were 25.0% of deposits versus a national median of 0.0%, while cash was 2.4% of assets versus 6.9%. Losses on bonds available for sale, as a share of equity, read -9.2% against a median of 0.3%, and the bank held $34.4 million in total assets versus a median of $204.8 million.

## Understanding the score

As of 2017-03-31, Fayette County Bank ranked 1 of 5,925 banks, at the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers the riskiest 2% of banks, or 119 banks that quarter.

The five factors pushing the score up most were the Tier 1 risk-based capital ratio at 1.3%, return on equity at -118.2%, the Texas ratio at 247.7%, loans 90 or more days past due or not accruing interest at 13.3% of loans, and the leverage ratio at 0.9%. The five factors pulling it down most were construction loans at 2.1% of loans, losses on bonds available for sale at -9.2% of equity, interest expense at 1.1% of assets, volatile funding at 1.9% of assets, and core deposits, the stable everyday deposits, at 72.3% of assets.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 13 | 6,193 | ▲ watchlist |
| 2016-06-30 | 6 | 6,129 | ▲ watchlist (first flag) |
| 2016-09-30 | 3 | 6,051 | ▲ watchlist |
| 2016-12-31 | 1 | 5,983 | ▲ watchlist |
| 2017-03-31 | 1 | 5,925 | ▲ watchlist |

## How early Canary caught it

In hindsight, Canary first flagged Fayette County Bank in the quarter ending 2016-06-30, under its lead-time rule. The bank failed on 2017-05-26, giving a lead time of 4 quarters before failure.

At that first flag, the main factors pushing the score up were return on equity at -74.1%, the Tier 1 risk-based capital ratio at 6.1%, the Texas ratio at 136.2%, loans 90 or more days past due or not accruing interest at 12.8%, and the total risk-based capital ratio at 7.4%. Several of the same warning signs were already present then and grew worse by the as-of quarter.

## What happened next

In hindsight, the last quarter Fayette County Bank reported data was 2017-03-31, and it stopped reporting after that. The bank failed on 2017-05-26.

## Sources

- F2 · Certificate number · n/a · 1802 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2017-03-31 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2017-03-31 · 5,925 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2017-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2017-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2017-03-31 · 119 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2017-03-31 · 1.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2017-03-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · 0.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2017-03-31 · 1.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2017-03-31 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2017-03-31 · 2.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2017-03-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 13.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 9.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2017-03-31 · 5.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2017-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 247.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 4.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2017-03-31 · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2017-03-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2017-03-31 · -118.2% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2017-03-31 · 8.0% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2017-03-31 · 25.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2017-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2017-03-31 · 2.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2017-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2017-03-31 · -9.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2017-03-31 · 0.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2017-03-31 · $34.4 million · data/features/fct_bank_features.parquet: log_total_assets
- F70 · National median: total assets · 2017-03-31 · $204.8 million · data/features/fct_bank_features.parquet: log_total_assets (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 1.3%; contribution to the score · 2017-03-31 · +2.037 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -118.2%; contribution to the score · 2017-03-31 · +1.311 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 247.7%; contribution to the score · 2017-03-31 · +1.137 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 13.3%; contribution to the score · 2017-03-31 · +0.686 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the leverage ratio (core capital as a share of average assets), value 0.9%; contribution to the score · 2017-03-31 · +0.557 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #1: construction loans as a share of loans, value 2.1%; contribution to the score · 2017-03-31 · -0.228 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F81 · Driver down #2: losses on bonds available for sale, as a share of equity, value -9.2%; contribution to the score · 2017-03-31 · -0.198 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F82 · Driver down #3: annualized interest expense as a share of assets, value 1.1%; contribution to the score · 2017-03-31 · -0.180 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F83 · Driver down #4: volatile funding as a share of assets, value 1.9%; contribution to the score · 2017-03-31 · -0.070 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F84 · Driver down #5: core deposits as a share of assets, value 72.3%; contribution to the score · 2017-03-31 · -0.061 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F85 · Failure date · 2017-05-26 · 2017-05-26 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-06-30 · 2016-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-06-30: return on equity (profit as a share of equity), value -74.1%; contribution to the score · 2016-06-30 · +1.121 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2016-06-30: the Tier 1 risk-based capital ratio, value 6.1%; contribution to the score · 2016-06-30 · +1.056 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F90 · Driver up #3 at 2016-06-30: the Texas ratio (troubled assets against capital plus reserves), value 136.2%; contribution to the score · 2016-06-30 · +0.880 · data/analyst/scores.parquet: feature texas_ratio contribution
- F91 · Driver up #4 at 2016-06-30: loans 90+ days past due or not accruing interest, as a share of loans, value 12.8%; contribution to the score · 2016-06-30 · +0.668 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2016-06-30: the total risk-based capital ratio, value 7.4%; contribution to the score · 2016-06-30 · +0.390 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
