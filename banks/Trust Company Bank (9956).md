---
cert: 9956
name: "Trust Company Bank"
as_of: 2016-03-31
rank: 3
n_banks: 6193
percentile: 99.96770547392218
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2016-04-29
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:47:51"
writer_model: "claude-opus-5-5"
checked: true
---

# Trust Company Bank (cert 9956)

*Hindsight: failed 2016-04-29. Canary flagged it 1 quarter ahead.*

## Summary

As of March 31, 2016, Trust Company Bank, a TN bank, ranked 3 out of 6,193 banks nationwide on Canary's risk score, which puts it in the 100.0th percentile, where higher means riskier. That placed it on Canary's watchlist, which holds the top 2% of banks by score. Its capital, the owners' cushion against losses, was negative, with equity at -6.5% of assets against a national median of 10.9%. Problem loans were also far above typical levels, at 13.4% of loans against a national median of 0.7%.

## Warning signs in the data

Capital was the clearest problem: equity as a share of assets was -6.5%, against a national median of 10.9%, meaning losses had used up more than the owners' entire stake. The leverage ratio (core capital as a share of average assets) was -6.2% against a median of 10.4%, the Tier 1 risk-based capital ratio (core capital measured against risk-weighted assets) was -12.5% against 15.2%, and the total risk-based capital ratio was -11.1% against 16.4%. The bank lost money heavily, with return on assets (profit as a share of assets) at -34.3% against a median of 0.9%, and an efficiency ratio (operating costs as a share of revenue) of 393.0% against 70.4%.

Credit quality was weak: loans 90+ days past due or no longer earning interest were 13.4% of loans against a national median of 0.7%, and nonaccrual assets plus foreclosed property were 14.3% of assets against 0.6%. Loans in the earlier stage of lateness were 3.7% of assets against a median of 0.3%, and the annualized provision for loan losses (money set aside for expected bad loans) was 5.6% of assets against 0.0%. Loan-loss reserves stood at 5.7% of loans, well above the median of 1.3%.

Funding looked stable on paper: uninsured deposits were 0.0% of deposits against a median of 16.6%, brokered deposits (funds placed through middlemen) were 0.0%, and cash was 14.1% of assets against 7.0%. The bank was small and shrinking, with total assets of $19.0 million against a median of $192.6 million, asset growth of -30.5% and deposit growth of -16.9% over the past four quarters. Unrealized losses on bonds were modest, at 2.8% of equity for bonds held to maturity and 0.6% for bonds available for sale.

## Understanding the score

As of 2016-03-31, Trust Company Bank ranked 3 of 6,193 banks, in the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks and held 124 banks that quarter.

The five factors pushing the score up most were the Tier 1 risk-based capital ratio at -12.5% (+1.605), return on equity, meaning profit as a share of equity (+1.137), the total risk-based capital ratio at -11.1% (+0.686), loans 90+ days past due or not accruing interest at 13.4% of loans (+0.637), and equity at -6.5% of assets (+0.473).

The five factors pulling the score down most were interest expense at 0.8% of assets (-0.992), the Texas ratio, which compares troubled assets with capital plus reserves, at -457.7% (-0.965), construction loans at 4.9% of loans (-0.209), deposit growth of -16.9% (-0.114), and the efficiency ratio at 393.0% (-0.071). The odd negative Texas ratio comes from the bank's negative capital, and the model treated it as lowering the score.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 3 | 6,193 | ▲ watchlist (first flag) |

## How its ratios moved

Each ratio is compared with its own prior range over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. As of 2016-03-31, 17 of 29 ratios checked sat outside their own prior range, and the table shows the 6 furthest outside. The bank ranked 3 of 6,193 banks that quarter.

The Tier 1 risk-based capital ratio was -12.5%, below its prior range of 0.1% to 6.0% after a drop of -15.0 pp in one quarter, and its contribution of +1.605 model log-odds units pushed the score up. The total risk-based capital ratio was -11.1%, below its prior range of 0.2% to 6.6%, and its contribution of +0.686 pushed the score up. The annualized provision for loan losses was 5.6% of assets, above its prior range of 0.0% to 0.7%, and its contribution of +0.164 pushed the score up. Return on assets was -34.3%, far below its prior range of -6.6% to -4.5% after a change of -27.6 pp over four quarters, and its contribution of +0.118 pushed the score up.

