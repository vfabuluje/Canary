---
cert: 6560
name: "Huntington National Bank"
as_of: 2026-06-30
rank: 3804
n_banks: 4313
percentile: 11.824715974959421
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:18"
writer_model: "claude-opus-5-5"
checked: true
---

# Huntington National Bank (cert 6560)

## Summary

As of 2026-06-30, Huntington National Bank ranked 3,804 out of 4,313 banks nationally on Canary's risk score, which places it at the 11.8th percentile on a 0 to 100 scale where higher means riskier. It was not flagged on the watchlist, and the model rated it safer than a year earlier, when it sat at the 48.2nd percentile. The data do show some soft spots, notably very fast deposit growth of 35.7% over the past four quarters and problem loans above the national median, but the model's largest drivers, led by the Texas ratio and capital, pushed the score down.

## Warning signs in the data

Capital, the owners' cushion that absorbs losses, is mixed: equity was 11.8% of assets, above the national median of 10.6%, but the leverage ratio (core capital as a share of average assets) was 9.3% against a median of 11.0%. The risk-based capital ratios, which weigh assets by how risky they are, were also below the median, with Tier 1 at 12.0% against 14.6% and total capital at 13.8% against 15.8%.

Credit quality is weaker than the typical bank: loans 90+ days past due or not accruing interest were 1.1% of loans against a national median of 0.5%, and loans 30-89 days past due were 0.5% of assets against 0.2%. The Texas ratio, which sets troubled assets against capital plus reserves, was 5.6%, above the median of 2.9%, though the bank also held more loan-loss reserves (money set aside for bad loans) at 1.7% of loans against 1.2%. Commercial real estate loans were a smaller share of lending than usual, at 14.5% against a median of 23.6%, and the real-estate concentration check found the bank did not cross either supervisory line.

On funding, uninsured deposits (balances above the government insurance limit) were 32.5% of deposits against a median of 24.8%, brokered deposits (money placed through middlemen) were 4.4% against 0.0%, and Federal Home Loan Bank borrowings were 2.6% of assets against 0.2%. Deposits grew 35.7% over the past four quarters against a national median of 4.2%, while volatile funding was lower than usual at 4.2% of assets against 9.0%. Paper losses on bonds held to maturity equaled 5.1% of equity against a national median of 0.0%, and losses on bonds available for sale were 7.1% against 5.6%; the peer section notes the first figure is typical among similar large banks.

## Understanding the score

As of 2026-06-30, the bank ranked 3,804 of 4,313 banks, placing it at the 11.8th percentile on a 0 to 100 scale where higher means riskier. It was not flagged on the watchlist, which covers the top 2% of banks and held 87 banks that quarter.

Three features pushed the score up: deposit growth over the past four quarters at 35.7% contributed +0.246, losses on bonds available for sale at 7.1% of equity contributed +0.048, and net loan write-offs (loans given up as lost, less recoveries) at 0.2% of loans contributed +0.001.

