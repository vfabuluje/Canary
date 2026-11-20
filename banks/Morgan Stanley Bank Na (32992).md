---
cert: 32992
name: "Morgan Stanley Bank Na"
as_of: 2026-06-30
rank: 72
n_banks: 4313
percentile: 98.35381405054487
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-20T09:56:00"
writer_model: "claude-opus-5-5"
checked: true
---

# Morgan Stanley Bank Na (cert 32992)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Canary's model ranked Morgan Stanley Bank Na, a Utah bank, 72 out of 4,313 banks nationally, placing it in the 98.4th percentile, where higher means riskier. That put it on the watchlist, which covers the top 2% of banks by score. The score was pushed up mostly by how the bank funds itself, especially brokered deposits (money placed through outside brokers) at 22.4% of deposits and deposit growth of 44.6% over the past four quarters. Its loan quality and risk-based capital looked strong, so its funding and its loan book point in different directions.

## Warning signs in the data

Funding is where the bank stands out most from the national median. Brokered deposits were 22.4% of deposits, against a national median of 0.0%. Uninsured deposits, balances above the government insurance limit, were 42.4% of deposits, well above the 24.8% median. Core deposits, the steadier everyday deposits, were only 49.2% of assets, well below the 75.5% median, while volatile funding was 14.5% of assets, above the 9.0% median. Interest expense was 2.5% of assets, above the 1.6% median, and assets grew 75.3% over the past four quarters, far above the 4.5% median. On the other side, cash was 18.9% of assets, well above the 6.2% median.

Capital, a bank's own money that absorbs losses, is mixed. Equity was 9.7% of assets and the leverage ratio was 10.4%, both a little below the national medians of 10.6% and 11.0%. The risk-based measures were stronger: the Tier 1 risk-based capital ratio was 18.2% against a 14.6% median, and the total risk-based capital ratio was 18.7% against 15.8%. Losses on bonds held to maturity equalled 6.5% of equity, well above the 0.0% median, while losses on bonds available for sale were 3.6% of equity, below the 5.6% median.

Credit quality shows few warning signs. Loans 90+ days past due or not accruing interest were 0.5% of loans, equal to the median, and the Texas ratio (troubled assets against capital plus reserves) was 1.3%, below the 2.9% median. Loan-loss reserves were thin at 0.5% of loans against a 1.2% median. The peer section notes that many of these funding figures are typical for similar large banks, even though they are unusual nationally, and the real-estate check found the bank did not cross either line.

## Understanding the score

The model ranked the bank 72 out of 4,313 banks on 2026-06-30, the 98.4th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks, 87 banks that quarter.

The five features that pushed the score up most were brokered deposits at 22.4% of deposits (+0.786), deposit growth over the past four quarters of 44.6% (+0.434), and core deposits at 49.2% of assets (+0.370). The other two were interest expense at 2.5% of assets (+0.353) and commercial real estate loans at 7.4% of loans (+0.279).

The five that pulled the score down most were the Texas ratio at 1.3% (-1.160), the Tier 1 risk-based capital ratio at 18.2% (-0.843), and return on equity, profit as a share of equity, at 15.3% (-0.529). The last two were loans 90+ days past due or not accruing interest at 0.5% of loans (-0.351) and total assets of $419.3 billion (-0.310).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 2,076 | 4,589 |  |
| 2024-12-31 | 788 | 4,560 |  |
| 2025-03-31 | 668 | 4,536 |  |
| 2025-06-30 | 439 | 4,494 |  |
| 2025-09-30 | 286 | 4,452 |  |
| 2025-12-31 | 485 | 4,411 |  |
| 2026-03-31 | 110 | 4,353 |  |
| 2026-06-30 | 72 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, the model ranked Morgan Stanley Bank Na 72 out of 4,313 banks nationally, placing it in the 98.4th percentile, where higher means riskier. A year earlier, on 2025-06-30, its percentile was 90.3%, and the model rated it riskier than a year earlier. Of the 30 ratios compared with the bank's own prior range, usually the prior 12 quarters, 15 sat outside that range.

