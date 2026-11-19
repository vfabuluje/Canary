---
cert: 4134
name: "First Nb Of Lindsay"
as_of: 2024-09-30
rank: 9
n_banks: 4589
percentile: 99.82567008062759
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2024-10-18
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:04:45"
writer_model: "claude-opus-5-5"
checked: true
---

# First Nb Of Lindsay (cert 4134)

*Hindsight: failed 2024-10-18. Canary flagged it 1 quarter ahead.*

## Summary

As of 2024-09-30, First Nb Of Lindsay, a bank in OK, ranked 9 out of 4,589 FDIC-insured banks on Canary's risk score, placing it in the 99.8th percentile. It was flagged on Canary's watchlist, which covers the riskiest 2% of banks, or 92 banks that quarter. The standout issue was troubled loans: its Texas ratio (troubled assets measured against capital plus reserves) was 133.7% against a national median of 2.2%, and 10.6% of its loans were 90 or more days past due or not accruing interest, against a national median of 0.4%.

## Warning signs in the data

Capital, the cushion that absorbs losses, looked roughly normal: equity was 11.1% of assets against a national median of 10.0%, and the leverage ratio (core capital as a share of average assets) was 10.0% against a median of 10.7%. Credit quality was far weaker than at a typical bank. Loans 90 or more days past due or not accruing interest were 10.6% of loans versus a national median of 0.4%. Loans that were recently past due, late but not yet seriously so, were 10.4% of assets versus a national median of 0.2%. Net loan write-offs (loans written off as lost, less recoveries) ran at an annualized 20.6% of loans against a median of 0.0%, and loan-loss reserves, money set aside for expected bad loans, showed an unusual negative reading of -11.2% of loans against a median of 1.2%. Together these pushed the Texas ratio to 133.7%, far above the national median of 2.2%.

Earnings were also weak: return on assets was -0.7% against a median of 0.9%, and the efficiency ratio (operating costs as a share of revenue) was 126.6% against a median of 67.8%, meaning costs exceeded revenue. Funding and liquidity looked steadier: core deposits, the stable everyday deposit base, were 83.6% of assets versus a median of 75.0%, cash was 21.4% of assets versus 6.2%, and brokered deposits were 0.0% of deposits. Uninsured deposits, those above the federal insurance limit, showed a reported value of -1.6% of deposits against a national median of 23.6%. Unrealized losses on bonds were small: losses on bonds available for sale were 0.1% of equity, well below the national median of 8.5%, and losses on bonds held to maturity were 0.0%.

## Understanding the score

First Nb Of Lindsay ranked 9 out of 4,589 banks as of 2024-09-30, which places it in the 99.8th percentile on a scale where higher means riskier. Its raw model score was 0.4977, and it was flagged on the watchlist, which holds the top 2% of banks, 92 banks that quarter.

Five factors pushed the score up most. The largest was the Texas ratio at 133.7%, adding +1.563, followed by loans 90 or more days past due or not accruing interest at 10.6% of loans, adding +1.261. Next came recently past-due loans at 10.4% of assets, adding +0.296; losses on bonds available for sale at 0.1% of equity, adding +0.104; and deposit growth over the past four quarters of 17.8%, adding +0.097.

Five factors pulled the score down most. The Tier 1 risk-based capital ratio, a measure of core capital against risk-weighted assets whose value is not listed here, contributed -0.670, and return on equity of -6.9% contributed -0.526. Construction loans at 3.9% of loans contributed -0.461, nonaccrual assets and foreclosed property at 0.9% of assets contributed -0.254, and loan-loss reserves at -11.2% of loans contributed -0.251.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2022-12-31 | 2,776 | 4,773 |  |
| 2023-03-31 | 1,256 | 4,740 |  |
| 2023-06-30 | 1,082 | 4,714 |  |
| 2023-09-30 | 2,298 | 4,686 |  |
| 2023-12-31 | 2,335 | 4,658 |  |
| 2024-03-31 | 799 | 4,640 |  |
| 2024-06-30 | 573 | 4,610 |  |
| 2024-09-30 | 9 | 4,589 | ▲ watchlist (first flag) |

## How its ratios moved

Each ratio is compared with its own range over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years, and 17 of the 28 ratios checked sat outside that range at 2024-09-30. The Texas ratio reached 133.7%, far above its prior range of 10.3% to 14.9% after a one-quarter jump of +120.9 pp, and contributed +1.563 model log-odds units, which pushed the score up. Loans 90 or more days past due or not accruing interest rose to 10.6% of loans, above a prior range of 1.7% to 2.8% after a one-quarter rise of +8.6 pp, and contributed +1.261, which pushed the score up.

