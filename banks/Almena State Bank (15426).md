---
cert: 15426
name: "Almena State Bank"
as_of: 2020-09-30
rank: 1
n_banks: 5098
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2020-10-23
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:14:02"
writer_model: "claude-opus-5-5"
checked: true
---

# Almena State Bank (cert 15426)

*Hindsight: failed 2020-10-23. Canary flagged it 4 quarters ahead.*

## Summary

As of 2020-09-30, Almena State Bank, a Kansas bank with $65.7 million in assets, ranked 1 out of 5,098 banks nationally, placing it in the 100.0th percentile, and it was on Canary's watchlist. Its capital cushion, the owners' money that absorbs losses, had all but disappeared, with equity at 0.0% of assets against a national median of 10.9%. Problem loans were very high and the bank was losing money: loans 90 or more days past due or not accruing interest were 23.8% of loans against a national median of 0.5%, and return on assets was -7.3%.

## Warning signs in the data

Capital was the weakest point: equity was 0.0% of assets against a national median of 10.9%, the leverage ratio (core capital as a share of average assets) was 0.0% against 10.2%, and the total risk-based capital ratio (capital against assets weighted by their riskiness) was 1.4% against 15.9%. Credit quality was also poor: loans 90 or more days past due or not accruing interest were 23.8% of loans against a national median of 0.5%, and nonaccrual assets and foreclosed property were 19.4% of assets against 0.3%. The Texas ratio, which weighs troubled assets against capital plus reserves, was 243.0% against a national median of 3.4%, while net loan write-offs ran at 2.8% of loans against 0.0%.

Earnings were deeply negative, with return on assets at -7.3% against a national median of 1.0%, and the efficiency ratio (operating costs as a share of revenue) at 207.1% against 65.6%. Losses on bonds available for sale (paper losses on bonds the bank could sell) equaled -34.5% of equity against a national median of -2.5%. As the trend section notes, the model treated this bond figure as pushing the score down rather than up, so the raw data and the model point different ways on this one item.

Funding also points two ways: core deposits (stable, everyday deposits) were 97.2% of assets against a national median of 78.8%, and uninsured deposits were only 2.4% of deposits against 21.3%. On the other hand, brokered deposits (money gathered through third-party brokers) were 31.4% of deposits against a national median of 0.0%, and deposit growth over the past four quarters was -15.7% against a median of 15.0%.

## Understanding the score

As of 2020-09-30, Almena State Bank ranked 1 out of 5,098 banks, the 100.0th percentile on a 0 to 100 scale where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks by score, or 102 banks that quarter.