The efficiency ratio, which is operating costs as a share of revenue, stood at 36.8%, well above its prior range of 14.3% to 18.1%, and its contribution of +0.258 model log-odds units pushed the score up. That ratio rose by +18.7 pp over four quarters. Loans as a share of deposits fell to 41.1%, below its prior range of 43.5% to 50.2%, and its contribution of +0.137 model log-odds units pushed the score up.

Several other ratios were also below their prior range, yet the model treated them differently. Return on equity, which is profit as a share of shareholders' money, was 15.3%, below its prior range of 19.5% to 23.9%, but its contribution of -0.529 model log-odds units pushed the score down. Return on assets, which is profit as a share of everything the bank owns, was 1.6%, below its prior range of 1.9% to 2.4%, but its contribution of -0.197 model log-odds units pushed the score down. The Tier 1 risk-based capital ratio, a measure of the bank's loss-absorbing cushion, was 18.2%, below its prior range of 19.5% to 23.0%, but its contribution of -0.843 model log-odds units pushed the score down. Net interest margin, the spread earned on lending and investing, was 1.5%, below its prior range of 2.0% to 2.7%, yet its contribution of -0.013 model log-odds units had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 36.8% | 14.3% to 18.1% | same quarter, prior 3 years | n/a | +18.7 pp | +0.258 | pushed the score up |
| return on equity (profit as a share of equity) | 15.3% | 19.5% to 23.9% | same quarter, prior 3 years | n/a | -4.2 pp | -0.529 | pushed the score down |
| net interest margin (the spread earned on lending and investing) | 1.5% | 2.0% to 2.7% | same quarter, prior 3 years | n/a | -0.5 pp | -0.013 | little effect on the score |
| return on assets (profit as a share of assets) | 1.6% | 1.9% to 2.4% | same quarter, prior 3 years | n/a | -0.4 pp | -0.197 | pushed the score down |
| the Tier 1 risk-based capital ratio | 18.2% | 19.5% to 23.0% | prior 12 quarters | -1.3 pp | -2.2 pp | -0.843 | pushed the score down |
| loans as a share of deposits | 41.1% | 43.5% to 50.2% | prior 12 quarters | -3.4 pp | -8.1 pp | +0.137 | pushed the score up |

15 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: All Other Over 1 Billion.

This is a general group: the FDIC did not record a lending specialty for this bank.

Peers: 30 banks in the same specialty group and size tier (over $10 billion).

The bank's assets grew 75.3% over the past four quarters, which places it in the 99.2nd percentile nationally, unusually high, and in the 95.0th percentile among its peers against a peer median of 6.6%, making it unusually high among its peers too. Its deposits grew 44.6% over the past four quarters, in the 98.1st percentile nationally, unusually high, and in the 94.8th percentile among its peers against a peer median of 6.1%, so this is also unusually high among its peers too.

Its net interest margin, the spread a bank earns on its lending and investing, is 1.5%, in the 1.3rd percentile nationally, unusually low, but in the 18.3rd percentile among its peers against a peer median of 2.6%, which is typical for its peer group. Core deposits, the steadier everyday deposits a bank relies on, make up 49.2% of its assets, in the 5.2nd percentile nationally, unusually low, and in the 15.5th percentile among its peers against a peer median of 69.5%, which is typical for its peer group. Brokered deposits, money placed with the bank through outside brokers, are 22.4% of its deposits, in the 96.3rd percentile nationally, unusually high, and in the 73.2nd percentile among its peers against a peer median of 6.0%, which is typical for its peer group. Losses on bonds the bank plans to hold until they mature equal 6.5% of its equity, its own capital cushion, in the 93.5th percentile nationally, unusually high, and in the 67.2nd percentile among its peers against a peer median of 0.7%, which is typical for its peer group.

