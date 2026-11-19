---
cert: 11317
name: "Iuka State Bank"
as_of: 2026-06-30
rank: 14
n_banks: 4313
percentile: 99.69858567122652
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:08:19"
writer_model: "claude-opus-5-5"
checked: true
---

# Iuka State Bank (cert 11317)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Iuka State Bank, a small Illinois bank, ranked 14 out of 4,313 banks on Canary's risk score, which puts it in the 99.7th percentile, where higher means riskier. That places it on Canary's watchlist, a group of 87 banks that quarter. The main reasons are troubled loans: 8.0% of its loans were 90 or more days late or no longer paying interest, against a national median of 0.5%. It also relied on brokered deposits (money placed through middlemen) for 20.2% of its deposits, while the typical bank used none (0.0%).

## Warning signs in the data

Capital, the bank's own cushion against losses, was slightly thinner than usual: equity was 9.6% of assets against a national median of 10.6%. Its leverage ratio (core capital as a share of average assets) was 10.3%, a little below the national median of 11.0%.

Credit quality stands out most. Loans 90 or more days past due or not accruing interest (no longer counted as earning) were 8.0% of loans, far above the national median of 0.5%. Nonaccrual assets and foreclosed property made up 6.9% of assets, against a national median of 0.3%. The Texas ratio, which weighs troubled assets against capital plus reserves, was 57.1%, versus a national median of 2.9%. Net loan write-offs (loans given up as lost) ran at 1.8% of loans, against a national median of 0.0%, and the provision for loan losses (money set aside for expected losses) was 1.2% of assets, against 0.1% nationally. Profit was thin, with return on assets of 0.1% against a national median of 1.2%.

On funding, brokered deposits were 20.2% of deposits against a national median of 0.0%, and core deposits (stable everyday deposits) were 63.6% of assets, below the national median of 75.5%. Borrowings from the Federal Home Loan Bank, a lender to banks, were 4.6% of assets against a national median of 0.2%, and loans equalled 94.1% of deposits against 80.2% nationally. Unrealized losses on bonds available for sale (bonds it could sell, now worth less than their cost) equalled 11.0% of equity, about double-digit compared with a national median of 5.6%.

## Understanding the score

As of 2026-06-30 the bank ranked 14 of 4,313 banks nationally, in the 99.7th percentile on a scale where higher means riskier. It is flagged on the watchlist, which covers the top 2% of banks by score, or 87 banks that quarter.

Five features pushed the score up most. The largest was the Texas ratio at 57.1%, adding +0.900. Next came loans 90 or more days past due or not accruing interest at 8.0% of loans, adding +0.844. Losses on bonds available for sale at 11.0% of equity added +0.589. Brokered deposits at 20.2% of deposits added +0.349. The provision for loan losses at 1.2% of assets added +0.145.

Five features pulled the score down. The biggest was the Tier 1 risk-based capital ratio (core capital against risk-weighted assets), at -0.733. Return on equity (profit as a share of equity) at 0.8% contributed -0.369. Construction loans at 1.7% of loans contributed -0.310. The leverage ratio at 10.3% contributed -0.272. Volatile funding at 11.8% of assets contributed -0.178.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 338 | 4,589 |  |
| 2024-12-31 | 212 | 4,560 |  |
| 2025-03-31 | 37 | 4,536 | ▲ watchlist |
| 2025-06-30 | 34 | 4,494 | ▲ watchlist |
| 2025-09-30 | 382 | 4,452 |  |
| 2025-12-31 | 19 | 4,411 | ▲ watchlist |
| 2026-03-31 | 16 | 4,353 | ▲ watchlist |
| 2026-06-30 | 14 | 4,313 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own range over the prior 12 quarters, and for year-to-date ratios with the same quarter in the prior 3 years. Of 28 ratios checked, 14 sat outside their own prior range. The bank ranked 14 nationally as of 2026-06-30, and a year earlier, on 2025-06-30, it was in the 99.3rd percentile, so the model rated it about the same as a year earlier.

Brokered deposits reached 20.2% of deposits, above a prior range of 0.0% to 15.3%, and contributed +0.349, which pushed the score up. That share rose +4.9 pp in the latest quarter and +17.3 pp over four quarters. The provision for loan losses was 1.2% of assets, above its prior range of 0.4% to 0.8%, and contributed +0.145, which pushed the score up.

