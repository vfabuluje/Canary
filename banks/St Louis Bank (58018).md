---
cert: 58018
name: "St Louis Bank"
as_of: 2026-06-30
rank: 20
n_banks: 4313
percentile: 99.55947136563876
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:08:49"
writer_model: "claude-opus-5-5"
checked: true
---

# St Louis Bank (cert 58018)

*Outcome not yet known.*

## Summary

St Louis Bank, a Missouri bank, ranked 20 out of 4,313 FDIC-insured banks on Canary's risk score as of 2026-06-30, placing it in the 99.6th percentile, where higher means riskier. That puts it on Canary's watchlist, which holds 2% of banks, or 87 banks that quarter. Its heavy use of brokered deposits (money placed through middlemen rather than gathered directly from local customers), at 42.2% of deposits, was the largest factor raising its score. Its capital cushion was thinner than most banks' and its share of troubled loans was higher than the national median.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was thin: equity was 8.6% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.8% against 11.0%. Its risk-based capital ratios, which weigh assets by how risky they are, were also well below the median: Tier 1 at 10.0% versus 14.6%, and total at 11.3% versus 15.8%.

Credit quality was weaker than typical: loans 90 or more days past due or no longer accruing interest were 2.9% of loans, against a national median of 0.5%. Nonaccrual assets and foreclosed property were 2.5% of assets versus a median of 0.3%, and the Texas ratio, which compares troubled assets with capital plus reserves, was 25.5% versus 2.9%. Commercial real estate loans made up 40.1% of loans against a median of 23.6%, and construction loans 10.9% against 5.3%.

On funding, brokered deposits were 42.2% of deposits while the national median was 0.0%, and core deposits (stable, everyday customer deposits) were only 48.6% of assets against a median of 75.5%. Interest expense ran at 2.4% of assets versus 1.6%, cash was 3.2% of assets versus 6.2%, and unrealized losses on bonds available for sale equaled 6.6% of equity versus a median of 5.6%.

## Understanding the score

As of 2026-06-30, St Louis Bank ranked 20 of 4,313 banks, in the 99.6th percentile on a scale from 0 to 100 where higher means riskier, and it was flagged on the watchlist.

Five features pushed the score up the most. The biggest was brokered deposits at 42.2% of deposits, followed by unrealized losses on bonds available for sale at 6.6% of equity. Next came core deposits at 48.6% of assets, the efficiency ratio (operating costs as a share of revenue) at 56.8%, and interest expense at 2.4% of assets.

Five features pulled the score down the most. These were return on equity (profit as a share of equity) at 10.7% and the Tier 1 risk-based capital ratio at 10.0%. They also included loans 30-89 days past due at 0.5% of assets, the Texas ratio at 25.5%, and construction loans at 10.9% of loans.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 421 | 4,589 |  |
| 2024-12-31 | 287 | 4,560 |  |
| 2025-03-31 | 225 | 4,536 |  |
| 2025-06-30 | 156 | 4,494 |  |
| 2025-09-30 | 113 | 4,452 |  |
| 2025-12-31 | 247 | 4,411 |  |
| 2026-03-31 | 21 | 4,353 | ▲ watchlist |
| 2026-06-30 | 20 | 4,313 | ▲ watchlist |

## How its ratios moved

Each ratio was compared with its own range over the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios, and 10 of 30 ratios sat outside that range. The bank ranked 20 of 4,313 at 2026-06-30, up from the 96.6th percentile a year earlier on 2025-06-30, and the model rated it riskier than a year earlier.

Core deposits fell to 48.6% of assets, below their prior range of 50.5% to 60.7%, and this pushed the score up with a contribution of +0.440 model log-odds units. The efficiency ratio improved to 56.8%, below its prior range of 59.8% to 78.0%, yet it pushed the score up with a contribution of +0.393.

