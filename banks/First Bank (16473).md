---
cert: 16473
name: "First Bank"
as_of: 2026-06-30
rank: 26
n_banks: 4313
percentile: 99.42035706005102
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:57:26"
writer_model: "claude-opus-5-5"
checked: true
---

# First Bank (cert 16473)

*Outcome not yet known.*

## Summary

First Bank, a Kansas bank, ranked 26 of 4,313 banks nationally on Canary's risk score as of 2026-06-30, which puts it in the 99.4th percentile and on the watchlist. The main reason is troubled loans: its Texas ratio, which weighs troubled assets against capital plus reserves, was 40.9%, and loans 90 or more days past due or no longer earning interest were 7.8% of loans, both far above the national medians of 2.9% and 0.5%. Against that, its capital cushion and profits look ordinary to solid, with a leverage ratio, core capital as a share of average assets, of 12.4% against a national median of 11.0%.

## Warning signs in the data

Credit quality is the clearest weak spot as of 2026-06-30. Loans 90 or more days past due or not accruing interest (loans on which the bank has stopped booking interest) made up 7.8% of loans, against a national median of 0.5%. Nonaccrual assets and foreclosed property were 3.3% of assets versus a median of 0.3%, and the Texas ratio stood at 40.9% versus a median of 2.9%. The bank has set aside more for losses than most banks, with loan-loss reserves at 2.9% of loans against a median of 1.2% and an annualized provision (the expense that builds those reserves) of 0.3% of assets against a median of 0.1%. Actual net write-offs, loans written off as lost minus recoveries, were only -0.0% of loans against a median of 0.0%, so problem loans have piled up without yet being written off.

Funding and liquidity lean on less common sources. Cash was just 1.4% of assets against a national median of 6.2%, while Federal Home Loan Bank borrowings (loans from a government-sponsored lender to banks) were 11.6% of assets against a median of 0.2%. Brokered deposits, money placed through middlemen, were 8.4% of deposits against a median of 0.0%, and core deposits, the stable everyday kind, were 67.8% of assets against a median of 75.5%. Loans equaled 90.3% of deposits, above the national median of 80.2%. Unrealized losses on bonds available for sale were 8.3% of equity, above the median of 5.6%, while losses on bonds held to maturity were 0.0%, in line with the median of 0.0%.

Capital points the other way: equity was 11.6% of assets against a national median of 10.6%, and the leverage ratio was 12.4% against 11.0%. Profitability is close to typical, with return on assets of 1.1% against a median of 1.2%, and the bank did not cross either commercial real estate concentration line in the code-written section.

## Understanding the score

First Bank ranked 26 of 4,313 banks as of 2026-06-30, the 99.4th percentile on a scale of 0 to 100 where higher means riskier. The watchlist covers the top 2% of banks, which was 87 banks that quarter, and this bank was flagged.

Five features pushed the score up most: the Texas ratio at 40.9% (contribution +1.046), loans 90 or more days past due or not accruing at 7.8% of loans (+0.843), losses on bonds available for sale at 8.3% of equity (+0.589), cash at 1.4% of assets (+0.141), and loan-loss reserves at 2.9% of loans (+0.050). Five features pulled it down most: the Tier 1 risk-based capital ratio, core capital measured against assets weighted by their riskiness, whose value is not shown in the fact sheet (-0.694); return on equity at 8.9% (-0.668); loans only recently past due, short of the seriously late stage, at 0.2% of assets (-0.377); return on assets at 1.1% (-0.301); and the leverage ratio at 12.4% (-0.275). In short, the model weighed heavy problem loans more than the bank's solid capital and steady profits.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 2,784 | 4,589 |  |
| 2024-12-31 | 1,141 | 4,560 |  |
| 2025-03-31 | 1,655 | 4,536 |  |
| 2025-06-30 | 1,318 | 4,494 |  |
| 2025-09-30 | 1,490 | 4,452 |  |
| 2025-12-31 | 320 | 4,411 |  |
| 2026-03-31 | 158 | 4,353 |  |
| 2026-06-30 | 26 | 4,313 | ▲ watchlist |

