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
written_at: "2026-11-19T14:05:15"
writer_model: "claude-opus-5-5"
checked: true
---

# Seaway Bank And Trust Company (cert 19328)

*Hindsight: failed 2017-01-27. Canary flagged it 4 quarters ahead.*

## Summary

As of 2016-12-31, Seaway Bank And Trust Company, based in IL, ranked 7 out of 5,983 banks on Canary's risk score, placing it in the 99.9th percentile, where higher means riskier. That put it on Canary's watchlist, which covers the top 2% of banks by score. Its capital, the owners' cushion that absorbs losses, had turned negative, with equity at -1.9% of assets against a national median of 10.7%. It was also losing money, with a return on assets of -7.2%, and 8.8% of its loans were seriously overdue or no longer paying interest, against a median of 0.6%.

## Warning signs in the data

Capital was the weakest area: equity was -1.9% of assets against a national median of 10.7%, and the leverage ratio (core capital as a share of average assets) was -1.8% against a median of 10.4%. The Tier 1 risk-based capital ratio, which measures core capital against assets weighted by their riskiness, stood at -3.1% against a median of 15.0%, and the total risk-based capital ratio was -1.8% against a median of 16.2%.

Credit quality, meaning how well borrowers were repaying, was also poor: loans 90+ days past due or not accruing interest made up 8.8% of loans against a median of 0.6%, and loans 30-89 days past due equaled 5.4% of assets against a median of 0.3%. Nonaccrual assets and foreclosed property were 4.1% of assets against a median of 0.5%, and net loan write-offs ran at 1.3% of loans against a median of 0.1%. Commercial real estate loans made up 42.2% of the loan book, well above the median of 22.5%, while the bank was losing money with a return on assets of -7.2% against a median of 0.9%.

On funding, borrowings from the Federal Home Loan Bank, a government-sponsored lender to banks, equaled 14.3% of assets against a median of 0.7%, and volatile funding (money that can leave quickly) was 17.7% against a median of 5.2%. The bank was shrinking, with assets down -19.5% and deposits down -12.3% over the past four quarters, while the medians grew 3.5% and 3.6%. Unrealized losses on bonds available for sale were modest at 1.7% of equity, somewhat above the median of 0.7%.

## Understanding the score

As of 2016-12-31, the bank ranked 7 out of 5,983 banks nationally, which is the 99.9th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks by score, or 120 banks that quarter.

The five factors that pushed the score up most were the Tier 1 risk-based capital ratio at -3.1% (contribution +1.908), return on equity, meaning profit as a share of the owners' stake, at -156.0% (+1.554), and the total risk-based capital ratio at -1.8% (+0.881). Next came the leverage ratio at -1.8% (+0.669) and loans 90+ days past due or not accruing interest at 8.8% of loans (+0.508).

The five factors that pulled the score down most were interest expense at 0.6% of assets (contribution -1.391) and the Texas ratio, which compares troubled assets with capital plus reserves, at -2563.3% (-1.043). The others were construction loans at 4.1% of loans (-0.199), total assets of $297.8 million (-0.162), and commercial real estate loans at 42.2% of loans (-0.099).

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

Canary compares each ratio with the bank's own history over the prior 12 quarters, or the same quarter in the prior 3 years for year-to-date ratios. As of 2016-12-31, when the bank ranked 7 out of 5,983, 16 of 30 ratios checked were outside their own prior range, and the table shows the 6 furthest out.

Return on equity fell to -156.0%, far below its prior range of -30.5% to 2.2%, and it pushed the score up with a contribution of +1.554 model log-odds units. The leverage ratio dropped to -1.8%, below its prior range of 1.9% to 9.4% after a fall of -7.5 pp over four quarters, and it pushed the score up with a contribution of +0.669. Return on assets reached -7.2%, below its prior range of -2.9% to 0.2%, and it pushed the score up with a contribution of +0.175.

