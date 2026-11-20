---
cert: 420
name: "Bank Of Vici"
as_of: 2026-06-30
rank: 19
n_banks: 4313
percentile: 99.58265708323673
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:16:24"
writer_model: "claude-opus-5-5"
checked: true
---

# Bank Of Vici (cert 420)

*Outcome not yet known.*

## Summary

As of 2026-06-30, Bank Of Vici, a small Oklahoma bank, ranked 19 out of 4,313 banks nationally on Canary's score, placing it in the 99.6th percentile, where 100 marks the highest risk. That placed it on Canary's watchlist, the top 2% of banks by score. The biggest pushes on its score came from large paper losses on its bond holdings, a high share of seriously overdue loans, and a high Texas ratio (troubled assets measured against capital plus reserves). Its percentile a year earlier was 99.8%, so the model rated it about the same as a year earlier.

## Warning signs in the data

Capital, the owners' cushion against losses, was thinner than at most banks: equity was 7.1% of assets against a national median of 10.6%. The leverage ratio (core capital as a share of average assets) was 10.2%, a little below the national median of 11.0%. Losses on bonds available for sale (bonds the bank could sell, now worth less than it paid) equaled 56.7% of equity, far above the national median of 5.6%.

Credit quality was weak: loans 90+ days past due or no longer earning interest were 12.3% of loans, against a national median of 0.5%. The Texas ratio was 69.0%, far above the national median of 2.9%, while loan-loss reserves (money set aside for bad loans) were 3.2% of loans against a median of 1.2%. The bank was losing money, with return on assets (profit as a share of assets) of -0.9% against a national median of 1.2%.

On funding, deposits changed by -13.5% over the past four quarters, while the national median grew 4.2%, and volatile funding (money that can leave quickly) was 15.7% of assets against a median of 9.0%. Some figures point the other way: uninsured deposits were 15.7% of deposits, below the national median of 24.8%, and the real-estate concentration section found it did not cross either regulatory screening line.

## Understanding the score

Bank Of Vici ranked 19 out of 4,313 banks on 2026-06-30, the 99.6th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks, or 87 banks that quarter.

The five features that pushed the score up most were losses on bonds available for sale at 56.7% of equity, contributing +0.920, and loans 90+ days past due or not earning interest at 12.3% of loans, contributing +0.917. Next came the Texas ratio at 69.0%, contributing +0.830, asset growth over the past four quarters of -11.7%, contributing +0.125, and loans as a share of deposits at 50.3%, contributing +0.122.

The five features that pulled the score down most were the Tier 1 risk-based capital ratio (core capital against risk-weighted assets), contributing -0.744, and nonaccrual assets and foreclosed property at 0.9% of assets, contributing -0.385. The efficiency ratio of 118.5% contributed -0.282, the leverage ratio of 10.2% contributed -0.272, and return on equity of -13.2% contributed -0.237, so the model treated these figures as easing the score in this case.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 21 | 4,589 | ▲ watchlist |
| 2024-12-31 | 18 | 4,560 | ▲ watchlist |
| 2025-03-31 | 11 | 4,536 | ▲ watchlist |
| 2025-06-30 | 9 | 4,494 | ▲ watchlist |
| 2025-09-30 | 25 | 4,452 | ▲ watchlist |
| 2025-12-31 | 34 | 4,411 | ▲ watchlist |
| 2026-03-31 | 197 | 4,353 |  |
| 2026-06-30 | 19 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, Bank Of Vici ranked 19 out of 4,313 banks nationally, placing it in the 99.6th percentile, where 100 marks the highest risk score. A year earlier it sat in the 99.8th percentile, and the model rated it about the same as a year earlier. Each ratio is compared with its own prior range, usually over the prior 12 quarters, and 6 of the 28 ratios checked fell outside that range; the table shows those 6.

The Texas ratio (troubled loans and assets measured against capital plus reserves) stood at 69.0%, above its prior range of 15.2% to 64.5%, and it pushed the score up with a contribution of +0.830 model log-odds units, where a positive number raises the score. That ratio rose +53.5 pp in one quarter. Loan-loss reserves (money set aside to cover expected loan losses) were 3.2% of loans, just above their prior range of 0.1% to 3.1%, and they pushed the score up with a contribution of +0.058. Commercial real estate loans were 9.7% of loans, below their prior range of 13.4% to 23.2%, yet this ratio still pushed the score up with a contribution of +0.102.

