---
cert: 59017
name: "First Republic Bank"
as_of: 2023-03-31
rank: 809
n_banks: 4740
percentile: 82.9535864978903
flagged: false
outcome: "missed"
after_test_window: false
failure_date: 2023-05-01
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:13:20"
writer_model: "claude-opus-5-5"
checked: true
---

# First Republic Bank (cert 59017)

*Hindsight: failed 2023-05-01. Canary did not flag it.*

## Summary

As of March 31, 2023, First Republic Bank, a bank based in CA, ranked 809 out of 4,740 banks on Canary's risk score, placing it in the 83.0th percentile, where higher means riskier. It was not flagged on the watchlist, which covers 2% of banks. Its funding stood out sharply: volatile funding, meaning money that can leave the bank quickly, was 53.0% of assets against a national median of 6.5%. Its loan quality and capital ratio, by contrast, looked healthy to the model and pulled its score down, so the data points in two different directions.

## Warning signs in the data

Capital, the owners' cushion against losses, was thinner than at most banks: equity was 7.7% of assets against a national median of 9.2%, and the leverage ratio (core capital as a share of average assets) was 8.2% against 10.4%. Its Tier 1 risk-based capital ratio, which weighs assets by how risky they are, was 11.7% against a median of 14.2%, and its total risk-based capital ratio was 12.7% against 15.4%. Earnings were weak: return on assets was 0.5% against a median of 1.0%, and the net interest margin (the spread earned on lending and investing) was 1.7% against 3.5%.

Credit quality, by contrast, looked clean: loans 90+ days past due or not accruing interest were 0.1% of loans against a median of 0.2%, and loans 30-89 days past due were 0.0% of assets against 0.2%. Loan-loss reserves, money set aside for loans that may not be repaid, were 0.5% of loans, well below the national median of 1.2%. The real-estate concentration section found the bank did not cross either regulatory screening line.

Funding was the clearest warning sign: volatile funding was 53.0% of assets against a median of 6.5%, and core deposits, the steady everyday deposits, were 25.2% of assets against 80.0%. Loans were 165.1% of deposits against a median of 73.4%, uninsured deposits (balances above the government insurance limit) were 48.7% of deposits against 24.2%, and deposit growth over the past four quarters was -35.5% against 0.0%. Federal Home Loan Bank borrowings, loans from a government-sponsored lender, were 12.1% of assets against a median of 0.5%, and losses on bonds held to maturity were 22.7% of equity against 0.0%, though losses on bonds available for sale were lower than usual at 2.0% against 15.5%. As the trend section notes, some of these funding shifts, such as the fall in deposit growth, actually pushed the model's score down rather than up.

## Understanding the score

As of 2023-03-31, First Republic Bank ranked 809 out of 4,740 banks, the 83.0th percentile on a scale of 0 to 100 where higher means riskier. It was not flagged on the watchlist, which held 95 banks that quarter, or 2% of banks.

The five features that pushed the score up most were volatile funding at 53.0% of assets, commercial real estate loans at 7.0% of loans, core deposits at 25.2% of assets, loans at 165.1% of deposits, and equity at 7.7% of assets. The five that pushed it down most were the Tier 1 risk-based capital ratio at 11.7%, the Texas ratio (troubled assets against capital plus reserves) at 0.7%, loans 90+ days past due or not accruing interest at 0.1% of loans, nonaccrual assets and foreclosed property at 0.1% of assets, and return on equity at 6.1%. The downward pulls from capital and clean loan quality were larger than the upward pushes from funding, which kept the bank off the watchlist.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2021-06-30 | 1,327 | 5,015 |  |
| 2021-09-30 | 566 | 4,979 |  |
| 2021-12-31 | 948 | 4,904 |  |
| 2022-03-31 | 3,502 | 4,861 |  |
| 2022-06-30 | 3,262 | 4,838 |  |
| 2022-09-30 | 3,095 | 4,813 |  |
| 2022-12-31 | 3,355 | 4,773 |  |
| 2023-03-31 | 809 | 4,740 |  |

## How its ratios moved

As of March 31, 2023, First Republic Bank ranked 809 out of 4,740 banks, placing it in the 83.0th percentile, where higher means riskier. A year earlier it sat in the 28.0th percentile, and the model rated it riskier than a year earlier. Of 30 ratios checked against the bank's own history, 13 were outside their prior range, which for most ratios means the prior 12 quarters.