By contrast, the Texas ratio was -457.7%, well outside its prior range of 45.3% to 296.1%, yet its contribution of -0.965 pushed the score down. Likewise, the efficiency ratio was 393.0%, above its prior range of 133.6% to 156.0%, yet its contribution of -0.071 pushed the score down.

There is no score from a year earlier to compare with (scores start 2016-03-31, or the bank did not report then).

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on assets (profit as a share of assets) | -34.3% | -6.6% to -4.5% | same quarter, prior 3 years | n/a | -27.6 pp | +0.118 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 393.0% | 133.6% to 156.0% | same quarter, prior 3 years | n/a | +237.0 pp | -0.071 | pushed the score down |
| annualized provision for loan losses as a share of assets | 5.6% | 0.0% to 0.7% | same quarter, prior 3 years | n/a | +5.6 pp | +0.164 | pushed the score up |
| the Tier 1 risk-based capital ratio | -12.5% | 0.1% to 6.0% | prior 12 quarters | -15.0 pp | -16.3 pp | +1.605 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | -457.7% | 45.3% to 296.1% | prior 12 quarters | -753.8 pp | -663.8 pp | -0.965 | pushed the score down |
| the total risk-based capital ratio | -11.1% | 0.2% to 6.6% | prior 12 quarters | -14.9 pp | -16.2 pp | +0.686 | pushed the score up |

17 of 29 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

With hindsight, this was a caught case: Canary first flagged the bank in the quarter ending 2016-03-31. The bank failed on 2016-04-29, giving a lead time of 1 quarter between the first flag and the failure. The lead time was short, but the bank was flagged before it failed.

## What happened next

In hindsight, Trust Company Bank failed on April 29, 2016. Its last reported quarter was 2016-03-31, so there are no later ranks or flags after the as-of quarter. The bank stopped reporting after that; in our data, stopping reporting can mean a merger or a closure, and the two are not distinguished.

## Sources

