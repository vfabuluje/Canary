---
cert: 30003
name: "Guaranty Bank"
as_of: 2017-03-31
rank: 33
n_banks: 5925
percentile: 99.45991561181434
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-05-05
model_run: "bf7af0bddf5b"
written_at: "2026-11-18T19:50:42"
writer_model: "claude-opus-5-5"
checked: true
---

# Guaranty Bank (cert 30003)

*Hindsight: failed 2017-05-05. Canary flagged it 4 quarters ahead.*

## Summary

As of 2017-03-31, Guaranty Bank, a Wisconsin bank, ranked 33 out of 5,925 banks on Canary's risk score, placing it in the 99.5th percentile, where higher means riskier. That put it on Canary's watchlist, the riskiest 2% of banks. Its equity, the owners' cushion against losses, was 2.1% of assets, far below the national median of 10.7%. Its Texas ratio, which compares troubled loans and property with capital plus reserves, was 109.7%, against a national median of 4.8%.

## Warning signs in the data

Capital, the bank's own money that absorbs losses, was very thin: the leverage ratio (core capital as a share of average assets) was 2.1%, against a national median of 10.5%. The Tier 1 risk-based capital ratio, which weighs capital against the riskiness of assets, was 3.1%, against a median of 15.1%. The total risk-based capital ratio was 4.4%, against a median of 16.2%.

Credit quality was weak: loans 90 or more days past due or no longer earning interest were 4.5% of loans, well above the median of 0.6%. Nonaccrual assets and foreclosed property were 3.4% of assets, against a median of 0.5%, and the Texas ratio stood at 109.7%, against a median of 4.8%. Costs were also high, with an efficiency ratio (operating costs as a share of revenue) of 93.9%, against a median of 69.8%.

Funding looked steady: core deposits, the stable everyday kind, were 97.0% of assets against a median of 79.0%, and uninsured deposits were only 1.3% of deposits against a median of 17.3%. Cash was 14.9% of assets, above the median of 6.9%. Unrealized bond losses were small: -0.2% of equity on bonds held to maturity against a median of 0.0%, and 0.4% on bonds available for sale against a median of 0.3%.

## Understanding the score

As of 2017-03-31, Guaranty Bank ranked 33 out of 5,925 banks, the 99.5th percentile on a 0 to 100 scale where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks, 119 banks that quarter.

The five factors that pushed the score up most were the Tier 1 risk-based capital ratio at 3.1% (+1.350), the Texas ratio at 109.7% (+0.604), the total risk-based capital ratio at 4.4% (+0.518), core deposits at 97.0% of assets (+0.318), and commercial real estate loans at 0.2% of loans (+0.281). The five that pulled it down most were interest expense at 0.0% of assets (-1.410), return on equity, profit as a share of equity, at 21.5% (-0.861), loans 30-89 days past due at 0.3% of assets (-0.619), return on assets at 0.4% (-0.558), and total assets of $1.0 billion (-0.340).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 20 | 6,193 | ▲ watchlist |
| 2016-06-30 | 21 | 6,129 | ▲ watchlist (first flag) |
| 2016-09-30 | 11 | 6,051 | ▲ watchlist |
| 2016-12-31 | 17 | 5,983 | ▲ watchlist |
| 2017-03-31 | 33 | 5,925 | ▲ watchlist |

## How its ratios moved

Canary compared 30 ratios with their own range over the prior 12 quarters, and 12 were outside that range; the 6 furthest outside are shown in the table. The bank was in the 99.7th percentile a year earlier, on 2016-03-31, and the model rated it about the same as a year earlier, at rank 33 out of 5,925 now.

The Texas ratio was 109.7%, below its prior range of 125.6% to 175.8%, yet it still pushed the score up, contributing +0.604 model log-odds units. The Texas ratio moved -16.3 pp over one quarter and -27.1 pp over four quarters. Nonaccrual assets and foreclosed property were 3.4% of assets, below their prior range of 3.9% to 8.4%, and had little effect on the score at +0.020. Net loan write-offs were 0.4% of loans, below their prior range of 0.9% to 3.7%, and had little effect on the score at -0.012.

Net interest margin, the spread earned on lending and investing, was 3.8%, above its prior range of 2.6% to 3.6%, yet it pushed the score down at -0.125. Loans 30-89 days past due were 0.3% of assets, below their prior range of 0.4% to 0.8%, and pushed the score down at -0.619. Construction loans were 0.0% of loans, below their prior range of 0.2% to 2.0%, and pushed the score down at -0.224.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | 109.7% | 125.6% to 175.8% | prior 12 quarters | -16.3 pp | -27.1 pp | +0.604 | pushed the score up |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.4% | 0.9% to 3.7% | same quarter, prior 3 years | n/a | -0.5 pp | -0.012 | little effect on the score |
| net interest margin (the spread earned on lending and investing) | 3.8% | 2.6% to 3.6% | same quarter, prior 3 years | n/a | +0.2 pp | -0.125 | pushed the score down |
| loans 30-89 days past due, as a share of assets | 0.3% | 0.4% to 0.8% | prior 12 quarters | -0.2 pp | -0.1 pp | -0.619 | pushed the score down |
| construction loans as a share of loans | 0.0% | 0.2% to 2.0% | prior 12 quarters | -0.2 pp | -0.4 pp | -0.224 | pushed the score down |
| nonaccrual assets and foreclosed property, as a share of assets | 3.4% | 3.9% to 8.4% | prior 12 quarters | -0.5 pp | -1.2 pp | +0.020 | little effect on the score |

12 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## How early Canary caught it

