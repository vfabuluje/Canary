---
cert: 8758
name: "Citizens Bank"
as_of: 2023-09-30
rank: 1
n_banks: 4686
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2023-11-03
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:14:01"
writer_model: "claude-opus-5-5"
checked: true
---

# Citizens Bank (cert 8758)

*Hindsight: failed 2023-11-03. Canary flagged it 2 quarters ahead.*

## Summary

As of September 30, 2023, Canary's model ranked Citizens Bank, a $65.6 million bank in Iowa, 1 out of 4,686 FDIC-insured banks, the 100.0th percentile, where higher means riskier. Its capital, the owners' cushion that absorbs losses, had all but disappeared: equity was -4.5% of assets and its Tier 1 risk-based capital ratio (the highest-quality capital measured against risk-weighted assets) was 0.0%, against national medians of 9.1% and 14.2%. At the same time, bad loans were piling up, with net write-offs running at an annualized 15.1% of loans against a national median of 0.0%. It was on Canary's watchlist, which holds the riskiest 2% of banks.

## Warning signs in the data

Capital was the clearest problem as of 2023-09-30. Equity (what would be left for the owners if all debts were paid) was -4.5% of assets, against a national median of 9.1%. The leverage ratio (core capital as a share of average assets) was 0.0% against a median of 10.6%, and the total risk-based capital ratio was 1.3% against a median of 15.4%. The Texas ratio (troubled assets against capital plus reserves) read -261.2% against a median of 2.0%; with capital below zero, this normally useful ratio stops being meaningful, so its low value is not a sign of strength.

Credit quality, meaning how well borrowers were repaying, was also far weaker than typical. Loans 90+ days past due or no longer earning interest were 9.6% of loans against a national median of 0.3%, and nonaccrual assets plus foreclosed property were 5.9% of assets against a median of 0.1%. Loans 30-89 days past due, an earlier stage of trouble, were 1.5% of assets against a median of 0.2%. The bank was setting aside an annualized 9.8% of assets for expected loan losses against a median of 0.0%, and return on assets (profit as a share of everything it holds) was -10.0% against a median of 1.0%.

Funding showed some strain: uninsured deposits (balances above the government guarantee) were 34.5% of deposits against a median of 23.6%, volatile funding was 20.9% of assets against a median of 8.3%, and deposits shrank by -9.2% over the past four quarters against a median of -0.6%. Cash was 2.6% of assets, below the median of 5.4%, though core deposits, a steadier funding source, were 83.5% of assets, above the median of 77.3%. Securities made up 38.2% of assets against a median of 20.2%, and losses on bonds available for sale (bonds the bank can sell before maturity) read -105.6% of equity against a median of 19.9%, a figure that is hard to interpret when equity itself is negative. By contrast, the real-estate concentration check points the other way: commercial real estate loans were only 0.1% of loans against a median of 23.3%, and the bank did not cross either supervisory line, so its troubles lay elsewhere.

## Understanding the score

As of 2023-09-30, Citizens Bank ranked 1 out of 4,686 banks nationally, the 100.0th percentile on a 0 to 100 scale where higher means riskier. It was on the watchlist, one of 94 banks flagged that quarter, the riskiest 2% of the country.

