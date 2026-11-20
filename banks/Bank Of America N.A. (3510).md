---
cert: 3510
name: "Bank Of America N.A."
as_of: 2026-06-30
rank: 2702
n_banks: 4313
percentile: 37.375376767910964
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:55:11"
writer_model: "claude-opus-5-5"
checked: true
---

# Bank Of America N.A. (cert 3510)

## Summary

As of 2026-06-30, Bank Of America N.A. (based in NC) ranked 2,702 out of 4,313 banks nationally on Canary's risk score, placing it in the 37.4th percentile, where a higher percentile means riskier. It was not flagged on the watchlist that quarter. The figures that stand out are paper losses on bonds held to maturity of 34.1% of equity against a national median of 0.0%, and a leverage ratio (core capital as a share of average assets) of 7.1% against a median of 11.0%. Even so, the model leaned on the bank's low troubled assets, its risk-based capital and its steady profits, which pulled the score down and kept the bank in the lower-risk part of the ranking.

## Warning signs in the data

Capital, the owners' cushion that absorbs losses, is thinner than at most banks: equity was 9.1% of assets against a national median of 10.6%, and the leverage ratio was 7.1% against 11.0%. The Tier 1 risk-based capital ratio (core capital measured against riskier assets) was 12.1% against a median of 14.6%, and the total risk-based capital ratio was 13.1% against 15.8%. The trend section notes that both risk-based ratios had slipped just below their own prior range.

Credit quality is close to typical: loans 90 or more days late or not accruing interest were 0.6% of loans against a median of 0.5%, and the Texas ratio (troubled assets against capital plus reserves) was 3.1% against 2.9%. Net loan write-offs, loans written off as uncollectable minus recoveries, were higher at 0.5% of loans against a national median of 0.0%. Commercial real estate lending is small at 5.1% of loans against a median of 23.6%, and the real-estate concentration section found the bank did not cross either supervisory line.

On funding, uninsured deposits (balances above the government insurance limit) were 42.4% of deposits against a median of 24.8%, and volatile funding was 14.7% of assets against 9.0%. Offsetting that, cash was 8.1% of assets against a median of 6.2%, and loans were only 56.5% of deposits against 80.2%. The largest outlier is paper losses on bonds held to maturity (bonds the bank plans to keep until they repay), at 34.1% of equity against a national median of 0.0%, while losses on bonds available for sale were 0.9% against 5.6%.

## Understanding the score

As of 2026-06-30 the bank ranked 2,702 out of 4,313 banks, the 37.4th percentile on a scale of 0 to 100 where higher means riskier. The watchlist covers the riskiest 2% of banks, 87 banks that quarter, and this bank was not flagged.

Five factors pushed the score up: the efficiency ratio (operating costs as a share of revenue) at 53.9%, contributing +0.139; the leverage ratio at 7.1%, contributing +0.065; and commercial real estate loans at 5.1% of loans, contributing +0.060. The other two were losses on bonds available for sale at 0.9% of equity, contributing +0.042, and cash at 8.1% of assets, contributing +0.038.

Five larger factors pushed the score down: the Texas ratio at 3.1%, contributing -1.093; the Tier 1 risk-based capital ratio at 12.1%, contributing -0.988; and return on equity (profit as a share of equity) at 12.3%, contributing -0.655. Interest expense at 1.4% of assets contributed -0.435, and return on assets (profit as a share of assets) at 1.1% contributed -0.286. Because the downward pushes were much stronger than the upward ones, the bank sat well outside the watchlist.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 2,522 | 4,589 |  |
| 2024-12-31 | 2,787 | 4,560 |  |
| 2025-03-31 | 3,335 | 4,536 |  |
| 2025-06-30 | 3,211 | 4,494 |  |
| 2025-09-30 | 2,732 | 4,452 |  |
| 2025-12-31 | 2,789 | 4,411 |  |
| 2026-03-31 | 2,819 | 4,353 |  |
| 2026-06-30 | 2,702 | 4,313 |  |

## How its ratios moved

As of 2026-06-30, the bank ranked 2,702 out of 4,313 banks nationally, which places it in the 37.4th percentile, where a higher percentile means riskier. A year earlier it sat in the 28.6th percentile, and the model rated it riskier than a year earlier. Each ratio is compared with the bank's own values over the prior 12 quarters, and 10 of the 30 ratios checked were outside that prior range.

The Tier 1 risk-based capital ratio, a core measure of the bank's cushion for absorbing losses relative to its riskier assets, was 12.1%, just below its prior range of 12.2% to 13.5%, yet at -0.988 model log-odds units it pushed the score down. The total risk-based capital ratio, a broader version of that cushion, was 13.1%, just below its prior range of 13.2% to 14.6%, and at -0.233 model log-odds units it also pushed the score down. Asset growth over the past four quarters was -0.4%, below its prior range of 0.4% to 5.0%, but at -0.088 model log-odds units it pushed the score down rather than up.

