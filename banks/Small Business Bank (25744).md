---
cert: 25744
name: "Small Business Bank"
as_of: 2026-03-31
rank: 10
n_banks: 4353
percentile: 99.79324603721571
flagged: true
outcome: "caught"
after_test_window: true
failure_date: 2026-07-17
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:48"
writer_model: "claude-opus-5-5"
checked: true
---

# Small Business Bank (cert 25744)

*Hindsight: failed 2026-07-17. Canary flagged it 4 quarters ahead.*
*After the test window: not part of the reported 2016-2024 results.*

## Summary

As of 2026-03-31, Small Business Bank, a Kansas bank, ranked 10 out of 4,353 banks nationally on Canary's risk score, placing it in the 99.8th percentile, where higher means riskier. That put it on Canary's watchlist, which covers the top 2% of banks. Its equity, the owners' cushion against losses, was 4.9% of assets against a national median of 10.4%, and it was losing money, with a return on assets of -4.3% against a median of 1.2%.

## Warning signs in the data

Capital was thin by simple measures: equity was 4.9% of assets versus a national median of 10.4%, and the leverage ratio (core capital as a share of average assets) was 4.8% versus 10.9%. Risk-based capital ratios, which weight assets by riskiness, looked closer to normal, with the Tier 1 ratio at 14.0% versus 14.5% and the total ratio at 15.3% versus 15.7%.

Credit quality was the clearest problem: loans 90+ days past due or not accruing interest were 4.8% of loans, far above the median of 0.5%. Loans 30-89 days past due, an early sign of trouble, were 9.4% of assets against a median of 0.3%, and nonaccrual assets plus foreclosed property were 4.1% of assets against 0.3%. The Texas ratio, which compares troubled assets with capital plus reserves, was 55.5%, far above the median of 2.9%. Earnings were deeply negative, with return on equity at -79.5% versus a median of 11.2%, and the efficiency ratio (operating costs as a share of revenue) was 249.0% versus 63.1%.

Funding looked steadier: uninsured deposits were 9.9% of deposits versus a median of 24.4%, core deposits (stable everyday deposits) were 94.3% of assets versus 75.8%, and cash was 13.2% of assets versus 6.9%. The bank was shrinking, though, with assets down -14.3% and deposits down -9.8% over the past four quarters, while the medians grew 4.3% and 4.0%. Bond losses were not a concern, since securities were 0.0% of assets versus a median of 17.5%, and losses on bonds available for sale were 0.0% of equity versus 5.8%.

## Understanding the score

In the quarter ending 2026-03-31, the bank ranked 10 of 4,353 banks, in the 99.8th percentile, and was one of 88 banks flagged on the watchlist, which holds the top 2% of scores.

The five factors pushing the score up most were return on equity at -79.5%, core deposits at 94.3% of assets, the Texas ratio at 55.5%, interest expense at 2.4% of assets, and return on assets at -4.3%. The five factors pulling the score down most were the Tier 1 risk-based capital ratio at 14.0%, construction loans at 2.7% of loans, the total risk-based capital ratio at 15.3%, uninsured deposits at 9.9% of deposits, and commercial real estate loans at 28.0% of loans. The Tier 1 ratio was the single largest factor in either direction, with a contribution of -1.507, while return on equity added +1.253.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-06-30 | 441 | 4,610 |  |
| 2024-09-30 | 799 | 4,589 |  |
| 2024-12-31 | 374 | 4,560 |  |
| 2025-03-31 | 106 | 4,536 |  |
| 2025-06-30 | 440 | 4,494 |  |
| 2025-09-30 | 65 | 4,452 | ▲ watchlist (first flag) |
| 2025-12-31 | 8 | 4,411 | ▲ watchlist |
| 2026-03-31 | 10 | 4,353 | ▲ watchlist |

## How early Canary caught it

In hindsight, Canary first flagged the bank in the quarter ending 2025-09-30, and the bank failed on 2026-07-17, a lead time of 4 quarters. At that first flag, the biggest factor pushing the score up was return on equity at -66.8%, followed by interest expense at 2.5% of assets and loan-loss provisions at 2.5% of assets. Its Tier 1 risk-based capital ratio of 21.6% was then still the largest factor holding the score down.

This pattern of mounting loan problems and losses fits the most common profile in the training data, where 96% of the 539 failed banks were credit-loss failures.

*After the test window: not part of the reported 2016-2024 results.*

## What happened next

In hindsight, the bank's last reported quarter was 2026-03-31, so there are no later ranks or flags in our data. The bank failed on 2026-07-17.

## Sources

- F3 · As-of quarter · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KS · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-03-31 · 10 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-03-31 · 4,353 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-03-31 · 99.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-03-31 · 88 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-03-31 · 4.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-03-31 · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-03-31 · 4.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-03-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-03-31 · 14.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-03-31 · 14.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-03-31 · 15.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-03-31 · 15.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-03-31 · 4.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-03-31 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-03-31 · 4.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-03-31 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-03-31 · 9.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-03-31 · 55.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-03-31 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-03-31 · -4.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-03-31 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-03-31 · -79.5% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-03-31 · 11.2% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-03-31 · 249.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-03-31 · 63.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-03-31 · 9.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-03-31 · 24.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-03-31 · 94.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-03-31 · 75.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-03-31 · 13.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-03-31 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-03-31 · 5.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2026-03-31 · 0.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2026-03-31 · 17.5% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2026-03-31 · -14.3% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2026-03-31 · 4.3% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-03-31 · -9.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-03-31 · 4.0% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -79.5%; contribution to the score · 2026-03-31 · +1.253 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: core deposits as a share of assets, value 94.3%; contribution to the score · 2026-03-31 · +0.516 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 55.5%; contribution to the score · 2026-03-31 · +0.505 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2026-03-31 · +0.351 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F79 · Driver up #5: return on assets (profit as a share of assets), value -4.3%; contribution to the score · 2026-03-31 · +0.306 · data/analyst/scores.parquet: feature return_on_assets contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 14.0%; contribution to the score · 2026-03-31 · -1.507 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: construction loans as a share of loans, value 2.7%; contribution to the score · 2026-03-31 · -0.283 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: the total risk-based capital ratio, value 15.3%; contribution to the score · 2026-03-31 · -0.273 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F83 · Driver down #4: uninsured deposits as a share of deposits, value 9.9%; contribution to the score · 2026-03-31 · -0.192 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F84 · Driver down #5: commercial real estate loans as a share of loans, value 28.0%; contribution to the score · 2026-03-31 · -0.125 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F85 · Failure date · 2026-07-17 · 2026-07-17 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2025-09-30 · 2025-09-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2025-09-30: return on equity (profit as a share of equity), value -66.8%; contribution to the score · 2025-09-30 · +1.081 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2025-09-30: annualized interest expense as a share of assets, value 2.5%; contribution to the score · 2025-09-30 · +0.347 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F90 · Driver up #3 at 2025-09-30: annualized provision for loan losses as a share of assets, value 2.5%; contribution to the score · 2025-09-30 · +0.319 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F93 · Driver down #1 at 2025-09-30: the Tier 1 risk-based capital ratio, value 21.6%; contribution to the score · 2025-09-30 · -1.700 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F100 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
