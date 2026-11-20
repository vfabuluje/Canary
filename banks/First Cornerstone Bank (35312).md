---
cert: 35312
name: "First Cornerstone Bank"
as_of: 2016-03-31
rank: 2
n_banks: 6193
percentile: 99.98385273696108
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2016-05-06
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:14:38"
writer_model: "claude-opus-5-5"
checked: true
---

# First Cornerstone Bank (cert 35312)

*Hindsight: failed 2016-05-06. Canary flagged it 1 quarter ahead.*

## Summary

As of 2016-03-31, Canary ranked First Cornerstone Bank, a Pennsylvania (PA) bank, 2 out of 6,193 banks nationally, placing it in the 100.0th percentile, where higher means riskier. It was flagged on Canary's watchlist, one of 124 banks that quarter. Its equity, the owners' stake that absorbs losses, was 2.0% of assets against a national median of 10.9%, and it was losing money, with a return on assets of -4.4% against a median of 0.9%. In contrast, its funding looked steady, with core deposits, the most stable kind of funding, at 96.9% of assets.

## Warning signs in the data

Capital, the cushion that absorbs losses, was very thin: equity was 2.0% of assets against a national median of 10.9%, and the leverage ratio (core capital as a share of average assets) was 2.0% against 10.4%. The risk-based measures, which weigh assets by how risky they are, were also far below normal: the Tier 1 ratio was 3.9% against a median of 15.2%, and the total ratio was 5.1% against 16.4%. The bank was also unprofitable, with return on assets of -4.4% against a national median of 0.9%, and its total assets shrank by -10.0% over the past four quarters while the median bank grew 3.0%.

Credit quality was weak: loans 90+ days past due or not accruing interest were 8.1% of loans against a national median of 0.7%, and nonaccrual assets plus foreclosed property were 7.8% of assets against 0.6%. Loans 30-89 days past due, an early sign of borrowers falling behind, were 5.4% of assets against a median of 0.3%. The Texas ratio, which compares troubled assets with capital plus reserves, stood at 299.1% against a national median of 5.5%, while loan-loss reserves were 1.9% of loans, somewhat above the 1.3% median. Commercial real estate loans made up 54.9% of loans, well above the 22.6% median, though the concentration section found the bank did not cross either of the supervisory screening lines.

Liquidity and funding point the other way: core deposits were 96.9% of assets against a median of 78.9%, and cash was 37.8% of assets against 7.0%. Uninsured deposits (balances above the insurance limit) were 9.5% of deposits against a median of 16.6%, brokered deposits were 0.0% against 0.0%, and volatile funding was 0.9% of assets against 4.9%. Bond losses were small: losses on bonds available for sale were -0.3% of equity against a median of -0.9%, and losses on bonds held to maturity were 0.0% against 0.0%. So the bank's funding looked stable while its capital, credit quality and earnings looked severely strained; these signals point in different directions and should be read separately.

## Understanding the score

As of 2016-03-31, First Cornerstone Bank ranked 2 out of 6,193 banks, in the 100.0th percentile on a 0 to 100 scale where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks and held 124 banks that quarter.

The five features that pushed the score up most were the Tier 1 risk-based capital ratio at 3.9% (+2.057), the Texas ratio at 299.1% (+1.339), return on equity at -180.8% (+1.280), the total risk-based capital ratio at 5.1% (+0.446), and loans 90+ days past due or not accruing interest at 8.1% of loans (+0.438).

The five that pulled it down most were interest expense at 0.8% of assets (-0.850), commercial real estate loans at 54.9% of loans (-0.399), volatile funding at 0.9% of assets (-0.242), construction loans at 3.0% of loans (-0.156), and losses on bonds available for sale at -0.3% of equity (-0.099).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 2 | 6,193 | ▲ watchlist (first flag) |

## How its ratios moved

As of 2016-03-31, the model ranked First Cornerstone Bank 2 out of 6,193 banks nationally, which places it in the 100.0th percentile, where higher means riskier. Each ratio is compared with the bank's own prior range, usually over the prior 12 quarters, or for year-to-date ratios over the same quarter in the prior 3 years. On that basis, 16 of the 30 ratios checked sat outside their own prior range.

Return on equity (profit as a share of the owners' stake) was -180.8%, far below its prior range of -62.5% to -32.2%, and its contribution of +1.280 model log-odds units (the model's internal scoring units) pushed the score up. Loans 30-89 days past due reached 5.4% of assets, above their prior range of 0.4% to 3.3%, after rising +2.5 pp in one quarter, and their contribution of +0.312 pushed the score up. Return on assets (profit as a share of everything the bank owns) was -4.4%, below its prior range of -3.4% to -1.9%, and its contribution of +0.201 pushed the score up.

