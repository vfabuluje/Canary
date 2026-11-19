---
cert: 29332
name: "First Southern Bank"
as_of: 2026-06-30
rank: 8
n_banks: 4313
percentile: 99.83769997681429
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:54:18"
writer_model: "claude-opus-5-5"
checked: true
---

# First Southern Bank (cert 29332)

*Outcome not yet known.*

## Summary

As of 2026-06-30, First Southern Bank, an Alabama bank (state AL), ranked 8 out of 4,313 FDIC-insured banks on Canary's risk score, placing it in the 99.8th percentile, where higher means riskier. That ranking put the bank on Canary's watchlist, which covers roughly the top 2% of banks. The main reasons are weak loan quality, with 10.9% of loans seriously overdue or not paying interest against a national median of 0.5%, and losses, with return on assets of -2.5% against a median of 1.2%.

## Warning signs in the data

Capital, the cushion that absorbs losses, is thinner than at a typical bank: equity was 8.8% of assets against a national median of 10.6%. The leverage ratio, core capital as a share of average assets, was 8.9% against a median of 11.0%.

Credit quality is the clearest problem: loans 90 or more days past due or not accruing interest were 10.9% of loans, far above the national median of 0.5%. Nonaccrual assets and foreclosed property were 7.4% of assets against a median of 0.3%, and loans that were late but not yet seriously overdue were 1.7% of assets against 0.2%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 70.5% against a median of 2.9%. Net loan write-offs, loans written off as lost minus recoveries, ran at an annualized 4.7% of loans against a median of 0.0%, and the bank posted a return on assets of -2.5% against a median of 1.2%.

On funding, uninsured deposits, balances above the government insurance limit, were 52.8% of deposits, well above the median of 24.8%, and Federal Home Loan Bank borrowings were 5.9% of assets against 0.2%. Offsetting this, cash was 13.4% of assets against a median of 6.2%, and unrealized losses on bonds available for sale were 1.5% of equity, below the median of 5.6%.

## Understanding the score

First Southern Bank ranked 8 of 4,313 banks as of 2026-06-30, in the 99.8th percentile on a scale of 0 to 100 where higher means riskier. It was flagged for the watchlist, one of 87 banks on it that quarter, a list that holds about 2% of banks.

The five factors that pushed the score up most were seriously overdue or nonaccruing loans at 10.9% of loans, the Texas ratio at 70.5%, loan-loss provisions (money set aside for expected losses) at an annualized 4.5% of assets, return on equity at -27.8%, and interest expense at an annualized 2.3% of assets. Their contributions to the score were +1.076, +0.904, +0.316, +0.198 and +0.127 respectively.

The five factors that pulled the score down most were the Tier 1 risk-based capital ratio, a measure of core capital against risk-weighted assets whose value is not shown, construction loans at 6.4% of loans, brokered deposits at 0.0% of deposits, total assets of $679.2 million, and deposit growth of 6.4%. Their contributions were -1.071, -0.362, -0.163, -0.163 and -0.125 respectively.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,089 | 4,589 |  |
| 2024-12-31 | 1,068 | 4,560 |  |
| 2025-03-31 | 29 | 4,536 | ▲ watchlist |
| 2025-06-30 | 50 | 4,494 | ▲ watchlist |
| 2025-09-30 | 35 | 4,452 | ▲ watchlist |
| 2025-12-31 | 105 | 4,411 |  |
| 2026-03-31 | 7 | 4,353 | ▲ watchlist |
| 2026-06-30 | 8 | 4,313 | ▲ watchlist |

## How its ratios moved

Canary compares each ratio with the bank's own history, usually the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 28 ratios compared, 17 were outside their own prior range, and the table shows the 6 furthest outside.

Loan-loss provisions reached 4.5% of assets, above a prior range of 0.2% to 1.3% and up +3.3 pp over four quarters; their contribution of +0.316 pushed the score up. Return on assets fell to -2.5%, below a prior range of 0.1% to 1.3%; its contribution of +0.081 pushed the score up. Return on equity fell to -27.8%, below a prior range of 0.5% to 14.8% and down -28.3 pp over four quarters; its contribution of +0.198 pushed the score up. Loan-loss reserves rose to 2.7% of loans, above a prior range of 1.1% to 1.9%; their contribution of +0.086 pushed the score up.

