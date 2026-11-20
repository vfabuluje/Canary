---
cert: 5753
name: "Fidelity Bank"
as_of: 2026-06-30
rank: 34
n_banks: 4313
percentile: 99.23487131926733
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:57:27"
writer_model: "claude-opus-5-5"
checked: true
---

# Fidelity Bank (cert 5753)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Fidelity Bank ranked 34 out of 4,313 FDIC-insured banks on Canary's risk score, placing it in the 99.2nd percentile, where higher means riskier, and it was on the model's watchlist. Its capital cushion, meaning the owners' own money that absorbs losses, was thin: equity was 7.3% of assets against a national median of 10.6%. The largest single push on the score came from paper losses on bonds available for sale, equal to 34.3% of equity against a national median of 5.6%. The bank also relied heavily on construction lending and on funding that can leave quickly, and the separate real-estate concentration check found it crossed both supervisory lines.

## Warning signs in the data

Capital was well below typical levels on every measure shown. Equity was 7.3% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 8.0% against 11.0%. The Tier 1 risk-based capital ratio, which weighs assets by their riskiness, was 11.0% against a median of 14.6%, and the total risk-based capital ratio was 11.8% against 15.8%.

On credit quality, loans 90 or more days late or no longer paying interest were 0.8% of loans, above the national median of 0.5%, and the Texas ratio (troubled assets against capital plus reserves) was 7.5% against 2.9%. Loan-loss reserves, money set aside for loans that may go bad, were 0.6% of loans, about half the national median of 1.2%. Construction loans were 32.4% of loans, far above the national median of 5.3%. These signals point different ways: problem-loan levels were above the median yet still small in absolute terms, and the model treated them as lowering the score, while the real-estate concentration check flagged the bank's construction and commercial real estate lending.

Funding leaned on less stable sources: brokered deposits, placed through middlemen, were 13.3% of deposits against a national median of 0.0%, and Federal Home Loan Bank borrowings were 8.1% of assets against 0.2%. Volatile funding was 24.3% of assets against a median of 9.0%, while cash was only 1.8% of assets against 6.2%. Unrealized losses on bonds available for sale equaled 34.3% of equity, well above the national median of 5.6%, and profits were weak, with return on assets of 0.3% against 1.2%.

## Understanding the score

At 2026-06-30 Fidelity Bank ranked 34 of 4,313 banks, the 99.2nd percentile on a 0 to 100 scale where higher means riskier. The watchlist covers the top 2% of banks by score; 87 banks were on it that quarter, and this bank was flagged.

The biggest push up came from losses on bonds available for sale, at 34.3% of equity, contributing +2.103. Next came brokered deposits at 13.3% of deposits, contributing +0.283, and interest expense at 2.3% of assets, contributing +0.203. Commercial real estate loans at 9.8% of loans added +0.115, and construction loans at 32.4% of loans added +0.079.

Pulling the score down most was the Texas ratio at 7.5%, contributing -0.772, followed by loans 90+ days past due or not accruing interest at 0.8% of loans, contributing -0.389. The Tier 1 risk-based capital ratio at 11.0% contributed -0.388, the efficiency ratio (operating costs as a share of revenue) at 92.0% contributed -0.359, and nonaccrual assets and foreclosed property at 0.6% of assets contributed -0.359.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 193 | 4,589 |  |
| 2024-12-31 | 156 | 4,560 |  |
| 2025-03-31 | 233 | 4,536 |  |
| 2025-06-30 | 90 | 4,494 | ▲ watchlist |
| 2025-09-30 | 34 | 4,452 | ▲ watchlist |
| 2025-12-31 | 33 | 4,411 | ▲ watchlist |
| 2026-03-31 | 40 | 4,353 | ▲ watchlist |
| 2026-06-30 | 34 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, Fidelity Bank held national rank 34 out of 4,313 banks, the 99.2nd percentile on a scale where higher means riskier. A year earlier, on 2025-06-30, it sat at the 98.0th percentile, and the model rated it riskier than a year earlier. Of 30 ratios compared with their own prior range, mostly the prior 12 quarters, 9 were outside that range at the as-of quarter.

