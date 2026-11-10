# Phase 2 Warehouse Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Put the Phase 1 FDIC Parquet files in S3, define them as Athena tables in hand-written SQL, and build tested dbt models (staging + `dim_failed_banks` + `fct_bank_quarters`) on top, with AWS cost guardrails.

**Architecture:** Phase 1 code is changed to write real dates. A small boto3 uploader mirrors `data/raw/` to S3. A DDL runner fills the bucket name into two SQL files and runs them on Athena. A dbt-athena project in `warehouse/` builds staging views and mart tables with data tests. One-time AWS setup is a CLI script Victor runs in CloudShell as his admin user. Day-to-day AWS calls use the limited `canary` profile.

**Tech Stack:** Python 3.12, pandas, pyarrow, boto3, moto (tests), dbt-core + dbt-athena, dbt_utils, AWS S3 / Athena (engine v3) / Glue Data Catalog / Budgets, AWS CLI v2.

**Spec:** `specs/2026-11-09-phase2-warehouse-design.md` (read it alongside this plan).

## Global Constraints

- Work on branch `phase2-warehouse`. Never commit `data/`, `.env`, or anything from `~/.aws/`. The repo is public.
- Region `us-east-1`. Athena workgroup `canary` (engine v3, enforced config, 1 GB per-query scan limit, results to `athena-results/`). Glue databases `canary_raw`, `canary_staging`, `canary_marts`.
- Bucket `canary-warehouse-<6 random lowercase chars>`, read from env var `CANARY_BUCKET` (in git-ignored `.env`; committed `.env.example` has a placeholder). AWS profile from `AWS_PROFILE`, default `canary`.
- S3 prefixes: `raw/fdic/financials/repdte=YYYYMMDD/part.parquet`, `raw/fdic/failures/failures.parquet`, `dbt/`, `athena-results/` (lifecycle: delete after 7 days).
- IAM user `canary-dev`: S3 read/write on the Canary bucket only; `s3:DeleteObject` only on `athena-results/*` and `dbt/*`; Athena on workgroup `canary` only; Glue on the three Canary databases (+ `catalog`) only; nothing else.
- **Never read `~/.aws/credentials`. Any AWS delete (S3 object, table, database, key) needs Victor's explicit "yes" first.** `dbt build` replaces its own mart tables under `dbt/` (a delete); until Victor says otherwise, ask him before each `dbt build` / `dbt run` that builds tables.
- Staging renames and retypes only: same row count as raw, units unchanged ($ thousands, percent, YTD), zeros stay zeros.
- New runtime deps: `boto3`. New optional group `warehouse`: `dbt-core>=1.9`, `dbt-athena>=1.9`. New dev deps: `moto[s3]>=5`, `pyyaml`. Unit tests must not touch the network or AWS.
- Every new table/column documented in `data-dictionary/`; decisions 0005–0008 in `decisions/`; `daily-log.md` updated at session end.

## Review Focus

1. **Rerun with nothing changed** → upload sends 0 files (size + MD5 match). Test: Task 3 `test_second_run_uploads_nothing`.
2. **Large file uploaded multipart** → S3 ETag is not an MD5, so comparing ETags would re-upload forever. Compare against an `md5` value stored in the object's metadata instead. Test: Task 3 `test_compares_md5_metadata_not_etag`.
3. **Stray files in `data/raw/`** (macOS `.DS_Store`, a leftover `part.parquet.tmp` from a crash) → never uploaded; only `*.parquet`. Test: Task 3 `test_skips_non_parquet_and_tmp`.
4. **`CANARY_BUCKET` unset or empty** → clear error and exit 1, never an upload to `s3://None/...` or a DDL with a blank location. Tests: Task 3 `test_missing_bucket_env_fails`, Task 4 `test_render_requires_bucket`.
5. **A new quarter is added** → the upload sends just that file and the raw Athena table sees it after the DDL runner is rerun. Tests: Task 3 `test_new_quarter_uploads_one_file`, Task 4 `test_enum_values_cover_all_quarters` (enum branch only).

---

### Task 1: Store dates as real dates (Phase 1 change)

