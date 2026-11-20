---
cert: 25851
name: "Heartland Tri-State Bank"
as_of: 2023-03-31
rank: 329
n_banks: 4740
percentile: 93.08016877637131
flagged: false
outcome: "missed"
after_test_window: false
failure_date: 2023-07-28
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:13:20"
writer_model: "claude-opus-5-5"
checked: true
---

# Heartland Tri-State Bank (cert 25851)

*Hindsight: failed 2023-07-28. Canary did not flag it.*

## Summary

As of 2023-03-31, Heartland Tri-State Bank, a Kansas bank with $139.4 million in total assets, ranked 329 out of 4,740 banks nationally on Canary's risk score, placing it in the 93.1st percentile, where higher means riskier. It was not flagged on Canary's watchlist, which covers roughly the top 2% of banks by score. The biggest red flag was paper losses on bonds available for sale (bonds the bank could sell, valued at market prices) equal to 80.2% of equity, the owners' cushion, against a national median of 15.5%. Past-due loans were also unusually high, but strong risk-based capital and high profits pulled the score down, so the trend and peer findings point in different directions: the unusual moves over time did not raise the score, while the peer comparison shows clear credit warning signs.

## Warning signs in the data

Capital looked thin on a simple basis but strong on a risk-weighted basis: equity was 5.9% of assets against a national median of 9.2%, and the leverage ratio (core capital as a share of average assets) was 9.1% against a median of 10.4%. By contrast, the Tier 1 risk-based capital ratio (core capital measured against assets weighted by their riskiness) was 17.7%, well above the national median of 14.2%.

Credit quality showed strain: loans 90+ days past due or not accruing interest were 2.1% of loans against a national median of 0.2%, and loans 30-89 days past due were 1.7% of assets against a median of 0.2%. The Texas ratio (troubled assets against capital plus reserves) was 11.5%, well above the national median of 1.7%, and loan-loss reserves (money set aside for bad loans) were 2.1% of loans against a median of 1.2%. One measure points the other way: nonaccrual assets and foreclosed property were 0.1% of assets, the same as the national median of 0.1%.

The largest outlier was bond losses: losses on bonds available for sale equaled 80.2% of equity against a national median of 15.5%, with securities making up 39.9% of assets against a median of 22.0%. Funding looked steadier: core deposits (stable, everyday customer deposits) were 87.9% of assets against a median of 80.0%, brokered deposits were 0.0% in line with the median of 0.0%, and uninsured deposits were 26.7% of deposits, slightly above the median of 24.2%. Lending was light, with loans at 37.1% of deposits against a national median of 73.4%.

## Understanding the score

As of 2023-03-31, the bank ranked 329 out of 4,740 banks, in the 93.1st percentile on a scale of 0 to 100 where higher means riskier. It was not flagged on the watchlist, which covers the top 2% of banks, or 95 banks that quarter.

Five features pushed the score up the most. By far the largest was losses on bonds available for sale at 80.2% of equity, contributing +1.298. Next came equity as a share of assets at 5.9%, contributing +0.147, and construction loans as a share of loans at 0.0%, contributing +0.146. Commercial real estate loans at 4.9% of loans and loans at 37.1% of deposits each added only +0.018.

Five features pulled the score down. The largest was the Tier 1 risk-based capital ratio at 17.7%, contributing -1.078, followed by return on equity (profit as a share of the owners' stake) at 14.5%, contributing -0.606. The Texas ratio at 11.5% contributed -0.514, interest expense at 1.1% of assets contributed -0.495, and the total risk-based capital ratio at 18.9% contributed -0.356.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2021-06-30 | 2,387 | 5,015 |  |
| 2021-09-30 | 1,822 | 4,979 |  |
| 2021-12-31 | 2,742 | 4,904 |  |
| 2022-03-31 | 619 | 4,861 |  |
| 2022-06-30 | 1,146 | 4,838 |  |
| 2022-09-30 | 571 | 4,813 |  |
| 2022-12-31 | 1,349 | 4,773 |  |
| 2023-03-31 | 329 | 4,740 |  |

## How its ratios moved

As of 2023-03-31, Heartland Tri-State Bank ranked 329 out of 4,740 banks nationally, placing it in the 93.1st percentile, where higher means riskier. A year earlier, on 2022-03-31, it sat at the 87.3rd percentile, and the model rated it riskier than a year earlier. Each ratio is compared with its own past: for most ratios, the prior 12 quarters, and for year-to-date ratios, the same quarter in the prior 3 years. Of 30 ratios compared this way, 10 were outside their own prior range, and the 6 furthest outside are discussed here.

Each ratio's contribution is given in model log-odds units, where a positive number pushes the risk score up and a negative one pulls it down. Interest expense (what the bank pays on deposits and borrowings, shown yearly as a share of assets) was 1.1%, above its prior range of 0.3% to 0.8%, yet it pushed the score down, with a contribution of -0.495. That ratio rose +0.8 pp over four quarters. Return on equity (profit as a share of the owners' stake) was 14.5%, above its prior range of 8.2% to 13.7%, and it pushed the score down, with a contribution of -0.606. Securities (bonds and similar investments) made up 39.9% of assets, above their prior range of 29.9% to 39.2%, and they pushed the score down, with a contribution of -0.160. Core deposits (stable, everyday customer deposits) were 87.9% of assets, above their prior range of 78.2% to 87.3%, and they pushed the score down, with a contribution of -0.079.

