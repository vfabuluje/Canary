---
cert: 27332
name: "Republic Bank"
as_of: 2023-12-31
rank: 135
n_banks: 4658
percentile: 97.12322885358523
flagged: false
outcome: "caught"
after_test_window: false
failure_date: 2024-04-26
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:50:19"
writer_model: "claude-opus-5-5"
checked: true
---

# Republic Bank (cert 27332)

*Hindsight: failed 2024-04-26. Canary flagged it 4 quarters ahead.*

## Summary

As of 2023-12-31, Republic Bank, a Pennsylvania bank, ranked 135 out of 4,658 FDIC-insured banks on Canary's risk score, placing it in the 97.1th percentile, where higher means riskier. It was not on Canary's watchlist, which covers the top 2% of banks, or 94 banks that quarter. The main concerns were very thin capital, with equity at 1.8% of assets against a national median of 9.5%, and a return on equity (profit as a share of the owners' stake) of -36.6%. It also carried large paper losses on the bonds it owned.

## Warning signs in the data

Capital, the cushion that absorbs losses, was far below typical levels: equity was 1.8% of assets against a national median of 9.5%, and the leverage ratio (core capital as a share of average assets) was 4.4% against a median of 10.6%. Its risk-based capital ratios, which weight assets by how risky they are, were also low, with Tier 1 at 8.8% versus a median of 14.1% and total capital at 9.6% versus 15.3%. Earnings were weak: return on assets was -0.7% against a median of 1.0%, the net interest margin (the spread earned on lending and investing) was 1.2% against 3.4%, and the efficiency ratio (operating costs as a share of revenue) was 145.3% against 66.5%.

Problem loans were modest but above typical levels, with loans 90+ days past due or not accruing interest at 0.7% of loans versus a median of 0.3%. The Texas ratio, which compares troubled assets with capital plus reserves, was 16.4% against a median of 1.8%, and commercial real estate loans made up 42.7% of loans against a median of 23.2%. On funding, uninsured deposits (balances above the government insurance limit) were 51.5% of deposits against a median of 23.9%, and borrowings from the Federal Home Loan Bank (a lender to banks) were 11.9% of assets against 1.0%. Deposit growth over the past four quarters was -12.8%, against a national median of 0.9%.

The largest strain was in its bond portfolio, which made up 40.5% of assets against a median of 20.1%. Unrealized losses on bonds held to maturity equaled 250.7% of equity, against a median of 0.0%, and losses on bonds available for sale equaled 155.9% of equity, against a median of 12.9%.

## Understanding the score

As of 2023-12-31, Republic Bank ranked 135 of 4,658 banks, in the 97.1th percentile on a scale from 0 to 100 where higher means riskier. It was not flagged on the watchlist, which that quarter held the top 2% of banks, or 94 banks.

The five factors that pushed its score up most were return on equity at -36.6%, losses on bonds available for sale at 155.9% of equity, equity at 1.8% of assets, the total risk-based capital ratio at 9.6%, and loans at 69.0% of deposits. The five factors that pulled its score down most were nonaccrual assets and foreclosed property at 0.4% of assets, loans 90+ days past due or not accruing at 0.7% of loans, the Texas ratio at 16.4%, loans 30-89 days past due at 0.2% of assets, and construction loans at 4.8% of loans. In short, the model saw weak profits, bond losses and thin capital as the risk, while relatively clean loan books held the score back.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2022-03-31 | 178 | 4,861 |  |
| 2022-06-30 | 159 | 4,838 |  |
| 2022-09-30 | 27 | 4,813 | ▲ watchlist |
| 2022-12-31 | 32 | 4,773 | ▲ watchlist |
| 2023-03-31 | 5 | 4,740 | ▲ watchlist |
| 2023-06-30 | 29 | 4,714 | ▲ watchlist (first flag) |
| 2023-09-30 | 65 | 4,686 | ▲ watchlist |
| 2023-12-31 | 135 | 4,658 |  |

## How its ratios moved

Most ratios are compared with the bank's own prior 12 quarters, and year-to-date ratios with the same quarter in the prior 3 years. Of 30 ratios checked, 13 sat outside their own prior range, and the table shows the 6 furthest outside.

Return on equity stood at -36.6%, far below its prior range of 2.8% to 9.1%, a change of -41.6 pp over four quarters, and with a contribution of +1.198 model log-odds units it pushed the score up. Annualized interest expense was 2.6% of assets, above its prior range of 0.3% to 0.5%, and with a contribution of +0.064 it pushed the score up. The efficiency ratio reached 145.3%, well above its prior range of 73.7% to 87.3%, yet its contribution of -0.198 pushed the score down. Return on assets was -0.7%, below its prior range of 0.2% to 0.5%, yet its contribution of -0.068 pushed the score down. Net interest margin was 1.2%, below its prior range of 2.4% to 2.7%, yet its contribution of +0.032 had little effect on the score. Uninsured deposits fell to 51.5% of deposits, below their prior range of 56.7% to 64.7%, and their contribution of -0.012 had little effect on the score.

The bank was in the 99.4th percentile a year earlier and ranked 135 of 4,658 at 2023-12-31, so the model rated it safer than a year earlier.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -36.6% | 2.8% to 9.1% | same quarter, prior 3 years | n/a | -41.6 pp | +1.198 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 145.3% | 73.7% to 87.3% | same quarter, prior 3 years | n/a | +69.7 pp | -0.198 | pushed the score down |
| annualized interest expense as a share of assets | 2.6% | 0.3% to 0.5% | same quarter, prior 3 years | n/a | +2.1 pp | +0.064 | pushed the score up |
| net interest margin (the spread earned on lending and investing) | 1.2% | 2.4% to 2.7% | same quarter, prior 3 years | n/a | -1.5 pp | +0.032 | little effect on the score |
| return on assets (profit as a share of assets) | -0.7% | 0.2% to 0.5% | same quarter, prior 3 years | n/a | -0.9 pp | -0.068 | pushed the score down |
| uninsured deposits as a share of deposits | 51.5% | 56.7% to 64.7% | prior 12 quarters | -5.2 pp | -12.4 pp | -0.012 | little effect on the score |

13 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Republic Bank failed on 2024-04-26. Under Canary's lead-time rule, the bank was first flagged in the quarter ending 2023-06-30, a lead time of 4 quarters before the failure.

At that first flag, the top factors pushing the score up were losses on bonds available for sale at 134.7% of equity, return on equity at -30.3%, and equity at 2.1% of assets. The total risk-based capital ratio at 9.9% and loans at 66.8% of deposits also added to the score then. The same pattern seen later, weak profits and bond losses against thin capital, was already driving the score at that point.

## What happened next

In hindsight, the bank's last regulatory report was for the quarter ending 2023-12-31, the same quarter this memo describes. Republic Bank failed on April 26, 2024, and stopped reporting after that point. Our data does not distinguish between a merger and a closure when a bank stops reporting, but here the failure date confirms the outcome.

## Sources

- F1 · Bank name · n/a · Republic Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2023-12-31 · 2023-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · PA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2023-12-31 · 135 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2023-12-31 · 4,658 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2023-12-31 · 97.1% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2023-12-31 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2023-12-31 · 94 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2023-12-31 · 1.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2023-12-31 · 9.5% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2023-12-31 · 4.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2023-12-31 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2023-12-31 · 8.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2023-12-31 · 14.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2023-12-31 · 9.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2023-12-31 · 15.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2023-12-31 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2023-12-31 · 0.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2023-12-31 · 42.7% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2023-12-31 · 23.2% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2023-12-31 · 16.4% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2023-12-31 · 1.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2023-12-31 · -0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2023-12-31 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2023-12-31 · -36.6% · data/features/fct_bank_features.parquet: return_on_equity
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2023-12-31 · 1.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2023-12-31 · 3.4% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2023-12-31 · 145.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2023-12-31 · 66.5% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2023-12-31 · 51.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2023-12-31 · 23.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2023-12-31 · 11.9% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2023-12-31 · 1.0% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2023-12-31 · 250.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2023-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2023-12-31 · 155.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2023-12-31 · 12.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2023-12-31 · 40.5% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2023-12-31 · 20.1% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2023-12-31 · -12.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2023-12-31 · 0.9% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -36.6%; contribution to the score · 2023-12-31 · +1.198 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 155.9%; contribution to the score · 2023-12-31 · +0.912 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: equity as a share of assets, value 1.8%; contribution to the score · 2023-12-31 · +0.367 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 9.6%; contribution to the score · 2023-12-31 · +0.089 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: loans as a share of deposits, value 69.0%; contribution to the score · 2023-12-31 · +0.087 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F80 · Driver down #1: nonaccrual assets and foreclosed property, as a share of assets, value 0.4%; contribution to the score · 2023-12-31 · -1.161 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F81 · Driver down #2: loans 90+ days past due or not accruing interest, as a share of loans, value 0.7%; contribution to the score · 2023-12-31 · -1.006 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 16.4%; contribution to the score · 2023-12-31 · -0.830 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: loans 30-89 days past due, as a share of assets, value 0.2%; contribution to the score · 2023-12-31 · -0.359 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F84 · Driver down #5: construction loans as a share of loans, value 4.8%; contribution to the score · 2023-12-31 · -0.260 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F85 · Failure date · 2024-04-26 · 2024-04-26 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2023-06-30 · 2023-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2023-06-30: losses on bonds available for sale, as a share of equity, value 134.7%; contribution to the score · 2023-06-30 · +1.306 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F89 · Driver up #2 at 2023-06-30: return on equity (profit as a share of equity), value -30.3%; contribution to the score · 2023-06-30 · +1.044 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2023-06-30: equity as a share of assets, value 2.1%; contribution to the score · 2023-06-30 · +0.233 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F91 · Driver up #4 at 2023-06-30: the total risk-based capital ratio, value 9.9%; contribution to the score · 2023-06-30 · +0.129 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F92 · Driver up #5 at 2023-06-30: loans as a share of deposits, value 66.8%; contribution to the score · 2023-06-30 · +0.084 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F98 · Last quarter the bank reported · 2023-12-31 · 2023-12-31 · data/features/fct_bank_features.parquet: report_date
- F103 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2023-12-31 · -36.6% · data/features/fct_bank_features.parquet: return_on_equity
- F104 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 2.8% · data/features/fct_bank_features.parquet: return_on_equity
- F105 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 9.1% · data/features/fct_bank_features.parquet: return_on_equity
- F106 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2023-12-31 · -41.6 pp · data/features/fct_bank_features.parquet: return_on_equity
- F107 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2023-12-31 · +1.198 · data/analyst/scores.parquet: feature return_on_equity contribution
- F108 · Trend: return on equity (profit as a share of equity), what the model did with it · 2023-12-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F109 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2023-12-31 · 145.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 73.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F111 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 87.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F113 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2023-12-31 · -0.198 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F114 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2023-12-31 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F115 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2023-12-31 · 2.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F116 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F117 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F119 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2023-12-31 · +0.064 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F120 · Trend: annualized interest expense as a share of assets, what the model did with it · 2023-12-31 · pushed the score up · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F121 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2023-12-31 · 1.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F122 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 2.4% · data/features/fct_bank_features.parquet: net_interest_margin
- F123 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 2.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F125 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2023-12-31 · +0.032 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F126 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2023-12-31 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F127 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2023-12-31 · -0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F128 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: return_on_assets
- F129 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: return_on_assets
- F131 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2023-12-31 · -0.068 · data/analyst/scores.parquet: feature return_on_assets contribution
- F132 · Trend: return on assets (profit as a share of assets), what the model did with it · 2023-12-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F133 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2023-12-31 · 51.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F134 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 56.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F135 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 64.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F138 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2023-12-31 · -0.012 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F139 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2023-12-31 · little effect on the score · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F140 · Trend: ratios outside their own prior range · 2023-12-31 · 13 · data/features/fct_bank_features.parquet
- F141 · Trend: ratios shown in the table (the furthest outside their prior range) · 2023-12-31 · 6 · data/features/fct_bank_features.parquet
- F142 · Trend: ratios compared with their own prior range · 2023-12-31 · 30 · data/features/fct_bank_features.parquet
- F143 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F144 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F145 · Percentile a year earlier (100 = highest risk) · 2022-12-31 · 99.4% · data/analyst/scores.parquet: percentile
- F146 · Trend: how the model's rating compares with a year earlier · 2023-12-31 · the model rated it safer than a year earlier · data/analyst/scores.parquet: percentile
