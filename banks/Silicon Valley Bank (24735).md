---
cert: 24735
name: "Silicon Valley Bank"
as_of: 2022-12-31
rank: 3494
n_banks: 4773
percentile: 26.81751518960821
flagged: false
outcome: "missed"
after_test_window: false
failure_date: 2023-03-10
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:04:13"
writer_model: "claude-opus-5-5"
checked: true
---

# Silicon Valley Bank (cert 24735)

*Hindsight: failed 2023-03-10. Canary did not flag it.*

## Summary

As of 2022-12-31, Silicon Valley Bank ranked 3,494 out of 4,773 FDIC-insured banks on Canary's risk score, which places it in the 26.8th percentile on a scale where higher means riskier. It was not flagged on Canary's watchlist, which covered 2% of banks. Two figures stood out. Uninsured deposits, meaning balances above the government insurance limit, made up 86.4% of its deposits against a national median of 25.5%, and losses on bonds held to maturity equaled 98.1% of its equity against a median of 0.0%.

## Warning signs in the data

Capital is the cushion that absorbs losses. On simple measures the bank's cushion was thinner than most: equity was 7.4% of assets against a national median of 9.0%, and the leverage ratio (core capital as a share of average assets) was 8.0% against 10.3%. On risk-weighted measures, which count safer assets less heavily, it looked stronger: the Tier 1 risk-based capital ratio was 15.3% against a median of 14.2%. Credit quality was clean. Loans 90+ days past due or not accruing interest were 0.2% of loans, matching the national median of 0.2%, and the Texas ratio (troubled assets against capital plus reserves) was 0.9% against 1.8%.

Funding was where the bank differed most. Uninsured deposits were 86.4% of deposits, far above the national median of 25.5%. Deposits changed by -8.4% over the past four quarters, while the median bank's grew 2.6%. Volatile funding, money that can leave quickly, was 14.8% of assets against a median of 5.7%, and borrowings from the Federal Home Loan Bank system, a lender to banks, were 7.2% of assets against 0.3%.

Securities, mostly bonds the bank invests in, made up 56.1% of assets against a national median of 22.3%. Losses on bonds held to maturity, those the bank plans to keep until they repay, equaled 98.1% of equity, against a national median of 0.0%. Losses on bonds available for sale were 16.3% of equity, close to the median of 18.6%.

## Understanding the score

Silicon Valley Bank ranked 3,494 of 4,773 banks at 2022-12-31, the 26.8th percentile on a scale of 0 to 100 where higher means riskier. It was not flagged on the watchlist, which covered 2% of banks, or 96 banks that quarter.

Each factor's contribution is measured in the model's internal units, where a positive value pushes the score up and a negative one pushes it down. The five factors that pushed the score up most were losses on bonds available for sale at 16.3% of equity (+0.804), the efficiency ratio (operating costs as a share of revenue) at 46.4% (+0.159), commercial real estate loans at 2.4% of loans (+0.118), equity at 7.4% of assets (+0.047), and construction loans at 0.6% of loans (+0.023). The five that pushed it down most were interest expense at 0.5% of assets (-1.065), the Tier 1 risk-based capital ratio at 15.3% (-1.054), the Texas ratio at 0.9% (-0.987), securities at 56.1% of assets (-0.864), and return on equity (profit as a share of equity) at 13.4% (-0.506). The downward pulls were larger than the upward ones, which kept the bank in the lower part of the ranking.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2021-03-31 | 1,263 | 5,044 |  |
| 2021-06-30 | 1,018 | 5,015 |  |
| 2021-09-30 | 1,142 | 4,979 |  |
| 2021-12-31 | 2,160 | 4,904 |  |
| 2022-03-31 | 3,638 | 4,861 |  |
| 2022-06-30 | 4,489 | 4,838 |  |
| 2022-09-30 | 3,640 | 4,813 |  |
| 2022-12-31 | 3,494 | 4,773 |  |

## How its ratios moved

Canary compares each ratio with its own prior range, usually the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 30 ratios compared, 11 sat outside their own prior range, and the table shows the 6 furthest outside.

Annualized interest expense was 0.5% of assets, above its prior range of 0.0% to 0.3%, yet its contribution of -1.065 pushed the score down. Volatile funding was 14.8% of assets, above its prior range of 7.4% to 13.4%, but its contribution of -0.089 pushed the score down. Core deposits, the steady everyday deposits, were 76.6% of assets, below their prior range of 77.6% to 84.1%, yet with a contribution of -0.048 they had little effect on the score. Deposit growth over the past four quarters was -8.4%, below its prior range of 3.8% to 99.7%, but its contribution of -0.125 pushed the score down. Asset growth over the past four quarters was 0.2%, below its prior range of 11.6% to 97.9%, but its contribution of -0.116 pushed the score down. Federal Home Loan Bank borrowings were 7.2% of assets, above their prior range of 0.0% to 6.4%, yet with a contribution of -0.004 they had little effect on the score.

