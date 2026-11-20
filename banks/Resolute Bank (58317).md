---
cert: 58317
name: "Resolute Bank"
as_of: 2019-09-30
rank: 3
n_banks: 5325
percentile: 99.962441314554
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2019-10-25
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:15:01"
writer_model: "claude-opus-5-5"
checked: true
---

# Resolute Bank (cert 58317)

*Hindsight: failed 2019-10-25. Canary flagged it 4 quarters ahead.*

## Summary

As of 2019-09-30, Resolute Bank, a small bank with total assets of $23.3 million, ranked number 3 of 5,325 banks nationally on Canary's risk score, placing it in the 100.0th percentile. Its capital cushion, the owners' money that absorbs losses, was very thin: equity was 0.7% of assets against a national median of 11.6%. It was also losing money, with a return on assets of -7.0% versus a national median of 1.1%, and it was on Canary's watchlist.

## Warning signs in the data

Capital was the clearest weak spot. The leverage ratio (core capital as a share of average assets) was 0.6%, far below the national median of 11.0%. The Tier 1 risk-based capital ratio (core capital measured against assets weighted by risk) was 1.3% versus a median of 15.6%, and the total risk-based capital ratio was 2.6% versus 16.7%.

Credit quality and profits were also poor. Loans 90 or more days past due or no longer earning interest were 3.5% of loans, well above the national median of 0.6%, and net loan write-offs (loans given up as lost, minus recoveries) were 6.2% against a median of 0.0%. The Texas ratio, which weighs troubled assets against capital plus loss reserves, was 115.1%, versus a national median of 3.7%. Return on equity was -274.3% against a median of 9.6%, and the efficiency ratio (operating costs as a share of revenue) was 145.5% against 66.8%, meaning costs exceeded revenue.

Funding and bonds point the other way and do not look stressed. Core deposits, the stable everyday kind, were 91.2% of assets versus a median of 77.3%, uninsured deposits were only 3.0% of deposits versus 19.0%, and cash was 44.8% of assets versus 6.9%. The bank held securities equal to 0.0% of assets against a median of 15.4%, so losses on bonds available for sale were 0.0% of equity, compared with a median of -0.8%. The bank was shrinking, though: assets changed by -19.9% and deposits by -15.6% over the past four quarters, while the national medians grew 4.7% and 4.4%. The real-estate concentration check found it did not cross either supervisory line, so the concern here is thin capital and loan losses rather than real estate lending.

## Understanding the score

On 2019-09-30, Resolute Bank ranked number 3 of 5,325 banks, the 100.0th percentile on a 0 to 100 scale where higher means riskier. It was flagged on Canary's watchlist, which covers the top 2% of banks, or 107 banks that quarter.

The five features that pushed the score up most were all about capital and profit. They were the Tier 1 risk-based capital ratio at 1.3% (contribution +1.951), return on equity at -274.3% (+1.347), the leverage ratio at 0.6% (+0.620), the total risk-based capital ratio at 2.6% (+0.614), and the Texas ratio at 115.1% (+0.413).

Five features pulled the score down slightly, though far less than the capital drivers pushed it up. They were interest expense at 1.0% of assets (contribution -0.287), deposit growth at -15.6% (-0.115), the efficiency ratio at 145.5% (-0.101), construction loans at 0.6% of loans (-0.083), and net interest margin, the spread earned on lending and investing, at 3.7% (-0.078).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2017-12-31 | 547 | 5,738 |  |
| 2018-03-31 | 27 | 5,674 | ▲ watchlist |
| 2018-06-30 | 18 | 5,610 | ▲ watchlist |
| 2018-09-30 | 16 | 5,544 | ▲ watchlist |
| 2018-12-31 | 10 | 5,473 | ▲ watchlist (first flag) |
| 2019-03-31 | 5 | 5,428 | ▲ watchlist |
| 2019-06-30 | 6 | 5,369 | ▲ watchlist |
| 2019-09-30 | 3 | 5,325 | ▲ watchlist |

## How its ratios moved

As of 2019-09-30, Resolute Bank ranked number 3 out of 5,325 banks nationally, placing it in the 100.0th percentile on a 0 to 100 scale where higher means riskier. A year earlier, on 2018-09-30, it sat in the 99.7th percentile, so the model rated it about the same as a year earlier. Each ratio is compared with its own history, usually the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios. Of 30 ratios checked this way, 12 were outside their own prior range, and the table shows the 6 furthest outside.

Return on equity (profit as a share of the owners' stake) was -274.3%, below its prior range of -140.1% to 3.0%, and its contribution of +1.347 model log-odds units pushed the score up. The leverage ratio (core capital, the bank's loss cushion, as a share of average assets) was 0.6%, below its prior range of 2.2% to 9.3%, and its contribution of +0.620 pushed the score up.

