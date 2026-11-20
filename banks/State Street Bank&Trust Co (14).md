---
cert: 14
name: "State Street Bank&Trust Co"
as_of: 2026-06-30
rank: 1088
n_banks: 4313
percentile: 74.79712497101785
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:00"
writer_model: "claude-opus-5-5"
checked: true
---

# State Street Bank&Trust Co (cert 14)

## Summary

As of 2026-06-30, State Street Bank&Trust Co ranked 1,088 out of 4,313 banks nationally on Canary's model score, placing it in the 74.8th percentile, where a higher percentile means the model sees more risk. It was not flagged on the watchlist that quarter. Its capital cushion against total assets was thin, with a leverage ratio (core capital as a share of average assets) of 5.8% against a national median of 11.0%, and 75.9% of its deposits were uninsured (above the government insurance limit), far above the national median of 24.8%. On the other side, its troubled-loan measures were low and its profits solid, and the model weighed those strengths toward lower risk.

## Warning signs in the data

Capital, the owners' cushion against losses, looks thin when measured against all assets: equity was 7.1% of assets against a national median of 10.6%, and the leverage ratio was 5.8% against a median of 11.0%. A different measure points the other way: the Tier 1 risk-based capital ratio, which counts riskier assets more heavily, was 14.7%, close to the national median of 14.6%.

Funding leans on large, less stable deposits: uninsured deposits were 75.9% of deposits against a national median of 24.8%, volatile funding (money more likely to leave quickly) was 22.7% of assets against 9.0%, and core deposits (steady, everyday deposits) were 54.8% of assets against 75.5%. At the same time, cash was 36.1% of assets against a national median of 6.2%, and loans were only 16.0% of deposits against 80.2%, so much of its money is held in cash rather than lent out.

Unrealized losses on bonds held to maturity (bonds the bank plans to keep until they pay back) equaled 14.4% of equity, well above the national median of 0.0%, while losses on bonds available for sale were -0.2% of equity against a median of 5.6%. Credit quality looks sound: loans 90 or more days past due or not accruing interest were 0.6% of loans against a median of 0.5%, and nonaccrual assets and foreclosed property were 0.1% of assets against 0.3%, though loan-loss reserves (money set aside for bad loans) were 0.3% of loans against a median of 1.2%. Commercial real estate loans were just 2.5% of loans against a national median of 23.6%, and the real-estate concentration section found the bank did not cross either supervisory line.

## Understanding the score

State Street Bank&Trust Co ranked 1,088 out of 4,313 banks at 2026-06-30, which is the 74.8th percentile on a scale of 0 to 100 where higher means riskier. It was not flagged on the watchlist, which covers the riskiest 2% of banks and held 87 banks that quarter.

The five factors that pushed the score up most were construction loans at 0.0% of loans (+0.266), core deposits at 54.8% of assets (+0.227), commercial real estate loans at 2.5% of loans (+0.126), equity at 7.1% of assets (+0.060), and the leverage ratio at 5.8% (+0.057). The five factors that pushed the score down most were the Texas ratio (troubled assets against capital plus reserves) at 1.0% (-1.155), the Tier 1 risk-based capital ratio at 14.7% (-0.904), return on equity (profit as a share of equity) at 13.0% (-0.575), loans 90 or more days past due or not accruing interest at 0.6% of loans (-0.344), and total assets of $412.6 billion (-0.337). The downward pulls were larger than the upward ones, which is why the bank sat outside the watchlist despite its thin capital against total assets.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,062 | 4,589 |  |
| 2024-12-31 | 1,160 | 4,560 |  |
| 2025-03-31 | 1,019 | 4,536 |  |
| 2025-06-30 | 941 | 4,494 |  |
| 2025-09-30 | 889 | 4,452 |  |
| 2025-12-31 | 997 | 4,411 |  |
| 2026-03-31 | 1,210 | 4,353 |  |
| 2026-06-30 | 1,088 | 4,313 |  |

## How its ratios moved

