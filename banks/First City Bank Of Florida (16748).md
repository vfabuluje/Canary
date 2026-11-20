---
cert: 16748
name: "First City Bank Of Florida"
as_of: 2020-09-30
rank: 2
n_banks: 5098
percentile: 99.98038446449588
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2020-10-16
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:14:02"
writer_model: "claude-opus-5-5"
checked: true
---

# First City Bank Of Florida (cert 16748)

*Hindsight: failed 2020-10-16. Canary flagged it 4 quarters ahead.*

## Summary

As of 2020-09-30, First City Bank Of Florida (certificate 16748, based in FL) ranked 2 out of 5,098 FDIC-insured banks on Canary's risk score, at the 100.0th percentile, and was on the watchlist. Its capital cushion was extremely thin, with equity at 1.5% of assets against a national median of 10.9%, and its Texas ratio, which weighs troubled assets against capital plus reserves, stood at 489.0% against a median of 3.4%. The bank was also losing money, with return on equity of -68.6%, even though its funding looked steady, with core deposits at 98.1% of assets.

## Warning signs in the data

Capital, the owners' money that absorbs losses before depositors are hurt, was far below normal levels. Equity was 1.5% of assets against a national median of 10.9%, and the leverage ratio (core capital as a share of average assets) was 1.4% against a median of 10.2%. The Tier 1 risk-based capital ratio, which measures top-quality capital against assets weighted by riskiness, was 2.5% against a median of 14.7%, and the broader total risk-based capital ratio was 3.7% against 15.9%. Profits were not rebuilding that cushion: return on equity (profit as a share of equity) was -68.6% against a median of 8.7%, and the efficiency ratio (operating costs as a share of revenue) was 148.2% against 65.6%.

Credit quality, meaning how well borrowers were repaying, was weak. Nonaccrual assets and foreclosed property (loans no longer paying interest plus repossessed property) equaled 12.7% of assets, far above the national median of 0.3%. Loans 30-89 days past due came to 3.0% of assets against a median of 0.2%, and loans 90+ days past due or not accruing interest were 1.6% of loans against 0.5%. Construction loans made up 15.6% of loans, well above the national median of 4.3%. One finding points the other way: the trend section shows troubled assets had fallen below their own prior range, so they had eased compared with the bank's own recent past even while remaining far above other banks.

Funding, by contrast, looked stable: core deposits, the steadier everyday deposits, were 98.1% of assets against a median of 78.8%, and brokered deposits were 0.0% of deposits while volatile funding was 0.0% of assets. Uninsured deposits, those above the federal insurance limit, were 12.3% of deposits against a median of 21.3%, and cash was 32.0% of assets against 9.6%. Unrealized losses on bonds available for sale (bonds the bank can sell before they mature) equaled -11.2% of equity against a national median of -2.5%, a heavier hit relative to its small capital base.

## Understanding the score

As of 2020-09-30 the bank ranked 2 out of 5,098 banks, placing it at the 100.0th percentile on a scale of 0 to 100 where higher means riskier. That put it on Canary's watchlist, which covers the top 2% of banks by score and held 102 banks that quarter. Each driver below is listed with the bank's value and its contribution in the model's internal units, where positive values raise the score and negative values lower it.

The five factors that pushed the score up most were the Tier 1 risk-based capital ratio at 2.5% (+2.082), the Texas ratio at 489.0% (+1.510), return on equity at -68.6% (+1.438), the leverage ratio at 1.4% (+0.590), and the total risk-based capital ratio at 3.7% (+0.436). The five factors that pulled it down most were loans 90+ days past due or not accruing interest at 1.6% of loans (-0.686), interest expense at 0.3% of assets (-0.622), losses on bonds available for sale at -11.2% of equity (-0.375), uninsured deposits at 12.3% of deposits (-0.131), and the net interest margin, the spread earned on lending and investing, at 3.7% (-0.108).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2018-12-31 | 4 | 5,473 | ▲ watchlist |
| 2019-03-31 | 3 | 5,428 | ▲ watchlist |
| 2019-06-30 | 4 | 5,369 | ▲ watchlist |
| 2019-09-30 | 5 | 5,325 | ▲ watchlist |
| 2019-12-31 | 3 | 5,244 | ▲ watchlist (first flag) |
| 2020-03-31 | 2 | 5,182 | ▲ watchlist |
| 2020-06-30 | 2 | 5,131 | ▲ watchlist |
| 2020-09-30 | 2 | 5,098 | ▲ watchlist |

