---
cert: 21111
name: "City National Bank Of New Jersey"
as_of: 2019-09-30
rank: 21
n_banks: 5325
percentile: 99.6244131455399
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2019-11-01
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:14:02"
writer_model: "claude-opus-5-5"
checked: true
---

# City National Bank Of New Jersey (cert 21111)

*Hindsight: failed 2019-11-01. Canary flagged it 4 quarters ahead.*

## Summary

As of 2019-09-30, City National Bank Of New Jersey, a New Jersey bank, ranked 21 out of 5,325 banks on Canary's risk score, placing it in the 99.6th percentile, where higher means riskier, and it was flagged on the watchlist. Its capital cushion was very thin, with equity (the owners' stake) at 2.9% of assets against a national median of 11.6%, and it was losing money, with a return on equity of -45.9%. Problem loans and shrinking deposits added to the picture, although the separate real-estate concentration screen found the bank did not cross either supervisory line.

## Warning signs in the data

Capital, the cushion that absorbs losses, was far below typical levels as of 2019-09-30: equity was 2.9% of assets versus a national median of 11.6%, and the leverage ratio (core capital as a share of average assets) was 2.6% versus 11.0%. The Tier 1 risk-based capital ratio (strongest capital measured against assets weighted by riskiness) was 4.9% versus a median of 15.6%, and the total risk-based capital ratio was 6.2% versus 16.7%. Profitability was weak, with return on assets at -1.4% against a median of 1.1% and an efficiency ratio (operating costs as a share of revenue) of 148.2% against 66.8%.

Credit quality was well worse than the national median: loans 90 or more days past due or not accruing interest were 2.6% of loans versus 0.6%, and loans 30-89 days past due were 1.3% of assets versus 0.3%. The Texas ratio (troubled assets against capital plus reserves) was 25.5% versus a median of 3.7%, while loan-loss reserves were high at 5.8% of loans versus 1.2%. Commercial real estate loans made up 62.1% of loans, well above the median of 22.6%, yet the separate concentration section found the bank did not cross either supervisory line, so these two views point different ways.

On funding, deposits shrank by -36.3% over the past four quarters against a median of 4.4%, and uninsured deposits (balances above the government insurance limit) were 32.1% of deposits versus 19.0%. On the other side, cash was 17.3% of assets versus a median of 6.9%, and brokered deposits were 0.0% of deposits. Losses on bonds available for sale (bonds the bank may sell before maturity) were 4.0% of equity, against a national median of -0.8%.

## Understanding the score

As of 2019-09-30, the bank ranked 21 out of 5,325 banks, which is the 99.6th percentile on a 0 to 100 scale where higher means riskier. It was flagged on the watchlist, which holds 2% of banks, or 107 banks that quarter.

Five features pushed the score up the most. They were return on equity at -45.9%, contributing +1.116, the Tier 1 risk-based capital ratio at 4.9%, contributing +0.973, and asset growth over the past four quarters at -33.2%, contributing +0.418. The total risk-based capital ratio at 6.2% added +0.284, and loans as a share of deposits at 54.0% added +0.150.

Five features pulled the score down the most. Annualized interest expense, the cost of the bank's funding, was 0.3% of assets, contributing -1.158, and the Texas ratio at 25.5% contributed -0.941. Nonaccrual assets and foreclosed property at 1.5% of assets contributed -0.699, construction loans at 4.8% of loans contributed -0.461, and commercial real estate loans at 62.1% of loans contributed -0.448.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2017-12-31 | 11 | 5,738 | ▲ watchlist |
| 2018-03-31 | 98 | 5,674 | ▲ watchlist |
| 2018-06-30 | 4 | 5,610 | ▲ watchlist |
| 2018-09-30 | 4 | 5,544 | ▲ watchlist |
| 2018-12-31 | 6 | 5,473 | ▲ watchlist (first flag) |
| 2019-03-31 | 17 | 5,428 | ▲ watchlist |
| 2019-06-30 | 16 | 5,369 | ▲ watchlist |
| 2019-09-30 | 21 | 5,325 | ▲ watchlist |

