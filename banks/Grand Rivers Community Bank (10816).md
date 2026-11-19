---
cert: 10816
name: "Grand Rivers Community Bank"
as_of: 2026-06-30
rank: 12
n_banks: 4313
percentile: 99.74495710642243
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:55:04"
writer_model: "claude-opus-5-5"
checked: true
---

# Grand Rivers Community Bank (cert 10816)

*Outcome not yet known.*

## Summary

As of June 30, 2026, Grand Rivers Community Bank, an Illinois bank, ranked 12 out of 4,313 banks on Canary's risk score, placing it in the 99.7th percentile (higher means riskier) and on the watchlist. Its main problem is troubled loans: 19.0% of its loans were 90+ days past due or no longer collecting interest, against a national median of 0.5%. It was also losing money, with a return on assets (profit as a share of assets) of -3.4% versus a national median of 1.2%, and it is very small, with total assets of $15.1 million.

## Warning signs in the data

Credit quality is the clearest weak spot: loans 90+ days past due or not accruing interest were 19.0% of loans, far above the national median of 0.5%. Nonaccrual assets and foreclosed property were 12.6% of assets against a median of 0.3%, and loans 30-89 days past due were 6.4% of assets against a median of 0.2%. The Texas ratio, which weighs troubled assets against the capital and reserves available to absorb them, stood at 113.1% versus a national median of 2.9%. The bank has set aside loan-loss reserves (money held back for expected loan losses) of 5.0% of loans, well above the median of 1.2%.

Capital, the bank's own cushion against losses, is thinner than at most banks: equity was 8.6% of assets versus a median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.4% versus 11.0%. Its Tier 1 risk-based capital ratio was 10.7% against a median of 14.6%, and its total risk-based capital ratio was 12.0% against 15.8%. Earnings were deeply negative, with return on equity at -38.7% versus a median of 11.6%, and the efficiency ratio (operating costs as a share of revenue) at 169.4% versus 62.1%.

Funding looks steadier: core deposits, the stable everyday deposits, were 89.2% of assets versus a median of 75.5%, cash was 13.8% of assets versus 6.2%, and volatile funding was 0.0% versus 9.0%. Uninsured deposits were 21.6% of deposits, a bit below the median of 24.8%, but the bank was shrinking, with asset growth of -14.0% and deposit growth of -13.6% over the past four quarters, against medians of 4.5% and 4.2%. Paper losses on bonds available for sale were small at 0.1% of equity, well below the national median of 5.6%.

## Understanding the score

On June 30, 2026, the bank ranked 12 out of 4,313 banks, which puts it in the 99.7th percentile on a scale where higher means riskier; its raw model score was 0.5394. It was flagged on the watchlist, which covers the riskiest 2% of banks, or 87 banks that quarter.

Five features pushed the score up the most: troubled loans 90+ days past due or not accruing at 19.0% of loans (+1.079), return on equity at -38.7% (+0.701), the Texas ratio at 113.1% (+0.672), loans 30-89 days past due at 6.4% of assets (+0.550), and the bank's small size of $15.1 million in assets (+0.459). Five features pulled the score down the most: the Tier 1 risk-based capital ratio at 10.7% (-1.502), low interest expense at 1.0% of assets (-0.902), the total risk-based capital ratio at 12.0% (-0.318), commercial real estate loans at 42.0% of loans (-0.240), and construction loans at 0.0% of loans (-0.198).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 7 | 4,589 | ▲ watchlist |
| 2024-12-31 | 207 | 4,560 |  |
| 2025-03-31 | 17 | 4,536 | ▲ watchlist |
| 2025-06-30 | 14 | 4,494 | ▲ watchlist |
| 2025-09-30 | 13 | 4,452 | ▲ watchlist |
| 2025-12-31 | 12 | 4,411 | ▲ watchlist |
| 2026-03-31 | 17 | 4,353 | ▲ watchlist |
| 2026-06-30 | 12 | 4,313 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own history over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years; 8 of 30 ratios sat outside their prior range, and the table shows the 6 furthest out. The model rated the bank about the same as a year earlier: it was in the 99.7th percentile on June 30, 2025, and the 99.7th percentile again at rank 12 on June 30, 2026.

Return on equity fell to -38.7%, below its prior range of -28.3% to -9.1%, and contributed +0.701 model log-odds units, which pushed the score up. That was a drop of -17.5 pp in return on equity over four quarters. Return on assets was -3.4%, below its prior range of -2.4% to -0.9%, and it contributed +0.080 model log-odds units, which pushed the score up. Loan-loss reserves rose to 5.0% of loans, just above the prior range of 2.7% to 4.9%, and contributed +0.073 model log-odds units, which pushed the score up.