The efficiency ratio (operating costs as a share of revenue, where lower means leaner) was 92.0%, below its prior range of 94.5% to 101.9%, yet despite being outside its range it pushed the score down, with a contribution of -0.359 model log-odds units (positive values push the score up). Return on equity (profit as a share of the owners' stake) was 4.3%, above its prior range of -11.4% to 1.1%, and despite being outside its range it pushed the score down, contributing -0.330. Return on assets (profit as a share of assets) was 0.3%, above its prior range of -0.7% to 0.1%, and it also pushed the score down despite being outside its range, contributing -0.115.

Construction loans made up 32.4% of loans, above their prior range of 23.9% to 31.2% after a rise of +5.9 pp over four quarters, and this ratio pushed the score up, contributing +0.079. Loans as a share of deposits reached 88.4%, above the prior range of 69.8% to 86.7%, yet despite being outside its range it pushed the score down, contributing -0.081. Cash as a share of assets was 1.8%, below its prior range of 2.0% to 4.9%, but despite being outside its range it had little effect on the score, contributing -0.049.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 92.0% | 94.5% to 101.9% | same quarter, prior 3 years | n/a | -3.6 pp | -0.359 | pushed the score down |
| return on equity (profit as a share of equity) | 4.3% | -11.4% to 1.1% | same quarter, prior 3 years | n/a | +3.2 pp | -0.330 | pushed the score down |
| return on assets (profit as a share of assets) | 0.3% | -0.7% to 0.1% | same quarter, prior 3 years | n/a | +0.2 pp | -0.115 | pushed the score down |
| construction loans as a share of loans | 32.4% | 23.9% to 31.2% | prior 12 quarters | +1.7 pp | +5.9 pp | +0.079 | pushed the score up |
| loans as a share of deposits | 88.4% | 69.8% to 86.7% | prior 12 quarters | +2.4 pp | +8.0 pp | -0.081 | pushed the score down |
| cash as a share of assets | 1.8% | 2.0% to 4.9% | prior 12 quarters | -0.3 pp | -1.3 pp | -0.049 | little effect on the score |

9 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

Construction loans make up 32.4% of the bank's loans, which is unusually high nationally at the 99.6th percentile, and it sits at the 99.3rd percentile among its peers against a peer median of 8.2%, unusually high among its peers too. Funding that can leave quickly, called volatile funding, equals 24.3% of assets, unusually high nationally at the 96.4th percentile, and at the 96.2nd percentile among peers versus a peer median of 9.4%, unusually high among its peers too. The efficiency ratio, operating costs as a share of revenue, is 92.0%, unusually high nationally at the 94.5th percentile, and at the 95.0th percentile among peers against a peer median of 63.7%, unusually high among its peers too. Losses on bonds available for sale, meaning bonds the bank could sell that are worth less than it paid, equal 34.3% of equity, unusually high nationally at the 92.4th percentile, and at the 93.0th percentile among peers versus a peer median of 5.4%, unusually high among its peers too.

On the cushion side, the leverage ratio, core capital (the bank's own money) as a share of average assets, is 8.0%, unusually low nationally at the 2.9th percentile, and at the 2.0th percentile among peers against a peer median of 10.8%, unusually low among its peers too. The total risk-based capital ratio, capital measured against assets weighted by the type of each asset, stands at 11.8%, unusually low nationally at the 5.5th percentile, and at the 6.7th percentile among peers versus a peer median of 15.4%, unusually low among its peers too. Loan-loss reserves, money set aside to cover loans that may go bad, equal 0.6% of loans, unusually low nationally at the 6.5th percentile, and at the 2.7th percentile among peers against a peer median of 1.2%, unusually low among its peers too. Equity as a share of assets is 7.3%, unusually low nationally at the 6.9th percentile, and at the 7.1st percentile among peers versus a peer median of 10.2%, unusually low among its peers too.

Overall, 12 of the bank's ratios fall in the national top or bottom 10%, and all 12 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| construction loans as a share of loans | 32.4% | 99.6th (unusually high) | 8.2% | 99.3rd | unusually high among its peers too |
| the leverage ratio (core capital as a share of average assets) | 8.0% | 2.9th (unusually low) | 10.8% | 2.0th | unusually low among its peers too |
| volatile funding as a share of assets | 24.3% | 96.4th (unusually high) | 9.4% | 96.2nd | unusually high among its peers too |
| the total risk-based capital ratio | 11.8% | 5.5th (unusually low) | 15.4% | 6.7th | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 92.0% | 94.5th (unusually high) | 63.7% | 95.0th | unusually high among its peers too |
| loan-loss reserves as a share of loans | 0.6% | 6.5th (unusually low) | 1.2% | 2.7th | unusually low among its peers too |
| equity as a share of assets | 7.3% | 6.9th (unusually low) | 10.2% | 7.1st | unusually low among its peers too |
| losses on bonds available for sale, as a share of equity | 34.3% | 92.4th (unusually high) | 5.4% | 93.0th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 284.7% | 100% or more | yes |
| Total commercial real estate loans ÷ capital | 334.4% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | 88.9% | 50% or more | yes |

It crossed both lines: construction loans and total commercial real estate loans.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

Hindsight: this is an open watchlist case, meaning the bank was flagged by the model and our records do not show it as having failed. The fact sheet for this memo contains no data from after the as-of quarter, so it cannot confirm or rule out how the bank's risks played out. The flag itself rests on the readings described above, chiefly large paper losses on bonds, thin capital, reliance on brokered and other volatile funding, and heavy construction lending.

## What happened next

Hindsight: the fact sheet includes no ranks, flags or filings for quarters after the as-of date. Because of that, this memo cannot say whether the bank stayed on the watchlist, moved in the rankings, or continued reporting; the score history table added by code shows any later quarters that are available.

## Sources

- F1 · Bank name · n/a · Fidelity Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2026-06-30 · 34 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.2% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 11.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F33 · Bank: construction loans as a share of loans · 2026-06-30 · 32.4% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F34 · National median: construction loans as a share of loans · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 7.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 13.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 8.1% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 24.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 34.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: losses on bonds available for sale, as a share of equity, value 34.3%; contribution to the score · 2026-06-30 · +2.103 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F76 · Driver up #2: brokered deposits as a share of deposits, value 13.3%; contribution to the score · 2026-06-30 · +0.283 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F77 · Driver up #3: annualized interest expense as a share of assets, value 2.3%; contribution to the score · 2026-06-30 · +0.203 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F78 · Driver up #4: commercial real estate loans as a share of loans, value 9.8%; contribution to the score · 2026-06-30 · +0.115 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F79 · Driver up #5: construction loans as a share of loans, value 32.4%; contribution to the score · 2026-06-30 · +0.079 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 7.5%; contribution to the score · 2026-06-30 · -0.772 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: loans 90+ days past due or not accruing interest, as a share of loans, value 0.8%; contribution to the score · 2026-06-30 · -0.389 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F82 · Driver down #3: the Tier 1 risk-based capital ratio, value 11.0%; contribution to the score · 2026-06-30 · -0.388 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F83 · Driver down #4: the efficiency ratio (operating costs as a share of revenue), value 92.0%; contribution to the score · 2026-06-30 · -0.359 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F84 · Driver down #5: nonaccrual assets and foreclosed property, as a share of assets, value 0.6%; contribution to the score · 2026-06-30 · -0.359 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F89 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 92.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F90 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 94.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F91 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 101.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.359 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F94 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F95 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 4.3% · data/features/fct_bank_features.parquet: return_on_equity
- F96 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -11.4% · data/features/fct_bank_features.parquet: return_on_equity
- F97 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: return_on_equity
- F99 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.330 · data/analyst/scores.parquet: feature return_on_equity contribution
- F100 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F101 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F102 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F103 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F105 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.115 · data/analyst/scores.parquet: feature return_on_assets contribution
- F106 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F107 · Trend: construction loans as a share of loans, value at the as-of quarter · 2026-06-30 · 32.4% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F108 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 23.9% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F109 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 31.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F111 · Trend: construction loans as a share of loans, change over four quarters, in percentage points · 2026-06-30 · +5.9 pp · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F112 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.079 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F113 · Trend: construction loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F114 · Trend: loans as a share of deposits, value at the as-of quarter · 2026-06-30 · 88.4% · data/features/fct_bank_features.parquet: loans_to_deposits
- F115 · Trend: loans as a share of deposits, lowest value in the comparison window · n/a · 69.8% · data/features/fct_bank_features.parquet: loans_to_deposits
- F116 · Trend: loans as a share of deposits, highest value in the comparison window · n/a · 86.7% · data/features/fct_bank_features.parquet: loans_to_deposits
- F119 · Trend: loans as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.081 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F120 · Trend: loans as a share of deposits, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F121 · Trend: cash as a share of assets, value at the as-of quarter · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F122 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 2.0% · data/features/fct_bank_features.parquet: cash_to_assets
- F123 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 4.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F126 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.049 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F127 · Trend: cash as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature cash_to_assets contribution
- F128 · Trend: ratios outside their own prior range · 2026-06-30 · 9 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F131 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F133 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 98.0% · data/analyst/scores.parquet: percentile
- F134 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F138 · Peers: construction loans as a share of loans, bank value at the as-of quarter · 2026-06-30 · 32.4% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F139 · Peers: construction loans as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.6th · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F140 · Peers: construction loans as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F141 · Peers: construction loans as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F142 · Peers: construction loans as a share of loans, peer median · 2026-06-30 · 8.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F143 · Peers: construction loans as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F144 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F145 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 2.9th · data/features/fct_bank_features.parquet: leverage_ratio
- F146 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F147 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 2.0th · data/features/fct_bank_features.parquet: leverage_ratio
- F148 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 10.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F149 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F150 · Peers: volatile funding as a share of assets, bank value at the as-of quarter · 2026-06-30 · 24.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F151 · Peers: volatile funding as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.4th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F152 · Peers: volatile funding as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F153 · Peers: volatile funding as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 96.2nd · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F154 · Peers: volatile funding as a share of assets, peer median · 2026-06-30 · 9.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F155 · Peers: volatile funding as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F156 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 11.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F157 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 5.5th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F158 · Peers: the total risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F159 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 6.7th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F160 · Peers: the total risk-based capital ratio, peer median · 2026-06-30 · 15.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F161 · Peers: the total risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F162 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-06-30 · 92.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F163 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-06-30 · 94.5th · data/features/fct_bank_features.parquet: efficiency_ratio
- F164 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F165 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-06-30 · 95.0th · data/features/fct_bank_features.parquet: efficiency_ratio
- F166 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-06-30 · 63.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F167 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F168 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: allowance_to_loans
- F169 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 6.5th · data/features/fct_bank_features.parquet: allowance_to_loans
- F170 · Peers: loan-loss reserves as a share of loans, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: allowance_to_loans
- F171 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 2.7th · data/features/fct_bank_features.parquet: allowance_to_loans
- F172 · Peers: loan-loss reserves as a share of loans, peer median · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F173 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F174 · Peers: equity as a share of assets, bank value at the as-of quarter · 2026-06-30 · 7.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F175 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 6.9th · data/features/fct_bank_features.parquet: equity_to_assets
- F176 · Peers: equity as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F177 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 7.1st · data/features/fct_bank_features.parquet: equity_to_assets
- F178 · Peers: equity as a share of assets, peer median · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F179 · Peers: equity as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F180 · Peers: losses on bonds available for sale, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 34.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F181 · Peers: losses on bonds available for sale, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 92.4th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F182 · Peers: losses on bonds available for sale, as a share of equity, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F183 · Peers: losses on bonds available for sale, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 93.0th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F184 · Peers: losses on bonds available for sale, as a share of equity, peer median · 2026-06-30 · 5.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F185 · Peers: losses on bonds available for sale, as a share of equity, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F187 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 12 · data/features/fct_bank_features.parquet
- F188 · Peers: those ratios also unusual among peers · 2026-06-30 · 12 · data/features/fct_bank_features.parquet
- F190 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
