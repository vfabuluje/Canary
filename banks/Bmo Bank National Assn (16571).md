---
cert: 16571
name: "Bmo Bank National Assn"
as_of: 2026-06-30
rank: 3756
n_banks: 4313
percentile: 12.937630419661483
flagged: false
outcome: "quiet"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:18"
writer_model: "claude-opus-5-5"
checked: true
---

# Bmo Bank National Assn (cert 16571)

## Summary

As of 2026-06-30, Canary's model ranked Bmo Bank National Assn, an IL bank with $255.0 billion in assets, 3,756 out of 4,313 banks, placing it in the 12.9th percentile, where higher means riskier. It was not on the watchlist, and its capital (the owners' cushion against losses) sat above the national median on every measure shown, which the model treated as the main reason for its low ranking. The weak spots were profit and funding: return on assets was 0.1% against a national median of 1.2%, and uninsured deposits (money above the government insurance limit) were 52.7% of deposits against a median of 24.8%. The peer section finds that this uninsured share is typical for large commercial lenders, while the weak profit stands out even among peers.

## Warning signs in the data

Capital was a strength: equity was 14.3% of assets against a national median of 10.6%, and the Tier 1 risk-based capital ratio (core capital measured against risk-weighted assets) was 15.0% against 14.6%. Credit quality was somewhat weaker than typical: loans 90+ days past due or not accruing interest were 0.9% of loans against a median of 0.5%, and net loan write-offs were 0.2% against 0.0%. The bank also held more in loan-loss reserves (money set aside for bad loans) than usual, at 1.6% of loans against a median of 1.2%.

On funding, uninsured deposits were 52.7% of deposits, well above the national median of 24.8%, though the peer section notes this is typical for its peer group. Deposits shrank by -2.6% over the past four quarters, while the median bank grew deposits by 4.2%. Borrowings from the Federal Home Loan Bank (a government-sponsored lender to banks) were 3.4% of assets against a median of 0.2%, but cash was a cushion at 10.0% of assets against 6.2%.

Unrealized losses on bonds held to maturity were 1.1% of equity against a median of 0.0%, while losses on bonds available for sale were 5.3% of equity, close to the median of 5.6%. Profitability was the clearest weak point: return on equity was 1.0% against a median of 11.6%, and the efficiency ratio (operating costs as a share of revenue) was 84.4% against 62.1%.

## Understanding the score

On 2026-06-30 the bank ranked 3,756 out of 4,313 banks, in the 12.9th percentile on a scale of 0 to 100 where higher means riskier. It was not flagged on the watchlist, which held 87 banks that quarter, the top 2% of banks by score.

Only one factor pushed the score up: losses on bonds available for sale, at 5.3% of equity, with a contribution of +0.073. Five factors pushed it down, led by the Tier 1 risk-based capital ratio at 15.0%, contributing -1.093, and the Texas ratio (troubled assets against capital plus reserves) at 3.5%, contributing -1.055. The total risk-based capital ratio at 16.2% and equity as a share of assets at 14.3% each contributed -0.409, and return on equity at 1.0% contributed -0.396. Overall, the model weighed the bank's strong capital far more heavily than its weak profits.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,850 | 4,589 |  |
| 2024-12-31 | 2,390 | 4,560 |  |
| 2025-03-31 | 3,187 | 4,536 |  |
| 2025-06-30 | 3,708 | 4,494 |  |
| 2025-09-30 | 3,429 | 4,452 |  |
| 2025-12-31 | 3,545 | 4,411 |  |
| 2026-03-31 | 4,203 | 4,353 |  |
| 2026-06-30 | 3,756 | 4,313 |  |

## How its ratios moved

As of the latest quarter, the model ranked the bank 3,756 out of 4,313 banks, placing it in the 12.9th percentile, where a higher percentile means a riskier score. A year earlier it sat at the 17.5th percentile, and the model rated it safer than a year earlier. Each ratio was compared with its own history, usually the prior 12 quarters, or, for year-to-date figures, the same quarter in the prior 3 years. Of 30 ratios checked, 8 fell outside their own prior range, and the table shows the 6 that were furthest outside.

The efficiency ratio (operating costs as a share of revenue) reached 84.4%, above its prior range of 54.1% to 69.9% and up +30.2 pp over four quarters, yet it pushed the score down, with a contribution of -0.114 model log-odds units (positive values push the score up). Losses on bonds held to maturity (bonds the bank plans to keep until they repay), as a share of equity, rose to 1.1%, above its prior range of 0.0% to 0.7%, but this also pushed the score down, with a contribution of -0.084. The annualized provision for loan losses (money set aside for loans that may go bad) was 0.0% of assets, below its prior range of 0.3% to 1.0%, and it pushed the score down, with a contribution of -0.124. Annualized net loan write-offs (loans written off as uncollectable, minus recoveries) were 0.2% of loans, below their prior range of 0.3% to 0.4%, and had little effect on the score, at -0.003. Construction loans made up 3.17% of loans, just under their prior range of 3.25% to 4.3%, and pushed the score down, with a contribution of -0.197. Annualized interest expense (what the bank pays on deposits and borrowings) was 1.6% of assets, below its prior range of 1.7% to 2.4%, and pushed the score down, with a contribution of -0.193.

