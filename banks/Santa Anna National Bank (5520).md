---
cert: 5520
name: "Santa Anna National Bank"
as_of: 2025-03-31
rank: 84
n_banks: 4536
percentile: 98.17019400352733
flagged: true
outcome: "missed"
after_test_window: false
failure_date: 2025-06-27
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:45:23"
writer_model: "claude-opus-5-5"
checked: true
---

# Santa Anna National Bank (cert 5520)

*Hindsight: failed 2025-06-27. Canary did not flag it.*

## Summary

As of 2025-03-31, Santa Anna National Bank, a small Texas bank, ranked 84 out of 4,536 banks on Canary's risk score, a percentile of 98.2%, where higher means riskier. That put it on the watchlist, which covers the riskiest 2% of banks. The biggest factor raising its score was large paper losses on bonds it holds for possible sale, equal to 40.8% of its equity (the owners' cushion), against a national median of 9.3%. Its loan problems were small and its profits were strong, which held the score down.

## Warning signs in the data

Capital, the cushion that absorbs losses, was thinner than at most banks: equity was 6.5% of assets against a national median of 9.9%. Its leverage ratio (core capital as a share of average assets) was 8.6%, below the national median of 10.7%. Unrealized losses on bonds available for sale equaled 40.8% of equity, far above the national median of 9.3%, and securities made up 29.5% of assets against a median of 18.3%.

Credit quality looked close to normal: loans 90 or more days past due or not accruing interest were 0.5% of loans, near the national median of 0.4%. The Texas ratio, which compares troubled assets with capital plus reserves, was 3.7%, a little above the median of 2.5% but still low.

On funding, uninsured deposits (balances above the government insurance limit) were 29.5% of deposits against a median of 23.9%, and volatile funding was 14.6% of assets against a median of 8.6%. Cash was 3.7% of assets, below the median of 6.9%. The bank also grew fast for its $76.9 million size, with assets up 26.1% and deposits up 33.2% over the past four quarters, against medians of 3.8% and 4.6%.

## Understanding the score

On 2025-03-31 the bank ranked 84 of 4,536 banks, a percentile of 98.2% on a 0 to 100 scale where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks by score and contained 91 banks that quarter.

Five factors pushed the score up most: losses on bonds available for sale at 40.8% of equity (+1.665), the efficiency ratio, operating costs as a share of revenue, at 52.9% (+0.354), and deposit growth over the past four quarters at 33.2% (+0.274). The other two were commercial real estate loans at 6.0% of loans (+0.174) and loans as a share of deposits at 56.9% (+0.119).

Five factors pulled the score down most: the Texas ratio at 3.7% (-1.296), the Tier 1 risk-based capital ratio, a core capital measure whose value is not shown (-0.914), and return on equity at 27.6% (-0.439). The others were loans 90 or more days past due or not accruing at 0.5% of loans (-0.304) and return on assets at 1.7% (-0.281).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2023-06-30 | 525 | 4,714 |  |
| 2023-09-30 | 429 | 4,686 |  |
| 2023-12-31 | 346 | 4,658 |  |
| 2024-03-31 | 282 | 4,640 |  |
| 2024-06-30 | 388 | 4,610 |  |
| 2024-09-30 | 191 | 4,589 |  |
| 2024-12-31 | 297 | 4,560 |  |
| 2025-03-31 | 84 | 4,536 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own history: most against the prior 12 quarters, and year-to-date ratios against the same quarter in the prior 3 years. Of 28 ratios compared, 9 sat outside their own prior range, and the 6 furthest outside are discussed here. The bank's percentile rose from 93.9% a year earlier to 98.2%, at rank 84, and the model rated it riskier than a year earlier.

Return on equity was 27.6%, above its prior range of 16.4% to 19.6% after rising +8.1 pp over four quarters, yet it contributed -0.439 model log-odds units and pushed the score down. Return on assets was 1.7%, just above its prior range of 1.4% to 1.6%, but it contributed -0.281 and pushed the score down. The efficiency ratio was 52.9%, below its prior range of 56.0% to 60.5% after a -7.6 pp change, and it contributed +0.354 and pushed the score up.

