# Tools in Canary

This page explains each tool in Canary in plain English: what it is, why this project uses it, and what it does today. The goal is to read it once and then be able to explain any of these tools to someone non-technical.

This is the pipeline as built so far:

```
FDIC BankFind API  ->  local Parquet files  ->  S3  ->  Athena raw tables  ->  dbt  ->  marts
   (public data)        (data/raw/)          (storage)   (SQL over files)    (clean + test)  (fct_bank_quarters,
                                                                                               dim_failed_banks,
                                                                                               fct_bank_features)
                                                  marts -> export (Athena UNLOAD) -> local Parquet -> XGBoost -> metrics
```

The first five tools below (S3, Athena, Glue, dbt, XGBoost) are running today. The other three (the Claude API, Streamlit, GitHub Actions) are planned for later phases. Their sections say so plainly.

---

## AWS S3

**What it is.** S3 is Amazon's file storage in the cloud. You put files in a "bucket" and organize them in folder-like paths. It's very cheap, it doesn't run out of space, and other AWS services can read straight from it.

**Why it's here.** Phase 1 saved the FDIC data as files on a laptop. To query that data with SQL in the cloud, the files need to live somewhere AWS can reach, and S3 is that place. It costs almost nothing at this size: about 172 MB of data costs well under a cent a month to store. See [decision 0008](decisions/0008-aws-setup-and-cost-guardrails.md).

**What it does in Canary now.**
- There is one bucket, `canary-warehouse-<random letters>`, with three areas:
  - **`raw/fdic/`** holds the 103 files copied from `data/raw/`: one Parquet file per quarter for 102 quarters, plus the failed-bank list.
  - **`dbt/`** holds the final tables dbt builds.
  - **`athena-results/`** holds query output, deleted automatically after 7 days.
- `python -m canary.upload` copies new or changed files up and skips files that are already there unchanged. It never deletes anything.
- The bucket is private and encrypted.
- Canary's day-to-day login (`canary-dev`) can delete only in `dbt/` and `athena-results/`, so a bug can't wipe the raw data.

## AWS Athena

**What it is.** Athena lets you run SQL queries directly on files sitting in S3, without loading them into a database first. There's no server to run, and you pay only for the data each query reads, about $5 per terabyte.

**Why it's here.** It turns the S3 files into tables I can query with ordinary SQL, which is the core skill in data engineering and analytics roles. It costs nothing when idle, which keeps the project under $5 a month. A traditional database would need a server running all the time.

**What it does in Canary now.**
- `python -m canary.athena_ddl` creates two raw tables over the S3 files: `canary_raw.fdic_financials` (710,691 bank-quarters) and `canary_raw.fdic_failures` (4,117 rows).
- The table definitions are SQL files written by hand in `warehouse/ddl/`, so every column and type is visible and tested. See [decision 0006](decisions/0006-athena-handwritten-ddl-and-dbt.md).
- The financials table has the full list of quarters written into it. Athena's automatic quarter detection was tested and found only 1 of the 102 quarters, so the list is explicit instead.
- Queries run in a workgroup called `canary` that blocks any single query from reading more than 1 GB. That caps the cost of a mistaken query at about half a cent.

## AWS Glue (Data Catalog)

**What it is.** Glue has several parts. Canary uses only the **Data Catalog**: AWS's shared list of databases and tables. For each table it records the column names, the types, and where the files are in S3. It's the "table of contents" Athena reads to know what a table is.

**Why it's here.** Athena needs a catalog to know what `canary_raw.fdic_financials` means, and Glue is the catalog Athena uses. Canary doesn't use Glue's other features. In particular it skips the crawler, a tool that scans files and guesses the tables. Decision 0006 rejected the crawler because it guesses types, costs money each time it runs, and is hard to explain.

**What it does in Canary now.**
- Glue holds three databases:
  - **`canary_raw`:** the raw tables over the S3 files.
  - **`canary_staging`:** cleaned-up views.
  - **`canary_marts`:** final tables.
- Every table Athena or dbt creates is recorded here automatically, and nothing is set up in Glue by hand.

## dbt

**What it is.** dbt (data build tool) is a way to write data transformations as plain SQL files. Each file defines one table or view, and dbt works out the order to build them in. dbt also runs **data tests**: SQL checks that fail loudly if the data looks wrong, such as duplicate rows, missing quarters or a known value that doesn't match. It's a standard tool on analytics and data engineering teams.

