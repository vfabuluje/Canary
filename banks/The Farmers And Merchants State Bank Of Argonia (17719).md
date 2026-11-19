---
cert: 17719
name: "The Farmers And Merchants State Bank Of Argonia"
as_of: 2017-09-30
rank: 1
n_banks: 5806
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-10-13
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:05:15"
writer_model: "claude-opus-5-5"
checked: true
---

# The Farmers And Merchants State Bank Of Argonia (cert 17719)

*Hindsight: failed 2017-10-13. Canary flagged it 4 quarters ahead.*

## Summary

As of 2017-09-30, The Farmers And Merchants State Bank Of Argonia, based in KS, ranked 1 out of 5,806 banks nationally on Canary's risk score, which places it in the 100.0th percentile. It was on Canary's watchlist, which covers the riskiest 2% of banks. Its capital, the owners' cushion against losses, was below zero, with equity at -1.1% of assets against a national median of 11.0%, and 11.5% of its loans were 90+ days past due or not accruing interest against a median of 0.6%. It was also losing money, with a return on assets of -10.5% compared with a national median of 0.9%.

## Warning signs in the data

Capital, the money owners have at stake to absorb losses, was negative on every measure as of 2017-09-30. Equity was -1.1% of assets against a national median of 11.0%, and the leverage ratio (core capital as a share of average assets) was -1.3% against a median of 10.6%. The Tier 1 risk-based capital ratio, which measures core capital against assets weighted by their riskiness, was -2.3% versus a median of 15.1%, and the total risk-based capital ratio was -1.0% versus 16.3%.

Credit quality, meaning whether borrowers repay, was very weak: 11.5% of loans were 90+ days past due or not accruing interest, far above the national median of 0.6%, and loans 30-89 days past due were 3.0% of assets against 0.3%. Nonaccrual assets and foreclosed property made up 9.1% of assets against a median of 0.5%, and the Texas ratio (troubled assets against capital plus reserves) stood at 292.3% versus 4.5%. The bank was writing off loans at an annualized 10.5% of loans, net of recoveries, against a median of 0.0%, and its provision for loan losses, the expense set aside for expected bad loans, was 8.1% of assets against 0.1%. Its loan-loss reserves were 6.1% of loans, well above the median of 1.2%.

On funding, brokered deposits (money placed through third-party brokers) were 10.3% of deposits against a national median of 0.0%, and Federal Home Loan Bank borrowings were 13.8% of assets against 0.9%. Volatile funding was 13.1% of assets versus 5.9%, core deposits, the stable everyday deposits, were 68.5% of assets versus 77.9%, and deposits shrank -9.9% over the past four quarters while the median grew 3.8%. Cash was high at 20.8% of assets against a median of 6.1%, and losses on bonds available for sale were -5.0% of equity against a median of 0.0%.

## Understanding the score

As of 2017-09-30, the bank ranked 1 out of 5,806 banks, the 100.0th percentile on a scale where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks and contained 117 banks that quarter.

The five factors that pushed the score up most were the Tier 1 risk-based capital ratio at -2.3% (+2.007), return on equity at -282.8% (+1.348), the Texas ratio at 292.3% (+1.262), the leverage ratio at -1.3% (+0.692), and the total risk-based capital ratio at -1.0% (+0.562).

The five factors that pulled the score down most were interest expense at 0.9% of assets (-0.635), losses on bonds available for sale at -5.0% of equity (-0.248), construction loans at 0.5% of loans (-0.168), deposit growth over the past four quarters at -9.9% (-0.125), and net interest margin, the spread earned on lending and investing, at 4.2% (-0.122).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 375 | 6,193 |  |
| 2016-06-30 | 426 | 6,129 |  |
| 2016-09-30 | 108 | 6,051 | ▲ watchlist |
| 2016-12-31 | 22 | 5,983 | ▲ watchlist (first flag) |
| 2017-03-31 | 12 | 5,925 | ▲ watchlist |
| 2017-06-30 | 3 | 5,856 | ▲ watchlist |
| 2017-09-30 | 1 | 5,806 | ▲ watchlist |

## How its ratios moved

Canary compares each ratio with the bank's own history, using the prior 12 quarters for most ratios and the same quarter in the prior 3 years for year-to-date ratios. As of 2017-09-30, 20 of 30 ratios checked sat outside their own prior range. Return on equity was -282.8%, far below its prior range of 6.4% to 8.2%, and it pushed the score up with a contribution of +1.348 model log-odds units. Return on assets was -10.5% against a prior range of 0.5% to 0.6%, and it pushed the score up by +0.141. The provision for loan losses was 8.1% of assets against a prior range of 0.0% to 0.1%, and it pushed the score up by +0.143.

