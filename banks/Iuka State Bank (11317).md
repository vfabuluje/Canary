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
written_at: "2026-11-19T21:16:24"
writer_model: "claude-opus-5-5"
checked: true
---

# Iuka State Bank (cert 11317)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Iuka State Bank, based in IL, ranked 14 out of 4,313 FDIC-insured banks, placing it in the 99.7th percentile, where higher means riskier, and on Canary's watchlist. The main concern is troubled loans: loans seriously past due or no longer earning interest were 8.0% of loans against a national median of 0.5%, and the Texas ratio, which weighs troubled assets against capital plus reserves, was 57.1% against a median of 2.9%. Profits have thinned, the bank leans far more than most on brokered deposits (money placed through outside middlemen), and its capital sits slightly below the national medians.

## Warning signs in the data

Credit quality is the clearest weak spot. Loans seriously past due or no longer earning interest were 8.0% of loans, far above the national median of 0.5%, and nonaccrual assets and foreclosed property were 6.9% of assets against a median of 0.3%. Loans in the early stage of delinquency were 1.5% of assets against a median of 0.2%, and net loan write-offs were 1.8% of loans against a median of 0.0%. The Texas ratio, troubled assets measured against capital plus reserves, was 57.1% against a national median of 2.9%. Pointing the other way, loan-loss reserves (the cushion set aside for bad loans) were 3.0% of loans, well above the median of 1.2%.

Capital, the owners' cushion that absorbs losses, is a little thin: equity was 9.6% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 10.3% against 11.0%. Earnings are weak, with return on assets of 0.1% against a median of 1.2%. Unrealized losses on bonds available for sale equaled 11.0% of equity, about the national median of 5.6% in direction but well above it, while losses on bonds held to maturity were 0.0%, matching the median of 0.0%.

On funding, brokered deposits were 20.2% of deposits against a national median of 0.0%, core deposits (steady customer deposits) were 63.6% of assets against 75.5%, and Federal Home Loan Bank borrowings were 4.6% of assets against 0.2%. Loans were 94.1% of deposits against a median of 80.2%, and cash was 5.4% of assets against 6.2%. Again pointing the other way, uninsured deposits, which can leave quickly in a scare, were only 12.4% of deposits, below the median of 24.8%.

## Understanding the score

Iuka State Bank ranked 14 out of 4,313 banks on 2026-06-30, which is the 99.7th percentile on a 0 to 100 scale where higher means riskier. Its raw model score was 0.5072, a number used mainly to order banks against each other. It is flagged on the watchlist, which holds about 2% of banks; 87 banks were on it that quarter.

The five biggest factors pushing the score up were the Texas ratio at 57.1%, loans seriously past due or not earning interest at 8.0% of loans, losses on bonds available for sale at 11.0% of equity, brokered deposits at 20.2% of deposits, and the provision for loan losses (money set aside for expected bad loans) at 1.2% of assets.

The five biggest factors pushing the score down were the Tier 1 risk-based capital ratio (core capital against risk-weighted assets, value not shown in our data), return on equity at 0.8%, construction loans at 1.7% of loans, the leverage ratio at 10.3%, and volatile funding at 11.8% of assets. The model treated the low return on equity as a point in the bank's favor, even though it sits far below the bank's own past range, as the trend section notes.

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

As of 2026-06-30, Iuka State Bank ranked 14 out of 4,313 banks nationally, which puts it in the 99.7th percentile, where higher means riskier. On 2025-06-30 it sat in the 99.3rd percentile, and the model rates it about the same as a year earlier. Of 28 ratios compared with their own prior range, 14 sat outside it, and the 6 furthest outside are shown here. Most ratios are compared with the bank's own prior 12 quarters, and year-to-date ratios are compared with the same quarter in the prior 3 years.

