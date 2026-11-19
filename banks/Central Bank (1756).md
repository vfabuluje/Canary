---
cert: 1756
name: "Central Bank"
as_of: 2026-06-30
rank: 10
n_banks: 4313
percentile: 99.79132854161836
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:08:19"
writer_model: "claude-opus-5-5"
checked: true
---

# Central Bank (cert 1756)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Central Bank, based in AR, ranked number 10 out of 4,313 FDIC-insured banks on Canary's risk score, which puts it in the 99.8th percentile on a scale where higher means riskier. That places it on Canary's watchlist, which covers the riskiest 2% of banks, or 87 banks that quarter. The biggest concerns are heavy use of brokered deposits (money gathered through outside middlemen), at 39.9% of deposits, and a Texas ratio (troubled assets measured against capital plus reserves) of 43.2%. The bank was still profitable, with a return on equity (profit as a share of equity) of 11.8%, close to the national median of 11.6%.

## Warning signs in the data

Capital, the cushion that absorbs losses, was thinner than at a typical bank: equity was 9.2% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 9.4% against 11.0%. Its Tier 1 risk-based capital ratio (core capital measured against risk-weighted assets) was 10.3% versus a median of 14.6%, and its total risk-based capital ratio was 11.6% versus 15.8%.

Credit quality stood out most: loans 90+ days past due or not accruing interest were 4.8% of loans, far above the national median of 0.5%. Nonaccrual assets and foreclosed property were 4.5% of assets against a median of 0.3%, and loans 30-89 days past due were 1.9% of assets against 0.2%. The Texas ratio was 43.2%, well above the national median of 2.9%, and commercial real estate loans made up 31.4% of loans versus a median of 23.6%.

On funding, brokered deposits were 39.9% of deposits while the national median was 0.0%, and core deposits (stable, everyday customer deposits) were only 40.0% of assets against a median of 75.5%. Borrowings from the Federal Home Loan Bank (a government-sponsored lender to banks) were 12.3% of assets versus a median of 0.2%, loans were 108.9% of deposits versus 80.2%, and cash was 3.4% of assets versus 6.2%. Unrealized losses on bonds available for sale were modest at 2.6% of equity, below the national median of 5.6%.

## Understanding the score

On 2026-06-30 Central Bank ranked number 10 of 4,313 banks, in the 99.8th percentile, and was flagged on the watchlist, which holds the top 2% of banks by score.

The five factors that pushed its score up most were brokered deposits at 39.9% of deposits (+0.785), the Texas ratio at 43.2% (+0.743), interest expense at 3.3% of assets (+0.581), loans 90+ days past due or not accruing at 4.8% of loans (+0.324), and the efficiency ratio (operating costs as a share of revenue) at 34.5% (+0.324).

The five factors that pulled its score down most were the Tier 1 risk-based capital ratio at 10.3% (-0.658), return on equity at 11.8% (-0.624), construction loans at 7.9% of loans (-0.414), loan-loss reserves (money set aside for expected bad loans) at 1.4% of loans (-0.292), and return on assets (profit as a share of assets) at 1.1% (-0.281).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 158 | 4,589 |  |
| 2024-12-31 | 292 | 4,560 |  |
| 2025-03-31 | 163 | 4,536 |  |
| 2025-06-30 | 209 | 4,494 |  |
| 2025-09-30 | 87 | 4,452 | ▲ watchlist |
| 2025-12-31 | 55 | 4,411 | ▲ watchlist |
| 2026-03-31 | 18 | 4,353 | ▲ watchlist |
| 2026-06-30 | 10 | 4,313 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own prior range, usually over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 30 ratios compared this way, 15 were outside their prior range, and 6 are shown in the table. The bank was in the 95.4th percentile a year earlier and ranked number 10 in the 99.8th percentile on 2026-06-30, so the model rated it riskier than a year earlier.

Loans 30-89 days past due were 1.9% of assets, above their prior range of 0.1% to 1.2%, after changes of +0.9 pp over one quarter and +1.7 pp over four quarters. At 1.9%, this ratio pushed the score up, contributing +0.141 model log-odds units. The provision for loan losses (money charged against profit for expected bad loans) was 0.7% of assets, above its prior range of 0.3% to 0.4%, and it pushed the score up by +0.077 model log-odds units. Net loan write-offs were 0.7% of loans, above a prior range of 0.0% to 0.0% after a change of +0.6 pp over four quarters, yet this ratio had little effect on the score, at +0.012 model log-odds units.

