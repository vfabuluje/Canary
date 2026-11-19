---
cert: 21805
name: "First State Bank Of Dequeen"
as_of: 2026-06-30
rank: 17
n_banks: 4313
percentile: 99.62902851843265
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:08:20"
writer_model: "claude-opus-5-5"
checked: true
---

# First State Bank Of Dequeen (cert 21805)

*Outcome not yet known.*

## Summary

First State Bank Of Dequeen, based in AR, ranked 17 out of 4,313 banks nationally on Canary's score as of 2026-06-30, placing it in the 99.6th percentile, where higher means riskier. It is flagged on Canary's watchlist, which covers the top 2% of banks by score. The biggest upward pushes on its score come from paper losses on bonds available for sale equal to 27.4% of its equity and from brokered deposits (money placed through third-party brokers) making up 24.1% of its deposits. Its capital cushion is thin, with equity at 6.7% of assets against a national median of 10.6%, although it is profitable.

## Warning signs in the data

Capital, the owners' money that absorbs losses, is low: equity was 6.7% of assets as of 2026-06-30, against a national median of 10.6%. The leverage ratio (core capital as a share of average assets) was 8.5%, below the national median of 11.0%. Credit quality is weaker than typical: loans 90 or more days past due or no longer earning interest were 1.2% of loans, against a median of 0.5%. The Texas ratio, which weighs troubled assets against capital plus reserves, was 9.7%, well above the median of 2.9%, though still a modest level.

On funding, brokered deposits were 24.1% of deposits, while the national median is 0.0%. Interest expense ran at 2.7% of assets, above the median of 1.6%, and borrowings from the Federal Home Loan Bank (a lender to banks) were 4.0% of assets against a median of 0.2%. Cash was 2.5% of assets, below the median of 6.2%, while uninsured deposits, which can leave quickly in a scare, were only 4.0% of deposits against a median of 24.8%.

Unrealized losses on bonds available for sale, meaning bonds worth less than the bank paid, equaled 27.4% of equity, far above the median of 5.6%. Securities made up 37.8% of assets, well above the median of 17.6%. On the positive side, return on assets was 1.5% against a median of 1.2%.

## Understanding the score

As of 2026-06-30, the bank ranked 17 out of 4,313 banks, in the 99.6th percentile on a scale of 0 to 100 where higher means riskier. That put it on the watchlist, the top 2% of banks, which held 87 banks that quarter.

The five factors pushing the score up most were: losses on bonds available for sale at 27.4% of equity (+1.634), brokered deposits at 24.1% of deposits (+1.019), the efficiency ratio, or operating costs as a share of revenue, at 53.5% (+0.558), interest expense at 2.7% of assets (+0.329), and deposit growth over the past four quarters of 14.6% (+0.100).

The five factors pulling the score down most were: the Texas ratio at 9.7% (-0.868), the Tier 1 risk-based capital ratio, a regulatory capital measure (-0.562), return on equity at 22.1% (-0.454), loans 90 or more days past due or not accruing interest at 1.2% of loans (-0.295), and nonaccrual assets and foreclosed property at 0.7% of assets (-0.277).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 64 | 4,589 | ▲ watchlist |
| 2024-12-31 | 83 | 4,560 | ▲ watchlist |
| 2025-03-31 | 80 | 4,536 | ▲ watchlist |
| 2025-06-30 | 19 | 4,494 | ▲ watchlist |
| 2025-09-30 | 24 | 4,452 | ▲ watchlist |
| 2025-12-31 | 52 | 4,411 | ▲ watchlist |
| 2026-03-31 | 20 | 4,353 | ▲ watchlist |
| 2026-06-30 | 17 | 4,313 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own prior range, usually the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. As of 2026-06-30, 4 of the 28 ratios checked sat outside their own prior range. The bank was in the 99.6th percentile on 2025-06-30, and the model rates it about the same as a year earlier, now at rank 17 of 4,313.

The efficiency ratio (operating costs as a share of revenue) was 53.5%, below its prior range of 56.1% to 63.5%, after a change of -2.6 pp over four quarters. For the efficiency ratio at 53.5%, the contribution was +0.558 model log-odds units, which pushed the score up. Securities as a share of assets rose to 37.8%, above its prior range of 16.7% to 34.9%, yet its contribution of -0.218 pushed the score down.

