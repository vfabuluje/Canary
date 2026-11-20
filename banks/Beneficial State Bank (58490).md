---
cert: 58490
name: "Beneficial State Bank"
as_of: 2026-06-30
rank: 28
n_banks: 4313
percentile: 99.3739856248551
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:57:27"
writer_model: "claude-opus-5-5"
checked: true
---

# Beneficial State Bank (cert 58490)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Beneficial State Bank ranked 28 out of 4,313 FDIC-insured banks on Canary's risk score, placing it in the 99.4th percentile, where higher means riskier. That puts it on Canary's watchlist, which holds 2% of banks, or 87 banks that quarter. The largest pushes up on the score came from big paper losses on bonds it holds and from heavy use of brokered deposits (money gathered through outside middlemen), while its Tier 1 risk-based capital ratio (core capital measured against riskier assets) pulled the score down the most. Its loan problems and thin profits also stand out against other banks, though a separate commercial real estate concentration check did not flag it.

## Warning signs in the data

On capital, the cushion that absorbs losses, the picture is mixed: equity was 9.3% of assets against a national median of 10.6%, but the leverage ratio (core capital as a share of average assets) was 11.2%, slightly above the median of 11.0%. Profits were thin, with return on assets of 0.1% against a national median of 1.2%, and an efficiency ratio (operating costs as a share of revenue) of 76.1% against 62.1%.

Credit quality is the clearest weak spot: loans 90 or more days past due or no longer accruing interest were 2.5% of loans against a national median of 0.5%, and nonaccrual assets plus foreclosed property were 1.9% of assets against 0.3%. Loans 30-89 days past due were 1.5% of assets against 0.2%, and the Texas ratio (troubled assets against capital plus reserves) was 18.2% against 2.9%. The bank did hold more loan-loss reserves than typical, at 1.8% of loans against a median of 1.2%. By contrast, the code-written real estate concentration check found it did not cross either supervisory line, so heavy commercial property lending is not where these figures point.

On funding, brokered deposits were 20.1% of deposits against a national median of 0.0%, core deposits (stable everyday customer deposits) were 65.1% of assets against 75.5%, and Federal Home Loan Bank borrowings were 5.5% of assets against 0.2%. Uninsured deposits were 28.6% of deposits against 24.8%, and loans equaled 89.3% of deposits against 80.2%, while volatile funding was lower than typical at 2.6% of assets against 9.0%, and cash was 6.7% of assets against 6.2%. Unrealized losses on bonds available for sale (bonds the bank can sell, marked to market value) equaled 34.2% of equity, far above the national median of 5.6%, while losses on bonds held to maturity were 0.0%, matching the median of 0.0%.

## Understanding the score

As of 2026-06-30, the bank ranked 28 out of 4,313 banks, in the 99.4th percentile on a scale of 0 to 100 where higher means riskier. It was flagged for the watchlist, which covers 2% of banks, 87 that quarter.

The five factors pushing the score up most were losses on bonds available for sale at 34.2% of equity, brokered deposits at 20.1% of deposits, equity at 9.3% of assets, the yearly provision for loan losses (money set aside for expected bad loans) at 0.8% of assets, and net loan write-offs at 0.7% of loans. The bond losses and brokered deposits did most of this work, with contributions of +1.397 and +0.875, while the other three added little.

The five factors pulling the score down most were the Tier 1 risk-based capital ratio, with a contribution of -1.017, the Texas ratio at 18.2%, interest expense at 1.4% of assets, volatile funding at 2.6% of assets, and construction loans at 3.1% of loans. Notably, the model treated the Texas ratio of 18.2% as lowering the score even though that figure is well above the national median of 2.9%, so the model's reading and the plain comparison point different ways.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 156 | 4,589 |  |
| 2024-12-31 | 87 | 4,560 | ▲ watchlist |
| 2025-03-31 | 60 | 4,536 | ▲ watchlist |
| 2025-06-30 | 81 | 4,494 | ▲ watchlist |
| 2025-09-30 | 44 | 4,452 | ▲ watchlist |
| 2025-12-31 | 58 | 4,411 | ▲ watchlist |
| 2026-03-31 | 37 | 4,353 | ▲ watchlist |
| 2026-06-30 | 28 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, Beneficial State Bank ranked 28 out of 4,313 banks nationally, placing it in the 99.4th percentile, where higher means riskier. A year earlier, on 2025-06-30, it sat in the 98.2nd percentile, and the model rated it riskier than a year earlier. Each ratio is compared with the bank's own prior range, which for most ratios is the prior 12 quarters and for year-to-date ratios is the same quarter in the prior 3 years. Of 28 ratios checked this way, 11 were outside their own prior range, and the 6 furthest outside are discussed here.

Loans 30-89 days past due (borrowers behind on payments, as a share of assets) stood at 1.5%, above its prior range of 0.7% to 1.3%, yet its contribution of -0.024 model log-odds units had little effect on the score. Core deposits (stable, everyday customer deposits, as a share of assets) were 65.1%, below their prior range of 66.8% to 85.4%, but at -0.028 model log-odds units this had little effect on the score. Securities (bonds and similar investments, as a share of assets) were 14.7%, below their prior range of 15.4% to 24.1%, and their contribution of -0.053 model log-odds units pushed the score down.

