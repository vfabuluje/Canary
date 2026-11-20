---
cert: 12166
name: "West Point Bank"
as_of: 2026-06-30
rank: 40
n_banks: 4313
percentile: 99.09575701367957
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:58:24"
writer_model: "claude-opus-5-5"
checked: true
---

# West Point Bank (cert 12166)

*Outcome not yet known.*

## Summary

As of 2026-06-30, West Point Bank, a Kentucky bank, ranked number 40 of 4,313 banks nationally on Canary's risk score, at the 99.1st percentile, and it is flagged on the watchlist. The main reason is large paper losses on bonds it holds for possible sale, along with thin capital, heavy reliance on costly borrowed and brokered money, and an unusually large share of construction loans. Its problem loans rose against its own history, yet the model treated those credit ratios as pulling the score down, so the trend data and the model's reading point in different directions.

## Warning signs in the data

Capital, the owners' cushion against losses, is thin: equity was 7.4% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.5% against 11.0%. Risk-based capital ratios, which weigh assets by how risky they are, were also below the middle, with Tier 1 at 11.7% against 14.6% and total capital at 12.3% against 15.8%. Paper losses on bonds available for sale equaled 23.9% of equity, far above the national median of 5.6%.

On credit quality, seriously late loans or loans no longer earning interest were 0.9% of loans against a median of 0.5%, and nonaccrual assets plus foreclosed property were 0.7% of assets against 0.3%. The Texas ratio, troubled assets compared with capital plus reserves, was 9.5% against a median of 2.9%, while loan-loss reserves were only 0.5% of loans against 1.2%. Construction loans made up 21.3% of loans against a median of 5.3%, and the concentration section found the bank crossed the regulators' construction screen but not the second commercial real estate screen. These credit ratios rose versus the bank's own history, yet the trend section shows the model read several of them as pushing the score down, so the two views differ.

On funding, brokered deposits (money placed through middlemen) were 11.7% of deposits against a median of 0.0%, and Federal Home Loan Bank borrowings were 7.2% of assets against 0.2%. Interest expense ran at 2.8% of assets against a median of 1.6%, loans equaled 92.7% of deposits against 80.2%, and cash was 3.7% of assets against 6.2%. Uninsured deposits, at 22.3% of deposits, were slightly below the median of 24.8%.

## Understanding the score

West Point Bank ranked number 40 of 4,313 banks as of 2026-06-30, placing it at the 99.1st percentile on a scale of 0 to 100 where higher means riskier. The watchlist covers the riskiest 2% of banks, 87 banks that quarter, and this bank is flagged.

The five features pushing the score up most were losses on bonds available for sale at 23.9% of equity (+2.305), the efficiency ratio of operating costs to revenue at 55.0% (+0.398), brokered deposits at 11.7% of deposits (+0.371), interest expense at 2.8% of assets (+0.301), and equity at 7.4% of assets (+0.026). The five pushing it down most were the Texas ratio at 9.5% (-0.802), the Tier 1 risk-based capital ratio at 11.7% (-0.550), return on equity at 15.1% (-0.460), early-stage late loans at 0.3% of assets (-0.362), and return on assets at 1.1% (-0.290). The bond-loss feature is by far the largest single push upward.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 47 | 4,589 | ▲ watchlist |
| 2024-12-31 | 80 | 4,560 | ▲ watchlist |
| 2025-03-31 | 54 | 4,536 | ▲ watchlist |
| 2025-06-30 | 72 | 4,494 | ▲ watchlist |
| 2025-09-30 | 62 | 4,452 | ▲ watchlist |
| 2025-12-31 | 67 | 4,411 | ▲ watchlist |
| 2026-03-31 | 22 | 4,353 | ▲ watchlist |
| 2026-06-30 | 40 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, West Point Bank ranked number 40 of 4,313 banks nationally, at the 99.1st percentile, where a higher percentile means a higher risk score. A year earlier it sat at the 98.4th percentile, and the model's rating of the bank is about the same as a year earlier. Of 30 ratios compared with the bank's own prior range, which for most ratios covers the prior 12 quarters, 12 were outside that range, and the 6 furthest outside are shown in the table.

The Texas ratio (troubled assets compared with capital plus reserves) stood at 9.5%, above its prior range of 0.2% to 5.6%, yet its contribution of -0.802 model log-odds units pushed the score down. That ratio rose +3.8 pp over one quarter. Loans 90 or more days past due or no longer earning interest made up 0.9% of loans, above their prior range of 0.0% to 0.5%, but this ratio's contribution of -0.261 pushed the score down. Nonaccrual assets (loans no longer earning interest) plus foreclosed property were 0.7% of assets, above their prior range of 0.0% to 0.4%, while their contribution of -0.256 also pushed the score down.

