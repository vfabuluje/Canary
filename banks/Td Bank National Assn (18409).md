---
cert: 18409
name: "Td Bank National Assn"
as_of: 2026-06-30
rank: 3068
n_banks: 4313
percentile: 28.889404127057727
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:01"
writer_model: "claude-opus-5-5"
checked: true
---

# Td Bank National Assn (cert 18409)

## Summary

As of 2026-06-30, Td Bank National Assn ranked 3,068 out of 4,313 banks on Canary's score, placing it at the 28.9th percentile, where a higher percentile means higher risk, and it was not flagged on the watchlist. Its risk-based capital ratios, which measure its cushion against its riskier assets, were above the national median, while its troubled loans and loan write-offs ran higher than typical. The most unusual readings were shrinking deposits and assets over the past four quarters, along with a share of uninsured deposits, meaning balances above the government insurance limit, that was well above the national median.

## Warning signs in the data

Equity, the owners' stake in the bank, was 13.3% of assets, above the national median of 10.6%. The leverage ratio, core capital as a share of average assets, was 10.3%, a little below the national median of 11.0%. The Tier 1 risk-based capital ratio was 16.2% and the total risk-based capital ratio was 17.4%, both above the national medians of 14.6% and 15.8%. These two point a different way in the trend section, which finds both ratios below the bank's own prior range, so the capital picture is strong against other banks but weaker than the bank's own recent history.

Loans 90 or more days past due or no longer earning interest were 1.1% of loans, above the national median of 0.5%. Net loan write-offs, loans written off as unlikely to be repaid minus recoveries, ran at an annualized 0.5% of loans against a national median of 0.0%, though the peer section finds this typical for its peer group. Loan-loss reserves, money set aside for expected losses, were 1.7% of loans versus a median of 1.2%, and the Texas ratio, troubled assets against capital plus reserves, was 3.8% against a median of 2.9%.

Uninsured deposits were 37.3% of deposits, well above the national median of 24.8%, and deposits changed by -5.3% over the past four quarters against a median of 4.2%. Federal Home Loan Bank borrowings, a form of secured borrowing from outside the deposit base, were 3.1% of assets versus a national median of 0.2%. Unrealized losses on bonds available for sale were 1.4% of equity, below the national median of 5.6%, and losses on bonds held to maturity were 0.0%, the same as the median.

## Understanding the score

As of 2026-06-30 the bank ranked 3,068 out of 4,313 banks, which is the 28.9th percentile on a 0 to 100 scale where higher means riskier. It was not flagged on the watchlist, which covers 2% of banks, or 87 banks that quarter.

The five factors that pushed the score up the most were loans as a share of deposits at 58.6%, commercial real estate loans as a share of loans at 11.7%, the efficiency ratio (operating costs as a share of revenue) at 66.6%, losses on bonds available for sale at 1.4% of equity, and net loan write-offs at 0.5% of loans. The five factors that pushed the score down the most were the Texas ratio at 3.8%, the Tier 1 risk-based capital ratio at 16.2%, the total risk-based capital ratio at 17.4%, return on equity (profit as a share of equity) at 5.9%, and interest expense at 1.4% of assets. The downward pushes were much larger than the upward ones, which is why the bank sits in the lower part of the national ranking.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 3,166 | 4,589 |  |
| 2024-12-31 | 3,424 | 4,560 |  |
| 2025-03-31 | 3,249 | 4,536 |  |
| 2025-06-30 | 3,194 | 4,494 |  |
| 2025-09-30 | 2,634 | 4,452 |  |
| 2025-12-31 | 2,573 | 4,411 |  |
| 2026-03-31 | 3,333 | 4,353 |  |
| 2026-06-30 | 3,068 | 4,313 |  |

## How its ratios moved

As of 2026-06-30 the bank ranked 3,068 out of 4,313 banks nationally, which puts it at the 28.9th percentile, where a higher percentile means higher risk. Its percentile a year earlier was also 28.9%, and the model rated the bank about the same as a year earlier. The model compares each ratio with that bank's own history, which for most ratios is the prior 12 quarters. Of the 30 ratios compared this way, 9 were outside their own prior range.

