---
cert: 9728
name: "First Security Bank"
as_of: 2026-06-30
rank: 7
n_banks: 4313
percentile: 99.86088569441223
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:16:01"
writer_model: "claude-opus-5-5"
checked: true
---

# First Security Bank (cert 9728)

*Outcome not yet known.*

## Summary

As of 2026-06-30, First Security Bank ranked 7 out of 4,313 banks nationally on Canary's risk score, placing it in the 99.9th percentile and on Canary's watchlist. The score is driven mainly by its heavy reliance on brokered deposits (money placed through third-party brokers), paper losses on its bond holdings, and thin capital compared with most banks. Troubled loans are also well above the national median, while strong profitability and its capital ratios worked to pull the score down rather than up. The code-written real-estate section adds that the bank crossed the regulators' construction-lending screen but not the total commercial real estate screen.

## Warning signs in the data

Capital, the bank's own money that absorbs losses, is thin: equity was 7.0% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 7.9% against 11.0%. Its Tier 1 risk-based capital ratio (core capital against assets weighted by riskiness) was 10.8% versus a median of 14.6%, and the total risk-based capital ratio was 12.1% versus 15.8%.

Credit quality is weaker than typical: loans 90 or more days past due or no longer earning interest were 2.6% of loans against a median of 0.5%, and nonaccrual assets plus foreclosed property were 2.0% of assets against 0.3%. Loans 30-89 days past due were 0.7% of assets versus 0.2%, the Texas ratio (troubled assets against capital plus reserves) was 24.5% versus 2.9%, and the provision for loan losses (money set aside for expected bad loans) was 0.5% of assets versus 0.1%. Construction loans made up 12.1% of loans, well above the median of 5.3%.

On funding, brokered deposits were 23.9% of deposits against a national median of 0.0%, core deposits (stable, everyday deposits) were 52.2% of assets against 75.5%, and volatile funding (money that can leave quickly) was 22.5% of assets against 9.0%. Loans equaled 98.6% of deposits versus a median of 80.2%, and interest expense was 2.5% of assets versus 1.6%, while uninsured deposits, at 23.7%, were close to the median of 24.8%. Unrealized losses on bonds available for sale equaled 9.9% of equity, above the median of 5.6%, though profitability points the other way, with return on equity of 15.0% against a median of 11.6%.

## Understanding the score

As of 2026-06-30, First Security Bank ranked 7 out of 4,313 banks, which is the 99.9th percentile on a 0 to 100 scale where higher means riskier. That places it on the watchlist, which covers the top 2% of banks and held 87 banks that quarter.

The five features that pushed the score up most were brokered deposits at 23.9% of deposits, contributing +1.395, and losses on bonds available for sale at 9.9% of equity, contributing +0.965. Next came core deposits at 52.2% of assets, contributing +0.454, the efficiency ratio (operating costs as a share of revenue) at 55.8%, contributing +0.424, and interest expense at 2.5% of assets, contributing +0.230. The efficiency ratio is better than the national median of 62.1%, yet the model still counted it toward higher risk.

The five features that pulled the score down most were return on equity at 15.0%, contributing -0.630, the Tier 1 risk-based capital ratio at 10.8%, contributing -0.588, and return on assets at 1.1%, contributing -0.288. The total risk-based capital ratio at 12.1% contributed -0.238, and loans 30-89 days past due at 0.7% of assets contributed -0.194, even though that past-due figure is above the national median.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 378 | 4,589 |  |
| 2024-12-31 | 427 | 4,560 |  |
| 2025-03-31 | 764 | 4,536 |  |
| 2025-06-30 | 464 | 4,494 |  |
| 2025-09-30 | 300 | 4,452 |  |
| 2025-12-31 | 317 | 4,411 |  |
| 2026-03-31 | 19 | 4,353 | ▲ watchlist |
| 2026-06-30 | 7 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, First Security Bank ranked 7 out of 4,313 banks nationally, placing it in the 99.9th percentile on a scale where higher means riskier. A year earlier, on 2025-06-30, it sat in the 89.7th percentile, and the model rated it riskier than a year earlier. Of the 30 ratios compared with their own prior range, usually the prior 12 quarters, 7 sat outside that range at 2026-06-30.