## How its ratios moved

Canary compares each ratio with the bank's own past, which for most ratios means the prior 12 quarters. At the latest quarter, 12 of the 28 ratios checked sat outside their own prior range, and the table shows the 6 furthest outside. The bank ranked 26 of 4,313 banks nationally, the 99.4th percentile, compared with the 70.7th percentile a year earlier, so the model rated it riskier than a year earlier.

The Texas ratio, which weighs troubled assets against capital plus reserves, stood at 40.9%, above its prior range of 0.8% to 29.0%. It rose +11.9 pp in one quarter and +36.6 pp over four quarters. At 40.9%, the Texas ratio pushed the score up, contributing +1.046 model log-odds units. Loans 90 or more days past due or no longer earning interest made up 7.8% of loans, above the prior range of 0.2% to 5.9%, and this ratio pushed the score up with a contribution of +0.843. That share rose +2.0 pp in one quarter and +7.6 pp over four quarters. Cash was 1.4% of assets, below its prior range of 2.0% to 4.0%, and it pushed the score up with a contribution of +0.141.

Net loan write-offs, meaning loans written off as lost minus amounts recovered, were 0.0% of loans, below the prior range of 0.2% to 0.8%, yet this ratio had little effect on the score, contributing +0.000. The provision for loan losses, money set aside to cover expected bad loans, was 0.3% of assets, above its prior range of 0.0% to 0.1%, but in contrast it pushed the score down, contributing -0.077. The efficiency ratio, operating costs as a share of revenue, was 64.8%, below its prior range of 67.4% to 84.5%, and it also pushed the score down, contributing -0.103.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 40.9% | 0.8% to 29.0% | prior 12 quarters | +11.9 pp | +36.6 pp | +1.046 | pushed the score up |
| loans 90+ days past due or not accruing interest, as a share of loans | 7.8% | 0.2% to 5.9% | prior 12 quarters | +2.0 pp | +7.6 pp | +0.843 | pushed the score up |
| cash as a share of assets | 1.4% | 2.0% to 4.0% | prior 12 quarters | -1.1 pp | -0.6 pp | +0.141 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.0% | 0.2% to 0.8% | same quarter, prior 3 years | n/a | -0.2 pp | +0.000 | little effect on the score |
| annualized provision for loan losses as a share of assets | 0.3% | 0.0% to 0.1% | same quarter, prior 3 years | n/a | +0.2 pp | -0.077 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 64.8% | 67.4% to 84.5% | same quarter, prior 3 years | n/a | -2.6 pp | -0.103 | pushed the score down |

12 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Agricultural Specialization.

Peers: 642 banks in the same specialty group and size tier ($100 million to $1 billion).

Loans that are seriously past due or no longer accruing interest (problem loans the bank has stopped booking interest on) made up 7.8% of First Bank's loans, at the 99.1st national percentile, which is unusually high, and at the 99.3rd percentile among its peers against a peer median of 0.4%, unusually high among its peers too. The Texas ratio, which weighs troubled assets against capital plus reserves, was 40.9%, at the 98.9th national percentile, which is unusually high, and at the 98.8th percentile among its peers against a peer median of 2.5%, unusually high among its peers too. Nonaccrual assets and foreclosed property (loans not earning interest plus property taken back from borrowers) were 3.3% of assets, at the 98.0th national percentile, which is unusually high, and at the 98.7th percentile among its peers against a peer median of 0.2%, unusually high among its peers too. Loan-loss reserves (money set aside to cover expected loan losses) were 2.9% of loans, at the 97.2nd national percentile, which is unusually high, and at the 98.1st percentile among its peers against a peer median of 1.2%, unusually high among its peers too.