Uninsured deposits, meaning deposit balances above the government insurance limit, made up 42.4% of deposits, above their prior range of 38.5% to 41.7%, yet at -0.055 model log-odds units this ratio pushed the score down. Loans as a share of deposits were 56.5%, slightly above the prior range of 50.5% to 56.0%, and at +0.011 model log-odds units this had little effect on the score. Cash as a share of assets was 8.1%, just below its prior range of 8.2% to 14.6%, and at +0.038 model log-odds units this also had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| uninsured deposits as a share of deposits | 42.4% | 38.5% to 41.7% | prior 12 quarters | +1.2 pp | +0.7 pp | -0.055 | pushed the score down |
| asset growth over the past four quarters | -0.4% | 0.4% to 5.0% | prior 12 quarters | -2.6 pp | -4.9 pp | -0.088 | pushed the score down |
| loans as a share of deposits | 56.5% | 50.5% to 56.0% | prior 12 quarters | +0.5 pp | +2.9 pp | +0.011 | little effect on the score |
| the total risk-based capital ratio | 13.1% | 13.2% to 14.6% | prior 12 quarters | -0.1 pp | -1.2 pp | -0.233 | pushed the score down |
| the Tier 1 risk-based capital ratio | 12.1% | 12.2% to 13.5% | prior 12 quarters | -0.1 pp | -1.2 pp | -0.988 | pushed the score down |
| cash as a share of assets | 8.1% | 8.2% to 14.6% | prior 12 quarters | -0.4 pp | -1.1 pp | +0.038 | little effect on the score |

10 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: All Other Over 1 Billion.

This is a general group: the FDIC did not record a lending specialty for this bank.

Peers: 30 banks in the same specialty group and size tier (over $10 billion).

