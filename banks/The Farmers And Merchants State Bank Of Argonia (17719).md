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
written_at: "2026-11-19T21:14:02"
writer_model: "claude-opus-5-5"
checked: true
---

# The Farmers And Merchants State Bank Of Argonia (cert 17719)

*Hindsight: failed 2017-10-13. Canary flagged it 4 quarters ahead.*

## Summary

As of 2017-09-30, Canary's model ranked The Farmers And Merchants State Bank Of Argonia (KS, cert 17719) 1 out of 5,806 FDIC-insured banks, placing it at the 100.0th percentile on a scale where higher means riskier. It was flagged on Canary's watchlist, which covers about 2% of banks. Its capital, the owners' own money that absorbs losses, had turned negative: equity was -1.1% of assets against a national median of 11.0%. Bad loans, loan write-offs and losses were all far above typical levels, and the separate real-estate concentration screen could not be applied because the bank's capital was zero or negative.

## Warning signs in the data

Capital was the starkest problem: equity was -1.1% of assets against a national median of 11.0%, and the leverage ratio (core capital as a share of average assets) was -1.3% against a median of 10.6%. The Tier 1 risk-based capital ratio was -2.3% against a median of 15.1%, and the total risk-based capital ratio was -1.0% against 16.3%. The Texas ratio, which compares troubled assets with capital plus loss reserves, was 292.3% against a national median of 4.5%.

Credit quality was also very weak: loans 90 or more days late or no longer paying interest were 11.5% of loans against a median of 0.6%, and loans 30-89 days late were 3.0% of assets against 0.3%. Annualized write-offs (loans recorded as lost, net of recoveries) were 10.5% of loans against a median of 0.0%, and the annualized provision for loan losses was 8.1% of assets against 0.1%. Return on assets was -10.5% against a median of 0.9%, and the efficiency ratio (operating costs as a share of revenue) was 139.0% against 68.0%. The trend section notes that some of these extremes, such as write-offs and the efficiency ratio, had little direct effect on the score; the model leaned mainly on capital and profit measures instead.

On funding, brokered deposits (money placed through middlemen) were 10.3% of deposits against a median of 0.0%, and Federal Home Loan Bank borrowings were 13.8% of assets against 0.9%. Deposits shrank -9.9% over the past four quarters, while the national median grew 3.8%; on the other hand, cash was a high 20.8% of assets against a median of 6.1%, and uninsured deposits were a low 4.2% of deposits against 17.8%. Bond losses were not a major theme: losses on bonds available for sale were -5.0% of equity against a median of 0.0%, and losses on bonds held to maturity were 0.0%, the same as the median.

## Understanding the score

As of 2017-09-30, the bank ranked 1 out of 5,806 banks, at the 100.0th percentile on a 0 to 100 scale where higher means riskier. It was flagged on the watchlist, one of 117 banks on it that quarter.

