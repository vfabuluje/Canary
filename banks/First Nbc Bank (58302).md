---
cert: 58302
name: "First Nbc Bank"
as_of: 2017-03-31
rank: 2
n_banks: 5925
percentile: 99.98312236286921
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-04-28
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:52:23"
writer_model: "claude-opus-5-5"
checked: true
---

# First Nbc Bank (cert 58302)

*Hindsight: failed 2017-04-28. Canary flagged it 2 quarters ahead.*

## Summary

As of 2017-03-31, First Nbc Bank in LA ranked 2 out of 5,925 FDIC-insured banks on Canary's risk score, placing it in the 100.0th percentile, where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks by score. Its equity, the owners' cushion against losses, stood at -3.4% of assets against a national median of 10.7%, and 22.0% of its loans were seriously overdue or no longer paying interest, against a median of 0.6%.

## Warning signs in the data

Capital, the money owners have at stake to absorb losses, was negative on every measure: equity was -3.4% of assets versus a national median of 10.7%, and the leverage ratio (core capital as a share of average assets) was -2.0% versus 10.5%. The Tier 1 risk-based capital ratio, which weighs assets by how risky they are, was -3.1% against a median of 15.1%, and the total risk-based capital ratio was -1.7% against 16.2%. The Texas ratio, which compares troubled assets with capital plus reserves, was 225.4%, far above the national median of 4.8%.

Credit quality was very weak: loans 90+ days past due or not accruing interest were 22.0% of loans versus a median of 0.6%, and nonaccrual assets plus foreclosed property were 17.3% of assets versus 0.5%. Loan-loss reserves, money set aside for expected bad loans, were 14.3% of loans, well above the median of 1.2%.

On funding, uninsured deposits (balances above the government insurance limit) were 45.5% of deposits versus a median of 17.3%, and volatile funding, money that can leave quickly, was 19.3% of assets versus 5.1%. Assets shrank by -31.5% and deposits by -23.4% over the past four quarters, while the national medians grew by 3.9% and 4.3%. Losses on bonds available for sale were -1.6% of equity, below the national median of 0.3%, so bond losses were not a source of strain in this data.

## Understanding the score

First Nbc Bank ranked 2 out of 5,925 banks as of 2017-03-31, which puts it in the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, one of 119 banks that quarter, a list covering the top 2% of banks.

Five factors pushed the score up most: the Tier 1 risk-based capital ratio at -3.1% (contribution +2.032), the Texas ratio at 225.4% (+1.227), return on equity, meaning profit as a share of owners' capital, whose value is not shown in our data (+1.175), loans 90+ days past due or not accruing at 22.0% (+0.792), and the total risk-based capital ratio at -1.7% (+0.683). Five factors pulled it down: return on assets, or profit as a share of assets, at 3.1% (-0.596), losses on bonds available for sale at -1.6% of equity (-0.198), loans 30-89 days past due at 1.2% of assets (-0.135), construction loans at 13.5% of loans (-0.127), and brokered deposits, money placed through middlemen, at 3.8% of deposits (-0.091). The upward pushes were much larger than the downward ones.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 191 | 6,193 |  |
| 2016-06-30 | 138 | 6,129 |  |
| 2016-09-30 | 135 | 6,051 |  |
| 2016-12-31 | 2 | 5,983 | ▲ watchlist (first flag) |
| 2017-03-31 | 2 | 5,925 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own range over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 29 ratios compared, 21 sat outside their own prior range at 2017-03-31. The bank was in the 96.9th percentile on 2016-03-31, and the model rated it riskier than a year earlier, at rank 2.

Volatile funding was 19.3% of assets, above its prior range of 9.8% to 12.9%, and contributed +0.053 log-odds units, which pushed the score up. Cash was 18.6% of assets, well above its prior range of 1.1% to 7.6%, yet it contributed -0.019 and had little effect on the score. Loans as a share of deposits fell to 72.8%, below its prior range of 88.1% to 101.0%, but contributed -0.043 and had little effect on the score.

