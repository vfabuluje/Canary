---
cert: 17438
name: "First Nb Of America"
as_of: 2026-06-30
rank: 76
n_banks: 4313
percentile: 98.26107118015302
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:16:43"
writer_model: "claude-opus-5-5"
checked: true
---

# First Nb Of America (cert 17438)

*Outcome not yet known.*

## Summary

As of 2026-06-30, First Nb Of America, a bank in MI with $6.8 billion in assets, ranked 76 out of 4,313 banks nationally, placing it in the 98.3rd percentile, and it was flagged on Canary's watchlist. Its funding stands out most: brokered deposits (money placed through outside intermediaries) were 43.4% of deposits, Federal Home Loan Bank borrowings were 34.2% of assets, and loans were 160.1% of deposits, all far above national medians. Against that, it was highly profitable, with return on assets of 2.8%, and its risk-based capital ratios were slightly above the national median, though its simpler leverage ratio of 8.1% was below the median of 11.0%. The trend section shows several problem-loan ratios rising above their own past range, yet the model counted those same ratios as pulling its score down, so the two views point in different directions.

## Warning signs in the data

Capital (the owners' cushion against losses) is mixed: equity was 8.1% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.1% against 11.0%. By contrast, the risk-weighted measures, which give less weight to safer assets, were a little above the median: the Tier 1 risk-based capital ratio was 15.3% against 14.6%, and the total risk-based capital ratio was 16.5% against 15.8%.

Credit quality is weaker than typical: loans 90+ days past due or not accruing interest were 1.9% of loans against a national median of 0.5%, and nonaccrual assets plus foreclosed property were 1.9% of assets against 0.3%. Loans 30-89 days past due were 0.8% of assets against a median of 0.2%, and the Texas ratio (troubled assets against capital plus reserves) was 20.6% against 2.9%. Loan-loss reserves, money set aside for expected bad loans, were 1.1% of loans, close to the median of 1.2%. The trend section shows these problem-loan ratios edging above their own past range, yet the model treated them as lowering the score; the two readings point different ways.

Liquidity and funding are the clearest outliers: loans were 160.1% of deposits against a national median of 80.2%, brokered deposits were 43.4% of deposits against 0.0%, and core deposits (steady everyday deposits) were only 26.0% of assets against 75.5%. Federal Home Loan Bank borrowings were 34.2% of assets against a median of 0.2%, interest expense was 3.5% of assets against 1.6%, and cash was 4.6% of assets against 6.2%. Bond losses are not a concern: unrealized losses on bonds available for sale were 0.1% of equity against a median of 5.6%, and losses on bonds held to maturity were 0.0% against 0.0%. The real-estate concentration screen found that the bank did not cross either of the regulators' lines.

## Understanding the score

As of 2026-06-30, the bank ranked 76 out of 4,313 banks, which is the 98.3rd percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers about 2% of banks and held 87 banks that quarter.

The five factors that pushed the score up most were brokered deposits at 43.4% of deposits (+1.179), interest expense at 3.5% of assets (+0.570), securities at 1.2% of assets (+0.358), commercial real estate loans at 1.1% of loans (+0.303), and the efficiency ratio at 26.6% (+0.191). Some of these are low values, such as the small securities holdings and the small commercial real estate share, and the model still counted them as adding to risk.

The five factors that pulled the score down most were the Tier 1 risk-based capital ratio at 15.3% (-0.967), return on equity at 34.7% (-0.796), return on assets at 2.8% (-0.549), the total risk-based capital ratio at 16.5% (-0.475), and the Texas ratio at 20.6% (-0.311). In short, strong profits and risk-based capital offset part of the funding concerns, but not enough to keep the bank off the watchlist.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 39 | 4,589 | ▲ watchlist |
| 2024-12-31 | 57 | 4,560 | ▲ watchlist |
| 2025-03-31 | 141 | 4,536 |  |
| 2025-06-30 | 139 | 4,494 |  |
| 2025-09-30 | 121 | 4,452 |  |
| 2025-12-31 | 116 | 4,411 |  |
| 2026-03-31 | 76 | 4,353 | ▲ watchlist |
| 2026-06-30 | 76 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, the model gave First Nb Of America a national rank of 76 out of 4,313 banks, placing it in the 98.3rd percentile, where a higher percentile means a riskier rating. A year earlier it sat in the 96.9th percentile, and the model rated it riskier than a year earlier. Of 30 ratios compared with their own prior range, mostly the prior 12 quarters, 10 sat outside that range, and the table shows the 6 furthest outside it.

Each ratio's contribution is given in model log-odds units, the model's internal scoring scale, where a positive number pushes the score up and a negative one pushes it down. Commercial real estate loans (loans backed by commercial property) were 1.1% of loans, below their prior range of 1.2% to 1.4%, and their contribution of +0.303 pushed the score up. The efficiency ratio (operating costs as a share of revenue) was 26.6%, above its prior range of 24.4% to 26.4%, and its contribution of +0.191 pushed the score up.

Several ratios rose above their prior range, yet the model treated them in the opposite direction. Construction loans were 3.9% of loans, above their prior range of 1.4% to 3.6%, yet their contribution of -0.307 pushed the score down. Loans 30-89 days past due (behind on payments) were 0.8% of assets, above their prior range of 0.5% to 0.7%, yet their contribution of -0.180 pushed the score down. Nonaccrual assets (loans no longer earning interest) plus foreclosed property were 1.9% of assets, above their prior range of 1.1% to 1.8%, yet their contribution of -0.116 pushed the score down. Loans 90+ days past due or not accruing interest were 1.90% of loans, above their prior range of 1.1% to 1.88%, yet their contribution of -0.217 pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| construction loans as a share of loans | 3.9% | 1.4% to 3.6% | prior 12 quarters | +0.3 pp | +0.9 pp | -0.307 | pushed the score down |
| loans 30-89 days past due, as a share of assets | 0.8% | 0.5% to 0.7% | prior 12 quarters | +0.1 pp | +0.3 pp | -0.180 | pushed the score down |
| commercial real estate loans as a share of loans | 1.1% | 1.2% to 1.4% | prior 12 quarters | -0.1 pp | -0.3 pp | +0.303 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 26.6% | 24.4% to 26.4% | same quarter, prior 3 years | n/a | +2.0 pp | +0.191 | pushed the score up |
| nonaccrual assets and foreclosed property, as a share of assets | 1.9% | 1.1% to 1.8% | prior 12 quarters | +0.03 pp | +0.2 pp | -0.116 | pushed the score down |
| loans 90+ days past due or not accruing interest, as a share of loans | 1.90% | 1.1% to 1.88% | prior 12 quarters | +0.02 pp | +0.1 pp | -0.217 | pushed the score down |

10 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Mortgage Lending Specialization.

Peers: 36 banks in the same specialty group and size tier ($1 billion to $10 billion).

Federal Home Loan Bank borrowings, which are loans to banks from a government-sponsored lender, equaled 34.2% of assets, at the 100.0th percentile nationally, which is unusually high; at the 98.6th percentile among its peers, against a peer median of 2.2%, it is unusually high among its peers too. Interest expense, the yearly cost of paying for deposits and borrowings, was 3.5% of assets, at the 99.8th percentile nationally, which is unusually high; at the 98.6th percentile among its peers, against a peer median of 1.7%, it is unusually high among its peers too. Loans equaled 160.1% of deposits, at the 99.7th percentile nationally, which is unusually high; at the 98.6th percentile among its peers, against a peer median of 94.5%, it is unusually high among its peers too. Brokered deposits, money placed with the bank through outside intermediaries, made up 43.4% of deposits, at the 99.3rd percentile nationally, which is unusually high; at the 98.6th percentile among its peers, against a peer median of 0.0%, it is unusually high among its peers too. Core deposits, the steadier everyday deposits from regular customers, were 26.0% of assets, at the 2.6th percentile nationally, which is unusually low; at the 1.4th percentile among its peers, against a peer median of 69.0%, it is unusually low among its peers too.

On the earnings side, the efficiency ratio, operating costs as a share of revenue, was 26.6%, at the 1.4th percentile nationally, which is unusually low; at the 6.9th percentile among its peers, against a peer median of 58.8%, it is unusually low among its peers too. Return on equity, profit as a share of the owners' stake, was 34.7%, at the 98.5th percentile nationally, which is unusually high; at the 95.8th percentile among its peers, against a peer median of 8.5%, it is unusually high among its peers too. Commercial real estate loans were 1.1% of loans, at the 3.7th percentile nationally, which is unusually low; at the 21.4th percentile among its peers, against a peer median of 7.9%, it is typical for its peer group.

Overall, 13 of the bank's ratios sit in the national top or bottom 10%, and 10 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| Federal Home Loan Bank borrowings as a share of assets | 34.2% | 100.0th (unusually high) | 2.2% | 98.6th | unusually high among its peers too |
| annualized interest expense as a share of assets | 3.5% | 99.8th (unusually high) | 1.7% | 98.6th | unusually high among its peers too |
| loans as a share of deposits | 160.1% | 99.7th (unusually high) | 94.5% | 98.6th | unusually high among its peers too |
| brokered deposits as a share of deposits | 43.4% | 99.3rd (unusually high) | 0.0% | 98.6th | unusually high among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 26.6% | 1.4th (unusually low) | 58.8% | 6.9th | unusually low among its peers too |
| return on equity (profit as a share of equity) | 34.7% | 98.5th (unusually high) | 8.5% | 95.8th | unusually high among its peers too |
| core deposits as a share of assets | 26.0% | 2.6th (unusually low) | 69.0% | 1.4th | unusually low among its peers too |
| commercial real estate loans as a share of loans | 1.1% | 3.7th (unusually low) | 7.9% | 21.4th | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 39.1% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 59.7% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 159.0% | 50% or more | yes |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight, this bank remains an open watchlist case: the fact sheet contains no data from after the as-of quarter, so there is no later outcome to report. Its place on the watchlist rests on the as-of picture described above, led by its heavy reliance on brokered deposits and borrowed funding rather than everyday deposits. Being on the watchlist is a ranking, not a finding that anything has gone wrong.

## What happened next

In hindsight, our data holds no ranks, flags or filings for this bank after the as-of quarter, so we cannot say how its rank moved or whether it is still reporting. Later quarters of data, when available, will show whether its rank and watchlist status changed.

## Sources

- F1 · Bank name · n/a · First Nb Of America · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · MI · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 76 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 98.3% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 15.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 16.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 20.6% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 2.8% · data/features/fct_bank_features.parquet: return_on_assets
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 3.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 160.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 43.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 26.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 34.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 4.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $6.8 billion · data/features/fct_bank_features.parquet: log_total_assets
- F75 · Driver up #1: brokered deposits as a share of deposits, value 43.4%; contribution to the score · 2026-06-30 · +1.179 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: annualized interest expense as a share of assets, value 3.5%; contribution to the score · 2026-06-30 · +0.570 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F77 · Driver up #3: securities as a share of assets, value 1.2%; contribution to the score · 2026-06-30 · +0.358 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F78 · Driver up #4: commercial real estate loans as a share of loans, value 1.1%; contribution to the score · 2026-06-30 · +0.303 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F79 · Driver up #5: the efficiency ratio (operating costs as a share of revenue), value 26.6%; contribution to the score · 2026-06-30 · +0.191 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 15.3%; contribution to the score · 2026-06-30 · -0.967 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 34.7%; contribution to the score · 2026-06-30 · -0.796 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: return on assets (profit as a share of assets), value 2.8%; contribution to the score · 2026-06-30 · -0.549 · data/analyst/scores.parquet: feature return_on_assets contribution
- F83 · Driver down #4: the total risk-based capital ratio, value 16.5%; contribution to the score · 2026-06-30 · -0.475 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F84 · Driver down #5: the Texas ratio (troubled assets against capital plus reserves), value 20.6%; contribution to the score · 2026-06-30 · -0.311 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Trend: construction loans as a share of loans, value at the as-of quarter · 2026-06-30 · 3.9% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F90 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F91 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 3.6% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F94 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.307 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F95 · Trend: construction loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F96 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F97 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F98 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F101 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.180 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F102 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F103 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F104 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F105 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F108 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.303 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F109 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 26.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F111 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 24.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F112 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 26.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F114 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.191 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F115 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F116 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F117 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F118 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 1.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F121 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.116 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F122 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F123 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 1.90% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F124 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F125 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 1.88% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F128 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.217 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F129 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F130 · Trend: ratios outside their own prior range · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F132 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F133 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F135 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 96.9% · data/analyst/scores.parquet: percentile
- F136 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F140 · Peers: Federal Home Loan Bank borrowings as a share of assets, bank value at the as-of quarter · 2026-06-30 · 34.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F141 · Peers: Federal Home Loan Bank borrowings as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 100.0th · data/features/fct_bank_features.parquet: fhlb_to_assets
- F142 · Peers: Federal Home Loan Bank borrowings as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: fhlb_to_assets
- F143 · Peers: Federal Home Loan Bank borrowings as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: fhlb_to_assets
- F144 · Peers: Federal Home Loan Bank borrowings as a share of assets, peer median · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F145 · Peers: Federal Home Loan Bank borrowings as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: fhlb_to_assets
- F146 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F147 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F148 · Peers: annualized interest expense as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F149 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F150 · Peers: annualized interest expense as a share of assets, peer median · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F151 · Peers: annualized interest expense as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F152 · Peers: loans as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 160.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F153 · Peers: loans as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: loans_to_deposits
- F154 · Peers: loans as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: loans_to_deposits
- F155 · Peers: loans as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: loans_to_deposits
- F156 · Peers: loans as a share of deposits, peer median · 2026-06-30 · 94.5% · data/features/fct_bank_features.parquet: loans_to_deposits
- F157 · Peers: loans as a share of deposits, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: loans_to_deposits
- F158 · Peers: brokered deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 43.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F159 · Peers: brokered deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: brokered_to_deposits
- F160 · Peers: brokered deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: brokered_to_deposits
- F161 · Peers: brokered deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F162 · Peers: brokered deposits as a share of deposits, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F163 · Peers: brokered deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: brokered_to_deposits
- F164 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-06-30 · 26.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F165 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-06-30 · 1.4th · data/features/fct_bank_features.parquet: efficiency_ratio
- F166 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: efficiency_ratio
- F167 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-06-30 · 6.9th · data/features/fct_bank_features.parquet: efficiency_ratio
- F168 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-06-30 · 58.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F169 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F170 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · 34.7% · data/features/fct_bank_features.parquet: return_on_equity
- F171 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 98.5th · data/features/fct_bank_features.parquet: return_on_equity
- F172 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: return_on_equity
- F173 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 95.8th · data/features/fct_bank_features.parquet: return_on_equity
- F174 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 8.5% · data/features/fct_bank_features.parquet: return_on_equity
- F175 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F176 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2026-06-30 · 26.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F177 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 2.6th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F178 · Peers: core deposits as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F179 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 1.4th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F180 · Peers: core deposits as a share of assets, peer median · 2026-06-30 · 69.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F181 · Peers: core deposits as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F182 · Peers: commercial real estate loans as a share of loans, bank value at the as-of quarter · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F183 · Peers: commercial real estate loans as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 3.7th · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F184 · Peers: commercial real estate loans as a share of loans, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F185 · Peers: commercial real estate loans as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 21.4th · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F186 · Peers: commercial real estate loans as a share of loans, peer median · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F187 · Peers: commercial real estate loans as a share of loans, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F189 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 13 · data/features/fct_bank_features.parquet
- F190 · Peers: those ratios also unusual among peers · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F192 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