The efficiency ratio climbed to 169.4%, above its prior range of 112.8% to 154.1%, yet at -0.033 model log-odds units it had little effect on the score. Net interest margin slipped to 4.4%, just under its prior range of 4.5% to 4.8%, but its contribution of -0.117 model log-odds units pushed the score down. Losses on bonds available for sale dropped to 0.1% of equity, below the prior range of 0.2% to 1.0%, and at +0.010 model log-odds units had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on assets (profit as a share of assets) | -3.4% | -2.4% to -0.9% | same quarter, prior 3 years | n/a | -1.4 pp | +0.080 | pushed the score up |
| return on equity (profit as a share of equity) | -38.7% | -28.3% to -9.1% | same quarter, prior 3 years | n/a | -17.5 pp | +0.701 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 169.4% | 112.8% to 154.1% | same quarter, prior 3 years | n/a | +15.3 pp | -0.033 | little effect on the score |
| losses on bonds available for sale, as a share of equity | 0.1% | 0.2% to 1.0% | prior 12 quarters | -0.1 pp | -0.4 pp | +0.010 | little effect on the score |
| net interest margin (the spread earned on lending and investing) | 4.4% | 4.5% to 4.8% | same quarter, prior 3 years | n/a | -0.1 pp | -0.117 | pushed the score down |
| loan-loss reserves as a share of loans | 5.0% | 2.7% to 4.9% | prior 12 quarters | +0.1 pp | +0.4 pp | +0.073 | pushed the score up |

8 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

With hindsight, Canary classes this bank as an open watchlist case: it was flagged as among the highest-risk banks and remains a bank to keep watching rather than a closed case. The fact sheet contains no hindsight data for this bank, so we cannot add any later figures that explain the outcome beyond the conditions described in the earlier sections.

## What happened next

Looking ahead with hindsight, our data for this memo holds no later ranks, watchlist flags or reporting status for the bank. We therefore cannot say how its rank moved after the as-of quarter or whether it kept filing reports, and the score history table added below is the place to check for later quarters.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F5 · Model score · 2026-06-30 · 0.5394 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 12 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 10.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 12.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 19.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 12.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 6.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 5.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 113.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -38.7% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 169.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 21.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 89.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 13.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $15.1 million · data/features/fct_bank_features.parquet: log_total_assets
- F71 · Bank: asset growth over the past four quarters · 2026-06-30 · -14.0% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -13.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 19.0%; contribution to the score · 2026-06-30 · +1.079 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -38.7%; contribution to the score · 2026-06-30 · +0.701 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 113.1%; contribution to the score · 2026-06-30 · +0.672 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 30-89 days past due, as a share of assets, value 6.4%; contribution to the score · 2026-06-30 · +0.550 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F79 · Driver up #5: total assets, value $15.1 million; contribution to the score · 2026-06-30 · +0.459 · data/analyst/scores.parquet: feature log_total_assets contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 10.7%; contribution to the score · 2026-06-30 · -1.502 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 1.0%; contribution to the score · 2026-06-30 · -0.902 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: the total risk-based capital ratio, value 12.0%; contribution to the score · 2026-06-30 · -0.318 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F83 · Driver down #4: commercial real estate loans as a share of loans, value 42.0%; contribution to the score · 2026-06-30 · -0.240 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F84 · Driver down #5: construction loans as a share of loans, value 0.0%; contribution to the score · 2026-06-30 · -0.198 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F85 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F86 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -2.4% · data/features/fct_bank_features.parquet: return_on_assets
- F87 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F89 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.080 · data/analyst/scores.parquet: feature return_on_assets contribution
- F90 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F91 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -38.7% · data/features/fct_bank_features.parquet: return_on_equity
- F92 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -28.3% · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -9.1% · data/features/fct_bank_features.parquet: return_on_equity
- F94 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2026-06-30 · -17.5 pp · data/features/fct_bank_features.parquet: return_on_equity
- F95 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · +0.701 · data/analyst/scores.parquet: feature return_on_equity contribution
- F96 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 169.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 112.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 154.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.033 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F102 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F103 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F104 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F105 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F108 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2026-06-30 · +0.010 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F109 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F110 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 4.4% · data/features/fct_bank_features.parquet: net_interest_margin
- F111 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 4.5% · data/features/fct_bank_features.parquet: net_interest_margin
- F112 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 4.8% · data/features/fct_bank_features.parquet: net_interest_margin
- F114 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.117 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F115 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F116 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2026-06-30 · 5.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F117 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 2.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F118 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 4.9% · data/features/fct_bank_features.parquet: allowance_to_loans
- F121 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.073 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F122 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F123 · Trend: ratios outside their own prior range · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F124 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F125 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F126 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F127 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F128 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F129 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
