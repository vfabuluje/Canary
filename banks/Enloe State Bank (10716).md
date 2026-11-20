---
cert: 10716
name: "Enloe State Bank"
as_of: 2019-03-31
rank: 1008
n_banks: 5428
percentile: 81.44804716285925
flagged: false
outcome: "missed"
after_test_window: false
failure_date: 2019-05-31
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T21:13:20"
writer_model: "claude-opus-5-5"
checked: true
---

# Enloe State Bank (cert 10716)

*Hindsight: failed 2019-05-31. Canary did not flag it.*

## Summary

As of 2019-03-31, Enloe State Bank, a small Texas lender, ranked 1,008 out of 5,428 banks nationally, placing it at the 81.4th percentile, where higher means riskier. It was not flagged on the watchlist, which covers the 2% of banks with the highest scores. Its capital cushion was well below the national median, but its reported problem loans were near zero and its profits were well above the national median. The model rated it safer than a year earlier.

## Warning signs in the data

Capital, the owners' own money that absorbs losses, was thin. Equity was 9.2% of assets, against a national median of 11.2%, and the leverage ratio (core capital as a share of average assets) was 9.2% against a median of 10.9%. The Tier 1 risk-based capital ratio (core capital measured against assets weighted by their chance of loss) was 11.0%, well below the national median of 15.4%, and the total risk-based capital ratio was 11.5% against a median of 16.6%.

Credit quality looked clean on the most serious measures: loans 90+ days past due or not accruing interest were 0.0% of loans, below the national median of 0.6%. However, loans 30-89 days past due, an earlier stage of trouble, were 0.9% of assets, well above the national median of 0.3%. Loan-loss reserves (money set aside for bad loans) were only 0.5% of loans, well below the national median of 1.2%.

On funding, loans were 98.4% of deposits, well above the national median of 81.2%, and borrowings from the Federal Home Loan Bank (a government-sponsored lender to banks) were 5.4% of assets against a median of 0.2%. Volatile funding, money that can leave quickly, was 9.5% of assets against a median of 6.0%, while cash was 4.7% of assets, below the median of 6.8%. Losses on bonds held to maturity (bonds the bank plans to keep until repaid) were 0.4% of equity, above the national median of 0.0%, though small in size. Pointing the other way, return on assets (profit as a share of assets) was 1.6%, above the national median of 1.1%, and uninsured deposits were just 4.5% of deposits against a median of 18.7%.

## Understanding the score

As of 2019-03-31, Enloe State Bank ranked 1,008 out of 5,428 banks, at the 81.4th percentile on a scale of 0 to 100 where higher means riskier. It was not on the watchlist, which holds the top 2% of banks by score, or 109 banks that quarter.

The five features that pushed the score up most were commercial real estate loans at 5.0% of loans (+0.193), total assets of $36.7 million (+0.188), construction loans at 0.5% of loans (+0.042), uninsured deposits at 4.5% of deposits (+0.037), and securities at 5.4% of assets (+0.035).

