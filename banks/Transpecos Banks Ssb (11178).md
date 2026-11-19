---
cert: 11178
name: "Transpecos Banks Ssb"
as_of: 2026-06-30
rank: 6
n_banks: 4313
percentile: 99.8840714120102
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:08:18"
writer_model: "claude-opus-5-5"
checked: true
---

# Transpecos Banks Ssb (cert 11178)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Transpecos Banks Ssb, a Texas bank, ranked 6 out of 4,313 FDIC-insured banks on Canary's risk score, which places it in the 99.9th percentile, where higher means riskier. That puts it on Canary's watchlist, which covers the riskiest 2% of banks. The main concerns in its data are a large share of loans in trouble (8.1% of loans are 90+ days late or no longer paying interest), thin capital (a leverage ratio of 6.7%), and a loss for the period (return on equity of -22.6%).

## Warning signs in the data

Capital, the cushion of the owners' money that absorbs losses, is thin: equity was 6.7% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 6.7% against a median of 11.0%. Its risk-based capital ratios, which weigh assets by how risky they are, were also well below typical levels: Tier 1 at 9.7% versus a median of 14.6%, and total at 10.7% versus 15.8%.

Credit quality is the clearest problem: loans 90+ days past due or not accruing interest made up 8.1% of loans, far above the national median of 0.5%. Nonaccrual assets and foreclosed property were 2.7% of assets versus a median of 0.3%, and loans 30-89 days late were 0.8% of assets versus 0.2%. The Texas ratio, which compares troubled assets with the capital and reserves available to cover them, stood at 74.8% against a national median of 2.9%. The bank was losing money, with a return on assets of -1.6% versus a median of 1.2%, and its operating costs were 146.4% of revenue versus a median of 62.1%.

On funding, uninsured deposits (balances above the federal insurance limit) were 39.8% of deposits versus a median of 24.8%, and brokered deposits, money placed through intermediaries, were 27.5% versus a median of 0.0%. Federal Home Loan Bank borrowings were 3.1% of assets versus a median of 0.2%, while cash was a comparatively strong 14.1% of assets versus 6.2%. Unrealized losses on bonds were modest: 2.0% of equity on bonds available for sale versus a median of 5.6%, and 0.0% on bonds held to maturity, in line with the median of 0.0%.

## Understanding the score

The bank ranked 6 of 4,313 banks scored for 2026-06-30, the 99.9th percentile on a scale of 0 to 100 where higher means riskier. It was flagged for the watchlist, which holds the top 2% of banks, or 87 banks that quarter.

The five factors pushing the score up most were: loans 90+ days late or not accruing interest at 8.1% of loans (+0.900), the Texas ratio at 74.8% (+0.678), return on equity at -22.6% (+0.608), brokered deposits at 27.5% of deposits (+0.587), and interest expense at 2.4% of assets (+0.394). The five factors pulling it down most were: the Tier 1 risk-based capital ratio at 9.7% (-0.777), construction loans at 3.1% of loans (-0.373), total assets of $972.1 million (-0.212), loan-loss reserves at 1.0% of loans (-0.191), and volatile funding at 3.4% of assets (-0.180).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 55 | 4,589 | ▲ watchlist |
| 2024-12-31 | 12 | 4,560 | ▲ watchlist |
| 2025-03-31 | 31 | 4,536 | ▲ watchlist |
| 2025-06-30 | 111 | 4,494 |  |
| 2025-09-30 | 103 | 4,452 |  |
| 2025-12-31 | 35 | 4,411 | ▲ watchlist |
| 2026-03-31 | 8 | 4,353 | ▲ watchlist |
| 2026-06-30 | 6 | 4,313 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own range over the prior 12 quarters, and 8 of the 28 ratios checked sat outside that range at the as-of quarter. The Texas ratio reached 74.8%, above its prior range of 13.1% to 57.0%, and contributed +0.678 log-odds units, which pushed the score up. The Texas ratio rose by +17.8 pp in the latest quarter alone and by +45.6 pp over four quarters. Return on equity fell to -22.6%, below its prior range of 3.9% to 42.0%, and contributed +0.608 log-odds units, which pushed the score up. The leverage ratio dropped to 6.7%, below its prior range of 7.8% to 9.8%, and contributed +0.099 log-odds units, which pushed the score up.

Some ratios moved outside their range yet mattered little or worked the other way. Return on assets fell to -1.6%, below its prior range of 0.3% to 3.4%, but contributed only +0.036 log-odds units, little effect on the score. The efficiency ratio rose to 146.4%, above its prior range of 49.3% to 110.0%, but contributed -0.035 log-odds units, little effect on the score. Net interest margin slipped to 3.1%, below its prior range of 3.4% to 4.4%, yet contributed -0.055 log-odds units, which pushed the score down.

