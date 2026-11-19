---
cert: 35495
name: "Proficio Bank"
as_of: 2016-12-31
rank: 6
n_banks: 5983
percentile: 99.91642988467324
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-03-03
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:51:56"
writer_model: "claude-opus-5-5"
checked: true
---

# Proficio Bank (cert 35495)

*Hindsight: failed 2017-03-03. Canary flagged it 4 quarters ahead.*

## Summary

As of 2016-12-31, Proficio Bank, a Utah bank, ranked number 6 out of 5,983 FDIC-insured banks on Canary's risk score, which places it in the 99.9th percentile. That put it on Canary's watchlist, the top 2% of banks by score. Its capital cushion was thin, with equity (the owners' own money) at 3.4% of assets against a national median of 10.7%. It was also losing money, with a return on assets of -4.5% versus a national median of 0.9%.

## Warning signs in the data

Capital, the buffer that absorbs losses, was far below typical levels: the leverage ratio (core capital as a share of average assets) was 3.1% against a national median of 10.4%. The Tier 1 risk-based capital ratio, which weighs capital against the riskiness of assets, was 3.6% versus a median of 15.0%, and the total risk-based capital ratio was 4.7% versus 16.2%. Earnings were deeply negative, with return on equity at -133.2% against a median of 8.0%, and the efficiency ratio (operating costs as a share of revenue) at 179.2% versus 69.7%.

Credit quality was weak: loans 90 or more days past due or not accruing interest were 2.2% of loans, well above the median of 0.6%. Nonaccrual assets and foreclosed property made up 5.0% of assets against a median of 0.5%, and the Texas ratio (troubled assets against capital plus reserves) stood at 114.1% versus a median of 4.9%. Lending leaned heavily on property, with commercial real estate loans at 60.6% of loans versus a median of 22.5%, and construction loans at 13.5% versus 4.2%.

The bank was shrinking quickly: assets changed by -37.7% over the past four quarters and deposits by -32.8%, while the national medians grew by 3.5% and 3.6%. Volatile funding (money that can leave quickly) was 15.4% of assets versus a median of 5.2%, and interest expense was 1.3% of assets versus 0.4%. Some funding figures were steadier: uninsured deposits were only 0.8% of deposits against a median of 17.3%, and cash was 11.1% of assets versus 6.6%. On bonds, the measure of losses on bonds available for sale was -4.9% of equity, below the median of 0.7%, and losses on bonds held to maturity were 0.0%, matching the median.

## Understanding the score

As of 2016-12-31, Proficio Bank ranked number 6 out of 5,983 banks, placing it in the 99.9th percentile on a scale where higher means riskier. It was flagged on Canary's watchlist, which covers the top 2% of banks by score, or 120 banks that quarter.

Five features pushed the score up the most. The largest was the Tier 1 risk-based capital ratio at 3.6%, adding +2.373, followed by return on equity at -133.2%, adding +1.406. Next came the Texas ratio at 114.1%, adding +0.569, the total risk-based capital ratio at 4.7%, adding +0.495, and asset growth over the past four quarters at -37.7%, adding +0.370.

Five features pulled the score down the most. These were loans 90 or more days past due or not accruing at 2.2% of loans, contributing -0.414, and interest expense at 1.3% of assets, contributing -0.333. They also included losses on bonds available for sale at -4.9% of equity, contributing -0.327, early-stage past-due loans at 0.4% of assets, contributing -0.293, and commercial real estate loans at 60.6% of loans, contributing -0.275.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 9 | 6,193 | ▲ watchlist (first flag) |
| 2016-06-30 | 7 | 6,129 | ▲ watchlist |
| 2016-09-30 | 14 | 6,051 | ▲ watchlist |
| 2016-12-31 | 6 | 5,983 | ▲ watchlist |

## How its ratios moved

Canary compares each ratio with the bank's own history, usually the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios. Of 30 ratios compared, 11 sat outside their own prior range, and the table shows the 6 furthest outside. At this point the bank ranked number 6 out of 5,983 banks.

Return on equity changed by -37.7 pp over four quarters. Return on equity was -133.2%, below its prior range of -95.5% to 3.4%, and it contributed +1.406 model log-odds units and pushed the score up. The efficiency ratio changed by +28.2 pp over four quarters. The efficiency ratio was 179.2%, above its prior range of 98.9% to 150.9%, yet it contributed only +0.021 and had little effect on the score.

Interest expense was 1.3% of assets, above its prior range of 0.6% to 0.9%, yet it contributed -0.333 and pushed the score down. Deposit growth was -32.8%, below its prior range of -28.6% to 1.8% after a one-quarter change of -8.0 pp, yet it contributed -0.110 and pushed the score down. Commercial real estate loans were 60.6% of loans, above their prior range of 9.4% to 55.5% after a change of +12.6 pp over four quarters, yet they contributed -0.275 and pushed the score down. The provision for loan losses (money set aside for expected bad loans) was 0.0% of assets, above its prior range of -0.5% to -0.1%, yet it contributed -0.057 and pushed the score down.

There is no score from a year earlier to compare with (scores start 2016-03-31, or the bank did not report then).

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 179.2% | 98.9% to 150.9% | same quarter, prior 3 years | n/a | +28.2 pp | +0.021 | little effect on the score |
| return on equity (profit as a share of equity) | -133.2% | -95.5% to 3.4% | same quarter, prior 3 years | n/a | -37.7 pp | +1.406 | pushed the score up |
| annualized interest expense as a share of assets | 1.3% | 0.6% to 0.9% | same quarter, prior 3 years | n/a | +0.4 pp | -0.333 | pushed the score down |
| deposit growth over the past four quarters | -32.8% | -28.6% to 1.8% | prior 12 quarters | -8.0 pp | -4.2 pp | -0.110 | pushed the score down |
| commercial real estate loans as a share of loans | 60.6% | 9.4% to 55.5% | prior 12 quarters | +5.3 pp | +12.6 pp | -0.275 | pushed the score down |
| annualized provision for loan losses as a share of assets | 0.0% | -0.5% to -0.1% | same quarter, prior 3 years | n/a | +0.6 pp | -0.057 | pushed the score down |

11 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Canary first flagged Proficio Bank in the quarter ending 2016-03-31, and the bank failed on 2017-03-03. That gave a lead time of 4 quarters before the failure.

At that first flag, the main drivers were already capital and earnings: the Tier 1 risk-based capital ratio was 4.2%, adding +2.485, and return on equity was -197.5%, adding +1.496. The Texas ratio was 175.8%, adding +1.038, the total risk-based capital ratio was 5.0%, adding +0.427, and the leverage ratio was 2.4%, adding +0.316.

## What happened next

In hindsight, the quarter ending 2016-12-31 was the last one Proficio Bank reported, so Canary has no later ranks or flags for it. The bank failed on 2017-03-03. Our data alone shows only that reporting stopped, which can mean either a merger or a closure.

## Sources

- F1 · Bank name · n/a · Proficio Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · UT · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-12-31 · 6 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-12-31 · 5,983 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-12-31 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-12-31 · 120 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-12-31 · 3.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-12-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · 3.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-12-31 · 3.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-12-31 · 15.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-12-31 · 4.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-12-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 2.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 5.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F33 · Bank: construction loans as a share of loans · 2016-12-31 · 13.5% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F34 · National median: construction loans as a share of loans · 2016-12-31 · 4.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2016-12-31 · 60.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2016-12-31 · 22.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2016-12-31 · 114.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2016-12-31 · 4.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-12-31 · -4.5% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-12-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2016-12-31 · -133.2% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2016-12-31 · 8.0% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2016-12-31 · 179.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2016-12-31 · 69.7% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2016-12-31 · 1.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2016-12-31 · 0.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2016-12-31 · 0.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2016-12-31 · 17.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2016-12-31 · 15.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2016-12-31 · 5.2% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2016-12-31 · 11.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2016-12-31 · 6.6% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2016-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2016-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2016-12-31 · -4.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2016-12-31 · 0.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2016-12-31 · -37.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2016-12-31 · 3.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2016-12-31 · -32.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2016-12-31 · 3.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 3.6%; contribution to the score · 2016-12-31 · +2.373 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -133.2%; contribution to the score · 2016-12-31 · +1.406 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 114.1%; contribution to the score · 2016-12-31 · +0.569 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 4.7%; contribution to the score · 2016-12-31 · +0.495 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: asset growth over the past four quarters, value -37.7%; contribution to the score · 2016-12-31 · +0.370 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F80 · Driver down #1: loans 90+ days past due or not accruing interest, as a share of loans, value 2.2%; contribution to the score · 2016-12-31 · -0.414 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 1.3%; contribution to the score · 2016-12-31 · -0.333 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: losses on bonds available for sale, as a share of equity, value -4.9%; contribution to the score · 2016-12-31 · -0.327 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F83 · Driver down #4: loans 30-89 days past due, as a share of assets, value 0.4%; contribution to the score · 2016-12-31 · -0.293 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F84 · Driver down #5: commercial real estate loans as a share of loans, value 60.6%; contribution to the score · 2016-12-31 · -0.275 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F85 · Failure date · 2017-03-03 · 2017-03-03 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-03-31: the Tier 1 risk-based capital ratio, value 4.2%; contribution to the score · 2016-03-31 · +2.485 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2016-03-31: return on equity (profit as a share of equity), value -197.5%; contribution to the score · 2016-03-31 · +1.496 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2016-03-31: the Texas ratio (troubled assets against capital plus reserves), value 175.8%; contribution to the score · 2016-03-31 · +1.038 · data/analyst/scores.parquet: feature texas_ratio contribution
- F91 · Driver up #4 at 2016-03-31: the total risk-based capital ratio, value 5.0%; contribution to the score · 2016-03-31 · +0.427 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F92 · Driver up #5 at 2016-03-31: the leverage ratio (core capital as a share of average assets), value 2.4%; contribution to the score · 2016-03-31 · +0.316 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F98 · Last quarter the bank reported · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2016-12-31 · 179.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F100 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 98.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 150.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F102 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2016-12-31 · +28.2 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F103 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2016-12-31 · +0.021 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F104 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2016-12-31 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F105 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2016-12-31 · -133.2% · data/features/fct_bank_features.parquet: return_on_equity
- F106 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -95.5% · data/features/fct_bank_features.parquet: return_on_equity
- F107 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 3.4% · data/features/fct_bank_features.parquet: return_on_equity
- F108 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2016-12-31 · -37.7 pp · data/features/fct_bank_features.parquet: return_on_equity
- F109 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2016-12-31 · +1.406 · data/analyst/scores.parquet: feature return_on_equity contribution
- F110 · Trend: return on equity (profit as a share of equity), what the model did with it · 2016-12-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F111 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2016-12-31 · 1.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F112 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F113 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F115 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2016-12-31 · -0.333 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F116 · Trend: annualized interest expense as a share of assets, what the model did with it · 2016-12-31 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F117 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2016-12-31 · -32.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F118 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · -28.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F119 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 1.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F120 · Trend: deposit growth over the past four quarters, change over one quarter, in percentage points · 2016-12-31 · -8.0 pp · data/features/fct_bank_features.parquet: deposit_growth_4q
- F122 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2016-12-31 · -0.110 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F123 · Trend: deposit growth over the past four quarters, what the model did with it · 2016-12-31 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F124 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2016-12-31 · 60.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F125 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 9.4% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F126 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 55.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F128 · Trend: commercial real estate loans as a share of loans, change over four quarters, in percentage points · 2016-12-31 · +12.6 pp · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F129 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2016-12-31 · -0.275 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F130 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2016-12-31 · pushed the score down · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F131 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2016-12-31 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F132 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · -0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F133 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · -0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F135 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2016-12-31 · -0.057 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F136 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2016-12-31 · pushed the score down · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F137 · Trend: ratios outside their own prior range · 2016-12-31 · 11 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios shown in the table (the furthest outside their prior range) · 2016-12-31 · 6 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios compared with their own prior range · 2016-12-31 · 30 · data/features/fct_bank_features.parquet
- F140 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