Brokered deposits are money placed through outside middlemen rather than gathered directly from customers. They made up 20.2% of deposits, above the bank's prior range of 0.0% to 15.3%, and the model's contribution of +0.349 model log-odds units (positive values push the score up) pushed the score up. That share rose +17.3 pp over four quarters, including +4.9 pp in the latest quarter. The provision for loan losses, money set aside for loans expected to go bad, was 1.2% of assets, above its prior range of 0.4% to 0.8%, and its contribution of +0.145 pushed the score up.

Return on equity was 0.8%, well below its prior range of 7.9% to 12.1%, yet its contribution of -0.369 pushed the score down rather than up. Return on assets was 0.1%, below its prior range of 0.7% to 1.1%, but its contribution of -0.163 also pushed the score down. The efficiency ratio was 74.4%, above its prior range of 59.0% to 65.6%, meaning costs took a bigger bite of revenue, but its contribution of -0.052 pushed the score down. Net loan write-offs, loans written off as lost minus amounts recovered, were 1.8% of loans, above their prior range of 0.0% to 0.4%, yet their contribution of -0.001 had little effect on the score.

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

Nonaccrual assets and foreclosed property (loans that have stopped paying interest plus repossessed real estate) were 6.9% of assets, at the 99.7th national percentile, which is unusually high, and at the 99.5th percentile among peers against a peer median of 0.3%, which is unusually high among its peers too. The Texas ratio, which weighs troubled assets against capital plus reserves, was 57.1%, at the 99.6th national percentile, which is unusually high, and at the 99.6th percentile among peers against a peer median of 3.0%, which is unusually high among its peers too. Loans 90 or more days past due or not accruing interest were 8.0% of loans, at the 99.2nd national percentile, which is unusually high, and at the 99.5th percentile among peers against a peer median of 0.4%, which is unusually high among its peers too.

The annualized provision for loan losses (money set aside from earnings to cover expected bad loans) was 1.2% of assets, at the 98.6th national percentile, which is unusually high, and at the 98.6th percentile among peers against a peer median of 0.1%, which is unusually high among its peers too. Annualized loan write-offs net of recoveries (loans written off as lost, minus amounts later recovered) were 1.8% of loans, at the 98.4th national percentile, which is unusually high, and at the 98.6th percentile among peers against a peer median of 0.0%, which is unusually high among its peers too. Loan-loss reserves (the cushion held against future loan losses) were 3.0% of loans, at the 97.7th national percentile, which is unusually high, and at the 99.0th percentile among peers against a peer median of 1.2%, which is unusually high among its peers too.

Asset growth over the past four quarters was -6.6%, at the 3.2nd national percentile, which is unusually low, and at the 3.0th percentile among peers against a peer median of 4.8%, which is unusually low among its peers too. Brokered deposits (deposits placed through outside middlemen rather than gathered directly) were 20.2% of deposits, at the 95.3rd national percentile, which is unusually high, and at the 94.7th percentile among peers against a peer median of 0.0%, which is unusually high among its peers too. Overall, 11 of the bank's ratios fell in the national top or bottom 10%, and all 11 of those were also unusual among its peers.

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

With hindsight: this bank's recorded outcome is that it remains open and on the watchlist. Our fact sheet holds no data from after the as-of quarter, so the reasons it is flagged are the as-of readings above: heavy troubled loans, thin earnings, and growing reliance on brokered deposits.

## What happened next

With hindsight: the fact sheet contains no later ranks, flags or reporting status beyond the as-of quarter. The outcome recorded for this bank is that it is open and on the watchlist, and no failure is recorded in our data. Whether it later stops reporting cannot be told from these facts.

## Sources

- F1 · Bank name · n/a · Iuka State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F5 · Model score · 2026-06-30 · 0.5072 · data/analyst/scores.parquet: score
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
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F25 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F26 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 57.1% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: loans as a share of deposits · 2026-06-30 · 94.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F46 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 12.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 20.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F51 · Bank: core deposits as a share of assets · 2026-06-30 · 63.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F52 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 4.6% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 5.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F59 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F60 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
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
- F119 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
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
