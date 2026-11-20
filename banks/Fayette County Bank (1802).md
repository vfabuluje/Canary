---
cert: 1802
name: "Fayette County Bank"
as_of: 2017-03-31
rank: 1
n_banks: 5925
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-05-26
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:13:39"
writer_model: "claude-opus-5-5"
checked: true
---

# Fayette County Bank (cert 1802)

*Hindsight: failed 2017-05-26. Canary flagged it 4 quarters ahead.*

## Summary

As of 2017-03-31, Fayette County Bank, an Illinois bank with total assets of $34.4 million, ranked 1 out of 5,925 banks nationally on Canary's risk score, the 100.0th percentile, and was on Canary's watchlist. Its capital cushion was extremely thin, with equity (the owners' stake that absorbs losses) at 1.0% of assets against a national median of 10.7%. Problem loans were high, with 13.3% of loans 90+ days past due or no longer earning interest against a national median of 0.6%, and the bank was losing money, with return on assets of -1.3% against a median of 0.9%. The separate commercial real estate screen did not flag it, so the concern here comes from capital, loan quality and losses rather than real-estate concentration.

## Warning signs in the data

Capital, the cushion that absorbs losses, was far below normal on every measure as of Q1 2017. Equity was 1.0% of assets against a national median of 10.7%, and the leverage ratio (core capital as a share of average assets) was 0.9% against a median of 10.5%. The Tier 1 risk-based capital ratio (core capital measured against assets weighted by riskiness) was 1.3% against a median of 15.1%, and the total risk-based capital ratio was 2.6% against a median of 16.2%.

Credit quality was poor: loans 90+ days past due or not accruing interest were 13.3% of loans against a national median of 0.6%, and loans 30-89 days past due were 5.0% of assets against a median of 0.3%. Nonaccrual assets and foreclosed property were 9.7% of assets against a median of 0.5%, and the Texas ratio (troubled assets against capital plus reserves) was 247.7% against a median of 4.8%. The bank was writing off loans at 2.2% of loans against a median of 0.0%, and it was unprofitable, with return on equity of -118.2% against a median of 8.0% and an efficiency ratio (costs as a share of revenue) of 130.2% against a median of 69.8%.

Funding points in a different direction and is mostly not stretched: uninsured deposits were only 3.4% of deposits against a median of 17.3%, and volatile funding was 1.9% of assets against a median of 5.1%. The exception is brokered deposits (money placed through outside brokers), at 25.0% of deposits against a national median of 0.0%, while cash was a low 2.4% of assets against a median of 6.9%. Unrealized losses on bonds available for sale (bonds the bank could sell) stood at -9.2% of equity against a national median of 0.3%, a sizable hit relative to its small capital base.

## Understanding the score

As of 2017-03-31, Fayette County Bank ranked 1 out of 5,925 banks, the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was one of 119 banks on Canary's watchlist that quarter, which covers the top 2% of banks by score.

The five factors that pushed the score up most were the Tier 1 risk-based capital ratio at 1.3%, return on equity at -118.2%, the Texas ratio at 247.7%, loans 90+ days past due or not accruing at 13.3% of loans, and the leverage ratio at 0.9%. The weak Tier 1 capital ratio was the single largest push, contributing +2.037 to the score.

The five factors that pulled the score down most were construction loans at 2.1% of loans, losses on bonds available for sale at -9.2% of equity, interest expense at 1.1% of assets, volatile funding at 1.9% of assets, and core deposits (stable everyday deposits) at 72.3% of assets. These offsets were small, the largest being -0.228 from construction loans, against much larger upward pushes.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 13 | 6,193 | ▲ watchlist |
| 2016-06-30 | 6 | 6,129 | ▲ watchlist (first flag) |
| 2016-09-30 | 3 | 6,051 | ▲ watchlist |
| 2016-12-31 | 1 | 5,983 | ▲ watchlist |
| 2017-03-31 | 1 | 5,925 | ▲ watchlist |

## How its ratios moved

As of 2017-03-31, Fayette County Bank ranked 1 out of 5,925 banks nationally, the 100.0th percentile, where higher means riskier. A year earlier it sat at the 99.8th percentile, and the model rated it about the same as a year earlier. Each ratio is compared with its own range over the prior 12 quarters, and 8 of the 30 ratios checked were outside that range.

Brokered deposits (money placed at the bank through outside brokers) made up 25.0% of deposits, just below their prior range of 25.8% to 41.0%, yet this ratio pushed the score up by +0.334 model log-odds units, the largest push in that direction. That share fell by -13.1 pp over four quarters. Losses on bonds available for sale (unrealized losses on bonds the bank could sell) stood at -9.2% of equity, below their prior range of -8.5% to 2.4%, but this ratio pushed the score down by -0.198. Interest expense, the cost of paying interest on deposits and borrowings, was 1.1% of assets, above its prior range of 0.7% to 1.0%, yet it pushed the score down by -0.180.

Core deposits (stable, everyday customer deposits) reached 72.3% of assets, above their prior range of 53.2% to 71.2%, and this pushed the score down by -0.061. The provision for loan losses, money set aside to cover expected bad loans, was 0.5% of assets, below its prior range of 1.8% to 4.7%, and it pushed the score down by -0.052. Return on assets, or profit as a share of assets, was -1.3%, above its prior range of -6.5% to -1.9%, yet it had little effect on the score at -0.029. The bank was still losing money, though less than before, with return on assets changing by +5.2 pp over four quarters.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | 0.5% | 1.8% to 4.7% | same quarter, prior 3 years | n/a | -4.2 pp | -0.052 | pushed the score down |
| return on assets (profit as a share of assets) | -1.3% | -6.5% to -1.9% | same quarter, prior 3 years | n/a | +5.2 pp | -0.029 | little effect on the score |
| annualized interest expense as a share of assets | 1.1% | 0.7% to 1.0% | same quarter, prior 3 years | n/a | +0.1 pp | -0.180 | pushed the score down |
| losses on bonds available for sale, as a share of equity | -9.2% | -8.5% to 2.4% | prior 12 quarters | -9.6 pp | -2.7 pp | -0.198 | pushed the score down |
| core deposits as a share of assets | 72.3% | 53.2% to 71.2% | prior 12 quarters | +1.0 pp | +15.4 pp | -0.061 | pushed the score down |
| brokered deposits as a share of deposits | 25.0% | 25.8% to 41.0% | prior 12 quarters | -0.8 pp | -13.1 pp | +0.334 | pushed the score up |

8 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2017-03-31: All Other Under 1 Billion.

This is a general group: the FDIC did not record a lending specialty for this bank.

Peers: 222 banks in the same specialty group and size tier (under $100 million).

As of Q1 2017, Fayette County Bank ranked 1 out of 5,925 banks nationally, which places it at the 100.0th percentile on Canary's scale. Its total risk-based capital ratio (capital measured against assets weighted by how likely they are to lose value) was 2.6%, at the 0.0th national percentile, which is unusually low, and at the 0.2nd percentile among its peers against a peer median of 19.9%, unusually low among its peers too. Its Tier 1 risk-based capital ratio (the same measure using only the strongest, core capital) was 1.3%, at the 0.0th national percentile, which is unusually low, and at the 0.2nd percentile among its peers against a peer median of 18.8%, unusually low among its peers too. Equity as a share of assets (the owners' cushion against losses) was 1.0%, at the 0.3rd national percentile, which is unusually low, and at the 0.2nd percentile among its peers against a peer median of 10.5%, unusually low among its peers too. The leverage ratio (core capital as a share of average assets) was 0.9%, at the 0.3rd national percentile, which is unusually low, and at the 0.2nd percentile among its peers against a peer median of 10.5%, unusually low among its peers too.

