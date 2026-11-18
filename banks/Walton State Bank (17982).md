---
cert: 17982
name: "Walton State Bank"
as_of: 2023-06-30
rank: 52
n_banks: 4714
percentile: 98.91811624946966
flagged: true
outcome: "false_alarm"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:08:55"
writer_model: "claude-opus-5-5"
checked: true
---

# Walton State Bank (cert 17982)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

As of 2023-06-30, Walton State Bank, a small Kansas bank, ranked 52 out of 4,714 FDIC-insured banks on Canary's risk score, placing it in the 98.9th percentile. That put it on the watchlist, the top 2% of banks by score, which held 95 banks that quarter. The main concerns in the data were a high share of seriously overdue loans, thin capital measured against total assets, and large unrealized losses on bonds. On the other side, its capital measured against the riskiness of its assets was well above the national median, and it leaned very little on loans relative to deposits.

## Warning signs in the data

Capital, the cushion that absorbs losses, looked mixed as of 2023-06-30. Equity was 7.8% of assets against a national median of 9.2%, and the leverage ratio (core capital as a share of average assets) was 7.8% against a median of 10.5%. By contrast, the Tier 1 risk-based capital ratio, which weighs capital against how risky the assets are, was 23.1% versus a median of 14.2%, and the total risk-based capital ratio was 24.4% versus 15.4%.

Credit quality was the clearest weak spot: loans 90 or more days overdue or no longer earning interest were 4.1% of loans, far above the national median of 0.3%. Nonaccrual assets and foreclosed property were 1.6% of assets versus a median of 0.1%, and the Texas ratio (troubled assets against capital plus reserves) was 19.0% versus 1.8%. Loan-loss reserves, money set aside for expected bad loans, were 1.7% of loans, above the median of 1.2%. Profitability was weak, with return on assets of 0.4% against a median of 1.0% and an efficiency ratio (operating costs as a share of revenue) of 86.3% against 65.5%.

Funding looked steady: core deposits, the stable everyday kind, were 92.0% of assets versus a median of 78.1%, and uninsured deposits were 14.4% of deposits versus 23.6%. Cash was 20.1% of assets against a median of 5.3%, and loans were only 27.1% of deposits against 76.0%. However, unrealized losses on bonds held to maturity, meaning bonds the bank plans to keep until they are repaid, equaled 31.9% of equity, while the national median was 0.0%. The bank was very small, with total assets of $11.0 million against a median of $325.5 million, and it shrank, with assets down -11.8% and deposits down -13.0% over the past four quarters.

## Understanding the score

On 2023-06-30 Walton State Bank ranked 52 of 4,714 banks, in the 98.9th percentile on a scale from 0 to 100 where higher means riskier, with a raw model score of 0.1172. It was flagged on the watchlist, which covers the top 2% of banks, 95 banks that quarter.

The five features pushing the score up most were core deposits as a share of assets at 92.0%, adding +0.730, and total assets of $11.0 million, adding +0.586. Next came seriously overdue or nonaccruing loans at 4.1% of loans, adding +0.452, construction loans at 0.0% of loans, adding +0.226, and loans as a share of deposits at 27.1%, adding +0.198.

The five features pulling the score down most were the Tier 1 risk-based capital ratio at 23.1%, contributing -0.894, and interest expense at 0.3% of assets, contributing -0.792. They were followed by the total risk-based capital ratio at 24.4%, contributing -0.544, the efficiency ratio at 86.3%, contributing -0.285, and return on equity at 5.9%, contributing -0.282.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2021-09-30 | 4 | 4,979 | ▲ watchlist |
| 2021-12-31 | 6 | 4,904 | ▲ watchlist |
| 2022-03-31 | 9 | 4,861 | ▲ watchlist |
| 2022-06-30 | 13 | 4,838 | ▲ watchlist |
| 2022-09-30 | 37 | 4,813 | ▲ watchlist |
| 2022-12-31 | 6 | 4,773 | ▲ watchlist |
| 2023-03-31 | 90 | 4,740 | ▲ watchlist |
| 2023-06-30 | 52 | 4,714 | ▲ watchlist |

## Why it was flagged, and what happened

In hindsight, this flag was a false alarm: the bank did not fail and kept reporting in later quarters. By 2023-09-30 its rank had fallen to 620 and it was no longer flagged.

The flag rested largely on a high share of troubled loans combined with the bank's very small size, patterns the model learned from past failures, of which 96% were credit-loss failures. Its strong risk-based capital, plentiful cash and low reliance on lending appear to have mattered more than the troubled-loan figures suggested.

## What happened next

Looking back with hindsight, Walton State Bank was never flagged again in the quarters after the as-of date. Its rank was 620 on 2023-09-30, 1,470 on 2023-12-31, 2,241 on 2024-03-31 and 1,902 on 2024-06-30. It then ranked 877 on 2024-09-30, 510 on 2024-12-31, 708 on 2025-03-31 and 529 on 2025-06-30. Later ranks were 1,462 on 2025-09-30, 1,029 on 2025-12-31, 2,650 on 2026-03-31 and 3,059 on 2026-06-30, none of them flagged.

