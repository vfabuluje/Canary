---
cert: 25054
name: "Summit National Bank"
as_of: 2026-06-30
rank: 11
n_banks: 4313
percentile: 99.7681428240204
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:54:42"
writer_model: "claude-opus-5-5"
checked: true
---

# Summit National Bank (cert 25054)

*Outcome not yet known.*

## Summary

Summit National Bank, a small bank in WY, ranked 11 out of 4,313 banks nationally as of 2026-06-30, placing it in the 99.8th percentile, where higher means riskier. That rank puts it on Canary's watchlist, the riskiest 2% of banks. Its capital cushion is thin, with equity at 2.4% of assets against a national median of 10.6%, and it lost money, with a return on equity of -101.6%. Its loan problems, by contrast, look close to typical, with loans 90+ days past due or not accruing interest at 0.5%, the same as the national median.

## Warning signs in the data

Capital, the owners' money that absorbs losses, is far below normal: equity is 2.4% of assets versus a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) is 2.5% versus 11.0%. The Tier 1 risk-based capital ratio, which weighs capital against how risky the assets are, is 4.8% versus a median of 14.6%, and the total risk-based capital ratio is 6.1% versus 15.8%. Earnings are deeply negative, with a return on assets of -2.2% against a median of 1.2%, and an efficiency ratio (operating costs as a share of revenue) of 233.1% against 62.1%.

Credit quality, meaning how well borrowers are repaying, looks mostly ordinary: loans 90+ days past due or not accruing interest are 0.5%, matching the median of 0.5%. The Texas ratio, which sets troubled assets against capital plus reserves, is 7.3%, above the median of 2.9%, largely because capital is so small.

On funding, brokered deposits (money placed through middlemen, which can leave quickly) make up 34.4% of deposits, while the national median is 0.0%. Uninsured deposits are low at 9.1% versus 24.8%, and cash is high at 27.8% of assets versus 6.2%. Unrealized losses on bonds available for sale equal 17.0% of equity, well above the median of 5.6%. The bank is also shrinking, with assets down -24.6% over the past four quarters while the median bank grew 4.5%.

## Understanding the score

As of 2026-06-30, the bank ranked 11 of 4,313 banks, the 99.8th percentile on a scale from 0 to 100 where higher means riskier. It is flagged on the watchlist, which holds the top 2% of banks, or 87 banks that quarter.

The five factors that raised the score most were a return on equity of -101.6%, contributing +1.509, and a Tier 1 risk-based capital ratio of 4.8%, contributing +1.371. Next came bond losses on available-for-sale securities at 17.0% of equity, contributing +0.545, a total risk-based capital ratio of 6.1%, contributing +0.482, and brokered deposits at 34.4% of deposits, contributing +0.410.

The five factors that lowered the score most were the Texas ratio of 7.3%, contributing -1.172, and nonaccrual assets and foreclosed property at 0.2% of assets, contributing -0.755. Deposit growth of -24.2% contributed -0.471, loans 90+ days past due or not accruing at 0.5% contributed -0.440, and securities at 17.1% of assets contributed -0.332.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 269 | 4,589 |  |
| 2024-12-31 | 17 | 4,560 | ▲ watchlist |
| 2025-03-31 | 12 | 4,536 | ▲ watchlist |
| 2025-06-30 | 3 | 4,494 | ▲ watchlist |
| 2025-09-30 | 3 | 4,452 | ▲ watchlist |
| 2025-12-31 | 5 | 4,411 | ▲ watchlist |
| 2026-03-31 | 100 | 4,353 |  |
| 2026-06-30 | 11 | 4,313 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own range over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 30 ratios compared this way, 7 sat outside their own prior range at 2026-06-30. The model rated the bank about the same as a year earlier, when it stood at the 100.0th percentile on 2025-06-30, versus the 99.8th percentile and rank 11 of 4,313 now.

Brokered deposits reached 34.4% of deposits, above their prior range of 0.0% to 32.0%, up +4.8 pp over four quarters, and contributed +0.410 log-odds units, which pushed the score up. Interest expense was 2.5% of assets, above its prior range of 0.3% to 2.1%, and contributed +0.094, which pushed the score up. The provision for loan losses was -0.9% of assets, below its prior range of 0.0% to 0.0%, and contributed +0.068, which pushed the score up. Asset growth was -24.6%, below its prior range of -22.7% to 34.1%, and contributed +0.078, which pushed the score up.

