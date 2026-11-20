---
cert: 14867
name: "Home State Bank"
as_of: 2026-06-30
rank: 24
n_banks: 4313
percentile: 99.46672849524693
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:50"
writer_model: "claude-opus-5-5"
checked: true
---

# Home State Bank (cert 14867)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Home State Bank ranked 24 out of 4,313 banks on Canary's score, placing it in the 99.5th percentile, where higher means riskier, and it was flagged on the watchlist. Its capital ratios sat well below national medians, its profits had turned negative, and it leaned heavily on brokered deposits (money placed through middlemen) and other fast-moving funding. On 2025-06-30 it sat at the 58.7th percentile, and the model rated it riskier than a year earlier.

## Warning signs in the data

Capital, the owners' cushion that absorbs losses, was thin: equity was 8.6% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.9% against 11.0%. The Tier 1 risk-based capital ratio (core capital against assets weighted by riskiness) was 10.0% versus a median of 14.6%, and the total risk-based capital ratio was 11.3% versus 15.8%.

Credit quality was weak: loans 90+ days past due or not accruing interest were 2.2% of loans against a median of 0.5%, and nonaccrual assets and foreclosed property were 1.8% of assets against 0.3%. The Texas ratio (troubled assets against capital plus reserves) was 16.9% against a median of 2.9%, and the provision for loan losses (money set aside for bad loans) ran 1.8% of assets against 0.1%. Return on assets (profit as a share of assets) was -0.3% against a median of 1.2%. Construction loans were 17.6% of loans against 5.3%, and commercial real estate loans were 36.1% against 23.6%; the concentration section shows the bank crossed the regulators' construction screen but not the total commercial real estate screen.

On funding, brokered deposits were 19.6% of deposits against a median of 0.0%, core deposits (steady everyday deposits) were 47.5% of assets against 75.5%, and volatile funding was 25.6% of assets against 9.0%. Interest expense ran 2.4% of assets against 1.6%, and losses on bonds available for sale (bonds the bank may sell) were 6.4% of equity, slightly above the median of 5.6%. One point runs the other way: uninsured deposits (balances above the insurance limit) were only 6.5% of deposits against a median of 24.8%. The model also reads some weak figures differently from a plain comparison: the low Tier 1 ratio, the losses and the past-due loans lowered its score rather than raising it.

## Understanding the score

Home State Bank ranked 24 out of 4,313 banks as of 2026-06-30, the 99.5th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks and held 87 banks that quarter.

