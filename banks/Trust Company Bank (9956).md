---
cert: 9956
name: "Trust Company Bank"
as_of: 2016-03-31
rank: 3
n_banks: 6193
percentile: 99.96770547392218
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2016-04-29
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:11"
writer_model: "claude-opus-5-5"
checked: true
---

# Trust Company Bank (cert 9956)

*Hindsight: failed 2016-04-29. Canary flagged it 1 quarter ahead.*

## Summary

As of Q1 2016, Trust Company Bank, a small bank in TN, ranked 3 out of 6,193 banks nationally on Canary's risk score, placing it in the 100.0th percentile. It was flagged on Canary's watchlist, the top 2% of banks by score, which held 124 banks that quarter. The bank's capital, the owners' cushion that absorbs losses, was negative, with equity at -6.5% of assets against a national median of 10.9%. With total assets of $19.0 million, it was far smaller than the national median of $192.6 million.

## Warning signs in the data

Capital was the starkest problem: equity as a share of assets was -6.5% versus a national median of 10.9%, and the leverage ratio (core capital as a share of average assets) was -6.2% versus 10.4%. Risk-based capital ratios, which weigh capital against how risky the bank's assets are, were also negative: the Tier 1 ratio was -12.5% against a median of 15.2%, and the total ratio was -11.1% against 16.4%.

Credit quality was weak: loans 90+ days past due or not accruing interest were 13.4% of loans versus a median of 0.7%, and nonaccrual assets plus foreclosed property were 14.3% of assets versus 0.6%. Loans 30-89 days past due, an earlier sign of trouble, were 3.7% of assets against a median of 0.3%, and the annualized provision for loan losses, money set aside for expected bad loans, was 5.6% of assets versus 0.0%. Return on assets was -34.3% against a median of 0.9%, and the efficiency ratio, operating costs as a share of revenue, was 393.0% versus 70.4%.

Funding looked steadier: uninsured deposits were 0.0% of deposits versus a median of 16.6%, core deposits, the stable everyday kind, were 106.1% of assets versus 78.9%, and cash was 14.1% of assets versus 7.0%. Still, the bank was shrinking, with assets down -30.5% and deposits down -16.9% over the past four quarters, while the medians grew 3.0% and 2.6%. Unrealized losses on bonds held to maturity were 2.8% of equity versus a median of 0.0%, and on bonds available for sale 0.6% versus -0.9%, though securities made up only 2.4% of assets against a median of 18.6%.

## Understanding the score

In Q1 2016 Trust Company Bank ranked 3 of 6,193 banks, in the 100.0th percentile on a scale of 0 to 100 where higher means riskier. That put it on the watchlist, which covers the top 2% of banks and held 124 banks that quarter.

The five features that pushed the score up most were the Tier 1 risk-based capital ratio at -12.5% (contribution +1.605), return on equity, profit as a share of equity (+1.137), the total risk-based capital ratio at -11.1% (+0.686), loans 90+ days past due or not accruing at 13.4% (+0.637), and equity as a share of assets at -6.5% (+0.473).

The five features that pulled the score down most were interest expense as a share of assets at 0.8% (contribution -0.992), the Texas ratio, troubled assets against capital plus reserves, at -457.7% (-0.965), construction loans at 4.9% of loans (-0.209), deposit growth at -16.9% (-0.114), and the efficiency ratio at 393.0% (-0.071).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 3 | 6,193 | ▲ watchlist (first flag) |

## How early Canary caught it

In hindsight, Canary caught this bank: it was first flagged in the quarter ending 2016-03-31. The bank failed on 2016-04-29, giving a lead time of 1 quarter between the first flag and the failure. The warning came late in the bank's decline, but it did come before the failure.

## What happened next

Looking back with hindsight, Trust Company Bank failed on April 29, 2016. The last quarter it reported was 2016-03-31, so there are no later ranks or flags in our data.

## Sources

