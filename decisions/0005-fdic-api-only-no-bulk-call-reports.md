# 0005 — Use the FDIC API only; defer bulk FFIEC call reports

**Date:** 2026-11-09
**Status:** Accepted

## Decision
Phase 2 (and the first model in Phase 3) uses the FDIC BankFind API data only. The bulk FFIEC call report files are deferred. If Phase 3 or the SVB replay needs a field we do not have, we add it to `FINANCIAL_FIELDS` and re-pull from the FDIC API. A small call-report pull for specific missing fields stays a possible later add-on.

## Why
- **The FDIC API is built from the call reports.** It exposes about 2,400 fields; Phase 1 pulls 45 of them.
- **The signals that matter most for SVB are already in Phase 1.** `DEPUNINS` (uninsured deposits), and `SCHA` minus `SCHF` and `SCAA` minus `SCAF` (unrealized losses on held-to-maturity and available-for-sale securities).
- **The bulk files are much more work.** About 40 tab-separated schedule files per quarter, with codes that change over 24 years, downloaded by hand or through a registered web service.
- **They would probably not fix the "amended values only" limitation.** The bulk files appear to hold corrected values too, so an SVB replay would still not see exactly what an analyst saw in early 2023. (This is "appears", not tested.)

## Alternatives
1. **Pull the bulk FFIEC call reports now.** Rejected: large effort, no clear gain for the first model, and it does not remove the main limitation.
2. **Never use call reports.** Not chosen: kept open as a later add-on for specific missing fields.

Related: [[decisions/0003-curated-45-financial-fields]], [[decisions/0004-store-raw-values-unchanged]], [[specs/2026-11-09-phase2-warehouse-design]].
