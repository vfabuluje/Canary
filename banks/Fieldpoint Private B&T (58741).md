---
cert: 58741
name: "Fieldpoint Private B&T"
as_of: 2026-06-30
rank: 39
n_banks: 4313
percentile: 99.11894273127754
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:58:04"
writer_model: "claude-opus-5-5"
checked: true
---

# Fieldpoint Private B&T (cert 58741)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Fieldpoint Private B&T ranked 39 out of 4,313 FDIC-insured banks on Canary's risk score, placing it in the 99.1st percentile and on the watchlist. Its capital cushion, meaning the bank's own funds that absorb losses, is thin, with a leverage ratio of 6.6% against a national median of 11.0%. It also relies heavily on brokered deposits, which is money placed with the bank through outside brokers, at 46.5% of deposits, and it was unprofitable, with a return on assets of -0.3%. The separate commercial real estate concentration screen did not flag the bank, since it did not cross either line.

## Warning signs in the data

Capital is well below typical levels: equity was 6.5% of assets against a national median of 10.6%. Its Tier 1 risk-based capital ratio, core capital measured against assets weighted by their risk of loss, was 10.1% against a median of 14.6%, and its total risk-based capital ratio was 11.2% against 15.8%. Credit quality is weaker than most banks: loans 90 or more days past due or not accruing interest were 1.9% of loans against a median of 0.5%. Its Texas ratio, which weighs troubled assets against capital plus reserves, was 19.2% against a median of 2.9%, while loan-loss reserves were 1.0% of loans against 1.2%. Its provision for loan losses, the money set aside for expected bad loans, was -0.2% of assets against a median of 0.1%, meaning it reduced rather than added to that cushion.

Funding is the biggest outlier: brokered deposits were 46.5% of deposits against a national median of 0.0%, and core deposits, the steadier everyday deposit base, were 46.2% of assets against 75.5%. Interest expense was 3.0% of assets against a median of 1.6%, and deposits changed by -9.3% over the past four quarters against a median of 4.2%. Some funding figures point the other way: uninsured deposits were 13.5% of deposits against a median of 24.8%, and cash was 10.3% of assets against 6.2%.

Unrealized losses on bonds available for sale, bonds the bank could sell at market prices, equaled 14.3% of equity against a national median of 5.6%. Commercial real estate loans were 28.9% of loans against a median of 23.6%, somewhat above typical, though the separate concentration screen was not crossed.

## Understanding the score

Fieldpoint Private B&T ranked 39 out of 4,313 banks as of 2026-06-30, which puts it in the 99.1st percentile on a scale where higher means riskier. It was flagged on the watchlist, one of 87 banks that quarter, a list that holds about 2% of banks.

Five features pushed the score up most: brokered deposits at 46.5% of deposits, core deposits at 46.2% of assets, losses on bonds available for sale at 14.3% of equity, interest expense at 3.0% of assets, and asset growth over the past four quarters of -19.7%. Brokered deposits were by far the largest of these, contributing +1.256 to the score.

Five features pushed the score down most: the Tier 1 risk-based capital ratio at 10.1%, return on equity at -4.7%, recently overdue loans (those behind on payments but not yet seriously delinquent) at 0.5% of assets, construction loans at 2.6% of loans, and the efficiency ratio at 119.0%. Some of these look weak next to national medians, yet the model still counted them as lowering the score, which reflects how it weighs them against its training data rather than a judgment that they are healthy.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 6 | 4,589 | ▲ watchlist |
| 2024-12-31 | 10 | 4,560 | ▲ watchlist |
| 2025-03-31 | 6 | 4,536 | ▲ watchlist |
| 2025-06-30 | 7 | 4,494 | ▲ watchlist |
| 2025-09-30 | 10 | 4,452 | ▲ watchlist |
| 2025-12-31 | 15 | 4,411 | ▲ watchlist |
| 2026-03-31 | 15 | 4,353 | ▲ watchlist |
| 2026-06-30 | 39 | 4,313 | ▲ watchlist |