Commercial real estate loans (loans backed by property such as offices and stores) made up 8.2% of loans, below their prior range of 9.9% to 13.4%, and this ratio pushed the score up with a contribution of +0.175 model log-odds units. That share changed by -1.9 pp over one quarter and -2.0 pp over four quarters. The efficiency ratio (operating costs as a share of revenue) was 55.8%, below its prior range of 57.8% to 63.2%, and it pushed the score up with a contribution of +0.424 model log-odds units.

The Tier 1 risk-based capital ratio (core capital held as a cushion against losses, relative to risk-weighted assets) was 10.8%, above its prior range of 9.8% to 10.7%, yet despite being outside its range it pushed the score down with a contribution of -0.588 model log-odds units. The total risk-based capital ratio, a broader capital cushion measure, was 12.1%, above its prior range of 10.8% to 11.9%, and despite being outside its range it also pushed the score down with a contribution of -0.238 model log-odds units. Net interest margin (the spread earned on lending and investing) was 3.51%, above its prior range of 3.2% to 3.45%, yet it pushed the score down with a contribution of -0.066 model log-odds units. The annualized provision for loan losses (money set aside for expected bad loans) as a share of assets was 0.5%, above its prior range of 0.1% to 0.3%, but it had little effect on the score, with a contribution of -0.033 model log-odds units.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| commercial real estate loans as a share of loans | 8.2% | 9.9% to 13.4% | prior 12 quarters | -1.9 pp | -2.0 pp | +0.175 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 55.8% | 57.8% to 63.2% | same quarter, prior 3 years | n/a | -2.1 pp | +0.424 | pushed the score up |
| the total risk-based capital ratio | 12.1% | 10.8% to 11.9% | prior 12 quarters | +0.3 pp | +0.9 pp | -0.238 | pushed the score down |
| annualized provision for loan losses as a share of assets | 0.5% | 0.1% to 0.3% | same quarter, prior 3 years | n/a | +0.3 pp | -0.033 | little effect on the score |
| the Tier 1 risk-based capital ratio | 10.8% | 9.8% to 10.7% | prior 12 quarters | +0.3 pp | +0.8 pp | -0.588 | pushed the score down |
| net interest margin (the spread earned on lending and investing) | 3.51% | 3.2% to 3.45% | same quarter, prior 3 years | n/a | +0.2 pp | -0.066 | pushed the score down |

7 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: All Other Under 1 Billion.

This is a general group: the FDIC did not record a lending specialty for this bank.

Peers: 255 banks in the same specialty group and size tier ($100 million to $1 billion).

First Security Bank ranked 7 out of 4,313 banks nationally on Canary's score, and its ratios stand out against both all banks and its peers. Its leverage ratio (core capital, the bank's own loss-absorbing money, as a share of average assets) was 7.9%, at the 2.7th percentile nationally, which is unusually low; among peers it sat at the 2.2nd percentile against a peer median of 11.4%, unusually low among its peers too. Its equity as a share of assets was 7.0%, at the 5.7th percentile nationally, which is unusually low; among peers it sat at the 9.2nd percentile against a peer median of 10.5%, unusually low among its peers too. Its Tier 1 risk-based capital ratio (core capital measured against assets weighted by riskiness) was 10.8%, at the 6.2nd percentile nationally, which is unusually low; among peers it sat at the 1.9th percentile against a peer median of 19.2%, unusually low among its peers too.

Brokered deposits (money placed through third-party brokers rather than gathered directly) made up 23.9% of deposits, at the 96.7th percentile nationally, which is unusually high; among peers this was the 98.6th percentile against a peer median of 0.0%, unusually high among its peers too. Volatile funding (money that can leave quickly) was 22.5% of assets, at the 95.4th percentile nationally, which is unusually high; among peers this was the 97.1st percentile against a peer median of 8.2%, unusually high among its peers too.

