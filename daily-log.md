# Daily Log

## 2026-11-19
**Done**
- Free fix (PR #9, branch `showcase-first-errors`): the showcase report now records first-attempt checker errors per bank and a per-section tally.
- **Phase 5c built: "Compared with similar banks"** (spec [[specs/2026-11-18-phase5c-peers-design]], plan [[plans/2026-11-18-phase5c-peers]], decision [[decisions/0020-peer-comparison-descriptive]]). For each ratio in the national top or bottom 10%, the note shows whether it is also unusual among banks in the same FDIC specialty group and size tier (minimum 15 banks, with fallbacks). Answers: is the bank an outlier in its own category, or just a different category? **Descriptive only**, rule fixed before computing any bank's readings.
- New raw table `data/raw/specialty/` (FDIC `SPECGRP` and `CITY` per bank-quarter, 710,691 rows, 102 quarters, 0 null; the 45-field financials files untouched). City search in `ask` now works for every bank.
- FDIC label used as published, per quarter: SVB is "All Other Over 1 Billion" (group 9), stated in its note as a finding. Live SVB memo (2022-12-31): among its 23-bank peer group (including itself), HTM bond losses (98.1% of equity, peer median 0.6%) and uninsured deposits (86.4%, peer median 41.1%) are still unusually high; 7 other nationally unusual ratios are typical for its group.
- Built subagent-driven: 6 tasks with reviews, a whole-branch review (fixes: a "10%" figure no fact supported, paraphrases rejected, an optimistic cost estimate). 525 pytest pass.
- **Cost:** one live memo, $0.35. Dry-run estimate for re-running the 61 showcase notes with both new sections is now **$12.99** ($5.02 batch + $7.97 retry allowance at the measured 60% retry rate).

**Next**
- Merge `phase5c-peers` and PR #9 (owner's consent), then Phase 5d (concentration risk).
- After 5d: one paid showcase re-run with 5b+5c+5d sections, only after a fresh dry run and Victor's approval. Check the new first-attempt error tally (PR #9) to cut the retry rate first.

**Open questions**
- The retry rate (60%) roughly doubles the showcase cost. Worth one cheap diagnostic (a few memos with first-attempt errors logged) before the big run?

## 2026-11-18
**Done**
- Phase 5a merged (PR #7). Branch `phase5b-trend-agent` from `main`.
- **Phase 5b built: "How its ratios moved"** (spec [[specs/2026-11-18-phase5b-trend-design]], plan [[plans/2026-11-18-phase5b-trend]], decision [[decisions/0019-ratio-trends-descriptive]]). Each memo lists the ratios outside the bank's own prior range (prior 12 quarters; same quarter of the prior 3 years for year-to-date ratios), how fast they moved, and the model's contribution for that same ratio, side by side. **Descriptive only**: no measured result, the rule was fixed before looking at more banks and not tuned.
- Seen during spec review and kept on purpose: SVB's note (as of 2022-12-31) does not list HTM bond losses, because 98% was inside its 12-quarter range by then. At 2022-03-31 it is listed (48.4% vs a prior range of -11.7% to 6.6%). SVB's note instead shows funding signals (deposit growth, core deposits, FHLB borrowings, volatile funding) outside their ranges, all pushing the score down.
- Checker gained trend rules: one ratio per sentence when stating a contribution or direction; no contradicting direction or rank wording; no prediction words.
- Built with subagent-driven development: 5 tasks, task reviews, a whole-branch review (6 fixes, incl. a pairing gap and false rejections), two follow-up fixes. 471 pytest pass.
- **Showcase re-run:** 60 of 61 written, $7.98 (estimate $6.87). Cert 17719 failed twice (checker rejected the ordinal "98.2nd"); fixed the checker forms and re-ran it alone ($0.24, passed after one retry), so all 61 notes have the section. 36 of 60 needed a retry; the run report doesn't record first-attempt errors, so the cause is unknown.
- **Cost:** Claude API about $8.49 for 5b ($0.27 test memo + $7.98 showcase + $0.24 re-run of 17719); total so far about $14.14. AWS unchanged.

**Next**
- Merge `phase5b-trend-agent` (owner's consent), then Phase 5c (peer comparison).
- Done (same day, branch `showcase-first-errors`): the showcase report now records first-attempt checker errors per bank and a per-section tally, and the CLI prints it.
- Older 5a follow-ups still open: rename "(first flag)", the checker residuals in decision 0016.

**Open questions**
- Why did 60% of showcase memos need a retry? Needs the first-attempt errors logged before the next paid run.
- Is `efficiency_ratio` really year-to-date in FDIC data? (Spec §11, Claude's call.)

## 2026-11-17
**Done**
- **Repo location:** the vault symlink `Obsidian Vault/canary` now points to `~/code/canary`. I checked the old `canary-OLD` folder: nothing is missing from the repo, so it is safe to delete (not yet deleted).
- **Phase 5 split into 5a-5d, in this order:** 5a risk analyst, 5b trend/watchlist agent, 5c peer-comparison agent (adds the FDIC specialty label), 5d concentration-risk agent.
- **5a built** (spec [[specs/2026-11-17-phase5a-risk-analyst-design]], plan [[plans/2026-11-17-phase5a-risk-analyst]]): fact sheet, Claude memo, citation checker, note renderer, showcase batch, `ask` agent. Decisions [[decisions/0016-analyst-memo-design]], [[decisions/0017-analyst-agent-tool-runner]], [[decisions/0018-failures-after-test-window]]; runbook [[runbooks/analyst]].
- **Reviews caught:** a history tail-before-sort bug, the 2025-failure outcome rule, an unsaved batch id, and checker false rejections and false acceptances.
- **Live model comparison** ([[analysis/phase5a-model-compare]]): Opus 5.5 passed 1 of 3 first try, Sonnet 5.5 0 of 3; both 3 of 3 after retry; $0.47 vs $0.21. Run 1 ($0.80) was discarded because the checker rejected the "1" in "Tier 1". Owner chose Opus.
- **Showcase:** 61 banks, 61 written, 0 failed (43 first try, 18 after retry); $3.94; outcomes 25 caught, 8 missed, 5 false alarms, 23 on the watchlist. Trimmed to the latest watchlist's top 20 to control cost.
- **After the test window:** all 4 banks that failed in 2026 were flagged 4 quarters ahead (not part of the reported results; see RESULTS.md and decision 0018). Santa Anna (2025) is a reported miss.
- **Cost:** Claude API about $5.65 for 5a (compare $1.48, showcase $3.94, `ask` tests about $0.20). AWS unchanged.

**Next**
- Whole-branch merge of `phase5a-risk-analyst` (owner's consent), then Phase 5b design.
- Small follow-ups: rename "(first flag)" to make clear it is the first flag in the final four quarters; fix the dry-run estimate constants; the checker residuals listed in decision 0016.

**Open questions**
- Regenerate the other 67 latest-watchlist notes later?
- Should the after-window catches get a fuller write-up?

## 2026-11-14
**Done**
- Vault: `dashboard.md` (Dataview index of decisions, specs, runbooks) and `canary-roadmap.md` (Kanban board); per-device Obsidian state and the Smart Connections cache added to `.gitignore` (PR #5, merged).
- **Repo moved out of iCloud to `~/code/canary`.** iCloud had evicted about 946 repo files (including `pyproject.toml` and `.git` objects) and would not download them again, so pytest could not start; it also left a stale `origin/main` lock and `data 2` / `.venv 2` duplicates. Fresh clone from GitHub, local-only files copied (`data.nosync`, `.env`, `CLAUDE.local.md`, Obsidian plugins, dbt packages), venv rebuilt with identical package versions. The old folder in `~/Documents/Obsidian Vault/canary` is untouched.
- **Phase 4 built** (spec [[specs/2026-11-11-phase4-replay-design]], plan [[plans/2026-11-11-phase4-replay]]): `canary.replay` package (run-risk check, corrected Texas baseline, failure mix, what-if, contributions, misses, false alarms) and CLI. Live run on real data, local only, model folder unchanged (checksums). Decisions [[decisions/0013-run-risk-check]], [[decisions/0014-corrected-texas-baseline]], [[decisions/0015-failure-mix-profiles]]; report [[analysis/phase4-replay]]; dictionary [[replay_outputs]]; runbook, glossary, README updated. 179 pytest pass.
- **Findings.** 515 of 539 training-era failures (96%) had a credit-loss profile; 1 looked like SVB. The model is flat in HTM loss for SVB (0 to 1.5 x equity gives the same score). In the test years 19 of 21 caught failures had the credit-loss profile and 0 of 8 misses did. Run-risk check (post-hoc): SVB flagged 4 quarters ahead (rank 9 of 4,861 at 2022-03-31), but 3 of 29 recall, AUC 0.515, 846 never-failed banks flagged; Signature and First Republic missed. Corrected Texas baseline (post-hoc): 20 of 29, AUC 0.803, so the model's recall edge over a fair baseline is one bank.

**Next**
- Whole-branch review of `phase4-replay`, then merge (owner's consent).
- Open `~/code/canary` as the Obsidian vault; delete the old iCloud copy once nothing is missing.
- Phase 5: AI risk analyst agent.

**Open questions**
- Are the credit-loss cut-offs (noncurrent >= 5%, Texas >= 100%) right? ([[decisions/0015-failure-mix-profiles]])
- Several model misses (e.g. Washington Federal 2017, Enloe 2019, Heartland Tri-State 2023) had clean loan books; were they non-financial failures (e.g. fraud)? Needs cited sources before saying so.
- Should a later model add HTM loss and uninsured share with a different training approach? Any such model must be reported as post-hoc for 2023.

## 2026-11-11 (session 3: README for two readers)
**Done**
- README rewritten in layers (spec: [[specs/2026-11-11-readme-layers-design]]): a plain-English top (what Canary is, the SVB story, what I found, why it missed the 2023 banks, what's next, built with) for a skimming recruiter, then a "Technical detail" part for engineers. Every term glossed on first use.
- New `RESULTS.md` holds the full case-study tables with top signals and the full miss analysis; the README keeps compact per-bank tables. A number check confirmed no figure was lost; all links resolve.
- Phase 4 spec, plan and Task 1 are on branch `phase4-replay` (paused by choice; interrupted Task 2 files are in `git stash`, "phase4 task2 partial").

**Next**
- Merge `readme-layers` (owner's consent). Resume Phase 4 at Task 2 in a few days.

**Open questions**
- None new. (Phase 4's open question on the credit-loss cut-offs is on branch `phase4-replay`.)

## 2026-11-11 (session 2: Phase 4 started, then paused)
**Done**
- Phase 4 spec approved: [[specs/2026-11-11-phase4-replay-design]]. Chosen approach: a post-hoc run-risk check (uninsured share × bond losses ÷ equity, top 2% per quarter, decision 0011's rule), kept separate from the clean Phase 3 test; plus a corrected Texas baseline and error analysis (failure mix, what-if, contributions, misses, false alarms).
- Pre-look (scratch, recorded in spec §5 as the reason the check is post-hoc): SVB ranks 3rd-70th of ~4,800 every quarter 2021-12-31 to 2022-12-31 on run-risk; Signature 23rd at 2021-12-31 then 184th-348th; First Republic ~87th percentile (its losses were on loans, which FDIC data can't see). 1,106 banks had bond losses ≥ 50% of equity at 2022-12-31, so bond losses alone don't single SVB out.
- Plan written: [[plans/2026-11-11-phase4-replay]] (7 tasks). Task 1 done and reviewed (shared synthetic test fixtures moved to `tests/conftest.py`; 142 tests pass).
- Paused by choice during Task 2; work resumes in a few days.

**Next**
- Resume the plan at Task 2 (subagent-driven). Leftover uncommitted Task 2 files from the interrupted run (`src/canary/replay/`, `tests/test_replay_runrisk.py`, edit to `src/canary/model/train.py`) should be reviewed or discarded first.
- Merge Phase 4 branch only after the whole-branch review (owner's consent).
- Tooling: install `uv` (`brew install uv`) so the `aws-mcp` server can start; retry the failed Claude Code auto-update (`claude update`).

**Open questions**
- Are the credit-loss profile cut-offs (noncurrent ≥ 5% or Texas ≥ 100%) the right rules of thumb? (Spec §8.1, Claude's call.)

## 2026-11-11
**Done**
- Phase 3 built (spec: [[specs/2026-11-11-phase3-features-model-design]]): `fct_bank_features` (710,691 rows, 31 features), Athena export, XGBoost training, evaluation, Texas-ratio baseline, case studies ([[decisions/0009-features-and-zero-handling]], [[decisions/0010-label-and-time-split]], [[decisions/0011-watchlist-flag-and-metrics]], [[decisions/0012-feature-export-via-unload]]).
- Live run, test once on 2016-2024 (188,250 rows, 102 positive): AUC 0.902 vs baseline 0.774; recall 21 of 29 vs 19 of 29; median lead time 4 quarters (from report date). False-alarm rate 98.3%, mostly structural (2% watchlist, few failures; about 32x better than random).
- **SVB, Signature and First Republic were not flagged in any quarter.** Signature closest (94.9th percentile at 2022-12-31); SVB fell to the 27th percentile. Verified (read-only contributions check): in SVB's 2022 reports low interest expense, strong Tier 1 capital, a low Texas ratio and a large securities book (each about -0.9 to -1.1) pushed it toward safe; its HTM loss (about 98% of equity) contributed only about -0.16. Among positive training rows the HTM-loss ratio 99th percentile is about 0.17 and only 11 exceed 0.3, so the model never saw large HTM losses before failure. Hypothesis (not proven): training failures were mostly credit-loss failures of 2008-2012. Also: the baseline ranks insolvent banks (negative Texas ratio) as safest, so the 21-vs-19 recall gap is effectively one bank (cert 9956); a corrected baseline goes to Phase 4 as post-hoc. SVB's 2022-09-30 and 2022-12-31 scores are identical despite different HTM ratios (model insensitive there).
- Docs: [[runbooks/model-training]], README results and limitations (uninsured-deposit line corrected, validation-gap caveat added), TOOLS.md, data dictionary quirks. 142 pytest pass; dbt test 24 pass, 5 warn, 0 errors.

**Next**
- Phase 4: SVB / Signature / First Republic replay and error analysis: why they were missed, and what signal would have caught them. Any change made after seeing the 2023 results means 2016-2024 is no longer a clean out-of-sample test, so report such changes separately.
- Merge the Phase 3 branch (owner's consent).

**Open questions**
- Does adding bond-loss and uninsured-deposit signals help without training on 2023 failures, or is a different approach needed? (Phase 4)
- Is a 2% watchlist the right size, given 746 banks that had not failed by the end of 2025 flagged at least once?

## 2026-11-10
**Done**
- Phase 2 warehouse built (spec: [[specs/2026-11-09-phase2-warehouse-design]]).
- AWS set up and verified: bucket, Athena workgroup, Glue databases, $5/month budget, limited `canary-dev` user ([[runbooks/aws-setup]], [[decisions/0008-aws-setup-and-cost-guardrails]]).
- Dates re-stored as Parquet `date32` so Athena reads them ([[decisions/0007-dates-stored-as-date32]]); uploaded 103 raw files to S3.
- Athena raw tables with hand-written DDL; the quarter list is explicit because date projection found only 1 of 102 quarters ([[decisions/0006-athena-handwritten-ddl-and-dbt]]).
- dbt staging views and two mart tables with data tests: `stg_fdic__financials` 710,691 rows, `stg_fdic__failures` 4,117, `dim_failed_banks` 574, `fct_bank_quarters` 710,691. Tests: 18 pass, 1 expected warning (cert 34264 failed before the first financials quarter).
- Dropped the temporary projection-test table, with owner approval.
- Case-study label check: SVB and Signature at 2022-12-31 and First Republic at 2023-03-31 each have `quarters_until_failure` = 1.
- Docs: four data dictionary files (plus a test that every dbt column is documented), [[decisions/0005-fdic-api-only-no-bulk-call-reports]], [[runbooks/warehouse-refresh]], README, `CLAUDE.md` data sources line.
- Found while writing the dictionary: `FUND` is a numeric code (1 to 5) consistently pairing with `SAVR`; the raw dictionary had described it wrongly. Fixed.
- Final whole-branch review fixes: the uploader now fails loudly on an empty or wrong `--root` (it used to report success with 0 files); both CLIs warn if the AWS profile isn't `canary`; the label check is stricter (no report may be dated after its bank's failure). 100 pytest tests pass (93 unit + 7 data); dbt tests 18 pass, 1 expected warning.
- AWS cost so far: $0.00 (Billing console, 2026-11-10). Recorded in the README.
- Opened PR #2 (`phase2-warehouse` → `main`).

**Next**
- Phase 3: CAMELS-style features, XGBoost, train 2001-2015 / test 2016-2024 (time-based only; `failure_date` and `quarters_until_failure` are labels, never inputs).
- Merge PR #2, then branch Phase 3 off `main`.

**Open questions**
- How to handle the amended-values-only limitation in the SVB replay. Decision 0005 says bulk call reports probably would not fix it; still open.
- How to treat 0 as "not reported" vs a real zero (Phase 3).
- Resolved: store dates as timestamps or a date type? Dates are `date32`, see [[decisions/0007-dates-stored-as-date32]].

## 2026-11-09
**Done**
- Installed Homebrew and the GitHub CLI (`gh`); confirmed Obsidian is installed.
- Initialized git in the vault folder, added `.gitignore` (Python, `.env`, `data/`, Obsidian workspace files). See [[decisions/0001-git-repo-and-gitignore]].
- First commit; pushed to public GitHub repo `vfabuluje/Canary`.
- Moved "About me" out of `CLAUDE.md` into gitignored `CLAUDE.local.md` so personal details stay off GitHub.

- Built and tested the Phase 1 FDIC pull (spec: [[specs/2026-11-09-phase1-fdic-ingestion-design]]). Full pull: 710,691 financial rows over 102 quarters, 4,117 failure rows, 172 MB, 6 min 47 s. 62 tests passing (55 unit + 7 data checks).
- Built with subagent-driven development: one implementer + one reviewer per task, then a whole-branch review. Reviews caught 4 wrong banking definitions in the data dictionary (ROA/NIM annualized, $100K insurance limit pre-2008, past-due excludes nonaccrual, FHLB isn't emergency funding) and 2 error-handling gaps (an empty API answer could overwrite good data; dropped connections weren't retried). All fixed.
- Wrote decisions [[decisions/0002-parquet-partitioned-by-quarter]], [[decisions/0003-curated-45-financial-fields]], [[decisions/0004-store-raw-values-unchanged]], the runbook [[runbooks/fdic-ingestion]], the README, and filled in data dictionary row counts.

**Next**
- Merge and push the Phase 1 branch (owner's consent).
- Phase 2: call report pipeline to S3/Athena, dbt models and data tests.

**Open questions**
- How to handle the amended-values-only limitation in the SVB replay (FFIEC call reports may help; to check in Phase 2).
- How to treat 0 as "not reported" vs a real zero (Phase 3).
- Store dates as Parquet timestamps (now) or convert to a date type for Athena? See [[decisions/0002-parquet-partitioned-by-quarter]] Phase 2 notes.