Return on assets was 3.1%, above its prior range of 1.1% to 2.0%, and contributed -0.596, so this unusual reading pushed the score down rather than up. The efficiency ratio was 50.7%, below its prior range of 76.9% to 103.0%, and contributed +0.050, with little effect on the score. Interest expense was 2.1% of assets, above its prior range of 1.1% to 1.2%, and contributed +0.036, with little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| volatile funding as a share of assets | 19.3% | 9.8% to 12.9% | prior 12 quarters | +6.3 pp | +9.3 pp | +0.053 | pushed the score up |
| cash as a share of assets | 18.6% | 1.1% to 7.6% | prior 12 quarters | +15.3 pp | +11.0 pp | -0.019 | little effect on the score |
| loans as a share of deposits | 72.8% | 88.1% to 101.0% | prior 12 quarters | -28.2 pp | -16.9 pp | -0.043 | little effect on the score |
| return on assets (profit as a share of assets) | 3.1% | 1.1% to 2.0% | same quarter, prior 3 years | n/a | +1.2 pp | -0.596 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 50.7% | 76.9% to 103.0% | same quarter, prior 3 years | n/a | -52.2 pp | +0.050 | little effect on the score |
| annualized interest expense as a share of assets | 2.1% | 1.1% to 1.2% | same quarter, prior 3 years | n/a | +1.0 pp | +0.036 | little effect on the score |

21 of 29 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Canary first flagged First Nbc Bank in the quarter ending 2016-12-31, and the bank failed on 2017-04-28, a lead time of 2 quarters. At that first flag, the biggest upward drivers were the Tier 1 risk-based capital ratio at -2.8% (+2.123), return on equity at -169.3% (+1.396), and the Texas ratio at 259.1% (+1.242). Loans 90+ days past due or not accruing were already 14.6% of loans then (+0.844).

## What happened next

With hindsight: the bank failed on 2017-04-28. Its last reported quarter was 2017-03-31, so no later ranks or flags exist in our data. Our data records only that a bank stopped reporting, without distinguishing a merger from a closure, but here the failure date is on record.

## Sources