Return on equity fell to 11.8%, below its prior range of 18.2% to 21.3%, a change of -6.4 pp over four quarters. Even though it was below its own range, return on equity at 11.8% pushed the score down, contributing -0.624 model log-odds units. Return on assets was 1.1%, below its prior range of 1.6% to 1.8% after a change of -0.7 pp over four quarters, but it still pushed the score down, by -0.281 model log-odds units. The net interest margin (the spread earned on lending and investing) was 3.2%, below its prior range of 3.7% to 3.9%, yet it also pushed the score down, by -0.075 model log-odds units.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 11.8% | 18.2% to 21.3% | same quarter, prior 3 years | n/a | -6.4 pp | -0.624 | pushed the score down |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.7% | 0.0% to 0.0% | same quarter, prior 3 years | n/a | +0.6 pp | +0.012 | little effect on the score |
| loans 30-89 days past due, as a share of assets | 1.9% | 0.1% to 1.2% | prior 12 quarters | +0.9 pp | +1.7 pp | +0.141 | pushed the score up |
| return on assets (profit as a share of assets) | 1.1% | 1.6% to 1.8% | same quarter, prior 3 years | n/a | -0.7 pp | -0.281 | pushed the score down |
| net interest margin (the spread earned on lending and investing) | 3.2% | 3.7% to 3.9% | same quarter, prior 3 years | n/a | -0.5 pp | -0.075 | pushed the score down |
| annualized provision for loan losses as a share of assets | 0.7% | 0.3% to 0.4% | same quarter, prior 3 years | n/a | +0.4 pp | +0.077 | pushed the score up |

15 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

Interest expense was 3.3% of assets, at the 99.5th percentile nationally, which is unusually high. Among its peers it sat at the 99.5th percentile against a peer median of 1.7%, unusually high among its peers too. Brokered deposits were 39.9% of deposits, at the 99.1st percentile nationally (unusually high) and the 99.3rd percentile among peers, whose median was 0.0%, unusually high among its peers too. The Texas ratio was 43.2%, at the 99.0th percentile nationally (unusually high) and the 98.9th percentile among peers, whose median was 3.0%, unusually high among its peers too.

Nonaccrual assets and foreclosed property were 4.5% of assets, at the 99.0th percentile nationally (unusually high) and the 98.3rd percentile among peers, whose median was 0.3%, unusually high among its peers too. Loans 90+ days past due or not accruing were 4.8% of loans, at the 97.4th percentile nationally (unusually high) and the 96.8th percentile among peers, whose median was 0.4%, unusually high among its peers too. The provision for loan losses was 0.7% of assets, at the 97.3rd percentile nationally (unusually high) and the 97.2nd percentile among peers, whose median was 0.1%, unusually high among its peers too.

Losses on bonds held to maturity were 0.0% of equity, at the 2.8th percentile nationally (unusually low) and the 2.8th percentile among peers, whose median was 0.0%, unusually low among its peers too. The efficiency ratio was 34.5%, at the 2.9th percentile nationally (unusually low) and the 1.2nd percentile among peers, whose median was 63.7%, unusually low among its peers too. Overall, 17 of the bank's ratios sat in the national top or bottom 10%, and 17 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| annualized interest expense as a share of assets | 3.3% | 99.5th (unusually high) | 1.7% | 99.5th | unusually high among its peers too |
| brokered deposits as a share of deposits | 39.9% | 99.1st (unusually high) | 0.0% | 99.3rd | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 43.2% | 99.0th (unusually high) | 3.0% | 98.9th | unusually high among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 4.5% | 99.0th (unusually high) | 0.3% | 98.3rd | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 4.8% | 97.4th (unusually high) | 0.4% | 96.8th | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 0.7% | 97.3rd (unusually high) | 0.1% | 97.2nd | unusually high among its peers too |
| losses on bonds held to maturity, as a share of equity | 0.0% | 2.8th (unusually low) | 0.0% | 2.8th | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 34.5% | 2.9th (unusually low) | 63.7% | 1.2nd | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 64.5% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 243.9% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 83.6% | 50% or more | yes |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

Hindsight: this is an open watchlist case, meaning the bank was flagged by the model and remains open. The fact sheet holds no data from after the as-of quarter, so there is no later record yet to explain how its situation developed. Its place on the watchlist rests on the as-of figures described above, not on any later event.

## What happened next

Hindsight: the fact sheet contains no quarters after the as-of date, so there are no later ranks or watchlist flags to report. There is no failure date on record, and nothing in the data shows that the bank has stopped reporting. Later quarters, once available, will show whether its rank and flag change.

## Sources

