---
cert: 1802
name: "Fayette County Bank"
as_of: 2017-03-31
rank: 1
n_banks: 5925
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-05-26
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:47:26"
writer_model: "claude-opus-5-5"
checked: true
---

# Fayette County Bank (cert 1802)

*Hindsight: failed 2017-05-26. Canary flagged it 4 quarters ahead.*

## Summary

Fayette County Bank (certificate 1802), an IL bank, ranked 1 out of 5,925 banks nationally in Canary's model as of 2017-03-31, placing it in the 100.0th percentile, where higher means riskier. That put it on Canary's watchlist, which covers the 2% of banks with the highest scores. Its capital cushion was very thin, with equity at 1.0% of assets against a national median of 10.7%. Problem loans were also high: 13.3% of its loans were 90 or more days late or no longer earning interest, compared with a national median of 0.6%.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was far below typical levels: equity was 1.0% of assets versus a national median of 10.7%, and the leverage ratio (core capital as a share of average assets) was 0.9% versus 10.5%. Risk-weighted measures, which give riskier assets more weight, told the same story, with a Tier 1 risk-based capital ratio of 1.3% against a median of 15.1% and a total risk-based capital ratio of 2.6% against 16.2%.

Credit quality was weak: loans 90 or more days past due or not accruing interest were 13.3% of loans versus a median of 0.6%, and loans at an earlier stage of lateness were 5.0% of assets versus a median of 0.3%. Nonaccrual assets and foreclosed property were 9.7% of assets against a median of 0.5%, and the Texas ratio, which compares troubled assets with capital plus reserves, stood at 247.7% versus a median of 4.8%. The bank was losing money, with return on assets of -1.3% versus a median of 0.9% and operating costs at 130.2% of revenue versus a median of 69.8%.

On funding, brokered deposits (money placed through outside intermediaries rather than gathered from local customers) were 25.0% of deposits, well above the national median of 0.0%, while cash was 2.4% of assets against a median of 6.9%. Losses on bonds available for sale (bonds the bank may sell before they mature) were -9.2% of equity, compared with a national median of 0.3%.

## Understanding the score

As of 2017-03-31, the bank ranked 1 out of 5,925 banks, the 100.0th percentile, with a model score of 0.9984. It was flagged on the watchlist, one of 119 banks that quarter, which make up the riskiest 2% of banks.

Five features pushed the score up most: the Tier 1 risk-based capital ratio at 1.3% (contribution +2.037), return on equity at -118.2% (+1.311), the Texas ratio at 247.7% (+1.137), loans 90 or more days late or not accruing interest at 13.3% of loans (+0.686), and the leverage ratio at 0.9% (+0.557). Five features pulled the score down slightly: construction loans at 2.1% of loans (-0.228), losses on bonds available for sale at -9.2% of equity (-0.198), interest expense at 1.1% of assets (-0.180), volatile funding at 1.9% of assets (-0.070), and core deposits, the stable everyday deposits, at 72.3% of assets (-0.061).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 13 | 6,193 | ▲ watchlist |
| 2016-06-30 | 6 | 6,129 | ▲ watchlist (first flag) |
| 2016-09-30 | 3 | 6,051 | ▲ watchlist |
| 2016-12-31 | 1 | 5,983 | ▲ watchlist |
| 2017-03-31 | 1 | 5,925 | ▲ watchlist |

## How its ratios moved

Canary compares each ratio with its own prior range, usually over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 30 ratios checked, 8 sat outside their prior range, and the 6 furthest outside are discussed here. The bank ranked 1 out of 5,925 in the 100.0th percentile, compared with the 99.8th percentile a year earlier, so the model rated it about the same as a year earlier.

The provision for loan losses (money set aside for expected bad loans) was 0.5% of assets, below its prior range of 1.8% to 4.7% after a change of -4.2 pp, and its contribution of -0.052 log-odds units pushed the score down. Return on assets was -1.3%, above its prior range of -6.5% to -1.9% after a change of +5.2 pp, yet with a contribution of -0.029 it had little effect on the score. Interest expense was 1.1% of assets, above its prior range of 0.7% to 1.0%, but its contribution of -0.180 pushed the score down rather than up.

