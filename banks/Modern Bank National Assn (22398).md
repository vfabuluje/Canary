---
cert: 22398
name: "Modern Bank National Assn"
as_of: 2026-06-30
rank: 36
n_banks: 4313
percentile: 99.18849988407142
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:57:27"
writer_model: "claude-opus-5-5"
checked: true
---

# Modern Bank National Assn (cert 22398)

*Outcome not yet known.*

## Summary

Modern Bank National Assn, a NY bank, ranked 36 out of 4,313 banks on Canary's risk score as of 2026-06-30, which puts it in the 99.2nd percentile and on the watchlist. Its main weak spots were troubled loans and costly funding: loans 90+ days past due or not accruing interest were 5.6% of loans against a national median of 0.5%, and brokered deposits (money placed through middlemen) were 26.6% of deposits against a median of 0.0%. Profits were thin, with a return on assets (profit as a share of assets) of 0.1% against a national median of 1.2%, and its capital ratios sat somewhat below the medians. Pointing the other way, a separate check of commercial real estate lending found the bank did not cross either supervisory line.

## Warning signs in the data

Credit quality was the clearest problem: loans 90+ days past due or not accruing interest were 5.6% of loans, far above the national median of 0.5%. Nonaccrual assets and foreclosed property (loans no longer earning interest plus property taken back from borrowers) were 4.2% of assets against a median of 0.3%, and the Texas ratio (troubled assets against capital plus reserves) was 36.6% against a median of 3.0% among peers and 2.9% nationally. The bank was releasing rather than adding to reserves, with an annualized provision for loan losses of -0.2% of assets against a median of 0.1%, though its loan-loss reserves of 1.5% of loans were above the median of 1.2%. Not every credit signal was bad: loans 30-89 days past due, an early sign of trouble, were 0.0% of assets against a median of 0.2%.

Funding leaned on costly, less stable sources: brokered deposits were 26.6% of deposits against a median of 0.0%, and Federal Home Loan Bank borrowings (loans from a government-sponsored lender) were 14.8% of assets against a median of 0.2%. Core deposits (steady everyday customer deposits) were 53.9% of assets, well below the median of 75.5%, and interest expense was 3.0% of assets against a median of 1.6%. Deposits shrank by -10.0% over the past four quarters while the median bank grew 4.2%, and loans were 99.8% of deposits against a median of 80.2%. On the steadier side, cash was 9.4% of assets against a median of 6.2%, and uninsured deposits were 19.6% of deposits, below the median of 24.8%.

