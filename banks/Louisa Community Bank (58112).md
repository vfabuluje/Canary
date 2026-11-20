---
cert: 58112
name: "Louisa Community Bank"
as_of: 2019-09-30
rank: 1
n_banks: 5325
percentile: 100.0
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2019-10-25
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:15:01"
writer_model: "claude-opus-5-5"
checked: true
---

# Louisa Community Bank (cert 58112)

*Hindsight: failed 2019-10-25. Canary flagged it 4 quarters ahead.*

## Summary

As of 2019-09-30, Louisa Community Bank, a small bank in KY with total assets of $28.2 million, ranked 1 out of 5,325 FDIC-insured banks on Canary's risk score, the 100.0th percentile, the very top of the national list. Its capital cushion was very thin, with a leverage ratio (core capital as a share of average assets) of 1.2% against a national median of 11.0%. It also carried a heavy load of troubled loans and was losing money, with a return on assets (profit as a share of everything it owns) of -6.4% against a national median of 1.1%. It was one of 107 banks on Canary's watchlist that quarter.

## Warning signs in the data

Capital, the owners' stake that absorbs losses, was far below normal levels. Equity was 3.9% of assets against a national median of 11.6%, and the leverage ratio (core capital as a share of average assets) was 1.2% against a median of 11.0%. The risk-based measures, which weigh assets by how risky they are, were just as weak: the Tier 1 ratio was 1.5% against a median of 15.6%, and the total risk-based capital ratio was 2.8% against a median of 16.7%.

Credit quality was poor by any measure. Loans 90+ days past due or no longer earning interest were 11.9% of loans against a national median of 0.6%, and nonaccrual assets plus foreclosed property were 11.2% of assets against a median of 0.4%. Loans 30-89 days past due, an early sign of trouble, were 4.8% of assets against a median of 0.3%. The Texas ratio (troubled assets against capital plus reserves) stood at 173.6%, far above the national median of 3.7%. The bank was setting aside money for bad loans at a high rate, with provisions of 2.7% of assets against a median of 0.1%, and net write-offs (loans recorded as lost, minus recoveries) of 1.7% of loans against a median of 0.0%. Costs also swamped revenue, with an efficiency ratio (operating costs as a share of revenue) of 226.9% against a median of 66.8%.

On funding, the bank leaned more than most on less stable sources: brokered deposits (money placed through middlemen) were 10.2% of deposits against a national median of 0.0%, and volatile funding was 24.7% of assets against a median of 6.1%. It also shrank, with assets down -15.9% and deposits down -11.3% over the past four quarters, while the national medians grew 4.7% and 4.4%. Uninsured deposits were lower than typical, at 11.6% of deposits against a median of 19.0%. Bond losses were not a concern: unrealized losses on bonds held to maturity were 0.0% of equity, matching the median of 0.0%, and on bonds available for sale they were 0.5% against a median of -0.8%, with securities only 2.4% of assets against a median of 15.4%.

## Understanding the score

On 2019-09-30 the bank ranked 1 out of 5,325 banks, the 100.0th percentile on a scale of 0 to 100 where higher means riskier, with a raw model score of 0.9978. That placed it on Canary's watchlist, which covers the top 2% of banks, alongside 107 banks that quarter.

The five features pushing the score up most were the Tier 1 risk-based capital ratio at 1.5%, contributing +1.956; return on equity (profit as a share of equity) at -107.3%, contributing +1.263; the Texas ratio at 173.6%, contributing +0.995; loans 90+ days past due or not accruing interest at 11.9% of loans, contributing +0.810; and the total risk-based capital ratio at 2.8%, contributing +0.557.

