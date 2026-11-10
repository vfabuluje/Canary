# Phase 2 Spec: FDIC Data → S3 / Athena → dbt Models and Tests

**Date:** 2026-11-09
**Status:** Approved by Victor 2026-11-09
**Phase:** 2 (see `CLAUDE.md`)

## 1. Intent: why this exists

Phase 1 saved two raw tables on the laptop as Parquet: FDIC quarterly financials (710,691 rows, 102 quarters, 45 fields) and the FDIC failed bank list (4,117 rows). Phase 2 turns them into a small **cloud data warehouse**:

1. The raw Parquet files live in **S3**.
2. **Athena** can query them with SQL, using table definitions stored in the **Glue Data Catalog**.
3. **dbt** builds clean, tested models on top: readable column names, proper dates, and one bank-quarter table that Phase 3 can build features from.

Two reasons. Phase 3 needs one clean, trusted table to engineer features from. And this is the core data-engineering work that bank data teams hire for (S3, Athena, Glue, dbt, data tests, cost control), so it must be built in a way Victor can explain line by line.

## 2. Scope decision: FDIC API only, no bulk FFIEC call reports (decided)

The FDIC BankFind API is built from the call reports and exposes about 2,400 fields, while Phase 1 pulls 45. The signals that matter most for SVB are already in Phase 1 (`DEPUNINS` uninsured deposits; `SCHA` − `SCHF` and `SCAA` − `SCAF` unrealized securities losses). The bulk FFIEC files are about 40 tab-separated schedule files per quarter with codes that change over 24 years, downloaded by hand or through a registered web service, and they appear to hold amended values too, so they would not fix the "amended values only" limitation.

**Decision:** Phase 2 uses the FDIC API data only. If Phase 3 or the SVB replay needs a field, add it to `FINANCIAL_FIELDS` and re-pull. A small call-report pull for specific missing fields stays a possible later add-on. Log this as a decision note and update the data sources line in `CLAUDE.md`.

## 3. Goals
- G1. Raw Parquet files in S3, same Hive-style layout as local (`repdte=YYYYMMDD/`).
- G2. Athena external tables over both raw tables, defined in SQL files in the repo.
- G3. A dbt project (dbt-athena) with staging models and mart models (see §7.5).
- G4. dbt data tests on every model, including the Phase 1 data checks moved into the warehouse.
- G5. Cost guardrails so AWS stays under $5/month (budget alert, per-query scan limit, auto-delete of query results).
- G6. Pipeline code (upload, DDL runner) has unit tests that need no AWS account.
- G7. Every new table and column in `data-dictionary/`; every major choice in `decisions/`; a runbook for setup and refresh.

## 4. Non-goals (later phases)
- No bulk FFIEC call reports (§2).
- No feature engineering, ratios, YTD-to-quarterly conversion, or the failure label definition (Phase 3). The marts only join facts that already exist.
- No model training, Lambda, or scheduling. GitHub Actions running dbt against AWS comes later.
- No new FDIC fields unless something in Phase 2 itself needs them.

## 5. Anti-goals (a failure even if it "works")
- **Credentials in git or in the repo folder.** AWS keys live only in `~/.aws/` under a named profile. The repo is public.
- **Using the AWS root account** for day-to-day work.
- **A surprise bill.** Any setup that could scan or store large amounts without a limit.
- **Silent data changes between raw and staging.** Staging renames and retypes; it does not filter rows or change values (except the documented date conversion). Row counts must match raw.
- **Black-box setup.** No crawler-guessed schemas, no click-only console steps that aren't written down in the runbook.

## 6. Approaches considered (for how to build the warehouse)

