---
cert: 15426
name: "Almena State Bank"
as_of: 2020-09-30
rank: 1
n_banks: 5098
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2020-10-23
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:48:36"
writer_model: "claude-opus-5-5"
checked: true
---

# Almena State Bank (cert 15426)

*Hindsight: failed 2020-10-23. Canary flagged it 4 quarters ahead.*

## Summary

As of 2020-09-30, Almena State Bank of KS ranked 1 out of 5,098 banks nationally in Canary's model, which puts it in the 100.0th percentile, where higher means riskier. It was flagged on the watchlist, which covers the riskiest 2% of banks. Its equity, the owners' cushion against losses, stood at 0.0% of assets against a national median of 10.9%, and 23.8% of its loans were 90+ days past due or not accruing interest, versus a median of 0.5%. The bank was also losing money, with a return on assets of -7.3% against a median of 1.0%.

## Warning signs in the data

Capital, the money a bank's owners have at risk to absorb losses, was nearly gone: equity was 0.0% of assets against a national median of 10.9%, and the leverage ratio (core capital as a share of average assets) was 0.0% against a median of 10.2%. The Tier 1 risk-based capital ratio, which weighs assets by how risky they are, was 0.0% versus a median of 14.7%, and the total risk-based capital ratio was 1.4% versus 15.9%.

Credit quality was weak: 23.8% of loans were 90+ days past due or not accruing interest, far above the median of 0.5%, and nonaccrual assets and foreclosed property made up 19.4% of assets versus 0.3%. The Texas ratio, which compares troubled assets with capital plus reserves, was 243.0% against a median of 3.4%. Loan-loss reserves, money set aside for expected bad loans, were 10.5% of loans versus a median of 1.2%, and annualized write-offs were 2.8% of loans versus 0.0%. Return on equity was -233.5% against a median of 8.7%.

On funding, brokered deposits, money placed through third-party brokers rather than gathered from local customers, were 31.4% of deposits versus a national median of 0.0%, while uninsured deposits were only 2.4% versus 21.3%. Deposits shrank by -15.7% over the past four quarters, while the median bank grew them by 15.0%. Unrealized losses on bonds available for sale, meaning bonds worth less than the bank paid, equaled -34.5% of equity, well beyond the median of -2.5%.

## Understanding the score

Almena State Bank ranked 1 of 5,098 banks on 2020-09-30, placing it in the 100.0th percentile on a scale of 0 to 100, where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks by score and included 102 banks that quarter.

The five features that pushed the score up most were the Tier 1 risk-based capital ratio at 0.0%, return on equity at -233.5%, the Texas ratio at 243.0%, loans 90+ days past due or not accruing at 23.8% of loans, and the total risk-based capital ratio at 1.4%. Their contributions were +1.798, +1.440, +1.035, +0.654 and +0.552 respectively.

The five features that pulled the score down most were losses on bonds available for sale at -34.5% of equity, deposit growth at -15.7%, construction loans at 0.0% of loans, loans 30-89 days past due at 1.2% of assets, and volatile funding at 2.0% of assets. Their contributions were -0.250, -0.140, -0.100, -0.090 and -0.078 respectively.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2018-12-31 | 15 | 5,473 | ▲ watchlist |
| 2019-03-31 | 7 | 5,428 | ▲ watchlist |
| 2019-06-30 | 5 | 5,369 | ▲ watchlist |
| 2019-09-30 | 6 | 5,325 | ▲ watchlist |
| 2019-12-31 | 5 | 5,244 | ▲ watchlist (first flag) |
| 2020-03-31 | 6 | 5,182 | ▲ watchlist |
| 2020-06-30 | 1 | 5,131 | ▲ watchlist |
| 2020-09-30 | 1 | 5,098 | ▲ watchlist |

## How its ratios moved

Most ratios were compared with the bank's own prior 12 quarters, and year-to-date ratios with the same quarter in the prior 3 years. Of 30 ratios compared, 16 sat outside their own prior range, and the table shows the 6 furthest outside. The bank ranked 1 of 5,098 in the 100.0th percentile, against the 99.9th percentile a year earlier, so the model rated it about the same as a year earlier.