The Texas ratio (troubled assets compared with capital plus reserves) was 24.5%, at the 96.4th percentile nationally, which is unusually high; among peers this was the 98.2nd percentile against a peer median of 3.7%, unusually high among its peers too. The annualized provision for loan losses (money set aside for expected bad loans) was 0.5% of assets, at the 96.0th percentile nationally, which is unusually high; among peers this was the 97.8th percentile against a peer median of 0.1%, unusually high among its peers too. Nonaccrual assets and foreclosed property (loans no longer paying interest plus repossessed property) were 2.0% of assets, at the 94.2nd percentile nationally, which is unusually high; among peers this was the 97.1st percentile against a peer median of 0.3%, unusually high among its peers too. Overall, 12 of the bank's ratios fell in the national top or bottom 10%, and 12 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the leverage ratio (core capital as a share of average assets) | 7.9% | 2.7th (unusually low) | 11.4% | 2.2nd | unusually low among its peers too |
| brokered deposits as a share of deposits | 23.9% | 96.7th (unusually high) | 0.0% | 98.6th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 24.5% | 96.4th (unusually high) | 3.7% | 98.2nd | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 0.5% | 96.0th (unusually high) | 0.1% | 97.8th | unusually high among its peers too |
| volatile funding as a share of assets | 22.5% | 95.4th (unusually high) | 8.2% | 97.1st | unusually high among its peers too |
| equity as a share of assets | 7.0% | 5.7th (unusually low) | 10.5% | 9.2nd | unusually low among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 2.0% | 94.2nd (unusually high) | 0.3% | 97.1st | unusually high among its peers too |
| the Tier 1 risk-based capital ratio | 10.8% | 6.2nd (unusually low) | 19.2% | 1.9th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 104.2% | 100% or more | yes |
| Total commercial real estate loans ÷ capital | 144.7% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 47.8% | 50% or more | no |

It crossed the construction line (100% or more of capital).
It did not cross the total commercial real estate line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight: this bank is an open watchlist case, meaning it was flagged by the model and the data available to this memo contain no record of it failing. The fact sheet holds no figures from after the as-of quarter, so this section cannot yet judge whether the flag was early, wrong, or still developing. The reasons it sits on the watchlist are those described above: thin capital, heavy use of brokered and volatile funding, bond losses, and elevated troubled loans.

## What happened next

In hindsight: the fact sheet contains no later ranks, watchlist flags or reporting status for this bank after the as-of quarter. Because of that, this memo cannot say how its rank moved afterward or whether it continued to file reports; the score history table added by code shows whatever later data exist.

## Sources

