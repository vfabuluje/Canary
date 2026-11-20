---
cert: 57450
name: "Charles Schwab Bank Ssb"
as_of: 2026-06-30
rank: 3293
n_banks: 4313
percentile: 23.672617667516803
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:18"
writer_model: "claude-opus-5-5"
checked: true
---

# Charles Schwab Bank Ssb (cert 57450)

## Summary

Charles Schwab Bank Ssb, a Texas bank, ranked 3,293 of 4,313 banks nationally on Canary's risk score as of 2026-06-30, placing it at the 23.7th percentile, and it was not flagged on the watchlist. Its Tier 1 risk-based capital ratio (core capital measured against risk-weighted loans and investments) was 30.1%, well above the national median of 14.6%, and its troubled loans were close to zero. The clearest weak spot is its bond portfolio: paper losses on bonds held to maturity equaled 47.0% of equity (the owners' cushion), against a national median of 0.0%. Losses on bonds available for sale, at 19.7% of equity, were the single largest factor pushing its score up.

## Warning signs in the data

Capital gives a mixed picture as of 2026-06-30. Equity as a share of assets was 7.2%, below the national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 10.7%, slightly below the median of 11.0%. Measured against risk-weighted assets, capital looks much stronger: the Tier 1 risk-based ratio was 30.1% and the total risk-based ratio 30.2%, against national medians of 14.6% and 15.8%. The trend section points the other way on that last measure: the total risk-based ratio fell below the bank's own prior range, even though it remains well above the national median.

Credit quality shows little stress: loans 90 or more days past due or not accruing interest were 0.0% of loans, against a median of 0.5%. Loan-loss reserves (money set aside for loans that may not be repaid) were only 0.1% of loans, well below the median of 1.2%, though the bank lends relatively little, with loans at 29.9% of deposits against a median of 80.2%. Funding looks steady: core deposits (everyday customer deposits) were 87.5% of assets against a median of 75.5%, and uninsured deposits (balances above the insurance limit) were 19.0% of deposits against 24.8%; brokered deposits (placed through middlemen) were 3.4%, above the median of 0.0%.

The main concern is bonds, which made up 63.4% of assets against a national median of 17.6%. Paper losses on bonds held to maturity (bonds the bank plans to keep until they repay) equaled 47.0% of equity against a median of 0.0%, and losses on bonds available for sale (bonds it may sell) equaled 19.7% against a median of 5.6%.

## Understanding the score

The bank ranked 3,293 of 4,313 banks as of 2026-06-30, at the 23.7th percentile on a scale where higher means riskier. The watchlist covers the top 2% of banks by score, 87 banks that quarter, and this bank was not flagged.

Five features pushed the score up most: losses on bonds available for sale at 19.7% of equity (contribution +0.808), the efficiency ratio (operating costs as a share of revenue) at 17.6% (+0.089), loans as a share of deposits at 29.9% (+0.084), construction loans at 0.0% of loans (+0.072), and commercial real estate loans at 0.0% of loans (+0.055). Five features pulled it down most: the Tier 1 risk-based capital ratio at 30.1% (contribution -0.964), the Texas ratio (troubled assets against capital plus reserves) at 0.1% (-0.962), interest expense at 0.3% of assets (-0.954), securities at 63.4% of assets (-0.881), and the total risk-based capital ratio at 30.2% (-0.478). The bond-loss driver is by far the largest upward push, but the downward pushes from strong risk-based capital and few troubled assets outweigh it.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 151 | 4,589 |  |
| 2024-12-31 | 450 | 4,560 |  |
| 2025-03-31 | 1,116 | 4,536 |  |
| 2025-06-30 | 2,320 | 4,494 |  |
| 2025-09-30 | 2,996 | 4,452 |  |
| 2025-12-31 | 3,366 | 4,411 |  |
| 2026-03-31 | 3,202 | 4,353 |  |
| 2026-06-30 | 3,293 | 4,313 |  |

## How its ratios moved

This section compares each ratio with the bank's own history: most ratios are checked against the prior 12 quarters, and year-to-date ratios against the same quarter in the prior 3 years. As of 2026-06-30, 15 of the 30 ratios compared sat outside their own prior range, and the table shows the 6 that were furthest outside. The bank ranked 3,293 of 4,313 banks nationally, placing it at the 23.7th percentile of the model's score. A year earlier it stood at the 48.4th percentile, and the model rated it safer than a year earlier.