## How its ratios moved

As of 2020-09-30, the bank ranked 2 out of 5,098 banks nationally, placing it at the 100.0th percentile on a scale where higher means riskier. A year earlier it sat at the 99.9th percentile, and the model's rating is about the same as a year earlier. Each ratio is compared with its own past values, usually over the prior 12 quarters; of 30 ratios compared, 19 were outside their prior range, and the table shows the 6 furthest outside.

The Tier 1 risk-based capital ratio (core capital as a share of loans and other assets weighted by risk) was 2.5%, below its prior range of 3.1% to 3.7%, and it pushed the score up, contributing +2.082 model log-odds units (positive values raise the score). That ratio changed by -0.6 pp over one quarter and -0.9 pp over four quarters. The total risk-based capital ratio, a broader capital measure, was 3.7%, below its prior range of 4.3% to 5.0%, and it pushed the score up with a contribution of +0.436. Return on equity (profit as a share of owners' equity) was -68.6%, well below its prior range of -24.2% to -12.0% after a change of -47.2 pp over four quarters, and it pushed the score up with a contribution of +1.438.

Return on assets (profit as a share of assets) was -1.5%, below its prior range of -0.6% to -0.3%, yet despite being outside its range it had little effect on the score, contributing +0.015. The efficiency ratio (operating costs as a share of revenue) was 148.2%, above its prior range of 110.7% to 114.7% after a change of +33.5 pp over four quarters, but it too had little effect on the score, contributing +0.010. Nonaccrual assets and foreclosed property (loans no longer paying interest plus repossessed property) were 12.7% of assets, below their prior range of 16.7% to 20.8% after a change of -4.1 pp over one quarter, and this ratio had little effect on the score, contributing +0.049.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 148.2% | 110.7% to 114.7% | same quarter, prior 3 years | n/a | +33.5 pp | +0.010 | little effect on the score |
| return on equity (profit as a share of equity) | -68.6% | -24.2% to -12.0% | same quarter, prior 3 years | n/a | -47.2 pp | +1.438 | pushed the score up |
| nonaccrual assets and foreclosed property, as a share of assets | 12.7% | 16.7% to 20.8% | prior 12 quarters | -4.1 pp | -5.2 pp | +0.049 | little effect on the score |
| return on assets (profit as a share of assets) | -1.5% | -0.6% to -0.3% | same quarter, prior 3 years | n/a | -0.9 pp | +0.015 | little effect on the score |
| the Tier 1 risk-based capital ratio | 2.5% | 3.1% to 3.7% | prior 12 quarters | -0.6 pp | -0.9 pp | +2.082 | pushed the score up |
| the total risk-based capital ratio | 3.7% | 4.3% to 5.0% | prior 12 quarters | -0.6 pp | -0.9 pp | +0.436 | pushed the score up |

19 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2020-09-30: Commercial Lending Specialization.

Peers: 1819 banks in the same specialty group and size tier ($100 million to $1 billion).

Core deposits, the bank's steadier everyday deposits, made up 98.1% of assets, at the 100.0th percentile nationally (unusually high), and at the 100.0th percentile among its peers against a peer median of 79.1%, which is unusually high among its peers too. The Texas ratio, which weighs troubled assets against capital plus reserves, was 489.0%, at the 100.0th percentile nationally (unusually high), and at the 100.0th percentile among its peers against a peer median of 3.6%, which is unusually high among its peers too. Nonaccrual assets (loans no longer paying interest) plus foreclosed property came to 12.7% of assets, at the 99.9th percentile nationally (unusually high), and at the 100.0th percentile among its peers against a peer median of 0.4%, which is unusually high among its peers too.

The total risk-based capital ratio, a bank's capital cushion measured against its assets weighted by riskiness, was 3.7%, at the 0.0th percentile nationally (unusually low), and at the 0.0th percentile among its peers against a peer median of 15.3%, which is unusually low among its peers too. The Tier 1 risk-based capital ratio, which counts only the highest-quality capital, was 2.5%, at the 0.0th percentile nationally (unusually low), and at the 0.0th percentile among its peers against a peer median of 14.2%, which is unusually low among its peers too. Equity as a share of assets was 1.5%, at the 0.4th percentile nationally (unusually low), and at the 0.1st percentile among its peers against a peer median of 10.2%, which is unusually low among its peers too. The leverage ratio, core capital as a share of average assets, was 1.4%, at the 0.4th percentile nationally (unusually low), and at the 0.1st percentile among its peers against a peer median of 9.8%, which is unusually low among its peers too.

Return on equity, profit as a share of shareholders' equity, was -68.6%, at the 0.1st percentile nationally (unusually low), and at the 0.0th percentile among its peers against a peer median of 9.4%, which is unusually low among its peers too. Overall, 20 of the bank's ratios sat in the national top or bottom 10%, and all 20 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| core deposits as a share of assets | 98.1% | 100.0th (unusually high) | 79.1% | 100.0th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 489.0% | 100.0th (unusually high) | 3.6% | 100.0th | unusually high among its peers too |
| the total risk-based capital ratio | 3.7% | 0.0th (unusually low) | 15.3% | 0.0th | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | 2.5% | 0.0th (unusually low) | 14.2% | 0.0th | unusually low among its peers too |
| nonaccrual assets and foreclosed property, as a share of assets | 12.7% | 99.9th (unusually high) | 0.4% | 100.0th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -68.6% | 0.1st (unusually low) | 9.4% | 0.0th | unusually low among its peers too |
| equity as a share of assets | 1.5% | 0.4th (unusually low) | 10.2% | 0.1st | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | 1.4% | 0.4th (unusually low) | 9.8% | 0.1st | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 282.1% | 100% or more | yes |
| Total commercial real estate loans ÷ capital | 768.2% | 300% or more | yes |
| Growth in commercial real estate loans over the prior 36 months | -53.5% | 50% or more | no |

It crossed the construction line (100% or more of capital).
Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## How early Canary caught it

In hindsight, Canary first flagged this bank at 2019-12-31 under its lead-time rule, 4 quarters before the bank failed on 2020-10-16. At that first flag, the top factors pushing the score up were already thin capital and heavy troubled assets: the Tier 1 risk-based capital ratio at 3.4%, the Texas ratio at 473.5%, and the total risk-based capital ratio at 4.7%. Loans 90+ days past due or not accruing interest were then 6.6% of loans and the leverage ratio was 2.4%, both also raising the score.

Looking back, the capital weakness deepened between the first flag and the as-of quarter, with the Tier 1 risk-based capital ratio going from 3.4% to 2.5%.

## What happened next

In hindsight, the bank failed on 2020-10-16, shortly after the as-of quarter of 2020-09-30. Its last reported quarter was 2020-09-30, so there are no later ranks or watchlist flags for it.

## Sources

- F1 · Bank name · n/a · First City Bank Of Florida · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 16748 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2020-09-30 · 2020-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · FL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2020-09-30 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2020-09-30 · 5,098 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2020-09-30 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2020-09-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2020-09-30 · 102 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2020-09-30 · 1.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2020-09-30 · 10.9% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2020-09-30 · 1.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2020-09-30 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2020-09-30 · 2.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2020-09-30 · 14.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2020-09-30 · 3.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2020-09-30 · 15.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2020-09-30 · 1.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2020-09-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2020-09-30 · 12.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2020-09-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2020-09-30 · 3.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2020-09-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F33 · Bank: construction loans as a share of loans · 2020-09-30 · 15.6% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F34 · National median: construction loans as a share of loans · 2020-09-30 · 4.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2020-09-30 · 489.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2020-09-30 · 3.4% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2020-09-30 · -68.6% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2020-09-30 · 8.7% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2020-09-30 · 148.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2020-09-30 · 65.6% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2020-09-30 · 12.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2020-09-30 · 21.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F55 · Bank: core deposits as a share of assets · 2020-09-30 · 98.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2020-09-30 · 78.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2020-09-30 · 0.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F61 · Bank: cash as a share of assets · 2020-09-30 · 32.0% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2020-09-30 · 9.6% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2020-09-30 · -11.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2020-09-30 · -2.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F75 · Driver up #1: the Tier 1 risk-based capital ratio, value 2.5%; contribution to the score · 2020-09-30 · +2.082 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F76 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 489.0%; contribution to the score · 2020-09-30 · +1.510 · data/analyst/scores.parquet: feature texas_ratio contribution
- F77 · Driver up #3: return on equity (profit as a share of equity), value -68.6%; contribution to the score · 2020-09-30 · +1.438 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver up #4: the leverage ratio (core capital as a share of average assets), value 1.4%; contribution to the score · 2020-09-30 · +0.590 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F79 · Driver up #5: the total risk-based capital ratio, value 3.7%; contribution to the score · 2020-09-30 · +0.436 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F80 · Driver down #1: loans 90+ days past due or not accruing interest, as a share of loans, value 1.6%; contribution to the score · 2020-09-30 · -0.686 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F81 · Driver down #2: annualized interest expense as a share of assets, value 0.3%; contribution to the score · 2020-09-30 · -0.622 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F82 · Driver down #3: losses on bonds available for sale, as a share of equity, value -11.2%; contribution to the score · 2020-09-30 · -0.375 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F83 · Driver down #4: uninsured deposits as a share of deposits, value 12.3%; contribution to the score · 2020-09-30 · -0.131 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F84 · Driver down #5: net interest margin (the spread earned on lending and investing), value 3.7%; contribution to the score · 2020-09-30 · -0.108 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F85 · Failure date · 2020-10-16 · 2020-10-16 · data/raw/failures: FAILDATE
- F86 · First flag quarter (Phase 3 lead-time rule) · 2019-12-31 · 2019-12-31 · data/analyst/scores.parquet: flagged
- F87 · Lead time in quarters before failure · n/a · 4 · data/analyst/scores.parquet: quarters_until_failure
- F88 · Driver up #1 at 2019-12-31: the Tier 1 risk-based capital ratio, value 3.4%; contribution to the score · 2019-12-31 · +1.988 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F89 · Driver up #2 at 2019-12-31: the Texas ratio (troubled assets against capital plus reserves), value 473.5%; contribution to the score · 2019-12-31 · +1.290 · data/analyst/scores.parquet: feature texas_ratio contribution
- F90 · Driver up #3 at 2019-12-31: the total risk-based capital ratio, value 4.7%; contribution to the score · 2019-12-31 · +0.539 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F91 · Driver up #4 at 2019-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 6.6%; contribution to the score · 2019-12-31 · +0.452 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F92 · Driver up #5 at 2019-12-31: the leverage ratio (core capital as a share of average assets), value 2.4%; contribution to the score · 2019-12-31 · +0.380 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F98 · Last quarter the bank reported · 2020-09-30 · 2020-09-30 · data/features/fct_bank_features.parquet: report_date
- F99 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2020-09-30 · 148.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F100 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 110.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F101 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 114.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F102 · Trend: the efficiency ratio (operating costs as a share of revenue), change over four quarters, in percentage points · 2020-09-30 · +33.5 pp · data/features/fct_bank_features.parquet: efficiency_ratio
- F103 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2020-09-30 · +0.010 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F104 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2020-09-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F105 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2020-09-30 · -68.6% · data/features/fct_bank_features.parquet: return_on_equity
- F106 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · -24.2% · data/features/fct_bank_features.parquet: return_on_equity
- F107 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · -12.0% · data/features/fct_bank_features.parquet: return_on_equity
- F108 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2020-09-30 · -47.2 pp · data/features/fct_bank_features.parquet: return_on_equity
- F109 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2020-09-30 · +1.438 · data/analyst/scores.parquet: feature return_on_equity contribution
- F110 · Trend: return on equity (profit as a share of equity), what the model did with it · 2020-09-30 · pushed the score up · data/analyst/scores.parquet: feature return_on_equity contribution
- F111 · Trend: nonaccrual assets and foreclosed property, as a share of assets, value at the as-of quarter · 2020-09-30 · 12.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F112 · Trend: nonaccrual assets and foreclosed property, as a share of assets, lowest value in the comparison window · n/a · 16.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F113 · Trend: nonaccrual assets and foreclosed property, as a share of assets, highest value in the comparison window · n/a · 20.8% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F114 · Trend: nonaccrual assets and foreclosed property, as a share of assets, change over one quarter, in percentage points · 2020-09-30 · -4.1 pp · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F116 · Trend: nonaccrual assets and foreclosed property, as a share of assets, contribution to the score (model log-odds units) · 2020-09-30 · +0.049 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F117 · Trend: nonaccrual assets and foreclosed property, as a share of assets, what the model did with it · 2020-09-30 · little effect on the score · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F118 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2020-09-30 · -1.5% · data/features/fct_bank_features.parquet: return_on_assets
- F119 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · -0.6% · data/features/fct_bank_features.parquet: return_on_assets
- F120 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · -0.3% · data/features/fct_bank_features.parquet: return_on_assets
- F122 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2020-09-30 · +0.015 · data/analyst/scores.parquet: feature return_on_assets contribution
- F123 · Trend: return on assets (profit as a share of assets), what the model did with it · 2020-09-30 · little effect on the score · data/analyst/scores.parquet: feature return_on_assets contribution
- F124 · Trend: the Tier 1 risk-based capital ratio, value at the as-of quarter · 2020-09-30 · 2.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F125 · Trend: the Tier 1 risk-based capital ratio, lowest value in the comparison window · n/a · 3.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F126 · Trend: the Tier 1 risk-based capital ratio, highest value in the comparison window · n/a · 3.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F127 · Trend: the Tier 1 risk-based capital ratio, change over one quarter, in percentage points · 2020-09-30 · -0.6 pp · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F128 · Trend: the Tier 1 risk-based capital ratio, change over four quarters, in percentage points · 2020-09-30 · -0.9 pp · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F129 · Trend: the Tier 1 risk-based capital ratio, contribution to the score (model log-odds units) · 2020-09-30 · +2.082 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F130 · Trend: the Tier 1 risk-based capital ratio, what the model did with it · 2020-09-30 · pushed the score up · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F131 · Trend: the total risk-based capital ratio, value at the as-of quarter · 2020-09-30 · 3.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F132 · Trend: the total risk-based capital ratio, lowest value in the comparison window · n/a · 4.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F133 · Trend: the total risk-based capital ratio, highest value in the comparison window · n/a · 5.0% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F136 · Trend: the total risk-based capital ratio, contribution to the score (model log-odds units) · 2020-09-30 · +0.436 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F137 · Trend: the total risk-based capital ratio, what the model did with it · 2020-09-30 · pushed the score up · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F138 · Trend: ratios outside their own prior range · 2020-09-30 · 19 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios shown in the table (the furthest outside their prior range) · 2020-09-30 · 6 · data/features/fct_bank_features.parquet
- F140 · Trend: ratios compared with their own prior range · 2020-09-30 · 30 · data/features/fct_bank_features.parquet
- F141 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F143 · Percentile a year earlier (100 = highest risk) · 2019-09-30 · 99.9% · data/analyst/scores.parquet: percentile
- F144 · Trend: how the model's rating compares with a year earlier · 2020-09-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F148 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2020-09-30 · 98.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F149 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2020-09-30 · 100.0th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F150 · Peers: core deposits as a share of assets, national reading · 2020-09-30 · unusually high · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F151 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2020-09-30 · 100.0th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F152 · Peers: core deposits as a share of assets, peer median · 2020-09-30 · 79.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F153 · Peers: core deposits as a share of assets, reading against its peers · 2020-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F154 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2020-09-30 · 489.0% · data/features/fct_bank_features.parquet: texas_ratio
- F155 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2020-09-30 · 100.0th · data/features/fct_bank_features.parquet: texas_ratio
- F156 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2020-09-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F157 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2020-09-30 · 100.0th · data/features/fct_bank_features.parquet: texas_ratio
- F158 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2020-09-30 · 3.6% · data/features/fct_bank_features.parquet: texas_ratio
- F159 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2020-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F160 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2020-09-30 · 3.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F161 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2020-09-30 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F162 · Peers: the total risk-based capital ratio, national reading · 2020-09-30 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F163 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2020-09-30 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F164 · Peers: the total risk-based capital ratio, peer median · 2020-09-30 · 15.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F165 · Peers: the total risk-based capital ratio, reading against its peers · 2020-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F166 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2020-09-30 · 2.5% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F167 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2020-09-30 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F168 · Peers: the Tier 1 risk-based capital ratio, national reading · 2020-09-30 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F169 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2020-09-30 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F170 · Peers: the Tier 1 risk-based capital ratio, peer median · 2020-09-30 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F171 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2020-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F172 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2020-09-30 · 12.7% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F173 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2020-09-30 · 99.9th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F174 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2020-09-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F175 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2020-09-30 · 100.0th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F176 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2020-09-30 · 0.4% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F177 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2020-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F178 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2020-09-30 · -68.6% · data/features/fct_bank_features.parquet: return_on_equity
- F179 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2020-09-30 · 0.1st · data/features/fct_bank_features.parquet: return_on_equity
- F180 · Peers: return on equity (profit as a share of equity), national reading · 2020-09-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F181 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2020-09-30 · 0.0th · data/features/fct_bank_features.parquet: return_on_equity
- F182 · Peers: return on equity (profit as a share of equity), peer median · 2020-09-30 · 9.4% · data/features/fct_bank_features.parquet: return_on_equity
- F183 · Peers: return on equity (profit as a share of equity), reading against its peers · 2020-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F184 · Peers: equity as a share of assets, bank value at the as-of quarter · 2020-09-30 · 1.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F185 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2020-09-30 · 0.4th · data/features/fct_bank_features.parquet: equity_to_assets
- F186 · Peers: equity as a share of assets, national reading · 2020-09-30 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F187 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2020-09-30 · 0.1st · data/features/fct_bank_features.parquet: equity_to_assets
- F188 · Peers: equity as a share of assets, peer median · 2020-09-30 · 10.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F189 · Peers: equity as a share of assets, reading against its peers · 2020-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F190 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2020-09-30 · 1.4% · data/features/fct_bank_features.parquet: leverage_ratio
- F191 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2020-09-30 · 0.4th · data/features/fct_bank_features.parquet: leverage_ratio
- F192 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2020-09-30 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F193 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2020-09-30 · 0.1st · data/features/fct_bank_features.parquet: leverage_ratio
- F194 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2020-09-30 · 9.8% · data/features/fct_bank_features.parquet: leverage_ratio
- F195 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2020-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F197 · Peers: ratios in the national top or bottom 10% · 2020-09-30 · 20 · data/features/fct_bank_features.parquet
- F198 · Peers: those ratios also unusual among peers · 2020-09-30 · 20 · data/features/fct_bank_features.parquet
- F200 · Peers: cut-off for unusual (top or bottom share of banks) · 2020-09-30 · 10% · data/features/fct_bank_features.parquet
