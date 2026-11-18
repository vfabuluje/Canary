---
cert: 28989
name: "Wcf Financial Bank"
as_of: 2026-06-30
rank: 16
n_banks: 4313
percentile: 99.6522142360306
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:08:37"
writer_model: "claude-opus-5-5"
checked: true
---

# Wcf Financial Bank (cert 28989)

*Outcome not yet known.*

## Summary

Wcf Financial Bank, based in Iowa, ranked 16 out of 4,313 banks nationally on Canary's risk score as of 2026-06-30, placing it in the 99.7th percentile, where higher means riskier. That rank put it on the watchlist, which covers the top 2% of banks by score. Its capital cushion was thinner than the typical bank's, its share of troubled loans was well above the national median, and it leaned more heavily than most on borrowed and brokered funding.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was below the national median on every measure: equity was 7.9% of assets against a median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.3% against 11.0%. The Tier 1 risk-based capital ratio, which weighs capital against the riskiness of assets, was 11.5% versus a median of 14.6%, and the total risk-based capital ratio was 12.7% versus 15.8%.

Credit quality stood out most: loans 90 or more days past due or no longer earning interest were 5.1% of loans, far above the median of 0.5%. Nonaccrual assets and foreclosed property were 4.0% of assets against a median of 0.3%, and loans 30-89 days late, an early sign of trouble, were 3.0% of assets against 0.2%. The Texas ratio, which compares troubled assets with capital plus reserves, was 45.9%, versus a national median of 2.9%. Profits were thin, with return on assets of 0.1% against a median of 1.2%, and operating costs ate 95.3% of revenue against a median of 62.1%.

On funding, brokered deposits (money placed through middlemen, which can leave quickly) were 15.2% of deposits versus a median of 0.0%, and Federal Home Loan Bank borrowings were 13.4% of assets versus 0.2%. Volatile funding was 30.6% of assets against a median of 9.0%, while stable core deposits were 48.4% of assets against 75.5%, and loans equaled 100.3% of deposits against 80.2%. Unrealized losses on bonds available for sale equaled 6.9% of equity, somewhat above the median of 5.6%.

## Understanding the score

As of 2026-06-30 the bank ranked 16 of 4,313 banks, in the 99.7th percentile on a scale of 0 to 100 where higher is riskier. It was flagged for the watchlist, the top 2% of banks by score, which held 87 banks that quarter.

The five factors pushing the score up most were the Texas ratio at 45.9% (+0.781), unrealized losses on bonds available for sale at 6.9% of equity (+0.641), loans 30-89 days past due at 3.0% of assets (+0.481), brokered deposits at 15.2% of deposits (+0.423), and interest expense at 2.7% of assets (+0.387).

The five factors pulling the score down most were the Tier 1 risk-based capital ratio at 11.5% (-1.448), the total risk-based capital ratio at 12.7% (-0.371), the efficiency ratio at 95.3% (-0.303), return on equity at 1.3% (-0.272), and construction loans at 5.9% of loans (-0.271).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,377 | 4,589 |  |
| 2024-12-31 | 1,386 | 4,560 |  |
| 2025-03-31 | 799 | 4,536 |  |
| 2025-06-30 | 678 | 4,494 |  |
| 2025-09-30 | 128 | 4,452 |  |
| 2025-12-31 | 18 | 4,411 | ▲ watchlist |
| 2026-03-31 | 12 | 4,353 | ▲ watchlist |
| 2026-06-30 | 16 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

This section is written with hindsight, but the fact sheet contains no data from after the as-of quarter. The bank is recorded as an open bank on the watchlist, so there is no later outcome yet to explain. Its place on the watchlist rests on the warning signs described above, not on any later event.

## What happened next

Looking with hindsight, the fact sheet provides no later ranks, flags or reporting status for this bank. We therefore cannot say how its rank moved after the as-of quarter or whether it kept reporting; it remains an open bank on the watchlist in our data.

## Sources

- F1 · Bank name · n/a · Wcf Financial Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 16 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 11.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 12.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 5.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 45.9% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 95.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 100.3% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 15.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 48.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 13.4% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 30.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 45.9%; contribution to the score · 2026-06-30 · +0.781 · data/analyst/scores.parquet: feature texas_ratio contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 6.9%; contribution to the score · 2026-06-30 · +0.641 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: loans 30-89 days past due, as a share of assets, value 3.0%; contribution to the score · 2026-06-30 · +0.481 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F78 · Driver up #4: brokered deposits as a share of deposits, value 15.2%; contribution to the score · 2026-06-30 · +0.423 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.7%; contribution to the score · 2026-06-30 · +0.387 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 11.5%; contribution to the score · 2026-06-30 · -1.448 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: the total risk-based capital ratio, value 12.7%; contribution to the score · 2026-06-30 · -0.371 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F82 · Driver down #3: the efficiency ratio (operating costs as a share of revenue), value 95.3%; contribution to the score · 2026-06-30 · -0.303 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F83 · Driver down #4: return on equity (profit as a share of equity), value 1.3%; contribution to the score · 2026-06-30 · -0.272 · data/analyst/scores.parquet: feature return_on_equity contribution
- F84 · Driver down #5: construction loans as a share of loans, value 5.9%; contribution to the score · 2026-06-30 · -0.271 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