A year earlier, at 2021-12-31, the bank sat in the 56.0th percentile; at its current rank of 3,494 of 4,773, the model rated it safer than a year earlier.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized interest expense as a share of assets | 0.5% | 0.0% to 0.3% | same quarter, prior 3 years | n/a | +0.5 pp | -1.065 | pushed the score down |
| volatile funding as a share of assets | 14.8% | 7.4% to 13.4% | prior 12 quarters | +1.3 pp | +6.9 pp | -0.089 | pushed the score down |
| core deposits as a share of assets | 76.6% | 77.6% to 84.1% | prior 12 quarters | -1.5 pp | -7.4 pp | -0.048 | little effect on the score |
| asset growth over the past four quarters | 0.2% | 11.6% to 97.9% | prior 12 quarters | -11.4 pp | -83.0 pp | -0.116 | pushed the score down |
| deposit growth over the past four quarters | -8.4% | 3.8% to 99.7% | prior 12 quarters | -12.2 pp | -93.9 pp | -0.125 | pushed the score down |
| Federal Home Loan Bank borrowings as a share of assets | 7.2% | 0.0% to 6.4% | prior 12 quarters | +0.8 pp | +7.2 pp | -0.004 | little effect on the score |

11 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2022-12-31: All Other Over 1 Billion.

This is a general group: the FDIC did not record a lending specialty for this bank.

Peers: 23 banks in the same specialty group and size tier (over $10 billion).

Losses on bonds held to maturity were 98.1% of equity, in the 99.7th percentile nationally, which is unusually high, and in the 93.2nd percentile among peers against a peer median of 0.6%, unusually high among its peers too. Uninsured deposits were 86.4% of deposits, in the 99.6th percentile nationally, which is unusually high, and in the 93.2nd percentile among peers against a peer median of 41.1%, unusually high among its peers too. Securities were 56.1% of assets, in the 95.5th percentile nationally, which is unusually high, but in the 89.1st percentile among peers against a peer median of 25.7%, typical for its peer group.

Net interest margin, the spread earned on lending and investing, was 2.2%, in the 5.6th percentile nationally, which is unusually low, and in the 45.7th percentile among peers against a peer median of 2.4%, typical for its peer group. The leverage ratio was 8.0%, in the 6.3rd percentile nationally, which is unusually low, and in the 32.6th percentile among peers against a peer median of 9.1%, typical for its peer group. Deposit growth over the past four quarters was -8.4%, in the 6.7th percentile nationally, which is unusually low, and in the 32.6th percentile among peers against a peer median of -2.9%, typical for its peer group. Commercial real estate loans were 2.4% of loans, in the 5.5th percentile nationally, which is unusually low, and in the 15.2nd percentile among peers against a peer median of 10.0%, typical for its peer group. The efficiency ratio was 46.4%, in the 8.5th percentile nationally, which is unusually low, and in the 32.6th percentile among peers against a peer median of 56.2%, typical for its peer group.

Overall, 9 of the bank's ratios were in the national top or bottom 10%, and 2 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| losses on bonds held to maturity, as a share of equity | 98.1% | 99.7th (unusually high) | 0.6% | 93.2nd | unusually high among its peers too |
| uninsured deposits as a share of deposits | 86.4% | 99.6th (unusually high) | 41.1% | 93.2nd | unusually high among its peers too |
| securities as a share of assets | 56.1% | 95.5th (unusually high) | 25.7% | 89.1st | typical for its peer group |
| commercial real estate loans as a share of loans | 2.4% | 5.5th (unusually low) | 10.0% | 15.2nd | typical for its peer group |
| net interest margin (the spread earned on lending and investing) | 2.2% | 5.6th (unusually low) | 2.4% | 45.7th | typical for its peer group |
| the leverage ratio (core capital as a share of average assets) | 8.0% | 6.3rd (unusually low) | 9.1% | 32.6th | typical for its peer group |
| deposit growth over the past four quarters | -8.4% | 6.7th (unusually low) | -2.9% | 32.6th | typical for its peer group |
| the efficiency ratio (operating costs as a share of revenue) | 46.4% | 8.5th (unusually low) | 56.2% | 32.6th | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 2.4% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 13.7% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 953.0% | 50% or more | yes |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why the model missed it

