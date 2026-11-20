---
cert: 33124
name: "Goldman Sachs Bank Usa"
as_of: 2026-06-30
rank: 115
n_banks: 4313
percentile: 97.3568281938326
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:55:44"
writer_model: "claude-opus-5-5"
checked: true
---

# Goldman Sachs Bank Usa (cert 33124)

## Summary

As of June 30, 2026, Canary ranks Goldman Sachs Bank Usa, a New York bank, number 115 out of 4,313 banks nationally, which places it at the 97.4th percentile on a scale where higher means riskier. It is not flagged on the watchlist, which held 87 banks that quarter. Its funding drives the score up most: brokered deposits (deposits placed through middlemen) make up 20.8% of deposits, and its interest costs are high, while few troubled loans and solid risk-based capital pull the score down. Its leverage ratio (core capital as a share of average assets) of 7.7% is well below the national median of 11.0%, although the peer section finds it typical for its group of large banks, so the national and peer views point different ways.

## Warning signs in the data

Capital, the cushion that absorbs losses, is thinner than at most banks: equity was 7.9% of assets against a national median of 10.6%, and the leverage ratio was 7.7% against a median of 11.0%. The leverage ratio also moved down, with a change of -2.7 pp over four quarters. Risk-based capital ratios, which weight assets by riskiness, were closer to typical, with Tier 1 capital at 13.5% against a median of 14.6% and total capital at 14.7% against a median of 15.8%.

On credit quality, loans 90 or more days past due or not earning interest were 1.0% of loans, above the national median of 0.5%, and net loan write-offs were 0.3% against a median of 0.0%. Loan-loss reserves, money set aside for bad loans, were 0.6% of loans, below the median of 1.2%, while the Texas ratio (troubled assets against capital plus reserves) was 4.2% against a median of 2.9%, both low levels in plain terms. The real-estate concentration check found the bank did not cross either supervisory line.

Funding is the clearest outlier: uninsured deposits, those above the government insurance limit, were 42.9% of deposits against a median of 24.8%, and brokered deposits were 20.8% against a median of 0.0%. Core deposits, the steadier customer money, were 43.6% of assets against a median of 75.5%, volatile funding was 24.4% against 9.0%, and interest expense was 3.0% of assets against 1.6%. Offsetting this, cash was 16.5% of assets against a median of 6.2%, and unrealized losses on bonds available for sale were only 0.9% of equity against a median of 5.6%, with held-to-maturity bond losses at 0.0%. The peer section notes that most of these funding figures are typical for its peer group, except volatile funding, which is unusual among peers too.

## Understanding the score

The bank ranks number 115 out of 4,313 banks, at the 97.4th percentile on a scale of 0 to 100 where higher means riskier. It is not flagged on the watchlist, which covers 2% of banks, or 87 banks that quarter.

The five factors pushing the score up were brokered deposits at 20.8% of deposits (+0.809), interest expense at 3.0% of assets (+0.449), core deposits at 43.6% of assets (+0.399), the efficiency ratio, operating costs as a share of revenue, at 38.5% (+0.286), and commercial real estate loans at 2.9% of loans (+0.111).

The five factors pulling the score down were the Texas ratio at 4.2% (-1.364), the Tier 1 risk-based capital ratio at 13.5% (-0.767), return on equity, profit as a share of equity, at 13.7% (-0.542), loans 90 or more days past due or not earning interest at 1.0% (-0.313), and total assets of $758.8 billion (-0.309).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 347 | 4,589 |  |
| 2024-12-31 | 904 | 4,560 |  |
| 2025-03-31 | 697 | 4,536 |  |
| 2025-06-30 | 215 | 4,494 |  |
| 2025-09-30 | 153 | 4,452 |  |
| 2025-12-31 | 216 | 4,411 |  |
| 2026-03-31 | 138 | 4,353 |  |
| 2026-06-30 | 115 | 4,313 |  |

## How its ratios moved

