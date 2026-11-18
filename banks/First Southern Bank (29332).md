---
cert: 29332
name: "First Southern Bank"
as_of: 2026-06-30
rank: 8
n_banks: 4313
percentile: 99.83769997681429
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:07:46"
writer_model: "claude-opus-5-5"
checked: true
---

# First Southern Bank (cert 29332)

*Outcome not yet known.*

## Summary

First Southern Bank, an Alabama bank, ranked 8 out of 4,313 FDIC-insured banks on Canary's risk score as of 2026-06-30, placing it in the 99.8th percentile. That puts it on Canary's watchlist, the riskiest 2% of banks. The main reason is loan trouble: 10.9% of its loans were 90 or more days late or no longer paying interest, against a national median of 0.5%. The bank also lost money, with a return on assets of -2.5% against a national median of 1.2%.

## Warning signs in the data

Capital, the cushion of the owners' own money that absorbs losses, was thinner than at a typical bank: equity was 8.8% of assets against a national median of 10.6%. The leverage ratio (core capital as a share of average assets) was 8.9%, below the national median of 11.0%.

Credit quality, meaning how well borrowers are repaying, stands out most: 10.9% of loans were 90+ days past due or not accruing interest, far above the national median of 0.5%. Nonaccrual assets (loans no longer earning interest) plus foreclosed property made up 7.4% of assets, against a national median of 0.3%, and loans 30-89 days past due were 1.7% of assets against 0.2%. Net loan write-offs ran at 4.7% of loans and the provision for loan losses (money set aside for expected bad loans) at 4.5% of assets, both far above national medians of 0.0% and 0.1%. The Texas ratio, which weighs troubled assets against capital plus reserves, was 70.5% against a national median of 2.9%, and return on equity was -27.8% against 11.6%.

On funding, uninsured deposits (balances above the FDIC insurance limit) were 52.8% of deposits, well above the national median of 24.8%, and Federal Home Loan Bank borrowings were 5.9% of assets against 0.2%. Offsetting this, cash was 13.4% of assets against a national median of 6.2%, brokered deposits were 0.0%, and losses on bonds available for sale were 1.5% of equity, below the national median of 5.6%.

## Understanding the score

First Southern Bank ranked 8 of 4,313 banks as of 2026-06-30, the 99.8th percentile on a scale from 0 to 100 where higher means riskier; its raw model score was 0.6122. It was flagged for the watchlist, which covers the top 2% of banks, or 87 banks that quarter.

The five factors pushing the score up most were: loans 90+ days past due or not accruing interest at 10.9% (+1.076), the Texas ratio at 70.5% (+0.904), the provision for loan losses at 4.5% of assets (+0.316), return on equity at -27.8% (+0.198), and interest expense at 2.3% of assets (+0.127).

The five factors pulling the score down most were: the Tier 1 risk-based capital ratio, a capital measure weighted by how risky the assets are (-1.071, value not shown), construction loans at 6.4% of loans (-0.362), brokered deposits at 0.0% of deposits (-0.163), total assets of $679.2 million (-0.163), and deposit growth over the past four quarters of 6.4% (-0.125).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,089 | 4,589 |  |
| 2024-12-31 | 1,068 | 4,560 |  |
| 2025-03-31 | 29 | 4,536 | ▲ watchlist |
| 2025-06-30 | 50 | 4,494 | ▲ watchlist |
| 2025-09-30 | 35 | 4,452 | ▲ watchlist |
| 2025-12-31 | 105 | 4,411 |  |
| 2026-03-31 | 7 | 4,353 | ▲ watchlist |
| 2026-06-30 | 8 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

Looking back in hindsight, this bank's outcome case is that it remains open and on the watchlist. Our fact sheet contains no figures from after the as-of quarter, so we cannot yet say whether its loan problems eased or worsened. Its watchlist status rests on the as-of data described above rather than on any later event.

## What happened next

In hindsight, no later ranks, flags or reporting data are available in our fact sheet for this bank. As far as this data shows, the bank is still open and remains on the watchlist, and later quarters will show whether its position changes.

## Sources

- F1 · Bank name · n/a · First Southern Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · AL · data/raw/financials: STALP
- F5 · Model score · 2026-06-30 · 0.6122 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 8 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 10.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 7.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F25 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 4.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F26 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F27 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F28 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 70.5% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -2.5% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F37 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -27.8% · data/features/fct_bank_features.parquet: return_on_equity
- F38 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 52.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 5.9% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 13.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 10.9%; contribution to the score · 2026-06-30 · +1.076 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F72 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 70.5%; contribution to the score · 2026-06-30 · +0.904 · data/analyst/scores.parquet: feature texas_ratio contribution
- F73 · Driver up #3: annualized provision for loan losses as a share of assets, value 4.5%; contribution to the score · 2026-06-30 · +0.316 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F74 · Driver up #4: return on equity (profit as a share of equity), value -27.8%; contribution to the score · 2026-06-30 · +0.198 · data/analyst/scores.parquet: feature return_on_equity contribution
- F75 · Driver up #5: annualized interest expense as a share of assets, value 2.3%; contribution to the score · 2026-06-30 · +0.127 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -1.071 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: construction loans as a share of loans, value 6.4%; contribution to the score · 2026-06-30 · -0.362 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F78 · Driver down #3: brokered deposits as a share of deposits, value 0.0%; contribution to the score · 2026-06-30 · -0.163 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F79 · Driver down #4: total assets, value $679.2 million; contribution to the score · 2026-06-30 · -0.163 · data/analyst/scores.parquet: feature log_total_assets contribution
- F80 · Driver down #5: deposit growth over the past four quarters, value 6.4%; contribution to the score · 2026-06-30 · -0.125 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
