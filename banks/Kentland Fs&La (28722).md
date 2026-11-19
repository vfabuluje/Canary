---
cert: 28722
name: "Kentland Fs&La"
as_of: 2026-03-31
rank: 1
n_banks: 4353
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: true
failure_date: 2026-07-10
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:52:50"
writer_model: "claude-opus-5-5"
checked: true
---

# Kentland Fs&La (cert 28722)

*Hindsight: failed 2026-07-10. Canary flagged it 4 quarters ahead.*
*After the test window: not part of the reported 2016-2024 results.*

## Summary

As of 2026-03-31, Kentland Fs&La of IN, certificate number 28722, ranked 1 out of 4,353 banks on Canary's risk score, placing it in the 100.0th percentile, the riskiest end of the scale. It was flagged on Canary's watchlist, which covers the riskiest 2% of banks and held 88 banks that quarter. Its capital cushion was very thin, with equity at 1.8% of assets against a national median of 10.4%, and it was losing money, with return on assets of -4.8% against a median of 1.2%.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was far below typical levels: equity was 1.8% of assets against a national median of 10.4%, and the leverage ratio (core capital as a share of average assets) was 1.7% against 10.9%. The risk-based capital ratios, which weigh assets by riskiness, were also low, with a Tier 1 ratio of 2.9% against a median of 14.5% and a total ratio of 4.2% against 15.7%.

Credit quality was weak: loans 90 or more days past due or no longer accruing interest were 6.3% of loans against a median of 0.5%, and loans 30-89 days past due were 2.5% of assets against 0.3%. Nonaccrual assets and foreclosed property were 5.9% of assets against a median of 0.3%, and the Texas ratio, which sets troubled assets against capital plus reserves, stood at 217.8% against a median of 2.9%. Earnings were deeply negative, with return on equity of -201.1% against a median of 11.2%, and the efficiency ratio (operating costs as a share of revenue) was 305.0% against 63.1%.

Funding looked steadier: uninsured deposits were only 2.8% of deposits against a median of 24.4%, and core deposits, the stable everyday kind, were 88.7% of assets against 75.8%. Cash was 5.5% of assets, a bit below the median of 6.9%, and the bank showed no losses on bonds available for sale at 0.0% of equity against a median of 5.8%. It was a very small bank, with total assets of $3.7 million against a national median of $381.7 million.

## Understanding the score

As of 2026-03-31, the bank ranked 1 of 4,353 banks, which is the 100.0th percentile on a scale of 0 to 100 where higher means riskier. That placed it on the watchlist, the top 2% of banks by score, alongside 88 banks flagged that quarter.

The five features that pushed the score up most were the Tier 1 risk-based capital ratio at 2.9%, contributing +1.457, and return on equity at -201.1%, contributing +1.409. Next came the Texas ratio at 217.8%, contributing +0.921, the leverage ratio at 1.7%, contributing +0.562, and the total risk-based capital ratio at 4.2%, contributing +0.460.

The five features that pulled the score down were loan-loss reserves (money set aside for bad loans) at 1.0% of loans, contributing -0.143, and cash at 5.5% of assets, contributing -0.063. Smaller offsets came from brokered deposits at 0.0% of deposits, contributing -0.056, net loan write-offs at 0.0% of loans, contributing -0.049, and construction loans at 0.0% of loans, contributing -0.032.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-06-30 | 1 | 4,610 | ▲ watchlist |
| 2024-09-30 | 8 | 4,589 | ▲ watchlist |
| 2024-12-31 | 8 | 4,560 | ▲ watchlist |
| 2025-03-31 | 1 | 4,536 | ▲ watchlist |
| 2025-06-30 | 6 | 4,494 | ▲ watchlist |
| 2025-09-30 | 1 | 4,452 | ▲ watchlist (first flag) |
| 2025-12-31 | 1 | 4,411 | ▲ watchlist |
| 2026-03-31 | 1 | 4,353 | ▲ watchlist |

## How its ratios moved