Commercial real estate loans were 12.6% of loans, just above their prior range of 10.5% to 12.5%, with a contribution of +0.051 that pushed the score up. Loans 30-89 days past due were 0.29% of assets, below their prior range of 0.32% to 1.3%, and this contribution of -0.244 pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 53.5% | 56.1% to 63.5% | same quarter, prior 3 years | n/a | -2.6 pp | +0.558 | pushed the score up |
| securities as a share of assets | 37.8% | 16.7% to 34.9% | prior 12 quarters | +3.3 pp | +3.2 pp | -0.218 | pushed the score down |
| commercial real estate loans as a share of loans | 12.6% | 10.5% to 12.5% | prior 12 quarters | +0.1 pp | +0.4 pp | +0.051 | pushed the score up |
| loans 30-89 days past due, as a share of assets | 0.29% | 0.32% to 1.3% | prior 12 quarters | -0.1 pp | -0.02 pp | -0.244 | pushed the score down |

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Agricultural Specialization.

Peers: 642 banks in the same specialty group and size tier ($100 million to $1 billion).

Brokered deposits were 24.1% of deposits, in the 96.8th percentile nationally, which is unusually high. Among its peers the bank sits in the 98.8th percentile against a peer median of 0.0%, unusually high among its peers too. Interest expense was 2.7% of assets, in the 96.3rd percentile nationally, which is unusually high. Against peers it is in the 99.3rd percentile with a peer median of 1.6%, unusually high among its peers too.

Equity was 6.7% of assets, in the 4.1st percentile nationally, which is unusually low. Among peers it is in the 3.3rd percentile with a peer median of 10.5%, unusually low among its peers too. The leverage ratio was 8.5%, in the 7.1st percentile nationally, which is unusually low. Among peers it is in the 5.8th percentile with a peer median of 11.0%, unusually low among its peers too.

Uninsured deposits were 4.0% of deposits, in the 1.3rd percentile nationally, which is unusually low. Among peers it is in the 0.4th percentile with a peer median of 22.6%, unusually low among its peers too. Return on equity was 22.1%, in the 93.0th percentile nationally, which is unusually high. Among peers it is in the 93.1st percentile with a peer median of 13.9%, unusually high among its peers too. Overall, 6 of the bank's ratios fall in the national top or bottom 10%, and all 6 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| uninsured deposits as a share of deposits | 4.0% | 1.3rd (unusually low) | 22.6% | 0.4th | unusually low among its peers too |
| brokered deposits as a share of deposits | 24.1% | 96.8th (unusually high) | 0.0% | 98.8th | unusually high among its peers too |
| annualized interest expense as a share of assets | 2.7% | 96.3rd (unusually high) | 1.6% | 99.3rd | unusually high among its peers too |
| equity as a share of assets | 6.7% | 4.1st (unusually low) | 10.5% | 3.3rd | unusually low among its peers too |
| return on equity (profit as a share of equity) | 22.1% | 93.0th (unusually high) | 13.9% | 93.1st | unusually high among its peers too |
| the leverage ratio (core capital as a share of average assets) | 8.5% | 7.1st (unusually low) | 11.0% | 5.8th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 39.7% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 59.8% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 76.7% | 50% or more | yes |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

Hindsight view: this bank's outcome case is that it remains open and on the watchlist. The fact sheet contains no data from after the as-of quarter, so there is no later information to explain or confirm how its situation developed. Its place on the watchlist rests on the as-of picture described above, not on any later event.

## What happened next

Hindsight view: no later quarters, ranks or flags for this bank are included in the fact sheet. Based on its outcome case, the bank is still open and on the watchlist, and later results will show whether its rank moves.

## Sources