Equity, the owners' cushion against losses, was 7.4% of assets, above its prior range of 5.7% to 7.0%, and its contribution of +0.026 had little effect on the score. The net interest margin, the spread earned on lending and investing, was 3.1%, above its prior range of 2.1% to 2.9%, and its contribution of -0.052 pushed the score down. The efficiency ratio, operating costs as a share of revenue, was 55.0%, below its prior range of 59.9% to 81.9%, and its contribution of +0.398 pushed the score up.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 9.5% | 0.2% to 5.6% | prior 12 quarters | +3.8 pp | +7.8 pp | -0.802 | pushed the score down |
| loans 90+ days past due or not accruing interest, as a share of loans | 0.9% | 0.0% to 0.5% | prior 12 quarters | +0.4 pp | +0.8 pp | -0.261 | pushed the score down |
| nonaccrual assets and foreclosed property, as a share of assets | 0.7% | 0.0% to 0.4% | prior 12 quarters | +0.3 pp | +0.6 pp | -0.256 | pushed the score down |
| equity as a share of assets | 7.4% | 5.7% to 7.0% | prior 12 quarters | +0.4 pp | +1.1 pp | +0.026 | little effect on the score |
| net interest margin (the spread earned on lending and investing) | 3.1% | 2.1% to 2.9% | same quarter, prior 3 years | n/a | +0.2 pp | -0.052 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 55.0% | 59.9% to 81.9% | same quarter, prior 3 years | n/a | -4.9 pp | +0.398 | pushed the score up |

12 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

Interest expense, what the bank pays to depositors and lenders, ran at an annualized 2.8% of assets, at the 97.2nd percentile nationally, which is unusually high, and at the 96.8th percentile among its peers against a peer median of 1.7%, so it is unusually high among its peers too. Construction loans, which fund building projects, made up 21.3% of the bank's loans, at the 97.2nd percentile nationally, which is unusually high, and at the 94.6th percentile among its peers against a peer median of 8.2%, so it is unusually high among its peers too. Loan-loss reserves, money set aside to cover loans that may not be repaid, were 0.5% of loans, at the 3.4th percentile nationally, which is unusually low, and at the 1.2nd percentile among its peers against a peer median of 1.2%, so it is unusually low among its peers too.

The leverage ratio, core capital as a share of average assets, was 8.5%, at the 7.2nd percentile nationally, which is unusually low, and at the 7.1st percentile among its peers against a peer median of 10.8%, so it is unusually low among its peers too. Equity, the owners' own money in the bank, was 7.4% of assets, at the 7.3rd percentile nationally, which is unusually low, and at the 7.6th percentile among its peers against a peer median of 10.2%, so it is unusually low among its peers too. The total risk-based capital ratio, capital measured against assets weighted by how likely they are to lose value, was 12.3%, at the 9.9th percentile nationally, which is unusually low, and at the 12.3rd percentile among its peers against a peer median of 15.4%, which is typical for its peer group. Overall, 6 of the bank's ratios sit in the national top or bottom 10%, and 5 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| annualized interest expense as a share of assets | 2.8% | 97.2nd (unusually high) | 1.7% | 96.8th | unusually high among its peers too |
| construction loans as a share of loans | 21.3% | 97.2nd (unusually high) | 8.2% | 94.6th | unusually high among its peers too |
| loan-loss reserves as a share of loans | 0.5% | 3.4th (unusually low) | 1.2% | 1.2nd | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | 8.5% | 7.2nd (unusually low) | 10.8% | 7.1st | unusually low among its peers too |
| equity as a share of assets | 7.4% | 7.3rd (unusually low) | 10.2% | 7.6th | unusually low among its peers too |
| the total risk-based capital ratio | 12.3% | 9.9th (unusually low) | 15.4% | 12.3rd | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 184.6% | 100% or more | yes |
| Total commercial real estate loans ÷ capital | 321.7% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | 43.8% | 50% or more | no |

It crossed the construction line (100% or more of capital).
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight: this case is classed as an open bank on the watchlist, meaning it was flagged and the outcome category does not record a closure. The fact sheet holds no data from after the as-of quarter, so the reason for the flag rests on the as-of picture: large paper bond losses, thin capital and costly borrowed funding.

## What happened next

