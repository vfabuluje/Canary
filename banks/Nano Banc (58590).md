---
cert: 58590
name: "Nano Banc"
as_of: 2026-06-30
rank: 3
n_banks: 4313
percentile: 99.95362856480408
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:07:23"
writer_model: "claude-opus-5-5"
checked: true
---

# Nano Banc (cert 58590)

*Outcome not yet known.*

## Summary

Nano Banc, a California bank, ranked 3 out of 4,313 FDIC-insured banks on Canary's risk score as of 2026-06-30, placing it in the 100.0th percentile, where higher means riskier. That put it on Canary's watchlist, which covers the riskiest 2% of banks. Its figures show thin capital (the owners' cushion that absorbs losses), a very large share of loans that borrowers have stopped paying on time, and a loss for the period.

## Warning signs in the data

Capital was well below typical levels: equity was 5.3% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 5.0% against 11.0%. Its Tier 1 risk-based capital ratio (core capital measured against assets weighted by riskiness) was 7.8% versus a median of 14.6%, and its total risk-based capital ratio was 9.1% versus 15.8%.

Credit quality stood far outside the norm: 25.7% of loans were 90 or more days past due or no longer accruing interest, against a national median of 0.5%. Nonaccrual assets and foreclosed property made up 16.7% of assets versus 0.3%, and loans 30-89 days past due were 5.6% of assets versus 0.2%. The Texas ratio, which compares troubled assets with capital plus loss reserves, was 209.8% against a median of 2.9%, and net loan write-offs ran at 3.3% of loans versus 0.0%. The bank was losing money, with a return on assets of -0.5% compared with a median of 1.2%.

On funding, uninsured deposits (balances above the government insurance limit) were 56.9% of deposits versus a median of 24.8%, and brokered deposits (money placed through third-party brokers) were 22.8% versus 0.0%. The bank was shrinking, with assets down -20.9% and deposits down -14.8% over the past four quarters, while the medians grew 4.5% and 4.2%. On the steadier side, cash was 27.3% of assets versus a median of 6.2%, and unrealized losses on bonds available for sale were 2.4% of equity, below the median of 5.6%, with 0.0% on bonds held to maturity.

## Understanding the score

As of 2026-06-30, Nano Banc ranked 3 out of 4,313 banks, in the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks by score, or 87 banks that quarter.

The five features that pushed the score up most were the Texas ratio at 209.8% (+1.216), loans 90+ days past due or not accruing interest at 25.7% of loans (+0.867), the Tier 1 risk-based capital ratio at 7.8% (+0.575), loans 30-89 days past due at 5.6% of assets (+0.378), and brokered deposits at 22.8% of deposits (+0.360).

The five features that pulled the score down most were return on equity at -10.9% (-0.340), construction loans at 9.8% of loans (-0.328), deposit growth over the past four quarters at -14.8% (-0.169), total assets of $736.2 million (-0.155), and volatile funding at 4.3% of assets (-0.077). These offsets were small next to the upward drivers.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 258 | 4,589 |  |
| 2024-12-31 | 3,759 | 4,560 |  |
| 2025-03-31 | 1,943 | 4,536 |  |
| 2025-06-30 | 122 | 4,494 |  |
| 2025-09-30 | 4 | 4,452 | ▲ watchlist |
| 2025-12-31 | 3 | 4,411 | ▲ watchlist |
| 2026-03-31 | 5 | 4,353 | ▲ watchlist |
| 2026-06-30 | 3 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight, this bank's outcome case is that it remains open and on the watchlist. Our fact sheet contains no data from after the as-of quarter, so this section cannot add later figures to explain that outcome. The reasons it sits on the watchlist are the as-of signals described above: thin capital, a very high share of troubled loans, losses and a shrinking balance sheet.

## What happened next

In hindsight, the fact sheet provides no later ranks, watchlist flags or reporting status for this bank after the as-of quarter. Based on the outcome case, the bank is treated as still open and still on the watchlist, so its story is not yet resolved.

## Sources

- F1 · Bank name · n/a · Nano Banc · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · CA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 3 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 5.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 7.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 9.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 25.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 16.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 209.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -0.5% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 56.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 22.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 27.3% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 2.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2026-06-30 · -20.9% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -14.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 209.8%; contribution to the score · 2026-06-30 · +1.216 · data/analyst/scores.parquet: feature texas_ratio contribution
- F76 · Driver up #2: loans 90+ days past due or not accruing interest, as a share of loans, value 25.7%; contribution to the score · 2026-06-30 · +0.867 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F77 · Driver up #3: the Tier 1 risk-based capital ratio, value 7.8%; contribution to the score · 2026-06-30 · +0.575 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F78 · Driver up #4: loans 30-89 days past due, as a share of assets, value 5.6%; contribution to the score · 2026-06-30 · +0.378 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F79 · Driver up #5: brokered deposits as a share of deposits, value 22.8%; contribution to the score · 2026-06-30 · +0.360 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F80 · Driver down #1: return on equity (profit as a share of equity), value -10.9%; contribution to the score · 2026-06-30 · -0.340 · data/analyst/scores.parquet: feature return_on_equity contribution
- F81 · Driver down #2: construction loans as a share of loans, value 9.8%; contribution to the score · 2026-06-30 · -0.328 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: deposit growth over the past four quarters, value -14.8%; contribution to the score · 2026-06-30 · -0.169 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F83 · Driver down #4: total assets, value $736.2 million; contribution to the score · 2026-06-30 · -0.155 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: volatile funding as a share of assets, value 4.3%; contribution to the score · 2026-06-30 · -0.077 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