Net interest margin, the spread the bank earns on lending and investing, was 2.1%, above its prior range of 0.6% to 1.4%, yet it had little effect on the score, contributing -0.001 model log-odds units (the model's internal scoring units, where positive values push the score up). Return on assets, profit as a share of assets, was 1.3%, above its prior range of 0.2% to 0.8%, and it pushed the score down with a contribution of -0.229. Return on equity, profit as a share of the owners' stake, was 18.0%, above its prior range of 3.8% to 13.3% after a +8.0 pp change over four quarters, and it pushed the score down with a contribution of -0.390.

Interest expense, what the bank pays for its funding as an annualized share of assets, was 0.3%, below its prior range of 1.0% to 1.8%, and it pushed the score down with a contribution of -0.954. Asset growth over the past four quarters was 1.3%, above its prior range of -19.3% to -6.7%, and it pushed the score down with a contribution of -0.085. The total risk-based capital ratio, the bank's capital cushion measured against its loans and investments weighted by risk, was 30.2%, below its prior range of 33.6% to 43.4% after a -11.8 pp change over four quarters, yet even though it moved outside its own range it still pushed the score down with a contribution of -0.478.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| net interest margin (the spread earned on lending and investing) | 2.1% | 0.6% to 1.4% | same quarter, prior 3 years | n/a | +0.7 pp | -0.001 | little effect on the score |
| annualized interest expense as a share of assets | 0.3% | 1.0% to 1.8% | same quarter, prior 3 years | n/a | -0.7 pp | -0.954 | pushed the score down |
| asset growth over the past four quarters | 1.3% | -19.3% to -6.7% | prior 12 quarters | +8.0 pp | +10.8 pp | -0.085 | pushed the score down |
| return on assets (profit as a share of assets) | 1.3% | 0.2% to 0.8% | same quarter, prior 3 years | n/a | +0.5 pp | -0.229 | pushed the score down |
| return on equity (profit as a share of equity) | 18.0% | 3.8% to 13.3% | same quarter, prior 3 years | n/a | +8.0 pp | -0.390 | pushed the score down |
| the total risk-based capital ratio | 30.2% | 33.6% to 43.4% | prior 12 quarters | -3.8 pp | -11.8 pp | -0.478 | pushed the score down |

15 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Mortgage Lending Specialization.

Peers: 311 banks in the same specialty group (all sizes), because fewer than 15 shared its size tier.

Losses on bonds held to maturity (the drop in value of bonds the bank plans to keep until they repay, measured against equity, the owners' cushion) stand at 47.0%, at the 99.8th percentile nationally, which is unusually high; among its peers it sits at the 99.2nd percentile against a peer median of 0.0%, which is unusually high among its peers too. Securities (bonds and similar investments) make up 63.4% of assets, at the 98.4th percentile nationally, which is unusually high; among its peers this is the 95.7th percentile against a peer median of 15.9%, which is unusually high among its peers too. Loan-loss reserves (money set aside to cover loans that may not be repaid) equal 0.1% of loans, at the 0.2nd percentile nationally, which is unusually low; among its peers this is the 0.5th percentile against a peer median of 0.8%, which is unusually low among its peers too.

The efficiency ratio (operating costs as a share of revenue) is 17.6%, at the 1.0th percentile nationally, which is unusually low; among its peers this is the 0.8th percentile against a peer median of 76.5%, which is unusually low among its peers too. Commercial real estate loans (loans on offices, shops and similar property) are 0.0% of loans, at the 1.0th percentile nationally, which is unusually low; among its peers this is the 3.5th percentile against a peer median of 7.1%, which is unusually low among its peers too. The net interest margin (the spread earned on lending and investing) is 2.1%, at the 2.7th percentile nationally, which is unusually low; among its peers this is the 9.2nd percentile against a peer median of 3.2%, which is unusually low among its peers too. Annualized interest expense (what the bank pays on deposits and borrowings) is 0.3% of assets, at the 3.2nd percentile nationally, which is unusually low; among its peers this is the 3.4th percentile against a peer median of 1.6%, which is unusually low among its peers too. Core deposits (steady, everyday customer deposits) make up 87.5% of assets, at the 96.6th percentile nationally, which is unusually high; among its peers this is the 95.0th percentile against a peer median of 71.8%, which is unusually high among its peers too.

Overall, 14 of the bank's ratios fall in the national top or bottom 10%, and 11 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| losses on bonds held to maturity, as a share of equity | 47.0% | 99.8th (unusually high) | 0.0% | 99.2nd | unusually high among its peers too |
| loan-loss reserves as a share of loans | 0.1% | 0.2nd (unusually low) | 0.8% | 0.5th | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 17.6% | 1.0th (unusually low) | 76.5% | 0.8th | unusually low among its peers too |
| commercial real estate loans as a share of loans | 0.0% | 1.0th (unusually low) | 7.1% | 3.5th | unusually low among its peers too |
| securities as a share of assets | 63.4% | 98.4th (unusually high) | 15.9% | 95.7th | unusually high among its peers too |
| net interest margin (the spread earned on lending and investing) | 2.1% | 2.7th (unusually low) | 3.2% | 9.2nd | unusually low among its peers too |
| annualized interest expense as a share of assets | 0.3% | 3.2nd (unusually low) | 1.6% | 3.4th | unusually low among its peers too |
| core deposits as a share of assets | 87.5% | 96.6th (unusually high) | 71.8% | 95.0th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 0.8% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -91.5% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

Hindsight: this fact sheet contains no data from after the as-of quarter. So this section cannot report the bank's later ranks or watchlist flags, or whether it still reports to regulators; the outcome banner and score history table added by code show what is known.

## Sources

- F1 · Bank name · n/a · Charles Schwab Bank Ssb · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · TX · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 3,293 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 23.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 30.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 30.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 29.9% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 19.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 87.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 47.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 19.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2026-06-30 · 63.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F75 · Driver up #1: losses on bonds available for sale, as a share of equity, value 19.7%; contribution to the score · 2026-06-30 · +0.808 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F76 · Driver up #2: the efficiency ratio (operating costs as a share of revenue), value 17.6%; contribution to the score · 2026-06-30 · +0.089 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F77 · Driver up #3: loans as a share of deposits, value 29.9%; contribution to the score · 2026-06-30 · +0.084 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F78 · Driver up #4: construction loans as a share of loans, value 0.0%; contribution to the score · 2026-06-30 · +0.072 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F79 · Driver up #5: commercial real estate loans as a share of loans, value 0.0%; contribution to the score · 2026-06-30 · +0.055 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 30.1%; contribution to the score · 2026-06-30 · -0.964 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 0.1%; contribution to the score · 2026-06-30 · -0.962 · data/analyst/scores.parquet: feature texas_ratio contribution
- F82 · Driver down #3: annualized interest expense as a share of assets, value 0.3%; contribution to the score · 2026-06-30 · -0.954 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F83 · Driver down #4: securities as a share of assets, value 63.4%; contribution to the score · 2026-06-30 · -0.881 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F84 · Driver down #5: the total risk-based capital ratio, value 30.2%; contribution to the score · 2026-06-30 · -0.478 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F89 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 2.1% · data/features/fct_bank_features.parquet: net_interest_margin
- F90 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 0.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F91 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: net_interest_margin
- F93 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.001 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F94 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F95 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F96 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F97 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 1.8% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F99 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.954 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F100 · Trend: annualized interest expense as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F101 · Trend: asset growth over the past four quarters, value at the as-of quarter · 2026-06-30 · 1.3% · data/features/fct_bank_features.parquet: asset_growth_4q
- F102 · Trend: asset growth over the past four quarters, lowest value in the comparison window · n/a · -19.3% · data/features/fct_bank_features.parquet: asset_growth_4q
- F103 · Trend: asset growth over the past four quarters, highest value in the comparison window · n/a · -6.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F106 · Trend: asset growth over the past four quarters, contribution to the score (model log-odds units) · 2026-06-30 · -0.085 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F107 · Trend: asset growth over the past four quarters, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F108 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: return_on_assets
- F110 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: return_on_assets
- F112 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.229 · data/analyst/scores.parquet: feature return_on_assets contribution
- F113 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F114 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 18.0% · data/features/fct_bank_features.parquet: return_on_equity
- F115 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 3.8% · data/features/fct_bank_features.parquet: return_on_equity
- F116 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 13.3% · data/features/fct_bank_features.parquet: return_on_equity
- F117 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2026-06-30 · +8.0 pp · data/features/fct_bank_features.parquet: return_on_equity
- F118 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.390 · data/analyst/scores.parquet: feature return_on_equity contribution
- F119 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F120 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2026-06-30 · 30.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F121 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 33.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F122 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 43.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F124 · Trend: the total risk-based capital ratio, change over four quarters, in percentage points · 2026-06-30 · -11.8 pp · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F125 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2026-06-30 · -0.478 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F126 · Trend: the total risk-based capital ratio, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F127 · Trend: ratios outside their own prior range · 2026-06-30 · 15 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F129 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F130 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F131 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F132 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 48.4% · data/analyst/scores.parquet: percentile
- F133 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it safer than a year earlier · data/analyst/scores.parquet: percentile
- F137 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 47.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F138 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F139 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F140 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 99.2nd · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F141 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F142 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F143 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F144 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.2nd · data/features/fct_bank_features.parquet: allowance_to_loans
- F145 · Peers: loan-loss reserves as a share of loans, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: allowance_to_loans
- F146 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 0.5th · data/features/fct_bank_features.parquet: allowance_to_loans
- F147 · Peers: loan-loss reserves as a share of loans, peer median · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: allowance_to_loans
- F148 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F149 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F150 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-06-30 · 1.0th · data/features/fct_bank_features.parquet: efficiency_ratio
- F151 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: efficiency_ratio
- F152 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-06-30 · 0.8th · data/features/fct_bank_features.parquet: efficiency_ratio
- F153 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-06-30 · 76.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F154 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F155 · Peers: commercial real estate loans as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F156 · Peers: commercial real estate loans as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 1.0th · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F157 · Peers: commercial real estate loans as a share of loans, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F158 · Peers: commercial real estate loans as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 3.5th · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F159 · Peers: commercial real estate loans as a share of loans, peer median · 2026-06-30 · 7.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F160 · Peers: commercial real estate loans as a share of loans, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F161 · Peers: securities as a share of assets, bank value at the as-of quarter · 2026-06-30 · 63.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F162 · Peers: securities as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.4th · data/features/fct_bank_features.parquet: securities_to_assets
- F163 · Peers: securities as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: securities_to_assets
- F164 · Peers: securities as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 95.7th · data/features/fct_bank_features.parquet: securities_to_assets
- F165 · Peers: securities as a share of assets, peer median · 2026-06-30 · 15.9% · data/features/fct_bank_features.parquet: securities_to_assets
- F166 · Peers: securities as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: securities_to_assets
- F167 · Peers: net interest margin (the spread earned on lending and investing), bank value at the as-of quarter · 2026-06-30 · 2.1% · data/features/fct_bank_features.parquet: net_interest_margin
- F168 · Peers: net interest margin (the spread earned on lending and investing), national percentile (100 = highest value among all banks) · 2026-06-30 · 2.7th · data/features/fct_bank_features.parquet: net_interest_margin
- F169 · Peers: net interest margin (the spread earned on lending and investing), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: net_interest_margin
- F170 · Peers: net interest margin (the spread earned on lending and investing), percentile among its peers (100 = highest value) · 2026-06-30 · 9.2nd · data/features/fct_bank_features.parquet: net_interest_margin
- F171 · Peers: net interest margin (the spread earned on lending and investing), peer median · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F172 · Peers: net interest margin (the spread earned on lending and investing), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: net_interest_margin
- F173 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F174 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 3.2nd · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F175 · Peers: annualized interest expense as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F176 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 3.4th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F177 · Peers: annualized interest expense as a share of assets, peer median · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F178 · Peers: annualized interest expense as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F179 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2026-06-30 · 87.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F180 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.6th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F181 · Peers: core deposits as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F182 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 95.0th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F183 · Peers: core deposits as a share of assets, peer median · 2026-06-30 · 71.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F184 · Peers: core deposits as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F186 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 14 · data/features/fct_bank_features.parquet
- F187 · Peers: those ratios also unusual among peers · 2026-06-30 · 11 · data/features/fct_bank_features.parquet
- F189 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
