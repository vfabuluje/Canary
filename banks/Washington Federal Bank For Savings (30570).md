---
cert: 30570
name: "Washington Federal Bank For Savings"
as_of: 2017-09-30
rank: 3736
n_banks: 5806
percentile: 35.66999655528763
flagged: false
outcome: "missed"
after_test_window: false
failure_date: 2017-12-15
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:13:39"
writer_model: "claude-opus-5-5"
checked: true
---

# Washington Federal Bank For Savings (cert 30570)

*Hindsight: failed 2017-12-15. Canary did not flag it.*

## Summary

As of 2017-09-30, Washington Federal Bank For Savings, a lender based in IL, ranked 3,736 out of 5,806 banks nationally on Canary's score, which places it at the 35.7th percentile, where higher means riskier. It was not flagged on the watchlist, which covers the riskiest 2% of banks. The model rated it riskier than a year earlier, when it sat at the 27.4th percentile, but its reported figures still showed strong capital, almost no troubled loans and above-median profits. The main oddities were high funding costs, a large share of volatile funding and no bond holdings at all.

## Warning signs in the data

Capital, the bank's own cushion against losses, was well above the national median: equity was 12.7% of assets against a median of 11.0%, and the leverage ratio (core capital as a share of average assets) was 12.6% against 10.6%. Its risk-based capital ratios, which weigh assets by how risky they are, were far above the median, with the Tier 1 ratio at 24.7% against 15.1% and the total ratio at 25.5% against 16.3%. Credit quality looked clean: loans 90 or more days late or no longer paying interest were 0.0% of loans against a median of 0.6%, and the Texas ratio (troubled assets against capital plus reserves) was 0.0% against 4.5%. One soft spot is loan-loss reserves, money set aside for bad loans, at 0.4% of loans against a national median of 1.2%, although the peer section finds this typical for its mortgage-lending peer group.

Funding stood out more: interest expense, the yearly cost of its deposits and borrowings, was 1.0% of assets against a national median of 0.4%. Volatile funding, money that can leave quickly, was 15.0% of assets, well above the national median of 5.9%, though the peer section rates this typical among its peers, so the two views point different ways. Loans were 94.5% of deposits against a median of 80.7%, while uninsured deposits, balances above the government guarantee, were lower than usual at 10.6% against 17.8%. The bank held 0.0% of assets in securities such as bonds against a median of 17.4%, but kept 14.1% in cash against 6.1%. With no bonds, it showed no bond losses: losses on bonds held to maturity and on bonds available for sale were both 0.0% of equity, matching the national median of 0.0%.

## Understanding the score

As of 2017-09-30, the bank ranked 3,736 out of 5,806 banks, placing it at the 35.7th percentile on a scale where higher means riskier. It was not flagged on the watchlist, which held 117 banks that quarter, the top 2% of banks.

The five features that pushed the score up most were securities as a share of assets at 0.0% (+0.376), commercial real estate loans as a share of loans at 6.7% (+0.118), cash as a share of assets at 14.1% (+0.006), Federal Home Loan Bank borrowings as a share of assets at 0.0% (+0.004), and loan-loss reserves as a share of loans at 0.4% (+0.004). The five that pushed it down most were the total risk-based capital ratio at 25.5% (-0.919), the Tier 1 risk-based capital ratio at 24.7% (-0.916), the Texas ratio at 0.0% (-0.868), interest expense as a share of assets at 1.0% (-0.607), and return on equity, profit as a share of the owners' stake, at 11.5% (-0.533). The downward pushes were much larger than the upward ones, which is why the bank sat in the lower half of the ranking.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2016-03-31 | 3,840 | 6,193 |  |
| 2016-06-30 | 4,173 | 6,129 |  |
| 2016-09-30 | 4,396 | 6,051 |  |
| 2016-12-31 | 5,383 | 5,983 |  |
| 2017-03-31 | 5,302 | 5,925 |  |
| 2017-06-30 | 4,039 | 5,856 |  |
| 2017-09-30 | 3,736 | 5,806 |  |