The efficiency ratio (operating costs as a share of revenue) was 145.5%, above its prior range of 99.4% to 123.2%, yet its contribution of -0.101 pushed the score down. Interest expense as a share of assets was 1.0%, above its prior range of 0.5% to 0.6%, yet its contribution of -0.287 pushed the score down. Loan write-offs net of recoveries (loans written off as uncollectable, minus amounts later recovered) were 6.2% of loans, above their prior range of -0.4% to 1.4%, yet their contribution of -0.019 had little effect on the score. Uninsured deposits (balances above the government insurance limit) were 3.0% of deposits, below their prior range of 6.2% to 13.3%, and their contribution of +0.049 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized loan write-offs, net of recoveries, as a share of loans | 6.2% | -0.4% to 1.4% | same quarter, prior 3 years | n/a | +6.5 pp | -0.019 | little effect on the score |
| the efficiency ratio (operating costs as a share of revenue) | 145.5% | 99.4% to 123.2% | same quarter, prior 3 years | n/a | +22.3 pp | -0.101 | pushed the score down |
| return on equity (profit as a share of equity) | -274.3% | -140.1% to 3.0% | same quarter, prior 3 years | n/a | -134.2 pp | +1.347 | pushed the score up |
| uninsured deposits as a share of deposits | 3.0% | 6.2% to 13.3% | prior 12 quarters | -10.3 pp | -8.0 pp | +0.049 | little effect on the score |
| annualized interest expense as a share of assets | 1.0% | 0.5% to 0.6% | same quarter, prior 3 years | n/a | +0.4 pp | -0.287 | pushed the score down |
| the leverage ratio (core capital as a share of average assets) | 0.6% | 2.2% to 9.3% | prior 12 quarters | -1.8 pp | -4.2 pp | +0.620 | pushed the score up |

12 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2019-09-30: Commercial Lending Specialization.

Peers: 238 banks in the same specialty group and size tier (under $100 million).

As of 2019-09-30, Resolute Bank ranked 3 out of 5,325 banks nationally on Canary's score, near the very top of the list. Its return on equity (profit as a share of the owners' stake) was -274.3%, at the 0.0th national percentile, which is unusually low, and at the 0.2nd percentile among its peers against a peer median of 6.5%, unusually low among its peers too. Its return on assets (profit as a share of everything the bank owns) was -7.0%, at the 0.1st national percentile, which is unusually low, and at the 1.1st percentile among its peers against a peer median of 0.8%, unusually low among its peers too. Its annualized loan write-offs, net of recoveries (loans given up as lost, minus amounts later collected), were 6.2% of loans, at the 99.9th national percentile, which is unusually high, and at the 98.9th percentile among its peers against a peer median of 0.0%, unusually high among its peers too. Its Texas ratio (troubled assets measured against capital plus loss reserves) was 115.1%, at the 99.8th national percentile, which is unusually high, and at the 98.5th percentile among its peers against a peer median of 5.5%, unusually high among its peers too.

Its total risk-based capital ratio (the cushion of capital against losses, measured against loans and other assets weighted by risk) was 2.6%, at the 0.0th national percentile, which is unusually low, and at the 0.2nd percentile among its peers against a peer median of 17.4%, unusually low among its peers too. Its Tier 1 risk-based capital ratio (the same idea using only the strongest, core capital) was 1.3%, at the 0.0th national percentile, which is unusually low, and at the 0.2nd percentile among its peers against a peer median of 16.4%, unusually low among its peers too. Its equity as a share of assets was 0.7%, at the 0.3rd national percentile, which is unusually low, and at the 0.2nd percentile among its peers against a peer median of 11.5%, unusually low among its peers too. Its leverage ratio (core capital as a share of average assets) was 0.6%, at the 0.3rd national percentile, which is unusually low, and at the 0.2nd percentile among its peers against a peer median of 11.1%, unusually low among its peers too.

Overall, 19 of the bank's ratios fell in the national top or bottom 10%, and 18 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -274.3% | 0.0th (unusually low) | 6.5% | 0.2nd | unusually low among its peers too |
| the total risk-based capital ratio | 2.6% | 0.0th (unusually low) | 17.4% | 0.2nd | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 1.3% | 0.0th (unusually low) | 16.4% | 0.2nd | unusually low among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 6.2% | 99.9th (unusually high) | 0.0% | 98.9th | unusually high among its peers too |
| return on assets (profit as a share of assets) | -7.0% | 0.1st (unusually low) | 0.8% | 1.1st | unusually low among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 115.1% | 99.8th (unusually high) | 5.5% | 98.5th | unusually high among its peers too |
| equity as a share of assets | 0.7% | 0.3rd (unusually low) | 11.5% | 0.2nd | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | 0.6% | 0.3rd (unusually low) | 11.1% | 0.2nd | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: total risk-based capital, as the 2006 guidance specifies.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 25.9% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 758.1% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | -34.9% | 50% or more | no |