Volatile funding, meaning money that can leave the bank quickly, reached 53.0% of assets, far above its prior range of 2.4% to 11.4%, and contributed +0.357 model log-odds units, which pushed the score up. Loans as a share of deposits rose to 165.1%, above its prior range of 85.9% to 101.5%, and contributed +0.072, which pushed the score up. Core deposits, the steady everyday deposits a bank relies on, fell to 25.2% of assets, well below their prior range of 68.5% to 84.0%, and contributed +0.090, which pushed the score up. That core deposit share dropped -48.3 pp in a single quarter.

Some ratios moved far outside their range yet worked the other way in the model. Deposit growth over the past four quarters was -35.5%, well below its prior range of 12.9% to 39.2%, yet its contribution of -0.136 pushed the score down. Uninsured deposits, the balances above the government insurance limit, were 48.7% of deposits, below their prior range of 65.0% to 74.7%, and at -0.038 had little effect on the score. Brokered deposits, money placed through outside middlemen, were 6.8% of deposits, above their prior range of 0.4% to 3.0%, yet their contribution of -0.110 pushed the score down.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| volatile funding as a share of assets | 53.0% | 2.4% to 11.4% | prior 12 quarters | +41.6 pp | +50.6 pp | +0.357 | pushed the score up |
| loans as a share of deposits | 165.1% | 85.9% to 101.5% | prior 12 quarters | +71.0 pp | +78.4 pp | +0.072 | pushed the score up |
| core deposits as a share of assets | 25.2% | 68.5% to 84.0% | prior 12 quarters | -48.3 pp | -58.9 pp | +0.090 | pushed the score up |
| deposit growth over the past four quarters | -35.5% | 12.9% to 39.2% | prior 12 quarters | -48.4 pp | -62.2 pp | -0.136 | pushed the score down |
| uninsured deposits as a share of deposits | 48.7% | 65.0% to 74.7% | prior 12 quarters | -19.0 pp | -24.9 pp | -0.038 | little effect on the score |
| brokered deposits as a share of deposits | 6.8% | 0.4% to 3.0% | prior 12 quarters | +3.8 pp | +6.2 pp | -0.110 | pushed the score down |

13 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2023-03-31: All Other Over 1 Billion.

This is a general group: the FDIC did not record a lending specialty for this bank.

Peers: 24 banks in the same specialty group and size tier (over $10 billion).

Volatile funding (money that can leave the bank quickly) was 53.0% of assets, at the 99.9th percentile nationally, which is unusually high; at the 97.8th percentile among its peers, against a peer median of 5.7%, it was unusually high among its peers too. Core deposits (steady, everyday customer deposits) were 25.2% of assets, at the 2.1st percentile nationally, which is unusually low; at the 6.5th percentile among its peers, against a peer median of 72.1%, they were unusually low among its peers too. Deposit growth over the past four quarters was -35.5%, at the 0.4th percentile nationally, which is unusually low; at the 2.1st percentile among its peers, against a peer median of -5.0%, it was unusually low among its peers too. Federal Home Loan Bank borrowings (loans to banks from a government-sponsored lender) were 12.1% of assets, at the 95.1st percentile nationally, which is unusually high; at the 93.5th percentile among its peers, against a peer median of 1.1%, they were unusually high among its peers too.

