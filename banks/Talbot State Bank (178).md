---
cert: 178
name: "Talbot State Bank"
as_of: 2026-06-30
rank: 22
n_banks: 4313
percentile: 99.51309993044285
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:08:55"
writer_model: "claude-opus-5-5"
checked: true
---

# Talbot State Bank (cert 178)

*Outcome not yet known.*

## Summary

Talbot State Bank, a Georgia bank, ranked 22 out of 4,313 banks in Canary's national ranking for Q2 2026, placing it in the 99.5th percentile, where higher means riskier. That ranking put it on the watchlist, which covers the top 2% of banks, or 87 banks that quarter. Its profile pairs thin capital against total assets, a high level of late loan payments and heavy reliance on less stable funding with large paper losses on its bond holdings.

## Warning signs in the data

Capital, the cushion a bank has to absorb losses, looks thin against total assets: equity was 4.5% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 7.8% against a median of 11.0%. Measured against risk-weighted assets, where safer assets count for less, capital looks stronger: the Tier 1 risk-based capital ratio was 16.8% versus a median of 14.6%, and the total risk-based capital ratio was 17.6% versus 15.8%. The bank also lost money, with a return on assets of -0.9% against a median of 1.2%, and its efficiency ratio (operating costs as a share of revenue) was 123.7% against a median of 62.1%, meaning costs exceeded revenue.

Credit quality, meaning how well borrowers are repaying, is weak: loans 30-89 days past due equaled 5.2% of assets against a median of 0.2%, and loans 90+ days past due or not accruing interest were 2.3% of loans against a median of 0.5%. Loan-loss reserves, money set aside for bad loans, were 0.6% of loans, about half-way below the median of 1.2%, while the Texas ratio (troubled assets against capital plus reserves) was 30.9% against a median of 2.9%.

On funding, brokered deposits (money placed through middlemen, which can leave quickly) made up 19.0% of deposits against a median of 0.0%, and volatile funding was 26.8% of assets against a median of 9.0%. Federal Home Loan Bank borrowings were 7.7% of assets against a median of 0.2%, and core deposits, the steadiest funding, were 58.8% of assets against a median of 75.5%. Finally, unrealized losses on bonds available for sale equaled 76.0% of equity, far above the national median of 5.6%.

## Understanding the score

In Q2 2026 Talbot State Bank ranked 22 of 4,313 banks, in the 99.5th percentile on a scale of 0 to 100 where higher means riskier, with a model score of 0.2961. It was flagged for the watchlist, which holds the top 2% of banks, 87 banks that quarter.

The five factors pushing the score up most were: losses on bonds available for sale at 76.0% of equity (+1.284), brokered deposits at 19.0% of deposits (+0.935), loans 30-89 days past due at 5.2% of assets (+0.445), commercial real estate loans at 1.6% of loans (+0.171), and interest expense at 2.5% of assets (+0.137).

The five factors pulling the score down most were: the Tier 1 risk-based capital ratio at 16.8% (-1.591), the Texas ratio at 30.9% (-0.505), the total risk-based capital ratio at 17.6% (-0.433), construction loans at 5.9% of loans (-0.257), and nonaccrual assets and foreclosed property at 0.8% of assets (-0.224).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 35 | 4,589 | ▲ watchlist |
| 2024-12-31 | 86 | 4,560 | ▲ watchlist |
| 2025-03-31 | 44 | 4,536 | ▲ watchlist |
| 2025-06-30 | 42 | 4,494 | ▲ watchlist |
| 2025-09-30 | 48 | 4,452 | ▲ watchlist |
| 2025-12-31 | 32 | 4,411 | ▲ watchlist |
| 2026-03-31 | 27 | 4,353 | ▲ watchlist |
| 2026-06-30 | 22 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight, this fact sheet contains no data from after the as-of quarter, so there is no later outcome to report for this bank. The bank remains on the watchlist on the strength of its Q2 2026 rank of 22, driven mainly by large bond losses relative to equity and reliance on brokered deposits.

## What happened next

In hindsight, our data holds no later ranks, flags or filings for this bank beyond the as-of quarter. Its story is still open, and later quarters will show whether its position on the ranking changes.

## Sources

- F1 · Bank name · n/a · Talbot State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · GA · data/raw/financials: STALP
- F5 · Model score · 2026-06-30 · 0.2961 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 22 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.5% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 7.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 16.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 2.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 5.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 30.9% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 123.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 19.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 58.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 7.7% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 26.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 76.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: losses on bonds available for sale, as a share of equity, value 76.0%; contribution to the score · 2026-06-30 · +1.284 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F76 · Driver up #2: brokered deposits as a share of deposits, value 19.0%; contribution to the score · 2026-06-30 · +0.935 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F77 · Driver up #3: loans 30-89 days past due, as a share of assets, value 5.2%; contribution to the score · 2026-06-30 · +0.445 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F78 · Driver up #4: commercial real estate loans as a share of loans, value 1.6%; contribution to the score · 2026-06-30 · +0.171 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.5%; contribution to the score · 2026-06-30 · +0.137 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 16.8%; contribution to the score · 2026-06-30 · -1.591 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 30.9%; contribution to the score · 2026-06-30 · -0.505 · data/analyst/scores.parquet: feature texas_ratio contribution
- F82 · Driver down #3: the total risk-based capital ratio, value 17.6%; contribution to the score · 2026-06-30 · -0.433 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F83 · Driver down #4: construction loans as a share of loans, value 5.9%; contribution to the score · 2026-06-30 · -0.257 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F84 · Driver down #5: nonaccrual assets and foreclosed property, as a share of assets, value 0.8%; contribution to the score · 2026-06-30 · -0.224 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
