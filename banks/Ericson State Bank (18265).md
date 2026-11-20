---
cert: 18265
name: "Ericson State Bank"
as_of: 2019-12-31
rank: 4
n_banks: 5244
percentile: 99.94279176201373
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2020-02-14
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:14:02"
writer_model: "claude-opus-5-5"
checked: true
---

# Ericson State Bank (cert 18265)

*Hindsight: failed 2020-02-14. Canary flagged it 4 quarters ahead.*

## Summary

As of 2019-12-31, Ericson State Bank ranked 4 out of 5,244 FDIC-insured banks on Canary's risk score, placing it in the 99.9th percentile, where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks by score. Its capital cushion was thin, with equity at 3.7% of assets against a national median of 11.4%, and it was losing money, with return on assets (profit as a share of assets) of -3.4%. Problem loans were high: loans 90+ days past due or not accruing interest were 6.9% of loans, compared with a national median of 0.5%.

## Warning signs in the data

Capital, the bank's own money available to absorb losses, was far below typical levels. Equity was 3.7% of assets versus a national median of 11.4%, and the leverage ratio (core capital as a share of average assets) was 3.4% versus 10.9%. The Tier 1 risk-based capital ratio, which weighs assets by how risky they are, was 4.3% against a median of 15.5%, and the total risk-based capital ratio was 5.6% against 16.6%.

Credit quality, meaning how well borrowers were repaying, was weak. Loans 90+ days past due or not accruing interest were 6.9% of loans compared with a national median of 0.5%, and loans 30-89 days past due were 2.5% of assets versus 0.3%. Net loan write-offs (loans given up as lost, minus recoveries) were 7.1% of loans against a median of 0.0%, and the annualized provision for loan losses (money set aside for expected bad loans) was 6.9% of assets against 0.1%. The Texas ratio, troubled assets measured against capital plus reserves, was 90.1% versus a median of 3.6%, and return on equity was -48.4% against 9.3%.

On liquidity and funding, cash was just 0.5% of assets versus a national median of 7.2%, loans equaled 90.5% of deposits against 81.5%, and brokered deposits (money placed through middlemen) were 4.2% of deposits where the median was 0.0%. Losses on bonds held to maturity were -7.5% of equity versus a median of 0.0%, while bonds available for sale showed 0.0% against a median of -0.6%. Some figures pointed the other way: core deposits (stable everyday deposits) were 83.8% of assets versus 77.6%, uninsured deposits were 4.3% of deposits versus 19.5%, and the net interest margin (the spread earned on lending and investing) was 4.0% versus 3.8%. Commercial real estate was not a concern either: construction loans were 0.0% of loans versus a median of 4.7%, and the separate real-estate concentration check found the bank did not cross either line.

## Understanding the score

On 2019-12-31, Ericson State Bank ranked 4 out of 5,244 banks, placing it in the 99.9th percentile on a 0 to 100 scale where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks and held 105 banks that quarter.

The five factors that pushed the score up most were the Tier 1 risk-based capital ratio at 4.3%, return on equity at -48.4%, the Texas ratio at 90.1%, loans 90+ days past due or not accruing interest at 6.9% of loans, and the annualized provision for loan losses at 6.9% of assets. The five factors that pulled the score down most were losses on bonds held to maturity at -7.5% of equity, construction loans at 0.0% of loans, the net interest margin at 4.0%, core deposits at 83.8% of assets, and volatile funding (money that can leave quickly) at 8.3% of assets.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2018-03-31 | 275 | 5,674 |  |
| 2018-06-30 | 252 | 5,610 |  |
| 2018-09-30 | 253 | 5,544 |  |
| 2018-12-31 | 11 | 5,473 | ▲ watchlist |
| 2019-03-31 | 9 | 5,428 | ▲ watchlist (first flag) |
| 2019-06-30 | 10 | 5,369 | ▲ watchlist |
| 2019-09-30 | 11 | 5,325 | ▲ watchlist |
| 2019-12-31 | 4 | 5,244 | ▲ watchlist |

## How its ratios moved

