---
cert: 28722
name: "Kentland Fs&La"
as_of: 2026-03-31
rank: 1
n_banks: 4353
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: true
failure_date: 2026-07-10
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:07:49"
writer_model: "claude-opus-5-5"
checked: true
---

# Kentland Fs&La (cert 28722)

*Hindsight: failed 2026-07-10. Canary flagged it 4 quarters ahead.*
*After the test window: not part of the reported 2016-2024 results.*

## Summary

Kentland Fs&La, a small bank in IN with total assets of $3.7 million, ranked 1 out of 4,353 banks nationally on Canary's risk score as of 2026-03-31, which puts it in the 100.0th percentile. That places it on Canary's watchlist, which covers the riskiest 2% of banks, or 88 banks that quarter. Its capital cushion is very thin, with equity (the owners' stake) at 1.8% of assets against a national median of 10.4%. It is also losing money, with a return on assets (profit as a share of assets) of -4.8% against a national median of 1.2%.

## Warning signs in the data

Capital, the money that absorbs losses before depositors are hurt, is far below normal levels. Equity was 1.8% of assets against a national median of 10.4%, and the leverage ratio (core capital as a share of average assets) was 1.7% against a median of 10.9%. The Tier 1 risk-based capital ratio (core capital measured against riskier assets) was 2.9% against a median of 14.5%, and the total risk-based capital ratio was 4.2% against a median of 15.7%.

Credit quality, meaning how well borrowers are repaying, is weak. Seriously overdue loans or loans no longer earning interest were 6.3% of loans against a national median of 0.5%. Loans in the early stages of being overdue were 2.5% of assets against a median of 0.3%. Nonaccrual assets and foreclosed property were 5.9% of assets against a median of 0.3%, and the Texas ratio (troubled assets against capital plus reserves) was 217.8% against a median of 2.9%. Loan-loss reserves, money set aside for expected bad loans, were 1.0% of loans, slightly below the median of 1.2%. Earnings are deeply negative, with return on equity at -201.1% against a median of 11.2% and the efficiency ratio (operating costs as a share of revenue) at 305.0% against a median of 63.1%.

Funding looks more stable than the rest of the picture: uninsured deposits were only 2.8% of deposits against a national median of 24.4%, and core deposits (steady, everyday deposits) were 88.7% of assets against a median of 75.8%. Cash was 5.5% of assets, somewhat below the median of 6.9%, and loans were 94.6% of deposits against a median of 79.1%. The bank showed no unrealized losses on its bonds, at 0.0% of equity for bonds available for sale against a median of 5.8%.

## Understanding the score

As of 2026-03-31, the bank ranked 1 out of 4,353 banks, the 100.0th percentile on a scale from 0 to 100 where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks by score, 88 banks that quarter.

Five factors pushed the score up the most. The largest were the Tier 1 risk-based capital ratio at 2.9%, contributing +1.457, and return on equity at -201.1%, contributing +1.409. Next came the Texas ratio at 217.8%, contributing +0.921, the leverage ratio at 1.7%, contributing +0.562, and the total risk-based capital ratio at 4.2%, contributing +0.460.

Five factors pulled the score down, all by small amounts. These were loan-loss reserves at 1.0% of loans, contributing -0.143, cash at 5.5% of assets, contributing -0.063, and brokered deposits (deposits placed through middlemen) at 0.0% of deposits, contributing -0.056. Net loan write-offs at 0.0% of loans contributed -0.049, and construction loans at 0.0% of loans contributed -0.032.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-06-30 | 1 | 4,610 | ▲ watchlist |
| 2024-09-30 | 8 | 4,589 | ▲ watchlist |
| 2024-12-31 | 8 | 4,560 | ▲ watchlist |
| 2025-03-31 | 1 | 4,536 | ▲ watchlist |
| 2025-06-30 | 6 | 4,494 | ▲ watchlist |
| 2025-09-30 | 1 | 4,452 | ▲ watchlist (first flag) |
| 2025-12-31 | 1 | 4,411 | ▲ watchlist |
| 2026-03-31 | 1 | 4,353 | ▲ watchlist |

## How its ratios moved

The bank ranked 1 out of 4,353 at 2026-03-31, and its percentile a year earlier was already 100.0%, so the model rated it about the same as a year earlier. Of 27 ratios compared with their own prior range, mostly the prior 12 quarters, 7 sat outside that range.

Return on equity was -201.1%, far below its prior range of -82.3% to -8.0%, and it pushed the score up with a contribution of +1.409. The Texas ratio was 217.8%, above its prior range of 0.0% to 154.9% after rising +62.9 pp in one quarter, and it pushed the score up by +0.921. The leverage ratio was 1.7%, below its prior range of 3.0% to 12.9%, and it pushed the score up by +0.562. Equity as a share of assets was 1.8%, below its prior range of 2.9% to 12.9%, and it pushed the score up by +0.251.

Cash as a share of assets was 5.5%, below its prior range of 6.0% to 12.9%, yet it pushed the score down, with a contribution of -0.063. Provision for loan losses was 0.4% of assets, above its prior range of 0.0% to 0.0%, but it had little effect on the score, with a contribution of -0.018.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -201.1% | -82.3% to -8.0% | same quarter, prior 3 years | n/a | -118.8 pp | +1.409 | pushed the score up |
| annualized provision for loan losses as a share of assets | 0.4% | 0.0% to 0.0% | same quarter, prior 3 years | n/a | +0.4 pp | -0.018 | little effect on the score |
| the Texas ratio (troubled assets against capital plus reserves) | 217.8% | 0.0% to 154.9% | prior 12 quarters | +62.9 pp | +135.6 pp | +0.921 | pushed the score up |
| the leverage ratio (core capital as a share of average assets) | 1.7% | 3.0% to 12.9% | prior 12 quarters | -1.4 pp | -5.8 pp | +0.562 | pushed the score up |
| equity as a share of assets | 1.8% | 2.9% to 12.9% | prior 12 quarters | -1.1 pp | -5.6 pp | +0.251 | pushed the score up |
| cash as a share of assets | 5.5% | 6.0% to 12.9% | prior 12 quarters | -6.8 pp | -7.2 pp | -0.063 | pushed the score down |

7 of 27 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-03-31: Mortgage Lending Specialization.

Peers: 75 banks in the same specialty group and size tier (under $100 million).

The Tier 1 risk-based capital ratio was 2.9%, in the 0.1st percentile nationally, which is unusually low, and in the 1.4th percentile among peers against a peer median of 22.5%, unusually low among its peers too. The total risk-based capital ratio was 4.2%, in the 0.1st percentile nationally, unusually low, and in the 1.4th percentile among peers against a peer median of 23.4%, unusually low among its peers too. The leverage ratio was 1.7%, in the 0.4th percentile nationally, unusually low, and in the 0.7th percentile among peers against a peer median of 14.2%, unusually low among its peers too. Equity as a share of assets was 1.8%, in the 0.6th percentile nationally, unusually low, and in the 0.7th percentile among peers against a peer median of 14.0%, unusually low among its peers too.

Return on equity was -201.1%, in the 0.0th percentile nationally, unusually low, and in the 0.7th percentile among peers against a peer median of 1.7%, unusually low among its peers too. The Texas ratio was 217.8%, in the 99.9th percentile nationally, unusually high, and in the 99.3rd percentile among peers against a peer median of 1.7%, unusually high among its peers too. Nonaccrual assets and foreclosed property were 5.9% of assets, in the 99.5th percentile nationally, unusually high, and in the 99.3rd percentile among peers against a peer median of 0.2%, unusually high among its peers too. The efficiency ratio was 305.0%, in the 99.7th percentile nationally, unusually high, and in the 99.3rd percentile among peers against a peer median of 87.6%, unusually high among its peers too.

Overall, 19 of the bank's ratios fell in the national top or bottom 10%, and 14 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -201.1% | 0.0th (unusually low) | 1.7% | 0.7th | unusually low among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 217.8% | 99.9th (unusually high) | 1.7% | 99.3rd | unusually high among its peers too |
| the total risk-based capital ratio | 4.2% | 0.1st (unusually low) | 23.4% | 1.4th | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 2.9% | 0.1st (unusually low) | 22.5% | 1.4th | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 305.0% | 99.7th (unusually high) | 87.6% | 99.3rd | unusually high among its peers too |
| the leverage ratio (core capital as a share of average assets) | 1.7% | 0.4th (unusually low) | 14.2% | 0.7th | unusually low among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 5.9% | 99.5th (unusually high) | 0.2% | 99.3rd | unusually high among its peers too |
| equity as a share of assets | 1.8% | 0.6th (unusually low) | 14.0% | 0.7th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 126.0% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | n/a | 50% or more | n/a |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, Canary first flagged this bank at 2025-09-30, and the bank failed on 2026-07-10, a lead time of 4 quarters. At that first flag, the main factors pushing the score up were return on equity at -154.3%, contributing +1.328, and the Texas ratio at 130.8%, contributing +0.806. Also pushing the score up then were the Tier 1 risk-based capital ratio at 7.5%, contributing +0.573, seriously overdue or non-interest-earning loans at 7.6% of loans, contributing +0.396, and interest expense at 3.6% of assets, contributing +0.358.

*After the test window: not part of the reported 2016-2024 results.*

## What happened next

In hindsight, the bank's last reported quarter was 2026-03-31, the same quarter this memo describes. The bank failed on 2026-07-10, so no later ranks are available.

## Sources

- F1 · Bank name · n/a · Kentland Fs&La · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IN · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-03-31 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-03-31 · 4,353 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-03-31 · 88 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-03-31 · 1.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-03-31 · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-03-31 · 1.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-03-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-03-31 · 2.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-03-31 · 14.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-03-31 · 4.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-03-31 · 15.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-03-31 · 6.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-03-31 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-03-31 · 5.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-03-31 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-03-31 · 2.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-03-31 · 1.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-03-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-03-31 · 217.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-03-31 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-03-31 · -4.8% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-03-31 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-03-31 · -201.1% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-03-31 · 11.2% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-03-31 · 305.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-03-31 · 63.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-03-31 · 94.6% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-03-31 · 79.1% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-03-31 · 2.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-03-31 · 24.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-03-31 · 88.7% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-03-31 · 75.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-03-31 · 5.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-03-31 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-03-31 · 5.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-03-31 · $3.7 million · data/features/fct_bank_features.parquet: log_total_assets
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 2.9%; contribution to the score · 2026-03-31 · +1.457 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -201.1%; contribution to the score · 2026-03-31 · +1.409 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 217.8%; contribution to the score · 2026-03-31 · +0.921 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value 1.7%; contribution to the score · 2026-03-31 · +0.562 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 4.2%; contribution to the score · 2026-03-31 · +0.460 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: loan-loss reserves as a share of loans, value 1.0%; contribution to the score · 2026-03-31 · -0.143 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F81 · Driver down #2: cash as a share of assets, value 5.5%; contribution to the score · 2026-03-31 · -0.063 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F82 · Driver down #3: brokered deposits as a share of deposits, value 0.0%; contribution to the score · 2026-03-31 · -0.056 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F83 · Driver down #4: annualized loan write-offs, net of recoveries, as a share of loans, value 0.0%; contribution to the score · 2026-03-31 · -0.049 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F84 · Driver down #5: construction loans as a share of loans, value 0.0%; contribution to the score · 2026-03-31 · -0.032 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F85 · Failure date · 2026-07-10 · 2026-07-10 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2025-09-30 · 2025-09-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2025-09-30: return on equity (profit as a share of equity), value -154.3%; contribution to the score · 2025-09-30 · +1.328 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2025-09-30: the Texas ratio (troubled assets against capital plus reserves), value 130.8%; contribution to the score · 2025-09-30 · +0.806 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2025-09-30: the Tier 1 risk-based capital ratio, value 7.5%; contribution to the score · 2025-09-30 · +0.573 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F91 · Driver up #4 at 2025-09-30: loans 90+ days past due or not accruing interest, as a share of loans, value 7.6%; contribution to the score · 2025-09-30 · +0.396 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2025-09-30: annualized interest expense as a share of assets, value 3.6%; contribution to the score · 2025-09-30 · +0.358 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F98 · Last quarter the bank reported · 2026-03-31 · 2026-03-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-03-31 · -201.1% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -82.3% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -8.0% · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-03-31 · +1.409 · data/analyst/scores.parquet: feature return_on_equity contribution
- F104 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F105 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-03-31 · 0.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F106 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F107 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F109 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-03-31 · -0.018 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F110 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-03-31 · little effect on the score · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F111 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-03-31 · 217.8% · data/features/fct_bank_features.parquet: texas_ratio
- F112 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: texas_ratio
- F113 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 154.9% · data/features/fct_bank_features.parquet: texas_ratio
- F114 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2026-03-31 · +62.9 pp · data/features/fct_bank_features.parquet: texas_ratio
- F116 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-03-31 · +0.921 · data/analyst/scores.parquet: feature texas_ratio contribution
- F117 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F118 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-03-31 · 1.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F119 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 3.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F120 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 12.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F123 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-03-31 · +0.562 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F124 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F125 · Trend: equity as a share of assets, value at the as-of quarter · 2026-03-31 · 1.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F126 · Trend: equity as a share of assets, lowest value in the comparison window · n/a · 2.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F127 · Trend: equity as a share of assets, highest value in the comparison window · n/a · 12.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F130 · Trend: equity as a share of assets, contribution to the score (model log-odds units) · 2026-03-31 · +0.251 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F131 · Trend: equity as a share of assets, what the model did with it · 2026-03-31 · pushed the score up · data/analyst/scores.parquet: feature equity_to_assets contribution
- F132 · Trend: cash as a share of assets, value at the as-of quarter · 2026-03-31 · 5.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F133 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 6.0% · data/features/fct_bank_features.parquet: cash_to_assets
- F134 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 12.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F137 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2026-03-31 · -0.063 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F138 · Trend: cash as a share of assets, what the model did with it · 2026-03-31 · pushed the score down · data/analyst/scores.parquet: feature cash_to_assets contribution
- F139 · Trend: ratios outside their own prior range · 2026-03-31 · 7 · data/features/fct_bank_features.parquet
- F141 · Trend: ratios compared with their own prior range · 2026-03-31 · 27 · data/features/fct_bank_features.parquet
- F142 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F144 · Percentile a year earlier (100 = highest risk) · 2025-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F145 · Trend: how the model's rating compares with a year earlier · 2026-03-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F149 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-03-31 · -201.1% · data/features/fct_bank_features.parquet: return_on_equity
- F150 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-03-31 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F151 · Peers: return on equity (profit as a share of equity), national reading · 2026-03-31 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F152 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-03-31 · 0.7th · data/features/fct_bank_features.parquet: return_on_equity
- F153 · Peers: return on equity (profit as a share of equity), peer median · 2026-03-31 · 1.7% · data/features/fct_bank_features.parquet: return_on_equity
- F154 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F155 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-03-31 · 217.8% · data/features/fct_bank_features.parquet: texas_ratio
- F156 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-03-31 · 99.9th · data/features/fct_bank_features.parquet: texas_ratio
- F157 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-03-31 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F158 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-03-31 · 99.3rd · data/features/fct_bank_features.parquet: texas_ratio
- F159 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-03-31 · 1.7% · data/features/fct_bank_features.parquet: texas_ratio
- F160 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F161 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2026-03-31 · 4.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F162 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-03-31 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F163 · Peers: the total risk-based capital ratio, national reading · 2026-03-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F164 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-03-31 · 1.4th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F165 · Peers: the total risk-based capital ratio, peer median · 2026-03-31 · 23.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F166 · Peers: the total risk-based capital ratio, reading against its peers · 2026-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F167 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-03-31 · 2.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F168 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-03-31 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F169 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-03-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F170 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-03-31 · 1.4th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F171 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-03-31 · 22.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F172 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F173 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-03-31 · 305.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F174 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-03-31 · 99.7th · data/features/fct_bank_features.parquet: efficiency_ratio
- F175 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-03-31 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F176 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-03-31 · 99.3rd · data/features/fct_bank_features.parquet: efficiency_ratio
- F177 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-03-31 · 87.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F178 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F179 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-03-31 · 1.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F180 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-03-31 · 0.4th · data/features/fct_bank_features.parquet: leverage_ratio
- F181 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-03-31 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F182 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-03-31 · 0.7th · data/features/fct_bank_features.parquet: leverage_ratio
- F183 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-03-31 · 14.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F184 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F185 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-03-31 · 5.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F186 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-03-31 · 99.5th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F187 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-03-31 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F188 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-03-31 · 99.3rd · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F189 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-03-31 · 0.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F190 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F191 · Peers: equity as a share of assets, bank value at the as-of quarter · 2026-03-31 · 1.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F192 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2026-03-31 · 0.6th · data/features/fct_bank_features.parquet: equity_to_assets
- F193 · Peers: equity as a share of assets, national reading · 2026-03-31 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F194 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2026-03-31 · 0.7th · data/features/fct_bank_features.parquet: equity_to_assets
- F195 · Peers: equity as a share of assets, peer median · 2026-03-31 · 14.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F196 · Peers: equity as a share of assets, reading against its peers · 2026-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F198 · Peers: ratios in the national top or bottom 10% · 2026-03-31 · 19 · data/features/fct_bank_features.parquet
- F199 · Peers: those ratios also unusual among peers · 2026-03-31 · 14 · data/features/fct_bank_features.parquet
- F201 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-03-31 · 10% · data/features/fct_bank_features.parquet