The five features that pushed the score up most were the Tier 1 risk-based capital ratio (highest-quality capital against risk-weighted assets) at 0.0%, return on equity (profit as a share of the owners' stake) at -233.5%, the Texas ratio at 243.0%, loans 90 or more days past due or not accruing interest at 23.8% of loans, and the total risk-based capital ratio at 1.4%. The five that pulled it down most were losses on bonds available for sale at -34.5% of equity, deposit growth over the past four quarters at -15.7%, construction loans at 0.0% of loans, loans 30-89 days past due at 1.2% of assets, and volatile funding (money that can leave quickly) at 2.0% of assets. These downward pulls were small next to the upward ones.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2018-12-31 | 15 | 5,473 | ▲ watchlist |
| 2019-03-31 | 7 | 5,428 | ▲ watchlist |
| 2019-06-30 | 5 | 5,369 | ▲ watchlist |
| 2019-09-30 | 6 | 5,325 | ▲ watchlist |
| 2019-12-31 | 5 | 5,244 | ▲ watchlist (first flag) |
| 2020-03-31 | 6 | 5,182 | ▲ watchlist |
| 2020-06-30 | 1 | 5,131 | ▲ watchlist |
| 2020-09-30 | 1 | 5,098 | ▲ watchlist |

## How its ratios moved

As of Q3 2020, Almena State Bank ranked 1 out of 5,098 banks nationally, placing it in the 100.0th percentile on a scale where higher means riskier. A year earlier, at 2019-09-30, it sat in the 99.9th percentile, and the model's rating is about the same as a year earlier. Of 30 ratios compared with their own prior range, 16 were outside it; most ratios are compared with the prior 12 quarters, and year-to-date ratios with the same quarter in the prior 3 years.

Return on equity (profit as a share of the owners' stake) was -233.5%, below its prior range of -119.7% to 38.7%, and at +1.440 model log-odds units it pushed the score up. Net interest margin (the spread earned on lending and investing) was 2.4%, below its prior range of 4.0% to 5.3%, and at +0.119 it pushed the score up. Loan-loss reserves (money set aside to cover loans that may go bad) were 10.5% of loans, above their prior range of 1.1% to 8.3%, and at +0.084 they pushed the score up.

Losses on bonds available for sale (paper losses on bonds the bank could sell) equaled -34.5% of equity, well outside the prior range of -2.5% to 1.4%, yet at -0.250 this ratio pushed the score down. The efficiency ratio (operating costs as a share of revenue) was 207.1%, far above its prior range of 52.6% to 86.1%, but at -0.036 it had little effect on the score. Cash as a share of assets was 9.9%, above its prior range of 1.1% to 3.3%, but at +0.006 it had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| losses on bonds available for sale, as a share of equity | -34.5% | -2.5% to 1.4% | prior 12 quarters | -32.2 pp | -33.4 pp | -0.250 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 207.1% | 52.6% to 86.1% | same quarter, prior 3 years | n/a | +121.0 pp | -0.036 | little effect on the score |
| cash as a share of assets | 9.9% | 1.1% to 3.3% | prior 12 quarters | +8.7 pp | +8.1 pp | +0.006 | little effect on the score |
| net interest margin (the spread earned on lending and investing) | 2.4% | 4.0% to 5.3% | same quarter, prior 3 years | n/a | -1.6 pp | +0.119 | pushed the score up |
| return on equity (profit as a share of equity) | -233.5% | -119.7% to 38.7% | same quarter, prior 3 years | n/a | -113.8 pp | +1.440 | pushed the score up |
| loan-loss reserves as a share of loans | 10.5% | 1.1% to 8.3% | prior 12 quarters | +2.2 pp | +4.3 pp | +0.084 | pushed the score up |

16 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2020-09-30: Agricultural Specialization.

Peers: 429 banks in the same specialty group and size tier (under $100 million).

Nonaccrual assets and foreclosed property (loans no longer earning interest plus repossessed property) were 19.4% of assets, at the 100.0th percentile nationally, which is unusually high; at the 99.9th percentile among its peers, against a peer median of 0.2%, this reading is unusually high among its peers too. Loans 90 or more days past due or not accruing interest were 23.8% of loans, at the 99.9th percentile nationally, which is unusually high; at the 99.9th percentile among its peers, against a peer median of 0.4%, this reading is unusually high among its peers too. The Texas ratio (troubled assets measured against capital plus loss reserves) was 243.0%, at the 100.0th percentile nationally, which is unusually high; at the 99.9th percentile among its peers, against a peer median of 2.5%, this reading is unusually high among its peers too.

The total risk-based capital ratio (the bank's capital cushion measured against its assets, weighted by how likely they are to lose value) was 1.4%, at the 0.0th percentile nationally, which is unusually low; at the 0.2nd percentile among its peers, against a peer median of 18.8%, this reading is unusually low among its peers too. The Tier 1 risk-based capital ratio (the same measure using only the highest-quality capital) was 0.0%, at the 0.0th percentile nationally, which is unusually low; at the 0.2nd percentile among its peers, against a peer median of 17.7%, this reading is unusually low among its peers too. Return on equity (profit as a share of the owners' stake) was -233.5%, at the 0.0th percentile nationally, which is unusually low; at the 0.1st percentile among its peers, against a peer median of 7.0%, this reading is unusually low among its peers too. Losses on bonds available for sale (bonds the bank could sell, marked at market value) were -34.5% of equity, at the 0.1st percentile nationally, which is unusually low; at the 0.1st percentile among its peers, against a peer median of -2.1%, this reading is unusually low among its peers too.

Core deposits (stable, everyday customer deposits) were 97.2% of assets, at the 100.0th percentile nationally, which is unusually high; at the 99.9th percentile among its peers, against a peer median of 80.8%, this reading is unusually high among its peers too. Overall, 23 of the bank's ratios fell in the national top or bottom 10%, and 21 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| nonaccrual assets and foreclosed property, as a share of assets | 19.4% | 100.0th (unusually high) | 0.2% | 99.9th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -233.5% | 0.0th (unusually low) | 7.0% | 0.1st | unusually low among its peers too |
| the total risk-based capital ratio | 1.4% | 0.0th (unusually low) | 18.8% | 0.2nd | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 0.0% | 0.0th (unusually low) | 17.7% | 0.2nd | unusually low among its peers too |
| core deposits as a share of assets | 97.2% | 100.0th (unusually high) | 80.8% | 99.9th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 243.0% | 100.0th (unusually high) | 2.5% | 99.9th | unusually high among its peers too |
| losses on bonds available for sale, as a share of equity | -34.5% | 0.1st (unusually low) | -2.1% | 0.1st | unusually low among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 23.8% | 99.9th (unusually high) | 0.4% | 99.9th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 219.5% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -1.5% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, Almena State Bank failed on 2020-10-23. Canary first flagged it in the quarter ending 2019-12-31, a lead time of 4 quarters before the failure. At that first flag, the main features pushing the score up were return on equity at -100.1%, the Texas ratio at 189.3%, the Tier 1 risk-based capital ratio at 5.9%, loans 90 or more days past due or not accruing interest at 22.9% of loans, and brokered deposits at 26.3% of deposits. The same problems of losses, troubled loans and thin capital were therefore already visible well before the end.

## What happened next

In hindsight, the bank failed on October 23, 2020, shortly after the as-of quarter. Its last reported quarter was 2020-09-30, so there are no later ranks or flags for it in our data.

## Sources

- F1 · Bank name · n/a · Almena State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2020-09-30 · 2020-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KS · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2020-09-30 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2020-09-30 · 5,098 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2020-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2020-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2020-09-30 · 102 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2020-09-30 · 10.9% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2020-09-30 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2020-09-30 · 1.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2020-09-30 · 15.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2020-09-30 · 23.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2020-09-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2020-09-30 · 19.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2020-09-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2020-09-30 · 2.8% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2020-09-30 · 243.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2020-09-30 · 3.4% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2020-09-30 · -7.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2020-09-30 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2020-09-30 · 207.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2020-09-30 · 65.6% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2020-09-30 · 2.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2020-09-30 · 21.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2020-09-30 · 31.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2020-09-30 · 97.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2020-09-30 · 78.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2020-09-30 · -34.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2020-09-30 · -2.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2020-09-30 · $65.7 million · data/features/fct_bank_features.parquet: log_total_assets
- F73 · Bank: deposit growth over the past four quarters · 2020-09-30 · -15.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2020-09-30 · 15.0% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 0.0%; contribution to the score · 2020-09-30 · +1.798 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -233.5%; contribution to the score · 2020-09-30 · +1.440 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 243.0%; contribution to the score · 2020-09-30 · +1.035 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 23.8%; contribution to the score · 2020-09-30 · +0.654 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 1.4%; contribution to the score · 2020-09-30 · +0.552 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: losses on bonds available for sale, as a share of equity, value -34.5%; contribution to the score · 2020-09-30 · -0.250 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F81 · Driver down #2: deposit growth over the past four quarters, value -15.7%; contribution to the score · 2020-09-30 · -0.140 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F82 · Driver down #3: construction loans as a share of loans, value 0.0%; contribution to the score · 2020-09-30 · -0.100 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: loans 30-89 days past due, as a share of assets, value 1.2%; contribution to the score · 2020-09-30 · -0.090 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F84 · Driver down #5: volatile funding as a share of assets, value 2.0%; contribution to the score · 2020-09-30 · -0.078 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F85 · Failure date · 2020-10-23 · 2020-10-23 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2019-12-31 · 2019-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2019-12-31: return on equity (profit as a share of equity), value -100.1%; contribution to the score · 2019-12-31 · +1.351 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2019-12-31: the Texas ratio (troubled assets against capital plus reserves), value 189.3%; contribution to the score · 2019-12-31 · +0.934 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2019-12-31: the Tier 1 risk-based capital ratio, value 5.9%; contribution to the score · 2019-12-31 · +0.860 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F91 · Driver up #4 at 2019-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 22.9%; contribution to the score · 2019-12-31 · +0.751 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2019-12-31: brokered deposits as a share of deposits, value 26.3%; contribution to the score · 2019-12-31 · +0.269 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F98 · Last quarter the bank reported · 2020-09-30 · 2020-09-30 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2020-09-30 · -34.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F100 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · -2.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F101 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F104 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2020-09-30 · -0.250 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F105 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2020-09-30 · pushed the score down · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2020-09-30 · 207.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 52.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F108 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 86.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2020-09-30 · -0.036 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F111 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2020-09-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F112 · Trend: cash as a share of assets, value at the as-of quarter · 2020-09-30 · 9.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F113 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F114 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 3.3% · data/features/fct_bank_features.parquet: cash_to_assets
- F117 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2020-09-30 · +0.006 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F118 · Trend: cash as a share of assets, what the model did with it · 2020-09-30 · little effect on the score · data/analyst/scores.parquet: feature cash_to_assets contribution
- F119 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2020-09-30 · 2.4% · data/features/fct_bank_features.parquet: net_interest_margin
- F120 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 4.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F121 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 5.3% · data/features/fct_bank_features.parquet: net_interest_margin
- F123 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2020-09-30 · +0.119 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F124 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2020-09-30 · pushed the score up · data/analyst/scores.parquet: feature net_interest_margin contribution
- F125 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2020-09-30 · -233.5% · data/features/fct_bank_features.parquet: return_on_equity
- F126 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -119.7% · data/features/fct_bank_features.parquet: return_on_equity
- F127 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 38.7% · data/features/fct_bank_features.parquet: return_on_equity
- F129 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2020-09-30 · +1.440 · data/analyst/scores.parquet: feature return_on_equity contribution
- F130 · Trend: return on equity (profit as a share of equity), what the model did with it · 2020-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F131 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2020-09-30 · 10.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F132 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F133 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 8.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F136 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2020-09-30 · +0.084 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F137 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2020-09-30 · pushed the score up · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F138 · Trend: ratios outside their own prior range · 2020-09-30 · 16 · data/features/fct_bank_features.parquet
- F140 · Trend: ratios compared with their own prior range · 2020-09-30 · 30 · data/features/fct_bank_features.parquet
- F141 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F142 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F143 · Percentile a year earlier (100 = highest risk) · 2019-09-30 · 99.9% · data/analyst/scores.parquet: percentile
- F144 · Trend: how the model's rating compares with a year earlier · 2020-09-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F148 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2020-09-30 · 19.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F149 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2020-09-30 · 100.0th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F150 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2020-09-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F151 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2020-09-30 · 99.9th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F152 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2020-09-30 · 0.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F153 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2020-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F154 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2020-09-30 · -233.5% · data/features/fct_bank_features.parquet: return_on_equity
- F155 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2020-09-30 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F156 · Peers: return on equity (profit as a share of equity), national reading · 2020-09-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F157 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2020-09-30 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F158 · Peers: return on equity (profit as a share of equity), peer median · 2020-09-30 · 7.0% · data/features/fct_bank_features.parquet: return_on_equity
- F159 · Peers: return on equity (profit as a share of equity), reading against its peers · 2020-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F160 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2020-09-30 · 1.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F161 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2020-09-30 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F162 · Peers: the total risk-based capital ratio, national reading · 2020-09-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F163 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2020-09-30 · 0.2nd · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F164 · Peers: the total risk-based capital ratio, peer median · 2020-09-30 · 18.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F165 · Peers: the total risk-based capital ratio, reading against its peers · 2020-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F166 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F167 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2020-09-30 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F168 · Peers: the Tier 1 risk-based capital ratio, national reading · 2020-09-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F169 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2020-09-30 · 0.2nd · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F170 · Peers: the Tier 1 risk-based capital ratio, peer median · 2020-09-30 · 17.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F171 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2020-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F172 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2020-09-30 · 97.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F173 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2020-09-30 · 100.0th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F174 · Peers: core deposits as a share of assets, national reading · 2020-09-30 · unusually high · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F175 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2020-09-30 · 99.9th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F176 · Peers: core deposits as a share of assets, peer median · 2020-09-30 · 80.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F177 · Peers: core deposits as a share of assets, reading against its peers · 2020-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F178 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2020-09-30 · 243.0% · data/features/fct_bank_features.parquet: texas_ratio
- F179 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2020-09-30 · 100.0th · data/features/fct_bank_features.parquet: texas_ratio
- F180 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2020-09-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F181 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2020-09-30 · 99.9th · data/features/fct_bank_features.parquet: texas_ratio
- F182 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2020-09-30 · 2.5% · data/features/fct_bank_features.parquet: texas_ratio
- F183 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2020-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F184 · Peers: losses on bonds available for sale, as a share of equity, bank value at the as-of quarter · 2020-09-30 · -34.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F185 · Peers: losses on bonds available for sale, as a share of equity, national percentile (100 = highest value among all banks) · 2020-09-30 · 0.1st · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F186 · Peers: losses on bonds available for sale, as a share of equity, national reading · 2020-09-30 · unusually low · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F187 · Peers: losses on bonds available for sale, as a share of equity, percentile among its peers (100 = highest value) · 2020-09-30 · 0.1st · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F188 · Peers: losses on bonds available for sale, as a share of equity, peer median · 2020-09-30 · -2.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F189 · Peers: losses on bonds available for sale, as a share of equity, reading against its peers · 2020-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F190 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2020-09-30 · 23.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F191 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2020-09-30 · 99.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F192 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2020-09-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F193 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2020-09-30 · 99.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F194 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2020-09-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F195 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2020-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F197 · Peers: ratios in the national top or bottom 10% · 2020-09-30 · 23 · data/features/fct_bank_features.parquet
- F198 · Peers: those ratios also unusual among peers · 2020-09-30 · 21 · data/features/fct_bank_features.parquet
- F200 · Peers: cut-off for unusual (top or bottom share of banks) · 2020-09-30 · 10% · data/features/fct_bank_features.parquet