The five features that pushed the score up most were brokered deposits at 19.6% of deposits, losses on bonds available for sale at 6.4% of equity, core deposits at 47.5% of assets, interest expense at 2.4% of assets, and the provision for loan losses at 1.8% of assets. The five that pushed it down most were the Tier 1 risk-based capital ratio at 10.0%, loans 30-89 days past due at 0.2% of assets, return on equity (profit as a share of the owners' stake) at -3.1%, loans 90+ days past due or not accruing at 2.2% of loans, and the Texas ratio at 16.9%. Several of those downward drivers look weak beside national medians, yet in the model's calculation they lowered the score.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,694 | 4,589 |  |
| 2024-12-31 | 1,846 | 4,560 |  |
| 2025-03-31 | 2,263 | 4,536 |  |
| 2025-06-30 | 1,855 | 4,494 |  |
| 2025-09-30 | 1,410 | 4,452 |  |
| 2025-12-31 | 154 | 4,411 |  |
| 2026-03-31 | 41 | 4,353 | ▲ watchlist |
| 2026-06-30 | 24 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, Home State Bank ranked 24 out of 4,313 banks nationally, placing it in the 99.5th percentile, where higher means riskier. On 2025-06-30 it sat at the 58.7th percentile, and the model rated it riskier than a year earlier. Of the 30 ratios compared with their own history, 10 were outside the range they had held over the prior 12 quarters.

Core deposits (steady everyday customer deposits, a stable source of funding) made up 47.5% of assets, below their prior range of 49.0% to 67.6%, after a change of -10.4 pp over four quarters. At 47.5% of assets, core deposits had a contribution of +0.447 model log-odds units and pushed the score up. The annualized provision for loan losses (money set aside for loans that may not be repaid) was 1.8% of assets, well above its prior range of 0.1% to 0.2%, with a contribution of +0.218 that pushed the score up. Loan-loss reserves (the cushion already held against bad loans) stood at 2.6% of loans, above their prior range of 1.1% to 2.4%, with a contribution of +0.121 that pushed the score up.

Return on equity (profit as a share of the owners' stake) was -3.1%, far below its prior range of 11.3% to 17.2%, yet its contribution of -0.384 pushed the score down rather than up. Commercial real estate loans (loans on business property) rose to 36.1% of loans, above their prior range of 29.5% to 34.3%, but this ratio's contribution of -0.154 also pushed the score down. Return on assets (profit as a share of assets) was -0.3%, below its prior range of 0.9% to 1.5%, yet its contribution of -0.030 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -3.1% | 11.3% to 17.2% | same quarter, prior 3 years | n/a | -17.3 pp | -0.384 | pushed the score down |
| annualized provision for loan losses as a share of assets | 1.8% | 0.1% to 0.2% | same quarter, prior 3 years | n/a | +1.7 pp | +0.218 | pushed the score up |
| return on assets (profit as a share of assets) | -0.3% | 0.9% to 1.5% | same quarter, prior 3 years | n/a | -1.5 pp | -0.030 | little effect on the score |
| commercial real estate loans as a share of loans | 36.1% | 29.5% to 34.3% | prior 12 quarters | +1.8 pp | +4.0 pp | -0.154 | pushed the score down |
| loan-loss reserves as a share of loans | 2.6% | 1.1% to 2.4% | prior 12 quarters | +0.2 pp | +1.3 pp | +0.121 | pushed the score up |
| core deposits as a share of assets | 47.5% | 49.0% to 67.6% | prior 12 quarters | -1.5 pp | -10.4 pp | +0.447 | pushed the score up |

10 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

As of 2026-06-30, Home State Bank ranked 24 out of 4,313 banks on Canary's score, where a lower rank means a higher score. Its annualized provision for loan losses (money set aside for loans that may not be repaid) was 1.8% of assets, at the 99.1st percentile nationally, which is unusually high, and at the 99.1st percentile among peers against a peer median of 0.1%, unusually high among its peers too. Its loan-loss reserves (the cushion already held for bad loans) were 2.6% of loans, at the 96.3rd percentile nationally, which is unusually high, and at the 97.7th percentile among peers against a peer median of 1.2%, unusually high among its peers too. Its return on equity (profit as a share of the owners' stake) was -3.1%, at the 2.9th percentile nationally, which is unusually low, and at the 2.4th percentile among peers against a peer median of 11.7%, unusually low among its peers too. Its return on assets (profit as a share of everything the bank owns) was -0.3%, at the 3.2nd percentile nationally, which is unusually low, and at the 2.7th percentile among peers against a peer median of 1.2%, unusually low among its peers too.

Its Tier 1 risk-based capital ratio (core capital compared with assets weighted by how likely they are to lose value) was 10.0%, at the 1.9th percentile nationally, which is unusually low, and at the 2.8th percentile among peers against a peer median of 14.3%, unusually low among its peers too. Its total risk-based capital ratio (a broader capital measure on the same basis) was 11.3%, at the 2.6th percentile nationally, which is unusually low, and at the 3.7th percentile among peers against a peer median of 15.4%, unusually low among its peers too. Its volatile funding (money that can leave the bank quickly) was 25.6% of assets, at the 97.2nd percentile nationally, which is unusually high, and at the 97.0th percentile among peers against a peer median of 9.4%, unusually high among its peers too. Its uninsured deposits (balances above the government insurance limit) were 6.5% of deposits, at the 3.4th percentile nationally, which is unusually low, and at the 0.7th percentile among peers against a peer median of 26.0%, unusually low among its peers too.

Overall, 13 of the bank's ratios fell in the national top or bottom 10%, and 11 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | 1.8% | 99.1st (unusually high) | 0.1% | 99.1st | unusually high among its peers too |
| the Tier 1 risk-based capital ratio | 10.0% | 1.9th (unusually low) | 14.3% | 2.8th | unusually low among its peers too |
| the total risk-based capital ratio | 11.3% | 2.6th (unusually low) | 15.4% | 3.7th | unusually low among its peers too |
| volatile funding as a share of assets | 25.6% | 97.2nd (unusually high) | 9.4% | 97.0th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -3.1% | 2.9th (unusually low) | 11.7% | 2.4th | unusually low among its peers too |
| return on assets (profit as a share of assets) | -0.3% | 3.2nd (unusually low) | 1.2% | 2.7th | unusually low among its peers too |
| uninsured deposits as a share of deposits | 6.5% | 3.4th (unusually low) | 26.0% | 0.7th | unusually low among its peers too |
| loan-loss reserves as a share of loans | 2.6% | 96.3rd (unusually high) | 1.2% | 97.7th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 128.4% | 100% or more | yes |
| Total commercial real estate loans ÷ capital | 275.5% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 25.8% | 50% or more | no |

It crossed the construction line (100% or more of capital).
It did not cross the total commercial real estate line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

Looking back with hindsight, this bank falls in the open watchlist case: it was flagged, and our data does not record a failure. The fact sheet holds no data from after the as-of quarter, so this hindsight view cannot add anything to why it was flagged beyond the funding, bond-loss and loan-loss signals described above.

## What happened next

In hindsight, this fact sheet contains no later ranks, watchlist flags or reporting status for the bank. We therefore cannot say here how its rank moved or whether it kept reporting; the score history table added by code shows any later quarters that are available.

## Sources

- F1 · Bank name · n/a · Home State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2026-06-30 · 24 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.5% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 8.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 11.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F33 · Bank: construction loans as a share of loans · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F34 · National median: construction loans as a share of loans · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 36.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 16.9% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 2.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 6.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 19.6% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 47.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 25.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 6.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 19.6%; contribution to the score · 2026-06-30 · +0.808 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 6.4%; contribution to the score · 2026-06-30 · +0.734 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: core deposits as a share of assets, value 47.5%; contribution to the score · 2026-06-30 · +0.447 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F78 · Driver up #4: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2026-06-30 · +0.222 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F79 · Driver up #5: annualized provision for loan losses as a share of assets, value 1.8%; contribution to the score · 2026-06-30 · +0.218 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 10.0%; contribution to the score · 2026-06-30 · -0.748 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: loans 30-89 days past due, as a share of assets, value 0.2%; contribution to the score · 2026-06-30 · -0.488 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value -3.1%; contribution to the score · 2026-06-30 · -0.384 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 2.2%; contribution to the score · 2026-06-30 · -0.287 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F84 · Driver down #5: the Texas ratio (troubled assets against capital plus reserves), value 16.9%; contribution to the score · 2026-06-30 · -0.282 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -3.1% · data/features/fct_bank_features.parquet: return_on_equity
- F90 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 11.3% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 17.2% · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.384 · data/analyst/scores.parquet: feature return_on_equity contribution
- F94 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F95 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F96 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F97 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F99 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.218 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F100 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F101 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F102 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F103 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.5% · data/features/fct_bank_features.parquet: return_on_assets
- F105 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.030 · data/analyst/scores.parquet: feature return_on_assets contribution
- F106 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature return_on_assets contribution
- F107 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 36.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F108 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 29.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F109 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 34.3% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F112 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.154 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F113 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F114 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: allowance_to_loans
- F115 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F116 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 2.4% · data/features/fct_bank_features.parquet: allowance_to_loans
- F119 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.121 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F120 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F121 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 47.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F122 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 49.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F123 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 67.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F125 · Trend: core deposits as a share of assets, change over four quarters, in percentage points · 2026-06-30 · -10.4 pp · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F126 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.447 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F127 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F128 · Trend: ratios outside their own prior range · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F131 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F133 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 58.7% · data/analyst/scores.parquet: percentile
- F134 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F138 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F139 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.1st · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F140 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F141 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.1st · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F142 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F143 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F144 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F145 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 1.9th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F146 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F147 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 2.8th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F148 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-06-30 · 14.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F149 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F150 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 11.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F151 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 2.6th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F152 · Peers: the total risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F153 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 3.7th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F154 · Peers: the total risk-based capital ratio, peer median · 2026-06-30 · 15.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F155 · Peers: the total risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F156 · Peers: volatile funding as a share of assets, bank value at the as-of quarter · 2026-06-30 · 25.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F157 · Peers: volatile funding as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.2nd · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F158 · Peers: volatile funding as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F159 · Peers: volatile funding as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 97.0th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F160 · Peers: volatile funding as a share of assets, peer median · 2026-06-30 · 9.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F161 · Peers: volatile funding as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F162 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -3.1% · data/features/fct_bank_features.parquet: return_on_equity
- F163 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 2.9th · data/features/fct_bank_features.parquet: return_on_equity
- F164 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F165 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 2.4th · data/features/fct_bank_features.parquet: return_on_equity
- F166 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 11.7% · data/features/fct_bank_features.parquet: return_on_equity
- F167 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F168 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2026-06-30 · -0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F169 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 3.2nd · data/features/fct_bank_features.parquet: return_on_assets
- F170 · Peers: return on assets (profit as a share of assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F171 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2026-06-30 · 2.7th · data/features/fct_bank_features.parquet: return_on_assets
- F172 · Peers: return on assets (profit as a share of assets), peer median · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F173 · Peers: return on assets (profit as a share of assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F174 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 6.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F175 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 3.4th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F176 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F177 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 0.7th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F178 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 26.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F179 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F180 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: allowance_to_loans
- F181 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.3rd · data/features/fct_bank_features.parquet: allowance_to_loans
- F182 · Peers: loan-loss reserves as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: allowance_to_loans
- F183 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 97.7th · data/features/fct_bank_features.parquet: allowance_to_loans
- F184 · Peers: loan-loss reserves as a share of loans, peer median · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F185 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F187 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 13 · data/features/fct_bank_features.parquet
- F188 · Peers: those ratios also unusual among peers · 2026-06-30 · 11 · data/features/fct_bank_features.parquet
- F190 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
