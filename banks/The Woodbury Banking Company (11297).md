---
cert: 11297
name: "The Woodbury Banking Company"
as_of: 2016-06-30
rank: 2
n_banks: 6129
percentile: 99.98368412465328
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2016-08-19
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:05:15"
writer_model: "claude-opus-5-5"
checked: true
---

# The Woodbury Banking Company (cert 11297)

*Hindsight: failed 2016-08-19. Canary flagged it 2 quarters ahead.*

## Summary

As of June 30, 2016, The Woodbury Banking Company, a bank based in Georgia, ranked 2 out of 6,129 banks on Canary's risk score, placing it in the 100.0th percentile. That put it on Canary's watchlist, which covers the 2% of banks with the highest scores. Its equity, the owners' cushion that absorbs losses, was just 1.0% of assets against a national median of 11.0%. It was also losing money, with a return on assets of -4.5% compared with a national median of 0.9%.

## Warning signs in the data

Capital, the bank's own money that stands between losses and depositors, was extremely thin. Equity was 1.0% of assets, against a national median of 11.0%. The leverage ratio (core capital as a share of average assets) was 0.8%, versus a national median of 10.5%. The Tier 1 risk-based capital ratio, which measures core capital against assets weighted by their riskiness, was 1.6% against a median of 15.1%, and the broader total risk-based capital ratio was 2.9% against 16.3%.

Loan problems were far above typical levels: loans 90 or more days past due or no longer paying interest were 8.3% of loans, against a national median of 0.7%. Nonaccrual assets and foreclosed property made up 12.8% of assets versus a median of 0.6%, and loans 30-89 days past due were 2.5% of assets versus 0.3%. The Texas ratio, which weighs troubled assets against capital plus loan-loss reserves, was 519.7%, far above the national median of 5.3%. Earnings were deeply negative, with return on assets at -4.5% against a median of 0.9%, and the efficiency ratio (operating costs as a share of revenue) at 561.8% against 69.7%.

Funding looked stable on paper: core deposits, the steady everyday deposits banks rely on, were 98.6% of assets against a national median of 78.4%, and volatile funding was 0.0% versus 5.1%. Cash was 13.1% of assets, well above the median of 6.4%. Unrealized losses on bonds available for sale equaled -21.3% of equity, much deeper than the national median of -1.6%, partly because equity itself was so small. The bank was small and shrinking, with total assets of $21.4 million and asset growth of -9.9% over the past four quarters, against medians of $195.3 million and 3.8%.

## Understanding the score

As of June 30, 2016, the bank ranked 2 out of 6,129 banks, in the 100.0th percentile on a scale from 0 to 100 where higher means riskier. It was flagged on the watchlist, one of 123 banks that quarter, the top 2% by score.

The five features that pushed the score up most were the Tier 1 risk-based capital ratio at 1.6% (+2.122), the Texas ratio at 519.7% (+1.338), return on equity at -195.4% (+1.335), the total risk-based capital ratio at 2.9% (+0.551), and the leverage ratio at 0.8% (+0.491).

The five features that pulled the score down most were interest expense as a share of assets at 0.4% (-0.558), losses on bonds available for sale as a share of equity at -21.3% (-0.317), construction loans as a share of loans at 3.4% (-0.194), net interest margin at 3.9% (-0.107), and brokered deposits, money placed through middlemen, at 0.0% of deposits (-0.093). These downward pulls were small next to the capital and loss figures pushing the score up.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 22 | 6,193 | ▲ watchlist (first flag) |
| 2016-06-30 | 2 | 6,129 | ▲ watchlist |

## How its ratios moved

Canary compared 29 of the bank's ratios with their own history, usually the prior 12 quarters, and found 16 outside that prior range. Year-to-date ratios were instead compared with the same quarter in the prior 3 years.

The Texas ratio reached 519.7%, above its prior range of 71.7% to 304.6%, rising +228.1 pp over one quarter and +356.3 pp over four quarters. At that 519.7% value, the Texas ratio contributed +1.338 model log-odds units and pushed the score up. Return on equity fell to -195.4%, far below its prior range of -34.5% to 9.7%, a change of -160.9 pp over four quarters, and its contribution of +1.335 pushed the score up. Return on assets dropped to -4.5%, below its prior range of -1.9% to 0.6%, and its contribution of +0.104 pushed the score up.

