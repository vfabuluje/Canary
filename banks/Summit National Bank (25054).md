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
written_at: "2026-11-19T14:08:19"
writer_model: "claude-opus-5-5"
checked: true
---

# Summit National Bank (cert 25054)

*Outcome not yet known.*

## Summary

Summit National Bank, a Wyoming bank, ranked 11 out of 4,313 banks nationally as of 2026-06-30, placing it in the 99.8th percentile of Canary's risk score. That puts it on the watchlist, the roughly 2% of banks with the highest scores. Its capital cushion was thin, with equity at 2.4% of assets against a national median of 10.6%, and it was losing money, with a return on equity of -101.6%.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was far below typical levels: equity was 2.4% of assets versus a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 2.5% versus 11.0%. The risk-based capital ratios, which weigh assets by how risky they are, were also low, with Tier 1 at 4.8% against a median of 14.6% and total capital at 6.1% against 15.8%. Profitability was weak: return on assets was -2.2% versus a median of 1.2%, and the efficiency ratio (operating costs as a share of revenue) was 233.1% versus 62.1%, meaning costs were well above revenue.

Loan quality looked roughly normal, with loans 90+ days past due or not accruing interest at 0.5%, the same as the national median of 0.5%, though the Texas ratio (troubled assets against capital plus reserves) was 7.3% versus 2.9%, higher mainly because capital was so small. On funding, brokered deposits (money placed through middlemen, which can leave quickly) were 34.4% of deposits against a national median of 0.0%, while uninsured deposits were a low 9.1% versus 24.8%. The bank held a lot of cash, 27.8% of assets versus a median of 6.2%, but it was shrinking, with deposits down -24.2% over the past four quarters against median growth of 4.2%. Unrealized losses on bonds available for sale equaled 17.0% of equity, well above the national median of 5.6%.

## Understanding the score

As of 2026-06-30, Summit National Bank ranked 11 of 4,313 banks, in the 99.8th percentile on a scale where higher means riskier. It was flagged on the watchlist, which covers about 2% of banks, or 87 banks that quarter.

The five factors that pushed the score up most were return on equity at -101.6% (contribution +1.509), the Tier 1 risk-based capital ratio at 4.8% (+1.371), losses on bonds available for sale at 17.0% of equity (+0.545), the total risk-based capital ratio at 6.1% (+0.482), and brokered deposits at 34.4% of deposits (+0.410). The five factors that pulled the score down most were the Texas ratio at 7.3% (contribution -1.172), nonaccrual assets and foreclosed property at 0.2% of assets (-0.755), deposit growth of -24.2% (-0.471), loans 90+ days past due or not accruing at 0.5% (-0.440), and securities at 17.1% of assets (-0.332).

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

Each ratio is compared with its own range over the prior 12 quarters, and 7 of the 30 ratios checked sat outside that range. The bank ranked 11 with a 99.8th percentile, against the 100.0th percentile a year earlier, so the model rated it about the same as a year earlier.

The annualized provision for loan losses (money set aside for expected bad loans) was -0.9% of assets, below its prior range of 0.0% to 0.0%, and it pushed the score up with a contribution of +0.068. Net interest margin fell to 2.2%, below its prior range of 2.6% to 3.8%, yet it had little effect on the score, with a contribution of -0.032. Interest expense rose to 2.5% of assets, above its prior range of 0.3% to 2.1%, and it pushed the score up with a contribution of +0.094. Brokered deposits reached 34.4% of deposits, above their prior range of 0.0% to 32.0%, and they pushed the score up with a contribution of +0.410. That share rose +2.4 pp over one quarter and +4.8 pp over four quarters. Deposit growth was -24.2%, below its prior range of -20.1% to 36.3%, but in contrast it pushed the score down, with a contribution of -0.471. Asset growth was -24.6%, below its prior range of -22.7% to 34.1%, and it pushed the score up with a contribution of +0.078.

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

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: All Other Under 1 Billion.

This is a general group: the FDIC did not record a lending specialty for this bank.

Peers: 77 banks in the same specialty group and size tier (under $100 million).

The bank ranked 11 nationally, in the 99.8th percentile. Its total risk-based capital ratio of 6.1% was in the 0.1st percentile nationally, unusually low, and in the 1.5th percentile among peers with a peer median of 22.0%, unusually low among its peers too. Its Tier 1 risk-based capital ratio of 4.8% was in the 0.1st percentile nationally, unusually low, and in the 1.5th percentile among peers with a peer median of 21.4%, unusually low among its peers too. Its leverage ratio of 2.5% was in the 0.4th percentile nationally, unusually low, and in the 0.6th percentile among peers with a peer median of 12.6%, unusually low among its peers too. Its return on equity of -101.6% was in the 0.1st percentile nationally, unusually low, and in the 0.6th percentile among peers with a peer median of 9.3%, unusually low among its peers too. Its efficiency ratio of 233.1% was in the 99.6th percentile nationally, unusually high, and in the 99.4th percentile among peers with a peer median of 72.0%, unusually high among its peers too.

