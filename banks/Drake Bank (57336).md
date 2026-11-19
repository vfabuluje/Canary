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
written_at: "2026-11-19T14:08:19"
writer_model: "claude-opus-5-5"
checked: true
---

# Drake Bank (cert 57336)

*Outcome not yet known.*

## Summary

As of June 30, 2026, Drake Bank, a Minnesota bank, ranked 15 out of 4,313 banks on Canary's risk score, placing it in the 99.7th percentile, where higher means riskier. That puts it on Canary's watchlist, which covers the top 2% of banks by score. Its troubled loans are large compared with its capital cushion, and it lost money in the quarter.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was thin: equity was 7.0% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 7.3% against 11.0%. Its risk-based capital ratios, which weigh assets by how risky they are, were also well below the median, with Tier 1 at 9.8% against 14.6% and total capital at 11.1% against 15.8%.

Credit quality was the clearest concern: loans 90 or more days past due or not accruing interest were 4.5% of loans, far above the national median of 0.5%. Nonaccrual assets and foreclosed property were 5.4% of assets against a median of 0.3%, and the Texas ratio, which compares troubled assets with capital plus reserves, was 57.8% against 2.9%. The bank set aside an annualized 2.2% of assets for expected loan losses against a median of 0.1%, and return on assets (profit as a share of assets) was -1.2% against 1.2%.

On funding, brokered deposits, money placed through middlemen that can be less loyal, were 20.2% of deposits against a national median of 0.0%, and Federal Home Loan Bank borrowings were 6.9% of assets against 0.2%. Deposits shrank by -9.5% over the past four quarters while the median bank grew them by 4.2%. Unrealized losses on bonds available for sale equaled 7.9% of equity, above the national median of 5.6%.

## Understanding the score

Drake Bank ranked 15 of 4,313 banks as of June 30, 2026, in the 99.7th percentile on a scale of 0 to 100 where higher means riskier. It was flagged for the watchlist, which holds the top 2% of banks, 87 banks that quarter.

