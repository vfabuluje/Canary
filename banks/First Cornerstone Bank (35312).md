---
cert: 35312
name: "First Cornerstone Bank"
as_of: 2016-03-31
rank: 2
n_banks: 6193
percentile: 99.98385273696108
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2016-05-06
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:51:28"
writer_model: "claude-opus-5-5"
checked: true
---

# First Cornerstone Bank (cert 35312)

*Hindsight: failed 2016-05-06. Canary flagged it 1 quarter ahead.*

## Summary

First Cornerstone Bank, a Pennsylvania bank, ranked 2 out of 6,193 banks nationwide on Canary's risk score as of 2016-03-31, placing it in the 100.0th percentile, where higher means riskier. That put it on Canary's watchlist, which covers the 2% of banks with the highest scores. Its cushion of owners' money (equity) was just 2.0% of assets, against a national median of 10.9%. It was also losing money, with a return on assets of -4.4% against a national median of 0.9%, and 8.1% of its loans were seriously overdue or no longer paying interest, against a median of 0.7%.

## Warning signs in the data

Capital, the bank's own money that absorbs losses before depositors are hurt, was very thin. Equity was 2.0% of assets against a national median of 10.9%, and the leverage ratio (core capital as a share of average assets) was 2.0% against 10.4%. Risk-based measures, which weigh assets by how risky they are, told the same story: the Tier 1 ratio was 3.9% against a median of 15.2%, and the total risk-based ratio was 5.1% against 16.4%.

Credit quality was weak: loans seriously overdue or no longer paying interest were 8.1% of loans, far above the national median of 0.7%. Loans in the early stages of being overdue were 5.4% of assets against a median of 0.3%, and the Texas ratio, which compares troubled assets with capital plus reserves, stood at 299.1% against a median of 5.5%. The bank was also unprofitable, with a return on equity of -180.8% against a national median of 7.7%, and operating costs ran at 503.1% of revenue against a median of 70.4%.

Funding and liquidity looked steadier: cash was 37.8% of assets against a median of 7.0%, and core deposits, the stable everyday kind, were 96.9% of assets against 78.9%. Unrealized losses on bonds available for sale were small at -0.3% of equity, milder than the national median of -0.9%. The bank was shrinking, with asset growth of -10.0% over the past four quarters against median growth of 3.0%.

## Understanding the score

As of 2016-03-31, First Cornerstone Bank ranked 2 out of 6,193 banks, which is the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was one of 124 banks on the watchlist that quarter, the group making up the top 2% of scores.

Five features pushed the score up most. They were the Tier 1 risk-based capital ratio at 3.9%, the Texas ratio at 299.1%, and return on equity at -180.8%. Next came the total risk-based capital ratio at 5.1% and seriously overdue or non-paying loans at 8.1% of loans.

Five features pulled the score down. The largest was interest expense at 0.8% of assets, followed by commercial real estate loans at 54.9% of loans and volatile, rate-sensitive funding at 0.9% of assets. Construction loans at 3.0% of loans and losses on bonds available for sale at -0.3% of equity also nudged the score down slightly.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 2 | 6,193 | ▲ watchlist (first flag) |

## How its ratios moved

Canary compares each ratio with the bank's own range over the prior 12 quarters, and 16 of 30 ratios checked were outside that range, with the 6 furthest out shown in the table. Return on equity was -180.8%, far below its prior range of -62.5% to -32.2%, and its contribution of +1.280 model log-odds units pushed the score up. Return on assets was -4.4%, below its prior range of -3.4% to -1.9%, and its contribution of +0.201 pushed the score up.

Loans in the early stages of being overdue were 5.4% of assets, above their prior range of 0.4% to 3.3%, and their contribution of +0.312 pushed the score up. The efficiency ratio was 503.1%, well above its prior range of 158.2% to 254.0%, yet its contribution of -0.031 had little effect on the score. Net loan write-offs were 0.5% of loans, above a prior range of 0.0% to 0.0%, but their contribution of +0.018 had little effect on the score. Uninsured deposits were 9.5% of deposits, above their prior range of 5.9% to 8.3%, yet their contribution of -0.092 pushed the score down.

There is no score from a year earlier to compare with (scores start 2016-03-31, or the bank did not report then).

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -180.8% | -62.5% to -32.2% | same quarter, prior 3 years | n/a | -118.3 pp | +1.280 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 503.1% | 158.2% to 254.0% | same quarter, prior 3 years | n/a | +249.2 pp | -0.031 | little effect on the score |
| loans 30-89 days past due, as a share of assets | 5.4% | 0.4% to 3.3% | prior 12 quarters | +2.5 pp | +2.1 pp | +0.312 | pushed the score up |
| return on assets (profit as a share of assets) | -4.4% | -3.4% to -1.9% | same quarter, prior 3 years | n/a | -1.0 pp | +0.201 | pushed the score up |
| uninsured deposits as a share of deposits | 9.5% | 5.9% to 8.3% | prior 12 quarters | +1.2 pp | +3.1 pp | -0.092 | pushed the score down |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.5% | 0.0% to 0.0% | same quarter, prior 3 years | n/a | +0.5 pp | +0.018 | little effect on the score |

