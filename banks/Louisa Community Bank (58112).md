---
cert: 58112
name: "Louisa Community Bank"
as_of: 2019-09-30
rank: 1
n_banks: 5325
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2019-10-25
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:52:23"
writer_model: "claude-opus-5-5"
checked: true
---

# Louisa Community Bank (cert 58112)

*Hindsight: failed 2019-10-25. Canary flagged it 4 quarters ahead.*

## Summary

As of 2019-09-30, Louisa Community Bank (certificate 58112, in KY) ranked 1 out of 5,325 banks nationally on Canary's risk score, which places it in the 100.0th percentile. That put it on Canary's watchlist, which covers the top 2% of banks. Its leverage ratio (core capital, the owners' cushion against losses, as a share of average assets) was 1.2% against a national median of 11.0%, while 11.9% of its loans were 90+ days past due or not accruing interest, against a median of 0.6%. The bank was also losing money, with a return on assets (profit as a share of assets) of -6.4% compared with a national median of 1.1%.

## Warning signs in the data

Capital, the owners' money that absorbs losses before depositors are hurt, was very thin. Equity was 3.9% of assets against a national median of 11.6%, and the leverage ratio was 1.2% against a median of 11.0%. Measured against riskier assets, the Tier 1 risk-based capital ratio was 1.5% (median 15.6%) and the total risk-based capital ratio was 2.8% (median 16.7%).

Loan quality was far worse than at a typical bank: 11.9% of loans were 90+ days past due or not accruing interest (median 0.6%), and nonaccrual assets plus foreclosed property were 11.2% of assets (median 0.4%). Loans 30-89 days past due, an early stage of trouble, were 4.8% of assets against a median of 0.3%. The Texas ratio, which weighs troubled assets against capital plus reserves, stood at 173.6% versus a median of 3.7%. Annualized net loan write-offs were 1.7% of loans (median 0.0%), and the annualized provision for loan losses was 2.7% of assets (median 0.1%). Earnings were deeply negative, with return on equity at -107.3% (median 9.6%) and an efficiency ratio, operating costs as a share of revenue, of 226.9% (median 66.8%).

On funding, the bank leaned more than most on less stable money: brokered deposits, gathered through middlemen, were 10.2% of deposits (median 0.0%), Federal Home Loan Bank borrowings were 6.2% of assets (median 0.4%), and volatile funding was 24.7% of assets (median 6.1%). Core deposits, the steadier everyday accounts, were 68.6% of assets against a median of 77.3%, while uninsured deposits were lower than typical at 11.6% versus 19.0%. The bank was shrinking, with asset growth of -15.9% over the past four quarters against a median of 4.7%, while bond losses were small: 0.0% of equity on held-to-maturity bonds (median 0.0%) and 0.5% on available-for-sale bonds (median -0.8%).

## Understanding the score

As of 2019-09-30, Louisa Community Bank ranked 1 of 5,325 banks, the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, one of 107 banks that quarter, a list that covers the top 2% of banks.

Five features pushed the score up most. The largest was the Tier 1 risk-based capital ratio at 1.5%, contributing +1.956, followed by return on equity at -107.3%, contributing +1.263. Next came the Texas ratio at 173.6% (+0.995), loans 90+ days past due or not accruing interest at 11.9% of loans (+0.810), and the total risk-based capital ratio at 2.8% (+0.557).

Five features pulled the score down, each only slightly by comparison. These were interest expense at 1.4% of assets (-0.281), construction loans at 4.6% of loans (-0.210), and deposit growth of -11.3% over the past four quarters (-0.099). The last two were total assets of $28.2 million (-0.065) and uninsured deposits at 11.6% of deposits (-0.054).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2017-12-31 | 29 | 5,738 | ▲ watchlist |
| 2018-03-31 | 22 | 5,674 | ▲ watchlist |
| 2018-06-30 | 15 | 5,610 | ▲ watchlist |
| 2018-09-30 | 11 | 5,544 | ▲ watchlist |
| 2018-12-31 | 7 | 5,473 | ▲ watchlist (first flag) |
| 2019-03-31 | 4 | 5,428 | ▲ watchlist |
| 2019-06-30 | 1 | 5,369 | ▲ watchlist |
| 2019-09-30 | 1 | 5,325 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own history: most against the prior 12 quarters, and year-to-date ratios against the same quarter in the prior 3 years. At 2019-09-30, 16 of the 30 ratios checked sat outside their own prior range. The bank ranked 1 of 5,325, in the 100.0th percentile, compared with the 99.8th percentile a year earlier, so the model's rating was about the same as a year earlier.

Return on equity was -107.3%, far below its prior range of -26.0% to -4.7% after a change of -81.3 pp over four quarters, and its contribution of +1.263 log-odds units pushed the score up. Return on assets was -6.4%, below its prior range of -2.6% to -0.7% after a change of -3.8 pp, and its contribution of +0.132 pushed the score up. The provision for loan losses, money set aside for expected bad loans, was 2.7% of assets, above its prior range of 0.4% to 1.1% after a change of +2.1 pp, and its contribution of +0.142 pushed the score up.

Three other ratios moved well outside their ranges yet had little effect on the score. The efficiency ratio reached 226.9%, above its prior range of 107.3% to 155.4%, but its contribution of -0.046 had little effect on the score. Net interest margin fell to 2.9%, below its prior range of 3.9% to 4.3%, but its contribution of +0.022 had little effect on the score. Net loan write-offs rose to 1.7% of loans, above their prior range of 0.3% to 0.9%, but their contribution of -0.012 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -107.3% | -26.0% to -4.7% | same quarter, prior 3 years | n/a | -81.3 pp | +1.263 | pushed the score up |
| return on assets (profit as a share of assets) | -6.4% | -2.6% to -0.7% | same quarter, prior 3 years | n/a | -3.8 pp | +0.132 | pushed the score up |
| annualized provision for loan losses as a share of assets | 2.7% | 0.4% to 1.1% | same quarter, prior 3 years | n/a | +2.1 pp | +0.142 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 226.9% | 107.3% to 155.4% | same quarter, prior 3 years | n/a | +71.5 pp | -0.046 | little effect on the score |
| net interest margin (the spread earned on lending and investing) | 2.9% | 3.9% to 4.3% | same quarter, prior 3 years | n/a | -1.0 pp | +0.022 | little effect on the score |
| annualized loan write-offs, net of recoveries, as a share of loans | 1.7% | 0.3% to 0.9% | same quarter, prior 3 years | n/a | +0.9 pp | -0.012 | little effect on the score |

16 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Louisa Community Bank failed on 2019-10-25. Canary first flagged it in the quarter ending 2018-12-31, a lead time of 4 quarters before the failure.

At that first flag, the main drivers pushing the score up were the Texas ratio at 139.0% (+0.936) and return on equity at -37.9% (+0.859). They were followed by loans 90+ days past due or not accruing interest at 14.9% of loans (+0.767), the Tier 1 risk-based capital ratio at 8.2% (+0.543), and loans 30-89 days past due at 4.1% of assets (+0.355). The largest offset then was interest expense at 1.3% of assets (-0.607).

## What happened next

In hindsight, the bank's last report was for the quarter ending 2019-09-30, so there are no later ranks or flags. It failed on 2019-10-25, shortly after that final report.

## Sources

- F1 · Bank name · n/a · Louisa Community Bank · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 58112 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KY · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2019-09-30 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2019-09-30 · 5,325 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2019-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2019-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2019-09-30 · 107 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2019-09-30 · 3.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2019-09-30 · 11.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 1.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2019-09-30 · 1.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2019-09-30 · 15.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2019-09-30 · 2.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2019-09-30 · 16.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 11.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2019-09-30 · 11.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2019-09-30 · 0.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2019-09-30 · 4.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2019-09-30 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2019-09-30 · 1.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2019-09-30 · 2.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2019-09-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 173.6% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 3.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2019-09-30 · -6.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2019-09-30 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2019-09-30 · -107.3% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2019-09-30 · 9.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 226.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 66.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2019-09-30 · 11.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2019-09-30 · 19.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2019-09-30 · 10.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2019-09-30 · 68.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2019-09-30 · 77.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2019-09-30 · 6.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2019-09-30 · 0.4% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2019-09-30 · 24.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2019-09-30 · 6.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2019-09-30 · 0.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2019-09-30 · -0.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2019-09-30 · -15.9% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2019-09-30 · 4.7% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 1.5%; contribution to the score · 2019-09-30 · +1.956 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -107.3%; contribution to the score · 2019-09-30 · +1.263 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 173.6%; contribution to the score · 2019-09-30 · +0.995 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 11.9%; contribution to the score · 2019-09-30 · +0.810 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 2.8%; contribution to the score · 2019-09-30 · +0.557 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 1.4%; contribution to the score · 2019-09-30 · -0.281 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: construction loans as a share of loans, value 4.6%; contribution to the score · 2019-09-30 · -0.210 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: deposit growth over the past four quarters, value -11.3%; contribution to the score · 2019-09-30 · -0.099 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F83 · Driver down #4: total assets, value $28.2 million; contribution to the score · 2019-09-30 · -0.065 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: uninsured deposits as a share of deposits, value 11.6%; contribution to the score · 2019-09-30 · -0.054 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F85 · Failure date · 2019-10-25 · 2019-10-25 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2018-12-31 · 2018-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2018-12-31: the Texas ratio (troubled assets against capital plus reserves), value 139.0%; contribution to the score · 2018-12-31 · +0.936 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Driver up #2 at 2018-12-31: return on equity (profit as a share of equity), value -37.9%; contribution to the score · 2018-12-31 · +0.859 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2018-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 14.9%; contribution to the score · 2018-12-31 · +0.767 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F91 · Driver up #4 at 2018-12-31: the Tier 1 risk-based capital ratio, value 8.2%; contribution to the score · 2018-12-31 · +0.543 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F92 · Driver up #5 at 2018-12-31: loans 30-89 days past due, as a share of assets, value 4.1%; contribution to the score · 2018-12-31 · +0.355 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F93 · Driver down #1 at 2018-12-31: annualized interest expense as a share of assets, value 1.3%; contribution to the score · 2018-12-31 · -0.607 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F98 · Last quarter the bank reported · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2019-09-30 · -107.3% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -26.0% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -4.7% · data/features/fct_bank_features.parquet: return_on_equity
- F102 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2019-09-30 · -81.3 pp · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2019-09-30 · +1.263 · data/analyst/scores.parquet: feature return_on_equity contribution
- F104 · Trend: return on equity (profit as a share of equity), what the model did with it · 2019-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F105 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2019-09-30 · -6.4% · data/features/fct_bank_features.parquet: return_on_assets
- F106 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -2.6% · data/features/fct_bank_features.parquet: return_on_assets
- F107 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F108 · Trend: return on assets (profit as a share of assets), change over four quarters, in percentage points · 2019-09-30 · -3.8 pp · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2019-09-30 · +0.132 · data/analyst/scores.parquet: feature return_on_assets contribution
- F110 · Trend: return on assets (profit as a share of assets), what the model did with it · 2019-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F111 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2019-09-30 · 2.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F112 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F113 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F114 · Trend: annualized provision for loan losses as a share of assets, change over four quarters, in percentage points · 2019-09-30 · +2.1 pp · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F115 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2019-09-30 · +0.142 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F116 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2019-09-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F117 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2019-09-30 · 226.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F118 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 107.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F119 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 155.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F121 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2019-09-30 · -0.046 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F122 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2019-09-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F123 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2019-09-30 · 2.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F124 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F125 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 4.3% · data/features/fct_bank_features.parquet: net_interest_margin
- F127 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2019-09-30 · +0.022 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F128 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2019-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F129 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2019-09-30 · 1.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F130 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F131 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F133 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2019-09-30 · -0.012 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F134 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2019-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F135 · Trend: ratios outside their own prior range · 2019-09-30 · 16 · data/features/fct_bank_features.parquet
- F137 · Trend: ratios compared with their own prior range · 2019-09-30 · 30 · data/features/fct_bank_features.parquet
- F138 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F139 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F140 · Percentile a year earlier (100 = highest risk) · 2018-09-30 · 99.8% · data/analyst/scores.parquet: percentile
- F141 · Trend: how the model's rating compares with a year earlier · 2019-09-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