Some ratios moved far outside their history yet barely moved the score. The efficiency ratio jumped to 561.8%, well above its prior range of 89.2% to 185.7%, yet its contribution of -0.031 had little effect on the score. Loan write-offs rose to 2.9% of loans from a prior range of -0.1% to -0.1%, yet their contribution of -0.014 had little effect on the score. Losses on bonds available for sale deepened to -21.3% of equity, below their prior range of -3.6% to 18.6%, yet their contribution of -0.317 pushed the score down.

There is no score from a year earlier to compare with (scores start 2016-03-31, or the bank did not report then).

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 561.8% | 89.2% to 185.7% | same quarter, prior 3 years | n/a | +376.1 pp | -0.031 | little effect on the score |
| return on equity (profit as a share of equity) | -195.4% | -34.5% to 9.7% | same quarter, prior 3 years | n/a | -160.9 pp | +1.335 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 2.9% | -0.1% to -0.1% | same quarter, prior 3 years | n/a | +2.9 pp | -0.014 | little effect on the score |
| return on assets (profit as a share of assets) | -4.5% | -1.9% to 0.6% | same quarter, prior 3 years | n/a | -2.6 pp | +0.104 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 519.7% | 71.7% to 304.6% | prior 12 quarters | +228.1 pp | +356.3 pp | +1.338 | pushed the score up |
| losses on bonds available for sale, as a share of equity | -21.3% | -3.6% to 18.6% | prior 12 quarters | -17.7 pp | -29.0 pp | -0.317 | pushed the score down |

16 of 29 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2016-06-30: All Other Under 1 Billion.

This is a general group: the FDIC did not record a lending specialty for this bank.

Peers: 254 banks in the same specialty group and size tier (under $100 million).

The Tier 1 risk-based capital ratio of 1.6% sat in the 0.0th percentile nationally, unusually low, and in the 0.2nd percentile among peers against a peer median of 19.2%, unusually low among its peers too. The total risk-based capital ratio of 2.9% was in the 0.0th percentile nationally, unusually low, and in the 0.2nd percentile among peers against a peer median of 20.3%, unusually low among its peers too. Equity at 1.0% of assets was in the 0.3rd percentile nationally, unusually low, and in the 0.2nd percentile among peers against a peer median of 11.1%, unusually low among its peers too.

Return on equity of -195.4% was in the 0.0th percentile nationally, unusually low, and in the 0.2nd percentile among peers against a peer median of 5.7%, unusually low among its peers too. Return on assets of -4.5% was in the 0.2nd percentile nationally, unusually low, and in the 0.2nd percentile among peers against a peer median of 0.6%, unusually low among its peers too. The Texas ratio of 519.7% was in the 100.0th percentile nationally, unusually high, and in the 99.8th percentile among peers against a peer median of 7.1%, unusually high among its peers too. The efficiency ratio of 561.8% was in the 99.9th percentile nationally, unusually high, and in the 99.8th percentile among peers against a peer median of 79.9%, unusually high among its peers too. Core deposits at 98.6% of assets were in the 100.0th percentile nationally, unusually high, and in the 99.8th percentile among peers against a peer median of 84.0%, unusually high among its peers too.

Overall, 20 of the bank's ratios fell in the national top or bottom 10%, and 18 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| core deposits as a share of assets | 98.6% | 100.0th (unusually high) | 84.0% | 99.8th | unusually high among its peers too |
| the total risk-based capital ratio | 2.9% | 0.0th (unusually low) | 20.3% | 0.2nd | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 1.6% | 0.0th (unusually low) | 19.2% | 0.2nd | unusually low among its peers too |
| return on equity (profit as a share of equity) | -195.4% | 0.0th (unusually low) | 5.7% | 0.2nd | unusually low among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 519.7% | 100.0th (unusually high) | 7.1% | 99.8th | unusually high among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 561.8% | 99.9th (unusually high) | 79.9% | 99.8th | unusually high among its peers too |
| return on assets (profit as a share of assets) | -4.5% | 0.2nd (unusually low) | 0.6% | 0.2nd | unusually low among its peers too |
| equity as a share of assets | 1.0% | 0.3rd (unusually low) | 11.1% | 0.2nd | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: total risk-based capital, as the 2006 guidance specifies.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 95.5% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 620.4% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | -55.9% | 50% or more | no |