## How its ratios moved

Fieldpoint Private B&T ranked 39 out of 4,313 banks nationally, placing it in the 99.1st percentile, where a higher percentile means a higher risk score. A year earlier it sat in the 99.9th percentile, and the model rates it about the same as a year earlier. Of 30 ratios checked against the bank's own history, 10 were outside their prior range, which for most ratios means the prior 12 quarters. Each ratio's contribution is shown in model log-odds units, an internal scale where a positive number pushes the score up and a negative number pushes it down.

Net interest margin (the spread the bank earns on lending and investing) was 2.1%, above its prior range of 0.8% to 1.2%, and its contribution of -0.060 pushed the score down. Interest expense as a share of assets was 3.0%, below its prior range of 3.6% to 4.0%, yet its contribution of +0.359 pushed the score up. Return on assets (profit as a share of assets) was -0.3%, above its prior range of -2.1% to -0.9%, but despite sitting outside that range its contribution of -0.047 had little effect on the score. Return on equity (profit as a share of the owners' stake) was -4.7%, above its prior range of -38.3% to -14.1%, and its contribution of -0.408 pushed the score down.

Securities (bonds and similar investments) made up 14.4% of assets, above the prior range of 8.9% to 13.1%, and despite being outside that range the contribution of -0.094 pushed the score down. Borrowings from the Federal Home Loan Bank, a government-sponsored lender to banks, were 2.3% of assets, below the prior range of 5.8% to 28.4%, but despite that the contribution of -0.003 had little effect on the score. Those borrowings fell by -10.8 pp over four quarters, while securities rose by +3.2 pp over the same span.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| net interest margin (the spread earned on lending and investing) | 2.1% | 0.8% to 1.2% | same quarter, prior 3 years | n/a | +0.9 pp | -0.060 | pushed the score down |
| annualized interest expense as a share of assets | 3.0% | 3.6% to 4.0% | same quarter, prior 3 years | n/a | -0.9 pp | +0.359 | pushed the score up |
| return on assets (profit as a share of assets) | -0.3% | -2.1% to -0.9% | same quarter, prior 3 years | n/a | +1.8 pp | -0.047 | little effect on the score |
| return on equity (profit as a share of equity) | -4.7% | -38.3% to -14.1% | same quarter, prior 3 years | n/a | +33.6 pp | -0.408 | pushed the score down |
| securities as a share of assets | 14.4% | 8.9% to 13.1% | prior 12 quarters | +3.2 pp | +3.2 pp | -0.094 | pushed the score down |
| Federal Home Loan Bank borrowings as a share of assets | 2.3% | 5.8% to 28.4% | prior 12 quarters | -4.3 pp | -10.8 pp | -0.003 | little effect on the score |

10 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

Fieldpoint Private B&T's assets shrank, with asset growth over the past four quarters of -19.7%, at the 0.4th national percentile, which is unusually low, and at the 0.2nd percentile among its peers against a peer median of 4.8%, unusually low among its peers too. Brokered deposits (money placed with the bank through outside brokers rather than gathered directly) made up 46.5% of its deposits, at the 99.4th national percentile, which is unusually high, and at the 99.5th percentile among its peers against a peer median of 0.0%, unusually high among its peers too. Its annualized interest expense (what it pays to borrow and hold deposits) was 3.0% of assets, at the 98.6th national percentile, which is unusually high, and at the 98.6th percentile among its peers against a peer median of 1.7%, unusually high among its peers too. Its efficiency ratio (operating costs as a share of revenue, where lower is leaner) was 119.0%, at the 98.3rd national percentile, which is unusually high, and at the 99.3rd percentile among its peers against a peer median of 63.7%, unusually high among its peers too.

Its leverage ratio (core capital, the bank's own loss-absorbing funds, as a share of average assets) was 6.6%, at the 0.8th national percentile, which is unusually low, and at the 0.3rd percentile among its peers against a peer median of 10.8%, unusually low among its peers too. Its Tier 1 risk-based capital ratio (core capital measured against assets weighted by their exposure to loss) was 10.1%, at the 2.1st national percentile, which is unusually low, and at the 3.1st percentile among its peers against a peer median of 14.3%, unusually low among its peers too. Its total risk-based capital ratio (a broader capital measure on the same weighted basis) was 11.2%, at the 2.2nd national percentile, which is unusually low, and at the 3.2nd percentile among its peers against a peer median of 15.4%, unusually low among its peers too. Its annualized provision for loan losses (money set aside for expected bad loans) was -0.2% of assets, a negative figure, at the 0.9th national percentile, which is unusually low, and at the 1.0th percentile among its peers against a peer median of 0.1%, unusually low among its peers too.

Overall, 15 of the bank's ratios sit in the national top or bottom 10%, and 15 of those are also unusual among its peers, so its unusual profile stands out against similar banks as well as nationally.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| asset growth over the past four quarters | -19.7% | 0.4th (unusually low) | 4.8% | 0.2nd | unusually low among its peers too |
| brokered deposits as a share of deposits | 46.5% | 99.4th (unusually high) | 0.0% | 99.5th | unusually high among its peers too |
| the leverage ratio (core capital as a share of average assets) | 6.6% | 0.8th (unusually low) | 10.8% | 0.3rd | unusually low among its peers too |
| annualized provision for loan losses as a share of assets | -0.2% | 0.9th (unusually low) | 0.1% | 1.0th | unusually low among its peers too |
| annualized interest expense as a share of assets | 3.0% | 98.6th (unusually high) | 1.7% | 98.6th | unusually high among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 119.0% | 98.3rd (unusually high) | 63.7% | 99.3rd | unusually high among its peers too |
| the Tier 1 risk-based capital ratio | 10.1% | 2.1st (unusually low) | 14.3% | 3.1st | unusually low among its peers too |
| the total risk-based capital ratio | 11.2% | 2.2nd (unusually low) | 15.4% | 3.2nd | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 24.1% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 257.7% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -61.7% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

Looking back with hindsight, the fact sheet for this memo contains no data from after the as-of quarter. So the reasons this bank sits on the watchlist are the as-of figures described above, chiefly its heavy reliance on brokered deposits, thin capital and weak profits, and no later information can be added here.

## What happened next

With hindsight, the fact sheet includes no later ranks, watchlist flags or reporting status for this bank. We therefore cannot say from this data how its rank moved afterward or whether it still reports to the FDIC.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2026-06-30 · 39 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.1% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 6.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 6.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 10.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 11.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 1.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · -0.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 28.9% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 19.2% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 13.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 46.5% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 46.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 10.3% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 14.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -9.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 46.5%; contribution to the score · 2026-06-30 · +1.256 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: core deposits as a share of assets, value 46.2%; contribution to the score · 2026-06-30 · +0.377 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F77 · Driver up #3: losses on bonds available for sale, as a share of equity, value 14.3%; contribution to the score · 2026-06-30 · +0.374 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F78 · Driver up #4: annualized interest expense as a share of assets, value 3.0%; contribution to the score · 2026-06-30 · +0.359 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F79 · Driver up #5: asset growth over the past four quarters, value -19.7%; contribution to the score · 2026-06-30 · +0.110 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 10.1%; contribution to the score · 2026-06-30 · -0.655 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value -4.7%; contribution to the score · 2026-06-30 · -0.408 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: loans 30-89 days past due, as a share of assets, value 0.5%; contribution to the score · 2026-06-30 · -0.323 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F83 · Driver down #4: construction loans as a share of loans, value 2.6%; contribution to the score · 2026-06-30 · -0.318 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F84 · Driver down #5: the efficiency ratio (operating costs as a share of revenue), value 119.0%; contribution to the score · 2026-06-30 · -0.289 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F89 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 2.1% · data/features/fct_bank_features.parquet: net_interest_margin
- F90 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: net_interest_margin
- F91 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F93 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.060 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F94 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F95 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F96 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 3.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F97 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 4.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F99 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.359 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F100 · Trend: annualized interest expense as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F101 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F102 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -2.1% · data/features/fct_bank_features.parquet: return_on_assets
- F103 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F105 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.047 · data/analyst/scores.parquet: feature return_on_assets contribution
- F106 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature return_on_assets contribution
- F107 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -4.7% · data/features/fct_bank_features.parquet: return_on_equity
- F108 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -38.3% · data/features/fct_bank_features.parquet: return_on_equity
- F109 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -14.1% · data/features/fct_bank_features.parquet: return_on_equity
- F111 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.408 · data/analyst/scores.parquet: feature return_on_equity contribution
- F112 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F113 · Trend: securities as a share of assets, value at the as-of quarter · 2026-06-30 · 14.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F114 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 8.9% · data/features/fct_bank_features.parquet: securities_to_assets
- F115 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 13.1% · data/features/fct_bank_features.parquet: securities_to_assets
- F117 · Trend: securities as a share of assets, change over four quarters, in percentage points · 2026-06-30 · +3.2 pp · data/features/fct_bank_features.parquet: securities_to_assets
- F118 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.094 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F119 · Trend: securities as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature securities_to_assets contribution
- F120 · Trend: Federal Home Loan Bank borrowings as a share of assets, value at the as-of quarter · 2026-06-30 · 2.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F121 · Trend: Federal Home Loan Bank borrowings as a share of assets, lowest value in the comparison window · n/a · 5.8% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F122 · Trend: Federal Home Loan Bank borrowings as a share of assets, highest value in the comparison window · n/a · 28.4% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F124 · Trend: Federal Home Loan Bank borrowings as a share of assets, change over four quarters, in percentage points · 2026-06-30 · -10.8 pp · data/features/fct_bank_features.parquet: fhlb_to_assets
- F125 · Trend: Federal Home Loan Bank borrowings as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.003 · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F126 · Trend: Federal Home Loan Bank borrowings as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F127 · Trend: ratios outside their own prior range · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F129 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F130 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F132 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 99.9% · data/analyst/scores.parquet: percentile
- F133 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F137 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -19.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F138 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.4th · data/features/fct_bank_features.parquet: asset_growth_4q
- F139 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F140 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 0.2nd · data/features/fct_bank_features.parquet: asset_growth_4q
- F141 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F142 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F143 · Peers: brokered deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 46.5% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F144 · Peers: brokered deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.4th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F145 · Peers: brokered deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: brokered_to_deposits
- F146 · Peers: brokered deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F147 · Peers: brokered deposits as a share of deposits, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F148 · Peers: brokered deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: brokered_to_deposits
- F149 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 6.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F150 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.8th · data/features/fct_bank_features.parquet: leverage_ratio
- F151 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F152 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 0.3rd · data/features/fct_bank_features.parquet: leverage_ratio
- F153 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 10.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F154 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F155 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · -0.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F156 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.9th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F157 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F158 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 1.0th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F159 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F160 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F161 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F162 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F163 · Peers: annualized interest expense as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F164 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.6th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F165 · Peers: annualized interest expense as a share of assets, peer median · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F166 · Peers: annualized interest expense as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F167 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-06-30 · 119.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F168 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-06-30 · 98.3rd · data/features/fct_bank_features.parquet: efficiency_ratio
- F169 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F170 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: efficiency_ratio
- F171 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-06-30 · 63.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F172 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F173 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 10.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F174 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 2.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F175 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F176 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 3.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F177 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-06-30 · 14.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F178 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F179 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 11.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F180 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 2.2nd · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F181 · Peers: the total risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F182 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 3.2nd · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F183 · Peers: the total risk-based capital ratio, peer median · 2026-06-30 · 15.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F184 · Peers: the total risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F186 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 15 · data/features/fct_bank_features.parquet
- F187 · Peers: those ratios also unusual among peers · 2026-06-30 · 15 · data/features/fct_bank_features.parquet
- F189 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
