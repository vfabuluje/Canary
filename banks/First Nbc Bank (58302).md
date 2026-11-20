---
cert: 58302
name: "First Nbc Bank"
as_of: 2017-03-31
rank: 2
n_banks: 5925
percentile: 99.98312236286921
flagged: true
outcome: "caught"
after_test_window: false
failure_date: 2017-04-28
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:15:01"
writer_model: "claude-opus-5-5"
checked: true
---

# First Nbc Bank (cert 58302)

*Hindsight: failed 2017-04-28. Canary flagged it 2 quarters ahead.*

## Summary

As of 2017-03-31, First Nbc Bank of LA ranked 2 out of 5,925 FDIC-insured banks on Canary's risk score, placing it in the 100.0th percentile, and it was on the watchlist. Its capital, the owners' cushion against losses, was negative, with equity at -3.4% of assets against a national median of 10.7%, and 22.0% of its loans were 90+ days past due or no longer earning interest, against a national median of 0.6%. One measure points the other way: return on assets, profit as a share of assets, was 3.1%, well above the national median of 0.9%, and this pulled the score down even as the bank's assets shrank by -31.5% over the past four quarters.

## Warning signs in the data

Capital was the clearest problem: equity was -3.4% of assets against a national median of 10.7%, and the leverage ratio, core capital as a share of average assets, was -2.0% against a median of 10.5%. The risk-based measures, which weigh assets by how likely they are to lose value, were also negative, with the Tier 1 ratio at -3.1% against a median of 15.1% and the total ratio at -1.7% against a median of 16.2%. Because capital was negative, the real-estate concentration screens elsewhere in this note could not be checked at all.

Credit quality was very weak: loans 90+ days past due or not accruing interest were 22.0% of loans against a national median of 0.6%, and nonaccrual assets plus foreclosed property were 17.3% of assets against a median of 0.5%. The Texas ratio, troubled assets compared with capital plus reserves, was 225.4% against a national median of 4.8%, and loan-loss reserves, money set aside for expected bad loans, were 14.3% of loans against a median of 1.2%. Loans 30-89 days past due, an early sign of trouble, were 1.2% of assets against a median of 0.3%.

On funding, uninsured deposits, balances above the FDIC insurance limit, were 45.5% of deposits against a national median of 17.3%, and volatile funding, money that can leave quickly, was 19.3% of assets against a median of 5.1%. Federal Home Loan Bank borrowings were 8.0% of assets against a median of 0.5%, and interest expense was 2.1% of assets against a median of 0.4%, while cash stood at 18.6% of assets against a median of 6.9%. Assets shrank -31.5% and deposits -23.4% over the past four quarters, against national medians of 3.9% and 4.3%; losses on bonds held to maturity were 0.0% of equity, in line with the median of 0.0%, and losses on bonds available for sale were -1.6% against a median of 0.3%, so bond losses were not a source of strain.

## Understanding the score

As of 2017-03-31, First Nbc Bank ranked 2 out of 5,925 banks, in the 100.0th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers the riskiest 2% of banks, or 119 banks that quarter.

The five factors that pushed the score up most were the Tier 1 risk-based capital ratio at -3.1% (+2.032), the Texas ratio at 225.4% (+1.227), return on equity, profit as a share of equity, whose value is not shown here (+1.175), loans 90+ days past due or not accruing interest at 22.0% of loans (+0.792), and the total risk-based capital ratio at -1.7% (+0.683). The five factors that pulled it down most were return on assets at 3.1% (-0.596), losses on bonds available for sale at -1.6% of equity (-0.198), loans 30-89 days past due at 1.2% of assets (-0.135), construction loans at 13.5% of loans (-0.127), and brokered deposits, money placed through middlemen, at 3.8% of deposits (-0.091). The upward pushes were far larger than the downward ones.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 191 | 6,193 |  |
| 2016-06-30 | 138 | 6,129 |  |
| 2016-09-30 | 135 | 6,051 |  |
| 2016-12-31 | 2 | 5,983 | ▲ watchlist (first flag) |
| 2017-03-31 | 2 | 5,925 | ▲ watchlist |