The five factors that pushed the score up most were all about capital and profit: the Tier 1 risk-based capital ratio at -2.3%, return on equity (profit as a share of the owners' stake) at -282.8%, the Texas ratio at 292.3%, the leverage ratio at -1.3%, and the total risk-based capital ratio at -1.0%.

The five factors that pulled the score down most were annualized interest expense at 0.9% of assets, losses on bonds available for sale at -5.0% of equity, construction loans at 0.5% of loans, deposit growth at -9.9%, and the net interest margin (the spread earned on lending and investing) at 4.2%. These offsets were much smaller than the upward pushes, so the bank stayed at the top of the national ranking.

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

As of 2017-09-30, the model ranked the bank 1 out of 5,806 banks nationally, placing it at the 100.0th percentile on a scale where higher means riskier. A year earlier, on 2016-09-30, it sat at the 98.2nd percentile, and the model rated it riskier than a year earlier. Each ratio is compared with its own prior range, usually the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios, and 20 of the 30 ratios checked sat outside that range.

Return on equity, which is profit as a share of the owners' stake, was -282.8% against a prior range of 6.4% to 8.2%, a change of -291.0 pp over four quarters, and it pushed the score up with a contribution of +1.348 model log-odds units. Return on assets, which is profit as a share of everything the bank owns, was -10.5% against a prior range of 0.5% to 0.6%, and it pushed the score up with a contribution of +0.141 model log-odds units. The annualized provision for loan losses, money set aside for loans expected to go bad, was 8.1% of assets against a prior range of 0.0% to 0.1%, and it pushed the score up with a contribution of +0.143 model log-odds units.

Annualized loan write-offs, net of recoveries, were 10.5% of loans against a prior range of 0.0% to 0.3%, yet despite being far outside that range this ratio had little effect on the score, contributing -0.011 model log-odds units. The efficiency ratio, operating costs as a share of revenue, was 139.0% against a prior range of 82.9% to 87.9%, but it too had little effect on the score, contributing -0.027 model log-odds units. Cash was 20.8% of assets against a prior range of 2.2% to 6.1%, up +17.6 pp in one quarter, but it also had little effect on the score, contributing -0.016 model log-odds units.

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

Equity, the owners' own money that cushions losses, was -1.1% of assets, at the 0.0th percentile nationally (unusually low) and the 0.1st percentile among its peers, whose median was 11.6%, which is unusually low among its peers too. The leverage ratio, core capital as a share of average assets, was -1.3%, at the 0.0th percentile nationally (unusually low) and the 0.1st percentile among peers against a peer median of 11.4%, which is unusually low among its peers too. The total risk-based capital ratio, capital measured against assets weighted by how likely regulators consider them to lose value, was -1.0%, at the 0.0th percentile nationally (unusually low) and the 0.1st percentile among peers against a peer median of 18.7%, which is unusually low among its peers too. The Tier 1 risk-based capital ratio, the same measure using only the strongest form of capital, was -2.3%, at the 0.0th percentile nationally (unusually low) and the 0.1st percentile among peers against a peer median of 17.6%, which is unusually low among its peers too.

Return on equity, profit as a share of equity, was -282.8%, at the 0.0th percentile nationally (unusually low) and the 0.1st percentile among peers against a peer median of 8.0%, which is unusually low among its peers too. Return on assets, profit as a share of assets, was -10.5%, at the 0.1st percentile nationally (unusually low) and the 0.1st percentile among peers against a peer median of 0.9%, which is unusually low among its peers too. Annualized loan write-offs, loans recorded as lost net of amounts recovered, were 10.5% of loans, at the 100.0th percentile nationally (unusually high) and the 99.9th percentile among peers against a peer median of 0.0%, which is unusually high among its peers too. The annualized provision for loan losses, money set aside for expected bad loans, was 8.1% of assets, at the 99.9th percentile nationally (unusually high) and the 99.9th percentile among peers against a peer median of 0.0%, which is unusually high among its peers too.

Overall, 21 of the bank's ratios sat in the national top or bottom 10%, and 19 of those were also unusual among its peers.

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

In hindsight, the bank failed on 2017-10-13. Canary first flagged it in the quarter ending 2016-12-31, a lead time of 4 quarters before the failure.

At that first flag, the warning came from loan quality rather than capital: loans 90 or more days late or not paying interest were 12.1% of loans, the Texas ratio was 115.6%, and loans 30-89 days late were 4.0% of assets. Back then the Tier 1 risk-based capital ratio was still 9.1% and actually pulled the score down, so the model picked up the trouble in the loans before capital was wiped out.

## What happened next

In hindsight, the quarter ending 2017-09-30 was the last one the bank reported. The bank failed on 2017-10-13, so there are no later ranks or flags after the as-of quarter.

## Sources

- F1 · Bank name · n/a · The Farmers And Merchants State Bank Of Argonia · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 17719 · data/features/fct_bank_features.parquet: cert
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
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2017-09-30 · 3.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2017-09-30 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2017-09-30 · 10.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2017-09-30 · 8.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2017-09-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2017-09-30 · 292.3% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2017-09-30 · 4.5% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2017-09-30 · -10.5% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2017-09-30 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2017-09-30 · 139.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2017-09-30 · 68.0% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2017-09-30 · 4.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2017-09-30 · 17.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2017-09-30 · 10.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2017-09-30 · 13.8% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2017-09-30 · 0.9% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2017-09-30 · 20.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2017-09-30 · 6.1% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
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
- F95 · Driver down #3 at 2016-12-31: the Tier 1 risk-based capital ratio, value 9.1%; contribution to the score · 2016-12-31 · -0.226 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2017-09-30 · 2017-09-30 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2017-09-30 · -282.8% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 6.4% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 8.2% · data/features/fct_bank_features.parquet: return_on_equity
- F102 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2017-09-30 · -291.0 pp · data/features/fct_bank_features.parquet: return_on_equity
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