Losses on bonds held to maturity (paper losses on bonds the bank plans to keep until they repay), measured against equity (the owners' cushion that absorbs losses), stood at 34.1%, at the 99.4th percentile nationally, which is unusually high; at the 94.8th percentile among peers, against a peer median of 0.7%, this ratio is unusually high among its peers too. The leverage ratio (core capital as a share of average assets) was 7.1%, at the 1.1st percentile nationally, which is unusually low; at the 21.7th percentile among peers, against a peer median of 9.2%, it is typical for its peer group. Net interest margin (the spread earned on lending and investing) was 2.5%, at the 5.0th percentile nationally, which is unusually low; at the 48.3rd percentile among peers, against a peer median of 2.6%, it is typical for its peer group.

Annualized loan write-offs, net of recoveries (loans written off as uncollectable, minus amounts later recovered), were 0.5% of loans, at the 93.2nd percentile nationally, which is unusually high; at the 66.1st percentile among peers, against a peer median of 0.2%, they are typical for its peer group. Commercial real estate loans (loans on properties such as offices and shops) made up 5.1% of loans, at the 9.7th percentile nationally, which is unusually low; at the 39.7th percentile among peers, against a peer median of 6.5%, this share is typical for its peer group. Overall, 5 of the bank's ratios fall in the national top or bottom 10%, and only 1 of those is also unusual among its peers, the bond losses measure.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| losses on bonds held to maturity, as a share of equity | 34.1% | 99.4th (unusually high) | 0.7% | 94.8th | unusually high among its peers too |
| the leverage ratio (core capital as a share of average assets) | 7.1% | 1.1st (unusually low) | 9.2% | 21.7th | typical for its peer group |
| net interest margin (the spread earned on lending and investing) | 2.5% | 5.0th (unusually low) | 2.6% | 48.3rd | typical for its peer group |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.5% | 93.2nd (unusually high) | 0.2% | 66.1st | typical for its peer group |
| commercial real estate loans as a share of loans | 5.1% | 9.7th (unusually low) | 6.5% | 39.7th | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 4.8% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 45.7% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 17.6% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

Hindsight: the fact sheet for this memo contains no data from after the as-of quarter. It therefore gives no later ranks, no later watchlist flags and no record of whether the bank kept reporting, so this section cannot describe what happened next beyond the score history table added by code.

## Sources

- F1 · Bank name · n/a · Bank Of America N.A. · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NC · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 2,702 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 37.4% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 9.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 7.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 12.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 13.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 5.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 3.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 56.5% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 42.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 14.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 8.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 34.1% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the efficiency ratio (operating costs as a share of revenue), value 53.9%; contribution to the score · 2026-06-30 · +0.139 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F76 · Driver up #2: the leverage ratio (core capital as a share of average assets), value 7.1%; contribution to the score · 2026-06-30 · +0.065 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F77 · Driver up #3: commercial real estate loans as a share of loans, value 5.1%; contribution to the score · 2026-06-30 · +0.060 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F78 · Driver up #4: losses on bonds available for sale, as a share of equity, value 0.9%; contribution to the score · 2026-06-30 · +0.042 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F79 · Driver up #5: cash as a share of assets, value 8.1%; contribution to the score · 2026-06-30 · +0.038 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 3.1%; contribution to the score · 2026-06-30 · -1.093 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 12.1%; contribution to the score · 2026-06-30 · -0.988 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 12.3%; contribution to the score · 2026-06-30 · -0.655 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: annualized interest expense as a share of assets, value 1.4%; contribution to the score · 2026-06-30 · -0.435 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F84 · Driver down #5: return on assets (profit as a share of assets), value 1.1%; contribution to the score · 2026-06-30 · -0.286 · data/analyst/scores.parquet: feature return_on_assets contribution
- F89 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 42.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F90 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 38.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F91 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 41.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F94 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.055 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F95 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F96 · Trend: asset growth over the past four quarters, value at the as-of quarter · 2026-06-30 · -0.4% · data/features/fct_bank_features.parquet: asset_growth_4q
- F97 · Trend: asset growth over the past four quarters, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: asset_growth_4q
- F98 · Trend: asset growth over the past four quarters, highest value in the comparison window · n/a · 5.0% · data/features/fct_bank_features.parquet: asset_growth_4q
- F101 · Trend: asset growth over the past four quarters, contribution to the score (model log-odds units) · 2026-06-30 · -0.088 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F102 · Trend: asset growth over the past four quarters, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F103 · Trend: loans as a share of deposits, value at the as-of quarter · 2026-06-30 · 56.5% · data/features/fct_bank_features.parquet: loans_to_deposits
- F104 · Trend: loans as a share of deposits, lowest value in the comparison window · n/a · 50.5% · data/features/fct_bank_features.parquet: loans_to_deposits
- F105 · Trend: loans as a share of deposits, highest value in the comparison window · n/a · 56.0% · data/features/fct_bank_features.parquet: loans_to_deposits
- F108 · Trend: loans as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · +0.011 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F109 · Trend: loans as a share of deposits, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F110 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2026-06-30 · 13.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F111 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 13.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F112 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 14.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F115 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2026-06-30 · -0.233 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F116 · Trend: the total risk-based capital ratio, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F117 · Trend: the Tier 1 risk-based capital ratio, value at the as-of quarter · 2026-06-30 · 12.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F118 · Trend: the Tier 1 risk-based capital ratio, lowest value in the comparison window · n/a · 12.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F119 · Trend: the Tier 1 risk-based capital ratio, highest value in the comparison window · n/a · 13.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F122 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2026-06-30 · -0.988 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F123 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F124 · Trend: cash as a share of assets, value at the as-of quarter · 2026-06-30 · 8.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F125 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 8.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F126 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 14.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F129 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.038 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F130 · Trend: cash as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature cash_to_assets contribution
- F131 · Trend: ratios outside their own prior range · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F133 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F134 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F136 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 28.6% · data/analyst/scores.parquet: percentile
- F137 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F141 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 34.1% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F142 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.4th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F143 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F144 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 94.8th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F145 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F146 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F147 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 7.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F148 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 1.1st · data/features/fct_bank_features.parquet: leverage_ratio
- F149 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F150 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 21.7th · data/features/fct_bank_features.parquet: leverage_ratio
- F151 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 9.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F152 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: leverage_ratio
- F153 · Peers: net interest margin (the spread earned on lending and investing), bank value at the as-of quarter · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: net_interest_margin
- F154 · Peers: net interest margin (the spread earned on lending and investing), national percentile (100 = highest value among all banks) · 2026-06-30 · 5.0th · data/features/fct_bank_features.parquet: net_interest_margin
- F155 · Peers: net interest margin (the spread earned on lending and investing), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: net_interest_margin
- F156 · Peers: net interest margin (the spread earned on lending and investing), percentile among its peers (100 = highest value) · 2026-06-30 · 48.3rd · data/features/fct_bank_features.parquet: net_interest_margin
- F157 · Peers: net interest margin (the spread earned on lending and investing), peer median · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F158 · Peers: net interest margin (the spread earned on lending and investing), reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: net_interest_margin
- F159 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F160 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 93.2nd · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F161 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F162 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 66.1st · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F163 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F164 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F165 · Peers: commercial real estate loans as a share of loans, bank value at the as-of quarter · 2026-06-30 · 5.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F166 · Peers: commercial real estate loans as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 9.7th · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F167 · Peers: commercial real estate loans as a share of loans, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F168 · Peers: commercial real estate loans as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 39.7th · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F169 · Peers: commercial real estate loans as a share of loans, peer median · 2026-06-30 · 6.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F170 · Peers: commercial real estate loans as a share of loans, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F172 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 5 · data/features/fct_bank_features.parquet
- F173 · Peers: those ratios also unusual among peers · 2026-06-30 · 1 · data/features/fct_bank_features.parquet
- F175 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