Its annualized provision for loan losses of -0.9% of assets was in the 0.2nd percentile nationally, unusually low, and in the 0.6th percentile among peers with a peer median of 0.0%, unusually low among its peers too. Its asset growth of -24.6% was in the 0.2nd percentile nationally, unusually low, and in the 0.6th percentile among peers with a peer median of 2.4%, unusually low among its peers too. Its deposit growth of -24.2% was in the 0.4th percentile nationally, unusually low, and in the 0.6th percentile among peers with a peer median of 2.0%, unusually low among its peers too. Overall, 17 of the bank's ratios fell in the national top or bottom 10%, and 14 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the total risk-based capital ratio | 6.1% | 0.1st (unusually low) | 22.0% | 1.5th | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 4.8% | 0.1st (unusually low) | 21.4% | 1.5th | unusually low among its peers too |
| return on equity (profit as a share of equity) | -101.6% | 0.1st (unusually low) | 9.3% | 0.6th | unusually low among its peers too |
| annualized provision for loan losses as a share of assets | -0.9% | 0.2nd (unusually low) | 0.0% | 0.6th | unusually low among its peers too |
| asset growth over the past four quarters | -24.6% | 0.2nd (unusually low) | 2.4% | 0.6th | unusually low among its peers too |
| deposit growth over the past four quarters | -24.2% | 0.4th (unusually low) | 2.0% | 0.6th | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 233.1% | 99.6th (unusually high) | 72.0% | 99.4th | unusually high among its peers too |
| the leverage ratio (core capital as a share of average assets) | 2.5% | 0.4th (unusually low) | 12.6% | 0.6th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 18.7% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 244.7% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 120.8% | 50% or more | yes |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight, this bank is treated as an open bank on the watchlist, meaning the high score has not been resolved one way or the other in our data. The fact sheet contains no data from after the as-of quarter, so there is no hindsight evidence here that confirms or contradicts the model's rating. Its place on the watchlist rests on the as-of picture described above: very thin capital, heavy losses, and a growing reliance on brokered deposits.

## What happened next

Looking back with hindsight, the fact sheet includes no later quarters for this bank, so later ranks, watchlist flags, and reporting status cannot be shown here. If a bank stops filing reports, our data does not distinguish whether it merged or closed.

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
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -24.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
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
- F110 · Trend: brokered deposits as a share of deposits, change over one quarter, in percentage points · 2026-06-30 · +2.4 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
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
- F133 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 100.0% · data/analyst/scores.parquet: percentile
- F134 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F138 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 6.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F139 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F140 · Peers: the total risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F141 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 1.5th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F142 · Peers: the total risk-based capital ratio, peer median · 2026-06-30 · 22.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F143 · Peers: the total risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F144 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F145 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F146 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F147 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 1.5th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F148 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-06-30 · 21.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F149 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F150 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -101.6% · data/features/fct_bank_features.parquet: return_on_equity
- F151 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F152 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F153 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 0.6th · data/features/fct_bank_features.parquet: return_on_equity
- F154 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 9.3% · data/features/fct_bank_features.parquet: return_on_equity
- F155 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F156 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · -0.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F157 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.2nd · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F158 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F159 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 0.6th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F160 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F161 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F162 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -24.6% · data/features/fct_bank_features.parquet: asset_growth_4q
- F163 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.2nd · data/features/fct_bank_features.parquet: asset_growth_4q
- F164 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F165 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 0.6th · data/features/fct_bank_features.parquet: asset_growth_4q
- F166 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 2.4% · data/features/fct_bank_features.parquet: asset_growth_4q
- F167 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F168 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -24.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F169 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.4th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F170 · Peers: deposit growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: deposit_growth_4q
- F171 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 0.6th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F172 · Peers: deposit growth over the past four quarters, peer median · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F173 · Peers: deposit growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F174 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-06-30 · 233.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F175 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.6th · data/features/fct_bank_features.parquet: efficiency_ratio
- F176 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F177 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-06-30 · 99.4th · data/features/fct_bank_features.parquet: efficiency_ratio
- F178 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-06-30 · 72.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F179 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F180 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F181 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.4th · data/features/fct_bank_features.parquet: leverage_ratio
- F182 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F183 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 0.6th · data/features/fct_bank_features.parquet: leverage_ratio
- F184 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 12.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F185 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F187 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 17 · data/features/fct_bank_features.parquet
- F188 · Peers: those ratios also unusual among peers · 2026-06-30 · 14 · data/features/fct_bank_features.parquet
- F190 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
