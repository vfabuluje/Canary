---
cert: 21805
name: "First State Bank Of Dequeen"
as_of: 2026-06-30
rank: 17
n_banks: 4313
percentile: 99.62902851843265
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:08:37"
writer_model: "claude-opus-5-5"
checked: true
---

# First State Bank Of Dequeen (cert 21805)

*Outcome not yet known.*

## Summary

First State Bank Of Dequeen, an Arkansas bank, ranked 17 out of 4,313 banks nationally on Canary's risk score for the quarter ending 2026-06-30, placing it in the 99.6th percentile, where higher means riskier. That put it on Canary's watchlist, the top 2% of banks, which held 87 banks that quarter. The main pressures in its data were large unrealized losses on its bond holdings and heavy use of brokered deposits, while its profits were strong.

## Warning signs in the data

Capital, the cushion that absorbs losses, was thin: equity was 6.7% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.5% against a median of 11.0%. Bond losses stood out most: unrealized losses on bonds available for sale (bonds the bank could sell, marked at current market prices) equaled 27.4% of equity, far above the median of 5.6%. Securities made up 37.8% of assets, roughly double-digit points above the median of 17.6%, so bond prices weigh heavily on this bank.

On funding, brokered deposits (money placed through third-party brokers, which can leave quickly) were 24.1% of deposits, while the median bank had 0.0%. Interest expense was 2.7% of assets against a median of 1.6%, and borrowings from the Federal Home Loan Bank were 4.0% of assets against a median of 0.2%. Cash was 2.5% of assets, well below the median of 6.2%, though uninsured deposits were only 4.0% of deposits against a median of 24.8%. Deposits grew 14.6% over the past four quarters, well above the median of 4.2%.

Credit quality was weaker than typical but not severe: loans 90 or more days past due or not accruing interest were 1.2% of loans against a median of 0.5%, and the Texas ratio (troubled assets against capital plus reserves) was 9.7% against a median of 2.9%. Profitability was a strength, with return on assets of 1.5% against a median of 1.2% and return on equity of 22.1% against a median of 11.6%.

## Understanding the score

For the quarter ending 2026-06-30, the bank ranked 17 of 4,313 banks, in the 99.6th percentile on a scale from 0 to 100 where higher means riskier. Its raw model score was 0.4318, and it was flagged on the watchlist, which covers the top 2% of banks.

Five features pushed the score up the most: losses on bonds available for sale at 27.4% of equity, brokered deposits at 24.1% of deposits, the efficiency ratio (operating costs as a share of revenue) at 53.5%, interest expense at 2.7% of assets, and deposit growth of 14.6%. Their contributions were +1.634, +1.019, +0.558, +0.329 and +0.100 respectively.

Five features pulled the score down the most: the Texas ratio at 9.7%, the Tier 1 risk-based capital ratio (core capital against risk-weighted assets; no value shown), return on equity at 22.1%, loans 90 or more days past due or not accruing at 1.2% of loans, and nonaccrual assets and foreclosed property at 0.7% of assets. Their contributions were -0.868, -0.562, -0.454, -0.295 and -0.277 respectively.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 64 | 4,589 | ▲ watchlist |
| 2024-12-31 | 83 | 4,560 | ▲ watchlist |
| 2025-03-31 | 80 | 4,536 | ▲ watchlist |
| 2025-06-30 | 19 | 4,494 | ▲ watchlist |
| 2025-09-30 | 24 | 4,452 | ▲ watchlist |
| 2025-12-31 | 52 | 4,411 | ▲ watchlist |
| 2026-03-31 | 20 | 4,353 | ▲ watchlist |
| 2026-06-30 | 17 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight, this is an open watchlist case: the bank was flagged, and our data does not show any later outcome for it. The fact sheet contains no data from after the as-of quarter, so there is nothing yet to confirm or contradict the flag. A watchlist flag marks a bank whose figures resemble those of past troubled banks; it is not a finding that anything has gone wrong.

## What happened next

Looking at hindsight data, none is available yet for this bank beyond the as-of quarter. We therefore cannot report later ranks, later watchlist flags, or whether the bank has kept filing its regular reports. Those details will appear as newer quarters are added to the data.

## Sources

- F1 · Bank name · n/a · First State Bank Of Dequeen · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · AR · data/raw/financials: STALP
- F5 · Model score · 2026-06-30 · 0.4318 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 17 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.6% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 9.7% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F37 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · 22.1% · data/features/fct_bank_features.parquet: return_on_equity
- F38 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F43 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 2.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F44 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 24.1% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 27.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F63 · Bank: securities as a share of assets · 2026-06-30 · 37.8% · data/features/fct_bank_features.parquet: securities_to_assets
- F64 · National median: securities as a share of assets · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F69 · Bank: deposit growth over the past four quarters · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F70 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F71 · Driver up #1: losses on bonds available for sale, as a share of equity, value 27.4%; contribution to the score · 2026-06-30 · +1.634 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F72 · Driver up #2: brokered deposits as a share of deposits, value 24.1%; contribution to the score · 2026-06-30 · +1.019 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F73 · Driver up #3: the efficiency ratio (operating costs as a share of revenue), value 53.5%; contribution to the score · 2026-06-30 · +0.558 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F74 · Driver up #4: annualized interest expense as a share of assets, value 2.7%; contribution to the score · 2026-06-30 · +0.329 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F75 · Driver up #5: deposit growth over the past four quarters, value 14.6%; contribution to the score · 2026-06-30 · +0.100 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F76 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 9.7%; contribution to the score · 2026-06-30 · -0.868 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver down #2: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.562 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F78 · Driver down #3: return on equity (profit as a share of equity), value 22.1%; contribution to the score · 2026-06-30 · -0.454 · data/analyst/scores.parquet: feature return_on_equity contribution
- F79 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 1.2%; contribution to the score · 2026-06-30 · -0.295 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F80 · Driver down #5: nonaccrual assets and foreclosed property, as a share of assets, value 0.7%; contribution to the score · 2026-06-30 · -0.277 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
