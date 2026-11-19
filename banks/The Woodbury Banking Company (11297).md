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
written_at: "2026-11-18T19:48:11"
writer_model: "claude-opus-5-5"
checked: true
---

# The Woodbury Banking Company (cert 11297)

*Hindsight: failed 2016-08-19. Canary flagged it 2 quarters ahead.*

## Summary

The Woodbury Banking Company, a small bank in GA with $21.4 million in total assets, ranked 2 out of 6,129 banks nationally on Canary's risk score as of 2016-06-30, which places it in the 100.0th percentile. That puts it on Canary's watchlist, the top 2% of banks by score. Its capital cushion was very thin: equity, the owners' stake that absorbs losses, was 1.0% of assets against a national median of 11.0%. It was also losing money, with a return on assets of -4.5% compared with a national median of 0.9%.

## Warning signs in the data

Capital, the cushion a bank holds to absorb losses, was far below normal levels. The leverage ratio (core capital as a share of average assets) was 0.8%, against a national median of 10.5%. The Tier 1 risk-based capital ratio, which measures core capital against riskier assets, was 1.6% versus a median of 15.1%, and the total risk-based capital ratio was 2.9% versus 16.3%.

Credit quality, meaning how well borrowers were repaying, was weak. Loans 90+ days past due or no longer earning interest made up 8.3% of loans, well above the national median of 0.7%. Nonaccrual assets and foreclosed property were 12.8% of assets against a median of 0.6%, and the Texas ratio, which compares troubled assets with capital plus reserves, stood at 519.7% versus a median of 5.3%. Net loan write-offs ran at an annualized 2.9% of loans, compared with a national median of 0.0%.

Funding looked stable: core deposits, the steady everyday deposits banks rely on, were 98.6% of assets against a median of 78.4%, and brokered deposits were 0.0%. Cash was 13.1% of assets, above the national median of 6.4%. Unrealized losses on bonds available for sale equalled -21.3% of equity, much deeper than the national median of -1.6%.

## Understanding the score

As of 2016-06-30, the bank ranked 2 out of 6,129 banks, in the 100.0th percentile on a scale where higher means riskier. It was flagged on the watchlist, one of 123 banks that quarter, which covers the top 2% of banks by score.

The five factors that pushed the score up most were all about thin capital, troubled loans and losses. They were the Tier 1 risk-based capital ratio at 1.6%, the Texas ratio at 519.7%, and return on equity (profit as a share of the owners' stake) at -195.4%. The other two were the total risk-based capital ratio at 2.9% and the leverage ratio at 0.8%.

Five factors pulled the score down somewhat. These were interest expense at 0.4% of assets, losses on bonds available for sale at -21.3% of equity, and construction loans at 3.4% of loans. The last two were the net interest margin, the spread earned on lending and investing, at 3.9%, and brokered deposits at 0.0% of deposits.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 22 | 6,193 | ▲ watchlist (first flag) |
| 2016-06-30 | 2 | 6,129 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own range over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 29 ratios compared this way, 16 were outside their own prior range at the as-of quarter, when the bank ranked 2 nationally.

The Texas ratio stood at 519.7%, well above its prior range of 71.7% to 304.6%, and its contribution of +1.338 model log-odds units pushed the score up. Return on equity was -195.4%, far below its prior range of -34.5% to 9.7%, and its contribution of +1.335 model log-odds units pushed the score up.

The efficiency ratio, operating costs as a share of revenue, reached 561.8%, far above its prior range of 89.2% to 185.7%, yet its contribution of -0.031 model log-odds units meant it had little effect on the score. Losses on bonds available for sale reached -21.3% of equity, outside their prior range of -3.6% to 18.6%, but in contrast this ratio's contribution of -0.317 model log-odds units pushed the score down.

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

## How early Canary caught it

With hindsight, Canary first flagged the bank in the quarter ending 2016-03-31, and the bank failed on 2016-08-19. That gave a lead time of 2 quarters before the failure. At that first flag, the top factors raising the score were the Texas ratio at 291.6% and the Tier 1 risk-based capital ratio at 4.9%. Past-due and nonaccruing loans at 10.4% of loans and the total risk-based capital ratio at 6.2% also pushed it up.

## What happened next

In hindsight, the bank failed on 2016-08-19. Its last reported quarter was 2016-06-30, the same quarter as this memo, so no later ranks exist. After that the bank stopped reporting; our data does not distinguish between a merger and a closure, though the failure date above records how it ended.

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
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2016-06-30 · 2.9% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2016-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2016-06-30 · 519.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2016-06-30 · 5.3% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-06-30 · -4.5% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-06-30 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: brokered deposits as a share of deposits · 2016-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F53 · Bank: core deposits as a share of assets · 2016-06-30 · 98.6% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F54 · National median: core deposits as a share of assets · 2016-06-30 · 78.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: cash as a share of assets · 2016-06-30 · 13.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F60 · National median: cash as a share of assets · 2016-06-30 · 6.4% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds available for sale, as a share of equity · 2016-06-30 · -21.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F64 · National median: losses on bonds available for sale, as a share of equity · 2016-06-30 · -1.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: total assets · 2016-06-30 · $21.4 million · data/features/fct_bank_features.parquet: log_total_assets
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
- F90 · Driver up #5 at 2016-03-31: the total risk-based capital ratio, value 6.2%; contribution to the score · 2016-03-31 · +0.304 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F96 · Last quarter the bank reported · 2016-06-30 · 2016-06-30 · data/features/fct_bank_features.parquet: report_date
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2016-06-30 · 561.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 89.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 185.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2016-06-30 · -0.031 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F102 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2016-06-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F103 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2016-06-30 · -195.4% · data/features/fct_bank_features.parquet: return_on_equity
- F104 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -34.5% · data/features/fct_bank_features.parquet: return_on_equity
- F105 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 9.7% · data/features/fct_bank_features.parquet: return_on_equity
- F107 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2016-06-30 · +1.335 · data/analyst/scores.parquet: feature return_on_equity contribution
- F108 · Trend: return on equity (profit as a share of equity), what the model did with it · 2016-06-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F121 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2016-06-30 · 519.7% · data/features/fct_bank_features.parquet: texas_ratio
- F122 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 71.7% · data/features/fct_bank_features.parquet: texas_ratio
- F123 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 304.6% · data/features/fct_bank_features.parquet: texas_ratio
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
