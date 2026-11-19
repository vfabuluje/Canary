---
cert: 17719
name: "The Farmers And Merchants State Bank Of Argonia"
as_of: 2017-09-30
rank: 1
n_banks: 5806
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-10-13
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T20:06:14"
writer_model: "claude-opus-5-5"
checked: true
---

# The Farmers And Merchants State Bank Of Argonia (cert 17719)

*Hindsight: failed 2017-10-13. Canary flagged it 4 quarters ahead.*

## Summary

As of 2017-09-30, The Farmers And Merchants State Bank Of Argonia, a Kansas bank, ranked 1 out of 5,806 banks nationally on Canary's risk score, placing it in the 100.0th percentile, where higher means riskier. That put it on Canary's watchlist, which covers the riskiest 2% of banks, or 117 banks that quarter. Its capital, the owners' cushion that absorbs losses, had fallen below zero, with equity at -1.1% of assets against a national median of 11.0%. Its loan problems were also severe, with 11.5% of loans 90 or more days late or no longer paying interest, compared with a national median of 0.6%.

## Warning signs in the data

Capital was the most striking weakness: equity was -1.1% of assets, against a national median of 11.0% for the same quarter. The leverage ratio, which measures core capital against average assets, was -1.3%, compared with a median of 10.6%. The Tier 1 risk-based capital ratio, which weighs capital against how risky the assets are, was -2.3% versus a median of 15.1%, and the total risk-based capital ratio was -1.0% versus 16.3%.

Credit quality was far worse than at a typical bank: 11.5% of loans were 90 or more days past due or not accruing interest, against a median of 0.6%. The Texas ratio, which compares troubled assets with the capital and reserves available to cover them, stood at 292.3%, against a median of 4.5%. Net loan write-offs, loans recorded as lost, ran at an annualized 10.5% of loans versus a median of 0.0%, and the bank lost money, with return on assets at -10.5% against a median of 0.9%.

On funding, brokered deposits, money placed through intermediaries, made up 10.3% of deposits against a median of 0.0%, and Federal Home Loan Bank borrowings were 13.8% of assets versus a median of 0.9%. Deposits shrank by -9.9% over the past four quarters, while the median bank grew deposits by 3.8%, though cash was high at 20.8% of assets against a median of 6.1%. Losses on bonds available for sale were -5.0% of equity versus a median of 0.0%, a figure that is hard to read when equity itself is below zero.

## Understanding the score

On 2017-09-30 the bank ranked 1 of 5,806 banks, the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks by score, 117 banks that quarter.

