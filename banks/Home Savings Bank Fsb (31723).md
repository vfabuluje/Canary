---
cert: 31723
name: "Home Savings Bank Fsb"
as_of: 2026-06-30
rank: 18
n_banks: 4313
percentile: 99.6058428008347
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:08:54"
writer_model: "claude-opus-5-5"
checked: true
---

# Home Savings Bank Fsb (cert 31723)

*Outcome not yet known.*

## Summary

Home Savings Bank Fsb, a small Kentucky bank, ranked 18 out of 4,313 FDIC-insured banks on Canary's risk score as of 2026-06-30, placing it in the 99.6th percentile, where higher means riskier. That rank put it on Canary's watchlist, which covers roughly the riskiest 2% of banks. The main concerns are a high share of troubled loans and losses on the bottom line, partly offset by capital levels near the national norm.

## Warning signs in the data

Credit quality is the clearest weak spot: loans seriously past due or no longer earning interest made up 7.5% of loans, against a national median of 0.5%. Nonaccrual assets (loans no longer earning interest) and foreclosed property were 5.8% of assets versus a median of 0.3%, and loans in the early stages of lateness were 0.9% of assets versus 0.2%. The Texas ratio, which compares troubled assets with the cushion of capital plus reserves, stood at 48.8%, far above the median of 2.9%, while loan-loss reserves (money set aside for bad loans) were only 0.8% of loans versus 1.2%.

Capital looked roughly normal: equity was 11.3% of assets against a median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 10.2% versus 11.0%. Earnings were weak, with return on assets of -1.3% against a median of 1.2%, a net interest margin (the spread earned on lending) of 2.6% versus 3.9%, and an efficiency ratio (costs as a share of revenue) of 147.6% versus 62.1%.

On funding, loans equaled 99.6% of deposits versus a median of 80.2%, and Federal Home Loan Bank borrowings were 9.8% of assets versus 0.2%. Offsetting this, uninsured deposits were just 2.0% of deposits versus 24.8%, and cash was 19.2% of assets versus 6.2%. The bank held no securities, 0.0% of assets against a median of 17.6%, so it showed no bond losses, 0.0% of equity versus a median of 5.6% on bonds available for sale.

## Understanding the score

As of 2026-06-30 the bank ranked 18 of 4,313 banks, in the 99.6th percentile on a scale of 0 to 100 where higher means riskier. It was flagged as one of 87 banks on the watchlist that quarter, the group making up about 2% of banks.

The five factors pushing the score up most were seriously late or non-earning loans at 7.5% of loans, the Texas ratio at 48.8%, securities at 0.0% of assets, interest expense at 2.4% of assets, and commercial real estate loans at 7.8% of loans.

The five factors pulling the score down most were the core risk-based capital ratio (core capital against risk-weighted assets), construction loans at 3.6% of loans, the leverage ratio at 10.2%, return on equity at -11.4%, and loan-loss reserves at 0.8% of loans.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 525 | 4,589 |  |
| 2024-12-31 | 511 | 4,560 |  |
| 2025-03-31 | 828 | 4,536 |  |
| 2025-06-30 | 404 | 4,494 |  |
| 2025-09-30 | 16 | 4,452 | ▲ watchlist |
| 2025-12-31 | 20 | 4,411 | ▲ watchlist |
| 2026-03-31 | 26 | 4,353 | ▲ watchlist |
| 2026-06-30 | 18 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight, this bank is an open watchlist case: it was flagged by the model and, in the data available to Canary, it has not failed. Its place on the watchlist reflects the weak credit quality and losses seen in the as-of data, not a known later event. A flag marks a bank for closer attention; on its own it does not mean a failure is coming.

## What happened next

In hindsight, the fact sheet contains no quarters after 2026-06-30, so there are no later ranks or flags to report yet. Based on the outcome case, the bank remains open and on the watchlist; later quarters will show whether its rank improves or it stops reporting.

## Sources

- F1 · Bank name · n/a · Home Savings Bank Fsb · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KY · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 18 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.6% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 11.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 7.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 5.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 48.8% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F39 · Bank: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F40 · National median: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F41 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 147.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F42 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F45 · Bank: loans as a share of deposits · 2026-06-30 · 99.6% · data/features/fct_bank_features.parquet: loans_to_deposits
- F46 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 19.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F63 · Bank: securities as a share of assets · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F64 · National median: securities as a share of assets · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F71 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 7.5%; contribution to the score · 2026-06-30 · +0.914 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F72 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 48.8%; contribution to the score · 2026-06-30 · +0.840 · data/analyst/scores.parquet: feature texas_ratio contribution
- F73 · Driver up #3: securities as a share of assets, value 0.0%; contribution to the score · 2026-06-30 · +0.365 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F74 · Driver up #4: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2026-06-30 · +0.278 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F75 · Driver up #5: commercial real estate loans as a share of loans, value 7.8%; contribution to the score · 2026-06-30 · +0.248 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.883 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: construction loans as a share of loans, value 3.6%; contribution to the score · 2026-06-30 · -0.463 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F78 · Driver down #3: the leverage ratio (core capital as a share of average assets), value 10.2%; contribution to the score · 2026-06-30 · -0.297 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver down #4: return on equity (profit as a share of equity), value -11.4%; contribution to the score · 2026-06-30 · -0.248 · data/analyst/scores.parquet: feature return_on_equity contribution
- F80 · Driver down #5: loan-loss reserves as a share of loans, value 0.8%; contribution to the score · 2026-06-30 · -0.225 · data/analyst/scores.parquet: feature allowance_to_loans contribution
