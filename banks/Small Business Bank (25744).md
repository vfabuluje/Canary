---
cert: 25744
name: "Small Business Bank"
as_of: 2026-03-31
rank: 10
n_banks: 4353
percentile: 99.79324603721571
flagged: true
outcome: "caught"
after_test_window: true
failure_date: 2026-07-17
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:52:49"
writer_model: "claude-opus-5-5"
checked: true
---

# Small Business Bank (cert 25744)

*Hindsight: failed 2026-07-17. Canary flagged it 4 quarters ahead.*
*After the test window: not part of the reported 2016-2024 results.*

## Summary

As of 2026-03-31, Small Business Bank, a Kansas bank, ranked 10 out of 4,353 banks on Canary's risk score, placing it in the 99.8th percentile, where higher means riskier. That put it on Canary's watchlist, the riskiest 2% of banks. The bank is small, with $72.9 million in assets, and its equity (its own capital cushion) was 4.9% of assets against a national median of 10.4%. It was also losing money, with a return on assets (profit as a share of assets) of -4.3% versus a national median of 1.2%.

## Warning signs in the data

Capital was thin by one measure: equity was 4.9% of assets against a national median of 10.4%, and the leverage ratio (core capital as a share of average assets) was 4.8% against a median of 10.9%. Risk-weighted capital looked closer to normal, with a Tier 1 risk-based capital ratio of 14.0% versus a median of 14.5%. The bank was also deeply unprofitable, with a return on equity of -79.5% against a median of 11.2%, and an efficiency ratio (operating costs as a share of revenue) of 249.0% against a median of 63.1%.

Credit quality stood out most: seriously overdue loans, or loans no longer accruing interest, were 4.8% of loans, far above the national median of 0.5%. Loans in the early stage of being past due were 9.4% of assets, against a median of 0.3%. The Texas ratio, which weighs troubled assets against capital plus reserves, was 55.5% versus a median of 2.9%, and loan-loss reserves (money set aside for bad loans) were 2.9% of loans versus a median of 1.2%.

Funding looked steadier: core deposits (stable, everyday deposits) were 94.3% of assets against a median of 75.8%, and uninsured deposits were 9.9% of deposits, well below the median of 24.4%. Cash was 13.2% of assets versus a median of 6.9%, and with securities at 0.0% of assets the bank showed 0.0% in losses on bonds available for sale, against a median of 5.8%. The bank was shrinking, with asset growth of -14.3% over the past four quarters while the national median was 4.3%.

## Understanding the score

As of 2026-03-31, the bank ranked 10 out of 4,353 banks, in the 99.8th percentile on a 0 to 100 scale where higher means riskier. It was flagged on the watchlist, which holds the riskiest 2% of banks, 88 banks that quarter.

The five factors pushing the score up most were a return on equity of -79.5%, adding +1.253; core deposits at 94.3% of assets, adding +0.516; and a Texas ratio of 55.5%, adding +0.505. Next came interest expense at 2.4% of assets, adding +0.351, and a return on assets of -4.3%, adding +0.306.

The five factors pulling the score down most were a Tier 1 risk-based capital ratio of 14.0%, at -1.507; construction loans at 2.7% of loans, at -0.283; and a total risk-based capital ratio of 15.3%, at -0.273. Uninsured deposits at 9.9% of deposits contributed -0.192, and commercial real estate loans at 28.0% of loans contributed -0.125.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-06-30 | 441 | 4,610 |  |
| 2024-09-30 | 799 | 4,589 |  |
| 2024-12-31 | 374 | 4,560 |  |
| 2025-03-31 | 106 | 4,536 |  |
| 2025-06-30 | 440 | 4,494 |  |
| 2025-09-30 | 65 | 4,452 | ▲ watchlist (first flag) |
| 2025-12-31 | 8 | 4,411 | ▲ watchlist |
| 2026-03-31 | 10 | 4,353 | ▲ watchlist |

## How its ratios moved

Canary compares each ratio with the bank's own history, usually the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios. As of 2026-03-31, 9 of 28 ratios checked sat outside their own prior range, and the 6 furthest outside are shown in the table. The bank ranked 10 out of 4,353, in the 99.8th percentile, up from the 97.7th percentile a year earlier, so the model rated it riskier than a year earlier.