Cash made up 6.6% of assets, above its prior range of 2.9% to 5.6%, but it had little effect on the score, with a contribution of -0.037. Loans as a share of deposits were 37.1%, below their prior range of 39.2% to 66.1%, and this ratio also had little effect on the score, with a contribution of +0.018. So although all six of these ratios moved outside their usual ranges, none of them pushed the score up in a meaningful way.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| cash as a share of assets | 6.6% | 2.9% to 5.6% | prior 12 quarters | +1.0 pp | +1.3 pp | -0.037 | little effect on the score |
| annualized interest expense as a share of assets | 1.1% | 0.3% to 0.8% | same quarter, prior 3 years | n/a | +0.8 pp | -0.495 | pushed the score down |
| return on equity (profit as a share of equity) | 14.5% | 8.2% to 13.7% | same quarter, prior 3 years | n/a | +6.4 pp | -0.606 | pushed the score down |
| loans as a share of deposits | 37.1% | 39.2% to 66.1% | prior 12 quarters | -4.4 pp | -5.3 pp | +0.018 | little effect on the score |
| core deposits as a share of assets | 87.9% | 78.2% to 87.3% | prior 12 quarters | +0.6 pp | +2.1 pp | -0.079 | pushed the score down |
| securities as a share of assets | 39.9% | 29.9% to 39.2% | prior 12 quarters | +2.1 pp | +4.4 pp | -0.160 | pushed the score down |

10 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2023-03-31: Agricultural Specialization.

Peers: 668 banks in the same specialty group and size tier ($100 million to $1 billion).

As of 2023-03-31, Heartland Tri-State Bank ranked 329 out of 4,740 banks nationally on Canary's score, placing it at the 93.1st percentile, where a higher percentile means a higher score. Loans 30-89 days past due (borrowers who are behind on payments) equal 1.7% of assets, at the 97.0th percentile nationally, which is unusually high; against its peers it sits at the 97.5th percentile versus a peer median of 0.2%, which is unusually high among its peers too. Loans 90+ days past due or not accruing interest (loans that have largely stopped paying) are 2.1% of loans, at the 94.3rd percentile nationally, which is unusually high; among peers it is at the 93.6th percentile versus a peer median of 0.2%, which is unusually high among its peers too. The Texas ratio (troubled assets against capital plus reserves) is 11.5%, at the 92.6th percentile nationally, which is unusually high; among peers it is at the 92.4th percentile versus a peer median of 1.4%, which is unusually high among its peers too. Losses on bonds available for sale (bonds the bank could sell, valued at market prices) equal 80.2% of equity (the owners' cushion), at the 93.3rd percentile nationally, which is unusually high; among peers it is at the 92.0th percentile versus a peer median of 22.0%, which is unusually high among its peers too.

Loan-loss reserves (money set aside for expected bad loans) are 2.1% of loans, at the 91.9th percentile nationally, which is unusually high; among peers it is at the 90.6th percentile versus a peer median of 1.3%, which is unusually high among its peers too. Loans as a share of deposits are 37.1%, at the 8.5th percentile nationally, which is unusually low; among peers it is at the 6.7th percentile versus a peer median of 68.2%, which is unusually low among its peers too. Construction loans as a share of loans are 0.0%, at the 4.2nd percentile nationally, which is unusually low; among peers it is at the 3.4th percentile versus a peer median of 2.3%, which is unusually low among its peers too. Annualized loan write-offs, net of recoveries (loans written off as uncollectable, minus amounts later recovered), are -0.1% of loans, at the 5.9th percentile nationally, which is unusually low; among peers it is at the 7.6th percentile versus a peer median of 0.0%, which is unusually low among its peers too. Overall, 9 of the bank's ratios fall in the national top or bottom 10%, and 8 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| loans 30-89 days past due, as a share of assets | 1.7% | 97.0th (unusually high) | 0.2% | 97.5th | unusually high among its peers too |
| construction loans as a share of loans | 0.0% | 4.2nd (unusually low) | 2.3% | 3.4th | unusually low among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 2.1% | 94.3rd (unusually high) | 0.2% | 93.6th | unusually high among its peers too |
| annualized loan write-offs, net of recoveries, as a share of loans | -0.1% | 5.9th (unusually low) | 0.0% | 7.6th | unusually low among its peers too |
| losses on bonds available for sale, as a share of equity | 80.2% | 93.3rd (unusually high) | 22.0% | 92.0th | unusually high among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 11.5% | 92.6th (unusually high) | 1.4% | 92.4th | unusually high among its peers too |
| loan-loss reserves as a share of loans | 2.1% | 91.9th (unusually high) | 1.3% | 90.6th | unusually high among its peers too |
| loans as a share of deposits | 37.1% | 8.5th (unusually low) | 68.2% | 6.7th | unusually low among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 4.0% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 63.9% | 50% or more | yes |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why the model missed it

