---
cert: 14361
name: "The First State Bank"
as_of: 2020-03-31
rank: 1
n_banks: 5182
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2020-04-03
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:05:15"
writer_model: "claude-opus-5-5"
checked: true
---

# The First State Bank (cert 14361)

*Hindsight: failed 2020-04-03. Canary flagged it 4 quarters ahead.*

## Summary

As of March 31, 2020, The First State Bank, based in WV, ranked 1 out of 5,182 banks nationally on Canary's risk score, which places it in the 100.0th percentile. It was flagged on Canary's watchlist, which covers the top 2% of banks. Its capital cushion was very thin, with equity (the owners' stake that absorbs losses) at 0.6% of assets against a national median of 11.4%, and 26.7% of its loans were 90 or more days past due or not earning interest, against a median of 0.6%. It was also losing money, with a return on assets (profit as a share of assets) of -4.1% versus a national median of 0.9%.

## Warning signs in the data

Capital, the cushion a bank holds to absorb losses, was far below normal levels. Equity was 0.6% of assets, compared with a national median of 11.4%. The leverage ratio (core capital as a share of average assets) was 0.3%, against a national median of 10.9%. The Tier 1 risk-based capital ratio, which measures top-quality capital against riskier assets, was 0.4% versus a median of 14.6%, and the total risk-based capital ratio was 1.7% versus 15.7%.

Credit quality, meaning how well borrowers were repaying, was very weak. Loans 90+ days past due or not accruing interest made up 26.7% of loans, compared with a national median of 0.6%. Nonaccrual assets and foreclosed property were 26.0% of assets, well above the national median of 0.4%. The Texas ratio, which weighs troubled assets against capital plus reserves, stood at 1704.3% against a median of 3.8%, and return on equity (profit as a share of equity) was -406.7% versus 7.9%.

Funding looked steadier: uninsured deposits were 3.4% of deposits versus a median of 19.4%, and core deposits (stable everyday deposits) were 83.6% of assets versus 77.6%. Cash was 15.9% of assets, above the national median of 7.8%, while brokered deposits (money placed through middlemen) were 4.2% of deposits against a median of 0.0%. Losses on bonds available for sale, as a share of equity, were -40.1%, far from the national median of -0.8%.

## Understanding the score

The First State Bank ranked 1 of 5,182 banks on March 31, 2020, which is the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks, and was one of 104 banks on it that quarter.

The five factors that pushed its score up most were the Tier 1 risk-based capital ratio at 0.4%, return on equity at -406.7%, the Texas ratio at 1704.3%, loans 90+ days past due or not accruing interest at 26.7% of loans, and the total risk-based capital ratio at 1.7%. The largest single push came from the Tier 1 capital ratio, with a contribution of +2.093.

The five factors that pulled the score down most were losses on bonds available for sale at -40.1% of equity, interest expense at 1.5% of assets, construction loans at 9.8% of loans, total assets of $151.8 million, and brokered deposits at 4.2% of deposits. These downward pulls were small, the largest being -0.267.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2018-06-30 | 6 | 5,610 | ▲ watchlist |
| 2018-09-30 | 6 | 5,544 | ▲ watchlist |
| 2018-12-31 | 1 | 5,473 | ▲ watchlist |
| 2019-03-31 | 1 | 5,428 | ▲ watchlist |
| 2019-06-30 | 2 | 5,369 | ▲ watchlist (first flag) |
| 2019-09-30 | 4 | 5,325 | ▲ watchlist |
| 2019-12-31 | 1 | 5,244 | ▲ watchlist |
| 2020-03-31 | 1 | 5,182 | ▲ watchlist |

## How its ratios moved

Canary compares each ratio with the bank's own prior range, using the prior 12 quarters for most ratios and the same quarter in the prior 3 years for year-to-date ratios. Of 30 ratios compared, 21 were outside their own prior range.

Return on equity was -406.7%, far below its prior range of -69.4% to -21.7%, and it pushed the score up with a contribution of +1.374. The Texas ratio was 1704.3%, above its prior range of 243.1% to 1120.2% after a rise of +584.1 pp in one quarter, and it pushed the score up with a contribution of +1.289. Return on assets was -4.1%, below its prior range of -2.5% to -1.3%, and it pushed the score up with a contribution of +0.205. Net interest margin, the spread earned on lending and investing, was 2.3%, below its prior range of 3.6% to 3.9%, and it pushed the score up with a contribution of +0.081.

The efficiency ratio, operating costs as a share of revenue, was 249.2%, well above its prior range of 122.3% to 150.0%, yet it had little effect on the score, with a contribution of -0.007. Losses on bonds available for sale were -40.1% of equity, below their prior range of -5.6% to 11.9%, yet this pushed the score down, with a contribution of -0.267. Overall the model rated the bank about the same as a year earlier: it was in the 100.0th percentile on March 31, 2019, and ranked 1 of 5,182 banks on March 31, 2020.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -406.7% | -69.4% to -21.7% | same quarter, prior 3 years | n/a | -337.3 pp | +1.374 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 249.2% | 122.3% to 150.0% | same quarter, prior 3 years | n/a | +110.1 pp | -0.007 | little effect on the score |
| losses on bonds available for sale, as a share of equity | -40.1% | -5.6% to 11.9% | prior 12 quarters | -34.5 pp | -44.7 pp | -0.267 | pushed the score down |
| return on assets (profit as a share of assets) | -4.1% | -2.5% to -1.3% | same quarter, prior 3 years | n/a | -2.2 pp | +0.205 | pushed the score up |
| net interest margin (the spread earned on lending and investing) | 2.3% | 3.6% to 3.9% | same quarter, prior 3 years | n/a | -1.4 pp | +0.081 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 1704.3% | 243.1% to 1120.2% | prior 12 quarters | +584.1 pp | +1017.9 pp | +1.289 | pushed the score up |

21 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2020-03-31: Commercial Lending Specialization.

Peers: 1805 banks in the same specialty group and size tier ($100 million to $1 billion).

Nonaccrual assets and foreclosed property were 26.0% of assets, the 100.0th percentile nationally, which is unusually high, and the 100.0th percentile among its peers, whose median was 0.4%, so it was unusually high among its peers too. The Texas ratio was 1704.3%, the 100.0th percentile nationally, which is unusually high, and the 100.0th percentile among peers with a peer median of 4.3%, so it was unusually high among its peers too. Loans 90+ days past due or not accruing interest were 26.7% of loans, the 99.9th percentile nationally, which is unusually high, and the 100.0th percentile among peers with a peer median of 0.5%, so it was unusually high among its peers too.

Return on equity was -406.7%, the 0.0th percentile nationally, which is unusually low, and the 0.0th percentile among peers with a peer median of 8.3%, so it was unusually low among its peers too. The Tier 1 risk-based capital ratio was 0.4%, the 0.0th percentile nationally, which is unusually low, and the 0.0th percentile among peers with a peer median of 13.8%, so it was unusually low among its peers too. The total risk-based capital ratio was 1.7%, the 0.0th percentile nationally, which is unusually low, and the 0.0th percentile among peers with a peer median of 14.9%, so it was unusually low among its peers too. Equity was 0.6% of assets, the 0.3rd percentile nationally, which is unusually low, and the 0.1st percentile among peers with a peer median of 10.9%, so it was unusually low among its peers too. Losses on bonds available for sale were -40.1% of equity, the 0.0th percentile nationally, which is unusually low, and the 0.0th percentile among peers with a peer median of -0.7%, so it was unusually low among its peers too.

Overall, 17 of the bank's ratios were in the national top or bottom 10%, and 17 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| nonaccrual assets and foreclosed property, as a share of assets | 26.0% | 100.0th (unusually high) | 0.4% | 100.0th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -406.7% | 0.0th (unusually low) | 8.3% | 0.0th | unusually low among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 1704.3% | 100.0th (unusually high) | 4.3% | 100.0th | unusually high among its peers too |
| the total risk-based capital ratio | 1.7% | 0.0th (unusually low) | 14.9% | 0.0th | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 0.4% | 0.0th (unusually low) | 13.8% | 0.0th | unusually low among its peers too |
| losses on bonds available for sale, as a share of equity | -40.1% | 0.0th (unusually low) | -0.7% | 0.0th | unusually low among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 26.7% | 99.9th (unusually high) | 0.5% | 100.0th | unusually high among its peers too |
| equity as a share of assets | 0.6% | 0.3rd (unusually low) | 10.9% | 0.1st | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 373.8% | 100% or more | yes |
| Total commercial real estate loans ÷ capital | 594.9% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | -25.6% | 50% or more | no |

It crossed the construction line (100% or more of capital).
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, The First State Bank failed on April 3, 2020. Canary first flagged it in the quarter ending 2019-06-30, a lead time of 4 quarters before the failure.

At that first flag, the main factors pushing the score up were the Tier 1 risk-based capital ratio at 3.3%, return on equity at -87.3%, and the Texas ratio at 704.2%. Loans 90+ days past due or not accruing interest were already 19.1% of loans, and the total risk-based capital ratio was 4.5%. The same weak capital and troubled loans that drove the early flag were still the top drivers in the later data.

## What happened next

In hindsight, the last quarter the bank reported was 2020-03-31, and it failed on 2020-04-03, only days after that quarter ended. Because its data stop after 2020-03-31, there are no later ranks or watchlist flags to show.

## Sources

- F1 · Bank name · n/a · The First State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2020-03-31 · 2020-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WV · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2020-03-31 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2020-03-31 · 5,182 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2020-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2020-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2020-03-31 · 104 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2020-03-31 · 0.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2020-03-31 · 11.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2020-03-31 · 0.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2020-03-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2020-03-31 · 0.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2020-03-31 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2020-03-31 · 1.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2020-03-31 · 15.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2020-03-31 · 26.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2020-03-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2020-03-31 · 26.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2020-03-31 · 0.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2020-03-31 · 1704.3% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2020-03-31 · 3.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2020-03-31 · -4.1% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2020-03-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2020-03-31 · -406.7% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2020-03-31 · 7.9% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2020-03-31 · 3.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2020-03-31 · 19.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2020-03-31 · 4.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2020-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2020-03-31 · 83.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2020-03-31 · 77.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2020-03-31 · 15.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2020-03-31 · 7.8% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2020-03-31 · -40.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2020-03-31 · -0.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 0.4%; contribution to the score · 2020-03-31 · +2.093 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -406.7%; contribution to the score · 2020-03-31 · +1.374 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 1704.3%; contribution to the score · 2020-03-31 · +1.289 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 26.7%; contribution to the score · 2020-03-31 · +0.836 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 1.7%; contribution to the score · 2020-03-31 · +0.573 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: losses on bonds available for sale, as a share of equity, value -40.1%; contribution to the score · 2020-03-31 · -0.267 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 1.5%; contribution to the score · 2020-03-31 · -0.170 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: construction loans as a share of loans, value 9.8%; contribution to the score · 2020-03-31 · -0.117 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: total assets, value $151.8 million; contribution to the score · 2020-03-31 · -0.089 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: brokered deposits as a share of deposits, value 4.2%; contribution to the score · 2020-03-31 · -0.085 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F85 · Failure date · 2020-04-03 · 2020-04-03 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2019-06-30 · 2019-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2019-06-30: the Tier 1 risk-based capital ratio, value 3.3%; contribution to the score · 2019-06-30 · +1.924 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2019-06-30: return on equity (profit as a share of equity), value -87.3%; contribution to the score · 2019-06-30 · +1.438 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2019-06-30: the Texas ratio (troubled assets against capital plus reserves), value 704.2%; contribution to the score · 2019-06-30 · +1.210 · data/analyst/scores.parquet: feature texas_ratio contribution
- F91 · Driver up #4 at 2019-06-30: loans 90+ days past due or not accruing interest, as a share of loans, value 19.1%; contribution to the score · 2019-06-30 · +0.793 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2019-06-30: the total risk-based capital ratio, value 4.5%; contribution to the score · 2019-06-30 · +0.504 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2020-03-31 · 2020-03-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2020-03-31 · -406.7% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -69.4% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -21.7% · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2020-03-31 · +1.374 · data/analyst/scores.parquet: feature return_on_equity contribution
- F104 · Trend: return on equity (profit as a share of equity), what the model did with it · 2020-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2020-03-31 · 249.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 122.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 150.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F109 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2020-03-31 · -0.007 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2020-03-31 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F111 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2020-03-31 · -40.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F112 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · -5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F113 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 11.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F116 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2020-03-31 · -0.267 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F117 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2020-03-31 · pushed the score down · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F118 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2020-03-31 · -4.1% · data/features/fct_bank_features.parquet: return_on_assets
- F119 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -2.5% · data/features/fct_bank_features.parquet: return_on_assets
- F120 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F122 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2020-03-31 · +0.205 · data/analyst/scores.parquet: feature return_on_assets contribution
- F123 · Trend: return on assets (profit as a share of assets), what the model did with it · 2020-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F124 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2020-03-31 · 2.3% · data/features/fct_bank_features.parquet: net_interest_margin
- F125 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F126 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F128 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2020-03-31 · +0.081 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F129 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2020-03-31 · pushed the score up · data/analyst/scores.parquet: feature net_interest_margin contribution
- F130 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2020-03-31 · 1704.3% · data/features/fct_bank_features.parquet: texas_ratio
- F131 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 243.1% · data/features/fct_bank_features.parquet: texas_ratio
- F132 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 1120.2% · data/features/fct_bank_features.parquet: texas_ratio
- F133 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2020-03-31 · +584.1 pp · data/features/fct_bank_features.parquet: texas_ratio
- F135 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2020-03-31 · +1.289 · data/analyst/scores.parquet: feature texas_ratio contribution
- F136 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2020-03-31 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F137 · Trend: ratios outside their own prior range · 2020-03-31 · 21 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios compared with their own prior range · 2020-03-31 · 30 · data/features/fct_bank_features.parquet
- F140 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F142 · Percentile a year earlier (100 = highest risk) · 2019-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F143 · Trend: how the model's rating compares with a year earlier · 2020-03-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F147 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2020-03-31 · 26.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F148 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2020-03-31 · 100.0th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F149 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2020-03-31 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F150 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2020-03-31 · 100.0th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F151 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2020-03-31 · 0.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F152 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2020-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F153 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2020-03-31 · -406.7% · data/features/fct_bank_features.parquet: return_on_equity
- F154 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2020-03-31 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F155 · Peers: return on equity (profit as a share of equity), national reading · 2020-03-31 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F156 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2020-03-31 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F157 · Peers: return on equity (profit as a share of equity), peer median · 2020-03-31 · 8.3% · data/features/fct_bank_features.parquet: return_on_equity
- F158 · Peers: return on equity (profit as a share of equity), reading against its peers · 2020-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F159 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2020-03-31 · 1704.3% · data/features/fct_bank_features.parquet: texas_ratio
- F160 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2020-03-31 · 100.0th · data/features/fct_bank_features.parquet: texas_ratio
- F161 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2020-03-31 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F162 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2020-03-31 · 100.0th · data/features/fct_bank_features.parquet: texas_ratio
- F163 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2020-03-31 · 4.3% · data/features/fct_bank_features.parquet: texas_ratio
- F164 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2020-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F165 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2020-03-31 · 1.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F166 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2020-03-31 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F167 · Peers: the total risk-based capital ratio, national reading · 2020-03-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F168 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2020-03-31 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F169 · Peers: the total risk-based capital ratio, peer median · 2020-03-31 · 14.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F170 · Peers: the total risk-based capital ratio, reading against its peers · 2020-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F171 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2020-03-31 · 0.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F172 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2020-03-31 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F173 · Peers: the Tier 1 risk-based capital ratio, national reading · 2020-03-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F174 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2020-03-31 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F175 · Peers: the Tier 1 risk-based capital ratio, peer median · 2020-03-31 · 13.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F176 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2020-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F177 · Peers: losses on bonds available for sale, as a share of equity, bank value at the as-of quarter · 2020-03-31 · -40.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F178 · Peers: losses on bonds available for sale, as a share of equity, national percentile (100 = highest value among all banks) · 2020-03-31 · 0.0th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F179 · Peers: losses on bonds available for sale, as a share of equity, national reading · 2020-03-31 · unusually low · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F180 · Peers: losses on bonds available for sale, as a share of equity, percentile among its peers (100 = highest value) · 2020-03-31 · 0.0th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F181 · Peers: losses on bonds available for sale, as a share of equity, peer median · 2020-03-31 · -0.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F182 · Peers: losses on bonds available for sale, as a share of equity, reading against its peers · 2020-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F183 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2020-03-31 · 26.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F184 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2020-03-31 · 99.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F185 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2020-03-31 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F186 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2020-03-31 · 100.0th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F187 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2020-03-31 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F188 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2020-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F189 · Peers: equity as a share of assets, bank value at the as-of quarter · 2020-03-31 · 0.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F190 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2020-03-31 · 0.3rd · data/features/fct_bank_features.parquet: equity_to_assets
- F191 · Peers: equity as a share of assets, national reading · 2020-03-31 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F192 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2020-03-31 · 0.1st · data/features/fct_bank_features.parquet: equity_to_assets
- F193 · Peers: equity as a share of assets, peer median · 2020-03-31 · 10.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F194 · Peers: equity as a share of assets, reading against its peers · 2020-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F196 · Peers: ratios in the national top or bottom 10% · 2020-03-31 · 17 · data/features/fct_bank_features.parquet
- F197 · Peers: those ratios also unusual among peers · 2020-03-31 · 17 · data/features/fct_bank_features.parquet
- F199 · Peers: cut-off for unusual (top or bottom share of banks) · 2020-03-31 · 10% · data/features/fct_bank_features.parquet
