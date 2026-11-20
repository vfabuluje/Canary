---
cert: 31723
name: "Home Savings Bank Fsb"
as_of: 2026-06-30
rank: 18
n_banks: 4313
percentile: 99.6058428008347
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:16:24"
writer_model: "claude-opus-5-5"
checked: true
---

# Home Savings Bank Fsb (cert 31723)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Home Savings Bank Fsb, a small bank based in KY, ranked 18 out of 4,313 FDIC-insured banks on Canary's risk score, placing it in the 99.6th percentile, where higher means riskier. That puts it on Canary's watchlist, which covers the top 2% of banks by score. The main concerns are troubled loans and losses: loans 90+ days past due or not accruing interest were 7.5% of loans against a national median of 0.5%, and return on assets (profit as a share of assets) was -1.3% against a median of 1.2%. Pointing the other way, its equity cushion of 11.3% of assets is above the national median of 10.6%, and only 2.0% of its deposits are uninsured.

## Warning signs in the data

Credit quality is the clearest weak spot: loans 90+ days past due or not accruing interest were 7.5% of loans, far above the national median of 0.5%. Nonaccrual assets (loans no longer booking interest) plus foreclosed property were 5.8% of assets against a median of 0.3%, and loans 30-89 days late were 0.9% of assets against a median of 0.2%. The Texas ratio, which weighs troubled assets against capital plus reserves, was 48.8%, well above the national median of 2.9%. Even so, loan-loss reserves (money set aside for expected bad loans) were only 0.8% of loans, below the median of 1.2%.

Earnings are weak: return on assets was -1.3% against a national median of 1.2%, and the efficiency ratio (operating costs as a share of revenue) was 147.6% against a median of 62.1%, meaning costs exceeded revenue. Its net interest margin (the spread earned on lending and investing) was 2.6%, below the median of 3.9%, while interest expense was 2.4% of assets, above the median of 1.6%.

Capital and liquidity look mixed rather than weak: equity was 11.3% of assets, above the median of 10.6%, though the leverage ratio (core capital as a share of average assets) was 10.2%, below the median of 11.0%. Loans were 99.6% of deposits against a median of 80.2%, and Federal Home Loan Bank borrowings (loans from a government-sponsored lender) were 9.8% of assets against a median of 0.2%. On the other hand, cash was 19.2% of assets, well above the median of 6.2%, and uninsured deposits were 2.0% of deposits against a median of 24.8%. Bond losses are not a concern here: the bank held securities worth 0.0% of assets against a median of 17.6%, so its unrealized losses on bonds available for sale were 0.0% of equity against a median of 5.6%. So the data points two ways: credit quality and earnings are poor, while cash, deposit mix and bond exposure look comfortable, and the separate real-estate concentration check found the bank did not cross either line.

## Understanding the score

As of 2026-06-30, the bank ranked 18 out of 4,313 banks, in the 99.6th percentile on a 0 to 100 scale where higher means riskier. It is flagged on the watchlist, which holds the top 2% of banks by score, or 87 banks that quarter.

Five features pushed the score up most: loans 90+ days past due or not accruing at 7.5% of loans, contributing +0.914; the Texas ratio at 48.8%, contributing +0.840; securities at 0.0% of assets, contributing +0.365; interest expense at 2.4% of assets, contributing +0.278; and commercial real estate loans at 7.8% of loans, contributing +0.248.