Five features pushed the score up most. They were the Tier 1 risk-based capital ratio at -2.3%, return on equity (profit as a share of the owners' stake) at -282.8%, and the Texas ratio at 292.3%. The other two were the leverage ratio at -1.3% and the total risk-based capital ratio at -1.0%.

Five features pulled the score down slightly. They were interest expense at 0.9% of assets, losses on bonds available for sale at -5.0% of equity, and construction loans at 0.5% of loans. The last two were deposit growth of -9.9% over four quarters and a net interest margin, the spread earned on lending and investing, of 4.2%.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 375 | 6,193 |  |
| 2016-06-30 | 426 | 6,129 |  |
| 2016-09-30 | 108 | 6,051 | ▲ watchlist |
| 2016-12-31 | 22 | 5,983 | ▲ watchlist (first flag) |
| 2017-03-31 | 12 | 5,925 | ▲ watchlist |
| 2017-06-30 | 3 | 5,856 | ▲ watchlist |
| 2017-09-30 | 1 | 5,806 | ▲ watchlist |

## How its ratios moved

Most ratios are compared with the bank's own prior 12 quarters, and year-to-date ratios with the same quarter in the prior 3 years. Of 30 ratios compared this way, 20 were outside their own prior range, and the 6 furthest outside are discussed here.

Return on equity was -282.8%, far below its prior range of 6.4% to 8.2%, a change of -291.0 pp over four quarters, and its contribution of +1.348 model log-odds units pushed the score up. Return on assets was -10.5%, below its prior range of 0.5% to 0.6%, and its contribution of +0.141 pushed the score up. The annualized provision for loan losses, money set aside for expected loan losses, was 8.1% of assets against a prior range of 0.0% to 0.1%, and its contribution of +0.143 pushed the score up.

Net loan write-offs were 10.5% of loans, well above their prior range of 0.0% to 0.3%, yet their contribution of -0.011 had little effect on the score. The efficiency ratio was 139.0%, above its prior range of 82.9% to 87.9%, yet its contribution of -0.027 had little effect on the score. Cash was 20.8% of assets, above its prior range of 2.2% to 6.1% after a +17.6 pp jump in one quarter, yet its contribution of -0.016 had little effect on the score. The bank sat in the 98.2th percentile on 2016-09-30 and ranked 1 at 2017-09-30, and the model rated it riskier than a year earlier.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -282.8% | 6.4% to 8.2% | same quarter, prior 3 years | n/a | -291.0 pp | +1.348 | pushed the score up |
| return on assets (profit as a share of assets) | -10.5% | 0.5% to 0.6% | same quarter, prior 3 years | n/a | -11.1 pp | +0.141 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 10.5% | 0.0% to 0.3% | same quarter, prior 3 years | n/a | +10.2 pp | -0.011 | little effect on the score |
| the efficiency ratio (operating costs as a share of revenue) | 139.0% | 82.9% to 87.9% | same quarter, prior 3 years | n/a | +52.5 pp | -0.027 | little effect on the score |
| annualized provision for loan losses as a share of assets | 8.1% | 0.0% to 0.1% | same quarter, prior 3 years | n/a | +8.0 pp | +0.143 | pushed the score up |
| cash as a share of assets | 20.8% | 2.2% to 6.1% | prior 12 quarters | +17.6 pp | +18.4 pp | -0.016 | little effect on the score |

20 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, the bank failed on 2017-10-13. Canary first flagged it in the quarter ending 2016-12-31, a lead time of 4 quarters before the failure.

At that first flag, the main drivers were loan troubles rather than capital: loans 90 or more days late or not accruing interest were 12.1% of loans, and the Texas ratio was 115.6%. Loans in the early stages of being past due were 4.0% of assets, while the Tier 1 risk-based capital ratio, still positive at 9.1%, pulled the score down at the time.

## What happened next

In hindsight, the last quarter the bank reported was 2017-09-30, the same quarter as this memo. The bank failed on 2017-10-13, so no later ranks exist for it.

## Sources

- F3 · As-of quarter · 2017-09-30 · 2017-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KS · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2017-09-30 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2017-09-30 · 5,806 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2017-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2017-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2017-09-30 · 117 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2017-09-30 · -1.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2017-09-30 · 11.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2017-09-30 · -1.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2017-09-30 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2017-09-30 · -2.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2017-09-30 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2017-09-30 · -1.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2017-09-30 · 16.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2017-09-30 · 11.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2017-09-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2017-09-30 · 10.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2017-09-30 · 292.3% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2017-09-30 · 4.5% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2017-09-30 · -10.5% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2017-09-30 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2017-09-30 · 10.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2017-09-30 · 13.8% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2017-09-30 · 0.9% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2017-09-30 · 20.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2017-09-30 · 6.1% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2017-09-30 · -5.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2017-09-30 · -9.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2017-09-30 · 3.8% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value -2.3%; contribution to the score · 2017-09-30 · +2.007 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -282.8%; contribution to the score · 2017-09-30 · +1.348 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 292.3%; contribution to the score · 2017-09-30 · +1.262 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value -1.3%; contribution to the score · 2017-09-30 · +0.692 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: the total risk-based capital ratio, value -1.0%; contribution to the score · 2017-09-30 · +0.562 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.9%; contribution to the score · 2017-09-30 · -0.635 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: losses on bonds available for sale, as a share of equity, value -5.0%; contribution to the score · 2017-09-30 · -0.248 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F82 · Driver down #3: construction loans as a share of loans, value 0.5%; contribution to the score · 2017-09-30 · -0.168 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: deposit growth over the past four quarters, value -9.9%; contribution to the score · 2017-09-30 · -0.125 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F84 · Driver down #5: net interest margin (the spread earned on lending and investing), value 4.2%; contribution to the score · 2017-09-30 · -0.122 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F85 · Failure date · 2017-10-13 · 2017-10-13 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-12-31 · 2016-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 12.1%; contribution to the score · 2016-12-31 · +0.956 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F89 · Driver up #2 at 2016-12-31: the Texas ratio (troubled assets against capital plus reserves), value 115.6%; contribution to the score · 2016-12-31 · +0.747 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2016-12-31: loans 30-89 days past due, as a share of assets, value 4.0%; contribution to the score · 2016-12-31 · +0.575 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F95 · Driver down #3 at 2016-12-31: the Tier 1 risk-based capital ratio, value 9.1%; contribution to the score · 2016-12-31 · -0.226 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2017-09-30 · 2017-09-30 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2017-09-30 · -282.8% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 6.4% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 8.2% · data/features/fct_bank_features.parquet: return_on_equity
- F102 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2017-09-30 · -291.0 pp · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2017-09-30 · +1.348 · data/analyst/scores.parquet: feature return_on_equity contribution
- F104 · Trend: return on equity (profit as a share of equity), what the model did with it · 2017-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F105 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2017-09-30 · -10.5% · data/features/fct_bank_features.parquet: return_on_assets
- F106 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: return_on_assets
- F107 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2017-09-30 · +0.141 · data/analyst/scores.parquet: feature return_on_assets contribution
- F110 · Trend: return on assets (profit as a share of assets), what the model did with it · 2017-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F111 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2017-09-30 · 10.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F112 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F113 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F115 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2017-09-30 · -0.011 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F116 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2017-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F117 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2017-09-30 · 139.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F118 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 82.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F119 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 87.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F121 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2017-09-30 · -0.027 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F122 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2017-09-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F123 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2017-09-30 · 8.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F124 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F125 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F127 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2017-09-30 · +0.143 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F128 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2017-09-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F129 · Trend: cash as a share of assets, value at the as-of quarter · 2017-09-30 · 20.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F130 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F131 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 6.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F132 · Trend: cash as a share of assets, change over one quarter, in percentage points · 2017-09-30 · +17.6 pp · data/features/fct_bank_features.parquet: cash_to_assets
- F134 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2017-09-30 · -0.016 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F135 · Trend: cash as a share of assets, what the model did with it · 2017-09-30 · little effect on the score · data/analyst/scores.parquet: feature cash_to_assets contribution
- F136 · Trend: ratios outside their own prior range · 2017-09-30 · 20 · data/features/fct_bank_features.parquet
- F137 · Trend: ratios shown in the table (the furthest outside their prior range) · 2017-09-30 · 6 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios compared with their own prior range · 2017-09-30 · 30 · data/features/fct_bank_features.parquet
- F139 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F140 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F141 · Percentile a year earlier (100 = highest risk) · 2016-09-30 · 98.2% · data/analyst/scores.parquet: percentile
- F142 · Trend: how the model's rating compares with a year earlier · 2017-09-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
