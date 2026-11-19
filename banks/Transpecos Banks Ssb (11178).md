---
cert: 11178
name: "Transpecos Banks Ssb"
as_of: 2026-06-30
rank: 6
n_banks: 4313
percentile: 99.8840714120102
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:53:35"
writer_model: "claude-opus-5-5"
checked: true
---

# Transpecos Banks Ssb (cert 11178)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Transpecos Banks Ssb, a Texas bank, ranked 6 out of 4,313 FDIC-insured banks on Canary's risk score, which places it in the 99.9th percentile, where higher means riskier. That ranking put the bank on Canary's watchlist, the riskiest 2% of banks, which held 87 banks that quarter. The main concerns were a high level of troubled loans, thin capital, losses rather than profits, and heavy use of brokered deposits (money placed through middlemen rather than gathered directly from local customers).

## Warning signs in the data

Capital, the cushion that absorbs losses, was thin: equity was 6.7% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 6.7% against a median of 11.0%. The risk-based capital ratios, which weigh assets by riskiness, were also well below typical levels, with Tier 1 at 9.7% against a median of 14.6% and total capital at 10.7% against a median of 15.8%.

Credit quality was the weakest area: loans 90 or more days past due or no longer earning interest were 8.1% of loans, far above the national median of 0.5%. The Texas ratio, which compares troubled assets with the capital and reserves available to cover them, stood at 74.8% against a median of 2.9%. The bank was also losing money, with a return on assets of -1.6% compared with a median of 1.2%.

On funding, brokered deposits made up 27.5% of deposits while the median bank had 0.0%, and uninsured deposits (balances above the government insurance limit) were 39.8% of deposits against a median of 24.8%. On the steadier side, cash was 14.1% of assets, well above the median of 6.2%, and unrealized losses on bonds available for sale were 2.0% of equity, below the median of 5.6%.

## Understanding the score

The bank ranked 6 of 4,313 banks as of 2026-06-30, the 99.9th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers the riskiest 2% of banks.

