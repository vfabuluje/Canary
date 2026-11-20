---
cert: 30003
name: "Guaranty Bank"
as_of: 2017-03-31
rank: 33
n_banks: 5925
percentile: 99.45991561181434
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-05-05
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:14:22"
writer_model: "claude-opus-5-5"
checked: true
---

# Guaranty Bank (cert 30003)

*Hindsight: failed 2017-05-05. Canary flagged it 4 quarters ahead.*

## Summary

As of 2017-03-31, Guaranty Bank, a bank based in WI with $1.0 billion in assets, ranked 33 out of 5,925 banks nationally on Canary's risk score, placing it at the 99.5th percentile on a scale where higher means riskier. That put it on Canary's watchlist, which covers the top 2% of banks by score. The central concern is thin capital, the owners' cushion against losses: equity was 2.1% of assets against a national median of 10.7%, and its Texas ratio, troubled assets measured against capital plus reserves, was 109.7%. Its funding, by contrast, looked stable, with core deposits, the steady everyday deposits of ordinary customers, making up 97.0% of assets.

## Warning signs in the data

Capital was the weakest area by far. Equity was 2.1% of assets against a national median of 10.7%, and the leverage ratio, core capital as a share of average assets, was 2.1% against a median of 10.5%. The Tier 1 risk-based capital ratio, which measures the strongest capital against assets weighted by their riskiness, was 3.1% against a median of 15.1%, and the total risk-based capital ratio was 4.4% against a median of 16.2%.

Credit quality was also well outside the norm. Loans 90 or more days past due or no longer paying interest were 4.5% of loans against a national median of 0.6%, and nonaccrual assets plus foreclosed property were 3.4% of assets against a median of 0.5%. The Texas ratio stood at 109.7%, far above the national median of 4.8%, and net loan write-offs, bad loans written off minus recoveries, ran at 0.4% of loans against a median of 0.0%. The two views point different ways: the trend section shows these credit measures had fallen below their own recent ranges, so they were improving against the bank's own history, yet they remained far worse than the national medians. Earnings were modest, with return on assets, profit as a share of assets, at 0.4% against a median of 0.9%, and an efficiency ratio, operating costs as a share of revenue, of 93.9% against a median of 69.8%. Return on equity was 21.5%, well above the 8.0% median, but it was measured against a very thin equity base.

Funding and liquidity, the ability to meet cash needs, looked strong. Core deposits were 97.0% of assets against a national median of 79.0%, uninsured deposits, balances above the FDIC insurance limit, were 1.3% of deposits against a median of 17.3%, and volatile funding was 0.1% of assets against a median of 5.1%. Cash was 14.9% of assets against a median of 6.9%. Bond losses were small: unrealized losses on bonds available for sale were 0.4% of equity against a median of 0.3%, and on bonds held to maturity were -0.2% against a median of 0.0%, with securities making up only 0.9% of assets against a median of 17.9%.

## Understanding the score

As of 2017-03-31, Guaranty Bank ranked 33 out of 5,925 banks nationally, which put it at the 99.5th percentile on a 0 to 100 scale where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks by score, one of 119 banks on it that quarter.

The five factors that pushed the score up most were a Tier 1 risk-based capital ratio of 3.1%, contributing +1.350, a Texas ratio of 109.7%, contributing +0.604, and a total risk-based capital ratio of 4.4%, contributing +0.518. The other two were core deposits at 97.0% of assets, contributing +0.318, and commercial real estate loans at 0.2% of loans, contributing +0.281.

The five factors that pulled the score down most were interest expense at 0.0% of assets, contributing -1.410, return on equity of 21.5%, contributing -0.861, and loans 30-89 days past due at 0.3% of assets, contributing -0.619. The remaining two were return on assets of 0.4%, contributing -0.558, and total assets of $1.0 billion, contributing -0.340.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 20 | 6,193 | ▲ watchlist |
| 2016-06-30 | 21 | 6,129 | ▲ watchlist (first flag) |
| 2016-09-30 | 11 | 6,051 | ▲ watchlist |
| 2016-12-31 | 17 | 5,983 | ▲ watchlist |
| 2017-03-31 | 33 | 5,925 | ▲ watchlist |

## How its ratios moved

As of 2017-03-31, Guaranty Bank ranked 33 out of 5,925 banks nationally, which put it at the 99.5th percentile on a scale where higher means riskier. A year earlier, on 2016-03-31, it sat at the 99.7th percentile, and the model rated it about the same as a year earlier. Of 30 ratios compared with their own prior range, usually the prior 12 quarters, 12 sat outside that range, and the 6 furthest outside are described here.