16 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Canary first flagged the bank in the quarter ending 2016-03-31, which was also the last quarter the bank reported. The bank failed on 2016-05-06, giving a lead time of 1 quarter between the first flag and the failure. This counts as a caught case, though the flag came late in the bank's decline.

## What happened next

Looking back with hindsight, the bank failed on 2016-05-06. Its last report was for the quarter ending 2016-03-31, so no later ranks exist for it.

## Sources

- F1 · Bank name · n/a · First Cornerstone Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2016-03-31 · 2016-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · PA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-03-31 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-03-31 · 6,193 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-03-31 · 124 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-03-31 · 2.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-03-31 · 10.9% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-03-31 · 2.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-03-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-03-31 · 3.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-03-31 · 15.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-03-31 · 5.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-03-31 · 16.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-03-31 · 8.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-03-31 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2016-03-31 · 5.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2016-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2016-03-31 · 299.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2016-03-31 · 5.5% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-03-31 · -4.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-03-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2016-03-31 · -180.8% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2016-03-31 · 7.7% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2016-03-31 · 503.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2016-03-31 · 70.4% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2016-03-31 · 96.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2016-03-31 · 78.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2016-03-31 · 37.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2016-03-31 · 7.0% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2016-03-31 · -0.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2016-03-31 · -0.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2016-03-31 · -10.0% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2016-03-31 · 3.0% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 3.9%; contribution to the score · 2016-03-31 · +2.057 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 299.1%; contribution to the score · 2016-03-31 · +1.339 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: return on equity (profit as a share of equity), value -180.8%; contribution to the score · 2016-03-31 · +1.280 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 5.1%; contribution to the score · 2016-03-31 · +0.446 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: loans 90+ days past due or not accruing interest, as a share of loans, value 8.1%; contribution to the score · 2016-03-31 · +0.438 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.8%; contribution to the score · 2016-03-31 · -0.850 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: commercial real estate loans as a share of loans, value 54.9%; contribution to the score · 2016-03-31 · -0.399 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F82 · Driver down #3: volatile funding as a share of assets, value 0.9%; contribution to the score · 2016-03-31 · -0.242 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F83 · Driver down #4: construction loans as a share of loans, value 3.0%; contribution to the score · 2016-03-31 · -0.156 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F84 · Driver down #5: losses on bonds available for sale, as a share of equity, value -0.3%; contribution to the score · 2016-03-31 · -0.099 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F85 · Failure date · 2016-05-06 · 2016-05-06 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 1 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Last quarter the bank reported · 2016-03-31 · 2016-03-31 · data/features/fct_bank_features.parquet: report_date
- F89 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2016-03-31 · -180.8% · data/features/fct_bank_features.parquet: return_on_equity
- F90 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -62.5% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -32.2% · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2016-03-31 · +1.280 · data/analyst/scores.parquet: feature return_on_equity contribution
- F94 · Trend: return on equity (profit as a share of equity), what the model did with it · 2016-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2016-03-31 · 503.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F96 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 158.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 254.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2016-03-31 · -0.031 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F100 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2016-03-31 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F101 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2016-03-31 · 5.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F102 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F103 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 3.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F106 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2016-03-31 · +0.312 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F107 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2016-03-31 · pushed the score up · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F108 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2016-03-31 · -4.4% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F110 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -1.9% · data/features/fct_bank_features.parquet: return_on_assets
- F112 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2016-03-31 · +0.201 · data/analyst/scores.parquet: feature return_on_assets contribution
- F113 · Trend: return on assets (profit as a share of assets), what the model did with it · 2016-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F114 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2016-03-31 · 9.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F115 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 5.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F116 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 8.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F119 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2016-03-31 · -0.092 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F120 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2016-03-31 · pushed the score down · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F121 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2016-03-31 · 0.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F122 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F123 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F125 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2016-03-31 · +0.018 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F126 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2016-03-31 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F127 · Trend: ratios outside their own prior range · 2016-03-31 · 16 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios shown in the table (the furthest outside their prior range) · 2016-03-31 · 6 · data/features/fct_bank_features.parquet
- F129 · Trend: ratios compared with their own prior range · 2016-03-31 · 30 · data/features/fct_bank_features.parquet
- F130 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
