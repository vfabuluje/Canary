---
cert: 27332
name: "Republic Bank"
as_of: 2023-12-31
rank: 135
n_banks: 4658
percentile: 97.12322885358523
flagged: false
outcome: "caught"
after_test_window: false
failure_date: 2024-04-26
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:14:22"
writer_model: "claude-opus-5-5"
checked: true
---

# Republic Bank (cert 27332)

*Hindsight: failed 2024-04-26. Canary flagged it 4 quarters ahead.*

## Summary

As of 2023-12-31, Republic Bank, based in PA, ranked 135 out of 4,658 banks nationally on Canary's risk score, placing it in the 97.1st percentile, where higher means riskier. Its capital cushion, the owners' money that absorbs losses, was very thin: equity was 1.8% of assets against a national median of 9.5%, and paper losses on its bonds were large compared with that equity. Losses and weak capital pushed the score up, while its relatively modest loan problems held the score down. The model rated it safer than a year earlier, and it was not on the watchlist, which covers 2% of banks.

## Warning signs in the data

Capital was far below typical levels. Equity was 1.8% of assets versus a national median of 9.5%, and the leverage ratio (core capital as a share of average assets) was 4.4% against a median of 10.6%. The total risk-based capital ratio (capital measured against assets weighted by their risk) was 9.6% versus a median of 15.3%, and the Tier 1 risk-based capital ratio, which counts only core capital, was 8.8% versus 14.1%. Paper losses on bonds were very large: losses on bonds held to maturity (bonds the bank plans to keep until they mature) equaled 250.7% of equity against a national median of 0.0%, and losses on bonds available for sale equaled 155.9% of equity versus a median of 12.9%. Securities made up 40.5% of assets, well above the national median of 20.1%.