The leverage ratio was 8.6%, below its prior range of 8.9% to 11.2% after a -1.9 pp change over four quarters, yet it contributed -0.082 and pushed the score down. Interest expense was 1.9% of assets, above its prior range of 0.2% to 1.7%, but it contributed -0.101 and pushed the score down. Construction loans were 0.6% of loans, below their prior range of 0.9% to 1.5%, and contributed +0.038, which had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 27.6% | 16.4% to 19.6% | same quarter, prior 3 years | n/a | +8.1 pp | -0.439 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 52.9% | 56.0% to 60.5% | same quarter, prior 3 years | n/a | -7.6 pp | +0.354 | pushed the score up |
| construction loans as a share of loans | 0.6% | 0.9% to 1.5% | prior 12 quarters | -0.9 pp | -0.9 pp | +0.038 | little effect on the score |
| return on assets (profit as a share of assets) | 1.7% | 1.4% to 1.6% | same quarter, prior 3 years | n/a | +0.2 pp | -0.281 | pushed the score down |
| the leverage ratio (core capital as a share of average assets) | 8.6% | 8.9% to 11.2% | prior 12 quarters | -0.3 pp | -1.9 pp | -0.082 | pushed the score down |
| annualized interest expense as a share of assets | 1.9% | 0.2% to 1.7% | same quarter, prior 3 years | n/a | +0.2 pp | -0.101 | pushed the score down |

9 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why the model missed it

In hindsight, the bank failed on 2025-06-27. The model did flag it at Q1 2025, but that quarter falls after the 2016-2024 test period, so the flag is not counted in the reported results. That is why this case is recorded as missed in the model's measured track record, even though the bank sat on the watchlist in its final reported quarter, 2025-03-31.

## What happened next

In hindsight, the last quarter the bank reported was 2025-03-31, so no later ranks exist for it. The bank failed on 2025-06-27.

## Sources