Overall, the model rated it riskier than a year earlier, when it sat in the 97.6th percentile on 2025-06-30, compared with the 99.9th percentile and a rank of 6 now.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -22.6% | 3.9% to 42.0% | same quarter, prior 3 years | n/a | -31.2 pp | +0.608 | pushed the score up |
| return on assets (profit as a share of assets) | -1.6% | 0.3% to 3.4% | same quarter, prior 3 years | n/a | -2.3 pp | +0.036 | little effect on the score |
| the efficiency ratio (operating costs as a share of revenue) | 146.4% | 49.3% to 110.0% | same quarter, prior 3 years | n/a | +36.4 pp | -0.035 | little effect on the score |
| the leverage ratio (core capital as a share of average assets) | 6.7% | 7.8% to 9.8% | prior 12 quarters | -1.1 pp | -2.8 pp | +0.099 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 74.8% | 13.1% to 57.0% | prior 12 quarters | +17.8 pp | +45.6 pp | +0.678 | pushed the score up |
| net interest margin (the spread earned on lending and investing) | 3.1% | 3.4% to 4.4% | same quarter, prior 3 years | n/a | -0.2 pp | -0.055 | pushed the score down |

8 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

The Texas ratio of 74.8% sits in the 99.8th national percentile, unusually high, and in the 99.8th percentile among peers against a peer median of 3.0%, unusually high among its peers too. Loans 90+ days late or not accruing interest, at 8.1% of loans, sit in the 99.2nd national percentile, unusually high, and the 99.5th among peers against a peer median of 0.4%, unusually high among its peers too. Return on equity of -22.6% is in the 0.8th national percentile, unusually low, and the 0.2nd among peers against a peer median of 11.7%, unusually low among its peers too. Return on assets of -1.6% is in the 1.4th national percentile, unusually low, and the 0.7th among peers against a peer median of 1.2%, unusually low among its peers too. The efficiency ratio of 146.4% is in the 98.9th national percentile, unusually high, and the 99.7th among peers against a peer median of 63.7%, unusually high among its peers too.

The leverage ratio of 6.7% is in the 0.8th national percentile, unusually low, and the 0.4th among peers against a peer median of 10.8%, unusually low among its peers too. The Tier 1 risk-based capital ratio of 9.7% is in the 0.9th national percentile, unusually low, and the 1.3rd among peers against a peer median of 14.3%, unusually low among its peers too. The total risk-based capital ratio of 10.7% is in the 0.9th national percentile, unusually low, and the 1.4th among peers against a peer median of 15.4%, unusually low among its peers too. Overall, 12 of the bank's ratios fall in the national top or bottom 10%, and 11 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 74.8% | 99.8th (unusually high) | 3.0% | 99.8th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -22.6% | 0.8th (unusually low) | 11.7% | 0.2nd | unusually low among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 8.1% | 99.2nd (unusually high) | 0.4% | 99.5th | unusually high among its peers too |
| the leverage ratio (core capital as a share of average assets) | 6.7% | 0.8th (unusually low) | 10.8% | 0.4th | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 9.7% | 0.9th (unusually low) | 14.3% | 1.3rd | unusually low among its peers too |
| the total risk-based capital ratio | 10.7% | 0.9th (unusually low) | 15.4% | 1.4th | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 146.4% | 98.9th (unusually high) | 63.7% | 99.7th | unusually high among its peers too |
| return on assets (profit as a share of assets) | -1.6% | 1.4th (unusually low) | 1.2% | 0.7th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 28.7% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 86.4% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -30.0% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight: this bank's case is recorded as still open and on the watchlist, so there is no later outcome to explain yet. The fact sheet contains no data from after the as-of quarter, so this memo cannot say how the bank's position has changed since then.

## What happened next

In hindsight: the fact sheet provides no later ranks, flags or reporting status for this bank after the as-of quarter. Its case remains open, and later quarters of data would be needed to see whether it stays on the watchlist or keeps reporting.

## Sources

