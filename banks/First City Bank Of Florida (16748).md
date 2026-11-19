---
cert: 16748
name: "First City Bank Of Florida"
as_of: 2020-09-30
rank: 2
n_banks: 5098
percentile: 99.98038446449588
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2020-10-16
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:48:36"
writer_model: "claude-opus-5-5"
checked: true
---

# First City Bank Of Florida (cert 16748)

*Hindsight: failed 2020-10-16. Canary flagged it 4 quarters ahead.*

## Summary

As of 2020-09-30, First City Bank Of Florida, a bank in FL, ranked 2 out of 5,098 banks nationally on Canary's risk score, placing it in the 100.0th percentile, where higher means riskier. It was on Canary's watchlist, the top 2% of banks by score, which held 102 banks that quarter. Its capital cushion was very thin: equity (the owners' stake) was 1.5% of assets against a national median of 10.9%, and it was losing money, with a return on assets of -1.5%.

## Warning signs in the data

Capital, the cushion that absorbs losses, was far below typical levels: the leverage ratio (core capital as a share of average assets) was 1.4% against a national median of 10.2%. The Tier 1 risk-based capital ratio, which weighs capital against the riskiness of assets, was 2.5% versus a median of 14.7%, and the total risk-based capital ratio was 3.7% versus 15.9%.

Credit quality was weak: nonaccrual assets (loans no longer paying interest) and foreclosed property made up 12.7% of assets, against a national median of 0.3%. Loans 30-89 days past due were 3.0% of assets versus a median of 0.2%, and loans 90+ days past due or not accruing interest were 1.6% of loans versus 0.5%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 489.0% against a median of 3.4%. Earnings were negative, with a return on equity of -68.6% versus a median of 8.7%, and operating costs ran at 148.2% of revenue versus a median of 65.6%.

Funding looked stable: core deposits, the steady everyday kind, were 98.1% of assets against a median of 78.8%, volatile funding was 0.0% versus 5.3%, and cash was 32.0% of assets versus 9.6%. Unrealized losses on bonds available for sale equaled -11.2% of equity, a deeper hit than the national median of -2.5%.

## Understanding the score

On 2020-09-30 the bank ranked 2 of 5,098 banks, the 100.0th percentile, with a model score of 0.9910, and it was flagged on the watchlist of the top 2% of banks.

The five factors that pushed the score up most were the Tier 1 risk-based capital ratio at 2.5% (+2.082), the Texas ratio at 489.0% (+1.510), return on equity at -68.6% (+1.438), the leverage ratio at 1.4% (+0.590) and the total risk-based capital ratio at 3.7% (+0.436).

The five factors that pulled the score down most were loans 90+ days past due or not accruing interest at 1.6% of loans (-0.686), interest expense at 0.3% of assets (-0.622), losses on bonds available for sale at -11.2% of equity (-0.375), uninsured deposits at 12.3% of deposits (-0.131) and net interest margin, the spread earned on lending, at 3.7% (-0.108).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2018-12-31 | 4 | 5,473 | ▲ watchlist |
| 2019-03-31 | 3 | 5,428 | ▲ watchlist |
| 2019-06-30 | 4 | 5,369 | ▲ watchlist |
| 2019-09-30 | 5 | 5,325 | ▲ watchlist |
| 2019-12-31 | 3 | 5,244 | ▲ watchlist (first flag) |
| 2020-03-31 | 2 | 5,182 | ▲ watchlist |
| 2020-06-30 | 2 | 5,131 | ▲ watchlist |
| 2020-09-30 | 2 | 5,098 | ▲ watchlist |

## How its ratios moved

Canary compares each ratio with its own range over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 30 ratios compared, 19 were outside their own prior range at 2020-09-30. The model rated the bank about the same as a year earlier: it sat in the 99.9th percentile then and ranked 2 of 5,098 now.

The Tier 1 risk-based capital ratio was 2.5%, below its prior range of 3.1% to 3.7%, and its contribution of +2.082 model log-odds units pushed the score up. The total risk-based capital ratio was 3.7%, below its prior range of 4.3% to 5.0%, and its contribution of +0.436 pushed the score up. Return on equity was -68.6%, below its prior range of -24.2% to -12.0%, and its contribution of +1.438 pushed the score up.

Return on assets was -1.5%, below its prior range of -0.6% to -0.3%, yet its contribution of +0.015 had little effect on the score. The efficiency ratio was 148.2%, above its prior range of 110.7% to 114.7%, yet its contribution of +0.010 had little effect on the score. Nonaccrual assets and foreclosed property were 12.7% of assets, below their prior range of 16.7% to 20.8%, and their contribution of +0.049 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 148.2% | 110.7% to 114.7% | same quarter, prior 3 years | n/a | +33.5 pp | +0.010 | little effect on the score |
| return on equity (profit as a share of equity) | -68.6% | -24.2% to -12.0% | same quarter, prior 3 years | n/a | -47.2 pp | +1.438 | pushed the score up |
| nonaccrual assets and foreclosed property, as a share of assets | 12.7% | 16.7% to 20.8% | prior 12 quarters | -4.1 pp | -5.2 pp | +0.049 | little effect on the score |
| return on assets (profit as a share of assets) | -1.5% | -0.6% to -0.3% | same quarter, prior 3 years | n/a | -0.9 pp | +0.015 | little effect on the score |
| the Tier 1 risk-based capital ratio | 2.5% | 3.1% to 3.7% | prior 12 quarters | -0.6 pp | -0.9 pp | +2.082 | pushed the score up |
| the total risk-based capital ratio | 3.7% | 4.3% to 5.0% | prior 12 quarters | -0.6 pp | -0.9 pp | +0.436 | pushed the score up |

19 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, the bank failed on 2020-10-16. Canary first flagged it in the quarter ending 2019-12-31, a lead time of 4 quarters before the failure, so this is a case the model caught. At that first flag, the top drivers were the Tier 1 risk-based capital ratio at 3.4% (+1.988) and the Texas ratio at 473.5% (+1.290).

## What happened next

In hindsight, the bank's last reported quarter was 2020-09-30, the same as the as-of quarter of this memo. It failed on 2020-10-16, so no later ranks exist.

## Sources

- F1 · Bank name · n/a · First City Bank Of Florida · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2020-09-30 · 2020-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · FL · data/raw/financials: STALP
- F5 · Model score · 2020-09-30 · 0.9910 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2020-09-30 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2020-09-30 · 5,098 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2020-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F10 · On the watchlist · 2020-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2020-09-30 · 102 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2020-09-30 · 1.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2020-09-30 · 10.9% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2020-09-30 · 1.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2020-09-30 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2020-09-30 · 2.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2020-09-30 · 14.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2020-09-30 · 3.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2020-09-30 · 15.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2020-09-30 · 1.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2020-09-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2020-09-30 · 12.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2020-09-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2020-09-30 · 3.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2020-09-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2020-09-30 · 489.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2020-09-30 · 3.4% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2020-09-30 · -1.5% · data/features/fct_bank_features.parquet: return_on_assets
- F41 · Bank: return on equity (profit as a share of equity) · 2020-09-30 · -68.6% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2020-09-30 · 8.7% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2020-09-30 · 148.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2020-09-30 · 65.6% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2020-09-30 · 98.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2020-09-30 · 78.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2020-09-30 · 5.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2020-09-30 · 32.0% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2020-09-30 · 9.6% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2020-09-30 · -11.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2020-09-30 · -2.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 2.5%; contribution to the score · 2020-09-30 · +2.082 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 489.0%; contribution to the score · 2020-09-30 · +1.510 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: return on equity (profit as a share of equity), value -68.6%; contribution to the score · 2020-09-30 · +1.438 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value 1.4%; contribution to the score · 2020-09-30 · +0.590 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 3.7%; contribution to the score · 2020-09-30 · +0.436 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: loans 90+ days past due or not accruing interest, as a share of loans, value 1.6%; contribution to the score · 2020-09-30 · -0.686 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 0.3%; contribution to the score · 2020-09-30 · -0.622 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: losses on bonds available for sale, as a share of equity, value -11.2%; contribution to the score · 2020-09-30 · -0.375 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F83 · Driver down #4: uninsured deposits as a share of deposits, value 12.3%; contribution to the score · 2020-09-30 · -0.131 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F84 · Driver down #5: net interest margin (the spread earned on lending and investing), value 3.7%; contribution to the score · 2020-09-30 · -0.108 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F85 · Failure date · 2020-10-16 · 2020-10-16 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2019-12-31 · 2019-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2019-12-31: the Tier 1 risk-based capital ratio, value 3.4%; contribution to the score · 2019-12-31 · +1.988 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2019-12-31: the Texas ratio (troubled assets against capital plus reserves), value 473.5%; contribution to the score · 2019-12-31 · +1.290 · data/analyst/scores.parquet: feature texas_ratio contribution
- F98 · Last quarter the bank reported · 2020-09-30 · 2020-09-30 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2020-09-30 · 148.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F100 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 110.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 114.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F103 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2020-09-30 · +0.010 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F104 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2020-09-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F105 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2020-09-30 · -68.6% · data/features/fct_bank_features.parquet: return_on_equity
- F106 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -24.2% · data/features/fct_bank_features.parquet: return_on_equity
- F107 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -12.0% · data/features/fct_bank_features.parquet: return_on_equity
- F109 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2020-09-30 · +1.438 · data/analyst/scores.parquet: feature return_on_equity contribution
- F110 · Trend: return on equity (profit as a share of equity), what the model did with it · 2020-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F111 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2020-09-30 · 12.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F112 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 16.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F113 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 20.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F116 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2020-09-30 · +0.049 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F117 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2020-09-30 · little effect on the score · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F118 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2020-09-30 · -1.5% · data/features/fct_bank_features.parquet: return_on_assets
- F119 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F120 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F122 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2020-09-30 · +0.015 · data/analyst/scores.parquet: feature return_on_assets contribution
- F123 · Trend: return on assets (profit as a share of assets), what the model did with it · 2020-09-30 · little effect on the score · data/analyst/scores.parquet: feature return_on_assets contribution
- F124 · Trend: the Tier 1 risk-based capital ratio, value at the as-of quarter · 2020-09-30 · 2.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F125 · Trend: the Tier 1 risk-based capital ratio, lowest value in the comparison window · n/a · 3.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F126 · Trend: the Tier 1 risk-based capital ratio, highest value in the comparison window · n/a · 3.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F129 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2020-09-30 · +2.082 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F130 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2020-09-30 · pushed the score up · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F131 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2020-09-30 · 3.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F132 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 4.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F133 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 5.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F136 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2020-09-30 · +0.436 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F137 · Trend: the total risk-based capital ratio, what the model did with it · 2020-09-30 · pushed the score up · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F138 · Trend: ratios outside their own prior range · 2020-09-30 · 19 · data/features/fct_bank_features.parquet
- F140 · Trend: ratios compared with their own prior range · 2020-09-30 · 30 · data/features/fct_bank_features.parquet
- F141 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F142 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F143 · Percentile a year earlier (100 = highest risk) · 2019-09-30 · 99.9% · data/analyst/scores.parquet: percentile
- F144 · Trend: how the model's rating compares with a year earlier · 2020-09-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
