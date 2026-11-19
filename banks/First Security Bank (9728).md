---
cert: 9728
name: "First Security Bank"
as_of: 2026-06-30
rank: 7
n_banks: 4313
percentile: 99.86088569441223
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:53:56"
writer_model: "claude-opus-5-5"
checked: true
---

# First Security Bank (cert 9728)

*Outcome not yet known.*

## Summary

As of 2026-06-30, First Security Bank, a Minnesota bank with $161.7 million in total assets, ranked 7 out of 4,313 FDIC-insured banks on Canary's risk score, placing it in the 99.9th percentile. That rank puts it on Canary's watchlist, the top 2% of banks by score, which held 87 banks that quarter. The score was pushed up mainly by heavy use of brokered deposits (money placed through middlemen rather than gathered from local customers) and by paper losses on its bond holdings. Strong profits and capital ratios pulled the score down somewhat, even though its capital sat below typical levels.

## Warning signs in the data

Capital, the cushion of the owners' own money that absorbs losses, was thinner than at most banks: equity was 7.0% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 7.9% against 11.0%. Risk-weighted measures were also below typical levels, with a Tier 1 risk-based capital ratio of 10.8% against a median of 14.6% and a total risk-based capital ratio of 12.1% against 15.8%.

Credit quality was weaker than usual: loans 90 or more days past due or no longer accruing interest were 2.6% of loans, well above the national median of 0.5%. Nonaccrual assets and foreclosed property made up 2.0% of assets against a median of 0.3%, and the Texas ratio (troubled assets against capital plus reserves) was 24.5% against a median of 2.9%.

Funding leaned on less stable sources: brokered deposits were 23.9% of deposits, while the national median was 0.0%, and core deposits (steady everyday customer deposits) were 52.2% of assets against 75.5%. Volatile funding was 22.5% of assets against a median of 9.0%, and loans equaled 98.6% of deposits against 80.2%. Unrealized losses on bonds available for sale, meaning drops in market value not yet booked as losses, equaled 9.9% of equity, well above the median of 5.6%.

## Understanding the score

First Security Bank ranked 7 of 4,313 banks as of 2026-06-30, the 99.9th percentile on a scale from 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks and held 87 banks that quarter.

The five factors pushing the score up most were brokered deposits at 23.9% of deposits (+1.395), unrealized losses on bonds available for sale at 9.9% of equity (+0.965), and core deposits at 52.2% of assets (+0.454). The other two were the efficiency ratio (operating costs as a share of revenue) at 55.8% (+0.424) and annualized interest expense at 2.5% of assets (+0.230).

