---
cert: 19328
name: "Seaway Bank And Trust Company"
as_of: 2016-12-31
rank: 7
n_banks: 5983
percentile: 99.89971586160789
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-01-27
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:49:52"
writer_model: "claude-opus-5-5"
checked: true
---

# Seaway Bank And Trust Company (cert 19328)

*Hindsight: failed 2017-01-27. Canary flagged it 4 quarters ahead.*

## Summary

Seaway Bank And Trust Company, based in IL, ranked 7 out of 5,983 banks nationally on Canary's risk score as of 2016-12-31, placing it in the 99.9th percentile. It was flagged on Canary's watchlist, which covers the riskiest 2% of banks. Its capital cushion had turned negative, with equity at -1.9% of assets against a national median of 10.7%. It was also losing money heavily, with a return on assets (profit as a share of assets) of -7.2% versus a median of 0.9%.

## Warning signs in the data

Capital, the owners' money that absorbs losses, was below zero on every measure shown. Equity was -1.9% of assets against a national median of 10.7%, and the leverage ratio (core capital as a share of average assets) was -1.8% against a median of 10.4%. The Tier 1 risk-based capital ratio, which weighs assets by riskiness, was -3.1% against a median of 15.0%, and the total risk-based capital ratio was -1.8% against a median of 16.2%.

Credit quality was weak: loans 90+ days past due or not accruing interest were 8.8% of loans, far above the median of 0.6%, and loans 30-89 days past due were 5.4% of assets against a median of 0.3%. Nonaccrual assets and foreclosed property were 4.1% of assets against a median of 0.5%, and net loan write-offs were 1.3% of loans against a median of 0.1%. Costs swamped income, with an efficiency ratio (operating costs as a share of revenue) of 249.2% against a median of 69.7%, and return on equity was -156.0% against a median of 8.0%.

On funding, the bank leaned on Federal Home Loan Bank borrowings at 14.3% of assets, well above the median of 0.7%, and volatile funding was 17.7% of assets against a median of 5.2%. It was shrinking, with asset growth of -19.5% and deposit growth of -12.3% over the past four quarters, while the medians were 3.5% and 3.6%. Some figures were less worrying: uninsured deposits were only 5.2% of deposits against a median of 17.3%, cash was 17.1% of assets against a median of 6.6%, and losses on bonds available for sale were a modest 1.7% of equity against a median of 0.7%.

## Understanding the score

The bank ranked 7 out of 5,983 banks as of 2016-12-31, which is the 99.9th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, one of 120 banks that quarter, a list that holds the top 2% of banks by score.

The five factors that pushed the score up most were the Tier 1 risk-based capital ratio at -3.1% (+1.908), return on equity at -156.0% (+1.554), the total risk-based capital ratio at -1.8% (+0.881), the leverage ratio at -1.8% (+0.669), and loans 90+ days past due or not accruing interest at 8.8% of loans (+0.508).

The five factors that pulled the score down most were interest expense at 0.6% of assets (-1.391), the Texas ratio (troubled assets against capital plus reserves) at -2563.3% (-1.043), construction loans at 4.1% of loans (-0.199), total assets of $297.8 million (-0.162), and commercial real estate loans at 42.2% of loans (-0.099).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 7 | 6,193 | ▲ watchlist (first flag) |
| 2016-06-30 | 9 | 6,129 | ▲ watchlist |
| 2016-09-30 | 2 | 6,051 | ▲ watchlist |
| 2016-12-31 | 7 | 5,983 | ▲ watchlist |

## How its ratios moved

Each ratio is compared with its own prior range over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 30 ratios checked, 16 were outside their own prior range, and the model ranked the bank 7 out of 5,983 at the 99.9th percentile.