- F1 · Bank name · n/a · First Security Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2026-06-30 · 7 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 10.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 12.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F33 · Bank: construction loans as a share of loans · 2026-06-30 · 12.1% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F34 · National median: construction loans as a share of loans · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 24.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · 15.0% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 55.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 98.6% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 23.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 23.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 52.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 22.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 9.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 23.9%; contribution to the score · 2026-06-30 · +1.395 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 9.9%; contribution to the score · 2026-06-30 · +0.965 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: core deposits as a share of assets, value 52.2%; contribution to the score · 2026-06-30 · +0.454 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F78 · Driver up #4: the efficiency ratio (operating costs as a share of revenue), value 55.8%; contribution to the score · 2026-06-30 · +0.424 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.5%; contribution to the score · 2026-06-30 · +0.230 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: return on equity (profit as a share of equity), value 15.0%; contribution to the score · 2026-06-30 · -0.630 · data/analyst/scores.parquet: feature return_on_equity contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 10.8%; contribution to the score · 2026-06-30 · -0.588 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: return on assets (profit as a share of assets), value 1.1%; contribution to the score · 2026-06-30 · -0.288 · data/analyst/scores.parquet: feature return_on_assets contribution
- F83 · Driver down #4: the total risk-based capital ratio, value 12.1%; contribution to the score · 2026-06-30 · -0.238 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F84 · Driver down #5: loans 30-89 days past due, as a share of assets, value 0.7%; contribution to the score · 2026-06-30 · -0.194 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F89 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 8.2% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F90 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 9.9% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F91 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 13.4% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F92 · Trend: commercial real estate loans as a share of loans, change over one quarter, in percentage points · 2026-06-30 · -1.9 pp · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F93 · Trend: commercial real estate loans as a share of loans, change over four quarters, in percentage points · 2026-06-30 · -2.0 pp · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F94 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.175 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F95 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F96 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 55.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 57.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 63.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F100 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.424 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F102 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2026-06-30 · 12.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F103 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 10.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F104 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 11.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F107 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2026-06-30 · -0.238 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F108 · Trend: the total risk-based capital ratio, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F109 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F110 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F111 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F113 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.033 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F114 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F115 · Trend: the Tier 1 risk-based capital ratio, value at the as-of quarter · 2026-06-30 · 10.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F116 · Trend: the Tier 1 risk-based capital ratio, lowest value in the comparison window · n/a · 9.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F117 · Trend: the Tier 1 risk-based capital ratio, highest value in the comparison window · n/a · 10.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F120 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2026-06-30 · -0.588 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F121 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F122 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 3.51% · data/features/fct_bank_features.parquet: net_interest_margin
- F123 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F124 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.45% · data/features/fct_bank_features.parquet: net_interest_margin
- F126 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.066 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F127 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F128 · Trend: ratios outside their own prior range · 2026-06-30 · 7 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F131 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F133 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 89.7% · data/analyst/scores.parquet: percentile
- F134 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F138 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F139 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 2.7th · data/features/fct_bank_features.parquet: leverage_ratio
- F140 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F141 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 2.2nd · data/features/fct_bank_features.parquet: leverage_ratio
- F142 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 11.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F143 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F144 · Peers: brokered deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 23.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F145 · Peers: brokered deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.7th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F146 · Peers: brokered deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: brokered_to_deposits
- F147 · Peers: brokered deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F148 · Peers: brokered deposits as a share of deposits, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F149 · Peers: brokered deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: brokered_to_deposits
- F150 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 24.5% · data/features/fct_bank_features.parquet: texas_ratio
- F151 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 96.4th · data/features/fct_bank_features.parquet: texas_ratio
- F152 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F153 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 98.2nd · data/features/fct_bank_features.parquet: texas_ratio
- F154 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.7% · data/features/fct_bank_features.parquet: texas_ratio
- F155 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F156 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F157 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.0th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F158 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F159 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 97.8th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F160 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F161 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F162 · Peers: volatile funding as a share of assets, bank value at the as-of quarter · 2026-06-30 · 22.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F163 · Peers: volatile funding as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 95.4th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F164 · Peers: volatile funding as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F165 · Peers: volatile funding as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 97.1st · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F166 · Peers: volatile funding as a share of assets, peer median · 2026-06-30 · 8.2% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F167 · Peers: volatile funding as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F168 · Peers: equity as a share of assets, bank value at the as-of quarter · 2026-06-30 · 7.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F169 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 5.7th · data/features/fct_bank_features.parquet: equity_to_assets
- F170 · Peers: equity as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F171 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 9.2nd · data/features/fct_bank_features.parquet: equity_to_assets
- F172 · Peers: equity as a share of assets, peer median · 2026-06-30 · 10.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F173 · Peers: equity as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F174 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F175 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 94.2nd · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F176 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F177 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 97.1st · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F178 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F179 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F180 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 10.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F181 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 6.2nd · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F182 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F183 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 1.9th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F184 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-06-30 · 19.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F185 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F187 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 12 · data/features/fct_bank_features.parquet
- F188 · Peers: those ratios also unusual among peers · 2026-06-30 · 12 · data/features/fct_bank_features.parquet
- F190 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
