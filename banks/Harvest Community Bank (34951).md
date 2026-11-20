---
cert: 34951
name: "Harvest Community Bank"
as_of: 2016-12-31
rank: 3
n_banks: 5983
percentile: 99.9665719538693
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-01-13
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:14:22"
writer_model: "claude-opus-5-5"
checked: true
---

# Harvest Community Bank (cert 34951)

*Hindsight: failed 2017-01-13. Canary flagged it 4 quarters ahead.*

## Summary

As of 2016-12-31, Harvest Community Bank, based in NJ, ranked 3 out of 5,983 FDIC-insured banks on Canary's risk score, placing it in the 100.0th percentile and on Canary's watchlist. Its capital cushion (the owners' money that absorbs losses) was very thin, with equity at 1.4% of assets against a national median of 10.7%. Problem loans were heavy: loans 90+ days past due or not accruing interest were 18.2% of loans against a national median of 0.6%, and the bank was losing money, with a return on equity of -64.3%. One measure pointed the other way: the bank funded itself almost entirely with stable core deposits, at 96.6% of assets, well above the national median of 78.8%.

## Warning signs in the data

Capital, the owners' stake that absorbs losses before depositors are affected, was far below typical levels. The leverage ratio (core capital as a share of average assets) was 1.4%, against a national median of 10.4%. The Tier 1 risk-based capital ratio, which weighs core capital against assets adjusted for riskiness, was 1.9% against a median of 15.0%, and the total risk-based capital ratio was 3.2% against 16.2%.

Credit quality was poor: nonaccrual assets and foreclosed property (assets no longer earning interest plus property taken back from borrowers) were 16.3% of assets, against a national median of 0.5%, and loans 30-89 days past due were 1.9% of assets against 0.3%. The Texas ratio, which weighs troubled assets against capital plus reserves, stood at 382.7%, far above the national median of 4.9%. The bank was unprofitable, with a return on assets of -1.3% against a median of 0.9%, and its efficiency ratio (operating costs as a share of revenue) was 143.4% against 69.7%. Losses on bonds available for sale (bonds the bank could sell, valued at market prices) equaled 6.7% of equity, well above the national median of 0.7%.

Funding looked steadier than the rest of the picture: core deposits were 96.6% of assets against a national median of 78.8%, and uninsured deposits (balances above the insurance limit) were only 2.3% of deposits against 17.3%. The bank was shrinking, though, with assets down -12.4% over the past four quarters against a median growth of 3.5%, and deposits down -9.5% against 3.6%. The real-estate concentration section found the bank crossed the construction-lending screen but not the second commercial real estate line.

## Understanding the score

As of 2016-12-31, Harvest Community Bank ranked 3 out of 5,983 banks nationally, the 100.0th percentile on a scale of 0 to 100 where higher means riskier. That placed it on Canary's watchlist, which covers the top 2% of banks, or 120 banks that quarter.

The five factors that pushed the score up most were a Tier 1 risk-based capital ratio of 1.9%, a Texas ratio of 382.7%, a return on equity of -64.3%, loans 90+ days past due or not accruing interest at 18.2% of loans, and a leverage ratio of 1.4%. Their contributions to the score were +2.139, +1.450, +1.282, +0.755 and +0.636 respectively.

The five factors that pulled the score down most were annualized interest expense at 0.7% of assets, construction loans at 9.7% of loans, volatile funding at 1.8% of assets, cash at 5.6% of assets, and an efficiency ratio of 143.4%. Their contributions were -0.720, -0.124, -0.112, -0.098 and -0.078 respectively, small next to the factors pushing up.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 4 | 6,193 | ▲ watchlist (first flag) |
| 2016-06-30 | 3 | 6,129 | ▲ watchlist |
| 2016-09-30 | 1 | 6,051 | ▲ watchlist |
| 2016-12-31 | 3 | 5,983 | ▲ watchlist |

## How its ratios moved

Canary compared 30 of this bank's ratios with the bank's own history, and 12 of them sat outside their prior range in the latest quarter; the 6 furthest outside are discussed here. For most ratios the prior range covers the previous 12 quarters, and for year-to-date ratios it covers the same quarter in the prior 3 years. In that quarter the model ranked Harvest Community Bank 3 out of 5,983 banks nationally.

The Texas ratio, which weighs troubled assets against capital plus reserves, reached 382.7%, above its prior range of 81.9% to 362.8%, and its contribution of +1.450 model log-odds units pushed the score up. That ratio rose +19.9 pp over one quarter and +75.7 pp over four quarters. Core deposits, the stable everyday deposits a bank funds itself with, equaled 96.6% of assets, above their prior range of 87.0% to 95.9%, and their contribution of +0.195 model log-odds units pushed the score up. Losses on bonds available for sale (bonds the bank could sell, valued at market prices) came to 6.7% of equity, above a prior range of -7.9% to 4.7%, and their contribution of +0.164 model log-odds units pushed the score up.

The efficiency ratio, operating costs as a share of revenue, was 143.4%, above its prior range of 82.3% to 139.7%, yet its contribution of -0.078 model log-odds units pushed the score down. Securities made up 11.6% of assets, below their prior range of 12.3% to 21.1%, but despite being outside that range their contribution of -0.061 model log-odds units pushed the score down. Uninsured deposits, balances above the deposit insurance limit, were 2.3% of deposits, below their prior range of 2.6% to 5.8%, yet their contribution of +0.043 model log-odds units had little effect on the score.

There is no score from a year earlier to compare with (scores start 2016-03-31, or the bank did not report then).

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| losses on bonds available for sale, as a share of equity | 6.7% | -7.9% to 4.7% | prior 12 quarters | +11.7 pp | +2.0 pp | +0.164 | pushed the score up |
| uninsured deposits as a share of deposits | 2.3% | 2.6% to 5.8% | prior 12 quarters | -0.3 pp | -1.2 pp | +0.043 | little effect on the score |
| securities as a share of assets | 11.6% | 12.3% to 21.1% | prior 12 quarters | -0.7 pp | -2.2 pp | -0.061 | pushed the score down |
| core deposits as a share of assets | 96.6% | 87.0% to 95.9% | prior 12 quarters | +0.7 pp | +3.3 pp | +0.195 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 382.7% | 81.9% to 362.8% | prior 12 quarters | +19.9 pp | +75.7 pp | +1.450 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 143.4% | 82.3% to 139.7% | same quarter, prior 3 years | n/a | +3.7 pp | -0.078 | pushed the score down |

12 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2016-12-31: Commercial Lending Specialization.

Peers: 2106 banks in the same specialty group and size tier ($100 million to $1 billion).

Core deposits (steady, everyday customer deposits) made up 96.6% of the bank's assets, at the 100.0th percentile nationally, which is unusually high; among its peers it sat at the 100.0th percentile against a peer median of 78.5%, unusually high among its peers too. The Texas ratio (troubled assets against capital plus reserves) stood at 382.7%, at the 99.9th percentile nationally, which is unusually high; among its peers it was at the 99.9th percentile against a peer median of 6.1%, unusually high among its peers too.

The total risk-based capital ratio (capital measured against assets weighted by their riskiness) was 3.2%, at the 0.1st percentile nationally, which is unusually low; among its peers it was at the 0.1st percentile against a peer median of 14.7%, unusually low among its peers too. The Tier 1 risk-based capital ratio (the same measure using only the strongest, core capital) was 1.9%, at the 0.1st percentile nationally, which is unusually low; among its peers it was at the 0.1st percentile against a peer median of 13.6%, unusually low among its peers too. Equity (the owners' stake) was 1.4% of assets, at the 0.4th percentile nationally, which is unusually low; among its peers it was at the 0.3rd percentile against a peer median of 10.3%, unusually low among its peers too.

Loans 90+ days past due or not accruing interest (loans where payments have stopped) were 18.2% of loans, at the 99.9th percentile nationally, which is unusually high; among its peers they were at the 99.9th percentile against a peer median of 0.6%, unusually high among its peers too. Nonaccrual assets and foreclosed property (assets no longer earning interest plus property taken back from borrowers) were 16.3% of assets, at the 99.9th percentile nationally, which is unusually high; among its peers they were at the 99.7th percentile against a peer median of 0.7%, unusually high among its peers too. Return on equity (profit as a share of equity) was -64.3%, at the 0.1st percentile nationally, which is unusually low; among its peers it was at the 0.2nd percentile against a peer median of 8.4%, unusually low among its peers too. Overall, 18 of the bank's ratios fell in the national top or bottom 10%, and 18 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| core deposits as a share of assets | 96.6% | 100.0th (unusually high) | 78.5% | 100.0th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 382.7% | 99.9th (unusually high) | 6.1% | 99.9th | unusually high among its peers too |
| the total risk-based capital ratio | 3.2% | 0.1st (unusually low) | 14.7% | 0.1st | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 1.9% | 0.1st (unusually low) | 13.6% | 0.1st | unusually low among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 18.2% | 99.9th (unusually high) | 0.6% | 99.9th | unusually high among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 16.3% | 99.9th (unusually high) | 0.7% | 99.7th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -64.3% | 0.1st (unusually low) | 8.4% | 0.2nd | unusually low among its peers too |
| equity as a share of assets | 1.4% | 0.4th (unusually low) | 10.3% | 0.3rd | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: total risk-based capital, as the 2006 guidance specifies.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 318.8% | 100% or more | yes |
| Total commercial real estate loans ÷ capital | 652.6% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | -18.3% | 50% or more | no |

It crossed the construction line (100% or more of capital).
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

With hindsight, Canary caught this bank early: it was first flagged in the quarter ending 2016-03-31, ahead of its failure on 2017-01-13. Under Canary's lead-time rule, that is a lead time of 4 quarters before failure.

At that first flag, the main factors pushing the score up were already visible: a Tier 1 risk-based capital ratio of 2.9%, a Texas ratio of 322.2%, and a return on equity of -51.7%. Loans 90+ days past due or not accruing interest were 17.9% of loans, and the total risk-based capital ratio was 4.2%.

## What happened next

In hindsight, the bank failed on 2017-01-13, shortly after the as-of quarter. Its last reported quarter was 2016-12-31, so there are no later ranks or flags for it in Canary's data.

## Sources

- F1 · Bank name · n/a · Harvest Community Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · NJ · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-12-31 · 3 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-12-31 · 5,983 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-12-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-12-31 · 120 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-12-31 · 1.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-12-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · 1.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-12-31 · 1.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-12-31 · 15.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-12-31 · 3.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-12-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 18.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 16.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2016-12-31 · 1.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2016-12-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2016-12-31 · 382.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2016-12-31 · 4.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-12-31 · -1.3% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-12-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2016-12-31 · -64.3% · data/features/fct_bank_features.parquet: return_on_equity
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2016-12-31 · 143.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2016-12-31 · 69.7% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2016-12-31 · 2.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2016-12-31 · 17.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2016-12-31 · 96.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2016-12-31 · 78.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2016-12-31 · 6.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2016-12-31 · 0.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2016-12-31 · -12.4% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2016-12-31 · 3.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2016-12-31 · -9.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2016-12-31 · 3.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 1.9%; contribution to the score · 2016-12-31 · +2.139 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 382.7%; contribution to the score · 2016-12-31 · +1.450 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: return on equity (profit as a share of equity), value -64.3%; contribution to the score · 2016-12-31 · +1.282 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 18.2%; contribution to the score · 2016-12-31 · +0.755 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the leverage ratio (core capital as a share of average assets), value 1.4%; contribution to the score · 2016-12-31 · +0.636 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.7%; contribution to the score · 2016-12-31 · -0.720 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: construction loans as a share of loans, value 9.7%; contribution to the score · 2016-12-31 · -0.124 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: volatile funding as a share of assets, value 1.8%; contribution to the score · 2016-12-31 · -0.112 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F83 · Driver down #4: cash as a share of assets, value 5.6%; contribution to the score · 2016-12-31 · -0.098 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F84 · Driver down #5: the efficiency ratio (operating costs as a share of revenue), value 143.4%; contribution to the score · 2016-12-31 · -0.078 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F85 · Failure date · 2017-01-13 · 2017-01-13 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-03-31: the Tier 1 risk-based capital ratio, value 2.9%; contribution to the score · 2016-03-31 · +2.088 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2016-03-31: the Texas ratio (troubled assets against capital plus reserves), value 322.2%; contribution to the score · 2016-03-31 · +1.217 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2016-03-31: return on equity (profit as a share of equity), value -51.7%; contribution to the score · 2016-03-31 · +0.923 · data/analyst/scores.parquet: feature return_on_equity contribution
- F91 · Driver up #4 at 2016-03-31: loans 90+ days past due or not accruing interest, as a share of loans, value 17.9%; contribution to the score · 2016-03-31 · +0.661 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2016-03-31: the total risk-based capital ratio, value 4.2%; contribution to the score · 2016-03-31 · +0.492 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F98 · Last quarter the bank reported · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2016-12-31 · 6.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F100 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · -7.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F101 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 4.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F104 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2016-12-31 · +0.164 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F105 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2016-12-31 · pushed the score up · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F106 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2016-12-31 · 2.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F107 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 2.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F108 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 5.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F111 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2016-12-31 · +0.043 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F112 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2016-12-31 · little effect on the score · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F113 · Trend: securities as a share of assets, value at the as-of quarter · 2016-12-31 · 11.6% · data/features/fct_bank_features.parquet: securities_to_assets
- F114 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 12.3% · data/features/fct_bank_features.parquet: securities_to_assets
- F115 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 21.1% · data/features/fct_bank_features.parquet: securities_to_assets
- F118 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2016-12-31 · -0.061 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F119 · Trend: securities as a share of assets, what the model did with it · 2016-12-31 · pushed the score down · data/analyst/scores.parquet: feature securities_to_assets contribution
- F120 · Trend: core deposits as a share of assets, value at the as-of quarter · 2016-12-31 · 96.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F121 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 87.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F122 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 95.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F125 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2016-12-31 · +0.195 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F126 · Trend: core deposits as a share of assets, what the model did with it · 2016-12-31 · pushed the score up · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F127 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2016-12-31 · 382.7% · data/features/fct_bank_features.parquet: texas_ratio
- F128 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 81.9% · data/features/fct_bank_features.parquet: texas_ratio
- F129 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 362.8% · data/features/fct_bank_features.parquet: texas_ratio
- F130 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2016-12-31 · +19.9 pp · data/features/fct_bank_features.parquet: texas_ratio
- F131 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over four quarters, in percentage points · 2016-12-31 · +75.7 pp · data/features/fct_bank_features.parquet: texas_ratio
- F132 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2016-12-31 · +1.450 · data/analyst/scores.parquet: feature texas_ratio contribution
- F133 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2016-12-31 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F134 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2016-12-31 · 143.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F135 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 82.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F136 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 139.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F138 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2016-12-31 · -0.078 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F139 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2016-12-31 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F140 · Trend: ratios outside their own prior range · 2016-12-31 · 12 · data/features/fct_bank_features.parquet
- F141 · Trend: ratios shown in the table (the furthest outside their prior range) · 2016-12-31 · 6 · data/features/fct_bank_features.parquet
- F142 · Trend: ratios compared with their own prior range · 2016-12-31 · 30 · data/features/fct_bank_features.parquet
- F143 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F144 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F148 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2016-12-31 · 96.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F149 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2016-12-31 · 100.0th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F150 · Peers: core deposits as a share of assets, national reading · 2016-12-31 · unusually high · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F151 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2016-12-31 · 100.0th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F152 · Peers: core deposits as a share of assets, peer median · 2016-12-31 · 78.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F153 · Peers: core deposits as a share of assets, reading against its peers · 2016-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F154 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2016-12-31 · 382.7% · data/features/fct_bank_features.parquet: texas_ratio
- F155 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2016-12-31 · 99.9th · data/features/fct_bank_features.parquet: texas_ratio
- F156 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2016-12-31 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F157 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2016-12-31 · 99.9th · data/features/fct_bank_features.parquet: texas_ratio
- F158 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2016-12-31 · 6.1% · data/features/fct_bank_features.parquet: texas_ratio
- F159 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2016-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F160 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2016-12-31 · 3.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F161 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F162 · Peers: the total risk-based capital ratio, national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F163 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F164 · Peers: the total risk-based capital ratio, peer median · 2016-12-31 · 14.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F165 · Peers: the total risk-based capital ratio, reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F166 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2016-12-31 · 1.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F167 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F168 · Peers: the Tier 1 risk-based capital ratio, national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F169 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F170 · Peers: the Tier 1 risk-based capital ratio, peer median · 2016-12-31 · 13.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F171 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F172 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2016-12-31 · 18.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F173 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2016-12-31 · 99.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F174 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2016-12-31 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F175 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2016-12-31 · 99.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F176 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2016-12-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F177 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2016-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F178 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2016-12-31 · 16.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F179 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2016-12-31 · 99.9th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F180 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2016-12-31 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F181 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2016-12-31 · 99.7th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F182 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2016-12-31 · 0.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F183 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2016-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F184 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2016-12-31 · -64.3% · data/features/fct_bank_features.parquet: return_on_equity
- F185 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F186 · Peers: return on equity (profit as a share of equity), national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F187 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2016-12-31 · 0.2nd · data/features/fct_bank_features.parquet: return_on_equity
- F188 · Peers: return on equity (profit as a share of equity), peer median · 2016-12-31 · 8.4% · data/features/fct_bank_features.parquet: return_on_equity
- F189 · Peers: return on equity (profit as a share of equity), reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F190 · Peers: equity as a share of assets, bank value at the as-of quarter · 2016-12-31 · 1.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F191 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2016-12-31 · 0.4th · data/features/fct_bank_features.parquet: equity_to_assets
- F192 · Peers: equity as a share of assets, national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F193 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2016-12-31 · 0.3rd · data/features/fct_bank_features.parquet: equity_to_assets
- F194 · Peers: equity as a share of assets, peer median · 2016-12-31 · 10.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F195 · Peers: equity as a share of assets, reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F197 · Peers: ratios in the national top or bottom 10% · 2016-12-31 · 18 · data/features/fct_bank_features.parquet
- F198 · Peers: those ratios also unusual among peers · 2016-12-31 · 18 · data/features/fct_bank_features.parquet
- F200 · Peers: cut-off for unusual (top or bottom share of banks) · 2016-12-31 · 10% · data/features/fct_bank_features.parquet