Losses on bonds available for sale moved -32.2 pp in one quarter. That ratio reached -34.5% of equity, below its prior range of -2.5% to 1.4%, yet it contributed -0.250 log-odds units and pushed the score down. The efficiency ratio, operating costs as a share of revenue, rose +121.0 pp over four quarters. That ratio was 207.1%, far above its range of 52.6% to 86.1%, yet it contributed -0.036 and had little effect on the score. Cash was 9.9% of assets, above its range of 1.1% to 3.3%, yet it contributed +0.006 and had little effect on the score.

Net interest margin, the spread earned on lending and investing, was 2.4%, below its range of 4.0% to 5.3%, and contributed +0.119, which pushed the score up. Return on equity was -233.5%, below its range of -119.7% to 38.7%, and contributed +1.440, which pushed the score up. Loan-loss reserves were 10.5% of loans, above their range of 1.1% to 8.3%, and contributed +0.084, which pushed the score up.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| losses on bonds available for sale, as a share of equity | -34.5% | -2.5% to 1.4% | prior 12 quarters | -32.2 pp | -33.4 pp | -0.250 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 207.1% | 52.6% to 86.1% | same quarter, prior 3 years | n/a | +121.0 pp | -0.036 | little effect on the score |
| cash as a share of assets | 9.9% | 1.1% to 3.3% | prior 12 quarters | +8.7 pp | +8.1 pp | +0.006 | little effect on the score |
| net interest margin (the spread earned on lending and investing) | 2.4% | 4.0% to 5.3% | same quarter, prior 3 years | n/a | -1.6 pp | +0.119 | pushed the score up |
| return on equity (profit as a share of equity) | -233.5% | -119.7% to 38.7% | same quarter, prior 3 years | n/a | -113.8 pp | +1.440 | pushed the score up |
| loan-loss reserves as a share of loans | 10.5% | 1.1% to 8.3% | prior 12 quarters | +2.2 pp | +4.3 pp | +0.084 | pushed the score up |

16 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Almena State Bank failed on 2020-10-23. Canary first flagged it in Q4 2019, on 2019-12-31, a lead time of 4 quarters before the failure.

At that first flag, the top drivers pushing the score up were return on equity at -100.1%, the Texas ratio at 189.3%, the Tier 1 risk-based capital ratio at 5.9%, loans 90+ days past due or not accruing at 22.9%, and brokered deposits at 26.3% of deposits. Their contributions were +1.351, +0.934, +0.860, +0.751 and +0.269 respectively.

## What happened next

In hindsight, the bank failed on 2020-10-23, shortly after the as-of quarter. The last quarter it reported data was 2020-09-30, so no later ranks exist for it.

## Sources

