---
cert: 58088
name: "Southpoint Bank"
as_of: 2026-06-30
rank: 4
n_banks: 4313
percentile: 99.93044284720612
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:53:34"
writer_model: "claude-opus-5-5"
checked: true
---

# Southpoint Bank (cert 58088)

*Outcome not yet known.*

## Summary

Southpoint Bank, an Alabama bank with $1.4 billion in total assets, ranked 4 out of 4,313 banks nationally on Canary's risk score as of 2026-06-30. That places it in the 99.9th percentile, where higher means riskier, and the bank was flagged on the watchlist. Its profits had turned to losses, its capital cushions sat well below national medians, and bad loans and write-offs were far above typical levels.

## Warning signs in the data

Capital, the bank's own money that absorbs losses, was thin: equity was 7.7% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 6.9% against 11.0%. Its Tier 1 risk-based capital ratio was 8.9% versus a median of 14.6%, and its total risk-based capital ratio was 10.2% versus 15.8%. Earnings were negative, with return on assets of -1.7% against a median of 1.2% and return on equity of -22.1% against 11.6%.

Credit quality was weak: loans 90+ days past due or not accruing interest were 3.5% of loans, well above the 0.5% median. Annualized write-offs of bad loans, net of recoveries, were 4.5% of loans against a median of 0.0%, and the provision (money set aside for expected loan losses) was 3.7% of assets against 0.1%. The Texas ratio, which weighs troubled assets against capital plus reserves, was 32.5%, far above the 2.9% median.

On funding, brokered deposits (money placed through intermediaries, often less loyal) made up 23.4% of deposits versus a median of 0.0%, while core deposits were 55.0% of assets versus 75.5%. Deposits changed by -18.8% over the past four quarters, while the median bank grew deposits by 4.2%; on the other side, cash was a relatively high 13.2% of assets versus 6.2%. Unrealized losses on bonds available for sale equaled 8.7% of equity, above the 5.6% median.

## Understanding the score

Southpoint Bank ranked 4 of 4,313 banks as of 2026-06-30, placing it in the 99.9th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks, or 87 banks that quarter.

The five factors that pushed the score up most were return on equity at -22.1% (+0.828), losses on bonds available for sale at 8.7% of equity (+0.762), brokered deposits at 23.4% of deposits (+0.511), the Tier 1 risk-based capital ratio at 8.9% (+0.419), and interest expense at 2.8% of assets (+0.376).

The five factors that pulled the score down most were construction loans at 10.0% of loans (-0.301), loans 30-89 days past due at 0.7% of assets (-0.233), the Texas ratio at 32.5% (-0.231), total assets of $1.4 billion (-0.178), and commercial real estate loans at 38.0% of loans (-0.165).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 31 | 4,589 | ▲ watchlist |
| 2024-12-31 | 7 | 4,560 | ▲ watchlist |
| 2025-03-31 | 18 | 4,536 | ▲ watchlist |
| 2025-06-30 | 13 | 4,494 | ▲ watchlist |
| 2025-09-30 | 7 | 4,452 | ▲ watchlist |
| 2025-12-31 | 6 | 4,411 | ▲ watchlist |
| 2026-03-31 | 6 | 4,353 | ▲ watchlist |
| 2026-06-30 | 4 | 4,313 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own prior range, usually over the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios. Of 30 ratios checked, 8 sat outside their own prior range as of 2026-06-30. The model rated the bank about the same as a year earlier, when it sat in the 99.7th percentile on 2025-06-30; it now ranks 4 of 4,313.

Return on equity was -22.1%, far below its prior range of 7.2% to 13.7%, and contributed +0.828 model log-odds units, which pushed the score up. Return on equity changed by -29.3 pp over four quarters. The loan-loss provision was 3.7% of assets, above its prior range of 0.2% to 0.9%, and contributed +0.168, which pushed the score up.

