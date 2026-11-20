---
cert: 17001
name: "First Security Bank&Trust Co"
as_of: 2026-06-30
rank: 13
n_banks: 4313
percentile: 99.7217713888245
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:16:24"
writer_model: "claude-opus-5-5"
checked: true
---

# First Security Bank&Trust Co (cert 17001)

*Outcome not yet known.*

## Summary

As of 2026-06-30, First Security Bank&Trust Co (FDIC certificate 17001) ranked 13 out of 4,313 banks on Canary's risk score, placing it in the 99.7th percentile and on the watchlist. The main concern is credit quality: loans 90+ days past due or not accruing interest were 13.2% of loans against a national median of 0.5%, and the Texas ratio (troubled assets against capital plus reserves) was 94.7% against a median of 2.9%. Its capital cushion looks close to typical, with equity at 10.5% of assets against a national median of 10.6%, but it relies more than most banks on borrowed and brokered funding.

## Warning signs in the data

Capital is roughly in line with other banks: equity was 10.5% of assets versus a national median of 10.6%, and the leverage ratio (core capital as a share of average assets) was 10.1% versus 11.0%. Credit quality is the clear weak spot. Nonaccrual assets and foreclosed property (loans no longer earning interest plus property the bank has taken back) were 8.0% of assets, against a national median of 0.3%. Loans 30-89 days past due, an early sign of repayment trouble, were 1.2% of assets versus a median of 0.2%. The bank is setting money aside for losses: loan-loss reserves were 2.1% of loans versus a median of 1.2%, and the annualized provision for loan losses was 0.7% of assets versus 0.1%, while actual write-offs stayed low at 0.1% of loans versus 0.0%.

Funding leans on costlier sources: loans were 108.0% of deposits versus a national median of 80.2%, so the bank lends out more than it holds in deposits. Brokered deposits (money placed through intermediaries) were 8.6% of deposits versus a median of 0.0%, and Federal Home Loan Bank borrowings were 9.0% of assets versus 0.2%. Interest expense was 3.4% of assets versus a median of 1.6%, and cash was only 0.8% of assets versus 6.2%. In its favour, uninsured deposits (balances above the government insurance limit) were just 4.8% of deposits versus a median of 24.8%.

Bond losses are not a concern: losses on bonds available for sale were 0.1% of equity versus a national median of 5.6%, and securities made up only 1.1% of assets versus 17.6%. Profits were thin, with return on assets (profit as a share of assets) of 0.2% versus a median of 1.2%. Some signals point different ways: the trend section shows profits falling below their usual range, yet the model treated the low return on equity as lowering the score rather than raising it. Likewise, construction loans were 13.7% of loans, well above the median of 5.3%, but the bank did not cross either of the regulators' real-estate concentration lines.

## Understanding the score

As of 2026-06-30, First Security Bank&Trust Co ranked 13 out of 4,313 banks, the 99.7th percentile on a scale of 0 to 100 where higher means riskier. That puts it on Canary's watchlist, which covers the top 2% of banks, or 87 banks that quarter; its raw model score of 0.5271 matters only for ordering banks.

The five factors that pushed the score up most were loans 90+ days past due or not accruing interest at 13.2% of loans (+1.091), the Texas ratio at 94.7% (+0.912), interest expense at 3.4% of assets (+0.461), securities at just 1.1% of assets (+0.232), and commercial real estate loans at 11.8% of loans (+0.207). The five factors that pulled it down most were the Tier 1 risk-based capital ratio, a measure of core capital against riskier assets (-0.717), return on equity at 1.9% (-0.453), the total risk-based capital ratio (-0.339), construction loans at 13.7% of loans (-0.260), and loans 30-89 days past due at 1.2% of assets (-0.200). These contributions are in the model's internal units and show direction and relative weight, not separate risks.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 416 | 4,589 |  |
| 2024-12-31 | 95 | 4,560 |  |
| 2025-03-31 | 33 | 4,536 | ▲ watchlist |
| 2025-06-30 | 59 | 4,494 | ▲ watchlist |
| 2025-09-30 | 22 | 4,452 | ▲ watchlist |
| 2025-12-31 | 10 | 4,411 | ▲ watchlist |
| 2026-03-31 | 13 | 4,353 | ▲ watchlist |
| 2026-06-30 | 13 | 4,313 | ▲ watchlist |

## How its ratios moved