The Texas ratio, which weighs troubled loans and property against capital plus reserves, stood at 109.7%, below its prior range of 125.6% to 175.8%, yet the model still pushed the score up with a contribution of +0.604 model log-odds units. That ratio changed by -16.3 pp over one quarter and by -27.1 pp over four quarters. Nonaccrual assets (loans no longer paying interest) plus foreclosed property were 3.4% of assets, below their prior range of 3.9% to 8.4%, but despite that move this ratio had little effect on the score, contributing +0.020. Net loan write-offs (bad loans written off, minus recoveries) ran at an annualized 0.4% of loans, below their prior range of 0.9% to 3.7%, yet this ratio also had little effect on the score, contributing -0.012.

Loans 30-89 days past due were 0.3% of assets, under their prior range of 0.4% to 0.8%, and this pushed the score down with a contribution of -0.619. Construction loans were 0.0% of all loans, below their prior range of 0.2% to 2.0%, and this pushed the score down with a contribution of -0.224. Net interest margin, the spread earned on lending and investing, was 3.8%, above its prior range of 2.6% to 3.6%, and this pushed the score down with a contribution of -0.125.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 109.7% | 125.6% to 175.8% | prior 12 quarters | -16.3 pp | -27.1 pp | +0.604 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.4% | 0.9% to 3.7% | same quarter, prior 3 years | n/a | -0.5 pp | -0.012 | little effect on the score |
| net interest margin (the spread earned on lending and investing) | 3.8% | 2.6% to 3.6% | same quarter, prior 3 years | n/a | +0.2 pp | -0.125 | pushed the score down |
| loans 30-89 days past due, as a share of assets | 0.3% | 0.4% to 0.8% | prior 12 quarters | -0.2 pp | -0.1 pp | -0.619 | pushed the score down |
| construction loans as a share of loans | 0.0% | 0.2% to 2.0% | prior 12 quarters | -0.2 pp | -0.4 pp | -0.224 | pushed the score down |
| nonaccrual assets and foreclosed property, as a share of assets | 3.4% | 3.9% to 8.4% | prior 12 quarters | -0.5 pp | -1.2 pp | +0.020 | little effect on the score |

12 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2017-03-31: Mortgage Lending Specialization.

Peers: 37 banks in the same specialty group and size tier ($1 billion to $10 billion).

Guaranty Bank ranked 33 out of 5,925 banks nationally, placing it at the 99.5th percentile of Canary's score. Its total risk-based capital ratio, the owners' cushion against losses measured against assets weighted by their risk, was 4.4%, at the 0.1st percentile nationally (unusually low), and at the 1.4th percentile among its peers against a peer median of 17.5%, which is unusually low among its peers too. Its Tier 1 risk-based capital ratio, the same measure using only the strongest form of capital, was 3.1%, at the 0.1st percentile nationally (unusually low), and at the 1.4th percentile among its peers against a peer median of 16.6%, which is unusually low among its peers too. Its leverage ratio, core capital as a share of average assets, was 2.1%, at the 0.4th percentile nationally (unusually low), and at the 1.4th percentile among its peers against a peer median of 9.7%, which is unusually low among its peers too. Its equity as a share of assets, the owners' stake in the bank, was 2.1%, at the 0.4th percentile nationally (unusually low), and at the 1.4th percentile among its peers against a peer median of 9.8%, which is unusually low among its peers too. Its Texas ratio, which compares troubled loans and assets with capital plus loss reserves, was 109.7%, at the 99.5th percentile nationally (unusually high), and at the 98.6th percentile among its peers against a peer median of 2.7%, which is unusually high among its peers too.

On the funding side, core deposits, the stable everyday deposits of ordinary customers, made up 97.0% of assets, at the 100.0th percentile nationally (unusually high), and at the 98.6th percentile among its peers against a peer median of 73.0%, which is unusually high among its peers too. Uninsured deposits, balances above the FDIC insurance limit, were 1.3% of deposits, at the 0.7th percentile nationally (unusually low), and at the 1.4th percentile among its peers against a peer median of 12.1%, which is unusually low among its peers too. Annualized interest expense, what the bank pays on its deposits and borrowings, was 0.0% of assets, at the 1.9th percentile nationally (unusually low), and at the 6.8th percentile among its peers against a peer median of 0.4%, which is unusually low among its peers too. Overall, 18 of the bank's ratios sat in the national top or bottom 10%, and 13 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| core deposits as a share of assets | 97.0% | 100.0th (unusually high) | 73.0% | 98.6th | unusually high among its peers too |
| the total risk-based capital ratio | 4.4% | 0.1st (unusually low) | 17.5% | 1.4th | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 3.1% | 0.1st (unusually low) | 16.6% | 1.4th | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | 2.1% | 0.4th (unusually low) | 9.7% | 1.4th | unusually low among its peers too |
| equity as a share of assets | 2.1% | 0.4th (unusually low) | 9.8% | 1.4th | unusually low among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 109.7% | 99.5th (unusually high) | 2.7% | 98.6th | unusually high among its peers too |
| uninsured deposits as a share of deposits | 1.3% | 0.7th (unusually low) | 12.1% | 1.4th | unusually low among its peers too |
| annualized interest expense as a share of assets | 0.0% | 1.9th (unusually low) | 0.4% | 6.8th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: total risk-based capital, as the 2006 guidance specifies.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.5% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 3.4% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -92.1% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, Canary caught this bank: it first flagged Guaranty Bank in the quarter ending 2016-06-30, and the bank failed on 2017-05-05. That gave a lead time of 4 quarters before the failure.