The five factors that pushed the score up most were troubled loans at 8.1% of loans, the Texas ratio at 74.8%, return on equity (profit as a share of shareholders' money) at -22.6%, brokered deposits at 27.5% of deposits, and interest expense at 2.4% of assets. The five factors that pulled the score down most were the Tier 1 risk-based capital ratio at 9.7%, construction loans at 3.1% of loans, total assets of $972.1 million, loan-loss reserves at 1.0% of loans, and volatile funding at 3.4% of assets.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 55 | 4,589 | ▲ watchlist |
| 2024-12-31 | 12 | 4,560 | ▲ watchlist |
| 2025-03-31 | 31 | 4,536 | ▲ watchlist |
| 2025-06-30 | 111 | 4,494 |  |
| 2025-09-30 | 103 | 4,452 |  |
| 2025-12-31 | 35 | 4,411 | ▲ watchlist |
| 2026-03-31 | 8 | 4,353 | ▲ watchlist |
| 2026-06-30 | 6 | 4,313 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own prior range over the previous 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years; 8 of 28 ratios fell outside that range, and 6 are discussed here. Return on equity was -22.6%, below its prior range of 3.9% to 42.0%, and contributed +0.608 model log-odds units, which pushed the score up. Return on assets was -1.6%, below its prior range of 0.3% to 3.4%, yet it contributed only +0.036 and had little effect on the score. The efficiency ratio (operating costs as a share of revenue) was 146.4%, above its prior range of 49.3% to 110.0%, but its contribution of -0.035 had little effect on the score.

The leverage ratio was 6.7%, below its prior range of 7.8% to 9.8%, and contributed +0.099, which pushed the score up. The Texas ratio was 74.8%, above its prior range of 13.1% to 57.0% after rising +45.6 pp over four quarters, and contributed +0.678, which pushed the score up. Net interest margin (the spread earned on lending and investing) was 3.1%, below its prior range of 3.4% to 4.4%, yet its contribution of -0.055 pushed the score down rather than up.

A year earlier, on 2025-06-30, the bank sat in the 97.6th percentile, and by 2026-06-30, ranked 6 of 4,313, the model rated it riskier than a year earlier.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -22.6% | 3.9% to 42.0% | same quarter, prior 3 years | n/a | -31.2 pp | +0.608 | pushed the score up |
| return on assets (profit as a share of assets) | -1.6% | 0.3% to 3.4% | same quarter, prior 3 years | n/a | -2.3 pp | +0.036 | little effect on the score |
| the efficiency ratio (operating costs as a share of revenue) | 146.4% | 49.3% to 110.0% | same quarter, prior 3 years | n/a | +36.4 pp | -0.035 | little effect on the score |
| the leverage ratio (core capital as a share of average assets) | 6.7% | 7.8% to 9.8% | prior 12 quarters | -1.1 pp | -2.8 pp | +0.099 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 74.8% | 13.1% to 57.0% | prior 12 quarters | +17.8 pp | +45.6 pp | +0.678 | pushed the score up |
| net interest margin (the spread earned on lending and investing) | 3.1% | 3.4% to 4.4% | same quarter, prior 3 years | n/a | -0.2 pp | -0.055 | pushed the score down |

8 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

In hindsight: this bank is an open watchlist case, meaning it was flagged and our data does not yet show a later outcome. The fact sheet contains no data from after the as-of quarter, so there is nothing yet to explain about how the bank's situation developed.

## What happened next

In hindsight: the fact sheet includes no later ranks, flags or reporting status for this bank. Because of that, this memo cannot say whether the bank stayed on the watchlist or whether it is still filing reports.

## Sources

- F1 · Bank name · n/a · Transpecos Banks Ssb · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · TX · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 6 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 9.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 10.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 8.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 74.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -1.6% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 39.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 27.5% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 14.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 8.1%; contribution to the score · 2026-06-30 · +0.900 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 74.8%; contribution to the score · 2026-06-30 · +0.678 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: return on equity (profit as a share of equity), value -22.6%; contribution to the score · 2026-06-30 · +0.608 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver up #4: brokered deposits as a share of deposits, value 27.5%; contribution to the score · 2026-06-30 · +0.587 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2026-06-30 · +0.394 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 9.7%; contribution to the score · 2026-06-30 · -0.777 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: construction loans as a share of loans, value 3.1%; contribution to the score · 2026-06-30 · -0.373 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: total assets, value $972.1 million; contribution to the score · 2026-06-30 · -0.212 · data/analyst/scores.parquet: feature log_total_assets contribution
- F83 · Driver down #4: loan-loss reserves as a share of loans, value 1.0%; contribution to the score · 2026-06-30 · -0.191 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F84 · Driver down #5: volatile funding as a share of assets, value 3.4%; contribution to the score · 2026-06-30 · -0.180 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F85 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -22.6% · data/features/fct_bank_features.parquet: return_on_equity
- F86 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 3.9% · data/features/fct_bank_features.parquet: return_on_equity
- F87 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 42.0% · data/features/fct_bank_features.parquet: return_on_equity
- F89 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · +0.608 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F91 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -1.6% · data/features/fct_bank_features.parquet: return_on_assets
- F92 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F93 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F95 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.036 · data/analyst/scores.parquet: feature return_on_assets contribution
- F96 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature return_on_assets contribution
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 146.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 49.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 110.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.035 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F102 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F103 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F104 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 7.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F105 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 9.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F108 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.099 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F109 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F110 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 74.8% · data/features/fct_bank_features.parquet: texas_ratio
- F111 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 13.1% · data/features/fct_bank_features.parquet: texas_ratio
- F112 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 57.0% · data/features/fct_bank_features.parquet: texas_ratio
- F114 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over four quarters, in percentage points · 2026-06-30 · +45.6 pp · data/features/fct_bank_features.parquet: texas_ratio
- F115 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · +0.678 · data/analyst/scores.parquet: feature texas_ratio contribution
- F116 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F117 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 3.1% · data/features/fct_bank_features.parquet: net_interest_margin
- F118 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.4% · data/features/fct_bank_features.parquet: net_interest_margin
- F119 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 4.4% · data/features/fct_bank_features.parquet: net_interest_margin
- F121 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.055 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F122 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F123 · Trend: ratios outside their own prior range · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F124 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F125 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F126 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F127 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F128 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 97.6% · data/analyst/scores.parquet: percentile
- F129 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