Overall, 10 of the bank's ratios fall in the national top or bottom 10%, and 2 of those are also unusual among its peers, suggesting that most of its standout figures are shared by similar large banks.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| asset growth over the past four quarters | 75.3% | 99.2nd (unusually high) | 6.6% | 95.0th | unusually high among its peers too |
| net interest margin (the spread earned on lending and investing) | 1.5% | 1.3rd (unusually low) | 2.6% | 18.3rd | typical for its peer group |
| deposit growth over the past four quarters | 44.6% | 98.1st (unusually high) | 6.1% | 94.8th | unusually high among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 36.8% | 3.7th (unusually low) | 53.4% | 25.0th | typical for its peer group |
| brokered deposits as a share of deposits | 22.4% | 96.3rd (unusually high) | 6.0% | 73.2nd | typical for its peer group |
| loan-loss reserves as a share of loans | 0.5% | 4.0th (unusually low) | 0.9% | 30.4th | typical for its peer group |
| core deposits as a share of assets | 49.2% | 5.2nd (unusually low) | 69.5% | 15.5th | typical for its peer group |
| losses on bonds held to maturity, as a share of equity | 6.5% | 93.5th (unusually high) | 0.7% | 67.2nd | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.6% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 23.4% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -4.3% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight, this bank's outcome case is that it remains open and on the watchlist. The fact sheet holds no data from after the as-of quarter, so this note cannot add later figures that explain why it stays flagged. The reasons on record are the as-of funding signals described above, which the model weighed more heavily than the bank's strong loan quality.

## What happened next

Looking back with hindsight, the bank is treated as still open and on the watchlist. Our fact sheet contains no later ranks, flags or reporting status, so we cannot say how its position has moved since the as-of quarter.

## Sources

