---
cert: 57920
name: "Prime Alliance Bank"
as_of: 2025-12-31
rank: 88
n_banks: 4411
percentile: 98.02765812740874
flagged: true
outcome: "false_alarm"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-19T14:08:50"
writer_model: "claude-opus-5-5"
checked: true
---

# Prime Alliance Bank (cert 57920)

*Hindsight: flagged, but had not failed as of 2026-06-30.*

## Summary

As of 2025-12-31, Prime Alliance Bank, a Utah bank, ranked 88 out of 4,411 FDIC-insured banks on Canary's risk score, placing it in the 98.0th percentile, where a higher percentile means riskier. That put it on Canary's watchlist, which covers the top 2% of banks by score. Its problem loans, its reliance on brokered deposits (money placed through middlemen rather than gathered from local customers) and its funding costs all stood well above national medians. Its profits were also far above typical levels, which pulled its score down.

## Warning signs in the data

Capital, the cushion of the owners' own money that absorbs losses, was thinner than at most banks: equity was 9.5% of assets against a national median of 10.4%. Its Tier 1 risk-based capital ratio (core capital measured against riskier assets) was 11.4%, below the national median of 14.4%, and its total risk-based capital ratio was 12.7% against a median of 15.6%.

Credit quality was weaker than typical: loans 90 or more days late or no longer paying interest were 2.0% of loans, well above the national median of 0.4%. Its Texas ratio, which compares troubled assets with capital plus reserves, was 12.8% against a national median of 2.7%. The bank was writing off loans at an annualized 0.7% of loans, against a national median of 0.0%, and setting aside new provisions for losses at 1.1% of assets, against a median of 0.1%. Its loan-loss reserves, money set aside for expected bad loans, were 3.4% of loans, well above the median of 1.2%.

On funding, brokered deposits made up 16.0% of deposits while the national median was 0.0%, and annualized interest expense was 3.3% of assets against a median of 1.7%. Cash was just 0.6% of assets, far below the national median of 6.5%, while deposits grew 26.6% over the past four quarters against a median of 4.1%. Unrealized losses on bonds available for sale were 5.3% of equity, close to the national median of 5.2%.

## Understanding the score

As of 2025-12-31, the bank ranked 88 out of 4,411 banks, which is the 98.0th percentile on a scale from 0 to 100 where higher means riskier. It was flagged on the watchlist, one of 89 banks that quarter, a list that covers the top 2% of banks.

Five features pushed the score up the most: brokered deposits at 16.0% of deposits (+0.449), the efficiency ratio, meaning operating costs as a share of revenue, at 21.0% (+0.449), and annualized interest expense at 3.3% of assets (+0.420). The other two were deposit growth over the past four quarters of 26.6% (+0.218) and losses on bonds available for sale at 5.3% of equity (+0.202).

Five features pushed the score down the most: the Tier 1 risk-based capital ratio at 11.4% (-0.811), return on equity, meaning profit as a share of equity, at 27.1% (-0.654), and return on assets at 2.4% (-0.569). The Texas ratio at 12.8% (-0.511) and total assets of $1.1 billion (-0.290) also pulled the score down.

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-03-31 | 31 | 4,640 | ▲ watchlist |
| 2024-06-30 | 204 | 4,610 |  |
| 2024-09-30 | 211 | 4,589 |  |
| 2024-12-31 | 96 | 4,560 |  |
| 2025-03-31 | 52 | 4,536 | ▲ watchlist |
| 2025-06-30 | 41 | 4,494 | ▲ watchlist |
| 2025-09-30 | 30 | 4,452 | ▲ watchlist |
| 2025-12-31 | 88 | 4,411 | ▲ watchlist |

## How its ratios moved

The bank was in the 98.0th percentile at 2025-12-31 versus the 97.9th percentile a year earlier, so the model rated it about the same as a year earlier. Each ratio is compared with its own range over the prior 12 quarters, or for year-to-date ratios the same quarter in the prior 3 years. Of 30 ratios compared this way, 9 were outside their prior range, and the table shows the 6 furthest outside.