Earnings were under strain: return on equity (profit as a share of the owners' stake) was -36.6% against a median of 10.8%, and net interest margin (the spread earned on lending and investing) was 1.2% versus 3.4%. Annualized interest expense was 2.6% of assets, well above the median of 1.2%. On funding, uninsured deposits (balances above the government insurance limit) were 51.5% of deposits versus a median of 23.9%, and deposit growth over the past four quarters was -12.8% against a median of 0.9%. Federal Home Loan Bank borrowings (secured loans banks take from the Federal Home Loan Banks) were 11.9% of assets versus a median of 1.0%, while cash was 3.5% of assets against a median of 5.6%.

Credit quality points a different way: problem loans were above the median but small in absolute terms, with loans 90+ days past due or not accruing interest at 0.7% of loans versus 0.3%, and the Texas ratio (troubled assets against capital plus reserves) at 16.4% versus 1.8%. The model treated these modest loan problems as lowering the score, even though they sit above the national medians. Commercial real estate loans were 42.7% of loans, well above the national median of 23.2%, though the separate real-estate concentration check found the bank did not cross either supervisory line.

## Understanding the score

Republic Bank ranked 135 out of 4,658 banks at 2023-12-31, the 97.1st percentile on a scale of 0 to 100 where higher means riskier. The watchlist holds the top 2% of banks, 94 banks that quarter, and Republic Bank was not flagged.

The five factors that pushed the score up most were return on equity at -36.6%, losses on bonds available for sale at 155.9% of equity, equity at 1.8% of assets, the total risk-based capital ratio at 9.6%, and loans at 69.0% of deposits. The five that pushed it down most were nonaccrual assets and foreclosed property at 0.4% of assets, loans 90+ days past due or not accruing interest at 0.7% of loans, the Texas ratio at 16.4%, loans 30-89 days past due at 0.2% of assets, and construction loans at 4.8% of loans. In short, losses and thin capital raised the score, while relatively clean loan books lowered it.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2022-03-31 | 178 | 4,861 |  |
| 2022-06-30 | 159 | 4,838 |  |
| 2022-09-30 | 27 | 4,813 | ▲ watchlist |
| 2022-12-31 | 32 | 4,773 | ▲ watchlist |
| 2023-03-31 | 5 | 4,740 | ▲ watchlist |
| 2023-06-30 | 29 | 4,714 | ▲ watchlist (first flag) |
| 2023-09-30 | 65 | 4,686 | ▲ watchlist |
| 2023-12-31 | 135 | 4,658 |  |

## How its ratios moved

As of 2023-12-31, Republic Bank ranked 135 out of 4,658 banks nationally, placing it in the 97.1st percentile, where higher means riskier. At 2022-12-31 it sat in the 99.4th percentile, so the model rated it safer than a year earlier. Each ratio is compared with its own past: most against the prior 12 quarters, and year-to-date ratios against the same quarter in the prior 3 years. Of 30 ratios compared this way, 13 were outside their own prior range, and the table shows the 6 furthest outside.

Return on equity (profit as a share of the owners' stake) fell to -36.6%, well below its prior range of 2.8% to 9.1%, a change of -41.6 pp over four quarters. The model's contribution for return on equity at -36.6% was +1.198 in model log-odds units (the model's internal scale, where positive means higher risk), which pushed the score up. The efficiency ratio (operating costs as a share of revenue) rose to 145.3%, far above its prior range of 73.7% to 87.3%, yet its contribution of -0.198 pushed the score down. Annualized interest expense as a share of assets climbed to 2.6%, above its prior range of 0.3% to 0.5%, and its contribution of +0.064 pushed the score up.

Net interest margin (the spread earned on lending and investing) dropped to 1.2%, below its prior range of 2.4% to 2.7%, but its contribution of +0.032 had little effect on the score. Return on assets (profit as a share of assets) was -0.7%, below its prior range of 0.2% to 0.5%, yet its contribution of -0.068 pushed the score down. Uninsured deposits (balances above the government insurance limit) were 51.5% of deposits, below their prior range of 56.7% to 64.7%, and their contribution of -0.012 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -36.6% | 2.8% to 9.1% | same quarter, prior 3 years | n/a | -41.6 pp | +1.198 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 145.3% | 73.7% to 87.3% | same quarter, prior 3 years | n/a | +69.7 pp | -0.198 | pushed the score down |
| annualized interest expense as a share of assets | 2.6% | 0.3% to 0.5% | same quarter, prior 3 years | n/a | +2.1 pp | +0.064 | pushed the score up |
| net interest margin (the spread earned on lending and investing) | 1.2% | 2.4% to 2.7% | same quarter, prior 3 years | n/a | -1.5 pp | +0.032 | little effect on the score |
| return on assets (profit as a share of assets) | -0.7% | 0.2% to 0.5% | same quarter, prior 3 years | n/a | -0.9 pp | -0.068 | pushed the score down |
| uninsured deposits as a share of deposits | 51.5% | 56.7% to 64.7% | prior 12 quarters | -5.2 pp | -12.4 pp | -0.012 | little effect on the score |

13 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2023-12-31: Commercial Lending Specialization.

Peers: 700 banks in the same specialty group and size tier ($1 billion to $10 billion).

Losses on bonds held to maturity (paper losses on bonds the bank plans to keep until they mature), as a share of equity, stood at 250.7%, the 100.0th percentile nationally, which is unusually high. Among its peers that same figure sits at the 99.9th percentile against a peer median of 0.0%, so it is unusually high among its peers too. The total risk-based capital ratio (the bank's capital cushion measured against its risk-weighted assets) was 9.6%, the 0.2nd percentile nationally and unusually low, and at the 0.1st percentile among peers with a peer median of 13.7%, it is unusually low among its peers too. The Tier 1 risk-based capital ratio (the same measure using only core capital) was 8.8%, the 0.2nd percentile nationally and unusually low, and at the 0.1st percentile among peers with a peer median of 12.6%, it is unusually low among its peers too. The leverage ratio (core capital as a share of average assets) was 4.4%, the 0.4th percentile nationally and unusually low, and at the 0.8th percentile among peers with a peer median of 10.0%, it is unusually low among its peers too.

Return on equity (profit as a share of equity) was -36.6%, the 0.4th percentile nationally and unusually low, and at the 0.2nd percentile among peers with a peer median of 10.7%, it is unusually low among its peers too. Equity as a share of assets was 1.8%, the 0.9th percentile nationally and unusually low, and at the 0.9th percentile among peers with a peer median of 9.5%, it is unusually low among its peers too. Net interest margin (the spread earned on lending and investing) was 1.2%, the 1.0th percentile nationally and unusually low, and at the 1.2nd percentile among peers with a peer median of 3.3%, it is unusually low among its peers too. The efficiency ratio (operating costs as a share of revenue, where higher means costlier) was 145.3%, the 98.9th percentile nationally and unusually high, and at the 99.8th percentile among peers with a peer median of 63.4%, it is unusually high among its peers too.

Overall, 16 of the bank's ratios fall in the national top or bottom 10%, and all 16 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| losses on bonds held to maturity, as a share of equity | 250.7% | 100.0th (unusually high) | 0.0% | 99.9th | unusually high among its peers too |
| the total risk-based capital ratio | 9.6% | 0.2nd (unusually low) | 13.7% | 0.1st | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 8.8% | 0.2nd (unusually low) | 12.6% | 0.1st | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | 4.4% | 0.4th (unusually low) | 10.0% | 0.8th | unusually low among its peers too |
| return on equity (profit as a share of equity) | -36.6% | 0.4th (unusually low) | 10.7% | 0.2nd | unusually low among its peers too |
| equity as a share of assets | 1.8% | 0.9th (unusually low) | 9.5% | 0.9th | unusually low among its peers too |
| net interest margin (the spread earned on lending and investing) | 1.2% | 1.0th (unusually low) | 3.3% | 1.2nd | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 145.3% | 98.9th (unusually high) | 63.4% | 99.8th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 46.2% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 340.0% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | 36.3% | 50% or more | no |

It did not cross the construction line.
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

With hindsight, Republic Bank failed on 2024-04-26. Canary first flagged it in the quarter ending 2023-06-30 under its lead-time rule, a lead time of 4 quarters before the failure. At that first flag, the top factors raising the score were losses on bonds available for sale at 134.7% of equity, return on equity at -30.3%, and equity at 2.1% of assets.

The same themes of bond losses, losses on the income statement and thin capital still led the drivers at 2023-12-31, when the bank was not on the watchlist despite the earlier flag.

## What happened next

In hindsight, the last quarter the bank reported was 2023-12-31, so there are no later ranks or flags. The bank failed on 2024-04-26.

## Sources

- F1 · Bank name · n/a · Republic Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2023-12-31 · 2023-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · PA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2023-12-31 · 135 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2023-12-31 · 4,658 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2023-12-31 · 97.1% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2023-12-31 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2023-12-31 · 94 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2023-12-31 · 1.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2023-12-31 · 9.5% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2023-12-31 · 4.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2023-12-31 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2023-12-31 · 8.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2023-12-31 · 14.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2023-12-31 · 9.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2023-12-31 · 15.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2023-12-31 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2023-12-31 · 0.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2023-12-31 · 42.7% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2023-12-31 · 23.2% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2023-12-31 · 16.4% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2023-12-31 · 1.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2023-12-31 · -36.6% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2023-12-31 · 10.8% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2023-12-31 · 1.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2023-12-31 · 3.4% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2023-12-31 · 2.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2023-12-31 · 1.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2023-12-31 · 51.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2023-12-31 · 23.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2023-12-31 · 11.9% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2023-12-31 · 1.0% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2023-12-31 · 3.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2023-12-31 · 5.6% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2023-12-31 · 250.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2023-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2023-12-31 · 155.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2023-12-31 · 12.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2023-12-31 · 40.5% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2023-12-31 · 20.1% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2023-12-31 · -12.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2023-12-31 · 0.9% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -36.6%; contribution to the score · 2023-12-31 · +1.198 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 155.9%; contribution to the score · 2023-12-31 · +0.912 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: equity as a share of assets, value 1.8%; contribution to the score · 2023-12-31 · +0.367 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 9.6%; contribution to the score · 2023-12-31 · +0.089 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: loans as a share of deposits, value 69.0%; contribution to the score · 2023-12-31 · +0.087 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F80 · Driver down #1: nonaccrual assets and foreclosed property, as a share of assets, value 0.4%; contribution to the score · 2023-12-31 · -1.161 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F81 · Driver down #2: loans 90+ days past due or not accruing interest, as a share of loans, value 0.7%; contribution to the score · 2023-12-31 · -1.006 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 16.4%; contribution to the score · 2023-12-31 · -0.830 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: loans 30-89 days past due, as a share of assets, value 0.2%; contribution to the score · 2023-12-31 · -0.359 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F84 · Driver down #5: construction loans as a share of loans, value 4.8%; contribution to the score · 2023-12-31 · -0.260 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F85 · Failure date · 2024-04-26 · 2024-04-26 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2023-06-30 · 2023-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2023-06-30: losses on bonds available for sale, as a share of equity, value 134.7%; contribution to the score · 2023-06-30 · +1.306 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F89 · Driver up #2 at 2023-06-30: return on equity (profit as a share of equity), value -30.3%; contribution to the score · 2023-06-30 · +1.044 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2023-06-30: equity as a share of assets, value 2.1%; contribution to the score · 2023-06-30 · +0.233 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F98 · Last quarter the bank reported · 2023-12-31 · 2023-12-31 · data/features/fct_bank_features.parquet: report_date
- F103 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2023-12-31 · -36.6% · data/features/fct_bank_features.parquet: return_on_equity
- F104 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 2.8% · data/features/fct_bank_features.parquet: return_on_equity
- F105 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 9.1% · data/features/fct_bank_features.parquet: return_on_equity
- F106 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2023-12-31 · -41.6 pp · data/features/fct_bank_features.parquet: return_on_equity
- F107 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2023-12-31 · +1.198 · data/analyst/scores.parquet: feature return_on_equity contribution
- F108 · Trend: return on equity (profit as a share of equity), what the model did with it · 2023-12-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F109 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2023-12-31 · 145.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 73.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F111 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 87.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F113 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2023-12-31 · -0.198 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F114 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2023-12-31 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F115 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2023-12-31 · 2.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F116 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F117 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F119 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2023-12-31 · +0.064 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F120 · Trend: annualized interest expense as a share of assets, what the model did with it · 2023-12-31 · pushed the score up · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F121 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2023-12-31 · 1.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F122 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 2.4% · data/features/fct_bank_features.parquet: net_interest_margin
- F123 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 2.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F125 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2023-12-31 · +0.032 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F126 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2023-12-31 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F127 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2023-12-31 · -0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F128 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: return_on_assets
- F129 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: return_on_assets
- F131 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2023-12-31 · -0.068 · data/analyst/scores.parquet: feature return_on_assets contribution
- F132 · Trend: return on assets (profit as a share of assets), what the model did with it · 2023-12-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F133 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2023-12-31 · 51.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F134 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 56.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F135 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 64.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F138 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2023-12-31 · -0.012 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F139 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2023-12-31 · little effect on the score · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F140 · Trend: ratios outside their own prior range · 2023-12-31 · 13 · data/features/fct_bank_features.parquet
- F141 · Trend: ratios shown in the table (the furthest outside their prior range) · 2023-12-31 · 6 · data/features/fct_bank_features.parquet
- F142 · Trend: ratios compared with their own prior range · 2023-12-31 · 30 · data/features/fct_bank_features.parquet
- F143 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F144 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F145 · Percentile a year earlier (100 = highest risk) · 2022-12-31 · 99.4% · data/analyst/scores.parquet: percentile
- F146 · Trend: how the model's rating compares with a year earlier · 2023-12-31 · the model rated it safer than a year earlier · data/analyst/scores.parquet: percentile
- F150 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2023-12-31 · 250.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F151 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2023-12-31 · 100.0th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F152 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2023-12-31 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F153 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2023-12-31 · 99.9th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F154 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2023-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F155 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2023-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F156 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2023-12-31 · 9.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F157 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2023-12-31 · 0.2nd · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F158 · Peers: the total risk-based capital ratio, national reading · 2023-12-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F159 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2023-12-31 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F160 · Peers: the total risk-based capital ratio, peer median · 2023-12-31 · 13.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F161 · Peers: the total risk-based capital ratio, reading against its peers · 2023-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F162 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2023-12-31 · 8.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F163 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2023-12-31 · 0.2nd · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F164 · Peers: the Tier 1 risk-based capital ratio, national reading · 2023-12-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F165 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2023-12-31 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F166 · Peers: the Tier 1 risk-based capital ratio, peer median · 2023-12-31 · 12.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F167 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2023-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F168 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2023-12-31 · 4.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F169 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2023-12-31 · 0.4th · data/features/fct_bank_features.parquet: leverage_ratio
- F170 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2023-12-31 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F171 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2023-12-31 · 0.8th · data/features/fct_bank_features.parquet: leverage_ratio
- F172 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2023-12-31 · 10.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F173 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2023-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F174 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2023-12-31 · -36.6% · data/features/fct_bank_features.parquet: return_on_equity
- F175 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2023-12-31 · 0.4th · data/features/fct_bank_features.parquet: return_on_equity
- F176 · Peers: return on equity (profit as a share of equity), national reading · 2023-12-31 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F177 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2023-12-31 · 0.2nd · data/features/fct_bank_features.parquet: return_on_equity
- F178 · Peers: return on equity (profit as a share of equity), peer median · 2023-12-31 · 10.7% · data/features/fct_bank_features.parquet: return_on_equity
- F179 · Peers: return on equity (profit as a share of equity), reading against its peers · 2023-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F180 · Peers: equity as a share of assets, bank value at the as-of quarter · 2023-12-31 · 1.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F181 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2023-12-31 · 0.9th · data/features/fct_bank_features.parquet: equity_to_assets
- F182 · Peers: equity as a share of assets, national reading · 2023-12-31 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F183 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2023-12-31 · 0.9th · data/features/fct_bank_features.parquet: equity_to_assets
- F184 · Peers: equity as a share of assets, peer median · 2023-12-31 · 9.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F185 · Peers: equity as a share of assets, reading against its peers · 2023-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F186 · Peers: net interest margin (the spread earned on lending and investing), bank value at the as-of quarter · 2023-12-31 · 1.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F187 · Peers: net interest margin (the spread earned on lending and investing), national percentile (100 = highest value among all banks) · 2023-12-31 · 1.0th · data/features/fct_bank_features.parquet: net_interest_margin
- F188 · Peers: net interest margin (the spread earned on lending and investing), national reading · 2023-12-31 · unusually low · data/features/fct_bank_features.parquet: net_interest_margin
- F189 · Peers: net interest margin (the spread earned on lending and investing), percentile among its peers (100 = highest value) · 2023-12-31 · 1.2nd · data/features/fct_bank_features.parquet: net_interest_margin
- F190 · Peers: net interest margin (the spread earned on lending and investing), peer median · 2023-12-31 · 3.3% · data/features/fct_bank_features.parquet: net_interest_margin
- F191 · Peers: net interest margin (the spread earned on lending and investing), reading against its peers · 2023-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: net_interest_margin
- F192 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2023-12-31 · 145.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F193 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2023-12-31 · 98.9th · data/features/fct_bank_features.parquet: efficiency_ratio
- F194 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2023-12-31 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F195 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2023-12-31 · 99.8th · data/features/fct_bank_features.parquet: efficiency_ratio
- F196 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2023-12-31 · 63.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F197 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2023-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F199 · Peers: ratios in the national top or bottom 10% · 2023-12-31 · 16 · data/features/fct_bank_features.parquet
- F200 · Peers: those ratios also unusual among peers · 2023-12-31 · 16 · data/features/fct_bank_features.parquet
- F202 · Peers: cut-off for unusual (top or bottom share of banks) · 2023-12-31 · 10% · data/features/fct_bank_features.parquet