Return on equity (profit as a share of the owners' stake) was -118.2%, at the 0.0th national percentile, which is unusually low, and at the 0.7th percentile among its peers against a peer median of 6.2%, unusually low among its peers too. The Texas ratio (troubled assets compared with capital plus loss reserves) was 247.7%, at the 99.9th national percentile, which is unusually high, and at the 99.8th percentile among its peers against a peer median of 6.6%, unusually high among its peers too. Loans 90 or more days past due or no longer earning interest made up 13.3% of loans, at the 99.7th national percentile, which is unusually high, and at the 99.8th percentile among its peers against a peer median of 0.9%, unusually high among its peers too. Losses on bonds available for sale (bonds the bank may sell before they mature), as a share of equity, stood at -9.2%, at the 0.3rd national percentile, which is unusually low, and at the 0.2nd percentile among its peers against a peer median of 0.2%, unusually low among its peers too.

Overall, 20 of the bank's ratios fell in the national top or bottom 10%, and 18 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the total risk-based capital ratio | 2.6% | 0.0th (unusually low) | 19.9% | 0.2nd | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 1.3% | 0.0th (unusually low) | 18.8% | 0.2nd | unusually low among its peers too |
| return on equity (profit as a share of equity) | -118.2% | 0.0th (unusually low) | 6.2% | 0.7th | unusually low among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 247.7% | 99.9th (unusually high) | 6.6% | 99.8th | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 13.3% | 99.7th (unusually high) | 0.9% | 99.8th | unusually high among its peers too |
| equity as a share of assets | 1.0% | 0.3rd (unusually low) | 10.5% | 0.2nd | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | 0.9% | 0.3rd (unusually low) | 10.5% | 0.2nd | unusually low among its peers too |
| losses on bonds available for sale, as a share of equity | -9.2% | 0.3rd (unusually low) | 0.2% | 0.2nd | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: total risk-based capital, as the 2006 guidance specifies.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 92.4% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 99.8% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -52.7% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, Fayette County Bank failed on 2017-05-26. Canary first flagged it in the quarter ending 2016-06-30, a lead time of 4 quarters before the failure.

At that first flag, the top factors pushing the score up were return on equity at -74.1%, the Tier 1 risk-based capital ratio at 6.1%, the Texas ratio at 136.2%, and loans 90+ days past due or not accruing at 12.8% of loans. The same themes of losses, thin capital and bad loans were already visible then and had deepened by the as-of quarter, when the Tier 1 ratio was 1.3% and the Texas ratio 247.7%.

## What happened next

In hindsight, the last quarter the bank reported was 2017-03-31, the same quarter this memo describes. The bank failed on May 26, 2017, so there are no later ranks or flags for it.

## Sources

- F1 · Bank name · n/a · Fayette County Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2017-03-31 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2017-03-31 · 5,925 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2017-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2017-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2017-03-31 · 119 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2017-03-31 · 1.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2017-03-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · 0.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2017-03-31 · 1.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2017-03-31 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2017-03-31 · 2.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2017-03-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 13.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 9.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2017-03-31 · 5.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2017-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2017-03-31 · 2.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2017-03-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 247.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 4.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2017-03-31 · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2017-03-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2017-03-31 · -118.2% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2017-03-31 · 8.0% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2017-03-31 · 130.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2017-03-31 · 69.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2017-03-31 · 3.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2017-03-31 · 17.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2017-03-31 · 25.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2017-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2017-03-31 · 1.9% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2017-03-31 · 5.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2017-03-31 · 2.4% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2017-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2017-03-31 · -9.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2017-03-31 · 0.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2017-03-31 · $34.4 million · data/features/fct_bank_features.parquet: log_total_assets
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 1.3%; contribution to the score · 2017-03-31 · +2.037 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -118.2%; contribution to the score · 2017-03-31 · +1.311 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 247.7%; contribution to the score · 2017-03-31 · +1.137 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 13.3%; contribution to the score · 2017-03-31 · +0.686 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the leverage ratio (core capital as a share of average assets), value 0.9%; contribution to the score · 2017-03-31 · +0.557 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #1: construction loans as a share of loans, value 2.1%; contribution to the score · 2017-03-31 · -0.228 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F81 · Driver down #2: losses on bonds available for sale, as a share of equity, value -9.2%; contribution to the score · 2017-03-31 · -0.198 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F82 · Driver down #3: annualized interest expense as a share of assets, value 1.1%; contribution to the score · 2017-03-31 · -0.180 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F83 · Driver down #4: volatile funding as a share of assets, value 1.9%; contribution to the score · 2017-03-31 · -0.070 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F84 · Driver down #5: core deposits as a share of assets, value 72.3%; contribution to the score · 2017-03-31 · -0.061 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F85 · Failure date · 2017-05-26 · 2017-05-26 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-06-30 · 2016-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-06-30: return on equity (profit as a share of equity), value -74.1%; contribution to the score · 2016-06-30 · +1.121 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2016-06-30: the Tier 1 risk-based capital ratio, value 6.1%; contribution to the score · 2016-06-30 · +1.056 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F90 · Driver up #3 at 2016-06-30: the Texas ratio (troubled assets against capital plus reserves), value 136.2%; contribution to the score · 2016-06-30 · +0.880 · data/analyst/scores.parquet: feature texas_ratio contribution
- F91 · Driver up #4 at 2016-06-30: loans 90+ days past due or not accruing interest, as a share of loans, value 12.8%; contribution to the score · 2016-06-30 · +0.668 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F98 · Last quarter the bank reported · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2017-03-31 · 0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F100 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 1.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F101 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 4.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F103 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2017-03-31 · -0.052 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F104 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2017-03-31 · pushed the score down · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F105 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2017-03-31 · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F106 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -6.5% · data/features/fct_bank_features.parquet: return_on_assets
- F107 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -1.9% · data/features/fct_bank_features.parquet: return_on_assets
- F108 · Trend: return on assets (profit as a share of assets), change over four quarters, in percentage points · 2017-03-31 · +5.2 pp · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2017-03-31 · -0.029 · data/analyst/scores.parquet: feature return_on_assets contribution
- F110 · Trend: return on assets (profit as a share of assets), what the model did with it · 2017-03-31 · little effect on the score · data/analyst/scores.parquet: feature return_on_assets contribution
- F111 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2017-03-31 · 1.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F112 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F113 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F115 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2017-03-31 · -0.180 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F116 · Trend: annualized interest expense as a share of assets, what the model did with it · 2017-03-31 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F117 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2017-03-31 · -9.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F118 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · -8.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F119 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 2.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F122 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2017-03-31 · -0.198 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F123 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2017-03-31 · pushed the score down · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F124 · Trend: core deposits as a share of assets, value at the as-of quarter · 2017-03-31 · 72.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F125 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 53.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F126 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 71.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F129 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2017-03-31 · -0.061 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F130 · Trend: core deposits as a share of assets, what the model did with it · 2017-03-31 · pushed the score down · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F131 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2017-03-31 · 25.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F132 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 25.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F133 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 41.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F135 · Trend: brokered deposits as a share of deposits, change over four quarters, in percentage points · 2017-03-31 · -13.1 pp · data/features/fct_bank_features.parquet: brokered_to_deposits
- F136 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2017-03-31 · +0.334 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F137 · Trend: brokered deposits as a share of deposits, what the model did with it · 2017-03-31 · pushed the score up · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F138 · Trend: ratios outside their own prior range · 2017-03-31 · 8 · data/features/fct_bank_features.parquet
- F140 · Trend: ratios compared with their own prior range · 2017-03-31 · 30 · data/features/fct_bank_features.parquet
- F141 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F143 · Percentile a year earlier (100 = highest risk) · 2016-03-31 · 99.8% · data/analyst/scores.parquet: percentile
- F144 · Trend: how the model's rating compares with a year earlier · 2017-03-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F148 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2017-03-31 · 2.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F149 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2017-03-31 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F150 · Peers: the total risk-based capital ratio, national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F151 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2017-03-31 · 0.2nd · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F152 · Peers: the total risk-based capital ratio, peer median · 2017-03-31 · 19.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F153 · Peers: the total risk-based capital ratio, reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F154 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2017-03-31 · 1.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F155 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2017-03-31 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F156 · Peers: the Tier 1 risk-based capital ratio, national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F157 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2017-03-31 · 0.2nd · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F158 · Peers: the Tier 1 risk-based capital ratio, peer median · 2017-03-31 · 18.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F159 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F160 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2017-03-31 · -118.2% · data/features/fct_bank_features.parquet: return_on_equity
- F161 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2017-03-31 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F162 · Peers: return on equity (profit as a share of equity), national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F163 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2017-03-31 · 0.7th · data/features/fct_bank_features.parquet: return_on_equity
- F164 · Peers: return on equity (profit as a share of equity), peer median · 2017-03-31 · 6.2% · data/features/fct_bank_features.parquet: return_on_equity
- F165 · Peers: return on equity (profit as a share of equity), reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F166 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2017-03-31 · 247.7% · data/features/fct_bank_features.parquet: texas_ratio
- F167 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2017-03-31 · 99.9th · data/features/fct_bank_features.parquet: texas_ratio
- F168 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2017-03-31 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F169 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2017-03-31 · 99.8th · data/features/fct_bank_features.parquet: texas_ratio
- F170 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2017-03-31 · 6.6% · data/features/fct_bank_features.parquet: texas_ratio
- F171 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2017-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F172 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2017-03-31 · 13.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F173 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2017-03-31 · 99.7th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F174 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2017-03-31 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F175 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2017-03-31 · 99.8th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F176 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2017-03-31 · 0.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F177 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2017-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F178 · Peers: equity as a share of assets, bank value at the as-of quarter · 2017-03-31 · 1.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F179 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2017-03-31 · 0.3rd · data/features/fct_bank_features.parquet: equity_to_assets
- F180 · Peers: equity as a share of assets, national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F181 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2017-03-31 · 0.2nd · data/features/fct_bank_features.parquet: equity_to_assets
- F182 · Peers: equity as a share of assets, peer median · 2017-03-31 · 10.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F183 · Peers: equity as a share of assets, reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F184 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2017-03-31 · 0.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F185 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2017-03-31 · 0.3rd · data/features/fct_bank_features.parquet: leverage_ratio
- F186 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F187 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2017-03-31 · 0.2nd · data/features/fct_bank_features.parquet: leverage_ratio
- F188 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2017-03-31 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F189 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F190 · Peers: losses on bonds available for sale, as a share of equity, bank value at the as-of quarter · 2017-03-31 · -9.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F191 · Peers: losses on bonds available for sale, as a share of equity, national percentile (100 = highest value among all banks) · 2017-03-31 · 0.3rd · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F192 · Peers: losses on bonds available for sale, as a share of equity, national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F193 · Peers: losses on bonds available for sale, as a share of equity, percentile among its peers (100 = highest value) · 2017-03-31 · 0.2nd · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F194 · Peers: losses on bonds available for sale, as a share of equity, peer median · 2017-03-31 · 0.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F195 · Peers: losses on bonds available for sale, as a share of equity, reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F197 · Peers: ratios in the national top or bottom 10% · 2017-03-31 · 20 · data/features/fct_bank_features.parquet
- F198 · Peers: those ratios also unusual among peers · 2017-03-31 · 18 · data/features/fct_bank_features.parquet
- F200 · Peers: cut-off for unusual (top or bottom share of banks) · 2017-03-31 · 10% · data/features/fct_bank_features.parquet