Net loan write-offs reached 4.7% of loans, well above a prior range of 0.2% to 2.1%, yet their contribution of +0.001 had little effect on the score. Core deposits, stable everyday deposits, rose to 79.6% of assets, above a prior range of 70.4% to 75.8%, but this contribution of -0.064 pushed the score down rather than up. Overall, the bank sat in the 99.8th percentile at rank 8, against the 98.9th percentile a year earlier on 2025-06-30, so the model rated it about the same as a year earlier.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | 4.5% | 0.2% to 1.3% | same quarter, prior 3 years | n/a | +3.3 pp | +0.316 | pushed the score up |
| return on assets (profit as a share of assets) | -2.5% | 0.1% to 1.3% | same quarter, prior 3 years | n/a | -2.6 pp | +0.081 | pushed the score up |
| return on equity (profit as a share of equity) | -27.8% | 0.5% to 14.8% | same quarter, prior 3 years | n/a | -28.3 pp | +0.198 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 4.7% | 0.2% to 2.1% | same quarter, prior 3 years | n/a | +2.7 pp | +0.001 | little effect on the score |
| loan-loss reserves as a share of loans | 2.7% | 1.1% to 1.9% | prior 12 quarters | +0.8 pp | +1.6 pp | +0.086 | pushed the score up |
| core deposits as a share of assets | 79.6% | 70.4% to 75.8% | prior 12 quarters | +4.3 pp | +7.3 pp | -0.064 | pushed the score down |

17 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

Hindsight: this bank's case is that it remains open and on the watchlist, but the fact sheet for this memo contains no hindsight data from after the as-of quarter. Its watchlist status therefore rests only on the as-of figures described above, chiefly weak loan quality and losses, and no later results can be reported here.

## What happened next

Hindsight: the fact sheet includes no later ranks, watchlist flags or reporting status for this bank after the as-of quarter. We therefore cannot say from this data how its ranking moved afterward or whether it continued to file reports.

## Sources

- F1 · Bank name · n/a · First Southern Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · AL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 8 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 10.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 7.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F25 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 4.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F26 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 70.5% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -2.5% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 52.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 5.9% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 13.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 10.9%; contribution to the score · 2026-06-30 · +1.076 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F72 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 70.5%; contribution to the score · 2026-06-30 · +0.904 · data/analyst/scores.parquet: feature texas_ratio contribution
- F73 · Driver up #3: annualized provision for loan losses as a share of assets, value 4.5%; contribution to the score · 2026-06-30 · +0.316 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F74 · Driver up #4: return on equity (profit as a share of equity), value -27.8%; contribution to the score · 2026-06-30 · +0.198 · data/analyst/scores.parquet: feature return_on_equity contribution
- F75 · Driver up #5: annualized interest expense as a share of assets, value 2.3%; contribution to the score · 2026-06-30 · +0.127 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -1.071 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: construction loans as a share of loans, value 6.4%; contribution to the score · 2026-06-30 · -0.362 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F78 · Driver down #3: brokered deposits as a share of deposits, value 0.0%; contribution to the score · 2026-06-30 · -0.163 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F79 · Driver down #4: total assets, value $679.2 million; contribution to the score · 2026-06-30 · -0.163 · data/analyst/scores.parquet: feature log_total_assets contribution
- F80 · Driver down #5: deposit growth over the past four quarters, value 6.4%; contribution to the score · 2026-06-30 · -0.125 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F81 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F82 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F83 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 1.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F84 · Trend: annualized provision for loan losses as a share of assets, change over four quarters, in percentage points · 2026-06-30 · +3.3 pp · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F85 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.316 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F86 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F87 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -2.5% · data/features/fct_bank_features.parquet: return_on_assets
- F88 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F89 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F91 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.081 · data/analyst/scores.parquet: feature return_on_assets contribution
- F92 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F93 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -27.8% · data/features/fct_bank_features.parquet: return_on_equity
- F94 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: return_on_equity
- F95 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 14.8% · data/features/fct_bank_features.parquet: return_on_equity
- F96 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2026-06-30 · -28.3 pp · data/features/fct_bank_features.parquet: return_on_equity
- F97 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · +0.198 · data/analyst/scores.parquet: feature return_on_equity contribution
- F98 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F99 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 4.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F100 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F101 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 2.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F103 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.001 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F104 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F105 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2026-06-30 · 2.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F106 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F107 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 1.9% · data/features/fct_bank_features.parquet: allowance_to_loans
- F110 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.086 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F111 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F112 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 79.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F113 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 70.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F114 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 75.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F117 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.064 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F118 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F119 · Trend: ratios outside their own prior range · 2026-06-30 · 17 · data/features/fct_bank_features.parquet
- F120 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F121 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F122 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F123 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F124 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 98.9% · data/analyst/scores.parquet: percentile
- F125 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