As of 2019-12-31, Ericson State Bank ranked 4 out of 5,244 banks nationally, placing it in the 99.9th percentile, where higher means riskier. A year earlier, on 2018-12-31, it sat in the 99.8th percentile, so the model's rating was about the same as a year earlier. Each ratio is compared with the bank's own history, mostly the prior 12 quarters, and 18 of the 30 ratios checked were outside that prior range.

Return on equity (profit as a share of the owners' stake) was -48.4%, far below its prior range of 2.8% to 16.7%, and it pushed the score up with a contribution of +0.809 model log-odds units. The provision for loan losses (money set aside to cover expected bad loans), as a share of assets, was 6.9% against a prior range of 0.4% to 1.9%, and it pushed the score up by +0.196. Loans 30-89 days past due (borrowers behind on payments) reached 2.5% of assets, well above a prior range of 0.0% to 0.1%, and they pushed the score up by +0.192. Return on assets (profit as a share of assets) was -3.4%, below its prior range of 0.3% to 1.6%, and it pushed the score up by +0.103.

Two ratios moved far outside their usual range yet had little effect on the score. The leverage ratio (core capital as a share of average assets) fell to 3.4%, below its prior range of 7.8% to 10.2%, but it had little effect on the score, contributing +0.015. Net loan write-offs (loans written off as lost, minus recoveries) rose to 7.1% of loans, above a prior range of 0.0% to 1.1%, but they also had little effect on the score, contributing -0.013.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized loan write-offs, net of recoveries, as a share of loans | 7.1% | 0.0% to 1.1% | same quarter, prior 3 years | n/a | +7.1 pp | -0.013 | little effect on the score |
| return on equity (profit as a share of equity) | -48.4% | 2.8% to 16.7% | same quarter, prior 3 years | n/a | -51.2 pp | +0.809 | pushed the score up |
| annualized provision for loan losses as a share of assets | 6.9% | 0.4% to 1.9% | same quarter, prior 3 years | n/a | +5.0 pp | +0.196 | pushed the score up |
| return on assets (profit as a share of assets) | -3.4% | 0.3% to 1.6% | same quarter, prior 3 years | n/a | -3.6 pp | +0.103 | pushed the score up |
| loans 30-89 days past due, as a share of assets | 2.5% | 0.0% to 0.1% | prior 12 quarters | +2.5 pp | +2.4 pp | +0.192 | pushed the score up |
| the leverage ratio (core capital as a share of average assets) | 3.4% | 7.8% to 10.2% | prior 12 quarters | -4.6 pp | -4.5 pp | +0.015 | little effect on the score |

18 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2019-12-31: Agricultural Specialization.

Peers: 751 banks in the same specialty group and size tier ($100 million to $1 billion).

Ericson State Bank ranked 4 out of 5,244 banks nationally that quarter, placing it at the 99.9th percentile of the model's score. Capital ratios measure the bank's cushion of its own money against losses, with Tier 1 counting only the core, highest-quality capital. Its total risk-based capital ratio was 5.6%, at the 0.1st percentile nationally (unusually low), and at the 0.1st percentile among its peers against a peer median of 16.0%, which is unusually low among its peers too. Its Tier 1 risk-based capital ratio was 4.3%, at the 0.1st percentile nationally (unusually low), and at the 0.1st percentile among its peers against a peer median of 14.9%, which is unusually low among its peers too.

A provision is money set aside for expected loan losses, and a write-off is a loan the bank has accepted it will not collect. Its annualized provision for loan losses was 6.9% of assets, at the 99.9th percentile nationally (unusually high), and at the 99.9th percentile among its peers against a peer median of 0.1%, which is unusually high among its peers too. Its annualized loan write-offs, net of recoveries, were 7.1% of loans, at the 99.9th percentile nationally (unusually high), and at the 99.9th percentile among its peers against a peer median of 0.0%, which is unusually high among its peers too. Its return on equity, meaning profit as a share of the owners' stake, was -48.4%, at the 0.1st percentile nationally (unusually low), and at the 0.1st percentile among its peers against a peer median of 10.8%, which is unusually low among its peers too. Its losses on bonds held to maturity, as a share of equity, were -7.5%, at the 0.3rd percentile nationally (unusually low), and at the 0.2nd percentile among its peers against a peer median of 0.0%, which is unusually low among its peers too.

The Texas ratio compares troubled loans and assets with the capital and reserves available to absorb them. Its Texas ratio was 90.1%, at the 99.7th percentile nationally (unusually high), and at the 99.8th percentile among its peers against a peer median of 3.9%, which is unusually high among its peers too. Its cash was 0.5% of assets, at the 0.4th percentile nationally (unusually low), and at the 0.2nd percentile among its peers against a peer median of 6.0%, which is unusually low among its peers too. Overall, 20 of the bank's ratios sat in the national top or bottom 10%, and all 20 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the total risk-based capital ratio | 5.6% | 0.1st (unusually low) | 16.0% | 0.1st | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 4.3% | 0.1st (unusually low) | 14.9% | 0.1st | unusually low among its peers too |
| annualized provision for loan losses as a share of assets | 6.9% | 99.9th (unusually high) | 0.1% | 99.9th | unusually high among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 7.1% | 99.9th (unusually high) | 0.0% | 99.9th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -48.4% | 0.1st (unusually low) | 10.8% | 0.1st | unusually low among its peers too |
| losses on bonds held to maturity, as a share of equity | -7.5% | 0.3rd (unusually low) | 0.0% | 0.2nd | unusually low among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 90.1% | 99.7th (unusually high) | 3.9% | 99.8th | unusually high among its peers too |
| cash as a share of assets | 0.5% | 0.4th (unusually low) | 6.0% | 0.2nd | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: total risk-based capital, as the 2006 guidance specifies.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 68.5% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 37.9% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, Canary first flagged Ericson State Bank in the quarter ending 2019-03-31, and the bank failed on 2020-02-14, giving a lead time of 4 quarters. At that first flag, the main factors pushing the score up were the Texas ratio at 77.2%, loans 90+ days past due or not accruing interest at 8.8% of loans, commercial real estate loans at 4.4% of loans, the efficiency ratio at 35.3%, and deposit growth of 24.3%. At that time the bank was still profitable, with return on equity of 26.6% and return on assets of 2.1%, and both pulled the score down.

## What happened next

In hindsight, the bank's last report was for the quarter ending 2019-12-31, and it failed on 2020-02-14. Because it stopped reporting after that, there are no later ranks or flags to show.

## Sources

- F1 · Bank name · n/a · Ericson State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2019-12-31 · 2019-12-31 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2019-12-31 · 4 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2019-12-31 · 5,244 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2019-12-31 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2019-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2019-12-31 · 105 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2019-12-31 · 3.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2019-12-31 · 11.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2019-12-31 · 3.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2019-12-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2019-12-31 · 4.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2019-12-31 · 15.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2019-12-31 · 5.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2019-12-31 · 16.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2019-12-31 · 6.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2019-12-31 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2019-12-31 · 2.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2019-12-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2019-12-31 · 7.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2019-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2019-12-31 · 6.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2019-12-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F33 · Bank: construction loans as a share of loans · 2019-12-31 · 0.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F34 · National median: construction loans as a share of loans · 2019-12-31 · 4.7% · data/features/fct_bank_features.parquet: construction_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2019-12-31 · 90.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2019-12-31 · 3.6% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2019-12-31 · -3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F41 · Bank: return on equity (profit as a share of equity) · 2019-12-31 · -48.4% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2019-12-31 · 9.3% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2019-12-31 · 4.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2019-12-31 · 3.8% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F49 · Bank: loans as a share of deposits · 2019-12-31 · 90.5% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2019-12-31 · 81.5% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2019-12-31 · 4.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2019-12-31 · 19.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2019-12-31 · 4.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2019-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2019-12-31 · 83.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2019-12-31 · 77.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2019-12-31 · 0.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2019-12-31 · 7.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2019-12-31 · -7.5% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2019-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2019-12-31 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2019-12-31 · -0.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 4.3%; contribution to the score · 2019-12-31 · +1.915 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -48.4%; contribution to the score · 2019-12-31 · +0.809 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 90.1%; contribution to the score · 2019-12-31 · +0.500 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 6.9%; contribution to the score · 2019-12-31 · +0.476 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: annualized provision for loan losses as a share of assets, value 6.9%; contribution to the score · 2019-12-31 · +0.196 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F80 · Driver down #1: losses on bonds held to maturity, as a share of equity, value -7.5%; contribution to the score · 2019-12-31 · -0.784 · data/analyst/scores.parquet: feature htm_unrealized_loss_to_equity contribution
- F81 · Driver down #2: construction loans as a share of loans, value 0.0%; contribution to the score · 2019-12-31 · -0.309 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: net interest margin (the spread earned on lending and investing), value 4.0%; contribution to the score · 2019-12-31 · -0.149 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F83 · Driver down #4: core deposits as a share of assets, value 83.8%; contribution to the score · 2019-12-31 · -0.131 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F84 · Driver down #5: volatile funding as a share of assets, value 8.3%; contribution to the score · 2019-12-31 · -0.092 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F85 · Failure date · 2020-02-14 · 2020-02-14 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2019-03-31 · 2019-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2019-03-31: the Texas ratio (troubled assets against capital plus reserves), value 77.2%; contribution to the score · 2019-03-31 · +1.067 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Driver up #2 at 2019-03-31: loans 90+ days past due or not accruing interest, as a share of loans, value 8.8%; contribution to the score · 2019-03-31 · +0.760 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F90 · Driver up #3 at 2019-03-31: commercial real estate loans as a share of loans, value 4.4%; contribution to the score · 2019-03-31 · +0.272 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F91 · Driver up #4 at 2019-03-31: the efficiency ratio (operating costs as a share of revenue), value 35.3%; contribution to the score · 2019-03-31 · +0.271 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F92 · Driver up #5 at 2019-03-31: deposit growth over the past four quarters, value 24.3%; contribution to the score · 2019-03-31 · +0.168 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F93 · Driver down #1 at 2019-03-31: return on equity (profit as a share of equity), value 26.6%; contribution to the score · 2019-03-31 · -0.616 · data/analyst/scores.parquet: feature return_on_equity contribution
- F95 · Driver down #3 at 2019-03-31: return on assets (profit as a share of assets), value 2.1%; contribution to the score · 2019-03-31 · -0.295 · data/analyst/scores.parquet: feature return_on_assets contribution
- F98 · Last quarter the bank reported · 2019-12-31 · 2019-12-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2019-12-31 · 7.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F100 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F101 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F103 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2019-12-31 · -0.013 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F104 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2019-12-31 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F105 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2019-12-31 · -48.4% · data/features/fct_bank_features.parquet: return_on_equity
- F106 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 2.8% · data/features/fct_bank_features.parquet: return_on_equity
- F107 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 16.7% · data/features/fct_bank_features.parquet: return_on_equity
- F109 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2019-12-31 · +0.809 · data/analyst/scores.parquet: feature return_on_equity contribution
- F110 · Trend: return on equity (profit as a share of equity), what the model did with it · 2019-12-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F111 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2019-12-31 · 6.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F112 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F113 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 1.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F115 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2019-12-31 · +0.196 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F116 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2019-12-31 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F117 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2019-12-31 · -3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F118 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F119 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.6% · data/features/fct_bank_features.parquet: return_on_assets
- F121 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2019-12-31 · +0.103 · data/analyst/scores.parquet: feature return_on_assets contribution
- F122 · Trend: return on assets (profit as a share of assets), what the model did with it · 2019-12-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F123 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2019-12-31 · 2.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F124 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F125 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F128 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2019-12-31 · +0.192 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F129 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2019-12-31 · pushed the score up · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F130 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2019-12-31 · 3.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F131 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 7.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F132 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F135 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2019-12-31 · +0.015 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F136 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2019-12-31 · little effect on the score · data/analyst/scores.parquet: feature leverage_ratio contribution
- F137 · Trend: ratios outside their own prior range · 2019-12-31 · 18 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios compared with their own prior range · 2019-12-31 · 30 · data/features/fct_bank_features.parquet
- F140 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F142 · Percentile a year earlier (100 = highest risk) · 2018-12-31 · 99.8% · data/analyst/scores.parquet: percentile
- F143 · Trend: how the model's rating compares with a year earlier · 2019-12-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F147 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2019-12-31 · 5.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F148 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2019-12-31 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F149 · Peers: the total risk-based capital ratio, national reading · 2019-12-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F150 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2019-12-31 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F151 · Peers: the total risk-based capital ratio, peer median · 2019-12-31 · 16.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F152 · Peers: the total risk-based capital ratio, reading against its peers · 2019-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F153 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2019-12-31 · 4.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F154 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2019-12-31 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F155 · Peers: the Tier 1 risk-based capital ratio, national reading · 2019-12-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F156 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2019-12-31 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F157 · Peers: the Tier 1 risk-based capital ratio, peer median · 2019-12-31 · 14.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F158 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2019-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F159 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2019-12-31 · 6.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F160 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2019-12-31 · 99.9th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F161 · Peers: annualized provision for loan losses as a share of assets, national reading · 2019-12-31 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F162 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2019-12-31 · 99.9th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F163 · Peers: annualized provision for loan losses as a share of assets, peer median · 2019-12-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F164 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2019-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F165 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2019-12-31 · 7.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F166 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2019-12-31 · 99.9th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F167 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2019-12-31 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F168 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2019-12-31 · 99.9th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F169 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2019-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F170 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2019-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F171 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2019-12-31 · -48.4% · data/features/fct_bank_features.parquet: return_on_equity
- F172 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2019-12-31 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F173 · Peers: return on equity (profit as a share of equity), national reading · 2019-12-31 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F174 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2019-12-31 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F175 · Peers: return on equity (profit as a share of equity), peer median · 2019-12-31 · 10.8% · data/features/fct_bank_features.parquet: return_on_equity
- F176 · Peers: return on equity (profit as a share of equity), reading against its peers · 2019-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F177 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2019-12-31 · -7.5% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F178 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2019-12-31 · 0.3rd · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F179 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2019-12-31 · unusually low · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F180 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2019-12-31 · 0.2nd · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F181 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2019-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F182 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2019-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F183 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2019-12-31 · 90.1% · data/features/fct_bank_features.parquet: texas_ratio
- F184 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2019-12-31 · 99.7th · data/features/fct_bank_features.parquet: texas_ratio
- F185 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2019-12-31 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F186 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2019-12-31 · 99.8th · data/features/fct_bank_features.parquet: texas_ratio
- F187 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2019-12-31 · 3.9% · data/features/fct_bank_features.parquet: texas_ratio
- F188 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2019-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F189 · Peers: cash as a share of assets, bank value at the as-of quarter · 2019-12-31 · 0.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F190 · Peers: cash as a share of assets, national percentile (100 = highest value among all banks) · 2019-12-31 · 0.4th · data/features/fct_bank_features.parquet: cash_to_assets
- F191 · Peers: cash as a share of assets, national reading · 2019-12-31 · unusually low · data/features/fct_bank_features.parquet: cash_to_assets
- F192 · Peers: cash as a share of assets, percentile among its peers (100 = highest value) · 2019-12-31 · 0.2nd · data/features/fct_bank_features.parquet: cash_to_assets
- F193 · Peers: cash as a share of assets, peer median · 2019-12-31 · 6.0% · data/features/fct_bank_features.parquet: cash_to_assets
- F194 · Peers: cash as a share of assets, reading against its peers · 2019-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: cash_to_assets
- F196 · Peers: ratios in the national top or bottom 10% · 2019-12-31 · 20 · data/features/fct_bank_features.parquet
- F197 · Peers: those ratios also unusual among peers · 2019-12-31 · 20 · data/features/fct_bank_features.parquet
- F199 · Peers: cut-off for unusual (top or bottom share of banks) · 2019-12-31 · 10% · data/features/fct_bank_features.parquet
