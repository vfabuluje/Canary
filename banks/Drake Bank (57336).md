---
cert: 57336
name: "Drake Bank"
as_of: 2026-06-30
rank: 15
n_banks: 4313
percentile: 99.67539995362856
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:08:37"
writer_model: "claude-opus-5-5"
checked: true
---

# Drake Bank (cert 57336)

*Outcome not yet known.*

## Summary

Drake Bank, a Minnesota bank, ranked 15 out of 4,313 FDIC-insured banks on Canary's risk score for the quarter ending 2026-06-30, placing it in the 99.7th percentile. That put it on Canary's watchlist, which covers the riskiest 2% of banks. Its capital cushion was thin, its troubled loans were high, and it was losing money, all compared with the typical US bank.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was well below typical levels: equity was 7.0% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 7.3% against 11.0%. The Tier 1 risk-based capital ratio, which weighs capital against how risky the assets are, was 9.8% against a median of 14.6%, and the total risk-based capital ratio was 11.1% against 15.8%.

Credit quality was weak: loans 90+ days past due or no longer earning interest were 4.5% of loans, far above the median of 0.5%, and nonaccrual assets plus foreclosed property were 5.4% of assets against 0.3%. The Texas ratio, which compares troubled assets with capital plus reserves, was 57.8%, far above the median of 2.9%. The bank was setting aside money for bad loans at a high rate, with provisions of 2.2% of assets against a median of 0.1%, and it lost money, with return on assets of -1.2% and return on equity of -17.7% versus medians of 1.2% and 11.6%.

On funding, brokered deposits (money placed through middlemen, which can leave quickly) were 20.2% of deposits against a median of 0.0%, and Federal Home Loan Bank borrowings were 6.9% of assets against 0.2%. Deposits shrank by -9.5% over the past four quarters while the median bank grew by 4.2%, and interest expense was 2.6% of assets against 1.6%. Unrealized losses on bonds available for sale equaled 7.9% of equity, above the median of 5.6%.

## Understanding the score

Drake Bank ranked 15 out of 4,313 banks for the quarter ending 2026-06-30, which is the 99.7th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, one of 87 banks that quarter, a list that holds the top 2% of scores.

The five factors that pushed the score up most were the Texas ratio at 57.8%, losses on bonds available for sale at 7.9% of equity, interest expense at 2.6% of assets, brokered deposits at 20.2% of deposits, and return on equity at -17.7%. The five factors that pulled the score down most were the Tier 1 risk-based capital ratio at 9.8%, loans 30-89 days past due at 0.0% of assets, construction loans at 5.9% of loans, total assets of $247.4 million, and volatile funding at 5.7% of assets.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,960 | 4,589 |  |
| 2024-12-31 | 895 | 4,560 |  |
| 2025-03-31 | 154 | 4,536 |  |
| 2025-06-30 | 357 | 4,494 |  |
| 2025-09-30 | 80 | 4,452 | ▲ watchlist |
| 2025-12-31 | 83 | 4,411 | ▲ watchlist |
| 2026-03-31 | 14 | 4,353 | ▲ watchlist |
| 2026-06-30 | 15 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

With hindsight: this bank falls in the case of a bank that remains open while on the watchlist. The fact sheet contains no data from after the as-of quarter of 2026-06-30, so there are no later figures to explain how its position developed.

## What happened next

With hindsight: the fact sheet holds no ranks, watchlist flags or reporting records for any quarter after 2026-06-30. Because of that, this memo cannot say how the bank's rank moved later or whether it kept filing reports.

## Sources

- F1 · Bank name · n/a · Drake Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · MN · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 15 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 7.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 11.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 5.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 57.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -17.7% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 20.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -9.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 57.8%; contribution to the score · 2026-06-30 · +0.781 · data/analyst/scores.parquet: feature texas_ratio contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 7.9%; contribution to the score · 2026-06-30 · +0.580 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: annualized interest expense as a share of assets, value 2.6%; contribution to the score · 2026-06-30 · +0.444 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F78 · Driver up #4: brokered deposits as a share of deposits, value 20.2%; contribution to the score · 2026-06-30 · +0.320 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F79 · Driver up #5: return on equity (profit as a share of equity), value -17.7%; contribution to the score · 2026-06-30 · +0.212 · data/analyst/scores.parquet: feature return_on_equity contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 9.8%; contribution to the score · 2026-06-30 · -0.824 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: loans 30-89 days past due, as a share of assets, value 0.0%; contribution to the score · 2026-06-30 · -0.433 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F82 · Driver down #3: construction loans as a share of loans, value 5.9%; contribution to the score · 2026-06-30 · -0.380 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: total assets, value $247.4 million; contribution to the score · 2026-06-30 · -0.208 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: volatile funding as a share of assets, value 5.7%; contribution to the score · 2026-06-30 · -0.151 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