Loans 30-89 days past due were 0.6% of assets, below their prior range of 1.4% to 5.5%, and in contrast to being outside their range they pushed the score down with a contribution of -0.192. Construction loans were 0.0% of loans, below their prior range of 1.0% to 3.3%, and this ratio also pushed the score down with a contribution of -0.176. Net loan write-offs (loans recorded as losses, minus amounts later recovered) were 0.3% of loans on an annualized basis, well below their prior range of 3.1% to 4.0%, yet despite falling outside that range they had little effect on the score, with a contribution of +0.007. That write-off ratio fell -3.7 pp over four quarters.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| annualized loan write-offs, net of recoveries, as a share of loans | 0.3% | 3.1% to 4.0% | same quarter, prior 3 years | n/a | -3.7 pp | +0.007 | little effect on the score |
| construction loans as a share of loans | 0.0% | 1.0% to 3.3% | prior 12 quarters | -1.3 pp | -2.1 pp | -0.176 | pushed the score down |
| commercial real estate loans as a share of loans | 9.7% | 13.4% to 23.2% | prior 12 quarters | -6.9 pp | -7.8 pp | +0.102 | pushed the score up |
| loans 30-89 days past due, as a share of assets | 0.6% | 1.4% to 5.5% | prior 12 quarters | -4.0 pp | -0.8 pp | -0.192 | pushed the score down |
| the Texas ratio (troubled assets against capital plus reserves) | 69.0% | 15.2% to 64.5% | prior 12 quarters | +53.5 pp | +28.0 pp | +0.830 | pushed the score up |
| loan-loss reserves as a share of loans | 3.2% | 0.1% to 3.1% | prior 12 quarters | +0.3 pp | +1.0 pp | +0.058 | pushed the score up |

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 95 banks in the same specialty group and size tier (under $100 million).

Bank Of Vici ranks 19 out of 4,313 banks nationally on Canary's score, where a lower rank means a higher score. Its share of loans that are seriously overdue or no longer earning interest is 12.3%, at the 99.7th percentile nationally, which is unusually high, and at the 98.4th percentile among its peers against a peer median of 0.5%, so it is unusually high among its peers too. The Texas ratio, which compares troubled assets with capital plus reserves, is 69.0%, at the 99.7th percentile nationally, which is unusually high, and at the 97.4th percentile among its peers against a peer median of 3.0%, so it is unusually high among its peers too. Loan-loss reserves, money set aside to cover loans that may not be repaid, equal 3.2% of loans, at the 98.0th percentile nationally, which is unusually high, and at the 95.3rd percentile among its peers against a peer median of 1.3%, so they are unusually high among its peers too.

Return on equity, profit as a share of the owners' stake, is -13.2%, at the 1.2nd percentile nationally, which is unusually low, and at the 8.9th percentile among its peers against a peer median of 7.0%, so it is unusually low among its peers too. Return on assets, profit as a share of everything the bank owns, is -0.9%, at the 2.0th percentile nationally, which is unusually low, while at the 15.3rd percentile among its peers against a peer median of 0.8% it is typical for its peer group. The efficiency ratio, operating costs as a share of revenue, is 118.5%, at the 98.2nd percentile nationally, which is unusually high, while at the 83.7th percentile among its peers against a peer median of 75.6% it is typical for its peer group. Deposits changed by -13.5% over the past four quarters, at the 1.2nd percentile nationally, which is unusually low, and at the 4.7th percentile among its peers against a peer median of 4.2%, so this is unusually low among its peers too. Total assets changed by -11.7% over the past four quarters, at the 1.3rd percentile nationally, which is unusually low, and at the 4.7th percentile among its peers against a peer median of 3.4%, so this is unusually low among its peers too.

