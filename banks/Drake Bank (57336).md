---
cert: 57336
name: "Drake Bank"
as_of: 2026-06-30
rank: 15
n_banks: 4313
percentile: 99.67539995362856
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:56:13"
writer_model: "claude-opus-5-5"
checked: true
---

# Drake Bank (cert 57336)

*Outcome not yet known.*

## Summary

Drake Bank, a Minnesota bank, ranked 15 out of 4,313 FDIC-insured banks on Canary's risk score as of 2026-06-30, placing it in the 99.7th percentile, where higher means riskier. That placed it on Canary's watchlist, the riskiest 2% of banks. The main concerns are a high Texas ratio (troubled assets against capital plus reserves) of 57.8%, a loss-making year with return on equity of -17.7%, and capital ratios well below the national median.

## Warning signs in the data

Capital, the cushion that absorbs losses, was thin: equity was 7.0% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 7.3% against 11.0%. Its Tier 1 risk-based capital ratio was 9.8% against a median of 14.6%, and its total risk-based capital ratio was 11.1% against 15.8%.

Credit quality was weak: loans 90+ days past due or not accruing interest were 4.5% of loans, far above the 0.5% median, and nonaccrual assets plus foreclosed property were 5.4% of assets against 0.3%. The Texas ratio stood at 57.8%, far above the national median of 2.9%. The bank set aside a provision for loan losses of 2.2% of assets against a median of 0.1%, and it lost money, with return on assets of -1.2% against a median of 1.2% and return on equity of -17.7% against 11.6%.

On funding, brokered deposits (money placed through intermediaries, which can leave quickly) were 20.2% of deposits against a median of 0.0%, and Federal Home Loan Bank borrowings were 6.9% of assets against 0.2%. Core deposits, the stable everyday kind, were 63.4% of assets, below the 75.5% median, though uninsured deposits were lower than typical at 14.2% against 24.8% and cash was higher at 9.2% against 6.2%. Unrealized losses on bonds available for sale equaled 7.9% of equity, somewhat above the 5.6% median.

## Understanding the score

Drake Bank ranked 15 out of 4,313 banks as of 2026-06-30, the 99.7th percentile on a scale from 0 to 100 where higher means riskier. It was flagged for the watchlist, which covers the top 2% of banks and held 87 banks that quarter.

The five factors that pushed the score up most were the Texas ratio at 57.8%, adding +0.781, and losses on bonds available for sale at 7.9% of equity, adding +0.580. Next came interest expense at 2.6% of assets, adding +0.444, brokered deposits at 20.2% of deposits, adding +0.320, and return on equity at -17.7%, adding +0.212.

The five factors that pulled the score down most were the Tier 1 risk-based capital ratio at 9.8%, contributing -0.824, and loans 30-89 days past due at 0.0% of assets, contributing -0.433. The others were construction loans at 5.9% of loans, contributing -0.380, total assets of $247.4 million, contributing -0.208, and volatile funding at 5.7% of assets, contributing -0.151.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,960 | 4,589 |  |
| 2024-12-31 | 895 | 4,560 |  |
| 2025-03-31 | 154 | 4,536 |  |
| 2025-06-30 | 357 | 4,494 |  |
| 2025-09-30 | 80 | 4,452 | ▲ watchlist |
| 2025-12-31 | 83 | 4,411 | ▲ watchlist |
| 2026-03-31 | 14 | 4,353 | ▲ watchlist |
| 2026-06-30 | 15 | 4,313 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own past: most against the prior 12 quarters, and year-to-date ratios against the same quarter in the prior 3 years. Of 28 ratios compared, 9 sat outside their own prior range, and the 6 furthest outside are discussed here. The bank ranked 15 out of 4,313, in the 99.7th percentile, compared with a percentile of 92.1% a year earlier, so the model rated it riskier than a year earlier.

The Texas ratio reached 57.8%, above its prior range of 0.2% to 43.7%, and contributed +0.781 model log-odds units, which pushed the score up. That ratio rose +18.3 pp in one quarter and +41.8 pp over four quarters. Loans 90+ days past due or not accruing were 4.5% of loans, above a prior range of 0.0% to 3.2%, and contributed +0.165, which pushed the score up. Nonaccrual assets and foreclosed property were 5.4% of assets, above a prior range of 0.0% to 3.4%, yet contributed only -0.005, having little effect on the score.

