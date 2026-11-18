---
cert: 58302
name: "First Nbc Bank"
as_of: 2017-03-31
rank: 2
n_banks: 5925
percentile: 99.98312236286921
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-04-28
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:06:48"
writer_model: "claude-opus-5-5"
checked: true
---

# First Nbc Bank (cert 58302)

*Hindsight: failed 2017-04-28. Canary flagged it 2 quarters ahead.*

## Summary

As of 2017-03-31, First Nbc Bank ranked 2 out of 5,925 FDIC-insured banks on Canary's risk score, which places it in the 100.0th percentile, the riskiest end of the scale. Its equity, the owners' cushion against losses, stood at -3.4% of assets, against a national median of 10.7%, so the cushion had been wiped out. Bad loans were also far above normal: 22.0% of loans were 90 or more days late or no longer paying interest, against a national median of 0.6%.

## Warning signs in the data

Capital, the money a bank can lose before depositors are at risk, was negative on every measure. Equity was -3.4% of assets versus a national median of 10.7%, and the leverage ratio (core capital as a share of average assets) was -2.0% versus 10.5%. The Tier 1 risk-based capital ratio, which weighs assets by riskiness, was -3.1% versus 15.1%, and the total risk-based capital ratio was -1.7% versus 16.2%.

Credit quality was very weak: 22.0% of loans were seriously late or not paying interest, against a median of 0.6%, and nonaccrual assets plus foreclosed property made up 17.3% of assets, against 0.5%. The Texas ratio, which compares troubled assets with capital plus reserves, was 225.4% versus a median of 4.8%, and loan-loss reserves, money set aside for expected losses, were 14.3% of loans versus 1.2%.

On funding, uninsured deposits (balances above the FDIC insurance limit) were 45.5% of deposits versus a median of 17.3%, and volatile funding was 19.3% of assets versus 5.1%. Over the past four quarters assets shrank by -31.5% and deposits by -23.4%, while the national medians grew by 3.9% and 4.3%. Losses on bonds were not a concern: losses on bonds available for sale were -1.6% of equity versus a median of 0.3%, and losses on bonds held to maturity were 0.0%, the same as the median.

## Understanding the score

On 2017-03-31 the bank ranked 2 of 5,925 banks, in the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on Canary's watchlist, which covers the top 2% of banks and held 119 banks that quarter.

The five features pushing the score up most were the Tier 1 risk-based capital ratio at -3.1%, the Texas ratio at 225.4%, return on equity (profit as a share of equity), loans 90+ days late or not accruing interest at 22.0%, and the total risk-based capital ratio at -1.7%.

The five features pulling the score down most were return on assets at 3.1%, losses on bonds available for sale at -1.6% of equity, loans 30-89 days past due at 1.2% of assets, construction loans at 13.5% of loans, and brokered deposits (deposits placed through middlemen) at 3.8% of deposits.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 191 | 6,193 |  |
| 2016-06-30 | 138 | 6,129 |  |
| 2016-09-30 | 135 | 6,051 |  |
| 2016-12-31 | 2 | 5,983 | ▲ watchlist (first flag) |
| 2017-03-31 | 2 | 5,925 | ▲ watchlist |

## How early Canary caught it

In hindsight, Canary first flagged First Nbc Bank in the quarter ending 2016-12-31, and the bank failed on 2017-04-28, a lead time of 2 quarters. At that first flag, the main drivers were a Tier 1 risk-based capital ratio of -2.8%, a return on equity of -169.3%, and a Texas ratio of 259.1%. Seriously late or non-paying loans were already 14.6% of loans and the total risk-based capital ratio was -1.5%.

## What happened next

In hindsight, the bank's last quarterly report was for 2017-03-31, the same quarter as this memo. The bank failed on 2017-04-28 and stopped reporting after that, so there are no later ranks or flags.

## Sources