Most ratios are compared with the bank's own prior 12 quarters, and year-to-date ratios with the same quarter in the prior 3 years. Of 27 ratios compared, 7 sat outside their own prior range, and the 6 furthest outside are shown in the table. The bank ranked 1 of 4,353 as of 2026-03-31, and its percentile a year earlier, at 2025-03-31, was 100.0%, so the model rated it about the same as a year earlier.

Return on equity was -201.1%, below its prior range of -82.3% to -8.0% after a change of -118.8 pp over four quarters, and its contribution of +1.409 model log-odds units pushed the score up. The Texas ratio was 217.8%, above its prior range of 0.0% to 154.9%, and its contribution of +0.921 pushed the score up. The leverage ratio was 1.7%, below its prior range of 3.0% to 12.9%, and its contribution of +0.562 pushed the score up. Equity as a share of assets was 1.8%, below its prior range of 2.9% to 12.9%, and its contribution of +0.251 pushed the score up.

Two ratios moved outside their range without adding to the score. Cash as a share of assets was 5.5%, below its prior range of 6.0% to 12.9%, yet its contribution of -0.063 pushed the score down. The provision for loan losses was 0.4% of assets, above its prior range of 0.0% to 0.0%, yet its contribution of -0.018 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -201.1% | -82.3% to -8.0% | same quarter, prior 3 years | n/a | -118.8 pp | +1.409 | pushed the score up |
| annualized provision for loan losses as a share of assets | 0.4% | 0.0% to 0.0% | same quarter, prior 3 years | n/a | +0.4 pp | -0.018 | little effect on the score |
| the Texas ratio (troubled assets against capital plus reserves) | 217.8% | 0.0% to 154.9% | prior 12 quarters | +62.9 pp | +135.6 pp | +0.921 | pushed the score up |
| the leverage ratio (core capital as a share of average assets) | 1.7% | 3.0% to 12.9% | prior 12 quarters | -1.4 pp | -5.8 pp | +0.562 | pushed the score up |
| equity as a share of assets | 1.8% | 2.9% to 12.9% | prior 12 quarters | -1.1 pp | -5.6 pp | +0.251 | pushed the score up |
| cash as a share of assets | 5.5% | 6.0% to 12.9% | prior 12 quarters | -6.8 pp | -7.2 pp | -0.063 | pushed the score down |

7 of 27 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Canary first flagged the bank in the quarter ending 2025-09-30, and the bank failed on 2026-07-10, a lead time of 4 quarters. This counts as a catch, with the failure falling after the model's test window.

At that first flag, the top drivers were return on equity at -154.3%, contributing +1.328, and the Texas ratio at 130.8%, contributing +0.806. They were followed by the Tier 1 risk-based capital ratio at 7.5%, contributing +0.573, seriously late loans at 7.6% of loans, contributing +0.396, and interest expense at 3.6% of assets, contributing +0.358.

*After the test window: not part of the reported 2016-2024 results.*

## What happened next

In hindsight, the last quarter the bank reported was 2026-03-31, the same quarter as this memo's as-of date. The bank failed on 2026-07-10, so no later ranks or flags exist for it in our data.

## Sources