The factor pushing the score up most was the Texas ratio at 57.8%, adding +0.781, followed by losses on bonds available for sale at 7.9% of equity, adding +0.580. Interest expense at 2.6% of assets added +0.444, brokered deposits at 20.2% of deposits added +0.320, and return on equity (profit as a share of owners' money) at -17.7% added +0.212.

Pulling the score down most was the Tier 1 risk-based capital ratio at 9.8%, at -0.824, along with loans 30-89 days past due at 0.0% of assets, at -0.433. Construction loans at 5.9% of loans contributed -0.380, total assets of $247.4 million contributed -0.208, and volatile funding at 5.7% of assets contributed -0.151.

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

The bank's percentile a year earlier, on June 30, 2025, was 92.1%, and as of June 30, 2026, at rank 15, the model rated it riskier than a year earlier. Each ratio is compared with its own prior range over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years, and 9 of 28 ratios checked sat outside that range.

The Texas ratio reached 57.8%, above its prior range of 0.2% to 43.7%, and contributed +0.781 log-odds units, which pushed the score up. Loans 90+ days past due or not accruing interest reached 4.5% of loans, above a prior range of 0.0% to 3.2%, and contributed +0.165, which pushed the score up. The loan-loss provision reached 2.2% of assets, above a prior range of 0.0% to 0.6%, and contributed +0.125, which pushed the score up. Return on equity fell to -17.7%, below a prior range of 5.9% to 13.2%, and contributed +0.212, which pushed the score up.

By contrast, nonaccrual assets and foreclosed property rose to 5.4% of assets, above a prior range of 0.0% to 3.4%, yet contributed only -0.005, little effect on the score. Likewise, return on assets fell to -1.2%, below a prior range of 0.4% to 1.0%, yet contributed -0.007, little effect on the score.

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

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

The Texas ratio of 57.8% sat at the 99.6th national percentile, unusually high, and at the 99.7th percentile among peers against a peer median of 3.0%, unusually high among its peers too. The loan-loss provision of 2.2% of assets sat at the 99.2nd national percentile, unusually high, and at the 99.3rd percentile among peers against a peer median of 0.1%, unusually high among its peers too. Nonaccrual assets and foreclosed property at 5.4% of assets sat at the 99.2nd national percentile, unusually high, and at the 99.0th percentile among peers against a peer median of 0.3%, unusually high among its peers too.

Return on equity of -17.7% sat at the 0.9th national percentile, unusually low, and at the 0.5th percentile among peers against a peer median of 11.7%, unusually low among its peers too. Return on assets of -1.2% sat at the 1.7th national percentile, unusually low, and at the 1.0th percentile among peers against a peer median of 1.2%, unusually low among its peers too. The Tier 1 risk-based capital ratio of 9.8% sat at the 1.1st national percentile, unusually low, and at the 1.7th percentile among peers against a peer median of 14.3%, unusually low among its peers too. The leverage ratio of 7.3% sat at the 1.2nd national percentile, unusually low, and at the 0.6th percentile among peers against a peer median of 10.8%, unusually low among its peers too. Asset growth of -9.4% sat at the 1.8th national percentile, unusually low, and at the 1.8th percentile among peers against a peer median of 4.8%, unusually low among its peers too.

Overall, 16 of the bank's ratios fell in the national top or bottom 10%, and 16 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 57.8% | 99.6th (unusually high) | 3.0% | 99.7th | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 2.2% | 99.2nd (unusually high) | 0.1% | 99.3rd | unusually high among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 5.4% | 99.2nd (unusually high) | 0.3% | 99.0th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -17.7% | 0.9th (unusually low) | 11.7% | 0.5th | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 9.8% | 1.1st (unusually low) | 14.3% | 1.7th | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | 7.3% | 1.2nd (unusually low) | 10.8% | 0.6th | unusually low among its peers too |
| return on assets (profit as a share of assets) | -1.2% | 1.7th (unusually low) | 1.2% | 1.0th | unusually low among its peers too |
| asset growth over the past four quarters | -9.4% | 1.8th (unusually low) | 4.8% | 1.8th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 46.9% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 167.3% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 8.3% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight, this bank falls in the open-watchlist case: it remains open and on Canary's watchlist, rather than having stopped reporting. The fact sheet provides no later data that explains this further, so no additional hindsight detail is given here.

## What happened next

In hindsight, the bank continued to be treated as an open bank on the watchlist after the as-of quarter. The fact sheet does not list its later ranks or flags, so those are not described here.

## Sources

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
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 20.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 6.9% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 7.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -9.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
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
- F126 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · +0.781 · data/analyst/scores.parquet: feature texas_ratio contribution
- F127 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F128 · Trend: ratios outside their own prior range · 2026-06-30 · 9 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F131 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F132 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F133 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 92.1% · data/analyst/scores.parquet: percentile
- F134 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F138 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 57.8% · data/features/fct_bank_features.parquet: texas_ratio
- F139 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.6th · data/features/fct_bank_features.parquet: texas_ratio
- F140 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F141 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: texas_ratio
- F142 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: texas_ratio
- F143 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F144 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F145 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.2nd · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F146 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F147 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.3rd · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F148 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F149 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F150 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 5.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F151 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.2nd · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F152 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F153 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.0th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F154 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F155 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F156 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -17.7% · data/features/fct_bank_features.parquet: return_on_equity
- F157 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.9th · data/features/fct_bank_features.parquet: return_on_equity
- F158 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F159 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 0.5th · data/features/fct_bank_features.parquet: return_on_equity
- F160 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 11.7% · data/features/fct_bank_features.parquet: return_on_equity
- F161 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F162 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F163 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 1.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F164 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F165 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 1.7th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F166 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-06-30 · 14.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F167 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F168 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 7.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F169 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 1.2nd · data/features/fct_bank_features.parquet: leverage_ratio
- F170 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F171 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 0.6th · data/features/fct_bank_features.parquet: leverage_ratio
- F172 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 10.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F173 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F174 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2026-06-30 · -1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F175 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 1.7th · data/features/fct_bank_features.parquet: return_on_assets
- F176 · Peers: return on assets (profit as a share of assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F177 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2026-06-30 · 1.0th · data/features/fct_bank_features.parquet: return_on_assets
- F178 · Peers: return on assets (profit as a share of assets), peer median · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F179 · Peers: return on assets (profit as a share of assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F180 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -9.4% · data/features/fct_bank_features.parquet: asset_growth_4q
- F181 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 1.8th · data/features/fct_bank_features.parquet: asset_growth_4q
- F182 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F183 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 1.8th · data/features/fct_bank_features.parquet: asset_growth_4q
- F184 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F185 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F187 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 16 · data/features/fct_bank_features.parquet
- F188 · Peers: those ratios also unusual among peers · 2026-06-30 · 16 · data/features/fct_bank_features.parquet
- F190 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
