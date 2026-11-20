---
cert: 628
name: "Jpmorgan Chase Bank Na"
as_of: 2026-06-30
rank: 1315
n_banks: 4313
percentile: 69.53396707628102
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:55:11"
writer_model: "claude-opus-5-5"
checked: true
---

# Jpmorgan Chase Bank Na (cert 628)

## Summary

As of 2026-06-30, Jpmorgan Chase Bank Na ranked 1,315 of 4,313 banks nationally on Canary's model, placing it in the 69.5th percentile, where higher means riskier. It was not flagged on Canary's watchlist, which holds about 2% of banks. Its profitability, at a return on assets (profit as a share of assets) of 1.6% against a national median of 1.2%, and its risk-based capital ratios were stronger than typical. Its simple leverage ratio (core capital as a share of average assets) of 7.5% was below the median of 11.0%, and it relied far more than most banks on uninsured deposits, at 49.4% of deposits.

## Warning signs in the data

On capital, the cushion that absorbs losses, the picture was mixed. Equity was 8.3% of assets against a national median of 10.6%, and the leverage ratio was 7.5% against 11.0%, both well below typical. Measured against risk-weighted assets, where riskier holdings count for more, capital looked slightly better than median: the Tier 1 ratio was 15.0% against 14.6%, and the total ratio was 16.2% against 15.8%.

On credit quality, loans 90 or more days past due or no longer earning interest were 0.8% of loans, above the 0.5% median. Annualized write-offs of bad loans, net of recoveries, were 0.6% of loans against a median of 0.0%, while loan-loss reserves (money set aside for expected losses) were 1.7% of loans, above the 1.2% median. Commercial real estate loans were only 3.4% of loans against a median of 23.6%, and the real-estate concentration section found the bank did not cross either regulatory screening line.

Funding is where the bank stood out most: uninsured deposits (balances above the government insurance limit) were 49.4% of deposits against a median of 24.8%, core deposits (steady everyday deposits) were 48.6% of assets against 75.5%, and volatile funding (money that can leave quickly) was 30.3% of assets against 9.0%. The trend section shows uninsured deposits rose above their own prior range, yet the model treated that ratio as pushing the score down, so the two readings point different ways. On bonds, unrealized losses on bonds held to maturity were 5.3% of equity against a median of 0.0%, while losses on bonds available for sale were 0.8% of equity, well below the 5.6% median.

## Understanding the score

As of 2026-06-30, the bank ranked 1,315 of 4,313 banks, in the 69.5th percentile on a scale of 0 to 100 where higher means riskier. It was not among the 87 banks on the watchlist that quarter.

The five features that pushed the score up most were core deposits at 48.6% of assets (+0.421), the efficiency ratio (operating costs as a share of revenue) at 54.4% (+0.138), commercial real estate loans at 3.4% of loans (+0.134), construction loans at 1.2% of loans (+0.111), and losses on bonds available for sale at 0.8% of equity (+0.087). Several of these values are low or better than median, yet in the model's reading they still added to the score.

The five features that pulled the score down most were the Texas ratio (troubled assets against capital plus reserves) at 3.4% (-1.143), the Tier 1 risk-based capital ratio at 15.0% (-0.950), return on equity (profit as a share of equity) at 18.6% (-0.628), the total risk-based capital ratio at 16.2% (-0.478), and annualized interest expense at 1.6% of assets (-0.386). The downward pulls were larger than the upward pushes, which helps explain why the bank sat in the middle-upper part of the ranking rather than near the top.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,248 | 4,589 |  |
| 2024-12-31 | 1,426 | 4,560 |  |
| 2025-03-31 | 1,541 | 4,536 |  |
| 2025-06-30 | 1,454 | 4,494 |  |
| 2025-09-30 | 1,561 | 4,452 |  |
| 2025-12-31 | 1,396 | 4,411 |  |
| 2026-03-31 | 1,375 | 4,353 |  |
| 2026-06-30 | 1,315 | 4,313 |  |

## How its ratios moved

This section compares each ratio with its own history over the prior 12 quarters, and 11 of the 30 ratios checked sat outside that prior range at 2026-06-30. As of that quarter the bank ranked 1,315 of 4,313 banks nationally, placing it in the 69.5th percentile, where higher means riskier. A year earlier, at 2025-06-30, it sat in the 67.7th percentile, so the model rated it riskier than a year earlier.

Uninsured deposits (balances above the government insurance limit) were 49.4% of deposits, above their prior range of 42.8% to 47.2%, after rising +3.2 pp in one quarter and +3.5 pp over four quarters. Even so, at 49.4% this ratio contributed -0.061 model log-odds units and pushed the score down, a contrast with its move outside its range. The leverage ratio (core capital as a share of average assets) was 7.5%, just below its prior range of 7.6% to 8.5%, and its contribution of +0.067 pushed the score up. Core deposits (steady, everyday customer deposits) were 48.6% of assets, below their prior range of 49.2% to 55.9% after a -2.0 pp change over four quarters, and their contribution of +0.421 pushed the score up.

