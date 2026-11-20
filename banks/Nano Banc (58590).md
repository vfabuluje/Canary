---
cert: 58590
name: "Nano Banc"
as_of: 2026-06-30
rank: 3
n_banks: 4313
percentile: 99.95362856480408
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:16:01"
writer_model: "claude-opus-5-5"
checked: true
---

# Nano Banc (cert 58590)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Canary's model ranked Nano Banc, a California bank, 3 out of 4,313 FDIC-insured banks, placing it in the 100.0th percentile, where higher means riskier. That puts it on Canary's watchlist, which covers the riskiest 2% of banks. The biggest reasons are a Texas ratio (troubled assets measured against capital plus loss reserves) of 209.8% and loans 90+ days past due or not accruing interest equal to 25.7% of loans, both far above the national median. Its capital cushion is also thin, with a Tier 1 risk-based capital ratio of 7.8% against a national median of 14.6%.

## Warning signs in the data

Capital, the bank's own money that absorbs losses, is well below typical levels: equity was 5.3% of assets against a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 5.0% against 11.0%. Its Tier 1 risk-based capital ratio was 7.8% and its total risk-based capital ratio was 9.1%, against national medians of 14.6% and 15.8%.

Credit quality is the sharpest problem: loans 90+ days past due or not accruing interest were 25.7% of loans against a national median of 0.5%, and nonaccrual assets plus foreclosed property were 16.7% of assets against 0.3%. Loans 30-89 days past due, an early sign of trouble, were 5.6% of assets against a median of 0.2%, and the Texas ratio was 209.8% against 2.9%. The bank is recognizing these losses: net loan write-offs ran at an annualized 3.3% of loans against a median of 0.0%, provisions for loan losses at 3.9% of assets against 0.1%, and reserves for bad loans stood at 4.2% of loans against 1.2%. It was losing money, with return on assets of -0.5% against a median of 1.2% and return on equity of -10.9% against 11.6%, and its net interest margin (the spread earned on lending and investing) was 2.2% against 3.9%.

On funding, uninsured deposits (balances above the FDIC insurance limit) were 56.9% of deposits against a national median of 24.8%, brokered deposits (money placed through middlemen) were 22.8% against 0.0%, and deposits shrank -14.8% over the past four quarters against median growth of 4.2%. Pointing the other way, cash was 27.3% of assets against a median of 6.2%, and volatile funding was 4.3% of assets against 9.0%, which gives the bank more ready liquidity than most. Unrealized losses on bonds were not a concern: 2.4% of equity on bonds available for sale against a median of 5.6%, and 0.0% on bonds held to maturity, matching the median of 0.0%. The separate real-estate concentration check found that the bank did not cross either of the regulators' screening lines, so the stress here comes mainly from troubled loans and thin capital rather than a flagged real estate concentration.

## Understanding the score

Nano Banc ranked 3 out of 4,313 banks at 2026-06-30, in the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which holds the top 2% of banks and numbered 87 banks that quarter.

The five features that pushed the score up most were the Texas ratio at 209.8% with a contribution of +1.216, loans 90+ days past due or not accruing at 25.7% with +0.867, and the Tier 1 risk-based capital ratio at 7.8% with +0.575. Next came loans 30-89 days past due at 5.6% of assets with +0.378, and brokered deposits at 22.8% of deposits with +0.360.

