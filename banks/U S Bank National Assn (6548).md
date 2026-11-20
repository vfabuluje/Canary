---
cert: 6548
name: "U S Bank National Assn"
as_of: 2026-06-30
rank: 1765
n_banks: 4313
percentile: 59.10039415719916
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:55:44"
writer_model: "claude-opus-5-5"
checked: true
---

# U S Bank National Assn (cert 6548)

## Summary

As of 2026-06-30, U S Bank National Assn, an Ohio bank with $705.6 billion in total assets, ranked 1,765 out of 4,313 banks nationally on Canary's risk score, which places it at the 59.1st percentile on a 0 to 100 scale where higher means riskier. It was not flagged on the watchlist that quarter. Against the national median, its capital cushions are somewhat thinner, and its share of uninsured deposits and its paper losses on bonds are much higher. The peer section finds these standouts typical for very large banks of its kind, so the picture is mixed rather than alarming.

## Warning signs in the data

Capital, the owners' money that absorbs losses, sits below the national median on every measure: equity was 9.8% of assets against a median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 9.5% against 11.0%. The Tier 1 risk-based capital ratio (core capital measured against riskier assets) was 13.0% against a median of 14.6%, and the total risk-based capital ratio was 14.9% against 15.8%.

On credit quality, loans 90+ days past due or not accruing interest were 1.4% of loans, well above the national median of 0.5%, and annualized net write-offs (loans written off as uncollectable, minus recoveries) were 0.5% of loans against a median of 0.0%. The Texas ratio (troubled assets against capital plus reserves) was 7.9%, above the median of 2.9%, though still a low reading in absolute terms.

On funding, uninsured deposits (balances above the government insurance limit) made up 52.2% of deposits, roughly far above the national median of 24.8%, and brokered deposits (money placed through intermediaries) were 6.1% against a median of 0.0%. Losses on bonds held to maturity (the drop in value of bonds the bank plans to keep) equaled 13.7% of equity against a national median of 0.0%, and losses on bonds available for sale were 6.4% against 5.6%. Offsetting this, cash was 9.3% of assets against a median of 6.2%, and the peer section judges each of these standouts typical for its group of large banks, so the national and peer views point different ways.

## Understanding the score

As of 2026-06-30, the bank ranked 1,765 out of 4,313 banks, at the 59.1st percentile, where higher means riskier. It was not flagged on the watchlist, which covers the top 2% of banks and held 87 banks that quarter.

Five features pushed the score up most: losses on bonds available for sale at 6.4% of equity (+0.479), the efficiency ratio (operating costs as a share of revenue) at 54.6% (+0.276), and commercial real estate loans at 6.5% of loans (+0.231). Smaller upward pushes came from cash at 9.3% of assets (+0.024) and loan-loss reserves (the cushion held against bad loans) at 1.8% of loans (+0.022).

Five features pulled the score down most: the Tier 1 risk-based capital ratio at 13.0% (-0.940), the Texas ratio at 7.9% (-0.907), and return on equity (profit as a share of equity) at 12.4% (-0.733). Losses on bonds held to maturity at 13.7% of equity (-0.333) and loans 30-89 days past due at 0.2% of assets (-0.300) also lowered the score.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 2,990 | 4,589 |  |
| 2024-12-31 | 3,073 | 4,560 |  |
| 2025-03-31 | 2,849 | 4,536 |  |
| 2025-06-30 | 2,071 | 4,494 |  |
| 2025-09-30 | 1,319 | 4,452 |  |
| 2025-12-31 | 1,473 | 4,411 |  |
| 2026-03-31 | 1,482 | 4,353 |  |
| 2026-06-30 | 1,765 | 4,313 |  |

## How its ratios moved

As of 2026-06-30, the bank ranked 1,765 out of 4,313 banks nationally, placing it at the 59.1st percentile on a 0 to 100 scale where higher means riskier. On 2025-06-30 it sat at the 53.9th percentile, and the model rated it riskier than a year earlier. Each ratio is compared with its own prior range, usually over the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios, and 13 of the 30 ratios checked fell outside that range.