As of 2026-06-30, the bank ranked 13 out of 4,313 banks nationally, placing it in the 99.7th percentile, where higher means riskier. A year earlier it sat in the 98.7th percentile, and the model rated it riskier than a year earlier. Of 28 ratios compared with the bank's own prior range, usually the prior 12 quarters, 13 were outside that range.

Loans 90+ days past due or not accruing interest (loans where the borrower has largely stopped paying) reached 13.2% of loans, above the prior range of 0.4% to 8.9%. That share rose +4.3 pp over one quarter and +10.9 pp over four quarters. At 13.2%, this ratio contributed +1.091 model log-odds units and pushed the score up. The Texas ratio (troubled assets against capital plus reserves) stood at 94.7%, above its prior range of 1.7% to 68.8%, after rising +76.2 pp over four quarters. At 94.7%, the Texas ratio contributed +0.912 model log-odds units and pushed the score up.

Profitability fell below its usual levels, yet the model treated these ratios differently. Return on equity (profit as a share of shareholders' money) was 1.9%, below its prior range of 6.3% to 11.4%, but it contributed -0.453 model log-odds units and pushed the score down. Return on assets (profit as a share of everything the bank owns) was 0.2%, below its prior range of 0.9% to 2.2%, and it also pushed the score down, contributing -0.184 model log-odds units. Net interest margin (the spread earned on lending and investing) was 4.0%, below its prior range of 5.0% to 6.0%, yet it pushed the score down with a contribution of -0.090 model log-odds units. The efficiency ratio (operating costs as a share of revenue) was 74.6%, above its prior range of 50.6% to 65.1%, but it had little effect on the score, contributing +0.005 model log-odds units.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| net interest margin (the spread earned on lending and investing) | 4.0% | 5.0% to 6.0% | same quarter, prior 3 years | n/a | -1.5 pp | -0.090 | pushed the score down |
| return on equity (profit as a share of equity) | 1.9% | 6.3% to 11.4% | same quarter, prior 3 years | n/a | -6.0 pp | -0.453 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 74.6% | 50.6% to 65.1% | same quarter, prior 3 years | n/a | +24.0 pp | +0.005 | little effect on the score |
| return on assets (profit as a share of assets) | 0.2% | 0.9% to 2.2% | same quarter, prior 3 years | n/a | -0.7 pp | -0.184 | pushed the score down |
| loans 90+ days past due or not accruing interest, as a share of loans | 13.2% | 0.4% to 8.9% | prior 12 quarters | +4.3 pp | +10.9 pp | +1.091 | pushed the score up |
| the Texas ratio (troubled assets against capital plus reserves) | 94.7% | 1.7% to 68.8% | prior 12 quarters | +25.9 pp | +76.2 pp | +0.912 | pushed the score up |

13 of 28 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2026-06-30: Commercial Lending Specialization.

Peers: 1444 banks in the same specialty group and size tier ($100 million to $1 billion).

Nonaccrual assets and foreclosed property (loans no longer earning interest plus property the bank has taken back) made up 8.0% of assets, at the 99.9th percentile nationally, which is unusually high; at the 99.8th percentile among its peers, against a peer median of 0.3%, this is unusually high among its peers too. The Texas ratio (troubled assets compared with capital plus loss reserves) was 94.7%, at the 99.8th percentile nationally, which is unusually high; at the 99.9th percentile among its peers, against a peer median of 3.0%, this is unusually high among its peers too. Loans 90+ days past due or not accruing interest were 13.2% of loans, at the 99.8th percentile nationally, which is unusually high; at the 99.8th percentile among its peers, against a peer median of 0.4%, this is unusually high among its peers too. The annualized provision for loan losses (money set aside to cover expected loan losses) was 0.7% of assets, at the 97.1st percentile nationally, which is unusually high; at the 96.8th percentile among its peers, against a peer median of 0.1%, this is unusually high among its peers too.

Annualized interest expense (what the bank pays on deposits and borrowings) was 3.4% of assets, at the 99.7th percentile nationally, which is unusually high; at the 99.7th percentile among its peers, against a peer median of 1.7%, this is unusually high among its peers too. Cash was 0.8% of assets, at the 0.8th percentile nationally, which is unusually low; at the 0.5th percentile among its peers, against a peer median of 6.5%, this is unusually low among its peers too. Loans were 108.0% of deposits, at the 95.7th percentile nationally, which is unusually high; at the 95.5th percentile among its peers, against a peer median of 83.3%, this is unusually high among its peers too. Uninsured deposits (balances above the government insurance limit) were 4.8% of deposits, at the 2.1st percentile nationally, which is unusually low; at the 0.4th percentile among its peers, against a peer median of 26.0%, this is unusually low among its peers too.

Overall, 14 of the bank's ratios sit in the national top or bottom 10%, and 13 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| nonaccrual assets and foreclosed property, as a share of assets | 8.0% | 99.9th (unusually high) | 0.3% | 99.8th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 94.7% | 99.8th (unusually high) | 3.0% | 99.9th | unusually high among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 13.2% | 99.8th (unusually high) | 0.4% | 99.8th | unusually high among its peers too |
| annualized interest expense as a share of assets | 3.4% | 99.7th (unusually high) | 1.7% | 99.7th | unusually high among its peers too |
| cash as a share of assets | 0.8% | 0.8th (unusually low) | 6.5% | 0.5th | unusually low among its peers too |
| uninsured deposits as a share of deposits | 4.8% | 2.1st (unusually low) | 26.0% | 0.4th | unusually low among its peers too |
| annualized provision for loan losses as a share of assets | 0.7% | 97.1st (unusually high) | 0.1% | 96.8th | unusually high among its peers too |
| loans as a share of deposits | 108.0% | 95.7th (unusually high) | 83.3% | 95.5th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 98.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 181.4% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 119.8% | 50% or more | yes |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it's on the watchlist

In hindsight: this bank's outcome case is an open watchlist entry, meaning it remains flagged rather than resolved either way. The fact sheet holds no data after the as-of quarter, so the reasons it sits on the watchlist are the ones described above: heavy problem loans, a high Texas ratio, and reliance on costlier funding.

## What happened next

In hindsight: the fact sheet contains no later ranks, watchlist flags or reporting status for this bank. We therefore cannot say here how its rank moved after the as-of quarter or whether it still files reports; the score history table added with this memo is the place to check later quarters.

## Sources

- F1 · Bank name · n/a · First Security Bank&Trust Co · data/features/fct_bank_features.parquet: institution_name
- F2 · Certificate number · n/a · 17001 · data/features/fct_bank_features.parquet: cert
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F5 · Model score · 2026-06-30 · 0.5271 · data/analyst/scores.parquet: score
- F6 · National rank (1 = highest score) · 2026-06-30 · 13 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.7% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 10.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 10.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 13.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F18 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F19 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F20 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F21 · Bank: loans 30-89 days past due, as a share of assets · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F22 · National median: loans 30-89 days past due, as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F23 · Bank: loan-loss reserves as a share of loans · 2026-06-30 · 2.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F24 · National median: loan-loss reserves as a share of loans · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F25 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F26 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F27 · Bank: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F28 · National median: annualized provision for loan losses as a share of assets · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F29 · Bank: construction loans as a share of loans · 2026-06-30 · 13.7% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F30 · National median: construction loans as a share of loans · 2026-06-30 · 5.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans (median of all banks)
- F33 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 94.7% · data/features/fct_bank_features.parquet: texas_ratio
- F34 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F35 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: return_on_assets
- F36 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F43 · Bank: annualized interest expense as a share of assets · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F44 · National median: annualized interest expense as a share of assets · 2026-06-30 · 1.6% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F45 · Bank: loans as a share of deposits · 2026-06-30 · 108.0% · data/features/fct_bank_features.parquet: loans_to_deposits
- F46 · National median: loans as a share of deposits · 2026-06-30 · 80.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F47 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F48 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F49 · Bank: brokered deposits as a share of deposits · 2026-06-30 · 8.6% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F50 · National median: brokered deposits as a share of deposits · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F53 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 9.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F54 · National median: Federal Home Loan Bank borrowings as a share of assets · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F57 · Bank: cash as a share of assets · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F58 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds available for sale, as a share of equity · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F62 · National median: losses on bonds available for sale, as a share of equity · 2026-06-30 · 5.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F63 · Bank: securities as a share of assets · 2026-06-30 · 1.1% · data/features/fct_bank_features.parquet: securities_to_assets
- F64 · National median: securities as a share of assets · 2026-06-30 · 17.6% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F71 · Driver up #1: loans 90+ days past due or not accruing interest, as a share of loans, value 13.2%; contribution to the score · 2026-06-30 · +1.091 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F72 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 94.7%; contribution to the score · 2026-06-30 · +0.912 · data/analyst/scores.parquet: feature texas_ratio contribution
- F73 · Driver up #3: annualized interest expense as a share of assets, value 3.4%; contribution to the score · 2026-06-30 · +0.461 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F74 · Driver up #4: securities as a share of assets, value 1.1%; contribution to the score · 2026-06-30 · +0.232 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F75 · Driver up #5: commercial real estate loans as a share of loans, value 11.8%; contribution to the score · 2026-06-30 · +0.207 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F76 · Driver down #1: the Tier 1 risk-based capital ratio; contribution to the score · 2026-06-30 · -0.717 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver down #2: return on equity (profit as a share of equity), value 1.9%; contribution to the score · 2026-06-30 · -0.453 · data/analyst/scores.parquet: feature return_on_equity contribution
- F78 · Driver down #3: the total risk-based capital ratio; contribution to the score · 2026-06-30 · -0.339 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver down #4: construction loans as a share of loans, value 13.7%; contribution to the score · 2026-06-30 · -0.260 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F80 · Driver down #5: loans 30-89 days past due, as a share of assets, value 1.2%; contribution to the score · 2026-06-30 · -0.200 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F81 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2026-06-30 · 4.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F82 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 5.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F83 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 6.0% · data/features/fct_bank_features.parquet: net_interest_margin
- F85 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2026-06-30 · -0.090 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F86 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature net_interest_margin contribution
- F87 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2026-06-30 · 1.9% · data/features/fct_bank_features.parquet: return_on_equity
- F88 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 6.3% · data/features/fct_bank_features.parquet: return_on_equity
- F89 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 11.4% · data/features/fct_bank_features.parquet: return_on_equity
- F91 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2026-06-30 · -0.453 · data/analyst/scores.parquet: feature return_on_equity contribution
- F92 · Trend: return on equity (profit as a share of equity), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2026-06-30 · 74.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F94 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 50.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 65.1% · data/features/fct_bank_features.parquet: efficiency_ratio
- F97 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2026-06-30 · +0.005 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F98 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2026-06-30 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F99 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2026-06-30 · 0.2% · data/features/fct_bank_features.parquet: return_on_assets
- F100 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 0.9% · data/features/fct_bank_features.parquet: return_on_assets
- F101 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: return_on_assets
- F103 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2026-06-30 · -0.184 · data/analyst/scores.parquet: feature return_on_assets contribution
- F104 · Trend: return on assets (profit as a share of assets), what the model did with it · 2026-06-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F105 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, value at the as-of quarter · 2026-06-30 · 13.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F106 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F107 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, highest value in the comparison window · n/a · 8.9% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F108 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, change over one quarter, in percentage points · 2026-06-30 · +4.3 pp · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F109 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, change over four quarters, in percentage points · 2026-06-30 · +10.9 pp · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F110 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, contribution to the score (model log-odds units) · 2026-06-30 · +1.091 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F111 · Trend: loans 90+ days past due or not accruing interest, as a share of loans, what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F112 · Trend: the Texas ratio (troubled assets against capital plus reserves), value at the as-of quarter · 2026-06-30 · 94.7% · data/features/fct_bank_features.parquet: texas_ratio
- F113 · Trend: the Texas ratio (troubled assets against capital plus reserves), lowest value in the comparison window · n/a · 1.7% · data/features/fct_bank_features.parquet: texas_ratio
- F114 · Trend: the Texas ratio (troubled assets against capital plus reserves), highest value in the comparison window · n/a · 68.8% · data/features/fct_bank_features.parquet: texas_ratio
- F116 · Trend: the Texas ratio (troubled assets against capital plus reserves), change over four quarters, in percentage points · 2026-06-30 · +76.2 pp · data/features/fct_bank_features.parquet: texas_ratio
- F117 · Trend: the Texas ratio (troubled assets against capital plus reserves), contribution to the score (model log-odds units) · 2026-06-30 · +0.912 · data/analyst/scores.parquet: feature texas_ratio contribution
- F118 · Trend: the Texas ratio (troubled assets against capital plus reserves), what the model did with it · 2026-06-30 · pushed the score up · data/analyst/scores.parquet: feature texas_ratio contribution
- F119 · Trend: ratios outside their own prior range · 2026-06-30 · 13 · data/features/fct_bank_features.parquet
- F121 · Trend: ratios compared with their own prior range · 2026-06-30 · 28 · data/features/fct_bank_features.parquet
- F122 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F124 · Percentile a year earlier (100 = highest risk) · 2025-06-30 · 98.7% · data/analyst/scores.parquet: percentile
- F125 · Trend: how the model's rating compares with a year earlier · 2026-06-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F129 · Peers: nonaccrual assets and foreclosed property, as a share of assets, bank value at the as-of quarter · 2026-06-30 · 8.0% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F130 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F131 · Peers: nonaccrual assets and foreclosed property, as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F132 · Peers: nonaccrual assets and foreclosed property, as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F133 · Peers: nonaccrual assets and foreclosed property, as a share of assets, peer median · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F134 · Peers: nonaccrual assets and foreclosed property, as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F135 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2026-06-30 · 94.7% · data/features/fct_bank_features.parquet: texas_ratio
- F136 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: texas_ratio
- F137 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F138 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2026-06-30 · 99.9th · data/features/fct_bank_features.parquet: texas_ratio
- F139 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2026-06-30 · 3.0% · data/features/fct_bank_features.parquet: texas_ratio
- F140 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F141 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2026-06-30 · 13.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F142 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F143 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F144 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2026-06-30 · 99.8th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F145 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2026-06-30 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F146 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F147 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2026-06-30 · 3.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F148 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F149 · Peers: annualized interest expense as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F150 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 99.7th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F151 · Peers: annualized interest expense as a share of assets, peer median · 2026-06-30 · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F152 · Peers: annualized interest expense as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F153 · Peers: cash as a share of assets, bank value at the as-of quarter · 2026-06-30 · 0.8% · data/features/fct_bank_features.parquet: cash_to_assets
- F154 · Peers: cash as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 0.8th · data/features/fct_bank_features.parquet: cash_to_assets
- F155 · Peers: cash as a share of assets, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: cash_to_assets
- F156 · Peers: cash as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 0.5th · data/features/fct_bank_features.parquet: cash_to_assets
- F157 · Peers: cash as a share of assets, peer median · 2026-06-30 · 6.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F158 · Peers: cash as a share of assets, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: cash_to_assets
- F159 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 4.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F160 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 2.1st · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F161 · Peers: uninsured deposits as a share of deposits, national reading · 2026-06-30 · unusually low · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F162 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 0.4th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F163 · Peers: uninsured deposits as a share of deposits, peer median · 2026-06-30 · 26.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F164 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2026-06-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F165 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2026-06-30 · 0.7% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F166 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2026-06-30 · 97.1st · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F167 · Peers: annualized provision for loan losses as a share of assets, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F168 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2026-06-30 · 96.8th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F169 · Peers: annualized provision for loan losses as a share of assets, peer median · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F170 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F171 · Peers: loans as a share of deposits, bank value at the as-of quarter · 2026-06-30 · 108.0% · data/features/fct_bank_features.parquet: loans_to_deposits
- F172 · Peers: loans as a share of deposits, national percentile (100 = highest value among all banks) · 2026-06-30 · 95.7th · data/features/fct_bank_features.parquet: loans_to_deposits
- F173 · Peers: loans as a share of deposits, national reading · 2026-06-30 · unusually high · data/features/fct_bank_features.parquet: loans_to_deposits
- F174 · Peers: loans as a share of deposits, percentile among its peers (100 = highest value) · 2026-06-30 · 95.5th · data/features/fct_bank_features.parquet: loans_to_deposits
- F175 · Peers: loans as a share of deposits, peer median · 2026-06-30 · 83.3% · data/features/fct_bank_features.parquet: loans_to_deposits
- F176 · Peers: loans as a share of deposits, reading against its peers · 2026-06-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: loans_to_deposits
- F178 · Peers: ratios in the national top or bottom 10% · 2026-06-30 · 14 · data/features/fct_bank_features.parquet
- F179 · Peers: those ratios also unusual among peers · 2026-06-30 · 13 · data/features/fct_bank_features.parquet
- F181 · Peers: cut-off for unusual (top or bottom share of banks) · 2026-06-30 · 10% · data/features/fct_bank_features.parquet
