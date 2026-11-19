---
cert: 21111
name: "City National Bank Of New Jersey"
as_of: 2019-09-30
rank: 21
n_banks: 5325
percentile: 99.6244131455399
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2019-11-01
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:49:53"
writer_model: "claude-opus-5-5"
checked: true
---

# City National Bank Of New Jersey (cert 21111)

*Hindsight: failed 2019-11-01. Canary flagged it 4 quarters ahead.*

## Summary

As of 2019-09-30, City National Bank Of New Jersey ranked 21 out of 5,325 banks nationally on Canary's risk score, placing it in the 99.6th percentile, where higher means riskier. That put it on Canary's watchlist, which covers the top 2% of banks by score. Its equity, the owners' cushion against losses, was 2.9% of assets against a national median of 11.6%, and it was losing money, with a return on assets of -1.4%.

## Warning signs in the data

Capital was very thin: the leverage ratio, core capital as a share of average assets, was 2.6% against a national median of 11.0%. The Tier 1 risk-based capital ratio, which measures core capital against riskier assets, was 4.9% versus a median of 15.6%, and the total risk-based capital ratio was 6.2% versus 16.7%. The bank was also unprofitable, with a return on equity of -45.9% against a median of 9.6%, and an efficiency ratio, operating costs as a share of revenue, of 148.2% versus 66.8%.

Credit quality was weaker than typical: loans 90 or more days past due or not accruing interest were 2.6% of loans against a median of 0.6%. The Texas ratio, which compares troubled assets with capital plus reserves, was 25.5%, well above the median of 3.7%. Commercial real estate loans made up 62.1% of the loan book, far above the median of 22.6%.

On funding, deposits shrank by -36.3% over the past four quarters while the median bank grew deposits by 4.4%, and uninsured deposits, balances above the government insurance limit, were 32.1% of deposits against a median of 19.0%. The bank did hold more cash than usual, at 17.3% of assets versus a median of 6.9%. Unrealized losses on bonds available for sale equaled 4.0% of equity, compared with a median of -0.8%.

## Understanding the score

City National Bank Of New Jersey ranked 21 out of 5,325 banks on 2019-09-30, the 99.6th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, one of 107 banks that quarter in the top 2% by score.

The five factors that pushed its score up most were return on equity at -45.9%, the Tier 1 risk-based capital ratio at 4.9%, asset growth over the past four quarters at -33.2%, the total risk-based capital ratio at 6.2%, and loans as a share of deposits at 54.0%. The five factors that pulled its score down most were interest expense as a share of assets at 0.3%, the Texas ratio at 25.5%, nonaccrual assets and foreclosed property at 1.5% of assets, construction loans at 4.8% of loans, and commercial real estate loans at 62.1% of loans.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2017-12-31 | 11 | 5,738 | ▲ watchlist |
| 2018-03-31 | 98 | 5,674 | ▲ watchlist |
| 2018-06-30 | 4 | 5,610 | ▲ watchlist |
| 2018-09-30 | 4 | 5,544 | ▲ watchlist |
| 2018-12-31 | 6 | 5,473 | ▲ watchlist (first flag) |
| 2019-03-31 | 17 | 5,428 | ▲ watchlist |
| 2019-06-30 | 16 | 5,369 | ▲ watchlist |
| 2019-09-30 | 21 | 5,325 | ▲ watchlist |

## How its ratios moved

The bank ranked 21 out of 5,325 banks, and a year earlier it sat in the 99.9th percentile, so the model rated it about the same as a year earlier. Of 30 ratios compared with the bank's own prior range, 12 were outside it; most ratios are compared with the prior 12 quarters and year-to-date ratios with the same quarter in the prior 3 years.

The provision for loan losses, money set aside for expected bad loans, was -2.7% of assets, below its prior range of 0.0% to 3.0%, and its contribution of +0.060 model log-odds units pushed the score up. The efficiency ratio rose to 148.2%, above its prior range of 108.8% to 139.0%, yet its contribution of -0.084 pushed the score down. Deposit growth was -36.3%, below its prior range of -29.3% to 4.2%, yet its contribution of -0.232 pushed the score down.

Securities reached 25.2% of assets, above their prior range of 15.4% to 22.6%, and their contribution of -0.086 pushed the score down. Construction loans were 4.8% of loans, above their prior range of 1.8% to 4.4%, and their contribution of -0.461 pushed the score down. Net interest margin was 4.1%, above its prior range of 2.9% to 3.7%, but its contribution of -0.019 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | -2.7% | 0.0% to 3.0% | same quarter, prior 3 years | n/a | -5.7 pp | +0.060 | pushed the score up |
| net interest margin (the spread earned on lending and investing) | 4.1% | 2.9% to 3.7% | same quarter, prior 3 years | n/a | +0.4 pp | -0.019 | little effect on the score |
| securities as a share of assets | 25.2% | 15.4% to 22.6% | prior 12 quarters | +3.2 pp | +6.6 pp | -0.086 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 148.2% | 108.8% to 139.0% | same quarter, prior 3 years | n/a | +39.4 pp | -0.084 | pushed the score down |
| deposit growth over the past four quarters | -36.3% | -29.3% to 4.2% | prior 12 quarters | -10.8 pp | -32.8 pp | -0.232 | pushed the score down |
| construction loans as a share of loans | 4.8% | 1.8% to 4.4% | prior 12 quarters | +1.5 pp | +2.3 pp | -0.461 | pushed the score down |

