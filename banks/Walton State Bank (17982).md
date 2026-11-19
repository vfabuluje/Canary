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
written_at: "2026-11-18T19:56:58"
writer_model: "claude-opus-5-5"
checked: true
---

# Walton State Bank (cert 17982)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

As of 2023-06-30, Walton State Bank, a small Kansas bank, ranked 52 out of 4,714 FDIC-insured banks on Canary's risk score, which places it in the 98.9th percentile. That put it on Canary's watchlist, which covers the 2% of banks with the highest scores. The main concerns were its very small size, at $11.0 million in total assets, and a share of seriously overdue or non-earning loans of 4.1%, far above the national median of 0.3%. On the other side, its risk-based capital ratios (capital measured against how risky its assets are) were well above the national median.

## Warning signs in the data

Capital, the cushion that absorbs losses, was thin on simple measures: equity was 7.8% of assets against a national median of 9.2%, and the leverage ratio (core capital as a share of average assets) was 7.8% against a median of 10.5%. Measured against risk-weighted assets, though, capital looked strong, with a Tier 1 risk-based capital ratio of 23.1% versus a median of 14.2%.

Credit quality was the weakest area: loans 90 or more days past due or not accruing interest were 4.1% of loans, against a national median of 0.3%. Nonaccrual assets and foreclosed property were 1.6% of assets versus a median of 0.1%, and the Texas ratio (troubled assets against capital plus reserves) was 19.0% versus a median of 1.8%. Profitability was weak, with return on assets of 0.4% against a median of 1.0% and an efficiency ratio (operating costs as a share of revenue) of 86.3% against 65.5%.

The bank was shrinking, with deposits down -13.0% and assets down -11.8% over the past four quarters, compared with national medians of -1.1% and 2.2%. Its funding otherwise looked steady: uninsured deposits were 14.4% of deposits versus a median of 23.6%, and cash was 20.1% of assets versus 5.3%. Unrealized losses on bonds held to maturity (bonds the bank plans to keep until they pay off) equaled 31.9% of equity, while the national median was 0.0%.

## Understanding the score

On 2023-06-30 Walton State Bank ranked 52 of 4,714 banks, in the 98.9th percentile on a scale where higher means riskier. It was flagged on the watchlist, the top 2% of scores, which held 95 banks that quarter.

The five features that pushed the score up most were core deposits (stable, everyday deposits) at 92.0% of assets, adding +0.730; total assets of $11.0 million, adding +0.586; seriously overdue or non-earning loans at 4.1% of loans, adding +0.452; construction loans at 0.0% of loans, adding +0.226; and loans at 27.1% of deposits, adding +0.198.

The five features that pulled the score down most were the Tier 1 risk-based capital ratio at 23.1%, at -0.894; interest expense at 0.3% of assets, at -0.792; the total risk-based capital ratio at 24.4%, at -0.544; the efficiency ratio at 86.3%, at -0.285; and return on equity at 5.9%, at -0.282.

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

## How its ratios moved

Each ratio was compared with its own range over the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios, and 13 of 30 ratios sat outside that range, with the 6 furthest outside shown in the table. The model rated the bank about the same as a year earlier, when it sat in the 99.8th percentile, compared with the 98.9th percentile at rank 52 on 2023-06-30.

The leverage ratio was 7.8%, above its prior range of 6.1% to 7.3%, and contributed +0.060 model log-odds units, which pushed the score up. Equity as a share of assets was 7.8%, above its prior range of 6.0% to 7.4%, yet its contribution of -0.029 had little effect on the score. The Tier 1 risk-based capital ratio was 23.1%, above its prior range of 18.1% to 22.3%, and its contribution of -0.894 pushed the score down. The total risk-based capital ratio was 24.4%, above its prior range of 19.3% to 23.6%, and its contribution of -0.544 pushed the score down.

The Texas ratio was 19.0%, below its prior range of 23.2% to 35.1% after a one-quarter change of -12.8 pp, and its contribution of -0.245 pushed the score down. Nonaccrual assets and foreclosed property were 1.6% of assets, below their prior range of 1.8% to 2.4%, and their contribution of -0.103 pushed the score down. So although these ratios moved outside their own past ranges, most of those moves were improvements that the model read as lowering the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the leverage ratio (core capital as a share of average assets) | 7.8% | 6.1% to 7.3% | prior 12 quarters | +1.0 pp | +1.5 pp | +0.060 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 19.0% | 23.2% to 35.1% | prior 12 quarters | -12.8 pp | -13.8 pp | -0.245 | pushed the score down |
| equity as a share of assets | 7.8% | 6.0% to 7.4% | prior 12 quarters | +0.8 pp | +1.6 pp | -0.029 | little effect on the score |
| nonaccrual assets and foreclosed property, as a share of assets | 1.6% | 1.8% to 2.4% | prior 12 quarters | -0.8 pp | -0.6 pp | -0.103 | pushed the score down |
| the Tier 1 risk-based capital ratio | 23.1% | 18.1% to 22.3% | prior 12 quarters | +3.1 pp | +5.0 pp | -0.894 | pushed the score down |
| the total risk-based capital ratio | 24.4% | 19.3% to 23.6% | prior 12 quarters | +3.1 pp | +5.1 pp | -0.544 | pushed the score down |