- F1 · Bank name · n/a · First Nbc Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
- F6 · National rank (1 = highest score) · 2017-03-31 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2017-03-31 · 5,925 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2017-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2017-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2017-03-31 · 119 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2017-03-31 · -3.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2017-03-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · -2.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2017-03-31 · -3.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2017-03-31 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2017-03-31 · -1.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2017-03-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 22.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 17.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2017-03-31 · 14.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2017-03-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 225.4% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 4.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F49 · Bank: uninsured deposits as a share of deposits · 2017-03-31 · 45.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F50 · National median: uninsured deposits as a share of deposits · 2017-03-31 · 17.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: volatile funding as a share of assets · 2017-03-31 · 19.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F58 · National median: volatile funding as a share of assets · 2017-03-31 · 5.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: losses on bonds held to maturity, as a share of equity · 2017-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F62 · National median: losses on bonds held to maturity, as a share of equity · 2017-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F63 · Bank: losses on bonds available for sale, as a share of equity · 2017-03-31 · -1.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F64 · National median: losses on bonds available for sale, as a share of equity · 2017-03-31 · 0.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: asset growth over the past four quarters · 2017-03-31 · -31.5% · data/features/fct_bank_features.parquet: asset_growth_4q
- F70 · National median: asset growth over the past four quarters · 2017-03-31 · 3.9% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F71 · Bank: deposit growth over the past four quarters · 2017-03-31 · -23.4% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F72 · National median: deposit growth over the past four quarters · 2017-03-31 · 4.3% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F73 · Driver up #1: the Tier 1 risk-based capital ratio, value -3.1%; contribution to the score · 2017-03-31 · +2.032 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F74 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 225.4%; contribution to the score · 2017-03-31 · +1.227 · data/analyst/scores.parquet: feature texas_ratio contribution
- F75 · Driver up #3: return on equity (profit as a share of equity); contribution to the score · 2017-03-31 · +1.175 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 22.0%; contribution to the score · 2017-03-31 · +0.792 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F77 · Driver up #5: the total risk-based capital ratio, value -1.7%; contribution to the score · 2017-03-31 · +0.683 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F78 · Driver down #1: return on assets (profit as a share of assets), value 3.1%; contribution to the score · 2017-03-31 · -0.596 · data/analyst/scores.parquet: feature return_on_assets contribution
- F79 · Driver down #2: losses on bonds available for sale, as a share of equity, value -1.6%; contribution to the score · 2017-03-31 · -0.198 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F80 · Driver down #3: loans 30-89 days past due, as a share of assets, value 1.2%; contribution to the score · 2017-03-31 · -0.135 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F81 · Driver down #4: construction loans as a share of loans, value 13.5%; contribution to the score · 2017-03-31 · -0.127 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #5: brokered deposits as a share of deposits, value 3.8%; contribution to the score · 2017-03-31 · -0.091 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F83 · Failure date · 2017-04-28 · 2017-04-28 · data/raw/failures: FAILDATE
- F84 · First flag quarter (Phase 3 lead-time rule) · 2016-12-31 · 2016-12-31 · data/analyst/scores.parquet: flagged
- F85 · Lead time in quarters before failure · n/a · 2 · data/analyst/scores.parquet: quarters_until_failure
- F86 · Driver up #1 at 2016-12-31: the Tier 1 risk-based capital ratio, value -2.8%; contribution to the score · 2016-12-31 · +2.123 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F87 · Driver up #2 at 2016-12-31: return on equity (profit as a share of equity), value -169.3%; contribution to the score · 2016-12-31 · +1.396 · data/analyst/scores.parquet: feature return_on_equity contribution
- F88 · Driver up #3 at 2016-12-31: the Texas ratio (troubled assets against capital plus reserves), value 259.1%; contribution to the score · 2016-12-31 · +1.242 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Driver up #4 at 2016-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 14.6%; contribution to the score · 2016-12-31 · +0.844 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F90 · Driver up #5 at 2016-12-31: the total risk-based capital ratio, value -1.5%; contribution to the score · 2016-12-31 · +0.646 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F96 · Last quarter the bank reported · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