The Texas ratio rose to 25.5%, above its prior range of 8.7% to 19.2% and up +6.2 pp in one quarter, but it pushed the score down with a contribution of -0.294. Loans 90+ days past due or not accruing reached 2.9% of loans, above their prior range of 0.3% to 2.1%, but this pushed the score down with a contribution of -0.180. Commercial real estate loans rose to 40.1% of loans, above their prior range of 35.7% to 39.0%, yet this pushed the score down with a contribution of -0.152. Nonaccrual assets and foreclosed property reached 2.5% of assets, above their prior range of 0.8% to 1.8%, but had little effect on the score, with a contribution of -0.010.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| nonaccrual assets and foreclosed property, as a share of assets | 2.5% | 0.8% to 1.8% | prior 12 quarters | +0.8 pp | +1.0 pp | -0.010 | little effect on the score |
| the Texas ratio (troubled assets against capital plus reserves) | 25.5% | 8.7% to 19.2% | prior 12 quarters | +6.2 pp | +10.4 pp | -0.294 | pushed the score down |
| loans 90+ days past due or not accruing interest, as a share of loans | 2.9% | 0.3% to 2.1% | prior 12 quarters | +0.8 pp | +1.3 pp | -0.180 | pushed the score down |
| commercial real estate loans as a share of loans | 40.1% | 35.7% to 39.0% | prior 12 quarters | +1.4 pp | +1.8 pp | -0.152 | pushed the score down |
| core deposits as a share of assets | 48.6% | 50.5% to 60.7% | prior 12 quarters | -1.9 pp | -3.4 pp | +0.440 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 56.8% | 59.8% to 78.0% | same quarter, prior 3 years | n/a | -3.0 pp | +0.393 | pushed the score up |

10 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 753 banks in the same specialty group and size tier ($1 billion to $10 billion).

Brokered deposits at 42.2% of deposits were in the 99.2nd percentile nationally, unusually high, and in the 99.3rd percentile among peers against a peer median of 1.7%, unusually high among its peers too. Core deposits at 48.6% of assets were in the 5.1st percentile nationally, unusually low, and in the 2.6th percentile among peers against a peer median of 74.1%, unusually low among its peers too.

The Tier 1 risk-based capital ratio of 10.0% was in the 1.8th percentile nationally, unusually low, and in the 1.1st percentile among peers against a peer median of 13.3%, unusually low among its peers too. The total risk-based capital ratio of 11.3% was in the 2.5th percentile nationally, unusually low, and in the 1.8th percentile among peers against a peer median of 14.5%, unusually low among its peers too.

The Texas ratio of 25.5% was in the 96.8th percentile nationally, unusually high, and in the 97.9th percentile among peers against a peer median of 3.7%, unusually high among its peers too. Nonaccrual assets and foreclosed property at 2.5% of assets were in the 96.1st percentile nationally, unusually high, and in the 96.1st percentile among peers against a peer median of 0.4%, unusually high among its peers too. Loans 90+ days past due or not accruing at 2.9% of loans were in the 93.2nd percentile nationally, unusually high, and in the 95.9th percentile among peers against a peer median of 0.5%, unusually high among its peers too. Net loan write-offs at 0.0% of loans were in the 7.2nd percentile nationally, unusually low, and in the 3.7th percentile among peers against a peer median of 0.0%, unusually low among its peers too. Overall, 10 of the bank's ratios fell in the national top or bottom 10%, and 9 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| brokered deposits as a share of deposits | 42.2% | 99.2nd (unusually high) | 1.7% | 99.3rd | unusually high among its peers too |
| the Tier 1 risk-based capital ratio | 10.0% | 1.8th (unusually low) | 13.3% | 1.1st | unusually low among its peers too |
| the total risk-based capital ratio | 11.3% | 2.5th (unusually low) | 14.5% | 1.8th | unusually low among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 25.5% | 96.8th (unusually high) | 3.7% | 97.9th | unusually high among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 2.5% | 96.1st (unusually high) | 0.4% | 96.1st | unusually high among its peers too |
| core deposits as a share of assets | 48.6% | 5.1st (unusually low) | 74.1% | 2.6th | unusually low among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 2.9% | 93.2nd (unusually high) | 0.5% | 95.9th | unusually high among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.0% | 7.2nd (unusually low) | 0.0% | 3.7th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 89.1% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 337.4% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | 49.2% | 50% or more | no |

It did not cross the construction line.
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight: the fact sheet for this memo contains no data from after the as-of quarter, so there is no later result to report here. The bank's place on the watchlist rests on the as-of figures described above, chiefly its reliance on brokered deposits, its thin capital and its rising troubled loans.

## What happened next

In hindsight: no later ranks, watchlist flags or reporting status after the as-of quarter appear in the fact sheet, so this memo cannot say what happened next. The score history table added below shows any later quarters available in Canary's data.

## Sources