- F1 · Bank name · n/a · Morgan Stanley Bank Na · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · UT · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 72 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 98.4% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 9.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 18.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 18.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 1.3% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 42.4% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 22.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 49.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 14.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 18.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 6.5% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 3.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2026-06-30 · 75.3% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2026-06-30 · 4.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 22.4%; contribution to the score · 2026-06-30 · +0.786 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: deposit growth over the past four quarters, value 44.6%; contribution to the score · 2026-06-30 · +0.434 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F77 · Driver up #3: core deposits as a share of assets, value 49.2%; contribution to the score · 2026-06-30 · +0.370 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F78 · Driver up #4: annualized interest expense as a share of assets, value 2.5%; contribution to the score · 2026-06-30 · +0.353 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F79 · Driver up #5: commercial real estate loans as a share of loans, value 7.4%; contribution to the score · 2026-06-30 · +0.279 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 1.3%; contribution to the score · 2026-06-30 · -1.160 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 18.2%; contribution to the score · 2026-06-30 · -0.843 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 15.3%; contribution to the score · 2026-06-30 · -0.529 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: loans 90+ days past due or not accruing interest, as a share of loans, value 0.5%; contribution to the score · 2026-06-30 · -0.351 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F84 · Driver down #5: total assets, value $419.3 billion; contribution to the score · 2026-06-30 · -0.310 · data/analyst/scores.parquet: feature log_total_assets contribution
- F89 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 36.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F90 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 14.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F91 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 18.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F92 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2026-06-30 · +18.7 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.258 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F94 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F95 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 15.3% · data/features/fct_bank_features.parquet: return_on_equity
- F96 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 19.5% · data/features/fct_bank_features.parquet: return_on_equity
- F97 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 23.9% · data/features/fct_bank_features.parquet: return_on_equity
- F99 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.529 · data/analyst/scores.parquet: feature return_on_equity contribution
- F100 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F101 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: net_interest_margin
- F102 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 2.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F103 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 2.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F105 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.013 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F106 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F107 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: return_on_assets
- F108 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 1.9% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 2.4% · data/features/fct_bank_features.parquet: return_on_assets
- F111 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.197 · data/analyst/scores.parquet: feature return_on_assets contribution
- F112 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F113 · Trend: the Tier 1 risk-based capital ratio, value at the as-of quarter · 2026-06-30 · 18.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F114 · Trend: the Tier 1 risk-based capital ratio, lowest value in the comparison window · n/a · 19.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F115 · Trend: the Tier 1 risk-based capital ratio, highest value in the comparison window · n/a · 23.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F118 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2026-06-30 · -0.843 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F119 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F120 · Trend: loans as a share of deposits, value at the as-of quarter · 2026-06-30 · 41.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F121 · Trend: loans as a share of deposits, lowest value in the comparison window · n/a · 43.5% · data/features/fct_bank_features.parquet: loans_to_deposits
- F122 · Trend: loans as a share of deposits, highest value in the comparison window · n/a · 50.2% · data/features/fct_bank_features.parquet: loans_to_deposits
- F125 · Trend: loans as a share of deposits, contribution to the score (model log-odds units) · 2026-06-30 · +0.137 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F126 · Trend: loans as a share of deposits, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F127 · Trend: ratios outside their own prior range · 2026-06-30 · 15 · data/features/fct_bank_features.parquet
- F129 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F130 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F132 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 90.3% · data/analyst/scores.parquet: percentile
- F133 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F137 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · 75.3% · data/features/fct_bank_features.parquet: asset_growth_4q
- F138 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.2nd · data/features/fct_bank_features.parquet: asset_growth_4q
- F139 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: asset_growth_4q
- F140 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 95.0th · data/features/fct_bank_features.parquet: asset_growth_4q
- F141 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 6.6% · data/features/fct_bank_features.parquet: asset_growth_4q
- F142 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F143 · Peers: net interest margin (the spread earned on lending and investing), bank value at the as-of quarter · 2026-06-30 · 1.5% · data/features/fct_bank_features.parquet: net_interest_margin
- F144 · Peers: net interest margin (the spread earned on lending and investing), national percentile (100 = highest value among all banks) · 2026-06-30 · 1.3rd · data/features/fct_bank_features.parquet: net_interest_margin
- F145 · Peers: net interest margin (the spread earned on lending and investing), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: net_interest_margin
- F146 · Peers: net interest margin (the spread earned on lending and investing), percentile among its peers (100 = highest value) · 2026-06-30 · 18.3rd · data/features/fct_bank_features.parquet: net_interest_margin
- F147 · Peers: net interest margin (the spread earned on lending and investing), peer median · 2026-06-30 · 2.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F148 · Peers: net interest margin (the spread earned on lending and investing), reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: net_interest_margin
- F149 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · 44.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F150 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.1st · data/features/fct_bank_features.parquet: deposit_growth_4q
- F151 · Peers: deposit growth over the past four quarters, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: deposit_growth_4q
- F152 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 94.8th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F153 · Peers: deposit growth over the past four quarters, peer median · 2026-06-30 · 6.1% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F154 · Peers: deposit growth over the past four quarters, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F161 · Peers: brokered deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 22.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F162 · Peers: brokered deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 96.3rd · data/features/fct_bank_features.parquet: brokered_to_deposits
- F163 · Peers: brokered deposits as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: brokered_to_deposits
- F164 · Peers: brokered deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 73.2nd · data/features/fct_bank_features.parquet: brokered_to_deposits
- F165 · Peers: brokered deposits as a share of deposits, peer median · 2026-06-30 · 6.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F166 · Peers: brokered deposits as a share of deposits, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: brokered_to_deposits
- F173 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2026-06-30 · 49.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F174 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 5.2nd · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F175 · Peers: core deposits as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F176 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 15.5th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F177 · Peers: core deposits as a share of assets, peer median · 2026-06-30 · 69.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F178 · Peers: core deposits as a share of assets, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F179 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2026-06-30 · 6.5% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F180 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2026-06-30 · 93.5th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F181 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F182 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2026-06-30 · 67.2nd · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F183 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F184 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F186 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 10 · data/features/fct_bank_features.parquet
- F187 · Peers: those ratios also unusual among peers · 2026-06-30 · 2 · data/features/fct_bank_features.parquet
- F189 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