Some ratios were far outside their range yet had little effect on the score. Net loan write-offs were 10.5% of loans against a prior range of 0.0% to 0.3%, yet they had little effect on the score, at -0.011. The efficiency ratio (operating costs as a share of revenue) was 139.0% against a prior range of 82.9% to 87.9%, yet it had little effect on the score, at -0.027. Cash was 20.8% of assets against a prior range of 2.2% to 6.1%, up +17.6 pp in one quarter, yet it had little effect on the score, at -0.016.

A year earlier, on 2016-09-30, the bank stood at the 98.2th percentile, and the model rated it riskier than a year earlier, ranking it 1 out of 5,806 as of 2017-09-30.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -282.8% | 6.4% to 8.2% | same quarter, prior 3 years | n/a | -291.0 pp | +1.348 | pushed the score up |
| return on assets (profit as a share of assets) | -10.5% | 0.5% to 0.6% | same quarter, prior 3 years | n/a | -11.1 pp | +0.141 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 10.5% | 0.0% to 0.3% | same quarter, prior 3 years | n/a | +10.2 pp | -0.011 | little effect on the score |
| the efficiency ratio (operating costs as a share of revenue) | 139.0% | 82.9% to 87.9% | same quarter, prior 3 years | n/a | +52.5 pp | -0.027 | little effect on the score |
| annualized provision for loan losses as a share of assets | 8.1% | 0.0% to 0.1% | same quarter, prior 3 years | n/a | +8.0 pp | +0.143 | pushed the score up |
| cash as a share of assets | 20.8% | 2.2% to 6.1% | prior 12 quarters | +17.6 pp | +18.4 pp | -0.016 | little effect on the score |

20 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2017-09-30: Agricultural Specialization.

Peers: 630 banks in the same specialty group and size tier (under $100 million).

Equity as a share of assets was -1.1%, at the 0.0th percentile nationally, which is unusually low, and at the 0.1st percentile among its peers, whose median was 11.6%, so it was unusually low among its peers too. The leverage ratio was -1.3%, at the 0.0th percentile nationally, unusually low, and at the 0.1st percentile among peers with a peer median of 11.4%, unusually low among its peers too. The Tier 1 risk-based capital ratio was -2.3%, at the 0.0th percentile nationally, unusually low, and at the 0.1st percentile among peers with a peer median of 17.6%, unusually low among its peers too. The total risk-based capital ratio was -1.0%, at the 0.0th percentile nationally, unusually low, and at the 0.1st percentile among peers with a peer median of 18.7%, unusually low among its peers too.

Return on equity was -282.8%, at the 0.0th percentile nationally, unusually low, and at the 0.1st percentile among peers with a peer median of 8.0%, unusually low among its peers too. Return on assets was -10.5%, at the 0.1st percentile nationally, unusually low, and at the 0.1st percentile among peers with a peer median of 0.9%, unusually low among its peers too. Net loan write-offs were 10.5% of loans, at the 100.0th percentile nationally, unusually high, and at the 99.9th percentile among peers with a peer median of 0.0%, unusually high among its peers too. The provision for loan losses was 8.1% of assets, at the 99.9th percentile nationally, unusually high, and at the 99.9th percentile among peers with a peer median of 0.0%, unusually high among its peers too.

Overall, 21 of the bank's ratios fell in the national top or bottom 10%, and 19 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| equity as a share of assets | -1.1% | 0.0th (unusually low) | 11.6% | 0.1st | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | -1.3% | 0.0th (unusually low) | 11.4% | 0.1st | unusually low among its peers too |
| return on equity (profit as a share of equity) | -282.8% | 0.0th (unusually low) | 8.0% | 0.1st | unusually low among its peers too |
| the total risk-based capital ratio | -1.0% | 0.0th (unusually low) | 18.7% | 0.1st | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | -2.3% | 0.0th (unusually low) | 17.6% | 0.1st | unusually low among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 10.5% | 100.0th (unusually high) | 0.0% | 99.9th | unusually high among its peers too |
| return on assets (profit as a share of assets) | -10.5% | 0.1st (unusually low) | 0.9% | 0.1st | unusually low among its peers too |
| annualized provision for loan losses as a share of assets | 8.1% | 99.9th (unusually high) | 0.0% | 99.9th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: total risk-based capital, as the 2006 guidance specifies.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | n/a | 100% or more | n/a |
| Total commercial real estate loans ÷ capital | n/a | 300% or more | n/a |
| Growth in commercial real estate loans over the prior 36 months | n/a | 50% or more | n/a |