It did not cross the construction line.
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, the bank failed on 2016-08-19. Canary first flagged it in the quarter ending 2016-03-31, a lead time of 2 quarters before the failure.

At that first flag, the main upward drivers were the Texas ratio at 291.6% (+1.063), the Tier 1 risk-based capital ratio at 4.9% (+0.623), and loans 90+ days past due or not accruing interest at 10.4% of loans (+0.450). By June 30, 2016, these capital and troubled-asset figures had worsened further, and the bank remained flagged.

## What happened next

In hindsight, the quarter ending 2016-06-30 was the last one the bank reported. The bank failed on 2016-08-19, less than two months after that final report.

## Sources

- F1 · Bank name · n/a · The Woodbury Banking Company · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2016-06-30 · 2016-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · GA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-06-30 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-06-30 · 6,129 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-06-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-06-30 · 123 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-06-30 · 1.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-06-30 · 11.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-06-30 · 0.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-06-30 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-06-30 · 1.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-06-30 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-06-30 · 2.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-06-30 · 16.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-06-30 · 8.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-06-30 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-06-30 · 12.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-06-30 · 0.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2016-06-30 · 2.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2016-06-30 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2016-06-30 · 519.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2016-06-30 · 5.3% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-06-30 · -4.5% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-06-30 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2016-06-30 · 561.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2016-06-30 · 69.7% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F53 · Bank: core deposits as a share of assets · 2016-06-30 · 98.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F54 · National median: core deposits as a share of assets · 2016-06-30 · 78.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: volatile funding as a share of assets · 2016-06-30 · 0.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F58 · National median: volatile funding as a share of assets · 2016-06-30 · 5.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F59 · Bank: cash as a share of assets · 2016-06-30 · 13.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F60 · National median: cash as a share of assets · 2016-06-30 · 6.4% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds available for sale, as a share of equity · 2016-06-30 · -21.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F64 · National median: losses on bonds available for sale, as a share of equity · 2016-06-30 · -1.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: total assets · 2016-06-30 · $21.4 million · data/features/fct_bank_features.parquet: log_total_assets
- F68 · National median: total assets · 2016-06-30 · $195.3 million · data/features/fct_bank_features.parquet: log_total_assets (median of all banks)
- F69 · Bank: asset growth over the past four quarters · 2016-06-30 · -9.9% · data/features/fct_bank_features.parquet: asset_growth_4q
- F70 · National median: asset growth over the past four quarters · 2016-06-30 · 3.8% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Driver up #1: the Tier 1 risk-based capital ratio, value 1.6%; contribution to the score · 2016-06-30 · +2.122 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F74 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 519.7%; contribution to the score · 2016-06-30 · +1.338 · data/analyst/scores.parquet: feature texas_ratio contribution
- F75 · Driver up #3: return on equity (profit as a share of equity), value -195.4%; contribution to the score · 2016-06-30 · +1.335 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #4: the total risk-based capital ratio, value 2.9%; contribution to the score · 2016-06-30 · +0.551 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F77 · Driver up #5: the leverage ratio (core capital as a share of average assets), value 0.8%; contribution to the score · 2016-06-30 · +0.491 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F78 · Driver down #1: annualized interest expense as a share of assets, value 0.4%; contribution to the score · 2016-06-30 · -0.558 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F79 · Driver down #2: losses on bonds available for sale, as a share of equity, value -21.3%; contribution to the score · 2016-06-30 · -0.317 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F80 · Driver down #3: construction loans as a share of loans, value 3.4%; contribution to the score · 2016-06-30 · -0.194 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F81 · Driver down #4: net interest margin (the spread earned on lending and investing), value 3.9%; contribution to the score · 2016-06-30 · -0.107 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F82 · Driver down #5: brokered deposits as a share of deposits, value 0.0%; contribution to the score · 2016-06-30 · -0.093 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F83 · Failure date · 2016-08-19 · 2016-08-19 · data/raw/failures: FAILDATE
- F84 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F85 · Lead time in quarters before failure · n/a · 2 · data/analyst/scores.parquet: quarters_until_failure
- F86 · Driver up #1 at 2016-03-31: the Texas ratio (troubled assets against capital plus reserves), value 291.6%; contribution to the score · 2016-03-31 · +1.063 · data/analyst/scores.parquet: feature texas_ratio contribution
- F87 · Driver up #2 at 2016-03-31: the Tier 1 risk-based capital ratio, value 4.9%; contribution to the score · 2016-03-31 · +0.623 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F88 · Driver up #3 at 2016-03-31: loans 90+ days past due or not accruing interest, as a share of loans, value 10.4%; contribution to the score · 2016-03-31 · +0.450 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F96 · Last quarter the bank reported · 2016-06-30 · 2016-06-30 · data/features/fct_bank_features.parquet: report_date
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2016-06-30 · 561.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 89.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 185.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2016-06-30 · -0.031 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F102 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2016-06-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F103 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2016-06-30 · -195.4% · data/features/fct_bank_features.parquet: return_on_equity
- F104 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -34.5% · data/features/fct_bank_features.parquet: return_on_equity
- F105 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 9.7% · data/features/fct_bank_features.parquet: return_on_equity
- F106 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2016-06-30 · -160.9 pp · data/features/fct_bank_features.parquet: return_on_equity
- F107 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2016-06-30 · +1.335 · data/analyst/scores.parquet: feature return_on_equity contribution
- F108 · Trend: return on equity (profit as a share of equity), what the model did with it · 2016-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F109 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2016-06-30 · 2.9% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F110 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · -0.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F111 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · -0.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F113 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2016-06-30 · -0.014 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F114 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2016-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F115 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2016-06-30 · -4.5% · data/features/fct_bank_features.parquet: return_on_assets
- F116 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -1.9% · data/features/fct_bank_features.parquet: return_on_assets
- F117 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F119 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2016-06-30 · +0.104 · data/analyst/scores.parquet: feature return_on_assets contribution
- F120 · Trend: return on assets (profit as a share of assets), what the model did with it · 2016-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F121 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2016-06-30 · 519.7% · data/features/fct_bank_features.parquet: texas_ratio
- F122 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 71.7% · data/features/fct_bank_features.parquet: texas_ratio
- F123 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 304.6% · data/features/fct_bank_features.parquet: texas_ratio
- F124 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2016-06-30 · +228.1 pp · data/features/fct_bank_features.parquet: texas_ratio
- F125 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over four quarters, in percentage points · 2016-06-30 · +356.3 pp · data/features/fct_bank_features.parquet: texas_ratio
- F126 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2016-06-30 · +1.338 · data/analyst/scores.parquet: feature texas_ratio contribution
- F127 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2016-06-30 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F128 · Trend: losses on bonds available for sale, as a share of equity, value at the as-of quarter · 2016-06-30 · -21.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F129 · Trend: losses on bonds available for sale, as a share of equity, lowest value in the comparison window · n/a · -3.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F130 · Trend: losses on bonds available for sale, as a share of equity, highest value in the comparison window · n/a · 18.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F133 · Trend: losses on bonds available for sale, as a share of equity, contribution to the score (model log-odds units) · 2016-06-30 · -0.317 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F134 · Trend: losses on bonds available for sale, as a share of equity, what the model did with it · 2016-06-30 · pushed the score down · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F135 · Trend: ratios outside their own prior range · 2016-06-30 · 16 · data/features/fct_bank_features.parquet
- F137 · Trend: ratios compared with their own prior range · 2016-06-30 · 29 · data/features/fct_bank_features.parquet
- F138 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F139 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F143 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2016-06-30 · 98.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F144 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2016-06-30 · 100.0th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F145 · Peers: core deposits as a share of assets, national reading · 2016-06-30 · unusually high · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F146 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2016-06-30 · 99.8th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F147 · Peers: core deposits as a share of assets, peer median · 2016-06-30 · 84.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F148 · Peers: core deposits as a share of assets, reading against its peers · 2016-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F149 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2016-06-30 · 2.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F150 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2016-06-30 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F151 · Peers: the total risk-based capital ratio, national reading · 2016-06-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F152 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2016-06-30 · 0.2nd · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F153 · Peers: the total risk-based capital ratio, peer median · 2016-06-30 · 20.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F154 · Peers: the total risk-based capital ratio, reading against its peers · 2016-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F155 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2016-06-30 · 1.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F156 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2016-06-30 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F157 · Peers: the Tier 1 risk-based capital ratio, national reading · 2016-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F158 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2016-06-30 · 0.2nd · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F159 · Peers: the Tier 1 risk-based capital ratio, peer median · 2016-06-30 · 19.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F160 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2016-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F161 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2016-06-30 · -195.4% · data/features/fct_bank_features.parquet: return_on_equity
- F162 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2016-06-30 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F163 · Peers: return on equity (profit as a share of equity), national reading · 2016-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F164 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2016-06-30 · 0.2nd · data/features/fct_bank_features.parquet: return_on_equity
- F165 · Peers: return on equity (profit as a share of equity), peer median · 2016-06-30 · 5.7% · data/features/fct_bank_features.parquet: return_on_equity
- F166 · Peers: return on equity (profit as a share of equity), reading against its peers · 2016-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F167 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2016-06-30 · 519.7% · data/features/fct_bank_features.parquet: texas_ratio
- F168 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2016-06-30 · 100.0th · data/features/fct_bank_features.parquet: texas_ratio
- F169 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2016-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F170 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2016-06-30 · 99.8th · data/features/fct_bank_features.parquet: texas_ratio
- F171 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2016-06-30 · 7.1% · data/features/fct_bank_features.parquet: texas_ratio
- F172 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2016-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F173 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2016-06-30 · 561.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F174 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2016-06-30 · 99.9th · data/features/fct_bank_features.parquet: efficiency_ratio
- F175 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2016-06-30 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F176 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2016-06-30 · 99.8th · data/features/fct_bank_features.parquet: efficiency_ratio
- F177 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2016-06-30 · 79.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F178 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2016-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F179 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2016-06-30 · -4.5% · data/features/fct_bank_features.parquet: return_on_assets
- F180 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2016-06-30 · 0.2nd · data/features/fct_bank_features.parquet: return_on_assets
- F181 · Peers: return on assets (profit as a share of assets), national reading · 2016-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F182 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2016-06-30 · 0.2nd · data/features/fct_bank_features.parquet: return_on_assets
- F183 · Peers: return on assets (profit as a share of assets), peer median · 2016-06-30 · 0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F184 · Peers: return on assets (profit as a share of assets), reading against its peers · 2016-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F185 · Peers: equity as a share of assets, bank value at the as-of quarter · 2016-06-30 · 1.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F186 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2016-06-30 · 0.3rd · data/features/fct_bank_features.parquet: equity_to_assets
- F187 · Peers: equity as a share of assets, national reading · 2016-06-30 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F188 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2016-06-30 · 0.2nd · data/features/fct_bank_features.parquet: equity_to_assets
- F189 · Peers: equity as a share of assets, peer median · 2016-06-30 · 11.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F190 · Peers: equity as a share of assets, reading against its peers · 2016-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F192 · Peers: ratios in the national top or bottom 10% · 2016-06-30 · 20 · data/features/fct_bank_features.parquet
- F193 · Peers: those ratios also unusual among peers · 2016-06-30 · 18 · data/features/fct_bank_features.parquet
- F195 · Peers: cut-off for unusual (top or bottom share of banks) · 2016-06-30 · 10% · data/features/fct_bank_features.parquet