- F1 · Bank name · n/a · Transpecos Banks Ssb · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · TX · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 6 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 9.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 10.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 8.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 2.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 74.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -1.6% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -22.6% · data/features/fct_bank_features.parquet: return_on_equity
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 146.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 39.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 27.5% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 3.1% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 14.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 2.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 8.1%; contribution to the score · 2026-06-30 · +0.900 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 74.8%; contribution to the score · 2026-06-30 · +0.678 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: return on equity (profit as a share of equity), value -22.6%; contribution to the score · 2026-06-30 · +0.608 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver up #4: brokered deposits as a share of deposits, value 27.5%; contribution to the score · 2026-06-30 · +0.587 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F79 · Driver up #5: annualized interest expense as a share of assets, value 2.4%; contribution to the score · 2026-06-30 · +0.394 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 9.7%; contribution to the score · 2026-06-30 · -0.777 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: construction loans as a share of loans, value 3.1%; contribution to the score · 2026-06-30 · -0.373 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: total assets, value $972.1 million; contribution to the score · 2026-06-30 · -0.212 · data/analyst/scores.parquet: feature log_total_assets contribution
- F83 · Driver down #4: loan-loss reserves as a share of loans, value 1.0%; contribution to the score · 2026-06-30 · -0.191 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F84 · Driver down #5: volatile funding as a share of assets, value 3.4%; contribution to the score · 2026-06-30 · -0.180 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F85 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · -22.6% · data/features/fct_bank_features.parquet: return_on_equity
- F86 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 3.9% · data/features/fct_bank_features.parquet: return_on_equity
- F87 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 42.0% · data/features/fct_bank_features.parquet: return_on_equity
- F89 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · +0.608 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F91 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · -1.6% · data/features/fct_bank_features.parquet: return_on_assets
- F92 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F93 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F95 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.036 · data/analyst/scores.parquet: feature return_on_assets contribution
- F96 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature return_on_assets contribution
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 146.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 49.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 110.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · -0.035 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F102 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F103 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F104 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 7.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F105 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 9.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F108 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2026-06-30 · +0.099 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F109 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F110 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 74.8% · data/features/fct_bank_features.parquet: texas_ratio
- F111 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 13.1% · data/features/fct_bank_features.parquet: texas_ratio
- F112 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 57.0% · data/features/fct_bank_features.parquet: texas_ratio
- F113 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2026-06-30 · +17.8 pp · data/features/fct_bank_features.parquet: texas_ratio
- F114 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over four quarters, in percentage points · 2026-06-30 · +45.6 pp · data/features/fct_bank_features.parquet: texas_ratio
- F115 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · +0.678 · data/analyst/scores.parquet: feature texas_ratio contribution
- F116 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F117 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 3.1% · data/features/fct_bank_features.parquet: net_interest_margin
- F118 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.4% · data/features/fct_bank_features.parquet: net_interest_margin
- F119 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 4.4% · data/features/fct_bank_features.parquet: net_interest_margin
- F121 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.055 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F122 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F123 · Trend: ratios outside their own prior range · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F125 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F126 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F128 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 97.6% · data/analyst/scores.parquet: percentile
- F129 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F133 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 74.8% · data/features/fct_bank_features.parquet: texas_ratio
- F134 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: texas_ratio
- F135 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F136 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: texas_ratio
- F137 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: texas_ratio
- F138 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F139 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -22.6% · data/features/fct_bank_features.parquet: return_on_equity
- F140 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.8th · data/features/fct_bank_features.parquet: return_on_equity
- F141 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F142 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 0.2nd · data/features/fct_bank_features.parquet: return_on_equity
- F143 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 11.7% · data/features/fct_bank_features.parquet: return_on_equity
- F144 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F145 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 8.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F146 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.2nd · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F147 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F148 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.5th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F149 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F150 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F151 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2026-06-30 · 6.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F152 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.8th · data/features/fct_bank_features.parquet: leverage_ratio
- F153 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F154 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2026-06-30 · 0.4th · data/features/fct_bank_features.parquet: leverage_ratio
- F155 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2026-06-30 · 10.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F156 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F157 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 9.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F158 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.9th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F159 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F160 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 1.3rd · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F161 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-06-30 · 14.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F162 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F163 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 10.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F164 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.9th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F165 · Peers: the total risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F166 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 1.4th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F167 · Peers: the total risk-based capital ratio, peer median · 2026-06-30 · 15.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F168 · Peers: the total risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F169 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-06-30 · 146.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F170 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-06-30 · 98.9th · data/features/fct_bank_features.parquet: efficiency_ratio
- F171 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F172 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: efficiency_ratio
- F173 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-06-30 · 63.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F174 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F175 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2026-06-30 · -1.6% · data/features/fct_bank_features.parquet: return_on_assets
- F176 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 1.4th · data/features/fct_bank_features.parquet: return_on_assets
- F177 · Peers: return on assets (profit as a share of assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F178 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2026-06-30 · 0.7th · data/features/fct_bank_features.parquet: return_on_assets
- F179 · Peers: return on assets (profit as a share of assets), peer median · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets
- F180 · Peers: return on assets (profit as a share of assets), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F182 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 12 · data/features/fct_bank_features.parquet
- F183 · Peers: those ratios also unusual among peers · 2026-06-30 · 11 · data/features/fct_bank_features.parquet
- F185 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
