---
cert: 27567
name: "Glen Burnie Mutual Sb"
as_of: 2022-12-31
rank: 36
n_banks: 4773
percentile: 99.26670856903415
flagged: true
outcome: "false_alarm"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:09:28"
writer_model: "claude-opus-5-5"
checked: true
---

# Glen Burnie Mutual Sb (cert 27567)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

As of 2022-12-31, Glen Burnie Mutual Sb, a bank in MD with $109.6 million in total assets, ranked 36 out of 4,773 banks on Canary's risk score, a percentile of 99.3%. That placed it on the watchlist, which covers the riskiest 2% of banks. Its profile pairs thin profits and a small cushion of core capital with very stable, mostly insured deposits and almost no bond holdings.

## Warning signs in the data

Capital: the leverage ratio (core capital as a share of average assets) was 7.6%, below the national median of 10.3%, and equity was 7.6% of assets against a median of 9.0%. By contrast, its risk-based capital ratios, which weight assets by riskiness, were above the median: Tier 1 at 16.1% versus 14.2%, and total at 16.8% versus 15.3%.

Credit quality: loans 90 or more days late or no longer earning interest were 0.7% of loans, above the median of 0.2%, and the Texas ratio (troubled assets against capital plus reserves) was 7.2% versus 1.8%. Loan-loss reserves, money set aside for bad loans, were 0.4% of loans, well below the median of 1.2%. Earnings were weak: return on assets was 0.1% versus 1.0%, the net interest margin (the spread earned on lending and investing) was 1.0% versus 3.4%, and interest expense was 2.2% of assets versus 0.3%.

Funding and bonds looked steadier: uninsured deposits were only 5.5% of deposits against a median of 25.5%, core deposits were 91.7% of assets versus 81.6%, and cash was 9.9% of assets versus 5.2%. Securities were just 1.4% of assets versus a median of 22.3%, and losses on bonds held to maturity were 0.8% of equity, against a median of 0.0%.

## Understanding the score

On 2022-12-31 the bank ranked 36 of 4,773 banks, a percentile of 99.3% on a 0 to 100 scale where higher means riskier, with a raw score of 0.0930. It was one of 96 banks flagged on the watchlist that quarter, the top 2% by score.

The five factors pushing the score up were: a low share of securities at 1.4% of assets (+0.520), a high share of core deposits at 91.7% of assets (+0.430), very little commercial real estate lending at 0.1% of loans (+0.359), high interest expense at 2.2% of assets (+0.281), and a leverage ratio of 7.6% (+0.136).

The five factors pulling it down were: a Tier 1 risk-based capital ratio of 16.1% (-1.006), a Texas ratio of 7.2% (-0.818), late or non-accruing loans at 0.7% of loans (-0.401), return on equity of 1.1% (-0.365), and a total risk-based capital ratio of 16.8% (-0.321).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2021-03-31 | 11 | 5,044 | ▲ watchlist |
| 2021-06-30 | 11 | 5,015 | ▲ watchlist |
| 2021-09-30 | 8 | 4,979 | ▲ watchlist |
| 2021-12-31 | 7 | 4,904 | ▲ watchlist |
| 2022-03-31 | 32 | 4,861 | ▲ watchlist |
| 2022-06-30 | 31 | 4,838 | ▲ watchlist |
| 2022-09-30 | 33 | 4,813 | ▲ watchlist |
| 2022-12-31 | 36 | 4,773 | ▲ watchlist |

## Why it was flagged, and what happened

In hindsight, this was a false alarm: the bank was flagged because of thin capital, weak earnings and an unusual balance sheet, but it did not fail. By 2023-03-31 its rank had eased to 101 and it was no longer flagged. The model learned mostly from credit-loss failures, which made up 96% of the 539 training-period failures, and this bank's loan losses stayed small.

## What happened next