Losses on bonds available for sale were -9.2% of equity, below their prior range of -8.5% to 2.4% after a one-quarter change of -9.6 pp, yet their contribution of -0.198 pushed the score down. Core deposits were 72.3% of assets, above their prior range of 53.2% to 71.2% after a four-quarter change of +15.4 pp, and their contribution of -0.061 pushed the score down. Brokered deposits were 25.0% of deposits, below their prior range of 25.8% to 41.0% after a four-quarter change of -13.1 pp, yet their contribution of +0.334 pushed the score up.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | 0.5% | 1.8% to 4.7% | same quarter, prior 3 years | n/a | -4.2 pp | -0.052 | pushed the score down |
| return on assets (profit as a share of assets) | -1.3% | -6.5% to -1.9% | same quarter, prior 3 years | n/a | +5.2 pp | -0.029 | little effect on the score |
| annualized interest expense as a share of assets | 1.1% | 0.7% to 1.0% | same quarter, prior 3 years | n/a | +0.1 pp | -0.180 | pushed the score down |
| losses on bonds available for sale, as a share of equity | -9.2% | -8.5% to 2.4% | prior 12 quarters | -9.6 pp | -2.7 pp | -0.198 | pushed the score down |
| core deposits as a share of assets | 72.3% | 53.2% to 71.2% | prior 12 quarters | +1.0 pp | +15.4 pp | -0.061 | pushed the score down |
| brokered deposits as a share of deposits | 25.0% | 25.8% to 41.0% | prior 12 quarters | -0.8 pp | -13.1 pp | +0.334 | pushed the score up |

8 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Canary first flagged the bank in the quarter ending 2016-06-30, 4 quarters before it failed on 2017-05-26. At that first flag, the main drivers pushing the score up were return on equity at -74.1% (+1.121), the Tier 1 risk-based capital ratio at 6.1% (+1.056), and the Texas ratio at 136.2% (+0.880). Problem loans 90 or more days late or not accruing interest at 12.8% of loans (+0.668) and the total risk-based capital ratio at 7.4% (+0.390) completed the top five.

## What happened next

Looking back with hindsight, the bank failed on 2017-05-26. Its last reported quarter was 2017-03-31, so there are no later ranks or flags after the as-of date. Our data shows only that the bank stopped reporting; it does not by itself distinguish a merger from a closure.

## Sources