The leverage ratio fell to -1.8%, below its prior range of 1.9% to 9.4%, after a -7.5 pp change over four quarters, and contributed +0.669 model log-odds units, which pushed the score up. Return on equity dropped to -156.0%, far below its prior range of -30.5% to 2.2%, and contributed +1.554 model log-odds units, which pushed the score up. Return on assets fell to -7.2%, below its prior range of -2.9% to 0.2%, and contributed +0.175 model log-odds units, which pushed the score up.

The Texas ratio swung to -2563.3%, far outside its prior range of 90.3% to 192.6%, yet it contributed -1.043 model log-odds units and pushed the score down. The efficiency ratio rose to 249.2%, above its prior range of 88.0% to 169.8%, but contributed only -0.027 model log-odds units, little effect on the score. Net interest margin, the spread earned on lending and investing, slipped to 3.1%, below its prior range of 4.0% to 4.9%, yet it contributed -0.054 model log-odds units and pushed the score down.

There is no score from a year earlier to compare with (scores start 2016-03-31, or the bank did not report then).

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | -2563.3% | 90.3% to 192.6% | prior 12 quarters | -2755.9 pp | -2721.8 pp | -1.043 | pushed the score down |
| return on equity (profit as a share of equity) | -156.0% | -30.5% to 2.2% | same quarter, prior 3 years | n/a | -125.5 pp | +1.554 | pushed the score up |
| return on assets (profit as a share of assets) | -7.2% | -2.9% to 0.2% | same quarter, prior 3 years | n/a | -4.3 pp | +0.175 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 249.2% | 88.0% to 169.8% | same quarter, prior 3 years | n/a | +79.4 pp | -0.027 | little effect on the score |
| net interest margin (the spread earned on lending and investing) | 3.1% | 4.0% to 4.9% | same quarter, prior 3 years | n/a | -0.9 pp | -0.054 | pushed the score down |
| the leverage ratio (core capital as a share of average assets) | -1.8% | 1.9% to 9.4% | prior 12 quarters | -3.7 pp | -7.5 pp | +0.669 | pushed the score up |

16 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Canary first flagged the bank in the quarter ending 2016-03-31, a lead time of 4 quarters before it failed on 2017-01-27. At that first flag, the top factors pushing the score up were the Tier 1 risk-based capital ratio at 5.5% (+1.369), the Texas ratio at 167.1% (+1.342), and return on equity at -63.1% (+1.324). Loans 90+ days past due or not accruing interest were also high then, at 19.5% of loans (+0.741).

## What happened next

In hindsight, the bank failed on January 27, 2017, shortly after the as-of quarter. Its last financial report was for the quarter ending 2016-12-31, so there are no later ranks or flags to show.

## Sources