Deposit growth was -24.2%, below its prior range of -20.1% to 36.3%, yet its contribution of -0.471 pushed the score down. Net interest margin was 2.2%, below its prior range of 2.6% to 3.8%, but its contribution of -0.032 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | -0.9% | 0.0% to 0.0% | same quarter, prior 3 years | n/a | -0.9 pp | +0.068 | pushed the score up |
| net interest margin (the spread earned on lending and investing) | 2.2% | 2.6% to 3.8% | same quarter, prior 3 years | n/a | -0.3 pp | -0.032 | little effect on the score |
| annualized interest expense as a share of assets | 2.5% | 0.3% to 2.1% | same quarter, prior 3 years | n/a | +0.4 pp | +0.094 | pushed the score up |
| brokered deposits as a share of deposits | 34.4% | 0.0% to 32.0% | prior 12 quarters | +2.4 pp | +4.8 pp | +0.410 | pushed the score up |
| deposit growth over the past four quarters | -24.2% | -20.1% to 36.3% | prior 12 quarters | -4.0 pp | -22.8 pp | -0.471 | pushed the score down |
| asset growth over the past four quarters | -24.6% | -22.7% to 34.1% | prior 12 quarters | -1.9 pp | -17.8 pp | +0.078 | pushed the score up |

7 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

Hindsight view: the fact sheet contains no data from after the as-of quarter, so it cannot show how the bank's position developed later. Its place on the watchlist rests on the as-of figures described above, chiefly very thin capital, heavy losses and a large reliance on brokered deposits.

## What happened next

Hindsight view: the fact sheet includes no later ranks, watchlist flags or reporting status for this bank. Because of that, this memo cannot say how its rank moved after the as-of quarter or whether it still files reports.

## Sources

- F1 · Bank name · n/a · Summit National Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WY · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 11 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 2.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 6.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 7.3% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -2.2% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -101.6% · data/features/fct_bank_features.parquet: return_on_equity
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 233.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 9.1% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 34.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 27.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 17.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2026-06-30 · -24.6% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -101.6%; contribution to the score · 2026-06-30 · +1.509 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: the Tier 1 risk-based capital ratio, value 4.8%; contribution to the score · 2026-06-30 · +1.371 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver up #3: losses on bonds available for sale, as a share of equity, value 17.0%; contribution to the score · 2026-06-30 · +0.545 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 6.1%; contribution to the score · 2026-06-30 · +0.482 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: brokered deposits as a share of deposits, value 34.4%; contribution to the score · 2026-06-30 · +0.410 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 7.3%; contribution to the score · 2026-06-30 · -1.172 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: nonaccrual assets and foreclosed property, as a share of assets, value 0.2%; contribution to the score · 2026-06-30 · -0.755 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F82 · Driver down #3: deposit growth over the past four quarters, value -24.2%; contribution to the score · 2026-06-30 · -0.471 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F83 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 0.5%; contribution to the score · 2026-06-30 · -0.440 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F84 · Driver down #5: securities as a share of assets, value 17.1%; contribution to the score · 2026-06-30 · -0.332 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F89 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · -0.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F90 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F91 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F93 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.068 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F94 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F95 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F96 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 2.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F97 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.8% · data/features/fct_bank_features.parquet: net_interest_margin
- F99 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.032 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F100 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F101 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F102 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F103 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 2.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F105 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.094 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F106 · Trend: annualized interest expense as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F107 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 34.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F108 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F109 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 32.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F111 · Trend: brokered deposits as a share of deposits, change over four quarters, in percentage points · 2026-06-30 · +4.8 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F112 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · +0.410 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F113 · Trend: brokered deposits as a share of deposits, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F114 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2026-06-30 · -24.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F115 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · -20.1% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F116 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 36.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F119 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2026-06-30 · -0.471 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F120 · Trend: deposit growth over the past four quarters, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F121 · Trend: asset growth over the past four quarters, value at the as-of quarter · 2026-06-30 · -24.6% · data/features/fct_bank_features.parquet: asset_growth_4q
- F122 · Trend: asset growth over the past four quarters, lowest value in the comparison window · n/a · -22.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F123 · Trend: asset growth over the past four quarters, highest value in the comparison window · n/a · 34.1% · data/features/fct_bank_features.parquet: asset_growth_4q
- F126 · Trend: asset growth over the past four quarters, contribution to the score (model log-odds units) · 2026-06-30 · +0.078 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F127 · Trend: asset growth over the past four quarters, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F128 · Trend: ratios outside their own prior range · 2026-06-30 · 7 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F131 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F132 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F133 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 100.0% · data/analyst/scores.parquet: percentile
- F134 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
