---
cert: 232
name: "Solon State Bank"
as_of: 2026-06-30
rank: 32
n_banks: 4313
percentile: 99.28124275446325
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:57:27"
writer_model: "claude-opus-5-5"
checked: true
---

# Solon State Bank (cert 232)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Solon State Bank, a small Iowa bank, ranked 32 out of 4,313 banks on Canary's score, placing it in the 99.3rd percentile, where higher means riskier, and it was flagged on the watchlist. Its loan troubles stood far above the national median, with loans 90+ days past due or not accruing interest at 11.7% of loans against a median of 0.5%. Pointing the other way, its capital cushion was unusually thick, with equity at 22.8% of assets against a national median of 10.6%.

## Warning signs in the data

Credit quality is the main concern: loans 90+ days past due or not accruing interest (no longer paying interest) were 11.7% of loans, against a national median of 0.5%. Nonaccrual assets and foreclosed property (repossessed property) were 10.7% of assets, against a median of 0.3%, and loans 30-89 days past due were 1.4% of assets, against a median of 0.2%. The Texas ratio, which weighs troubled assets against capital plus reserves, was 43.9%, well above the national median of 2.9%. The bank set aside an annualized 2.9% of assets for expected loan losses, against a median of 0.1%, and wrote off 0.9% of loans net of recoveries, against a median of 0.0%; profit was thin, with return on assets at 0.0% against a median of 1.2%.

Capital points the other way: equity was 22.8% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 23.0% against a median of 11.0%. So the bank paired unusually heavy loan problems with an unusually large cushion to absorb losses.

On funding, loans were 93.8% of deposits against a median of 80.2%, brokered deposits (funds placed through middlemen) were 7.8% of deposits against a median of 0.0%, and cash was 2.0% of assets against a median of 6.2%. Uninsured deposits were 20.0% of deposits, a little below the median of 24.8%, and paper losses on bonds available for sale were 5.4% of equity, close to the median of 5.6%. On the separate commercial real estate concentration screens, the bank did not cross either line.

## Understanding the score

Solon State Bank ranked 32 out of 4,313 banks nationally as of 2026-06-30, in the 99.3rd percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks and held 87 banks that quarter.