Loans as a share of deposits were 165.1%, at the 99.8th percentile nationally, which is unusually high; at the 97.9th percentile among its peers, against a peer median of 63.2%, this was unusually high among its peers too. Net interest margin (the spread earned on lending and investing) was 1.7%, at the 1.6th percentile nationally, which is unusually low; at the 18.8th percentile among its peers, against a peer median of 3.1%, it was typical for its peer group. Loan-loss reserves (money set aside for loans that may not be repaid) were 0.5% of loans, at the 2.6th percentile nationally, which is unusually low; at the 15.2nd percentile among its peers, against a peer median of 1.2%, they were typical for its peer group. Losses on bonds held to maturity (bonds the bank plans to keep until they are repaid) were 22.7% of equity (the owners' cushion), at the 96.1st percentile nationally, which is unusually high; at the 84.8th percentile among its peers, against a peer median of 0.6%, they were typical for its peer group.

Overall, 12 of the bank's ratios were in the national top or bottom 10%, and 5 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| volatile funding as a share of assets | 53.0% | 99.9th (unusually high) | 5.7% | 97.8th | unusually high among its peers too |
| loans as a share of deposits | 165.1% | 99.8th (unusually high) | 63.2% | 97.9th | unusually high among its peers too |
| deposit growth over the past four quarters | -35.5% | 0.4th (unusually low) | -5.0% | 2.1st | unusually low among its peers too |
| net interest margin (the spread earned on lending and investing) | 1.7% | 1.6th (unusually low) | 3.1% | 18.8th | typical for its peer group |
| core deposits as a share of assets | 25.2% | 2.1st (unusually low) | 72.1% | 6.5th | unusually low among its peers too |
| loan-loss reserves as a share of loans | 0.5% | 2.6th (unusually low) | 1.2% | 15.2nd | typical for its peer group |
| losses on bonds held to maturity, as a share of equity | 22.7% | 96.1st (unusually high) | 0.6% | 84.8th | typical for its peer group |
| Federal Home Loan Bank borrowings as a share of assets | 12.1% | 95.1st (unusually high) | 1.1% | 93.5th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 20.7% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 200.7% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 65.8% | 50% or more | yes |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why the model missed it

In hindsight, First Republic Bank failed on 2023-05-01, while the model had ranked it 809 and left it off the watchlist. The model learned from 539 failed banks, and 96% of those were credit-loss failures, where bad loans eat through capital. Of those failures, 462 were credit-loss only and just 53 combined credit losses with run risk, the danger of depositors pulling money quickly. This bank's loans looked clean, so the features the model weighs most heavily pointed toward safety.

A Run-risk rank (post-hoc check, designed after the 2023 failures) placed it at 895, so even that funding-focused check did not put it near the top. In a What-if (post-hoc check, designed after the 2023 failures) that set uninsured deposits as a share of deposits to each value from 0.0% to 100.0% with other data unchanged, the best rank reached was 543 of 4,740, at 0.0%. In a What-if (post-hoc check, designed after the 2023 failures) for losses on bonds held to maturity, as a share of equity, set from 0.0% to 150.0%, the best rank reached was 809 of 4,740, at 0.0%, the same as its actual rank. In a What-if (post-hoc check, designed after the 2023 failures) for losses on bonds available for sale, as a share of equity, set from 0.0% to 100.0%, the best rank reached was 298 of 4,740, at 30.0%.

## What happened next

In hindsight, the last quarter First Republic Bank reported was 2023-03-31, and it failed on 2023-05-01. Because it stopped reporting after that quarter, there are no later ranks or watchlist flags for it. Our data does not by itself distinguish a merger from a closure when a bank stops reporting, but the failure date in the fact sheet records the outcome.

## Sources

- F1 · Bank name · n/a · First Republic Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2023-03-31 · 2023-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · CA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2023-03-31 · 809 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2023-03-31 · 4,740 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2023-03-31 · 83.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2023-03-31 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2023-03-31 · 95 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2023-03-31 · 7.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2023-03-31 · 9.2% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2023-03-31 · 8.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2023-03-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2023-03-31 · 11.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2023-03-31 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2023-03-31 · 12.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2023-03-31 · 15.4% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2023-03-31 · 0.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2023-03-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2023-03-31 · 0.0% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2023-03-31 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2023-03-31 · 0.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2023-03-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2023-03-31 · 0.5% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2023-03-31 · 1.0% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2023-03-31 · 1.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2023-03-31 · 3.5% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F49 · Bank: loans as a share of deposits · 2023-03-31 · 165.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2023-03-31 · 73.4% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2023-03-31 · 48.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2023-03-31 · 24.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2023-03-31 · 25.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2023-03-31 · 80.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2023-03-31 · 12.1% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2023-03-31 · 0.5% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2023-03-31 · 53.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2023-03-31 · 6.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2023-03-31 · 22.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2023-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2023-03-31 · 2.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2023-03-31 · 15.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2023-03-31 · -35.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2023-03-31 · 0.0% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: volatile funding as a share of assets, value 53.0%; contribution to the score · 2023-03-31 · +0.357 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F76 · Driver up #2: commercial real estate loans as a share of loans, value 7.0%; contribution to the score · 2023-03-31 · +0.306 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F77 · Driver up #3: core deposits as a share of assets, value 25.2%; contribution to the score · 2023-03-31 · +0.090 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F78 · Driver up #4: loans as a share of deposits, value 165.1%; contribution to the score · 2023-03-31 · +0.072 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F79 · Driver up #5: equity as a share of assets, value 7.7%; contribution to the score · 2023-03-31 · +0.053 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 11.7%; contribution to the score · 2023-03-31 · -0.986 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: the Texas ratio (troubled assets against capital plus reserves), value 0.7%; contribution to the score · 2023-03-31 · -0.902 · data/analyst/scores.parquet: feature texas_ratio contribution
- F82 · Driver down #3: loans 90+ days past due or not accruing interest, as a share of loans, value 0.1%; contribution to the score · 2023-03-31 · -0.546 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F83 · Driver down #4: nonaccrual assets and foreclosed property, as a share of assets, value 0.1%; contribution to the score · 2023-03-31 · -0.286 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F84 · Driver down #5: return on equity (profit as a share of equity), value 6.1%; contribution to the score · 2023-03-31 · -0.259 · data/analyst/scores.parquet: feature return_on_equity contribution
- F85 · Failure date · 2023-05-01 · 2023-05-01 · data/raw/failures: FAILDATE
- F86 · Last quarter the bank reported · 2023-03-31 · 2023-03-31 · data/features/fct_bank_features.parquet: report_date
- F87 · Run-risk rank (post-hoc check, designed after the 2023 failures) · 2023-03-31 · 895 · data/replay/replay_banks.csv: run_risk_rank
- F88 · What-if (post-hoc check, designed after the 2023 failures): losses on bonds available for sale, as a share of equity set to each value from 0.0% to 100.0%, other data unchanged; best rank reached 298 of 4,740, at 30.0% · 2023-03-31 · 298 · data/replay/what_if.csv: rank (feature afs_unrealized_loss_to_equity)
- F89 · What-if (post-hoc check, designed after the 2023 failures): losses on bonds held to maturity, as a share of equity set to each value from 0.0% to 150.0%, other data unchanged; best rank reached 809 of 4,740, at 0.0% · 2023-03-31 · 809 · data/replay/what_if.csv: rank (feature htm_unrealized_loss_to_equity)
- F90 · What-if (post-hoc check, designed after the 2023 failures): uninsured deposits as a share of deposits set to each value from 0.0% to 100.0%, other data unchanged; best rank reached 543 of 4,740, at 0.0% · 2023-03-31 · 543 · data/replay/what_if.csv: rank (feature uninsured_to_deposits)
- F91 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F92 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F93 · Training failures with profile: credit-loss only · n/a · 462 · data/replay/posthoc_metrics.json: failure_mix.training
- F94 · Training failures with profile: credit-loss and run-risk · n/a · 53 · data/replay/posthoc_metrics.json: failure_mix.training
- F95 · Trend: volatile funding as a share of assets, value at the as-of quarter · 2023-03-31 · 53.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F96 · Trend: volatile funding as a share of assets, lowest value in the comparison window · n/a · 2.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F97 · Trend: volatile funding as a share of assets, highest value in the comparison window · n/a · 11.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F100 · Trend: volatile funding as a share of assets, contribution to the score (model log-odds units) · 2023-03-31 · +0.357 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F101 · Trend: volatile funding as a share of assets, what the model did with it · 2023-03-31 · pushed the score up · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F102 · Trend: loans as a share of deposits, value at the as-of quarter · 2023-03-31 · 165.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F103 · Trend: loans as a share of deposits, lowest value in the comparison window · n/a · 85.9% · data/features/fct_bank_features.parquet: loans_to_deposits
- F104 · Trend: loans as a share of deposits, highest value in the comparison window · n/a · 101.5% · data/features/fct_bank_features.parquet: loans_to_deposits
- F107 · Trend: loans as a share of deposits, contribution to the score (model log-odds units) · 2023-03-31 · +0.072 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F108 · Trend: loans as a share of deposits, what the model did with it · 2023-03-31 · pushed the score up · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F109 · Trend: core deposits as a share of assets, value at the as-of quarter · 2023-03-31 · 25.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F110 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 68.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F111 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 84.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F112 · Trend: core deposits as a share of assets, change over one quarter, in percentage points · 2023-03-31 · -48.3 pp · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F114 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2023-03-31 · +0.090 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F115 · Trend: core deposits as a share of assets, what the model did with it · 2023-03-31 · pushed the score up · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F116 · Trend: deposit growth over the past four quarters, value at the as-of quarter · 2023-03-31 · -35.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F117 · Trend: deposit growth over the past four quarters, lowest value in the comparison window · n/a · 12.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F118 · Trend: deposit growth over the past four quarters, highest value in the comparison window · n/a · 39.2% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F121 · Trend: deposit growth over the past four quarters, contribution to the score (model log-odds units) · 2023-03-31 · -0.136 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F122 · Trend: deposit growth over the past four quarters, what the model did with it · 2023-03-31 · pushed the score down · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F123 · Trend: uninsured deposits as a share of deposits, value at the as-of quarter · 2023-03-31 · 48.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F124 · Trend: uninsured deposits as a share of deposits, lowest value in the comparison window · n/a · 65.0% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F125 · Trend: uninsured deposits as a share of deposits, highest value in the comparison window · n/a · 74.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F128 · Trend: uninsured deposits as a share of deposits, contribution to the score (model log-odds units) · 2023-03-31 · -0.038 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F129 · Trend: uninsured deposits as a share of deposits, what the model did with it · 2023-03-31 · little effect on the score · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F130 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2023-03-31 · 6.8% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F131 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F132 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 3.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F135 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2023-03-31 · -0.110 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F136 · Trend: brokered deposits as a share of deposits, what the model did with it · 2023-03-31 · pushed the score down · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F137 · Trend: ratios outside their own prior range · 2023-03-31 · 13 · data/features/fct_bank_features.parquet
- F139 · Trend: ratios compared with their own prior range · 2023-03-31 · 30 · data/features/fct_bank_features.parquet
- F140 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F142 · Percentile a year earlier (100 = highest risk) · 2022-03-31 · 28.0% · data/analyst/scores.parquet: percentile
- F143 · Trend: how the model's rating compares with a year earlier · 2023-03-31 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F147 · Peers: volatile funding as a share of assets, bank value at the as-of quarter · 2023-03-31 · 53.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F148 · Peers: volatile funding as a share of assets, national percentile (100 = highest value among all banks) · 2023-03-31 · 99.9th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F149 · Peers: volatile funding as a share of assets, national reading · 2023-03-31 · unusually high · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F150 · Peers: volatile funding as a share of assets, percentile among its peers (100 = highest value) · 2023-03-31 · 97.8th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F151 · Peers: volatile funding as a share of assets, peer median · 2023-03-31 · 5.7% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F152 · Peers: volatile funding as a share of assets, reading against its peers · 2023-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F153 · Peers: loans as a share of deposits, bank value at the as-of quarter · 2023-03-31 · 165.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F154 · Peers: loans as a share of deposits, national percentile (100 = highest value among all banks) · 2023-03-31 · 99.8th · data/features/fct_bank_features.parquet: loans_to_deposits
- F155 · Peers: loans as a share of deposits, national reading · 2023-03-31 · unusually high · data/features/fct_bank_features.parquet: loans_to_deposits
- F156 · Peers: loans as a share of deposits, percentile among its peers (100 = highest value) · 2023-03-31 · 97.9th · data/features/fct_bank_features.parquet: loans_to_deposits
- F157 · Peers: loans as a share of deposits, peer median · 2023-03-31 · 63.2% · data/features/fct_bank_features.parquet: loans_to_deposits
- F158 · Peers: loans as a share of deposits, reading against its peers · 2023-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: loans_to_deposits
- F159 · Peers: deposit growth over the past four quarters, bank value at the as-of quarter · 2023-03-31 · -35.5% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F160 · Peers: deposit growth over the past four quarters, national percentile (100 = highest value among all banks) · 2023-03-31 · 0.4th · data/features/fct_bank_features.parquet: deposit_growth_4q
- F161 · Peers: deposit growth over the past four quarters, national reading · 2023-03-31 · unusually low · data/features/fct_bank_features.parquet: deposit_growth_4q
- F162 · Peers: deposit growth over the past four quarters, percentile among its peers (100 = highest value) · 2023-03-31 · 2.1st · data/features/fct_bank_features.parquet: deposit_growth_4q
- F163 · Peers: deposit growth over the past four quarters, peer median · 2023-03-31 · -5.0% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F164 · Peers: deposit growth over the past four quarters, reading against its peers · 2023-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: deposit_growth_4q
- F165 · Peers: net interest margin (the spread earned on lending and investing), bank value at the as-of quarter · 2023-03-31 · 1.7% · data/features/fct_bank_features.parquet: net_interest_margin
- F166 · Peers: net interest margin (the spread earned on lending and investing), national percentile (100 = highest value among all banks) · 2023-03-31 · 1.6th · data/features/fct_bank_features.parquet: net_interest_margin
- F167 · Peers: net interest margin (the spread earned on lending and investing), national reading · 2023-03-31 · unusually low · data/features/fct_bank_features.parquet: net_interest_margin
- F168 · Peers: net interest margin (the spread earned on lending and investing), percentile among its peers (100 = highest value) · 2023-03-31 · 18.8th · data/features/fct_bank_features.parquet: net_interest_margin
- F169 · Peers: net interest margin (the spread earned on lending and investing), peer median · 2023-03-31 · 3.1% · data/features/fct_bank_features.parquet: net_interest_margin
- F170 · Peers: net interest margin (the spread earned on lending and investing), reading against its peers · 2023-03-31 · typical for its peer group · data/features/fct_bank_features.parquet: net_interest_margin
- F171 · Peers: core deposits as a share of assets, bank value at the as-of quarter · 2023-03-31 · 25.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F172 · Peers: core deposits as a share of assets, national percentile (100 = highest value among all banks) · 2023-03-31 · 2.1st · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F173 · Peers: core deposits as a share of assets, national reading · 2023-03-31 · unusually low · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F174 · Peers: core deposits as a share of assets, percentile among its peers (100 = highest value) · 2023-03-31 · 6.5th · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F175 · Peers: core deposits as a share of assets, peer median · 2023-03-31 · 72.1% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F176 · Peers: core deposits as a share of assets, reading against its peers · 2023-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F177 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2023-03-31 · 0.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F178 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2023-03-31 · 2.6th · data/features/fct_bank_features.parquet: allowance_to_loans
- F179 · Peers: loan-loss reserves as a share of loans, national reading · 2023-03-31 · unusually low · data/features/fct_bank_features.parquet: allowance_to_loans
- F180 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2023-03-31 · 15.2nd · data/features/fct_bank_features.parquet: allowance_to_loans
- F181 · Peers: loan-loss reserves as a share of loans, peer median · 2023-03-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F182 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2023-03-31 · typical for its peer group · data/features/fct_bank_features.parquet: allowance_to_loans
- F183 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2023-03-31 · 22.7% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F184 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2023-03-31 · 96.1st · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F185 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2023-03-31 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F186 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2023-03-31 · 84.8th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F187 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2023-03-31 · 0.6% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F188 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2023-03-31 · typical for its peer group · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F189 · Peers: Federal Home Loan Bank borrowings as a share of assets, bank value at the as-of quarter · 2023-03-31 · 12.1% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F190 · Peers: Federal Home Loan Bank borrowings as a share of assets, national percentile (100 = highest value among all banks) · 2023-03-31 · 95.1st · data/features/fct_bank_features.parquet: fhlb_to_assets
- F191 · Peers: Federal Home Loan Bank borrowings as a share of assets, national reading · 2023-03-31 · unusually high · data/features/fct_bank_features.parquet: fhlb_to_assets
- F192 · Peers: Federal Home Loan Bank borrowings as a share of assets, percentile among its peers (100 = highest value) · 2023-03-31 · 93.5th · data/features/fct_bank_features.parquet: fhlb_to_assets
- F193 · Peers: Federal Home Loan Bank borrowings as a share of assets, peer median · 2023-03-31 · 1.1% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F194 · Peers: Federal Home Loan Bank borrowings as a share of assets, reading against its peers · 2023-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: fhlb_to_assets
- F196 · Peers: ratios in the national top or bottom 10% · 2023-03-31 · 12 · data/features/fct_bank_features.parquet
- F197 · Peers: those ratios also unusual among peers · 2023-03-31 · 5 · data/features/fct_bank_features.parquet
- F199 · Peers: cut-off for unusual (top or bottom share of banks) · 2023-03-31 · 10% · data/features/fct_bank_features.parquet
