---
cert: 57957
name: "Citizens Bank National Assn"
as_of: 2026-06-30
rank: 3200
n_banks: 4313
percentile: 25.828889404127054
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:33"
writer_model: "claude-opus-5-5"
checked: true
---

# Citizens Bank National Assn (cert 57957)

## Summary

As of 2026-06-30, Canary's model ranked Citizens Bank National Assn, a Rhode Island bank with $232.5 billion in assets, 3,200 out of 4,313 banks, which is the 25.8th percentile on a scale where higher means riskier. It was not flagged on the watchlist, though the model rated it riskier than a year earlier, when it sat in the 8.5th percentile. The figures that stand out are uninsured deposits at 47.5% of deposits against a national median of 24.8%, and seriously late loans at 1.4% of loans against a median of 0.5%. Its main capital ratios sat below the national medians, yet the model treated its capital and troubled-asset levels as reasons to lower the score, so the raw comparisons and the model point in different directions.

## Warning signs in the data

Capital, the bank's own money that absorbs losses, was mixed: equity, the owners' stake, was 11.4% of assets against a national median of 10.6%. The leverage ratio, core capital as a share of average assets, was 9.4% against a median of 11.0%, and the Tier 1 risk-based capital ratio, core capital measured against assets weighted by riskiness, was 11.9% against 14.6%. The total risk-based capital ratio, which adds some extra loss-absorbing items, was 13.7% against a median of 15.8%.

Credit quality was weaker than typical: loans 90 or more days past due or no longer accruing interest were 1.4% of loans against a median of 0.5%, and nonaccrual assets plus foreclosed property were 0.6% of assets against 0.3%. Net loan write-offs, loans written off as unlikely to be repaid, ran at 0.4% of loans against a median of 0.0%, and the Texas ratio, troubled assets against capital plus reserves, was 7.2% against 2.9%. The peer section notes that against other large banks in its group, both the uninsured deposit share and the write-off rate look typical rather than unusual.

On funding, uninsured deposits, balances above the government insurance limit, were 47.5% of deposits against a median of 24.8%, brokered deposits, money placed through middlemen, were 2.6% against 0.0%, and Federal Home Loan Bank borrowings, loans from a government-sponsored lender, were 2.7% of assets against 0.2%. Volatile funding, money that can leave quickly, was lower than typical at 3.4% of assets against a median of 9.0%. Paper losses on bonds held to maturity were 3.2% of equity against a median of 0.0%, while losses on bonds available for sale were 5.5% of equity, close to the median of 5.6%.

## Understanding the score

As of 2026-06-30, the bank ranked 3,200 out of 4,313 banks, placing it in the 25.8th percentile on a scale of 0 to 100 where higher means riskier. It was not flagged on the watchlist, which covers the 2% of banks with the highest scores and held 87 banks that quarter.

Three factors pushed the score up: commercial real estate loans at 9.5% of loans contributed +0.170, losses on bonds available for sale at 5.5% of equity contributed +0.097, and net loan write-offs at 0.4% of loans contributed +0.002. Five factors pushed it down: the Tier 1 risk-based capital ratio at 11.9% contributed -0.908, the Texas ratio at 7.2% contributed -0.893, and return on equity, profit as a share of equity, at 8.5% contributed -0.701. Loans 90 or more days past due or not accruing interest at 1.4% of loans contributed -0.334, and the total risk-based capital ratio at 13.7% contributed -0.289. The downward pushes were much larger than the upward ones, which is why the bank sits in the lower part of the national ranking.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 3,361 | 4,589 |  |
| 2024-12-31 | 3,528 | 4,560 |  |
| 2025-03-31 | 3,402 | 4,536 |  |
| 2025-06-30 | 4,114 | 4,494 |  |
| 2025-09-30 | 3,314 | 4,452 |  |
| 2025-12-31 | 3,245 | 4,411 |  |
| 2026-03-31 | 3,235 | 4,353 |  |
| 2026-06-30 | 3,200 | 4,313 |  |

## How its ratios moved

As of 2026-06-30, Canary's model ranked Citizens Bank National Assn 3,200 out of 4,313 banks, placing it in the 25.8th percentile, where a higher percentile means a riskier score. A year earlier it sat in the 8.5th percentile, and the model rated it riskier than a year earlier. Each ratio is compared with its own range over the prior 12 quarters, and 11 of the 30 ratios checked fell outside that range. A ratio's contribution is measured in model log-odds units, an internal score scale where positive numbers push the score up and negative numbers push it down.

Asset growth over the past four quarters reached 6.7%, above its prior range of -2.4% to 4.0%, yet its contribution of -0.074 pushed the score down. Deposit growth over the past four quarters was 5.6%, also above its prior range of -1.6% to 4.7%, and its contribution of -0.162 pushed the score down. Uninsured deposits, meaning balances above the government insurance limit, were 47.5% of deposits, above their prior range of 39.6% to 46.6%, but their contribution of -0.037 had little effect on the score.

