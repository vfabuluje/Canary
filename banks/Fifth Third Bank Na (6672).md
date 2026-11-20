---
cert: 6672
name: "Fifth Third Bank Na"
as_of: 2026-06-30
rank: 3764
n_banks: 4313
percentile: 12.752144678877809
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:01"
writer_model: "claude-opus-5-5"
checked: true
---

# Fifth Third Bank Na (cert 6672)

## Summary

As of 2026-06-30, Fifth Third Bank Na of OH ranked 3,764 of 4,313 banks nationally, which puts it in the 12.8th percentile, where higher means riskier. It was not flagged on Canary's watchlist, and the model rated it safer than a year earlier, when it sat in the 37.5th percentile. The data do show points worth watching: deposits grew 43.5% over the past four quarters, uninsured deposits (balances above the government insurance limit) were 44.4% of deposits, and its risk-based capital ratios sat below the national medians. The trend section points the other way from the score on profits, since return on equity fell below its own prior range while the model still treated it as lowering the score.

## Warning signs in the data

Capital, the cushion that absorbs losses, is mixed: equity was 12.6% of assets against a national median of 10.6%, but the leverage ratio (core capital as a share of average assets) was 10.0% against a median of 11.0%. The Tier 1 risk-based capital ratio, which weighs assets by riskiness, was 11.7% against a median of 14.6%, and the total risk-based capital ratio was 13.0% against 15.8%.

On credit quality, loans 90+ days past due or not accruing interest were 0.8% of loans against a median of 0.5%, and annualized write-offs (loans written off as lost, net of recoveries) were 0.3% against 0.0%. Its loan-loss reserves, money set aside for expected bad loans, were 1.6% of loans, above the median of 1.2%. Separately, the code-written real-estate section found the bank did not cross either regulatory concentration line.

On funding, uninsured deposits were 44.4% of deposits, well above the national median of 24.8%, and deposits grew 43.5% over the past four quarters against a median of 4.2%. Federal Home Loan Bank borrowings were 2.0% of assets against a median of 0.2%, though volatile funding (money likely to leave quickly) was 3.4% against 9.0% and cash was 7.9% against 6.2%. Unrealized losses on bonds available for sale were 8.4% of equity against a median of 5.6%, and losses on bonds held to maturity were 0.4% against 0.0%.

## Understanding the score

As of 2026-06-30, the bank ranked 3,764 of 4,313 banks, placing it in the 12.8th percentile on a scale of 0 to 100 where higher means riskier. Canary's watchlist covers the top 2% of banks, 87 banks that quarter, and this bank was not flagged.

Four features pushed the score up: deposit growth over the past four quarters at 43.5% added +0.270, and commercial real estate loans at 12.0% of loans added +0.115. Losses on bonds available for sale at 8.4% of equity added +0.060, and net loan write-offs at 0.3% of loans added +0.002. The commercial real estate share counted upward even though it is below the national median, so that driver reflects the model's pattern rather than a high reading.

Five features pushed the score down: the Texas ratio (troubled assets against capital plus reserves) at 3.8% contributed -1.143, and the Tier 1 risk-based capital ratio at 11.7% contributed -0.874. Return on equity at 7.9% contributed -0.673, loans 90+ days past due or not accruing at 0.8% contributed -0.353, and interest expense at 1.3% of assets contributed -0.332.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,425 | 4,589 |  |
| 2024-12-31 | 1,154 | 4,560 |  |
| 2025-03-31 | 3,460 | 4,536 |  |
| 2025-06-30 | 2,808 | 4,494 |  |
| 2025-09-30 | 2,016 | 4,452 |  |
| 2025-12-31 | 1,514 | 4,411 |  |
| 2026-03-31 | 3,449 | 4,353 |  |
| 2026-06-30 | 3,764 | 4,313 |  |

## How its ratios moved

As of 2026-06-30, the bank ranked 3,764 of 4,313 banks nationally, placing it in the 12.8th percentile, where higher means riskier. A year earlier it sat in the 37.5th percentile, and the model rated it safer than a year earlier. Canary compared 30 of the bank's ratios with their own prior range, usually the prior 12 quarters, and 11 of them fell outside that range; the 6 furthest outside are discussed here.

