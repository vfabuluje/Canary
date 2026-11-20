---
cert: 26704
name: "Balboa Thrift&Loan Assn"
as_of: 2026-06-30
rank: 33
n_banks: 4313
percentile: 99.25805703686528
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:57:27"
writer_model: "claude-opus-5-5"
checked: true
---

# Balboa Thrift&Loan Assn (cert 26704)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Balboa Thrift&Loan Assn, a California bank, ranked 33 out of 4,313 banks nationally, the 99.3rd percentile, and was flagged on Canary's watchlist. Its loan book showed strain: loans 30-89 days past due were 3.4% of assets against a national median of 0.2%, and it was setting aside 2.6% of assets for expected loan losses against a median of 0.1%. It also leaned on costly, flighty funding, with volatile funding (money that can leave quickly) at 40.8% of assets against a median of 9.0%, and it lost money, with a return on assets of -0.7%. Its capital, by contrast, sat close to the national median, and several capital and credit measures pulled the model's score down rather than up.

## Warning signs in the data

Capital (the owners' cushion against losses) looked roughly typical: equity was 11.1% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 10.6% against a median of 11.0%. Profit did not add to that cushion, as return on assets was -0.7% against a national median of 1.2%.

Credit quality was the clearest weak spot: loans 90+ days past due or not accruing interest were 1.1% of loans against a median of 0.5%, and nonaccrual assets plus foreclosed property were 1.0% of assets against 0.3%. Earlier-stage trouble was larger still, with loans 30-89 days past due at 3.4% of assets against 0.2%, and net write-offs (loans given up as lost) at 2.6% of loans against 0.0%. The Texas ratio (troubled assets against capital plus reserves) was 7.6% against a median of 2.9%, and reserves for loan losses were 2.5% of loans against 1.2%; note that the model treated the Texas ratio as pulling the score down, even though it is well above the median.

On funding, loans equalled 99.4% of deposits against a median of 80.2%, brokered deposits (funds placed through middlemen) were 13.9% of deposits against 0.0%, and core deposits (stable, everyday deposits) were 46.5% of assets against 75.5%. Cash was 8.1% of assets against a median of 6.2%, a modest buffer. Bond losses were not a concern: the bank held securities of 0.0% of assets, and unrealized losses on bonds available for sale were 0.0% of equity against a national median of 5.6%.

## Understanding the score

Balboa Thrift&Loan Assn ranked 33 out of 4,313 banks as of 2026-06-30, placing it in the 99.3rd percentile on a 0 to 100 scale where higher means riskier. That put it on Canary's watchlist, which covers the top 2% of banks and held 87 banks that quarter.

The five factors pushing the score up most were: money set aside for loan losses at 2.6% of assets (+0.608), interest expense (what it pays on deposits and borrowings) at 3.7% of assets (+0.474), volatile funding at 40.8% of assets (+0.382), brokered deposits at 13.9% of deposits (+0.357), and loans 30-89 days past due at 3.4% of assets (+0.223).

The five factors pulling the score down most were: the Texas ratio at 7.6% (-0.966), the Tier 1 risk-based capital ratio, a measure of core capital against riskier assets (-0.643), loans 90+ days past due or not accruing at 1.1% of loans (-0.499), return on equity at -6.3% (-0.278), and the leverage ratio at 10.6% (-0.252).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 95 | 4,589 |  |
| 2024-12-31 | 137 | 4,560 |  |
| 2025-03-31 | 119 | 4,536 |  |
| 2025-06-30 | 71 | 4,494 | ▲ watchlist |
| 2025-09-30 | 58 | 4,452 | ▲ watchlist |
| 2025-12-31 | 89 | 4,411 | ▲ watchlist |
| 2026-03-31 | 52 | 4,353 | ▲ watchlist |
| 2026-06-30 | 33 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, Balboa Thrift&Loan Assn ranked 33 out of 4,313 banks nationally, placing it in the 99.3rd percentile on a scale where higher means riskier. A year earlier, on 2025-06-30, it sat in the 98.4th percentile, and the model rates it about the same as a year earlier. Each ratio is compared with its own prior range, usually the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios. Of 28 ratios checked this way, 13 were outside their prior range, and the table shows the 6 furthest outside.

The annualized provision for loan losses (money set aside to cover expected bad loans) was 2.6% of assets, above its prior range of 1.1% to 1.5%, and contributed +0.608 model log-odds units (the model's internal scale, where positive values raise the score), which pushed the score up. Loans 30-89 days past due (behind on payments, but not yet severely) were 3.4% of assets, above their prior range of 1.6% to 2.5%, and contributed +0.223 model log-odds units, which pushed the score up.

The Texas ratio (troubled assets against capital plus reserves) was 7.6%, above its prior range of 1.7% to 6.7%, yet its contribution of -0.966 model log-odds units pushed the score down. Loans 90+ days past due or not accruing interest were 1.1% of loans, above their prior range of 0.2% to 1.0%, yet their contribution of -0.499 model log-odds units pushed the score down. Return on equity (profit as a share of equity) was -6.3%, below its prior range of -4.5% to 1.9%, yet its contribution of -0.278 model log-odds units pushed the score down. Annualized loan write-offs, net of recoveries, were 2.6% of loans, above their prior range of 1.3% to 2.0%, yet their contribution of -0.054 model log-odds units pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | 2.6% | 1.1% to 1.5% | same quarter, prior 3 years | n/a | +1.1 pp | +0.608 | pushed the score up |
| loans 30-89 days past due, as a share of assets | 3.4% | 1.6% to 2.5% | prior 12 quarters | +0.9 pp | +1.3 pp | +0.223 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 2.6% | 1.3% to 2.0% | same quarter, prior 3 years | n/a | +0.6 pp | -0.054 | pushed the score down |
| return on equity (profit as a share of equity) | -6.3% | -4.5% to 1.9% | same quarter, prior 3 years | n/a | -3.6 pp | -0.278 | pushed the score down |
| the Texas ratio (troubled assets against capital plus reserves) | 7.6% | 1.7% to 6.7% | prior 12 quarters | +0.9 pp | +5.5 pp | -0.966 | pushed the score down |
| loans 90+ days past due or not accruing interest, as a share of loans | 1.1% | 0.2% to 1.0% | prior 12 quarters | +0.2 pp | +0.8 pp | -0.499 | pushed the score down |

13 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

Interest expense, meaning what the bank pays on its deposits and borrowings, measured on an annualized basis as a share of assets, is 3.7%, at the 99.9th percentile nationally, which is unusually high; at the 100.0th percentile among peers against a peer median of 1.7%, it is unusually high among its peers too. Volatile funding, meaning money that can leave the bank quickly, is 40.8% of assets, at the 99.7th percentile nationally, which is unusually high; at the 99.9th percentile among peers against a peer median of 9.4%, it is unusually high among its peers too. Securities, meaning bonds and similar holdings that can usually be sold for cash, are 0.0% of assets, at the 1.3rd percentile nationally, which is unusually low; at the 1.2nd percentile among peers against a peer median of 14.7%, this is unusually low among its peers too.

The annualized provision for loan losses, money set aside to cover loans expected to go bad, is 2.6% of assets, at the 99.4th percentile nationally, which is unusually high; at the 99.3rd percentile among peers against a peer median of 0.1%, it is unusually high among its peers too. Loans 30-89 days past due, meaning borrowers who are behind on payments, equal 3.4% of assets, at the 99.1st percentile nationally, which is unusually high; at the 99.1st percentile among peers against a peer median of 0.2%, this is unusually high among its peers too. Annualized loan write-offs net of recoveries, meaning loans given up as uncollectable minus amounts later recovered, are 2.6% of loans, at the 99.0th percentile nationally, which is unusually high; at the 99.3rd percentile among peers against a peer median of 0.0%, they are unusually high among its peers too.

Return on equity, profit as a share of the owners' stake, is -6.3%, at the 2.1st percentile nationally, which is unusually low; at the 1.6th percentile among peers against a peer median of 11.7%, it is unusually low among its peers too. Return on assets, profit as a share of everything the bank owns, is -0.7%, at the 2.3rd percentile nationally, which is unusually low; at the 1.5th percentile among peers against a peer median of 1.2%, it is unusually low among its peers too. Overall, 15 of the bank's ratios fall in the national top or bottom 10%, and 15 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| annualized interest expense as a share of assets | 3.7% | 99.9th (unusually high) | 1.7% | 100.0th | unusually high among its peers too |
| volatile funding as a share of assets | 40.8% | 99.7th (unusually high) | 9.4% | 99.9th | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 2.6% | 99.4th (unusually high) | 0.1% | 99.3rd | unusually high among its peers too |
| loans 30-89 days past due, as a share of assets | 3.4% | 99.1st (unusually high) | 0.2% | 99.1st | unusually high among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 2.6% | 99.0th (unusually high) | 0.0% | 99.3rd | unusually high among its peers too |
| securities as a share of assets | 0.0% | 1.3rd (unusually low) | 14.7% | 1.2nd | unusually low among its peers too |
| return on equity (profit as a share of equity) | -6.3% | 2.1st (unusually low) | 11.7% | 1.6th | unusually low among its peers too |
| return on assets (profit as a share of assets) | -0.7% | 2.3rd (unusually low) | 1.2% | 1.5th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 193.8% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 1.3% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

Hindsight view: this bank falls in the open-watchlist case, meaning the model flagged it and our records do not show a failure. The fact sheet holds no data from after the as-of quarter, so we cannot yet judge in hindsight whether the flag was borne out.

## What happened next

Hindsight view: the fact sheet contains no ranks, flags or filings from after the as-of quarter. Because of that, we cannot say here how its ranking moved afterwards or whether it still reports to regulators; the score history table added by code is the place to check later quarters.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · CA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 33 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.3% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 11.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 1.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F25 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F26 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F27 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F28 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 7.6% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: loans as a share of deposits · 2026-06-30 · 99.4% · data/features/fct_bank_features.parquet: loans_to_deposits
- F46 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 13.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F51 · Bank: core deposits as a share of assets · 2026-06-30 · 46.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F52 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F55 · Bank: volatile funding as a share of assets · 2026-06-30 · 40.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F56 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 8.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F63 · Bank: securities as a share of assets · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F71 · Driver up #1: annualized provision for loan losses as a share of assets, value 2.6%; contribution to the score · 2026-06-30 · +0.608 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F72 · Driver up #2: annualized interest expense as a share of assets, value 3.7%; contribution to the score · 2026-06-30 · +0.474 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F73 · Driver up #3: volatile funding as a share of assets, value 40.8%; contribution to the score · 2026-06-30 · +0.382 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F74 · Driver up #4: brokered deposits as a share of deposits, value 13.9%; contribution to the score · 2026-06-30 · +0.357 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F75 · Driver up #5: loans 30-89 days past due, as a share of assets, value 3.4%; contribution to the score · 2026-06-30 · +0.223 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F76 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 7.6%; contribution to the score · 2026-06-30 · -0.966 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver down #2: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.643 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F78 · Driver down #3: loans 90+ days past due or not accruing interest, as a share of loans, value 1.1%; contribution to the score · 2026-06-30 · -0.499 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver down #4: return on equity (profit as a share of equity), value -6.3%; contribution to the score · 2026-06-30 · -0.278 · data/analyst/scores.parquet: feature return_on_equity contribution
- F80 · Driver down #5: the leverage ratio (core capital as a share of average assets), value 10.6%; contribution to the score · 2026-06-30 · -0.252 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F85 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F86 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F87 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 1.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F89 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.608 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F90 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F91 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F92 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 1.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F93 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 2.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F96 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.223 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F97 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F98 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F99 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 1.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F100 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 2.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F102 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.054 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F103 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F104 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -6.3% · data/features/fct_bank_features.parquet: return_on_equity
- F105 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -4.5% · data/features/fct_bank_features.parquet: return_on_equity
- F106 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 1.9% · data/features/fct_bank_features.parquet: return_on_equity
- F108 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.278 · data/analyst/scores.parquet: feature return_on_equity contribution
- F109 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F110 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 7.6% · data/features/fct_bank_features.parquet: texas_ratio
- F111 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 1.7% · data/features/fct_bank_features.parquet: texas_ratio
- F112 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 6.7% · data/features/fct_bank_features.parquet: texas_ratio
- F115 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · -0.966 · data/analyst/scores.parquet: feature texas_ratio contribution
- F116 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature texas_ratio contribution
- F117 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F118 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F119 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F122 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.499 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F123 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F124 · Trend: ratios outside their own prior range · 2026-06-30 · 13 · data/features/fct_bank_features.parquet
- F125 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F126 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F127 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F128 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F129 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 98.4% · data/analyst/scores.parquet: percentile
- F130 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F134 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F135 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F136 · Peers: annualized interest expense as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F137 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 100.0th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F138 · Peers: annualized interest expense as a share of assets, peer median · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F139 · Peers: annualized interest expense as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F140 · Peers: volatile funding as a share of assets, bank value at the as-of quarter · 2026-06-30 · 40.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F141 · Peers: volatile funding as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F142 · Peers: volatile funding as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F143 · Peers: volatile funding as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F144 · Peers: volatile funding as a share of assets, peer median · 2026-06-30 · 9.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F145 · Peers: volatile funding as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F146 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F147 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.4th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F148 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F149 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F150 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F151 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F152 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F153 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.1st · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F154 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F155 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.1st · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F156 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F157 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F158 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F159 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F160 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F161 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F162 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F163 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F164 · Peers: securities as a share of assets, bank value at the as-of quarter · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F165 · Peers: securities as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 1.3rd · data/features/fct_bank_features.parquet: securities_to_assets
- F166 · Peers: securities as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: securities_to_assets
- F167 · Peers: securities as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 1.2nd · data/features/fct_bank_features.parquet: securities_to_assets
- F168 · Peers: securities as a share of assets, peer median · 2026-06-30 · 14.7% · data/features/fct_bank_features.parquet: securities_to_assets
- F169 · Peers: securities as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: securities_to_assets
- F170 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -6.3% · data/features/fct_bank_features.parquet: return_on_equity
- F171 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 2.1st · data/features/fct_bank_features.parquet: return_on_equity
- F172 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F173 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 1.6th · data/features/fct_bank_features.parquet: return_on_equity
- F174 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 11.7% · data/features/fct_bank_features.parquet: return_on_equity
- F175 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F176 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2026-06-30 · -0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F177 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 2.3rd · data/features/fct_bank_features.parquet: return_on_assets
- F178 · Peers: return on assets (profit as a share of assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F179 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2026-06-30 · 1.5th · data/features/fct_bank_features.parquet: return_on_assets
- F180 · Peers: return on assets (profit as a share of assets), peer median · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F181 · Peers: return on assets (profit as a share of assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F183 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 15 · data/features/fct_bank_features.parquet
- F184 · Peers: those ratios also unusual among peers · 2026-06-30 · 15 · data/features/fct_bank_features.parquet
- F186 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
