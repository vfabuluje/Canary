---
cert: 58317
name: "Resolute Bank"
as_of: 2019-09-30
rank: 3
n_banks: 5325
percentile: 99.962441314554
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2019-10-25
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:48"
writer_model: "claude-opus-5-5"
checked: true
---

# Resolute Bank (cert 58317)

*Hindsight: failed 2019-10-25. Canary flagged it 4 quarters ahead.*

## Summary

Resolute Bank, based in OH, ranked 3 out of 5,325 FDIC-insured banks on Canary's risk score as of 2019-09-30, which places it in the 100.0th percentile, the riskiest end of the scale. Its capital cushion was extremely thin, with equity (the owners' stake) at 0.7% of assets against a national median of 11.6%. The bank was also losing money, with a return on assets of -7.0% compared with a national median of 1.1%.

## Warning signs in the data

Capital, the money a bank can lose before depositors are at risk, was far below normal levels. The leverage ratio (core capital as a share of average assets) was 0.6%, against a national median of 11.0%. The Tier 1 risk-based capital ratio was 1.3% and the total risk-based capital ratio was 2.6%, compared with national medians of 15.6% and 16.7%.

Credit quality, meaning how well borrowers were repaying, was weak. Loans 90+ days past due or not accruing interest made up 3.5% of loans, well above the national median of 0.6%. Annualized loan write-offs (loans given up as lost, net of recoveries) were 6.2% of loans, while the national median was 0.0%. The Texas ratio, which weighs troubled assets against capital plus reserves, stood at 115.1% versus a national median of 3.7%. Profitability was deeply negative, with return on equity at -274.3% against a median of 9.6%, and operating costs at 145.5% of revenue against a median of 66.8%.

On funding and liquidity, the bank held cash equal to 44.8% of assets, far above the national median of 6.9%, and core deposits (stable, everyday deposits) were 91.2% of assets against a median of 77.3%. Uninsured deposits were only 3.0% of deposits versus a median of 19.0%, but deposits shrank by -15.6% over the past four quarters while the median bank grew 4.4%. Bond losses were not a concern: the bank held securities equal to 0.0% of assets against a median of 15.4%, and its losses on bonds available for sale were 0.0% of equity versus a median of -0.8%.

## Understanding the score

As of 2019-09-30, Resolute Bank ranked 3 of 5,325 banks, in the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on Canary's watchlist, which covers the riskiest 2% of banks and held 107 banks that quarter.

The five features that pushed the score up most were the Tier 1 risk-based capital ratio at 1.3% (contribution +1.951), return on equity at -274.3% (+1.347), the leverage ratio at 0.6% (+0.620), the total risk-based capital ratio at 2.6% (+0.614), and the Texas ratio at 115.1% (+0.413).

The five features that pulled the score down most were interest expense at 1.0% of assets (contribution -0.287), deposit growth over the past four quarters at -15.6% (-0.115), the efficiency ratio at 145.5% (-0.101), construction loans at 0.6% of loans (-0.083), and net interest margin, the spread earned on lending and investing, at 3.7% (-0.078).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2017-12-31 | 547 | 5,738 |  |
| 2018-03-31 | 27 | 5,674 | ▲ watchlist |
| 2018-06-30 | 18 | 5,610 | ▲ watchlist |
| 2018-09-30 | 16 | 5,544 | ▲ watchlist |
| 2018-12-31 | 10 | 5,473 | ▲ watchlist (first flag) |
| 2019-03-31 | 5 | 5,428 | ▲ watchlist |
| 2019-06-30 | 6 | 5,369 | ▲ watchlist |
| 2019-09-30 | 3 | 5,325 | ▲ watchlist |

## How early Canary caught it

In hindsight, Canary first flagged Resolute Bank in the quarter ending 2018-12-31, and the bank failed on 2019-10-25, a lead time of 4 quarters. At that first flag, the main drivers pushing the score up were return on equity at -133.7% (+1.036), asset growth at -36.0% (+0.441), the Texas ratio at 83.4% (+0.403), seriously late or nonaccruing loans at 9.5% of loans (+0.328), and return on assets at -7.9% (+0.272). The largest offsetting driver then was interest expense at 0.7% of assets, which pulled the score down by -1.622.

## What happened next

In hindsight, the bank failed on 2019-10-25, less than a month after the as-of quarter. Its last reported quarter was 2019-09-30, so there are no later ranks or flags in our data. Our data shows only that the bank stopped reporting, which can mean a merger or a closure; the failure record above explains this case.

## Sources

- F1 · Bank name · n/a · Resolute Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · OH · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2019-09-30 · 3 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2019-09-30 · 5,325 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2019-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2019-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2019-09-30 · 107 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2019-09-30 · 0.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2019-09-30 · 11.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 0.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2019-09-30 · 1.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2019-09-30 · 15.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2019-09-30 · 2.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2019-09-30 · 16.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 3.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2019-09-30 · 6.2% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 115.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 3.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2019-09-30 · -7.0% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2019-09-30 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2019-09-30 · -274.3% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2019-09-30 · 9.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 145.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 66.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2019-09-30 · 3.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2019-09-30 · 19.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2019-09-30 · 91.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2019-09-30 · 77.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2019-09-30 · 44.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2019-09-30 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2019-09-30 · -0.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2019-09-30 · 15.4% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2019-09-30 · -15.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2019-09-30 · 4.4% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 1.3%; contribution to the score · 2019-09-30 · +1.951 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -274.3%; contribution to the score · 2019-09-30 · +1.347 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the leverage ratio (core capital as a share of average assets), value 0.6%; contribution to the score · 2019-09-30 · +0.620 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 2.6%; contribution to the score · 2019-09-30 · +0.614 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: the Texas ratio (troubled assets against capital plus reserves), value 115.1%; contribution to the score · 2019-09-30 · +0.413 · data/analyst/scores.parquet: feature texas_ratio contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 1.0%; contribution to the score · 2019-09-30 · -0.287 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: deposit growth over the past four quarters, value -15.6%; contribution to the score · 2019-09-30 · -0.115 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F82 · Driver down #3: the efficiency ratio (operating costs as a share of revenue), value 145.5%; contribution to the score · 2019-09-30 · -0.101 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F83 · Driver down #4: construction loans as a share of loans, value 0.6%; contribution to the score · 2019-09-30 · -0.083 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F84 · Driver down #5: net interest margin (the spread earned on lending and investing), value 3.7%; contribution to the score · 2019-09-30 · -0.078 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F85 · Failure date · 2019-10-25 · 2019-10-25 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2018-12-31 · 2018-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2018-12-31: return on equity (profit as a share of equity), value -133.7%; contribution to the score · 2018-12-31 · +1.036 · data/analyst/scores.parquet: feature return_on_equity contribution
- F89 · Driver up #2 at 2018-12-31: asset growth over the past four quarters, value -36.0%; contribution to the score · 2018-12-31 · +0.441 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F90 · Driver up #3 at 2018-12-31: the Texas ratio (troubled assets against capital plus reserves), value 83.4%; contribution to the score · 2018-12-31 · +0.403 · data/analyst/scores.parquet: feature texas_ratio contribution
- F91 · Driver up #4 at 2018-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 9.5%; contribution to the score · 2018-12-31 · +0.328 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2018-12-31: return on assets (profit as a share of assets), value -7.9%; contribution to the score · 2018-12-31 · +0.272 · data/analyst/scores.parquet: feature return_on_assets contribution
- F93 · Driver down #1 at 2018-12-31: annualized interest expense as a share of assets, value 0.7%; contribution to the score · 2018-12-31 · -1.622 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F98 · Last quarter the bank reported · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