**Files:**
- Modify: `src/canary/schema.py` (`_convert`, `to_typed_frame`)
- Modify: `tests/test_schema.py`, `tests/data_checks/test_raw_files.py`
- Modify: `data-dictionary/fdic_financials.md`, `data-dictionary/fdic_failures.md` (type column for `REPDTE`, `FAILDATE`, `RESDATE`, `ingested_at`)
- Create: `decisions/0007-dates-stored-as-date32.md`

**Interfaces:**
- Produces: Parquet files where `REPDTE`/`FAILDATE`/`RESDATE` are Arrow `date32[day]` and `ingested_at` is `timestamp[ms, tz=UTC]`. Tasks 4–6 declare these as Athena `date` and `timestamp`.

- [ ] **Step 1: Update tests to the new types.** In `tests/test_schema.py`: the date test asserts `df["REPDTE"].iloc[0] == date(2022, 12, 31)` and that the column holds `datetime.date` objects (pandas `object` dtype backed by Arrow `date32` on write); `test_mdy_date_parsed` expects `date(2023, 3, 10)`; `ingested_at` dtype is `datetime64[ms, UTC]`. Add `test_parquet_roundtrip_types(tmp_path)`: write a typed frame with `write_parquet_atomic`, read it with `pyarrow.parquet.read_schema`, assert `REPDTE` type `pa.date32()` and `ingested_at` type `pa.timestamp("ms", tz="UTC")`.
- [ ] **Step 2: Run** `pytest tests/test_schema.py -v`. Expected: the changed tests FAIL.
- [ ] **Step 3: Implement.** In `_convert`, date dtypes return `parsed.dt.date` (object column of `datetime.date`, nulls as `None`). In `to_typed_frame`, `ingested_at` uses dtype `datetime64[ms, UTC]`. If pandas writes the date column as something other than `date32`, pass an explicit Arrow schema in `write_parquet_atomic` instead; the roundtrip test is the judge.
- [ ] **Step 4: Run** `pytest -m "not data" -v`. Expected: all PASS.
- [ ] **Step 5: Fix the data checks** in `tests/data_checks/test_raw_files.py` so they compare against `datetime.date` values (drop the `pd.to_datetime`/`pd.Timestamp` wrappers where needed).
- [ ] **Step 6: Re-pull** `python -m canary.ingest financials --force && python -m canary.ingest failures` (~7 min, network, no AWS). Then `pytest -v`. Expected: all PASS including data checks, and `python -c "import pyarrow.parquet as pq; print(pq.read_schema('data/raw/financials/repdte=20221231/part.parquet').field('REPDTE').type)"` prints `date32[day]`.
- [ ] **Step 7: Docs.** Update the four type cells in the dictionaries. Write decision 0007 (why: they are dates, not times; Athena misreads nanosecond timestamps; alternative of keeping timestamps and casting in dbt rejected). Close the date question in decision 0002's Phase 2 notes with a link.
- [ ] **Step 8: Commit** `git commit -m "Store report and failure dates as Parquet date32"`.

### Task 2: AWS setup script, IAM policy, config, runbook

**Files:**
- Create: `infra/iam-policy-canary-dev.json`, `infra/setup.sh`, `.env.example`, `src/canary/config.py`, `runbooks/aws-setup.md`, `decisions/0008-aws-setup-and-cost-guardrails.md`
- Create: `tests/test_iam_policy.py`, `tests/test_config.py`
- Modify: `pyproject.toml` (deps listed in Global Constraints), `README.md` (setup pointer)

**Interfaces:**
- Produces: `canary.config.Settings` (frozen dataclass: `bucket: str`, `region: str = "us-east-1"`, `profile: str = "canary"`, `workgroup: str = "canary"`); `canary.config.load_settings(env: Mapping[str, str] | None = None) -> Settings` reading `CANARY_BUCKET`, `AWS_PROFILE`, also loading `.env` from the repo root if present (simple `KEY=VALUE` parser, no new dependency); raises `canary.config.ConfigError` if the bucket is missing/blank. `infra/iam-policy-canary-dev.json` uses the literal placeholder `BUCKET_NAME`, which `setup.sh` substitutes.