In hindsight: the bank failed on 2023-03-10, while the model had ranked it 3,494 of 4,773 at its last reported quarter, 2022-12-31. The model learned from 539 failed banks in its training period, and 96% of those were credit-loss failures, where bad loans eat through capital. Of those failures, 462 had a credit-loss-only profile and 53 combined credit losses with run risk, meaning the danger of depositors pulling money quickly. This bank's loans looked clean, while its unusual features were in funding and bond losses, a pattern the training data rarely showed.

A run-risk rank (post-hoc check, designed after the 2023 failures) placed the bank at 54. In a what-if (post-hoc check, designed after the 2023 failures) that set losses on bonds held to maturity anywhere from 0.0% to 150.0% of equity with other data unchanged, the best rank reached was 3,494 of 4,773, at 0.0%, so this figure did not raise the bank's rank. In a what-if (post-hoc check, designed after the 2023 failures) that set uninsured deposits anywhere from 0.0% to 100.0% of deposits, the best rank reached was 3,019 of 4,773, at 0.0%. In a what-if (post-hoc check, designed after the 2023 failures) that set losses on bonds available for sale anywhere from 0.0% to 100.0% of equity, the best rank reached was 1,948 of 4,773, at 30.0%, still far from the top of the list.

## What happened next

In hindsight: Silicon Valley Bank failed on 2023-03-10. Its last reported quarter was 2022-12-31, the same quarter this memo describes, so there are no later ranks or watchlist flags for it.

## Sources