The Texas ratio swung to -2563.3%, far outside its prior range of 90.3% to 192.6%, yet it pushed the score down with a contribution of -1.043. The efficiency ratio, operating costs as a share of revenue, rose to 249.2%, above its prior range of 88.0% to 169.8%, yet it had little effect on the score, with a contribution of -0.027. Net interest margin, the spread earned on lending and investing, slipped to 3.1%, below its prior range of 4.0% to 4.9%, yet it pushed the score down with a contribution of -0.054.

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

## Compared with similar banks

The FDIC's specialty group for this bank at 2016-12-31: Commercial Lending Specialization.

Peers: 2106 banks in the same specialty group and size tier ($100 million to $1 billion).

Its Tier 1 risk-based capital ratio of -3.1% was at the 0.0th percentile nationally, unusually low, and at the 0.1st percentile among peers against a peer median of 13.6%, unusually low among its peers too. Its total risk-based capital ratio of -1.8% was at the 0.0th percentile nationally, unusually low, and at the 0.1st percentile among peers against a peer median of 14.7%, unusually low among its peers too. Its leverage ratio of -1.8% was at the 0.0th percentile nationally, unusually low, and at the 0.1st percentile among peers against a peer median of 10.2%, unusually low among its peers too. Its equity of -1.9% of assets was at the 0.0th percentile nationally, unusually low, and at the 0.1st percentile among peers against a peer median of 10.3%, unusually low among its peers too.

Its return on equity of -156.0% was at the 0.0th percentile nationally, unusually low, and at the 0.1st percentile among peers against a peer median of 8.4%, unusually low among its peers too. Its return on assets of -7.2% was at the 0.1st percentile nationally, unusually low, and at the 0.1st percentile among peers against a peer median of 0.9%, unusually low among its peers too. Its efficiency ratio of 249.2% was at the 99.9th percentile nationally, unusually high, and at the 99.9th percentile among peers against a peer median of 70.1%, unusually high among its peers too. Its Texas ratio of -2563.3% was at the 0.0th percentile nationally, unusually low, and at the 0.0th percentile among peers against a peer median of 6.1%, unusually low among its peers too.

Overall, 20 of the bank's ratios sat in the national top or bottom 10%, and 19 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the Texas ratio (troubled assets against capital plus reserves) | -2563.3% | 0.0th (unusually low) | 6.1% | 0.0th | unusually low among its peers too |
| the total risk-based capital ratio | -1.8% | 0.0th (unusually low) | 14.7% | 0.1st | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | -3.1% | 0.0th (unusually low) | 13.6% | 0.1st | unusually low among its peers too |
| equity as a share of assets | -1.9% | 0.0th (unusually low) | 10.3% | 0.1st | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | -1.8% | 0.0th (unusually low) | 10.2% | 0.1st | unusually low among its peers too |
| return on equity (profit as a share of equity) | -156.0% | 0.0th (unusually low) | 8.4% | 0.1st | unusually low among its peers too |
| return on assets (profit as a share of assets) | -7.2% | 0.1st (unusually low) | 0.9% | 0.1st | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 249.2% | 99.9th (unusually high) | 70.1% | 99.9th | unusually high among its peers too |

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

In hindsight, the bank failed on 2017-01-27. Canary first flagged it in the quarter ending 2016-03-31, giving a lead time of 4 quarters before the failure.

At that first flag, the main factors pushing the score up were a Tier 1 risk-based capital ratio of 5.5% (contribution +1.369), a Texas ratio of 167.1% (+1.342) and return on equity of -63.1% (+1.324). Loans 90+ days past due or not accruing interest at 19.5% of loans (+0.741) and a total risk-based capital ratio of 6.8% (+0.472) also added to the score.

## What happened next