- [ ] **Step 1: Write failing tests.** `tests/test_config.py`: `test_load_settings_reads_env` (`{"CANARY_BUCKET": "canary-warehouse-abc123"}` → `bucket == "canary-warehouse-abc123"`, `profile == "canary"`); `test_missing_bucket_raises` and `test_blank_bucket_raises` (→ `ConfigError`). `tests/test_iam_policy.py` loads the JSON and asserts: every statement allowing `s3:DeleteObject` has resources only ending in `/athena-results/*` or `/dbt/*`; no statement has `"Action": "*"` or `"iam:*"`; every S3 resource contains `BUCKET_NAME`; Athena resources reference `workgroup/canary`; Glue resources reference only `catalog`, `database/canary_*`, `table/canary_*/*`.
- [ ] **Step 2: Run** `pytest tests/test_config.py tests/test_iam_policy.py -v`. Expected: FAIL.
- [ ] **Step 3: Implement** `config.py` and the policy JSON. The policy must also allow what dbt-athena needs inside those scopes (Glue get/create/update/delete table and partitions, `athena:StartQueryExecution`/`GetQueryExecution`/`GetQueryResults`/`StopQueryExecution`/`GetWorkGroup`, `s3:ListBucket`/`GetBucketLocation`/`GetObject`/`PutObject`/`AbortMultipartUpload`).
- [ ] **Step 4: Run** the tests. Expected: PASS.
- [ ] **Step 5: Write `infra/setup.sh`** (bash, `set -euo pipefail`, run in CloudShell as admin). Inputs as env vars: `CANARY_BUCKET`, `ALERT_EMAIL` (never committed). Steps, each skipping with a message if the resource exists: create bucket; block public access; SSE-S3 default encryption; lifecycle rule (expire `athena-results/` after 7 days); Glue databases `canary_raw`, `canary_staging`, `canary_marts`; Athena workgroup `canary` (engine v3, `EnforceWorkGroupConfiguration=true`, `BytesScannedCutoffPerQuery=1073741824`, output `s3://$CANARY_BUCKET/athena-results/`); $5 monthly cost budget with alerts at 50% and 100% actual and 100% forecast to `$ALERT_EMAIL`; IAM user `canary-dev` with the policy (placeholder substituted via `sed`). It does **not** create access keys. Verify with `bash -n infra/setup.sh` (and `shellcheck` if installed). Expected: no errors.
- [ ] **Step 6: Write `runbooks/aws-setup.md`**: (a) root MFA; (b) admin IAM user with console password + MFA, sign out of root; (c) open CloudShell as admin, upload/paste `setup.sh` and the policy JSON, run with `CANARY_BUCKET=... ALERT_EMAIL=... bash setup.sh`; (d) confirm the budget email subscription; (e) create one access key for `canary-dev` in the console; (f) on the Mac: `brew install awscli`, `aws configure --profile canary` (region `us-east-1`, output `json`), put `CANARY_BUCKET` in `.env`; (g) check: `aws sts get-caller-identity --profile canary` shows `user/canary-dev`. Explain every command in one plain line. Add how to revoke (delete the key).
- [ ] **Step 7: Decision 0008** (IAM user vs root/admin keys, CloudShell, bucket layout and naming, budget, scan limit, lifecycle; Terraform rejected for now). `.env.example` contains `CANARY_BUCKET=canary-warehouse-xxxxxx` and `AWS_PROFILE=canary`.
- [ ] **Step 8: Commit** `git commit -m "Add AWS setup script, least-privilege IAM policy, config"`.
- [ ] **Step 9: HUMAN CHECKPOINT. Stop and hand Victor `runbooks/aws-setup.md`.** Wait until `aws sts get-caller-identity --profile canary` returns `canary-dev` and `.env` has the bucket. Do not continue to live AWS steps before this.

### Task 3: Upload raw files to S3

**Files:**
- Create: `src/canary/upload.py`, `tests/test_upload.py`
- Modify: `runbooks/fdic-ingestion.md` (add the upload step)