## How its ratios moved

As of 2017-03-31, the model ranked First Nbc Bank 2 out of 5,925 banks nationally, placing it in the 100.0th percentile, where higher means riskier. A year earlier, on 2016-03-31, it sat in the 96.9th percentile, so the model rated it riskier than a year earlier. Each ratio is compared with its own history, mostly the prior 12 quarters, and 21 of the 29 ratios checked were outside their own prior range.

Volatile funding, meaning money that can leave the bank quickly, was 19.3% of assets, well above its prior range of 9.8% to 12.9%, and its contribution of +0.053 model log-odds units pushed the score up. That share rose +6.3 pp over one quarter and +9.3 pp over four quarters. Annualized interest expense, the cost of the bank's funding, was 2.1% of assets against a prior range of 1.1% to 1.2%, yet its contribution of +0.036 had little effect on the score. Cash was 18.6% of assets, far above its prior range of 1.1% to 7.6%, but its contribution of -0.019 had little effect on the score.

Return on assets, profit as a share of assets, was 3.1%, above its prior range of 1.1% to 2.0%, and despite being outside that range its contribution of -0.596 pushed the score down. Loans as a share of deposits fell to 72.8%, below its prior range of 88.1% to 101.0%, but its contribution of -0.043 had little effect on the score. The efficiency ratio, operating costs as a share of revenue, was 50.7%, below its prior range of 76.9% to 103.0%, and its contribution of +0.050 also had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| volatile funding as a share of assets | 19.3% | 9.8% to 12.9% | prior 12 quarters | +6.3 pp | +9.3 pp | +0.053 | pushed the score up |
| cash as a share of assets | 18.6% | 1.1% to 7.6% | prior 12 quarters | +15.3 pp | +11.0 pp | -0.019 | little effect on the score |
| loans as a share of deposits | 72.8% | 88.1% to 101.0% | prior 12 quarters | -28.2 pp | -16.9 pp | -0.043 | little effect on the score |
| return on assets (profit as a share of assets) | 3.1% | 1.1% to 2.0% | same quarter, prior 3 years | n/a | +1.2 pp | -0.596 | pushed the score down |
| the efficiency ratio (operating costs as a share of revenue) | 50.7% | 76.9% to 103.0% | same quarter, prior 3 years | n/a | -52.2 pp | +0.050 | little effect on the score |
| annualized interest expense as a share of assets | 2.1% | 1.1% to 1.2% | same quarter, prior 3 years | n/a | +1.0 pp | +0.036 | little effect on the score |

21 of 29 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2017-03-31: Commercial Lending Specialization.

Peers: 519 banks in the same specialty group and size tier ($1 billion to $10 billion).

As of 2017-03-31, First Nbc Bank ranked 2 out of 5,925 banks nationally on Canary's score. Its equity as a share of assets, the owners' own cushion against losses, was -3.4%, at the 0.0th national percentile, which is unusually low, and at the 0.1st percentile among its 519 peers against a peer median of 10.6%, unusually low among its peers too. Its leverage ratio, core capital as a share of average assets, was -2.0%, at the 0.0th national percentile, which is unusually low, and at the 0.1st peer percentile against a peer median of 9.9%, unusually low among its peers too. Its total risk-based capital ratio, capital measured against assets weighted by how likely they are to lose value, was -1.7%, at the 0.0th national percentile, which is unusually low, and at the 0.1st peer percentile against a peer median of 13.3%, unusually low among its peers too. Its Tier 1 risk-based capital ratio, the same measure using only the highest-quality capital, was -3.1%, at the 0.0th national percentile, which is unusually low, and at the 0.1st peer percentile against a peer median of 12.3%, unusually low among its peers too.