- F1 · Bank name · n/a · St Louis Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · MO · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 20 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.6% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 11.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F33 · Bank: construction loans as a share of loans · 2026-06-30 · 10.9% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F34 · National median: construction loans as a share of loans · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 40.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 25.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 2.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 42.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 48.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 6.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 42.2%; contribution to the score · 2026-06-30 · +1.489 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 6.6%; contribution to the score · 2026-06-30 · +0.804 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: core deposits as a share of assets, value 48.6%; contribution to the score · 2026-06-30 · +0.440 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F78 · Driver up #4: the efficiency ratio (operating costs as a share of revenue), value 56.8%; contribution to the score · 2026-06-30 · +0.393 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2026-06-30 · +0.256 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: return on equity (profit as a share of equity), value 10.7%; contribution to the score · 2026-06-30 · -0.656 · data/analyst/scores.parquet: feature return_on_equity contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 10.0%; contribution to the score · 2026-06-30 · -0.600 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: loans 30-89 days past due, as a share of assets, value 0.5%; contribution to the score · 2026-06-30 · -0.424 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F83 · Driver down #4: the Texas ratio (troubled assets against capital plus reserves), value 25.5%; contribution to the score · 2026-06-30 · -0.294 · data/analyst/scores.parquet: feature texas_ratio contribution
- F84 · Driver down #5: construction loans as a share of loans, value 10.9%; contribution to the score · 2026-06-30 · -0.294 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F89 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F90 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F91 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 1.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F94 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.010 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F95 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F96 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 25.5% · data/features/fct_bank_features.parquet: texas_ratio
- F97 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 8.7% · data/features/fct_bank_features.parquet: texas_ratio
- F98 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 19.2% · data/features/fct_bank_features.parquet: texas_ratio
- F99 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2026-06-30 · +6.2 pp · data/features/fct_bank_features.parquet: texas_ratio
- F101 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · -0.294 · data/analyst/scores.parquet: feature texas_ratio contribution
- F102 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature texas_ratio contribution
- F103 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F104 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F105 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 2.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F108 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.180 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F109 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F110 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 40.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F111 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 35.7% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F112 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 39.0% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F115 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.152 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F116 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F117 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 48.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F118 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 50.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F119 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 60.7% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F122 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.440 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F123 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F124 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 56.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F125 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 59.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F126 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 78.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F128 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.393 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F129 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F130 · Trend: ratios outside their own prior range · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F132 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F133 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F134 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F135 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 96.6% · data/analyst/scores.parquet: percentile
- F136 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F140 · Peers: brokered deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 42.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F141 · Peers: brokered deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.2nd · data/features/fct_bank_features.parquet: brokered_to_deposits
- F142 · Peers: brokered deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: brokered_to_deposits
- F143 · Peers: brokered deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: brokered_to_deposits
- F144 · Peers: brokered deposits as a share of deposits, peer median · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F145 · Peers: brokered deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: brokered_to_deposits
- F146 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F147 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 1.8th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F148 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F149 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 1.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F150 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-06-30 · 13.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F151 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F152 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 11.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F153 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 2.5th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F154 · Peers: the total risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F155 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 1.8th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F156 · Peers: the total risk-based capital ratio, peer median · 2026-06-30 · 14.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F157 · Peers: the total risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F158 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 25.5% · data/features/fct_bank_features.parquet: texas_ratio
- F159 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 96.8th · data/features/fct_bank_features.parquet: texas_ratio
- F160 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F161 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 97.9th · data/features/fct_bank_features.parquet: texas_ratio
- F162 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.7% · data/features/fct_bank_features.parquet: texas_ratio
- F163 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F164 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F165 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.1st · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F166 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F167 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 96.1st · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F168 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F169 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F170 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2026-06-30 · 48.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F171 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 5.1st · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F172 · Peers: core deposits as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F173 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 2.6th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F174 · Peers: core deposits as a share of assets, peer median · 2026-06-30 · 74.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F175 · Peers: core deposits as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F176 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F177 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 93.2nd · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F178 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F179 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 95.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F180 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F181 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F182 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F183 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 7.2nd · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F184 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F185 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 3.7th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F186 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F187 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F189 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F190 · Peers: those ratios also unusual among peers · 2026-06-30 · 9 · data/features/fct_bank_features.parquet
- F192 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