As of Q2 2026, State Street Bank&Trust Co ranked 1,088 out of 4,313 banks nationally, placing it in the 74.8th percentile, where a higher percentile means the model sees more risk. A year earlier, on 2025-06-30, it sat in the 79.1st percentile, and the model rated it safer than a year earlier. Each ratio is compared with its own prior range over the prior 12 quarters, and 16 of the 30 ratios checked fell outside that range, with the 6 furthest outside discussed here.

Return on equity (profit as a share of the owners' stake) was 13.0%, above its prior range of 9.7% to 10.3%, and its contribution of -0.575 model log-odds units pushed the score down. The efficiency ratio (operating costs as a share of revenue) was 66.1%, below its prior range of 68.7% to 70.8%, and its contribution of -0.017 had little effect on the score. Core deposits (steady, everyday customer deposits) made up 54.8% of assets, above their prior range of 48.5% to 52.5%, and their contribution of +0.227 pushed the score up. Brokered deposits (money placed at the bank through middlemen) were 4.5% of deposits, below their prior range of 4.9% to 6.3%, and their contribution of -0.170 pushed the score down. Securities (mainly bonds the bank holds) were 26.0% of assets, below their prior range of 27.9% to 36.8%, and their contribution of -0.160 pushed the score down. Equity (the owners' loss-absorbing cushion) was 7.1% of assets, below its prior range of 7.4% to 9.2%, and its contribution of +0.060 pushed the score up.

Being outside its usual range did not always mean more risk in the model's eyes: return on equity, brokered deposits and securities all moved outside their ranges yet pushed the score down, and the efficiency ratio moved outside its range but had little effect on the score. Only the core deposit and equity ratios pushed the score up.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 13.0% | 9.7% to 10.3% | same quarter, prior 3 years | n/a | +2.8 pp | -0.575 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 66.1% | 68.7% to 70.8% | same quarter, prior 3 years | n/a | -3.3 pp | -0.017 | little effect on the score |
| core deposits as a share of assets | 54.8% | 48.5% to 52.5% | prior 12 quarters | +2.6 pp | +3.6 pp | +0.227 | pushed the score up |
| brokered deposits as a share of deposits | 4.5% | 4.9% to 6.3% | prior 12 quarters | -0.6 pp | -0.6 pp | -0.170 | pushed the score down |
| securities as a share of assets | 26.0% | 27.9% to 36.8% | prior 12 quarters | -1.9 pp | -4.5 pp | -0.160 | pushed the score down |
| equity as a share of assets | 7.1% | 7.4% to 9.2% | prior 12 quarters | -0.4 pp | -0.8 pp | +0.060 | pushed the score up |

16 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: All Other Over 1 Billion.

This is a general group: the FDIC did not record a lending specialty for this bank.

Peers: 30 banks in the same specialty group and size tier (over $10 billion).

The bank's leverage ratio, its core capital (the owners' cushion against losses) as a share of average assets, was 5.8%, which is unusually low nationally at the 0.6th percentile; among its peers it sits at the 5.0th percentile against a peer median of 9.2%, which is unusually low among its peers too. Uninsured deposits, meaning balances above the government insurance limit, made up 75.9% of deposits, which is unusually high nationally at the 99.2nd percentile; among its peers it sits at the 94.6th percentile against a peer median of 40.3%, which is unusually high among its peers too. Losses on bonds available for sale (bonds the bank may sell before they mature), as a share of equity, were -0.2%, which is unusually low nationally at the 1.0th percentile; among its peers it sits at the 5.2nd percentile against a peer median of 3.6%, which is unusually low among its peers too. Loans as a share of deposits were 16.0%, which is unusually low nationally at the 2.8th percentile; among its peers it sits at the 8.3rd percentile against a peer median of 63.6%, which is unusually low among its peers too.

The net interest margin, the spread the bank earns on lending and investing, was 1.2%, which is unusually low nationally at the 1.1st percentile; among its peers it sits at the 15.0th percentile against a peer median of 2.6%, which is typical for its peer group. Loan-loss reserves, money set aside to cover loans that may go bad, were 0.3% of loans, which is unusually low nationally at the 1.1st percentile; among its peers it sits at the 23.2nd percentile against a peer median of 0.9%, which is typical for its peer group. Losses on bonds held to maturity (bonds the bank plans to keep until they pay back), as a share of equity, were 14.4%, which is unusually high nationally at the 97.1st percentile; among its peers it sits at the 81.0th percentile against a peer median of 0.7%, which is typical for its peer group. Cash made up 36.1% of assets, which is unusually high nationally at the 97.1st percentile; among its peers it sits at the 88.3rd percentile against a peer median of 9.4%, which is typical for its peer group.

