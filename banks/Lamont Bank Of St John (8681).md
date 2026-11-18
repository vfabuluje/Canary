---
cert: 8681
name: "Lamont Bank Of St John"
as_of: 2026-06-30
rank: 2
n_banks: 4313
percentile: 99.97681428240203
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:07:23"
writer_model: "claude-opus-5-5"
checked: true
---

# Lamont Bank Of St John (cert 8681)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Lamont Bank Of St John, a small Washington bank, ranked 2 out of 4,313 FDIC-insured banks on Canary's risk score, placing it at the 100.0% mark, the 100.0th percentile, where higher means riskier. That puts it on Canary's watchlist, which is flagged for this bank. Its capital cushion was very thin, with equity at 1.8% of assets against a national median of 10.6%, and 49.8% of its loans were seriously overdue or not paying interest, versus a median of 0.5%.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was far below typical levels: equity was 1.8% of assets versus a national median of 10.6%. The leverage ratio (core capital as a share of average assets) was 3.0% against a median of 11.0%, the Tier 1 risk-based capital ratio was 3.2% against 14.6%, and the total risk-based capital ratio was 4.5% against 15.8%.

Credit quality was very weak: loans 90 or more days past due or not accruing interest made up 49.8% of loans, compared with a median of 0.5%. Nonaccrual assets and foreclosed property were 33.9% of assets versus a median of 0.3%, and the Texas ratio, which weighs troubled assets against capital plus reserves, was 519.1% against a median of 2.9%. The bank was losing money, with return on assets of -6.2% against a median of 1.2%, and annualized loan write-offs of 4.3% of loans against a median of 0.0%.

Funding looked steadier: core deposits, the stable everyday deposits, were 91.3% of assets versus a median of 75.5%, and uninsured deposits were 8.7% of deposits versus 24.8%. However, unrealized losses on bonds available for sale equaled 87.8% of equity, well above the median of 5.6%, and total assets shrank by -15.2% over the past four quarters while the median grew by 4.5%.

## Understanding the score

On 2026-06-30 the bank ranked 2 of 4,313 banks, at the 100.0th percentile on a scale of 0 to 100 where higher means riskier, with a model score of 0.9959. The watchlist covers the top 2% of banks, 87 banks that quarter, and this bank was flagged.

The five factors pushing the score up most were the Tier 1 risk-based capital ratio at 3.2%, return on equity (profit as a share of equity) at -228.8%, the Texas ratio at 519.1%, seriously overdue or nonaccruing loans at 49.8% of loans, and the total risk-based capital ratio at 4.5%. The five factors pulling it down most were interest expense at 1.7% of assets, the efficiency ratio (operating costs as a share of revenue) at 165.5%, loans 30-89 days past due at 0.7% of assets, construction loans at 0.0% of loans, and securities at 25.9% of assets. These downward pulls were small compared with the upward pushes.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 246 | 4,589 |  |
| 2024-12-31 | 128 | 4,560 |  |
| 2025-03-31 | 153 | 4,536 |  |
| 2025-06-30 | 149 | 4,494 |  |
| 2025-09-30 | 8 | 4,452 | ▲ watchlist |
| 2025-12-31 | 7 | 4,411 | ▲ watchlist |
| 2026-03-31 | 3 | 4,353 | ▲ watchlist |
| 2026-06-30 | 2 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight: this bank's case is an open watchlist case, meaning it was flagged and our data does not show a resolution. The fact sheet contains no data from after the as-of quarter, so there is nothing later to confirm or contradict the flag yet. The flag rests on the very thin capital and heavy share of troubled loans described above.

## What happened next

In hindsight: our data has no later ranks, flags or failure record for this bank after the as-of quarter. Whether it keeps reporting, or stops because it merged or closed, will only show up in future quarters of data.

## Sources

- F1 · Bank name · n/a · Lamont Bank Of St John · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WA · data/raw/financials: STALP
- F5 · Model score · 2026-06-30 · 0.9959 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 49.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 33.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 4.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 519.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -6.2% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 8.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 91.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 87.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2026-06-30 · -15.2% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 3.2%; contribution to the score · 2026-06-30 · +1.776 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -228.8%; contribution to the score · 2026-06-30 · +1.190 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 519.1%; contribution to the score · 2026-06-30 · +1.019 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 49.8%; contribution to the score · 2026-06-30 · +0.505 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 4.5%; contribution to the score · 2026-06-30 · +0.445 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 1.7%; contribution to the score · 2026-06-30 · -0.193 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: the efficiency ratio (operating costs as a share of revenue), value 165.5%; contribution to the score · 2026-06-30 · -0.149 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F82 · Driver down #3: loans 30-89 days past due, as a share of assets, value 0.7%; contribution to the score · 2026-06-30 · -0.146 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F83 · Driver down #4: construction loans as a share of loans, value 0.0%; contribution to the score · 2026-06-30 · -0.124 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F84 · Driver down #5: securities as a share of assets, value 25.9%; contribution to the score · 2026-06-30 · -0.115 · data/analyst/scores.parquet: feature securities_to_assets contribution
