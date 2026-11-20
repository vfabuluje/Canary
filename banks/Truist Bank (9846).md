---
cert: 9846
name: "Truist Bank"
as_of: 2026-06-30
rank: 2699
n_banks: 4313
percentile: 37.44493392070485
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:00"
writer_model: "claude-opus-5-5"
checked: true
---

# Truist Bank (cert 9846)

## Summary

As of 2026-06-30, Truist Bank of NC ranked 2,699 out of 4,313 banks on Canary's model score, placing it in the 37.4th percentile, where higher means riskier. It was not flagged on the watchlist, though the model rated it riskier than a year earlier, when it sat in the 28.9th percentile. With $548.3 billion in assets against a national median of $384.7 million, it is far larger than a typical bank. Several of its ratios look unusual next to all banks nationally, but the peer comparison finds them typical for large banks of its kind, so the two views point different ways.

## Warning signs in the data

Capital, the owners' cushion against losses, is mixed: equity was 11.5% of assets, above the national median of 10.6%, but the leverage ratio (core capital as a share of average assets) was 9.8% against a median of 11.0%. Its risk-based capital ratios, which weigh assets by how risky they are, were also below the national medians: Tier 1 at 12.1% versus 14.6%, and total capital at 13.6% versus 15.8%.

On credit quality, loans 90+ days past due or not accruing interest were 0.7% of loans, above the national median of 0.5%. Annualized loan write-offs net of recoveries (loans given up on, minus amounts recovered) were 0.5% of loans versus a median of 0.0%, and the provision for loan losses (money set aside for expected bad loans) was 0.3% of assets versus 0.1%. Loan-loss reserves were 1.5% of loans, above the median of 1.2%.

On funding, uninsured deposits (balances above the government insurance limit) were 44.9% of deposits, well above the national median of 24.8%, while brokered deposits (money placed through middlemen) were 6.4% versus 0.0% and Federal Home Loan Bank borrowings were 5.1% of assets versus 0.2%. Deposit growth over the past four quarters was 0.4%, below the median of 4.2%. Paper losses on bonds held to maturity were 13.0% of equity versus a median of 0.0%, and on bonds available for sale 7.3% versus 5.6%; the peer section, however, finds the bond losses, write-offs, provisions and uninsured deposits typical for its peer group.

## Understanding the score

Truist Bank ranked 2,699 out of 4,313 banks as of 2026-06-30, the 37.4th percentile on a scale where higher means riskier. It was not flagged on the watchlist, which covers the top 2% of banks and held 87 banks that quarter.

Four features pushed the score up: losses on bonds available for sale at 7.3% of equity (+0.527), the efficiency ratio (operating costs as a share of revenue) at 53.0% (+0.282), commercial real estate loans at 10.5% of loans (+0.131), and net loan write-offs at 0.5% of loans (+0.001). Five features pushed it down: the Texas ratio (troubled assets against capital plus reserves) at 3.5% (-1.103), the Tier 1 risk-based capital ratio at 12.1% (-0.887), return on equity at 10.0% (-0.617), loans 90+ days past due or not accruing at 0.7% of loans (-0.350), and losses on bonds held to maturity at 13.0% of equity (-0.332). These contributions are in the model's internal scoring units, where positive values raise the score and negative values lower it.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 2,552 | 4,589 |  |
| 2024-12-31 | 2,919 | 4,560 |  |
| 2025-03-31 | 3,046 | 4,536 |  |
| 2025-06-30 | 3,197 | 4,494 |  |
| 2025-09-30 | 2,703 | 4,452 |  |
| 2025-12-31 | 2,529 | 4,411 |  |
| 2026-03-31 | 2,752 | 4,353 |  |
| 2026-06-30 | 2,699 | 4,313 |  |

## How its ratios moved