The construction line can't be checked: the bank's capital was zero or negative this quarter.
The total commercial real estate line can't be checked: the bank's capital was zero or negative this quarter.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, Canary first flagged the bank in the quarter ending 2016-12-31, 4 quarters before it failed on 2017-10-13. At that first flag, the main factors pushing the score up were loans 90+ days past due or not accruing interest at 12.1% of loans (+0.956), the Texas ratio at 115.6% (+0.747), and loans 30-89 days past due at 4.0% of assets (+0.575). The provision for loan losses at 1.7% of assets (+0.286) and commercial real estate loans at 10.7% of loans (+0.164) also pushed it up. Pulling it down then were low interest expense at 0.6% of assets (-1.436) and a Tier 1 risk-based capital ratio that was still positive at 9.1% (-0.226).

## What happened next

In hindsight, the bank failed on 2017-10-13, shortly after the as-of quarter. Its last reported quarter was 2017-09-30, when it ranked 1 out of 5,806 banks, and it stopped reporting after that. Our data does not by itself distinguish a merger from a closure when a bank stops reporting, but the failure date confirms how this case ended.

## Sources

- F1 · Bank name · n/a · The Farmers And Merchants State Bank Of Argonia · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2017-09-30 · 2017-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KS · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2017-09-30 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2017-09-30 · 5,806 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2017-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2017-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2017-09-30 · 117 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2017-09-30 · -1.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2017-09-30 · 11.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2017-09-30 · -1.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2017-09-30 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2017-09-30 · -2.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2017-09-30 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2017-09-30 · -1.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2017-09-30 · 16.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2017-09-30 · 11.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2017-09-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2017-09-30 · 9.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2017-09-30 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2017-09-30 · 3.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2017-09-30 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2017-09-30 · 6.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2017-09-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2017-09-30 · 10.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2017-09-30 · 8.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2017-09-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2017-09-30 · 292.3% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2017-09-30 · 4.5% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2017-09-30 · -10.5% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2017-09-30 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2017-09-30 · 10.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2017-09-30 · 68.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2017-09-30 · 77.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2017-09-30 · 13.8% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2017-09-30 · 0.9% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2017-09-30 · 13.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2017-09-30 · 5.9% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2017-09-30 · 20.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2017-09-30 · 6.1% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2017-09-30 · -5.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2017-09-30 · -9.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2017-09-30 · 3.8% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value -2.3%; contribution to the score · 2017-09-30 · +2.007 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -282.8%; contribution to the score · 2017-09-30 · +1.348 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 292.3%; contribution to the score · 2017-09-30 · +1.262 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value -1.3%; contribution to the score · 2017-09-30 · +0.692 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: the total risk-based capital ratio, value -1.0%; contribution to the score · 2017-09-30 · +0.562 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.9%; contribution to the score · 2017-09-30 · -0.635 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: losses on bonds available for sale, as a share of equity, value -5.0%; contribution to the score · 2017-09-30 · -0.248 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F82 · Driver down #3: construction loans as a share of loans, value 0.5%; contribution to the score · 2017-09-30 · -0.168 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: deposit growth over the past four quarters, value -9.9%; contribution to the score · 2017-09-30 · -0.125 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F84 · Driver down #5: net interest margin (the spread earned on lending and investing), value 4.2%; contribution to the score · 2017-09-30 · -0.122 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F85 · Failure date · 2017-10-13 · 2017-10-13 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-12-31 · 2016-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 12.1%; contribution to the score · 2016-12-31 · +0.956 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F89 · Driver up #2 at 2016-12-31: the Texas ratio (troubled assets against capital plus reserves), value 115.6%; contribution to the score · 2016-12-31 · +0.747 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2016-12-31: loans 30-89 days past due, as a share of assets, value 4.0%; contribution to the score · 2016-12-31 · +0.575 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F91 · Driver up #4 at 2016-12-31: annualized provision for loan losses as a share of assets, value 1.7%; contribution to the score · 2016-12-31 · +0.286 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F92 · Driver up #5 at 2016-12-31: commercial real estate loans as a share of loans, value 10.7%; contribution to the score · 2016-12-31 · +0.164 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F93 · Driver down #1 at 2016-12-31: annualized interest expense as a share of assets, value 0.6%; contribution to the score · 2016-12-31 · -1.436 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F95 · Driver down #3 at 2016-12-31: the Tier 1 risk-based capital ratio, value 9.1%; contribution to the score · 2016-12-31 · -0.226 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2017-09-30 · 2017-09-30 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2017-09-30 · -282.8% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 6.4% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 8.2% · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2017-09-30 · +1.348 · data/analyst/scores.parquet: feature return_on_equity contribution
- F104 · Trend: return on equity (profit as a share of equity), what the model did with it · 2017-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F105 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2017-09-30 · -10.5% · data/features/fct_bank_features.parquet: return_on_assets
- F106 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: return_on_assets
- F107 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2017-09-30 · +0.141 · data/analyst/scores.parquet: feature return_on_assets contribution
- F110 · Trend: return on assets (profit as a share of assets), what the model did with it · 2017-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F111 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2017-09-30 · 10.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F112 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F113 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F115 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2017-09-30 · -0.011 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F116 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2017-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F117 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2017-09-30 · 139.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F118 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 82.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F119 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 87.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F121 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2017-09-30 · -0.027 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F122 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2017-09-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F123 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2017-09-30 · 8.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F124 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F125 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F127 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2017-09-30 · +0.143 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F128 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2017-09-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F129 · Trend: cash as a share of assets, value at the as-of quarter · 2017-09-30 · 20.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F130 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F131 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 6.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F132 · Trend: cash as a share of assets, change over one quarter, in percentage points · 2017-09-30 · +17.6 pp · data/features/fct_bank_features.parquet: cash_to_assets
- F134 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2017-09-30 · -0.016 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F135 · Trend: cash as a share of assets, what the model did with it · 2017-09-30 · little effect on the score · data/analyst/scores.parquet: feature cash_to_assets contribution
- F136 · Trend: ratios outside their own prior range · 2017-09-30 · 20 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios compared with their own prior range · 2017-09-30 · 30 · data/features/fct_bank_features.parquet
- F139 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F140 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F141 · Percentile a year earlier (100 = highest risk) · 2016-09-30 · 98.2% · data/analyst/scores.parquet: percentile
- F142 · Trend: how the model's rating compares with a year earlier · 2017-09-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F146 · Peers: equity as a share of assets, bank value at the as-of quarter · 2017-09-30 · -1.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F147 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2017-09-30 · 0.0th · data/features/fct_bank_features.parquet: equity_to_assets
- F148 · Peers: equity as a share of assets, national reading · 2017-09-30 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F149 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2017-09-30 · 0.1st · data/features/fct_bank_features.parquet: equity_to_assets
- F150 · Peers: equity as a share of assets, peer median · 2017-09-30 · 11.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F151 · Peers: equity as a share of assets, reading against its peers · 2017-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F152 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2017-09-30 · -1.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F153 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2017-09-30 · 0.0th · data/features/fct_bank_features.parquet: leverage_ratio
- F154 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2017-09-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F155 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2017-09-30 · 0.1st · data/features/fct_bank_features.parquet: leverage_ratio
- F156 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2017-09-30 · 11.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F157 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2017-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F158 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2017-09-30 · -282.8% · data/features/fct_bank_features.parquet: return_on_equity
- F159 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2017-09-30 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F160 · Peers: return on equity (profit as a share of equity), national reading · 2017-09-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F161 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2017-09-30 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F162 · Peers: return on equity (profit as a share of equity), peer median · 2017-09-30 · 8.0% · data/features/fct_bank_features.parquet: return_on_equity
- F163 · Peers: return on equity (profit as a share of equity), reading against its peers · 2017-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F164 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2017-09-30 · -1.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F165 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2017-09-30 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F166 · Peers: the total risk-based capital ratio, national reading · 2017-09-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F167 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2017-09-30 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F168 · Peers: the total risk-based capital ratio, peer median · 2017-09-30 · 18.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F169 · Peers: the total risk-based capital ratio, reading against its peers · 2017-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F170 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2017-09-30 · -2.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F171 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2017-09-30 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F172 · Peers: the Tier 1 risk-based capital ratio, national reading · 2017-09-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F173 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2017-09-30 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F174 · Peers: the Tier 1 risk-based capital ratio, peer median · 2017-09-30 · 17.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F175 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2017-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F176 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2017-09-30 · 10.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F177 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2017-09-30 · 100.0th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F178 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2017-09-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F179 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2017-09-30 · 99.9th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F180 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F181 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2017-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F182 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2017-09-30 · -10.5% · data/features/fct_bank_features.parquet: return_on_assets
- F183 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2017-09-30 · 0.1st · data/features/fct_bank_features.parquet: return_on_assets
- F184 · Peers: return on assets (profit as a share of assets), national reading · 2017-09-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F185 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2017-09-30 · 0.1st · data/features/fct_bank_features.parquet: return_on_assets
- F186 · Peers: return on assets (profit as a share of assets), peer median · 2017-09-30 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F187 · Peers: return on assets (profit as a share of assets), reading against its peers · 2017-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F188 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2017-09-30 · 8.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F189 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2017-09-30 · 99.9th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F190 · Peers: annualized provision for loan losses as a share of assets, national reading · 2017-09-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F191 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2017-09-30 · 99.9th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F192 · Peers: annualized provision for loan losses as a share of assets, peer median · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F193 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2017-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F195 · Peers: ratios in the national top or bottom 10% · 2017-09-30 · 21 · data/features/fct_bank_features.parquet
- F196 · Peers: those ratios also unusual among peers · 2017-09-30 · 19 · data/features/fct_bank_features.parquet
- F198 · Peers: cut-off for unusual (top or bottom share of banks) · 2017-09-30 · 10% · data/features/fct_bank_features.parquet