So although all 6 ratios in the table sat outside their usual range, none of them pushed the score up; each either pushed it down or had little effect.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 84.4% | 54.1% to 69.9% | same quarter, prior 3 years | n/a | +30.2 pp | -0.114 | pushed the score down |
| losses on bonds held to maturity, as a share of equity | 1.1% | 0.0% to 0.7% | prior 12 quarters | +0.4 pp | +0.5 pp | -0.084 | pushed the score down |
| annualized provision for loan losses as a share of assets | 0.0% | 0.3% to 1.0% | same quarter, prior 3 years | n/a | -0.3 pp | -0.124 | pushed the score down |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.2% | 0.3% to 0.4% | same quarter, prior 3 years | n/a | -0.1 pp | -0.003 | little effect on the score |
| construction loans as a share of loans | 3.17% | 3.25% to 4.3% | prior 12 quarters | -0.1 pp | -0.7 pp | -0.197 | pushed the score down |
| annualized interest expense as a share of assets | 1.6% | 1.7% to 2.4% | same quarter, prior 3 years | n/a | -0.4 pp | -0.193 | pushed the score down |

8 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 114 banks in the same specialty group and size tier (over $10 billion).

Uninsured deposits (money held above the government's deposit insurance limit) made up 52.7% of the bank's deposits, placing it in the 95.6th percentile nationally, which is unusually high. Among its 114 peers it sits in the 88.1st percentile, against a peer median of 40.3%, which is typical for its peer group.

Return on equity (yearly profit as a share of the owners' stake in the bank) was 1.0%, placing it in the 5.4th percentile nationally, which is unusually low. Among its peers it sits in the 2.3rd percentile, against a peer median of 10.3%, which is unusually low among its peers too. Return on assets (yearly profit as a share of everything the bank owns) was 0.1%, placing it in the 6.0th percentile nationally, which is unusually low. Among its peers it sits in the 7.5th percentile, against a peer median of 1.2%, which is unusually low among its peers too.

Overall, 3 of the bank's ratios fall in the national top or bottom 10%, and 2 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| uninsured deposits as a share of deposits | 52.7% | 95.6th (unusually high) | 40.3% | 88.1st | typical for its peer group |
| return on equity (profit as a share of equity) | 1.0% | 5.4th (unusually low) | 10.3% | 2.3rd | unusually low among its peers too |
| return on assets (profit as a share of assets) | 0.1% | 6.0th (unusually low) | 1.2% | 7.5th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 15.1% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 86.5% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 5.3% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## What happened next

Hindsight: this case is marked quiet, but the fact sheet contains no data from after the as-of quarter. We therefore cannot report later ranks, watchlist flags, or whether the bank kept filing reports; the score history table added by code shows whatever later quarters are available.

## Sources

- F1 · Bank name · n/a · Bmo Bank National Assn · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 3,756 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 12.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 14.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 15.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · 1.0% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 84.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 52.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2026-06-30 · $255.0 billion · data/features/fct_bank_features.parquet: log_total_assets
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -2.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: losses on bonds available for sale, as a share of equity, value 5.3%; contribution to the score · 2026-06-30 · +0.073 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio, value 15.0%; contribution to the score · 2026-06-30 · -1.093 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 3.5%; contribution to the score · 2026-06-30 · -1.055 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver down #3: the total risk-based capital ratio, value 16.2%; contribution to the score · 2026-06-30 · -0.409 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver down #4: equity as a share of assets, value 14.3%; contribution to the score · 2026-06-30 · -0.409 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F80 · Driver down #5: return on equity (profit as a share of equity), value 1.0%; contribution to the score · 2026-06-30 · -0.396 · data/analyst/scores.parquet: feature return_on_equity contribution
- F85 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 84.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F86 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 54.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F87 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 69.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F88 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2026-06-30 · +30.2 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F89 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.114 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F90 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F91 · Trend: losses on bonds held to maturity, as a share of equity, value at the as-of quarter · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F92 · Trend: losses on bonds held to maturity, as a share of equity, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F93 · Trend: losses on bonds held to maturity, as a share of equity, highest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F96 · Trend: losses on bonds held to maturity, as a share of equity, contribution to the score (model log-odds units) · 2026-06-30 · -0.084 · data/analyst/scores.parquet: feature htm_unrealized_loss_to_equity contribution
- F97 · Trend: losses on bonds held to maturity, as a share of equity, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature htm_unrealized_loss_to_equity contribution
- F98 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F99 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F100 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F102 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.124 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F103 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F104 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F105 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F106 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F108 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.003 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F109 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F110 · Trend: construction loans as a share of loans, value at the as-of quarter · 2026-06-30 · 3.17% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F111 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 3.25% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F112 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 4.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F115 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.197 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F116 · Trend: construction loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F117 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F118 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F119 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 2.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F121 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.193 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F122 · Trend: annualized interest expense as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F123 · Trend: ratios outside their own prior range · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F124 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F125 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F126 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F127 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F128 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 17.5% · data/analyst/scores.parquet: percentile
- F129 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it safer than a year earlier · data/analyst/scores.parquet: percentile
- F133 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 52.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F134 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 95.6th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F135 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F136 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 88.1st · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F137 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 40.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F138 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F139 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · 1.0% · data/features/fct_bank_features.parquet: return_on_equity
- F140 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 5.4th · data/features/fct_bank_features.parquet: return_on_equity
- F141 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F142 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 2.3rd · data/features/fct_bank_features.parquet: return_on_equity
- F143 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 10.3% · data/features/fct_bank_features.parquet: return_on_equity
- F144 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F145 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: return_on_assets
- F146 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 6.0th · data/features/fct_bank_features.parquet: return_on_assets
- F147 · Peers: return on assets (profit as a share of assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F148 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2026-06-30 · 7.5th · data/features/fct_bank_features.parquet: return_on_assets
- F149 · Peers: return on assets (profit as a share of assets), peer median · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F150 · Peers: return on assets (profit as a share of assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F151 · Peers: banks in the peer group (including this bank) · 2026-06-30 · 114 · data/raw/specialty/: SPECGRP
- F152 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 3 · data/features/fct_bank_features.parquet
- F153 · Peers: those ratios also unusual among peers · 2026-06-30 · 2 · data/features/fct_bank_features.parquet
- F155 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