The five features that pushed the score down most were the Texas ratio (troubled assets against capital plus reserves) at 0.0% (-1.026), the Tier 1 risk-based capital ratio at 11.0% (-0.883), return on equity (profit as a share of the owners' stake) at 17.6% (-0.693), interest expense at 1.1% of assets (-0.626), and loans 90+ days past due or not accruing interest at 0.0% of loans (-0.473). The downward pushes were much larger than the upward ones, which is why the bank sat outside the watchlist.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2017-06-30 | 1,333 | 5,856 |  |
| 2017-09-30 | 1,556 | 5,806 |  |
| 2017-12-31 | 476 | 5,738 |  |
| 2018-03-31 | 458 | 5,674 |  |
| 2018-06-30 | 783 | 5,610 |  |
| 2018-09-30 | 475 | 5,544 |  |
| 2018-12-31 | 428 | 5,473 |  |
| 2019-03-31 | 1,008 | 5,428 |  |

## How its ratios moved

As of 2019-03-31, Enloe State Bank ranked 1,008 out of 5,428 banks nationally, which places it at the 81.4th percentile on a scale where higher means riskier. A year earlier, on 2018-03-31, it stood at the 91.9th percentile, so the model rated it safer than a year earlier. Each ratio is compared with its own prior range, usually the prior 12 quarters, and 6 of the 30 ratios checked were outside that range.

Return on equity (profit as a share of the owners' stake) was 17.6%, above its prior range of 15.2% to 17.1%, yet it pushed the score down by -0.693 model log-odds units (the model's internal scoring units, where negative lowers the score). Interest expense as a share of assets (what the bank pays on deposits and borrowings) was 1.1%, above its prior range of 0.7% to 1.0%, but it still pushed the score down, contributing -0.626 model log-odds units. The efficiency ratio (operating costs as a share of revenue) was 57.0%, above its prior range of 52.4% to 54.2%, and it too pushed the score down, at -0.090 model log-odds units.

Provision for loan losses (money set aside for expected bad loans) was 0.1% of assets, above its prior range of 0.0% to 0.0%, while it pushed the score down by -0.190 model log-odds units. Cash as a share of assets was 4.7%, below its prior range of 5.2% to 10.7% after a -2.9 pp change, and it pushed the score down at -0.105 model log-odds units. Securities (bonds and similar investments) were 5.4% of assets, just below their prior range of 5.5% to 6.6%, but at +0.035 model log-odds units they had little effect on the score.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| the efficiency ratio (operating costs as a share of revenue) | 57.0% | 52.4% to 54.2% | same quarter, prior 3 years | n/a | +2.8 pp | -0.090 | pushed the score down |
| return on equity (profit as a share of equity) | 17.6% | 15.2% to 17.1% | same quarter, prior 3 years | n/a | +2.4 pp | -0.693 | pushed the score down |
| annualized interest expense as a share of assets | 1.1% | 0.7% to 1.0% | same quarter, prior 3 years | n/a | +0.2 pp | -0.626 | pushed the score down |
| cash as a share of assets | 4.7% | 5.2% to 10.7% | prior 12 quarters | -1.0 pp | -2.9 pp | -0.105 | pushed the score down |
| annualized provision for loan losses as a share of assets | 0.1% | 0.0% to 0.0% | same quarter, prior 3 years | n/a | +0.1 pp | -0.190 | pushed the score down |
| securities as a share of assets | 5.4% | 5.5% to 6.6% | prior 12 quarters | -0.03 pp | -0.2 pp | +0.035 | little effect on the score |

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2019-03-31: Agricultural Specialization.

Peers: 552 banks in the same specialty group and size tier (under $100 million).

The total risk-based capital ratio (capital measured against assets, with each asset weighted by its chance of loss) was 11.5%, at the 3.6th percentile nationally, which is unusually low; at the 2.3rd percentile among peers, against a peer median of 19.2%, it is unusually low among its peers too. The Tier 1 risk-based capital ratio (the same idea using only the core layer of capital) was 11.0%, at the 7.3rd percentile nationally, which is unusually low; at the 3.9th percentile among peers, against a peer median of 18.0%, it is unusually low among its peers too. Loan-loss reserves (money set aside to cover bad loans) were 0.5% of loans, at the 4.8th percentile nationally, which is unusually low; at the 2.8th percentile among peers, against a peer median of 1.4%, this is unusually low among its peers too.

Uninsured deposits (deposits above the government insurance limit) were 4.5% of deposits, at the 4.7th percentile nationally, which is unusually low; at the 8.7th percentile among peers, against a peer median of 12.2%, this is unusually low among its peers too. The Texas ratio (troubled assets against capital plus reserves) was 0.0%, at the 4.7th percentile nationally, which is unusually low; at the 10.5th percentile among peers, against a peer median of 2.5%, it is typical for its peer group. Loans 90+ days past due or not accruing interest were 0.0% of loans, at the 4.9th percentile nationally, which is unusually low; at the 11.2nd percentile among peers, against a peer median of 0.4%, this is typical for its peer group. Losses on bonds held to maturity (bonds the bank plans to keep until they are repaid) were 0.4% of equity, at the 93.6th percentile nationally, which is unusually high; at the 92.3rd percentile among peers, against a peer median of 0.0%, this is unusually high among its peers too. Return on equity (profit as a share of equity) was 17.6%, at the 91.7th percentile nationally, which is unusually high; at the 93.8th percentile among peers, against a peer median of 8.5%, it is unusually high among its peers too.

Overall, 8 of the bank's ratios sit in the national top or bottom 10%, and 6 of those are also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| the total risk-based capital ratio | 11.5% | 3.6th (unusually low) | 19.2% | 2.3rd | unusually low among its peers too |
| the Texas ratio (troubled assets against capital plus reserves) | 0.0% | 4.7th (unusually low) | 2.5% | 10.5th | typical for its peer group |
| uninsured deposits as a share of deposits | 4.5% | 4.7th (unusually low) | 12.2% | 8.7th | unusually low among its peers too |
| loan-loss reserves as a share of loans | 0.5% | 4.8th (unusually low) | 1.4% | 2.8th | unusually low among its peers too |
| loans 90+ days past due or not accruing interest, as a share of loans | 0.0% | 4.9th (unusually low) | 0.4% | 11.2nd | typical for its peer group |
| losses on bonds held to maturity, as a share of equity | 0.4% | 93.6th (unusually high) | 0.0% | 92.3rd | unusually high among its peers too |
| the Tier 1 risk-based capital ratio | 11.0% | 7.3rd (unusually low) | 18.0% | 3.9th | unusually low among its peers too |
| return on equity (profit as a share of equity) | 17.6% | 91.7th (unusually high) | 8.5% | 93.8th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: total risk-based capital, as the 2006 guidance specifies.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 4.2% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 13.7% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -43.5% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why the model missed it

In hindsight, Enloe State Bank failed on 2019-05-31, and its last report was for the quarter ending 2019-03-31. At that last report the model ranked it 1,008 out of 5,428 banks and did not place it on the watchlist, so this is a miss.

The model learned from 539 failed banks, and 96% of them were credit-loss failures, where bad loans build up and eat into capital. This bank's reported figures showed almost none of that pattern: its Texas ratio and its seriously past-due loans were both 0.0%, and its return on equity of 17.6% was high, and these were the strongest forces lowering its score. Its thin capital and rising early-stage past-due loans were visible, but they were not enough to outweigh the clean picture the rest of the reported data painted.

## What happened next

In hindsight, the bank failed on 2019-05-31. The last quarter it reported was 2019-03-31, so there are no later ranks or watchlist flags for it in our data. Our data on its own records only that the bank stopped reporting, which can mean a merger or a closure; here the recorded failure date shows how its history ended.

## Sources

- F1 · Bank name · n/a · Enloe State Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2019-03-31 · 2019-03-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · TX · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2019-03-31 · 1,008 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2019-03-31 · 5,428 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2019-03-31 · 81.4% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2019-03-31 · not flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2019-03-31 · 109 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2019-03-31 · 9.2% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2019-03-31 · 11.2% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2019-03-31 · 9.2% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2019-03-31 · 10.9% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2019-03-31 · 11.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2019-03-31 · 15.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2019-03-31 · 11.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2019-03-31 · 16.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2019-03-31 · 0.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2019-03-31 · 0.6% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F25 · Bank: loans 30-89 days past due, as a share of assets · 2019-03-31 · 0.9% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets
- F26 · National median: loans 30-89 days past due, as a share of assets · 2019-03-31 · 0.3% · data/features/fct_bank_features.parquet: past_due_30_89_to_assets (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2019-03-31 · 0.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2019-03-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2019-03-31 · 1.6% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2019-03-31 · 1.1% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F49 · Bank: loans as a share of deposits · 2019-03-31 · 98.4% · data/features/fct_bank_features.parquet: loans_to_deposits
- F50 · National median: loans as a share of deposits · 2019-03-31 · 81.2% · data/features/fct_bank_features.parquet: loans_to_deposits (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2019-03-31 · 4.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2019-03-31 · 18.7% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F57 · Bank: Federal Home Loan Bank borrowings as a share of assets · 2019-03-31 · 5.4% · data/features/fct_bank_features.parquet: fhlb_to_assets
- F58 · National median: Federal Home Loan Bank borrowings as a share of assets · 2019-03-31 · 0.2% · data/features/fct_bank_features.parquet: fhlb_to_assets (median of all banks)
- F59 · Bank: volatile funding as a share of assets · 2019-03-31 · 9.5% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets
- F60 · National median: volatile funding as a share of assets · 2019-03-31 · 6.0% · data/features/fct_bank_features.parquet: volatile_liabilities_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2019-03-31 · 4.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2019-03-31 · 6.8% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2019-03-31 · 0.4% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2019-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F69 · Bank: total assets · 2019-03-31 · $36.7 million · data/features/fct_bank_features.parquet: log_total_assets
- F75 · Driver up #1: commercial real estate loans as a share of loans, value 5.0%; contribution to the score · 2019-03-31 · +0.193 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F76 · Driver up #2: total assets, value $36.7 million; contribution to the score · 2019-03-31 · +0.188 · data/analyst/scores.parquet: feature log_total_assets contribution
- F77 · Driver up #3: construction loans as a share of loans, value 0.5%; contribution to the score · 2019-03-31 · +0.042 · data/analyst/scores.parquet: feature construction_loans_to_loans contribution
- F78 · Driver up #4: uninsured deposits as a share of deposits, value 4.5%; contribution to the score · 2019-03-31 · +0.037 · data/analyst/scores.parquet: feature uninsured_to_deposits contribution
- F79 · Driver up #5: securities as a share of assets, value 5.4%; contribution to the score · 2019-03-31 · +0.035 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 0.0%; contribution to the score · 2019-03-31 · -1.026 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: the Tier 1 risk-based capital ratio, value 11.0%; contribution to the score · 2019-03-31 · -0.883 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F82 · Driver down #3: return on equity (profit as a share of equity), value 17.6%; contribution to the score · 2019-03-31 · -0.693 · data/analyst/scores.parquet: feature return_on_equity contribution
- F83 · Driver down #4: annualized interest expense as a share of assets, value 1.1%; contribution to the score · 2019-03-31 · -0.626 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F84 · Driver down #5: loans 90+ days past due or not accruing interest, as a share of loans, value 0.0%; contribution to the score · 2019-03-31 · -0.473 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F85 · Failure date · 2019-05-31 · 2019-05-31 · data/raw/failures: FAILDATE
- F86 · Last quarter the bank reported · 2019-03-31 · 2019-03-31 · data/features/fct_bank_features.parquet: report_date
- F87 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F88 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F91 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2019-03-31 · 57.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F92 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 52.4% · data/features/fct_bank_features.parquet: efficiency_ratio
- F93 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 54.2% · data/features/fct_bank_features.parquet: efficiency_ratio
- F95 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2019-03-31 · -0.090 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F96 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2019-03-31 · pushed the score down · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F97 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2019-03-31 · 17.6% · data/features/fct_bank_features.parquet: return_on_equity
- F98 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 15.2% · data/features/fct_bank_features.parquet: return_on_equity
- F99 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 17.1% · data/features/fct_bank_features.parquet: return_on_equity
- F101 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2019-03-31 · -0.693 · data/analyst/scores.parquet: feature return_on_equity contribution
- F102 · Trend: return on equity (profit as a share of equity), what the model did with it · 2019-03-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F103 · Trend: annualized interest expense as a share of assets, value at the as-of quarter · 2019-03-31 · 1.1% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F104 · Trend: annualized interest expense as a share of assets, lowest value in the comparison window · n/a · 0.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F105 · Trend: annualized interest expense as a share of assets, highest value in the comparison window · n/a · 1.0% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F107 · Trend: annualized interest expense as a share of assets, contribution to the score (model log-odds units) · 2019-03-31 · -0.626 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F108 · Trend: annualized interest expense as a share of assets, what the model did with it · 2019-03-31 · pushed the score down · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F109 · Trend: cash as a share of assets, value at the as-of quarter · 2019-03-31 · 4.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F110 · Trend: cash as a share of assets, lowest value in the comparison window · n/a · 5.2% · data/features/fct_bank_features.parquet: cash_to_assets
- F111 · Trend: cash as a share of assets, highest value in the comparison window · n/a · 10.7% · data/features/fct_bank_features.parquet: cash_to_assets
- F113 · Trend: cash as a share of assets, change over four quarters, in percentage points · 2019-03-31 · -2.9 pp · data/features/fct_bank_features.parquet: cash_to_assets
- F114 · Trend: cash as a share of assets, contribution to the score (model log-odds units) · 2019-03-31 · -0.105 · data/analyst/scores.parquet: feature cash_to_assets contribution
- F115 · Trend: cash as a share of assets, what the model did with it · 2019-03-31 · pushed the score down · data/analyst/scores.parquet: feature cash_to_assets contribution
- F116 · Trend: annualized provision for loan losses as a share of assets, value at the as-of quarter · 2019-03-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F117 · Trend: annualized provision for loan losses as a share of assets, lowest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F118 · Trend: annualized provision for loan losses as a share of assets, highest value in the comparison window · n/a · 0.0% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F120 · Trend: annualized provision for loan losses as a share of assets, contribution to the score (model log-odds units) · 2019-03-31 · -0.190 · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F121 · Trend: annualized provision for loan losses as a share of assets, what the model did with it · 2019-03-31 · pushed the score down · data/analyst/scores.parquet: feature provision_to_assets_ann contribution
- F122 · Trend: securities as a share of assets, value at the as-of quarter · 2019-03-31 · 5.4% · data/features/fct_bank_features.parquet: securities_to_assets
- F123 · Trend: securities as a share of assets, lowest value in the comparison window · n/a · 5.5% · data/features/fct_bank_features.parquet: securities_to_assets
- F124 · Trend: securities as a share of assets, highest value in the comparison window · n/a · 6.6% · data/features/fct_bank_features.parquet: securities_to_assets
- F127 · Trend: securities as a share of assets, contribution to the score (model log-odds units) · 2019-03-31 · +0.035 · data/analyst/scores.parquet: feature securities_to_assets contribution
- F128 · Trend: securities as a share of assets, what the model did with it · 2019-03-31 · little effect on the score · data/analyst/scores.parquet: feature securities_to_assets contribution
- F129 · Trend: ratios outside their own prior range · 2019-03-31 · 6 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios compared with their own prior range · 2019-03-31 · 30 · data/features/fct_bank_features.parquet
- F132 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F134 · Percentile a year earlier (100 = highest risk) · 2018-03-31 · 91.9% · data/analyst/scores.parquet: percentile
- F135 · Trend: how the model's rating compares with a year earlier · 2019-03-31 · the model rated it safer than a year earlier · data/analyst/scores.parquet: percentile
- F139 · Peers: the total risk-based capital ratio, bank value at the as-of quarter · 2019-03-31 · 11.5% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F140 · Peers: the total risk-based capital ratio, national percentile (100 = highest value among all banks) · 2019-03-31 · 3.6th · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F141 · Peers: the total risk-based capital ratio, national reading · 2019-03-31 · unusually low · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F142 · Peers: the total risk-based capital ratio, percentile among its peers (100 = highest value) · 2019-03-31 · 2.3rd · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F143 · Peers: the total risk-based capital ratio, peer median · 2019-03-31 · 19.2% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F144 · Peers: the total risk-based capital ratio, reading against its peers · 2019-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F145 · Peers: the Texas ratio (troubled assets against capital plus reserves), bank value at the as-of quarter · 2019-03-31 · 0.0% · data/features/fct_bank_features.parquet: texas_ratio
- F146 · Peers: the Texas ratio (troubled assets against capital plus reserves), national percentile (100 = highest value among all banks) · 2019-03-31 · 4.7th · data/features/fct_bank_features.parquet: texas_ratio
- F147 · Peers: the Texas ratio (troubled assets against capital plus reserves), national reading · 2019-03-31 · unusually low · data/features/fct_bank_features.parquet: texas_ratio
- F148 · Peers: the Texas ratio (troubled assets against capital plus reserves), percentile among its peers (100 = highest value) · 2019-03-31 · 10.5th · data/features/fct_bank_features.parquet: texas_ratio
- F149 · Peers: the Texas ratio (troubled assets against capital plus reserves), peer median · 2019-03-31 · 2.5% · data/features/fct_bank_features.parquet: texas_ratio
- F150 · Peers: the Texas ratio (troubled assets against capital plus reserves), reading against its peers · 2019-03-31 · typical for its peer group · data/features/fct_bank_features.parquet: texas_ratio
- F151 · Peers: uninsured deposits as a share of deposits, bank value at the as-of quarter · 2019-03-31 · 4.5% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F152 · Peers: uninsured deposits as a share of deposits, national percentile (100 = highest value among all banks) · 2019-03-31 · 4.7th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F153 · Peers: uninsured deposits as a share of deposits, national reading · 2019-03-31 · unusually low · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F154 · Peers: uninsured deposits as a share of deposits, percentile among its peers (100 = highest value) · 2019-03-31 · 8.7th · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F155 · Peers: uninsured deposits as a share of deposits, peer median · 2019-03-31 · 12.2% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F156 · Peers: uninsured deposits as a share of deposits, reading against its peers · 2019-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F157 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2019-03-31 · 0.5% · data/features/fct_bank_features.parquet: allowance_to_loans
- F158 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2019-03-31 · 4.8th · data/features/fct_bank_features.parquet: allowance_to_loans
- F159 · Peers: loan-loss reserves as a share of loans, national reading · 2019-03-31 · unusually low · data/features/fct_bank_features.parquet: allowance_to_loans
- F160 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2019-03-31 · 2.8th · data/features/fct_bank_features.parquet: allowance_to_loans
- F161 · Peers: loan-loss reserves as a share of loans, peer median · 2019-03-31 · 1.4% · data/features/fct_bank_features.parquet: allowance_to_loans
- F162 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2019-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F163 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, bank value at the as-of quarter · 2019-03-31 · 0.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F164 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national percentile (100 = highest value among all banks) · 2019-03-31 · 4.9th · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F165 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, national reading · 2019-03-31 · unusually low · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F166 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, percentile among its peers (100 = highest value) · 2019-03-31 · 11.2nd · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F167 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, peer median · 2019-03-31 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F168 · Peers: loans 90+ days past due or not accruing interest, as a share of loans, reading against its peers · 2019-03-31 · typical for its peer group · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F169 · Peers: losses on bonds held to maturity, as a share of equity, bank value at the as-of quarter · 2019-03-31 · 0.4% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F170 · Peers: losses on bonds held to maturity, as a share of equity, national percentile (100 = highest value among all banks) · 2019-03-31 · 93.6th · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F171 · Peers: losses on bonds held to maturity, as a share of equity, national reading · 2019-03-31 · unusually high · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F172 · Peers: losses on bonds held to maturity, as a share of equity, percentile among its peers (100 = highest value) · 2019-03-31 · 92.3rd · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F173 · Peers: losses on bonds held to maturity, as a share of equity, peer median · 2019-03-31 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F174 · Peers: losses on bonds held to maturity, as a share of equity, reading against its peers · 2019-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F175 · Peers: the Tier 1 risk-based capital ratio, bank value at the as-of quarter · 2019-03-31 · 11.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F176 · Peers: the Tier 1 risk-based capital ratio, national percentile (100 = highest value among all banks) · 2019-03-31 · 7.3rd · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F177 · Peers: the Tier 1 risk-based capital ratio, national reading · 2019-03-31 · unusually low · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F178 · Peers: the Tier 1 risk-based capital ratio, percentile among its peers (100 = highest value) · 2019-03-31 · 3.9th · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F179 · Peers: the Tier 1 risk-based capital ratio, peer median · 2019-03-31 · 18.0% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F180 · Peers: the Tier 1 risk-based capital ratio, reading against its peers · 2019-03-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F181 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2019-03-31 · 17.6% · data/features/fct_bank_features.parquet: return_on_equity
- F182 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2019-03-31 · 91.7th · data/features/fct_bank_features.parquet: return_on_equity
- F183 · Peers: return on equity (profit as a share of equity), national reading · 2019-03-31 · unusually high · data/features/fct_bank_features.parquet: return_on_equity
- F184 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2019-03-31 · 93.8th · data/features/fct_bank_features.parquet: return_on_equity
- F185 · Peers: return on equity (profit as a share of equity), peer median · 2019-03-31 · 8.5% · data/features/fct_bank_features.parquet: return_on_equity
- F186 · Peers: return on equity (profit as a share of equity), reading against its peers · 2019-03-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F188 · Peers: ratios in the national top or bottom 10% · 2019-03-31 · 8 · data/features/fct_bank_features.parquet
- F189 · Peers: those ratios also unusual among peers · 2019-03-31 · 6 · data/features/fct_bank_features.parquet
- F191 · Peers: cut-off for unusual (top or bottom share of banks) · 2019-03-31 · 10% · data/features/fct_bank_features.parquet
