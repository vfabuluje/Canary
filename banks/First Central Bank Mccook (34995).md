---
cert: 34995
name: "First Central Bank Mccook"
as_of: 2025-12-31
rank: 82
n_banks: 4411
percentile: 98.16368170482885
flagged: true
outcome: "false_alarm"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:09:53"
writer_model: "claude-opus-5-5"
checked: true
---

# First Central Bank Mccook (cert 34995)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

First Central Bank Mccook, a Nebraska bank with $127.3 million in total assets, ranked 82 out of 4,411 banks nationally as of 2025-12-31, with a percentile of 98.2% on Canary's risk scale. That put it on Canary's watchlist, which covers the riskiest 2% of banks. The main concerns were troubled loans, at 6.4% of loans against a national median of 0.4%, and a heavy use of brokered deposits (money placed through middlemen), at 18.9% of deposits against a median of 0.0%.

## Warning signs in the data

Capital, the cushion of the owners' money that absorbs losses, was close to typical: equity was 10.6% of assets against a national median of 10.4%, though the Tier 1 risk-based capital ratio (core capital measured against riskier assets) was 13.7% against a median of 14.4%. Credit quality stood out most: loans 90 or more days past due or no longer earning interest were 6.4% of loans, far above the 0.4% median, and nonaccrual assets plus foreclosed property were 4.5% of assets against a median of 0.3%. The Texas ratio, which weighs troubled assets against capital plus reserves, was 37.6% versus a median of 2.7%, and net loan write-offs were 1.3% of loans versus a median of 0.0%.

On funding, brokered deposits were 18.9% of deposits while the median bank had 0.0%, and core deposits, the steadier everyday accounts, were 59.6% of assets against a median of 75.4%. Interest expense was 2.4% of assets versus a median of 1.7%, and Federal Home Loan Bank borrowings (loans from a government-sponsored lender to banks) were 3.3% of assets versus 0.2%. Unrealized losses on bonds held to maturity were 2.9% of equity against a median of 0.0%, while bonds available for sale showed -0.4% of equity against a median of 5.2%, so bond losses were modest overall.

## Understanding the score

As of 2025-12-31 the bank ranked 82 of 4,411 banks, with a percentile of 98.2% on a scale of 0 to 100 where higher means riskier. It was one of 89 banks flagged on the watchlist that quarter, which holds the top 2% of scores.

Five factors pushed the score up most: troubled loans 90 or more days past due or not accruing interest at 6.4% of loans, brokered deposits at 18.9% of deposits, interest expense at 2.4% of assets, recently past-due loans at 0.0% of assets, and commercial real estate loans at 11.4% of loans.

Five factors pulled the score down most: the Tier 1 risk-based capital ratio at 13.7%, the total risk-based capital ratio at 14.9%, return on equity (profit as a share of the owners' money) at 5.5%, return on assets at 0.6%, and deposit growth over the past four quarters at -0.8%.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-03-31 | 1,257 | 4,640 |  |
| 2024-06-30 | 654 | 4,610 |  |
| 2024-09-30 | 895 | 4,589 |  |
| 2024-12-31 | 25 | 4,560 | ▲ watchlist |
| 2025-03-31 | 49 | 4,536 | ▲ watchlist |
| 2025-06-30 | 43 | 4,494 | ▲ watchlist |
| 2025-09-30 | 261 | 4,452 |  |
| 2025-12-31 | 82 | 4,411 | ▲ watchlist |

## Why it was flagged, and what happened

In hindsight, this flag looks like a false alarm based on the data available so far. The bank kept reporting after the as-of quarter, and its rank improved to 271 at 2026-03-31 and to 534 at 2026-06-30, with no watchlist flag in either quarter. The model reacted to high troubled loans and reliance on brokered deposits, but the bank stayed off the watchlist in the following quarters in our data.

## What happened next

Looking back with hindsight, the bank continued to file reports after the as-of quarter. It ranked 271 nationally at 2026-03-31 and 534 at 2026-06-30, and was not flagged on the watchlist in either quarter.

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2026-03-31 | 271 | 4,353 |  |
| 2026-06-30 | 534 | 4,313 |  |

## Sources

- F1 · Bank name · n/a · First Central Bank Mccook · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2025-12-31 · 2025-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NE · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2025-12-31 · 82 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2025-12-31 · 4,411 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2025-12-31 · 98.2% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2025-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2025-12-31 · 89 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2025-12-31 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2025-12-31 · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2025-12-31 · 13.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2025-12-31 · 14.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2025-12-31 · 6.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2025-12-31 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2025-12-31 · 4.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2025-12-31 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2025-12-31 · 1.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 37.6% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 2.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2025-12-31 · 2.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2025-12-31 · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2025-12-31 · 18.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2025-12-31 · 59.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2025-12-31 · 75.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2025-12-31 · 3.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2025-12-31 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2025-12-31 · 2.9% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2025-12-31 · -0.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2025-12-31 · 5.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2025-12-31 · $127.3 million · data/features/fct_bank_features.parquet: log_total_assets
- F75 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 6.4%; contribution to the score · 2025-12-31 · +0.867 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F76 · Driver up #2: brokered deposits as a share of deposits, value 18.9%; contribution to the score · 2025-12-31 · +0.677 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F77 · Driver up #3: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2025-12-31 · +0.340 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F78 · Driver up #4: loans 30-89 days past due, as a share of assets, value 0.0%; contribution to the score · 2025-12-31 · +0.163 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F79 · Driver up #5: commercial real estate loans as a share of loans, value 11.4%; contribution to the score · 2025-12-31 · +0.097 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 13.7%; contribution to the score · 2025-12-31 · -1.178 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: the total risk-based capital ratio, value 14.9%; contribution to the score · 2025-12-31 · -0.402 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 5.5%; contribution to the score · 2025-12-31 · -0.384 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: return on assets (profit as a share of assets), value 0.6%; contribution to the score · 2025-12-31 · -0.368 · data/analyst/scores.parquet: feature return_on_assets contribution
- F84 · Driver down #5: deposit growth over the past four quarters, value -0.8%; contribution to the score · 2025-12-31 · -0.298 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F85 · Rank in a later quarter (2026-03-31), not flagged · 2026-03-31 · 271 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F86 · Rank in a later quarter (2026-06-30), not flagged · 2026-06-30 · 534 (not flagged) · data/analyst/scores.parquet: rank, flagged