As of June 30, 2026, the model ranked the bank 115 out of 4,313 banks, placing it at the 97.4th percentile, where higher means riskier. The model rated it riskier than a year earlier, when it sat at the 95.2nd percentile. Each ratio is compared with its own values over the prior 12 quarters, and 14 of the 30 ratios checked sat outside that prior range.

Annualized interest expense, the yearly cost of interest paid as a share of assets, was 3.0% against a prior range of 3.3% to 4.2%, and its contribution of +0.449 model log-odds units pushed the score up. Core deposits, the steadier customer deposits, made up 43.6% of assets, below their prior range of 45.6% to 52.4%, and their contribution of +0.399 pushed the score up. Commercial real estate loans were 2.9% of loans, below a prior range of 3.3% to 4.9%, and their contribution of +0.111 pushed the score up. The leverage ratio, core capital as a share of average assets, was 7.7%, below its prior range of 8.8% to 11.0%, and its contribution of +0.082 pushed the score up.

Volatile funding, money that can leave the bank quickly, reached 24.4% of assets, above its prior range of 14.0% to 22.1%, yet its contribution of -0.044 had little effect on the score. Loan write-offs net of recoveries, the share of loans written off as lost, were 0.3%, below a prior range of 0.7% to 0.9%, yet their contribution of -0.001 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the leverage ratio (core capital as a share of average assets) | 7.7% | 8.8% to 11.0% | prior 12 quarters | -1.1 pp | -2.7 pp | +0.082 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.3% | 0.7% to 0.9% | same quarter, prior 3 years | n/a | -0.5 pp | -0.001 | little effect on the score |
| core deposits as a share of assets | 43.6% | 45.6% to 52.4% | prior 12 quarters | -2.2 pp | -2.1 pp | +0.399 | pushed the score up |
| annualized interest expense as a share of assets | 3.0% | 3.3% to 4.2% | same quarter, prior 3 years | n/a | -0.3 pp | +0.449 | pushed the score up |
| volatile funding as a share of assets | 24.4% | 14.0% to 22.1% | prior 12 quarters | +2.4 pp | +6.2 pp | -0.044 | little effect on the score |
| commercial real estate loans as a share of loans | 2.9% | 3.3% to 4.9% | prior 12 quarters | -0.5 pp | -1.0 pp | +0.111 | pushed the score up |

14 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: All Other Over 1 Billion.

This is a general group: the FDIC did not record a lending specialty for this bank.

Peers: 30 banks in the same specialty group and size tier (over $10 billion).

As of 2026-06-30, Canary ranks Goldman Sachs Bank Usa number 115 out of 4,313 banks nationally, near the top of the national ranking. Its annualized interest expense as a share of assets (what it pays to borrow and hold deposits) was 3.0%, at the 98.5th national percentile, which is unusually high, while it sat at the 91.4th percentile among its peers against a peer median of 1.8%, typical for its peer group. Its net interest margin (the spread earned on lending and investing) was 1.8%, at the 1.7th national percentile, which is unusually low, and at the 25.0th percentile among its peers against a peer median of 2.6%, typical for its peer group. Its leverage ratio (core capital as a share of average assets) was 7.7%, at the 1.9th national percentile, which is unusually low, and at the 31.7th percentile among its peers against a peer median of 9.2%, typical for its peer group.

Volatile funding (money that can leave quickly) made up 24.4% of assets, at the 96.5th national percentile, which is unusually high, and at the 98.3rd percentile among its peers against a peer median of 5.7%, unusually high among its peers too. Core deposits (stable, everyday customer deposits) made up 43.6% of assets, at the 3.8th national percentile, which is unusually low, and at the 12.1st percentile among its peers against a peer median of 69.5%, typical for its peer group. Brokered deposits (deposits placed through middlemen) were 20.8% of deposits, at the 95.7th national percentile, which is unusually high, and at the 69.6th percentile among its peers against a peer median of 6.0%, typical for its peer group.

