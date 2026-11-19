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
written_at: "2026-11-18T19:57:47"
writer_model: "claude-opus-5-5"
checked: true
---

# Glen Burnie Mutual Sb (cert 27567)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

As of 2022-12-31, Glen Burnie Mutual Sb, a bank in MD, ranked 36 out of 4,773 FDIC-insured banks on Canary's risk score, with a percentile of 99.3% on a scale where higher means riskier. That put it on Canary's watchlist, which covers the top 2% of banks and held 96 banks that quarter. Its cushion of equity was 7.6% of assets against a national median of 9.0%, and its profits were thin, with return on assets of 0.1% against a median of 1.0%. At the same time, it relied heavily on stable deposits and had few uninsured deposits.

## Warning signs in the data

On capital, the bank's equity (the owners' cushion against losses) was 7.6% of assets versus a national median of 9.0%, and its leverage ratio (core capital as a share of average assets) was 7.6% versus a median of 10.3%. By contrast, its Tier 1 risk-based capital ratio, which weighs capital against how risky the assets are, was 16.1%, above the median of 14.2%. On credit quality, loans 90+ days past due or not accruing interest were 0.7% of loans versus a median of 0.2%, and its Texas ratio (troubled assets against capital plus reserves) was 7.2% versus 1.8%, both above typical but still low in absolute terms. Its loan-loss reserves, money set aside for bad loans, were 0.4% of loans, well below the median of 1.2%.

Earnings were weak: the net interest margin (the spread earned on lending and investing) was 1.0% against a median of 3.4%, and the efficiency ratio (operating costs as a share of revenue) was 88.5% against 65.1%. Interest expense ran at 2.2% of assets, far above the median of 0.3%.

Funding looked steady: core deposits (stable, everyday deposits) were 91.7% of assets versus a median of 81.6%, uninsured deposits were 5.5% of deposits versus 25.5%, and cash was 9.9% of assets versus 5.2%. Loans were 86.2% of deposits, above the median of 72.5%. Unrealized losses on bonds held to maturity were 0.8% of equity versus a median of 0.0%, while losses on bonds available for sale were 0.0% versus a median of 18.6%, as securities made up only 1.4% of assets.

## Understanding the score

As of 2022-12-31, the bank ranked 36 out of 4,773 banks, with a percentile of 99.3% on a scale where higher means riskier. That placed it on the watchlist, the top 2% of banks, which numbered 96 that quarter.

Five features pushed the score up the most. Securities were only 1.4% of assets, contributing +0.520. Core deposits were 91.7% of assets, contributing +0.430. Commercial real estate loans were 0.1% of loans, contributing +0.359. Interest expense was 2.2% of assets, contributing +0.281. The leverage ratio was 7.6%, contributing +0.136.

Five features pulled the score down the most. The Tier 1 risk-based capital ratio of 16.1% contributed -1.006, and the Texas ratio of 7.2% contributed -0.818. Loans 90+ days past due or not accruing interest at 0.7% of loans contributed -0.401, return on equity (profit as a share of equity) of 1.1% contributed -0.365, and the total risk-based capital ratio of 16.8% contributed -0.321.

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

## How its ratios moved

Canary compared 30 of the bank's ratios with their own prior range, mostly the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of these, 10 sat outside their prior range, and the 6 furthest outside are discussed here. The model rated the bank about the same as a year earlier: its percentile was 99.9% at 2021-12-31 and 99.3% at 2022-12-31.

Cash fell to 9.9% of assets, below its prior range of 15.6% to 22.7%, with a one-quarter change of -10.4 pp; its contribution of +0.082 pushed the score up. The efficiency ratio rose to 88.5%, above its prior range of 71.7% to 80.5% with a four-quarter change of +8.3 pp, yet its contribution of -0.115 pushed the score down. Return on equity slipped to 1.1%, below its prior range of 2.4% to 4.2%, yet its contribution of -0.365 pushed the score down.

Asset growth over the past four quarters was 1.6%, below its prior range of 2.2% to 4.6%, yet its contribution of -0.051 pushed the score down. Deposit growth over the past four quarters was 1.6%, below its prior range of 2.1% to 4.7%, yet its contribution of -0.167 pushed the score down. Construction loans were 4.0% of loans, above their prior range of 2.0% to 3.7%, yet their contribution of -0.229 pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 88.5% | 71.7% to 80.5% | same quarter, prior 3 years | n/a | +8.3 pp | -0.115 | pushed the score down |
| cash as a share of assets | 9.9% | 15.6% to 22.7% | prior 12 quarters | -10.4 pp | -9.1 pp | +0.082 | pushed the score up |
| return on equity (profit as a share of equity) | 1.1% | 2.4% to 4.2% | same quarter, prior 3 years | n/a | -3.1 pp | -0.365 | pushed the score down |
| asset growth over the past four quarters | 1.6% | 2.2% to 4.6% | prior 12 quarters | -1.4 pp | -2.5 pp | -0.051 | pushed the score down |
| deposit growth over the past four quarters | 1.6% | 2.1% to 4.7% | prior 12 quarters | -1.5 pp | -2.5 pp | -0.167 | pushed the score down |
| construction loans as a share of loans | 4.0% | 2.0% to 3.7% | prior 12 quarters | +0.3 pp | +0.7 pp | -0.229 | pushed the score down |

10 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it was flagged, and what happened

In hindsight, this was a false alarm: the bank was flagged for its thin profits, high funding costs and modest leverage ratio, but it kept reporting and was not flagged again in the quarters that followed. By 2023-03-31 it had moved to rank 101, off the watchlist, and by 2026-06-30 it ranked 209, still not flagged.

## What happened next