- F1 · Bank name · n/a · Kentland Fs&La · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 28722 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IN · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-03-31 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-03-31 · 4,353 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-03-31 · 88 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-03-31 · 1.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-03-31 · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-03-31 · 1.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-03-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-03-31 · 2.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-03-31 · 14.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-03-31 · 4.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-03-31 · 15.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-03-31 · 6.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-03-31 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-03-31 · 5.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-03-31 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-03-31 · 2.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-03-31 · 217.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-03-31 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-03-31 · -4.8% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-03-31 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-03-31 · -201.1% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-03-31 · 11.2% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-03-31 · 305.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-03-31 · 63.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-03-31 · 2.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-03-31 · 24.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-03-31 · 88.7% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-03-31 · 75.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-03-31 · 5.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-03-31 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-03-31 · 5.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-03-31 · $3.7 million · data/features/fct_bank_features.parquet: log_total_assets
- F70 · National median: total assets · 2026-03-31 · $381.7 million · data/features/fct_bank_features.parquet: log_total_assets (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 2.9%; contribution to the score · 2026-03-31 · +1.457 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -201.1%; contribution to the score · 2026-03-31 · +1.409 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 217.8%; contribution to the score · 2026-03-31 · +0.921 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value 1.7%; contribution to the score · 2026-03-31 · +0.562 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 4.2%; contribution to the score · 2026-03-31 · +0.460 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: loan-loss reserves as a share of loans, value 1.0%; contribution to the score · 2026-03-31 · -0.143 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F81 · Driver down #2: cash as a share of assets, value 5.5%; contribution to the score · 2026-03-31 · -0.063 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F82 · Driver down #3: brokered deposits as a share of deposits, value 0.0%; contribution to the score · 2026-03-31 · -0.056 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F83 · Driver down #4: annualized loan write-offs, net of recoveries, as a share of loans, value 0.0%; contribution to the score · 2026-03-31 · -0.049 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F84 · Driver down #5: construction loans as a share of loans, value 0.0%; contribution to the score · 2026-03-31 · -0.032 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F85 · Failure date · 2026-07-10 · 2026-07-10 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2025-09-30 · 2025-09-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2025-09-30: return on equity (profit as a share of equity), value -154.3%; contribution to the score · 2025-09-30 · +1.328 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2025-09-30: the Texas ratio (troubled assets against capital plus reserves), value 130.8%; contribution to the score · 2025-09-30 · +0.806 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2025-09-30: the Tier 1 risk-based capital ratio, value 7.5%; contribution to the score · 2025-09-30 · +0.573 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F91 · Driver up #4 at 2025-09-30: loans 90+ days past due or not accruing interest, as a share of loans, value 7.6%; contribution to the score · 2025-09-30 · +0.396 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2025-09-30: annualized interest expense as a share of assets, value 3.6%; contribution to the score · 2025-09-30 · +0.358 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F98 · Last quarter the bank reported · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-03-31 · -201.1% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -82.3% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -8.0% · data/features/fct_bank_features.parquet: return_on_equity
- F102 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2026-03-31 · -118.8 pp · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-03-31 · +1.409 · data/analyst/scores.parquet: feature return_on_equity contribution
- F104 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F105 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-03-31 · 0.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F106 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F107 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F109 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-03-31 · -0.018 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F110 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-03-31 · little effect on the score · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F111 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-03-31 · 217.8% · data/features/fct_bank_features.parquet: texas_ratio
- F112 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: texas_ratio
- F113 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 154.9% · data/features/fct_bank_features.parquet: texas_ratio
- F116 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-03-31 · +0.921 · data/analyst/scores.parquet: feature texas_ratio contribution
- F117 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F118 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-03-31 · 1.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F119 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 3.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F120 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 12.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F123 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-03-31 · +0.562 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F124 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F125 · Trend: equity as a share of assets, value at the as-of quarter · 2026-03-31 · 1.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F126 · Trend: equity as a share of assets, lowest value in the comparison window · n/a · 2.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F127 · Trend: equity as a share of assets, highest value in the comparison window · n/a · 12.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F130 · Trend: equity as a share of assets, contribution to the score (model log-odds units) · 2026-03-31 · +0.251 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F131 · Trend: equity as a share of assets, what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature equity_to_assets contribution
- F132 · Trend: cash as a share of assets, value at the as-of quarter · 2026-03-31 · 5.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F133 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 6.0% · data/features/fct_bank_features.parquet: cash_to_assets
- F134 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 12.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F137 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2026-03-31 · -0.063 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F138 · Trend: cash as a share of assets, what the model did with it · 2026-03-31 · pushed the score down · data/analyst/scores.parquet: feature cash_to_assets contribution
- F139 · Trend: ratios outside their own prior range · 2026-03-31 · 7 · data/features/fct_bank_features.parquet
- F140 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-03-31 · 6 · data/features/fct_bank_features.parquet
- F141 · Trend: ratios compared with their own prior range · 2026-03-31 · 27 · data/features/fct_bank_features.parquet
- F142 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F143 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F144 · Percentile a year earlier (100 = highest risk) · 2025-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F145 · Trend: how the model's rating compares with a year earlier · 2026-03-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
