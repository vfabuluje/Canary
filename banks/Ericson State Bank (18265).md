---
cert: 18265
name: "Ericson State Bank"
as_of: 2019-12-31
rank: 4
n_banks: 5244
percentile: 99.94279176201373
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2020-02-14
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:49:29"
writer_model: "claude-opus-5-5"
checked: true
---

# Ericson State Bank (cert 18265)

*Hindsight: failed 2020-02-14. Canary flagged it 4 quarters ahead.*

## Summary

As of 2019-12-31, Ericson State Bank (cert 18265, state NE) ranked 4 out of 5,244 banks on Canary's risk score, placing it in the 99.9th percentile, where higher means riskier. It was on Canary's watchlist, which covers the 2% of banks with the highest scores. Its capital cushion was thin, with equity at 3.7% of assets against a national median of 11.4%. Problem loans were high: loans 90+ days past due or not accruing interest were 6.9% of loans, compared with a national median of 0.5%.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was far below typical levels: equity was 3.7% of assets versus a national median of 11.4%. The leverage ratio (core capital as a share of average assets) was 3.4% against a median of 10.9%, and the Tier 1 risk-based capital ratio (core capital measured against assets weighted by riskiness) was 4.3% against a median of 15.5%. The total risk-based capital ratio was 5.6%, well below the median of 16.6%.

Credit quality, meaning how well borrowers were repaying, looked weak: loans 90+ days past due or not accruing interest were 6.9% of loans versus a median of 0.5%, and loans 30-89 days past due were 2.5% of assets versus 0.3%. Annualized loan write-offs, net of recoveries, were 7.1% of loans against a median of 0.0%, and the provision for loan losses (money set aside for expected losses) was 6.9% of assets against 0.1%. The Texas ratio, which compares troubled assets with capital plus reserves, was 90.1%, far above the median of 3.6%. These costs left the bank unprofitable, with return on assets of -3.4% versus a median of 1.1% and return on equity of -48.4% versus 9.3%.

On funding and liquidity, cash was 0.5% of assets versus a median of 7.2%, brokered deposits (money placed through intermediaries) were 4.2% of deposits versus 0.0%, and interest expense was 2.0% of assets versus 0.7%. Uninsured deposits were lower than typical, at 4.3% of deposits against a median of 19.5%. On bonds, losses on bonds held to maturity were -7.5% of equity versus a median of 0.0%, while losses on bonds available for sale were 0.0% versus -0.6%.

## Understanding the score

As of 2019-12-31, the bank ranked 4 out of 5,244 banks, in the 99.9th percentile on a scale of 0 to 100 where higher means riskier. That put it on the watchlist, the top 2% of banks by score, which held 105 banks that quarter.

The five factors that pushed the score up most were the Tier 1 risk-based capital ratio at 4.3% (contribution +1.915), return on equity at -48.4% (+0.809), and the Texas ratio at 90.1% (+0.500). Next came loans 90+ days past due or not accruing interest at 6.9% of loans (+0.476) and the provision for loan losses at 6.9% of assets (+0.196).

The five factors that pulled the score down most were losses on bonds held to maturity at -7.5% of equity (contribution -0.784), construction loans at 0.0% of loans (-0.309), and net interest margin at 4.0% (-0.149). Core deposits, the stable everyday deposits, at 83.8% of assets (-0.131) and volatile funding at 8.3% of assets (-0.092) also lowered the score slightly.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2018-03-31 | 275 | 5,674 |  |
| 2018-06-30 | 252 | 5,610 |  |
| 2018-09-30 | 253 | 5,544 |  |
| 2018-12-31 | 11 | 5,473 | ▲ watchlist |
| 2019-03-31 | 9 | 5,428 | ▲ watchlist (first flag) |
| 2019-06-30 | 10 | 5,369 | ▲ watchlist |
| 2019-09-30 | 11 | 5,325 | ▲ watchlist |
| 2019-12-31 | 4 | 5,244 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own range over the prior 12 quarters, or over the same quarter in the prior 3 years for year-to-date ratios. As of 2019-12-31, 18 of the 30 ratios checked sat outside their own prior range, and the table shows the 6 furthest outside. The bank ranked 4 nationally, and its percentile of 99.8% at 2018-12-31 means the model rated it about the same as a year earlier.