**Interfaces:**
- Consumes: `load_settings()`, `ConfigError` (Task 2).
- Produces: `canary.upload.plan_keys(root: Path) -> list[tuple[Path, str]]` (local file → S3 key, sorted, only `*.parquet`, excludes `*.tmp`); `canary.upload.sync(root: Path, bucket: str, s3_client) -> UploadReport` where `UploadReport` is a dataclass `uploaded: list[str]`, `skipped: list[str]`; `canary.upload.main(argv: list[str] | None = None, s3_client=None) -> int` (CLI `python -m canary.upload [--root data/raw]`, returns 1 on `ConfigError` or boto `ClientError`).
- Key mapping: `data/raw/financials/repdte=20221231/part.parquet` → `raw/fdic/financials/repdte=20221231/part.parquet`; `data/raw/failures/failures.parquet` → `raw/fdic/failures/failures.parquet`.

- [ ] **Step 1: Write failing tests** using `moto.mock_aws` and a `tmp_path` raw tree with two quarters and a failures file:
  - `test_plan_keys_maps_paths` (exact keys above).
  - `test_skips_non_parquet_and_tmp` (`.DS_Store` and `part.parquet.tmp` present → not in plan).
  - `test_first_run_uploads_all` (3 uploaded, 0 skipped; each object has metadata `md5` = hex MD5 of the file).
  - `test_second_run_uploads_nothing` (0 uploaded, 3 skipped).
  - `test_changed_file_reuploaded` (rewrite one file → exactly that key uploaded).
  - `test_new_quarter_uploads_one_file`.
  - `test_compares_md5_metadata_not_etag` (pre-put an object with matching size but metadata `md5` different → uploaded; with matching `md5` but a non-MD5 ETag → skipped).
  - `test_never_deletes` (an extra object in S3 under `raw/` is still there after sync).
  - `test_missing_bucket_env_fails` (`main` with empty env → returns 1, no S3 calls).
- [ ] **Step 2: Run** `pytest tests/test_upload.py -v`. Expected: FAIL (module missing).
- [ ] **Step 3: Implement** `upload.py`. Skip test: S3 `head_object` exists AND `ContentLength` equals local size AND `Metadata["md5"]` equals local MD5. Upload with `upload_file(..., ExtraArgs={"Metadata": {"md5": ...}})`. Log one line per file (`uploaded`/`skipped`) and a summary. The real client is `boto3.Session(profile_name=settings.profile, region_name=settings.region).client("s3")`.
- [ ] **Step 4: Run** `pytest -m "not data" -v`. Expected: all PASS.
- [ ] **Step 5: Live run** (after the Task 2 checkpoint): `python -m canary.upload`. Expected: 103 uploaded (102 quarters + failures; the number follows the local quarter count). Run again. Expected: 0 uploaded. `aws s3 ls s3://$CANARY_BUCKET/raw/fdic/financials/ --profile canary | wc -l` equals the quarter count.
- [ ] **Step 6: Commit** `git commit -m "Add S3 uploader for raw FDIC files"`.

### Task 4: Raw Athena tables (DDL + runner)

**Files:**
- Create: `warehouse/ddl/fdic_financials.sql`, `warehouse/ddl/fdic_failures.sql`, `src/canary/athena_ddl.py`, `tests/test_athena_ddl.py`
- Create: `decisions/0006-athena-handwritten-ddl-and-dbt.md`

**Interfaces:**
- Consumes: `load_settings()` (Task 2); `quarter_ends()` (`canary.quarters`); `FINANCIAL_FIELDS`, `FAILURE_FIELDS` (`canary.schema`).
- Produces: tables `canary_raw.fdic_financials` (all `FINANCIAL_FIELDS` except `REPDTE`, plus `ingested_at timestamp`, partitioned by `repdte string`) and `canary_raw.fdic_failures` (all `FAILURE_FIELDS` + `ingested_at`). Column names lower-case in Athena. Functions: `render(sql: str, bucket: str) -> str` (replaces `{{bucket}}`; raises `ConfigError` on blank bucket); `statements(settings: Settings, latest: date) -> list[str]` (all SQL to run, in order); `run(statements: list[str], athena_client, workgroup: str) -> None` (start, poll until done, raise `AthenaError` with the reason on FAILED/CANCELLED); `main(argv=None, athena_client=None) -> int`.
- Type map from `Field.dtype`: `string`→`string`, `int64`/`Int64`→`bigint`, `float64`→`double`, `date_ymd`/`date_mdy`→`date`.

