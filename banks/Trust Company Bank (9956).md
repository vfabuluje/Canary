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
written_at: "2026-11-19T14:05:14"
writer_model: "claude-opus-5-5"
checked: true
---

# Trust Company Bank (cert 9956)

*Hindsight: failed 2016-04-29. Canary flagged it 1 quarter ahead.*

## Summary

As of March 31, 2016, Trust Company Bank, based in TN, ranked 3 out of 6,193 banks nationally on Canary's risk score, which places it in the 100.0th percentile, where higher means riskier. It was flagged on the watchlist, which covers roughly the riskiest 2% of banks. Its capital, the cushion that absorbs losses, was below zero, with equity at -6.5% of assets against a national median of 10.9%, and its return on assets (profit as a share of assets) was -34.3%. Problem loans, meaning loans 90+ days past due or no longer paying interest, made up 13.4% of its loans, compared with a national median of 0.7%.

## Warning signs in the data

Capital was the most striking weakness: equity was -6.5% of assets versus a national median of 10.9%, and the leverage ratio (core capital as a share of average assets) was -6.2% versus 10.4%. The Tier 1 risk-based capital ratio, which compares core capital with assets weighted by their riskiness, was -12.5% against a median of 15.2%, and the broader total risk-based capital ratio was -11.1% against 16.4%. The bank was also losing money heavily, with return on assets of -34.3% against a median of 0.9%, and an efficiency ratio (operating costs as a share of revenue) of 393.0% against 70.4%.

Credit quality was far worse than typical: loans 90+ days past due or not accruing interest were 13.4% of loans versus a median of 0.7%, and nonaccrual assets plus foreclosed property were 14.3% of assets versus 0.6%. Loans 30-89 days past due, an early sign of trouble, were 3.7% of assets versus 0.3%. The bank had set aside loan-loss reserves of 5.7% of loans versus a median of 1.3%, and its annualized provision for loan losses (new money set aside for bad loans) was 5.6% of assets versus 0.0%. The Texas ratio, which weighs troubled assets against capital plus reserves, read an unusual negative -457.7%, against a median of 5.5%.

On funding, the bank relied on stable core deposits equal to 106.1% of assets versus a median of 78.9%, with uninsured deposits at 0.0% of deposits versus 16.6% and volatile funding at 0.0% of assets versus 4.9%. Cash was 14.1% of assets versus 7.0%, but the bank was shrinking, with assets down -30.5% and deposits down -16.9% over the past four quarters, against national medians of 3.0% and 2.6%. Unrealized losses on bonds held to maturity were 2.8% of equity versus a median of 0.0%, and on bonds available for sale 0.6% versus -0.9%, though securities were only 2.4% of assets versus 18.6%.

## Understanding the score

For the quarter ending March 31, 2016, the bank ranked 3 out of 6,193 banks, putting it in the 100.0th percentile on a scale from 0 to 100 where higher means riskier. It was flagged on the watchlist, one of 124 banks that quarter; the watchlist covers about 2% of banks.

The five factors that pushed the score up most were the Tier 1 risk-based capital ratio at -12.5% (+1.605), return on equity, meaning profit as a share of equity (+1.137), the total risk-based capital ratio at -11.1% (+0.686), loans 90+ days past due or not accruing interest at 13.4% of loans (+0.637), and equity as a share of assets at -6.5% (+0.473). The five factors that pulled the score down most were interest expense at 0.8% of assets (-0.992), the Texas ratio at -457.7% (-0.965), construction loans at 4.9% of loans (-0.209), deposit growth of -16.9% over four quarters (-0.114), and the efficiency ratio at 393.0% (-0.071). Positive contributions raise the score and negative ones lower it; the upward pushes were much larger overall.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 3 | 6,193 | ▲ watchlist (first flag) |

## How its ratios moved

Each ratio is compared with its own range over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 29 ratios checked this way, 17 sat outside their own prior range, and the table shows the 6 furthest outside.

The Tier 1 risk-based capital ratio was -12.5%, below its prior range of 0.1% to 6.0%, and contributed +1.605 model log-odds units, which pushed the score up. That ratio fell by -15.0 pp in a single quarter and by -16.3 pp over four quarters. The total risk-based capital ratio was -11.1%, below its prior range of 0.2% to 6.6%, and contributed +0.686, which pushed the score up. Annualized provision for loan losses was 5.6% of assets, above its prior range of 0.0% to 0.7%, and contributed +0.164, which pushed the score up. Return on assets was -34.3%, below its prior range of -6.6% to -4.5%, and contributed +0.118, which pushed the score up.