Several other ratios moved far outside their range yet did not raise the score. Net loan write-offs reached 20.6% of loans against a prior range of 0.0% to 0.1%, yet contributed only -0.005, little effect on the score. Loan-loss reserves fell to -11.2% of loans, below a prior range of 2.8% to 3.6% after a one-quarter drop of -14.8 pp, yet contributed -0.251, which pushed the score down. The efficiency ratio climbed to 126.6%, well above its prior range of 42.3% to 50.5%, yet contributed -0.062, which pushed the score down. Return on equity fell to -6.9%, below its prior range of 14.6% to 18.0%, yet contributed -0.526, which pushed the score down.

Overall, the model rated it riskier than a year earlier: the bank stood in the 51.0th percentile at 2023-09-30 and in the 99.8th percentile at 2024-09-30.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 133.7% | 10.3% to 14.9% | prior 12 quarters | +120.9 pp | +121.8 pp | +1.563 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 20.6% | 0.0% to 0.1% | same quarter, prior 3 years | n/a | +20.5 pp | -0.005 | little effect on the score |
| loan-loss reserves as a share of loans | -11.2% | 2.8% to 3.6% | prior 12 quarters | -14.8 pp | -14.7 pp | -0.251 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 126.6% | 42.3% to 50.5% | same quarter, prior 3 years | n/a | +76.1 pp | -0.062 | pushed the score down |
| loans 90+ days past due or not accruing interest, as a share of loans | 10.6% | 1.7% to 2.8% | prior 12 quarters | +8.6 pp | +8.5 pp | +1.261 | pushed the score up |
| return on equity (profit as a share of equity) | -6.9% | 14.6% to 18.0% | same quarter, prior 3 years | n/a | -21.5 pp | -0.526 | pushed the score down |

17 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2024-09-30: Commercial Lending Specialization.

Peers: 1533 banks in the same specialty group and size tier ($100 million to $1 billion).

The Texas ratio of 133.7% sat at the 100.0th percentile nationally, unusually high, and at the 100.0th percentile among peers against a peer median of 2.1%, unusually high among its peers too. Loans 90 or more days past due or not accruing interest at 10.6% of loans sat at the 99.7th percentile nationally, unusually high, and at the 99.9th percentile among peers against a peer median of 0.3%, unusually high among its peers too. Recently past-due loans at 10.4% of assets sat at the 100.0th percentile nationally, unusually high, and at the 100.0th percentile among peers against a peer median of 0.2%, unusually high among its peers too. Net loan write-offs at 20.6% of loans sat at the 100.0th percentile nationally, unusually high, and at the 100.0th percentile among peers against a peer median of 0.0%, unusually high among its peers too.

Loan-loss reserves at -11.2% of loans sat at the 0.0th percentile nationally, unusually low, and at the 0.0th percentile among peers against a peer median of 1.2%, unusually low among its peers too. The efficiency ratio of 126.6% sat at the 98.1st percentile nationally, unusually high, and at the 99.0th percentile among peers against a peer median of 69.0%, unusually high among its peers too. Return on equity of -6.9% sat at the 2.2nd percentile nationally, unusually low, and at the 1.3rd percentile among peers against a peer median of 10.0%, unusually low among its peers too. Uninsured deposits at a reported -1.6% of deposits sat at the 0.0th percentile nationally, unusually low, and at the 0.0th percentile among peers against a peer median of 24.7%, unusually low among its peers too.

Overall, 12 of the bank's ratios fell in the national top or bottom 10%, and 11 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 133.7% | 100.0th (unusually high) | 2.1% | 100.0th | unusually high among its peers too |
| uninsured deposits as a share of deposits | -1.6% | 0.0th (unusually low) | 24.7% | 0.0th | unusually low among its peers too |
| loan-loss reserves as a share of loans | -11.2% | 0.0th (unusually low) | 1.2% | 0.0th | unusually low among its peers too |
| loans 30-89 days past due, as a share of assets | 10.4% | 100.0th (unusually high) | 0.2% | 100.0th | unusually high among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 20.6% | 100.0th (unusually high) | 0.0% | 100.0th | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 10.6% | 99.7th (unusually high) | 0.3% | 99.9th | unusually high among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 126.6% | 98.1st (unusually high) | 69.0% | 99.0th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -6.9% | 2.2nd (unusually low) | 10.0% | 1.3rd | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 68.4% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 163.3% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -28.3% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, Canary first flagged First Nb Of Lindsay at 2024-09-30, which was also the last quarter the bank reported. The bank failed on 2024-10-18, giving a lead time of 1 quarter between the first flag and the failure. The flag came late but before the failure, so this counts as a case the model caught, with little time to spare.