Overall, 12 of the bank's ratios fall in the national top or bottom 10%, and 8 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| loans 90+ days past due or not accruing interest, as a share of loans | 12.3% | 99.7th (unusually high) | 0.5% | 98.4th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 69.0% | 99.7th (unusually high) | 3.0% | 97.4th | unusually high among its peers too |
| return on equity (profit as a share of equity) | -13.2% | 1.2nd (unusually low) | 7.0% | 8.9th | unusually low among its peers too |
| deposit growth over the past four quarters | -13.5% | 1.2nd (unusually low) | 4.2% | 4.7th | unusually low among its peers too |
| asset growth over the past four quarters | -11.7% | 1.3rd (unusually low) | 3.4% | 4.7th | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 118.5% | 98.2nd (unusually high) | 75.6% | 83.7th | typical for its peer group |
| loan-loss reserves as a share of loans | 3.2% | 98.0th (unusually high) | 1.3% | 95.3rd | unusually high among its peers too |
| return on assets (profit as a share of assets) | -0.9% | 2.0th (unusually low) | 0.8% | 15.3rd | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 55.0% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -43.9% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight: this bank is a watchlist case that, in our data, had not reached a resolution. The fact sheet holds no data from after the as-of quarter, so there is no later evidence to explain how its situation developed. Its place on the watchlist rests on the as-of figures described above, not on any later outcome.

## What happened next

In hindsight: the fact sheet contains no later ranks, watchlist flags or reporting status for this bank. We therefore cannot say from our data whether its rank changed, whether it stayed on the watchlist, or whether it kept filing reports.

## Sources

- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · OK · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 19 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.6% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 7.1% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 12.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 69.0% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 15.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: volatile funding as a share of assets · 2026-06-30 · 15.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F56 · National median: volatile funding as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 56.7% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: deposit growth over the past four quarters · 2026-06-30 · -13.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F70 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F71 · Driver up #1: losses on bonds available for sale, as a share of equity, value 56.7%; contribution to the score · 2026-06-30 · +0.920 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F72 · Driver up #2: loans 90+ days past due or not accruing interest, as a share of loans, value 12.3%; contribution to the score · 2026-06-30 · +0.917 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F73 · Driver up #3: the Texas ratio (troubled assets against capital plus reserves), value 69.0%; contribution to the score · 2026-06-30 · +0.830 · data/analyst/scores.parquet: feature texas_ratio contribution
- F74 · Driver up #4: asset growth over the past four quarters, value -11.7%; contribution to the score · 2026-06-30 · +0.125 · data/analyst/scores.parquet: feature asset_growth_4q contribution
- F75 · Driver up #5: loans as a share of deposits, value 50.3%; contribution to the score · 2026-06-30 · +0.122 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.744 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: nonaccrual assets and foreclosed property, as a share of assets, value 0.9%; contribution to the score · 2026-06-30 · -0.385 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F78 · Driver down #3: the efficiency ratio (operating costs as a share of revenue), value 118.5%; contribution to the score · 2026-06-30 · -0.282 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F79 · Driver down #4: the leverage ratio (core capital as a share of average assets), value 10.2%; contribution to the score · 2026-06-30 · -0.272 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #5: return on equity (profit as a share of equity), value -13.2%; contribution to the score · 2026-06-30 · -0.237 · data/analyst/scores.parquet: feature return_on_equity contribution
- F81 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F82 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 3.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F83 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 4.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F84 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, change over four quarters, in percentage points · 2026-06-30 · -3.7 pp · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F85 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.007 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F86 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F87 · Trend: construction loans as a share of loans, value at the as-of quarter · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F88 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F89 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 3.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F92 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · -0.176 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F93 · Trend: construction loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F94 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2026-06-30 · 9.7% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F95 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 13.4% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F96 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 23.2% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F99 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.102 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F100 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F101 · Trend: loans 30-89 days past due, as a share of assets, value at the as-of quarter · 2026-06-30 · 0.6% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F102 · Trend: loans 30-89 days past due, as a share of assets, lowest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F103 · Trend: loans 30-89 days past due, as a share of assets, highest value in the comparison window · n/a · 5.5% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F106 · Trend: loans 30-89 days past due, as a share of assets, contribution to the score (model log-odds units) · 2026-06-30 · -0.192 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F107 · Trend: loans 30-89 days past due, as a share of assets, what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F108 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 69.0% · data/features/fct_bank_features.parquet: texas_ratio
- F109 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 15.2% · data/features/fct_bank_features.parquet: texas_ratio
- F110 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 64.5% · data/features/fct_bank_features.parquet: texas_ratio
- F111 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over one quarter, in percentage points · 2026-06-30 · +53.5 pp · data/features/fct_bank_features.parquet: texas_ratio
- F113 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · +0.830 · data/analyst/scores.parquet: feature texas_ratio contribution
- F114 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F115 · Trend: loan-loss reserves as a share of loans, value at the as-of quarter · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F116 · Trend: loan-loss reserves as a share of loans, lowest value in the comparison window · n/a · 0.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F117 · Trend: loan-loss reserves as a share of loans, highest value in the comparison window · n/a · 3.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F120 · Trend: loan-loss reserves as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +0.058 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F121 · Trend: loan-loss reserves as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F122 · Trend: ratios outside their own prior range · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F123 · Trend: ratios shown in the table (the furthest outside their prior range) · 2026-06-30 · 6 · data/features/fct_bank_features.parquet
- F124 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F125 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F127 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 99.8% · data/analyst/scores.parquet: percentile
- F128 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F132 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 12.3% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F133 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F134 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F135 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 98.4th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F136 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F137 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F138 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 69.0% · data/features/fct_bank_features.parquet: texas_ratio
- F139 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: texas_ratio
- F140 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F141 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 97.4th · data/features/fct_bank_features.parquet: texas_ratio
- F142 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: texas_ratio
- F143 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F144 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2026-06-30 · -13.2% · data/features/fct_bank_features.parquet: return_on_equity
- F145 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2026-06-30 · 1.2nd · data/features/fct_bank_features.parquet: return_on_equity
- F146 · Peers: return on equity (profit as a share of equity), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_equity
- F147 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2026-06-30 · 8.9th · data/features/fct_bank_features.parquet: return_on_equity
- F148 · Peers: return on equity (profit as a share of equity), peer median · 2026-06-30 · 7.0% · data/features/fct_bank_features.parquet: return_on_equity
- F149 · Peers: return on equity (profit as a share of equity), reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F150 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -13.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F151 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 1.2nd · data/features/fct_bank_features.parquet: deposit_growth_4q
- F152 · Peers: deposit growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: deposit_growth_4q
- F153 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 4.7th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F154 · Peers: deposit growth over the past four quarters, peer median · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F155 · Peers: deposit growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F156 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2026-06-30 · -11.7% · data/features/fct_bank_features.parquet: asset_growth_4q
- F157 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2026-06-30 · 1.3rd · data/features/fct_bank_features.parquet: asset_growth_4q
- F158 · Peers: asset growth over the past four quarters, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F159 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2026-06-30 · 4.7th · data/features/fct_bank_features.parquet: asset_growth_4q
- F160 · Peers: asset growth over the past four quarters, peer median · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: asset_growth_4q
- F161 · Peers: asset growth over the past four quarters, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F162 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2026-06-30 · 118.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F163 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2026-06-30 · 98.2nd · data/features/fct_bank_features.parquet: efficiency_ratio
- F164 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: efficiency_ratio
- F165 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2026-06-30 · 83.7th · data/features/fct_bank_features.parquet: efficiency_ratio
- F166 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2026-06-30 · 75.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F167 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: efficiency_ratio
- F168 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2026-06-30 · 3.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F169 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 98.0th · data/features/fct_bank_features.parquet: allowance_to_loans
- F170 · Peers: loan-loss reserves as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: allowance_to_loans
- F171 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 95.3rd · data/features/fct_bank_features.parquet: allowance_to_loans
- F172 · Peers: loan-loss reserves as a share of loans, peer median · 2026-06-30 · 1.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F173 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F174 · Peers: return on assets (profit as a share of assets), bank value at the as-of quarter · 2026-06-30 · -0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F175 · Peers: return on assets (profit as a share of assets), national percentile (100 = highest value among all banks) · 2026-06-30 · 2.0th · data/features/fct_bank_features.parquet: return_on_assets
- F176 · Peers: return on assets (profit as a share of assets), national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: return_on_assets
- F177 · Peers: return on assets (profit as a share of assets), percentile among its peers (100 = highest value) · 2026-06-30 · 15.3rd · data/features/fct_bank_features.parquet: return_on_assets
- F178 · Peers: return on assets (profit as a share of assets), peer median · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: return_on_assets
- F179 · Peers: return on assets (profit as a share of assets), reading against its peers · 2026-06-30 · typical for its peer group · data/features/fct_bank_features.parquet: return_on_assets
- F181 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 12 · data/features/fct_bank_features.parquet
- F182 · Peers: those ratios also unusual among peers · 2026-06-30 · 8 · data/features/fct_bank_features.parquet
- F184 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