In hindsight, the bank failed on 2023-07-28, and its last reported quarter was 2023-03-31, so the model's final reading of it was the one described above. At that point it ranked 329, high in the national ranking but outside the watchlist of 95 banks, so the model did not flag it.

The data show why the score stayed below the watchlist line: strong risk-based capital, with a Tier 1 ratio of 17.7%, and high profits, with return on equity of 14.5%, pulled the score down. Some readings that looked troubling against other banks, such as the Texas ratio of 11.5%, also pulled the score down rather than up, while past-due loans were not among the main drivers. The data cannot tell us what ultimately caused the failure.

## What happened next

In hindsight, Heartland Tri-State Bank failed on 2023-07-28. Its last reported quarter was 2023-03-31, so there are no later ranks or watchlist flags for it.

## Sources

- F1 · Bank name · n/a · Heartland Tri-State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2023-03-31 · 2023-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · KS · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2023-03-31 · 329 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2023-03-31 · 4,740 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2023-03-31 · 93.1% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2023-03-31 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2023-03-31 · 95 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2023-03-31 · 5.9% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2023-03-31 · 9.2% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2023-03-31 · 9.1% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2023-03-31 · 10.4% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2023-03-31 · 17.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2023-03-31 · 14.2% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2023-03-31 · 2.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2023-03-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F23 · Bank: nonaccrual assets and foreclosed property, as a share of assets · 2023-03-31 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets
- F24 · National median: nonaccrual assets and foreclosed property, as a share of assets · 2023-03-31 · 0.1% · data/features/fct_bank_features.parquet: nonaccrual_ore_to_assets (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2023-03-31 · 1.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2023-03-31 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2023-03-31 · 2.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2023-03-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2023-03-31 · 11.5% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2023-03-31 · 1.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F49 · Bank: loans as a share of deposits · 2023-03-31 · 37.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2023-03-31 · 73.4% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2023-03-31 · 26.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2023-03-31 · 24.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2023-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2023-03-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2023-03-31 · 87.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2023-03-31 · 80.0% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2023-03-31 · 80.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2023-03-31 · 15.5% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2023-03-31 · 39.9% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2023-03-31 · 22.0% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F69 · Bank: total assets · 2023-03-31 · $139.4 million · data/features/fct_bank_features.parquet: log_total_assets
- F75 · Driver up #1: losses on bonds available for sale, as a share of equity, value 80.2%; contribution to the score · 2023-03-31 · +1.298 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F76 · Driver up #2: equity as a share of assets, value 5.9%; contribution to the score · 2023-03-31 · +0.147 · data/analyst/scores.parquet: feature equity_to_assets contribution
- F77 · Driver up #3: construction loans as a share of loans, value 0.0%; contribution to the score · 2023-03-31 · +0.146 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F78 · Driver up #4: commercial real estate loans as a share of loans, value 4.9%; contribution to the score · 2023-03-31 · +0.018 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F79 · Driver up #5: loans as a share of deposits, value 37.1%; contribution to the score · 2023-03-31 · +0.018 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 17.7%; contribution to the score · 2023-03-31 · -1.078 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 14.5%; contribution to the score · 2023-03-31 · -0.606 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 11.5%; contribution to the score · 2023-03-31 · -0.514 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: annualized interest expense as a share of assets, value 1.1%; contribution to the score · 2023-03-31 · -0.495 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F84 · Driver down #5: the total risk-based capital ratio, value 18.9%; contribution to the score · 2023-03-31 · -0.356 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F85 · Failure date · 2023-07-28 · 2023-07-28 · data/raw/failures: FAILDATE
- F86 · Last quarter the bank reported · 2023-03-31 · 2023-03-31 · data/features/fct_bank_features.parquet: report_date
- F91 · Trend: cash as a share of assets, value at the as-of quarter · 2023-03-31 · 6.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F92 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 2.9% · data/features/fct_bank_features.parquet: cash_to_assets
- F93 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 5.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F96 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2023-03-31 · -0.037 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F97 · Trend: cash as a share of assets, what the model did with it · 2023-03-31 · little effect on the score · data/analyst/scores.parquet: feature cash_to_assets contribution
- F98 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2023-03-31 · 1.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F99 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F100 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F101 · Trend: annualized interest expense as a share of assets, change over four quarters, in percentage points · 2023-03-31 · +0.8 pp · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F102 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2023-03-31 · -0.495 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F103 · Trend: annualized interest expense as a share of assets, what the model did with it · 2023-03-31 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F104 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2023-03-31 · 14.5% · data/features/fct_bank_features.parquet: return_on_equity
- F105 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 8.2% · data/features/fct_bank_features.parquet: return_on_equity
- F106 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 13.7% · data/features/fct_bank_features.parquet: return_on_equity
- F108 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2023-03-31 · -0.606 · data/analyst/scores.parquet: feature return_on_equity contribution
- F109 · Trend: return on equity (profit as a share of equity), what the model did with it · 2023-03-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F110 · Trend: loans as a share of deposits, value at the as-of quarter · 2023-03-31 · 37.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F111 · Trend: loans as a share of deposits, lowest value in the comparison window · n/a · 39.2% · data/features/fct_bank_features.parquet: loans_to_deposits
- F112 · Trend: loans as a share of deposits, highest value in the comparison window · n/a · 66.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F115 · Trend: loans as a share of deposits, contribution to the score (model log-odds units) · 2023-03-31 · +0.018 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F116 · Trend: loans as a share of deposits, what the model did with it · 2023-03-31 · little effect on the score · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F117 · Trend: core deposits as a share of assets, value at the as-of quarter · 2023-03-31 · 87.9% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F118 · Trend: core deposits as a share of assets, lowest value in the comparison window · n/a · 78.2% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F119 · Trend: core deposits as a share of assets, highest value in the comparison window · n/a · 87.3% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F122 · Trend: core deposits as a share of assets, contribution to the score (model log-odds units) · 2023-03-31 · -0.079 · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F123 · Trend: core deposits as a share of assets, what the model did with it · 2023-03-31 · pushed the score down · data/analyst/scores.parquet: feature core_deposits_to_assets contribution
- F124 · Trend: securities as a share of assets, value at the as-of quarter · 2023-03-31 · 39.9% · data/features/fct_bank_features.parquet: securities_to_assets
- F125 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 29.9% · data/features/fct_bank_features.parquet: securities_to_assets
- F126 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 39.2% · data/features/fct_bank_features.parquet: securities_to_assets
- F129 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2023-03-31 · -0.160 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F130 · Trend: securities as a share of assets, what the model did with it · 2023-03-31 · pushed the score down · data/analyst/scores.parquet: feature securities_to_assets contribution
- F131 · Trend: ratios outside their own prior range · 2023-03-31 · 10 · data/features/fct_bank_features.parquet
- F132 · Trend: ratios shown in the table (the furthest outside their prior range) · 2023-03-31 · 6 · data/features/fct_bank_features.parquet
- F133 · Trend: ratios compared with their own prior range · 2023-03-31 · 30 · data/features/fct_bank_features.parquet
- F134 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F135 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F136 · Percentile a year earlier (100 = highest risk) · 2022-03-31 · 87.3% · data/analyst/scores.parquet: percentile
- F137 · Trend: how the model's rating compares with a year earlier · 2023-03-31 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F141 · Peers: loans 30-89 days past due, as a share of assets, bank value at the as-of quarter · 2023-03-31 · 1.7% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F142 · Peers: loans 30-89 days past due, as a share of assets, national percentile (100 = highest value among all banks) · 2023-03-31 · 97.0th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F143 · Peers: loans 30-89 days past due, as a share of assets, national reading · 2023-03-31 · unusually high · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F144 · Peers: loans 30-89 days past due, as a share of assets, percentile among its peers (100 = highest value) · 2023-03-31 · 97.5th · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F145 · Peers: loans 30-89 days past due, as a share of assets, peer median · 2023-03-31 · 0.2% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F146 · Peers: loans 30-89 days past due, as a share of assets, reading against its peers · 2023-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F147 · Peers: construction loans as a share of loans, bank value at the as-of quarter · 2023-03-31 · 0.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F148 · Peers: construction loans as a share of loans, national percentile (100 = highest value among all banks) · 2023-03-31 · 4.2nd · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F149 · Peers: construction loans as a share of loans, national reading · 2023-03-31 · unusually low · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F150 · Peers: construction loans as a share of loans, percentile among its peers (100 = highest value) · 2023-03-31 · 3.4th · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F151 · Peers: construction loans as a share of loans, peer median · 2023-03-31 · 2.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F152 · Peers: construction loans as a share of loans, reading against its peers · 2023-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F153 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2023-03-31 · 2.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F154 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2023-03-31 · 94.3rd · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F155 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2023-03-31 · unusually high · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F156 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2023-03-31 · 93.6th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F157 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2023-03-31 · 0.2% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F158 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2023-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F159 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, bank value at the as-of quarter · 2023-03-31 · -0.1% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F160 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national percentile (100 = highest value among all banks) · 2023-03-31 · 5.9th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F161 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, national reading · 2023-03-31 · unusually low · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F162 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, percentile among its peers (100 = highest value) · 2023-03-31 · 7.6th · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F163 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, peer median · 2023-03-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F164 · Peers: annualized loan write-offs, net of recoveries, as a share of loans, reading against its peers · 2023-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F165 · Peers: losses on bonds available for sale, as a share of equity, bank value at the as-of quarter · 2023-03-31 · 80.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F166 · Peers: losses on bonds available for sale, as a share of equity, national percentile (100 = highest value among all banks) · 2023-03-31 · 93.3rd · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F167 · Peers: losses on bonds available for sale, as a share of equity, national reading · 2023-03-31 · unusually high · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F168 · Peers: losses on bonds available for sale, as a share of equity, percentile among its peers (100 = highest value) · 2023-03-31 · 92.0th · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F169 · Peers: losses on bonds available for sale, as a share of equity, peer median · 2023-03-31 · 22.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F170 · Peers: losses on bonds available for sale, as a share of equity, reading against its peers · 2023-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F171 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2023-03-31 · 11.5% · data/features/fct_bank_features.parquet: texas_ratio
- F172 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2023-03-31 · 92.6th · data/features/fct_bank_features.parquet: texas_ratio
- F173 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2023-03-31 · unusually high · data/features/fct_bank_features.parquet: texas_ratio
- F174 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2023-03-31 · 92.4th · data/features/fct_bank_features.parquet: texas_ratio
- F175 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2023-03-31 · 1.4% · data/features/fct_bank_features.parquet: texas_ratio
- F176 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2023-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F177 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2023-03-31 · 2.1% · data/features/fct_bank_features.parquet: allowance_to_loans
- F178 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2023-03-31 · 91.9th · data/features/fct_bank_features.parquet: allowance_to_loans
- F179 · Peers: loan-loss reserves as a share of loans, national reading · 2023-03-31 · unusually high · data/features/fct_bank_features.parquet: allowance_to_loans
- F180 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2023-03-31 · 90.6th · data/features/fct_bank_features.parquet: allowance_to_loans
- F181 · Peers: loan-loss reserves as a share of loans, peer median · 2023-03-31 · 1.3% · data/features/fct_bank_features.parquet: allowance_to_loans
- F182 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2023-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F183 · Peers: loans as a share of deposits, bank value at the as-of quarter · 2023-03-31 · 37.1% · data/features/fct_bank_features.parquet: loans_to_deposits
- F184 · Peers: loans as a share of deposits, national percentile (100 = highest value among all banks) · 2023-03-31 · 8.5th · data/features/fct_bank_features.parquet: loans_to_deposits
- F185 · Peers: loans as a share of deposits, national reading · 2023-03-31 · unusually low · data/features/fct_bank_features.parquet: loans_to_deposits
- F186 · Peers: loans as a share of deposits, percentile among its peers (100 = highest value) · 2023-03-31 · 6.7th · data/features/fct_bank_features.parquet: loans_to_deposits
- F187 · Peers: loans as a share of deposits, peer median · 2023-03-31 · 68.2% · data/features/fct_bank_features.parquet: loans_to_deposits
- F188 · Peers: loans as a share of deposits, reading against its peers · 2023-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: loans_to_deposits
- F190 · Peers: ratios in the national top or bottom 10% · 2023-03-31 · 9 · data/features/fct_bank_features.parquet
- F191 · Peers: those ratios also unusual among peers · 2023-03-31 · 8 · data/features/fct_bank_features.parquet
- F193 · Peers: cut-off for unusual (top or bottom share of banks) · 2023-03-31 · 10% · data/features/fct_bank_features.parquet