Return on equity reached 27.1%, above its prior range of 15.2% to 21.7% after rising +5.4 pp over four quarters. Even though it was outside its range, return on equity at 27.1% pushed the score down, with a contribution of -0.654 model log-odds units. Return on assets at 2.4%, above its prior range of 1.5% to 2.2%, likewise pushed the score down, contributing -0.569.

Brokered deposits fell to 16.0% of deposits, below their prior range of 17.6% to 24.1%, yet this ratio pushed the score up, contributing +0.449. The efficiency ratio at 21.0%, below its prior range of 22.7% to 30.0%, pushed the score up, contributing +0.449. Commercial real estate loans dropped to 4.3% of loans, below their prior range of 6.0% to 8.6%, and pushed the score up, contributing +0.175. Net loan write-offs at 0.7% of loans sat below their prior range of 0.8% to 1.4%, but had little effect on the score, contributing +0.014.

| Ratio | As-of value | Prior range | Window | Change 1q | Change 4q | Model contribution | Direction |
|---|---|---|---|---|---|---|---|
| return on equity (profit as a share of equity) | 27.1% | 15.2% to 21.7% | same quarter, prior 3 years | n/a | +5.4 pp | -0.654 | pushed the score down |
| commercial real estate loans as a share of loans | 4.3% | 6.0% to 8.6% | prior 12 quarters | -2.0 pp | -3.9 pp | +0.175 | pushed the score up |
| brokered deposits as a share of deposits | 16.0% | 17.6% to 24.1% | prior 12 quarters | -4.3 pp | -2.3 pp | +0.449 | pushed the score up |
| the efficiency ratio (operating costs as a share of revenue) | 21.0% | 22.7% to 30.0% | same quarter, prior 3 years | n/a | -1.7 pp | +0.449 | pushed the score up |
| return on assets (profit as a share of assets) | 2.4% | 1.5% to 2.2% | same quarter, prior 3 years | n/a | +0.3 pp | -0.569 | pushed the score down |
| annualized loan write-offs, net of recoveries, as a share of loans | 0.7% | 0.8% to 1.4% | same quarter, prior 3 years | n/a | -0.7 pp | +0.014 | little effect on the score |

9 of 30 ratios were outside their prior range; the 6 furthest are shown.

This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure.

## Compared with similar banks

The FDIC's specialty group for this bank at 2025-12-31: Commercial Lending Specialization.

Peers: 757 banks in the same specialty group and size tier ($1 billion to $10 billion).

Cash was 0.6% of assets, at the 0.7th national percentile, which is unusually low, and at the 0.6th percentile among peers against a peer median of 5.5%, unusually low among its peers too. The efficiency ratio was 21.0%, at the 1.0th national percentile, which is unusually low, and at the 0.7th percentile among peers against a peer median of 60.8%, unusually low among its peers too. Annualized interest expense was 3.3% of assets, at the 98.9th national percentile, which is unusually high, and at the 98.7th percentile among peers against a peer median of 1.9%, unusually high among its peers too. Loan-loss reserves were 3.4% of loans, at the 98.2nd national percentile, which is unusually high, and at the 99.3rd percentile among peers against a peer median of 1.2%, unusually high among its peers too.

The annualized provision for loan losses was 1.1% of assets, at the 98.2nd national percentile, which is unusually high, and at the 97.8th percentile among peers against a peer median of 0.1%, unusually high among its peers too. Return on equity was 27.1%, at the 97.1st national percentile, which is unusually high, and at the 98.7th percentile among peers against a peer median of 11.3%, unusually high among its peers too. Construction loans were 0.0% of loans, at the 4.0th national percentile, which is unusually low, and at the 1.1st percentile among peers against a peer median of 7.3%, unusually low among its peers too. Asset growth over the past four quarters was 27.3%, at the 95.9th national percentile, which is unusually high, and at the 96.6th percentile among peers against a peer median of 5.1%, unusually high among its peers too.

Overall, 14 of the bank's ratios fell in the national top or bottom 10%, and all 14 of those were also unusual among its peers.