The bank was still reporting as of 2026-06-30, the latest quarter in our data.

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2023-09-30 | 620 | 4,686 |  |
| 2023-12-31 | 1,470 | 4,658 |  |
| 2024-03-31 | 2,241 | 4,640 |  |
| 2024-06-30 | 1,902 | 4,610 |  |
| 2024-09-30 | 877 | 4,589 |  |
| 2024-12-31 | 510 | 4,560 |  |
| 2025-03-31 | 708 | 4,536 |  |
| 2025-06-30 | 529 | 4,494 |  |
| 2025-09-30 | 1,462 | 4,452 |  |
| 2025-12-31 | 1,029 | 4,411 |  |
| 2026-03-31 | 2,650 | 4,353 |  |
| 2026-06-30 | 3,059 | 4,313 |  |

## Sources

- F1 · Bank name · n/a · Walton State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2023-06-30 · 2023-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KS · data/raw/financials: STALP
- F5 · Model score · 2023-06-30 · 0.1172 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2023-06-30 · 52 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2023-06-30 · 4,714 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2023-06-30 · 98.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2023-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2023-06-30 · 95 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2023-06-30 · 7.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2023-06-30 · 9.2% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2023-06-30 · 7.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2023-06-30 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2023-06-30 · 23.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2023-06-30 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2023-06-30 · 24.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2023-06-30 · 15.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2023-06-30 · 4.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2023-06-30 · 0.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2023-06-30 · 1.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2023-06-30 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2023-06-30 · 1.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2023-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2023-06-30 · 19.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2023-06-30 · 1.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2023-06-30 · 0.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2023-06-30 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2023-06-30 · 86.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2023-06-30 · 65.5% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F49 · Bank: loans as a share of deposits · 2023-06-30 · 27.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2023-06-30 · 76.0% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2023-06-30 · 14.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2023-06-30 · 23.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2023-06-30 · 92.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2023-06-30 · 78.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2023-06-30 · 20.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2023-06-30 · 5.3% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2023-06-30 · 31.9% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2023-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2023-06-30 · $11.0 million · data/features/fct_bank_features.parquet: log_total_assets
- F70 · National median: total assets · 2023-06-30 · $325.5 million · data/features/fct_bank_features.parquet: log_total_assets (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2023-06-30 · -11.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F73 · Bank: deposit growth over the past four quarters · 2023-06-30 · -13.0% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F75 · Driver up #1: core deposits as a share of assets, value 92.0%; contribution to the score · 2023-06-30 · +0.730 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F76 · Driver up #2: total assets, value $11.0 million; contribution to the score · 2023-06-30 · +0.586 · data/analyst/scores.parquet: feature log_total_assets contribution
- F77 · Driver up #3: loans 90+ days past due or not accruing interest, as a share of loans, value 4.1%; contribution to the score · 2023-06-30 · +0.452 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F78 · Driver up #4: construction loans as a share of loans, value 0.0%; contribution to the score · 2023-06-30 · +0.226 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F79 · Driver up #5: loans as a share of deposits, value 27.1%; contribution to the score · 2023-06-30 · +0.198 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 23.1%; contribution to the score · 2023-06-30 · -0.894 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 0.3%; contribution to the score · 2023-06-30 · -0.792 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: the total risk-based capital ratio, value 24.4%; contribution to the score · 2023-06-30 · -0.544 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F83 · Driver down #4: the efficiency ratio (operating costs as a share of revenue), value 86.3%; contribution to the score · 2023-06-30 · -0.285 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F84 · Driver down #5: return on equity (profit as a share of equity), value 5.9%; contribution to the score · 2023-06-30 · -0.282 · data/analyst/scores.parquet: feature return_on_equity contribution
- F85 · Rank in a later quarter (2023-09-30), not flagged · 2023-09-30 · 620 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F86 · Rank in a later quarter (2023-12-31), not flagged · 2023-12-31 · 1,470 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F87 · Rank in a later quarter (2024-03-31), not flagged · 2024-03-31 · 2,241 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F88 · Rank in a later quarter (2024-06-30), not flagged · 2024-06-30 · 1,902 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F89 · Rank in a later quarter (2024-09-30), not flagged · 2024-09-30 · 877 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F90 · Rank in a later quarter (2024-12-31), not flagged · 2024-12-31 · 510 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F91 · Rank in a later quarter (2025-03-31), not flagged · 2025-03-31 · 708 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F92 · Rank in a later quarter (2025-06-30), not flagged · 2025-06-30 · 529 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F93 · Rank in a later quarter (2025-09-30), not flagged · 2025-09-30 · 1,462 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F94 · Rank in a later quarter (2025-12-31), not flagged · 2025-12-31 · 1,029 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F95 · Rank in a later quarter (2026-03-31), not flagged · 2026-03-31 · 2,650 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F96 · Rank in a later quarter (2026-06-30), not flagged · 2026-06-30 · 3,059 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F97 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