The five features pulling the score down were much smaller: interest expense at 1.4% of assets, contributing -0.281; construction loans at 4.6% of loans, contributing -0.210; deposit growth over the past four quarters at -11.3%, contributing -0.099; total assets of $28.2 million, contributing -0.065; and uninsured deposits at 11.6% of deposits, contributing -0.054.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2017-12-31 | 29 | 5,738 | ▲ watchlist |
| 2018-03-31 | 22 | 5,674 | ▲ watchlist |
| 2018-06-30 | 15 | 5,610 | ▲ watchlist |
| 2018-09-30 | 11 | 5,544 | ▲ watchlist |
| 2018-12-31 | 7 | 5,473 | ▲ watchlist (first flag) |
| 2019-03-31 | 4 | 5,428 | ▲ watchlist |
| 2019-06-30 | 1 | 5,369 | ▲ watchlist |
| 2019-09-30 | 1 | 5,325 | ▲ watchlist |

## How its ratios moved

As of 2019-09-30, Louisa Community Bank ranked 1 out of 5,325 banks, the 100.0th percentile, which puts it at the very top of the national list. A year earlier, on 2018-09-30, it sat at the 99.8th percentile, so the model's rating is about the same as a year earlier. Each ratio is compared with its own prior range, usually the prior 12 quarters, and 16 of the 30 ratios checked sat outside that range.