| Ratio | Bank | National percentile | Peer median | Peer percentile | Reading |
|---|---|---|---|---|---|
| cash as a share of assets | 0.6% | 0.7th (unusually low) | 5.5% | 0.6th | unusually low among its peers too |
| the efficiency ratio (operating costs as a share of revenue) | 21.0% | 1.0th (unusually low) | 60.8% | 0.7th | unusually low among its peers too |
| annualized interest expense as a share of assets | 3.3% | 98.9th (unusually high) | 1.9% | 98.7th | unusually high among its peers too |
| loan-loss reserves as a share of loans | 3.4% | 98.2nd (unusually high) | 1.2% | 99.3rd | unusually high among its peers too |
| annualized provision for loan losses as a share of assets | 1.1% | 98.2nd (unusually high) | 0.1% | 97.8th | unusually high among its peers too |
| return on equity (profit as a share of equity) | 27.1% | 97.1st (unusually high) | 11.3% | 98.7th | unusually high among its peers too |
| construction loans as a share of loans | 0.0% | 4.0th (unusually low) | 7.3% | 1.1st | unusually low among its peers too |
| asset growth over the past four quarters | 27.3% | 95.9th (unusually high) | 5.1% | 96.6th | unusually high among its peers too |

This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal.

## Real-estate concentration (2006 regulator thresholds)

This section checks a different, more common way banks have failed than SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending limits.

Capital measure: Tier 1 capital plus the loan-loss allowance, which the regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal Reserve SR 20-8). The 2006 thresholds were not restated for this measure.

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | 0.0% | 100% or more | no |
| Total commercial real estate loans ÷ capital | 25.6% | 300% or more | no |
| Growth in commercial real estate loans over the prior 36 months | -8.8% | 50% or more | no |

It did not cross either line.

Total commercial real estate here means construction and land, multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial real estate not secured by real estate (FDIC call report data).

Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary.

## Why it was flagged, and what happened

In hindsight, this flag looks like a false alarm. The model was trained on 539 bank failures, and 96% of them were credit-loss failures, so it gives weight to signs such as costly funding and brokered deposits that often appeared in those cases. This bank showed several of those signs at 2025-12-31, but it also had very strong profits, and it kept reporting afterward. By 2026-03-31 its rank had eased to 177 and it was no longer flagged on the watchlist.

## What happened next

Looking back with hindsight, the bank continued to file reports after the as-of quarter. It ranked 177 at 2026-03-31 and 249 at 2026-06-30, and it was not flagged on the watchlist in either quarter.

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2026-03-31 | 177 | 4,353 |  |
| 2026-06-30 | 249 | 4,313 |  |

## Sources