Construction loans were 3.2% of loans, below their prior range of 3.4% to 5.1%, and their contribution of -0.183 pushed the score down. Commercial real estate loans, which fund properties such as offices and stores, were 9.5% of loans, below their prior range of 9.7% to 11.9%, while their contribution of +0.170 pushed the score up. Loans 30-89 days past due, where borrowers are behind on payments, were 0.2% of assets, below their prior range of 0.3% to 0.5%, and their contribution of -0.254 pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| asset growth over the past four quarters | 6.7% | -2.4% to 4.0% | prior 12 quarters | +3.4 pp | +7.4 pp | -0.074 | pushed the score down |
| deposit growth over the past four quarters | 5.6% | -1.6% to 4.7% | prior 12 quarters | +2.6 pp | +6.3 pp | -0.162 | pushed the score down |
| construction loans as a share of loans | 3.2% | 3.4% to 5.1% | prior 12 quarters | -0.2 pp | -1.4 pp | -0.183 | pushed the score down |
| uninsured deposits as a share of deposits | 47.5% | 39.6% to 46.6% | prior 12 quarters | +0.8 pp | +3.1 pp | -0.037 | little effect on the score |
| commercial real estate loans as a share of loans | 9.5% | 9.7% to 11.9% | prior 12 quarters | -0.2 pp | -1.0 pp | +0.170 | pushed the score up |
| loans 30-89 days past due, as a share of assets | 0.2% | 0.3% to 0.5% | prior 12 quarters | -0.2 pp | -0.1 pp | -0.254 | pushed the score down |

11 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: All Other Over 1 Billion.

This is a general group: the FDIC did not record a lending specialty for this bank.

Peers: 30 banks in the same specialty group and size tier (over $10 billion).

Uninsured deposits, meaning money held above the government deposit insurance limit, made up 47.5% of this bank's deposits, placing it at the 92.5th percentile nationally, which is unusually high among all banks. Among its peers it sat at the 66.1st percentile, against a peer median of 40.3%, which is typical for its peer group.

Loan write-offs, the yearly rate of loans written off as unlikely to be repaid after subtracting amounts later recovered, were 0.4% of loans, placing the bank at the 91.3rd percentile nationally, which is unusually high among all banks. Among its peers it sat at the 55.4th percentile, against a peer median of 0.2%, which is typical for its peer group.

Overall, 2 of the bank's ratios fell in the national top or bottom 10%, and 0 of those were also unusual when compared with similar banks.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| uninsured deposits as a share of deposits | 47.5% | 92.5th (unusually high) | 40.3% | 66.1st | typical for its peer group |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.4% | 91.3rd (unusually high) | 0.2% | 55.4th | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 20.8% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 109.8% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -17.8% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

Hindsight: the fact sheet for this memo contains no data from after the as-of quarter. As a result, this section cannot report later ranks, watchlist flags, or whether the bank kept filing reports, and the outcome banner and score history table added by code are the place to check for any later information.

## Sources

- F1 · Bank name · n/a · Citizens Bank National Assn · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · RI · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 3,200 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 25.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 11.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 9.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 11.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 13.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 7.2% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 47.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 2.7% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $232.5 billion · data/features/fct_bank_features.parquet: log_total_assets
- F75 · Driver up #1: commercial real estate loans as a share of loans, value 9.5%; contribution to the score · 2026-06-30 · +0.170 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 5.5%; contribution to the score · 2026-06-30 · +0.097 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: annualized loan write-offs, net of recoveries, as a share of loans, value 0.4%; contribution to the score · 2026-06-30 · +0.002 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F78 · Driver down #1: the Tier 1 risk-based capital ratio, value 11.9%; contribution to the score · 2026-06-30 · -0.908 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F79 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 7.2%; contribution to the score · 2026-06-30 · -0.893 · data/analyst/scores.parquet: feature texas_ratio contribution
- F80 · Driver down #3: return on equity (profit as a share of equity), value 8.5%; contribution to the score · 2026-06-30 · -0.701 · data/analyst/scores.parquet: feature return_on_equity contribution
- F81 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 1.4%; contribution to the score · 2026-06-30 · -0.334 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F82 · Driver down #5: the total risk-based capital ratio, value 13.7%; contribution to the score · 2026-06-30 · -0.289 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F87 · Trend: asset growth over the past four quarters, value at the as-of quarter · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F88 · Trend: asset growth over the past four quarters, lowest value in the comparison window · n/a · -2.4% · data/features/fct_bank_features.parquet: asset_growth_4q
- F89 · Trend: asset growth over the past four quarters, highest value in the comparison window · n/a · 4.0% · data/features/fct_bank_features.parquet: asset_growth_4q
- F92 · Trend: asset growth over the past four quarters, contribution to the score (model log-odds units) · 2026-06-30 · -0.074 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F93 · Trend: asset growth over the past four quarters, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F94 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F95 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · -1.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F96 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 4.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F99 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2026-06-30 · -0.162 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F100 · Trend: deposit growth over the past four quarters, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F101 · Trend: construction loans as a share of loans, value at the as-of quarter · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F102 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 3.4% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F103 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 5.1% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F106 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.183 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F107 · Trend: construction loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F108 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 47.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F109 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 39.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F110 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 46.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F113 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.037 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F114 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F115 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 9.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F116 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 9.7% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F117 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 11.9% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F120 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.170 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F121 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F122 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F123 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F124 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F127 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.254 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F128 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F129 · Trend: ratios outside their own prior range · 2026-06-30 · 11 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F132 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F134 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 8.5% · data/analyst/scores.parquet: percentile
- F135 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F139 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 47.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F140 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 92.5th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F141 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F142 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 66.1st · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F143 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 40.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F144 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F145 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F146 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 91.3rd · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F147 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F148 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 55.4th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F149 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F150 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F152 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 2 · data/features/fct_bank_features.parquet
- F153 · Peers: those ratios also unusual among peers · 2026-06-30 · 0 · data/features/fct_bank_features.parquet
- F155 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