As of 2026-06-30, Truist Bank ranked 2,699 out of 4,313 banks, placing it in the 37.4th percentile, where higher means riskier. A year earlier, on 2025-06-30, it sat in the 28.9th percentile, so the model rated it riskier than a year earlier. Of 30 ratios compared with their own prior range, mostly the prior 12 quarters, 8 sat outside that range, and the table shows the 6 that were furthest outside.

Return on equity (profit as a share of the owners' stake) reached 10.0%, above its prior range of 7.5% to 9.7%, yet it pushed the score down, contributing -0.617 model log-odds units (the model's internal scoring units, where positive values raise the score). Return on assets (profit as a share of everything the bank owns) was 1.2%, above its prior range of 0.8% to 1.1%, and it also pushed the score down, at -0.277. The efficiency ratio (operating costs as a share of revenue) was 53.0%, below its prior range of 54.3% to 56.7%, and it pushed the score up, at +0.282.

Uninsured deposits (balances above the government insurance limit) made up 44.9% of deposits, above their prior range of 39.3% to 43.7%, but despite being outside that range they had little effect on the score, at -0.037. Brokered deposits (money placed through outside middlemen) were 6.4% of deposits, below their prior range of 6.7% to 8.5%, and even though they sat outside that range they pushed the score down, at -0.126. Construction loans were 2.3% of loans, below their prior range of 2.4% to 3.2%, and despite sitting outside that range they pushed the score down, at -0.187.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 53.0% | 54.3% to 56.7% | same quarter, prior 3 years | n/a | -1.3 pp | +0.282 | pushed the score up |
| uninsured deposits as a share of deposits | 44.9% | 39.3% to 43.7% | prior 12 quarters | +1.3 pp | +1.2 pp | -0.037 | little effect on the score |
| return on equity (profit as a share of equity) | 10.0% | 7.5% to 9.7% | same quarter, prior 3 years | n/a | +1.4 pp | -0.617 | pushed the score down |
| brokered deposits as a share of deposits | 6.4% | 6.7% to 8.5% | prior 12 quarters | -0.5 pp | -0.8 pp | -0.126 | pushed the score down |
| construction loans as a share of loans | 2.3% | 2.4% to 3.2% | prior 12 quarters | -0.1 pp | -0.5 pp | -0.187 | pushed the score down |
| return on assets (profit as a share of assets) | 1.2% | 0.8% to 1.1% | same quarter, prior 3 years | n/a | +0.2 pp | -0.277 | pushed the score down |

8 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: All Other Over 1 Billion.

This is a general group: the FDIC did not record a lending specialty for this bank.

Peers: 30 banks in the same specialty group and size tier (over $10 billion).

