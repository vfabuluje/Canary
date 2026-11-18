---
cert: 25054
name: "Summit National Bank"
as_of: 2026-06-30
rank: 11
n_banks: 4313
percentile: 99.7681428240204
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:08:01"
writer_model: "claude-opus-5-5"
checked: true
---

# Summit National Bank (cert 25054)

*Outcome not yet known.*

## Summary

Summit National Bank, a Wyoming bank with $65.9 million in total assets, ranked 11 out of 4,313 banks nationally on Canary's risk score as of 2026-06-30, placing it in the 99.8th percentile. That rank put it on Canary's watchlist, which covers roughly the riskiest 2% of banks. Its thin capital cushion, the owners' money that absorbs losses, and deep losses drive the score: equity was 2.4% of assets and return on equity was -101.6%. Its loan quality, by contrast, looked close to the national median.

## Warning signs in the data

Capital is the clearest concern: equity was 2.4% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 2.5% against 11.0%. The Tier 1 risk-based capital ratio, which weighs capital against how risky the assets are, was 4.8% versus a median of 14.6%, and the total risk-based capital ratio was 6.1% versus 15.8%. The bank was also losing money: return on assets was -2.2% against a median of 1.2%, return on equity was -101.6% against 11.6%, and operating costs ran at 233.1% of revenue against a median of 62.1%.

Credit quality looked ordinary: loans 90 or more days late or not paying interest were 0.5% of loans, the same as the national median of 0.5%. The Texas ratio, which compares troubled assets with capital plus reserves, was 7.3% against a median of 2.9%, higher than typical mainly because the capital base is so small.

On funding, brokered deposits (money placed through middlemen, which can leave quickly) made up 34.4% of deposits, while the median bank had 0.0%. Deposits shrank by -24.2% over the past four quarters, compared with median growth of 4.2%, though the bank held a large cash buffer of 27.8% of assets against a median of 6.2%. Unrealized losses on bonds available for sale equaled 17.0% of equity, well above the national median of 5.6%.

## Understanding the score

As of 2026-06-30, Summit National Bank ranked 11 of 4,313 banks, which is the 99.8th percentile on a scale of 0 to 100 where higher means riskier. The bank was flagged on the watchlist, one of 87 banks that quarter, a list meant to cover about 2% of banks.

The five factors that pushed the score up most were return on equity at -101.6%, the Tier 1 risk-based capital ratio at 4.8%, bond losses available for sale at 17.0% of equity, the total risk-based capital ratio at 6.1%, and brokered deposits at 34.4% of deposits.

The five factors that pulled the score down most were the Texas ratio at 7.3%, nonaccrual assets and foreclosed property at 0.2% of assets, deposit growth over the past four quarters at -24.2%, loans 90 or more days past due or not accruing at 0.5% of loans, and securities at 17.1% of assets.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 269 | 4,589 |  |
| 2024-12-31 | 17 | 4,560 | ▲ watchlist |
| 2025-03-31 | 12 | 4,536 | ▲ watchlist |
| 2025-06-30 | 3 | 4,494 | ▲ watchlist |
| 2025-09-30 | 3 | 4,452 | ▲ watchlist |
| 2025-12-31 | 5 | 4,411 | ▲ watchlist |
| 2026-03-31 | 100 | 4,353 |  |
| 2026-06-30 | 11 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight, this bank falls in the open-watchlist case: the model flagged it, and our data does not record it as having failed. The fact sheet contains no data from after the as-of quarter, so this memo cannot say whether its condition later improved or worsened. A watchlist flag marks a bank whose figures resemble those of past failures; it is not a prediction that this particular bank will close.

## What happened next

Looking back with hindsight, the fact sheet provides no later ranks, flags or reporting status for this bank. Because of that, this memo cannot say whether the bank stayed on the watchlist or kept filing reports; the score history table added below is the place to check for later quarters.

## Sources

- F1 · Bank name · n/a · Summit National Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WY · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 11 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 2.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 6.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 7.3% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -2.2% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -101.6% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 233.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 34.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 27.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 17.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $65.9 million · data/features/fct_bank_features.parquet: log_total_assets
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -24.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -101.6%; contribution to the score · 2026-06-30 · +1.509 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: the Tier 1 risk-based capital ratio, value 4.8%; contribution to the score · 2026-06-30 · +1.371 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver up #3: losses on bonds available for sale, as a share of equity, value 17.0%; contribution to the score · 2026-06-30 · +0.545 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 6.1%; contribution to the score · 2026-06-30 · +0.482 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: brokered deposits as a share of deposits, value 34.4%; contribution to the score · 2026-06-30 · +0.410 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 7.3%; contribution to the score · 2026-06-30 · -1.172 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: nonaccrual assets and foreclosed property, as a share of assets, value 0.2%; contribution to the score · 2026-06-30 · -0.755 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F82 · Driver down #3: deposit growth over the past four quarters, value -24.2%; contribution to the score · 2026-06-30 · -0.471 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F83 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 0.5%; contribution to the score · 2026-06-30 · -0.440 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F84 · Driver down #5: securities as a share of assets, value 17.1%; contribution to the score · 2026-06-30 · -0.332 · data/analyst/scores.parquet: feature securities_to_assets contribution
