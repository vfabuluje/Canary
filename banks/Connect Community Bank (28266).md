---
cert: 28266
name: "Connect Community Bank"
as_of: 2026-06-30
rank: 9
n_banks: 4313
percentile: 99.81451425921632
flagged: true
outcome: "open_watchlist"
after_test_window: false
failure_date: null
model_run: "bf7af0bddf5b"
written_at: "2026-11-17T22:07:46"
writer_model: "claude-opus-5-5"
checked: true
---

# Connect Community Bank (cert 28266)

*Outcome not yet known.*

## Summary

Connect Community Bank, a Washington State bank, ranked 9 out of 4,313 banks nationally in Canary's risk ranking for the quarter ending 2026-06-30, placing it in the 99.8th percentile, where higher means riskier. It was flagged on Canary's watchlist that quarter. The ranking mainly reflects thin capital, the cushion of the owners' own money that absorbs losses, and a sizeable loss, with return on equity at -43.1% against a national median of 11.6%.

## Warning signs in the data

Capital was well below typical levels: equity was 3.7% of assets, against a national median of 10.6%. The leverage ratio, core capital as a share of average assets, was 3.6% against a median of 11.0%. The risk-based capital ratios, which weigh capital against how risky the bank's assets are, were also low: Tier 1 at 7.7% against 14.6%, and total at 8.9% against 15.8%.

The bank was losing money, with return on assets, profit as a share of assets, at -1.7% against a median of 1.2%. Its efficiency ratio, operating costs as a share of revenue, was 153.5% against a median of 62.1%, meaning costs exceeded revenue. Its net interest margin, the spread earned on lending and investing, was 2.9% against a median of 3.9%. On bonds, unrealized losses on bonds held to maturity, those the bank plans to keep until they repay, equaled 36.6% of equity, against a national median of 0.0%.

Credit quality looked mostly clean: loans 90 or more days past due or not accruing interest were 0.1% of loans, against a median of 0.5%, although net loan write-offs ran at 0.3% against a median of 0.0%. Funding looked stable: uninsured deposits, those above the government insurance limit, were 3.3% of deposits against a median of 24.8%, and core deposits, the steadier everyday kind, were 89.8% of assets against 75.5%. Cash was 10.0% of assets against a median of 6.2%, and deposits grew 22.9% over the past four quarters against a median of 4.2%.

## Understanding the score

For the quarter ending 2026-06-30, the bank ranked 9 of 4,313 banks, in the 99.8th percentile on a scale of 0 to 100 where higher means riskier. It was flagged on the watchlist, which covers the top 2% of banks by score, or 87 banks that quarter.

The five factors that pushed the score up most were return on equity at -43.1% (contribution +1.775), the Tier 1 risk-based capital ratio at 7.7% (+0.537), commercial real estate loans as a share of loans at 1.1% (+0.369), the total risk-based capital ratio at 8.9% (+0.327), and the leverage ratio at 3.6% (+0.149).

The five factors that pulled the score down most were the Texas ratio, troubled assets against capital plus reserves, at 2.6% (contribution -1.180), loans 90 or more days past due or not accruing at 0.1% (-0.995), nonaccrual assets and foreclosed property at 0.1% of assets (-0.613), loan-loss reserves at 1.0% of loans (-0.131), and loans as a share of deposits at 82.8% (-0.092).

The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.

**What the model can't see.** This bank does not show a credit-loss profile in the data. The model was trained on failures that were 96% credit-loss failures, and it is flat in losses on bonds held to maturity, so it can miss a bank that fails for other reasons. FDIC data has no loan fair values, no depositor identity, and no non-financial causes such as fraud or management, so the model cannot see them.

## Score history

| Quarter | Rank | Of | Watchlist |
|---|---|---|---|
| 2024-09-30 | 1,206 | 4,589 |  |
| 2024-12-31 | 2,128 | 4,560 |  |
| 2025-03-31 | 428 | 4,536 |  |
| 2025-06-30 | 591 | 4,494 |  |
| 2025-09-30 | 108 | 4,452 |  |
| 2025-12-31 | 64 | 4,411 | ▲ watchlist |
| 2026-03-31 | 28 | 4,353 | ▲ watchlist |
| 2026-06-30 | 9 | 4,313 | ▲ watchlist |

## Why it's on the watchlist

