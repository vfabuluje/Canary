---
cert: 1655
name: "Bank Of Old Monroe"
as_of: 2026-06-30
rank: 35
n_banks: 4313
percentile: 99.21168560166937
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:57:27"
writer_model: "claude-opus-5-5"
checked: true
---

# Bank Of Old Monroe (cert 1655)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Bank Of Old Monroe in MO ranked 35 out of 4,313 banks nationally on Canary's score, the 99.2nd percentile, and is flagged on the watchlist. The main concerns are paper losses on bonds it could sell equal to 55.0% of its equity, brokered deposits (money placed through outside middlemen) at 28.5% of deposits, and an owners' stake of only 7.1% of assets. Pulling the other way, almost no loans were seriously overdue at 0.0% of loans, and profits were strong, with return on equity of 23.4%.

## Warning signs in the data

Capital, the owners' cushion against losses, was thin: equity was 7.1% of assets against a national median of 10.6%. The leverage ratio (core capital as a share of average assets) was closer to normal at 10.5%, slightly below the national median of 11.0%. Paper losses on bonds available for sale equaled 55.0% of equity, far above the national median of 5.6%, and securities made up 28.6% of assets against a median of 17.6%.

Funding leaned on less steady sources: brokered deposits were 28.5% of deposits while the national median was 0.0%, and core deposits (steady everyday deposits) were 57.4% of assets against a median of 75.5%. Cash was 2.0% of assets, well below the national median of 6.2%, though uninsured deposits, at 21.0% of deposits, were below the median of 24.8%.

Credit quality points two ways. Loans 90+ days past due or not accruing interest were 0.0% of loans, below the national median of 0.5%, but the bank set aside provisions for loan losses of 0.5% of assets, well above the median of 0.1%. Construction loans were 35.2% of loans against a national median of 5.3%, and the real-estate concentration section finds the bank crossed the regulators' construction screen while staying under the total commercial real estate line.

## Understanding the score

As of 2026-06-30, the bank ranked 35 out of 4,313 banks, the 99.2nd percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which holds about 2% of banks, or 87 banks that quarter.

The five factors that pushed the score up most were losses on bonds available for sale at 55.0% of equity (+1.764), brokered deposits at 28.5% of deposits (+0.923), the efficiency ratio (operating costs as a share of revenue) at 46.6% (+0.393), construction loans at 35.2% of loans (+0.153), and equity at 7.1% of assets (+0.086). The five that pushed it down most were the Texas ratio (troubled assets against capital plus reserves) at 0.0% (-1.249), the Tier 1 risk-based capital ratio, a capital measure whose value is not shown (-0.758), seriously overdue loans at 0.0% of loans (-0.473), return on equity at 23.4% (-0.455), and return on assets at 1.6% (-0.334).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 25 | 4,589 | ▲ watchlist |
| 2024-12-31 | 26 | 4,560 | ▲ watchlist |
| 2025-03-31 | 43 | 4,536 | ▲ watchlist |
| 2025-06-30 | 31 | 4,494 | ▲ watchlist |
| 2025-09-30 | 29 | 4,452 | ▲ watchlist |
| 2025-12-31 | 36 | 4,411 | ▲ watchlist |
| 2026-03-31 | 33 | 4,353 | ▲ watchlist |
| 2026-06-30 | 35 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, the bank ranked 35 out of 4,313 banks nationally, the 99.2nd percentile, where higher means riskier. A year earlier, on 2025-06-30, it sat at the 99.3rd percentile, so the model rated it about the same as a year earlier. To spot unusual moves, each ratio is compared with its own prior range, usually the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios. Of 28 ratios checked, 10 were outside their own prior range, and the table shows the 6 furthest outside it.