The five features that pulled the score down most were return on equity at -10.9% with a contribution of -0.340, construction loans at 9.8% of loans with -0.328, and deposit growth over the past four quarters at -14.8% with -0.169. The last two were total assets of $736.2 million with -0.155, and volatile funding at 4.3% of assets with -0.077. Some of these downward pushes, such as negative profits and shrinking deposits, look counterintuitive, and they were small next to the upward pushes from bad loans and thin capital.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 258 | 4,589 |  |
| 2024-12-31 | 3,759 | 4,560 |  |
| 2025-03-31 | 1,943 | 4,536 |  |
| 2025-06-30 | 122 | 4,494 |  |
| 2025-09-30 | 4 | 4,452 | ▲ watchlist |
| 2025-12-31 | 3 | 4,411 | ▲ watchlist |
| 2026-03-31 | 5 | 4,353 | ▲ watchlist |
| 2026-06-30 | 3 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, the model ranked Nano Banc 3 out of 4,313 banks nationally, placing it in the 100.0th percentile, where higher means riskier. A year earlier, on 2025-06-30, it sat in the 97.3rd percentile, so the model rated it riskier than a year earlier. Each ratio is compared with its own prior range, which for most ratios covers the prior 12 quarters. Of the 30 ratios compared this way, 8 sat outside their own prior range at 2026-06-30. Each ratio's contribution is shown in model log-odds units, where a positive number pushes the score up and a negative one pushes it down.

The provision for loan losses (money set aside to cover expected bad loans) was an annualized 3.9% of assets, above its prior range of -0.1% to 1.4% and up +2.5 pp over four quarters, and it pushed the score up with a contribution of +0.167. Interest expense (what the bank pays to borrow money, including on deposits) was an annualized 2.5% of assets, above its prior range of 1.3% to 1.7% and up +0.9 pp over four quarters, and it pushed the score up with a contribution of +0.262. The efficiency ratio (operating costs as a share of revenue) read -5.6%, far below its prior range of 71.5% to 178.0% after a change of -183.6 pp over four quarters, and it pushed the score up with a contribution of +0.162. Asset growth over the past four quarters was -20.9%, below its prior range of -13.8% to 11.1%, and it pushed the score up with a contribution of +0.061.

Net interest margin (the spread earned on lending and investing) fell to 2.2%, below its prior range of 3.7% to 5.0%, yet the model gave it little effect on the score, with a contribution of +0.045. Construction loans made up 9.8% of all loans, above their prior range of 4.2% to 8.4%, yet this ratio pushed the score down, with a contribution of -0.328.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized provision for loan losses as a share of assets | 3.9% | -0.1% to 1.4% | same quarter, prior 3 years | n/a | +2.5 pp | +0.167 | pushed the score up |
| net interest margin (the spread earned on lending and investing) | 2.2% | 3.7% to 5.0% | same quarter, prior 3 years | n/a | -1.5 pp | +0.045 | little effect on the score |
| annualized interest expense as a share of assets | 2.5% | 1.3% to 1.7% | same quarter, prior 3 years | n/a | +0.9 pp | +0.262 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | -5.6% | 71.5% to 178.0% | same quarter, prior 3 years | n/a | -183.6 pp | +0.162 | pushed the score up |
| construction loans as a share of loans | 9.8% | 4.2% to 8.4% | prior 12 quarters | +1.4 pp | +3.5 pp | -0.328 | pushed the score down |
| asset growth over the past four quarters | -20.9% | -13.8% to 11.1% | prior 12 quarters | -7.2 pp | -18.1 pp | +0.061 | pushed the score up |

8 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

Nano Banc's nonaccrual assets and foreclosed property (loans no longer collecting interest plus repossessed property) equal 16.7% of assets, at the 100.0th percentile nationally, which is unusually high, and at the 100.0th percentile among its peers against a peer median of 0.3%, which is unusually high among its peers too. Its Texas ratio (troubled assets measured against capital plus loss reserves) is 209.8%, at the 99.9th percentile nationally, which is unusually high, and at the 100.0th percentile among its peers against a peer median of 3.0%, which is unusually high among its peers too. Loans 90+ days past due or not accruing interest make up 25.7% of loans, at the 99.9th percentile nationally, which is unusually high, and at the 100.0th percentile among its peers against a peer median of 0.4%, which is unusually high among its peers too. Loans 30-89 days past due equal 5.6% of assets, at the 99.9th percentile nationally, which is unusually high, and at the 99.8th percentile among its peers against a peer median of 0.2%, which is unusually high among its peers too.

