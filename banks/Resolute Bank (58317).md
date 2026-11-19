---
cert: 58317
name: "Resolute Bank"
as_of: 2019-09-30
rank: 3
n_banks: 5325
percentile: 99.962441314554
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2019-10-25
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:52:23"
writer_model: "claude-opus-5-5"
checked: true
---

# Resolute Bank (cert 58317)

*Hindsight: failed 2019-10-25. Canary flagged it 4 quarters ahead.*

## Summary

As of 2019-09-30, Resolute Bank, an Ohio bank, ranked 3 out of 5,325 banks nationally on Canary's risk score, placing it in the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was on Canary's watchlist, which holds the top 2% of banks by score. Its capital cushion (the owners' money that absorbs losses) was very thin, with equity at 0.7% of assets against a national median of 11.6%. It was also losing money, with a return on assets (profit as a share of assets) of -7.0% compared with a national median of 1.1%.

## Warning signs in the data

Capital was far below typical levels: equity was 0.7% of assets against a national median of 11.6%, and the leverage ratio (core capital as a share of average assets) was 0.6% against a median of 11.0%. The risk-based measures, which weigh assets by how risky they are, were just as weak, with a Tier 1 ratio of 1.3% against a median of 15.6% and a total ratio of 2.6% against a median of 16.7%.

Credit quality was poor: loans 90 or more days past due or no longer paying interest were 3.5% of loans against a national median of 0.6%, and net loan write-offs (loans given up as lost) ran at 6.2% of loans against a median of 0.0%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 115.1% against a median of 3.7%. Costs also outran revenue, with an efficiency ratio (operating costs as a share of revenue) of 145.5% against a median of 66.8%.

On funding, the bank leaned on stable sources: core deposits were 91.2% of assets against a median of 77.3%, uninsured deposits (balances above the insurance limit) were 3.0% of deposits against a median of 19.0%, and cash was 44.8% of assets against a median of 6.9%. It was shrinking, though, with deposits down -15.6% over four quarters against a median of 4.4%. Bond losses were not a factor, since securities were 0.0% of assets against a median of 15.4%.

## Understanding the score

As of 2019-09-30, Resolute Bank ranked 3 out of 5,325 banks, in the 100.0th percentile, where 100 is the riskiest end of the scale. It was one of 107 banks on the watchlist that quarter, a list covering the top 2% of banks by score.

The five factors pushing the score up most were all about thin capital and heavy losses. The Tier 1 risk-based capital ratio of 1.3% added +1.951, and return on equity (profit as a share of equity) of -274.3% added +1.347. The leverage ratio of 0.6% added +0.620, the total risk-based capital ratio of 2.6% added +0.614, and the Texas ratio of 115.1% added +0.413.

The five factors pulling the score down were smaller in size. Interest expense of 1.0% of assets took off -0.287, deposit growth of -15.6% took off -0.115, and the efficiency ratio of 145.5% took off -0.101. Construction loans at 0.6% of loans took off -0.083, and a net interest margin (the spread earned on lending and investing) of 3.7% took off -0.078.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2017-12-31 | 547 | 5,738 |  |
| 2018-03-31 | 27 | 5,674 | ▲ watchlist |
| 2018-06-30 | 18 | 5,610 | ▲ watchlist |
| 2018-09-30 | 16 | 5,544 | ▲ watchlist |
| 2018-12-31 | 10 | 5,473 | ▲ watchlist (first flag) |
| 2019-03-31 | 5 | 5,428 | ▲ watchlist |
| 2019-06-30 | 6 | 5,369 | ▲ watchlist |
| 2019-09-30 | 3 | 5,325 | ▲ watchlist |

## How its ratios moved

Canary compares each ratio with its own history over the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios. As of 2019-09-30, 12 of 30 ratios sat outside their own prior range, and the table shows the 6 furthest outside. The bank ranked 3 out of 5,325 in the 100.0th percentile, against the 99.7th percentile a year earlier, so the model rated it about the same as a year earlier.

Return on equity fell to -274.3%, below its prior range of -140.1% to 3.0% and a change of -134.2 pp over four quarters, and its contribution of +1.347 pushed the score up. The leverage ratio dropped to 0.6%, below its prior range of 2.2% to 9.3% and down -4.2 pp over four quarters, and its contribution of +0.620 pushed the score up.

Net loan write-offs rose to 6.2%, above their prior range of -0.4% to 1.4%, yet their contribution of -0.019 had little effect on the score. The efficiency ratio climbed to 145.5%, above its prior range of 99.4% to 123.2%, yet its contribution of -0.101 pushed the score down. Interest expense rose to 1.0% of assets, above its prior range of 0.5% to 0.6%, yet its contribution of -0.287 pushed the score down. Uninsured deposits fell to 3.0% of deposits, below their prior range of 6.2% to 13.3%, and their contribution of +0.049 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized loan write-offs, net of recoveries, as a share of loans | 6.2% | -0.4% to 1.4% | same quarter, prior 3 years | n/a | +6.5 pp | -0.019 | little effect on the score |
| the efficiency ratio (operating costs as a share of revenue) | 145.5% | 99.4% to 123.2% | same quarter, prior 3 years | n/a | +22.3 pp | -0.101 | pushed the score down |
| return on equity (profit as a share of equity) | -274.3% | -140.1% to 3.0% | same quarter, prior 3 years | n/a | -134.2 pp | +1.347 | pushed the score up |
| uninsured deposits as a share of deposits | 3.0% | 6.2% to 13.3% | prior 12 quarters | -10.3 pp | -8.0 pp | +0.049 | little effect on the score |
| annualized interest expense as a share of assets | 1.0% | 0.5% to 0.6% | same quarter, prior 3 years | n/a | +0.4 pp | -0.287 | pushed the score down |
| the leverage ratio (core capital as a share of average assets) | 0.6% | 2.2% to 9.3% | prior 12 quarters | -1.8 pp | -4.2 pp | +0.620 | pushed the score up |

12 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

With hindsight, Resolute Bank failed on 2019-10-25, and Canary first flagged it in the quarter ending 2018-12-31. That gave a lead time of 4 quarters before the failure.

At that first flag, the largest factors pushing the score up were return on equity of -133.7%, adding +1.036, and asset growth of -36.0%, adding +0.441. The Texas ratio of 83.4% added +0.403, loans 90 or more days past due or not accruing interest at 9.5% of loans added +0.328, and return on assets of -7.9% added +0.272. The biggest factor pulling the score down then was interest expense of 0.7% of assets, at -1.622.

## What happened next

In hindsight, the bank's last reported quarter was 2019-09-30, the same quarter this memo describes. Resolute Bank failed on October 25, 2019, less than a month after that quarter ended. Because it stopped reporting after that, there are no later ranks or flags for it in Canary's data.

## Sources

- F1 · Bank name · n/a · Resolute Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · OH · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2019-09-30 · 3 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2019-09-30 · 5,325 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2019-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2019-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2019-09-30 · 107 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2019-09-30 · 0.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2019-09-30 · 11.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 0.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2019-09-30 · 1.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2019-09-30 · 15.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2019-09-30 · 2.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2019-09-30 · 16.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 3.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2019-09-30 · 6.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 115.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 3.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2019-09-30 · -7.0% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2019-09-30 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 145.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 66.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2019-09-30 · 3.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2019-09-30 · 19.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2019-09-30 · 91.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2019-09-30 · 77.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2019-09-30 · 44.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2019-09-30 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F67 · Bank: securities as a share of assets · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2019-09-30 · 15.4% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2019-09-30 · -15.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2019-09-30 · 4.4% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 1.3%; contribution to the score · 2019-09-30 · +1.951 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -274.3%; contribution to the score · 2019-09-30 · +1.347 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the leverage ratio (core capital as a share of average assets), value 0.6%; contribution to the score · 2019-09-30 · +0.620 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 2.6%; contribution to the score · 2019-09-30 · +0.614 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: the Texas ratio (troubled assets against capital plus reserves), value 115.1%; contribution to the score · 2019-09-30 · +0.413 · data/analyst/scores.parquet: feature texas_ratio contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 1.0%; contribution to the score · 2019-09-30 · -0.287 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: deposit growth over the past four quarters, value -15.6%; contribution to the score · 2019-09-30 · -0.115 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F82 · Driver down #3: the efficiency ratio (operating costs as a share of revenue), value 145.5%; contribution to the score · 2019-09-30 · -0.101 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F83 · Driver down #4: construction loans as a share of loans, value 0.6%; contribution to the score · 2019-09-30 · -0.083 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F84 · Driver down #5: net interest margin (the spread earned on lending and investing), value 3.7%; contribution to the score · 2019-09-30 · -0.078 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F85 · Failure date · 2019-10-25 · 2019-10-25 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2018-12-31 · 2018-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2018-12-31: return on equity (profit as a share of equity), value -133.7%; contribution to the score · 2018-12-31 · +1.036 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2018-12-31: asset growth over the past four quarters, value -36.0%; contribution to the score · 2018-12-31 · +0.441 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F90 · Driver up #3 at 2018-12-31: the Texas ratio (troubled assets against capital plus reserves), value 83.4%; contribution to the score · 2018-12-31 · +0.403 · data/analyst/scores.parquet: feature texas_ratio contribution
- F91 · Driver up #4 at 2018-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 9.5%; contribution to the score · 2018-12-31 · +0.328 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2018-12-31: return on assets (profit as a share of assets), value -7.9%; contribution to the score · 2018-12-31 · +0.272 · data/analyst/scores.parquet: feature return_on_assets contribution
- F93 · Driver down #1 at 2018-12-31: annualized interest expense as a share of assets, value 0.7%; contribution to the score · 2018-12-31 · -1.622 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F98 · Last quarter the bank reported · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2019-09-30 · 6.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F100 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · -0.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F101 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F103 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2019-09-30 · -0.019 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F104 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2019-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2019-09-30 · 145.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 99.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 123.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F109 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2019-09-30 · -0.101 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2019-09-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F111 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2019-09-30 · -274.3% · data/features/fct_bank_features.parquet: return_on_equity
- F112 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -140.1% · data/features/fct_bank_features.parquet: return_on_equity
- F113 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 3.0% · data/features/fct_bank_features.parquet: return_on_equity
- F114 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2019-09-30 · -134.2 pp · data/features/fct_bank_features.parquet: return_on_equity
- F115 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2019-09-30 · +1.347 · data/analyst/scores.parquet: feature return_on_equity contribution
- F116 · Trend: return on equity (profit as a share of equity), what the model did with it · 2019-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F117 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2019-09-30 · 3.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F118 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 6.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F119 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 13.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F122 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2019-09-30 · +0.049 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F123 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2019-09-30 · little effect on the score · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F124 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2019-09-30 · 1.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F125 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F126 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 0.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F128 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2019-09-30 · -0.287 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F129 · Trend: annualized interest expense as a share of assets, what the model did with it · 2019-09-30 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F130 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2019-09-30 · 0.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F131 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F132 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 9.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F134 · Trend: the leverage ratio (core capital as a share of average assets), change over four quarters, in percentage points · 2019-09-30 · -4.2 pp · data/features/fct_bank_features.parquet: leverage_ratio
- F135 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2019-09-30 · +0.620 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F136 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2019-09-30 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F137 · Trend: ratios outside their own prior range · 2019-09-30 · 12 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios shown in the table (the furthest outside their prior range) · 2019-09-30 · 6 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios compared with their own prior range · 2019-09-30 · 30 · data/features/fct_bank_features.parquet
- F140 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F142 · Percentile a year earlier (100 = highest risk) · 2018-09-30 · 99.7% · data/analyst/scores.parquet: percentile
- F143 · Trend: how the model's rating compares with a year earlier · 2019-09-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