Five features pulled the score down most: the Tier 1 risk-based capital ratio (core capital against risk-weighted assets), contributing -0.883; construction loans at 3.6% of loans, contributing -0.463; the leverage ratio at 10.2%, contributing -0.297; return on equity (profit as a share of the owners' stake) at -11.4%, contributing -0.248; and loan-loss reserves at 0.8% of loans, contributing -0.225. Some of these pulls look counterintuitive, such as a negative return on equity lowering the score; that is how the model weighed them, not a judgment that losses are good.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 525 | 4,589 |  |
| 2024-12-31 | 511 | 4,560 |  |
| 2025-03-31 | 828 | 4,536 |  |
| 2025-06-30 | 404 | 4,494 |  |
| 2025-09-30 | 16 | 4,452 | ▲ watchlist |
| 2025-12-31 | 20 | 4,411 | ▲ watchlist |
| 2026-03-31 | 26 | 4,353 | ▲ watchlist |
| 2026-06-30 | 18 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, the bank ranked 18 out of 4,313 banks nationally, placing it in the 99.6th percentile, where a higher percentile means riskier. A year earlier, on 2025-06-30, it sat in the 91.0th percentile, and the model rated it riskier than a year earlier. Each ratio is compared with its own range over the prior 12 quarters, or over the same quarter in the prior 3 years for year-to-date ratios, and 13 of the 28 ratios checked fell outside that range. Each ratio's contribution is shown in model log-odds units, where a positive number pushes the score up and a negative one pushes it down.

Return on equity (profit as a share of the owners' stake) was -11.4%, below its prior range of -8.5% to 0.1%, yet it pushed the score down, with a contribution of -0.248. Return on assets (profit as a share of assets) was -1.3%, also below its prior range of -1.0% to 0.0%, yet it too pushed the score down, contributing -0.126. The efficiency ratio (operating costs as a share of revenue) was 147.6%, above its prior range of 99.3% to 136.5%, but it had little effect on the score, contributing -0.013.

Federal Home Loan Bank borrowings (loans to banks from a government-sponsored lender) were 9.8% of assets, below their prior range of 15.0% to 21.0%, and had little effect on the score, contributing -0.014. Core deposits (steady, everyday customer deposits) were 72.5% of assets, above their prior range of 62.5% to 68.7%, and also had little effect on the score, contributing -0.050. The leverage ratio (core capital as a share of average assets) was 10.2%, just below its prior range of 10.5% to 12.8%, yet it pushed the score down, contributing -0.297.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| Federal Home Loan Bank borrowings as a share of assets | 9.8% | 15.0% to 21.0% | prior 12 quarters | -5.2 pp | -9.2 pp | -0.014 | little effect on the score |
| core deposits as a share of assets | 72.5% | 62.5% to 68.7% | prior 12 quarters | +3.7 pp | +5.2 pp | -0.050 | little effect on the score |
| return on equity (profit as a share of equity) | -11.4% | -8.5% to 0.1% | same quarter, prior 3 years | n/a | -2.9 pp | -0.248 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 147.6% | 99.3% to 136.5% | same quarter, prior 3 years | n/a | +11.1 pp | -0.013 | little effect on the score |
| return on assets (profit as a share of assets) | -1.3% | -1.0% to 0.0% | same quarter, prior 3 years | n/a | -0.3 pp | -0.126 | pushed the score down |
| the leverage ratio (core capital as a share of average assets) | 10.2% | 10.5% to 12.8% | prior 12 quarters | -0.3 pp | -0.5 pp | -0.297 | pushed the score down |

13 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Mortgage Lending Specialization.

Peers: 76 banks in the same specialty group and size tier (under $100 million).

The Texas ratio, which weighs troubled assets against the bank's capital plus reserves, was 48.8%, at the 99.5th percentile nationally, which is unusually high; at the 98.0th percentile among its peers, against a peer median of 1.7%, it is unusually high among its peers too. Nonaccrual assets (loans on which the bank has stopped booking interest) plus foreclosed property made up 5.8% of assets, at the 99.4th percentile nationally, which is unusually high; at the 99.3rd percentile among its peers, against a peer median of 0.1%, this is unusually high among its peers too. Loans 90+ days past due or not accruing interest were 7.5% of loans, at the 99.1st percentile nationally, which is unusually high; at the 97.9th percentile among its peers, against a peer median of 0.5%, this is unusually high among its peers too.

The efficiency ratio, operating costs as a share of revenue, was 147.6%, at the 98.9th percentile nationally, which is unusually high; at the 96.7th percentile among its peers, against a peer median of 83.5%, it is unusually high among its peers too. Return on equity, profit as a share of the owners' stake, was -11.4%, at the 1.2nd percentile nationally, which is unusually low; at the 5.9th percentile among its peers, against a peer median of 2.6%, it is unusually low among its peers too. Return on assets, profit as a share of assets, was -1.3%, at the 1.6th percentile nationally, which is unusually low; at the 7.2nd percentile among its peers, against a peer median of 0.3%, it is unusually low among its peers too. Asset growth over the past four quarters was -7.4%, at the 2.7th percentile nationally, which is unusually low; at the 7.2nd percentile among its peers, against a peer median of 1.0%, it is unusually low among its peers too.

Uninsured deposits, money held above the government insurance limit, were 2.0% of deposits, at the 0.6th percentile nationally, which is unusually low; at the 8.6th percentile among its peers, against a peer median of 9.9%, this is unusually low among its peers too. Overall, 13 of the bank's ratios sit in the national top or bottom 10%, and 8 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 48.8% | 99.5th (unusually high) | 1.7% | 98.0th | unusually high among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 5.8% | 99.4th (unusually high) | 0.1% | 99.3rd | unusually high among its peers too |
| uninsured deposits as a share of deposits | 2.0% | 0.6th (unusually low) | 9.9% | 8.6th | unusually low among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 7.5% | 99.1st (unusually high) | 0.5% | 97.9th | unusually high among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 147.6% | 98.9th (unusually high) | 83.5% | 96.7th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -11.4% | 1.2nd (unusually low) | 2.6% | 5.9th | unusually low among its peers too |
| return on assets (profit as a share of assets) | -1.3% | 1.6th (unusually low) | 0.3% | 7.2nd | unusually low among its peers too |
| asset growth over the past four quarters | -7.4% | 2.7th (unusually low) | 1.0% | 7.2nd | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 25.8% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 150.9% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -3.8% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

Hindsight view: this bank is an open watchlist case, meaning it was flagged and no later outcome is recorded in our data yet. The fact sheet holds no information from after the as-of quarter, so there is nothing yet to confirm or contradict the flag.

## What happened next

Hindsight view: our data does not yet include any quarter after the as-of quarter for this bank. Later ranks, watchlist flags and whether the bank keeps reporting are therefore not available here; they will appear once newer filings are added.

## Sources

- F1 · Bank name · n/a · Home Savings Bank Fsb · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KY · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 18 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.6% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 11.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 7.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 5.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 48.8% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F39 · Bank: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F40 · National median: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F41 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 147.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F42 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F43 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 2.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F44 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F45 · Bank: loans as a share of deposits · 2026-06-30 · 99.6% · data/features/fct_bank_features.parquet: loans_to_deposits
- F46 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 19.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F63 · Bank: securities as a share of assets · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F64 · National median: securities as a share of assets · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F71 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 7.5%; contribution to the score · 2026-06-30 · +0.914 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F72 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 48.8%; contribution to the score · 2026-06-30 · +0.840 · data/analyst/scores.parquet: feature texas_ratio contribution
- F73 · Driver up #3: securities as a share of assets, value 0.0%; contribution to the score · 2026-06-30 · +0.365 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F74 · Driver up #4: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2026-06-30 · +0.278 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F75 · Driver up #5: commercial real estate loans as a share of loans, value 7.8%; contribution to the score · 2026-06-30 · +0.248 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.883 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: construction loans as a share of loans, value 3.6%; contribution to the score · 2026-06-30 · -0.463 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F78 · Driver down #3: the leverage ratio (core capital as a share of average assets), value 10.2%; contribution to the score · 2026-06-30 · -0.297 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver down #4: return on equity (profit as a share of equity), value -11.4%; contribution to the score · 2026-06-30 · -0.248 · data/analyst/scores.parquet: feature return_on_equity contribution
- F80 · Driver down #5: loan-loss reserves as a share of loans, value 0.8%; contribution to the score · 2026-06-30 · -0.225 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F81 · Trend: Federal Home Loan Bank borrowings as a share of assets, value at the as-of quarter · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F82 · Trend: Federal Home Loan Bank borrowings as a share of assets, lowest value in the comparison window · n/a · 15.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F83 · Trend: Federal Home Loan Bank borrowings as a share of assets, highest value in the comparison window · n/a · 21.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F86 · Trend: Federal Home Loan Bank borrowings as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.014 · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F87 · Trend: Federal Home Loan Bank borrowings as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F88 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 72.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F89 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 62.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F90 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 68.7% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F93 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.050 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F94 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F95 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -11.4% · data/features/fct_bank_features.parquet: return_on_equity
- F96 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -8.5% · data/features/fct_bank_features.parquet: return_on_equity
- F97 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: return_on_equity
- F99 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.248 · data/analyst/scores.parquet: feature return_on_equity contribution
- F100 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 147.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F102 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 99.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F103 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 136.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.013 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F107 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F108 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -1.0% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: return_on_assets
- F111 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.126 · data/analyst/scores.parquet: feature return_on_assets contribution
- F112 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F113 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F114 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F115 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 12.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F118 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.297 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F119 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature leverage_ratio contribution
- F120 · Trend: ratios outside their own prior range · 2026-06-30 · 13 · data/features/fct_bank_features.parquet
- F122 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F123 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F124 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F125 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 91.0% · data/analyst/scores.parquet: percentile
- F126 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F130 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 48.8% · data/features/fct_bank_features.parquet: texas_ratio
- F131 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: texas_ratio
- F132 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F133 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 98.0th · data/features/fct_bank_features.parquet: texas_ratio
- F134 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: texas_ratio
- F135 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F136 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 5.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F137 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.4th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F138 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F139 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F140 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F141 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F142 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F143 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.6th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F144 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F145 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 8.6th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F146 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 9.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F147 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F148 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 7.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F149 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.1st · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F150 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F151 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 97.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F152 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F153 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F154 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-06-30 · 147.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F155 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-06-30 · 98.9th · data/features/fct_bank_features.parquet: efficiency_ratio
- F156 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F157 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-06-30 · 96.7th · data/features/fct_bank_features.parquet: efficiency_ratio
- F158 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-06-30 · 83.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F159 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F160 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -11.4% · data/features/fct_bank_features.parquet: return_on_equity
- F161 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 1.2nd · data/features/fct_bank_features.parquet: return_on_equity
- F162 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F163 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 5.9th · data/features/fct_bank_features.parquet: return_on_equity
- F164 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: return_on_equity
- F165 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F166 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2026-06-30 · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F167 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 1.6th · data/features/fct_bank_features.parquet: return_on_assets
- F168 · Peers: return on assets (profit as a share of assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F169 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2026-06-30 · 7.2nd · data/features/fct_bank_features.parquet: return_on_assets
- F170 · Peers: return on assets (profit as a share of assets), peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F171 · Peers: return on assets (profit as a share of assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F172 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -7.4% · data/features/fct_bank_features.parquet: asset_growth_4q
- F173 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 2.7th · data/features/fct_bank_features.parquet: asset_growth_4q
- F174 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F175 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 7.2nd · data/features/fct_bank_features.parquet: asset_growth_4q
- F176 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 1.0% · data/features/fct_bank_features.parquet: asset_growth_4q
- F177 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F179 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 13 · data/features/fct_bank_features.parquet
- F180 · Peers: those ratios also unusual among peers · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F182 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