In hindsight: Canary classifies this case as an open bank on the watchlist, meaning it was flagged and no closure is recorded in our data. The fact sheet holds no data after the as-of quarter of 2026-06-30, so the reasons for the flag rest on that quarter's figures: very thin capital and a large loss, rather than bad loans or unstable funding. Most failures the model learned from were credit-loss failures, 96% of the 539 in the training period, and this bank's loan quality did not fit that typical pattern.

## What happened next

In hindsight: the fact sheet contains no ranks, flags or reporting data for quarters after 2026-06-30. We therefore cannot say from this data how its rank moved afterward or whether it kept reporting; it remains an open case on the watchlist.

## Sources

- F1 · Bank name · n/a · Connect Community Bank · data/features/fct_bank_features.parquet: institution_name
- F3 · As-of quarter · 2026-06-30 · 2026-06-30 · data/features/fct_bank_features.parquet: report_date
- F4 · State · n/a · WA · data/raw/financials: STALP
- F6 · National rank (1 = highest score) · 2026-06-30 · 9 · data/analyst/scores.parquet: rank
- F7 · Banks ranked that quarter · 2026-06-30 · 4,313 · data/analyst/scores.parquet: n_banks
- F8 · Percentile (100 = highest risk) · 2026-06-30 · 99.8% · data/analyst/scores.parquet: percentile
- F9 · Percentile scale (0 to 100; higher means riskier) · n/a · 0 to 100 · canary.analyst.facts: percentile scale (fixed)
- F10 · On the watchlist · 2026-06-30 · flagged · data/analyst/scores.parquet: flagged
- F11 · Watchlist share of banks · n/a · 2% · canary.model.metrics.WATCHLIST_SHARE
- F12 · Banks on the watchlist that quarter · 2026-06-30 · 87 · data/analyst/scores.parquet: flagged
- F13 · Bank: equity as a share of assets · 2026-06-30 · 3.7% · data/features/fct_bank_features.parquet: equity_to_assets
- F14 · National median: equity as a share of assets · 2026-06-30 · 10.6% · data/features/fct_bank_features.parquet: equity_to_assets (median of all banks)
- F15 · Bank: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 3.6% · data/features/fct_bank_features.parquet: leverage_ratio
- F16 · National median: the leverage ratio (core capital as a share of average assets) · 2026-06-30 · 11.0% · data/features/fct_bank_features.parquet: leverage_ratio (median of all banks)
- F17 · Bank: the Tier 1 risk-based capital ratio · 2026-06-30 · 7.7% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio
- F18 · National median: the Tier 1 risk-based capital ratio · 2026-06-30 · 14.6% · data/features/fct_bank_features.parquet: tier1_risk_based_ratio (median of all banks)
- F19 · Bank: the total risk-based capital ratio · 2026-06-30 · 8.9% · data/features/fct_bank_features.parquet: total_risk_based_ratio
- F20 · National median: the total risk-based capital ratio · 2026-06-30 · 15.8% · data/features/fct_bank_features.parquet: total_risk_based_ratio (median of all banks)
- F21 · Bank: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.1% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans
- F22 · National median: loans 90+ days past due or not accruing interest, as a share of loans · 2026-06-30 · 0.5% · data/features/fct_bank_features.parquet: noncurrent_loans_to_loans (median of all banks)
- F29 · Bank: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.3% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann
- F30 · National median: annualized loan write-offs, net of recoveries, as a share of loans · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: net_charge_offs_to_loans_ann (median of all banks)
- F39 · Bank: return on assets (profit as a share of assets) · 2026-06-30 · -1.7% · data/features/fct_bank_features.parquet: return_on_assets
- F40 · National median: return on assets (profit as a share of assets) · 2026-06-30 · 1.2% · data/features/fct_bank_features.parquet: return_on_assets (median of all banks)
- F41 · Bank: return on equity (profit as a share of equity) · 2026-06-30 · -43.1% · data/features/fct_bank_features.parquet: return_on_equity
- F42 · National median: return on equity (profit as a share of equity) · 2026-06-30 · 11.6% · data/features/fct_bank_features.parquet: return_on_equity (median of all banks)
- F43 · Bank: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 2.9% · data/features/fct_bank_features.parquet: net_interest_margin
- F44 · National median: net interest margin (the spread earned on lending and investing) · 2026-06-30 · 3.9% · data/features/fct_bank_features.parquet: net_interest_margin (median of all banks)
- F45 · Bank: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 153.5% · data/features/fct_bank_features.parquet: efficiency_ratio
- F46 · National median: the efficiency ratio (operating costs as a share of revenue) · 2026-06-30 · 62.1% · data/features/fct_bank_features.parquet: efficiency_ratio (median of all banks)
- F51 · Bank: uninsured deposits as a share of deposits · 2026-06-30 · 3.3% · data/features/fct_bank_features.parquet: uninsured_to_deposits
- F52 · National median: uninsured deposits as a share of deposits · 2026-06-30 · 24.8% · data/features/fct_bank_features.parquet: uninsured_to_deposits (median of all banks)
- F55 · Bank: core deposits as a share of assets · 2026-06-30 · 89.8% · data/features/fct_bank_features.parquet: core_deposits_to_assets
- F56 · National median: core deposits as a share of assets · 2026-06-30 · 75.5% · data/features/fct_bank_features.parquet: core_deposits_to_assets (median of all banks)
- F61 · Bank: cash as a share of assets · 2026-06-30 · 10.0% · data/features/fct_bank_features.parquet: cash_to_assets
- F62 · National median: cash as a share of assets · 2026-06-30 · 6.2% · data/features/fct_bank_features.parquet: cash_to_assets (median of all banks)
- F63 · Bank: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 36.6% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity
- F64 · National median: losses on bonds held to maturity, as a share of equity · 2026-06-30 · 0.0% · data/features/fct_bank_features.parquet: htm_unrealized_loss_to_equity (median of all banks)
- F73 · Bank: deposit growth over the past four quarters · 2026-06-30 · 22.9% · data/features/fct_bank_features.parquet: deposit_growth_4q
- F74 · National median: deposit growth over the past four quarters · 2026-06-30 · 4.2% · data/features/fct_bank_features.parquet: deposit_growth_4q (median of all banks)
- F75 · Driver up #1: return on equity (profit as a share of equity), value -43.1%; contribution to the score · 2026-06-30 · +1.775 · data/analyst/scores.parquet: feature return_on_equity contribution
- F76 · Driver up #2: the Tier 1 risk-based capital ratio, value 7.7%; contribution to the score · 2026-06-30 · +0.537 · data/analyst/scores.parquet: feature tier1_risk_based_ratio contribution
- F77 · Driver up #3: commercial real estate loans as a share of loans, value 1.1%; contribution to the score · 2026-06-30 · +0.369 · data/analyst/scores.parquet: feature cre_loans_to_loans contribution
- F78 · Driver up #4: the total risk-based capital ratio, value 8.9%; contribution to the score · 2026-06-30 · +0.327 · data/analyst/scores.parquet: feature total_risk_based_ratio contribution
- F79 · Driver up #5: the leverage ratio (core capital as a share of average assets), value 3.6%; contribution to the score · 2026-06-30 · +0.149 · data/analyst/scores.parquet: feature leverage_ratio contribution
- F80 · Driver down #1: the Texas ratio (troubled assets against capital plus reserves), value 2.6%; contribution to the score · 2026-06-30 · -1.180 · data/analyst/scores.parquet: feature texas_ratio contribution
- F81 · Driver down #2: loans 90+ days past due or not accruing interest, as a share of loans, value 0.1%; contribution to the score · 2026-06-30 · -0.995 · data/analyst/scores.parquet: feature noncurrent_loans_to_loans contribution
- F82 · Driver down #3: nonaccrual assets and foreclosed property, as a share of assets, value 0.1%; contribution to the score · 2026-06-30 · -0.613 · data/analyst/scores.parquet: feature nonaccrual_ore_to_assets contribution
- F83 · Driver down #4: loan-loss reserves as a share of loans, value 1.0%; contribution to the score · 2026-06-30 · -0.131 · data/analyst/scores.parquet: feature allowance_to_loans contribution
- F84 · Driver down #5: loans as a share of deposits, value 82.8%; contribution to the score · 2026-06-30 · -0.092 · data/analyst/scores.parquet: feature loans_to_deposits contribution
- F85 · Training failures that were credit-loss failures (share) · n/a · 96% · data/replay/posthoc_metrics.json: failure_mix.training
- F86 · Failed banks in the training period · n/a · 539 · data/replay/posthoc_metrics.json: failure_mix.training
