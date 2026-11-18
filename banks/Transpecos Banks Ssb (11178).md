---
cert: 11178
name: "Transpecos Banks Ssb"
as_of: 2026-06-30
rank: 6
n_banks: 4313
percentile: 99.8840714120102
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:07:45"
writer_model: "claude-opus-5-5"
checked: true
---

# Transpecos Banks Ssb (cert 11178)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Transpecos Banks Ssb, a Texas bank with $972.1 million in total assets, ranked 6 out of 4,313 banks on Canary's risk score, placing it in the 99.9th percentile. That puts it on Canary's watchlist, which covers the riskiest 2% of banks. The main reasons are a high level of loans not being repaid, thin capital compared with peers, losses on the bottom line, and heavy reliance on brokered deposits, meaning money placed through middlemen rather than gathered from local customers.

## Warning signs in the data

Capital, the bank's own money that absorbs losses, was well below typical levels: equity was 6.7% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 6.7% against 11.0%. Its risk-based capital ratios, which weigh assets by how risky they are, were also lower than the median, with a Tier 1 ratio of 9.7% against 14.6% and a total ratio of 10.7% against 15.8%.

Credit quality was the weakest area: loans 90+ days past due or no longer earning interest made up 8.1% of loans, far above the national median of 0.5%. Nonaccrual assets and foreclosed property were 2.7% of assets against a median of 0.3%, and loans 30-89 days past due were 0.8% of assets against 0.2%. The Texas ratio, which compares troubled assets with the capital and reserves available to cover them, was 74.8%, very far above the median of 2.9%, while loan-loss reserves were 1.0% of loans, slightly below the median of 1.2%. The bank was also losing money, with a return on assets of -1.6% against a median of 1.2% and a return on equity of -22.6% against 11.6%, and its operating costs ran at 146.4% of revenue against a median of 62.1%.

On funding, brokered deposits were 27.5% of deposits against a national median of 0.0%, uninsured deposits (balances above the government insurance limit) were 39.8% against 24.8%, and interest expense was 2.4% of assets against 1.6%. On the steadier side, cash was 14.1% of assets against a median of 6.2%, and unrealized losses on bonds available for sale were 2.0% of equity, below the median of 5.6%.

## Understanding the score

As of 2026-06-30, the bank ranked 6 out of 4,313 banks, in the 99.9th percentile on a scale of 0 to 100 where higher means riskier, with a model score of 0.7761. It was flagged as one of 87 banks on the watchlist that quarter, the group making up the top 2% of scores.

The five factors pushing the score up most were seriously late or non-earning loans at 8.1% of loans, adding +0.900, and the Texas ratio at 74.8%, adding +0.678. Next came return on equity of -22.6%, adding +0.608, brokered deposits at 27.5% of deposits, adding +0.587, and interest expense at 2.4% of assets, adding +0.394.

The five factors pulling the score down most were the Tier 1 risk-based capital ratio of 9.7%, contributing -0.777, and construction loans at 3.1% of loans, contributing -0.373. Total assets of $972.1 million contributed -0.212, loan-loss reserves at 1.0% of loans contributed -0.191, and volatile funding at 3.4% of assets contributed -0.180.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 55 | 4,589 | ▲ watchlist |
| 2024-12-31 | 12 | 4,560 | ▲ watchlist |
| 2025-03-31 | 31 | 4,536 | ▲ watchlist |
| 2025-06-30 | 111 | 4,494 |  |
| 2025-09-30 | 103 | 4,452 |  |
| 2025-12-31 | 35 | 4,411 | ▲ watchlist |
| 2026-03-31 | 8 | 4,353 | ▲ watchlist |
| 2026-06-30 | 6 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight: this fact sheet contains no data from after the as-of quarter, so there is no later outcome to report. The bank appears here because it was flagged on the watchlist and, based on the information available, remains open, so its story is still unfolding.

## What happened next

In hindsight: the fact sheet includes no later ranks, watchlist flags, or reporting records for this bank beyond the as-of quarter. Whether it keeps reporting, or stops because it merged or closed, cannot yet be determined from our data.

## Sources

- F1 · Bank name · n/a · Transpecos Banks Ssb · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · TX · data/raw/financials: STALP
- F5 · Model score · 2026-06-30 · 0.7761 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 6 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 9.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 10.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 8.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 2.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 1.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 74.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -1.6% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -22.6% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 146.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 2.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 39.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 27.5% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 14.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $972.1 million · data/features/fct_bank_features.parquet: log_total_assets
- F75 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 8.1%; contribution to the score · 2026-06-30 · +0.900 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 74.8%; contribution to the score · 2026-06-30 · +0.678 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: return on equity (profit as a share of equity), value -22.6%; contribution to the score · 2026-06-30 · +0.608 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver up #4: brokered deposits as a share of deposits, value 27.5%; contribution to the score · 2026-06-30 · +0.587 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2026-06-30 · +0.394 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 9.7%; contribution to the score · 2026-06-30 · -0.777 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: construction loans as a share of loans, value 3.1%; contribution to the score · 2026-06-30 · -0.373 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: total assets, value $972.1 million; contribution to the score · 2026-06-30 · -0.212 · data/analyst/scores.parquet: feature log_total_assets contribution
- F83 · Driver down #4: loan-loss reserves as a share of loans, value 1.0%; contribution to the score · 2026-06-30 · -0.191 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F84 · Driver down #5: volatile funding as a share of assets, value 3.4%; contribution to the score · 2026-06-30 · -0.180 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