- F1 · Bank name · n/a · Trust Company Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2016-03-31 · 2016-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · TN · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-03-31 · 3 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-03-31 · 6,193 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-03-31 · 124 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-03-31 · -6.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-03-31 · 10.9% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-03-31 · -6.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-03-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-03-31 · -12.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-03-31 · 15.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-03-31 · -11.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-03-31 · 16.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-03-31 · 13.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-03-31 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-03-31 · 14.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-03-31 · 0.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2016-03-31 · 3.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2016-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2016-03-31 · 5.6% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2016-03-31 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-03-31 · -34.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-03-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F43 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2016-03-31 · 393.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F44 · National median: the efficiency ratio (operating costs as a share of revenue) · 2016-03-31 · 70.4% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F49 · Bank: uninsured deposits as a share of deposits · 2016-03-31 · 0.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F50 · National median: uninsured deposits as a share of deposits · 2016-03-31 · 16.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: core deposits as a share of assets · 2016-03-31 · 106.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F54 · National median: core deposits as a share of assets · 2016-03-31 · 78.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: cash as a share of assets · 2016-03-31 · 14.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F60 · National median: cash as a share of assets · 2016-03-31 · 7.0% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds held to maturity, as a share of equity · 2016-03-31 · 2.8% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F62 · National median: losses on bonds held to maturity, as a share of equity · 2016-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F63 · Bank: losses on bonds available for sale, as a share of equity · 2016-03-31 · 0.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F64 · National median: losses on bonds available for sale, as a share of equity · 2016-03-31 · -0.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: securities as a share of assets · 2016-03-31 · 2.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F66 · National median: securities as a share of assets · 2016-03-31 · 18.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F67 · Bank: total assets · 2016-03-31 · $19.0 million · data/features/fct_bank_features.parquet: log_total_assets
- F68 · National median: total assets · 2016-03-31 · $192.6 million · data/features/fct_bank_features.parquet: log_total_assets (median of all banks)
- F69 · Bank: asset growth over the past four quarters · 2016-03-31 · -30.5% · data/features/fct_bank_features.parquet: asset_growth_4q
- F70 · National median: asset growth over the past four quarters · 2016-03-31 · 3.0% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F71 · Bank: deposit growth over the past four quarters · 2016-03-31 · -16.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F72 · National median: deposit growth over the past four quarters · 2016-03-31 · 2.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F73 · Driver up #1: the Tier 1 risk-based capital ratio, value -12.5%; contribution to the score · 2016-03-31 · +1.605 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F74 · Driver up #2: return on equity (profit as a share of equity); contribution to the score · 2016-03-31 · +1.137 · data/analyst/scores.parquet: feature return_on_equity contribution
- F75 · Driver up #3: the total risk-based capital ratio, value -11.1%; contribution to the score · 2016-03-31 · +0.686 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F76 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 13.4%; contribution to the score · 2016-03-31 · +0.637 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F77 · Driver up #5: equity as a share of assets, value -6.5%; contribution to the score · 2016-03-31 · +0.473 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F78 · Driver down #1: annualized interest expense as a share of assets, value 0.8%; contribution to the score · 2016-03-31 · -0.992 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F79 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value -457.7%; contribution to the score · 2016-03-31 · -0.965 · data/analyst/scores.parquet: feature texas_ratio contribution
- F80 · Driver down #3: construction loans as a share of loans, value 4.9%; contribution to the score · 2016-03-31 · -0.209 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F81 · Driver down #4: deposit growth over the past four quarters, value -16.9%; contribution to the score · 2016-03-31 · -0.114 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F82 · Driver down #5: the efficiency ratio (operating costs as a share of revenue), value 393.0%; contribution to the score · 2016-03-31 · -0.071 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F83 · Failure date · 2016-04-29 · 2016-04-29 · data/raw/failures: FAILDATE
- F84 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F85 · Lead time in quarters before failure · n/a · 1 · data/analyst/scores.parquet: quarters_until_failure
- F86 · Last quarter the bank reported · 2016-03-31 · 2016-03-31 · data/features/fct_bank_features.parquet: report_date