The Tier 1 risk-based capital ratio, the bank's core capital cushion measured against its riskier assets, was 16.2%, below its prior range of 16.9% to 18.3%, yet its contribution of -0.963 model log-odds units pushed the score down. The total risk-based capital ratio, a broader capital cushion measure, was 17.4%, also below its prior range of 18.2% to 19.5%, and its contribution of -0.443 still pushed the score down. Uninsured deposits, meaning balances above the government insurance limit, were 37.3% of deposits, above their prior range of 35.0% to 36.6%, but this had little effect on the score, with a contribution of -0.039.

Return on equity, profit as a share of shareholders' money, was 5.9%, above its prior range of 2.7% to 4.7%, and its contribution of -0.396 pushed the score down. Return on assets, profit as a share of everything the bank owns, was 0.8%, above its prior range of 0.3% to 0.5%, and its contribution of -0.241 pushed the score down. Net interest margin, the spread earned on lending and investing, was 3.2%, above its prior range of 2.6% to 2.9%, and its contribution of -0.060 pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the Tier 1 risk-based capital ratio | 16.2% | 16.9% to 18.3% | prior 12 quarters | -2.1 pp | -1.7 pp | -0.963 | pushed the score down |
| the total risk-based capital ratio | 17.4% | 18.2% to 19.5% | prior 12 quarters | -2.1 pp | -1.7 pp | -0.443 | pushed the score down |
| return on equity (profit as a share of equity) | 5.9% | 2.7% to 4.7% | same quarter, prior 3 years | n/a | +1.9 pp | -0.396 | pushed the score down |
| uninsured deposits as a share of deposits | 37.3% | 35.0% to 36.6% | prior 12 quarters | +1.2 pp | +1.0 pp | -0.039 | little effect on the score |
| net interest margin (the spread earned on lending and investing) | 3.2% | 2.6% to 2.9% | same quarter, prior 3 years | n/a | +0.3 pp | -0.060 | pushed the score down |
| return on assets (profit as a share of assets) | 0.8% | 0.3% to 0.5% | same quarter, prior 3 years | n/a | +0.3 pp | -0.241 | pushed the score down |

9 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: All Other Over 1 Billion.

This is a general group: the FDIC did not record a lending specialty for this bank.

Peers: 30 banks in the same specialty group and size tier (over $10 billion).

As of 2026-06-30, Td Bank National Assn ranked 3,068 out of 4,313 banks on Canary's score, which places it at the 28.9th percentile, where higher percentiles mean a higher score. Its deposits, the money customers keep at the bank, changed by -5.3% over the past four quarters, which is at the 6.0th percentile nationally (unusually low) and at the 5.2nd percentile among its peers against a peer median of 6.1%, so it is unusually low among its peers too. Its net loan write-offs, meaning loans written off as unlikely to be repaid minus any amounts later recovered, ran at an annualized 0.5% of loans, at the 93.4th percentile nationally (unusually high), but at the 69.6th percentile among its peers against a peer median of 0.2%, which is typical for its peer group. Its total assets, everything the bank owns including loans and securities, changed by -3.8% over the past four quarters, at the 6.7th percentile nationally (unusually low) and at the 8.3rd percentile among its peers against a peer median of 6.6%, so it is unusually low among its peers too.

Overall, 3 of the bank's ratios fall in the national top or bottom 10%, and 2 of those are also unusual when compared with its peer group, both of them reflecting shrinking deposits and assets rather than loan losses.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| deposit growth over the past four quarters | -5.3% | 6.0th (unusually low) | 6.1% | 5.2nd | unusually low among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.5% | 93.4th (unusually high) | 0.2% | 69.6th | typical for its peer group |
| asset growth over the past four quarters | -3.8% | 6.7th (unusually low) | 6.6% | 8.3rd | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 11.7% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 65.9% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 2.8% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