The provision for loan losses was 2.2% of assets, above a prior range of 0.0% to 0.6%, and contributed +0.125, which pushed the score up. Return on equity fell to -17.7%, below a prior range of 5.9% to 13.2%, and contributed +0.212, which pushed the score up. Return on assets fell to -1.2%, below a prior range of 0.4% to 1.0%, but contributed just -0.007, having little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -17.7% | 5.9% to 13.2% | same quarter, prior 3 years | n/a | -31.0 pp | +0.212 | pushed the score up |
| return on assets (profit as a share of assets) | -1.2% | 0.4% to 1.0% | same quarter, prior 3 years | n/a | -2.2 pp | -0.007 | little effect on the score |
| annualized provision for loan losses as a share of assets | 2.2% | 0.0% to 0.6% | same quarter, prior 3 years | n/a | +1.6 pp | +0.125 | pushed the score up |
| nonaccrual assets and foreclosed property, as a share of assets | 5.4% | 0.0% to 3.4% | prior 12 quarters | +1.9 pp | +4.0 pp | -0.005 | little effect on the score |
| loans 90+ days past due or not accruing interest, as a share of loans | 4.5% | 0.0% to 3.2% | prior 12 quarters | +2.3 pp | +2.8 pp | +0.165 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 57.8% | 0.2% to 43.7% | prior 12 quarters | +18.3 pp | +41.8 pp | +0.781 | pushed the score up |

9 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Why it's on the watchlist

In hindsight, this bank's case is that it remained open and on the watchlist rather than reaching a final outcome. The fact sheet for this memo contains no data from after the as-of quarter, so this section cannot add hindsight evidence beyond that status. Its place on the watchlist rests on the as-of figures described above, chiefly rising troubled loans, losses and thin capital.

## What happened next

Looking ahead in hindsight, the fact sheet includes no later ranks, flags or reporting status for this bank. We therefore cannot say from this data how its rank moved afterward or whether it kept filing reports; the score history table added below shows whatever later quarters are available.

## Sources

- F1 · Bank name · n/a · Drake Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · MN · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 15 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 7.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 11.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 5.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 57.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -17.7% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 14.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 20.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 63.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 9.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 57.8%; contribution to the score · 2026-06-30 · +0.781 · data/analyst/scores.parquet: feature texas_ratio contribution
- F76 · Driver up #2: losses on bonds available for sale, as a share of equity, value 7.9%; contribution to the score · 2026-06-30 · +0.580 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F77 · Driver up #3: annualized interest expense as a share of assets, value 2.6%; contribution to the score · 2026-06-30 · +0.444 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F78 · Driver up #4: brokered deposits as a share of deposits, value 20.2%; contribution to the score · 2026-06-30 · +0.320 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F79 · Driver up #5: return on equity (profit as a share of equity), value -17.7%; contribution to the score · 2026-06-30 · +0.212 · data/analyst/scores.parquet: feature return_on_equity contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 9.8%; contribution to the score · 2026-06-30 · -0.824 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: loans 30-89 days past due, as a share of assets, value 0.0%; contribution to the score · 2026-06-30 · -0.433 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F82 · Driver down #3: construction loans as a share of loans, value 5.9%; contribution to the score · 2026-06-30 · -0.380 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: total assets, value $247.4 million; contribution to the score · 2026-06-30 · -0.208 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: volatile funding as a share of assets, value 5.7%; contribution to the score · 2026-06-30 · -0.151 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F89 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -17.7% · data/features/fct_bank_features.parquet: return_on_equity
- F90 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 5.9% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 13.2% · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · +0.212 · data/analyst/scores.parquet: feature return_on_equity contribution
- F94 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F95 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F96 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: return_on_assets
- F97 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: return_on_assets
- F99 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.007 · data/analyst/scores.parquet: feature return_on_assets contribution
- F100 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature return_on_assets contribution
- F101 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F102 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F103 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.6% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F105 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.125 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F106 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F107 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2026-06-30 · 5.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F108 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F109 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 3.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F112 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.005 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F113 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F114 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F115 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F116 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 3.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F119 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.165 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F120 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F121 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 57.8% · data/features/fct_bank_features.parquet: texas_ratio
- F122 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: texas_ratio
- F123 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 43.7% · data/features/fct_bank_features.parquet: texas_ratio
- F124 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2026-06-30 · +18.3 pp · data/features/fct_bank_features.parquet: texas_ratio
- F125 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over four quarters, in percentage points · 2026-06-30 · +41.8 pp · data/features/fct_bank_features.parquet: texas_ratio
- F126 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · +0.781 · data/analyst/scores.parquet: feature texas_ratio contribution
- F127 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F128 · Trend: ratios outside their own prior range · 2026-06-30 · 9 · data/features/fct_bank_features.parquet
- F129 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F131 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F132 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F133 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 92.1% · data/analyst/scores.parquet: percentile
- F134 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