By contrast, the Texas ratio was -457.7%, far below its prior range of 45.3% to 296.1%, yet it contributed -0.965 and pushed the score down. Likewise, the efficiency ratio was 393.0%, well above its prior range of 133.6% to 156.0%, but it contributed -0.071 and pushed the score down.

There is no score from a year earlier to compare with (scores start 2016-03-31, or the bank did not report then).

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on assets (profit as a share of assets) | -34.3% | -6.6% to -4.5% | same quarter, prior 3 years | n/a | -27.6 pp | +0.118 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 393.0% | 133.6% to 156.0% | same quarter, prior 3 years | n/a | +237.0 pp | -0.071 | pushed the score down |
| annualized provision for loan losses as a share of assets | 5.6% | 0.0% to 0.7% | same quarter, prior 3 years | n/a | +5.6 pp | +0.164 | pushed the score up |
| the Tier 1 risk-based capital ratio | -12.5% | 0.1% to 6.0% | prior 12 quarters | -15.0 pp | -16.3 pp | +1.605 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | -457.7% | 45.3% to 296.1% | prior 12 quarters | -753.8 pp | -663.8 pp | -0.965 | pushed the score down |
| the total risk-based capital ratio | -11.1% | 0.2% to 6.6% | prior 12 quarters | -14.9 pp | -16.2 pp | +0.686 | pushed the score up |

17 of 29 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2016-03-31: Commercial Lending Specialization.

Peers: 373 banks in the same specialty group and size tier (under $100 million).

Equity as a share of assets was -6.5%, in the 0.0th percentile nationally (unusually low), and in the 0.1st percentile among peers against a peer median of 11.0%, which is unusually low among its peers too. The leverage ratio was -6.2%, in the 0.0th percentile nationally (unusually low), and in the 0.1st percentile among peers against a peer median of 10.7%, which is unusually low among its peers too. The Tier 1 risk-based capital ratio was -12.5%, in the 0.0th percentile nationally (unusually low), and in the 0.1st percentile among peers against a peer median of 15.4%, which is unusually low among its peers too. The total risk-based capital ratio was -11.1%, in the 0.0th percentile nationally (unusually low), and in the 0.1st percentile among peers against a peer median of 16.5%, which is unusually low among its peers too.

Return on assets was -34.3%, in the 0.0th percentile nationally (unusually low), and in the 0.1st percentile among peers against a peer median of 0.6%, which is unusually low among its peers too. The Texas ratio was -457.7%, in the 0.0th percentile nationally (unusually low), and in the 0.1st percentile among peers against a peer median of 8.2%, which is unusually low among its peers too. Core deposits were 106.1% of assets, in the 100.0th percentile nationally (unusually high), and in the 99.9th percentile among peers against a peer median of 81.6%, which is unusually high among its peers too. Uninsured deposits were 0.0% of deposits, in the 0.0th percentile nationally (unusually low), and in the 0.1st percentile among peers against a peer median of 11.7%, which is unusually low among its peers too.

Overall, 21 of the bank's ratios fell in the national top or bottom 10%, and 20 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| equity as a share of assets | -6.5% | 0.0th (unusually low) | 11.0% | 0.1st | unusually low among its peers too |
| return on assets (profit as a share of assets) | -34.3% | 0.0th (unusually low) | 0.6% | 0.1st | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | -6.2% | 0.0th (unusually low) | 10.7% | 0.1st | unusually low among its peers too |
| core deposits as a share of assets | 106.1% | 100.0th (unusually high) | 81.6% | 99.9th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | -457.7% | 0.0th (unusually low) | 8.2% | 0.1st | unusually low among its peers too |
| the total risk-based capital ratio | -11.1% | 0.0th (unusually low) | 16.5% | 0.1st | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | -12.5% | 0.0th (unusually low) | 15.4% | 0.1st | unusually low among its peers too |
| uninsured deposits as a share of deposits | 0.0% | 0.0th (unusually low) | 11.7% | 0.1st | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: total risk-based capital, as the 2006 guidance specifies.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | n/a | 100% or more | n/a |
| Total commercial real estate loans ÷ capital | n/a | 300% or more | n/a |
| Growth in commercial real estate loans over the prior 36 months | n/a | 50% or more | n/a |