- F1 · Bank name · n/a · First State Bank Of Dequeen · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · AR · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 17 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.6% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 9.7% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F43 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 2.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F44 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 24.1% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 27.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F63 · Bank: securities as a share of assets · 2026-06-30 · 37.8% · data/features/fct_bank_features.parquet: securities_to_assets
- F64 · National median: securities as a share of assets · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F71 · Driver up #1: losses on bonds available for sale, as a share of equity, value 27.4%; contribution to the score · 2026-06-30 · +1.634 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F72 · Driver up #2: brokered deposits as a share of deposits, value 24.1%; contribution to the score · 2026-06-30 · +1.019 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F73 · Driver up #3: the efficiency ratio (operating costs as a share of revenue), value 53.5%; contribution to the score · 2026-06-30 · +0.558 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F74 · Driver up #4: annualized interest expense as a share of assets, value 2.7%; contribution to the score · 2026-06-30 · +0.329 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F75 · Driver up #5: deposit growth over the past four quarters, value 14.6%; contribution to the score · 2026-06-30 · +0.100 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F76 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 9.7%; contribution to the score · 2026-06-30 · -0.868 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver down #2: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.562 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F78 · Driver down #3: return on equity (profit as a share of equity), value 22.1%; contribution to the score · 2026-06-30 · -0.454 · data/analyst/scores.parquet: feature return_on_equity contribution
- F79 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 1.2%; contribution to the score · 2026-06-30 · -0.295 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F80 · Driver down #5: nonaccrual assets and foreclosed property, as a share of assets, value 0.7%; contribution to the score · 2026-06-30 · -0.277 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F85 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 53.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F86 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 56.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F87 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 63.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F88 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2026-06-30 · -2.6 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F89 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.558 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F90 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F91 · Trend: securities as a share of assets, value at the as-of quarter · 2026-06-30 · 37.8% · data/features/fct_bank_features.parquet: securities_to_assets
- F92 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 16.7% · data/features/fct_bank_features.parquet: securities_to_assets
- F93 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 34.9% · data/features/fct_bank_features.parquet: securities_to_assets
- F96 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.218 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F97 · Trend: securities as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature securities_to_assets contribution
- F98 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 12.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F99 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 10.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F100 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 12.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F103 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.051 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F104 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F105 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2026-06-30 · 0.29% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F106 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.32% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F107 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 1.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F110 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.244 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F111 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F112 · Trend: ratios outside their own prior range · 2026-06-30 · 4 · data/features/fct_bank_features.parquet
- F114 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F115 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F116 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F117 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 99.6% · data/analyst/scores.parquet: percentile
- F118 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F122 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F123 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 1.3rd · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F124 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F125 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 0.4th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F126 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 22.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F127 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F128 · Peers: brokered deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 24.1% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F129 · Peers: brokered deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.8th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F130 · Peers: brokered deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: brokered_to_deposits
- F131 · Peers: brokered deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 98.8th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F132 · Peers: brokered deposits as a share of deposits, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F133 · Peers: brokered deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: brokered_to_deposits
- F134 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2026-06-30 · 2.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F135 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.3rd · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F136 · Peers: annualized interest expense as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F137 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F138 · Peers: annualized interest expense as a share of assets, peer median · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F139 · Peers: annualized interest expense as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F140 · Peers: equity as a share of assets, bank value at the as-of quarter · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F141 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 4.1st · data/features/fct_bank_features.parquet: equity_to_assets
- F142 · Peers: equity as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F143 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 3.3rd · data/features/fct_bank_features.parquet: equity_to_assets
- F144 · Peers: equity as a share of assets, peer median · 2026-06-30 · 10.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F145 · Peers: equity as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F146 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · 22.1% · data/features/fct_bank_features.parquet: return_on_equity
- F147 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 93.0th · data/features/fct_bank_features.parquet: return_on_equity
- F148 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: return_on_equity
- F149 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 93.1st · data/features/fct_bank_features.parquet: return_on_equity
- F150 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 13.9% · data/features/fct_bank_features.parquet: return_on_equity
- F151 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F152 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 8.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F153 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 7.1st · data/features/fct_bank_features.parquet: leverage_ratio
- F154 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F155 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 5.8th · data/features/fct_bank_features.parquet: leverage_ratio
- F156 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F157 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F159 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F160 · Peers: those ratios also unusual among peers · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F162 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
