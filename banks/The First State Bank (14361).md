---
cert: 14361
name: "The First State Bank"
as_of: 2020-03-31
rank: 1
n_banks: 5182
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2020-04-03
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:14:02"
writer_model: "claude-opus-5-5"
checked: true
---

# The First State Bank (cert 14361)

*Hindsight: failed 2020-04-03. Canary flagged it 4 quarters ahead.*

## Summary

As of 2020-03-31, The First State Bank in WV ranked 1 out of 5,182 banks nationally on Canary's risk score, placing it at the 100.0th percentile and on the watchlist. Its capital cushion, the owners' money that absorbs losses, was very thin, with equity at 0.6% of assets against a national median of 11.4%. Problem loans were extreme: 26.7% of loans were seriously past due or not accruing interest, against a national median of 0.6%, and the bank was losing money. Its funding looked steadier than its capital or loans, because most of its money came from core deposits (stable, everyday deposits) and few deposits were uninsured.

## Warning signs in the data

Capital was far below normal levels. Equity was 0.6% of assets against a national median of 11.4%, and the leverage ratio (core capital as a share of average assets) was 0.3% against a median of 10.9%. The Tier 1 risk-based capital ratio (the strongest capital measured against assets weighted by riskiness) was 0.4% against a median of 14.6%, and the total risk-based capital ratio was 1.7% against 15.7%.

Credit quality was very weak: loans 90+ days past due or not accruing interest were 26.7% of loans against a national median of 0.6%, and nonaccrual assets plus foreclosed property were 26.0% of assets against 0.4%. The Texas ratio (troubled assets against capital plus reserves) was 1704.3% against a median of 3.8%, meaning troubled assets far exceeded the capital and reserves set aside to cover them. Loan-loss reserves were 2.0% of loans, above the 1.2% median, but small next to the scale of the problem loans. The bank was unprofitable, with return on assets of -4.1% against a median of 0.9% and an efficiency ratio (operating costs as a share of revenue) of 249.2% against 68.7%.

Funding pointed the other way: core deposits were 83.6% of assets against a median of 77.6%, uninsured deposits were 3.4% of deposits against 19.4%, and cash was 15.9% of assets against 7.8%. It did rely somewhat more than usual on brokered deposits (placed through middlemen), at 4.2% of deposits against 0.0%, and on Federal Home Loan Bank borrowings, at 3.8% of assets against 0.5%. Unrealized losses on bonds available for sale (bonds the bank may sell before maturity) were -40.1% of equity against a median of -0.8%, a large figure relative to its thin equity, though securities were only 6.9% of assets against a median of 15.2%. The trend section notes that the model treated this bond measure as lowering the score, so on this point the raw figure and the model's reading point different ways.

## Understanding the score

As of 2020-03-31, The First State Bank ranked 1 out of 5,182 banks, the 100.0th percentile on a 0 to 100 scale where higher means riskier. That put it on the watchlist, which covers the top 2% of banks by score and held 104 banks that quarter.

The five factors that pushed the score up most, with their contributions in model units, were the Tier 1 risk-based capital ratio at 0.4% (+2.093), return on equity (profit as a share of equity) at -406.7% (+1.374), the Texas ratio at 1704.3% (+1.289), loans 90+ days past due or not accruing interest at 26.7% of loans (+0.836), and the total risk-based capital ratio at 1.7% (+0.573). The five that pulled it down most were losses on bonds available for sale at -40.1% of equity (-0.267), interest expense at 1.5% of assets (-0.170), construction loans at 9.8% of loans (-0.117), total assets of $151.8 million (-0.089), and brokered deposits at 4.2% of deposits (-0.085). These downward pulls were small next to the capital and loan-quality factors pushing the score up.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2018-06-30 | 6 | 5,610 | ▲ watchlist |
| 2018-09-30 | 6 | 5,544 | ▲ watchlist |
| 2018-12-31 | 1 | 5,473 | ▲ watchlist |
| 2019-03-31 | 1 | 5,428 | ▲ watchlist |
| 2019-06-30 | 2 | 5,369 | ▲ watchlist (first flag) |
| 2019-09-30 | 4 | 5,325 | ▲ watchlist |
| 2019-12-31 | 1 | 5,244 | ▲ watchlist |
| 2020-03-31 | 1 | 5,182 | ▲ watchlist |

