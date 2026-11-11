# Glossary

The acronyms and terms used across Canary, in plain English, each tied to where it shows up in this repo: a column, a feature, a file or a decision. Field names in `CAPS` are raw FDIC columns ([data-dictionary/fdic_financials.md](../data-dictionary/fdic_financials.md)). Names in `snake_case` are Canary's own columns (staging, marts or features). For the tools themselves, see [STACK.md](STACK.md).

---

## Banking and regulatory terms

### CAMELS
Bank supervisors' rating system. Examiners score a bank 1 (best) to 5 (worst) on six areas:
- **C**apital adequacy
- **A**sset quality
- **M**anagement
- **E**arnings
- **L**iquidity
- **S**ensitivity to market risk, mainly interest rates

Real CAMELS ratings are confidential, so Canary builds a **"CAMELS-style"** version from public data. [Decision 0003](../decisions/0003-curated-45-financial-fields.md) picked the 45 FDIC fields with these areas in mind. `fct_bank_features` turns them into 31 ratios grouped by area ([decision 0009](../decisions/0009-features-and-zero-handling.md)). **Management** is left out: its quality can't be read from a balance sheet.

### FDIC
**Federal Deposit Insurance Corporation.** The US agency that insures bank deposits and takes over banks that fail. The insurance limit is $250,000 per depositor per bank: it was raised from $100,000 in 2008 and made permanent in 2010. Canary's two data sources both come from the FDIC:
- the BankFind API for quarterly financials (`data/raw/financials/`)
- the failed bank list for the labels (`data/raw/failures/`)

`cert`, the FDIC certificate number, is the bank ID used everywhere in Canary (e.g. SVB is 24735). Deposits above the limit are "uninsured" (see `DEPUNINS` under Tier 1 capital below).

### FFIEC
**Federal Financial Institutions Examination Council.** The group of US bank regulators that sets the quarterly **Call Report** every bank files: its balance sheet, income and capital. The FDIC numbers Canary uses come from those Call Reports. The FFIEC also publishes the raw reports in bulk, but Canary uses only the FDIC API for now ([decision 0005](../decisions/0005-fdic-api-only-no-bulk-call-reports.md)).

### ROA
**Return on assets.** Yearly profit as a percent of total assets: how much the bank earns per dollar it holds. About 1% is typical.
- **In Canary:** the FDIC field `ROA`, already annualized, which becomes the staging column `return_on_assets` and the feature `return_on_assets`.
- **Units:** percent. It is not converted to a fraction.

### ROE
**Return on equity.** Yearly profit as a percent of the owners' equity.
- **In Canary:** the FDIC field `ROE`, which becomes `return_on_equity`, in percent and annualized.
- **What the model did with it:** a healthy ROE helped push SVB's 2022 scores toward "safe" (README case study).

### NIM
**Net interest margin.** Interest earned on loans and bonds minus interest paid on deposits and borrowings, as a percent of the assets that earn interest. It's the core of how a bank makes money. When deposit costs rise faster than loan yields, it gets squeezed.
- **In Canary:** the FDIC field `NIMY` (the "Y" means annualized, year-to-date), which becomes `net_interest_margin`, in percent.

### Tier 1 capital
A bank's highest-quality loss cushion: mainly common stock and retained earnings, minus items like goodwill. Regulators judge it in two ways:
- **Leverage ratio** = Tier 1 ÷ average total assets. FDIC field `RBC1AAJ` ("LEVERAGE RATIO-PCA"), which becomes `leverage_ratio`.
- **Tier 1 risk-based ratio** = Tier 1 ÷ risk-weighted assets, where riskier assets count for more. FDIC field `IDT1RWAJR`, which becomes `tier1_risk_based_ratio`.

The broader **total risk-based ratio** (`RBCRWAJ` → `total_risk_based_ratio`) adds lower-quality capital. All three are in percent.

Since 2020, some small banks may use the simpler community bank leverage ratio and stop reporting risk-based ratios. That's why Canary treats a 0 in the risk-based ratios as "not reported" ([decision 0009](../decisions/0009-features-and-zero-handling.md)).

### PCA
**Prompt Corrective Action.** The US law that ties a bank's capital ratios to required regulator action. Banks are sorted into categories from "well capitalized" down to "critically undercapitalized", and regulators must step in harder as capital falls. In Canary, "PCA" appears in FDIC field titles such as `RBC1AAJ` = "LEVERAGE RATIO-PCA" and `RBCRWAJ` = "TOTAL RBC RATIO-PCA". That marks these as the ratios the PCA categories are based on.