At that first flag, the main factors pushing the score up were already capital and troubled assets: a Tier 1 risk-based capital ratio of 3.3%, contributing +1.814, a Texas ratio of 125.6%, contributing +1.083, and a total risk-based capital ratio of 4.5%, contributing +0.426. The same weaknesses still led the drivers up at the as-of quarter, so the warning was consistent over time.

## What happened next

In hindsight, the quarter ending 2017-03-31 was the last one for which Guaranty Bank reported data. The bank failed on 2017-05-05, so there are no later ranks or watchlist flags for it.

## Sources

- F1 · Bank name · n/a · Guaranty Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WI · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2017-03-31 · 33 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2017-03-31 · 5,925 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2017-03-31 · 99.5% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2017-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2017-03-31 · 119 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2017-03-31 · 2.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2017-03-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · 2.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2017-03-31 · 3.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2017-03-31 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2017-03-31 · 4.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2017-03-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 4.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 3.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2017-03-31 · 0.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2017-03-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 109.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 4.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2017-03-31 · 0.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2017-03-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2017-03-31 · 21.5% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2017-03-31 · 8.0% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2017-03-31 · 93.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2017-03-31 · 69.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2017-03-31 · 1.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2017-03-31 · 17.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2017-03-31 · 97.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2017-03-31 · 79.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2017-03-31 · 0.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2017-03-31 · 5.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2017-03-31 · 14.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2017-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2017-03-31 · -0.2% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2017-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2017-03-31 · 0.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2017-03-31 · 0.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2017-03-31 · 0.9% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2017-03-31 · 17.9% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F69 · Bank: total assets · 2017-03-31 · $1.0 billion · data/features/fct_bank_features.parquet: log_total_assets
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 3.1%; contribution to the score · 2017-03-31 · +1.350 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 109.7%; contribution to the score · 2017-03-31 · +0.604 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: the total risk-based capital ratio, value 4.4%; contribution to the score · 2017-03-31 · +0.518 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F78 · Driver up #4: core deposits as a share of assets, value 97.0%; contribution to the score · 2017-03-31 · +0.318 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F79 · Driver up #5: commercial real estate loans as a share of loans, value 0.2%; contribution to the score · 2017-03-31 · +0.281 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.0%; contribution to the score · 2017-03-31 · -1.410 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 21.5%; contribution to the score · 2017-03-31 · -0.861 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: loans 30-89 days past due, as a share of assets, value 0.3%; contribution to the score · 2017-03-31 · -0.619 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F83 · Driver down #4: return on assets (profit as a share of assets), value 0.4%; contribution to the score · 2017-03-31 · -0.558 · data/analyst/scores.parquet: feature return_on_assets contribution
- F84 · Driver down #5: total assets, value $1.0 billion; contribution to the score · 2017-03-31 · -0.340 · data/analyst/scores.parquet: feature log_total_assets contribution
- F85 · Failure date · 2017-05-05 · 2017-05-05 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-06-30 · 2016-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-06-30: the Tier 1 risk-based capital ratio, value 3.3%; contribution to the score · 2016-06-30 · +1.814 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2016-06-30: the Texas ratio (troubled assets against capital plus reserves), value 125.6%; contribution to the score · 2016-06-30 · +1.083 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2016-06-30: the total risk-based capital ratio, value 4.5%; contribution to the score · 2016-06-30 · +0.426 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2017-03-31 · 109.7% · data/features/fct_bank_features.parquet: texas_ratio
- F100 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 125.6% · data/features/fct_bank_features.parquet: texas_ratio
- F101 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 175.8% · data/features/fct_bank_features.parquet: texas_ratio
- F102 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2017-03-31 · -16.3 pp · data/features/fct_bank_features.parquet: texas_ratio
- F103 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over four quarters, in percentage points · 2017-03-31 · -27.1 pp · data/features/fct_bank_features.parquet: texas_ratio
- F104 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2017-03-31 · +0.604 · data/analyst/scores.parquet: feature texas_ratio contribution
- F105 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2017-03-31 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F106 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2017-03-31 · 0.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F107 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F108 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 3.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F110 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2017-03-31 · -0.012 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F111 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2017-03-31 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F112 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2017-03-31 · 3.8% · data/features/fct_bank_features.parquet: net_interest_margin
- F113 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 2.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F114 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F116 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2017-03-31 · -0.125 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F117 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2017-03-31 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F118 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2017-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F119 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F120 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F123 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2017-03-31 · -0.619 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F124 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2017-03-31 · pushed the score down · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F125 · Trend: construction loans as a share of loans, value at the as-of quarter · 2017-03-31 · 0.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F126 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F127 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 2.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F130 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2017-03-31 · -0.224 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F131 · Trend: construction loans as a share of loans, what the model did with it · 2017-03-31 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F132 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2017-03-31 · 3.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F133 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 3.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F134 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 8.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F137 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2017-03-31 · +0.020 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F138 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2017-03-31 · little effect on the score · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F139 · Trend: ratios outside their own prior range · 2017-03-31 · 12 · data/features/fct_bank_features.parquet
- F140 · Trend: ratios shown in the table (the furthest outside their prior range) · 2017-03-31 · 6 · data/features/fct_bank_features.parquet
- F141 · Trend: ratios compared with their own prior range · 2017-03-31 · 30 · data/features/fct_bank_features.parquet
- F142 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F144 · Percentile a year earlier (100 = highest risk) · 2016-03-31 · 99.7% · data/analyst/scores.parquet: percentile
- F145 · Trend: how the model's rating compares with a year earlier · 2017-03-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F149 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2017-03-31 · 97.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F150 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2017-03-31 · 100.0th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F151 · Peers: core deposits as a share of assets, national reading · 2017-03-31 · unusually high · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F152 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2017-03-31 · 98.6th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F153 · Peers: core deposits as a share of assets, peer median · 2017-03-31 · 73.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F154 · Peers: core deposits as a share of assets, reading against its peers · 2017-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F155 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2017-03-31 · 4.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F156 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2017-03-31 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F157 · Peers: the total risk-based capital ratio, national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F158 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2017-03-31 · 1.4th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F159 · Peers: the total risk-based capital ratio, peer median · 2017-03-31 · 17.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F160 · Peers: the total risk-based capital ratio, reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F161 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2017-03-31 · 3.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F162 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2017-03-31 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F163 · Peers: the Tier 1 risk-based capital ratio, national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F164 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2017-03-31 · 1.4th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F165 · Peers: the Tier 1 risk-based capital ratio, peer median · 2017-03-31 · 16.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F166 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F167 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2017-03-31 · 2.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F168 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2017-03-31 · 0.4th · data/features/fct_bank_features.parquet: leverage_ratio
- F169 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F170 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2017-03-31 · 1.4th · data/features/fct_bank_features.parquet: leverage_ratio
- F171 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2017-03-31 · 9.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F172 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F173 · Peers: equity as a share of assets, bank value at the as-of quarter · 2017-03-31 · 2.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F174 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2017-03-31 · 0.4th · data/features/fct_bank_features.parquet: equity_to_assets
- F175 · Peers: equity as a share of assets, national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F176 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2017-03-31 · 1.4th · data/features/fct_bank_features.parquet: equity_to_assets
- F177 · Peers: equity as a share of assets, peer median · 2017-03-31 · 9.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F178 · Peers: equity as a share of assets, reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F179 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2017-03-31 · 109.7% · data/features/fct_bank_features.parquet: texas_ratio
- F180 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2017-03-31 · 99.5th · data/features/fct_bank_features.parquet: texas_ratio
- F181 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2017-03-31 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F182 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2017-03-31 · 98.6th · data/features/fct_bank_features.parquet: texas_ratio
- F183 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2017-03-31 · 2.7% · data/features/fct_bank_features.parquet: texas_ratio
- F184 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2017-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F185 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2017-03-31 · 1.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F186 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2017-03-31 · 0.7th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F187 · Peers: uninsured deposits as a share of deposits, national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F188 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2017-03-31 · 1.4th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F189 · Peers: uninsured deposits as a share of deposits, peer median · 2017-03-31 · 12.1% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F190 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F191 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2017-03-31 · 0.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F192 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2017-03-31 · 1.9th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F193 · Peers: annualized interest expense as a share of assets, national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F194 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2017-03-31 · 6.8th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F195 · Peers: annualized interest expense as a share of assets, peer median · 2017-03-31 · 0.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F196 · Peers: annualized interest expense as a share of assets, reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F198 · Peers: ratios in the national top or bottom 10% · 2017-03-31 · 18 · data/features/fct_bank_features.parquet
- F199 · Peers: those ratios also unusual among peers · 2017-03-31 · 13 · data/features/fct_bank_features.parquet
- F201 · Peers: cut-off for unusual (top or bottom share of banks) · 2017-03-31 · 10% · data/features/fct_bank_features.parquet
