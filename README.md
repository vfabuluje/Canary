# Canary

**Can public data spot a failing bank before it fails?**

**Research tool, not financial advice.**

## What Canary is
Canary is an early-warning system for US banks. Every quarter, each FDIC-insured bank (about 4,300 today, nearly 10,000 in 2001) publishes its financial results. Canary reads all of them and ranks every bank by how likely it is to fail within the next year. The big test: would it have warned about Silicon Valley Bank, Signature Bank and First Republic before they collapsed in 2023?

**Why the name "Canary"?** Coal miners once carried canaries underground. The birds reacted to toxic gas before people did, so a sick canary was the signal to get out. Canary aims to be that early signal for banks.

## The SVB story
Silicon Valley Bank (SVB) served tech startups. In 2020-2021 it took in a flood of deposits and put much of the money into long-term government bonds while interest rates were low. In 2022 rates rose quickly, and those bonds lost value. Most of SVB's deposits were also uninsured: above the FDIC's $250K protection limit, so customers had a reason to run at the first sign of trouble. In March 2023 SVB announced it had sold bonds at a loss, customers pulled about $42B in one day, and regulators closed the bank on March 10, 2023.

The warning signs were in SVB's public filings months earlier. Its last report before failing (2022 Q4) showed:

| Signal | Value |
|---|---|
| Held-to-maturity bonds, cost vs fair value | $91.3B vs $76.2B ($15.2B unrealized loss) |
| Equity | $15.5B, so the bond loss was about all of it |
| Uninsured deposits | 86% ($151.6B of $175.4B) |