Federal Home Loan Bank borrowings (loans from a government-sponsored lender to banks) were 11.6% of assets, at the 95.2nd national percentile, which is unusually high, and at the 95.9th percentile among its peers against a peer median of 0.7%, unusually high among its peers too. Cash was 1.4% of assets, at the 6.0th national percentile, which is unusually low, and at the 10.0th percentile among its peers against a peer median of 4.6%, typical for its peer group. Annualized loan write-offs net of recoveries (loans written off as uncollectible, minus amounts later recovered) were 0.0% of loans, at the 6.5th national percentile, which is unusually low, and at the 8.8th percentile among its peers against a peer median of 0.0%, unusually low among its peers too. The annualized provision for loan losses (the expense a bank books to build its reserves) was 0.3% of assets, at the 90.6th national percentile, which is unusually high, and at the 93.7th percentile among its peers against a peer median of 0.1%, unusually high among its peers too.

Overall, 8 of the ratios shown fall in the national top or bottom 10%, and 7 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| loans 90+ days past due or not accruing interest, as a share of loans | 7.8% | 99.1st (unusually high) | 0.4% | 99.3rd | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 40.9% | 98.9th (unusually high) | 2.5% | 98.8th | unusually high among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 3.3% | 98.0th (unusually high) | 0.2% | 98.7th | unusually high among its peers too |
| loan-loss reserves as a share of loans | 2.9% | 97.2nd (unusually high) | 1.2% | 98.1st | unusually high among its peers too |
| Federal Home Loan Bank borrowings as a share of assets | 11.6% | 95.2nd (unusually high) | 0.7% | 95.9th | unusually high among its peers too |
| cash as a share of assets | 1.4% | 6.0th (unusually low) | 4.6% | 10.0th | typical for its peer group |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.0% | 6.5th (unusually low) | 0.0% | 8.8th | unusually low among its peers too |
| annualized provision for loan losses as a share of assets | 0.3% | 90.6th (unusually high) | 0.1% | 93.7th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 3.2% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 79.1% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 1.0% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight: this bank is an open watchlist case, meaning it was flagged by the model but the fact sheet contains no data from after the as-of quarter. Because there are no hindsight facts, this memo cannot say whether the warning signs eased or worsened later, and it makes no claim either way. The flag itself rests on the as-of picture described above, chiefly a large build-up of troubled loans relative to the bank's capital and reserves.

## What happened next

In hindsight: the fact sheet holds no later ranks, watchlist flags or reporting status for this bank after the as-of quarter. So this memo cannot say whether First Bank still reports to the FDIC or how its score moved afterwards; the score history table added by code is the place to check for any later quarters.

## Sources