- F3 · As-of quarter · 2022-12-31 · 2022-12-31 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2022-12-31 · 3,494 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2022-12-31 · 4,773 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2022-12-31 · 26.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2022-12-31 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2022-12-31 · 96 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2022-12-31 · 7.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2022-12-31 · 9.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2022-12-31 · 8.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2022-12-31 · 10.3% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2022-12-31 · 15.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2022-12-31 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2022-12-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2022-12-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2022-12-31 · 0.9% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2022-12-31 · 1.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2022-12-31 · 86.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2022-12-31 · 25.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2022-12-31 · 7.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2022-12-31 · 0.3% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2022-12-31 · 14.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2022-12-31 · 5.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2022-12-31 · 98.1% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2022-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2022-12-31 · 16.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2022-12-31 · 18.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2022-12-31 · 56.1% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2022-12-31 · 22.3% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2022-12-31 · -8.4% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2022-12-31 · 2.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: losses on bonds available for sale, as a share of equity, value 16.3%; contribution to the score · 2022-12-31 · +0.804 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F76 · Driver up #2: the efficiency ratio (operating costs as a share of revenue), value 46.4%; contribution to the score · 2022-12-31 · +0.159 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F77 · Driver up #3: commercial real estate loans as a share of loans, value 2.4%; contribution to the score · 2022-12-31 · +0.118 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F78 · Driver up #4: equity as a share of assets, value 7.4%; contribution to the score · 2022-12-31 · +0.047 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F79 · Driver up #5: construction loans as a share of loans, value 0.6%; contribution to the score · 2022-12-31 · +0.023 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.5%; contribution to the score · 2022-12-31 · -1.065 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 15.3%; contribution to the score · 2022-12-31 · -1.054 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 0.9%; contribution to the score · 2022-12-31 · -0.987 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: securities as a share of assets, value 56.1%; contribution to the score · 2022-12-31 · -0.864 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F84 · Driver down #5: return on equity (profit as a share of equity), value 13.4%; contribution to the score · 2022-12-31 · -0.506 · data/analyst/scores.parquet: feature return_on_equity contribution
- F85 · Failure date · 2023-03-10 · 2023-03-10 · data/raw/failures: FAILDATE
- F86 · Last quarter the bank reported · 2022-12-31 · 2022-12-31 · data/features/fct_bank_features.parquet: report_date
- F87 · Run-risk rank (post-hoc check, designed after the 2023 failures) · 2022-12-31 · 54 · data/replay/replay_banks.csv: run_risk_rank
- F88 · What-if (post-hoc check, designed after the 2023 failures): losses on bonds available for sale, as a share of equity set to each value from 0.0% to 100.0%, other data unchanged; best rank reached 1,948 of 4,773, at 30.0% · 2022-12-31 · 1,948 · data/replay/what_if.csv: rank (feature afs_unrealized_loss_to_equity)
- F89 · What-if (post-hoc check, designed after the 2023 failures): losses on bonds held to maturity, as a share of equity set to each value from 0.0% to 150.0%, other data unchanged; best rank reached 3,494 of 4,773, at 0.0% · 2022-12-31 · 3,494 · data/replay/what_if.csv: rank (feature htm_unrealized_loss_to_equity)
- F90 · What-if (post-hoc check, designed after the 2023 failures): uninsured deposits as a share of deposits set to each value from 0.0% to 100.0%, other data unchanged; best rank reached 3,019 of 4,773, at 0.0% · 2022-12-31 · 3,019 · data/replay/what_if.csv: rank (feature uninsured_to_deposits)
- F91 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F92 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F93 · Training failures with profile: credit-loss only · n/a · 462 · data/replay/posthoc_metrics.json: failure_mix.training
- F94 · Training failures with profile: credit-loss and run-risk · n/a · 53 · data/replay/posthoc_metrics.json: failure_mix.training
- F95 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2022-12-31 · 0.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F96 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F97 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F99 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2022-12-31 · -1.065 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F100 · Trend: annualized interest expense as a share of assets, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F101 · Trend: volatile funding as a share of assets, value at the as-of quarter · 2022-12-31 · 14.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F102 · Trend: volatile funding as a share of assets, lowest value in the comparison window · n/a · 7.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F103 · Trend: volatile funding as a share of assets, highest value in the comparison window · n/a · 13.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F106 · Trend: volatile funding as a share of assets, contribution to the score (model log-odds units) · 2022-12-31 · -0.089 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F107 · Trend: volatile funding as a share of assets, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F108 · Trend: core deposits as a share of assets, value at the as-of quarter · 2022-12-31 · 76.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F109 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 77.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F110 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 84.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F113 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2022-12-31 · -0.048 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F114 · Trend: core deposits as a share of assets, what the model did with it · 2022-12-31 · little effect on the score · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F115 · Trend: asset growth over the past four quarters, value at the as-of quarter · 2022-12-31 · 0.2% · data/features/fct_bank_features.parquet: asset_growth_4q
- F116 · Trend: asset growth over the past four quarters, lowest value in the comparison window · n/a · 11.6% · data/features/fct_bank_features.parquet: asset_growth_4q
- F117 · Trend: asset growth over the past four quarters, highest value in the comparison window · n/a · 97.9% · data/features/fct_bank_features.parquet: asset_growth_4q
- F120 · Trend: asset growth over the past four quarters, contribution to the score (model log-odds units) · 2022-12-31 · -0.116 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F121 · Trend: asset growth over the past four quarters, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F122 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2022-12-31 · -8.4% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F123 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · 3.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F124 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 99.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F127 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2022-12-31 · -0.125 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F128 · Trend: deposit growth over the past four quarters, what the model did with it · 2022-12-31 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F129 · Trend: Federal Home Loan Bank borrowings as a share of assets, value at the as-of quarter · 2022-12-31 · 7.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F130 · Trend: Federal Home Loan Bank borrowings as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F131 · Trend: Federal Home Loan Bank borrowings as a share of assets, highest value in the comparison window · n/a · 6.4% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F134 · Trend: Federal Home Loan Bank borrowings as a share of assets, contribution to the score (model log-odds units) · 2022-12-31 · -0.004 · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F135 · Trend: Federal Home Loan Bank borrowings as a share of assets, what the model did with it · 2022-12-31 · little effect on the score · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F136 · Trend: ratios outside their own prior range · 2022-12-31 · 11 · data/features/fct_bank_features.parquet
- F137 · Trend: ratios shown in the table (the furthest outside their prior range) · 2022-12-31 · 6 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios compared with their own prior range · 2022-12-31 · 30 · data/features/fct_bank_features.parquet
- F139 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F140 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F141 · Percentile a year earlier (100 = highest risk) · 2021-12-31 · 56.0% · data/analyst/scores.parquet: percentile
- F142 · Trend: how the model's rating compares with a year earlier · 2022-12-31 · the model rated it safer than a year earlier · data/analyst/scores.parquet: percentile
- F146 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2022-12-31 · 98.1% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F147 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2022-12-31 · 99.7th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F148 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2022-12-31 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F149 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2022-12-31 · 93.2nd · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F150 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2022-12-31 · 0.6% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F151 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2022-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F152 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2022-12-31 · 86.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F153 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2022-12-31 · 99.6th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F154 · Peers: uninsured deposits as a share of deposits, national reading · 2022-12-31 · unusually high · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F155 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2022-12-31 · 93.2nd · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F156 · Peers: uninsured deposits as a share of deposits, peer median · 2022-12-31 · 41.1% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F157 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2022-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F158 · Peers: securities as a share of assets, bank value at the as-of quarter · 2022-12-31 · 56.1% · data/features/fct_bank_features.parquet: securities_to_assets
- F159 · Peers: securities as a share of assets, national percentile (100 = highest value among all banks) · 2022-12-31 · 95.5th · data/features/fct_bank_features.parquet: securities_to_assets
- F160 · Peers: securities as a share of assets, national reading · 2022-12-31 · unusually high · data/features/fct_bank_features.parquet: securities_to_assets
- F161 · Peers: securities as a share of assets, percentile among its peers (100 = highest value) · 2022-12-31 · 89.1st · data/features/fct_bank_features.parquet: securities_to_assets
- F162 · Peers: securities as a share of assets, peer median · 2022-12-31 · 25.7% · data/features/fct_bank_features.parquet: securities_to_assets
- F163 · Peers: securities as a share of assets, reading against its peers · 2022-12-31 · typical for its peer group · data/features/fct_bank_features.parquet: securities_to_assets
- F164 · Peers: commercial real estate loans as a share of loans, bank value at the as-of quarter · 2022-12-31 · 2.4% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F165 · Peers: commercial real estate loans as a share of loans, national percentile (100 = highest value among all banks) · 2022-12-31 · 5.5th · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F166 · Peers: commercial real estate loans as a share of loans, national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F167 · Peers: commercial real estate loans as a share of loans, percentile among its peers (100 = highest value) · 2022-12-31 · 15.2nd · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F168 · Peers: commercial real estate loans as a share of loans, peer median · 2022-12-31 · 10.0% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F169 · Peers: commercial real estate loans as a share of loans, reading against its peers · 2022-12-31 · typical for its peer group · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F170 · Peers: net interest margin (the spread earned on lending and investing), bank value at the as-of quarter · 2022-12-31 · 2.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F171 · Peers: net interest margin (the spread earned on lending and investing), national percentile (100 = highest value among all banks) · 2022-12-31 · 5.6th · data/features/fct_bank_features.parquet: net_interest_margin
- F172 · Peers: net interest margin (the spread earned on lending and investing), national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: net_interest_margin
- F173 · Peers: net interest margin (the spread earned on lending and investing), percentile among its peers (100 = highest value) · 2022-12-31 · 45.7th · data/features/fct_bank_features.parquet: net_interest_margin
- F174 · Peers: net interest margin (the spread earned on lending and investing), peer median · 2022-12-31 · 2.4% · data/features/fct_bank_features.parquet: net_interest_margin
- F175 · Peers: net interest margin (the spread earned on lending and investing), reading against its peers · 2022-12-31 · typical for its peer group · data/features/fct_bank_features.parquet: net_interest_margin
- F176 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2022-12-31 · 8.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F177 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2022-12-31 · 6.3rd · data/features/fct_bank_features.parquet: leverage_ratio
- F178 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F179 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2022-12-31 · 32.6th · data/features/fct_bank_features.parquet: leverage_ratio
- F180 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2022-12-31 · 9.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F181 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2022-12-31 · typical for its peer group · data/features/fct_bank_features.parquet: leverage_ratio
- F182 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2022-12-31 · -8.4% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F183 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2022-12-31 · 6.7th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F184 · Peers: deposit growth over the past four quarters, national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: deposit_growth_4q
- F185 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2022-12-31 · 32.6th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F186 · Peers: deposit growth over the past four quarters, peer median · 2022-12-31 · -2.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F187 · Peers: deposit growth over the past four quarters, reading against its peers · 2022-12-31 · typical for its peer group · data/features/fct_bank_features.parquet: deposit_growth_4q
- F188 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2022-12-31 · 46.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F189 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2022-12-31 · 8.5th · data/features/fct_bank_features.parquet: efficiency_ratio
- F190 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2022-12-31 · unusually low · data/features/fct_bank_features.parquet: efficiency_ratio
- F191 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2022-12-31 · 32.6th · data/features/fct_bank_features.parquet: efficiency_ratio
- F192 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2022-12-31 · 56.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F193 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2022-12-31 · typical for its peer group · data/features/fct_bank_features.parquet: efficiency_ratio
- F195 · Peers: ratios in the national top or bottom 10% · 2022-12-31 · 9 · data/features/fct_bank_features.parquet
- F196 · Peers: those ratios also unusual among peers · 2022-12-31 · 2 · data/features/fct_bank_features.parquet
- F198 · Peers: cut-off for unusual (top or bottom share of banks) · 2022-12-31 · 10% · data/features/fct_bank_features.parquet
