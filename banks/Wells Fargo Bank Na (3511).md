---
cert: 3511
name: "Wells Fargo Bank Na"
as_of: 2026-06-30
rank: 1580
n_banks: 4313
percentile: 63.3897519128217
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:55:26"
writer_model: "claude-opus-5-5"
checked: true
---

# Wells Fargo Bank Na (cert 3511)

## Summary

Wells Fargo Bank Na ranked 1,580 out of 4,313 banks nationally as of 2026-06-30, which puts it at the 63.4th percentile on a scale where higher means riskier, and it was not flagged on Canary's watchlist. Its capital ratios were below national medians and below their own recent ranges, and its share of uninsured deposits and its paper losses on bonds were unusually high nationally, though typical for its peer group of large banks. Above-median profits and a modest level of troubled loans against capital pulled the score down and offset much of this. The model rated it riskier than a year earlier.

## Warning signs in the data

Capital, the owners' cushion that absorbs losses, was thinner than at most banks: equity was 8.9% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.0% against a median of 11.0%. The risk-based capital measures, which weigh assets by how risky they are, were also below the median, with the Tier 1 ratio at 12.1% versus 14.6% and the total ratio at 13.5% versus 15.8%.

On credit quality, loans 90 or more days past due or no longer earning interest were 1.0% of loans, above the national median of 0.5%, and net write-offs (loans recorded as lost) were 0.4% of loans against a median of 0.0%. The Texas ratio, which sets troubled assets against capital plus reserves, was 5.8% against a median of 2.9%, while reserves set aside for loan losses were 1.4% of loans, above the 1.2% median.

On funding, uninsured deposits (balances above the government insurance limit) were 50.3% of deposits, well above the national median of 24.8%, and brokered deposits (money placed through middlemen) were 9.7% against a median of 0.0%, though cash was a larger cushion than usual at 10.6% of assets versus 6.2%. Paper losses on bonds held to maturity equaled 19.2% of equity against a national median of 0.0%, while losses on bonds available for sale were 1.8%, below the 5.6% median. The peer section finds these same readings typical for its peer group of similarly large banks, so the national and peer comparisons point different ways.

## Understanding the score

Wells Fargo Bank Na ranked 1,580 out of 4,313 banks as of 2026-06-30, the 63.4th percentile, on a scale where higher means riskier. It was not flagged on the watchlist, which covers 2% of banks; 87 banks were on it that quarter.

The five features that pushed the score up most were the efficiency ratio (operating costs as a share of revenue) at 54.8%, commercial real estate loans at 8.3% of loans, brokered deposits at 9.7% of deposits, loans at 62.9% of deposits, and cash at 10.6% of assets. The five that pulled it down most were the Texas ratio at 5.8%, the Tier 1 risk-based capital ratio at 12.1%, return on equity (profit as a share of equity) at 14.9%, interest expense at 1.4% of assets, and loans 30-89 days past due at 0.2% of assets. The downward pulls were larger in size than the upward ones.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 2,209 | 4,589 |  |
| 2024-12-31 | 2,714 | 4,560 |  |
| 2025-03-31 | 2,969 | 4,536 |  |
| 2025-06-30 | 2,568 | 4,494 |  |
| 2025-09-30 | 2,336 | 4,452 |  |
| 2025-12-31 | 2,078 | 4,411 |  |
| 2026-03-31 | 1,921 | 4,353 |  |
| 2026-06-30 | 1,580 | 4,313 |  |

## How its ratios moved

As of this quarter, the bank ranked 1,580 out of 4,313 banks nationally, placing it at the 63.4th percentile on a scale where higher means riskier. A year earlier it sat at the 42.9th percentile, and the model rated it riskier than a year earlier. Of 30 ratios compared with their own prior range, which for most ratios covers the prior 12 quarters, 18 were outside that range.

