---
cert: 28266
name: "Connect Community Bank"
as_of: 2026-06-30
rank: 9
n_banks: 4313
percentile: 99.81451425921632
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:54:19"
writer_model: "claude-opus-5-5"
checked: true
---

# Connect Community Bank (cert 28266)

*Outcome not yet known.*

## Summary

Connect Community Bank, a Washington state bank, ranked 9 out of 4,313 banks nationally on Canary's risk score as of 2026-06-30, placing it in the 99.8th percentile, where higher means riskier. That ranking put it on Canary's watchlist, which covers the top 2% of banks, or 87 banks that quarter. The main reasons were heavy losses, with return on equity (profit as a share of the owners' stake) at -43.1%, and thin capital, with equity at 3.7% of assets. Its loan problems, by contrast, were low, which pulled the score down.

## Warning signs in the data

Capital, the owners' cushion that absorbs losses, was thin: equity was 3.7% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 3.6% against 11.0%. Its risk-based capital ratios, which weigh assets by riskiness, were also well below typical levels, with Tier 1 at 7.7% versus 14.6% and total capital at 8.9% versus 15.8%. The bank was losing money, with return on assets of -1.7% against a median of 1.2% and return on equity of -43.1% against 11.6%. Its efficiency ratio (operating costs as a share of revenue) was 153.5% versus a median of 62.1%, meaning costs exceeded revenue, and its net interest margin (the spread earned on lending and investing) was 2.9% versus 3.9%.

Credit quality looked sound: loans 90 or more days past due or not accruing interest were 0.1% of loans versus a median of 0.5%, and nonaccrual assets and foreclosed property were 0.1% of assets versus 0.3%. Loan write-offs (loans recorded as lost, net of recoveries) were somewhat higher than typical, at 0.3% of loans against a median of 0.0%.

Funding looked stable: uninsured deposits were 3.3% of deposits versus a median of 24.8%, core deposits (steady customer deposits) were 89.8% of assets versus 75.5%, and cash was 10.0% of assets versus 6.2%. Deposits grew 22.9% over the past four quarters, well above the median of 4.2%. Unrealized losses on bonds held to maturity (bonds the bank plans to keep until they are repaid) equaled 36.6% of equity, far above the national median of 0.0%.

## Understanding the score

As of 2026-06-30, the bank ranked 9 out of 4,313 banks, in the 99.8th percentile on a scale of 0 to 100 where higher means riskier. It was flagged for the watchlist, which holds the top 2% of banks by score, 87 banks that quarter.

The five factors that pushed the score up most were return on equity at -43.1% (contribution +1.775), the Tier 1 risk-based capital ratio at 7.7% (+0.537), commercial real estate loans as a share of loans at 1.1% (+0.369), the total risk-based capital ratio at 8.9% (+0.327), and the leverage ratio at 3.6% (+0.149).

The five factors that pulled the score down most were the Texas ratio (troubled assets against capital plus reserves) at 2.6% (contribution -1.180), loans 90 or more days past due or not accruing at 0.1% (-0.995), nonaccrual assets and foreclosed property at 0.1% (-0.613), loan-loss reserves at 1.0% of loans (-0.131), and loans as a share of deposits at 82.8% (-0.092).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,206 | 4,589 |  |
| 2024-12-31 | 2,128 | 4,560 |  |
| 2025-03-31 | 428 | 4,536 |  |
| 2025-06-30 | 591 | 4,494 |  |
| 2025-09-30 | 108 | 4,452 |  |
| 2025-12-31 | 64 | 4,411 | ▲ watchlist |
| 2026-03-31 | 28 | 4,353 | ▲ watchlist |
| 2026-06-30 | 9 | 4,313 | ▲ watchlist |

## How its ratios moved

Canary compared 30 of the bank's ratios with their own prior range, mostly over the prior 12 quarters, and 15 fell outside that range; the table shows the 6 furthest outside. The bank ranked 9 nationally at 2026-06-30, and its percentile a year earlier, at 2025-06-30, was 86.9%, so the model rated it riskier than a year earlier.

Return on equity was -43.1%, below its prior range of -29.9% to -2.1%, and its contribution of +1.775 model log-odds units pushed the score up. Commercial real estate loans were 1.1% of loans, above a prior range of 0.0% to 0.1%, and their contribution of +0.369 pushed the score up. Loan write-offs were 0.3% of loans, above a prior range of 0.0% to 0.0%, yet their contribution of +0.046 had little effect on the score.

Core deposits were 89.8% of assets, above a prior range of 67.7% to 78.6%, but their contribution of +0.004 had little effect on the score. Losses on bonds held to maturity were 36.6% of equity, above a prior range of 19.0% to 32.7%, yet their contribution of -0.057 pushed the score down. Nonaccrual assets and foreclosed property were 0.1% of assets, above a prior range of 0.0% to 0.0%, yet their contribution of -0.613 pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| commercial real estate loans as a share of loans | 1.1% | 0.0% to 0.1% | prior 12 quarters | +1.1 pp | +1.1 pp | +0.369 | pushed the score up |
| core deposits as a share of assets | 89.8% | 67.7% to 78.6% | prior 12 quarters | +13.6 pp | +15.3 pp | +0.004 | little effect on the score |
| return on equity (profit as a share of equity) | -43.1% | -29.9% to -2.1% | same quarter, prior 3 years | n/a | -13.2 pp | +1.775 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.3% | 0.0% to 0.0% | same quarter, prior 3 years | n/a | +0.3 pp | +0.046 | little effect on the score |
| losses on bonds held to maturity, as a share of equity | 36.6% | 19.0% to 32.7% | prior 12 quarters | +5.2 pp | +3.9 pp | -0.057 | pushed the score down |
| nonaccrual assets and foreclosed property, as a share of assets | 0.1% | 0.0% to 0.0% | prior 12 quarters | +0.1 pp | +0.1 pp | -0.613 | pushed the score down |

15 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

In hindsight, this fact sheet contains no information from after the as-of quarter, so there is no later record to explain how the bank's situation developed. The bank's place on the watchlist rests only on the as-of data described above, and it remains an open watchlist case.

## What happened next

In hindsight, our data includes no later ranks, flags or reporting status for this bank after the as-of quarter. We therefore cannot yet say how its rank moved or whether it continued to report.

## Sources

- F1 · Bank name · n/a · Connect Community Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 9 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 3.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 3.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 7.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -1.7% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -43.1% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 153.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 89.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 36.6% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · 22.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -43.1%; contribution to the score · 2026-06-30 · +1.775 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: the Tier 1 risk-based capital ratio, value 7.7%; contribution to the score · 2026-06-30 · +0.537 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver up #3: commercial real estate loans as a share of loans, value 1.1%; contribution to the score · 2026-06-30 · +0.369 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 8.9%; contribution to the score · 2026-06-30 · +0.327 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: the leverage ratio (core capital as a share of average assets), value 3.6%; contribution to the score · 2026-06-30 · +0.149 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 2.6%; contribution to the score · 2026-06-30 · -1.180 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: loans 90+ days past due or not accruing interest, as a share of loans, value 0.1%; contribution to the score · 2026-06-30 · -0.995 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F82 · Driver down #3: nonaccrual assets and foreclosed property, as a share of assets, value 0.1%; contribution to the score · 2026-06-30 · -0.613 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F83 · Driver down #4: loan-loss reserves as a share of loans, value 1.0%; contribution to the score · 2026-06-30 · -0.131 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F84 · Driver down #5: loans as a share of deposits, value 82.8%; contribution to the score · 2026-06-30 · -0.092 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F89 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F90 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F91 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F94 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.369 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F95 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F96 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 89.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F97 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 67.7% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F98 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 78.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F101 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.004 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F102 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F103 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -43.1% · data/features/fct_bank_features.parquet: return_on_equity
- F104 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -29.9% · data/features/fct_bank_features.parquet: return_on_equity
- F105 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -2.1% · data/features/fct_bank_features.parquet: return_on_equity
- F107 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · +1.775 · data/analyst/scores.parquet: feature return_on_equity contribution
- F108 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F109 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F110 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F111 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F113 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.046 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F114 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F115 · Trend: losses on bonds held to maturity, as a share of equity, value at the as-of quarter · 2026-06-30 · 36.6% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F116 · Trend: losses on bonds held to maturity, as a share of equity, lowest value in the comparison window · n/a · 19.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F117 · Trend: losses on bonds held to maturity, as a share of equity, highest value in the comparison window · n/a · 32.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F120 · Trend: losses on bonds held to maturity, as a share of equity, contribution to the score (model log-odds units) · 2026-06-30 · -0.057 · data/analyst/scores.parquet: feature htm_unrealized_loss_to_equity contribution
- F121 · Trend: losses on bonds held to maturity, as a share of equity, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature htm_unrealized_loss_to_equity contribution
- F122 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F123 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F124 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F127 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.613 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F128 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F129 · Trend: ratios outside their own prior range · 2026-06-30 · 15 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F132 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F134 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 86.9% · data/analyst/scores.parquet: percentile
- F135 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
