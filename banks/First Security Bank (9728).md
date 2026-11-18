---
cert: 9728
name: "First Security Bank"
as_of: 2026-06-30
rank: 7
n_banks: 4313
percentile: 99.86088569441223
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:07:46"
writer_model: "claude-opus-5-5"
checked: true
---

# First Security Bank (cert 9728)

*Outcome not yet known.*

## Summary

First Security Bank, a Minnesota bank with $161.7 million in total assets, ranked 7 out of 4,313 banks nationally on Canary's risk score as of 2026-06-30. That places it in the 99.9th percentile, where higher means riskier, and it is flagged on Canary's watchlist. Its profile combines thinner capital than most banks, more troubled loans, and a heavy reliance on less stable funding sources.

## Warning signs in the data

Capital, the cushion a bank has to absorb losses, is thinner than at a typical bank: equity was 7.0% of assets against a national median of 10.6%. The leverage ratio, core capital as a share of average assets, was 7.9% versus a median of 11.0%. The Tier 1 risk-based capital ratio was 10.8% against a median of 14.6%, and the total risk-based capital ratio was 12.1% against 15.8%.

Credit quality is weaker than average: loans 90 or more days past due or no longer earning interest were 2.6% of loans, well above the median of 0.5%. The Texas ratio, which compares troubled assets with capital plus reserves, was 24.5% against a median of 2.9%, and loans 30-89 days past due were 0.7% of assets versus 0.2%. Construction loans, often a riskier category, made up 12.1% of loans compared with a median of 5.3%.

On funding, brokered deposits, money placed through intermediaries that can leave quickly, were 23.9% of deposits while the median bank had 0.0%. Core deposits, the steadier everyday customer money, were 52.2% of assets against a median of 75.5%, and volatile funding was 22.5% of assets versus 9.0%. Loans equaled 98.6% of deposits against a median of 80.2%, and unrealized losses on bonds available for sale were 9.9% of equity compared with a median of 5.6%.

## Understanding the score

As of 2026-06-30, First Security Bank ranked 7 of 4,313 banks, placing it in the 99.9th percentile on a scale of 0 to 100 where higher means riskier. The watchlist covers the top 2% of banks, which was 87 banks that quarter, and this bank was flagged.

The five factors pushing the score up most were brokered deposits at 23.9% of deposits, bond losses on available-for-sale securities at 9.9% of equity, core deposits at 52.2% of assets, the efficiency ratio (operating costs as a share of revenue) at 55.8%, and interest expense at 2.5% of assets. Their contributions to the score were +1.395, +0.965, +0.454, +0.424 and +0.230 respectively.

The five factors pulling the score down most were return on equity at 15.0%, the Tier 1 risk-based capital ratio at 10.8%, return on assets at 1.1%, the total risk-based capital ratio at 12.1%, and loans 30-89 days past due at 0.7% of assets. Their contributions were -0.630, -0.588, -0.288, -0.238 and -0.194 respectively.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 378 | 4,589 |  |
| 2024-12-31 | 427 | 4,560 |  |
| 2025-03-31 | 764 | 4,536 |  |
| 2025-06-30 | 464 | 4,494 |  |
| 2025-09-30 | 300 | 4,452 |  |
| 2025-12-31 | 317 | 4,411 |  |
| 2026-03-31 | 19 | 4,353 | ▲ watchlist |
| 2026-06-30 | 7 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight, this bank is an open watchlist case: it was flagged by the model and the data available to us does not show it leaving the system. The fact sheet contains no later-quarter figures, so there is no hindsight evidence yet to confirm or contradict the flag.

## What happened next

Looking back with hindsight, our data contains no reports for this bank after the as-of quarter. No later ranks, watchlist flags, or closure information are available, so it remains an open case to watch as new quarterly filings arrive.

## Sources

- F1 · Bank name · n/a · First Security Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · MN · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 7 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 10.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 12.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F33 · Bank: construction loans as a share of loans · 2026-06-30 · 12.1% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F34 · National median: construction loans as a share of loans · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 24.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 98.6% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 23.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 52.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 22.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 9.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $161.7 million · data/features/fct_bank_features.parquet: log_total_assets
- F75 · Driver up #1: brokered deposits as a share of deposits, value 23.9%; contribution to the score · 2026-06-30 · +1.395 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 9.9%; contribution to the score · 2026-06-30 · +0.965 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: core deposits as a share of assets, value 52.2%; contribution to the score · 2026-06-30 · +0.454 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F78 · Driver up #4: the efficiency ratio (operating costs as a share of revenue), value 55.8%; contribution to the score · 2026-06-30 · +0.424 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.5%; contribution to the score · 2026-06-30 · +0.230 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: return on equity (profit as a share of equity), value 15.0%; contribution to the score · 2026-06-30 · -0.630 · data/analyst/scores.parquet: feature return_on_equity contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 10.8%; contribution to the score · 2026-06-30 · -0.588 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: return on assets (profit as a share of assets), value 1.1%; contribution to the score · 2026-06-30 · -0.288 · data/analyst/scores.parquet: feature return_on_assets contribution
- F83 · Driver down #4: the total risk-based capital ratio, value 12.1%; contribution to the score · 2026-06-30 · -0.238 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F84 · Driver down #5: loans 30-89 days past due, as a share of assets, value 0.7%; contribution to the score · 2026-06-30 · -0.194 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