This is hindsight: the fact sheet for this memo contains no data from after the as-of quarter, so later ranks, watchlist flags and reporting status cannot be described here. The score history table added below this memo is the place to check any later quarters.

## Sources

- F1 · Bank name · n/a · Td Bank National Assn · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2026-06-30 · 3,068 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 28.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 13.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 16.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 17.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 3.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 37.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 3.1% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 1.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2026-06-30 · -3.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -5.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: loans as a share of deposits, value 58.6%; contribution to the score · 2026-06-30 · +0.138 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F76 · Driver up #2: commercial real estate loans as a share of loans, value 11.7%; contribution to the score · 2026-06-30 · +0.105 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F77 · Driver up #3: the efficiency ratio (operating costs as a share of revenue), value 66.6%; contribution to the score · 2026-06-30 · +0.040 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F78 · Driver up #4: losses on bonds available for sale, as a share of equity, value 1.4%; contribution to the score · 2026-06-30 · +0.003 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F79 · Driver up #5: annualized loan write-offs, net of recoveries, as a share of loans, value 0.5%; contribution to the score · 2026-06-30 · +0.002 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 3.8%; contribution to the score · 2026-06-30 · -1.034 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 16.2%; contribution to the score · 2026-06-30 · -0.963 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: the total risk-based capital ratio, value 17.4%; contribution to the score · 2026-06-30 · -0.443 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F83 · Driver down #4: return on equity (profit as a share of equity), value 5.9%; contribution to the score · 2026-06-30 · -0.396 · data/analyst/scores.parquet: feature return_on_equity contribution
- F84 · Driver down #5: annualized interest expense as a share of assets, value 1.4%; contribution to the score · 2026-06-30 · -0.344 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F89 · Trend: the Tier 1 risk-based capital ratio, value at the as-of quarter · 2026-06-30 · 16.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F90 · Trend: the Tier 1 risk-based capital ratio, lowest value in the comparison window · n/a · 16.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F91 · Trend: the Tier 1 risk-based capital ratio, highest value in the comparison window · n/a · 18.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F94 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2026-06-30 · -0.963 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F95 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F96 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2026-06-30 · 17.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F97 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 18.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F98 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 19.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F101 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2026-06-30 · -0.443 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F102 · Trend: the total risk-based capital ratio, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F103 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 5.9% · data/features/fct_bank_features.parquet: return_on_equity
- F104 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 2.7% · data/features/fct_bank_features.parquet: return_on_equity
- F105 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 4.7% · data/features/fct_bank_features.parquet: return_on_equity
- F107 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.396 · data/analyst/scores.parquet: feature return_on_equity contribution
- F108 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F109 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 37.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F110 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 35.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F111 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 36.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F114 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.039 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F115 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F116 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F117 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 2.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F118 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 2.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F120 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.060 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F121 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F122 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: return_on_assets
- F123 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F124 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: return_on_assets
- F126 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.241 · data/analyst/scores.parquet: feature return_on_assets contribution
- F127 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F128 · Trend: ratios outside their own prior range · 2026-06-30 · 9 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F131 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F133 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 28.9% · data/analyst/scores.parquet: percentile
- F134 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F138 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -5.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F139 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 6.0th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F140 · Peers: deposit growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: deposit_growth_4q
- F141 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 5.2nd · data/features/fct_bank_features.parquet: deposit_growth_4q
- F142 · Peers: deposit growth over the past four quarters, peer median · 2026-06-30 · 6.1% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F143 · Peers: deposit growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F144 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F145 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 93.4th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F146 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F147 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 69.6th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F148 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F149 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F150 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -3.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F151 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 6.7th · data/features/fct_bank_features.parquet: asset_growth_4q
- F152 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F153 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 8.3rd · data/features/fct_bank_features.parquet: asset_growth_4q
- F154 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 6.6% · data/features/fct_bank_features.parquet: asset_growth_4q
- F155 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F157 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 3 · data/features/fct_bank_features.parquet
- F158 · Peers: those ratios also unusual among peers · 2026-06-30 · 2 · data/features/fct_bank_features.parquet
- F160 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