With hindsight, the bank's rank eased away from the top of the list after the as-of quarter: 101 at 2023-03-31, 108 at 2023-06-30, 199 at 2023-09-30 and 273 at 2023-12-31, none of them flagged. It stayed off the watchlist through 2024, ranking 289 at 2024-03-31, 541 at 2024-06-30, 189 at 2024-09-30 and 426 at 2024-12-31. In 2025 it ranked 253 at 2025-03-31, 141 at 2025-06-30, 322 at 2025-09-30 and 255 at 2025-12-31, all not flagged. The bank was still reporting in the latest quarters, ranking 266 at 2026-03-31 and 209 at 2026-06-30, again not flagged.

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
- F6 · National rank (1 = highest score) · 2022-12-31 · 36 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2022-12-31 · 4,773 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2022-12-31 · 99.3% · data/analyst/scores.parquet: percentile
- F10 · On the watchlist · 2022-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2022-12-31 · 96 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2022-12-31 · 7.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2022-12-31 · 9.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2022-12-31 · 7.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2022-12-31 · 10.3% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2022-12-31 · 16.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2022-12-31 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
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
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2022-12-31 · 88.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2022-12-31 · 65.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2022-12-31 · 2.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2022-12-31 · 0.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: loans as a share of deposits · 2022-12-31 · 86.2% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2022-12-31 · 72.5% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2022-12-31 · 5.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2022-12-31 · 25.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2022-12-31 · 91.7% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2022-12-31 · 81.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2022-12-31 · 9.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2022-12-31 · 5.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2022-12-31 · 0.8% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2022-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2022-12-31 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2022-12-31 · 18.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2022-12-31 · 1.4% · data/features/fct_bank_features.parquet: securities_to_assets
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
- F87 · Rank in a later quarter (2023-09-30), not flagged · 2023-09-30 · 199 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F88 · Rank in a later quarter (2023-12-31), not flagged · 2023-12-31 · 273 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F89 · Rank in a later quarter (2024-03-31), not flagged · 2024-03-31 · 289 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F90 · Rank in a later quarter (2024-06-30), not flagged · 2024-06-30 · 541 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F91 · Rank in a later quarter (2024-09-30), not flagged · 2024-09-30 · 189 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F92 · Rank in a later quarter (2024-12-31), not flagged · 2024-12-31 · 426 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F93 · Rank in a later quarter (2025-03-31), not flagged · 2025-03-31 · 253 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F94 · Rank in a later quarter (2025-06-30), not flagged · 2025-06-30 · 141 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F95 · Rank in a later quarter (2025-09-30), not flagged · 2025-09-30 · 322 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F96 · Rank in a later quarter (2025-12-31), not flagged · 2025-12-31 · 255 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F97 · Rank in a later quarter (2026-03-31), not flagged · 2026-03-31 · 266 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F98 · Rank in a later quarter (2026-06-30), not flagged · 2026-06-30 · 209 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F103 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2022-12-31 · 88.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F104 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 71.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 80.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2022-12-31 · +8.3 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2022-12-31 · -0.115 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F108 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F109 · Trend: cash as a share of assets, value at the as-of quarter · 2022-12-31 · 9.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F110 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 15.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F111 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 22.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F112 · Trend: cash as a share of assets, change over one quarter, in percentage points · 2022-12-31 · -10.4 pp · data/features/fct_bank_features.parquet: cash_to_assets
- F114 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2022-12-31 · +0.082 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F115 · Trend: cash as a share of assets, what the model did with it · 2022-12-31 · pushed the score up · data/analyst/scores.parquet: feature cash_to_assets contribution
- F116 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2022-12-31 · 1.1% · data/features/fct_bank_features.parquet: return_on_equity
- F117 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 2.4% · data/features/fct_bank_features.parquet: return_on_equity
- F118 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 4.2% · data/features/fct_bank_features.parquet: return_on_equity
- F120 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2022-12-31 · -0.365 · data/analyst/scores.parquet: feature return_on_equity contribution
- F121 · Trend: return on equity (profit as a share of equity), what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F122 · Trend: asset growth over the past four quarters, value at the as-of quarter · 2022-12-31 · 1.6% · data/features/fct_bank_features.parquet: asset_growth_4q
- F123 · Trend: asset growth over the past four quarters, lowest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: asset_growth_4q
- F124 · Trend: asset growth over the past four quarters, highest value in the comparison window · n/a · 4.6% · data/features/fct_bank_features.parquet: asset_growth_4q
- F127 · Trend: asset growth over the past four quarters, contribution to the score (model log-odds units) · 2022-12-31 · -0.051 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F128 · Trend: asset growth over the past four quarters, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F129 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2022-12-31 · 1.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F130 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · 2.1% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F131 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 4.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F134 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2022-12-31 · -0.167 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F135 · Trend: deposit growth over the past four quarters, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F136 · Trend: construction loans as a share of loans, value at the as-of quarter · 2022-12-31 · 4.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F137 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 2.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F138 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 3.7% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F141 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2022-12-31 · -0.229 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F142 · Trend: construction loans as a share of loans, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F143 · Trend: ratios outside their own prior range · 2022-12-31 · 10 · data/features/fct_bank_features.parquet
- F144 · Trend: ratios shown in the table (the furthest outside their prior range) · 2022-12-31 · 6 · data/features/fct_bank_features.parquet
- F145 · Trend: ratios compared with their own prior range · 2022-12-31 · 30 · data/features/fct_bank_features.parquet
- F146 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F147 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F148 · Percentile a year earlier (100 = highest risk) · 2021-12-31 · 99.9% · data/analyst/scores.parquet: percentile
- F149 · Trend: how the model's rating compares with a year earlier · 2022-12-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
