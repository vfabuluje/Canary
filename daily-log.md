# Daily Log

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