It did not cross the construction line.
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, Canary caught this bank early: it failed on 2019-10-25. The model first flagged it at the 2018-12-31 quarter, a lead time of 4 quarters before the failure.

At that first flag, the main drivers were already about losses and troubled loans. Return on equity was -133.7% (contribution +1.036), assets had shrunk by -36.0% over four quarters (+0.441), and the Texas ratio was 83.4% (+0.403). Loans 90 or more days past due or not accruing were 9.5% of loans (+0.328), and return on assets was -7.9% (+0.272).

## What happened next

In hindsight, the bank's last reported quarter was 2019-09-30, the same quarter this memo describes, when it ranked number 3 nationally. Resolute Bank failed on 2019-10-25 and filed no later reports, so there are no further ranks or flags.

## Sources

- F1 · Bank name · n/a · Resolute Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2019-09-30 · 3 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2019-09-30 · 5,325 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2019-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2019-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2019-09-30 · 107 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2019-09-30 · 0.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2019-09-30 · 11.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 0.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2019-09-30 · 1.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2019-09-30 · 15.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2019-09-30 · 2.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2019-09-30 · 16.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 3.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2019-09-30 · 6.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 115.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 3.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2019-09-30 · -7.0% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2019-09-30 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2019-09-30 · -274.3% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2019-09-30 · 9.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 145.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 66.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2019-09-30 · 3.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2019-09-30 · 19.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2019-09-30 · 91.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2019-09-30 · 77.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2019-09-30 · 44.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2019-09-30 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2019-09-30 · -0.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2019-09-30 · 15.4% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F69 · Bank: total assets · 2019-09-30 · $23.3 million · data/features/fct_bank_features.parquet: log_total_assets
- F71 · Bank: asset growth over the past four quarters · 2019-09-30 · -19.9% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2019-09-30 · 4.7% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2019-09-30 · -15.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2019-09-30 · 4.4% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 1.3%; contribution to the score · 2019-09-30 · +1.951 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -274.3%; contribution to the score · 2019-09-30 · +1.347 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the leverage ratio (core capital as a share of average assets), value 0.6%; contribution to the score · 2019-09-30 · +0.620 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 2.6%; contribution to the score · 2019-09-30 · +0.614 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: the Texas ratio (troubled assets against capital plus reserves), value 115.1%; contribution to the score · 2019-09-30 · +0.413 · data/analyst/scores.parquet: feature texas_ratio contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 1.0%; contribution to the score · 2019-09-30 · -0.287 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: deposit growth over the past four quarters, value -15.6%; contribution to the score · 2019-09-30 · -0.115 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F82 · Driver down #3: the efficiency ratio (operating costs as a share of revenue), value 145.5%; contribution to the score · 2019-09-30 · -0.101 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F83 · Driver down #4: construction loans as a share of loans, value 0.6%; contribution to the score · 2019-09-30 · -0.083 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F84 · Driver down #5: net interest margin (the spread earned on lending and investing), value 3.7%; contribution to the score · 2019-09-30 · -0.078 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F85 · Failure date · 2019-10-25 · 2019-10-25 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2018-12-31 · 2018-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2018-12-31: return on equity (profit as a share of equity), value -133.7%; contribution to the score · 2018-12-31 · +1.036 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2018-12-31: asset growth over the past four quarters, value -36.0%; contribution to the score · 2018-12-31 · +0.441 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F90 · Driver up #3 at 2018-12-31: the Texas ratio (troubled assets against capital plus reserves), value 83.4%; contribution to the score · 2018-12-31 · +0.403 · data/analyst/scores.parquet: feature texas_ratio contribution
- F91 · Driver up #4 at 2018-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 9.5%; contribution to the score · 2018-12-31 · +0.328 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2018-12-31: return on assets (profit as a share of assets), value -7.9%; contribution to the score · 2018-12-31 · +0.272 · data/analyst/scores.parquet: feature return_on_assets contribution
- F98 · Last quarter the bank reported · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2019-09-30 · 6.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F100 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · -0.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F101 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F103 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2019-09-30 · -0.019 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F104 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2019-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2019-09-30 · 145.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 99.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 123.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F109 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2019-09-30 · -0.101 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2019-09-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F111 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2019-09-30 · -274.3% · data/features/fct_bank_features.parquet: return_on_equity
- F112 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -140.1% · data/features/fct_bank_features.parquet: return_on_equity
- F113 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 3.0% · data/features/fct_bank_features.parquet: return_on_equity
- F115 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2019-09-30 · +1.347 · data/analyst/scores.parquet: feature return_on_equity contribution
- F116 · Trend: return on equity (profit as a share of equity), what the model did with it · 2019-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F117 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2019-09-30 · 3.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F118 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 6.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F119 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 13.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F122 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2019-09-30 · +0.049 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F123 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2019-09-30 · little effect on the score · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F124 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2019-09-30 · 1.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F125 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F126 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 0.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F128 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2019-09-30 · -0.287 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F129 · Trend: annualized interest expense as a share of assets, what the model did with it · 2019-09-30 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F130 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2019-09-30 · 0.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F131 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F132 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 9.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F135 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2019-09-30 · +0.620 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F136 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2019-09-30 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F137 · Trend: ratios outside their own prior range · 2019-09-30 · 12 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios shown in the table (the furthest outside their prior range) · 2019-09-30 · 6 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios compared with their own prior range · 2019-09-30 · 30 · data/features/fct_bank_features.parquet
- F140 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F142 · Percentile a year earlier (100 = highest risk) · 2018-09-30 · 99.7% · data/analyst/scores.parquet: percentile
- F143 · Trend: how the model's rating compares with a year earlier · 2019-09-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F147 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2019-09-30 · -274.3% · data/features/fct_bank_features.parquet: return_on_equity
- F148 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2019-09-30 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F149 · Peers: return on equity (profit as a share of equity), national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F150 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2019-09-30 · 0.2nd · data/features/fct_bank_features.parquet: return_on_equity
- F151 · Peers: return on equity (profit as a share of equity), peer median · 2019-09-30 · 6.5% · data/features/fct_bank_features.parquet: return_on_equity
- F152 · Peers: return on equity (profit as a share of equity), reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F153 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2019-09-30 · 2.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F154 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2019-09-30 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F155 · Peers: the total risk-based capital ratio, national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F156 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2019-09-30 · 0.2nd · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F157 · Peers: the total risk-based capital ratio, peer median · 2019-09-30 · 17.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F158 · Peers: the total risk-based capital ratio, reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F159 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2019-09-30 · 1.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F160 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2019-09-30 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F161 · Peers: the Tier 1 risk-based capital ratio, national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F162 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2019-09-30 · 0.2nd · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F163 · Peers: the Tier 1 risk-based capital ratio, peer median · 2019-09-30 · 16.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F164 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F165 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2019-09-30 · 6.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F166 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2019-09-30 · 99.9th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F167 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2019-09-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F168 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2019-09-30 · 98.9th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F169 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F170 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2019-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F171 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2019-09-30 · -7.0% · data/features/fct_bank_features.parquet: return_on_assets
- F172 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2019-09-30 · 0.1st · data/features/fct_bank_features.parquet: return_on_assets
- F173 · Peers: return on assets (profit as a share of assets), national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F174 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2019-09-30 · 1.1st · data/features/fct_bank_features.parquet: return_on_assets
- F175 · Peers: return on assets (profit as a share of assets), peer median · 2019-09-30 · 0.8% · data/features/fct_bank_features.parquet: return_on_assets
- F176 · Peers: return on assets (profit as a share of assets), reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F177 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2019-09-30 · 115.1% · data/features/fct_bank_features.parquet: texas_ratio
- F178 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2019-09-30 · 99.8th · data/features/fct_bank_features.parquet: texas_ratio
- F179 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2019-09-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F180 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2019-09-30 · 98.5th · data/features/fct_bank_features.parquet: texas_ratio
- F181 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2019-09-30 · 5.5% · data/features/fct_bank_features.parquet: texas_ratio
- F182 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2019-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F183 · Peers: equity as a share of assets, bank value at the as-of quarter · 2019-09-30 · 0.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F184 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2019-09-30 · 0.3rd · data/features/fct_bank_features.parquet: equity_to_assets
- F185 · Peers: equity as a share of assets, national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F186 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2019-09-30 · 0.2nd · data/features/fct_bank_features.parquet: equity_to_assets
- F187 · Peers: equity as a share of assets, peer median · 2019-09-30 · 11.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F188 · Peers: equity as a share of assets, reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F189 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2019-09-30 · 0.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F190 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2019-09-30 · 0.3rd · data/features/fct_bank_features.parquet: leverage_ratio
- F191 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F192 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2019-09-30 · 0.2nd · data/features/fct_bank_features.parquet: leverage_ratio
- F193 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2019-09-30 · 11.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F194 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F196 · Peers: ratios in the national top or bottom 10% · 2019-09-30 · 19 · data/features/fct_bank_features.parquet
- F197 · Peers: those ratios also unusual among peers · 2019-09-30 · 18 · data/features/fct_bank_features.parquet
- F199 · Peers: cut-off for unusual (top or bottom share of banks) · 2019-09-30 · 10% · data/features/fct_bank_features.parquet
