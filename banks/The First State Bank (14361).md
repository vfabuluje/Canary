---
cert: 14361
name: "The First State Bank"
as_of: 2020-03-31
rank: 1
n_banks: 5182
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2020-04-03
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:48:12"
writer_model: "claude-opus-5-5"
checked: true
---

# The First State Bank (cert 14361)

*Hindsight: failed 2020-04-03. Canary flagged it 4 quarters ahead.*

## Summary

As of 2020-03-31, The First State Bank, a West Virginia bank, ranked 1 out of 5,182 banks on Canary's risk score, which places it in the 100.0th percentile, where higher means riskier. It was on the watchlist, which covers the 2% of banks with the highest scores. Its capital cushion was very thin, with equity (the owners' stake) at 0.6% of assets against a national median of 11.4%. Problem loans were also heavy, with 26.7% of loans seriously late or not paying interest, compared with a national median of 0.6%.

## Warning signs in the data

Capital, the money a bank has to absorb losses, was far below typical levels as of 2020-03-31. Equity was 0.6% of assets versus a national median of 11.4%, and the leverage ratio (core capital as a share of average assets) was 0.3% versus 10.9%. The Tier 1 risk-based capital ratio, which weighs assets by riskiness, was 0.4% against a median of 14.6%, and the total risk-based capital ratio was 1.7% against 15.7%.

Credit quality was weak: loans 90 or more days past due or not accruing interest made up 26.7% of loans, versus a national median of 0.6%. Nonaccrual assets and foreclosed property were 26.0% of assets, against a median of 0.4%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 1704.3%, far above the median of 3.8%. The bank was losing money, with a return on assets of -4.1% compared with a median of 0.9%.

On funding, brokered deposits (money placed through middlemen) were 4.2% of deposits versus a median of 0.0%, while uninsured deposits were low at 3.4% versus 19.4%, and cash was 15.9% of assets versus 7.8%. Unrealized losses on bonds available for sale were -40.1% of equity, much deeper than the national median of -0.8%.

## Understanding the score

As of 2020-03-31, the bank ranked 1 of 5,182 banks, the 100.0th percentile on a scale of 0 to 100 where higher means riskier. That put it on the watchlist, which held 104 banks that quarter, the top 2% by score.