In hindsight, the last quarter the bank reported was 2016-12-31, the same quarter as this memo. The bank failed on 2017-01-27, less than a month later, so no later ranks are available.

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
- F35 · Bank: commercial real estate loans as a share of loans · 2016-12-31 · 42.2% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2016-12-31 · 22.5% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-12-31 · -7.2% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-12-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2016-12-31 · 14.3% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2016-12-31 · 0.7% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2016-12-31 · 17.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2016-12-31 · 5.2% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
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
- F92 · Driver up #5 at 2016-03-31: the total risk-based capital ratio, value 6.8%; contribution to the score · 2016-03-31 · +0.472 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
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
- F138 · Trend: ratios shown in the table (the furthest outside their prior range) · 2016-12-31 · 6 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios compared with their own prior range · 2016-12-31 · 30 · data/features/fct_bank_features.parquet
- F140 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F145 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2016-12-31 · -2563.3% · data/features/fct_bank_features.parquet: texas_ratio
- F146 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2016-12-31 · 0.0th · data/features/fct_bank_features.parquet: texas_ratio
- F147 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: texas_ratio
- F148 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2016-12-31 · 0.0th · data/features/fct_bank_features.parquet: texas_ratio
- F149 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2016-12-31 · 6.1% · data/features/fct_bank_features.parquet: texas_ratio
- F150 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F151 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2016-12-31 · -1.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F152 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2016-12-31 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F153 · Peers: the total risk-based capital ratio, national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F154 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F155 · Peers: the total risk-based capital ratio, peer median · 2016-12-31 · 14.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F156 · Peers: the total risk-based capital ratio, reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F157 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2016-12-31 · -3.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F158 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2016-12-31 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F159 · Peers: the Tier 1 risk-based capital ratio, national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F160 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F161 · Peers: the Tier 1 risk-based capital ratio, peer median · 2016-12-31 · 13.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F162 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F163 · Peers: equity as a share of assets, bank value at the as-of quarter · 2016-12-31 · -1.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F164 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2016-12-31 · 0.0th · data/features/fct_bank_features.parquet: equity_to_assets
- F165 · Peers: equity as a share of assets, national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F166 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: equity_to_assets
- F167 · Peers: equity as a share of assets, peer median · 2016-12-31 · 10.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F168 · Peers: equity as a share of assets, reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F169 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2016-12-31 · -1.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F170 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2016-12-31 · 0.0th · data/features/fct_bank_features.parquet: leverage_ratio
- F171 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F172 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: leverage_ratio
- F173 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2016-12-31 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F174 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F175 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2016-12-31 · -156.0% · data/features/fct_bank_features.parquet: return_on_equity
- F176 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2016-12-31 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F177 · Peers: return on equity (profit as a share of equity), national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F178 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F179 · Peers: return on equity (profit as a share of equity), peer median · 2016-12-31 · 8.4% · data/features/fct_bank_features.parquet: return_on_equity
- F180 · Peers: return on equity (profit as a share of equity), reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F181 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2016-12-31 · -7.2% · data/features/fct_bank_features.parquet: return_on_assets
- F182 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: return_on_assets
- F183 · Peers: return on assets (profit as a share of assets), national reading · 2016-12-31 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F184 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2016-12-31 · 0.1st · data/features/fct_bank_features.parquet: return_on_assets
- F185 · Peers: return on assets (profit as a share of assets), peer median · 2016-12-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F186 · Peers: return on assets (profit as a share of assets), reading against its peers · 2016-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F187 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2016-12-31 · 249.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F188 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2016-12-31 · 99.9th · data/features/fct_bank_features.parquet: efficiency_ratio
- F189 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2016-12-31 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F190 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2016-12-31 · 99.9th · data/features/fct_bank_features.parquet: efficiency_ratio
- F191 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2016-12-31 · 70.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F192 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2016-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F194 · Peers: ratios in the national top or bottom 10% · 2016-12-31 · 20 · data/features/fct_bank_features.parquet
- F195 · Peers: those ratios also unusual among peers · 2016-12-31 · 19 · data/features/fct_bank_features.parquet
- F197 · Peers: cut-off for unusual (top or bottom share of banks) · 2016-12-31 · 10% · data/features/fct_bank_features.parquet