Its efficiency ratio (operating costs as a share of revenue, where lower means leaner) was 38.5%, at the 4.4th national percentile, which is unusually low, and at the 28.3rd percentile among its peers against a peer median of 53.4%, typical for its peer group. Loan-loss reserves (money set aside for loans that may go bad) were 0.6% of loans, at the 4.5th national percentile, which is unusually low, and at the 37.5th percentile among its peers against a peer median of 0.9%, typical for its peer group. Overall, 11 of the bank's ratios fall in the national top or bottom 10%, but only 1 of those is also unusual among its peers, so most of what stands out nationally is typical for this peer group.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| annualized interest expense as a share of assets | 3.0% | 98.5th (unusually high) | 1.8% | 91.4th | typical for its peer group |
| net interest margin (the spread earned on lending and investing) | 1.8% | 1.7th (unusually low) | 2.6% | 25.0th | typical for its peer group |
| the leverage ratio (core capital as a share of average assets) | 7.7% | 1.9th (unusually low) | 9.2% | 31.7th | typical for its peer group |
| volatile funding as a share of assets | 24.4% | 96.5th (unusually high) | 5.7% | 98.3rd | unusually high among its peers too |
| core deposits as a share of assets | 43.6% | 3.8th (unusually low) | 69.5% | 12.1st | typical for its peer group |
| brokered deposits as a share of deposits | 20.8% | 95.7th (unusually high) | 6.0% | 69.6th | typical for its peer group |
| the efficiency ratio (operating costs as a share of revenue) | 38.5% | 4.4th (unusually low) | 53.4% | 28.3rd | typical for its peer group |
| loan-loss reserves as a share of loans | 0.6% | 4.5th (unusually low) | 0.9% | 37.5th | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 6.9% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 28.1% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 16.2% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

This section uses hindsight, looking past the as-of quarter of June 30, 2026. The fact sheet for this memo contains no later ranks, watchlist flags or reporting status for the bank, so this note cannot describe how its standing changed or whether it kept reporting. The outcome banner shown with this memo classifies the case as quiet.

## Sources