Annualized loan write-offs net of recoveries (loans the bank gave up on, as a share of loans) were 0.7%, below the prior range of 0.8% to 1.1%, with a contribution of +0.005 model log-odds units that had little effect on the score. Net interest margin, the spread earned on lending and investing, was 4.0%, just above its prior range of 3.9% to 3.9%, and its contribution of -0.011 model log-odds units had little effect on the score. Return on equity, profit as a share of equity, was 1.5%, below its prior range of 1.7% to 4.3%, yet its contribution of -0.119 model log-odds units pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| loans 30-89 days past due, as a share of assets | 1.5% | 0.7% to 1.3% | prior 12 quarters | +0.6 pp | +0.5 pp | -0.024 | little effect on the score |
| core deposits as a share of assets | 65.1% | 66.8% to 85.4% | prior 12 quarters | -1.7 pp | -5.4 pp | -0.028 | little effect on the score |
| securities as a share of assets | 14.7% | 15.4% to 24.1% | prior 12 quarters | -0.7 pp | -3.9 pp | -0.053 | pushed the score down |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.7% | 0.8% to 1.1% | same quarter, prior 3 years | n/a | -0.4 pp | +0.005 | little effect on the score |
| net interest margin (the spread earned on lending and investing) | 4.0% | 3.9% to 3.9% | same quarter, prior 3 years | n/a | +0.1 pp | -0.011 | little effect on the score |
| return on equity (profit as a share of equity) | 1.5% | 1.7% to 4.3% | same quarter, prior 3 years | n/a | -0.2 pp | -0.119 | pushed the score down |

11 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 753 banks in the same specialty group and size tier ($1 billion to $10 billion).

The bank's annualized provision for loan losses (money set aside to cover expected bad loans) was 0.8% of assets, at the 97.7th percentile nationally, which is unusually high, and at the 97.1st percentile among its peers against a peer median of 0.1%, unusually high among its peers too. Its annualized loan write-offs, net of recoveries (loans written off as uncollectible, minus amounts later recovered), were 0.7% of loans, at the 95.9th percentile nationally, which is unusually high, and at the 95.3rd percentile among its peers against a peer median of 0.0%, unusually high among its peers too. Brokered deposits (deposits gathered through outside middlemen rather than directly from customers) made up 20.1% of deposits, at the 95.2nd percentile nationally, which is unusually high, and at the 93.8th percentile among its peers against a peer median of 1.7%, unusually high among its peers too.