- F1 · Bank name · n/a · Almena State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2020-09-30 · 2020-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KS · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2020-09-30 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2020-09-30 · 5,098 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2020-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2020-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2020-09-30 · 102 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2020-09-30 · 10.9% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2020-09-30 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2020-09-30 · 14.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2020-09-30 · 1.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2020-09-30 · 15.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2020-09-30 · 23.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2020-09-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2020-09-30 · 19.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2020-09-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2020-09-30 · 10.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2020-09-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2020-09-30 · 2.8% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2020-09-30 · 243.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2020-09-30 · 3.4% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2020-09-30 · -7.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2020-09-30 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2020-09-30 · -233.5% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2020-09-30 · 8.7% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2020-09-30 · 2.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2020-09-30 · 21.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2020-09-30 · 31.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2020-09-30 · -34.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2020-09-30 · -2.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2020-09-30 · -15.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2020-09-30 · 15.0% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 0.0%; contribution to the score · 2020-09-30 · +1.798 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -233.5%; contribution to the score · 2020-09-30 · +1.440 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 243.0%; contribution to the score · 2020-09-30 · +1.035 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 23.8%; contribution to the score · 2020-09-30 · +0.654 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 1.4%; contribution to the score · 2020-09-30 · +0.552 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: losses on bonds available for sale, as a share of equity, value -34.5%; contribution to the score · 2020-09-30 · -0.250 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F81 · Driver down #2: deposit growth over the past four quarters, value -15.7%; contribution to the score · 2020-09-30 · -0.140 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F82 · Driver down #3: construction loans as a share of loans, value 0.0%; contribution to the score · 2020-09-30 · -0.100 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: loans 30-89 days past due, as a share of assets, value 1.2%; contribution to the score · 2020-09-30 · -0.090 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F84 · Driver down #5: volatile funding as a share of assets, value 2.0%; contribution to the score · 2020-09-30 · -0.078 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F85 · Failure date · 2020-10-23 · 2020-10-23 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2019-12-31 · 2019-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2019-12-31: return on equity (profit as a share of equity), value -100.1%; contribution to the score · 2019-12-31 · +1.351 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2019-12-31: the Texas ratio (troubled assets against capital plus reserves), value 189.3%; contribution to the score · 2019-12-31 · +0.934 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2019-12-31: the Tier 1 risk-based capital ratio, value 5.9%; contribution to the score · 2019-12-31 · +0.860 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F91 · Driver up #4 at 2019-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 22.9%; contribution to the score · 2019-12-31 · +0.751 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2019-12-31: brokered deposits as a share of deposits, value 26.3%; contribution to the score · 2019-12-31 · +0.269 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F98 · Last quarter the bank reported · 2020-09-30 · 2020-09-30 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2020-09-30 · -34.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F100 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · -2.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F101 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F102 · Trend: losses on bonds available for sale, as a share of equity, change over one quarter, in percentage points · 2020-09-30 · -32.2 pp · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F104 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2020-09-30 · -0.250 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F105 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2020-09-30 · pushed the score down · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2020-09-30 · 207.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 52.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F108 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 86.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F109 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2020-09-30 · +121.0 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2020-09-30 · -0.036 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F111 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2020-09-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F112 · Trend: cash as a share of assets, value at the as-of quarter · 2020-09-30 · 9.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F113 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F114 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 3.3% · data/features/fct_bank_features.parquet: cash_to_assets
- F117 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2020-09-30 · +0.006 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F118 · Trend: cash as a share of assets, what the model did with it · 2020-09-30 · little effect on the score · data/analyst/scores.parquet: feature cash_to_assets contribution
- F119 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2020-09-30 · 2.4% · data/features/fct_bank_features.parquet: net_interest_margin
- F120 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 4.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F121 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 5.3% · data/features/fct_bank_features.parquet: net_interest_margin
- F123 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2020-09-30 · +0.119 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F124 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2020-09-30 · pushed the score up · data/analyst/scores.parquet: feature net_interest_margin contribution
- F125 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2020-09-30 · -233.5% · data/features/fct_bank_features.parquet: return_on_equity
- F126 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -119.7% · data/features/fct_bank_features.parquet: return_on_equity
- F127 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 38.7% · data/features/fct_bank_features.parquet: return_on_equity
- F129 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2020-09-30 · +1.440 · data/analyst/scores.parquet: feature return_on_equity contribution
- F130 · Trend: return on equity (profit as a share of equity), what the model did with it · 2020-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F131 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2020-09-30 · 10.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F132 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F133 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 8.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F136 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2020-09-30 · +0.084 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F137 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2020-09-30 · pushed the score up · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F138 · Trend: ratios outside their own prior range · 2020-09-30 · 16 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios shown in the table (the furthest outside their prior range) · 2020-09-30 · 6 · data/features/fct_bank_features.parquet
- F140 · Trend: ratios compared with their own prior range · 2020-09-30 · 30 · data/features/fct_bank_features.parquet
- F141 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F142 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F143 · Percentile a year earlier (100 = highest risk) · 2019-09-30 · 99.9% · data/analyst/scores.parquet: percentile
- F144 · Trend: how the model's rating compares with a year earlier · 2020-09-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