- F1 · Bank name · n/a · Trust Company Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2016-03-31 · 2016-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · TN · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-03-31 · 3 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-03-31 · 6,193 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-03-31 · 124 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-03-31 · -6.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-03-31 · 10.9% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-03-31 · -6.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-03-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-03-31 · -12.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-03-31 · 15.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-03-31 · -11.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-03-31 · 16.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-03-31 · 13.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-03-31 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-03-31 · 14.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-03-31 · 0.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2016-03-31 · 3.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2016-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2016-03-31 · 5.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2016-03-31 · 1.3% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2016-03-31 · 5.6% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2016-03-31 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-03-31 · -34.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-03-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F43 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2016-03-31 · 393.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F44 · National median: the efficiency ratio (operating costs as a share of revenue) · 2016-03-31 · 70.4% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F49 · Bank: uninsured deposits as a share of deposits · 2016-03-31 · 0.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F50 · National median: uninsured deposits as a share of deposits · 2016-03-31 · 16.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F51 · Bank: brokered deposits as a share of deposits · 2016-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F59 · Bank: cash as a share of assets · 2016-03-31 · 14.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F60 · National median: cash as a share of assets · 2016-03-31 · 7.0% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds held to maturity, as a share of equity · 2016-03-31 · 2.8% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F63 · Bank: losses on bonds available for sale, as a share of equity · 2016-03-31 · 0.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F67 · Bank: total assets · 2016-03-31 · $19.0 million · data/features/fct_bank_features.parquet: log_total_assets
- F68 · National median: total assets · 2016-03-31 · $192.6 million · data/features/fct_bank_features.parquet: log_total_assets (median of all banks)
- F69 · Bank: asset growth over the past four quarters · 2016-03-31 · -30.5% · data/features/fct_bank_features.parquet: asset_growth_4q
- F71 · Bank: deposit growth over the past four quarters · 2016-03-31 · -16.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F73 · Driver up #1: the Tier 1 risk-based capital ratio, value -12.5%; contribution to the score · 2016-03-31 · +1.605 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F74 · Driver up #2: return on equity (profit as a share of equity); contribution to the score · 2016-03-31 · +1.137 · data/analyst/scores.parquet: feature return_on_equity contribution
- F75 · Driver up #3: the total risk-based capital ratio, value -11.1%; contribution to the score · 2016-03-31 · +0.686 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F76 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 13.4%; contribution to the score · 2016-03-31 · +0.637 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F77 · Driver up #5: equity as a share of assets, value -6.5%; contribution to the score · 2016-03-31 · +0.473 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F78 · Driver down #1: annualized interest expense as a share of assets, value 0.8%; contribution to the score · 2016-03-31 · -0.992 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F79 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value -457.7%; contribution to the score · 2016-03-31 · -0.965 · data/analyst/scores.parquet: feature texas_ratio contribution
- F80 · Driver down #3: construction loans as a share of loans, value 4.9%; contribution to the score · 2016-03-31 · -0.209 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F81 · Driver down #4: deposit growth over the past four quarters, value -16.9%; contribution to the score · 2016-03-31 · -0.114 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F82 · Driver down #5: the efficiency ratio (operating costs as a share of revenue), value 393.0%; contribution to the score · 2016-03-31 · -0.071 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F83 · Failure date · 2016-04-29 · 2016-04-29 · data/raw/failures: FAILDATE
- F84 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F85 · Lead time in quarters before failure · n/a · 1 · data/analyst/scores.parquet: quarters_until_failure
- F86 · Last quarter the bank reported · 2016-03-31 · 2016-03-31 · data/features/fct_bank_features.parquet: report_date
- F87 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2016-03-31 · -34.3% · data/features/fct_bank_features.parquet: return_on_assets
- F88 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -6.6% · data/features/fct_bank_features.parquet: return_on_assets
- F89 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -4.5% · data/features/fct_bank_features.parquet: return_on_assets
- F90 · Trend: return on assets (profit as a share of assets), change over four quarters, in percentage points · 2016-03-31 · -27.6 pp · data/features/fct_bank_features.parquet: return_on_assets
- F91 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2016-03-31 · +0.118 · data/analyst/scores.parquet: feature return_on_assets contribution
- F92 · Trend: return on assets (profit as a share of assets), what the model did with it · 2016-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2016-03-31 · 393.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F94 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 133.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 156.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2016-03-31 · -0.071 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2016-03-31 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F99 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2016-03-31 · 5.6% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F100 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F101 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F103 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2016-03-31 · +0.164 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F104 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2016-03-31 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F105 · Trend: the Tier 1 risk-based capital ratio, value at the as-of quarter · 2016-03-31 · -12.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F106 · Trend: the Tier 1 risk-based capital ratio, lowest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F107 · Trend: the Tier 1 risk-based capital ratio, highest value in the comparison window · n/a · 6.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F108 · Trend: the Tier 1 risk-based capital ratio, change over one quarter, in percentage points · 2016-03-31 · -15.0 pp · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F110 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2016-03-31 · +1.605 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F111 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2016-03-31 · pushed the score up · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F112 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2016-03-31 · -457.7% · data/features/fct_bank_features.parquet: texas_ratio
- F113 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 45.3% · data/features/fct_bank_features.parquet: texas_ratio
- F114 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 296.1% · data/features/fct_bank_features.parquet: texas_ratio
- F117 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2016-03-31 · -0.965 · data/analyst/scores.parquet: feature texas_ratio contribution
- F118 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2016-03-31 · pushed the score down · data/analyst/scores.parquet: feature texas_ratio contribution
- F119 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2016-03-31 · -11.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F120 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F121 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 6.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F124 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2016-03-31 · +0.686 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F125 · Trend: the total risk-based capital ratio, what the model did with it · 2016-03-31 · pushed the score up · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F126 · Trend: ratios outside their own prior range · 2016-03-31 · 17 · data/features/fct_bank_features.parquet
- F127 · Trend: ratios shown in the table (the furthest outside their prior range) · 2016-03-31 · 6 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios compared with their own prior range · 2016-03-31 · 29 · data/features/fct_bank_features.parquet
- F129 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F130 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