Commercial real estate loans were 3.4% of loans, slightly below their prior range of 3.5% to 4.1%, and their contribution of +0.134 pushed the score up. Net interest margin (the spread earned on lending and investing) was 2.88%, below its prior range of 2.94% to 3.1%, yet its contribution of +0.017 had little effect on the score. The Tier 1 risk-based capital ratio (core capital measured against risk-weighted assets) was 15.0%, below its prior range of 15.1% to 17.3%, but its contribution of -0.950 pushed the score down, the largest pull in that direction among these ratios.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| uninsured deposits as a share of deposits | 49.4% | 42.8% to 47.2% | prior 12 quarters | +3.2 pp | +3.5 pp | -0.061 | pushed the score down |
| the leverage ratio (core capital as a share of average assets) | 7.5% | 7.6% to 8.5% | prior 12 quarters | -0.1 pp | -0.2 pp | +0.067 | pushed the score up |
| core deposits as a share of assets | 48.6% | 49.2% to 55.9% | prior 12 quarters | -0.7 pp | -2.0 pp | +0.421 | pushed the score up |
| commercial real estate loans as a share of loans | 3.4% | 3.5% to 4.1% | prior 12 quarters | -0.1 pp | -0.3 pp | +0.134 | pushed the score up |
| net interest margin (the spread earned on lending and investing) | 2.88% | 2.94% to 3.1% | same quarter, prior 3 years | n/a | -0.1 pp | +0.017 | little effect on the score |
| the Tier 1 risk-based capital ratio | 15.0% | 15.1% to 17.3% | prior 12 quarters | -0.1 pp | -0.5 pp | -0.950 | pushed the score down |

11 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: International Specialization.

There are not enough comparable banks (4 in its specialty group) for a reliable comparison, so none is shown.

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 5.7% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 61.5% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 18.1% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

Hindsight: the fact sheet for this memo contains no data from after the as-of quarter, so later ranks, watchlist flags and reporting status cannot be described here. The outcome banner and score history table added with this note show what followed.

## Sources

- F1 · Bank name · n/a · Jpmorgan Chase Bank Na · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2026-06-30 · 1,315 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 69.5% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 7.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 15.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 49.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 48.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 30.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: core deposits as a share of assets, value 48.6%; contribution to the score · 2026-06-30 · +0.421 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F76 · Driver up #2: the efficiency ratio (operating costs as a share of revenue), value 54.4%; contribution to the score · 2026-06-30 · +0.138 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F77 · Driver up #3: commercial real estate loans as a share of loans, value 3.4%; contribution to the score · 2026-06-30 · +0.134 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F78 · Driver up #4: construction loans as a share of loans, value 1.2%; contribution to the score · 2026-06-30 · +0.111 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F79 · Driver up #5: losses on bonds available for sale, as a share of equity, value 0.8%; contribution to the score · 2026-06-30 · +0.087 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 3.4%; contribution to the score · 2026-06-30 · -1.143 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 15.0%; contribution to the score · 2026-06-30 · -0.950 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 18.6%; contribution to the score · 2026-06-30 · -0.628 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: the total risk-based capital ratio, value 16.2%; contribution to the score · 2026-06-30 · -0.478 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F84 · Driver down #5: annualized interest expense as a share of assets, value 1.6%; contribution to the score · 2026-06-30 · -0.386 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F89 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 49.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F90 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 42.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F91 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 47.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F92 · Trend: uninsured deposits as a share of deposits, change over one quarter, in percentage points · 2026-06-30 · +3.2 pp · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F93 · Trend: uninsured deposits as a share of deposits, change over four quarters, in percentage points · 2026-06-30 · +3.5 pp · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F94 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.061 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F95 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F96 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-06-30 · 7.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F97 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 7.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F98 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 8.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F101 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.067 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F102 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F103 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 48.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F104 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 49.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F105 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 55.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F107 · Trend: core deposits as a share of assets, change over four quarters, in percentage points · 2026-06-30 · -2.0 pp · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F108 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.421 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F109 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F110 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F111 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 3.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F112 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 4.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F115 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.134 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F116 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F117 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 2.88% · data/features/fct_bank_features.parquet: net_interest_margin
- F118 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 2.94% · data/features/fct_bank_features.parquet: net_interest_margin
- F119 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.1% · data/features/fct_bank_features.parquet: net_interest_margin
- F121 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · +0.017 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F122 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F123 · Trend: the Tier 1 risk-based capital ratio, value at the as-of quarter · 2026-06-30 · 15.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F124 · Trend: the Tier 1 risk-based capital ratio, lowest value in the comparison window · n/a · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F125 · Trend: the Tier 1 risk-based capital ratio, highest value in the comparison window · n/a · 17.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F128 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2026-06-30 · -0.950 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F129 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F130 · Trend: ratios outside their own prior range · 2026-06-30 · 11 · data/features/fct_bank_features.parquet
- F132 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F133 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F135 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 67.7% · data/analyst/scores.parquet: percentile
- F136 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