- F1 · Bank name · n/a · Central Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · AR · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 10 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.8% · data/analyst/scores.parquet: percentile
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 9.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 9.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 10.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 31.4% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 43.2% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · 11.8% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 108.9% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 39.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 40.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 12.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 39.9%; contribution to the score · 2026-06-30 · +0.785 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 43.2%; contribution to the score · 2026-06-30 · +0.743 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: annualized interest expense as a share of assets, value 3.3%; contribution to the score · 2026-06-30 · +0.581 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 4.8%; contribution to the score · 2026-06-30 · +0.324 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the efficiency ratio (operating costs as a share of revenue), value 34.5%; contribution to the score · 2026-06-30 · +0.324 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 10.3%; contribution to the score · 2026-06-30 · -0.658 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 11.8%; contribution to the score · 2026-06-30 · -0.624 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: construction loans as a share of loans, value 7.9%; contribution to the score · 2026-06-30 · -0.414 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: loan-loss reserves as a share of loans, value 1.4%; contribution to the score · 2026-06-30 · -0.292 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F84 · Driver down #5: return on assets (profit as a share of assets), value 1.1%; contribution to the score · 2026-06-30 · -0.281 · data/analyst/scores.parquet: feature return_on_assets contribution
- F89 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 11.8% · data/features/fct_bank_features.parquet: return_on_equity
- F90 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 18.2% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 21.3% · data/features/fct_bank_features.parquet: return_on_equity
- F92 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2026-06-30 · -6.4 pp · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.624 · data/analyst/scores.parquet: feature return_on_equity contribution
- F94 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F95 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F96 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F97 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F98 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, change over four quarters, in percentage points · 2026-06-30 · +0.6 pp · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F99 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.012 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F100 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F101 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F102 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F103 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F104 · Trend: loans 30-89 days past due, as a share of assets, change over one quarter, in percentage points · 2026-06-30 · +0.9 pp · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F105 · Trend: loans 30-89 days past due, as a share of assets, change over four quarters, in percentage points · 2026-06-30 · +1.7 pp · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F106 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.141 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F107 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F108 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 1.6% · data/features/fct_bank_features.parquet: return_on_assets
- F110 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.8% · data/features/fct_bank_features.parquet: return_on_assets
- F111 · Trend: return on assets (profit as a share of assets), change over four quarters, in percentage points · 2026-06-30 · -0.7 pp · data/features/fct_bank_features.parquet: return_on_assets
- F112 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.281 · data/analyst/scores.parquet: feature return_on_assets contribution
- F113 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F114 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F115 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F116 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F118 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.075 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F119 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F120 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F121 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F122 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F124 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.077 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F125 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F126 · Trend: ratios outside their own prior range · 2026-06-30 · 15 · data/features/fct_bank_features.parquet
- F127 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F129 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F130 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F131 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 95.4% · data/analyst/scores.parquet: percentile
- F132 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F136 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F137 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F138 · Peers: annualized interest expense as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F139 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F140 · Peers: annualized interest expense as a share of assets, peer median · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F141 · Peers: annualized interest expense as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F142 · Peers: brokered deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 39.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F143 · Peers: brokered deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.1st · data/features/fct_bank_features.parquet: brokered_to_deposits
- F144 · Peers: brokered deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: brokered_to_deposits
- F145 · Peers: brokered deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: brokered_to_deposits
- F146 · Peers: brokered deposits as a share of deposits, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F147 · Peers: brokered deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: brokered_to_deposits
- F148 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 43.2% · data/features/fct_bank_features.parquet: texas_ratio
- F149 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: texas_ratio
- F150 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F151 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 98.9th · data/features/fct_bank_features.parquet: texas_ratio
- F152 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: texas_ratio
- F153 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F154 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F155 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F156 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F157 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.3rd · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F158 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F159 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F160 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F161 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.4th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F162 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F163 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 96.8th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F164 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F165 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F166 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F167 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.3rd · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F168 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F169 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 97.2nd · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F170 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F171 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F172 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F173 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 2.8th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F174 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F175 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 2.8th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F176 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F177 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F178 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-06-30 · 34.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F179 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-06-30 · 2.9th · data/features/fct_bank_features.parquet: efficiency_ratio
- F180 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: efficiency_ratio
- F181 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-06-30 · 1.2nd · data/features/fct_bank_features.parquet: efficiency_ratio
- F182 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-06-30 · 63.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F183 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F185 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 17 · data/features/fct_bank_features.parquet
- F186 · Peers: those ratios also unusual among peers · 2026-06-30 · 17 · data/features/fct_bank_features.parquet
- F188 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