Five features pushed the score up the most. The Tier 1 risk-based capital ratio of 0.4% added +2.093, and return on equity (profit as a share of the owners' stake) of -406.7% added +1.374. The Texas ratio of 1704.3% added +1.289, loans 90+ days past due or not accruing interest at 26.7% added +0.836, and the total risk-based capital ratio of 1.7% added +0.573.

Five features pulled the score down slightly. Losses on bonds available for sale at -40.1% of equity contributed -0.267, and interest expense at 1.5% of assets contributed -0.170. Construction loans at 9.8% of loans contributed -0.117, total assets of $151.8 million contributed -0.089, and brokered deposits at 4.2% of deposits contributed -0.085.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2018-06-30 | 6 | 5,610 | ▲ watchlist |
| 2018-09-30 | 6 | 5,544 | ▲ watchlist |
| 2018-12-31 | 1 | 5,473 | ▲ watchlist |
| 2019-03-31 | 1 | 5,428 | ▲ watchlist |
| 2019-06-30 | 2 | 5,369 | ▲ watchlist (first flag) |
| 2019-09-30 | 4 | 5,325 | ▲ watchlist |
| 2019-12-31 | 1 | 5,244 | ▲ watchlist |
| 2020-03-31 | 1 | 5,182 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own history over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 30 ratios compared, 21 sat outside their own prior range as of 2020-03-31. The bank ranked 1 that quarter and was in the 100.0th percentile a year earlier as well, so the model rated it about the same as a year earlier.

Return on equity was -406.7%, below its prior range of -69.4% to -21.7%, and it pushed the score up by +1.374 model log-odds units. Return on assets was -4.1%, below its prior range of -2.5% to -1.3%, and it pushed the score up by +0.205 model log-odds units. The Texas ratio was 1704.3%, above its prior range of 243.1% to 1120.2%, and it pushed the score up by +1.289 model log-odds units. Net interest margin was 2.3%, below its prior range of 3.6% to 3.9%, and it pushed the score up by +0.081 model log-odds units.

The efficiency ratio (costs as a share of revenue) was 249.2%, well above its prior range of 122.3% to 150.0%, yet it had little effect on the score, at -0.007 model log-odds units. Losses on bonds available for sale were -40.1% of equity, below their prior range of -5.6% to 11.9%, yet this pushed the score down by -0.267 model log-odds units.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -406.7% | -69.4% to -21.7% | same quarter, prior 3 years | n/a | -337.3 pp | +1.374 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 249.2% | 122.3% to 150.0% | same quarter, prior 3 years | n/a | +110.1 pp | -0.007 | little effect on the score |
| losses on bonds available for sale, as a share of equity | -40.1% | -5.6% to 11.9% | prior 12 quarters | -34.5 pp | -44.7 pp | -0.267 | pushed the score down |
| return on assets (profit as a share of assets) | -4.1% | -2.5% to -1.3% | same quarter, prior 3 years | n/a | -2.2 pp | +0.205 | pushed the score up |
| net interest margin (the spread earned on lending and investing) | 2.3% | 3.6% to 3.9% | same quarter, prior 3 years | n/a | -1.4 pp | +0.081 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 1704.3% | 243.1% to 1120.2% | prior 12 quarters | +584.1 pp | +1017.9 pp | +1.289 | pushed the score up |

21 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Canary first flagged the bank in the quarter ending 2019-06-30, and the bank failed on 2020-04-03. That gave a lead time of 4 quarters before the failure.

At that first flag, the main drivers were already capital and credit: a Tier 1 risk-based capital ratio of 3.3% added +1.924 and return on equity of -87.3% added +1.438. The Texas ratio of 704.2% added +1.210, and loans 90+ days past due or not accruing interest at 19.1% added +0.793.

## What happened next

In hindsight, the bank's last reported quarter was 2020-03-31, the same quarter as this memo. The bank failed on 2020-04-03, so no later ranks exist after that quarter.

## Sources

- F3 · As-of quarter · 2020-03-31 · 2020-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WV · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2020-03-31 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2020-03-31 · 5,182 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2020-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2020-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2020-03-31 · 104 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2020-03-31 · 0.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2020-03-31 · 11.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2020-03-31 · 0.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2020-03-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2020-03-31 · 0.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2020-03-31 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2020-03-31 · 1.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2020-03-31 · 15.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2020-03-31 · 26.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2020-03-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2020-03-31 · 26.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2020-03-31 · 0.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2020-03-31 · 1704.3% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2020-03-31 · 3.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2020-03-31 · -4.1% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2020-03-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2020-03-31 · 3.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2020-03-31 · 19.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2020-03-31 · 4.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2020-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2020-03-31 · 15.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2020-03-31 · 7.8% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2020-03-31 · -40.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2020-03-31 · -0.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 0.4%; contribution to the score · 2020-03-31 · +2.093 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -406.7%; contribution to the score · 2020-03-31 · +1.374 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 1704.3%; contribution to the score · 2020-03-31 · +1.289 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 26.7%; contribution to the score · 2020-03-31 · +0.836 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 1.7%; contribution to the score · 2020-03-31 · +0.573 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: losses on bonds available for sale, as a share of equity, value -40.1%; contribution to the score · 2020-03-31 · -0.267 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 1.5%; contribution to the score · 2020-03-31 · -0.170 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: construction loans as a share of loans, value 9.8%; contribution to the score · 2020-03-31 · -0.117 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: total assets, value $151.8 million; contribution to the score · 2020-03-31 · -0.089 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: brokered deposits as a share of deposits, value 4.2%; contribution to the score · 2020-03-31 · -0.085 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F85 · Failure date · 2020-04-03 · 2020-04-03 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2019-06-30 · 2019-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2019-06-30: the Tier 1 risk-based capital ratio, value 3.3%; contribution to the score · 2019-06-30 · +1.924 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2019-06-30: return on equity (profit as a share of equity), value -87.3%; contribution to the score · 2019-06-30 · +1.438 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2019-06-30: the Texas ratio (troubled assets against capital plus reserves), value 704.2%; contribution to the score · 2019-06-30 · +1.210 · data/analyst/scores.parquet: feature texas_ratio contribution
- F91 · Driver up #4 at 2019-06-30: loans 90+ days past due or not accruing interest, as a share of loans, value 19.1%; contribution to the score · 2019-06-30 · +0.793 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F98 · Last quarter the bank reported · 2020-03-31 · 2020-03-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2020-03-31 · -406.7% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -69.4% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -21.7% · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2020-03-31 · +1.374 · data/analyst/scores.parquet: feature return_on_equity contribution
- F104 · Trend: return on equity (profit as a share of equity), what the model did with it · 2020-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2020-03-31 · 249.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 122.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 150.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F109 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2020-03-31 · -0.007 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2020-03-31 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F111 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2020-03-31 · -40.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F112 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · -5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F113 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 11.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F116 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2020-03-31 · -0.267 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F117 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2020-03-31 · pushed the score down · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F118 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2020-03-31 · -4.1% · data/features/fct_bank_features.parquet: return_on_assets
- F119 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -2.5% · data/features/fct_bank_features.parquet: return_on_assets
- F120 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F122 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2020-03-31 · +0.205 · data/analyst/scores.parquet: feature return_on_assets contribution
- F123 · Trend: return on assets (profit as a share of assets), what the model did with it · 2020-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F124 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2020-03-31 · 2.3% · data/features/fct_bank_features.parquet: net_interest_margin
- F125 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F126 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F128 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2020-03-31 · +0.081 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F129 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2020-03-31 · pushed the score up · data/analyst/scores.parquet: feature net_interest_margin contribution
- F130 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2020-03-31 · 1704.3% · data/features/fct_bank_features.parquet: texas_ratio
- F131 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 243.1% · data/features/fct_bank_features.parquet: texas_ratio
- F132 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 1120.2% · data/features/fct_bank_features.parquet: texas_ratio
- F135 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2020-03-31 · +1.289 · data/analyst/scores.parquet: feature texas_ratio contribution
- F136 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2020-03-31 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F137 · Trend: ratios outside their own prior range · 2020-03-31 · 21 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios compared with their own prior range · 2020-03-31 · 30 · data/features/fct_bank_features.parquet
- F140 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F142 · Percentile a year earlier (100 = highest risk) · 2019-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F143 · Trend: how the model's rating compares with a year earlier · 2020-03-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