The five features that pushed the score up most were the Texas ratio at 43.9%, loans 90+ days past due or not accruing interest at 11.7% of loans, the annualized provision for loan losses at 2.9% of assets, the efficiency ratio (operating costs as a share of revenue) at 39.6%, and losses on bonds available for sale at 5.4% of equity. The five that pushed it down most were the Tier 1 risk-based capital ratio (core capital against risk-weighted assets), the leverage ratio at 23.0%, return on equity (profit as a share of the owners' stake) at 0.2%, annualized interest expense at 1.5% of assets, and construction loans at 9.2% of loans.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 359 | 4,589 |  |
| 2024-12-31 | 222 | 4,560 |  |
| 2025-03-31 | 99 | 4,536 |  |
| 2025-06-30 | 904 | 4,494 |  |
| 2025-09-30 | 590 | 4,452 |  |
| 2025-12-31 | 606 | 4,411 |  |
| 2026-03-31 | 1,257 | 4,353 |  |
| 2026-06-30 | 32 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, Solon State Bank ranked 32 out of 4,313 banks nationally, placing it in the 99.3rd percentile, where higher means riskier. A year earlier, on 2025-06-30, it sat in the 79.9th percentile, so the model rated it riskier than a year earlier. Each ratio is compared with the bank's own prior 12 quarters, or with the same quarter in the prior 3 years for year-to-date ratios, and 10 of 28 ratios checked fell outside that prior range.

The annualized provision for loan losses (money set aside to cover expected bad loans), as a share of assets, was 2.9% against a prior range of 0.0% to 0.4%, and at +0.325 model log-odds units it pushed the score up. Nonaccrual assets and foreclosed property (loans no longer paying interest plus repossessed property) reached 10.7% of assets, above a prior range of 5.3% to 6.9%, and at +0.084 it pushed the score up. That ratio rose +5.4 pp in one quarter alone. Loan-loss reserves (the cushion held against bad loans) were 2.2% of loans, above a prior range of 0.5% to 1.0%, and at +0.068 this ratio pushed the score up.

Return on equity (profit as a share of the owners' stake) fell to 0.2%, well below its prior range of 9.3% to 11.5%, yet at -0.289 the model says it pushed the score down. Return on assets dropped to 0.0%, below its prior range of 1.7% to 2.4%, but at -0.103 it also pushed the score down rather than up. Federal Home Loan Bank borrowings (loans from a government-sponsored lender to banks) fell to 2.4% of assets, below a prior range of 4.3% to 7.9%, yet at -0.020 this had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 0.2% | 9.3% to 11.5% | same quarter, prior 3 years | n/a | -11.3 pp | -0.289 | pushed the score down |
| annualized provision for loan losses as a share of assets | 2.9% | 0.0% to 0.4% | same quarter, prior 3 years | n/a | +2.5 pp | +0.325 | pushed the score up |
| nonaccrual assets and foreclosed property, as a share of assets | 10.7% | 5.3% to 6.9% | prior 12 quarters | +5.4 pp | +5.3 pp | +0.084 | pushed the score up |
| return on assets (profit as a share of assets) | 0.0% | 1.7% to 2.4% | same quarter, prior 3 years | n/a | -2.4 pp | -0.103 | pushed the score down |
| loan-loss reserves as a share of loans | 2.2% | 0.5% to 1.0% | prior 12 quarters | +1.5 pp | +1.3 pp | +0.068 | pushed the score up |
| Federal Home Loan Bank borrowings as a share of assets | 2.4% | 4.3% to 7.9% | prior 12 quarters | -2.3 pp | -3.5 pp | -0.020 | little effect on the score |

10 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

On Canary's score, the bank ranked 32 out of 4,313 banks nationally in the quarter ending 2026-06-30, near the very top of the list. Nonaccrual assets and foreclosed property (loans that have stopped paying interest, plus property taken back from borrowers) were 10.7% of assets, at the 99.9th national percentile, which is unusually high, and at the 99.8th percentile among its peers against a peer median of 0.3%, which is unusually high among its peers too. Loans 90+ days past due or not accruing interest were 11.7% of loans, at the 99.7th national percentile, which is unusually high, and at the 99.8th percentile among its peers against a peer median of 0.4%, which is unusually high among its peers too. The annualized provision for loan losses (money set aside to cover expected bad loans) was 2.9% of assets, at the 99.5th national percentile, which is unusually high, and at the 99.5th percentile among its peers against a peer median of 0.1%, which is unusually high among its peers too. The Texas ratio (troubled assets against capital plus reserves) was 43.9%, at the 99.1st national percentile, which is unusually high, and at the 99.0th percentile among its peers against a peer median of 3.0%, which is unusually high among its peers too. Annualized loan write-offs, net of recoveries (loans written off as uncollectable, minus amounts later recovered), were 0.9% of loans, at the 96.7th national percentile, which is unusually high, and at the 97.1st percentile among its peers against a peer median of 0.0%, which is unusually high among its peers too.

Return on equity (profit as a share of equity) was 0.2%, at the 4.4th national percentile, which is unusually low, and at the 4.3rd percentile among its peers against a peer median of 11.7%, which is unusually low among its peers too. Equity as a share of assets (the owners' cushion against losses) was 22.8%, at the 95.5th national percentile, which is unusually high, and at the 98.3rd percentile among its peers against a peer median of 10.2%, which is unusually high among its peers too. The leverage ratio (core capital as a share of average assets) was 23.0%, at the 95.5th national percentile, which is unusually high, and at the 98.3rd percentile among its peers against a peer median of 10.8%, which is unusually high among its peers too.

Overall, 12 of the bank's ratios sat in the national top or bottom 10%, and 12 of those were also unusual among its peers, pairing very high loan troubles and weak profit with an unusually thick capital cushion.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| nonaccrual assets and foreclosed property, as a share of assets | 10.7% | 99.9th (unusually high) | 0.3% | 99.8th | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 11.7% | 99.7th (unusually high) | 0.4% | 99.8th | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 2.9% | 99.5th (unusually high) | 0.1% | 99.5th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 43.9% | 99.1st (unusually high) | 3.0% | 99.0th | unusually high among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.9% | 96.7th (unusually high) | 0.0% | 97.1st | unusually high among its peers too |
| return on equity (profit as a share of equity) | 0.2% | 4.4th (unusually low) | 11.7% | 4.3rd | unusually low among its peers too |
| equity as a share of assets | 22.8% | 95.5th (unusually high) | 10.2% | 98.3rd | unusually high among its peers too |
| the leverage ratio (core capital as a share of average assets) | 23.0% | 95.5th (unusually high) | 10.8% | 98.3rd | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 25.5% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 111.9% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 66.7% | 50% or more | yes |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight: this bank is on the watchlist, and Canary's data holds no later quarters to show how its situation developed. Its place on the list therefore rests on the as-of figures described above, mainly its heavy loan problems, rather than on any later event.

## What happened next

In hindsight: the fact sheet contains no data after the as-of quarter, so there are no later ranks, flags or reporting status to describe yet. Later quarters will show whether the bank stays on the watchlist and keeps reporting.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 32 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.3% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 22.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 23.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 11.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 10.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 1.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F25 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F26 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F27 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F28 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 43.9% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: loans as a share of deposits · 2026-06-30 · 93.8% · data/features/fct_bank_features.parquet: loans_to_deposits
- F46 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 20.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 7.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 43.9%; contribution to the score · 2026-06-30 · +0.909 · data/analyst/scores.parquet: feature texas_ratio contribution
- F72 · Driver up #2: loans 90+ days past due or not accruing interest, as a share of loans, value 11.7%; contribution to the score · 2026-06-30 · +0.875 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F73 · Driver up #3: annualized provision for loan losses as a share of assets, value 2.9%; contribution to the score · 2026-06-30 · +0.325 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F74 · Driver up #4: the efficiency ratio (operating costs as a share of revenue), value 39.6%; contribution to the score · 2026-06-30 · +0.136 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F75 · Driver up #5: losses on bonds available for sale, as a share of equity, value 5.4%; contribution to the score · 2026-06-30 · +0.120 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.809 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: the leverage ratio (core capital as a share of average assets), value 23.0%; contribution to the score · 2026-06-30 · -0.338 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F78 · Driver down #3: return on equity (profit as a share of equity), value 0.2%; contribution to the score · 2026-06-30 · -0.289 · data/analyst/scores.parquet: feature return_on_equity contribution
- F79 · Driver down #4: annualized interest expense as a share of assets, value 1.5%; contribution to the score · 2026-06-30 · -0.283 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #5: construction loans as a share of loans, value 9.2%; contribution to the score · 2026-06-30 · -0.247 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F81 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: return_on_equity
- F82 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 9.3% · data/features/fct_bank_features.parquet: return_on_equity
- F83 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 11.5% · data/features/fct_bank_features.parquet: return_on_equity
- F85 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.289 · data/analyst/scores.parquet: feature return_on_equity contribution
- F86 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F87 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F88 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F89 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F91 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.325 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F92 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F93 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2026-06-30 · 10.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F94 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 5.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F95 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 6.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F96 · Trend: nonaccrual assets and foreclosed property, as a share of assets, change over one quarter, in percentage points · 2026-06-30 · +5.4 pp · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F98 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.084 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F99 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F100 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: return_on_assets
- F101 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 1.7% · data/features/fct_bank_features.parquet: return_on_assets
- F102 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 2.4% · data/features/fct_bank_features.parquet: return_on_assets
- F104 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.103 · data/analyst/scores.parquet: feature return_on_assets contribution
- F105 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F106 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F107 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F108 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F111 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.068 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F112 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F113 · Trend: Federal Home Loan Bank borrowings as a share of assets, value at the as-of quarter · 2026-06-30 · 2.4% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F114 · Trend: Federal Home Loan Bank borrowings as a share of assets, lowest value in the comparison window · n/a · 4.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F115 · Trend: Federal Home Loan Bank borrowings as a share of assets, highest value in the comparison window · n/a · 7.9% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F118 · Trend: Federal Home Loan Bank borrowings as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.020 · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F119 · Trend: Federal Home Loan Bank borrowings as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F120 · Trend: ratios outside their own prior range · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F122 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F123 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F124 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F125 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 79.9% · data/analyst/scores.parquet: percentile
- F126 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F130 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 10.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F131 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F132 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F133 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F134 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F135 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F136 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 11.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F137 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F138 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F139 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F140 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F141 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F142 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F143 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F144 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F145 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F146 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F147 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F148 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 43.9% · data/features/fct_bank_features.parquet: texas_ratio
- F149 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.1st · data/features/fct_bank_features.parquet: texas_ratio
- F150 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F151 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: texas_ratio
- F152 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: texas_ratio
- F153 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F154 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F155 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.7th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F156 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F157 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 97.1st · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F158 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F159 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F160 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: return_on_equity
- F161 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 4.4th · data/features/fct_bank_features.parquet: return_on_equity
- F162 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F163 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 4.3rd · data/features/fct_bank_features.parquet: return_on_equity
- F164 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 11.7% · data/features/fct_bank_features.parquet: return_on_equity
- F165 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F166 · Peers: equity as a share of assets, bank value at the as-of quarter · 2026-06-30 · 22.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F167 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 95.5th · data/features/fct_bank_features.parquet: equity_to_assets
- F168 · Peers: equity as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: equity_to_assets
- F169 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.3rd · data/features/fct_bank_features.parquet: equity_to_assets
- F170 · Peers: equity as a share of assets, peer median · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F171 · Peers: equity as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F172 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 23.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F173 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 95.5th · data/features/fct_bank_features.parquet: leverage_ratio
- F174 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: leverage_ratio
- F175 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 98.3rd · data/features/fct_bank_features.parquet: leverage_ratio
- F176 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 10.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F177 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F179 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 12 · data/features/fct_bank_features.parquet
- F180 · Peers: those ratios also unusual among peers · 2026-06-30 · 12 · data/features/fct_bank_features.parquet
- F182 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