The construction line can't be checked: the bank's capital was zero or negative this quarter.
The total commercial real estate line can't be checked: the bank's capital was zero or negative this quarter.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

With hindsight, this is a case Canary caught: the bank was first flagged in the quarter ending March 31, 2016. The bank failed on April 29, 2016, giving a lead time of 1 quarter between the first flag and the failure. At that first flag the bank ranked 3 out of 6,193 banks nationally.

## What happened next

In hindsight, the last quarter the bank reported was 2016-03-31, so there are no later ranks or watchlist flags to show. The fact sheet records a failure date of April 29, 2016, shortly after that final report. On its own, a bank that stops reporting may have merged or closed, and our reporting data does not distinguish the two; here the recorded failure date explains why the reports ended.

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
- F27 · Bank: loan-loss reserves as a share of loans · 2016-03-31 · 5.7% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2016-03-31 · 1.3% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2016-03-31 · 5.6% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2016-03-31 · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2016-03-31 · -457.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2016-03-31 · 5.5% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-03-31 · -34.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-03-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F43 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2016-03-31 · 393.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F44 · National median: the efficiency ratio (operating costs as a share of revenue) · 2016-03-31 · 70.4% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F49 · Bank: uninsured deposits as a share of deposits · 2016-03-31 · 0.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F50 · National median: uninsured deposits as a share of deposits · 2016-03-31 · 16.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: core deposits as a share of assets · 2016-03-31 · 106.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F54 · National median: core deposits as a share of assets · 2016-03-31 · 78.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: volatile funding as a share of assets · 2016-03-31 · 0.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F58 · National median: volatile funding as a share of assets · 2016-03-31 · 4.9% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F59 · Bank: cash as a share of assets · 2016-03-31 · 14.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F60 · National median: cash as a share of assets · 2016-03-31 · 7.0% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds held to maturity, as a share of equity · 2016-03-31 · 2.8% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F62 · National median: losses on bonds held to maturity, as a share of equity · 2016-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F63 · Bank: losses on bonds available for sale, as a share of equity · 2016-03-31 · 0.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F64 · National median: losses on bonds available for sale, as a share of equity · 2016-03-31 · -0.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: securities as a share of assets · 2016-03-31 · 2.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F66 · National median: securities as a share of assets · 2016-03-31 · 18.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
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
- F87 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2016-03-31 · -34.3% · data/features/fct_bank_features.parquet: return_on_assets
- F88 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -6.6% · data/features/fct_bank_features.parquet: return_on_assets
- F89 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -4.5% · data/features/fct_bank_features.parquet: return_on_assets
- F91 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2016-03-31 · +0.118 · data/analyst/scores.parquet: feature return_on_assets contribution
- F92 · Trend: return on assets (profit as a share of assets), what the model did with it · 2016-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2016-03-31 · 393.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F94 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 133.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 156.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2016-03-31 · -0.071 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2016-03-31 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F99 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2016-03-31 · 5.6% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F100 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F101 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F103 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2016-03-31 · +0.164 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F104 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2016-03-31 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F105 · Trend: the Tier 1 risk-based capital ratio, value at the as-of quarter · 2016-03-31 · -12.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F106 · Trend: the Tier 1 risk-based capital ratio, lowest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F107 · Trend: the Tier 1 risk-based capital ratio, highest value in the comparison window · n/a · 6.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F108 · Trend: the Tier 1 risk-based capital ratio, change over one quarter, in percentage points · 2016-03-31 · -15.0 pp · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F109 · Trend: the Tier 1 risk-based capital ratio, change over four quarters, in percentage points · 2016-03-31 · -16.3 pp · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F110 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2016-03-31 · +1.605 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F111 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2016-03-31 · pushed the score up · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F112 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2016-03-31 · -457.7% · data/features/fct_bank_features.parquet: texas_ratio
- F113 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 45.3% · data/features/fct_bank_features.parquet: texas_ratio
- F114 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 296.1% · data/features/fct_bank_features.parquet: texas_ratio
- F117 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2016-03-31 · -0.965 · data/analyst/scores.parquet: feature texas_ratio contribution
- F118 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2016-03-31 · pushed the score down · data/analyst/scores.parquet: feature texas_ratio contribution
- F119 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2016-03-31 · -11.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F120 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F121 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 6.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F124 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2016-03-31 · +0.686 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F125 · Trend: the total risk-based capital ratio, what the model did with it · 2016-03-31 · pushed the score up · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F126 · Trend: ratios outside their own prior range · 2016-03-31 · 17 · data/features/fct_bank_features.parquet
- F127 · Trend: ratios shown in the table (the furthest outside their prior range) · 2016-03-31 · 6 · data/features/fct_bank_features.parquet
- F128 · Trend: ratios compared with their own prior range · 2016-03-31 · 29 · data/features/fct_bank_features.parquet
- F129 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F130 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F134 · Peers: equity as a share of assets, bank value at the as-of quarter · 2016-03-31 · -6.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F135 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2016-03-31 · 0.0th · data/features/fct_bank_features.parquet: equity_to_assets
- F136 · Peers: equity as a share of assets, national reading · 2016-03-31 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F137 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2016-03-31 · 0.1st · data/features/fct_bank_features.parquet: equity_to_assets
- F138 · Peers: equity as a share of assets, peer median · 2016-03-31 · 11.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F139 · Peers: equity as a share of assets, reading against its peers · 2016-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F140 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2016-03-31 · -34.3% · data/features/fct_bank_features.parquet: return_on_assets
- F141 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2016-03-31 · 0.0th · data/features/fct_bank_features.parquet: return_on_assets
- F142 · Peers: return on assets (profit as a share of assets), national reading · 2016-03-31 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F143 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2016-03-31 · 0.1st · data/features/fct_bank_features.parquet: return_on_assets
- F144 · Peers: return on assets (profit as a share of assets), peer median · 2016-03-31 · 0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F145 · Peers: return on assets (profit as a share of assets), reading against its peers · 2016-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F146 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2016-03-31 · -6.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F147 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2016-03-31 · 0.0th · data/features/fct_bank_features.parquet: leverage_ratio
- F148 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2016-03-31 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F149 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2016-03-31 · 0.1st · data/features/fct_bank_features.parquet: leverage_ratio
- F150 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2016-03-31 · 10.7% · data/features/fct_bank_features.parquet: leverage_ratio
- F151 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2016-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F152 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2016-03-31 · 106.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F153 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2016-03-31 · 100.0th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F154 · Peers: core deposits as a share of assets, national reading · 2016-03-31 · unusually high · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F155 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2016-03-31 · 99.9th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F156 · Peers: core deposits as a share of assets, peer median · 2016-03-31 · 81.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F157 · Peers: core deposits as a share of assets, reading against its peers · 2016-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F158 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2016-03-31 · -457.7% · data/features/fct_bank_features.parquet: texas_ratio
- F159 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2016-03-31 · 0.0th · data/features/fct_bank_features.parquet: texas_ratio
- F160 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2016-03-31 · unusually low · data/features/fct_bank_features.parquet: texas_ratio
- F161 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2016-03-31 · 0.1st · data/features/fct_bank_features.parquet: texas_ratio
- F162 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2016-03-31 · 8.2% · data/features/fct_bank_features.parquet: texas_ratio
- F163 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2016-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F164 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2016-03-31 · -11.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F165 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2016-03-31 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F166 · Peers: the total risk-based capital ratio, national reading · 2016-03-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F167 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2016-03-31 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F168 · Peers: the total risk-based capital ratio, peer median · 2016-03-31 · 16.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F169 · Peers: the total risk-based capital ratio, reading against its peers · 2016-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F170 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2016-03-31 · -12.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F171 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2016-03-31 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F172 · Peers: the Tier 1 risk-based capital ratio, national reading · 2016-03-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F173 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2016-03-31 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F174 · Peers: the Tier 1 risk-based capital ratio, peer median · 2016-03-31 · 15.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F175 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2016-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F176 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2016-03-31 · 0.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F177 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2016-03-31 · 0.0th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F178 · Peers: uninsured deposits as a share of deposits, national reading · 2016-03-31 · unusually low · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F179 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2016-03-31 · 0.1st · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F180 · Peers: uninsured deposits as a share of deposits, peer median · 2016-03-31 · 11.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F181 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2016-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F183 · Peers: ratios in the national top or bottom 10% · 2016-03-31 · 21 · data/features/fct_bank_features.parquet
- F184 · Peers: those ratios also unusual among peers · 2016-03-31 · 20 · data/features/fct_bank_features.parquet
- F186 · Peers: cut-off for unusual (top or bottom share of banks) · 2016-03-31 · 10% · data/features/fct_bank_features.parquet