Loans 90+ days past due or no longer accruing interest, meaning borrowers had largely stopped paying, made up 22.0% of loans, at the 100.0th national percentile, which is unusually high, and at the 99.9th peer percentile against a peer median of 0.6%, unusually high among its peers too. Loan-loss reserves, money set aside to cover expected bad loans, were 14.3% of loans, at the 100.0th national percentile, which is unusually high, and at the 99.9th peer percentile against a peer median of 1.1%, unusually high among its peers too. Annualized interest expense, what the bank pays on deposits and borrowings, was 2.1% of assets, at the 100.0th national percentile, which is unusually high, and at the 99.9th peer percentile against a peer median of 0.4%, unusually high among its peers too. Asset growth over the past four quarters was -31.5%, a shrinking balance sheet, at the 0.1st national percentile, which is unusually low, and at the 0.1st peer percentile against a peer median of 7.8%, unusually low among its peers too.

Overall, 20 of the bank's ratios fell in the national top or bottom 10%, and 17 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| equity as a share of assets | -3.4% | 0.0th (unusually low) | 10.6% | 0.1st | unusually low among its peers too |
| the leverage ratio (core capital as a share of average assets) | -2.0% | 0.0th (unusually low) | 9.9% | 0.1st | unusually low among its peers too |
| the total risk-based capital ratio | -1.7% | 0.0th (unusually low) | 13.3% | 0.1st | unusually low among its peers too |
| the Tier 1 risk-based capital ratio | -3.1% | 0.0th (unusually low) | 12.3% | 0.1st | unusually low among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 22.0% | 100.0th (unusually high) | 0.6% | 99.9th | unusually high among its peers too |
| annualized interest expense as a share of assets | 2.1% | 100.0th (unusually high) | 0.4% | 99.9th | unusually high among its peers too |
| loan-loss reserves as a share of loans | 14.3% | 100.0th (unusually high) | 1.1% | 99.9th | unusually high among its peers too |
| asset growth over the past four quarters | -31.5% | 0.1st (unusually low) | 7.8% | 0.1st | unusually low among its peers too |

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

In hindsight, Canary caught this bank: it was first flagged in the quarter ending 2016-12-31, and the bank failed on 2017-04-28, a lead time of 2 quarters. At that first flag, the main drivers were already capital and credit: the Tier 1 risk-based capital ratio at -2.8% (+2.123), return on equity at -169.3% (+1.396), and the Texas ratio at 259.1% (+1.242). Loans 90+ days past due or not accruing interest were 14.6% of loans (+0.844), and the total risk-based capital ratio was -1.5% (+0.646).

## What happened next

In hindsight, the bank's last report was for the quarter ending 2017-03-31, and it failed on 2017-04-28. Because it stopped reporting after that, there are no later ranks or flags for it in our data.

## Sources