Loans in the early stage of being past due reached 9.4% of assets, above a prior range of 0.0% to 6.2%, and contributed +0.273 model log-odds units, which pushed the score up. That share rose +3.2 pp in one quarter and +8.5 pp over four quarters. The Texas ratio stood at 55.5%, above its prior range of 4.3% to 49.7%, and contributed +0.505, which pushed the score up. Loan-loss reserves were 2.9% of loans, above a prior range of 0.6% to 2.7%, and contributed +0.077, which pushed the score up.

Equity fell to 4.9% of assets, below its prior range of 5.9% to 10.7%, down -5.2 pp over four quarters, and contributed +0.104, which pushed the score up. The leverage ratio dropped to 4.8%, below its prior range of 5.7% to 10.1%, and contributed +0.105, which pushed the score up. Core deposits rose to 94.3% of assets, above a prior range of 88.6% to 93.3%, and contributed +0.516, which pushed the score up.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| loans 30-89 days past due, as a share of assets | 9.4% | 0.0% to 6.2% | prior 12 quarters | +3.2 pp | +8.5 pp | +0.273 | pushed the score up |
| equity as a share of assets | 4.9% | 5.9% to 10.7% | prior 12 quarters | -1.1 pp | -5.2 pp | +0.104 | pushed the score up |
| core deposits as a share of assets | 94.3% | 88.6% to 93.3% | prior 12 quarters | +1.0 pp | +5.4 pp | +0.516 | pushed the score up |
| the leverage ratio (core capital as a share of average assets) | 4.8% | 5.7% to 10.1% | prior 12 quarters | -0.9 pp | -3.5 pp | +0.105 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 55.5% | 4.3% to 49.7% | prior 12 quarters | +5.8 pp | +40.7 pp | +0.505 | pushed the score up |
| loan-loss reserves as a share of loans | 2.9% | 0.6% to 2.7% | prior 12 quarters | +0.2 pp | +1.2 pp | +0.077 | pushed the score up |

9 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Canary first flagged the bank in the quarter ending 2025-09-30, and the bank failed on 2026-07-17, a lead time of 4 quarters. At that first flag, the biggest factor pushing the score up was a return on equity of -66.8%, adding +1.081. Interest expense at 2.5% of assets added +0.347 and loan-loss provisions at 2.5% of assets added +0.319. A strong Tier 1 risk-based capital ratio of 21.6% pulled the score down by -1.700 at that time.

*After the test window: not part of the reported 2016-2024 results.*

## What happened next

In hindsight, the bank's last quarterly report was for 2026-03-31, and it failed on 2026-07-17. After that the bank stopped reporting, which in our data covers both mergers and closures without telling them apart.

## Sources