13 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it was flagged, and what happened

In hindsight, this flag turned out to be a false alarm. The bank kept reporting in every later quarter in our data and was never flagged again, with its rank already easing to 620 by 2023-09-30. Its high score had rested largely on its very small size and a cluster of overdue loans, while its strong risk-based capital pulled in the other direction.

## What happened next

In hindsight, the bank dropped off the watchlist and stayed off it: its rank was 620 on 2023-09-30, 1,470 on 2023-12-31 and 2,241 on 2024-03-31. It ranked 1,902 on 2024-06-30, 877 on 2024-09-30 and 510 on 2024-12-31, still not flagged. Later ranks were 708 on 2025-03-31, 529 on 2025-06-30, 1,462 on 2025-09-30 and 1,029 on 2025-12-31. The bank was still reporting at the latest quarters in our data, ranking 2,650 on 2026-03-31 and 3,059 on 2026-06-30, not flagged.

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
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2023-06-30 · 4.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2023-06-30 · 0.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2023-06-30 · 1.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2023-06-30 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2023-06-30 · 19.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2023-06-30 · 1.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2023-06-30 · 0.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2023-06-30 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2023-06-30 · 86.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2023-06-30 · 65.5% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2023-06-30 · 14.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2023-06-30 · 23.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2023-06-30 · 20.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2023-06-30 · 5.3% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2023-06-30 · 31.9% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2023-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2023-06-30 · $11.0 million · data/features/fct_bank_features.parquet: log_total_assets
- F71 · Bank: asset growth over the past four quarters · 2023-06-30 · -11.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2023-06-30 · 2.2% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2023-06-30 · -13.0% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2023-06-30 · -1.1% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
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
- F101 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2023-06-30 · 7.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F102 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 6.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F103 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 7.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F106 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2023-06-30 · +0.060 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F107 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2023-06-30 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F108 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2023-06-30 · 19.0% · data/features/fct_bank_features.parquet: texas_ratio
- F109 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 23.2% · data/features/fct_bank_features.parquet: texas_ratio
- F110 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 35.1% · data/features/fct_bank_features.parquet: texas_ratio
- F111 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2023-06-30 · -12.8 pp · data/features/fct_bank_features.parquet: texas_ratio
- F113 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2023-06-30 · -0.245 · data/analyst/scores.parquet: feature texas_ratio contribution
- F114 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2023-06-30 · pushed the score down · data/analyst/scores.parquet: feature texas_ratio contribution
- F115 · Trend: equity as a share of assets, value at the as-of quarter · 2023-06-30 · 7.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F116 · Trend: equity as a share of assets, lowest value in the comparison window · n/a · 6.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F117 · Trend: equity as a share of assets, highest value in the comparison window · n/a · 7.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F120 · Trend: equity as a share of assets, contribution to the score (model log-odds units) · 2023-06-30 · -0.029 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F121 · Trend: equity as a share of assets, what the model did with it · 2023-06-30 · little effect on the score · data/analyst/scores.parquet: feature equity_to_assets contribution
- F122 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2023-06-30 · 1.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F123 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 1.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F124 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 2.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F127 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2023-06-30 · -0.103 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F128 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2023-06-30 · pushed the score down · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F129 · Trend: the Tier 1 risk-based capital ratio, value at the as-of quarter · 2023-06-30 · 23.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F130 · Trend: the Tier 1 risk-based capital ratio, lowest value in the comparison window · n/a · 18.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F131 · Trend: the Tier 1 risk-based capital ratio, highest value in the comparison window · n/a · 22.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F134 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2023-06-30 · -0.894 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F135 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2023-06-30 · pushed the score down · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F136 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2023-06-30 · 24.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F137 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 19.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F138 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 23.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F141 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2023-06-30 · -0.544 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F142 · Trend: the total risk-based capital ratio, what the model did with it · 2023-06-30 · pushed the score down · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F143 · Trend: ratios outside their own prior range · 2023-06-30 · 13 · data/features/fct_bank_features.parquet
- F144 · Trend: ratios shown in the table (the furthest outside their prior range) · 2023-06-30 · 6 · data/features/fct_bank_features.parquet
- F145 · Trend: ratios compared with their own prior range · 2023-06-30 · 30 · data/features/fct_bank_features.parquet
- F146 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F147 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F148 · Percentile a year earlier (100 = highest risk) · 2022-06-30 · 99.8% · data/analyst/scores.parquet: percentile
- F149 · Trend: how the model's rating compares with a year earlier · 2023-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