- F1 · Bank name · n/a · First Nbc Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · LA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2017-03-31 · 2 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2017-03-31 · 5,925 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2017-03-31 · 100.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2017-03-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2017-03-31 · 119 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2017-03-31 · -3.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2017-03-31 · 10.7% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · -2.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2017-03-31 · 10.5% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2017-03-31 · -3.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2017-03-31 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2017-03-31 · -1.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2017-03-31 · 16.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 22.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2017-03-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 17.3% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2017-03-31 · 0.5% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2017-03-31 · 1.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2017-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2017-03-31 · 14.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2017-03-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 225.4% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2017-03-31 · 4.8% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2017-03-31 · 3.1% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2017-03-31 · 0.9% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F45 · Bank: annualized interest expense as a share of assets · 2017-03-31 · 2.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F46 · National median: annualized interest expense as a share of assets · 2017-03-31 · 0.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: uninsured deposits as a share of deposits · 2017-03-31 · 45.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F50 · National median: uninsured deposits as a share of deposits · 2017-03-31 · 17.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2017-03-31 · 8.0% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F56 · National median: Federal Home Loan Bank borrowings as a share of assets · 2017-03-31 · 0.5% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F57 · Bank: volatile funding as a share of assets · 2017-03-31 · 19.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F58 · National median: volatile funding as a share of assets · 2017-03-31 · 5.1% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F59 · Bank: cash as a share of assets · 2017-03-31 · 18.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F60 · National median: cash as a share of assets · 2017-03-31 · 6.9% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F61 · Bank: losses on bonds held to maturity, as a share of equity · 2017-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F62 · National median: losses on bonds held to maturity, as a share of equity · 2017-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F63 · Bank: losses on bonds available for sale, as a share of equity · 2017-03-31 · -1.6% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F64 · National median: losses on bonds available for sale, as a share of equity · 2017-03-31 · 0.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: asset growth over the past four quarters · 2017-03-31 · -31.5% · data/features/fct_bank_features.parquet: asset_growth_4q
- F70 · National median: asset growth over the past four quarters · 2017-03-31 · 3.9% · data/features/fct_bank_features.parquet: asset_growth_4q (median of all banks)
- F71 · Bank: deposit growth over the past four quarters · 2017-03-31 · -23.4% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F72 · National median: deposit growth over the past four quarters · 2017-03-31 · 4.3% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F73 · Driver up #1: the Tier 1 risk-based capital ratio, value -3.1%; contribution to the score · 2017-03-31 · +2.032 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F74 · Driver up #2: the Texas ratio (troubled assets against capital plus reserves), value 225.4%; contribution to the score · 2017-03-31 · +1.227 · data/analyst/scores.parquet: feature texas_ratio contribution
- F75 · Driver up #3: return on equity (profit as a share of equity); contribution to the score · 2017-03-31 · +1.175 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #4: loans 90+ days past due or not accruing interest, as a share of loans, value 22.0%; contribution to the score · 2017-03-31 · +0.792 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F77 · Driver up #5: the total risk-based capital ratio, value -1.7%; contribution to the score · 2017-03-31 · +0.683 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F78 · Driver down #1: return on assets (profit as a share of assets), value 3.1%; contribution to the score · 2017-03-31 · -0.596 · data/analyst/scores.parquet: feature return_on_assets contribution
- F79 · Driver down #2: losses on bonds available for sale, as a share of equity, value -1.6%; contribution to the score · 2017-03-31 · -0.198 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F80 · Driver down #3: loans 30-89 days past due, as a share of assets, value 1.2%; contribution to the score · 2017-03-31 · -0.135 · data/analyst/scores.parquet: feature past_due_30_89_to_assets contribution
- F81 · Driver down #4: construction loans as a share of loans, value 13.5%; contribution to the score · 2017-03-31 · -0.127 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F82 · Driver down #5: brokered deposits as a share of deposits, value 3.8%; contribution to the score · 2017-03-31 · -0.091 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F83 · Failure date · 2017-04-28 · 2017-04-28 · data/raw/failures: FAILDATE
- F84 · First flag quarter (Phase 3 lead-time rule) · 2016-12-31 · 2016-12-31 · data/analyst/scores.parquet: flagged
- F85 · Lead time in quarters before failure · n/a · 2 · data/analyst/scores.parquet: quarters_until_failure
- F86 · Driver up #1 at 2016-12-31: the Tier 1 risk-based capital ratio, value -2.8%; contribution to the score · 2016-12-31 · +2.123 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F87 · Driver up #2 at 2016-12-31: return on equity (profit as a share of equity), value -169.3%; contribution to the score · 2016-12-31 · +1.396 · data/analyst/scores.parquet: feature return_on_equity contribution
- F88 · Driver up #3 at 2016-12-31: the Texas ratio (troubled assets against capital plus reserves), value 259.1%; contribution to the score · 2016-12-31 · +1.242 · data/analyst/scores.parquet: feature texas_ratio contribution
- F89 · Driver up #4 at 2016-12-31: loans 90+ days past due or not accruing interest, as a share of loans, value 14.6%; contribution to the score · 2016-12-31 · +0.844 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F90 · Driver up #5 at 2016-12-31: the total risk-based capital ratio, value -1.5%; contribution to the score · 2016-12-31 · +0.646 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F96 · Last quarter the bank reported · 2017-03-31 · 2017-03-31 · data/features/fct_bank_features.parquet: report_date
- F97 · Trend: volatile funding as a share of assets, value at the as-of quarter · 2017-03-31 · 19.3% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F98 · Trend: volatile funding as a share of assets, lowest value in the comparison window · n/a · 9.8% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F99 · Trend: volatile funding as a share of assets, highest value in the comparison window · n/a · 12.9% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F100 · Trend: volatile funding as a share of assets, change over one quarter, in percentage points · 2017-03-31 · +6.3 pp · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F101 · Trend: volatile funding as a share of assets, change over four quarters, in percentage points · 2017-03-31 · +9.3 pp · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F102 · Trend: volatile funding as a share of assets, contribution to the score (model log-odds units) · 2017-03-31 · +0.053 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F103 · Trend: volatile funding as a share of assets, what the model did with it · 2017-03-31 · pushed the score up · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F104 · Trend: cash as a share of assets, value at the as-of quarter · 2017-03-31 · 18.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F105 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F106 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 7.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F109 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2017-03-31 · -0.019 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F110 · Trend: cash as a share of assets, what the model did with it · 2017-03-31 · little effect on the score · data/analyst/scores.parquet: feature cash_to_assets contribution
- F111 · Trend: loans as a share of deposits, value at the as-of quarter · 2017-03-31 · 72.8% · data/features/fct_bank_features.parquet: loans_to_deposits
- F112 · Trend: loans as a share of deposits, lowest value in the comparison window · n/a · 88.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F113 · Trend: loans as a share of deposits, highest value in the comparison window · n/a · 101.0% · data/features/fct_bank_features.parquet: loans_to_deposits
- F116 · Trend: loans as a share of deposits, contribution to the score (model log-odds units) · 2017-03-31 · -0.043 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F117 · Trend: loans as a share of deposits, what the model did with it · 2017-03-31 · little effect on the score · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F118 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2017-03-31 · 3.1% · data/features/fct_bank_features.parquet: return_on_assets
- F119 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: return_on_assets
- F120 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 2.0% · data/features/fct_bank_features.parquet: return_on_assets
- F122 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2017-03-31 · -0.596 · data/analyst/scores.parquet: feature return_on_assets contribution
- F123 · Trend: return on assets (profit as a share of assets), what the model did with it · 2017-03-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F124 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2017-03-31 · 50.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F125 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 76.9% · data/features/fct_bank_features.parquet: efficiency_ratio
- F126 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 103.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F128 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2017-03-31 · +0.050 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F129 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2017-03-31 · little effect on the score · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F130 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2017-03-31 · 2.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F131 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 1.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F132 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 1.2% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F134 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2017-03-31 · +0.036 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F135 · Trend: annualized interest expense as a share of assets, what the model did with it · 2017-03-31 · little effect on the score · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F136 · Trend: ratios outside their own prior range · 2017-03-31 · 21 · data/features/fct_bank_features.parquet
- F138 · Trend: ratios compared with their own prior range · 2017-03-31 · 29 · data/features/fct_bank_features.parquet
- F139 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F141 · Percentile a year earlier (100 = highest risk) · 2016-03-31 · 96.9% · data/analyst/scores.parquet: percentile
- F142 · Trend: how the model's rating compares with a year earlier · 2017-03-31 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F146 · Peers: equity as a share of assets, bank value at the as-of quarter · 2017-03-31 · -3.4% · data/features/fct_bank_features.parquet: equity_to_assets
- F147 · Peers: equity as a share of assets, national percentile (100 = highest value among all banks) · 2017-03-31 · 0.0th · data/features/fct_bank_features.parquet: equity_to_assets
- F148 · Peers: equity as a share of assets, national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: equity_to_assets
- F149 · Peers: equity as a share of assets, percentile among its peers (100 = highest value) · 2017-03-31 · 0.1st · data/features/fct_bank_features.parquet: equity_to_assets
- F150 · Peers: equity as a share of assets, peer median · 2017-03-31 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets
- F151 · Peers: equity as a share of assets, reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: equity_to_assets
- F152 · Peers: the leverage ratio (core capital as a share of average assets), bank value at the as-of quarter · 2017-03-31 · -2.0% · data/features/fct_bank_features.parquet: leverage_ratio
- F153 · Peers: the leverage ratio (core capital as a share of average assets), national percentile (100 = highest value among all banks) · 2017-03-31 · 0.0th · data/features/fct_bank_features.parquet: leverage_ratio
- F154 · Peers: the leverage ratio (core capital as a share of average assets), national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: leverage_ratio
- F155 · Peers: the leverage ratio (core capital as a share of average assets), percentile among its peers (100 = highest value) · 2017-03-31 · 0.1st · data/features/fct_bank_features.parquet: leverage_ratio
- F156 · Peers: the leverage ratio (core capital as a share of average assets), peer median · 2017-03-31 · 9.9% · data/features/fct_bank_features.parquet: leverage_ratio
- F157 · Peers: the leverage ratio (core capital as a share of average assets), reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: leverage_ratio
- F158 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2017-03-31 · -1.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F159 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2017-03-31 · 0.0th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F160 · Peers: the total risk-based capital ratio, national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F161 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2017-03-31 · 0.1st · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F162 · Peers: the total risk-based capital ratio, peer median · 2017-03-31 · 13.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F163 · Peers: the total risk-based capital ratio, reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F164 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2017-03-31 · -3.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F165 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2017-03-31 · 0.0th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F166 · Peers: the Tier 1 risk-based capital ratio, national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F167 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2017-03-31 · 0.1st · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F168 · Peers: the Tier 1 risk-based capital ratio, peer median · 2017-03-31 · 12.3% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F169 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F170 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2017-03-31 · 22.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F171 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2017-03-31 · 100.0th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F172 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2017-03-31 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F173 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2017-03-31 · 99.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F174 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2017-03-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F175 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2017-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F176 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2017-03-31 · 2.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F177 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2017-03-31 · 100.0th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F178 · Peers: annualized interest expense as a share of assets, national reading · 2017-03-31 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F179 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2017-03-31 · 99.9th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F180 · Peers: annualized interest expense as a share of assets, peer median · 2017-03-31 · 0.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F181 · Peers: annualized interest expense as a share of assets, reading against its peers · 2017-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F182 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2017-03-31 · 14.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F183 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2017-03-31 · 100.0th · data/features/fct_bank_features.parquet: allowance_to_loans
- F184 · Peers: loan-loss reserves as a share of loans, national reading · 2017-03-31 · unusually high · data/features/fct_bank_features.parquet: allowance_to_loans
- F185 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2017-03-31 · 99.9th · data/features/fct_bank_features.parquet: allowance_to_loans
- F186 · Peers: loan-loss reserves as a share of loans, peer median · 2017-03-31 · 1.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F187 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2017-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F188 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2017-03-31 · -31.5% · data/features/fct_bank_features.parquet: asset_growth_4q
- F189 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2017-03-31 · 0.1st · data/features/fct_bank_features.parquet: asset_growth_4q
- F190 · Peers: asset growth over the past four quarters, national reading · 2017-03-31 · unusually low · data/features/fct_bank_features.parquet: asset_growth_4q
- F191 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2017-03-31 · 0.1st · data/features/fct_bank_features.parquet: asset_growth_4q
- F192 · Peers: asset growth over the past four quarters, peer median · 2017-03-31 · 7.8% · data/features/fct_bank_features.parquet: asset_growth_4q
- F193 · Peers: asset growth over the past four quarters, reading against its peers · 2017-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F194 · Peers: banks in the peer group (including this bank) · 2017-03-31 · 519 · data/raw/specialty/: SPECGRP
- F195 · Peers: ratios in the national top or bottom 10% · 2017-03-31 · 20 · data/features/fct_bank_features.parquet
- F196 · Peers: those ratios also unusual among peers · 2017-03-31 · 17 · data/features/fct_bank_features.parquet
- F198 · Peers: cut-off for unusual (top or bottom share of banks) · 2017-03-31 · 10% · data/features/fct_bank_features.parquet