The five factors pulling the score down most were return on equity (profit as a share of the owners' stake) at 15.0% (-0.630), the Tier 1 risk-based capital ratio at 10.8% (-0.588), and return on assets at 1.1% (-0.288). The other two were the total risk-based capital ratio at 12.1% (-0.238) and loans 30-89 days past due at 0.7% of assets (-0.194).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 378 | 4,589 |  |
| 2024-12-31 | 427 | 4,560 |  |
| 2025-03-31 | 764 | 4,536 |  |
| 2025-06-30 | 464 | 4,494 |  |
| 2025-09-30 | 300 | 4,452 |  |
| 2025-12-31 | 317 | 4,411 |  |
| 2026-03-31 | 19 | 4,353 | ▲ watchlist |
| 2026-06-30 | 7 | 4,313 | ▲ watchlist |

## How its ratios moved

Canary compares each ratio with the bank's own history, usually the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios. As of 2026-06-30, 7 of the 30 ratios checked sat outside their own prior range, and the bank ranked 7 of 4,313. A year earlier it was in the 89.7th percentile, and the model rated it riskier than a year earlier.

Commercial real estate loans fell to 8.2% of loans, below their prior range of 9.9% to 13.4%, and their contribution of +0.175 model log-odds units pushed the score up. The efficiency ratio was 55.8%, below its prior range of 57.8% to 63.2%, and its contribution of +0.424 pushed the score up.

The total risk-based capital ratio rose to 12.1%, above its prior range of 10.8% to 11.9%, yet its contribution of -0.238 pushed the score down. The Tier 1 risk-based capital ratio reached 10.8%, above its prior range of 9.8% to 10.7%, yet its contribution of -0.588 pushed the score down. Net interest margin was 3.51%, above its prior range of 3.2% to 3.45%, yet its contribution of -0.066 pushed the score down. The provision for loan losses (money set aside for expected bad loans) was 0.5% of assets, above its prior range of 0.1% to 0.3%, yet its contribution of -0.033 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| commercial real estate loans as a share of loans | 8.2% | 9.9% to 13.4% | prior 12 quarters | -1.9 pp | -2.0 pp | +0.175 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 55.8% | 57.8% to 63.2% | same quarter, prior 3 years | n/a | -2.1 pp | +0.424 | pushed the score up |
| the total risk-based capital ratio | 12.1% | 10.8% to 11.9% | prior 12 quarters | +0.3 pp | +0.9 pp | -0.238 | pushed the score down |
| annualized provision for loan losses as a share of assets | 0.5% | 0.1% to 0.3% | same quarter, prior 3 years | n/a | +0.3 pp | -0.033 | little effect on the score |
| the Tier 1 risk-based capital ratio | 10.8% | 9.8% to 10.7% | prior 12 quarters | +0.3 pp | +0.8 pp | -0.588 | pushed the score down |
| net interest margin (the spread earned on lending and investing) | 3.51% | 3.2% to 3.45% | same quarter, prior 3 years | n/a | +0.2 pp | -0.066 | pushed the score down |

7 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

In hindsight, this bank falls in Canary's open-watchlist group: it remains open and on the watchlist rather than having left the data. The fact sheet for this memo contains no figures from after the as-of quarter, so this section cannot add later measurements that explain the outcome. Its place on the watchlist rests on the as-of picture described above, chiefly its reliance on brokered and volatile funding and its bond losses.

## What happened next

In hindsight, the bank is still open and still flagged on the watchlist, according to its outcome group. The fact sheet provided here does not include later ranks, later flags, or reporting status beyond the as-of quarter, so no further detail can be given.

## Sources

- F1 · Bank name · n/a · First Security Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · MN · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 7 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 10.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 12.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 24.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 98.6% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 23.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 52.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 22.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 9.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $161.7 million · data/features/fct_bank_features.parquet: log_total_assets
- F75 · Driver up #1: brokered deposits as a share of deposits, value 23.9%; contribution to the score · 2026-06-30 · +1.395 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 9.9%; contribution to the score · 2026-06-30 · +0.965 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: core deposits as a share of assets, value 52.2%; contribution to the score · 2026-06-30 · +0.454 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F78 · Driver up #4: the efficiency ratio (operating costs as a share of revenue), value 55.8%; contribution to the score · 2026-06-30 · +0.424 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.5%; contribution to the score · 2026-06-30 · +0.230 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: return on equity (profit as a share of equity), value 15.0%; contribution to the score · 2026-06-30 · -0.630 · data/analyst/scores.parquet: feature return_on_equity contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 10.8%; contribution to the score · 2026-06-30 · -0.588 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: return on assets (profit as a share of assets), value 1.1%; contribution to the score · 2026-06-30 · -0.288 · data/analyst/scores.parquet: feature return_on_assets contribution
- F83 · Driver down #4: the total risk-based capital ratio, value 12.1%; contribution to the score · 2026-06-30 · -0.238 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F84 · Driver down #5: loans 30-89 days past due, as a share of assets, value 0.7%; contribution to the score · 2026-06-30 · -0.194 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F89 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 8.2% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F90 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 9.9% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F91 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 13.4% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F94 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.175 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F95 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F96 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 55.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 57.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 63.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F100 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.424 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F102 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2026-06-30 · 12.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F103 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 10.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F104 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 11.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F107 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2026-06-30 · -0.238 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F108 · Trend: the total risk-based capital ratio, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F109 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F110 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F111 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F113 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.033 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F114 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F115 · Trend: the Tier 1 risk-based capital ratio, value at the as-of quarter · 2026-06-30 · 10.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F116 · Trend: the Tier 1 risk-based capital ratio, lowest value in the comparison window · n/a · 9.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F117 · Trend: the Tier 1 risk-based capital ratio, highest value in the comparison window · n/a · 10.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F120 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2026-06-30 · -0.588 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F121 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F122 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 3.51% · data/features/fct_bank_features.parquet: net_interest_margin
- F123 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F124 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.45% · data/features/fct_bank_features.parquet: net_interest_margin
- F126 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.066 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F127 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F128 · Trend: ratios outside their own prior range · 2026-06-30 · 7 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F131 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F132 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F133 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 89.7% · data/analyst/scores.parquet: percentile
- F134 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
