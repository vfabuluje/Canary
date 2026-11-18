---
cert: 1756
name: "Central Bank"
as_of: 2026-06-30
rank: 10
n_banks: 4313
percentile: 99.79132854161836
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:08:01"
writer_model: "claude-opus-5-5"
checked: true
---

# Central Bank (cert 1756)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Central Bank, an Arkansas bank, ranked 10 out of 4,313 FDIC-insured banks on Canary's risk score, placing it in the 99.8th percentile. That ranking puts it on Canary's watchlist, which covers the riskiest 2% of banks. The ranking is driven mostly by heavy reliance on brokered deposits (money placed by middlemen rather than local customers), a high level of troubled loans relative to its capital, and high interest costs, partly offset by solid profits.

## Warning signs in the data

Capital, the cushion that absorbs losses, is thinner than at a typical bank: equity was 9.2% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 9.4% against 11.0%. Its risk-weighted capital ratios were also well below the median, with a Tier 1 ratio of 10.3% against 14.6% and a total ratio of 11.6% against 15.8%.

Credit quality stands out the most: loans 90+ days past due or not accruing interest were 4.8% of loans, far above the national median of 0.5%. Loans 30-89 days past due, an early sign of trouble, were 1.9% of assets against a median of 0.2%. The Texas ratio, which compares troubled assets with capital plus reserves, was 43.2% against a median of 2.9%, and net loan write-offs ran at 0.7% of loans against 0.0%. Commercial real estate loans made up 31.4% of loans, above the median of 23.6%.

On funding, brokered deposits were 39.9% of deposits while the median bank had 0.0%, and core deposits (stable, everyday customer deposits) were only 40.0% of assets against a median of 75.5%. The bank also leaned on Federal Home Loan Bank borrowings at 12.3% of assets against a median of 0.2%, lent out 108.9% of its deposits against a median of 80.2%, and held cash of 3.4% of assets against 6.2%. Bond losses were not a concern: unrealized losses on bonds available for sale were 2.6% of equity, below the median of 5.6%, and losses on bonds held to maturity were -0.0% against 0.0%.

## Understanding the score

Central Bank ranked 10 of 4,313 banks as of 2026-06-30, the 99.8th percentile on a scale of 0 to 100 where higher means riskier. It is flagged on the watchlist, which holds the top 2% of banks and contained 87 banks that quarter.

The five factors pushing the score up most were brokered deposits at 39.9% of deposits, the Texas ratio at 43.2%, interest expense at 3.3% of assets, seriously delinquent or nonaccruing loans at 4.8% of loans, and the efficiency ratio (operating costs as a share of revenue) at 34.5%. The five factors pulling it down most were the Tier 1 risk-based capital ratio at 10.3%, return on equity at 11.8%, construction loans at 7.9% of loans, loan-loss reserves at 1.4% of loans, and return on assets at 1.1%.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 158 | 4,589 |  |
| 2024-12-31 | 292 | 4,560 |  |
| 2025-03-31 | 163 | 4,536 |  |
| 2025-06-30 | 209 | 4,494 |  |
| 2025-09-30 | 87 | 4,452 | ▲ watchlist |
| 2025-12-31 | 55 | 4,411 | ▲ watchlist |
| 2026-03-31 | 18 | 4,353 | ▲ watchlist |
| 2026-06-30 | 10 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight terms, this bank remains an open watchlist case: the fact sheet contains no data from after the as-of quarter, so there is no later outcome to report yet. It is on the watchlist because of its standing in the latest available quarter, not because of anything observed afterward.

## What happened next

Looking back with hindsight, there is nothing yet to report: our data includes no ranks, flags or filings for this bank after the as-of quarter. Whether it keeps reporting, and how its rank moves, will only be known once later quarters are published.

## Sources

- F1 · Bank name · n/a · Central Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · AR · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 10 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 9.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 9.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 10.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 31.4% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 43.2% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 108.9% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 39.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 40.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 12.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · -0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 39.9%; contribution to the score · 2026-06-30 · +0.785 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 43.2%; contribution to the score · 2026-06-30 · +0.743 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: annualized interest expense as a share of assets, value 3.3%; contribution to the score · 2026-06-30 · +0.581 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 4.8%; contribution to the score · 2026-06-30 · +0.324 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the efficiency ratio (operating costs as a share of revenue), value 34.5%; contribution to the score · 2026-06-30 · +0.324 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 10.3%; contribution to the score · 2026-06-30 · -0.658 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 11.8%; contribution to the score · 2026-06-30 · -0.624 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: construction loans as a share of loans, value 7.9%; contribution to the score · 2026-06-30 · -0.414 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: loan-loss reserves as a share of loans, value 1.4%; contribution to the score · 2026-06-30 · -0.292 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F84 · Driver down #5: return on assets (profit as a share of assets), value 1.1%; contribution to the score · 2026-06-30 · -0.281 · data/analyst/scores.parquet: feature return_on_assets contribution
