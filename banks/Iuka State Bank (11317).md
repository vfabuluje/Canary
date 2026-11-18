---
cert: 11317
name: "Iuka State Bank"
as_of: 2026-06-30
rank: 14
n_banks: 4313
percentile: 99.69858567122652
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:08:37"
writer_model: "claude-opus-5-5"
checked: true
---

# Iuka State Bank (cert 11317)

*Outcome not yet known.*

## Summary

Iuka State Bank, an Illinois bank with $133.0 million in total assets, ranked 14 out of 4,313 banks nationally on Canary's risk score for the quarter ending 2026-06-30. That places it in the 99.7th percentile, where higher means riskier, and it is flagged on Canary's watchlist. The ranking is driven mainly by a large share of troubled loans and a heavy reliance on brokered deposits, which are funds placed through middlemen rather than gathered from local customers.

## Warning signs in the data

Credit quality is the clearest weak spot: loans 90 or more days past due or no longer earning interest made up 8.0% of loans, against a national median of 0.5%. Nonaccrual assets and foreclosed property were 6.9% of assets versus a median of 0.3%, and the Texas ratio, which weighs troubled assets against capital plus reserves, stood at 57.1% compared with a median of 2.9%. Annualized loan write-offs, net of recoveries, were 1.8% of loans, while the median bank wrote off 0.0%.

Capital, the owners' cushion against losses, was somewhat thinner than typical: equity was 9.6% of assets versus a median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 10.3% versus 11.0%. Profits were slim, with return on assets of 0.1% against a median of 1.2%.

On funding, brokered deposits were 20.2% of deposits while the median bank had 0.0%, and core deposits, the steadier everyday accounts, were 63.6% of assets versus a median of 75.5%. Loans equaled 94.1% of deposits, above the 80.2% median. Unrealized losses on bonds available for sale equaled 11.0% of equity, roughly well above the national median of 5.6%.

## Understanding the score

For the quarter ending 2026-06-30, Iuka State Bank ranked 14 of 4,313 banks, placing it in the 99.7th percentile on a scale of 0 to 100 where higher means riskier. Canary's watchlist covers the top 2% of banks by score, which was 87 banks that quarter, and this bank is flagged on it.

The five factors pushing the score up most were the Texas ratio at 57.1%, loans 90 or more days past due or not accruing interest at 8.0% of loans, losses on bonds available for sale at 11.0% of equity, brokered deposits at 20.2% of deposits, and the annualized provision for loan losses (money set aside for expected bad loans) at 1.2% of assets.

The five factors pulling the score down most were the Tier 1 risk-based capital ratio (core capital measured against riskier assets, value not shown in our data), return on equity at 0.8%, construction loans at 1.7% of loans, the leverage ratio at 10.3%, and volatile funding at 11.8% of assets.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 338 | 4,589 |  |
| 2024-12-31 | 212 | 4,560 |  |
| 2025-03-31 | 37 | 4,536 | ▲ watchlist |
| 2025-06-30 | 34 | 4,494 | ▲ watchlist |
| 2025-09-30 | 382 | 4,452 |  |
| 2025-12-31 | 19 | 4,411 | ▲ watchlist |
| 2026-03-31 | 16 | 4,353 | ▲ watchlist |
| 2026-06-30 | 14 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight: the bank remains open and on the watchlist, and our data does not yet include any later quarters that would confirm or overturn the warning. Its placement rests on the figures described above, chiefly troubled loans and reliance on brokered deposits, and the outcome is still unknown.

## What happened next

In hindsight: there is no data yet after the as-of quarter, so we have no later ranks or flags to report. The bank was still reporting as of its latest filing, and future quarters will show whether its rank improves or it stays on the watchlist.

## Sources

- F1 · Bank name · n/a · Iuka State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 14 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 9.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F26 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 57.1% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: loans as a share of deposits · 2026-06-30 · 94.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F46 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 20.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F51 · Bank: core deposits as a share of assets · 2026-06-30 · 63.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F52 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: total assets · 2026-06-30 · $133.0 million · data/features/fct_bank_features.parquet: log_total_assets
- F71 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 57.1%; contribution to the score · 2026-06-30 · +0.900 · data/analyst/scores.parquet: feature texas_ratio contribution
- F72 · Driver up #2: loans 90+ days past due or not accruing interest, as a share of loans, value 8.0%; contribution to the score · 2026-06-30 · +0.844 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F73 · Driver up #3: losses on bonds available for sale, as a share of equity, value 11.0%; contribution to the score · 2026-06-30 · +0.589 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F74 · Driver up #4: brokered deposits as a share of deposits, value 20.2%; contribution to the score · 2026-06-30 · +0.349 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F75 · Driver up #5: annualized provision for loan losses as a share of assets, value 1.2%; contribution to the score · 2026-06-30 · +0.145 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.733 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: return on equity (profit as a share of equity), value 0.8%; contribution to the score · 2026-06-30 · -0.369 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver down #3: construction loans as a share of loans, value 1.7%; contribution to the score · 2026-06-30 · -0.310 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F79 · Driver down #4: the leverage ratio (core capital as a share of average assets), value 10.3%; contribution to the score · 2026-06-30 · -0.272 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #5: volatile funding as a share of assets, value 11.8%; contribution to the score · 2026-06-30 · -0.178 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