### HTM
**Held-to-maturity securities.** Bonds a bank says it will keep until they're repaid. They're carried at **amortized cost** (roughly the purchase price), so when interest rates rise and their market value falls, that loss **doesn't reduce reported equity** unless the bonds are sold. This was SVB's hidden problem.
- **In Canary:** the cost is `SCHA` and the fair (market) value is `SCHF`. The feature `htm_unrealized_loss_to_equity` = (`SCHA` − `SCHF`) ÷ equity.
  - For SVB at 2022-12-31 it was **0.98**: the hidden loss was about equal to all of its equity. A dbt test pins this value.
  - If cost is above 0 but fair value is 0 or missing, the feature is left blank, since that means "not reported" ([decision 0009](../decisions/0009-features-and-zero-handling.md)).
- **The AFS counterpart:** **AFS (available-for-sale)** bonds are carried at market value. Their cost is `SCAA` and their fair value is `SCAF`, which gives `afs_unrealized_loss_to_equity`. AFS losses do flow into GAAP equity.
- **What the model did with it:** see the README case study for how both features moved SVB's and Signature's scores.

---

## Technical terms

### AUC
**Area under the ROC curve.** One number for how well a model ranks risky cases above safe ones. If you pick one bank-quarter that went on to fail within 4 quarters and one that didn't, AUC is the chance the model scored the failing one higher. A value of 0.5 is a coin flip and 1.0 is perfect.
- **Canary's result:** on 2016–2024 the model scored **0.902**, against **0.774** for the Texas-ratio baseline ([decision 0011](../decisions/0011-watchlist-flag-and-metrics.md); `metrics.json`).
- **What it doesn't tell you:** AUC measures ranking only. Whether a particular bank was flagged is decided by the 2% watchlist rule, not by AUC.

### XGBoost
**eXtreme Gradient Boosting.** A machine-learning library that builds many small decision trees, each one correcting the mistakes of the trees before it. Canary's model is 79 trees, each up to 5 levels deep, trained on 2001–2014 report dates ([decision 0010](../decisions/0010-label-and-time-split.md)). The code is in `src/canary/model/train.py`, and the run's settings are saved to `data/model/run_config.json`. More in [STACK.md](STACK.md).

### DDL
**Data Definition Language.** The part of SQL that defines structure (`CREATE TABLE`, `ALTER TABLE`) rather than reading data.
- **Where it lives:** Canary's raw Athena tables are defined by hand-written DDL in `warehouse/ddl/fdic_financials.sql` and `warehouse/ddl/fdic_failures.sql`.
- **How it runs:** `python -m canary.athena_ddl` runs them ([decision 0006](../decisions/0006-athena-handwritten-ddl-and-dbt.md)).
- **Why it's safe to rerun:** every statement is `CREATE ... IF NOT EXISTS` or `ALTER ... SET TBLPROPERTIES`, so rerunning never drops anything.

### dbt
**data build tool.** It's officially written in lowercase as just "dbt". You write each table as a SQL `SELECT` in its own file, and dbt builds them in the right order and runs data tests on them.
- **The project:** Canary's dbt project is `warehouse/`, and it builds four kinds of models:
  - staging views (`stg_fdic__financials`, `stg_fdic__failures`)
  - mart tables (`fct_bank_quarters`, `dim_failed_banks`)
  - the features table (`fct_bank_features`)
- **The tests:** 29 data tests, including the SVB check values.
- **Approval rule:** building tables needs the owner's yes, because rebuilds replace files under `dbt/`.

### IAM
**Identity and Access Management.** AWS's system of users and permissions. Canary's everyday user, `canary-dev`, can only touch the Canary bucket, its Athena workgroup and its three Glue databases. It can delete only under `dbt/` and `athena-results/`. The permissions are in [`infra/iam-policy-canary-dev.json`](../infra/iam-policy-canary-dev.json), and the reasons are in [decision 0008](../decisions/0008-aws-setup-and-cost-guardrails.md).

### MFA
**Multi-factor authentication.** Logging in needs a second proof, such as a code from an authenticator app, as well as the password, so a stolen password alone isn't enough. Canary's AWS root account and `admin` user both have MFA, set up in steps (a) and (b) of [runbooks/aws-setup.md](../runbooks/aws-setup.md).

### S3
**Simple Storage Service.** AWS's cloud file storage. Canary keeps everything in one private, encrypted bucket:
- `raw/fdic/`: one Parquet file per quarter, plus the failed-bank list
- `dbt/`: dbt's output tables
- `athena-results/`: query results, deleted automatically after 7 days

See [STACK.md](STACK.md) and [decision 0008](../decisions/0008-aws-setup-and-cost-guardrails.md).