The efficiency ratio (operating costs as a share of revenue) jumped to 503.1%, well above its prior range of 158.2% to 254.0%, yet its contribution of -0.031 had little effect on the score. Uninsured deposits (balances above the government insurance limit) rose to 9.5% of deposits, above their prior range of 5.9% to 8.3%, but their contribution of -0.092 pushed the score down. Net loan write-offs (loans recorded as losses, minus recoveries) were 0.5% of loans, above a prior range of 0.0% to 0.0%, but their contribution of +0.018 had little effect on the score.

There is no score from a year earlier to compare with (scores start 2016-03-31, or the bank did not report then).

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -180.8% | -62.5% to -32.2% | same quarter, prior 3 years | n/a | -118.3 pp | +1.280 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 503.1% | 158.2% to 254.0% | same quarter, prior 3 years | n/a | +249.2 pp | -0.031 | little effect on the score |
| loans 30-89 days past due, as a share of assets | 5.4% | 0.4% to 3.3% | prior 12 quarters | +2.5 pp | +2.1 pp | +0.312 | pushed the score up |
| return on assets (profit as a share of assets) | -4.4% | -3.4% to -1.9% | same quarter, prior 3 years | n/a | -1.0 pp | +0.201 | pushed the score up |
| uninsured deposits as a share of deposits | 9.5% | 5.9% to 8.3% | prior 12 quarters | +1.2 pp | +3.1 pp | -0.092 | pushed the score down |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.5% | 0.0% to 0.0% | same quarter, prior 3 years | n/a | +0.5 pp | +0.018 | little effect on the score |

16 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2016-03-31: Commercial Lending Specialization.

Peers: 2114 banks in the same specialty group and size tier ($100 million to $1 billion).

Core deposits, the bank's most stable kind of funding, made up 96.9% of assets, the 100.0th percentile nationally, which is unusually high; among its peers it sat at the 100.0th percentile against a peer median of 78.4%, unusually high among its peers too. Return on equity, the profit earned as a share of the owners' stake, was -180.8%, the 0.0th percentile nationally and unusually low; it sat at the 0.1st percentile among peers, whose median was 7.8%, unusually low among its peers too. The efficiency ratio, operating costs as a share of revenue, was 503.1%, the 99.9th percentile nationally and unusually high; it sat at the 99.9th percentile among peers against a peer median of 71.1%, unusually high among its peers too. Loans 30-89 days past due, meaning borrowers behind on payments but not yet in default, equalled 5.4% of assets, the 99.8th percentile nationally and unusually high; it sat at the 99.8th percentile among peers against a peer median of 0.3%, unusually high among its peers too.

The Texas ratio, which weighs troubled assets against capital plus reserves, was 299.1%, the 99.9th percentile nationally and unusually high; it sat at the 99.8th percentile among peers against a peer median of 7.2%, unusually high among its peers too. The Tier 1 risk-based capital ratio, core capital measured against assets adjusted for their riskiness, was 3.9%, the 0.2nd percentile nationally and unusually low; it sat at the 0.2nd percentile among peers against a peer median of 13.8%, unusually low among its peers too. The total risk-based capital ratio, a broader version of the same capital cushion, was 5.1%, the 0.2nd percentile nationally and unusually low; it sat at the 0.3rd percentile among peers against a peer median of 15.0%, unusually low among its peers too. Equity, the owners' stake, was 2.0% of assets, the 0.3rd percentile nationally and unusually low; it sat at the 0.1st percentile among peers against a peer median of 10.5%, unusually low among its peers too.

Canary ranked the bank 2 out of 6,193 banks that quarter, the 100.0th percentile on a scale where higher means a higher score. Overall, 19 of the bank's ratios fell in the national top or bottom 10%, and 19 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| core deposits as a share of assets | 96.9% | 100.0th (unusually high) | 78.4% | 100.0th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -180.8% | 0.0th (unusually low) | 7.8% | 0.1st | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 503.1% | 99.9th (unusually high) | 71.1% | 99.9th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 299.1% | 99.9th (unusually high) | 7.2% | 99.8th | unusually high among its peers too |
| the Tier 1 risk-based capital ratio | 3.9% | 0.2nd (unusually low) | 13.8% | 0.2nd | unusually low among its peers too |
| loans 30-89 days past due, as a share of assets | 5.4% | 99.8th (unusually high) | 0.3% | 99.8th | unusually high among its peers too |
| the total risk-based capital ratio | 5.1% | 0.2nd (unusually low) | 15.0% | 0.3rd | unusually low among its peers too |
| equity as a share of assets | 2.0% | 0.3rd (unusually low) | 10.5% | 0.1st | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: total risk-based capital, as the 2006 guidance specifies.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 53.7% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 142.0% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -63.2% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, Canary first flagged First Cornerstone Bank in the quarter ending 2016-03-31, when it ranked 2 out of 6,193 banks. The bank failed on 2016-05-06, giving a lead time of 1 quarter between the first flag and the failure. That quarter was also the last one the bank reported, so the flag came on its final available data.