## How its ratios moved

As of 2017-09-30, Washington Federal Bank For Savings ranked 3,736 out of 5,806 banks nationally, which places it at the 35.7th percentile, where higher means riskier. A year earlier, on 2016-09-30, it sat at the 27.4th percentile, so the model rated it riskier than a year earlier. Each ratio was compared with its own history: most against the prior 12 quarters, and year-to-date ratios against the same quarter in the prior 3 years. Of 30 ratios checked this way, 15 were outside their own prior range, and the 6 furthest outside are discussed here. Each ratio's contribution is given in model log-odds units, the model's internal scale, where a positive number pushes the score up and a negative one pushes it down.

Construction loans as a share of loans were 2.9%, above their prior range of 0.4% to 2.2%, yet this ratio pushed the score down, with a contribution of -0.184. The leverage ratio, core capital (the bank's own cushion of funds) as a share of average assets, was 12.6%, above its prior range of 11.2% to 12.5%, and it pushed the score down, with a contribution of -0.516. Volatile funding, money that tends to be less stable than ordinary deposits, was 15.0% of assets, above its prior range of 11.0% to 14.6%, yet it pushed the score down, with a contribution of -0.070.

Return on equity, profit as a share of the owners' stake, was 11.5%, below its prior range of 12.6% to 14.0%, yet it pushed the score down, with a contribution of -0.533. Return on assets, profit as a share of assets, was 1.4%, just below a prior range of 1.5% to 1.5%, and it pushed the score down, with a contribution of -0.193. Net interest margin, the spread earned on lending and investing, was 4.57%, below its prior range of 4.63% to 4.9%, but it had little effect on the score, with a contribution of -0.047.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 11.5% | 12.6% to 14.0% | same quarter, prior 3 years | n/a | -1.1 pp | -0.533 | pushed the score down |
| construction loans as a share of loans | 2.9% | 0.4% to 2.2% | prior 12 quarters | +0.9 pp | +1.0 pp | -0.184 | pushed the score down |
| the leverage ratio (core capital as a share of average assets) | 12.6% | 11.2% to 12.5% | prior 12 quarters | +0.3 pp | +0.4 pp | -0.516 | pushed the score down |
| volatile funding as a share of assets | 15.0% | 11.0% to 14.6% | prior 12 quarters | +0.4 pp | +1.4 pp | -0.070 | pushed the score down |
| return on assets (profit as a share of assets) | 1.4% | 1.5% to 1.5% | same quarter, prior 3 years | n/a | -0.1 pp | -0.193 | pushed the score down |
| net interest margin (the spread earned on lending and investing) | 4.57% | 4.63% to 4.9% | same quarter, prior 3 years | n/a | -0.1 pp | -0.047 | little effect on the score |

15 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2017-09-30: Mortgage Lending Specialization.

Peers: 265 banks in the same specialty group and size tier ($100 million to $1 billion).

As of 2017-09-30, the bank ranked 3,736 out of 5,806 banks nationally, placing it at the 35.7th percentile of Canary's score. Its interest expense, the yearly cost of paying for its deposits and borrowings as a share of assets, was 1.0%, at the 97.4th percentile nationally (unusually high), and at the 94.5th percentile among its peers against a peer median of 0.5%, which is unusually high among its peers too. Its net interest margin, the spread earned on lending and investing, was 4.6%, at the 91.0th percentile nationally (unusually high), and at the 97.2nd percentile among its peers against a peer median of 3.2%, which is unusually high among its peers too. Volatile funding, money that can leave quickly, was 15.0% of assets, at the 90.7th percentile nationally (unusually high), and at the 88.9th percentile among its peers against a peer median of 6.4%, which is typical for its peer group.

Loan-loss reserves, money set aside to cover bad loans, were 0.4% of loans, at the 2.9th percentile nationally (unusually low), and at the 12.7th percentile among its peers against a peer median of 0.9%, which is typical for its peer group. Securities such as bonds made up 0.0% of assets, at the 3.2nd percentile nationally (unusually low), and at the 2.1st percentile among its peers against a peer median of 17.7%, which is unusually low among its peers too. The Texas ratio, troubled assets measured against capital plus reserves, was 0.0%, at the 4.4th percentile nationally (unusually low), and at the 2.6th percentile among its peers against a peer median of 4.6%, which is unusually low among its peers too. Loans 90 or more days past due or no longer paying interest were 0.0% of loans, at the 4.7th percentile nationally (unusually low), and at the 2.5th percentile among its peers against a peer median of 0.7%, which is unusually low among its peers too. The efficiency ratio, operating costs as a share of revenue, was 46.6%, at the 6.2nd percentile nationally (unusually low), and at the 1.7th percentile among its peers against a peer median of 77.3%, which is unusually low among its peers too.

Overall, 8 of the bank's ratios fell in the national top or bottom 10%, and 6 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| annualized interest expense as a share of assets | 1.0% | 97.4th (unusually high) | 0.5% | 94.5th | unusually high among its peers too |
| loan-loss reserves as a share of loans | 0.4% | 2.9th (unusually low) | 0.9% | 12.7th | typical for its peer group |
| securities as a share of assets | 0.0% | 3.2nd (unusually low) | 17.7% | 2.1st | unusually low among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 0.0% | 4.4th (unusually low) | 4.6% | 2.6th | unusually low among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 0.0% | 4.7th (unusually low) | 0.7% | 2.5th | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 46.6% | 6.2nd (unusually low) | 77.3% | 1.7th | unusually low among its peers too |
| net interest margin (the spread earned on lending and investing) | 4.6% | 91.0th (unusually high) | 3.2% | 97.2nd | unusually high among its peers too |
| volatile funding as a share of assets | 15.0% | 90.7th (unusually high) | 6.4% | 88.9th | typical for its peer group |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: total risk-based capital, as the 2006 guidance specifies.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 18.8% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 62.5% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | 22.8% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why the model missed it

In hindsight, the bank failed on 2017-12-15, and its last reported quarter was 2017-09-30, the same quarter this memo describes. The model missed it because the reported figures looked healthy: very high capital and a Texas ratio of 0.0% were the strongest forces pulling the score down. The model learned mostly from failures driven by loan losses, which made up 96% of the 539 failures in its training period, and this bank's reports showed almost no troubled loans. Whatever caused the failure did not show up in the figures the model sees.

## What happened next

In hindsight, the bank failed on 2017-12-15. Its last reported quarter was 2017-09-30, so our data hold no later ranks or watchlist flags for it. Our data record only that the bank stopped reporting; they do not distinguish a merger from a closure.

## Sources

- F1 · Bank name · n/a · Washington Federal Bank For Savings · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2017-09-30 · 2017-09-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · IL · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2017-09-30 · 3,736 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2017-09-30 · 5,806 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2017-09-30 · 35.7% · data/analyst/scores.parquet: percentile
- F10 · On the watchlist · 2017-09-30 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2017-09-30 · 117 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2017-09-30 · 12.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2017-09-30 · 11.0% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2017-09-30 · 12.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2017-09-30 · 10.6% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2017-09-30 · 24.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2017-09-30 · 15.1% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2017-09-30 · 25.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2017-09-30 · 16.3% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2017-09-30 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2017-09-30 · 0.4% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2017-09-30 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2017-09-30 · 4.5% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2017-09-30 · 1.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2017-09-30 · 0.4% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F49 · Bank: loans as a share of deposits · 2017-09-30 · 94.5% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2017-09-30 · 80.7% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2017-09-30 · 10.6% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2017-09-30 · 17.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2017-09-30 · 15.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2017-09-30 · 5.9% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2017-09-30 · 14.1% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2017-09-30 · 6.1% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F67 · Bank: securities as a share of assets · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F68 · National median: securities as a share of assets · 2017-09-30 · 17.4% · data/features/fct_bank_features.parquet: securities_to_assets (median of all banks)
- F75 · Driver up #1: securities as a share of assets, value 0.0%; contribution to the score · 2017-09-30 · +0.376 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F76 · Driver up #2: commercial real estate loans as a share of loans, value 6.7%; contribution to the score · 2017-09-30 · +0.118 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F77 · Driver up #3: cash as a share of assets, value 14.1%; contribution to the score · 2017-09-30 · +0.006 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F78 · Driver up #4: Federal Home Loan Bank borrowings as a share of assets, value 0.0%; contribution to the score · 2017-09-30 · +0.004 · data/analyst/scores.parquet: feature fhlb_to_assets contribution
- F79 · Driver up #5: loan-loss reserves as a share of loans, value 0.4%; contribution to the score · 2017-09-30 · +0.004 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F80 · Driver down #1: the total risk-based capital ratio, value 25.5%; contribution to the score · 2017-09-30 · -0.919 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 24.7%; contribution to the score · 2017-09-30 · -0.916 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: the Texas ratio (troubled assets against capital plus reserves), value 0.0%; contribution to the score · 2017-09-30 · -0.868 · data/analyst/scores.parquet: feature texas_ratio contribution
- F83 · Driver down #4: annualized interest expense as a share of assets, value 1.0%; contribution to the score · 2017-09-30 · -0.607 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F84 · Driver down #5: return on equity (profit as a share of equity), value 11.5%; contribution to the score · 2017-09-30 · -0.533 · data/analyst/scores.parquet: feature return_on_equity contribution
- F85 · Failure date · 2017-12-15 · 2017-12-15 · data/raw/failures: FAILDATE
- F86 · Last quarter the bank reported · 2017-09-30 · 2017-09-30 · data/features/fct_bank_features.parquet: report_date
- F87 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F88 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F91 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2017-09-30 · 11.5% · data/features/fct_bank_features.parquet: return_on_equity
- F92 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 12.6% · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 14.0% · data/features/fct_bank_features.parquet: return_on_equity
- F95 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2017-09-30 · -0.533 · data/analyst/scores.parquet: feature return_on_equity contribution
- F96 · Trend: return on equity (profit as a share of equity), what the model did with it · 2017-09-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F97 · Trend: construction loans as a share of loans, value at the as-of quarter · 2017-09-30 · 2.9% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F98 · Trend: construction loans as a share of loans, lowest value in the comparison window · n/a · 0.4% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F99 · Trend: construction loans as a share of loans, highest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F102 · Trend: construction loans as a share of loans, contribution to the score (model log-odds units) · 2017-09-30 · -0.184 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F103 · Trend: construction loans as a share of loans, what the model did with it · 2017-09-30 · pushed the score down · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F104 · Trend: the leverage ratio (core capital as a share of average assets), value at the as-of quarter · 2017-09-30 · 12.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F105 · Trend: the leverage ratio (core capital as a share of average assets), lowest value in the comparison window · n/a · 11.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F106 · Trend: the leverage ratio (core capital as a share of average assets), highest value in the comparison window · n/a · 12.5% · data/features/fct_bank_features.parquet: leverage_ratio
- F109 · Trend: the leverage ratio (core capital as a share of average assets), contribution to the score (model log-odds units) · 2017-09-30 · -0.516 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F110 · Trend: the leverage ratio (core capital as a share of average assets), what the model did with it · 2017-09-30 · pushed the score down · data/analyst/scores.parquet: feature leverage_ratio contribution
- F111 · Trend: volatile funding as a share of assets, value at the as-of quarter · 2017-09-30 · 15.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F112 · Trend: volatile funding as a share of assets, lowest value in the comparison window · n/a · 11.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F113 · Trend: volatile funding as a share of assets, highest value in the comparison window · n/a · 14.6% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F116 · Trend: volatile funding as a share of assets, contribution to the score (model log-odds units) · 2017-09-30 · -0.070 · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F117 · Trend: volatile funding as a share of assets, what the model did with it · 2017-09-30 · pushed the score down · data/analyst/scores.parquet: feature volatile_liabilities_to_assets contribution
- F118 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2017-09-30 · 1.4% · data/features/fct_bank_features.parquet: return_on_assets
- F119 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 1.5% · data/features/fct_bank_features.parquet: return_on_assets
- F120 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 1.5% · data/features/fct_bank_features.parquet: return_on_assets
- F122 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2017-09-30 · -0.193 · data/analyst/scores.parquet: feature return_on_assets contribution
- F123 · Trend: return on assets (profit as a share of assets), what the model did with it · 2017-09-30 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F124 · Trend: net interest margin (the spread earned on lending and investing), value at the as-of quarter · 2017-09-30 · 4.57% · data/features/fct_bank_features.parquet: net_interest_margin
- F125 · Trend: net interest margin (the spread earned on lending and investing), lowest value in the comparison window · n/a · 4.63% · data/features/fct_bank_features.parquet: net_interest_margin
- F126 · Trend: net interest margin (the spread earned on lending and investing), highest value in the comparison window · n/a · 4.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F128 · Trend: net interest margin (the spread earned on lending and investing), contribution to the score (model log-odds units) · 2017-09-30 · -0.047 · data/analyst/scores.parquet: feature net_interest_margin contribution
- F129 · Trend: net interest margin (the spread earned on lending and investing), what the model did with it · 2017-09-30 · little effect on the score · data/analyst/scores.parquet: feature net_interest_margin contribution
- F130 · Trend: ratios outside their own prior range · 2017-09-30 · 15 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios shown in the table (the furthest outside their prior range) · 2017-09-30 · 6 · data/features/fct_bank_features.parquet
- F132 · Trend: ratios compared with their own prior range · 2017-09-30 · 30 · data/features/fct_bank_features.parquet
- F133 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F134 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F135 · Percentile a year earlier (100 = highest risk) · 2016-09-30 · 27.4% · data/analyst/scores.parquet: percentile
- F136 · Trend: how the model's rating compares with a year earlier · 2017-09-30 · the model rated it riskier than a year earlier · data/analyst/scores.parquet: percentile
- F140 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2017-09-30 · 1.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F141 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2017-09-30 · 97.4th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F142 · Peers: annualized interest expense as a share of assets, national reading · 2017-09-30 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F143 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2017-09-30 · 94.5th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F144 · Peers: annualized interest expense as a share of assets, peer median · 2017-09-30 · 0.5% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F145 · Peers: annualized interest expense as a share of assets, reading against its peers · 2017-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F146 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2017-09-30 · 0.4% · data/features/fct_bank_features.parquet: allowance_to_loans
- F147 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2017-09-30 · 2.9th · data/features/fct_bank_features.parquet: allowance_to_loans
- F148 · Peers: loan-loss reserves as a share of loans, national reading · 2017-09-30 · unusually low · data/features/fct_bank_features.parquet: allowance_to_loans
- F149 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2017-09-30 · 12.7th · data/features/fct_bank_features.parquet: allowance_to_loans
- F150 · Peers: loan-loss reserves as a share of loans, peer median · 2017-09-30 · 0.9% · data/features/fct_bank_features.parquet: allowance_to_loans
- F151 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2017-09-30 · typical for its peer group · data/features/fct_bank_features.parquet: allowance_to_loans
- F152 · Peers: securities as a share of assets, bank value at the as-of quarter · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: securities_to_assets
- F153 · Peers: securities as a share of assets, national percentile (100 = highest value among all banks) · 2017-09-30 · 3.2nd · data/features/fct_bank_features.parquet: securities_to_assets
- F154 · Peers: securities as a share of assets, national reading · 2017-09-30 · unusually low · data/features/fct_bank_features.parquet: securities_to_assets
- F155 · Peers: securities as a share of assets, percentile among its peers (100 = highest value) · 2017-09-30 · 2.1st · data/features/fct_bank_features.parquet: securities_to_assets
- F156 · Peers: securities as a share of assets, peer median · 2017-09-30 · 17.7% · data/features/fct_bank_features.parquet: securities_to_assets
- F157 · Peers: securities as a share of assets, reading against its peers · 2017-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: securities_to_assets
- F158 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: texas_ratio
- F159 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2017-09-30 · 4.4th · data/features/fct_bank_features.parquet: texas_ratio
- F160 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2017-09-30 · unusually low · data/features/fct_bank_features.parquet: texas_ratio
- F161 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2017-09-30 · 2.6th · data/features/fct_bank_features.parquet: texas_ratio
- F162 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2017-09-30 · 4.6% · data/features/fct_bank_features.parquet: texas_ratio
- F163 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2017-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: texas_ratio
- F164 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2017-09-30 · 0.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F165 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2017-09-30 · 4.7th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F166 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2017-09-30 · unusually low · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F167 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2017-09-30 · 2.5th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F168 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2017-09-30 · 0.7% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F169 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2017-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F170 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2017-09-30 · 46.6% · data/features/fct_bank_features.parquet: efficiency_ratio
- F171 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2017-09-30 · 6.2nd · data/features/fct_bank_features.parquet: efficiency_ratio
- F172 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2017-09-30 · unusually low · data/features/fct_bank_features.parquet: efficiency_ratio
- F173 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2017-09-30 · 1.7th · data/features/fct_bank_features.parquet: efficiency_ratio
- F174 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2017-09-30 · 77.3% · data/features/fct_bank_features.parquet: efficiency_ratio
- F175 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2017-09-30 · unusually low among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F176 · Peers: net interest margin (the spread earned on lending and investing), bank value at the as-of quarter · 2017-09-30 · 4.6% · data/features/fct_bank_features.parquet: net_interest_margin
- F177 · Peers: net interest margin (the spread earned on lending and investing), national percentile (100 = highest value among all banks) · 2017-09-30 · 91.0th · data/features/fct_bank_features.parquet: net_interest_margin
- F178 · Peers: net interest margin (the spread earned on lending and investing), national reading · 2017-09-30 · unusually high · data/features/fct_bank_features.parquet: net_interest_margin
- F179 · Peers: net interest margin (the spread earned on lending and investing), percentile among its peers (100 = highest value) · 2017-09-30 · 97.2nd · data/features/fct_bank_features.parquet: net_interest_margin
- F180 · Peers: net interest margin (the spread earned on lending and investing), peer median · 2017-09-30 · 3.2% · data/features/fct_bank_features.parquet: net_interest_margin
- F181 · Peers: net interest margin (the spread earned on lending and investing), reading against its peers · 2017-09-30 · unusually high among its peers too · data/features/fct_bank_features.parquet: net_interest_margin
- F182 · Peers: volatile funding as a share of assets, bank value at the as-of quarter · 2017-09-30 · 15.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F183 · Peers: volatile funding as a share of assets, national percentile (100 = highest value among all banks) · 2017-09-30 · 90.7th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F184 · Peers: volatile funding as a share of assets, national reading · 2017-09-30 · unusually high · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F185 · Peers: volatile funding as a share of assets, percentile among its peers (100 = highest value) · 2017-09-30 · 88.9th · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F186 · Peers: volatile funding as a share of assets, peer median · 2017-09-30 · 6.4% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F187 · Peers: volatile funding as a share of assets, reading against its peers · 2017-09-30 · typical for its peer group · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F189 · Peers: ratios in the national top or bottom 10% · 2017-09-30 · 8 · data/features/fct_bank_features.parquet
- F190 · Peers: those ratios also unusual among peers · 2017-09-30 · 6 · data/features/fct_bank_features.parquet
- F192 · Peers: cut-off for unusual (top or bottom share of banks) · 2017-09-30 · 10% · data/features/fct_bank_features.parquet