Five features pushed it down: the Texas ratio at 5.6% contributed -1.160, the Tier 1 risk-based capital ratio at 12.0% contributed -0.887, and return on equity (profit as a share of the owners' stake) at 9.5% contributed -0.711. Loans 90+ days past due or not accruing interest at 1.1% of loans contributed -0.356, and losses on bonds held to maturity at 5.1% of equity contributed -0.305. Some of these move against intuition, since weaker-looking credit figures still lowered the score, which matches the trend section's finding that ratios outside their past range did not push the score up.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 2,628 | 4,589 |  |
| 2024-12-31 | 3,001 | 4,560 |  |
| 2025-03-31 | 2,180 | 4,536 |  |
| 2025-06-30 | 2,329 | 4,494 |  |
| 2025-09-30 | 1,893 | 4,452 |  |
| 2025-12-31 | 2,497 | 4,411 |  |
| 2026-03-31 | 3,859 | 4,353 |  |
| 2026-06-30 | 3,804 | 4,313 |  |

## How its ratios moved

As of 2026-06-30, the model gave Huntington National Bank a national rank of 3,804 out of 4,313 banks, which places it at the 11.8th percentile on a 0 to 100 scale where higher means riskier. A year earlier it sat at the 48.2nd percentile, so the model rated it safer than a year earlier. Each ratio is compared with its own range over the prior 12 quarters, and 13 of the 30 ratios checked now sit outside that range.

Return on equity (profit as a share of the owners' stake) was 9.5%, below its prior range of 11.4% to 14.6%, yet its contribution of -0.711 model log-odds units pushed the score down. The Texas ratio (troubled assets against capital plus reserves) was 5.6%, above its prior range of 3.5% to 4.9%, but its contribution of -1.160 pushed the score down. The efficiency ratio (operating costs as a share of revenue) was 59.9%, above its prior range of 51.7% to 58.1%, and its contribution of -0.163 pushed the score down. Loans 90+ days past due or not accruing interest made up 1.1% of loans, above the prior range of 0.6% to 0.9%, with a contribution of -0.356 that pushed the score down. Construction loans were 2.8% of loans, above the prior range of 1.0% to 2.6%, and their contribution of -0.175 pushed the score down. Loans as a share of deposits reached 82.7%, just above the prior range of 76.6% to 82.2%, with a contribution of -0.072 that pushed the score down.

In every case shown here the ratio moved outside its own past range, yet the model's contribution pushed the score down rather than up, which is the main contrast in this section.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 9.5% | 11.4% to 14.6% | same quarter, prior 3 years | n/a | -2.3 pp | -0.711 | pushed the score down |
| the Texas ratio (troubled assets against capital plus reserves) | 5.6% | 3.5% to 4.9% | prior 12 quarters | +0.7 pp | +0.9 pp | -1.160 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 59.9% | 51.7% to 58.1% | same quarter, prior 3 years | n/a | +5.5 pp | -0.163 | pushed the score down |
| loans 90+ days past due or not accruing interest, as a share of loans | 1.1% | 0.6% to 0.9% | prior 12 quarters | +0.1 pp | +0.3 pp | -0.356 | pushed the score down |
| construction loans as a share of loans | 2.8% | 1.0% to 2.6% | prior 12 quarters | +0.2 pp | +1.7 pp | -0.175 | pushed the score down |
| loans as a share of deposits | 82.7% | 76.6% to 82.2% | prior 12 quarters | +0.8 pp | +3.1 pp | -0.072 | pushed the score down |

13 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 114 banks in the same specialty group and size tier (over $10 billion).

Over the past four quarters, the bank's total assets (everything it owns, mainly loans and securities) grew 37.0%, which places it at the 97.5th percentile nationally, a reading of unusually high. Among its peers, that asset growth sits at the 92.5th percentile against a peer median of 5.9%, which is unusually high among its peers too. Deposits (money customers keep at the bank) grew 35.7% over the same past four quarters, at the 97.1st percentile nationally, a reading of unusually high. Among its peers, that deposit growth sits at the 91.7th percentile against a peer median of 5.7%, which is unusually high among its peers too.

Losses on bonds held to maturity (the drop in value of bonds the bank plans to keep until they mature) equal 5.1% of equity, the owners' capital cushion, at the 92.2nd percentile nationally, a reading of unusually high. Among its peers, this ratio sits at the 84.5th percentile against a peer median of 1.5%, which is typical for its peer group.

Overall, 3 of the bank's ratios fall in the national top or bottom 10%, and 2 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| asset growth over the past four quarters | 37.0% | 97.5th (unusually high) | 5.9% | 92.5th | unusually high among its peers too |
| deposit growth over the past four quarters | 35.7% | 97.1st (unusually high) | 5.7% | 91.7th | unusually high among its peers too |
| losses on bonds held to maturity, as a share of equity | 5.1% | 92.2nd (unusually high) | 1.5% | 84.5th | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 18.4% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 92.9% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 80.8% | 50% or more | yes |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

This section looks back with hindsight, after the as-of quarter. The outcome case for this bank is quiet, meaning our data record no failure for it. The fact sheet for this memo includes no later ranks, watchlist flags or reporting status, so we cannot say how its standing changed afterward or whether it still reports.

## Sources

- F1 · Bank name · n/a · Huntington National Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2026-06-30 · 3,804 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 11.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 11.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 9.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 12.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 13.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 14.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 32.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 4.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 5.1% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 7.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · 35.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: deposit growth over the past four quarters, value 35.7%; contribution to the score · 2026-06-30 · +0.246 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 7.1%; contribution to the score · 2026-06-30 · +0.048 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: annualized loan write-offs, net of recoveries, as a share of loans, value 0.2%; contribution to the score · 2026-06-30 · +0.001 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F78 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 5.6%; contribution to the score · 2026-06-30 · -1.160 · data/analyst/scores.parquet: feature texas_ratio contribution
- F79 · Driver down #2: the Tier 1 risk-based capital ratio, value 12.0%; contribution to the score · 2026-06-30 · -0.887 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F80 · Driver down #3: return on equity (profit as a share of equity), value 9.5%; contribution to the score · 2026-06-30 · -0.711 · data/analyst/scores.parquet: feature return_on_equity contribution
- F81 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 1.1%; contribution to the score · 2026-06-30 · -0.356 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F82 · Driver down #5: losses on bonds held to maturity, as a share of equity, value 5.1%; contribution to the score · 2026-06-30 · -0.305 · data/analyst/scores.parquet: feature htm_unrealized_loss_to_equity contribution
- F87 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 9.5% · data/features/fct_bank_features.parquet: return_on_equity
- F88 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 11.4% · data/features/fct_bank_features.parquet: return_on_equity
- F89 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 14.6% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.711 · data/analyst/scores.parquet: feature return_on_equity contribution
- F92 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F93 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: texas_ratio
- F94 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 3.5% · data/features/fct_bank_features.parquet: texas_ratio
- F95 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 4.9% · data/features/fct_bank_features.parquet: texas_ratio
- F98 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · -1.160 · data/analyst/scores.parquet: feature texas_ratio contribution
- F99 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature texas_ratio contribution
- F100 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 59.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 51.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F102 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 58.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F104 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.163 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F106 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F107 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F108 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F111 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.356 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F112 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F113 · Trend: construction loans as a share of loans, value at the as-of quarter · 2026-06-30 · 2.8% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F114 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F115 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 2.6% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F118 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.175 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F119 · Trend: construction loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F120 · Trend: loans as a share of deposits, value at the as-of quarter · 2026-06-30 · 82.7% · data/features/fct_bank_features.parquet: loans_to_deposits
- F121 · Trend: loans as a share of deposits, lowest value in the comparison window · n/a · 76.6% · data/features/fct_bank_features.parquet: loans_to_deposits
- F122 · Trend: loans as a share of deposits, highest value in the comparison window · n/a · 82.2% · data/features/fct_bank_features.parquet: loans_to_deposits
- F125 · Trend: loans as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.072 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F126 · Trend: loans as a share of deposits, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F127 · Trend: ratios outside their own prior range · 2026-06-30 · 13 · data/features/fct_bank_features.parquet
- F129 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F130 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F132 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 48.2% · data/analyst/scores.parquet: percentile
- F133 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it safer than a year earlier · data/analyst/scores.parquet: percentile
- F137 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · 37.0% · data/features/fct_bank_features.parquet: asset_growth_4q
- F138 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.5th · data/features/fct_bank_features.parquet: asset_growth_4q
- F139 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: asset_growth_4q
- F140 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 92.5th · data/features/fct_bank_features.parquet: asset_growth_4q
- F141 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 5.9% · data/features/fct_bank_features.parquet: asset_growth_4q
- F142 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F143 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · 35.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F144 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.1st · data/features/fct_bank_features.parquet: deposit_growth_4q
- F145 · Peers: deposit growth over the past four quarters, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: deposit_growth_4q
- F146 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 91.7th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F147 · Peers: deposit growth over the past four quarters, peer median · 2026-06-30 · 5.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F148 · Peers: deposit growth over the past four quarters, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F149 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 5.1% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F150 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 92.2nd · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F151 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F152 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 84.5th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F153 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F154 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F156 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 3 · data/features/fct_bank_features.parquet
- F157 · Peers: those ratios also unusual among peers · 2026-06-30 · 2 · data/features/fct_bank_features.parquet
- F159 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