- F3 · As-of quarter · 2025-03-31 · 2025-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · TX · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2025-03-31 · 84 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2025-03-31 · 4,536 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2025-03-31 · 98.2% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2025-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2025-03-31 · 91 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2025-03-31 · 6.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2025-03-31 · 9.9% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2025-03-31 · 8.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2025-03-31 · 10.7% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2025-03-31 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2025-03-31 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2025-03-31 · 3.7% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2025-03-31 · 2.5% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2025-03-31 · 29.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2025-03-31 · 23.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: volatile funding as a share of assets · 2025-03-31 · 14.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F56 · National median: volatile funding as a share of assets · 2025-03-31 · 8.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2025-03-31 · 3.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2025-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2025-03-31 · 40.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2025-03-31 · 9.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F63 · Bank: securities as a share of assets · 2025-03-31 · 29.5% · data/features/fct_bank_features.parquet: securities_to_assets
- F64 · National median: securities as a share of assets · 2025-03-31 · 18.3% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F65 · Bank: total assets · 2025-03-31 · $76.9 million · data/features/fct_bank_features.parquet: log_total_assets
- F67 · Bank: asset growth over the past four quarters · 2025-03-31 · 26.1% · data/features/fct_bank_features.parquet: asset_growth_4q
- F68 · National median: asset growth over the past four quarters · 2025-03-31 · 3.8% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F69 · Bank: deposit growth over the past four quarters · 2025-03-31 · 33.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F70 · National median: deposit growth over the past four quarters · 2025-03-31 · 4.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F71 · Driver up #1: losses on bonds available for sale, as a share of equity, value 40.8%; contribution to the score · 2025-03-31 · +1.665 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F72 · Driver up #2: the efficiency ratio (operating costs as a share of revenue), value 52.9%; contribution to the score · 2025-03-31 · +0.354 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F73 · Driver up #3: deposit growth over the past four quarters, value 33.2%; contribution to the score · 2025-03-31 · +0.274 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F74 · Driver up #4: commercial real estate loans as a share of loans, value 6.0%; contribution to the score · 2025-03-31 · +0.174 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F75 · Driver up #5: loans as a share of deposits, value 56.9%; contribution to the score · 2025-03-31 · +0.119 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F76 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 3.7%; contribution to the score · 2025-03-31 · -1.296 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver down #2: the Tier 1 risk-based capital ratio; contribution to the score · 2025-03-31 · -0.914 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F78 · Driver down #3: return on equity (profit as a share of equity), value 27.6%; contribution to the score · 2025-03-31 · -0.439 · data/analyst/scores.parquet: feature return_on_equity contribution
- F79 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 0.5%; contribution to the score · 2025-03-31 · -0.304 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F80 · Driver down #5: return on assets (profit as a share of assets), value 1.7%; contribution to the score · 2025-03-31 · -0.281 · data/analyst/scores.parquet: feature return_on_assets contribution
- F81 · Failure date · 2025-06-27 · 2025-06-27 · data/raw/failures: FAILDATE
- F82 · Flagged at Q1 2025, after the 2016-2024 test period (not counted in the reported results) · 2025-03-31 · 2025-03-31 · data/analyst/scores.parquet: flagged
- F83 · Last quarter the bank reported · 2025-03-31 · 2025-03-31 · data/features/fct_bank_features.parquet: report_date
- F88 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2025-03-31 · 27.6% · data/features/fct_bank_features.parquet: return_on_equity
- F89 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 16.4% · data/features/fct_bank_features.parquet: return_on_equity
- F90 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 19.6% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2025-03-31 · +8.1 pp · data/features/fct_bank_features.parquet: return_on_equity
- F92 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2025-03-31 · -0.439 · data/analyst/scores.parquet: feature return_on_equity contribution
- F93 · Trend: return on equity (profit as a share of equity), what the model did with it · 2025-03-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F94 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2025-03-31 · 52.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 56.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F96 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 60.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2025-03-31 · -7.6 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2025-03-31 · +0.354 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2025-03-31 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F100 · Trend: construction loans as a share of loans, value at the as-of quarter · 2025-03-31 · 0.6% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F101 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F102 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 1.5% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F105 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2025-03-31 · +0.038 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F106 · Trend: construction loans as a share of loans, what the model did with it · 2025-03-31 · little effect on the score · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F107 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2025-03-31 · 1.7% · data/features/fct_bank_features.parquet: return_on_assets
- F108 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.6% · data/features/fct_bank_features.parquet: return_on_assets
- F111 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2025-03-31 · -0.281 · data/analyst/scores.parquet: feature return_on_assets contribution
- F112 · Trend: return on assets (profit as a share of assets), what the model did with it · 2025-03-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F113 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2025-03-31 · 8.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F114 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 8.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F115 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 11.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F117 · Trend: the leverage ratio (core capital as a share of average assets), change over four quarters, in percentage points · 2025-03-31 · -1.9 pp · data/features/fct_bank_features.parquet: leverage_ratio
- F118 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2025-03-31 · -0.082 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F119 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2025-03-31 · pushed the score down · data/analyst/scores.parquet: feature leverage_ratio contribution
- F120 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2025-03-31 · 1.9% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F121 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F122 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F124 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2025-03-31 · -0.101 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F125 · Trend: annualized interest expense as a share of assets, what the model did with it · 2025-03-31 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F126 · Trend: ratios outside their own prior range · 2025-03-31 · 9 · data/features/fct_bank_features.parquet
- F127 · Trend: ratios shown in the table (the furthest outside their prior range) · 2025-03-31 · 6 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios compared with their own prior range · 2025-03-31 · 28 · data/features/fct_bank_features.parquet
- F129 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F130 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F131 · Percentile a year earlier (100 = highest risk) · 2024-03-31 · 93.9% · data/analyst/scores.parquet: percentile
- F132 · Trend: how the model's rating compares with a year earlier · 2025-03-31 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