Return on equity was -48.4%, below its prior range of 2.8% to 16.7% after a change of -51.2 pp over four quarters, and it pushed the score up, contributing +0.809 model log-odds units. Return on assets was -3.4%, below its prior range of 0.3% to 1.6%, and pushed the score up with a contribution of +0.103. The provision for loan losses was 6.9% of assets, above its prior range of 0.4% to 1.9%, and pushed the score up with a contribution of +0.196. Loans 30-89 days past due were 2.5% of assets, above their prior range of 0.0% to 0.1%, and pushed the score up with a contribution of +0.192.

Two ratios moved far outside their ranges yet barely moved the score. Net loan write-offs were 7.1% of loans, well above their prior range of 0.0% to 1.1%, but had little effect on the score, contributing -0.013. The leverage ratio fell to 3.4%, below its prior range of 7.8% to 10.2% after a change of -4.6 pp in one quarter, yet it also had little effect on the score, contributing +0.015.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized loan write-offs, net of recoveries, as a share of loans | 7.1% | 0.0% to 1.1% | same quarter, prior 3 years | n/a | +7.1 pp | -0.013 | little effect on the score |
| return on equity (profit as a share of equity) | -48.4% | 2.8% to 16.7% | same quarter, prior 3 years | n/a | -51.2 pp | +0.809 | pushed the score up |
| annualized provision for loan losses as a share of assets | 6.9% | 0.4% to 1.9% | same quarter, prior 3 years | n/a | +5.0 pp | +0.196 | pushed the score up |
| return on assets (profit as a share of assets) | -3.4% | 0.3% to 1.6% | same quarter, prior 3 years | n/a | -3.6 pp | +0.103 | pushed the score up |
| loans 30-89 days past due, as a share of assets | 2.5% | 0.0% to 0.1% | prior 12 quarters | +2.5 pp | +2.4 pp | +0.192 | pushed the score up |
| the leverage ratio (core capital as a share of average assets) | 3.4% | 7.8% to 10.2% | prior 12 quarters | -4.6 pp | -4.5 pp | +0.015 | little effect on the score |

18 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Canary first flagged the bank in the quarter ending 2019-03-31, a lead time of 4 quarters before it failed on 2020-02-14. At that first flag, the biggest factors raising the score were the Texas ratio at 77.2% (contribution +1.067) and loans 90+ days past due or not accruing interest at 8.8% of loans (+0.760). Commercial real estate loans at 4.4% of loans (+0.272), the efficiency ratio at 35.3% (+0.271) and deposit growth of 24.3% (+0.168) also added to it. At that time the bank was still profitable, and return on equity of 26.6% was the largest factor lowering the score (-0.616).

## What happened next

In hindsight, the last quarter the bank reported was 2019-12-31, the as-of quarter of this memo. The bank failed on February 14, 2020, so no later ranks or flags exist for it.

## Sources