- F1 · Bank name · n/a · Goldman Sachs Bank Usa · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NY · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 115 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 97.4% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 7.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 13.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 14.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 42.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 20.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 43.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 24.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 16.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 20.8%; contribution to the score · 2026-06-30 · +0.809 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: annualized interest expense as a share of assets, value 3.0%; contribution to the score · 2026-06-30 · +0.449 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F77 · Driver up #3: core deposits as a share of assets, value 43.6%; contribution to the score · 2026-06-30 · +0.399 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F78 · Driver up #4: the efficiency ratio (operating costs as a share of revenue), value 38.5%; contribution to the score · 2026-06-30 · +0.286 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F79 · Driver up #5: commercial real estate loans as a share of loans, value 2.9%; contribution to the score · 2026-06-30 · +0.111 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 4.2%; contribution to the score · 2026-06-30 · -1.364 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 13.5%; contribution to the score · 2026-06-30 · -0.767 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 13.7%; contribution to the score · 2026-06-30 · -0.542 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 1.0%; contribution to the score · 2026-06-30 · -0.313 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F84 · Driver down #5: total assets, value $758.8 billion; contribution to the score · 2026-06-30 · -0.309 · data/analyst/scores.parquet: feature log_total_assets contribution
- F89 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-06-30 · 7.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F90 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 8.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F91 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F93 · Trend: the leverage ratio (core capital as a share of average assets), change over four quarters, in percentage points · 2026-06-30 · -2.7 pp · data/features/fct_bank_features.parquet: leverage_ratio
- F94 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.082 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F95 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F96 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F97 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F98 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F100 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.001 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F101 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F102 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 43.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F103 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 45.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F104 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 52.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F107 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.399 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F108 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F109 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F110 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 3.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F111 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 4.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F113 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.449 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F114 · Trend: annualized interest expense as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F115 · Trend: volatile funding as a share of assets, value at the as-of quarter · 2026-06-30 · 24.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F116 · Trend: volatile funding as a share of assets, lowest value in the comparison window · n/a · 14.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F117 · Trend: volatile funding as a share of assets, highest value in the comparison window · n/a · 22.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F120 · Trend: volatile funding as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.044 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F121 · Trend: volatile funding as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F122 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F123 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 3.3% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F124 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 4.9% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F127 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.111 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F128 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F129 · Trend: ratios outside their own prior range · 2026-06-30 · 14 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F132 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F134 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 95.2% · data/analyst/scores.parquet: percentile
- F135 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F139 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F140 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.5th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F141 · Peers: annualized interest expense as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F142 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 91.4th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F143 · Peers: annualized interest expense as a share of assets, peer median · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F144 · Peers: annualized interest expense as a share of assets, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F145 · Peers: net interest margin (the spread earned on lending and investing), bank value at the as-of quarter · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: net_interest_margin
- F146 · Peers: net interest margin (the spread earned on lending and investing), national percentile (100 = highest value among all banks) · 2026-06-30 · 1.7th · data/features/fct_bank_features.parquet: net_interest_margin
- F147 · Peers: net interest margin (the spread earned on lending and investing), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: net_interest_margin
- F148 · Peers: net interest margin (the spread earned on lending and investing), percentile among its peers (100 = highest value) · 2026-06-30 · 25.0th · data/features/fct_bank_features.parquet: net_interest_margin
- F149 · Peers: net interest margin (the spread earned on lending and investing), peer median · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F150 · Peers: net interest margin (the spread earned on lending and investing), reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: net_interest_margin
- F151 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 7.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F152 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 1.9th · data/features/fct_bank_features.parquet: leverage_ratio
- F153 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F154 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 31.7th · data/features/fct_bank_features.parquet: leverage_ratio
- F155 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 9.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F156 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: leverage_ratio
- F157 · Peers: volatile funding as a share of assets, bank value at the as-of quarter · 2026-06-30 · 24.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F158 · Peers: volatile funding as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.5th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F159 · Peers: volatile funding as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F160 · Peers: volatile funding as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 98.3rd · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F161 · Peers: volatile funding as a share of assets, peer median · 2026-06-30 · 5.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F162 · Peers: volatile funding as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F163 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2026-06-30 · 43.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F164 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 3.8th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F165 · Peers: core deposits as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F166 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 12.1st · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F167 · Peers: core deposits as a share of assets, peer median · 2026-06-30 · 69.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F168 · Peers: core deposits as a share of assets, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F169 · Peers: brokered deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 20.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F170 · Peers: brokered deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 95.7th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F171 · Peers: brokered deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: brokered_to_deposits
- F172 · Peers: brokered deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 69.6th · data/features/fct_bank_features.parquet: brokered_to_deposits
- F173 · Peers: brokered deposits as a share of deposits, peer median · 2026-06-30 · 6.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F174 · Peers: brokered deposits as a share of deposits, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: brokered_to_deposits
- F175 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-06-30 · 38.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F176 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-06-30 · 4.4th · data/features/fct_bank_features.parquet: efficiency_ratio
- F177 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: efficiency_ratio
- F178 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-06-30 · 28.3rd · data/features/fct_bank_features.parquet: efficiency_ratio
- F179 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-06-30 · 53.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F180 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: efficiency_ratio
- F181 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: allowance_to_loans
- F182 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 4.5th · data/features/fct_bank_features.parquet: allowance_to_loans
- F183 · Peers: loan-loss reserves as a share of loans, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: allowance_to_loans
- F184 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 37.5th · data/features/fct_bank_features.parquet: allowance_to_loans
- F185 · Peers: loan-loss reserves as a share of loans, peer median · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: allowance_to_loans
- F186 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: allowance_to_loans
- F188 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 11 · data/features/fct_bank_features.parquet
- F189 · Peers: those ratios also unusual among peers · 2026-06-30 · 1 · data/features/fct_bank_features.parquet
- F191 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
