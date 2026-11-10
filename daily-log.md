# Daily Log

## 2026-11-10
**Done**
- Phase 2 warehouse built (spec: [[specs/2026-11-09-phase2-warehouse-design]]).
- AWS set up and verified: bucket, Athena workgroup, Glue databases, $5/month budget, limited `canary-dev` user ([[runbooks/aws-setup]], [[decisions/0008-aws-setup-and-cost-guardrails]]).
- Dates re-stored as Parquet `date32` so Athena reads them ([[decisions/0007-dates-stored-as-date32]]); uploaded 103 raw files to S3.
- Athena raw tables with hand-written DDL; the quarter list is explicit because date projection found only 1 of 102 quarters ([[decisions/0006-athena-handwritten-ddl-and-dbt]]).
- dbt staging views and two mart tables with data tests: `stg_fdic__financials` 710,691 rows, `stg_fdic__failures` 4,117, `dim_failed_banks` 574, `fct_bank_quarters` 710,691. Tests: 18 pass, 1 expected warning (cert 34264 failed before the first financials quarter).
- Case-study label check: SVB and Signature at 2022-12-31 and First Republic at 2023-03-31 each have `quarters_until_failure` = 1.
- Docs: four data dictionary files (plus a test that every dbt column is documented), [[decisions/0005-fdic-api-only-no-bulk-call-reports]], [[runbooks/warehouse-refresh]], README, `CLAUDE.md` data sources line. 92 pytest tests pass.
- Found while writing the dictionary: `FUND` is a numeric code (1 to 5) pairing one-to-one with `SAVR`; the raw dictionary had described it wrongly. Fixed.

**Next**
- Phase 3: CAMELS-style features, XGBoost, train 2001-2015 / test 2016-2024 (time-based only; `failure_date` and `quarters_until_failure` are labels, never inputs).
- Fill in the AWS cost line in the README from the Billing console.
- Drop the throwaway Glue table `tmp_projection_check` (needs the owner's yes).

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