The Tier 1 risk-based capital ratio (core capital measured against assets weighted by how risky they are) was 12.1%, below its prior range of 12.3% to 13.3%, yet it pushed the score down, with a contribution of -0.880 model log-odds units (the model's internal scoring units). The total risk-based capital ratio was 13.5%, also below its prior range of 14.1% to 15.3%, and it too pushed the score down, with a contribution of -0.248. The leverage ratio (core capital as a share of average assets) was 8.0%, below its prior range of 8.4% to 8.9%, and it pushed the score up, with a contribution of +0.056. Equity as a share of assets was 8.9%, below its prior range of 9.3% to 10.0%, but it had little effect on the score, with a contribution of +0.001.

The efficiency ratio (operating costs as a share of revenue) was 54.8%, below its prior range of 55.8% to 58.0%, and it pushed the score up, with a contribution of +0.240. Deposit growth over the past four quarters was 11.8%, above its prior range of -5.4% to 6.9%, yet it had little effect on the score, with a contribution of +0.036.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 54.8% | 55.8% to 58.0% | same quarter, prior 3 years | n/a | -1.1 pp | +0.240 | pushed the score up |
| equity as a share of assets | 8.9% | 9.3% to 10.0% | prior 12 quarters | -0.5 pp | -0.9 pp | +0.001 | little effect on the score |
| the total risk-based capital ratio | 13.5% | 14.1% to 15.3% | prior 12 quarters | -0.6 pp | -1.3 pp | -0.248 | pushed the score down |
| deposit growth over the past four quarters | 11.8% | -5.4% to 6.9% | prior 12 quarters | +4.9 pp | +13.5 pp | +0.036 | little effect on the score |
| the leverage ratio (core capital as a share of average assets) | 8.0% | 8.4% to 8.9% | prior 12 quarters | -0.4 pp | -0.9 pp | +0.056 | pushed the score up |
| the Tier 1 risk-based capital ratio | 12.1% | 12.3% to 13.3% | prior 12 quarters | -0.5 pp | -1.2 pp | -0.880 | pushed the score down |

18 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: All Other Over 1 Billion.

This is a general group: the FDIC did not record a lending specialty for this bank.

Peers: 30 banks in the same specialty group and size tier (over $10 billion).

Wells Fargo Bank Na ranks 1,580 out of 4,313 banks nationally on Canary's score as of 2026-06-30. Losses on bonds held to maturity (paper losses on bonds the bank plans to keep until they are repaid), as a share of equity (the owners' cushion), were 19.2%, at the 98.1st percentile nationally, which is unusually high. Among its peers, that ratio sits at the 84.5th percentile against a peer median of 0.7%, which is typical for its peer group. The leverage ratio (core capital as a share of average assets) was 8.0%, at the 3.2nd percentile nationally, which is unusually low. Among its peers, the leverage ratio sits at the 38.3rd percentile against a peer median of 9.2%, which is typical for its peer group.

Uninsured deposits (balances above the government deposit insurance limit) made up 50.3% of deposits, at the 94.4th percentile nationally, which is unusually high. Among its peers, the uninsured deposit share sits at the 69.6th percentile against a peer median of 40.3%, which is typical for its peer group. Annualized loan write-offs (loans recorded as lost, net of later recoveries) were 0.4% of loans, at the 92.0th percentile nationally, which is unusually high. Among its peers, loan write-offs sit at the 58.9th percentile against a peer median of 0.2%, which is typical for its peer group.

Overall, 4 ratios fall in the national top or bottom 10%, and 0 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| losses on bonds held to maturity, as a share of equity | 19.2% | 98.1st (unusually high) | 0.7% | 84.5th | typical for its peer group |
| the leverage ratio (core capital as a share of average assets) | 8.0% | 3.2nd (unusually low) | 9.2% | 38.3rd | typical for its peer group |
| uninsured deposits as a share of deposits | 50.3% | 94.4th (unusually high) | 40.3% | 69.6th | typical for its peer group |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.4% | 92.0th (unusually high) | 0.2% | 58.9th | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 7.7% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 81.8% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -7.3% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