12 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Canary first flagged the bank in the quarter ending 2018-12-31, and the bank failed on 2019-11-01, a lead time of 4 quarters. At that first flag, the main factors pushing the score up were a Tier 1 risk-based capital ratio of 5.3%, a return on equity of -88.2%, and unrealized losses on bonds available for sale equal to 34.1% of equity. The Texas ratio of 56.8% and a total risk-based capital ratio of 6.6% also pushed the score up at that time.

## What happened next

In hindsight, the bank's last reported quarter was 2019-09-30, and it failed on 2019-11-01. After that it stopped reporting, so there are no later ranks or flags; our data does not distinguish a merger from a closure for banks that stop reporting.

## Sources

- F1 · Bank name · n/a · City National Bank Of New Jersey · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2019-09-30 · 21 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2019-09-30 · 5,325 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2019-09-30 · 99.6% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2019-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2019-09-30 · 107 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2019-09-30 · 2.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2019-09-30 · 11.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 2.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2019-09-30 · 4.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2019-09-30 · 15.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2019-09-30 · 6.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2019-09-30 · 16.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 2.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2019-09-30 · 62.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2019-09-30 · 22.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 25.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 3.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2019-09-30 · -1.4% · data/features/fct_bank_features.parquet: return_on_assets
- F41 · Bank: return on equity (profit as a share of equity) · 2019-09-30 · -45.9% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2019-09-30 · 9.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 148.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 66.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2019-09-30 · 32.1% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2019-09-30 · 19.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2019-09-30 · 17.3% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2019-09-30 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2019-09-30 · 4.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2019-09-30 · -0.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2019-09-30 · -36.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2019-09-30 · 4.4% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -45.9%; contribution to the score · 2019-09-30 · +1.116 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: the Tier 1 risk-based capital ratio, value 4.9%; contribution to the score · 2019-09-30 · +0.973 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver up #3: asset growth over the past four quarters, value -33.2%; contribution to the score · 2019-09-30 · +0.418 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 6.2%; contribution to the score · 2019-09-30 · +0.284 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: loans as a share of deposits, value 54.0%; contribution to the score · 2019-09-30 · +0.150 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.3%; contribution to the score · 2019-09-30 · -1.158 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 25.5%; contribution to the score · 2019-09-30 · -0.941 · data/analyst/scores.parquet: feature texas_ratio contribution
- F82 · Driver down #3: nonaccrual assets and foreclosed property, as a share of assets, value 1.5%; contribution to the score · 2019-09-30 · -0.699 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F83 · Driver down #4: construction loans as a share of loans, value 4.8%; contribution to the score · 2019-09-30 · -0.461 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F84 · Driver down #5: commercial real estate loans as a share of loans, value 62.1%; contribution to the score · 2019-09-30 · -0.448 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F85 · Failure date · 2019-11-01 · 2019-11-01 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2018-12-31 · 2018-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2018-12-31: the Tier 1 risk-based capital ratio, value 5.3%; contribution to the score · 2018-12-31 · +1.364 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2018-12-31: return on equity (profit as a share of equity), value -88.2%; contribution to the score · 2018-12-31 · +0.941 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2018-12-31: losses on bonds available for sale, as a share of equity, value 34.1%; contribution to the score · 2018-12-31 · +0.661 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F91 · Driver up #4 at 2018-12-31: the Texas ratio (troubled assets against capital plus reserves), value 56.8%; contribution to the score · 2018-12-31 · +0.656 · data/analyst/scores.parquet: feature texas_ratio contribution
- F92 · Driver up #5 at 2018-12-31: the total risk-based capital ratio, value 6.6%; contribution to the score · 2018-12-31 · +0.498 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
- F103 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2019-09-30 · -2.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F104 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F105 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 3.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F107 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2019-09-30 · +0.060 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F108 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2019-09-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F109 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2019-09-30 · 4.1% · data/features/fct_bank_features.parquet: net_interest_margin
- F110 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 2.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F111 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F113 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2019-09-30 · -0.019 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F114 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2019-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F115 · Trend: securities as a share of assets, value at the as-of quarter · 2019-09-30 · 25.2% · data/features/fct_bank_features.parquet: securities_to_assets
- F116 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 15.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F117 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 22.6% · data/features/fct_bank_features.parquet: securities_to_assets
- F120 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2019-09-30 · -0.086 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F121 · Trend: securities as a share of assets, what the model did with it · 2019-09-30 · pushed the score down · data/analyst/scores.parquet: feature securities_to_assets contribution
- F122 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2019-09-30 · 148.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F123 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 108.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F124 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 139.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F126 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2019-09-30 · -0.084 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F127 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2019-09-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F128 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2019-09-30 · -36.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F129 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · -29.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F130 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F133 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2019-09-30 · -0.232 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F134 · Trend: deposit growth over the past four quarters, what the model did with it · 2019-09-30 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F135 · Trend: construction loans as a share of loans, value at the as-of quarter · 2019-09-30 · 4.8% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F136 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 1.8% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F137 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 4.4% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F140 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2019-09-30 · -0.461 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F141 · Trend: construction loans as a share of loans, what the model did with it · 2019-09-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F142 · Trend: ratios outside their own prior range · 2019-09-30 · 12 · data/features/fct_bank_features.parquet
- F144 · Trend: ratios compared with their own prior range · 2019-09-30 · 30 · data/features/fct_bank_features.parquet
- F145 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F146 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F147 · Percentile a year earlier (100 = highest risk) · 2018-09-30 · 99.9% · data/analyst/scores.parquet: percentile
- F148 · Trend: how the model's rating compares with a year earlier · 2019-09-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