In hindsight, Canary first flagged Guaranty Bank in the quarter ending 2016-06-30, a lead time of 4 quarters before it failed on 2017-05-05. At that first flag, the main factors pushing the score up were the Tier 1 risk-based capital ratio at 3.3% (+1.814), the Texas ratio at 125.6% (+1.083), and the total risk-based capital ratio at 4.5% (+0.426). The largest factors pulling it down then were interest expense at 0.0% of assets (-1.043) and return on equity at -9.9% (-0.778).

## What happened next

In hindsight, the last quarter Guaranty Bank reported was 2017-03-31, the same quarter as this memo. The bank failed on May 5, 2017, so no later ranks or flags exist for it.

## Sources

- F3 · As-of quarter · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WI · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2017-03-31 · 33 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2017-03-31 · 5,925 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2017-03-31 · 99.5% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2017-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2017-03-31 · 119 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2017-03-31 · 2.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2017-03-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · 2.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2017-03-31 · 3.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2017-03-31 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2017-03-31 · 4.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2017-03-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 4.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 3.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 109.7% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 4.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2017-03-31 · 93.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2017-03-31 · 69.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2017-03-31 · 1.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2017-03-31 · 17.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2017-03-31 · 97.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2017-03-31 · 79.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2017-03-31 · 14.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2017-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2017-03-31 · -0.2% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2017-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2017-03-31 · 0.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2017-03-31 · 0.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 3.1%; contribution to the score · 2017-03-31 · +1.350 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 109.7%; contribution to the score · 2017-03-31 · +0.604 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: the total risk-based capital ratio, value 4.4%; contribution to the score · 2017-03-31 · +0.518 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F78 · Driver up #4: core deposits as a share of assets, value 97.0%; contribution to the score · 2017-03-31 · +0.318 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F79 · Driver up #5: commercial real estate loans as a share of loans, value 0.2%; contribution to the score · 2017-03-31 · +0.281 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.0%; contribution to the score · 2017-03-31 · -1.410 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 21.5%; contribution to the score · 2017-03-31 · -0.861 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: loans 30-89 days past due, as a share of assets, value 0.3%; contribution to the score · 2017-03-31 · -0.619 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F83 · Driver down #4: return on assets (profit as a share of assets), value 0.4%; contribution to the score · 2017-03-31 · -0.558 · data/analyst/scores.parquet: feature return_on_assets contribution
- F84 · Driver down #5: total assets, value $1.0 billion; contribution to the score · 2017-03-31 · -0.340 · data/analyst/scores.parquet: feature log_total_assets contribution
- F85 · Failure date · 2017-05-05 · 2017-05-05 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-06-30 · 2016-06-30 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2016-06-30: the Tier 1 risk-based capital ratio, value 3.3%; contribution to the score · 2016-06-30 · +1.814 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2016-06-30: the Texas ratio (troubled assets against capital plus reserves), value 125.6%; contribution to the score · 2016-06-30 · +1.083 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2016-06-30: the total risk-based capital ratio, value 4.5%; contribution to the score · 2016-06-30 · +0.426 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F93 · Driver down #1 at 2016-06-30: annualized interest expense as a share of assets, value 0.0%; contribution to the score · 2016-06-30 · -1.043 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F94 · Driver down #2 at 2016-06-30: return on equity (profit as a share of equity), value -9.9%; contribution to the score · 2016-06-30 · -0.778 · data/analyst/scores.parquet: feature return_on_equity contribution
- F98 · Last quarter the bank reported · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2017-03-31 · 109.7% · data/features/fct_bank_features.parquet: texas_ratio
- F100 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 125.6% · data/features/fct_bank_features.parquet: texas_ratio
- F101 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 175.8% · data/features/fct_bank_features.parquet: texas_ratio
- F102 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2017-03-31 · -16.3 pp · data/features/fct_bank_features.parquet: texas_ratio
- F103 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over four quarters, in percentage points · 2017-03-31 · -27.1 pp · data/features/fct_bank_features.parquet: texas_ratio
- F104 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2017-03-31 · +0.604 · data/analyst/scores.parquet: feature texas_ratio contribution
- F105 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2017-03-31 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F106 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2017-03-31 · 0.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F107 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F108 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 3.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F110 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2017-03-31 · -0.012 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F111 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2017-03-31 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F112 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2017-03-31 · 3.8% · data/features/fct_bank_features.parquet: net_interest_margin
- F113 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 2.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F114 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 3.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F116 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2017-03-31 · -0.125 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F117 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2017-03-31 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F118 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2017-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F119 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F120 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F123 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2017-03-31 · -0.619 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F124 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2017-03-31 · pushed the score down · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F125 · Trend: construction loans as a share of loans, value at the as-of quarter · 2017-03-31 · 0.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F126 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 0.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F127 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 2.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F130 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2017-03-31 · -0.224 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F131 · Trend: construction loans as a share of loans, what the model did with it · 2017-03-31 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F132 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2017-03-31 · 3.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F133 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 3.9% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F134 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 8.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F137 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2017-03-31 · +0.020 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F138 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2017-03-31 · little effect on the score · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F139 · Trend: ratios outside their own prior range · 2017-03-31 · 12 · data/features/fct_bank_features.parquet
- F140 · Trend: ratios shown in the table (the furthest outside their prior range) · 2017-03-31 · 6 · data/features/fct_bank_features.parquet
- F141 · Trend: ratios compared with their own prior range · 2017-03-31 · 30 · data/features/fct_bank_features.parquet
- F142 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F144 · Percentile a year earlier (100 = highest risk) · 2016-03-31 · 99.7% · data/analyst/scores.parquet: percentile
- F145 · Trend: how the model's rating compares with a year earlier · 2017-03-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
