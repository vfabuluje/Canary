---
cert: 58088
name: "Southpoint Bank"
as_of: 2026-06-30
rank: 4
n_banks: 4313
percentile: 99.93044284720612
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:07:23"
writer_model: "claude-opus-5-5"
checked: true
---

# Southpoint Bank (cert 58088)

*Outcome not yet known.*

## Summary

Southpoint Bank, an Alabama bank, ranked 4 out of 4,313 banks nationally on Canary's risk score as of 2026-06-30, which places it in the 99.9th percentile. That ranking puts it on Canary's watchlist, the small group of highest-scoring banks. Its figures show thin capital, heavy loan losses, a loss-making quarter and a reliance on brokered deposits (money placed through middlemen rather than gathered from local customers).

## Warning signs in the data

Capital, the bank's own cushion against losses, is thin: equity was 7.7% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 6.9% against 11.0%. Its Tier 1 risk-based capital ratio was 8.9% and its total risk-based capital ratio was 10.2%, both well below the medians of 14.6% and 15.8%.

Credit quality is weak: loans 90+ days past due or not accruing interest were 3.5% of loans versus a median of 0.5%, and annualized write-offs (loans written off as lost, net of recoveries) were 4.5% of loans versus 0.0%. The Texas ratio, which compares troubled assets with capital plus reserves, was 32.5% against a median of 2.9%, and return on assets was -1.7% against 1.2%, meaning the bank was losing money.

On funding, brokered deposits made up 23.4% of deposits while the median bank had 0.0%, and core deposits (stable customer deposits) were 55.0% of assets against 75.5%. Deposits shrank by -18.8% over the past four quarters, while the median bank grew 4.2%; on the other hand, cash was a sizable 13.2% of assets versus 6.2%. Unrealized losses on bonds available for sale equaled 8.7% of equity, above the median of 5.6%.

## Understanding the score

Southpoint Bank ranked 4 of 4,313 banks as of 2026-06-30, the 99.9th percentile on a scale of 0 to 100 where higher means riskier. The watchlist covers the top 2% of banks, which was 87 banks that quarter, and this bank was flagged.

Five factors pushed the score up most: return on equity of -22.1% (contribution +0.828), bond losses of 8.7% of equity (+0.762), and brokered deposits at 23.4% of deposits (+0.511). The other two were a Tier 1 risk-based capital ratio of 8.9% (+0.419) and interest expense of 2.8% of assets (+0.376).

Five factors pulled the score down: construction loans at 10.0% of loans (-0.301), loans 30-89 days past due at 0.7% of assets (-0.233), and a Texas ratio of 32.5% (-0.231). The rest were total assets of $1.4 billion (-0.178) and commercial real estate loans at 38.0% of loans (-0.165).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 31 | 4,589 | ▲ watchlist |
| 2024-12-31 | 7 | 4,560 | ▲ watchlist |
| 2025-03-31 | 18 | 4,536 | ▲ watchlist |
| 2025-06-30 | 13 | 4,494 | ▲ watchlist |
| 2025-09-30 | 7 | 4,452 | ▲ watchlist |
| 2025-12-31 | 6 | 4,411 | ▲ watchlist |
| 2026-03-31 | 6 | 4,353 | ▲ watchlist |
| 2026-06-30 | 4 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

Hindsight view: this bank's outcome case is that it remains open and on the watchlist. The fact sheet holds no data from after the as-of quarter, so there is no later evidence yet to confirm or contradict the model's warning. Its high ranking rests on the losses, thin capital and brokered funding described above, all measured at the as-of date.

## What happened next

Hindsight view: the bank is treated as open and still on the watchlist. Our data for this memo contains no later ranks, flags or reporting history beyond the as-of quarter, so we cannot yet say how its position changed or whether it stopped reporting.

## Sources

- F1 · Bank name · n/a · Southpoint Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · AL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 4 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 3.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 32.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -1.7% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 23.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 55.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 13.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 8.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -18.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -22.1%; contribution to the score · 2026-06-30 · +0.828 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 8.7%; contribution to the score · 2026-06-30 · +0.762 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: brokered deposits as a share of deposits, value 23.4%; contribution to the score · 2026-06-30 · +0.511 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F78 · Driver up #4: the Tier 1 risk-based capital ratio, value 8.9%; contribution to the score · 2026-06-30 · +0.419 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.8%; contribution to the score · 2026-06-30 · +0.376 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: construction loans as a share of loans, value 10.0%; contribution to the score · 2026-06-30 · -0.301 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F81 · Driver down #2: loans 30-89 days past due, as a share of assets, value 0.7%; contribution to the score · 2026-06-30 · -0.233 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 32.5%; contribution to the score · 2026-06-30 · -0.231 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: total assets, value $1.4 billion; contribution to the score · 2026-06-30 · -0.178 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: commercial real estate loans as a share of loans, value 38.0%; contribution to the score · 2026-06-30 · -0.165 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