- [ ] **Step 1: Partition projection spike (live, throwaway).** In the Athena console or `aws athena start-query-execution --work-group canary --profile canary`, create a temporary table `canary_raw.tmp_projection_check` over `raw/fdic/financials/` with only `cert bigint`, partitioned by `repdte string`, with `projection.enabled=true`, `projection.repdte.type=date`, `projection.repdte.format=yyyyMMdd`, `projection.repdte.range=20010331,NOW`, `projection.repdte.interval=3`, `projection.repdte.interval.unit=MONTHS`, `storage.location.template=s3://<bucket>/raw/fdic/financials/repdte=${repdte}/`. Run `SELECT count(DISTINCT repdte) FROM canary_raw.tmp_projection_check`. **If it equals the local quarter count, use the `date` branch; otherwise use the `enum` branch.** Record the result in decision 0006. Ask Victor before dropping the temp table (it's a delete).
- [ ] **Step 2: Write failing tests:** `test_render_fills_bucket`; `test_render_requires_bucket`; `test_financials_ddl_columns_match_schema` (parse the column list from `fdic_financials.sql`: names equal lower-cased `FINANCIAL_FIELDS` minus `repdte` plus `ingested_at`, types per the map; `repdte` appears only in `PARTITIONED BY`); `test_failures_ddl_columns_match_schema`; `test_statements_are_idempotent` (every CREATE uses `IF NOT EXISTS`). Enum branch only: `test_enum_values_cover_all_quarters` (`statements(settings, date(2026, 6, 30))` includes an `ALTER TABLE canary_raw.fdic_financials SET TBLPROPERTIES ('projection.repdte.values'=...)` listing exactly `quarter_ends(2001-03-31, 2026-06-30)` as `YYYYMMDD`). `test_run_raises_on_failed_query` with a fake Athena client returning `FAILED` and a reason.
- [ ] **Step 3: Run** `pytest tests/test_athena_ddl.py -v`. Expected: FAIL.
- [ ] **Step 4: Implement** the two SQL files (`STORED AS PARQUET`, `LOCATION 's3://{{bucket}}/raw/fdic/.../'`, projection properties for the chosen branch) and `athena_ddl.py`. `latest` = newest `repdte=` folder under `data/raw/financials` (fall back to `--latest YYYYMMDD`).
- [ ] **Step 5: Run** `pytest -m "not data" -v`. Expected: all PASS.
- [ ] **Step 6: Live run** `python -m canary.athena_ddl`, then in Athena: `SELECT count(*) FROM canary_raw.fdic_financials` = local total (710,691 at spec time), `count(DISTINCT repdte)` = quarter count, `SELECT asset FROM canary_raw.fdic_financials WHERE cert = 24735 AND repdte = '20221231'` = 209026000, `SELECT count(*) FROM canary_raw.fdic_failures` = 4,117 (or current). Run `python -m canary.athena_ddl` a second time. Expected: succeeds, no changes.
- [ ] **Step 7: Decision 0006** (hand-written DDL vs Glue crawler vs DuckDB; projection branch chosen and the spike's evidence; the `REPDTE`/`repdte` clash handled by leaving `REPDTE` out). Commit `git commit -m "Add Athena raw tables and DDL runner"`.

### Task 5: dbt project and staging models

**Files:**
- Create: `warehouse/dbt_project.yml`, `warehouse/profiles.yml`, `warehouse/packages.yml`, `warehouse/macros/generate_schema_name.sql`, `warehouse/models/staging/_sources.yml`, `warehouse/models/staging/_staging.yml`, `warehouse/models/staging/stg_fdic__financials.sql`, `warehouse/models/staging/stg_fdic__failures.sql`, `warehouse/tests/assert_stg_financials_row_count_matches_raw.sql`
- Modify: `.gitignore` (`warehouse/target/`, `warehouse/dbt_packages/`, `warehouse/logs/` if the existing dbt lines don't cover them)

**Interfaces:**
- Consumes: `canary_raw.fdic_financials`, `canary_raw.fdic_failures` (Task 4).
- Produces: views `canary_staging.stg_fdic__financials` (key `cert bigint`, `report_date date`, readable snake_case for every other financial field, `ingested_at`) and `canary_staging.stg_fdic__failures` (readable names, `failure_date date`, `resolution_date date`, `is_failure boolean`). Task 6 relies on `cert`, `report_date`, `failure_date`, `is_failure`, `failure_year`, `resolution_type` (`restype`), plus `institution_name`, `estimated_loss` (`cost`), `total_assets_at_failure` (`qbfasset`). Other names are the builder's call per spec §9, used identically in yml and dictionary.

- [ ] **Step 1: Scaffold.** `profiles.yml` (profile `canary`, `type: athena`, `region_name: us-east-1`, `database: awsdatacatalog`, `schema: canary_staging`, `work_group: canary`, `s3_staging_dir` = `s3://{{ env_var('CANARY_BUCKET') }}/athena-results/`, `s3_data_dir` = `s3://{{ env_var('CANARY_BUCKET') }}/dbt/`, `s3_data_naming: schema_table`, `aws_profile_name: "{{ env_var('AWS_PROFILE', 'canary') }}"`, `threads: 4`). `dbt_project.yml`: staging `+materialized: view`, `+schema: canary_staging`; marts `+materialized: table`, `+format: parquet`, `+schema: canary_marts`. `generate_schema_name` macro returns the custom schema unchanged (otherwise dbt would make `canary_staging_canary_marts`). `packages.yml`: `dbt-labs/dbt_utils` pinned to a 1.x version. Run with `--profiles-dir .` from `warehouse/`, with `.env` exported.
- [ ] **Step 2: Write the models' tests first in `_staging.yml`:** `stg_fdic__financials`: `dbt_utils.unique_combination_of_columns` on (`cert`, `report_date`); `not_null` on `cert`, `report_date`. `stg_fdic__failures`: `accepted_values` on `resolution_type` (`FAILURE`, `ASSISTANCE`); `not_null` on `failure_date`, `is_failure`. Singular test `assert_stg_financials_row_count_matches_raw.sql` returns a row when `count(*)` of the model differs from the source. Every column gets a description including units.
- [ ] **Step 3: Verify offline** `dbt deps && dbt parse` (with `CANARY_BUCKET` set). Expected: parse succeeds, errors only for missing model SQL until Step 4.
- [ ] **Step 4: Write the two staging SQL files.** Financials: select from the source, `cast(date_parse(repdte, '%Y%m%d') as date) as report_date`, rename every column, no filters, no arithmetic. Failures: rename, `restype = 'FAILURE' as is_failure`.
- [ ] **Step 5: Live build** (views only, no deletes): `dbt build --select staging`. Expected: 2 views created, all tests PASS.
- [ ] **Step 6: Commit** `git commit -m "Add dbt project and staging models with tests"`.

### Task 6: Marts and warehouse data tests

**Files:**
- Create: `warehouse/models/marts/_marts.yml`, `warehouse/models/marts/dim_failed_banks.sql`, `warehouse/models/marts/fct_bank_quarters.sql`
- Create singular tests in `warehouse/tests/`: `assert_no_missing_quarters.sql`, `assert_rows_per_quarter_in_range.sql`, `assert_svb_2022q4_assets.sql`, `assert_2023_failures_present.sql`, `assert_svb_2022q4_one_quarter_to_failure.sql`

**Interfaces:**
- Consumes: staging columns from Task 5.
- Produces: `canary_marts.dim_failed_banks` (one row per `cert`, `is_failure` and `failure_year >= 2001` and `cert is not null`: `cert`, `institution_name`, `failure_date`, `estimated_loss`, `total_assets_at_failure`) and `canary_marts.fct_bank_quarters` (every `stg_fdic__financials` column + `failure_date` + `quarters_until_failure int`). Phase 3 reads `fct_bank_quarters`.

- [ ] **Step 1: Write the tests first.** `_marts.yml`: `dim_failed_banks.cert` `unique` + `not_null`; `relationships` from `dim_failed_banks.cert` to `ref('stg_fdic__financials').cert` with `config: {severity: warn}`; `fct_bank_quarters`: `unique_combination_of_columns` (`cert`, `report_date`), `not_null` on keys, `dbt_utils.expression_is_true` that `quarters_until_failure >= 0` where not null. Singular tests (each returns failing rows): every quarter end from 2001-03-31 to `max(report_date)` is present (generate the expected list with `sequence(date '2001-03-31', max_date, interval '3' month)` and correct month-end with `last_day_of_month`); every quarter has 3,000–12,000 rows; SVB (24735) 2022-12-31 `total_assets` = 209026000; certs 24735 / 57053 / 59017 have failure dates 2023-03-10 / 2023-03-12 / 2023-05-01 in `dim_failed_banks`; SVB 2022-12-31 `quarters_until_failure` = 1.
- [ ] **Step 2: Write `dim_failed_banks.sql`** (filter and select only; no dedup logic, so the `unique` test fails loudly if a bank appears twice).
- [ ] **Step 3: Write `fct_bank_quarters.sql`:** left join financials to `dim_failed_banks` on `cert`; `quarters_until_failure` = `(year(failure_date)*4 + quarter(failure_date)) - (year(report_date)*4 + quarter(report_date))`, null when `failure_date` is null.
- [ ] **Step 4: Ask Victor** before the first table build (it creates tables and later rebuilds replace them). Then `dbt build`. Expected: all models built; all tests PASS; the relationships test may WARN (1 failed bank without financials, per the builder check), which is expected.
- [ ] **Step 5: Spot-check in Athena:** `SELECT count(*) FROM canary_marts.fct_bank_quarters` equals the staging count; `SELECT count(*) FROM canary_marts.dim_failed_banks` = 574 (or current FAILURE-since-2001 count).
- [ ] **Step 6: Commit** `git commit -m "Add dim_failed_banks and fct_bank_quarters marts with data tests"`.

### Task 7: Documentation, dictionary check, wrap-up

**Files:**
- Create: `data-dictionary/stg_fdic__financials.md`, `data-dictionary/stg_fdic__failures.md`, `data-dictionary/dim_failed_banks.md`, `data-dictionary/fct_bank_quarters.md`, `decisions/0005-fdic-api-only-no-bulk-call-reports.md`, `runbooks/warehouse-refresh.md`
- Modify: `tests/test_data_dictionary.py`, `README.md`, `CLAUDE.md` (data sources line), `daily-log.md`

**Interfaces:**
- Consumes: model column lists from `warehouse/models/**/*.yml`.

- [ ] **Step 1: Write the failing test** `test_every_dbt_column_documented` in `tests/test_data_dictionary.py`: for each model in the yml files, `data-dictionary/<model>.md` exists and contains `` | `<column>` | `` for every column.
- [ ] **Step 2: Run** it. Expected: FAIL (files missing).
- [ ] **Step 3: Write the four dictionary files** in the existing format (grain, primary key, source, row count, "read this first" caveats, column table with raw field, meaning, units). Row counts from Task 6 Step 5.
- [ ] **Step 4: Run** `pytest -m "not data" -v`. Expected: all PASS.
- [ ] **Step 5: Write** decision 0005 (spec §2 reasoning; call reports as a possible later add-on), `runbooks/warehouse-refresh.md` (spec §7.7 commands, what each does, what to do if each fails, the confirm-before-delete rule), README (text architecture diagram, how to run, test counts, AWS cost so far from the Billing console, limitations incl. amended values; keeps "Research tool, not financial advice."), `CLAUDE.md` data sources line ("FFIEC bulk call reports: deferred, see decision 0005"), `daily-log.md`.
- [ ] **Step 6: Final verification:** `pytest -v` all pass; `cd warehouse && dbt build` all pass (ask Victor first, per the rule); `git status` shows no `data/`, `.env`, or credentials. Commit `git commit -m "Phase 2 docs: data dictionary, decisions, runbooks, README"`.