- F1 · Bank name · n/a · Small Business Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KS · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-03-31 · 10 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-03-31 · 4,353 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-03-31 · 99.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-03-31 · 88 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-03-31 · 4.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-03-31 · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-03-31 · 4.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-03-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-03-31 · 14.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-03-31 · 14.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-03-31 · 4.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-03-31 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-03-31 · 9.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-03-31 · 2.9% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-03-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-03-31 · 55.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-03-31 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-03-31 · -4.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-03-31 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-03-31 · -79.5% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-03-31 · 11.2% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-03-31 · 249.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-03-31 · 63.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-03-31 · 9.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-03-31 · 24.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-03-31 · 94.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-03-31 · 75.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-03-31 · 13.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-03-31 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-03-31 · 5.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2026-03-31 · 0.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F69 · Bank: total assets · 2026-03-31 · $72.9 million · data/features/fct_bank_features.parquet: log_total_assets
- F71 · Bank: asset growth over the past four quarters · 2026-03-31 · -14.3% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2026-03-31 · 4.3% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -79.5%; contribution to the score · 2026-03-31 · +1.253 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: core deposits as a share of assets, value 94.3%; contribution to the score · 2026-03-31 · +0.516 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 55.5%; contribution to the score · 2026-03-31 · +0.505 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2026-03-31 · +0.351 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F79 · Driver up #5: return on assets (profit as a share of assets), value -4.3%; contribution to the score · 2026-03-31 · +0.306 · data/analyst/scores.parquet: feature return_on_assets contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 14.0%; contribution to the score · 2026-03-31 · -1.507 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: construction loans as a share of loans, value 2.7%; contribution to the score · 2026-03-31 · -0.283 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: the total risk-based capital ratio, value 15.3%; contribution to the score · 2026-03-31 · -0.273 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F83 · Driver down #4: uninsured deposits as a share of deposits, value 9.9%; contribution to the score · 2026-03-31 · -0.192 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F84 · Driver down #5: commercial real estate loans as a share of loans, value 28.0%; contribution to the score · 2026-03-31 · -0.125 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F85 · Failure date · 2026-07-17 · 2026-07-17 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2025-09-30 · 2025-09-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2025-09-30: return on equity (profit as a share of equity), value -66.8%; contribution to the score · 2025-09-30 · +1.081 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2025-09-30: annualized interest expense as a share of assets, value 2.5%; contribution to the score · 2025-09-30 · +0.347 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F90 · Driver up #3 at 2025-09-30: annualized provision for loan losses as a share of assets, value 2.5%; contribution to the score · 2025-09-30 · +0.319 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F93 · Driver down #1 at 2025-09-30: the Tier 1 risk-based capital ratio, value 21.6%; contribution to the score · 2025-09-30 · -1.700 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
- F103 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2026-03-31 · 9.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F104 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F105 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 6.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F106 · Trend: loans 30-89 days past due, as a share of assets, change over one quarter, in percentage points · 2026-03-31 · +3.2 pp · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F107 · Trend: loans 30-89 days past due, as a share of assets, change over four quarters, in percentage points · 2026-03-31 · +8.5 pp · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F108 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2026-03-31 · +0.273 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F109 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F110 · Trend: equity as a share of assets, value at the as-of quarter · 2026-03-31 · 4.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F111 · Trend: equity as a share of assets, lowest value in the comparison window · n/a · 5.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F112 · Trend: equity as a share of assets, highest value in the comparison window · n/a · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F114 · Trend: equity as a share of assets, change over four quarters, in percentage points · 2026-03-31 · -5.2 pp · data/features/fct_bank_features.parquet: equity_to_assets
- F115 · Trend: equity as a share of assets, contribution to the score (model log-odds units) · 2026-03-31 · +0.104 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F116 · Trend: equity as a share of assets, what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature equity_to_assets contribution
- F117 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-03-31 · 94.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F118 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 88.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F119 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 93.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F122 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-03-31 · +0.516 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F123 · Trend: core deposits as a share of assets, what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F124 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-03-31 · 4.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F125 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 5.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F126 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 10.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F129 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-03-31 · +0.105 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F130 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F131 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-03-31 · 55.5% · data/features/fct_bank_features.parquet: texas_ratio
- F132 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 4.3% · data/features/fct_bank_features.parquet: texas_ratio
- F133 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 49.7% · data/features/fct_bank_features.parquet: texas_ratio
- F136 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-03-31 · +0.505 · data/analyst/scores.parquet: feature texas_ratio contribution
- F137 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F138 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2026-03-31 · 2.9% · data/features/fct_bank_features.parquet: allowance_to_loans
- F139 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 0.6% · data/features/fct_bank_features.parquet: allowance_to_loans
- F140 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 2.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F143 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2026-03-31 · +0.077 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F144 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F145 · Trend: ratios outside their own prior range · 2026-03-31 · 9 · data/features/fct_bank_features.parquet
- F146 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-03-31 · 6 · data/features/fct_bank_features.parquet
- F147 · Trend: ratios compared with their own prior range · 2026-03-31 · 28 · data/features/fct_bank_features.parquet
- F148 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F149 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F150 · Percentile a year earlier (100 = highest risk) · 2025-03-31 · 97.7% · data/analyst/scores.parquet: percentile
- F151 · Trend: how the model's rating compares with a year earlier · 2026-03-31 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