The efficiency ratio, which is operating costs as a share of revenue, was 66.3%, above its prior range of 55.0% to 57.4% after rising +10.7 pp over four quarters. Even though the efficiency ratio of 66.3% sat outside its range, its contribution was -0.115 model log-odds units, so it pushed the score down. Return on equity, profit as a share of shareholders' equity, was 7.9%, below its prior range of 11.4% to 13.0%, yet its contribution of -0.673 pushed the score down. Return on assets, profit as a share of total assets, was 1.0%, below its prior range of 1.2% to 1.3%, and its contribution of -0.262 also pushed the score down.

Net interest margin, the spread earned on lending and investing, was 3.8%, above its prior range of 3.2% to 3.5%, but its contribution of -0.048 had little effect on the score. Securities as a share of assets were 20.6%, below their prior range of 20.9% to 23.9%, while the contribution of -0.169 pushed the score down. Loans as a share of deposits were 73.2%, just above the prior range of 65.4% to 72.7%, and the contribution of -0.068 pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 66.3% | 55.0% to 57.4% | same quarter, prior 3 years | n/a | +10.7 pp | -0.115 | pushed the score down |
| return on equity (profit as a share of equity) | 7.9% | 11.4% to 13.0% | same quarter, prior 3 years | n/a | -3.5 pp | -0.673 | pushed the score down |
| return on assets (profit as a share of assets) | 1.0% | 1.2% to 1.3% | same quarter, prior 3 years | n/a | -0.3 pp | -0.262 | pushed the score down |
| net interest margin (the spread earned on lending and investing) | 3.8% | 3.2% to 3.5% | same quarter, prior 3 years | n/a | +0.4 pp | -0.048 | little effect on the score |
| securities as a share of assets | 20.6% | 20.9% to 23.9% | prior 12 quarters | -0.3 pp | -2.9 pp | -0.169 | pushed the score down |
| loans as a share of deposits | 73.2% | 65.4% to 72.7% | prior 12 quarters | +0.6 pp | +1.4 pp | -0.068 | pushed the score down |

11 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 114 banks in the same specialty group and size tier (over $10 billion).

Asset growth, meaning how much the bank's total holdings of loans, securities and cash grew over the past four quarters, was 42.9%, which put it in the 98.2nd percentile of all banks nationally, unusually high. Among its peers, the bank's asset growth sat in the 94.3rd percentile against a peer median (the middle value of the group) of 5.9%, which is unusually high among its peers too. Deposit growth, meaning the rise in money customers keep at the bank over the past four quarters, was 43.5%, which put it in the 98.0th percentile nationally, unusually high. Against its peers, the bank's deposit growth stood in the 94.3rd percentile, with a peer median of 5.7%, which is unusually high among its peers too.

Overall, 2 of the bank's ratios fell in the national top or bottom 10%, and 2 of those were also unusual among its peers, both reflecting very fast growth over the past year.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| asset growth over the past four quarters | 42.9% | 98.2nd (unusually high) | 5.9% | 94.3rd | unusually high among its peers too |
| deposit growth over the past four quarters | 43.5% | 98.0th (unusually high) | 5.7% | 94.3rd | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 25.2% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 80.3% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 108.7% | 50% or more | yes |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

Hindsight: the fact sheet for this note contains no data from after the as-of quarter. So this section cannot report later ranks, watchlist flags, or whether the bank kept reporting; the outcome banner and score history table added by code show what is known.

## Sources