## What happened next

In hindsight, the bank failed on 2024-10-18, shortly after the as-of quarter. Its last report was for 2024-09-30, so there are no later ranks or flags to show.

## Sources

- F1 · Bank name · n/a · First Nb Of Lindsay · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2024-09-30 · 2024-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · OK · data/raw/financials: STALP
- F5 · Model score · 2024-09-30 · 0.4977 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2024-09-30 · 9 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2024-09-30 · 4,589 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2024-09-30 · 99.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2024-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2024-09-30 · 92 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2024-09-30 · 11.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2024-09-30 · 10.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2024-09-30 · 10.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2024-09-30 · 10.7% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2024-09-30 · 10.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2024-09-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2024-09-30 · 10.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2024-09-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2024-09-30 · -11.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2024-09-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F25 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2024-09-30 · 20.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F26 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2024-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2024-09-30 · 133.7% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2024-09-30 · 2.2% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2024-09-30 · -0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2024-09-30 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2024-09-30 · 126.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F42 · National median: the efficiency ratio (operating costs as a share of revenue) · 2024-09-30 · 67.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2024-09-30 · -1.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2024-09-30 · 23.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2024-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F51 · Bank: core deposits as a share of assets · 2024-09-30 · 83.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F52 · National median: core deposits as a share of assets · 2024-09-30 · 75.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2024-09-30 · 21.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2024-09-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F59 · Bank: losses on bonds held to maturity, as a share of equity · 2024-09-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2024-09-30 · 0.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2024-09-30 · 8.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 133.7%; contribution to the score · 2024-09-30 · +1.563 · data/analyst/scores.parquet: feature texas_ratio contribution
- F72 · Driver up #2: loans 90+ days past due or not accruing interest, as a share of loans, value 10.6%; contribution to the score · 2024-09-30 · +1.261 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F73 · Driver up #3: loans 30-89 days past due, as a share of assets, value 10.4%; contribution to the score · 2024-09-30 · +0.296 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F74 · Driver up #4: losses on bonds available for sale, as a share of equity, value 0.1%; contribution to the score · 2024-09-30 · +0.104 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F75 · Driver up #5: deposit growth over the past four quarters, value 17.8%; contribution to the score · 2024-09-30 · +0.097 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2024-09-30 · -0.670 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: return on equity (profit as a share of equity), value -6.9%; contribution to the score · 2024-09-30 · -0.526 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver down #3: construction loans as a share of loans, value 3.9%; contribution to the score · 2024-09-30 · -0.461 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F79 · Driver down #4: nonaccrual assets and foreclosed property, as a share of assets, value 0.9%; contribution to the score · 2024-09-30 · -0.254 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F80 · Driver down #5: loan-loss reserves as a share of loans, value -11.2%; contribution to the score · 2024-09-30 · -0.251 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F81 · Failure date · 2024-10-18 · 2024-10-18 · data/raw/failures: FAILDATE
- F82 · First flag quarter (Phase 3 lead-time rule) · 2024-09-30 · 2024-09-30 · data/analyst/scores.parquet: flagged
- F83 · Lead time in quarters before failure · n/a · 1 · data/analyst/scores.parquet: quarters_until_failure
- F84 · Last quarter the bank reported · 2024-09-30 · 2024-09-30 · data/features/fct_bank_features.parquet: report_date
- F85 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2024-09-30 · 133.7% · data/features/fct_bank_features.parquet: texas_ratio
- F86 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 10.3% · data/features/fct_bank_features.parquet: texas_ratio
- F87 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 14.9% · data/features/fct_bank_features.parquet: texas_ratio
- F88 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2024-09-30 · +120.9 pp · data/features/fct_bank_features.parquet: texas_ratio
- F90 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2024-09-30 · +1.563 · data/analyst/scores.parquet: feature texas_ratio contribution
- F91 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2024-09-30 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F92 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2024-09-30 · 20.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F93 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F94 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F96 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2024-09-30 · -0.005 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F97 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2024-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F98 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2024-09-30 · -11.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F99 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 2.8% · data/features/fct_bank_features.parquet: allowance_to_loans
- F100 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 3.6% · data/features/fct_bank_features.parquet: allowance_to_loans
- F101 · Trend: loan-loss reserves as a share of loans, change over one quarter, in percentage points · 2024-09-30 · -14.8 pp · data/features/fct_bank_features.parquet: allowance_to_loans
- F103 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2024-09-30 · -0.251 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F104 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2024-09-30 · pushed the score down · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2024-09-30 · 126.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 42.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 50.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F109 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2024-09-30 · -0.062 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2024-09-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F111 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2024-09-30 · 10.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F112 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 1.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F113 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 2.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F114 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, change over one quarter, in percentage points · 2024-09-30 · +8.6 pp · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F116 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2024-09-30 · +1.261 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F117 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2024-09-30 · pushed the score up · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F118 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2024-09-30 · -6.9% · data/features/fct_bank_features.parquet: return_on_equity
- F119 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 14.6% · data/features/fct_bank_features.parquet: return_on_equity
- F120 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 18.0% · data/features/fct_bank_features.parquet: return_on_equity
- F122 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2024-09-30 · -0.526 · data/analyst/scores.parquet: feature return_on_equity contribution
- F123 · Trend: return on equity (profit as a share of equity), what the model did with it · 2024-09-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F124 · Trend: ratios outside their own prior range · 2024-09-30 · 17 · data/features/fct_bank_features.parquet
- F126 · Trend: ratios compared with their own prior range · 2024-09-30 · 28 · data/features/fct_bank_features.parquet
- F127 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F128 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F129 · Percentile a year earlier (100 = highest risk) · 2023-09-30 · 51.0% · data/analyst/scores.parquet: percentile
- F130 · Trend: how the model's rating compares with a year earlier · 2024-09-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F134 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2024-09-30 · 133.7% · data/features/fct_bank_features.parquet: texas_ratio
- F135 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2024-09-30 · 100.0th · data/features/fct_bank_features.parquet: texas_ratio
- F136 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2024-09-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F137 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2024-09-30 · 100.0th · data/features/fct_bank_features.parquet: texas_ratio
- F138 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2024-09-30 · 2.1% · data/features/fct_bank_features.parquet: texas_ratio
- F139 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2024-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F140 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2024-09-30 · -1.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F141 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2024-09-30 · 0.0th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F142 · Peers: uninsured deposits as a share of deposits, national reading · 2024-09-30 · unusually low · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F143 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2024-09-30 · 0.0th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F144 · Peers: uninsured deposits as a share of deposits, peer median · 2024-09-30 · 24.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F145 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2024-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F146 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2024-09-30 · -11.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F147 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2024-09-30 · 0.0th · data/features/fct_bank_features.parquet: allowance_to_loans
- F148 · Peers: loan-loss reserves as a share of loans, national reading · 2024-09-30 · unusually low · data/features/fct_bank_features.parquet: allowance_to_loans
- F149 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2024-09-30 · 0.0th · data/features/fct_bank_features.parquet: allowance_to_loans
- F150 · Peers: loan-loss reserves as a share of loans, peer median · 2024-09-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F151 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2024-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F152 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2024-09-30 · 10.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F153 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2024-09-30 · 100.0th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F154 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2024-09-30 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F155 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2024-09-30 · 100.0th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F156 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2024-09-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F157 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2024-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F158 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2024-09-30 · 20.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F159 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2024-09-30 · 100.0th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F160 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2024-09-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F161 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2024-09-30 · 100.0th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F162 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2024-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F163 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2024-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F164 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2024-09-30 · 10.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F165 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2024-09-30 · 99.7th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F166 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2024-09-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F167 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2024-09-30 · 99.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F168 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2024-09-30 · 0.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F169 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2024-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F170 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2024-09-30 · 126.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F171 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2024-09-30 · 98.1st · data/features/fct_bank_features.parquet: efficiency_ratio
- F172 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2024-09-30 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F173 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2024-09-30 · 99.0th · data/features/fct_bank_features.parquet: efficiency_ratio
- F174 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2024-09-30 · 69.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F175 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2024-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F176 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2024-09-30 · -6.9% · data/features/fct_bank_features.parquet: return_on_equity
- F177 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2024-09-30 · 2.2nd · data/features/fct_bank_features.parquet: return_on_equity
- F178 · Peers: return on equity (profit as a share of equity), national reading · 2024-09-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F179 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2024-09-30 · 1.3rd · data/features/fct_bank_features.parquet: return_on_equity
- F180 · Peers: return on equity (profit as a share of equity), peer median · 2024-09-30 · 10.0% · data/features/fct_bank_features.parquet: return_on_equity
- F181 · Peers: return on equity (profit as a share of equity), reading against its peers · 2024-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F183 · Peers: ratios in the national top or bottom 10% · 2024-09-30 · 12 · data/features/fct_bank_features.parquet
- F184 · Peers: those ratios also unusual among peers · 2024-09-30 · 11 · data/features/fct_bank_features.parquet
- F186 · Peers: cut-off for unusual (top or bottom share of banks) · 2024-09-30 · 10% · data/features/fct_bank_features.parquet
