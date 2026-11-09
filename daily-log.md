# Daily Log

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