This section looks back in hindsight from after the as-of quarter of 2026-06-30. The fact sheet for this memo contains no data from after the as-of quarter, so later ranks, watchlist flags and whether the bank still reports cannot be described here. The score history table and outcome banner added with this memo show what the later data record.

## Sources

- F1 · Bank name · n/a · Wells Fargo Bank Na · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2026-06-30 · 1,580 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 63.4% · data/analyst/scores.parquet: percentile
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 12.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 13.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 1.4% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 5.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 50.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 9.7% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 19.2% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the efficiency ratio (operating costs as a share of revenue), value 54.8%; contribution to the score · 2026-06-30 · +0.240 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F76 · Driver up #2: commercial real estate loans as a share of loans, value 8.3%; contribution to the score · 2026-06-30 · +0.201 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F77 · Driver up #3: brokered deposits as a share of deposits, value 9.7%; contribution to the score · 2026-06-30 · +0.150 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F78 · Driver up #4: loans as a share of deposits, value 62.9%; contribution to the score · 2026-06-30 · +0.148 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F79 · Driver up #5: cash as a share of assets, value 10.6%; contribution to the score · 2026-06-30 · +0.083 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 5.8%; contribution to the score · 2026-06-30 · -1.073 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 12.1%; contribution to the score · 2026-06-30 · -0.880 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 14.9%; contribution to the score · 2026-06-30 · -0.661 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: annualized interest expense as a share of assets, value 1.4%; contribution to the score · 2026-06-30 · -0.444 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F84 · Driver down #5: loans 30-89 days past due, as a share of assets, value 0.2%; contribution to the score · 2026-06-30 · -0.332 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F89 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 54.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F90 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 55.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F91 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 58.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.240 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F94 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F95 · Trend: equity as a share of assets, value at the as-of quarter · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F96 · Trend: equity as a share of assets, lowest value in the comparison window · n/a · 9.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F97 · Trend: equity as a share of assets, highest value in the comparison window · n/a · 10.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F100 · Trend: equity as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.001 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F101 · Trend: equity as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature equity_to_assets contribution
- F102 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2026-06-30 · 13.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F103 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 14.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F104 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 15.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F107 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2026-06-30 · -0.248 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F108 · Trend: the total risk-based capital ratio, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F109 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2026-06-30 · 11.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F110 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · -5.4% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F111 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 6.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F114 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2026-06-30 · +0.036 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F115 · Trend: deposit growth over the past four quarters, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F116 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F117 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 8.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F118 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 8.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F121 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.056 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F122 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F123 · Trend: the Tier 1 risk-based capital ratio, value at the as-of quarter · 2026-06-30 · 12.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F124 · Trend: the Tier 1 risk-based capital ratio, lowest value in the comparison window · n/a · 12.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F125 · Trend: the Tier 1 risk-based capital ratio, highest value in the comparison window · n/a · 13.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F128 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2026-06-30 · -0.880 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F129 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F130 · Trend: ratios outside their own prior range · 2026-06-30 · 18 · data/features/fct_bank_features.parquet
- F132 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F133 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F135 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 42.9% · data/analyst/scores.parquet: percentile
- F136 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F140 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 19.2% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F141 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.1st · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F142 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F143 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 84.5th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F144 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F145 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F146 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F147 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 3.2nd · data/features/fct_bank_features.parquet: leverage_ratio
- F148 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F149 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 38.3rd · data/features/fct_bank_features.parquet: leverage_ratio
- F150 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 9.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F151 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: leverage_ratio
- F152 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 50.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F153 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 94.4th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F154 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F155 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 69.6th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F156 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 40.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F157 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F158 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F159 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 92.0th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F160 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F161 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 58.9th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F162 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F163 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F165 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 4 · data/features/fct_bank_features.parquet
- F166 · Peers: those ratios also unusual among peers · 2026-06-30 · 0 · data/features/fct_bank_features.parquet
- F168 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
