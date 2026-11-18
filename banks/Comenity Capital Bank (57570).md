---
cert: 57570
name: "Comenity Capital Bank"
as_of: 2026-06-30
rank: 80
n_banks: 4313
percentile: 98.1683283097612
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:10:11"
writer_model: "claude-opus-5-5"
checked: true
---

# Comenity Capital Bank (cert 57570)

*Outcome not yet known.*

## Summary

Comenity Capital Bank, a Utah bank, ranked 80 out of 4,313 banks nationally on Canary's risk score as of 2026-06-30, with a percentile of 98.2%, where higher means riskier. That rank put it on the watchlist, which holds 2% of banks and numbered 87 banks that quarter. Its loan losses and past-due loans ran far above national medians, while its capital cushions and profits were mostly stronger than typical.

## Warning signs in the data

Credit quality, meaning how well borrowers keep up with payments, stood out most: loans 90 or more days past due or no longer earning interest were 3.2% of loans, against a national median of 0.5%. Loans in early-stage delinquency, behind on payments but not yet seriously late, were 2.8% of assets, versus a median of 0.2%, and annualized write-offs of bad loans, net of recoveries, were 7.5% of loans, versus 0.0%. The provision for loan losses, the amount set aside each period for expected bad loans, ran at an annualized 6.5% of assets against a median of 0.1%, and loan-loss reserves were 11.4% of loans against 1.2%. The Texas ratio, which compares troubled assets with capital plus reserves, was 12.0%, above the median of 2.9%.

Capital, the bank's own money that absorbs losses, was generally solid: equity was 13.0% of assets versus a median of 10.6%, and the leverage ratio was 12.8% versus 11.0%. The total risk-based capital ratio was 17.7% against a median of 15.8%, though the Tier 1 risk-based capital ratio, a measure of core capital against risk-weighted assets, was slightly below the median at 14.2% versus 14.6%.

On funding, annualized interest expense was 3.3% of assets, well above the median of 1.6%, and brokered deposits, money placed through intermediaries, were 9.8% of deposits versus a median of 0.0%. Core deposits, the steadier everyday deposits, were 64.1% of assets versus a median of 75.5%, while uninsured deposits were only 8.8% of deposits versus 24.8% and cash was a high 17.8% of assets versus 6.2%. Losses on bonds available for sale were small at 0.6% of equity against a median of 5.6%, with securities making up just 0.8% of assets versus a median of 17.6%.

## Understanding the score

As of 2026-06-30 the bank ranked 80 of 4,313 banks, with a percentile of 98.2% on a scale of 0 to 100 where higher means riskier, and a raw model score of 0.1040. It was flagged for the watchlist, which covers 2% of banks and held 87 banks that quarter.

The five features pushing the score up most were the provision for loan losses at 6.5% of assets, interest expense at 3.3% of assets, securities at only 0.8% of assets, early-stage past-due loans at 2.8% of assets, and brokered deposits at 9.8% of deposits. The five features pulling the score down most were the Tier 1 risk-based capital ratio at 14.2%, return on equity at 12.7%, the leverage ratio at 12.8%, the total risk-based capital ratio at 17.7%, and the Texas ratio at 12.0%.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 45 | 4,589 | ▲ watchlist |
| 2024-12-31 | 54 | 4,560 | ▲ watchlist |
| 2025-03-31 | 90 | 4,536 | ▲ watchlist |
| 2025-06-30 | 79 | 4,494 | ▲ watchlist |
| 2025-09-30 | 70 | 4,452 | ▲ watchlist |
| 2025-12-31 | 111 | 4,411 |  |
| 2026-03-31 | 63 | 4,353 | ▲ watchlist |
| 2026-06-30 | 80 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight, this is an open watchlist case: the bank was flagged by the model, and the fact sheet contains no later data showing that it stopped operating. The flag reflects heavy loan-loss provisions, high past-due loans and high funding costs, offset only partly by strong capital and profits. A watchlist flag marks a bank whose figures resemble those of past failures; it is not a finding that the bank will fail.

## What happened next

Looking at hindsight, the fact sheet includes no data after the as-of quarter, so later ranks, flags and reporting status cannot be described here. The score history table added below shows any later quarters that are available; if a bank stops reporting, our data does not distinguish a merger from a closure.

## Sources

- F1 · Bank name · n/a · Comenity Capital Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · UT · data/raw/financials: STALP
- F5 · Model score · 2026-06-30 · 0.1040 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 80 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 98.2% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 13.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 12.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 17.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 2.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 11.4% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 7.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 6.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 12.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 8.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 64.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 17.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F75 · Driver up #1: annualized provision for loan losses as a share of assets, value 6.5%; contribution to the score · 2026-06-30 · +0.625 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F76 · Driver up #2: annualized interest expense as a share of assets, value 3.3%; contribution to the score · 2026-06-30 · +0.488 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F77 · Driver up #3: securities as a share of assets, value 0.8%; contribution to the score · 2026-06-30 · +0.406 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F78 · Driver up #4: loans 30-89 days past due, as a share of assets, value 2.8%; contribution to the score · 2026-06-30 · +0.206 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F79 · Driver up #5: brokered deposits as a share of deposits, value 9.8%; contribution to the score · 2026-06-30 · +0.194 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 14.2%; contribution to the score · 2026-06-30 · -0.967 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 12.7%; contribution to the score · 2026-06-30 · -0.544 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: the leverage ratio (core capital as a share of average assets), value 12.8%; contribution to the score · 2026-06-30 · -0.456 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F83 · Driver down #4: the total risk-based capital ratio, value 17.7%; contribution to the score · 2026-06-30 · -0.447 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F84 · Driver down #5: the Texas ratio (troubled assets against capital plus reserves), value 12.0%; contribution to the score · 2026-06-30 · -0.377 · data/analyst/scores.parquet: feature texas_ratio contribution
