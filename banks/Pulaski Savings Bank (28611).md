---
cert: 28611
name: "Pulaski Savings Bank"
as_of: 2024-09-30
rank: 1814
n_banks: 4589
percentile: 60.49248202222706
flagged: false
outcome: "missed"
after_test_window: false
failure_date: 2025-01-17
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:05:53"
writer_model: "claude-opus-5-5"
checked: true
---

# Pulaski Savings Bank (cert 28611)

*Hindsight: failed 2025-01-17. Canary did not flag it.*

## Summary

As of 2024-09-30, Pulaski Savings Bank, a small Illinois savings bank, ranked 1,814 out of 4,589 FDIC-insured banks on Canary's risk score, placing it in the 60.5th percentile, where higher means riskier. It was not flagged on Canary's watchlist that quarter. Its capital cushions were strong and its overdue-loan figures were clean, but the bank was losing money, with a return on assets of -0.6% against a national median of 0.9%.

## Warning signs in the data

Profitability was the weakest area: return on assets (profit as a share of assets) was -0.6% versus a national median of 0.9%, and return on equity (profit as a share of owners' capital) was -5.7% versus 9.8%. The efficiency ratio, which measures operating costs as a share of revenue, was 117.4% against a median of 67.8%, meaning costs exceeded revenue. Loans 30-89 days past due, an early sign of borrowers falling behind, were 0.9% of assets, well above the national median of 0.2%.

Capital looked solid: the Tier 1 risk-based capital ratio (core capital against risk-weighted assets) was 20.0% versus a median of 14.3%, and equity was 10.2% of assets versus 10.0%, though the leverage ratio of 10.3% sat slightly below the 10.7% median. Seriously troubled loans, those 90+ days past due or not accruing interest, were 0.0% of loans against a median of 0.4%.

On funding, loans equaled 97.3% of deposits versus a median of 79.2%, and Federal Home Loan Bank borrowings (loans from a government-sponsored lender to banks) were 3.0% of assets versus 0.8%. Uninsured deposits were only 5.0% of deposits against a median of 23.6%, and losses on bonds available for sale were 0.4% of equity versus a median of 8.5%. The bank was small, with total assets of $49.5 million compared with a national median of $352.9 million.

## Understanding the score

For the quarter ending 2024-09-30, Pulaski Savings Bank ranked 1,814 of 4,589 banks, the 60.5th percentile on a 0 to 100 scale where higher means riskier, with a raw score of 0.0089. It was not flagged on the watchlist, which covers the top 2% of banks and held 92 banks that quarter.

The five factors pushing the score up were a low share of assets in securities at 0.6% (+0.493), small total assets of $49.5 million (+0.184), commercial real estate loans at 5.9% of loans (+0.151), equity at 10.2% of assets (+0.097), and losses on bonds available for sale at 0.4% of equity (+0.070).

The five factors pulling the score down were the Tier 1 risk-based capital ratio of 20.0% (-1.106), interest expense at 1.3% of assets (-0.833), a Texas ratio, which weighs troubled assets against capital plus reserves, of 0.0% (-0.806), the total risk-based capital ratio of 21.3% (-0.682), and seriously overdue or non-accruing loans at 0.0% of loans (-0.402).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2022-12-31 | 2,651 | 4,773 |  |
| 2023-03-31 | 3,017 | 4,740 |  |
| 2023-06-30 | 3,038 | 4,714 |  |
| 2023-09-30 | 3,169 | 4,686 |  |
| 2023-12-31 | 2,323 | 4,658 |  |
| 2024-03-31 | 2,738 | 4,640 |  |
| 2024-06-30 | 1,980 | 4,610 |  |
| 2024-09-30 | 1,814 | 4,589 |  |

## Why the model missed it

In hindsight, the bank failed on January 17, 2025, and its last reported quarter was 2024-09-30, when it ranked 1,814 and was not on the watchlist. The model learned mostly from credit-loss failures, which made up 96% of the 539 failed banks in its training period. This bank showed few credit-loss signs, and its strong risk-based capital and near-zero troubled loans pulled its score down, outweighing its losses and high costs. The data does not show why the bank failed, so the cause cannot be confirmed here.

## What happened next

In hindsight, the bank's last filed report covered the quarter ending 2024-09-30, and it failed on January 17, 2025. Because it stopped reporting after that quarter, there are no later ranks or watchlist flags for it.

## Sources

- F1 · Bank name · n/a · Pulaski Savings Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2024-09-30 · 2024-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F5 · Model score · 2024-09-30 · 0.0089 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2024-09-30 · 1,814 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2024-09-30 · 4,589 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2024-09-30 · 60.5% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2024-09-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2024-09-30 · 92 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2024-09-30 · 10.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2024-09-30 · 10.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2024-09-30 · 10.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2024-09-30 · 10.7% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2024-09-30 · 20.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2024-09-30 · 14.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2024-09-30 · 0.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2024-09-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2024-09-30 · 0.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2024-09-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2024-09-30 · -0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2024-09-30 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2024-09-30 · -5.7% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2024-09-30 · 9.8% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2024-09-30 · 117.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2024-09-30 · 67.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F49 · Bank: loans as a share of deposits · 2024-09-30 · 97.3% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2024-09-30 · 79.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2024-09-30 · 5.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2024-09-30 · 23.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2024-09-30 · 3.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2024-09-30 · 0.8% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2024-09-30 · 0.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2024-09-30 · 8.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2024-09-30 · $49.5 million · data/features/fct_bank_features.parquet: log_total_assets
- F70 · National median: total assets · 2024-09-30 · $352.9 million · data/features/fct_bank_features.parquet: log_total_assets (median of all banks)
- F75 · Driver up #1: securities as a share of assets, value 0.6%; contribution to the score · 2024-09-30 · +0.493 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F76 · Driver up #2: total assets, value $49.5 million; contribution to the score · 2024-09-30 · +0.184 · data/analyst/scores.parquet: feature log_total_assets contribution
- F77 · Driver up #3: commercial real estate loans as a share of loans, value 5.9%; contribution to the score · 2024-09-30 · +0.151 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F78 · Driver up #4: equity as a share of assets, value 10.2%; contribution to the score · 2024-09-30 · +0.097 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F79 · Driver up #5: losses on bonds available for sale, as a share of equity, value 0.4%; contribution to the score · 2024-09-30 · +0.070 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 20.0%; contribution to the score · 2024-09-30 · -1.106 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 1.3%; contribution to the score · 2024-09-30 · -0.833 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 0.0%; contribution to the score · 2024-09-30 · -0.806 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: the total risk-based capital ratio, value 21.3%; contribution to the score · 2024-09-30 · -0.682 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F84 · Driver down #5: loans 90+ days past due or not accruing interest, as a share of loans, value 0.0%; contribution to the score · 2024-09-30 · -0.402 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F85 · Failure date · 2025-01-17 · 2025-01-17 · data/raw/failures: FAILDATE
- F86 · Last quarter the bank reported · 2024-09-30 · 2024-09-30 · data/features/fct_bank_features.parquet: report_date
- F87 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F88 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
