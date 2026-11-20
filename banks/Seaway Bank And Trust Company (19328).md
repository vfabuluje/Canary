---
cert: 19328
name: "Seaway Bank And Trust Company"
as_of: 2016-12-31
rank: 7
n_banks: 5983
percentile: 99.89971586160789
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-01-27
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:14:02"
writer_model: "claude-opus-5-5"
checked: true
---

# Seaway Bank And Trust Company (cert 19328)

*Hindsight: failed 2017-01-27. Canary flagged it 4 quarters ahead.*

## Summary

As of 2016-12-31, Seaway Bank And Trust Company, a bank based in IL, ranked 7 of 5,983 banks nationally on Canary's risk score, the 99.9th percentile, and was flagged on the watchlist. Its capital, the owners' cushion for absorbing losses, had turned negative, with equity at -1.9% of assets against a national median of 10.7%. It was also losing money heavily, with return on assets (profit as a share of assets) of -7.2% against a median of 0.9%. Bad loans were common too: 8.8% of its loans were 90 or more days overdue or no longer earning interest, against a national median of 0.6%.

## Warning signs in the data

Capital was the clearest problem, because the bank's cushion against losses had fallen below zero on every measure. Equity as a share of assets was -1.9% against a national median of 10.7%, and the leverage ratio (core capital as a share of average assets) was -1.8% against 10.4%. The Tier 1 risk-based capital ratio (top-quality capital measured against risk-weighted assets) was -3.1% against 15.0%, and the total risk-based capital ratio was -1.8% against 16.2%. Because capital was negative, the code-written real-estate concentration section could not check either of its commercial real estate lines.

Credit quality, meaning how well borrowers were repaying, was also far weaker than typical. Loans 90+ days past due or not accruing interest were 8.8% of loans against a national median of 0.6%, and loans 30-89 days past due were 5.4% of assets against 0.3%. Nonaccrual assets and foreclosed property made up 4.1% of assets against 0.5%, and net loan write-offs (loans given up as lost) ran at 1.3% of loans against 0.1%. Commercial real estate loans were 42.2% of loans, well above the national median of 22.5%. Earnings did not help: return on assets was -7.2% against 0.9%, and the efficiency ratio (operating costs as a share of revenue) was 249.2% against 69.7%.

Funding showed a mixed picture. The bank leaned more on borrowed money than most, with Federal Home Loan Bank borrowings at 14.3% of assets against a median of 0.7%, and volatile funding (money that can leave quickly) at 17.7% against 5.2%. On the other hand, uninsured deposits were only 5.2% of deposits against 17.3%, core deposits were 82.2% of assets against 78.8%, and cash was 17.1% of assets against 6.6%. The bank was shrinking, with assets down -19.5% and deposits down -12.3% over the past four quarters, against national medians of 3.5% and 3.6%. Bond losses were small: unrealized losses on bonds available for sale were 1.7% of equity against a median of 0.7%, and losses on bonds held to maturity were -0.0% against 0.0%. One reading points the other way: the Texas ratio (troubled assets against capital plus reserves) was -2563.3% against a median of 4.9%, a negative figure that arises because capital had gone below zero, and the model treated it as lowering the score.

## Understanding the score

As of 2016-12-31, the bank ranked 7 of 5,983 banks, placing it in the 99.9th percentile on a scale of 0 to 100 where higher means riskier. That put it on the watchlist, which covers the top 2% of banks and held 120 banks that quarter.

