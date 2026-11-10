# 0008 — AWS setup: limited IAM user, CloudShell script, cost guardrails

**Date:** 2026-11-10
**Status:** Accepted

## Decision
- One-time setup is a bash script (`infra/setup.sh`) run by an admin in AWS CloudShell. See [[runbooks/aws-setup]].
- Day-to-day work uses an IAM user `canary-dev` with a least-privilege policy (`infra/iam-policy-canary-dev.json`), never root or admin keys.
- One bucket, `canary-warehouse-<6 random lowercase chars>`, region us-east-1. Layout: `raw/fdic/financials/repdte=YYYYMMDD/part.parquet`, `raw/fdic/failures/failures.parquet`, `dbt/` (dbt output tables), `athena-results/` (query output).
- Guardrails: $5/month budget with email alerts (50% and 100% actual, 100% forecast); Athena workgroup `canary` with a 1 GB per-query scan limit, enforced; `athena-results/` deleted after 7 days; public access blocked; encryption on.

## Why
- **IAM user, not root/admin keys.** If the key leaks, the damage is limited to this one bucket, three databases and one workgroup. Delete rights exist only on `athena-results/` and `dbt/`, so a bug cannot erase the raw data.
- **CloudShell.** It is already logged in as the admin, so powerful keys never touch my laptop.
- **Script that skips what exists.** Re-runnable and readable, so I can explain every line.
- **Random bucket suffix.** S3 names are global; random letters avoid clashes and guessing.
- **1 GB scan limit.** Athena bills by data scanned (about $5 per TB). The limit makes one bad query cost at most about half a cent.
- **7-day lifecycle.** Query result files are throwaway; expiring them stops slow storage creep.
- **Fixed region.** Cross-region traffic costs money and adds confusion.

## Alternatives
1. **Terraform/CloudFormation.** Better for teams and repeatability, but a new tool to learn for a one-bucket setup. Rejected for now; revisit if the infrastructure grows.
2. **Click everything in the console.** No record of what was done, hard to repeat. Rejected.
3. **Use admin keys locally.** Simplest, but a leaked key could run up unlimited cost. Rejected.

Related: [[decisions/0002-parquet-partitioned-by-quarter]]. Design: [[specs/2026-11-09-phase2-warehouse-design]].