## How its ratios moved

As of 2020-03-31, the bank ranked 1 out of 5,182 banks nationally, placing it at the 100.0th percentile on a scale where higher means riskier. On 2019-03-31 it was also at the 100.0th percentile, and the model rated it about the same as a year earlier. Of 30 ratios compared with their own prior range, 21 sat outside it, and the table shows the 6 furthest outside. The prior range is the low and high over the prior 12 quarters, or, for year-to-date ratios, the same quarter in the prior 3 years.

Return on equity (profit as a share of the owners' stake) was -406.7%, far below its prior range of -69.4% to -21.7%, and its contribution of +1.374 model log-odds units pushed the score up. That ratio changed by -337.3 pp over four quarters. The Texas ratio (troubled assets against capital plus reserves) was 1704.3%, well above its prior range of 243.1% to 1120.2%, and its contribution of +1.289 model log-odds units pushed the score up. The Texas ratio rose by +584.1 pp over one quarter and by +1017.9 pp over four quarters. Return on assets (profit as a share of assets) was -4.1%, below its prior range of -2.5% to -1.3%, and its contribution of +0.205 model log-odds units pushed the score up. Net interest margin (the spread earned on lending and investing) was 2.3%, below its prior range of 3.6% to 3.9%, and its contribution of +0.081 model log-odds units pushed the score up.

The efficiency ratio (operating costs as a share of revenue) was 249.2%, well above its prior range of 122.3% to 150.0%, yet its contribution of -0.007 model log-odds units had little effect on the score. Losses on bonds available for sale (bonds the bank could sell), as a share of equity, were -40.1%, below their prior range of -5.6% to 11.9%, yet their contribution of -0.267 model log-odds units pushed the score down. That bond measure moved by -34.5 pp over one quarter and by -44.7 pp over four quarters.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -406.7% | -69.4% to -21.7% | same quarter, prior 3 years | n/a | -337.3 pp | +1.374 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 249.2% | 122.3% to 150.0% | same quarter, prior 3 years | n/a | +110.1 pp | -0.007 | little effect on the score |
| losses on bonds available for sale, as a share of equity | -40.1% | -5.6% to 11.9% | prior 12 quarters | -34.5 pp | -44.7 pp | -0.267 | pushed the score down |
| return on assets (profit as a share of assets) | -4.1% | -2.5% to -1.3% | same quarter, prior 3 years | n/a | -2.2 pp | +0.205 | pushed the score up |
| net interest margin (the spread earned on lending and investing) | 2.3% | 3.6% to 3.9% | same quarter, prior 3 years | n/a | -1.4 pp | +0.081 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 1704.3% | 243.1% to 1120.2% | prior 12 quarters | +584.1 pp | +1017.9 pp | +1.289 | pushed the score up |

21 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2020-03-31: Commercial Lending Specialization.

Peers: 1805 banks in the same specialty group and size tier ($100 million to $1 billion).

As of 2020-03-31, The First State Bank ranked 1 out of 5,182 banks nationally by Canary's score. Nonaccrual assets and foreclosed property (loans that have stopped paying interest plus repossessed property) were 26.0% of assets, at the 100.0th percentile nationally, which is unusually high, and at the 100.0th percentile among its peers against a peer median of 0.4%, which is unusually high among its peers too. Loans seriously past due or not accruing interest were 26.7% of loans, at the 99.9th percentile nationally, which is unusually high, and at the 100.0th percentile among its peers against a peer median of 0.5%, which is unusually high among its peers too. The Texas ratio (troubled assets measured against capital plus reserves) was 1704.3%, at the 100.0th percentile nationally, which is unusually high, and at the 100.0th percentile among its peers against a peer median of 4.3%, which is unusually high among its peers too.

Return on equity (profit as a share of the owners' stake) was -406.7%, at the 0.0th percentile nationally, which is unusually low, and at the 0.0th percentile among its peers against a peer median of 8.3%, which is unusually low among its peers too. The total risk-based capital ratio (capital held against assets weighted by their riskiness) was 1.7%, at the 0.0th percentile nationally, which is unusually low, and at the 0.0th percentile among its peers against a peer median of 14.9%, which is unusually low among its peers too. The Tier 1 risk-based capital ratio (the same measure using only the strongest form of capital) was 0.4%, at the 0.0th percentile nationally, which is unusually low, and at the 0.0th percentile among its peers against a peer median of 13.8%, which is unusually low among its peers too. Equity as a share of assets was 0.6%, at the 0.3rd percentile nationally, which is unusually low, and at the 0.1st percentile among its peers against a peer median of 10.9%, which is unusually low among its peers too. Losses on bonds available for sale (bonds the bank may sell before they mature), as a share of equity, were -40.1%, at the 0.0th percentile nationally, which is unusually low, and at the 0.0th percentile among its peers against a peer median of -0.7%, which is unusually low among its peers too.

Overall, 17 of the bank's ratios fell in the national top or bottom 10%, and 17 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| nonaccrual assets and foreclosed property, as a share of assets | 26.0% | 100.0th (unusually high) | 0.4% | 100.0th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -406.7% | 0.0th (unusually low) | 8.3% | 0.0th | unusually low among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 1704.3% | 100.0th (unusually high) | 4.3% | 100.0th | unusually high among its peers too |
| the total risk-based capital ratio | 1.7% | 0.0th (unusually low) | 14.9% | 0.0th | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 0.4% | 0.0th (unusually low) | 13.8% | 0.0th | unusually low among its peers too |
| losses on bonds available for sale, as a share of equity | -40.1% | 0.0th (unusually low) | -0.7% | 0.0th | unusually low among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 26.7% | 99.9th (unusually high) | 0.5% | 100.0th | unusually high among its peers too |
| equity as a share of assets | 0.6% | 0.3rd (unusually low) | 10.9% | 0.1st | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 373.8% | 100% or more | yes |
| Total commercial real estate loans ÷ capital | 594.9% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | -25.6% | 50% or more | no |

It crossed the construction line (100% or more of capital).
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, The First State Bank failed on 2020-04-03. Canary first flagged it in Q2 2019 under its lead-time rule, 4 quarters before the failure. At that first flag, the main drivers were already in place: the Tier 1 risk-based capital ratio was 3.3%, return on equity was -87.3%, and the Texas ratio was 704.2%. Loans 90+ days past due or not accruing interest were 19.1% of loans at that point, and each of these measures had worsened by the as-of quarter.

## What happened next

In hindsight, the bank's last reported quarter was 2020-03-31, and it failed on 2020-04-03. Because it stopped reporting after that quarter, there are no later ranks or watchlist flags to show.

## Sources

- F1 · Bank name · n/a · The First State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2020-03-31 · 2020-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WV · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2020-03-31 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2020-03-31 · 5,182 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2020-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2020-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2020-03-31 · 104 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2020-03-31 · 0.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2020-03-31 · 11.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2020-03-31 · 0.3% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2020-03-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2020-03-31 · 0.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2020-03-31 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2020-03-31 · 1.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2020-03-31 · 15.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2020-03-31 · 26.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2020-03-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2020-03-31 · 26.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2020-03-31 · 0.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2020-03-31 · 2.0% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2020-03-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2020-03-31 · 1704.3% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2020-03-31 · 3.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2020-03-31 · -4.1% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2020-03-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2020-03-31 · 249.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2020-03-31 · 68.7% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2020-03-31 · 3.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2020-03-31 · 19.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2020-03-31 · 4.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2020-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2020-03-31 · 83.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2020-03-31 · 77.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2020-03-31 · 3.8% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2020-03-31 · 0.5% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2020-03-31 · 15.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2020-03-31 · 7.8% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2020-03-31 · -40.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2020-03-31 · -0.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2020-03-31 · 6.9% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2020-03-31 · 15.2% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 0.4%; contribution to the score · 2020-03-31 · +2.093 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -406.7%; contribution to the score · 2020-03-31 · +1.374 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 1704.3%; contribution to the score · 2020-03-31 · +1.289 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 26.7%; contribution to the score · 2020-03-31 · +0.836 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 1.7%; contribution to the score · 2020-03-31 · +0.573 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: losses on bonds available for sale, as a share of equity, value -40.1%; contribution to the score · 2020-03-31 · -0.267 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 1.5%; contribution to the score · 2020-03-31 · -0.170 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: construction loans as a share of loans, value 9.8%; contribution to the score · 2020-03-31 · -0.117 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: total assets, value $151.8 million; contribution to the score · 2020-03-31 · -0.089 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: brokered deposits as a share of deposits, value 4.2%; contribution to the score · 2020-03-31 · -0.085 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F85 · Failure date · 2020-04-03 · 2020-04-03 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2019-06-30 · 2019-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2019-06-30: the Tier 1 risk-based capital ratio, value 3.3%; contribution to the score · 2019-06-30 · +1.924 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2019-06-30: return on equity (profit as a share of equity), value -87.3%; contribution to the score · 2019-06-30 · +1.438 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2019-06-30: the Texas ratio (troubled assets against capital plus reserves), value 704.2%; contribution to the score · 2019-06-30 · +1.210 · data/analyst/scores.parquet: feature texas_ratio contribution
- F91 · Driver up #4 at 2019-06-30: loans 90+ days past due or not accruing interest, as a share of loans, value 19.1%; contribution to the score · 2019-06-30 · +0.793 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F98 · Last quarter the bank reported · 2020-03-31 · 2020-03-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2020-03-31 · -406.7% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -69.4% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -21.7% · data/features/fct_bank_features.parquet: return_on_equity
- F102 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2020-03-31 · -337.3 pp · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2020-03-31 · +1.374 · data/analyst/scores.parquet: feature return_on_equity contribution
- F104 · Trend: return on equity (profit as a share of equity), what the model did with it · 2020-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2020-03-31 · 249.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 122.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 150.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F109 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2020-03-31 · -0.007 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2020-03-31 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F111 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2020-03-31 · -40.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F112 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · -5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F113 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 11.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F114 · Trend: losses on bonds available for sale, as a share of equity, change over one quarter, in percentage points · 2020-03-31 · -34.5 pp · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F115 · Trend: losses on bonds available for sale, as a share of equity, change over four quarters, in percentage points · 2020-03-31 · -44.7 pp · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F116 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2020-03-31 · -0.267 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F117 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2020-03-31 · pushed the score down · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F118 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2020-03-31 · -4.1% · data/features/fct_bank_features.parquet: return_on_assets
- F119 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -2.5% · data/features/fct_bank_features.parquet: return_on_assets
- F120 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F122 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2020-03-31 · +0.205 · data/analyst/scores.parquet: feature return_on_assets contribution
- F123 · Trend: return on assets (profit as a share of assets), what the model did with it · 2020-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F124 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2020-03-31 · 2.3% · data/features/fct_bank_features.parquet: net_interest_margin
- F125 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F126 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F128 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2020-03-31 · +0.081 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F129 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2020-03-31 · pushed the score up · data/analyst/scores.parquet: feature net_interest_margin contribution
- F130 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2020-03-31 · 1704.3% · data/features/fct_bank_features.parquet: texas_ratio
- F131 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 243.1% · data/features/fct_bank_features.parquet: texas_ratio
- F132 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 1120.2% · data/features/fct_bank_features.parquet: texas_ratio
- F133 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2020-03-31 · +584.1 pp · data/features/fct_bank_features.parquet: texas_ratio
- F134 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over four quarters, in percentage points · 2020-03-31 · +1017.9 pp · data/features/fct_bank_features.parquet: texas_ratio
- F135 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2020-03-31 · +1.289 · data/analyst/scores.parquet: feature texas_ratio contribution
- F136 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2020-03-31 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F137 · Trend: ratios outside their own prior range · 2020-03-31 · 21 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios shown in the table (the furthest outside their prior range) · 2020-03-31 · 6 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios compared with their own prior range · 2020-03-31 · 30 · data/features/fct_bank_features.parquet
- F140 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F142 · Percentile a year earlier (100 = highest risk) · 2019-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F143 · Trend: how the model's rating compares with a year earlier · 2020-03-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F147 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2020-03-31 · 26.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F148 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2020-03-31 · 100.0th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F149 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2020-03-31 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F150 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2020-03-31 · 100.0th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F151 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2020-03-31 · 0.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F152 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2020-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F153 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2020-03-31 · -406.7% · data/features/fct_bank_features.parquet: return_on_equity
- F154 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2020-03-31 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F155 · Peers: return on equity (profit as a share of equity), national reading · 2020-03-31 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F156 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2020-03-31 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F157 · Peers: return on equity (profit as a share of equity), peer median · 2020-03-31 · 8.3% · data/features/fct_bank_features.parquet: return_on_equity
- F158 · Peers: return on equity (profit as a share of equity), reading against its peers · 2020-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F159 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2020-03-31 · 1704.3% · data/features/fct_bank_features.parquet: texas_ratio
- F160 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2020-03-31 · 100.0th · data/features/fct_bank_features.parquet: texas_ratio
- F161 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2020-03-31 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F162 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2020-03-31 · 100.0th · data/features/fct_bank_features.parquet: texas_ratio
- F163 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2020-03-31 · 4.3% · data/features/fct_bank_features.parquet: texas_ratio
- F164 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2020-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F165 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2020-03-31 · 1.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F166 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2020-03-31 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F167 · Peers: the total risk-based capital ratio, national reading · 2020-03-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F168 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2020-03-31 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F169 · Peers: the total risk-based capital ratio, peer median · 2020-03-31 · 14.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F170 · Peers: the total risk-based capital ratio, reading against its peers · 2020-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F171 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2020-03-31 · 0.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F172 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2020-03-31 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F173 · Peers: the Tier 1 risk-based capital ratio, national reading · 2020-03-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F174 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2020-03-31 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F175 · Peers: the Tier 1 risk-based capital ratio, peer median · 2020-03-31 · 13.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F176 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2020-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F177 · Peers: losses on bonds available for sale, as a share of equity, bank value at the as-of quarter · 2020-03-31 · -40.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F178 · Peers: losses on bonds available for sale, as a share of equity, national percentile (100 = highest value among all banks) · 2020-03-31 · 0.0th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F179 · Peers: losses on bonds available for sale, as a share of equity, national reading · 2020-03-31 · unusually low · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F180 · Peers: losses on bonds available for sale, as a share of equity, percentile among its peers (100 = highest value) · 2020-03-31 · 0.0th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F181 · Peers: losses on bonds available for sale, as a share of equity, peer median · 2020-03-31 · -0.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F182 · Peers: losses on bonds available for sale, as a share of equity, reading against its peers · 2020-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F183 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2020-03-31 · 26.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F184 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2020-03-31 · 99.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F185 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2020-03-31 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F186 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2020-03-31 · 100.0th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F187 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2020-03-31 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F188 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2020-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F189 · Peers: equity as a share of assets, bank value at the as-of quarter · 2020-03-31 · 0.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F190 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2020-03-31 · 0.3rd · data/features/fct_bank_features.parquet: equity_to_assets
- F191 · Peers: equity as a share of assets, national reading · 2020-03-31 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F192 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2020-03-31 · 0.1st · data/features/fct_bank_features.parquet: equity_to_assets
- F193 · Peers: equity as a share of assets, peer median · 2020-03-31 · 10.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F194 · Peers: equity as a share of assets, reading against its peers · 2020-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F196 · Peers: ratios in the national top or bottom 10% · 2020-03-31 · 17 · data/features/fct_bank_features.parquet
- F197 · Peers: those ratios also unusual among peers · 2020-03-31 · 17 · data/features/fct_bank_features.parquet
- F199 · Peers: cut-off for unusual (top or bottom share of banks) · 2020-03-31 · 10% · data/features/fct_bank_features.parquet