In hindsight: our fact sheet contains no later ranks, flags or reporting status for this bank, so this note cannot say what happened after the as-of quarter. The score history table added by code shows any later quarters that are available.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KY · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 40 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.1% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 11.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 12.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F33 · Bank: construction loans as a share of loans · 2026-06-30 · 21.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F34 · National median: construction loans as a share of loans · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 9.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 2.8% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 92.7% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 22.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 11.7% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 7.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 3.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 23.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: losses on bonds available for sale, as a share of equity, value 23.9%; contribution to the score · 2026-06-30 · +2.305 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F76 · Driver up #2: the efficiency ratio (operating costs as a share of revenue), value 55.0%; contribution to the score · 2026-06-30 · +0.398 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F77 · Driver up #3: brokered deposits as a share of deposits, value 11.7%; contribution to the score · 2026-06-30 · +0.371 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F78 · Driver up #4: annualized interest expense as a share of assets, value 2.8%; contribution to the score · 2026-06-30 · +0.301 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F79 · Driver up #5: equity as a share of assets, value 7.4%; contribution to the score · 2026-06-30 · +0.026 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 9.5%; contribution to the score · 2026-06-30 · -0.802 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 11.7%; contribution to the score · 2026-06-30 · -0.550 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 15.1%; contribution to the score · 2026-06-30 · -0.460 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: loans 30-89 days past due, as a share of assets, value 0.3%; contribution to the score · 2026-06-30 · -0.362 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F84 · Driver down #5: return on assets (profit as a share of assets), value 1.1%; contribution to the score · 2026-06-30 · -0.290 · data/analyst/scores.parquet: feature return_on_assets contribution
- F89 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 9.5% · data/features/fct_bank_features.parquet: texas_ratio
- F90 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: texas_ratio
- F91 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 5.6% · data/features/fct_bank_features.parquet: texas_ratio
- F92 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2026-06-30 · +3.8 pp · data/features/fct_bank_features.parquet: texas_ratio
- F94 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · -0.802 · data/analyst/scores.parquet: feature texas_ratio contribution
- F95 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature texas_ratio contribution
- F96 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F97 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F98 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F101 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.261 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F102 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F103 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F104 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F105 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F108 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.256 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F109 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F110 · Trend: equity as a share of assets, value at the as-of quarter · 2026-06-30 · 7.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F111 · Trend: equity as a share of assets, lowest value in the comparison window · n/a · 5.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F112 · Trend: equity as a share of assets, highest value in the comparison window · n/a · 7.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F115 · Trend: equity as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.026 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F116 · Trend: equity as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature equity_to_assets contribution
- F117 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 3.1% · data/features/fct_bank_features.parquet: net_interest_margin
- F118 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 2.1% · data/features/fct_bank_features.parquet: net_interest_margin
- F119 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 2.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F121 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.052 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F122 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F123 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 55.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F124 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 59.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F125 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 81.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F127 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.398 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F128 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F129 · Trend: ratios outside their own prior range · 2026-06-30 · 12 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F132 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F134 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 98.4% · data/analyst/scores.parquet: percentile
- F135 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F139 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2026-06-30 · 2.8% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F140 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.2nd · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F141 · Peers: annualized interest expense as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F142 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 96.8th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F143 · Peers: annualized interest expense as a share of assets, peer median · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F144 · Peers: annualized interest expense as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F145 · Peers: construction loans as a share of loans, bank value at the as-of quarter · 2026-06-30 · 21.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F146 · Peers: construction loans as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.2nd · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F147 · Peers: construction loans as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F148 · Peers: construction loans as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 94.6th · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F149 · Peers: construction loans as a share of loans, peer median · 2026-06-30 · 8.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F150 · Peers: construction loans as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F151 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F152 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 3.4th · data/features/fct_bank_features.parquet: allowance_to_loans
- F153 · Peers: loan-loss reserves as a share of loans, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: allowance_to_loans
- F154 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 1.2nd · data/features/fct_bank_features.parquet: allowance_to_loans
- F155 · Peers: loan-loss reserves as a share of loans, peer median · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F156 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F157 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 8.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F158 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 7.2nd · data/features/fct_bank_features.parquet: leverage_ratio
- F159 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F160 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 7.1st · data/features/fct_bank_features.parquet: leverage_ratio
- F161 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 10.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F162 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F163 · Peers: equity as a share of assets, bank value at the as-of quarter · 2026-06-30 · 7.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F164 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 7.3rd · data/features/fct_bank_features.parquet: equity_to_assets
- F165 · Peers: equity as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F166 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 7.6th · data/features/fct_bank_features.parquet: equity_to_assets
- F167 · Peers: equity as a share of assets, peer median · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F168 · Peers: equity as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F169 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 12.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F170 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 9.9th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F171 · Peers: the total risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F172 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 12.3rd · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F173 · Peers: the total risk-based capital ratio, peer median · 2026-06-30 · 15.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F174 · Peers: the total risk-based capital ratio, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F176 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F177 · Peers: those ratios also unusual among peers · 2026-06-30 · 5 · data/features/fct_bank_features.parquet
- F179 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