## How its ratios moved

As of 2019-09-30, the model ranked the bank 21 out of 5,325 banks, placing it in the 99.6th percentile, where higher means riskier. On 2018-09-30 it sat in the 99.9th percentile, and the model rates it about the same as a year earlier. Of the 30 ratios compared with their own prior range, which for most ratios means the prior 12 quarters, 12 were outside that range, and the 6 furthest outside are covered here.

Provision for loan losses (money set aside to cover expected bad loans), as an annualized share of assets, was -2.7%, below its prior range of 0.0% to 3.0%, and it pushed the score up, contributing +0.060 model log-odds units. Net interest margin, the spread earned on lending and investing, was 4.1%, above its prior range of 2.9% to 3.7%, yet it had little effect on the score, at -0.019 model log-odds units. Securities as a share of assets reached 25.2%, above its prior range of 15.4% to 22.6%, but it pushed the score down, at -0.086 model log-odds units. The efficiency ratio, operating costs as a share of revenue, was 148.2%, above its prior range of 108.8% to 139.0%, yet it pushed the score down, at -0.084 model log-odds units. Deposit growth over the past four quarters was -36.3%, below its prior range of -29.3% to 4.2%, but it pushed the score down, at -0.232 model log-odds units. Construction loans as a share of loans were 4.8%, above their prior range of 1.8% to 4.4%, and this too pushed the score down, at -0.461 model log-odds units.

In plain terms, five of these ratios moved outside their own history while the model either pushed the score down with them or barely moved it; only the loan-loss provision ratio pushed the score up.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | -2.7% | 0.0% to 3.0% | same quarter, prior 3 years | n/a | -5.7 pp | +0.060 | pushed the score up |
| net interest margin (the spread earned on lending and investing) | 4.1% | 2.9% to 3.7% | same quarter, prior 3 years | n/a | +0.4 pp | -0.019 | little effect on the score |
| securities as a share of assets | 25.2% | 15.4% to 22.6% | prior 12 quarters | +3.2 pp | +6.6 pp | -0.086 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 148.2% | 108.8% to 139.0% | same quarter, prior 3 years | n/a | +39.4 pp | -0.084 | pushed the score down |
| deposit growth over the past four quarters | -36.3% | -29.3% to 4.2% | prior 12 quarters | -10.8 pp | -32.8 pp | -0.232 | pushed the score down |
| construction loans as a share of loans | 4.8% | 1.8% to 4.4% | prior 12 quarters | +1.5 pp | +2.3 pp | -0.461 | pushed the score down |

12 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2019-09-30: Commercial Lending Specialization.

Peers: 1873 banks in the same specialty group and size tier ($100 million to $1 billion).

As of 2019-09-30, the bank ranked 21 out of 5,325 banks nationally, which puts it in the 99.6th percentile of Canary's score. Its annualized provision for loan losses (money set aside for loans that may not be repaid) was -2.7% of assets, in the 0.0th percentile nationally (unusually low) and the 0.0th percentile among peers against a peer median of 0.1%, which is unusually low among its peers too. Losses on bonds available for sale (bonds the bank may sell before they mature) were 4.0% of equity, in the 99.9th percentile nationally (unusually high) and the 100.0th percentile among peers against a peer median of -0.6%, which is unusually high among its peers too. Return on equity (profit as a share of the owners' stake) was -45.9%, in the 0.1st percentile nationally (unusually low) and the 0.1st percentile among peers against a peer median of 10.1%, which is unusually low among its peers too.