Overall, 13 of the bank's ratios fall in the national top or bottom 10%, and 4 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the leverage ratio (core capital as a share of average assets) | 5.8% | 0.6th (unusually low) | 9.2% | 5.0th | unusually low among its peers too |
| uninsured deposits as a share of deposits | 75.9% | 99.2nd (unusually high) | 40.3% | 94.6th | unusually high among its peers too |
| losses on bonds available for sale, as a share of equity | -0.2% | 1.0th (unusually low) | 3.6% | 5.2nd | unusually low among its peers too |
| net interest margin (the spread earned on lending and investing) | 1.2% | 1.1st (unusually low) | 2.6% | 15.0th | typical for its peer group |
| loan-loss reserves as a share of loans | 0.3% | 1.1st (unusually low) | 0.9% | 23.2nd | typical for its peer group |
| loans as a share of deposits | 16.0% | 2.8th (unusually low) | 63.6% | 8.3rd | unusually low among its peers too |
| losses on bonds held to maturity, as a share of equity | 14.4% | 97.1st (unusually high) | 0.7% | 81.0th | typical for its peer group |
| cash as a share of assets | 36.1% | 97.1st (unusually high) | 9.4% | 88.3rd | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 16.5% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 14.6% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

This section looks past the as-of quarter, but the fact sheet contains no data from after that quarter for this bank. We therefore cannot report its later ranks, any later watchlist flags, or whether it kept filing reports; the outcome case for this bank is marked quiet.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2026-06-30 · 1,088 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 74.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 5.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2026-06-30 · 23.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F49 · Bank: loans as a share of deposits · 2026-06-30 · 16.0% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 75.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 54.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 22.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 36.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 14.4% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · -0.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: construction loans as a share of loans, value 0.0%; contribution to the score · 2026-06-30 · +0.266 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F76 · Driver up #2: core deposits as a share of assets, value 54.8%; contribution to the score · 2026-06-30 · +0.227 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F77 · Driver up #3: commercial real estate loans as a share of loans, value 2.5%; contribution to the score · 2026-06-30 · +0.126 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F78 · Driver up #4: equity as a share of assets, value 7.1%; contribution to the score · 2026-06-30 · +0.060 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F79 · Driver up #5: the leverage ratio (core capital as a share of average assets), value 5.8%; contribution to the score · 2026-06-30 · +0.057 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 1.0%; contribution to the score · 2026-06-30 · -1.155 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 14.7%; contribution to the score · 2026-06-30 · -0.904 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 13.0%; contribution to the score · 2026-06-30 · -0.575 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 0.6%; contribution to the score · 2026-06-30 · -0.344 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F84 · Driver down #5: total assets, value $412.6 billion; contribution to the score · 2026-06-30 · -0.337 · data/analyst/scores.parquet: feature log_total_assets contribution
- F89 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 13.0% · data/features/fct_bank_features.parquet: return_on_equity
- F90 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 9.7% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 10.3% · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.575 · data/analyst/scores.parquet: feature return_on_equity contribution
- F94 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 66.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F96 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 68.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 70.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.017 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F100 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F101 · Trend: core deposits as a share of assets, value at the as-of quarter · 2026-06-30 · 54.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F102 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 48.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F103 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 52.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F106 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.227 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F107 · Trend: core deposits as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F108 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F109 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 4.9% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F110 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 6.3% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F113 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.170 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F114 · Trend: brokered deposits as a share of deposits, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F115 · Trend: securities as a share of assets, value at the as-of quarter · 2026-06-30 · 26.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F116 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 27.9% · data/features/fct_bank_features.parquet: securities_to_assets
- F117 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 36.8% · data/features/fct_bank_features.parquet: securities_to_assets
- F120 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.160 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F121 · Trend: securities as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature securities_to_assets contribution
- F122 · Trend: equity as a share of assets, value at the as-of quarter · 2026-06-30 · 7.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F123 · Trend: equity as a share of assets, lowest value in the comparison window · n/a · 7.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F124 · Trend: equity as a share of assets, highest value in the comparison window · n/a · 9.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F127 · Trend: equity as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.060 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F128 · Trend: equity as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature equity_to_assets contribution
- F129 · Trend: ratios outside their own prior range · 2026-06-30 · 16 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F132 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F134 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 79.1% · data/analyst/scores.parquet: percentile
- F135 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it safer than a year earlier · data/analyst/scores.parquet: percentile
- F139 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 5.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F140 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.6th · data/features/fct_bank_features.parquet: leverage_ratio
- F141 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F142 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 5.0th · data/features/fct_bank_features.parquet: leverage_ratio
- F143 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 9.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F144 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F145 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 75.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F146 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.2nd · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F147 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F148 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 94.6th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F149 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 40.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F150 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F151 · Peers: losses on bonds available for sale, as a share of equity, bank value at the as-of quarter · 2026-06-30 · -0.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F152 · Peers: losses on bonds available for sale, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 1.0th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F153 · Peers: losses on bonds available for sale, as a share of equity, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F154 · Peers: losses on bonds available for sale, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 5.2nd · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F155 · Peers: losses on bonds available for sale, as a share of equity, peer median · 2026-06-30 · 3.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F156 · Peers: losses on bonds available for sale, as a share of equity, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F157 · Peers: net interest margin (the spread earned on lending and investing), bank value at the as-of quarter · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F158 · Peers: net interest margin (the spread earned on lending and investing), national percentile (100 = highest value among all banks) · 2026-06-30 · 1.1st · data/features/fct_bank_features.parquet: net_interest_margin
- F159 · Peers: net interest margin (the spread earned on lending and investing), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: net_interest_margin
- F160 · Peers: net interest margin (the spread earned on lending and investing), percentile among its peers (100 = highest value) · 2026-06-30 · 15.0th · data/features/fct_bank_features.parquet: net_interest_margin
- F161 · Peers: net interest margin (the spread earned on lending and investing), peer median · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F162 · Peers: net interest margin (the spread earned on lending and investing), reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: net_interest_margin
- F163 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F164 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 1.1st · data/features/fct_bank_features.parquet: allowance_to_loans
- F165 · Peers: loan-loss reserves as a share of loans, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: allowance_to_loans
- F166 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 23.2nd · data/features/fct_bank_features.parquet: allowance_to_loans
- F167 · Peers: loan-loss reserves as a share of loans, peer median · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: allowance_to_loans
- F168 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: allowance_to_loans
- F169 · Peers: loans as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 16.0% · data/features/fct_bank_features.parquet: loans_to_deposits
- F170 · Peers: loans as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 2.8th · data/features/fct_bank_features.parquet: loans_to_deposits
- F171 · Peers: loans as a share of deposits, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: loans_to_deposits
- F172 · Peers: loans as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 8.3rd · data/features/fct_bank_features.parquet: loans_to_deposits
- F173 · Peers: loans as a share of deposits, peer median · 2026-06-30 · 63.6% · data/features/fct_bank_features.parquet: loans_to_deposits
- F174 · Peers: loans as a share of deposits, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: loans_to_deposits
- F175 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 14.4% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F176 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.1st · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F177 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F178 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 81.0th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F179 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F180 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F181 · Peers: cash as a share of assets, bank value at the as-of quarter · 2026-06-30 · 36.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F182 · Peers: cash as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.1st · data/features/fct_bank_features.parquet: cash_to_assets
- F183 · Peers: cash as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: cash_to_assets
- F184 · Peers: cash as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 88.3rd · data/features/fct_bank_features.parquet: cash_to_assets
- F185 · Peers: cash as a share of assets, peer median · 2026-06-30 · 9.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F186 · Peers: cash as a share of assets, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: cash_to_assets
- F188 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 13 · data/features/fct_bank_features.parquet
- F189 · Peers: those ratios also unusual among peers · 2026-06-30 · 4 · data/features/fct_bank_features.parquet
- F191 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