Return on equity fell to 0.8%, below its prior range of 7.9% to 12.1%, yet its contribution of -0.369 pushed the score down. Return on assets was 0.1%, below its prior range of 0.7% to 1.1%, but its contribution of -0.163 also pushed the score down. The efficiency ratio (operating costs as a share of revenue) rose to 74.4%, above its prior range of 59.0% to 65.6%, yet its contribution of -0.052 pushed the score down. Net loan write-offs reached 1.8% of loans, above their prior range of 0.0% to 0.4%, but at -0.001 they had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 0.8% | 7.9% to 12.1% | same quarter, prior 3 years | n/a | -11.3 pp | -0.369 | pushed the score down |
| annualized loan write-offs, net of recoveries, as a share of loans | 1.8% | 0.0% to 0.4% | same quarter, prior 3 years | n/a | +1.4 pp | -0.001 | little effect on the score |
| the efficiency ratio (operating costs as a share of revenue) | 74.4% | 59.0% to 65.6% | same quarter, prior 3 years | n/a | +8.8 pp | -0.052 | pushed the score down |
| return on assets (profit as a share of assets) | 0.1% | 0.7% to 1.1% | same quarter, prior 3 years | n/a | -1.1 pp | -0.163 | pushed the score down |
| annualized provision for loan losses as a share of assets | 1.2% | 0.4% to 0.8% | same quarter, prior 3 years | n/a | +0.8 pp | +0.145 | pushed the score up |
| brokered deposits as a share of deposits | 20.2% | 0.0% to 15.3% | prior 12 quarters | +4.9 pp | +17.3 pp | +0.349 | pushed the score up |

14 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

The bank ranked 14 nationally as of 2026-06-30. Nonaccrual assets and foreclosed property were 6.9% of assets, in the 99.7th percentile nationally, which is unusually high, and in the 99.5th percentile among peers against a peer median of 0.3%, unusually high among its peers too. The Texas ratio was 57.1%, in the 99.6th percentile nationally, which is unusually high, and in the 99.6th percentile among peers against a peer median of 3.0%, unusually high among its peers too. Loans 90 or more days past due or not accruing interest were 8.0% of loans, in the 99.2nd percentile nationally, which is unusually high, and in the 99.5th percentile among peers against a peer median of 0.4%, unusually high among its peers too. The provision for loan losses was 1.2% of assets, in the 98.6th percentile nationally, which is unusually high, and in the 98.6th percentile among peers against a peer median of 0.1%, unusually high among its peers too.

Net loan write-offs were 1.8% of loans, in the 98.4th percentile nationally, which is unusually high, and in the 98.6th percentile among peers against a peer median of 0.0%, unusually high among its peers too. Loan-loss reserves were 3.0% of loans, in the 97.7th percentile nationally, which is unusually high, and in the 99.0th percentile among peers against a peer median of 1.2%, unusually high among its peers too. Asset growth over the past four quarters was -6.6%, in the 3.2nd percentile nationally, which is unusually low, and in the 3.0th percentile among peers against a peer median of 4.8%, unusually low among its peers too. Brokered deposits were 20.2% of deposits, in the 95.3rd percentile nationally, which is unusually high, and in the 94.7th percentile among peers against a peer median of 0.0%, unusually high among its peers too. Overall, 11 of the bank's ratios fell in the national top or bottom 10%, and 11 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| nonaccrual assets and foreclosed property, as a share of assets | 6.9% | 99.7th (unusually high) | 0.3% | 99.5th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 57.1% | 99.6th (unusually high) | 3.0% | 99.6th | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 8.0% | 99.2nd (unusually high) | 0.4% | 99.5th | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 1.2% | 98.6th (unusually high) | 0.1% | 98.6th | unusually high among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 1.8% | 98.4th (unusually high) | 0.0% | 98.6th | unusually high among its peers too |
| loan-loss reserves as a share of loans | 3.0% | 97.7th (unusually high) | 1.2% | 99.0th | unusually high among its peers too |
| asset growth over the past four quarters | -6.6% | 3.2nd (unusually low) | 4.8% | 3.0th | unusually low among its peers too |
| brokered deposits as a share of deposits | 20.2% | 95.3rd (unusually high) | 0.0% | 94.7th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 10.7% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 28.0% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -58.9% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

Hindsight view: this bank remains an open watchlist case, meaning there is no later outcome to report yet. The fact sheet for this memo contains no data from after the as-of quarter, so it cannot confirm or explain what followed; the reasons the bank sits on the watchlist are the as-of figures described above, chiefly troubled loans and reliance on brokered deposits.

## What happened next

Hindsight view: the fact sheet includes no ranks, watchlist flags or reporting status from after the as-of quarter. Because of that, this memo cannot say whether the bank's rank changed later or whether it is still filing reports; later quarters will show whether its troubled loans and funding mix improve or worsen.

