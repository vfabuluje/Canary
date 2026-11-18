---
cert: 33492
name: "Crescent Bank"
as_of: 2024-12-31
rank: 59
n_banks: 4560
percentile: 98.7280701754386
flagged: true
outcome: "false_alarm"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:09:28"
writer_model: "claude-opus-5-5"
checked: true
---

# Crescent Bank (cert 33492)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

Crescent Bank, a Louisiana bank, ranked 59 out of 4,560 FDIC-insured banks on Canary's risk score as of 2024-12-31, placing it in the 98.7th percentile, where higher means riskier. That rank put it on the watchlist, the riskiest 2% of banks. The main concerns were very high levels of late loans and loan write-offs (loans the bank gave up on collecting), along with a small loss for the year: return on assets was -0.2% against a national median of 0.9%.

## Warning signs in the data

Credit quality stood out most. Loans 30-89 days past due equaled 17.6% of assets, against a national median of 0.2%, and loans 90+ days past due or not accruing interest were 3.3% of loans, versus a median of 0.4%. Net loan write-offs ran at an annualized 11.4% of loans, compared with a median of 0.0%, and the provision for loan losses (money set aside for expected bad loans) was 8.4% of assets, versus 0.1%. The bank held large loan-loss reserves of 11.2% of loans, far above the median of 1.2%.

Capital, the cushion that absorbs losses, was somewhat thinner than typical on most measures: equity was 9.1% of assets versus a median of 9.7%, and the Tier 1 risk-based capital ratio was 12.4% versus 14.3%. The leverage ratio (core capital as a share of average assets) was slightly above the median, at 10.8% against 10.6%. Profitability was weak, with return on equity at -2.8% compared with a median of 9.7%, even though the net interest margin (the spread earned on lending) was very high at 14.0% versus 3.4%.

On funding, interest expense was 4.2% of assets versus a median of 1.8%, and volatile funding (money that can leave quickly) was 18.3% of assets versus 8.8%. Deposits shrank by -19.5% over the past four quarters, while the median bank grew deposits by 3.9%. Unrealized losses on bonds available for sale were 10.0% of equity, a little below the median of 11.2%, and uninsured deposits were low at 4.6% of deposits versus 24.1%.

## Understanding the score

As of 2024-12-31, Crescent Bank ranked 59 of 4,560 banks, the 98.7th percentile on a scale of 0 to 100 where higher means riskier. It was one of 92 banks on the watchlist that quarter, which covers the riskiest 2% of banks.

The five factors pushing the score up most were interest expense at 4.2% of assets, losses on bonds available for sale at 10.0% of equity, the provision for loan losses at 8.4% of assets, the efficiency ratio (operating costs as a share of revenue) at 45.3%, and commercial real estate loans at 1.9% of loans.

The five factors pulling the score down most were the Tier 1 risk-based capital ratio at 12.4%, deposit growth of -19.5%, the Texas ratio (troubled assets against capital plus reserves) at 15.7%, return on equity at -2.8%, and the leverage ratio at 10.8%.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2023-03-31 | 6 | 4,740 | ▲ watchlist |
| 2023-06-30 | 11 | 4,714 | ▲ watchlist |
| 2023-09-30 | 21 | 4,686 | ▲ watchlist |
| 2023-12-31 | 55 | 4,658 | ▲ watchlist |
| 2024-03-31 | 64 | 4,640 | ▲ watchlist |
| 2024-06-30 | 59 | 4,610 | ▲ watchlist |
| 2024-09-30 | 44 | 4,589 | ▲ watchlist |
| 2024-12-31 | 59 | 4,560 | ▲ watchlist |

## Why it was flagged, and what happened

In hindsight, this flag was a false alarm. The bank kept reporting after the as-of quarter and dropped off the watchlist, ranking 240 in Q1 2025 and 244 in Q2 2025, neither flagged. The heavy late loans and write-offs drove the flag, but in the data that followed the bank's risk rank eased rather than worsened, with a rank of 4,037 by 2026-06-30.

## What happened next

Looking back with hindsight, Crescent Bank continued to report in every later quarter in our data. Its rank was 299 at 2025-09-30 and 145 at 2025-12-31, both not flagged. It then fell much further down the risk list, to 3,355 at 2026-03-31 and 4,037 at 2026-06-30, again not flagged.

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2025-03-31 | 240 | 4,536 |  |
| 2025-06-30 | 244 | 4,494 |  |
| 2025-09-30 | 299 | 4,452 |  |
| 2025-12-31 | 145 | 4,411 |  |
| 2026-03-31 | 3,355 | 4,353 |  |
| 2026-06-30 | 4,037 | 4,313 |  |

## Sources

- F1 · Bank name · n/a · Crescent Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2024-12-31 · 2024-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · LA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2024-12-31 · 59 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2024-12-31 · 4,560 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2024-12-31 · 98.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2024-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2024-12-31 · 92 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2024-12-31 · 9.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2024-12-31 · 9.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2024-12-31 · 10.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2024-12-31 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2024-12-31 · 12.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2024-12-31 · 14.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2024-12-31 · 3.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2024-12-31 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2024-12-31 · 17.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2024-12-31 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2024-12-31 · 11.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2024-12-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2024-12-31 · 11.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2024-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2024-12-31 · 8.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2024-12-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2024-12-31 · -0.2% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2024-12-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2024-12-31 · -2.8% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2024-12-31 · 9.7% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2024-12-31 · 14.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2024-12-31 · 3.4% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2024-12-31 · 4.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2024-12-31 · 1.8% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2024-12-31 · 4.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2024-12-31 · 24.1% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2024-12-31 · 18.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2024-12-31 · 8.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2024-12-31 · 10.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2024-12-31 · 11.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2024-12-31 · -19.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2024-12-31 · 3.9% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: annualized interest expense as a share of assets, value 4.2%; contribution to the score · 2024-12-31 · +0.688 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 10.0%; contribution to the score · 2024-12-31 · +0.673 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: annualized provision for loan losses as a share of assets, value 8.4%; contribution to the score · 2024-12-31 · +0.562 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F78 · Driver up #4: the efficiency ratio (operating costs as a share of revenue), value 45.3%; contribution to the score · 2024-12-31 · +0.290 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F79 · Driver up #5: commercial real estate loans as a share of loans, value 1.9%; contribution to the score · 2024-12-31 · +0.147 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 12.4%; contribution to the score · 2024-12-31 · -1.220 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: deposit growth over the past four quarters, value -19.5%; contribution to the score · 2024-12-31 · -0.403 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 15.7%; contribution to the score · 2024-12-31 · -0.402 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: return on equity (profit as a share of equity), value -2.8%; contribution to the score · 2024-12-31 · -0.363 · data/analyst/scores.parquet: feature return_on_equity contribution
- F84 · Driver down #5: the leverage ratio (core capital as a share of average assets), value 10.8%; contribution to the score · 2024-12-31 · -0.261 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F85 · Rank in a later quarter (2025-03-31), not flagged · 2025-03-31 · 240 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F86 · Rank in a later quarter (2025-06-30), not flagged · 2025-06-30 · 244 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F87 · Rank in a later quarter (2025-09-30), not flagged · 2025-09-30 · 299 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F88 · Rank in a later quarter (2025-12-31), not flagged · 2025-12-31 · 145 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F89 · Rank in a later quarter (2026-03-31), not flagged · 2026-03-31 · 3,355 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F90 · Rank in a later quarter (2026-06-30), not flagged · 2026-06-30 · 4,037 (not flagged) · data/analyst/scores.parquet: rank, flagged