| # | Approach | Trade-off | Verdict |
|---|---|---|---|
| 1 | **dbt on Athena from day one; raw tables defined by hand-written `CREATE EXTERNAL TABLE` SQL** | One SQL dialect everywhere; every definition is readable code; pennies to run on 172 MB. Needs internet + AWS setup. | **Chosen by Victor** |
| 2 | Glue crawler discovers raw tables; dbt on top | Little SQL to write, but guesses types, can trip on the `repdte`/`REPDTE` clash, costs ~$0.44/run, hard to explain. | Rejected |
| 3 | dbt + DuckDB locally first, then switch to Athena | Free, offline, fast iteration; but DuckDB and Athena SQL differ, so everything is debugged twice and two setups are maintained. | Rejected |

Glue is still used: the Athena tables live in the Glue Data Catalog.

## 7. Design: the parts that are decided

### 7.1 AWS account setup (Victor has an existing AWS account, root login only today)
- **Region:** `us-east-1` (cheapest, all services available).
- **Step 0, account hygiene (Victor, in the console, guided by the runbook):** turn on MFA for the root user and stop using root. Create an admin IAM user for Victor with a console password and MFA. No access keys for root or for the admin user.
- **Admin setup runs in AWS CloudShell** (a browser terminal already signed in as the admin user), so no admin keys ever sit on the laptop. Victor runs `infra/setup.sh` there.
- **IAM:** `setup.sh` creates an IAM user `canary-dev` (no console password) with a **least-privilege policy** committed at `infra/iam-policy-canary-dev.json`: list/read/write on the Canary bucket only, with `s3:DeleteObject` allowed **only** under `athena-results/` and `dbt/` (never `raw/`); Athena on the `canary` workgroup only; Glue catalog actions on the Canary databases only; no IAM, billing, or other services. Victor creates one access key for `canary-dev` and saves it on his Mac with `aws configure --profile canary` (stored in `~/.aws/credentials`, outside the repo). All code and dbt use `AWS_PROFILE=canary`.
- **Who runs what:** Claude Code runs day-to-day AWS commands (upload, DDL, `dbt build`, checks) with the `canary` profile, never reading the credentials file. **Any delete in AWS (S3 objects, tables, databases, keys) needs Victor's explicit confirmation first.** Victor can cut access instantly by deleting the `canary-dev` key.
- **Tools to install:** AWS CLI v2 (`brew install awscli`), and Python packages `boto3`, `dbt-athena` (dbt-core + Athena adapter), `moto` (dev, for tests).
- **Setup is a script, not console clicks:** `infra/setup.sh` runs the AWS CLI commands to create the bucket, lifecycle rule, workgroup, Glue databases and budget, so the setup is repeatable and readable. It is run once by Victor with an admin profile; the runbook explains each command. (Terraform would also work; rejected for now as one more tool to learn and explain. Possible later upgrade.)

### 7.2 S3 layout (one bucket)
```
s3://<bucket>/
  raw/fdic/financials/repdte=YYYYMMDD/part.parquet   ← uploaded from data/raw/financials
  raw/fdic/failures/failures.parquet                 ← uploaded from data/raw/failures
  dbt/                                               ← tables dbt builds (Parquet)
  athena-results/                                    ← Athena query output, auto-deleted after 7 days
```
- **Bucket name:** `canary-warehouse-<random 6-char suffix>` (bucket names are global; the suffix avoids clashes and keeps personal details out). Stored in a git-ignored `.env` as `CANARY_BUCKET`, with a committed `.env.example`.
- Block all public access; default SSE-S3 encryption; versioning off (data is re-creatable).

### 7.3 Cost guardrails
- **AWS Budget:** $5/month cost budget, email alerts at 50% and 100% of actual and 100% of forecast. (The first two budgets are free.)
- **Athena workgroup `canary`:** enforced settings; results go to `athena-results/`; **per-query data-scanned limit of 1 GB** (the whole dataset is ~172 MB, so any query hitting the limit is a mistake).
- **S3 lifecycle rule:** delete objects under `athena-results/` after 7 days.
- Expected cost: S3 ~$0.01/month for <1 GB; Athena $5/TB scanned, so a full rebuild scanning the data a few times costs well under $0.01. Record the real bill at the end of the phase for the README.

### 7.4 Getting the raw data into S3 and Athena