The efficiency ratio (operating costs as a share of revenue) was 46.6%, above its prior range of 41.8% to 43.2%, and its contribution of +0.393 model log-odds units pushed the score up. That ratio rose by +4.9 pp over four quarters, meaning costs took a larger share of revenue. Return on equity (profit as a share of the owners' stake) was 23.4%, below its prior range of 39.1% to 62.1%, yet its contribution of -0.455 pushed the score down. Return on assets (profit as a share of assets) was 1.6%, also below its prior range of 2.1% to 2.3%, but its contribution of -0.334 likewise pushed the score down. So although both profit measures fell outside their usual ranges, the model still treated their levels as lowering the score.

The provision for loan losses (money set aside for expected bad loans), at 0.5% of assets, was above its prior range of 0.0% to 0.2%, but its contribution of -0.036 had little effect on the score. Loan-loss reserves (the cushion held against bad loans) were 1.74% of loans, above their prior range of 1.3% to 1.67%, yet their contribution of -0.030 had little effect on the score. Net loan write-offs (loans written off as lost, minus recoveries) were -0.04% of loans, against a prior range of 0.00% to 0.0%, and their contribution of -0.006 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 46.6% | 41.8% to 43.2% | same quarter, prior 3 years | n/a | +4.9 pp | +0.393 | pushed the score up |
| return on equity (profit as a share of equity) | 23.4% | 39.1% to 62.1% | same quarter, prior 3 years | n/a | -16.2 pp | -0.455 | pushed the score down |
| return on assets (profit as a share of assets) | 1.6% | 2.1% to 2.3% | same quarter, prior 3 years | n/a | -0.6 pp | -0.334 | pushed the score down |
| annualized provision for loan losses as a share of assets | 0.5% | 0.0% to 0.2% | same quarter, prior 3 years | n/a | +0.3 pp | -0.036 | little effect on the score |
| loan-loss reserves as a share of loans | 1.74% | 1.3% to 1.67% | prior 12 quarters | +0.3 pp | +0.3 pp | -0.030 | little effect on the score |
| annualized loan write-offs, net of recoveries, as a share of loans | -0.04% | 0.00% to 0.0% | same quarter, prior 3 years | n/a | -0.05 pp | -0.006 | little effect on the score |

10 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

Construction loans, which fund building projects, made up 35.2% of the bank's loans, at the 99.8th percentile nationally, which is unusually high, and at the 99.6th percentile among its peers against a peer median of 8.2%, which is unusually high among its peers too. Brokered deposits, meaning money placed with the bank through outside middlemen, were 28.5% of deposits, at the 97.8th percentile nationally, which is unusually high, and at the 98.0th percentile among its peers against a peer median of 0.0%, which is unusually high among its peers too. Losses on bonds available for sale (paper losses on bonds the bank could sell) equaled 55.0% of equity, at the 96.9th percentile nationally, which is unusually high, and at the 97.3rd percentile among its peers against a peer median of 5.4%, which is unusually high among its peers too.

The annualized provision for loan losses, money set aside for loans that may go bad, was 0.5% of assets, at the 95.7th percentile nationally, which is unusually high, and at the 95.1st percentile among its peers against a peer median of 0.1%, which is unusually high among its peers too. Annualized loan write-offs net of recoveries, meaning loans written off as uncollectable, were 0.0% of loans, at the 4.6th percentile nationally, which is unusually low, and at the 4.2nd percentile among its peers against a peer median of 0.0%, which is unusually low among its peers too. Return on equity, profit as a share of the owners' stake, was 23.4%, at the 94.5th percentile nationally, which is unusually high, and at the 94.9th percentile among its peers against a peer median of 11.7%, which is unusually high among its peers too.

Equity as a share of assets, the owners' cushion against losses, was 7.1%, at the 5.9th percentile nationally, which is unusually low, and at the 5.9th percentile among its peers against a peer median of 10.2%, which is unusually low among its peers too. Core deposits, the steadier everyday deposits from regular customers, were 57.4% of assets, at the 9.6th percentile nationally, which is unusually low, and at the 7.7th percentile among its peers against a peer median of 75.6%, which is unusually low among its peers too. Overall, 8 of the bank's ratios sit in the national top or bottom 10%, and all 8 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| construction loans as a share of loans | 35.2% | 99.8th (unusually high) | 8.2% | 99.6th | unusually high among its peers too |
| brokered deposits as a share of deposits | 28.5% | 97.8th (unusually high) | 0.0% | 98.0th | unusually high among its peers too |
| losses on bonds available for sale, as a share of equity | 55.0% | 96.9th (unusually high) | 5.4% | 97.3rd | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 0.5% | 95.7th (unusually high) | 0.1% | 95.1st | unusually high among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.0% | 4.6th (unusually low) | 0.0% | 4.2nd | unusually low among its peers too |
| return on equity (profit as a share of equity) | 23.4% | 94.5th (unusually high) | 11.7% | 94.9th | unusually high among its peers too |
| equity as a share of assets | 7.1% | 5.9th (unusually low) | 10.2% | 5.9th | unusually low among its peers too |
| core deposits as a share of assets | 57.4% | 9.6th (unusually low) | 75.6% | 7.7th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 195.4% | 100% or more | yes |
| Total commercial real estate loans ÷ capital | 237.9% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 144.1% | 50% or more | yes |

It crossed the construction line (100% or more of capital).
It did not cross the total commercial real estate line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight, this bank's case is an open bank on the watchlist, but the fact sheet contains no data from after the as-of quarter. Without later figures, we cannot say which of the warning signs, if any, grew worse or eased, so the reasons it was flagged remain those described above.

## What happened next

Looking back with hindsight, our data hold no later ranks, watchlist flags, or reporting status for this bank after the as-of quarter. We therefore cannot say whether it stayed on the watchlist or still reports to the FDIC.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · MO · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 35 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.2% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F28 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F29 · Bank: construction loans as a share of loans · 2026-06-30 · 35.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F30 · National median: construction loans as a share of loans · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans (median of all banks)
- F37 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · 23.4% · data/features/fct_bank_features.parquet: return_on_equity
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 21.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 28.5% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F51 · Bank: core deposits as a share of assets · 2026-06-30 · 57.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F52 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 55.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F63 · Bank: securities as a share of assets · 2026-06-30 · 28.6% · data/features/fct_bank_features.parquet: securities_to_assets
- F64 · National median: securities as a share of assets · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F71 · Driver up #1: losses on bonds available for sale, as a share of equity, value 55.0%; contribution to the score · 2026-06-30 · +1.764 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F72 · Driver up #2: brokered deposits as a share of deposits, value 28.5%; contribution to the score · 2026-06-30 · +0.923 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F73 · Driver up #3: the efficiency ratio (operating costs as a share of revenue), value 46.6%; contribution to the score · 2026-06-30 · +0.393 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F74 · Driver up #4: construction loans as a share of loans, value 35.2%; contribution to the score · 2026-06-30 · +0.153 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F75 · Driver up #5: equity as a share of assets, value 7.1%; contribution to the score · 2026-06-30 · +0.086 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F76 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 0.0%; contribution to the score · 2026-06-30 · -1.249 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver down #2: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.758 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F78 · Driver down #3: loans 90+ days past due or not accruing interest, as a share of loans, value 0.0%; contribution to the score · 2026-06-30 · -0.473 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver down #4: return on equity (profit as a share of equity), value 23.4%; contribution to the score · 2026-06-30 · -0.455 · data/analyst/scores.parquet: feature return_on_equity contribution
- F80 · Driver down #5: return on assets (profit as a share of assets), value 1.6%; contribution to the score · 2026-06-30 · -0.334 · data/analyst/scores.parquet: feature return_on_assets contribution
- F85 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 46.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F86 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 41.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F87 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 43.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F88 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2026-06-30 · +4.9 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F89 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.393 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F90 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F91 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 23.4% · data/features/fct_bank_features.parquet: return_on_equity
- F92 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 39.1% · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 62.1% · data/features/fct_bank_features.parquet: return_on_equity
- F95 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.455 · data/analyst/scores.parquet: feature return_on_equity contribution
- F96 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F97 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: return_on_assets
- F98 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 2.1% · data/features/fct_bank_features.parquet: return_on_assets
- F99 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 2.3% · data/features/fct_bank_features.parquet: return_on_assets
- F101 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.334 · data/analyst/scores.parquet: feature return_on_assets contribution
- F102 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F103 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F104 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F105 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F107 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.036 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F108 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F109 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2026-06-30 · 1.74% · data/features/fct_bank_features.parquet: allowance_to_loans
- F110 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 1.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F111 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 1.67% · data/features/fct_bank_features.parquet: allowance_to_loans
- F114 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.030 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F115 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F116 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · -0.04% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F117 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.00% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F118 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F120 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.006 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F121 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F122 · Trend: ratios outside their own prior range · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F123 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F124 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F125 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F126 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F127 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 99.3% · data/analyst/scores.parquet: percentile
- F128 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F132 · Peers: construction loans as a share of loans, bank value at the as-of quarter · 2026-06-30 · 35.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F133 · Peers: construction loans as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F134 · Peers: construction loans as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F135 · Peers: construction loans as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.6th · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F136 · Peers: construction loans as a share of loans, peer median · 2026-06-30 · 8.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F137 · Peers: construction loans as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F138 · Peers: brokered deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 28.5% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F139 · Peers: brokered deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.8th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F140 · Peers: brokered deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: brokered_to_deposits
- F141 · Peers: brokered deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 98.0th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F142 · Peers: brokered deposits as a share of deposits, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F143 · Peers: brokered deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: brokered_to_deposits
- F144 · Peers: losses on bonds available for sale, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 55.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F145 · Peers: losses on bonds available for sale, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.9th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F146 · Peers: losses on bonds available for sale, as a share of equity, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F147 · Peers: losses on bonds available for sale, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 97.3rd · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F148 · Peers: losses on bonds available for sale, as a share of equity, peer median · 2026-06-30 · 5.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F149 · Peers: losses on bonds available for sale, as a share of equity, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F150 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F151 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 95.7th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F152 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F153 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 95.1st · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F154 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F155 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F156 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F157 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 4.6th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F158 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F159 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 4.2nd · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F160 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F161 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F162 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · 23.4% · data/features/fct_bank_features.parquet: return_on_equity
- F163 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 94.5th · data/features/fct_bank_features.parquet: return_on_equity
- F164 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: return_on_equity
- F165 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 94.9th · data/features/fct_bank_features.parquet: return_on_equity
- F166 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 11.7% · data/features/fct_bank_features.parquet: return_on_equity
- F167 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F168 · Peers: equity as a share of assets, bank value at the as-of quarter · 2026-06-30 · 7.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F169 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 5.9th · data/features/fct_bank_features.parquet: equity_to_assets
- F170 · Peers: equity as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F171 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 5.9th · data/features/fct_bank_features.parquet: equity_to_assets
- F172 · Peers: equity as a share of assets, peer median · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F173 · Peers: equity as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F174 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2026-06-30 · 57.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F175 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 9.6th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F176 · Peers: core deposits as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F177 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 7.7th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F178 · Peers: core deposits as a share of assets, peer median · 2026-06-30 · 75.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F179 · Peers: core deposits as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F181 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F182 · Peers: those ratios also unusual among peers · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F184 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