Return on assets (profit as a share of assets) was 0.1%, at the 5.9th percentile nationally, which is unusually low, and at the 3.3rd percentile among its peers against a peer median of 1.2%, unusually low among its peers too. Return on equity (profit as a share of the owners' stake) was 1.5%, at the 6.3rd percentile nationally, which is unusually low, and at the 3.1st percentile among its peers against a peer median of 11.8%, unusually low among its peers too. Nonaccrual assets and foreclosed property (loans no longer earning interest plus property taken back from borrowers) were 1.9% of assets, at the 93.8th percentile nationally, which is unusually high, and at the 94.6th percentile among its peers against a peer median of 0.4%, unusually high among its peers too. Loans 30-89 days past due were 1.5% of assets, at the 93.6th percentile nationally, which is unusually high, and at the 98.2nd percentile among its peers against a peer median of 0.2%, unusually high among its peers too. The Texas ratio (troubled assets compared with capital plus loss reserves) was 18.2%, at the 93.4th percentile nationally, which is unusually high, and at the 94.7th percentile among its peers against a peer median of 3.7%, unusually high among its peers too.

Overall, 11 of the bank's ratios fall in the national top or bottom 10%, and 11 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | 0.8% | 97.7th (unusually high) | 0.1% | 97.1st | unusually high among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.7% | 95.9th (unusually high) | 0.0% | 95.3rd | unusually high among its peers too |
| brokered deposits as a share of deposits | 20.1% | 95.2nd (unusually high) | 1.7% | 93.8th | unusually high among its peers too |
| return on assets (profit as a share of assets) | 0.1% | 5.9th (unusually low) | 1.2% | 3.3rd | unusually low among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 1.9% | 93.8th (unusually high) | 0.4% | 94.6th | unusually high among its peers too |
| return on equity (profit as a share of equity) | 1.5% | 6.3rd (unusually low) | 11.8% | 3.1st | unusually low among its peers too |
| loans 30-89 days past due, as a share of assets | 1.5% | 93.6th (unusually high) | 0.2% | 98.2nd | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 18.2% | 93.4th (unusually high) | 3.7% | 94.7th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 18.5% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 255.4% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 37.1% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight: this bank is an open watchlist case, meaning it was still operating and flagged by the model, and the fact sheet contains no data from after the as-of quarter. Because there are no hindsight figures, this section cannot confirm or rule out any later outcome; the reasons for the flag are the as-of drivers described above, chiefly bond losses and brokered deposits.

## What happened next

In hindsight: the fact sheet holds no later ranks, flags or reporting status for this bank, so we cannot say how its position changed or whether it kept reporting. The score history table added by code shows whatever later quarters are available.

## Sources

- F1 · Bank name · n/a · Beneficial State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2026-06-30 · 28 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.4% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 9.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 18.2% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 76.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F42 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F45 · Bank: loans as a share of deposits · 2026-06-30 · 89.3% · data/features/fct_bank_features.parquet: loans_to_deposits
- F46 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 28.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 20.1% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F51 · Bank: core deposits as a share of assets · 2026-06-30 · 65.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F52 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 5.5% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F55 · Bank: volatile funding as a share of assets · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F56 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F59 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F60 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 34.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Driver up #1: losses on bonds available for sale, as a share of equity, value 34.2%; contribution to the score · 2026-06-30 · +1.397 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F72 · Driver up #2: brokered deposits as a share of deposits, value 20.1%; contribution to the score · 2026-06-30 · +0.875 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F73 · Driver up #3: equity as a share of assets, value 9.3%; contribution to the score · 2026-06-30 · +0.097 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F74 · Driver up #4: annualized provision for loan losses as a share of assets, value 0.8%; contribution to the score · 2026-06-30 · +0.082 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F75 · Driver up #5: annualized loan write-offs, net of recoveries, as a share of loans, value 0.7%; contribution to the score · 2026-06-30 · +0.005 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -1.017 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 18.2%; contribution to the score · 2026-06-30 · -0.598 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver down #3: annualized interest expense as a share of assets, value 1.4%; contribution to the score · 2026-06-30 · -0.355 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F79 · Driver down #4: volatile funding as a share of assets, value 2.6%; contribution to the score · 2026-06-30 · -0.235 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F80 · Driver down #5: construction loans as a share of loans, value 3.1%; contribution to the score · 2026-06-30 · -0.188 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F85 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F86 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F87 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 1.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F90 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.024 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F91 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F92 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 65.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F93 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 66.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F94 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 85.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F97 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.028 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F98 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F99 · Trend: securities as a share of assets, value at the as-of quarter · 2026-06-30 · 14.7% · data/features/fct_bank_features.parquet: securities_to_assets
- F100 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 15.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F101 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 24.1% · data/features/fct_bank_features.parquet: securities_to_assets
- F104 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.053 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F105 · Trend: securities as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature securities_to_assets contribution
- F106 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F107 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F108 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F110 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.005 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F111 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F112 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F113 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F114 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F116 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.011 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F117 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F118 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: return_on_equity
- F119 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 1.7% · data/features/fct_bank_features.parquet: return_on_equity
- F120 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 4.3% · data/features/fct_bank_features.parquet: return_on_equity
- F122 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.119 · data/analyst/scores.parquet: feature return_on_equity contribution
- F123 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F124 · Trend: ratios outside their own prior range · 2026-06-30 · 11 · data/features/fct_bank_features.parquet
- F125 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F126 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F127 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F128 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F129 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 98.2% · data/analyst/scores.parquet: percentile
- F130 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F134 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F135 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.7th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F136 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F137 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 97.1st · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F138 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F139 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F140 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F141 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 95.9th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F142 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F143 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 95.3rd · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F144 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F145 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F146 · Peers: brokered deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 20.1% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F147 · Peers: brokered deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 95.2nd · data/features/fct_bank_features.parquet: brokered_to_deposits
- F148 · Peers: brokered deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: brokered_to_deposits
- F149 · Peers: brokered deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 93.8th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F150 · Peers: brokered deposits as a share of deposits, peer median · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F151 · Peers: brokered deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: brokered_to_deposits
- F152 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F153 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 5.9th · data/features/fct_bank_features.parquet: return_on_assets
- F154 · Peers: return on assets (profit as a share of assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F155 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2026-06-30 · 3.3rd · data/features/fct_bank_features.parquet: return_on_assets
- F156 · Peers: return on assets (profit as a share of assets), peer median · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F157 · Peers: return on assets (profit as a share of assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F158 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F159 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 93.8th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F160 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F161 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 94.6th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F162 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F163 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F164 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: return_on_equity
- F165 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 6.3rd · data/features/fct_bank_features.parquet: return_on_equity
- F166 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F167 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 3.1st · data/features/fct_bank_features.parquet: return_on_equity
- F168 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 11.8% · data/features/fct_bank_features.parquet: return_on_equity
- F169 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F170 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F171 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 93.6th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F172 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F173 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.2nd · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F174 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F175 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F176 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 18.2% · data/features/fct_bank_features.parquet: texas_ratio
- F177 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 93.4th · data/features/fct_bank_features.parquet: texas_ratio
- F178 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F179 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 94.7th · data/features/fct_bank_features.parquet: texas_ratio
- F180 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.7% · data/features/fct_bank_features.parquet: texas_ratio
- F181 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F183 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 11 · data/features/fct_bank_features.parquet
- F184 · Peers: those ratios also unusual among peers · 2026-06-30 · 11 · data/features/fct_bank_features.parquet
- F186 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