- F1 · Bank name · n/a · First Nbc Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · LA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2017-03-31 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2017-03-31 · 5,925 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2017-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2017-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2017-03-31 · 119 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2017-03-31 · -3.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2017-03-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · -2.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2017-03-31 · -3.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2017-03-31 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2017-03-31 · -1.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2017-03-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 22.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 17.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2017-03-31 · 14.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2017-03-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 225.4% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 4.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F49 · Bank: uninsured deposits as a share of deposits · 2017-03-31 · 45.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F50 · National median: uninsured deposits as a share of deposits · 2017-03-31 · 17.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: volatile funding as a share of assets · 2017-03-31 · 19.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F58 · National median: volatile funding as a share of assets · 2017-03-31 · 5.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F63 · Bank: losses on bonds available for sale, as a share of equity · 2017-03-31 · -1.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F64 · National median: losses on bonds available for sale, as a share of equity · 2017-03-31 · 0.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: asset growth over the past four quarters · 2017-03-31 · -31.5% · data/features/fct_bank_features.parquet: asset_growth_4q
- F70 · National median: asset growth over the past four quarters · 2017-03-31 · 3.9% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F71 · Bank: deposit growth over the past four quarters · 2017-03-31 · -23.4% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F72 · National median: deposit growth over the past four quarters · 2017-03-31 · 4.3% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F73 · Driver up #1: the Tier 1 risk-based capital ratio, value -3.1%; contribution to the score · 2017-03-31 · +2.032 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F74 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 225.4%; contribution to the score · 2017-03-31 · +1.227 · data/analyst/scores.parquet: feature texas_ratio contribution
- F75 · Driver up #3: return on equity (profit as a share of equity); contribution to the score · 2017-03-31 · +1.175 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 22.0%; contribution to the score · 2017-03-31 · +0.792 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F77 · Driver up #5: the total risk-based capital ratio, value -1.7%; contribution to the score · 2017-03-31 · +0.683 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F78 · Driver down #1: return on assets (profit as a share of assets), value 3.1%; contribution to the score · 2017-03-31 · -0.596 · data/analyst/scores.parquet: feature return_on_assets contribution
- F79 · Driver down #2: losses on bonds available for sale, as a share of equity, value -1.6%; contribution to the score · 2017-03-31 · -0.198 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F80 · Driver down #3: loans 30-89 days past due, as a share of assets, value 1.2%; contribution to the score · 2017-03-31 · -0.135 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F81 · Driver down #4: construction loans as a share of loans, value 13.5%; contribution to the score · 2017-03-31 · -0.127 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #5: brokered deposits as a share of deposits, value 3.8%; contribution to the score · 2017-03-31 · -0.091 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F83 · Failure date · 2017-04-28 · 2017-04-28 · data/raw/failures: FAILDATE
- F84 · First flag quarter (Phase 3 lead-time rule) · 2016-12-31 · 2016-12-31 · data/analyst/scores.parquet: flagged
- F85 · Lead time in quarters before failure · n/a · 2 · data/analyst/scores.parquet: quarters_until_failure
- F86 · Driver up #1 at 2016-12-31: the Tier 1 risk-based capital ratio, value -2.8%; contribution to the score · 2016-12-31 · +2.123 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F87 · Driver up #2 at 2016-12-31: return on equity (profit as a share of equity), value -169.3%; contribution to the score · 2016-12-31 · +1.396 · data/analyst/scores.parquet: feature return_on_equity contribution
- F88 · Driver up #3 at 2016-12-31: the Texas ratio (troubled assets against capital plus reserves), value 259.1%; contribution to the score · 2016-12-31 · +1.242 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Driver up #4 at 2016-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 14.6%; contribution to the score · 2016-12-31 · +0.844 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F96 · Last quarter the bank reported · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
- F97 · Trend: volatile funding as a share of assets, value at the as-of quarter · 2017-03-31 · 19.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F98 · Trend: volatile funding as a share of assets, lowest value in the comparison window · n/a · 9.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F99 · Trend: volatile funding as a share of assets, highest value in the comparison window · n/a · 12.9% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F102 · Trend: volatile funding as a share of assets, contribution to the score (model log-odds units) · 2017-03-31 · +0.053 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F103 · Trend: volatile funding as a share of assets, what the model did with it · 2017-03-31 · pushed the score up · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F104 · Trend: cash as a share of assets, value at the as-of quarter · 2017-03-31 · 18.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F105 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F106 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 7.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F109 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2017-03-31 · -0.019 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F110 · Trend: cash as a share of assets, what the model did with it · 2017-03-31 · little effect on the score · data/analyst/scores.parquet: feature cash_to_assets contribution
- F111 · Trend: loans as a share of deposits, value at the as-of quarter · 2017-03-31 · 72.8% · data/features/fct_bank_features.parquet: loans_to_deposits
- F112 · Trend: loans as a share of deposits, lowest value in the comparison window · n/a · 88.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F113 · Trend: loans as a share of deposits, highest value in the comparison window · n/a · 101.0% · data/features/fct_bank_features.parquet: loans_to_deposits
- F116 · Trend: loans as a share of deposits, contribution to the score (model log-odds units) · 2017-03-31 · -0.043 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F117 · Trend: loans as a share of deposits, what the model did with it · 2017-03-31 · little effect on the score · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F118 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2017-03-31 · 3.1% · data/features/fct_bank_features.parquet: return_on_assets
- F119 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: return_on_assets
- F120 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 2.0% · data/features/fct_bank_features.parquet: return_on_assets
- F122 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2017-03-31 · -0.596 · data/analyst/scores.parquet: feature return_on_assets contribution
- F123 · Trend: return on assets (profit as a share of assets), what the model did with it · 2017-03-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F124 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2017-03-31 · 50.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F125 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 76.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F126 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 103.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F128 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2017-03-31 · +0.050 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F129 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2017-03-31 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F130 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2017-03-31 · 2.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F131 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F132 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F134 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2017-03-31 · +0.036 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F135 · Trend: annualized interest expense as a share of assets, what the model did with it · 2017-03-31 · little effect on the score · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F136 · Trend: ratios outside their own prior range · 2017-03-31 · 21 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios compared with their own prior range · 2017-03-31 · 29 · data/features/fct_bank_features.parquet
- F139 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F140 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F141 · Percentile a year earlier (100 = highest risk) · 2016-03-31 · 96.9% · data/analyst/scores.parquet: percentile
- F142 · Trend: how the model's rating compares with a year earlier · 2017-03-31 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