- F1 · Bank name · n/a · First Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KS · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 26 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.4% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 12.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 7.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F25 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · -0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F26 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F27 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F28 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 40.9% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: loans as a share of deposits · 2026-06-30 · 90.3% · data/features/fct_bank_features.parquet: loans_to_deposits
- F46 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 8.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F51 · Bank: core deposits as a share of assets · 2026-06-30 · 67.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F52 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 1.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F59 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F60 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 8.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 40.9%; contribution to the score · 2026-06-30 · +1.046 · data/analyst/scores.parquet: feature texas_ratio contribution
- F72 · Driver up #2: loans 90+ days past due or not accruing interest, as a share of loans, value 7.8%; contribution to the score · 2026-06-30 · +0.843 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F73 · Driver up #3: losses on bonds available for sale, as a share of equity, value 8.3%; contribution to the score · 2026-06-30 · +0.589 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F74 · Driver up #4: cash as a share of assets, value 1.4%; contribution to the score · 2026-06-30 · +0.141 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F75 · Driver up #5: loan-loss reserves as a share of loans, value 2.9%; contribution to the score · 2026-06-30 · +0.050 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.694 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: return on equity (profit as a share of equity), value 8.9%; contribution to the score · 2026-06-30 · -0.668 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver down #3: loans 30-89 days past due, as a share of assets, value 0.2%; contribution to the score · 2026-06-30 · -0.377 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F79 · Driver down #4: return on assets (profit as a share of assets), value 1.1%; contribution to the score · 2026-06-30 · -0.301 · data/analyst/scores.parquet: feature return_on_assets contribution
- F80 · Driver down #5: the leverage ratio (core capital as a share of average assets), value 12.4%; contribution to the score · 2026-06-30 · -0.275 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F81 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 40.9% · data/features/fct_bank_features.parquet: texas_ratio
- F82 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: texas_ratio
- F83 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 29.0% · data/features/fct_bank_features.parquet: texas_ratio
- F84 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2026-06-30 · +11.9 pp · data/features/fct_bank_features.parquet: texas_ratio
- F85 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over four quarters, in percentage points · 2026-06-30 · +36.6 pp · data/features/fct_bank_features.parquet: texas_ratio
- F86 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · +1.046 · data/analyst/scores.parquet: feature texas_ratio contribution
- F87 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F88 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 7.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F89 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F90 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 5.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F91 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, change over one quarter, in percentage points · 2026-06-30 · +2.0 pp · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F92 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, change over four quarters, in percentage points · 2026-06-30 · +7.6 pp · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F93 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.843 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F94 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F95 · Trend: cash as a share of assets, value at the as-of quarter · 2026-06-30 · 1.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F96 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 2.0% · data/features/fct_bank_features.parquet: cash_to_assets
- F97 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 4.0% · data/features/fct_bank_features.parquet: cash_to_assets
- F100 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.141 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F101 · Trend: cash as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature cash_to_assets contribution
- F102 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F103 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F104 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F106 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.000 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F107 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F108 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F109 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F110 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F112 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.077 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F113 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F114 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 64.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F115 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 67.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F116 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 84.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F118 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.103 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F119 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F120 · Trend: ratios outside their own prior range · 2026-06-30 · 12 · data/features/fct_bank_features.parquet
- F121 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F122 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F123 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F125 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 70.7% · data/analyst/scores.parquet: percentile
- F126 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F130 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 7.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F131 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.1st · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F132 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F133 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F134 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F135 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F136 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 40.9% · data/features/fct_bank_features.parquet: texas_ratio
- F137 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 98.9th · data/features/fct_bank_features.parquet: texas_ratio
- F138 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F139 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 98.8th · data/features/fct_bank_features.parquet: texas_ratio
- F140 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: texas_ratio
- F141 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F142 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F143 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.0th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F144 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F145 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.7th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F146 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F147 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F148 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: allowance_to_loans
- F149 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.2nd · data/features/fct_bank_features.parquet: allowance_to_loans
- F150 · Peers: loan-loss reserves as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: allowance_to_loans
- F151 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 98.1st · data/features/fct_bank_features.parquet: allowance_to_loans
- F152 · Peers: loan-loss reserves as a share of loans, peer median · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F153 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F154 · Peers: Federal Home Loan Bank borrowings as a share of assets, bank value at the as-of quarter · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F155 · Peers: Federal Home Loan Bank borrowings as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 95.2nd · data/features/fct_bank_features.parquet: fhlb_to_assets
- F156 · Peers: Federal Home Loan Bank borrowings as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: fhlb_to_assets
- F157 · Peers: Federal Home Loan Bank borrowings as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 95.9th · data/features/fct_bank_features.parquet: fhlb_to_assets
- F158 · Peers: Federal Home Loan Bank borrowings as a share of assets, peer median · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F159 · Peers: Federal Home Loan Bank borrowings as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: fhlb_to_assets
- F160 · Peers: cash as a share of assets, bank value at the as-of quarter · 2026-06-30 · 1.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F161 · Peers: cash as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 6.0th · data/features/fct_bank_features.parquet: cash_to_assets
- F162 · Peers: cash as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: cash_to_assets
- F163 · Peers: cash as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 10.0th · data/features/fct_bank_features.parquet: cash_to_assets
- F164 · Peers: cash as a share of assets, peer median · 2026-06-30 · 4.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F165 · Peers: cash as a share of assets, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: cash_to_assets
- F166 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F167 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 6.5th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F168 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F169 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 8.8th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F170 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F171 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F172 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F173 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 90.6th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F174 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F175 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 93.7th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F176 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F177 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F179 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F180 · Peers: those ratios also unusual among peers · 2026-06-30 · 7 · data/features/fct_bank_features.parquet
- F182 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