Five features pushed the score up most. The strongest was the Tier 1 risk-based capital ratio at 0.0%, contributing +2.465, followed by return on equity (profit as a share of the owners' stake) at -596.8%, contributing +2.131. Next came the total risk-based capital ratio at 1.3%, contributing +0.728, the leverage ratio at 0.0%, contributing +0.618, and equity as a share of assets at -4.5%, contributing +0.390.

Five features pulled the score down. The largest was the Texas ratio at -261.2%, contributing -0.910, then securities as a share of assets at 38.2%, contributing -0.312, and losses on bonds available for sale at -105.6% of equity, contributing -0.293. Interest expense at 1.1% of assets contributed -0.236, and deposit growth of -9.2% contributed -0.132. Several of these downward pushes come from ratios that turn negative only because capital is below zero, so they say little about real strength, and the upward drivers far outweighed them.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2021-12-31 | 297 | 4,904 |  |
| 2022-03-31 | 20 | 4,861 | ▲ watchlist |
| 2022-06-30 | 586 | 4,838 |  |
| 2022-09-30 | 261 | 4,813 |  |
| 2022-12-31 | 515 | 4,773 |  |
| 2023-03-31 | 303 | 4,740 |  |
| 2023-06-30 | 33 | 4,714 | ▲ watchlist (first flag) |
| 2023-09-30 | 1 | 4,686 | ▲ watchlist |

## How its ratios moved

As of September 30, 2023, the model ranked Citizens Bank 1 out of 4,686 banks nationally, placing it in the 100.0th percentile, where higher means riskier. The model rated it riskier than a year earlier, when it sat in the 94.6th percentile. Of the 30 ratios compared with their own prior range, usually the prior 12 quarters, 17 were outside that range.

Return on equity (profit as a share of the owners' stake) was -596.8%, far below its prior range of 11.9% to 23.8%, and its contribution of +2.131 model log-odds units pushed the score up. The leverage ratio (core capital as a share of average assets, a cushion against losses) stood at 0.0%, below its prior range of 7.5% to 8.8%, and its contribution of +0.618 pushed the score up. That leverage ratio fell by -8.3 pp over one quarter. Provisions for loan losses (money set aside for expected bad loans) ran at an annualized 9.8% of assets, above the prior range of 0.0% to 0.5%, and their contribution of +0.200 pushed the score up. Return on assets (profit as a share of everything the bank holds) was -10.0%, below its prior range of 1.0% to 1.4%, and its contribution of +0.116 pushed the score up.

The efficiency ratio (operating costs as a share of revenue) was 88.3%, above its prior range of 61.9% to 62.6%, yet its contribution of -0.120 model log-odds units pushed the score down. Net loan write-offs (loans recorded as lost, minus recoveries) reached an annualized 15.1% of loans, well above the prior range of 0.3% to 2.2%, but with a contribution of -0.026 they had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -596.8% | 11.9% to 23.8% | same quarter, prior 3 years | n/a | -620.6 pp | +2.131 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 88.3% | 61.9% to 62.6% | same quarter, prior 3 years | n/a | +25.7 pp | -0.120 | pushed the score down |
| return on assets (profit as a share of assets) | -10.0% | 1.0% to 1.4% | same quarter, prior 3 years | n/a | -11.2 pp | +0.116 | pushed the score up |
| annualized provision for loan losses as a share of assets | 9.8% | 0.0% to 0.5% | same quarter, prior 3 years | n/a | +9.7 pp | +0.200 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 15.1% | 0.3% to 2.2% | same quarter, prior 3 years | n/a | +12.9 pp | -0.026 | little effect on the score |
| the leverage ratio (core capital as a share of average assets) | 0.0% | 7.5% to 8.8% | prior 12 quarters | -8.3 pp | -8.2 pp | +0.618 | pushed the score up |

17 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2023-09-30: Agricultural Specialization.

Peers: 309 banks in the same specialty group and size tier (under $100 million).

As of 2023-09-30, Citizens Bank ranked 1 out of 4,686 banks nationally, the 100.0th percentile, where a higher percentile means a higher model score. Its return on equity (profit as a share of the owners' stake) was -596.8%, at the 0.0th percentile nationally, which is unusually low, and at the 0.2nd percentile among its peers against a peer median of 10.6%, which is unusually low among its peers too. Its total risk-based capital ratio (the owners' cushion against losses, measured against risk-weighted assets) was 1.3%, at the 0.0th percentile nationally, which is unusually low, and at the 0.3rd percentile among its peers against a peer median of 18.9%, which is unusually low among its peers too. Its Tier 1 risk-based capital ratio (the same cushion counting only the highest-quality capital) was 0.0%, at the 0.0th percentile nationally, which is unusually low, and at the 0.3rd percentile among its peers against a peer median of 17.8%, which is unusually low among its peers too. Its equity as a share of assets was -4.5%, at the 0.2nd percentile nationally, which is unusually low, and at the 0.2nd percentile among its peers against a peer median of 9.9%, which is unusually low among its peers too.

Its annualized provision for loan losses (money set aside for expected bad loans) was 9.8% of assets, at the 100.0th percentile nationally, which is unusually high, and at the 99.8th percentile among its peers against a peer median of 0.0%, which is unusually high among its peers too. Its annualized loan write-offs, net of recoveries (loans given up as uncollectible), were 15.1% of loans, at the 99.9th percentile nationally, which is unusually high, and at the 99.8th percentile among its peers against a peer median of 0.0%, which is unusually high among its peers too. Its nonaccrual assets and foreclosed property (loans no longer paying interest plus repossessed property) were 5.9% of assets, at the 99.8th percentile nationally, which is unusually high, and at the 99.8th percentile among its peers against a peer median of 0.0%, which is unusually high among its peers too. Its Texas ratio (troubled assets against capital plus reserves) was -261.2%, at the 0.1st percentile nationally, which is unusually low, and at the 0.2nd percentile among its peers against a peer median of 0.9%, which is unusually low among its peers too.

Overall, 18 of the bank's ratios fell in the national top or bottom 10%, and 16 of those were also unusual among its 309 peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -596.8% | 0.0th (unusually low) | 10.6% | 0.2nd | unusually low among its peers too |
| the total risk-based capital ratio | 1.3% | 0.0th (unusually low) | 18.9% | 0.3rd | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 0.0% | 0.0th (unusually low) | 17.8% | 0.3rd | unusually low among its peers too |
| annualized provision for loan losses as a share of assets | 9.8% | 100.0th (unusually high) | 0.0% | 99.8th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | -261.2% | 0.1st (unusually low) | 0.9% | 0.2nd | unusually low among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | 15.1% | 99.9th (unusually high) | 0.0% | 99.8th | unusually high among its peers too |
| equity as a share of assets | -4.5% | 0.2nd (unusually low) | 9.9% | 0.2nd | unusually low among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 5.9% | 99.8th (unusually high) | 0.0% | 99.8th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 1.6% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -42.5% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, Citizens Bank failed on 2023-11-03, and Canary had first flagged it in the quarter ending 2023-06-30, a lead time of 2 quarters. At that first flag, the bank's capital still looked healthy on paper, with a Tier 1 risk-based capital ratio of 10.4% and return on equity of 16.9%, both of which actually pulled the score down.

What raised the alarm in Q2 2023 were other signals: losses on bonds available for sale at 119.8% of equity, contributing +1.104, and a Texas ratio of 143.5%, contributing +1.045. Loans 90+ days past due or not accruing interest were already 9.7% of loans, contributing +0.295. In other words, looking back, the model spotted the bond losses and bad loans before they showed up as a collapse in capital.

## What happened next

In hindsight, the bank failed on November 3, 2023. Its last reported quarter in our data is 2023-09-30, the same quarter this memo describes, so there are no later ranks or flags to show.

## Sources

- F1 · Bank name · n/a · Citizens Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2023-09-30 · 2023-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2023-09-30 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2023-09-30 · 4,686 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2023-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2023-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2023-09-30 · 94 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2023-09-30 · -4.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2023-09-30 · 9.1% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2023-09-30 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2023-09-30 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2023-09-30 · 1.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2023-09-30 · 15.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2023-09-30 · 9.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2023-09-30 · 0.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2023-09-30 · 5.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2023-09-30 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2023-09-30 · 1.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2023-09-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2023-09-30 · 15.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2023-09-30 · 9.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2023-09-30 · 0.1% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2023-09-30 · 23.3% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2023-09-30 · -261.2% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2023-09-30 · 2.0% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2023-09-30 · -10.0% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2023-09-30 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2023-09-30 · 34.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2023-09-30 · 23.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2023-09-30 · 83.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2023-09-30 · 77.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2023-09-30 · 20.9% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2023-09-30 · 8.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2023-09-30 · 2.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2023-09-30 · 5.4% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2023-09-30 · -105.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2023-09-30 · 19.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2023-09-30 · 38.2% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2023-09-30 · 20.2% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F69 · Bank: total assets · 2023-09-30 · $65.6 million · data/features/fct_bank_features.parquet: log_total_assets
- F73 · Bank: deposit growth over the past four quarters · 2023-09-30 · -9.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2023-09-30 · -0.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 0.0%; contribution to the score · 2023-09-30 · +2.465 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -596.8%; contribution to the score · 2023-09-30 · +2.131 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the total risk-based capital ratio, value 1.3%; contribution to the score · 2023-09-30 · +0.728 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value 0.0%; contribution to the score · 2023-09-30 · +0.618 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: equity as a share of assets, value -4.5%; contribution to the score · 2023-09-30 · +0.390 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value -261.2%; contribution to the score · 2023-09-30 · -0.910 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: securities as a share of assets, value 38.2%; contribution to the score · 2023-09-30 · -0.312 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F82 · Driver down #3: losses on bonds available for sale, as a share of equity, value -105.6%; contribution to the score · 2023-09-30 · -0.293 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F83 · Driver down #4: annualized interest expense as a share of assets, value 1.1%; contribution to the score · 2023-09-30 · -0.236 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F84 · Driver down #5: deposit growth over the past four quarters, value -9.2%; contribution to the score · 2023-09-30 · -0.132 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F85 · Failure date · 2023-11-03 · 2023-11-03 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2023-06-30 · 2023-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 2 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2023-06-30: losses on bonds available for sale, as a share of equity, value 119.8%; contribution to the score · 2023-06-30 · +1.104 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F89 · Driver up #2 at 2023-06-30: the Texas ratio (troubled assets against capital plus reserves), value 143.5%; contribution to the score · 2023-06-30 · +1.045 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2023-06-30: loans 90+ days past due or not accruing interest, as a share of loans, value 9.7%; contribution to the score · 2023-06-30 · +0.295 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F94 · Driver down #2 at 2023-06-30: the Tier 1 risk-based capital ratio, value 10.4%; contribution to the score · 2023-06-30 · -0.829 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F95 · Driver down #3 at 2023-06-30: return on equity (profit as a share of equity), value 16.9%; contribution to the score · 2023-06-30 · -0.685 · data/analyst/scores.parquet: feature return_on_equity contribution
- F98 · Last quarter the bank reported · 2023-09-30 · 2023-09-30 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2023-09-30 · -596.8% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 11.9% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 23.8% · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2023-09-30 · +2.131 · data/analyst/scores.parquet: feature return_on_equity contribution
- F104 · Trend: return on equity (profit as a share of equity), what the model did with it · 2023-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2023-09-30 · 88.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 61.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 62.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F109 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2023-09-30 · -0.120 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F110 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2023-09-30 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F111 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2023-09-30 · -10.0% · data/features/fct_bank_features.parquet: return_on_assets
- F112 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: return_on_assets
- F113 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: return_on_assets
- F115 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2023-09-30 · +0.116 · data/analyst/scores.parquet: feature return_on_assets contribution
- F116 · Trend: return on assets (profit as a share of assets), what the model did with it · 2023-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F117 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2023-09-30 · 9.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F118 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F119 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.5% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F121 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2023-09-30 · +0.200 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F122 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2023-09-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F123 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2023-09-30 · 15.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F124 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F125 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F127 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2023-09-30 · -0.026 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F128 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2023-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F129 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F130 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 7.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F131 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 8.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F132 · Trend: the leverage ratio (core capital as a share of average assets), change over one quarter, in percentage points · 2023-09-30 · -8.3 pp · data/features/fct_bank_features.parquet: leverage_ratio
- F134 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2023-09-30 · +0.618 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F135 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2023-09-30 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F136 · Trend: ratios outside their own prior range · 2023-09-30 · 17 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios compared with their own prior range · 2023-09-30 · 30 · data/features/fct_bank_features.parquet
- F139 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Percentile a year earlier (100 = highest risk) · 2022-09-30 · 94.6% · data/analyst/scores.parquet: percentile
- F142 · Trend: how the model's rating compares with a year earlier · 2023-09-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F146 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2023-09-30 · -596.8% · data/features/fct_bank_features.parquet: return_on_equity
- F147 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2023-09-30 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F148 · Peers: return on equity (profit as a share of equity), national reading · 2023-09-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F149 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2023-09-30 · 0.2nd · data/features/fct_bank_features.parquet: return_on_equity
- F150 · Peers: return on equity (profit as a share of equity), peer median · 2023-09-30 · 10.6% · data/features/fct_bank_features.parquet: return_on_equity
- F151 · Peers: return on equity (profit as a share of equity), reading against its peers · 2023-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F152 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2023-09-30 · 1.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F153 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2023-09-30 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F154 · Peers: the total risk-based capital ratio, national reading · 2023-09-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F155 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2023-09-30 · 0.3rd · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F156 · Peers: the total risk-based capital ratio, peer median · 2023-09-30 · 18.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F157 · Peers: the total risk-based capital ratio, reading against its peers · 2023-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F158 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F159 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2023-09-30 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F160 · Peers: the Tier 1 risk-based capital ratio, national reading · 2023-09-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F161 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2023-09-30 · 0.3rd · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F162 · Peers: the Tier 1 risk-based capital ratio, peer median · 2023-09-30 · 17.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F163 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2023-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F164 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2023-09-30 · 9.8% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F165 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2023-09-30 · 100.0th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F166 · Peers: annualized provision for loan losses as a share of assets, national reading · 2023-09-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F167 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2023-09-30 · 99.8th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F168 · Peers: annualized provision for loan losses as a share of assets, peer median · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F169 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2023-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F170 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2023-09-30 · -261.2% · data/features/fct_bank_features.parquet: texas_ratio
- F171 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2023-09-30 · 0.1st · data/features/fct_bank_features.parquet: texas_ratio
- F172 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2023-09-30 · unusually low · data/features/fct_bank_features.parquet: texas_ratio
- F173 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2023-09-30 · 0.2nd · data/features/fct_bank_features.parquet: texas_ratio
- F174 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2023-09-30 · 0.9% · data/features/fct_bank_features.parquet: texas_ratio
- F175 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2023-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F176 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2023-09-30 · 15.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F177 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2023-09-30 · 99.9th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F178 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2023-09-30 · unusually high · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F179 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2023-09-30 · 99.8th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F180 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F181 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2023-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F182 · Peers: equity as a share of assets, bank value at the as-of quarter · 2023-09-30 · -4.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F183 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2023-09-30 · 0.2nd · data/features/fct_bank_features.parquet: equity_to_assets
- F184 · Peers: equity as a share of assets, national reading · 2023-09-30 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F185 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2023-09-30 · 0.2nd · data/features/fct_bank_features.parquet: equity_to_assets
- F186 · Peers: equity as a share of assets, peer median · 2023-09-30 · 9.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F187 · Peers: equity as a share of assets, reading against its peers · 2023-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F188 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2023-09-30 · 5.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F189 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2023-09-30 · 99.8th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F190 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2023-09-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F191 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2023-09-30 · 99.8th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F192 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2023-09-30 · 0.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F193 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2023-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F194 · Peers: banks in the peer group (including this bank) · 2023-09-30 · 309 · data/raw/specialty/: SPECGRP
- F195 · Peers: ratios in the national top or bottom 10% · 2023-09-30 · 18 · data/features/fct_bank_features.parquet
- F196 · Peers: those ratios also unusual among peers · 2023-09-30 · 16 · data/features/fct_bank_features.parquet
- F198 · Peers: cut-off for unusual (top or bottom share of banks) · 2023-09-30 · 10% · data/features/fct_bank_features.parquet