## What happened next

In hindsight, the bank failed on May 6, 2016. Its last reported quarter was 2016-03-31, so there are no later ranks or flags for it in Canary's data.

## Sources

- F1 · Bank name · n/a · First Cornerstone Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2016-03-31 · 2016-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · PA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2016-03-31 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2016-03-31 · 6,193 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2016-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2016-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2016-03-31 · 124 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2016-03-31 · 2.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2016-03-31 · 10.9% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2016-03-31 · 2.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2016-03-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2016-03-31 · 3.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2016-03-31 · 15.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2016-03-31 · 5.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2016-03-31 · 16.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2016-03-31 · 8.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2016-03-31 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2016-03-31 · 7.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2016-03-31 · 0.6% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2016-03-31 · 5.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2016-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2016-03-31 · 1.9% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2016-03-31 · 1.3% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F35 · Bank: commercial real estate loans as a share of loans · 2016-03-31 · 54.9% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F36 · National median: commercial real estate loans as a share of loans · 2016-03-31 · 22.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2016-03-31 · 299.1% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2016-03-31 · 5.5% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2016-03-31 · -4.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2016-03-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2016-03-31 · 9.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2016-03-31 · 16.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2016-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2016-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2016-03-31 · 96.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2016-03-31 · 78.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2016-03-31 · 0.9% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2016-03-31 · 4.9% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2016-03-31 · 37.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2016-03-31 · 7.0% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2016-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2016-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2016-03-31 · -0.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2016-03-31 · -0.9% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F71 · Bank: asset growth over the past four quarters · 2016-03-31 · -10.0% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2016-03-31 · 3.0% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 3.9%; contribution to the score · 2016-03-31 · +2.057 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 299.1%; contribution to the score · 2016-03-31 · +1.339 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: return on equity (profit as a share of equity), value -180.8%; contribution to the score · 2016-03-31 · +1.280 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 5.1%; contribution to the score · 2016-03-31 · +0.446 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: loans 90+ days past due or not accruing interest, as a share of loans, value 8.1%; contribution to the score · 2016-03-31 · +0.438 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 0.8%; contribution to the score · 2016-03-31 · -0.850 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: commercial real estate loans as a share of loans, value 54.9%; contribution to the score · 2016-03-31 · -0.399 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F82 · Driver down #3: volatile funding as a share of assets, value 0.9%; contribution to the score · 2016-03-31 · -0.242 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F83 · Driver down #4: construction loans as a share of loans, value 3.0%; contribution to the score · 2016-03-31 · -0.156 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F84 · Driver down #5: losses on bonds available for sale, as a share of equity, value -0.3%; contribution to the score · 2016-03-31 · -0.099 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F85 · Failure date · 2016-05-06 · 2016-05-06 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2016-03-31 · 2016-03-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 1 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Last quarter the bank reported · 2016-03-31 · 2016-03-31 · data/features/fct_bank_features.parquet: report_date
- F89 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2016-03-31 · -180.8% · data/features/fct_bank_features.parquet: return_on_equity
- F90 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -62.5% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -32.2% · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2016-03-31 · +1.280 · data/analyst/scores.parquet: feature return_on_equity contribution
- F94 · Trend: return on equity (profit as a share of equity), what the model did with it · 2016-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2016-03-31 · 503.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F96 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 158.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 254.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2016-03-31 · -0.031 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F100 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2016-03-31 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F101 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2016-03-31 · 5.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F102 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F103 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 3.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F104 · Trend: loans 30-89 days past due, as a share of assets, change over one quarter, in percentage points · 2016-03-31 · +2.5 pp · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F106 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2016-03-31 · +0.312 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F107 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2016-03-31 · pushed the score up · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F108 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2016-03-31 · -4.4% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -3.4% · data/features/fct_bank_features.parquet: return_on_assets
- F110 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -1.9% · data/features/fct_bank_features.parquet: return_on_assets
- F112 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2016-03-31 · +0.201 · data/analyst/scores.parquet: feature return_on_assets contribution
- F113 · Trend: return on assets (profit as a share of assets), what the model did with it · 2016-03-31 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F114 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2016-03-31 · 9.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F115 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 5.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F116 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 8.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F119 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2016-03-31 · -0.092 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F120 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2016-03-31 · pushed the score down · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F121 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2016-03-31 · 0.5% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F122 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F123 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F125 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2016-03-31 · +0.018 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F126 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2016-03-31 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F127 · Trend: ratios outside their own prior range · 2016-03-31 · 16 · data/features/fct_bank_features.parquet
- F129 · Trend: ratios compared with their own prior range · 2016-03-31 · 30 · data/features/fct_bank_features.parquet
- F130 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F131 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F135 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2016-03-31 · 96.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F136 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2016-03-31 · 100.0th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F137 · Peers: core deposits as a share of assets, national reading · 2016-03-31 · unusually high · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F138 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2016-03-31 · 100.0th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F139 · Peers: core deposits as a share of assets, peer median · 2016-03-31 · 78.4% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F140 · Peers: core deposits as a share of assets, reading against its peers · 2016-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F141 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2016-03-31 · -180.8% · data/features/fct_bank_features.parquet: return_on_equity
- F142 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2016-03-31 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F143 · Peers: return on equity (profit as a share of equity), national reading · 2016-03-31 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F144 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2016-03-31 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F145 · Peers: return on equity (profit as a share of equity), peer median · 2016-03-31 · 7.8% · data/features/fct_bank_features.parquet: return_on_equity
- F146 · Peers: return on equity (profit as a share of equity), reading against its peers · 2016-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F147 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2016-03-31 · 503.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F148 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2016-03-31 · 99.9th · data/features/fct_bank_features.parquet: efficiency_ratio
- F149 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2016-03-31 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F150 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2016-03-31 · 99.9th · data/features/fct_bank_features.parquet: efficiency_ratio
- F151 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2016-03-31 · 71.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F152 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2016-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F153 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2016-03-31 · 299.1% · data/features/fct_bank_features.parquet: texas_ratio
- F154 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2016-03-31 · 99.9th · data/features/fct_bank_features.parquet: texas_ratio
- F155 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2016-03-31 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F156 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2016-03-31 · 99.8th · data/features/fct_bank_features.parquet: texas_ratio
- F157 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2016-03-31 · 7.2% · data/features/fct_bank_features.parquet: texas_ratio
- F158 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2016-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F159 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2016-03-31 · 3.9% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F160 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2016-03-31 · 0.2nd · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F161 · Peers: the Tier 1 risk-based capital ratio, national reading · 2016-03-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F162 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2016-03-31 · 0.2nd · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F163 · Peers: the Tier 1 risk-based capital ratio, peer median · 2016-03-31 · 13.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F164 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2016-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F165 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2016-03-31 · 5.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F166 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2016-03-31 · 99.8th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F167 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2016-03-31 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F168 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2016-03-31 · 99.8th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F169 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2016-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F170 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2016-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F171 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2016-03-31 · 5.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F172 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2016-03-31 · 0.2nd · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F173 · Peers: the total risk-based capital ratio, national reading · 2016-03-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F174 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2016-03-31 · 0.3rd · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F175 · Peers: the total risk-based capital ratio, peer median · 2016-03-31 · 15.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F176 · Peers: the total risk-based capital ratio, reading against its peers · 2016-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F177 · Peers: equity as a share of assets, bank value at the as-of quarter · 2016-03-31 · 2.0% · data/features/fct_bank_features.parquet: equity_to_assets
- F178 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2016-03-31 · 0.3rd · data/features/fct_bank_features.parquet: equity_to_assets
- F179 · Peers: equity as a share of assets, national reading · 2016-03-31 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F180 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2016-03-31 · 0.1st · data/features/fct_bank_features.parquet: equity_to_assets
- F181 · Peers: equity as a share of assets, peer median · 2016-03-31 · 10.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F182 · Peers: equity as a share of assets, reading against its peers · 2016-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F184 · Peers: ratios in the national top or bottom 10% · 2016-03-31 · 19 · data/features/fct_bank_features.parquet
- F185 · Peers: those ratios also unusual among peers · 2016-03-31 · 19 · data/features/fct_bank_features.parquet
- F187 · Peers: cut-off for unusual (top or bottom share of banks) · 2016-03-31 · 10% · data/features/fct_bank_features.parquet
