---
cert: 17438
name: "First Nb Of America"
as_of: 2026-06-30
rank: 76
n_banks: 4313
percentile: 98.26107118015302
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:09:12"
writer_model: "claude-opus-5-5"
checked: true
---

# First Nb Of America (cert 17438)

*Outcome not yet known.*

## Summary

First Nb Of America, a Michigan bank, ranked 76 out of 4,313 FDIC-insured banks on Canary's risk score as of June 30, 2026, with a percentile of 98.3%, where higher means riskier. That rank put it on Canary's watchlist, the 2% of banks with the highest scores. The main concerns in the data are heavy reliance on borrowed and brokered money (deposits gathered through middlemen) and above-median problem loans, while strong profits and solid risk-based capital partly offset them.

## Warning signs in the data

Capital, the bank's own cushion against losses, is mixed: equity was 8.1% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.1% against a median of 11.0%. Measured against risk-weighted assets, capital looks stronger, with a Tier 1 risk-based capital ratio of 15.3% against a median of 14.6% and a total risk-based capital ratio of 16.5% against 15.8%.

Credit quality is weaker than typical: loans 90 or more days past due or no longer earning interest were 1.9% of loans, well above the median of 0.5%, and loans 30-89 days past due were 0.8% of assets against a median of 0.2%. Nonaccrual assets and foreclosed property were 1.9% of assets against a median of 0.3%, and the Texas ratio (troubled assets against capital plus reserves) was 20.6%, far above the median of 2.9%. Loan-loss reserves, money set aside for expected bad loans, were 1.1% of loans, close to the median of 1.2%.

Funding is the most unusual area: brokered deposits made up 43.4% of deposits against a median of 0.0%, and Federal Home Loan Bank borrowings (loans from a government-sponsored lender to banks) were 34.2% of assets against a median of 0.2%. Core deposits, the stable everyday deposits most banks rely on, were only 26.0% of assets against a median of 75.5%, and loans were 160.1% of deposits against a median of 80.2%. This costlier funding shows in interest expense of 3.5% of assets, well above the median of 1.6%. Bond losses are not a concern: unrealized losses on bonds available for sale were 0.1% of equity against a median of 5.6%, partly because securities were just 1.2% of assets against a median of 17.6%.

## Understanding the score

As of June 30, 2026, the bank ranked 76 of 4,313 banks, with a percentile of 98.3% on a scale of 0 to 100 where higher means riskier. It was flagged as one of the 87 banks on the watchlist that quarter, which covers the 2% of banks with the highest scores.

Five features pushed the score up the most: brokered deposits at 43.4% of deposits, interest expense at 3.5% of assets, securities at 1.2% of assets, commercial real estate loans at 1.1% of loans, and an efficiency ratio (operating costs as a share of revenue) of 26.6%. Their contributions to the score were +1.179, +0.570, +0.358, +0.303 and +0.191 respectively.

Five features pulled the score down the most: a Tier 1 risk-based capital ratio of 15.3%, return on equity of 34.7%, return on assets of 2.8%, a total risk-based capital ratio of 16.5%, and a Texas ratio of 20.6%. Their contributions were -0.967, -0.796, -0.549, -0.475 and -0.311 respectively.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 39 | 4,589 | ▲ watchlist |
| 2024-12-31 | 57 | 4,560 | ▲ watchlist |
| 2025-03-31 | 141 | 4,536 |  |
| 2025-06-30 | 139 | 4,494 |  |
| 2025-09-30 | 121 | 4,452 |  |
| 2025-12-31 | 116 | 4,411 |  |
| 2026-03-31 | 76 | 4,353 | ▲ watchlist |
| 2026-06-30 | 76 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight terms, this bank is an open watchlist case: it was flagged by the model and our data does not show it leaving the system. The fact sheet contains no data from after the as-of quarter, so there is no later evidence yet to confirm or contradict the flag. The reasons for the flag are the ones described above, chiefly its reliance on brokered deposits and costly borrowed funding.

## What happened next

Looking at hindsight data, there is nothing to report yet: the fact sheet includes no ranks, flags or filings from any quarter after the as-of quarter. Based on the data available, the bank remains open and on the watchlist, and later quarters will show whether its rank changes.

## Sources

- F1 · Bank name · n/a · First Nb Of America · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · MI · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 76 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 98.3% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 15.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 16.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 20.6% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 3.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 160.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 43.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 26.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 34.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 43.4%; contribution to the score · 2026-06-30 · +1.179 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: annualized interest expense as a share of assets, value 3.5%; contribution to the score · 2026-06-30 · +0.570 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F77 · Driver up #3: securities as a share of assets, value 1.2%; contribution to the score · 2026-06-30 · +0.358 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F78 · Driver up #4: commercial real estate loans as a share of loans, value 1.1%; contribution to the score · 2026-06-30 · +0.303 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F79 · Driver up #5: the efficiency ratio (operating costs as a share of revenue), value 26.6%; contribution to the score · 2026-06-30 · +0.191 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 15.3%; contribution to the score · 2026-06-30 · -0.967 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 34.7%; contribution to the score · 2026-06-30 · -0.796 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: return on assets (profit as a share of assets), value 2.8%; contribution to the score · 2026-06-30 · -0.549 · data/analyst/scores.parquet: feature return_on_assets contribution
- F83 · Driver down #4: the total risk-based capital ratio, value 16.5%; contribution to the score · 2026-06-30 · -0.475 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F84 · Driver down #5: the Texas ratio (troubled assets against capital plus reserves), value 20.6%; contribution to the score · 2026-06-30 · -0.311 · data/analyst/scores.parquet: feature texas_ratio contribution