The total risk-based capital ratio (the bank's loss-absorbing cushion measured against its loans and other holdings, weighted by how safe they are) was 6.2%, in the 0.1st percentile nationally (unusually low) and the 0.1st percentile among peers against a peer median of 15.4%, which is unusually low among its peers too. The Tier 1 risk-based capital ratio (the same measure using only the strongest form of capital) was 4.9%, in the 0.1st percentile nationally (unusually low) and the 0.1st percentile among peers against a peer median of 14.4%, which is unusually low among its peers too. Equity as a share of assets was 2.9%, in the 0.4th percentile nationally (unusually low) and the 0.2nd percentile among peers against a peer median of 11.0%, which is unusually low among its peers too.

Deposit growth over the past four quarters was -36.3%, in the 0.2nd percentile nationally (unusually low) and the 0.1st percentile among peers against a peer median of 5.6%, which is unusually low among its peers too. Asset growth over the past four quarters was -33.2%, in the 0.2nd percentile nationally (unusually low) and the 0.1st percentile among peers against a peer median of 5.7%, which is unusually low among its peers too. Overall, 17 of the bank's ratios sat in the national top or bottom 10%, and 17 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | -2.7% | 0.0th (unusually low) | 0.1% | 0.0th | unusually low among its peers too |
| losses on bonds available for sale, as a share of equity | 4.0% | 99.9th (unusually high) | -0.6% | 100.0th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -45.9% | 0.1st (unusually low) | 10.1% | 0.1st | unusually low among its peers too |
| the total risk-based capital ratio | 6.2% | 0.1st (unusually low) | 15.4% | 0.1st | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 4.9% | 0.1st (unusually low) | 14.4% | 0.1st | unusually low among its peers too |
| deposit growth over the past four quarters | -36.3% | 0.2nd (unusually low) | 5.6% | 0.1st | unusually low among its peers too |
| asset growth over the past four quarters | -33.2% | 0.2nd (unusually low) | 5.7% | 0.1st | unusually low among its peers too |
| equity as a share of assets | 2.9% | 0.4th (unusually low) | 11.0% | 0.2nd | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: total risk-based capital, as the 2006 guidance specifies.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 67.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 192.8% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -70.7% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

With hindsight, the bank failed on 2019-11-01, and Canary had caught it in advance. Under Canary's lead-time rule, the bank was first flagged in the quarter ending 2018-12-31, a lead time of 4 quarters before the failure.

At that first flag, the biggest push upward came from the Tier 1 risk-based capital ratio at 5.3%, contributing +1.364, followed by return on equity at -88.2%, contributing +0.941. Losses on bonds available for sale at 34.1% of equity added +0.661, and the Texas ratio at 56.8% added +0.656. In short, thin capital and heavy losses were already driving the score when the bank was first flagged.

## What happened next

Looking back with hindsight, the last quarter the bank reported was 2019-09-30, the same quarter as this memo. The bank failed on November 1, 2019, so there are no later ranks or flags. It stopped reporting after that quarter; our data does not separate a merger from a closure, but here the failure date accounts for it.

## Sources

- F1 · Bank name · n/a · City National Bank Of New Jersey · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NJ · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2019-09-30 · 21 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2019-09-30 · 5,325 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2019-09-30 · 99.6% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2019-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2019-09-30 · 107 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2019-09-30 · 2.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2019-09-30 · 11.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 2.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2019-09-30 · 4.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2019-09-30 · 15.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2019-09-30 · 6.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2019-09-30 · 16.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 2.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2019-09-30 · 1.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2019-09-30 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2019-09-30 · 5.8% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2019-09-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2019-09-30 · 62.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2019-09-30 · 22.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 25.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 3.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2019-09-30 · -1.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2019-09-30 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2019-09-30 · -45.9% · data/features/fct_bank_features.parquet: return_on_equity
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 148.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 66.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2019-09-30 · 32.1% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2019-09-30 · 19.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F61 · Bank: cash as a share of assets · 2019-09-30 · 17.3% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2019-09-30 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2019-09-30 · 4.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2019-09-30 · -0.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2019-09-30 · -36.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2019-09-30 · 4.4% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -45.9%; contribution to the score · 2019-09-30 · +1.116 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: the Tier 1 risk-based capital ratio, value 4.9%; contribution to the score · 2019-09-30 · +0.973 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver up #3: asset growth over the past four quarters, value -33.2%; contribution to the score · 2019-09-30 · +0.418 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 6.2%; contribution to the score · 2019-09-30 · +0.284 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: loans as a share of deposits, value 54.0%; contribution to the score · 2019-09-30 · +0.150 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.3%; contribution to the score · 2019-09-30 · -1.158 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 25.5%; contribution to the score · 2019-09-30 · -0.941 · data/analyst/scores.parquet: feature texas_ratio contribution
- F82 · Driver down #3: nonaccrual assets and foreclosed property, as a share of assets, value 1.5%; contribution to the score · 2019-09-30 · -0.699 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F83 · Driver down #4: construction loans as a share of loans, value 4.8%; contribution to the score · 2019-09-30 · -0.461 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F84 · Driver down #5: commercial real estate loans as a share of loans, value 62.1%; contribution to the score · 2019-09-30 · -0.448 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F85 · Failure date · 2019-11-01 · 2019-11-01 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2018-12-31 · 2018-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2018-12-31: the Tier 1 risk-based capital ratio, value 5.3%; contribution to the score · 2018-12-31 · +1.364 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2018-12-31: return on equity (profit as a share of equity), value -88.2%; contribution to the score · 2018-12-31 · +0.941 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2018-12-31: losses on bonds available for sale, as a share of equity, value 34.1%; contribution to the score · 2018-12-31 · +0.661 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F91 · Driver up #4 at 2018-12-31: the Texas ratio (troubled assets against capital plus reserves), value 56.8%; contribution to the score · 2018-12-31 · +0.656 · data/analyst/scores.parquet: feature texas_ratio contribution
- F98 · Last quarter the bank reported · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
- F103 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2019-09-30 · -2.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F104 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F105 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 3.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F107 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2019-09-30 · +0.060 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F108 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2019-09-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F109 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2019-09-30 · 4.1% · data/features/fct_bank_features.parquet: net_interest_margin
- F110 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 2.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F111 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F113 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2019-09-30 · -0.019 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F114 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2019-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F115 · Trend: securities as a share of assets, value at the as-of quarter · 2019-09-30 · 25.2% · data/features/fct_bank_features.parquet: securities_to_assets
- F116 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 15.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F117 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 22.6% · data/features/fct_bank_features.parquet: securities_to_assets
- F120 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2019-09-30 · -0.086 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F121 · Trend: securities as a share of assets, what the model did with it · 2019-09-30 · pushed the score down · data/analyst/scores.parquet: feature securities_to_assets contribution
- F122 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2019-09-30 · 148.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F123 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 108.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F124 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 139.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F126 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2019-09-30 · -0.084 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F127 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2019-09-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F128 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2019-09-30 · -36.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F129 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · -29.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F130 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F133 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2019-09-30 · -0.232 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F134 · Trend: deposit growth over the past four quarters, what the model did with it · 2019-09-30 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F135 · Trend: construction loans as a share of loans, value at the as-of quarter · 2019-09-30 · 4.8% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F136 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 1.8% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F137 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 4.4% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F140 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2019-09-30 · -0.461 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F141 · Trend: construction loans as a share of loans, what the model did with it · 2019-09-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F142 · Trend: ratios outside their own prior range · 2019-09-30 · 12 · data/features/fct_bank_features.parquet
- F143 · Trend: ratios shown in the table (the furthest outside their prior range) · 2019-09-30 · 6 · data/features/fct_bank_features.parquet
- F144 · Trend: ratios compared with their own prior range · 2019-09-30 · 30 · data/features/fct_bank_features.parquet
- F145 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F147 · Percentile a year earlier (100 = highest risk) · 2018-09-30 · 99.9% · data/analyst/scores.parquet: percentile
- F148 · Trend: how the model's rating compares with a year earlier · 2019-09-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F152 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2019-09-30 · -2.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F153 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2019-09-30 · 0.0th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F154 · Peers: annualized provision for loan losses as a share of assets, national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F155 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2019-09-30 · 0.0th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F156 · Peers: annualized provision for loan losses as a share of assets, peer median · 2019-09-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F157 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F158 · Peers: losses on bonds available for sale, as a share of equity, bank value at the as-of quarter · 2019-09-30 · 4.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F159 · Peers: losses on bonds available for sale, as a share of equity, national percentile (100 = highest value among all banks) · 2019-09-30 · 99.9th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F160 · Peers: losses on bonds available for sale, as a share of equity, national reading · 2019-09-30 · unusually high · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F161 · Peers: losses on bonds available for sale, as a share of equity, percentile among its peers (100 = highest value) · 2019-09-30 · 100.0th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F162 · Peers: losses on bonds available for sale, as a share of equity, peer median · 2019-09-30 · -0.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F163 · Peers: losses on bonds available for sale, as a share of equity, reading against its peers · 2019-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F164 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2019-09-30 · -45.9% · data/features/fct_bank_features.parquet: return_on_equity
- F165 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2019-09-30 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F166 · Peers: return on equity (profit as a share of equity), national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F167 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2019-09-30 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F168 · Peers: return on equity (profit as a share of equity), peer median · 2019-09-30 · 10.1% · data/features/fct_bank_features.parquet: return_on_equity
- F169 · Peers: return on equity (profit as a share of equity), reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F170 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2019-09-30 · 6.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F171 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2019-09-30 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F172 · Peers: the total risk-based capital ratio, national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F173 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2019-09-30 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F174 · Peers: the total risk-based capital ratio, peer median · 2019-09-30 · 15.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F175 · Peers: the total risk-based capital ratio, reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F176 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2019-09-30 · 4.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F177 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2019-09-30 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F178 · Peers: the Tier 1 risk-based capital ratio, national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F179 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2019-09-30 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F180 · Peers: the Tier 1 risk-based capital ratio, peer median · 2019-09-30 · 14.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F181 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F182 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2019-09-30 · -36.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F183 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2019-09-30 · 0.2nd · data/features/fct_bank_features.parquet: deposit_growth_4q
- F184 · Peers: deposit growth over the past four quarters, national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: deposit_growth_4q
- F185 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2019-09-30 · 0.1st · data/features/fct_bank_features.parquet: deposit_growth_4q
- F186 · Peers: deposit growth over the past four quarters, peer median · 2019-09-30 · 5.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F187 · Peers: deposit growth over the past four quarters, reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F188 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2019-09-30 · -33.2% · data/features/fct_bank_features.parquet: asset_growth_4q
- F189 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2019-09-30 · 0.2nd · data/features/fct_bank_features.parquet: asset_growth_4q
- F190 · Peers: asset growth over the past four quarters, national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F191 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2019-09-30 · 0.1st · data/features/fct_bank_features.parquet: asset_growth_4q
- F192 · Peers: asset growth over the past four quarters, peer median · 2019-09-30 · 5.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F193 · Peers: asset growth over the past four quarters, reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F194 · Peers: equity as a share of assets, bank value at the as-of quarter · 2019-09-30 · 2.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F195 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2019-09-30 · 0.4th · data/features/fct_bank_features.parquet: equity_to_assets
- F196 · Peers: equity as a share of assets, national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F197 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2019-09-30 · 0.2nd · data/features/fct_bank_features.parquet: equity_to_assets
- F198 · Peers: equity as a share of assets, peer median · 2019-09-30 · 11.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F199 · Peers: equity as a share of assets, reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F201 · Peers: ratios in the national top or bottom 10% · 2019-09-30 · 17 · data/features/fct_bank_features.parquet
- F202 · Peers: those ratios also unusual among peers · 2019-09-30 · 17 · data/features/fct_bank_features.parquet
- F204 · Peers: cut-off for unusual (top or bottom share of banks) · 2019-09-30 · 10% · data/features/fct_bank_features.parquet