Net loan write-offs were 4.5% of loans, above their prior range of 0.0% to 0.9%, yet contributed only -0.005, having little effect on the score. Return on assets was -1.7%, below its prior range of 0.5% to 1.2%, but contributed just +0.043, having little effect on the score. The efficiency ratio was 65.3%, above its prior range of 53.7% to 57.9%, yet contributed -0.044, having little effect on the score. Construction loans were 10.0% of loans, below their prior range of 10.7% to 17.5%, and contributed -0.301, which pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -22.1% | 7.2% to 13.7% | same quarter, prior 3 years | n/a | -29.3 pp | +0.828 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 4.5% | 0.0% to 0.9% | same quarter, prior 3 years | n/a | +3.6 pp | -0.005 | little effect on the score |
| annualized provision for loan losses as a share of assets | 3.7% | 0.2% to 0.9% | same quarter, prior 3 years | n/a | +2.8 pp | +0.168 | pushed the score up |
| return on assets (profit as a share of assets) | -1.7% | 0.5% to 1.2% | same quarter, prior 3 years | n/a | -2.2 pp | +0.043 | little effect on the score |
| the efficiency ratio (operating costs as a share of revenue) | 65.3% | 53.7% to 57.9% | same quarter, prior 3 years | n/a | +7.4 pp | -0.044 | little effect on the score |
| construction loans as a share of loans | 10.0% | 10.7% to 17.5% | prior 12 quarters | -0.7 pp | -4.2 pp | -0.301 | pushed the score down |

8 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

In hindsight: the bank is in the open-watchlist case, meaning it was flagged but our fact sheet holds no later data showing what came after. Without hindsight facts, we cannot say whether its condition improved or worsened after the as-of quarter.

## What happened next

In hindsight: this fact sheet contains no later ranks, flags, or reporting status for the bank. So we cannot state from this data whether it stayed on the watchlist or whether it still reports.

## Sources

- F1 · Bank name · n/a · Southpoint Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · AL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 4 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 3.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 3.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 32.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -1.7% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -22.1% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 23.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 55.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 13.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 8.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $1.4 billion · data/features/fct_bank_features.parquet: log_total_assets
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -18.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -22.1%; contribution to the score · 2026-06-30 · +0.828 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 8.7%; contribution to the score · 2026-06-30 · +0.762 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: brokered deposits as a share of deposits, value 23.4%; contribution to the score · 2026-06-30 · +0.511 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F78 · Driver up #4: the Tier 1 risk-based capital ratio, value 8.9%; contribution to the score · 2026-06-30 · +0.419 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.8%; contribution to the score · 2026-06-30 · +0.376 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: construction loans as a share of loans, value 10.0%; contribution to the score · 2026-06-30 · -0.301 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F81 · Driver down #2: loans 30-89 days past due, as a share of assets, value 0.7%; contribution to the score · 2026-06-30 · -0.233 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 32.5%; contribution to the score · 2026-06-30 · -0.231 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: total assets, value $1.4 billion; contribution to the score · 2026-06-30 · -0.178 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: commercial real estate loans as a share of loans, value 38.0%; contribution to the score · 2026-06-30 · -0.165 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F89 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -22.1% · data/features/fct_bank_features.parquet: return_on_equity
- F90 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 7.2% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 13.7% · data/features/fct_bank_features.parquet: return_on_equity
- F92 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2026-06-30 · -29.3 pp · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · +0.828 · data/analyst/scores.parquet: feature return_on_equity contribution
- F94 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F95 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F96 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F97 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F99 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.005 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F100 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F101 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 3.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F102 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F103 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F105 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.168 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F106 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F107 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -1.7% · data/features/fct_bank_features.parquet: return_on_assets
- F108 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F111 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.043 · data/analyst/scores.parquet: feature return_on_assets contribution
- F112 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature return_on_assets contribution
- F113 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 65.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F114 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 53.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F115 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 57.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F117 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.044 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F118 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F119 · Trend: construction loans as a share of loans, value at the as-of quarter · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F120 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 10.7% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F121 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 17.5% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F124 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.301 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F125 · Trend: construction loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F126 · Trend: ratios outside their own prior range · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F129 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F130 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F131 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F132 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