- F1 · Bank name · n/a · Prime Alliance Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2025-12-31 · 2025-12-31 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · UT · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2025-12-31 · 88 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2025-12-31 · 4,411 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2025-12-31 · 98.0% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2025-12-31 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2025-12-31 · 89 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2025-12-31 · 9.5% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2025-12-31 · 10.4% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2025-12-31 · 11.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2025-12-31 · 14.4% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2025-12-31 · 12.7% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2025-12-31 · 15.6% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2025-12-31 · 2.0% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2025-12-31 · 0.4% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F27 · Bank: loan-loss reserves as a share of loans · 2025-12-31 · 3.4% · data/features/fct_bank_features.parquet: allowance_to_loans
- F28 · National median: loan-loss reserves as a share of loans · 2025-12-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2025-12-31 · 0.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F31 · Bank: annualized provision for loan losses as a share of assets · 2025-12-31 · 1.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F32 · National median: annualized provision for loan losses as a share of assets · 2025-12-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann (median of all banks)
- F37 · Bank: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 12.8% · data/features/fct_bank_features.parquet: texas_ratio
- F38 · National median: the Texas ratio (troubled assets against capital plus reserves) · 2025-12-31 · 2.7% · data/features/fct_bank_features.parquet: texas_ratio (median of all banks)
- F47 · Bank: annualized interest expense as a share of assets · 2025-12-31 · 3.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F48 · National median: annualized interest expense as a share of assets · 2025-12-31 · 1.7% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann (median of all banks)
- F53 · Bank: brokered deposits as a share of deposits · 2025-12-31 · 16.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F54 · National median: brokered deposits as a share of deposits · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: brokered_to_deposits (median of all banks)
- F61 · Bank: cash as a share of assets · 2025-12-31 · 0.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2025-12-31 · 6.5% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F65 · Bank: losses on bonds available for sale, as a share of equity · 2025-12-31 · 5.3% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity
- F66 · National median: losses on bonds available for sale, as a share of equity · 2025-12-31 · 5.2% · data/features/fct_bank_features.parquet: afs_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2025-12-31 · 26.6% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2025-12-31 · 4.1% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: brokered deposits as a share of deposits, value 16.0%; contribution to the score · 2025-12-31 · +0.449 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F76 · Driver up #2: the efficiency ratio (operating costs as a share of revenue), value 21.0%; contribution to the score · 2025-12-31 · +0.449 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F77 · Driver up #3: annualized interest expense as a share of assets, value 3.3%; contribution to the score · 2025-12-31 · +0.420 · data/analyst/scores.parquet: feature interest_expense_to_assets_ann contribution
- F78 · Driver up #4: deposit growth over the past four quarters, value 26.6%; contribution to the score · 2025-12-31 · +0.218 · data/analyst/scores.parquet: feature deposit_growth_4q contribution
- F79 · Driver up #5: losses on bonds available for sale, as a share of equity, value 5.3%; contribution to the score · 2025-12-31 · +0.202 · data/analyst/scores.parquet: feature afs_unrealized_loss_to_equity contribution
- F80 · Driver down #1: the Tier 1 risk-based capital ratio, value 11.4%; contribution to the score · 2025-12-31 · -0.811 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F81 · Driver down #2: return on equity (profit as a share of equity), value 27.1%; contribution to the score · 2025-12-31 · -0.654 · data/analyst/scores.parquet: feature return_on_equity contribution
- F82 · Driver down #3: return on assets (profit as a share of assets), value 2.4%; contribution to the score · 2025-12-31 · -0.569 · data/analyst/scores.parquet: feature return_on_assets contribution
- F83 · Driver down #4: the Texas ratio (troubled assets against capital plus reserves), value 12.8%; contribution to the score · 2025-12-31 · -0.511 · data/analyst/scores.parquet: feature texas_ratio contribution
- F84 · Driver down #5: total assets, value $1.1 billion; contribution to the score · 2025-12-31 · -0.290 · data/analyst/scores.parquet: feature log_total_assets contribution
- F85 · Rank in a later quarter (2026-03-31), not flagged · 2026-03-31 · 177 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F86 · Rank in a later quarter (2026-06-30), not flagged · 2026-06-30 · 249 (not flagged) · data/analyst/scores.parquet: rank, flagged
- F87 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F88 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
- F91 · Trend: return on equity (profit as a share of equity), value at the as-of quarter · 2025-12-31 · 27.1% · data/features/fct_bank_features.parquet: return_on_equity
- F92 · Trend: return on equity (profit as a share of equity), lowest value in the comparison window · n/a · 15.2% · data/features/fct_bank_features.parquet: return_on_equity
- F93 · Trend: return on equity (profit as a share of equity), highest value in the comparison window · n/a · 21.7% · data/features/fct_bank_features.parquet: return_on_equity
- F94 · Trend: return on equity (profit as a share of equity), change over four quarters, in percentage points · 2025-12-31 · +5.4 pp · data/features/fct_bank_features.parquet: return_on_equity
- F95 · Trend: return on equity (profit as a share of equity), contribution to the score (model log-odds units) · 2025-12-31 · -0.654 · data/analyst/scores.parquet: feature return_on_equity contribution
- F96 · Trend: return on equity (profit as a share of equity), what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_equity contribution
- F97 · Trend: commercial real estate loans as a share of loans, value at the as-of quarter · 2025-12-31 · 4.3% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F98 · Trend: commercial real estate loans as a share of loans, lowest value in the comparison window · n/a · 6.0% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F99 · Trend: commercial real estate loans as a share of loans, highest value in the comparison window · n/a · 8.6% · data/features/fct_bank_features.parquet: cre_loans_to_loans
- F102 · Trend: commercial real estate loans as a share of loans, contribution to the score (model log-odds units) · 2025-12-31 · +0.175 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F103 · Trend: commercial real estate loans as a share of loans, what the model did with it · 2025-12-31 · pushed the score up · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F104 · Trend: brokered deposits as a share of deposits, value at the as-of quarter · 2025-12-31 · 16.0% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F105 · Trend: brokered deposits as a share of deposits, lowest value in the comparison window · n/a · 17.6% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F106 · Trend: brokered deposits as a share of deposits, highest value in the comparison window · n/a · 24.1% · data/features/fct_bank_features.parquet: brokered_to_deposits
- F109 · Trend: brokered deposits as a share of deposits, contribution to the score (model log-odds units) · 2025-12-31 · +0.449 · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F110 · Trend: brokered deposits as a share of deposits, what the model did with it · 2025-12-31 · pushed the score up · data/analyst/scores.parquet: feature brokered_to_deposits contribution
- F111 · Trend: the efficiency ratio (operating costs as a share of revenue), value at the as-of quarter · 2025-12-31 · 21.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F112 · Trend: the efficiency ratio (operating costs as a share of revenue), lowest value in the comparison window · n/a · 22.7% · data/features/fct_bank_features.parquet: efficiency_ratio
- F113 · Trend: the efficiency ratio (operating costs as a share of revenue), highest value in the comparison window · n/a · 30.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F115 · Trend: the efficiency ratio (operating costs as a share of revenue), contribution to the score (model log-odds units) · 2025-12-31 · +0.449 · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F116 · Trend: the efficiency ratio (operating costs as a share of revenue), what the model did with it · 2025-12-31 · pushed the score up · data/analyst/scores.parquet: feature efficiency_ratio contribution
- F117 · Trend: return on assets (profit as a share of assets), value at the as-of quarter · 2025-12-31 · 2.4% · data/features/fct_bank_features.parquet: return_on_assets
- F118 · Trend: return on assets (profit as a share of assets), lowest value in the comparison window · n/a · 1.5% · data/features/fct_bank_features.parquet: return_on_assets
- F119 · Trend: return on assets (profit as a share of assets), highest value in the comparison window · n/a · 2.2% · data/features/fct_bank_features.parquet: return_on_assets
- F121 · Trend: return on assets (profit as a share of assets), contribution to the score (model log-odds units) · 2025-12-31 · -0.569 · data/analyst/scores.parquet: feature return_on_assets contribution
- F122 · Trend: return on assets (profit as a share of assets), what the model did with it · 2025-12-31 · pushed the score down · data/analyst/scores.parquet: feature return_on_assets contribution
- F123 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, value at the as-of quarter · 2025-12-31 · 0.7% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F124 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, lowest value in the comparison window · n/a · 0.8% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F125 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, highest value in the comparison window · n/a · 1.4% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F127 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, contribution to the score (model log-odds units) · 2025-12-31 · +0.014 · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F128 · Trend: annualized loan write-offs, net of recoveries, as a share of loans, what the model did with it · 2025-12-31 · little effect on the score · data/analyst/scores.parquet: feature net_charge_offs_to_loans_ann contribution
- F129 · Trend: ratios outside their own prior range · 2025-12-31 · 9 · data/features/fct_bank_features.parquet
- F130 · Trend: ratios shown in the table (the furthest outside their prior range) · 2025-12-31 · 6 · data/features/fct_bank_features.parquet
- F131 · Trend: ratios compared with their own prior range · 2025-12-31 · 30 · data/features/fct_bank_features.parquet
- F132 · Comparison window for most ratios: the prior 12 quarters (at least 8 with a value) · n/a · 12 quarters · canary.analyst.trends: range rule (fixed)
- F133 · Comparison window for year-to-date ratios: the same quarter in the prior 3 years (at least 2 with a value) · n/a · 3 years · canary.analyst.trends: range rule (fixed)
- F134 · Percentile a year earlier (100 = highest risk) · 2024-12-31 · 97.9% · data/analyst/scores.parquet: percentile
- F135 · Trend: how the model's rating compares with a year earlier · 2025-12-31 · about the same as a year earlier · data/analyst/scores.parquet: percentile
- F139 · Peers: cash as a share of assets, bank value at the as-of quarter · 2025-12-31 · 0.6% · data/features/fct_bank_features.parquet: cash_to_assets
- F140 · Peers: cash as a share of assets, national percentile (100 = highest value among all banks) · 2025-12-31 · 0.7th · data/features/fct_bank_features.parquet: cash_to_assets
- F141 · Peers: cash as a share of assets, national reading · 2025-12-31 · unusually low · data/features/fct_bank_features.parquet: cash_to_assets
- F142 · Peers: cash as a share of assets, percentile among its peers (100 = highest value) · 2025-12-31 · 0.6th · data/features/fct_bank_features.parquet: cash_to_assets
- F143 · Peers: cash as a share of assets, peer median · 2025-12-31 · 5.5% · data/features/fct_bank_features.parquet: cash_to_assets
- F144 · Peers: cash as a share of assets, reading against its peers · 2025-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: cash_to_assets
- F145 · Peers: the efficiency ratio (operating costs as a share of revenue), bank value at the as-of quarter · 2025-12-31 · 21.0% · data/features/fct_bank_features.parquet: efficiency_ratio
- F146 · Peers: the efficiency ratio (operating costs as a share of revenue), national percentile (100 = highest value among all banks) · 2025-12-31 · 1.0th · data/features/fct_bank_features.parquet: efficiency_ratio
- F147 · Peers: the efficiency ratio (operating costs as a share of revenue), national reading · 2025-12-31 · unusually low · data/features/fct_bank_features.parquet: efficiency_ratio
- F148 · Peers: the efficiency ratio (operating costs as a share of revenue), percentile among its peers (100 = highest value) · 2025-12-31 · 0.7th · data/features/fct_bank_features.parquet: efficiency_ratio
- F149 · Peers: the efficiency ratio (operating costs as a share of revenue), peer median · 2025-12-31 · 60.8% · data/features/fct_bank_features.parquet: efficiency_ratio
- F150 · Peers: the efficiency ratio (operating costs as a share of revenue), reading against its peers · 2025-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: efficiency_ratio
- F151 · Peers: annualized interest expense as a share of assets, bank value at the as-of quarter · 2025-12-31 · 3.3% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F152 · Peers: annualized interest expense as a share of assets, national percentile (100 = highest value among all banks) · 2025-12-31 · 98.9th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F153 · Peers: annualized interest expense as a share of assets, national reading · 2025-12-31 · unusually high · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F154 · Peers: annualized interest expense as a share of assets, percentile among its peers (100 = highest value) · 2025-12-31 · 98.7th · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F155 · Peers: annualized interest expense as a share of assets, peer median · 2025-12-31 · 1.9% · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F156 · Peers: annualized interest expense as a share of assets, reading against its peers · 2025-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: interest_expense_to_assets_ann
- F157 · Peers: loan-loss reserves as a share of loans, bank value at the as-of quarter · 2025-12-31 · 3.4% · data/features/fct_bank_features.parquet: allowance_to_loans
- F158 · Peers: loan-loss reserves as a share of loans, national percentile (100 = highest value among all banks) · 2025-12-31 · 98.2nd · data/features/fct_bank_features.parquet: allowance_to_loans
- F159 · Peers: loan-loss reserves as a share of loans, national reading · 2025-12-31 · unusually high · data/features/fct_bank_features.parquet: allowance_to_loans
- F160 · Peers: loan-loss reserves as a share of loans, percentile among its peers (100 = highest value) · 2025-12-31 · 99.3rd · data/features/fct_bank_features.parquet: allowance_to_loans
- F161 · Peers: loan-loss reserves as a share of loans, peer median · 2025-12-31 · 1.2% · data/features/fct_bank_features.parquet: allowance_to_loans
- F162 · Peers: loan-loss reserves as a share of loans, reading against its peers · 2025-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: allowance_to_loans
- F163 · Peers: annualized provision for loan losses as a share of assets, bank value at the as-of quarter · 2025-12-31 · 1.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F164 · Peers: annualized provision for loan losses as a share of assets, national percentile (100 = highest value among all banks) · 2025-12-31 · 98.2nd · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F165 · Peers: annualized provision for loan losses as a share of assets, national reading · 2025-12-31 · unusually high · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F166 · Peers: annualized provision for loan losses as a share of assets, percentile among its peers (100 = highest value) · 2025-12-31 · 97.8th · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F167 · Peers: annualized provision for loan losses as a share of assets, peer median · 2025-12-31 · 0.1% · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F168 · Peers: annualized provision for loan losses as a share of assets, reading against its peers · 2025-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: provision_to_assets_ann
- F169 · Peers: return on equity (profit as a share of equity), bank value at the as-of quarter · 2025-12-31 · 27.1% · data/features/fct_bank_features.parquet: return_on_equity
- F170 · Peers: return on equity (profit as a share of equity), national percentile (100 = highest value among all banks) · 2025-12-31 · 97.1st · data/features/fct_bank_features.parquet: return_on_equity
- F171 · Peers: return on equity (profit as a share of equity), national reading · 2025-12-31 · unusually high · data/features/fct_bank_features.parquet: return_on_equity
- F172 · Peers: return on equity (profit as a share of equity), percentile among its peers (100 = highest value) · 2025-12-31 · 98.7th · data/features/fct_bank_features.parquet: return_on_equity
- F173 · Peers: return on equity (profit as a share of equity), peer median · 2025-12-31 · 11.3% · data/features/fct_bank_features.parquet: return_on_equity
- F174 · Peers: return on equity (profit as a share of equity), reading against its peers · 2025-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: return_on_equity
- F175 · Peers: construction loans as a share of loans, bank value at the as-of quarter · 2025-12-31 · 0.0% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F176 · Peers: construction loans as a share of loans, national percentile (100 = highest value among all banks) · 2025-12-31 · 4.0th · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F177 · Peers: construction loans as a share of loans, national reading · 2025-12-31 · unusually low · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F178 · Peers: construction loans as a share of loans, percentile among its peers (100 = highest value) · 2025-12-31 · 1.1st · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F179 · Peers: construction loans as a share of loans, peer median · 2025-12-31 · 7.3% · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F180 · Peers: construction loans as a share of loans, reading against its peers · 2025-12-31 · unusually low among its peers too · data/features/fct_bank_features.parquet: construction_loans_to_loans
- F181 · Peers: asset growth over the past four quarters, bank value at the as-of quarter · 2025-12-31 · 27.3% · data/features/fct_bank_features.parquet: asset_growth_4q
- F182 · Peers: asset growth over the past four quarters, national percentile (100 = highest value among all banks) · 2025-12-31 · 95.9th · data/features/fct_bank_features.parquet: asset_growth_4q
- F183 · Peers: asset growth over the past four quarters, national reading · 2025-12-31 · unusually high · data/features/fct_bank_features.parquet: asset_growth_4q
- F184 · Peers: asset growth over the past four quarters, percentile among its peers (100 = highest value) · 2025-12-31 · 96.6th · data/features/fct_bank_features.parquet: asset_growth_4q
- F185 · Peers: asset growth over the past four quarters, peer median · 2025-12-31 · 5.1% · data/features/fct_bank_features.parquet: asset_growth_4q
- F186 · Peers: asset growth over the past four quarters, reading against its peers · 2025-12-31 · unusually high among its peers too · data/features/fct_bank_features.parquet: asset_growth_4q
- F188 · Peers: ratios in the national top or bottom 10% · 2025-12-31 · 14 · data/features/fct_bank_features.parquet
- F189 · Peers: those ratios also unusual among peers · 2025-12-31 · 14 · data/features/fct_bank_features.parquet
- F191 · Peers: cut-off for unusual (top or bottom share of banks) · 2025-12-31 · 10% · data/features/fct_bank_features.parquet