- F1 · Bank name · n/a · Ericson State Bank · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 18265 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2019-12-31 · 2019-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NE · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2019-12-31 · 4 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2019-12-31 · 5,244 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2019-12-31 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2019-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2019-12-31 · 105 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2019-12-31 · 3.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2019-12-31 · 11.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2019-12-31 · 3.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2019-12-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2019-12-31 · 4.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2019-12-31 · 15.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2019-12-31 · 5.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2019-12-31 · 16.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2019-12-31 · 6.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2019-12-31 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2019-12-31 · 2.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2019-12-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2019-12-31 · 7.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2019-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2019-12-31 · 6.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2019-12-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2019-12-31 · 90.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2019-12-31 · 3.6% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2019-12-31 · -3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2019-12-31 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2019-12-31 · -48.4% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2019-12-31 · 9.3% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2019-12-31 · 2.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2019-12-31 · 0.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2019-12-31 · 4.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2019-12-31 · 19.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2019-12-31 · 4.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2019-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2019-12-31 · 0.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2019-12-31 · 7.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2019-12-31 · -7.5% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2019-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2019-12-31 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2019-12-31 · -0.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 4.3%; contribution to the score · 2019-12-31 · +1.915 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -48.4%; contribution to the score · 2019-12-31 · +0.809 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 90.1%; contribution to the score · 2019-12-31 · +0.500 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 6.9%; contribution to the score · 2019-12-31 · +0.476 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: annualized provision for loan losses as a share of assets, value 6.9%; contribution to the score · 2019-12-31 · +0.196 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F80 · Driver down #1: losses on bonds held to maturity, as a share of equity, value -7.5%; contribution to the score · 2019-12-31 · -0.784 · data/analyst/scores.parquet: feature htm_unrealized_loss_to_equity contribution
- F81 · Driver down #2: construction loans as a share of loans, value 0.0%; contribution to the score · 2019-12-31 · -0.309 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: net interest margin (the spread earned on lending and investing), value 4.0%; contribution to the score · 2019-12-31 · -0.149 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F83 · Driver down #4: core deposits as a share of assets, value 83.8%; contribution to the score · 2019-12-31 · -0.131 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F84 · Driver down #5: volatile funding as a share of assets, value 8.3%; contribution to the score · 2019-12-31 · -0.092 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F85 · Failure date · 2020-02-14 · 2020-02-14 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2019-03-31 · 2019-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2019-03-31: the Texas ratio (troubled assets against capital plus reserves), value 77.2%; contribution to the score · 2019-03-31 · +1.067 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Driver up #2 at 2019-03-31: loans 90+ days past due or not accruing interest, as a share of loans, value 8.8%; contribution to the score · 2019-03-31 · +0.760 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F90 · Driver up #3 at 2019-03-31: commercial real estate loans as a share of loans, value 4.4%; contribution to the score · 2019-03-31 · +0.272 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F91 · Driver up #4 at 2019-03-31: the efficiency ratio (operating costs as a share of revenue), value 35.3%; contribution to the score · 2019-03-31 · +0.271 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F92 · Driver up #5 at 2019-03-31: deposit growth over the past four quarters, value 24.3%; contribution to the score · 2019-03-31 · +0.168 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F93 · Driver down #1 at 2019-03-31: return on equity (profit as a share of equity), value 26.6%; contribution to the score · 2019-03-31 · -0.616 · data/analyst/scores.parquet: feature return_on_equity contribution
- F98 · Last quarter the bank reported · 2019-12-31 · 2019-12-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2019-12-31 · 7.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F100 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F101 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F103 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2019-12-31 · -0.013 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F104 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2019-12-31 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F105 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2019-12-31 · -48.4% · data/features/fct_bank_features.parquet: return_on_equity
- F106 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 2.8% · data/features/fct_bank_features.parquet: return_on_equity
- F107 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 16.7% · data/features/fct_bank_features.parquet: return_on_equity
- F108 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2019-12-31 · -51.2 pp · data/features/fct_bank_features.parquet: return_on_equity
- F109 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2019-12-31 · +0.809 · data/analyst/scores.parquet: feature return_on_equity contribution
- F110 · Trend: return on equity (profit as a share of equity), what the model did with it · 2019-12-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F111 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2019-12-31 · 6.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F112 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F113 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 1.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F115 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2019-12-31 · +0.196 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F116 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2019-12-31 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F117 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2019-12-31 · -3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F118 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F119 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.6% · data/features/fct_bank_features.parquet: return_on_assets
- F121 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2019-12-31 · +0.103 · data/analyst/scores.parquet: feature return_on_assets contribution
- F122 · Trend: return on assets (profit as a share of assets), what the model did with it · 2019-12-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F123 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2019-12-31 · 2.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F124 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F125 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F128 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2019-12-31 · +0.192 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F129 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2019-12-31 · pushed the score up · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F130 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2019-12-31 · 3.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F131 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 7.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F132 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F133 · Trend: the leverage ratio (core capital as a share of average assets), change over one quarter, in percentage points · 2019-12-31 · -4.6 pp · data/features/fct_bank_features.parquet: leverage_ratio
- F135 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2019-12-31 · +0.015 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F136 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2019-12-31 · little effect on the score · data/analyst/scores.parquet: feature leverage_ratio contribution
- F137 · Trend: ratios outside their own prior range · 2019-12-31 · 18 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios shown in the table (the furthest outside their prior range) · 2019-12-31 · 6 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios compared with their own prior range · 2019-12-31 · 30 · data/features/fct_bank_features.parquet
- F140 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F142 · Percentile a year earlier (100 = highest risk) · 2018-12-31 · 99.8% · data/analyst/scores.parquet: percentile
- F143 · Trend: how the model's rating compares with a year earlier · 2019-12-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