**Why it's here.** Raw FDIC column names like `lnlsgr` and `depunins` are hard to read. dbt turns them into clean, readable tables in version-controlled SQL that anyone can review. The tests prove the data is right instead of assuming it. The `dbt-athena` adapter lets dbt run directly on Athena, so there's one SQL dialect and no second database. See decision 0006.

**What it does in Canary now.** The project lives in `warehouse/`.
- **Staging views** (`stg_fdic__financials`, `stg_fdic__failures`) rename columns to plain English and turn date text into real dates. They change nothing else: the same rows, units and zeros as the raw data.
- **Mart tables:**
  - **`dim_failed_banks`:** the 574 banks that failed since 2001.
  - **`fct_bank_quarters`:** one row per bank per quarter, 710,691 rows, with `quarters_until_failure`, the label Phase 3 learns to predict.
- **29 data tests** (24 pass, 5 known warnings, 0 errors) check, for example:
  - no quarter is missing from 2001 to 2026
  - each bank appears once per quarter
  - SVB's 2022 assets equal $209B
  - SVB, Signature and First Republic have the correct 2023 failure dates
- A Python test also checks that every column is documented in `data-dictionary/`.
- Because building tables replaces old ones, `dbt build` runs only with the owner's approval.

## XGBoost

**What it is.** XGBoost is a machine-learning library that builds many small decision trees. Each tree asks a few yes/no questions, like "Is capital below X?" or "Are bad loans above Y?". Each new tree corrects the mistakes of the trees before it. Together they produce a risk score.

**Why it's here.** Canary's data is a table of numbers per bank per quarter, and that's exactly what XGBoost is strongest at. It picks up threshold effects such as "risky only once capital drops below a level". It copes with missing values, and it can show which signals drove a score, which matters when explaining a risk score. It's widely used in credit-risk modeling at banks.

**What it does in Canary now.**
- A tested dbt table, `fct_bank_features`, holds 31 CAMELS-style ratios per bank per quarter (capital, asset quality, earnings, liquidity, interest-rate sensitivity such as unrealized bond losses compared with equity, and size and growth).
- XGBoost trains on report dates 2001-2014 to predict "fails within the next 4 quarters". 2015 is dropped so no 2016 outcome leaks in. Settings are picked on a 2012-2014 validation block, never on the test years.
- It scores 2016-2024 once. Each quarter the riskiest 2% of banks are flagged, and the result is compared with a simple Texas-ratio baseline.
- Result: AUC 0.902 against 0.774 for the baseline, but it did not flag SVB, Signature or First Republic. See the README results section.

## Claude API *(planned: Phase 5)*

**What it is.** The Claude API lets a program send text to Anthropic's Claude model and get a written answer back. It's the same AI as the Claude chat app, but called from code.

**Why it's here.** A risk score alone doesn't say *why* a bank looks risky. The Claude API powers Canary's risk-analyst agent, which turns a bank's numbers into a short plain-English memo. A project rule says every memo must cite the bank, the quarter and the exact numbers it relies on, so it can be checked rather than trusted blindly. (This is separate from Claude Code, the coding assistant used to *build* Canary. The Claude API is part of the *product*.)

**What it will do in Canary.** In Phase 5, the agent reads a bank's features and score and writes one cited risk note per bank into the Obsidian vault. In the vault's graph view, those notes show the banking system at a glance. Nothing calls the Claude API yet.

## Streamlit *(planned: Phase 6)*

**What it is.** Streamlit turns a Python script into an interactive web page, with charts, tables, dropdowns and search, without writing any web front-end code (no HTML or JavaScript).

**Why it's here.** Canary's work is all in Python and SQL. Streamlit gives it a dashboard someone can click through in a demo or an interview without learning web development. The time goes into the data and the model instead.

**What it will do in Canary.** In Phase 6, a dashboard will show the quarterly watchlist and each bank's risk over time. It will also include the SVB, Signature and First Republic case studies, reading from the warehouse tables and the model's scores. It isn't built yet.

## GitHub Actions *(planned)*

**What it is.** GitHub Actions runs automated jobs on GitHub's servers. They can run whenever code is pushed or a pull request opens, or on a schedule. A common use is running a project's tests automatically on every change.

**Why it's here.** Canary is a public repo, and passing tests that run on every pull request are proof anyone can see that the code works. Later, a scheduled job could pull each new FDIC quarter automatically, making Canary a live system instead of a snapshot.

**What it does in Canary.** Nothing yet: the repo has no workflows. Today the tests run locally: 100 Python tests, plus the dbt data tests. The plan is first to run the Python tests on every pull request (no AWS access needed, since they use fakes), then add scheduled quarterly re-runs after v1 launches.