Losses on bonds held to maturity (paper losses on bonds the bank plans to keep until they are repaid), measured as a share of equity (the owners' cushion), stand at 13.0%, the 96.7th percentile nationally and unusually high, but at the 74.1st percentile among its peers against a peer median of 0.7%, which is typical for its peer group. Annualized loan write-offs net of recoveries (loans the bank has given up on collecting, minus amounts later recovered) are 0.5% of loans, the 94.2nd percentile nationally and unusually high, while the 80.4th percentile among its peers against a peer median of 0.2% is typical for its peer group.

The annualized provision for loan losses (money set aside to cover loans expected to go bad) is 0.3% of assets, the 91.6th percentile nationally and unusually high, yet the 74.1st percentile among its peers against a peer median of 0.1% is typical for its peer group. Uninsured deposits (balances above the government insurance limit) make up 44.9% of deposits, the 90.1st percentile nationally and unusually high, while the 62.5th percentile among its peers against a peer median of 40.3% is typical for its peer group.

Overall, 4 of the bank's ratios fall in the national top or bottom 10%, and 0 of those are also unusual among its peers, so these readings look ordinary for large banks of its kind.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| losses on bonds held to maturity, as a share of equity | 13.0% | 96.7th (unusually high) | 0.7% | 74.1st | typical for its peer group |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.5% | 94.2nd (unusually high) | 0.2% | 80.4th | typical for its peer group |
| annualized provision for loan losses as a share of assets | 0.3% | 91.6th (unusually high) | 0.1% | 74.1st | typical for its peer group |
| uninsured deposits as a share of deposits | 44.9% | 90.1st (unusually high) | 40.3% | 62.5th | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 13.3% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 76.1% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -0.1% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

Hindsight: the fact sheet for this note contains no data from after the as-of quarter, so later ranks, watchlist flags and whether the bank kept reporting cannot be described here. The outcome banner and score history table added to this note show what our data records for the period that followed.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NC · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 2,699 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 37.4% · data/analyst/scores.parquet: percentile
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 11.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 12.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 13.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 44.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 6.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 5.1% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 13.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 7.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $548.3 billion · data/features/fct_bank_features.parquet: log_total_assets
- F70 · National median: total assets · 2026-06-30 · $384.7 million · data/features/fct_bank_features.parquet: log_total_assets (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: losses on bonds available for sale, as a share of equity, value 7.3%; contribution to the score · 2026-06-30 · +0.527 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F76 · Driver up #2: the efficiency ratio (operating costs as a share of revenue), value 53.0%; contribution to the score · 2026-06-30 · +0.282 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F77 · Driver up #3: commercial real estate loans as a share of loans, value 10.5%; contribution to the score · 2026-06-30 · +0.131 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F78 · Driver up #4: annualized loan write-offs, net of recoveries, as a share of loans, value 0.5%; contribution to the score · 2026-06-30 · +0.001 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F79 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 3.5%; contribution to the score · 2026-06-30 · -1.103 · data/analyst/scores.parquet: feature texas_ratio contribution
- F80 · Driver down #2: the Tier 1 risk-based capital ratio, value 12.1%; contribution to the score · 2026-06-30 · -0.887 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #3: return on equity (profit as a share of equity), value 10.0%; contribution to the score · 2026-06-30 · -0.617 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 0.7%; contribution to the score · 2026-06-30 · -0.350 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F83 · Driver down #5: losses on bonds held to maturity, as a share of equity, value 13.0%; contribution to the score · 2026-06-30 · -0.332 · data/analyst/scores.parquet: feature htm_unrealized_loss_to_equity contribution
- F88 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 53.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F89 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 54.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F90 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 56.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F92 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.282 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F94 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 44.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F95 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 39.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F96 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 43.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F99 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.037 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F100 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F101 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: return_on_equity
- F102 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 7.5% · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 9.7% · data/features/fct_bank_features.parquet: return_on_equity
- F105 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.617 · data/analyst/scores.parquet: feature return_on_equity contribution
- F106 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F107 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 6.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F108 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 6.7% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F109 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 8.5% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F112 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.126 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F113 · Trend: brokered deposits as a share of deposits, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F114 · Trend: construction loans as a share of loans, value at the as-of quarter · 2026-06-30 · 2.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F115 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 2.4% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F116 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 3.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F119 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.187 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F120 · Trend: construction loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F121 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F122 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: return_on_assets
- F123 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: return_on_assets
- F125 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.277 · data/analyst/scores.parquet: feature return_on_assets contribution
- F126 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F127 · Trend: ratios outside their own prior range · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F129 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F130 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F132 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 28.9% · data/analyst/scores.parquet: percentile
- F133 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F137 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 13.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F138 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.7th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F139 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F140 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 74.1st · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F141 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F142 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F143 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F144 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 94.2nd · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F145 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F146 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 80.4th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F147 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F148 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F149 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F150 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 91.6th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F151 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F152 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 74.1st · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F153 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F154 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F155 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 44.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F156 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 90.1st · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F157 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F158 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 62.5th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F159 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 40.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F160 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F162 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 4 · data/features/fct_bank_features.parquet
- F163 · Peers: those ratios also unusual among peers · 2026-06-30 · 0 · data/features/fct_bank_features.parquet
- F165 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
