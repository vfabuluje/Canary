---
cert: 17001
name: "First Security Bank&Trust Co"
as_of: 2026-06-30
rank: 13
n_banks: 4313
percentile: 99.7217713888245
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:08:36"
writer_model: "claude-opus-5-5"
checked: true
---

# First Security Bank&Trust Co (cert 17001)

*Outcome not yet known.*

## Summary

First Security Bank&Trust Co, an Oklahoma bank, ranked 13 out of 4,313 FDIC-insured banks on Canary's risk score as of 2026-06-30, which places it in the 99.7th percentile, where higher means riskier. That puts it on Canary's watchlist, the top 2% of banks by score, which held 87 banks that quarter. The main reasons are a very high share of troubled loans, 13.2% of loans against a national median of 0.5%, and a Texas ratio (troubled assets measured against capital plus reserves) of 94.7% against a median of 2.9%.

## Warning signs in the data

Capital, the bank's own cushion against losses, was close to typical: equity was 10.5% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 10.1% against a median of 11.0%. Credit quality stood out the most: loans 90+ days past due or no longer earning interest were 13.2% of loans, far above the 0.5% median, and nonaccrual assets plus foreclosed property were 8.0% of assets against a median of 0.3%. The Texas ratio was 94.7%, far above the 2.9% median, and loans 30-89 days past due were 1.2% of assets against a median of 0.2%. The bank was setting aside more for expected losses, with reserves at 2.1% of loans against a median of 1.2% and an annualized provision (new money set aside for losses) of 0.7% of assets against a median of 0.1%.

Profits were thin: return on assets (profit as a share of assets) was 0.2% against a median of 1.2%, and the efficiency ratio (costs as a share of revenue) was 74.6% against a median of 62.1%. Interest expense was 3.4% of assets, well above the 1.6% median, suggesting relatively costly funding. On funding and liquidity (the ability to meet cash needs), loans were 108.0% of deposits against a median of 80.2%, brokered deposits (money placed through intermediaries) were 8.6% of deposits against a median of 0.0%, and Federal Home Loan Bank borrowings were 9.0% of assets against a median of 0.2%. Volatile funding was 16.7% of assets against a median of 9.0%, and cash was only 0.8% of assets against a median of 6.2%, although uninsured deposits were a low 4.8% of deposits against a median of 24.8%.

Bond losses were not a concern: unrealized losses on bonds available for sale were 0.1% of equity against a median of 5.6%, and losses on bonds held to maturity were 0.0% against a median of 0.0%.

## Understanding the score

As of 2026-06-30 the bank ranked 13 of 4,313 banks, in the 99.7th percentile, and was flagged on the watchlist, which covers the top 2% of banks, or 87 banks that quarter. Its raw model score was 0.5271, which is useful only for ranking banks against each other.

The five factors pushing the score up most were: troubled loans 90+ days late or not accruing interest at 13.2% of loans, contributing +1.091; the Texas ratio at 94.7%, contributing +0.912; interest expense at 3.4% of assets, contributing +0.461; securities at only 1.1% of assets, contributing +0.232; and commercial real estate loans at 11.8% of loans, contributing +0.207. The five factors pulling the score down most were: the Tier 1 risk-based capital ratio (core capital against risk-weighted assets, value not shown), contributing -0.717; return on equity at 1.9%, contributing -0.453; the total risk-based capital ratio (value not shown), contributing -0.339; construction loans at 13.7% of loans, contributing -0.260; and loans 30-89 days past due at 1.2% of assets, contributing -0.200.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 416 | 4,589 |  |
| 2024-12-31 | 95 | 4,560 |  |
| 2025-03-31 | 33 | 4,536 | ▲ watchlist |
| 2025-06-30 | 59 | 4,494 | ▲ watchlist |
| 2025-09-30 | 22 | 4,452 | ▲ watchlist |
| 2025-12-31 | 10 | 4,411 | ▲ watchlist |
| 2026-03-31 | 13 | 4,353 | ▲ watchlist |
| 2026-06-30 | 13 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

Hindsight view: the fact sheet contains no data from after the as-of quarter, so there is no later outcome to report for this bank. It is on the watchlist because, as of 2026-06-30, it ranked 13 of 4,313 banks, driven mainly by its large share of troubled loans and its high Texas ratio. Being on the watchlist marks a bank as unusually risky compared with its peers; it does not mean anything has happened to the bank.

## What happened next

Hindsight view: no later ranks, watchlist flags or reporting status after the as-of quarter of 2026-06-30 appear in the fact sheet. Whether the bank keeps reporting, and whether its rank rises or falls, can only be judged once newer quarterly data is available.

## Sources

- F1 · Bank name · n/a · First Security Bank&Trust Co · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · OK · data/raw/financials: STALP
- F5 · Model score · 2026-06-30 · 0.5271 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 13 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 10.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 13.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 2.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F27 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F28 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 94.7% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 74.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F42 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F43 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F44 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F45 · Bank: loans as a share of deposits · 2026-06-30 · 108.0% · data/features/fct_bank_features.parquet: loans_to_deposits
- F46 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 8.6% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F55 · Bank: volatile funding as a share of assets · 2026-06-30 · 16.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F56 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F59 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F60 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 13.2%; contribution to the score · 2026-06-30 · +1.091 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F72 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 94.7%; contribution to the score · 2026-06-30 · +0.912 · data/analyst/scores.parquet: feature texas_ratio contribution
- F73 · Driver up #3: annualized interest expense as a share of assets, value 3.4%; contribution to the score · 2026-06-30 · +0.461 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F74 · Driver up #4: securities as a share of assets, value 1.1%; contribution to the score · 2026-06-30 · +0.232 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F75 · Driver up #5: commercial real estate loans as a share of loans, value 11.8%; contribution to the score · 2026-06-30 · +0.207 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.717 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: return on equity (profit as a share of equity), value 1.9%; contribution to the score · 2026-06-30 · -0.453 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver down #3: the total risk-based capital ratio; contribution to the score · 2026-06-30 · -0.339 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver down #4: construction loans as a share of loans, value 13.7%; contribution to the score · 2026-06-30 · -0.260 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F80 · Driver down #5: loans 30-89 days past due, as a share of assets, value 1.2%; contribution to the score · 2026-06-30 · -0.200 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