- F1 · Bank name · n/a · Fifth Third Bank Na · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · OH · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 3,764 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 12.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 12.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 11.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 13.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 44.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 8.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · 43.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: deposit growth over the past four quarters, value 43.5%; contribution to the score · 2026-06-30 · +0.270 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F76 · Driver up #2: commercial real estate loans as a share of loans, value 12.0%; contribution to the score · 2026-06-30 · +0.115 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F77 · Driver up #3: losses on bonds available for sale, as a share of equity, value 8.4%; contribution to the score · 2026-06-30 · +0.060 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F78 · Driver up #4: annualized loan write-offs, net of recoveries, as a share of loans, value 0.3%; contribution to the score · 2026-06-30 · +0.002 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F79 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 3.8%; contribution to the score · 2026-06-30 · -1.143 · data/analyst/scores.parquet: feature texas_ratio contribution
- F80 · Driver down #2: the Tier 1 risk-based capital ratio, value 11.7%; contribution to the score · 2026-06-30 · -0.874 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #3: return on equity (profit as a share of equity), value 7.9%; contribution to the score · 2026-06-30 · -0.673 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 0.8%; contribution to the score · 2026-06-30 · -0.353 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F83 · Driver down #5: annualized interest expense as a share of assets, value 1.3%; contribution to the score · 2026-06-30 · -0.332 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F88 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 66.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F89 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 55.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F90 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 57.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F91 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2026-06-30 · +10.7 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F92 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.115 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F94 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: return_on_equity
- F95 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 11.4% · data/features/fct_bank_features.parquet: return_on_equity
- F96 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 13.0% · data/features/fct_bank_features.parquet: return_on_equity
- F98 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.673 · data/analyst/scores.parquet: feature return_on_equity contribution
- F99 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F100 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets
- F101 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F102 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F104 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.262 · data/analyst/scores.parquet: feature return_on_assets contribution
- F105 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F106 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 3.8% · data/features/fct_bank_features.parquet: net_interest_margin
- F107 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F108 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.5% · data/features/fct_bank_features.parquet: net_interest_margin
- F110 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.048 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F111 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F112 · Trend: securities as a share of assets, value at the as-of quarter · 2026-06-30 · 20.6% · data/features/fct_bank_features.parquet: securities_to_assets
- F113 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 20.9% · data/features/fct_bank_features.parquet: securities_to_assets
- F114 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 23.9% · data/features/fct_bank_features.parquet: securities_to_assets
- F117 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.169 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F118 · Trend: securities as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature securities_to_assets contribution
- F119 · Trend: loans as a share of deposits, value at the as-of quarter · 2026-06-30 · 73.2% · data/features/fct_bank_features.parquet: loans_to_deposits
- F120 · Trend: loans as a share of deposits, lowest value in the comparison window · n/a · 65.4% · data/features/fct_bank_features.parquet: loans_to_deposits
- F121 · Trend: loans as a share of deposits, highest value in the comparison window · n/a · 72.7% · data/features/fct_bank_features.parquet: loans_to_deposits
- F124 · Trend: loans as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · -0.068 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F125 · Trend: loans as a share of deposits, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F126 · Trend: ratios outside their own prior range · 2026-06-30 · 11 · data/features/fct_bank_features.parquet
- F127 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F129 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F131 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 37.5% · data/analyst/scores.parquet: percentile
- F132 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it safer than a year earlier · data/analyst/scores.parquet: percentile
- F136 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · 42.9% · data/features/fct_bank_features.parquet: asset_growth_4q
- F137 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.2nd · data/features/fct_bank_features.parquet: asset_growth_4q
- F138 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: asset_growth_4q
- F139 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 94.3rd · data/features/fct_bank_features.parquet: asset_growth_4q
- F140 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 5.9% · data/features/fct_bank_features.parquet: asset_growth_4q
- F141 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F142 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · 43.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F143 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.0th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F144 · Peers: deposit growth over the past four quarters, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: deposit_growth_4q
- F145 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 94.3rd · data/features/fct_bank_features.parquet: deposit_growth_4q
- F146 · Peers: deposit growth over the past four quarters, peer median · 2026-06-30 · 5.7% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F147 · Peers: deposit growth over the past four quarters, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F149 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 2 · data/features/fct_bank_features.parquet
- F150 · Peers: those ratios also unusual among peers · 2026-06-30 · 2 · data/features/fct_bank_features.parquet
- F152 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