Return on equity (profit as a share of the owners' stake) was -107.3%, far below its prior range of -26.0% to -4.7% after a change of -81.3 pp over four quarters, and its contribution of +1.263 model log-odds units pushed the score up. Return on assets (profit as a share of everything the bank owns) was -6.4%, below its prior range of -2.6% to -0.7%, and its contribution of +0.132 pushed the score up. The provision for loan losses (money set aside for loans expected to go bad) was 2.7% of assets, above its prior range of 0.4% to 1.1%, and its contribution of +0.142 pushed the score up.

The efficiency ratio (operating costs as a share of revenue) was 226.9%, well above its prior range of 107.3% to 155.4%, yet its contribution of -0.046 had little effect on the score. Net interest margin (the spread earned on lending and investing) was 2.9%, below its prior range of 3.9% to 4.3%, but its contribution of +0.022 had little effect on the score. Net loan write-offs (loans recorded as lost, minus recoveries) were 1.7% of loans, above their prior range of 0.3% to 0.9%, yet their contribution of -0.012 had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | -107.3% | -26.0% to -4.7% | same quarter, prior 3 years | n/a | -81.3 pp | +1.263 | pushed the score up |
| return on assets (profit as a share of assets) | -6.4% | -2.6% to -0.7% | same quarter, prior 3 years | n/a | -3.8 pp | +0.132 | pushed the score up |
| annualized provision for loan losses as a share of assets | 2.7% | 0.4% to 1.1% | same quarter, prior 3 years | n/a | +2.1 pp | +0.142 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 226.9% | 107.3% to 155.4% | same quarter, prior 3 years | n/a | +71.5 pp | -0.046 | little effect on the score |
| net interest margin (the spread earned on lending and investing) | 2.9% | 3.9% to 4.3% | same quarter, prior 3 years | n/a | -1.0 pp | +0.022 | little effect on the score |
| annualized loan write-offs, net of recoveries, as a share of loans | 1.7% | 0.3% to 0.9% | same quarter, prior 3 years | n/a | +0.9 pp | -0.012 | little effect on the score |

16 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2019-09-30: Commercial Lending Specialization.

Peers: 238 banks in the same specialty group and size tier (under $100 million).

The bank's total risk-based capital ratio (its capital cushion measured against loans and other assets weighted by risk) was 2.8%, at the 0.0th national percentile, which is unusually low, and at the 0.6th percentile among peers against a peer median of 17.4%, so it was unusually low among its peers too. Its Tier 1 risk-based capital ratio (the same measure using only the highest-quality capital) was 1.5%, at the 0.0th national percentile, which is unusually low, and at the 0.6th percentile among peers against a peer median of 16.4%, so it was unusually low among its peers too. Its return on equity (profit as a share of equity) was -107.3%, at the 0.1st national percentile, which is unusually low, and at the 1.1st percentile among peers against a peer median of 6.5%, so it was unusually low among its peers too. Its return on assets (profit as a share of assets) was -6.4%, at the 0.2nd national percentile, which is unusually low, and at the 1.9th percentile among peers against a peer median of 0.8%, so it was unusually low among its peers too.

Its Texas ratio (troubled assets against capital plus reserves) was 173.6%, at the 99.9th national percentile, which is unusually high, and at the 99.8th percentile among peers against a peer median of 5.5%, so it was unusually high among its peers too. Nonaccrual assets (loans no longer earning interest) and foreclosed property made up 11.2% of assets, at the 99.8th national percentile, which is unusually high, and at the 99.4th percentile among peers against a peer median of 0.5%, so this was unusually high among its peers too. Loans 30-89 days past due equaled 4.8% of assets, at the 99.8th national percentile, which is unusually high, and at the 98.5th percentile among peers against a peer median of 0.4%, so this was unusually high among its peers too. Loans 90+ days past due or not accruing interest were 11.9% of loans, at the 99.7th national percentile, which is unusually high, and at the 99.4th percentile among peers against a peer median of 0.6%, so this was unusually high among its peers too. Overall, 20 of the bank's ratios fell in the national top or bottom 10%, and all 20 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the total risk-based capital ratio | 2.8% | 0.0th (unusually low) | 17.4% | 0.6th | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 1.5% | 0.0th (unusually low) | 16.4% | 0.6th | unusually low among its peers too |
| return on equity (profit as a share of equity) | -107.3% | 0.1st (unusually low) | 6.5% | 1.1st | unusually low among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 173.6% | 99.9th (unusually high) | 5.5% | 99.8th | unusually high among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 11.2% | 99.8th (unusually high) | 0.5% | 99.4th | unusually high among its peers too |
| return on assets (profit as a share of assets) | -6.4% | 0.2nd (unusually low) | 0.8% | 1.9th | unusually low among its peers too |
| loans 30-89 days past due, as a share of assets | 4.8% | 99.8th (unusually high) | 0.4% | 98.5th | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 11.9% | 99.7th (unusually high) | 0.6% | 99.4th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: total risk-based capital, as the 2006 guidance specifies.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 162.2% | 100% or more | yes |
| Total commercial real estate loans ÷ capital | 1,157.7% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | -47.6% | 50% or more | no |

It crossed the construction line (100% or more of capital).
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, the bank failed on 2019-10-25. Canary first flagged it in Q4 2018, at the quarter ending 2018-12-31, giving a lead time of 4 quarters before the failure.

At that first flag, the main drivers up were the Texas ratio at 139.0%, contributing +0.936; return on equity at -37.9%, contributing +0.859; and loans 90+ days past due or not accruing interest at 14.9% of loans, contributing +0.767. The Tier 1 risk-based capital ratio at 8.2%, contributing +0.543, and loans 30-89 days past due at 4.1% of assets, contributing +0.355, completed the list. So the credit problems and losses that dominated the later picture were already visible to the model well before capital fell to its lowest levels.

## What happened next

In hindsight, the last quarter the bank reported was 2019-09-30, the same quarter as this memo's data. It failed shortly after, on 2019-10-25, so there are no later ranks or flags to report.

## Sources

- F1 · Bank name · n/a · Louisa Community Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KY · data/raw/financials: STALP
- F5 · Model score · 2019-09-30 · 0.9978 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2019-09-30 · 1 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2019-09-30 · 5,325 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2019-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2019-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2019-09-30 · 107 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2019-09-30 · 3.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2019-09-30 · 11.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 1.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2019-09-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2019-09-30 · 1.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2019-09-30 · 15.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2019-09-30 · 2.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2019-09-30 · 16.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 11.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2019-09-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2019-09-30 · 11.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2019-09-30 · 0.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2019-09-30 · 4.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2019-09-30 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2019-09-30 · 1.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2019-09-30 · 2.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2019-09-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 173.6% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2019-09-30 · 3.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2019-09-30 · -6.4% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2019-09-30 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 226.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2019-09-30 · 66.8% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2019-09-30 · 11.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2019-09-30 · 19.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2019-09-30 · 10.2% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2019-09-30 · 24.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2019-09-30 · 6.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2019-09-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2019-09-30 · 0.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2019-09-30 · -0.8% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2019-09-30 · 2.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2019-09-30 · 15.4% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F69 · Bank: total assets · 2019-09-30 · $28.2 million · data/features/fct_bank_features.parquet: log_total_assets
- F71 · Bank: asset growth over the past four quarters · 2019-09-30 · -15.9% · data/features/fct_bank_features.parquet: asset_growth_4q
- F72 · National median: asset growth over the past four quarters · 2019-09-30 · 4.7% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2019-09-30 · -11.3% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2019-09-30 · 4.4% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 1.5%; contribution to the score · 2019-09-30 · +1.956 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: return on equity (profit as a share of equity), value -107.3%; contribution to the score · 2019-09-30 · +1.263 · data/analyst/scores.parquet: feature return_on_equity contribution
- F77 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 173.6%; contribution to the score · 2019-09-30 · +0.995 · data/analyst/scores.parquet: feature texas_ratio contribution
- F78 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 11.9%; contribution to the score · 2019-09-30 · +0.810 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 2.8%; contribution to the score · 2019-09-30 · +0.557 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: annualized interest expense as a share of assets, value 1.4%; contribution to the score · 2019-09-30 · -0.281 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F81 · Driver down #2: construction loans as a share of loans, value 4.6%; contribution to the score · 2019-09-30 · -0.210 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: deposit growth over the past four quarters, value -11.3%; contribution to the score · 2019-09-30 · -0.099 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F83 · Driver down #4: total assets, value $28.2 million; contribution to the score · 2019-09-30 · -0.065 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: uninsured deposits as a share of deposits, value 11.6%; contribution to the score · 2019-09-30 · -0.054 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F85 · Failure date · 2019-10-25 · 2019-10-25 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2018-12-31 · 2018-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2018-12-31: the Texas ratio (troubled assets against capital plus reserves), value 139.0%; contribution to the score · 2018-12-31 · +0.936 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Driver up #2 at 2018-12-31: return on equity (profit as a share of equity), value -37.9%; contribution to the score · 2018-12-31 · +0.859 · data/analyst/scores.parquet: feature return_on_equity contribution
- F90 · Driver up #3 at 2018-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 14.9%; contribution to the score · 2018-12-31 · +0.767 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F91 · Driver up #4 at 2018-12-31: the Tier 1 risk-based capital ratio, value 8.2%; contribution to the score · 2018-12-31 · +0.543 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F92 · Driver up #5 at 2018-12-31: loans 30-89 days past due, as a share of assets, value 4.1%; contribution to the score · 2018-12-31 · +0.355 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F98 · Last quarter the bank reported · 2019-09-30 · 2019-09-30 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2019-09-30 · -107.3% · data/features/fct_bank_features.parquet: return_on_equity
- F100 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -26.0% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -4.7% · data/features/fct_bank_features.parquet: return_on_equity
- F102 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2019-09-30 · -81.3 pp · data/features/fct_bank_features.parquet: return_on_equity
- F103 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2019-09-30 · +1.263 · data/analyst/scores.parquet: feature return_on_equity contribution
- F104 · Trend: return on equity (profit as a share of equity), what the model did with it · 2019-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F105 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2019-09-30 · -6.4% · data/features/fct_bank_features.parquet: return_on_assets
- F106 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -2.6% · data/features/fct_bank_features.parquet: return_on_assets
- F107 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -0.7% · data/features/fct_bank_features.parquet: return_on_assets
- F109 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2019-09-30 · +0.132 · data/analyst/scores.parquet: feature return_on_assets contribution
- F110 · Trend: return on assets (profit as a share of assets), what the model did with it · 2019-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_assets contribution
- F111 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2019-09-30 · 2.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F112 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F113 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F115 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2019-09-30 · +0.142 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F116 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2019-09-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F117 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2019-09-30 · 226.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F118 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 107.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F119 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 155.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F121 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2019-09-30 · -0.046 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F122 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2019-09-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F123 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2019-09-30 · 2.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F124 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F125 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 4.3% · data/features/fct_bank_features.parquet: net_interest_margin
- F127 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2019-09-30 · +0.022 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F128 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2019-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F129 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2019-09-30 · 1.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F130 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F131 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F133 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2019-09-30 · -0.012 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F134 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2019-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F135 · Trend: ratios outside their own prior range · 2019-09-30 · 16 · data/features/fct_bank_features.parquet
- F137 · Trend: ratios compared with their own prior range · 2019-09-30 · 30 · data/features/fct_bank_features.parquet
- F138 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F140 · Percentile a year earlier (100 = highest risk) · 2018-09-30 · 99.8% · data/analyst/scores.parquet: percentile
- F141 · Trend: how the model's rating compares with a year earlier · 2019-09-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F145 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2019-09-30 · 2.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F146 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2019-09-30 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F147 · Peers: the total risk-based capital ratio, national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F148 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2019-09-30 · 0.6th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F149 · Peers: the total risk-based capital ratio, peer median · 2019-09-30 · 17.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F150 · Peers: the total risk-based capital ratio, reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F151 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2019-09-30 · 1.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F152 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2019-09-30 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F153 · Peers: the Tier 1 risk-based capital ratio, national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F154 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2019-09-30 · 0.6th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F155 · Peers: the Tier 1 risk-based capital ratio, peer median · 2019-09-30 · 16.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F156 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F157 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2019-09-30 · -107.3% · data/features/fct_bank_features.parquet: return_on_equity
- F158 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2019-09-30 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F159 · Peers: return on equity (profit as a share of equity), national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F160 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2019-09-30 · 1.1st · data/features/fct_bank_features.parquet: return_on_equity
- F161 · Peers: return on equity (profit as a share of equity), peer median · 2019-09-30 · 6.5% · data/features/fct_bank_features.parquet: return_on_equity
- F162 · Peers: return on equity (profit as a share of equity), reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F163 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2019-09-30 · 173.6% · data/features/fct_bank_features.parquet: texas_ratio
- F164 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2019-09-30 · 99.9th · data/features/fct_bank_features.parquet: texas_ratio
- F165 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2019-09-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F166 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2019-09-30 · 99.8th · data/features/fct_bank_features.parquet: texas_ratio
- F167 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2019-09-30 · 5.5% · data/features/fct_bank_features.parquet: texas_ratio
- F168 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2019-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F169 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2019-09-30 · 11.2% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F170 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2019-09-30 · 99.8th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F171 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2019-09-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F172 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2019-09-30 · 99.4th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F173 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2019-09-30 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F174 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2019-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F175 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2019-09-30 · -6.4% · data/features/fct_bank_features.parquet: return_on_assets
- F176 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2019-09-30 · 0.2nd · data/features/fct_bank_features.parquet: return_on_assets
- F177 · Peers: return on assets (profit as a share of assets), national reading · 2019-09-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F178 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2019-09-30 · 1.9th · data/features/fct_bank_features.parquet: return_on_assets
- F179 · Peers: return on assets (profit as a share of assets), peer median · 2019-09-30 · 0.8% · data/features/fct_bank_features.parquet: return_on_assets
- F180 · Peers: return on assets (profit as a share of assets), reading against its peers · 2019-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_assets
- F181 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2019-09-30 · 4.8% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F182 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2019-09-30 · 99.8th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F183 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2019-09-30 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F184 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2019-09-30 · 98.5th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F185 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2019-09-30 · 0.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F186 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2019-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F187 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2019-09-30 · 11.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F188 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2019-09-30 · 99.7th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F189 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2019-09-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F190 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2019-09-30 · 99.4th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F191 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2019-09-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F192 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2019-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F194 · Peers: ratios in the national top or bottom 10% · 2019-09-30 · 20 · data/features/fct_bank_features.parquet
- F195 · Peers: those ratios also unusual among peers · 2019-09-30 · 20 · data/features/fct_bank_features.parquet
- F197 · Peers: cut-off for unusual (top or bottom share of banks) · 2019-09-30 · 10% · data/features/fct_bank_features.parquet