Capital (the owners' cushion against losses) was somewhat below typical levels: the leverage ratio was 9.6% against a median of 11.0%, and the Tier 1 risk-based capital ratio was 13.0% against 14.6%. Unrealized losses on bonds available for sale were 6.0% of equity, slightly above the median of 5.6%, and losses on bonds held to maturity were 3.8% of equity against a median of 0.0%. Earnings were weak, with an efficiency ratio (operating costs as a share of revenue) of 101.6% against a median of 62.1% and a net interest margin (the spread earned on lending) of 2.6% against 3.9%.

## Understanding the score

As of 2026-06-30, Modern Bank National Assn ranked 36 out of 4,313 banks, placing it in the 99.2nd percentile on a 0 to 100 scale where higher means riskier. Its model score was 0.2140, and it was flagged on the watchlist, which covers roughly the top 2% of banks and held 87 banks that quarter.

The five factors that pushed the score up most were brokered deposits at 26.6% of deposits (+0.839), interest expense at 3.0% of assets (+0.534), and loans 90+ days past due or not accruing at 5.6% of loans (+0.401). Next came losses on bonds available for sale at 6.0% of equity (+0.264) and core deposits at 53.9% of assets (+0.224).

The five factors that pulled the score down most were the Tier 1 risk-based capital ratio at 13.0% (-1.238), return on equity at 1.3% (-0.367), and the total risk-based capital ratio at 14.2% (-0.324). The bank's size, with total assets of $648.5 million (-0.251), and its return on assets of 0.1% (-0.216) also lowered the score.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 11 | 4,589 | ▲ watchlist |
| 2024-12-31 | 20 | 4,560 | ▲ watchlist |
| 2025-03-31 | 56 | 4,536 | ▲ watchlist |
| 2025-06-30 | 27 | 4,494 | ▲ watchlist |
| 2025-09-30 | 37 | 4,452 | ▲ watchlist |
| 2025-12-31 | 22 | 4,411 | ▲ watchlist |
| 2026-03-31 | 24 | 4,353 | ▲ watchlist |
| 2026-06-30 | 36 | 4,313 | ▲ watchlist |

## How its ratios moved

Canary compared 30 of this bank's financial ratios with each ratio's own history, usually the prior 12 quarters, and found 2 outside that prior range. For year-to-date ratios, the comparison is the same quarter in the prior 3 years. Overall, the model rated the bank about the same as a year earlier: it ranked 36 out of 4,313 banks, in the 99.2nd percentile, compared with the 99.4th percentile a year earlier.

The annualized provision for loan losses as a share of assets (money set aside to cover expected bad loans, scaled to the bank's size) was -0.2% at 2026-06-30, below its prior range of 0.0% to 1.6%. It changed by -1.8 pp over four quarters. Even though this ratio sat outside its prior range, at -0.2% it pushed the score down, with a contribution of -0.121 model log-odds units.

Uninsured deposits as a share of deposits (money held above the government deposit insurance limit) were 19.6%, just above their prior range of 12.4% to 19.3%. The share changed by +0.2 pp over one quarter and +0.6 pp over four quarters. Despite being outside its prior range, at 19.6% this ratio had little effect on the score, with a contribution of -0.038 model log-odds units.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | -0.2% | 0.0% to 1.6% | same quarter, prior 3 years | n/a | -1.8 pp | -0.121 | pushed the score down |
| uninsured deposits as a share of deposits | 19.6% | 12.4% to 19.3% | prior 12 quarters | +0.2 pp | +0.6 pp | -0.038 | little effect on the score |

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

The bank's nonaccrual assets and foreclosed property (loans no longer earning interest plus property taken back from borrowers) were 4.2% of assets, at the 98.8th percentile nationally, which is unusually high. On that measure it sat at the 98.2nd percentile of its peers against a peer median of 0.3%, unusually high among its peers too. Loans 90+ days past due or not accruing interest were 5.6% of loans, at the 98.1st percentile nationally (unusually high), and at the 97.8th percentile of its peers against a peer median of 0.4%, unusually high among its peers too. The Texas ratio (troubled assets against capital plus reserves) was 36.6%, at the 98.6th percentile nationally (unusually high), and at the 98.2nd percentile of its peers against a peer median of 3.0%, unusually high among its peers too. The annualized provision for loan losses (money set aside for expected loan losses) was -0.2% of assets, at the 0.6th percentile nationally (unusually low), and at the 0.8th percentile of its peers against a peer median of 0.1%, unusually low among its peers too.

Annualized interest expense (what the bank pays on its deposits and borrowings) was 3.0% of assets, at the 98.3rd percentile nationally (unusually high), and at the 98.2nd percentile of its peers against a peer median of 1.7%, unusually high among its peers too. Federal Home Loan Bank borrowings (loans to banks from a government-sponsored lender) were 14.8% of assets, at the 97.7th percentile nationally (unusually high), and at the 98.3rd percentile of its peers against a peer median of 0.3%, unusually high among its peers too. Asset growth over the past four quarters was -8.8%, at the 2.1st percentile nationally (unusually low), and at the 2.0th percentile of its peers against a peer median of 4.8%, unusually low among its peers too. Deposit growth over the past four quarters was -10.0%, at the 2.2nd percentile nationally (unusually low), and at the 2.5th percentile of its peers against a peer median of 4.3%, unusually low among its peers too.

Overall, 17 of the bank's ratios fell in the national top or bottom 10%, and all 17 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | -0.2% | 0.6th (unusually low) | 0.1% | 0.8th | unusually low among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 4.2% | 98.8th (unusually high) | 0.3% | 98.2nd | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 36.6% | 98.6th (unusually high) | 3.0% | 98.2nd | unusually high among its peers too |
| annualized interest expense as a share of assets | 3.0% | 98.3rd (unusually high) | 1.7% | 98.2nd | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 5.6% | 98.1st (unusually high) | 0.4% | 97.8th | unusually high among its peers too |
| asset growth over the past four quarters | -8.8% | 2.1st (unusually low) | 4.8% | 2.0th | unusually low among its peers too |
| deposit growth over the past four quarters | -10.0% | 2.2nd (unusually low) | 4.3% | 2.5th | unusually low among its peers too |
| Federal Home Loan Bank borrowings as a share of assets | 14.8% | 97.7th (unusually high) | 0.3% | 98.3rd | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 252.2% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -33.6% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight, this is an open watchlist case: the bank was flagged, and the fact sheet holds no later data showing how its situation turned out. Without hindsight facts, we cannot say whether the warning signs eased or worsened after the as-of quarter.

## What happened next

Looking back with hindsight, the fact sheet contains no ranks, watchlist flags or filings after the as-of quarter. So we cannot report how its rank moved or whether it still reports, and if it had stopped reporting our data would not distinguish a merger from a closure.

## Sources

- F1 · Bank name · n/a · Modern Bank National Assn · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NY · data/raw/financials: STALP
- F5 · Model score · 2026-06-30 · 0.2140 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 36 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.2% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 9.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 13.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · -0.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 36.6% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 101.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 99.8% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 19.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 26.6% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 53.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 14.8% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 9.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 3.8% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 6.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -10.0% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 26.6%; contribution to the score · 2026-06-30 · +0.839 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: annualized interest expense as a share of assets, value 3.0%; contribution to the score · 2026-06-30 · +0.534 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F77 · Driver up #3: loans 90+ days past due or not accruing interest, as a share of loans, value 5.6%; contribution to the score · 2026-06-30 · +0.401 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F78 · Driver up #4: losses on bonds available for sale, as a share of equity, value 6.0%; contribution to the score · 2026-06-30 · +0.264 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F79 · Driver up #5: core deposits as a share of assets, value 53.9%; contribution to the score · 2026-06-30 · +0.224 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 13.0%; contribution to the score · 2026-06-30 · -1.238 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 1.3%; contribution to the score · 2026-06-30 · -0.367 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: the total risk-based capital ratio, value 14.2%; contribution to the score · 2026-06-30 · -0.324 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F83 · Driver down #4: total assets, value $648.5 million; contribution to the score · 2026-06-30 · -0.251 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: return on assets (profit as a share of assets), value 0.1%; contribution to the score · 2026-06-30 · -0.216 · data/analyst/scores.parquet: feature return_on_assets contribution
- F85 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · -0.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F86 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F87 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 1.6% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F88 · Trend: annualized provision for loan losses as a share of assets, change over four quarters, in percentage points · 2026-06-30 · -1.8 pp · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F89 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.121 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F90 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F91 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 19.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F92 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 12.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F93 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 19.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F94 · Trend: uninsured deposits as a share of deposits, change over one quarter, in percentage points · 2026-06-30 · +0.2 pp · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F95 · Trend: uninsured deposits as a share of deposits, change over four quarters, in percentage points · 2026-06-30 · +0.6 pp · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F96 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.038 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F97 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F98 · Trend: ratios outside their own prior range · 2026-06-30 · 2 · data/features/fct_bank_features.parquet
- F100 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F101 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F102 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F103 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 99.4% · data/analyst/scores.parquet: percentile
- F104 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F108 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · -0.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F109 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.6th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F110 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F111 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 0.8th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F112 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F113 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F114 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F115 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.8th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F116 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F117 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.2nd · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F118 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F119 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F120 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 36.6% · data/features/fct_bank_features.parquet: texas_ratio
- F121 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: texas_ratio
- F122 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F123 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 98.2nd · data/features/fct_bank_features.parquet: texas_ratio
- F124 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: texas_ratio
- F125 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F126 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F127 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.3rd · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F128 · Peers: annualized interest expense as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F129 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.2nd · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F130 · Peers: annualized interest expense as a share of assets, peer median · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F131 · Peers: annualized interest expense as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F132 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F133 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.1st · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F134 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F135 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 97.8th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F136 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F137 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F138 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -8.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F139 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 2.1st · data/features/fct_bank_features.parquet: asset_growth_4q
- F140 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F141 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 2.0th · data/features/fct_bank_features.parquet: asset_growth_4q
- F142 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F143 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F144 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -10.0% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F145 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 2.2nd · data/features/fct_bank_features.parquet: deposit_growth_4q
- F146 · Peers: deposit growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: deposit_growth_4q
- F147 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 2.5th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F148 · Peers: deposit growth over the past four quarters, peer median · 2026-06-30 · 4.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F149 · Peers: deposit growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F150 · Peers: Federal Home Loan Bank borrowings as a share of assets, bank value at the as-of quarter · 2026-06-30 · 14.8% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F151 · Peers: Federal Home Loan Bank borrowings as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.7th · data/features/fct_bank_features.parquet: fhlb_to_assets
- F152 · Peers: Federal Home Loan Bank borrowings as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: fhlb_to_assets
- F153 · Peers: Federal Home Loan Bank borrowings as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.3rd · data/features/fct_bank_features.parquet: fhlb_to_assets
- F154 · Peers: Federal Home Loan Bank borrowings as a share of assets, peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F155 · Peers: Federal Home Loan Bank borrowings as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: fhlb_to_assets
- F157 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 17 · data/features/fct_bank_features.parquet
- F158 · Peers: those ratios also unusual among peers · 2026-06-30 · 17 · data/features/fct_bank_features.parquet
- F160 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