With hindsight, the bank was never flagged again in any later quarter in our data, with ranks of 108 in Q2 2023, 273 in Q4 2023, 541 in Q2 2024, 426 in Q4 2024 and 255 in Q4 2025. It was still reporting as of 2026-06-30, when it ranked 209 and was not flagged.

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2023-03-31 | 101 | 4,740 |  |
| 2023-06-30 | 108 | 4,714 |  |
| 2023-09-30 | 199 | 4,686 |  |
| 2023-12-31 | 273 | 4,658 |  |
| 2024-03-31 | 289 | 4,640 |  |
| 2024-06-30 | 541 | 4,610 |  |
| 2024-09-30 | 189 | 4,589 |  |
| 2024-12-31 | 426 | 4,560 |  |
| 2025-03-31 | 253 | 4,536 |  |
| 2025-06-30 | 141 | 4,494 |  |
| 2025-09-30 | 322 | 4,452 |  |
| 2025-12-31 | 255 | 4,411 |  |
| 2026-03-31 | 266 | 4,353 |  |
| 2026-06-30 | 209 | 4,313 |  |

## Sources

- F1 · Bank name · n/a · Glen Burnie Mutual Sb · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2022-12-31 · 2022-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · MD · data/raw/financials: STALP
- F5 · Model score · 2022-12-31 · 0.0930 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2022-12-31 · 36 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2022-12-31 · 4,773 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2022-12-31 · 99.3% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2022-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2022-12-31 · 96 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2022-12-31 · 7.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2022-12-31 · 9.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2022-12-31 · 7.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2022-12-31 · 10.3% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2022-12-31 · 16.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2022-12-31 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2022-12-31 · 16.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2022-12-31 · 15.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2022-12-31 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2022-12-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2022-12-31 · 0.4% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2022-12-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2022-12-31 · 7.2% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2022-12-31 · 1.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2022-12-31 · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2022-12-31 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2022-12-31 · 1.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2022-12-31 · 3.4% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2022-12-31 · 2.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2022-12-31 · 0.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2022-12-31 · 5.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2022-12-31 · 25.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2022-12-31 · 91.7% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2022-12-31 · 81.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2022-12-31 · 9.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2022-12-31 · 5.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2022-12-31 · 0.8% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2022-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2022-12-31 · 1.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2022-12-31 · 22.3% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F69 · Bank: total assets · 2022-12-31 · $109.6 million · data/features/fct_bank_features.parquet: log_total_assets
- F75 · Driver up #1: securities as a share of assets, value 1.4%; contribution to the score · 2022-12-31 · +0.520 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F76 · Driver up #2: core deposits as a share of assets, value 91.7%; contribution to the score · 2022-12-31 · +0.430 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F77 · Driver up #3: commercial real estate loans as a share of loans, value 0.1%; contribution to the score · 2022-12-31 · +0.359 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F78 · Driver up #4: annualized interest expense as a share of assets, value 2.2%; contribution to the score · 2022-12-31 · +0.281 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F79 · Driver up #5: the leverage ratio (core capital as a share of average assets), value 7.6%; contribution to the score · 2022-12-31 · +0.136 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 16.1%; contribution to the score · 2022-12-31 · -1.006 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 7.2%; contribution to the score · 2022-12-31 · -0.818 · data/analyst/scores.parquet: feature texas_ratio contribution
- F82 · Driver down #3: loans 90+ days past due or not accruing interest, as a share of loans, value 0.7%; contribution to the score · 2022-12-31 · -0.401 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F83 · Driver down #4: return on equity (profit as a share of equity), value 1.1%; contribution to the score · 2022-12-31 · -0.365 · data/analyst/scores.parquet: feature return_on_equity contribution
- F84 · Driver down #5: the total risk-based capital ratio, value 16.8%; contribution to the score · 2022-12-31 · -0.321 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F85 · Rank in a later quarter (2023-03-31), not flagged · 2023-03-31 · 101 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F86 · Rank in a later quarter (2023-06-30), not flagged · 2023-06-30 · 108 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F88 · Rank in a later quarter (2023-12-31), not flagged · 2023-12-31 · 273 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F90 · Rank in a later quarter (2024-06-30), not flagged · 2024-06-30 · 541 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F92 · Rank in a later quarter (2024-12-31), not flagged · 2024-12-31 · 426 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F96 · Rank in a later quarter (2025-12-31), not flagged · 2025-12-31 · 255 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F98 · Rank in a later quarter (2026-06-30), not flagged · 2026-06-30 · 209 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F99 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F100 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