The model explains its score with contributions in internal units, where a positive number pushes the score up; these are the five largest in each direction. Pushing the score up were the Tier 1 risk-based capital ratio at -3.1% (+1.908), return on equity (profit as a share of the owners' stake) at -156.0% (+1.554), and the total risk-based capital ratio at -1.8% (+0.881). Also pushing it up were the leverage ratio at -1.8% (+0.669) and loans 90+ days past due or not accruing interest at 8.8% of loans (+0.508).

Pulling the score down were interest expense at 0.6% of assets (-1.391), the Texas ratio at -2563.3% (-1.043), and construction loans at 4.1% of loans (-0.199). Total assets of $297.8 million (-0.162) and commercial real estate loans at 42.2% of loans (-0.099) also pulled it down slightly.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 7 | 6,193 | ▲ watchlist (first flag) |
| 2016-06-30 | 9 | 6,129 | ▲ watchlist |
| 2016-09-30 | 2 | 6,051 | ▲ watchlist |
| 2016-12-31 | 7 | 5,983 | ▲ watchlist |

## How its ratios moved

As of 2016-12-31, Seaway Bank And Trust Company ranked 7 of 5,983 banks nationally, placing it in the 99.9th percentile of the model's risk score. Of 30 financial ratios compared with the bank's own history, 16 sat outside their prior range, and the table shows the 6 furthest outside it. Most ratios are compared with the prior 12 quarters, while year-to-date ratios are compared with the same quarter in the prior 3 years.

Contributions below are in model log-odds units, an internal scale where a positive number pushes the score up. Return on equity (profit as a share of the owners' stake) fell to -156.0%, far below its prior range of -30.5% to 2.2%, and contributed +1.554, which pushed the score up. The leverage ratio (core capital as a share of average assets) dropped to -1.8%, below its prior range of 1.9% to 9.4%, a change of -7.5 pp over four quarters, and contributed +0.669, which pushed the score up. Return on assets (profit as a share of assets) was -7.2%, below its prior range of -2.9% to 0.2%, and contributed +0.175, which pushed the score up.

The Texas ratio (troubled assets against capital plus reserves) stood at an unusual -2563.3%, well outside its prior range of 90.3% to 192.6%, yet its contribution of -1.043 pushed the score down. Net interest margin (the spread earned on lending and investing) slipped to 3.1%, below its prior range of 4.0% to 4.9%, but its contribution of -0.054 pushed the score down. The efficiency ratio (operating costs as a share of revenue) jumped to 249.2%, well above its prior range of 88.0% to 169.8%, yet its contribution of -0.027 had little effect on the score.

There is no score from a year earlier to compare with (scores start 2016-03-31, or the bank did not report then).

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | -2563.3% | 90.3% to 192.6% | prior 12 quarters | -2755.9 pp | -2721.8 pp | -1.043 | pushed the score down |
| return on equity (profit as a share of equity) | -156.0% | -30.5% to 2.2% | same quarter, prior 3 years | n/a | -125.5 pp | +1.554 | pushed the score up |
| return on assets (profit as a share of assets) | -7.2% | -2.9% to 0.2% | same quarter, prior 3 years | n/a | -4.3 pp | +0.175 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 249.2% | 88.0% to 169.8% | same quarter, prior 3 years | n/a | +79.4 pp | -0.027 | little effect on the score |
| net interest margin (the spread earned on lending and investing) | 3.1% | 4.0% to 4.9% | same quarter, prior 3 years | n/a | -0.9 pp | -0.054 | pushed the score down |
| the leverage ratio (core capital as a share of average assets) | -1.8% | 1.9% to 9.4% | prior 12 quarters | -3.7 pp | -7.5 pp | +0.669 | pushed the score up |

16 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2016-12-31: Commercial Lending Specialization.

Peers: 2106 banks in the same specialty group and size tier ($100 million to $1 billion).

As of 2016-12-31, Seaway Bank And Trust Company ranked 7 out of 5,983 banks nationally on Canary's score, near the very top of the list. Its capital cushion, the money owners have at stake to absorb losses, stood out in this comparison. Its total risk-based capital ratio (capital measured against loans and other assets weighted by riskiness) was -1.8%, at the 0.0th national percentile, which is unusually low; among peers it sat at the 0.1st percentile against a peer median of 14.7%, unusually low among its peers too. Its Tier 1 risk-based capital ratio (the same measure using only the highest-quality capital) was -3.1%, at the 0.0th national percentile, which is unusually low; among peers it sat at the 0.1st percentile against a peer median of 13.6%, unusually low among its peers too. Equity as a share of assets was -1.9%, at the 0.0th national percentile, which is unusually low; among peers it sat at the 0.1st percentile against a peer median of 10.3%, unusually low among its peers too. The leverage ratio (core capital as a share of average assets) was -1.8%, at the 0.0th national percentile, which is unusually low; among peers it sat at the 0.1st percentile against a peer median of 10.2%, unusually low among its peers too. The Texas ratio (troubled assets against capital plus reserves) was -2563.3%, at the 0.0th national percentile, which is unusually low; among peers it sat at the 0.0th percentile against a peer median of 6.1%, unusually low among its peers too.

Profitability and costs were also far from the middle. Return on equity (profit as a share of equity) was -156.0%, at the 0.0th national percentile, which is unusually low; among peers it sat at the 0.1st percentile against a peer median of 8.4%, unusually low among its peers too. Return on assets (profit as a share of assets) was -7.2%, at the 0.1st national percentile, which is unusually low; among peers it sat at the 0.1st percentile against a peer median of 0.9%, unusually low among its peers too. The efficiency ratio (operating costs as a share of revenue, where higher means costlier) was 249.2%, at the 99.9th national percentile, which is unusually high; among peers it sat at the 99.9th percentile against a peer median of 70.1%, unusually high among its peers too.

Overall, 20 of the bank's ratios fell in the national top or bottom 10%, and 19 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | -2563.3% | 0.0th (unusually low) | 6.1% | 0.0th | unusually low among its peers too |
| the total risk-based capital ratio | -1.8% | 0.0th (unusually low) | 14.7% | 0.1st | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | -3.1% | 0.0th (unusually low) | 13.6% | 0.1st | unusually low among its peers too |
| equity as a share of assets | -1.9% | 0.0th (unusually low) | 10.3% | 0.1st | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | -1.8% | 0.0th (unusually low) | 10.2% | 0.1st | unusually low among its peers too |
| return on equity (profit as a share of equity) | -156.0% | 0.0th (unusually low) | 8.4% | 0.1st | unusually low among its peers too |
| return on assets (profit as a share of assets) | -7.2% | 0.1st (unusually low) | 0.9% | 0.1st | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 249.2% | 99.9th (unusually high) | 70.1% | 99.9th | unusually high among its peers too |

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

In hindsight, Canary first flagged the bank in the quarter ending 2016-03-31, and the bank failed on 2017-01-27. Under Canary's lead-time rule, that warning came 4 quarters before the failure. The bank was still on the watchlist at 2016-12-31, ranked 7 of 5,983.

At the first flag, capital was still positive but thin, with a Tier 1 risk-based capital ratio of 5.5% and a total risk-based capital ratio of 6.8%. At that point the Texas ratio was 167.1%, return on equity was -63.1%, and 19.5% of loans were 90+ days past due or not accruing interest, all of which pushed the score up.

## What happened next

In hindsight, the bank failed on 2017-01-27. Its last report in our data was for the quarter ending 2016-12-31, so there are no later ranks or flags. Our data shows only that the bank stopped reporting; the failure date comes from the fact sheet, not from the reports themselves.

## Sources

- F1 · Bank name · n/a · Seaway Bank And Trust Company · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-12-31 · 7 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-12-31 · 5,983 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-12-31 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-12-31 · 120 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-12-31 · -1.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-12-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · -1.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-12-31 · -3.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-12-31 · 15.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-12-31 · -1.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-12-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 8.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 4.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2016-12-31 · 5.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2016-12-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2016-12-31 · 1.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2016-12-31 · 0.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2016-12-31 · 42.2% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2016-12-31 · 22.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2016-12-31 · -2563.3% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2016-12-31 · 4.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-12-31 · -7.2% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-12-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2016-12-31 · 249.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2016-12-31 · 69.7% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2016-12-31 · 5.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2016-12-31 · 17.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2016-12-31 · 82.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2016-12-31 · 78.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2016-12-31 · 14.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2016-12-31 · 0.7% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2016-12-31 · 17.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2016-12-31 · 5.2% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2016-12-31 · 17.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2016-12-31 · 6.6% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2016-12-31 · -0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2016-12-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2016-12-31 · 1.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2016-12-31 · 0.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2016-12-31 · -19.5% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2016-12-31 · 3.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2016-12-31 · -12.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2016-12-31 · 3.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value -3.1%; contribution to the score · 2016-12-31 · +1.908 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -156.0%; contribution to the score · 2016-12-31 · +1.554 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the total risk-based capital ratio, value -1.8%; contribution to the score · 2016-12-31 · +0.881 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value -1.8%; contribution to the score · 2016-12-31 · +0.669 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: loans 90+ days past due or not accruing interest, as a share of loans, value 8.8%; contribution to the score · 2016-12-31 · +0.508 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.6%; contribution to the score · 2016-12-31 · -1.391 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value -2563.3%; contribution to the score · 2016-12-31 · -1.043 · data/analyst/scores.parquet: feature texas_ratio contribution
- F82 · Driver down #3: construction loans as a share of loans, value 4.1%; contribution to the score · 2016-12-31 · -0.199 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: total assets, value $297.8 million; contribution to the score · 2016-12-31 · -0.162 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: commercial real estate loans as a share of loans, value 42.2%; contribution to the score · 2016-12-31 · -0.099 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F85 · Failure date · 2017-01-27 · 2017-01-27 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-03-31: the Tier 1 risk-based capital ratio, value 5.5%; contribution to the score · 2016-03-31 · +1.369 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2016-03-31: the Texas ratio (troubled assets against capital plus reserves), value 167.1%; contribution to the score · 2016-03-31 · +1.342 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2016-03-31: return on equity (profit as a share of equity), value -63.1%; contribution to the score · 2016-03-31 · +1.324 · data/analyst/scores.parquet: feature return_on_equity contribution
- F91 · Driver up #4 at 2016-03-31: loans 90+ days past due or not accruing interest, as a share of loans, value 19.5%; contribution to the score · 2016-03-31 · +0.741 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2016-03-31: the total risk-based capital ratio, value 6.8%; contribution to the score · 2016-03-31 · +0.472 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2016-12-31 · -2563.3% · data/features/fct_bank_features.parquet: texas_ratio
- F100 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 90.3% · data/features/fct_bank_features.parquet: texas_ratio
- F101 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 192.6% · data/features/fct_bank_features.parquet: texas_ratio
- F104 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2016-12-31 · -1.043 · data/analyst/scores.parquet: feature texas_ratio contribution
- F105 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2016-12-31 · pushed the score down · data/analyst/scores.parquet: feature texas_ratio contribution
- F106 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2016-12-31 · -156.0% · data/features/fct_bank_features.parquet: return_on_equity
- F107 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -30.5% · data/features/fct_bank_features.parquet: return_on_equity
- F108 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: return_on_equity
- F110 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2016-12-31 · +1.554 · data/analyst/scores.parquet: feature return_on_equity contribution
- F111 · Trend: return on equity (profit as a share of equity), what the model did with it · 2016-12-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F112 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2016-12-31 · -7.2% · data/features/fct_bank_features.parquet: return_on_assets
- F113 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -2.9% · data/features/fct_bank_features.parquet: return_on_assets
- F114 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: return_on_assets
- F116 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2016-12-31 · +0.175 · data/analyst/scores.parquet: feature return_on_assets contribution
- F117 · Trend: return on assets (profit as a share of assets), what the model did with it · 2016-12-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F118 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2016-12-31 · 249.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F119 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 88.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F120 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 169.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F122 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2016-12-31 · -0.027 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F123 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2016-12-31 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F124 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2016-12-31 · 3.1% · data/features/fct_bank_features.parquet: net_interest_margin
- F125 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 4.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F126 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 4.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F128 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2016-12-31 · -0.054 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F129 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2016-12-31 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F130 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2016-12-31 · -1.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F131 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 1.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F132 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 9.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F134 · Trend: the leverage ratio (core capital as a share of average assets), change over four quarters, in percentage points · 2016-12-31 · -7.5 pp · data/features/fct_bank_features.parquet: leverage_ratio
- F135 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2016-12-31 · +0.669 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F136 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2016-12-31 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F137 · Trend: ratios outside their own prior range · 2016-12-31 · 16 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios shown in the table (the furthest outside their prior range) · 2016-12-31 · 6 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios compared with their own prior range · 2016-12-31 · 30 · data/features/fct_bank_features.parquet
- F140 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F145 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2016-12-31 · -2563.3% · data/features/fct_bank_features.parquet: texas_ratio
- F146 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2016-12-31 · 0.0th · data/features/fct_bank_features.parquet: texas_ratio
- F147 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: texas_ratio
- F148 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2016-12-31 · 0.0th · data/features/fct_bank_features.parquet: texas_ratio
- F149 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2016-12-31 · 6.1% · data/features/fct_bank_features.parquet: texas_ratio
- F150 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F151 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2016-12-31 · -1.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F152 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2016-12-31 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F153 · Peers: the total risk-based capital ratio, national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F154 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F155 · Peers: the total risk-based capital ratio, peer median · 2016-12-31 · 14.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F156 · Peers: the total risk-based capital ratio, reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F157 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2016-12-31 · -3.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F158 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2016-12-31 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F159 · Peers: the Tier 1 risk-based capital ratio, national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F160 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F161 · Peers: the Tier 1 risk-based capital ratio, peer median · 2016-12-31 · 13.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F162 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F163 · Peers: equity as a share of assets, bank value at the as-of quarter · 2016-12-31 · -1.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F164 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2016-12-31 · 0.0th · data/features/fct_bank_features.parquet: equity_to_assets
- F165 · Peers: equity as a share of assets, national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F166 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: equity_to_assets
- F167 · Peers: equity as a share of assets, peer median · 2016-12-31 · 10.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F168 · Peers: equity as a share of assets, reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F169 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2016-12-31 · -1.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F170 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2016-12-31 · 0.0th · data/features/fct_bank_features.parquet: leverage_ratio
- F171 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F172 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: leverage_ratio
- F173 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2016-12-31 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F174 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F175 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2016-12-31 · -156.0% · data/features/fct_bank_features.parquet: return_on_equity
- F176 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2016-12-31 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F177 · Peers: return on equity (profit as a share of equity), national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F178 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F179 · Peers: return on equity (profit as a share of equity), peer median · 2016-12-31 · 8.4% · data/features/fct_bank_features.parquet: return_on_equity
- F180 · Peers: return on equity (profit as a share of equity), reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F181 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2016-12-31 · -7.2% · data/features/fct_bank_features.parquet: return_on_assets
- F182 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: return_on_assets
- F183 · Peers: return on assets (profit as a share of assets), national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F184 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: return_on_assets
- F185 · Peers: return on assets (profit as a share of assets), peer median · 2016-12-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F186 · Peers: return on assets (profit as a share of assets), reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F187 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2016-12-31 · 249.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F188 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2016-12-31 · 99.9th · data/features/fct_bank_features.parquet: efficiency_ratio
- F189 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2016-12-31 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F190 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2016-12-31 · 99.9th · data/features/fct_bank_features.parquet: efficiency_ratio
- F191 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2016-12-31 · 70.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F192 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2016-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F194 · Peers: ratios in the national top or bottom 10% · 2016-12-31 · 20 · data/features/fct_bank_features.parquet
- F195 · Peers: those ratios also unusual among peers · 2016-12-31 · 19 · data/features/fct_bank_features.parquet
- F197 · Peers: cut-off for unusual (top or bottom share of banks) · 2016-12-31 · 10% · data/features/fct_bank_features.parquet