The total risk-based capital ratio (the bank's capital cushion measured against its loans and other assets weighted by risk) is 9.1%, at the 0.2nd percentile nationally, which is unusually low, and at the 0.1st percentile among its peers against a peer median of 15.4%, which is unusually low among its peers too. The Tier 1 risk-based capital ratio (the same measure using only the strongest form of capital) is 7.8%, at the 0.2nd percentile nationally, which is unusually low, and at the 0.1st percentile among its peers against a peer median of 14.3%, which is unusually low among its peers too. Asset growth over the past four quarters is -20.9%, at the 0.4th percentile nationally, which is unusually low, and at the 0.1st percentile among its peers against a peer median of 4.8%, which is unusually low among its peers too. The efficiency ratio (operating costs as a share of revenue) is -5.6%, at the 0.0th percentile nationally, which is unusually low, and at the 0.0th percentile among its peers against a peer median of 63.7%, which is unusually low among its peers too.

Overall, 21 of the bank's ratios sit in the national top or bottom 10%, and all 21 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | -5.6% | 0.0th (unusually low) | 63.7% | 0.0th | unusually low among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 16.7% | 100.0th (unusually high) | 0.3% | 100.0th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 209.8% | 99.9th (unusually high) | 3.0% | 100.0th | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 25.7% | 99.9th (unusually high) | 0.4% | 100.0th | unusually high among its peers too |
| loans 30-89 days past due, as a share of assets | 5.6% | 99.9th (unusually high) | 0.2% | 99.8th | unusually high among its peers too |
| the total risk-based capital ratio | 9.1% | 0.2nd (unusually low) | 15.4% | 0.1st | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 7.8% | 0.2nd (unusually low) | 14.3% | 0.1st | unusually low among its peers too |
| asset growth over the past four quarters | -20.9% | 0.4th (unusually low) | 4.8% | 0.1st | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 78.8% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 584.4% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | -38.9% | 50% or more | no |

It did not cross the construction line.
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

Hindsight: this bank's outcome case is that it remains open and on the watchlist. The fact sheet contains no data from after the as-of quarter, so there is no later information here to explain or confirm the model's reading. The reasons it sits on the watchlist are therefore the ones described in the earlier sections: heavy troubled loans, thin capital and losses.

## What happened next

Hindsight: the fact sheet holds no later ranks, watchlist flags or reporting status for this bank after the as-of quarter. Whether it keeps reporting, and how its rank moves, will only be known once newer quarterly data is added.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · CA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 3 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 5.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 7.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 9.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 25.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 16.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 3.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 209.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -0.5% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -10.9% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 56.9% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 22.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2026-06-30 · 4.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 27.3% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 2.4% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · -14.8% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: the Texas ratio (troubled assets against capital plus reserves), value 209.8%; contribution to the score · 2026-06-30 · +1.216 · data/analyst/scores.parquet: feature texas_ratio contribution
- F76 · Driver up #2: loans 90+ days past due or not accruing interest, as a share of loans, value 25.7%; contribution to the score · 2026-06-30 · +0.867 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F77 · Driver up #3: the Tier 1 risk-based capital ratio, value 7.8%; contribution to the score · 2026-06-30 · +0.575 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F78 · Driver up #4: loans 30-89 days past due, as a share of assets, value 5.6%; contribution to the score · 2026-06-30 · +0.378 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F79 · Driver up #5: brokered deposits as a share of deposits, value 22.8%; contribution to the score · 2026-06-30 · +0.360 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F80 · Driver down #1: return on equity (profit as a share of equity), value -10.9%; contribution to the score · 2026-06-30 · -0.340 · data/analyst/scores.parquet: feature return_on_equity contribution
- F81 · Driver down #2: construction loans as a share of loans, value 9.8%; contribution to the score · 2026-06-30 · -0.328 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #3: deposit growth over the past four quarters, value -14.8%; contribution to the score · 2026-06-30 · -0.169 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F83 · Driver down #4: total assets, value $736.2 million; contribution to the score · 2026-06-30 · -0.155 · data/analyst/scores.parquet: feature log_total_assets contribution
- F84 · Driver down #5: volatile funding as a share of assets, value 4.3%; contribution to the score · 2026-06-30 · -0.077 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F85 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2026-06-30 · 3.9% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F86 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · -0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F87 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F88 · Trend: annualized provision for loan losses as a share of assets, change over four quarters, in percentage points · 2026-06-30 · +2.5 pp · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F89 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.167 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F90 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F91 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 2.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F92 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 3.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F93 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 5.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F95 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · +0.045 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F96 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F97 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2026-06-30 · 2.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F98 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 1.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F99 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F100 · Trend: annualized interest expense as a share of assets, change over four quarters, in percentage points · 2026-06-30 · +0.9 pp · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F101 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · +0.262 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F102 · Trend: annualized interest expense as a share of assets, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F103 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · -5.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F104 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 71.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F105 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 178.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F106 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2026-06-30 · -183.6 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F107 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.162 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F108 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F109 · Trend: construction loans as a share of loans, value at the as-of quarter · 2026-06-30 · 9.8% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F110 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 4.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F111 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 8.4% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F114 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.328 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F115 · Trend: construction loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F116 · Trend: asset growth over the past four quarters, value at the as-of quarter · 2026-06-30 · -20.9% · data/features/fct_bank_features.parquet: asset_growth_4q
- F117 · Trend: asset growth over the past four quarters, lowest value in the comparison window · n/a · -13.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F118 · Trend: asset growth over the past four quarters, highest value in the comparison window · n/a · 11.1% · data/features/fct_bank_features.parquet: asset_growth_4q
- F121 · Trend: asset growth over the past four quarters, contribution to the score (model log-odds units) · 2026-06-30 · +0.061 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F122 · Trend: asset growth over the past four quarters, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F123 · Trend: ratios outside their own prior range · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F125 · Trend: ratios compared with their own prior range · 2026-06-30 · 30 · data/features/fct_bank_features.parquet
- F126 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F128 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 97.3% · data/analyst/scores.parquet: percentile
- F129 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F133 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-06-30 · -5.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F134 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-06-30 · 0.0th · data/features/fct_bank_features.parquet: efficiency_ratio
- F135 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: efficiency_ratio
- F136 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-06-30 · 0.0th · data/features/fct_bank_features.parquet: efficiency_ratio
- F137 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-06-30 · 63.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F138 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F139 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 16.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F140 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 100.0th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F141 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F142 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 100.0th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F143 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F144 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F145 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 209.8% · data/features/fct_bank_features.parquet: texas_ratio
- F146 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: texas_ratio
- F147 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F148 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 100.0th · data/features/fct_bank_features.parquet: texas_ratio
- F149 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: texas_ratio
- F150 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F151 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 25.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F152 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F153 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F154 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 100.0th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F155 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F156 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F157 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F158 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F159 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F160 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F161 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F162 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F163 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 9.1% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F164 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.2nd · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F165 · Peers: the total risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F166 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F167 · Peers: the total risk-based capital ratio, peer median · 2026-06-30 · 15.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F168 · Peers: the total risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F169 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2026-06-30 · 7.8% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F170 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.2nd · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F171 · Peers: the Tier 1 risk-based capital ratio, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F172 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F173 · Peers: the Tier 1 risk-based capital ratio, peer median · 2026-06-30 · 14.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F174 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F175 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -20.9% · data/features/fct_bank_features.parquet: asset_growth_4q
- F176 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.4th · data/features/fct_bank_features.parquet: asset_growth_4q
- F177 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F178 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 0.1st · data/features/fct_bank_features.parquet: asset_growth_4q
- F179 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F180 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F182 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 21 · data/features/fct_bank_features.parquet
- F183 · Peers: those ratios also unusual among peers · 2026-06-30 · 21 · data/features/fct_bank_features.parquet
- F185 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