- F1 · Bank name · n/a · Seaway Bank And Trust Company · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-12-31 · 7 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-12-31 · 5,983 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-12-31 · 99.9% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-12-31 · 120 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-12-31 · -1.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-12-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · -1.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-12-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-12-31 · -3.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-12-31 · 15.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-12-31 · -1.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-12-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 8.8% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-12-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 4.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-12-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2016-12-31 · 5.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2016-12-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2016-12-31 · 1.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2016-12-31 · 0.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-12-31 · -7.2% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-12-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2016-12-31 · -156.0% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2016-12-31 · 8.0% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2016-12-31 · 249.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2016-12-31 · 69.7% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2016-12-31 · 5.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2016-12-31 · 17.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2016-12-31 · 14.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2016-12-31 · 0.7% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2016-12-31 · 17.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2016-12-31 · 5.2% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2016-12-31 · 17.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2016-12-31 · 6.6% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2016-12-31 · 1.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2016-12-31 · 0.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2016-12-31 · -19.5% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2016-12-31 · 3.5% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2016-12-31 · -12.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2016-12-31 · 3.6% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value -3.1%; contribution to the score · 2016-12-31 · +1.908 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -156.0%; contribution to the score · 2016-12-31 · +1.554 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the total risk-based capital ratio, value -1.8%; contribution to the score · 2016-12-31 · +0.881 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value -1.8%; contribution to the score · 2016-12-31 · +0.669 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: loans 90+ days past due or not accruing interest, as a share of loans, value 8.8%; contribution to the score · 2016-12-31 · +0.508 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.6%; contribution to the score · 2016-12-31 · -1.391 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value -2563.3%; contribution to the score · 2016-12-31 · -1.043 · data/analyst/scores.parquet: feature texas_ratio contribution
- F82 · Driver down #3: construction loans as a share of loans, value 4.1%; contribution to the score · 2016-12-31 · -0.199 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F83 · Driver down #4: total assets, value $297.8 million; contribution to the score · 2016-12-31 · -0.162 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: commercial real estate loans as a share of loans, value 42.2%; contribution to the score · 2016-12-31 · -0.099 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F85 · Failure date · 2017-01-27 · 2017-01-27 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-03-31: the Tier 1 risk-based capital ratio, value 5.5%; contribution to the score · 2016-03-31 · +1.369 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2016-03-31: the Texas ratio (troubled assets against capital plus reserves), value 167.1%; contribution to the score · 2016-03-31 · +1.342 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2016-03-31: return on equity (profit as a share of equity), value -63.1%; contribution to the score · 2016-03-31 · +1.324 · data/analyst/scores.parquet: feature return_on_equity contribution
- F91 · Driver up #4 at 2016-03-31: loans 90+ days past due or not accruing interest, as a share of loans, value 19.5%; contribution to the score · 2016-03-31 · +0.741 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F98 · Last quarter the bank reported · 2016-12-31 · 2016-12-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2016-12-31 · -2563.3% · data/features/fct_bank_features.parquet: texas_ratio
- F100 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 90.3% · data/features/fct_bank_features.parquet: texas_ratio
- F101 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 192.6% · data/features/fct_bank_features.parquet: texas_ratio
- F104 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2016-12-31 · -1.043 · data/analyst/scores.parquet: feature texas_ratio contribution
- F105 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2016-12-31 · pushed the score down · data/analyst/scores.parquet: feature texas_ratio contribution
- F106 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2016-12-31 · -156.0% · data/features/fct_bank_features.parquet: return_on_equity
- F107 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -30.5% · data/features/fct_bank_features.parquet: return_on_equity
- F108 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: return_on_equity
- F110 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2016-12-31 · +1.554 · data/analyst/scores.parquet: feature return_on_equity contribution
- F111 · Trend: return on equity (profit as a share of equity), what the model did with it · 2016-12-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F112 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2016-12-31 · -7.2% · data/features/fct_bank_features.parquet: return_on_assets
- F113 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -2.9% · data/features/fct_bank_features.parquet: return_on_assets
- F114 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: return_on_assets
- F116 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2016-12-31 · +0.175 · data/analyst/scores.parquet: feature return_on_assets contribution
- F117 · Trend: return on assets (profit as a share of assets), what the model did with it · 2016-12-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F118 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2016-12-31 · 249.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F119 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 88.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F120 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 169.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F122 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2016-12-31 · -0.027 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F123 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2016-12-31 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F124 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2016-12-31 · 3.1% · data/features/fct_bank_features.parquet: net_interest_margin
- F125 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 4.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F126 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 4.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F128 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2016-12-31 · -0.054 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F129 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2016-12-31 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F130 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2016-12-31 · -1.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F131 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 1.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F132 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 9.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F134 · Trend: the leverage ratio (core capital as a share of average assets), change over four quarters, in percentage points · 2016-12-31 · -7.5 pp · data/features/fct_bank_features.parquet: leverage_ratio
- F135 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2016-12-31 · +0.669 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F136 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2016-12-31 · pushed the score up · data/analyst/scores.parquet: feature leverage_ratio contribution
- F137 · Trend: ratios outside their own prior range · 2016-12-31 · 16 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios compared with their own prior range · 2016-12-31 · 30 · data/features/fct_bank_features.parquet
- F140 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