**Date storage fix in Phase 1 code (the open question from Phase 1).** Dates are currently Parquet `timestamp[ns]`. Athena does not reliably read nanosecond timestamps. Change `schema.py` so `REPDTE`, `FAILDATE`, `RESDATE` are written as **Parquet `date32`** (a plain date, which is what they are) and `ingested_at` as **timestamp in milliseconds, UTC**. Then re-pull with `--force` (~7 minutes). Update unit tests, data checks and the data dictionary to match. Log as a decision note.

**Upload: `python -m canary.upload`.** Mirrors `data/raw/` to `s3://<bucket>/raw/fdic/` with boto3. Uploads a file only if it is new or its size or MD5 differs from the S3 copy (so a refresh after the latest-2-quarters re-pull uploads ~3 files, not 103). Never deletes in S3. Logs one line per file (uploaded/skipped). Unit-tested with `moto` (fake S3).

**Raw table DDL: `warehouse/ddl/*.sql` + `python -m canary.athena_ddl`.** Two hand-written SQL files:
- `fdic_financials.sql`: `CREATE EXTERNAL TABLE IF NOT EXISTS canary_raw.fdic_financials (...) PARTITIONED BY (repdte string) STORED AS PARQUET LOCATION 's3://<bucket>/raw/fdic/financials/'`. Per decision 0002's note, the `REPDTE` data column is **left out** of the column list; the partition column `repdte` (text `YYYYMMDD`) carries the date. Column types match the Parquet types (`bigint`, `double`, `string`, `date`, `timestamp`).
- `fdic_failures.sql`: an unpartitioned external table over `raw/fdic/failures/`.
- **Partitions use partition projection**, so Athena works out the quarter folders itself and nothing needs refreshing when a new quarter is uploaded. **Must be verified first**: Athena's `date` projection type steps from a start date by an interval, and stepping 3 months from March 31 may land on Dec 30 instead of Dec 31. If a test query does not return exactly the 102 expected quarters, fall back to `enum` projection, with the list of quarter values generated by the DDL runner from `canary.quarters`. Because `CREATE ... IF NOT EXISTS` won't change an existing table, the runner then also runs `ALTER TABLE canary_raw.fdic_financials SET TBLPROPERTIES ('projection.repdte.values'='...')` every time, so rerunning it after a new quarter picks that quarter up (builder's call, chosen over drop-and-recreate).
- The runner reads the SQL files, fills in the bucket name, and runs them through the Athena API (boto3). The SQL text generation is unit-tested; running it against Athena is covered by the dbt source tests.

### 7.5 dbt project (`warehouse/`)
- dbt-athena adapter, Athena engine v3, workgroup `canary`, `profiles.yml` committed inside `warehouse/` with no secrets: it reads the AWS profile and bucket from environment variables.
- Glue databases: `canary_raw` (external tables from §7.4), `canary_staging`, `canary_marts`.
- **Materialization:** staging = **views** (no storage, always current); marts = **tables** written as Parquet to `s3://<bucket>/dbt/`.
- Package: `dbt_utils` (for `unique_combination_of_columns` and `expression_is_true`).

**Sources** (`models/staging/_sources.yml`): `canary_raw.fdic_financials`, `canary_raw.fdic_failures`, with column descriptions.

**Staging** (rename and retype only, same row count as raw):
- `stg_fdic__financials`: one row per bank (`cert`) per quarter (`report_date`). FDIC codes renamed to readable snake_case (`ASSET` → `total_assets`, `DEPUNINS` → `uninsured_deposits`, `SCHA` → `htm_securities_amortized_cost`, …; the full mapping lives in the model and the data dictionary). `report_date` = `date_parse(repdte, '%Y%m%d')` as a date. Units unchanged: dollars stay in **$ thousands**, ratios stay in **percent**, YTD fields stay YTD; each column's description says so. Zeros stay zeros.
- `stg_fdic__failures`: one row per failure/assistance event, readable names, plus `is_failure` = (`restype` = 'FAILURE'). All rows kept.

**Marts:**
- `dim_failed_banks`: one row per `cert` for `FAILURE` events since 2001 (where `cert` is not null), with `failure_date`, name, cost, assets at failure. Test that `cert` is unique here; if a bank ever appears twice, the test must fail loudly rather than pick one silently.
- `fct_bank_quarters`: one row per bank per quarter, all staging financial columns plus `failure_date` (null if the bank never failed since 2001) and `quarters_until_failure` (whole quarters from `report_date` to the quarter of `failure_date`, null if never failed). This is the table Phase 3 reads. It does **not** define the training label; Phase 3 does that.

### 7.6 dbt data tests (every model has some)
- **Generic tests:** `not_null` on keys and dates; `unique_combination_of_columns(cert, report_date)` on `stg_fdic__financials` and `fct_bank_quarters`; `accepted_values` on `restype` (`FAILURE`, `ASSISTANCE`); `unique` on `dim_failed_banks.cert`; `relationships` from `dim_failed_banks.cert` to `stg_fdic__financials.cert` with **severity warn** (a failed bank might have no financials in 2001+; report it, don't block).
- **Singular tests** (`warehouse/tests/*.sql`), the Phase 1 data checks moved into the warehouse:
  - every quarter from 2001-03-31 to the latest has between 3,000 and 12,000 rows, and no quarter is missing;
  - SVB (cert 24735) 2022-12-31 `total_assets` = 209,026,000;
  - SVB 2023-03-10, Signature (57053) 2023-03-12 and First Republic (59017) 2023-05-01 are in `dim_failed_banks` with those dates;
  - row count of `stg_fdic__financials` equals row count of the raw source (no silent drops);
  - SVB 2022-12-31 `quarters_until_failure` = 1.
- The Phase 1 pytest data checks on local files stay in place (they guard the local files; dbt tests guard the warehouse).

### 7.7 How it's run (full refresh)
```
python -m canary.ingest financials      # Phase 1 (resume + refresh latest 2)
python -m canary.ingest failures
python -m canary.upload                  # changed files → S3
python -m canary.athena_ddl              # create raw tables if missing (safe to rerun)
cd warehouse && dbt build                # models + tests
```

### 7.8 Documentation outputs
- `decisions/`: 0005 FDIC API only (no bulk call reports); 0006 Athena + hand-written DDL + dbt (vs crawler, vs DuckDB); 0007 dates as Parquet `date32`; 0008 AWS setup and cost guardrails (IAM user, bucket layout, budget, workgroup limit).
- `data-dictionary/`: one file per dbt model (`stg_fdic__financials`, `stg_fdic__failures`, `dim_failed_banks`, `fct_bank_quarters`) plus updates to the two raw files for the date type change. dbt `.yml` descriptions say the same thing in shorter form. The existing dictionary test is extended to fail if a dbt model column is missing from `data-dictionary/`.
- `runbooks/aws-setup.md` (one-time setup, every command explained) and `runbooks/warehouse-refresh.md` (§7.7, plus what to do if each step fails).
- `README.md`: architecture diagram (text), how to run, cost so far. Keeps "Research tool, not financial advice."
- `CLAUDE.md`: data sources line updated per §2.
- `daily-log.md` at the end of each session.

## 8. Known limitations carried forward
- **Amended values only** (from Phase 1): unchanged by Phase 2. Stays in README limitations.
- **0 vs not reported:** staging keeps zeros as zeros; Phase 3 decides.
- **YTD income fields** are not converted to quarterly until Phase 3.

## 9. Left to the builder
- Exact snake_case names for each column (following the examples in §7.5, documented in the dictionary).
- The exact IAM policy statements, as long as they are scoped to the Canary bucket, workgroup and Glue databases.
- How `setup.sh` handles a resource that already exists (skip with a message is fine).
- Test layout under `tests/` and `warehouse/tests/`.
- Whether `quarters_until_failure` is computed with date arithmetic or a quarter index, as long as SVB 2022-12-31 gives 1.