The efficiency ratio (operating costs as a share of revenue) was 54.6%, below its prior range of 56.8% to 60.3%, and its contribution of +0.276 model log-odds units (positive values raise the score) pushed the score up. Return on equity (profit as a share of shareholders' money) was 12.4%, above its prior range of 9.8% to 11.5%, yet despite being outside that range its contribution of -0.733 pushed the score down. Loans as a share of deposits reached 74.9%, above its prior range of 68.4% to 73.2%, but its contribution of -0.063 still pushed the score down.

Borrowings from the Federal Home Loan Banks (government-sponsored lenders to banks) were 3.8% of assets, above their prior range of 1.8% to 3.3%, yet their contribution of -0.015 had little effect on the score. Core deposits (stable, everyday customer deposits) were 69.5% of assets, below their prior range of 70.1% to 72.6%, but their contribution of -0.140 pushed the score down. Uninsured deposits (balances above the government insurance limit) were 52.2% of deposits, above their prior range of 49.3% to 51.8%, yet their contribution of -0.031 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 54.6% | 56.8% to 60.3% | same quarter, prior 3 years | n/a | -2.2 pp | +0.276 | pushed the score up |
| return on equity (profit as a share of equity) | 12.4% | 9.8% to 11.5% | same quarter, prior 3 years | n/a | +0.9 pp | -0.733 | pushed the score down |
| loans as a share of deposits | 74.9% | 68.4% to 73.2% | prior 12 quarters | +1.7 pp | +4.1 pp | -0.063 | pushed the score down |
| Federal Home Loan Bank borrowings as a share of assets | 3.8% | 1.8% to 3.3% | prior 12 quarters | +2.1 pp | +1.2 pp | -0.015 | little effect on the score |
| core deposits as a share of assets | 69.5% | 70.1% to 72.6% | prior 12 quarters | -2.1 pp | -0.6 pp | -0.140 | pushed the score down |
| uninsured deposits as a share of deposits | 52.2% | 49.3% to 51.8% | prior 12 quarters | +0.4 pp | +2.5 pp | -0.031 | little effect on the score |

13 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: All Other Over 1 Billion.

This is a general group: the FDIC did not record a lending specialty for this bank.

Peers: 30 banks in the same specialty group and size tier (over $10 billion).

Losses on bonds held to maturity (the drop in value of bonds the bank plans to keep, measured against its equity, the owners' cushion) were 13.7% of equity, at the 96.9th national percentile, which is unusually high nationally; among its peers it sat at the 77.6th percentile against a peer median of 0.7%, which is typical for its peer group. Uninsured deposits (balances above the government insurance limit) made up 52.2% of deposits, at the 95.4th national percentile, which is unusually high nationally; among its peers it sat at the 76.8th percentile against a peer median of 40.3%, which is typical for its peer group.

Annualized loan write-offs net of recoveries (loans written off as uncollectable, minus amounts later recovered) were 0.5% of loans, at the 94.0th national percentile, which is unusually high nationally; among its peers it sat at the 73.2nd percentile against a peer median of 0.2%, which is typical for its peer group. The annualized provision for loan losses (money set aside for expected loan losses) was 0.3% of assets, at the 91.4th national percentile, which is unusually high nationally; among its peers it sat at the 70.7th percentile against a peer median of 0.1%, which is typical for its peer group. Loan-loss reserves (the cushion already held against bad loans) were 1.8% of loans, at the 90.1st national percentile, which is unusually high nationally; among its peers it sat at the 76.8th percentile against a peer median of 0.9%, which is typical for its peer group. The net interest margin (the spread earned on lending and investing) was 2.9%, at the 9.5th national percentile, which is unusually low nationally; among its peers it sat at the 58.3rd percentile against a peer median of 2.6%, which is typical for its peer group.

Overall, 6 of the bank's ratios fall in the national top or bottom 10%, but 0 of those are also unusual among its peers, so its standouts look normal for large banks of its kind.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| losses on bonds held to maturity, as a share of equity | 13.7% | 96.9th (unusually high) | 0.7% | 77.6th | typical for its peer group |
| uninsured deposits as a share of deposits | 52.2% | 95.4th (unusually high) | 40.3% | 76.8th | typical for its peer group |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.5% | 94.0th (unusually high) | 0.2% | 73.2nd | typical for its peer group |
| annualized provision for loan losses as a share of assets | 0.3% | 91.4th (unusually high) | 0.1% | 70.7th | typical for its peer group |
| net interest margin (the spread earned on lending and investing) | 2.9% | 9.5th (unusually low) | 2.6% | 58.3rd | typical for its peer group |
| loan-loss reserves as a share of loans | 1.8% | 90.1st (unusually high) | 0.9% | 76.8th | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 13.2% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 80.7% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 1.4% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

This section looks past the as-of quarter, using hindsight. The fact sheet for this memo contains no data from after the as-of quarter, so later ranks, watchlist flags and whether the bank kept reporting cannot be described here. The score history table and outcome banner added below show what the record holds.

## Sources

- F1 · Bank name · n/a · U S Bank National Assn · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · OH · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 1,765 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 59.1% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 9.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 13.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 14.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 1.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 52.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 6.1% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 9.3% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 13.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 6.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $705.6 billion · data/features/fct_bank_features.parquet: log_total_assets
- F75 · Driver up #1: losses on bonds available for sale, as a share of equity, value 6.4%; contribution to the score · 2026-06-30 · +0.479 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F76 · Driver up #2: the efficiency ratio (operating costs as a share of revenue), value 54.6%; contribution to the score · 2026-06-30 · +0.276 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F77 · Driver up #3: commercial real estate loans as a share of loans, value 6.5%; contribution to the score · 2026-06-30 · +0.231 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F78 · Driver up #4: cash as a share of assets, value 9.3%; contribution to the score · 2026-06-30 · +0.024 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F79 · Driver up #5: loan-loss reserves as a share of loans, value 1.8%; contribution to the score · 2026-06-30 · +0.022 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 13.0%; contribution to the score · 2026-06-30 · -0.940 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 7.9%; contribution to the score · 2026-06-30 · -0.907 · data/analyst/scores.parquet: feature texas_ratio contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 12.4%; contribution to the score · 2026-06-30 · -0.733 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: losses on bonds held to maturity, as a share of equity, value 13.7%; contribution to the score · 2026-06-30 · -0.333 · data/analyst/scores.parquet: feature htm_unrealized_loss_to_equity contribution
- F84 · Driver down #5: loans 30-89 days past due, as a share of assets, value 0.2%; contribution to the score · 2026-06-30 · -0.300 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F89 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 54.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F90 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 56.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F91 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 60.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.276 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F94 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F95 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 12.4% · data/features/fct_bank_features.parquet: return_on_equity
- F96 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 9.8% · data/features/fct_bank_features.parquet: return_on_equity
- F97 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 11.5% · data/features/fct_bank_features.parquet: return_on_equity
- F99 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.733 · data/analyst/scores.parquet: feature return_on_equity contribution
- F100 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F101 · Trend: loans as a share of deposits, value at the as-of quarter · 2026-06-30 · 74.9% · data/features/fct_bank_features.parquet: loans_to_deposits
- F102 · Trend: loans as a share of deposits, lowest value in the comparison window · n/a · 68.4% · data/features/fct_bank_features.parquet: loans_to_deposits
- F103 · Trend: loans as a share of deposits, highest value in the comparison window · n/a · 73.2% · data/features/fct_bank_features.parquet: loans_to_deposits
- F106 · Trend: loans as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.063 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F107 · Trend: loans as a share of deposits, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F108 · Trend: Federal Home Loan Bank borrowings as a share of assets, value at the as-of quarter · 2026-06-30 · 3.8% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F109 · Trend: Federal Home Loan Bank borrowings as a share of assets, lowest value in the comparison window · n/a · 1.8% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F110 · Trend: Federal Home Loan Bank borrowings as a share of assets, highest value in the comparison window · n/a · 3.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F113 · Trend: Federal Home Loan Bank borrowings as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.015 · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F114 · Trend: Federal Home Loan Bank borrowings as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F115 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 69.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F116 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 70.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F117 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 72.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F120 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.140 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F121 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F122 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 52.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F123 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 49.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F124 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 51.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F127 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.031 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F128 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F129 · Trend: ratios outside their own prior range · 2026-06-30 · 13 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F132 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F133 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F134 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 53.9% · data/analyst/scores.parquet: percentile
- F135 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F139 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 13.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F140 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.9th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F141 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F142 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 77.6th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F143 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F144 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F145 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 52.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F146 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 95.4th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F147 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F148 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 76.8th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F149 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 40.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F150 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F151 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F152 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 94.0th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F153 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F154 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 73.2nd · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F155 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F156 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F157 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F158 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 91.4th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F159 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F160 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 70.7th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F161 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F162 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F163 · Peers: net interest margin (the spread earned on lending and investing), bank value at the as-of quarter · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F164 · Peers: net interest margin (the spread earned on lending and investing), national percentile (100 = highest value among all banks) · 2026-06-30 · 9.5th · data/features/fct_bank_features.parquet: net_interest_margin
- F165 · Peers: net interest margin (the spread earned on lending and investing), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: net_interest_margin
- F166 · Peers: net interest margin (the spread earned on lending and investing), percentile among its peers (100 = highest value) · 2026-06-30 · 58.3rd · data/features/fct_bank_features.parquet: net_interest_margin
- F167 · Peers: net interest margin (the spread earned on lending and investing), peer median · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F168 · Peers: net interest margin (the spread earned on lending and investing), reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: net_interest_margin
- F169 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2026-06-30 · 1.8% · data/features/fct_bank_features.parquet: allowance_to_loans
- F170 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 90.1st · data/features/fct_bank_features.parquet: allowance_to_loans
- F171 · Peers: loan-loss reserves as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: allowance_to_loans
- F172 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 76.8th · data/features/fct_bank_features.parquet: allowance_to_loans
- F173 · Peers: loan-loss reserves as a share of loans, peer median · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: allowance_to_loans
- F174 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: allowance_to_loans
- F176 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F177 · Peers: those ratios also unusual among peers · 2026-06-30 · 0 · data/features/fct_bank_features.parquet
- F179 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
