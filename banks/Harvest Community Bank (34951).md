---
cert: 34951
name: "Harvest Community Bank"
as_of: 2016-12-31
rank: 3
n_banks: 5983
percentile: 99.9665719538693
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-01-13
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:51:05"
writer_model: "claude-opus-5-5"
checked: true
---

# Harvest Community Bank (cert 34951)

*Hindsight: failed 2017-01-13. Canary flagged it 4 quarters ahead.*

## Summary

Harvest Community Bank, a New Jersey bank with $124.2 million in total assets, ranked 3 out of 5,983 banks nationally on Canary's risk score as of 2016-12-31, placing it in the 100.0th percentile. That put it on Canary's watchlist, the 2% of banks with the highest scores. Its capital cushion (the owners' money that absorbs losses) was very thin, with equity at 1.4% of assets against a national median of 10.7%. At the same time, 18.2% of its loans were 90 or more days past due or no longer earning interest, far above the national median of 0.6%.

## Warning signs in the data

Capital was the weakest point: the leverage ratio (core capital as a share of average assets) was 1.4% against a national median of 10.4%. The Tier 1 risk-based capital ratio (core capital measured against riskier assets) was 1.9% versus a median of 15.0%, and the total risk-based capital ratio was 3.2% versus 16.2%. Profits were negative, with return on assets at -1.3% against a median of 0.9% and return on equity at -64.3% against 8.0%.

Credit quality, meaning how well borrowers were repaying, was poor. Loans 90 or more days past due or not accruing interest were 18.2% of loans against a median of 0.6%, and nonaccrual assets plus foreclosed property were 16.3% of assets against 0.5%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 382.7% versus a national median of 4.9%. Loans that were recently past due but not yet seriously late were 1.9% of assets, well above the median of 0.3%.

Funding looked steadier: core deposits (stable everyday deposits) were 96.6% of assets against a median of 78.8%, and uninsured deposits were only 2.3% of deposits versus 17.3%. Still, the bank was shrinking, with asset growth of -12.4% and deposit growth of -9.5% over the past four quarters, while the medians were 3.5% and 3.6%. Unrealized losses on bonds available for sale were 6.7% of equity, well above the median of 0.7%.

## Understanding the score

As of 2016-12-31, Harvest Community Bank ranked 3 out of 5,983 banks, the 100.0th percentile on a scale where higher means riskier. It was flagged on the watchlist, which held 120 banks that quarter, the top 2% by score.

The five factors that pushed the score up most were a Tier 1 risk-based capital ratio of 1.9% (+2.139), a Texas ratio of 382.7% (+1.450), and return on equity of -64.3% (+1.282). They also included loans 90 or more days past due or not accruing interest at 18.2% of loans (+0.755) and a leverage ratio of 1.4% (+0.636).

The five factors that pulled the score down most were interest expense at 0.7% of assets (-0.720), construction loans at 9.7% of loans (-0.124), and volatile funding at 1.8% of assets (-0.112). They also included cash at 5.6% of assets (-0.098) and an efficiency ratio, operating costs as a share of revenue, of 143.4% (-0.078).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 4 | 6,193 | ▲ watchlist (first flag) |
| 2016-06-30 | 3 | 6,129 | ▲ watchlist |
| 2016-09-30 | 1 | 6,051 | ▲ watchlist |
| 2016-12-31 | 3 | 5,983 | ▲ watchlist |

## How its ratios moved

As of 2016-12-31 the bank ranked 3 out of 5,983 banks, and 12 of the 30 ratios Canary tracks sat outside their own prior range, with the 6 furthest outside shown in the table. For most ratios the comparison window is the prior 12 quarters, and for year-to-date ratios it is the same quarter in the prior 3 years.

The Texas ratio reached 382.7%, above its prior range of 81.9% to 362.8% after rising +75.7 pp over four quarters, and its contribution of +1.450 model log-odds units pushed the score up. Losses on bonds available for sale were 6.7% of equity, above their prior range of -7.9% to 4.7%, and contributed +0.164, which pushed the score up. Core deposits were 96.6% of assets, above their prior range of 87.0% to 95.9%, and contributed +0.195, which pushed the score up.

The efficiency ratio was 143.4%, above its prior range of 82.3% to 139.7%, yet its contribution of -0.078 pushed the score down. Securities were 11.6% of assets, below their prior range of 12.3% to 21.1%, and their contribution of -0.061 pushed the score down. Uninsured deposits were 2.3% of deposits, below their prior range of 2.6% to 5.8%, but their contribution of +0.043 had little effect on the score.

There is no score from a year earlier to compare with (scores start 2016-03-31, or the bank did not report then).

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| losses on bonds available for sale, as a share of equity | 6.7% | -7.9% to 4.7% | prior 12 quarters | +11.7 pp | +2.0 pp | +0.164 | pushed the score up |
| uninsured deposits as a share of deposits | 2.3% | 2.6% to 5.8% | prior 12 quarters | -0.3 pp | -1.2 pp | +0.043 | little effect on the score |
| securities as a share of assets | 11.6% | 12.3% to 21.1% | prior 12 quarters | -0.7 pp | -2.2 pp | -0.061 | pushed the score down |
| core deposits as a share of assets | 96.6% | 87.0% to 95.9% | prior 12 quarters | +0.7 pp | +3.3 pp | +0.195 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 382.7% | 81.9% to 362.8% | prior 12 quarters | +19.9 pp | +75.7 pp | +1.450 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 143.4% | 82.3% to 139.7% | same quarter, prior 3 years | n/a | +3.7 pp | -0.078 | pushed the score down |

12 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Canary first flagged Harvest Community Bank in the quarter ending 2016-03-31, and the bank failed on 2017-01-13. That gave a lead time of 4 quarters before failure under Canary's lead-time rule.

At that first flag, the main factors pushing the score up were a Tier 1 risk-based capital ratio of 2.9% (+2.088), a Texas ratio of 322.2% (+1.217), and return on equity of -51.7% (+0.923). Loans 90 or more days past due or not accruing interest at 17.9% of loans (+0.661) and a total risk-based capital ratio of 4.2% (+0.492) completed the top five.

## What happened next

In hindsight, the last quarter Harvest Community Bank reported was 2016-12-31, the same quarter this memo describes. The bank failed on 2017-01-13, shortly after that report, so it has no later ranks or flags.

## Sources

- F1 · Bank name · n/a · Harvest Community Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NJ · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-12-31 · 3 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-12-31 · 5,983 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-12-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-12-31 · 120 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-12-31 · 1.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-12-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · 1.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-12-31 · 1.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-12-31 · 15.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-12-31 · 3.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-12-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 18.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 16.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2016-12-31 · 1.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2016-12-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2016-12-31 · 382.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2016-12-31 · 4.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-12-31 · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-12-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2016-12-31 · -64.3% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2016-12-31 · 8.0% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2016-12-31 · 2.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2016-12-31 · 17.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2016-12-31 · 96.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2016-12-31 · 78.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2016-12-31 · 6.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2016-12-31 · 0.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2016-12-31 · $124.2 million · data/features/fct_bank_features.parquet: log_total_assets
- F71 · Bank: asset growth over the past four quarters · 2016-12-31 · -12.4% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2016-12-31 · 3.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2016-12-31 · -9.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2016-12-31 · 3.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 1.9%; contribution to the score · 2016-12-31 · +2.139 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 382.7%; contribution to the score · 2016-12-31 · +1.450 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: return on equity (profit as a share of equity), value -64.3%; contribution to the score · 2016-12-31 · +1.282 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 18.2%; contribution to the score · 2016-12-31 · +0.755 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the leverage ratio (core capital as a share of average assets), value 1.4%; contribution to the score · 2016-12-31 · +0.636 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.7%; contribution to the score · 2016-12-31 · -0.720 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: construction loans as a share of loans, value 9.7%; contribution to the score · 2016-12-31 · -0.124 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: volatile funding as a share of assets, value 1.8%; contribution to the score · 2016-12-31 · -0.112 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F83 · Driver down #4: cash as a share of assets, value 5.6%; contribution to the score · 2016-12-31 · -0.098 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F84 · Driver down #5: the efficiency ratio (operating costs as a share of revenue), value 143.4%; contribution to the score · 2016-12-31 · -0.078 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F85 · Failure date · 2017-01-13 · 2017-01-13 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-03-31: the Tier 1 risk-based capital ratio, value 2.9%; contribution to the score · 2016-03-31 · +2.088 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2016-03-31: the Texas ratio (troubled assets against capital plus reserves), value 322.2%; contribution to the score · 2016-03-31 · +1.217 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2016-03-31: return on equity (profit as a share of equity), value -51.7%; contribution to the score · 2016-03-31 · +0.923 · data/analyst/scores.parquet: feature return_on_equity contribution
- F91 · Driver up #4 at 2016-03-31: loans 90+ days past due or not accruing interest, as a share of loans, value 17.9%; contribution to the score · 2016-03-31 · +0.661 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2016-03-31: the total risk-based capital ratio, value 4.2%; contribution to the score · 2016-03-31 · +0.492 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2016-12-31 · 6.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F100 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · -7.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F101 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 4.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F104 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2016-12-31 · +0.164 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F105 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2016-12-31 · pushed the score up · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F106 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2016-12-31 · 2.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F107 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 2.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F108 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 5.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F111 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2016-12-31 · +0.043 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F112 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2016-12-31 · little effect on the score · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F113 · Trend: securities as a share of assets, value at the as-of quarter · 2016-12-31 · 11.6% · data/features/fct_bank_features.parquet: securities_to_assets
- F114 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 12.3% · data/features/fct_bank_features.parquet: securities_to_assets
- F115 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 21.1% · data/features/fct_bank_features.parquet: securities_to_assets
- F118 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2016-12-31 · -0.061 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F119 · Trend: securities as a share of assets, what the model did with it · 2016-12-31 · pushed the score down · data/analyst/scores.parquet: feature securities_to_assets contribution
- F120 · Trend: core deposits as a share of assets, value at the as-of quarter · 2016-12-31 · 96.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F121 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 87.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F122 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 95.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F125 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2016-12-31 · +0.195 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F126 · Trend: core deposits as a share of assets, what the model did with it · 2016-12-31 · pushed the score up · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F127 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2016-12-31 · 382.7% · data/features/fct_bank_features.parquet: texas_ratio
- F128 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 81.9% · data/features/fct_bank_features.parquet: texas_ratio
- F129 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 362.8% · data/features/fct_bank_features.parquet: texas_ratio
- F131 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over four quarters, in percentage points · 2016-12-31 · +75.7 pp · data/features/fct_bank_features.parquet: texas_ratio
- F132 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2016-12-31 · +1.450 · data/analyst/scores.parquet: feature texas_ratio contribution
- F133 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2016-12-31 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F134 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2016-12-31 · 143.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F135 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 82.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F136 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 139.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F138 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2016-12-31 · -0.078 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F139 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2016-12-31 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F140 · Trend: ratios outside their own prior range · 2016-12-31 · 12 · data/features/fct_bank_features.parquet
- F141 · Trend: ratios shown in the table (the furthest outside their prior range) · 2016-12-31 · 6 · data/features/fct_bank_features.parquet
- F142 · Trend: ratios compared with their own prior range · 2016-12-31 · 30 · data/features/fct_bank_features.parquet
- F143 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F144 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