## Sources

- F1 · Bank name · n/a · Iuka State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 14 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 9.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F26 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F27 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F28 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 57.1% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: loans as a share of deposits · 2026-06-30 · 94.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F46 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 20.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F51 · Bank: core deposits as a share of assets · 2026-06-30 · 63.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F52 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 4.6% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 57.1%; contribution to the score · 2026-06-30 · +0.900 · data/analyst/scores.parquet: feature texas_ratio contribution
- F72 · Driver up #2: loans 90+ days past due or not accruing interest, as a share of loans, value 8.0%; contribution to the score · 2026-06-30 · +0.844 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F73 · Driver up #3: losses on bonds available for sale, as a share of equity, value 11.0%; contribution to the score · 2026-06-30 · +0.589 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F74 · Driver up #4: brokered deposits as a share of deposits, value 20.2%; contribution to the score · 2026-06-30 · +0.349 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F75 · Driver up #5: annualized provision for loan losses as a share of assets, value 1.2%; contribution to the score · 2026-06-30 · +0.145 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.733 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: return on equity (profit as a share of equity), value 0.8%; contribution to the score · 2026-06-30 · -0.369 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver down #3: construction loans as a share of loans, value 1.7%; contribution to the score · 2026-06-30 · -0.310 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F79 · Driver down #4: the leverage ratio (core capital as a share of average assets), value 10.3%; contribution to the score · 2026-06-30 · -0.272 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #5: volatile funding as a share of assets, value 11.8%; contribution to the score · 2026-06-30 · -0.178 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F81 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: return_on_equity
- F82 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 7.9% · data/features/fct_bank_features.parquet: return_on_equity
- F83 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 12.1% · data/features/fct_bank_features.parquet: return_on_equity
- F85 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.369 · data/analyst/scores.parquet: feature return_on_equity contribution
- F86 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F87 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F88 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F89 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F91 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.001 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F92 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 74.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F94 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 59.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 65.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.052 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F99 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F100 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F101 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: return_on_assets
- F103 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.163 · data/analyst/scores.parquet: feature return_on_assets contribution
- F104 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F105 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F106 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F107 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F109 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.145 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F110 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F111 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 20.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F112 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F113 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 15.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F114 · Trend: brokered deposits as a share of deposits, change over one quarter, in percentage points · 2026-06-30 · +4.9 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F115 · Trend: brokered deposits as a share of deposits, change over four quarters, in percentage points · 2026-06-30 · +17.3 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F116 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · +0.349 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F117 · Trend: brokered deposits as a share of deposits, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F118 · Trend: ratios outside their own prior range · 2026-06-30 · 14 · data/features/fct_bank_features.parquet
- F120 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F121 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F122 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F123 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 99.3% · data/analyst/scores.parquet: percentile
- F124 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F128 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F129 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F130 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F131 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F132 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F133 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F134 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 57.1% · data/features/fct_bank_features.parquet: texas_ratio
- F135 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.6th · data/features/fct_bank_features.parquet: texas_ratio
- F136 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F137 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 99.6th · data/features/fct_bank_features.parquet: texas_ratio
- F138 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: texas_ratio
- F139 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F140 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F141 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.2nd · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F142 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F143 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F144 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F145 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F146 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F147 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F148 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F149 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F150 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F151 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F152 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F153 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.4th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F154 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F155 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F156 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F157 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F158 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F159 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.7th · data/features/fct_bank_features.parquet: allowance_to_loans
- F160 · Peers: loan-loss reserves as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: allowance_to_loans
- F161 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: allowance_to_loans
- F162 · Peers: loan-loss reserves as a share of loans, peer median · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F163 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F164 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -6.6% · data/features/fct_bank_features.parquet: asset_growth_4q
- F165 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 3.2nd · data/features/fct_bank_features.parquet: asset_growth_4q
- F166 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F167 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 3.0th · data/features/fct_bank_features.parquet: asset_growth_4q
- F168 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F169 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F170 · Peers: brokered deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 20.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F171 · Peers: brokered deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 95.3rd · data/features/fct_bank_features.parquet: brokered_to_deposits
- F172 · Peers: brokered deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: brokered_to_deposits
- F173 · Peers: brokered deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 94.7th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F174 · Peers: brokered deposits as a share of deposits, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F175 · Peers: brokered deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: brokered_to_deposits
- F177 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 11 · data/features/fct_bank_features.parquet
- F178 · Peers: those ratios also unusual among peers · 2026-06-30 · 11 · data/features/fct_bank_features.parquet
- F180 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