("Held-to-maturity" bonds are ones a bank says it will keep until they pay out. They stay on the books at what the bank paid, so a fall in their market value doesn't reduce the bank's reported profit or its equity, its capital cushion. "Unrealized loss" means the bonds are worth less than the bank paid, but it hasn't sold them yet.)

## What I found
I trained a machine-learning model on bank reports from 2001-2014, then tested it, once, on 2016-2024, years it had never seen. That is the honest way to check whether a model would have worked at the time.

- **It caught most failing banks early.** Of the 29 banks that failed in the test years (and had a report 1 to 4 quarters before failing), the model put 21 (72%) on its watchlist (the 2% of banks it rates riskiest each quarter) at least once before they failed, usually at the earliest point the test checks: 9 to 12 months before failing, counted from the report date (the report itself becomes public about a month later).
- **It ranks banks better than a classic rule of thumb.** Its AUC is 0.902, against 0.774 for the "Texas ratio" (bad loans compared with the bank's cushion to absorb them), a rule analysts have used for decades. AUC is the chance that a bank about to fail gets a higher risk score than one that isn't: 0.5 is a coin flip, 1.0 is perfect.
- **Most of its warnings were false alarms, which is expected.** The watchlist holds about 105 banks a quarter, while only about 3 banks fail a year. So about 98% of the times a bank was flagged, it did not fail within a year. Even so, a flagged bank was about 32 times more likely to fail soon than a random bank.
- **It missed SVB, Signature and First Republic.** None of the three was on the watchlist in any quarter. Right before it failed, the model rated SVB safer than most banks.

## Why it missed SVB, Signature and First Republic
A model can only learn from the failures it has seen. Most banks that failed in 2001-2014 failed in the 2008-2012 crisis, and the data confirms it was about bad loans: 515 of the 539 failures (96%) had bad loans when they failed, and only one looked like SVB. SVB failed differently: its loans were fine, but its bonds lost value and its uninsured depositors ran.

The training data shows how unusual that was. SVB's held-to-maturity bond loss was about 98% of its equity. In 99% of the training reports from banks about to fail, that loss was about 17% of equity or less. So the model had almost never seen "large bond loss, then failure" (only 11 training reports from banks about to fail had a bond loss above 30% of equity), and it read SVB's cheap funding, strong capital and big bond book as signs of safety. That is the honest result: **a model trained only on data from before 2015 did not catch SVB.** The full analysis is in [RESULTS.md](RESULTS.md).

**What would have caught it?** After seeing the 2023 failures, I tested one simple check: bond losses as a share of equity, multiplied by the share of uninsured deposits. It would have put SVB on a 2%-of-banks watchlist from its March 2022 report (ranked 9th of 4,861 banks), which became public about a month later, roughly ten months before SVB failed. But it caught only 3 of the 29 banks that failed in 2016-2024, missed Signature and First Republic, and flagged 846 banks that never failed. Because the check was designed with the answer in view, it is reported separately from the clean test above, as a second lens and not a fix. First Republic's main losses were on mortgages it held as loans, which FDIC data has no market value for. Full write-up: [analysis/phase4-replay.md](analysis/phase4-replay.md).

## The plan, in six phases
1. **Collect the data (done).** Download every US bank's quarterly financial report since 2001, plus the FDIC's list of every bank that failed.
2. **Build the warehouse (done).** Store the data in the cloud (AWS) and clean it into tidy, tested tables, so every number can be trusted and traced.
3. **Train and test the model (done).** Turn each report into about 30 health measures (capital, bad loans, profits, funding, bond losses), train the model on 2001-2014, and test it once on 2016-2024. The results are above.
4. **Replay the 2023 failures (done).** Work out why SVB, Signature and First Republic were missed, and test whether a simple, explainable check (bond losses combined with uninsured deposits) would have flagged them, and at what cost in false alarms. It is reported separately from the clean test, because it was designed after seeing the 2023 failures. The results are above.
5. **Add AI analyst agents and sections (5a-5d done).** The risk analyst, an AI agent (Claude), writes a short memo for a bank citing the exact quarter and numbers it relies on, and a code checker rejects any number it cannot trace. 61 notes are written. The memo has since grown sections: 5b and 5c are AI-written sections (written by the risk analyst, checked by the same code checker), and 5d is a code-written section. The trend section (5b) is built and in all of them: every new memo shows which of the bank's ratios left their own prior range, descriptive only, with no measured result. The peer section (5c) is built: each new memo compares the bank with banks the FDIC puts in the same specialty group and size tier, descriptive only, with no measured result; the 61 committed notes do not have it yet (the showcase is re-run once after 5d). The concentration section (5d) is built: each new memo checks whether the bank crossed the two 2006 regulator lines for commercial real estate lending (supervisory screens, not predictions, with no measured result). It is written by code, not by an AI agent, and adds no Claude API cost; the 61 committed notes do not have it yet either.
6. **Build a dashboard.** An interactive web page to look up any bank's risk over time, plus a short demo video.

## Built with
Python and pandas for the data pipeline; AWS (S3, Athena, Glue) as the data warehouse; dbt for tested data models; XGBoost for the model. Claude (via the Claude API) as the AI risk analyst that writes cited risk memos per bank; a Streamlit dashboard is planned. All data is public, from the FDIC.

---

# Technical detail

The rest of this page is for readers who want the method, the numbers behind the summary, the limitations and how to run it.

## Results (2016-2024 test, run once)
**The question:** from public quarterly data alone, can a model trained only on data from before 2015 pick out the banks that failed in 2016-2024, including SVB, Signature Bank and First Republic, before they failed?

**The setup.** An XGBoost model on 31 CAMELS-style ratios (the capital, asset quality, earnings, liquidity and interest-rate sensitivity measures bank supervisors use), trained on report dates 2001-03-31 to 2014-12-31. 2015 is dropped, because whether a 2015 bank failed "within 4 quarters" depends on 2016 failures, which belong to the test years ([decision 0010](decisions/0010-label-and-time-split.md)). A row is "positive" if the bank failed 1 to 4 quarters after that report. Each quarter the 2% of banks with the highest score are flagged ([decision 0011](decisions/0011-watchlist-flag-and-metrics.md)). The test set has 188,250 bank-quarters, 102 of them positive. The baseline is the Texas ratio (bad loans and foreclosed property divided by equity plus loan-loss reserve), flagged the same way. Numbers come from `metrics.json` of the single evaluation run.

| Metric | XGBoost | Texas-ratio baseline |
|---|---|---|
| AUC (2016-2024) | 0.902 | 0.774 |
| Recall: failed banks flagged at least once 1-4 quarters before failing | 21 of 29 (72%) | 19 of 29 (66%) |
| Recall with 2+ quarters notice | 18 of 27 (67%) | 17 of 27 (63%) |
| Lead time (first flag, quarters before failure): median, range | 4, 1-4 | 4, 1-4 |
| False-alarm rate (flagged rows not within 4 quarters of failing) | 98.3% | 98.4% |
| Never-failed banks flagged at least once in 9 years | 746 | 544 |

**Reading the numbers.**
- **Small sample.** The 29 "eligible" banks are the failed banks with at least one report 1-4 quarters before failure from 2016 on, so one bank moves recall by about 3 points. The gap between 21 and 19 is two banks, not strong evidence.
- **The recall gap is effectively one bank.** When a bank's equity plus loan-loss reserve is below zero (insolvent), its Texas ratio comes out negative, so the baseline ranks it as the safest bank. Of the 102 positive test rows, 3 have a negative Texas ratio (certs 8758, 19328, 9956). The baseline caught the first two banks on earlier quarters, but the only eligible row for cert 9956 (2016-03-31, 1 quarter before failure) was missed by the baseline purely because of that sign, while the model flagged it. The baseline was not corrected after seeing the results.
- **The 98.3% false-alarm rate is mostly built in.** The watchlist flags 2% of about 5,200 banks on average, about 105 per quarter (3,783 flagged rows over 36 quarters), while only about 3 banks fail per year. Even a good ranking cannot avoid flagging many banks that survive. Precision is about 1.7% against a base rate of 102 / 188,250 = 0.054%, so a flagged bank is about 32 times more likely to be a near-term failure than a random one. Still, 746 different banks that did not fail within the window were flagged at least once over 9 years; a supervisor would call that a lot of wasted attention.
- **Lead time is capped at 4 by the label window**, so a median of 4 means most caught banks were already flagged at the earliest point the label can show. It is counted from the report date. Reports become public about a month after quarter-end, so the real warning is about a month shorter.
- **The Texas-ratio baseline is hard to beat on recall**; the model's clearer advantage is the overall ranking (AUC).
- **No tuning on the test years.** The settings were chosen on a 2012-2014 validation block. Settings: max depth 5, learning rate 0.1, min child weight 10, 79 trees, seed 42 (`run_config.json`).

## Case studies: SVB, Signature, First Republic
**None of the three was flagged in any quarter**, by the model or by the Texas-ratio baseline. Percentile is the bank's risk rank among all banks that quarter (99 = riskier than 99% of banks). The flag needs the top 2%: rank 96 or better for 4,773 banks, about the 98th percentile. Rank 1 is the riskiest bank. The full tables, with the signals that pushed each score up, are in [RESULTS.md](RESULTS.md).

**Silicon Valley Bank**

| Report | Qtrs before failure | Percentile | Rank / banks | Flagged |
|---|---|---|---|---|
| 2021-03-31 | 8 | 75.0 | 1263 / 5044 | no |
| 2021-06-30 | 7 | 79.7 | 1018 / 5015 | no |
| 2021-09-30 | 6 | 77.1 | 1142 / 4979 | no |
| 2021-12-31 | 5 | 56.0 | 2160 / 4904 | no |
| 2022-03-31 | 4 | 25.2 | 3638 / 4861 | no |
| 2022-06-30 | 3 | 7.2 | 4489 / 4838 | no |
| 2022-09-30 | 2 | 24.4 | 3640 / 4813 | no |
| 2022-12-31 | 1 | 26.8 | 3494 / 4773 | no |

**Signature Bank**

| Report | Qtrs before failure | Percentile | Rank / banks | Flagged |
|---|---|---|---|---|
| 2021-03-31 | 8 | 79.8 | 1022 / 5044 | no |
| 2021-06-30 | 7 | 83.4 | 831 / 5015 | no |
| 2021-09-30 | 6 | 81.7 | 913 / 4979 | no |
| 2021-12-31 | 5 | 79.9 | 986 / 4904 | no |
| 2022-03-31 | 4 | 49.5 | 2456 / 4861 | no |
| 2022-06-30 | 3 | 55.3 | 2162 / 4838 | no |
| 2022-09-30 | 2 | 91.3 | 420 / 4813 | no |
| 2022-12-31 | 1 | 94.9 | 246 / 4773 | no |

**First Republic Bank**

| Report | Qtrs before failure | Percentile | Rank / banks | Flagged |
|---|---|---|---|---|
| 2021-03-31 | 9 | 80.3 | 995 / 5044 | no |
| 2021-06-30 | 8 | 73.6 | 1327 / 5015 | no |
| 2021-09-30 | 7 | 88.7 | 566 / 4979 | no |
| 2021-12-31 | 6 | 80.7 | 948 / 4904 | no |
| 2022-03-31 | 5 | 28.0 | 3502 / 4861 | no |
| 2022-06-30 | 4 | 32.6 | 3262 / 4838 | no |
| 2022-09-30 | 3 | 35.7 | 3095 / 4813 | no |
| 2022-12-31 | 2 | 29.7 | 3355 / 4773 | no |
| 2023-03-31 | 1 | 83.0 | 809 / 4740 | no |

### What was caught, what wasn't, and why
- **Closest calls.** Signature came closest: 94.9th percentile at 2022-12-31 (rank 246, against a cutoff of rank 96). First Republic reached the 83rd percentile in its last report. SVB was around the 80th percentile in mid-2021, then **fell** to the 27th percentile by 2022-12-31.
- **Bond losses did register, but not enough.** Unrealized losses on available-for-sale (AFS) bonds were the top push upward for SVB and Signature in the second half of 2022.
- **SVB's held-to-maturity (HTM) loss did not.** It was about 98% of SVB's equity at 2022-12-31, but in all four 2022 reports it nudged the score slightly *down* (about -0.16 in the model's log-odds units). Low interest expense (about -1.1), strong Tier 1 capital (about -1.0), a low Texas ratio (about -1.0) and a large securities book (about -0.9) pushed SVB toward "safe".
- **The model had nothing to learn the HTM signal from.** Among the 2,134 positive training rows, the 99th percentile of HTM loss ÷ equity is about 0.17, and only 11 exceed 0.3 (145 across all 470,361 training rows), compared with SVB's roughly 0.5 to 1.0 in 2022.
- **The model does not react to HTM loss at all for SVB.** SVB's 2022-09-30 and 2022-12-31 reports got identical scores (0.0023) although their HTM ratios differed (about 1.05 vs 0.98). Phase 4's what-if test explains it: setting SVB's 2022-12-31 HTM loss to anything from 0 to 1.5 times equity leaves the score at 0.0023 (`what_if.csv`).
- **Confirmed in Phase 4:** the training years are dominated by credit-loss failures. 515 of 539 training-era failures (96%) had noncurrent loans of at least 5% or a Texas ratio of at least 100%; 1 had SVB's profile. In the test years, 19 of the 21 banks the model caught had that credit-loss profile, and none of the 8 it missed did.

Full contribution analysis and per-quarter signals: [RESULTS.md](RESULTS.md).

## Post-hoc: Phase 4 replay and error analysis
**Everything in this section was designed after seeing the 2023 failures, so it is not an out-of-sample test.** It does not change the model or the results above. Full report: [analysis/phase4-replay.md](analysis/phase4-replay.md); decisions [0013](decisions/0013-run-risk-check.md), [0014](decisions/0014-corrected-texas-baseline.md), [0015](decisions/0015-failure-mix-profiles.md).

- **Run-risk check:** `clip(uninsured / deposits, 0, 1) x (HTM + AFS unrealized loss) / equity`, top 2% per quarter (the model's watchlist rule). The formula was fixed before results were computed, and no variants were tried.
- **Corrected Texas baseline:** an insolvent bank (negative Texas ratio) ranks worst instead of safest.

| Metric (2016-2024) | Phase 3 model (clean) | Run-risk (post-hoc) | Corrected Texas baseline (post-hoc) |
|---|---|---|---|
| AUC | 0.902 | 0.515 | 0.803 |
| Recall, 1-4 quarters | 21 of 29 | 3 of 29 | 20 of 29 |
| Recall, 2+ quarters | 18 of 27 | 3 of 27 | 17 of 27 |
| Never-failed banks flagged | 746 | 846 | 527 |
| SVB | missed | flagged 4 quarters ahead (rank 9 of 4,861, 2022-03-31) | missed |
| Signature | missed | missed (on the list in 2021, 5-8 quarters out, then off) | missed |
| First Republic | missed | missed (best rank 599) | missed |

- **The run-risk check is a narrow detector, not a risk score.** Its AUC is a coin flip, because bond losses and uninsured deposits are not what sank most banks. By late 2022, rising rates had given 1,360 banks bond losses of at least half their equity, which is why Signature dropped off the list.
- **The model's recall edge over a fair baseline is one bank** (21 vs 20). Its clearer advantage is the ranking (AUC 0.902 vs 0.803).
- **First Republic is a data limit:** its main losses were on low-rate mortgages held as loans, and FDIC financials give market values for securities only.

## Limitations
- **Amended data only.** The FDIC API serves current, corrected values, not what banks originally filed. The SVB replay uses numbers as corrected later, not exactly what an analyst saw at the time.
- **0 can mean "not reported."** Some fields did not exist in early years. Phase 1 keeps the 0; Phase 3 applies documented 0-to-null rules when building the features ([decision 0009](decisions/0009-features-and-zero-handling.md)).
- **FDIC API only.** Bulk FFIEC call reports are deferred ([decision 0005](decisions/0005-fdic-api-only-no-bulk-call-reports.md)); they appear to hold amended values too, so they would likely not fix the limitation above.
- **The real warning window is shorter than the label suggests.** Banks file each quarter's report about a month after the quarter ends. SVB's December 31, 2022 numbers became public around late January 2023, roughly six weeks before it closed on March 10, not a full quarter earlier. Any lead time Canary reports is counted from the report date, so the time an analyst would really have had is about a month less.
- **Small test, rare events.** 29 eligible failed banks and 102 positive rows: results are noisy, and no confidence intervals are reported.
- **Validation is slightly optimistic.** The inner validation split (fit through 2011, validate 2012-2014) has no gap: fit rows from late 2011 carry labels from 2012 failures, which fall inside the validation block. This slightly flatters the validation score used to pick settings. It does not affect the test result.
- **Outliers kept in the features.** About 183 of 710,691 feature rows fall outside their expected 0-1 range (reporting errors); they were kept as-is ([data dictionary](data-dictionary/fct_bank_features.md)). Tree models are robust to them.
- **Uninsured-deposit estimates** are filled in for about 99% of banks every year, so they are not limited to large banks ([decision 0009](decisions/0009-features-and-zero-handling.md)). Reported 0s are treated as missing in the feature. The estimate is a regulatory one, not an exact count.
- **Failure label is FDIC closures only.** A distressed bank that was acquired or merged before it failed counts as a survivor, so some "false alarms" may be real near-failures. This inflates the false-alarm rate.
- **No market values for loans.** FDIC financials give fair values for securities only. A bank whose losses sit in low-rate loans (First Republic's mortgages) looks healthy on every feature here.
- **Phase 4 checks are post-hoc.** The run-risk check and corrected baseline were designed after seeing the 2023 failures and are not out-of-sample results; they are kept out of the headline numbers ([decision 0013](decisions/0013-run-risk-check.md)).
- Dollar income fields are year-to-date and dollar amounts are in thousands.

See `decisions/` for the reasoning and `data-dictionary/` for every column.

## How it works
### Architecture
```
FDIC BankFind API
      |  python -m canary.ingest            (Phase 1)
      v
local Parquet  data/raw/            one folder per quarter
      |  python -m canary.upload            (skips unchanged files, never deletes)
      v
S3  raw/fdic/
      |  python -m canary.athena_ddl        (raw tables; rerun after a new quarter)
      v
Athena raw tables   canary_raw
      |  dbt build                          (needs the owner's yes: replaces mart tables)
      v
stg_fdic__financials, stg_fdic__failures    views      canary_staging
dim_failed_banks, fct_bank_quarters         tables     canary_marts
fct_bank_features                           table      canary_marts  (Phase 3)
      |  python -m canary.export_features   (Athena UNLOAD to local Parquet)
      v
python -m canary.model train / evaluate     XGBoost, metrics.json, case_studies.csv
      |
python -m canary.replay                     Phase 4 post-hoc checks and error analysis (local, read-only on the model)
```
What each tool is, why Canary uses it, and what it does here: [reference/STACK.md](reference/STACK.md).

### AI risk analyst (Phase 5a)
For a bank and a quarter, code builds a **fact sheet** of numbered facts from the data; Claude writes a **memo** that cites those fact numbers; a **citation checker** verifies every number and label sentence by sentence (one retry, and a memo that fails twice is not saved); then code renders the **note**. An `ask` agent answers questions in plain English using the same tools (for example "which banks are on the watchlist right now?"). Sample note: [banks/Silicon Valley Bank (24735).md](<banks/Silicon Valley Bank (24735).md>). How to run it: [runbooks/analyst.md](runbooks/analyst.md). Decisions: [0016](decisions/0016-analyst-memo-design.md) (memo design, model choice), [0017](decisions/0017-analyst-agent-tool-runner.md) (the `ask` agent), [0018](decisions/0018-failures-after-test-window.md) (failures after the test window). Model comparison: [analysis/phase5a-model-compare.md](analysis/phase5a-model-compare.md).
- **Showcase (2026-11-17, Claude Opus 5.5, batch):** 61 banks (a trimmed set, with only the latest watchlist's top 20 to control cost), 61 written, 0 failed; 43 passed the checker first try, 18 after one retry; 525,985 input and 216,030 output tokens, $3.94. Outcomes in the notes: 25 caught, 8 missed, 5 false alarms, 23 still on the watchlist.
- **Showcase re-run with the trend section (2026-11-18, Claude Opus 5.5, batch):** 61 banks, 60 written, 1 failed (cert 17719: the checker rejected the ordinal "98.2nd"; fixed, then re-run alone for $0.24, passing after one retry); 24 passed the checker first try, 36 after one retry; 999,817 input and 384,007 output tokens, $7.98 (dry-run estimate $6.87; more retries than the 30% assumed).
- **Claude API cost** is separate from AWS: about $14.14 so far (5a: model comparison $1.48, showcase $3.94, `ask` tests about $0.20; 5b: one test memo $0.27, showcase re-run $7.98, cert 17719 re-run $0.24). AWS cost is unchanged because Phase 5a runs locally.
- **Out-of-sample extra:** the 4 banks that failed after the test window (2026) were all flagged 4 quarters ahead. They are not part of the reported 2016-2024 results ([decision 0018](decisions/0018-failures-after-test-window.md), [RESULTS.md](RESULTS.md)).
- **Ratio trends (Phase 5b):** each new memo has a "How its ratios moved" section: the ratios outside the bank's own prior range, how fast they moved, and the model's contribution for the same ratio. It is **descriptive only**; the range rule is fixed by convention and has not been tested as a warning signal ([decision 0019](decisions/0019-ratio-trends-descriptive.md)). All 61 showcase notes have it (re-run 2026-11-18).
- **Peer comparison (Phase 5c):** each new memo has a "Compared with similar banks" section: for ratios in the national top or bottom 10%, whether the bank is also unusual among banks the FDIC groups with it (same specialty group and size tier). It is **descriptive only**, with no measured result ([decision 0020](decisions/0020-peer-comparison-descriptive.md)). The 61 committed notes get it at the next showcase re-run.
- **Real-estate concentration (Phase 5d):** each new memo has a "Real-estate concentration (2006 regulator thresholds)" section, written by code (no AI text, no API cost): whether the bank crossed the OCC/Fed/FDIC 2006 screens (construction at 100% of capital; total commercial real estate at 300% of capital with 50% growth over 36 months). Supervisory screens, not predictions, with **no measured result** ([decision 0021](decisions/0021-cre-concentration-2006-thresholds.md)). It covers memo quarters from 2016 on, so 2008-era failures are not covered. The 61 committed notes get it at the next showcase re-run.
- Memos are AI-written and checked for numbers and labels, not for every claim; see the limits in decisions 0016 and 0019.

### Scale (measured)
- **Financials:** 710,691 rows over 102 quarters (2001-03-31 to 2026-06-30); 9,940 banks in the first quarter, 4,313 in the latest.
- **Failures:** 4,117 rows (3,524 FAILURE, 593 ASSISTANCE; 574 FAILURE since 2001).
- **On disk:** 172 MB. Full pull: 6 min 47 s (102 API calls). Rerun: about 7 s.
- **Warehouse:** `fct_bank_quarters` 710,691 rows; `dim_failed_banks` 574 rows; `fct_bank_features` 710,691 rows with 31 features.
- **Model data:** 470,361 training rows (2,134 positive), 188,250 test rows (102 positive).
- **Tests:** 558 pytest tests passing. dbt: 29 data tests, 24 pass and 5 warnings, 0 errors. The warnings are the known ones: cert 34264 (First Alliance Bank and Trust Co, failed 2001-02-02, before the first quarter of financials) and four range checks on `fct_bank_features` (see [data-dictionary/fct_bank_features.md](data-dictionary/fct_bank_features.md)).
- **AWS cost so far:** $0.02 as of 2026-11-11, per the AWS Billing console (budget cap: $5/month). Billing posts with up to a day's delay, so the Phase 3 build and export (run 2026-11-11) may add a few cents.
- **Case-study label check:** SVB and Signature at 2022-12-31 and First Republic at 2023-03-31 each show 1 quarter until failure, meaning that report was the last one before the bank closed.

## Run it yourself
### Quickstart
```
python3.12 -m venv .venv
.venv/bin/pip install -e ".[dev]"
.venv/bin/python -m canary.ingest financials
.venv/bin/python -m canary.ingest failures
.venv/bin/pytest -v
```
More detail, including what to do if a pull fails: `runbooks/fdic-ingestion.md`.

### Refresh the warehouse
One-time AWS setup (bucket, Athena, budget, limited IAM user): [runbooks/aws-setup.md](runbooks/aws-setup.md). Copy `.env.example` to `.env` and set `CANARY_BUCKET`.

Each refresh, in order: `canary.ingest`, `canary.upload`, `canary.athena_ddl`, then `dbt build --no-partial-parse` from `warehouse/`. Details and what to do if a step fails: [runbooks/warehouse-refresh.md](runbooks/warehouse-refresh.md). Features, training and the one-time test: [runbooks/model-training.md](runbooks/model-training.md). To re-run only the dbt tests (read-only): `dbt test --no-partial-parse --profiles-dir .` from `warehouse/`.

## Status and roadmap
1. **(done) FDIC data pull.** Pulls quarterly financials for every FDIC-insured bank and the FDIC failed bank list to local Parquet files.
2. **(done) Warehouse.** The raw files are copied to S3, exposed as Athena tables, and cleaned into dbt models with data tests.
3. **(done) Features and model.** 31 CAMELS-style ratios per bank per quarter, an XGBoost model trained on report dates 2001-2014 and tested once on 2016-2024 (time-based only). Results are above.
4. **(done) SVB / Signature / First Republic replay; error analysis.** The training-era failure mix, a what-if test of the model, a post-hoc run-risk check and a corrected baseline. See the post-hoc section above and [analysis/phase4-replay.md](analysis/phase4-replay.md).
5. **(5a-5d done)** AI risk analyst agent that writes cited risk memos per bank (see below), now with descriptive ratio-trends and peer-comparison sections and a code-written real-estate concentration section (5d).
6. Streamlit dashboard; metrics and limitations; demo video.

## Reference
- [RESULTS.md](RESULTS.md): full case-study tables with the signals behind each score, and the full analysis of the misses.
- [analysis/phase4-replay.md](analysis/phase4-replay.md): Phase 4 replay, what-if test, training-era failure mix and the post-hoc run-risk check.
- [reference/STACK.md](reference/STACK.md): each tool in the stack (S3, Athena, Glue, IAM, dbt, XGBoost, Claude API, Streamlit, GitHub Actions): what it is and how Canary uses it.
- [reference/GLOSSARY.md](reference/GLOSSARY.md): banking and technical terms (CAMELS, FDIC, FFIEC, ROA, ROE, NIM, Tier 1 capital, PCA, HTM, AUC, XGBoost, DDL, dbt, IAM, MFA, S3), each tied to the columns and decisions where it appears.