- F1 · Bank name · n/a · Fayette County Bank · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 1802 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F5 · Model score · 2017-03-31 · 0.9984 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2017-03-31 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2017-03-31 · 5,925 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2017-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F10 · On the watchlist · 2017-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2017-03-31 · 119 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2017-03-31 · 1.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2017-03-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · 0.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2017-03-31 · 1.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2017-03-31 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2017-03-31 · 2.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2017-03-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 13.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 9.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2017-03-31 · 5.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2017-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 247.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 4.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2017-03-31 · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2017-03-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2017-03-31 · 130.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2017-03-31 · 69.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2017-03-31 · 25.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2017-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2017-03-31 · 2.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2017-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2017-03-31 · -9.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2017-03-31 · 0.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 1.3%; contribution to the score · 2017-03-31 · +2.037 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -118.2%; contribution to the score · 2017-03-31 · +1.311 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 247.7%; contribution to the score · 2017-03-31 · +1.137 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 13.3%; contribution to the score · 2017-03-31 · +0.686 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the leverage ratio (core capital as a share of average assets), value 0.9%; contribution to the score · 2017-03-31 · +0.557 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #1: construction loans as a share of loans, value 2.1%; contribution to the score · 2017-03-31 · -0.228 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F81 · Driver down #2: losses on bonds available for sale, as a share of equity, value -9.2%; contribution to the score · 2017-03-31 · -0.198 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F82 · Driver down #3: annualized interest expense as a share of assets, value 1.1%; contribution to the score · 2017-03-31 · -0.180 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F83 · Driver down #4: volatile funding as a share of assets, value 1.9%; contribution to the score · 2017-03-31 · -0.070 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F84 · Driver down #5: core deposits as a share of assets, value 72.3%; contribution to the score · 2017-03-31 · -0.061 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F85 · Failure date · 2017-05-26 · 2017-05-26 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-06-30 · 2016-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-06-30: return on equity (profit as a share of equity), value -74.1%; contribution to the score · 2016-06-30 · +1.121 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2016-06-30: the Tier 1 risk-based capital ratio, value 6.1%; contribution to the score · 2016-06-30 · +1.056 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F90 · Driver up #3 at 2016-06-30: the Texas ratio (troubled assets against capital plus reserves), value 136.2%; contribution to the score · 2016-06-30 · +0.880 · data/analyst/scores.parquet: feature texas_ratio contribution
- F91 · Driver up #4 at 2016-06-30: loans 90+ days past due or not accruing interest, as a share of loans, value 12.8%; contribution to the score · 2016-06-30 · +0.668 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2016-06-30: the total risk-based capital ratio, value 7.4%; contribution to the score · 2016-06-30 · +0.390 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2017-03-31 · 0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F100 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 1.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F101 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 4.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F102 · Trend: annualized provision for loan losses as a share of assets, change over four quarters, in percentage points · 2017-03-31 · -4.2 pp · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F103 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2017-03-31 · -0.052 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F104 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2017-03-31 · pushed the score down · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F105 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2017-03-31 · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F106 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -6.5% · data/features/fct_bank_features.parquet: return_on_assets
- F107 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -1.9% · data/features/fct_bank_features.parquet: return_on_assets
- F108 · Trend: return on assets (profit as a share of assets), change over four quarters, in percentage points · 2017-03-31 · +5.2 pp · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2017-03-31 · -0.029 · data/analyst/scores.parquet: feature return_on_assets contribution
- F110 · Trend: return on assets (profit as a share of assets), what the model did with it · 2017-03-31 · little effect on the score · data/analyst/scores.parquet: feature return_on_assets contribution
- F111 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2017-03-31 · 1.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F112 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F113 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F115 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2017-03-31 · -0.180 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F116 · Trend: annualized interest expense as a share of assets, what the model did with it · 2017-03-31 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F117 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2017-03-31 · -9.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F118 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · -8.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F119 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 2.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F120 · Trend: losses on bonds available for sale, as a share of equity, change over one quarter, in percentage points · 2017-03-31 · -9.6 pp · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F122 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2017-03-31 · -0.198 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F123 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2017-03-31 · pushed the score down · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F124 · Trend: core deposits as a share of assets, value at the as-of quarter · 2017-03-31 · 72.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F125 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 53.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F126 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 71.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F128 · Trend: core deposits as a share of assets, change over four quarters, in percentage points · 2017-03-31 · +15.4 pp · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F129 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2017-03-31 · -0.061 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F130 · Trend: core deposits as a share of assets, what the model did with it · 2017-03-31 · pushed the score down · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F131 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2017-03-31 · 25.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F132 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 25.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F133 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 41.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F135 · Trend: brokered deposits as a share of deposits, change over four quarters, in percentage points · 2017-03-31 · -13.1 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F136 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2017-03-31 · +0.334 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F137 · Trend: brokered deposits as a share of deposits, what the model did with it · 2017-03-31 · pushed the score up · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F138 · Trend: ratios outside their own prior range · 2017-03-31 · 8 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios shown in the table (the furthest outside their prior range) · 2017-03-31 · 6 · data/features/fct_bank_features.parquet
- F140 · Trend: ratios compared with their own prior range · 2017-03-31 · 30 · data/features/fct_bank_features.parquet
- F141 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F142 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F143 · Percentile a year earlier (100 = highest risk) · 2016-03-31 · 99.8% · data/analyst/scores.parquet: percentile
- F144 · Trend: how the model's rating compares with a year earlier · 2017-03-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
