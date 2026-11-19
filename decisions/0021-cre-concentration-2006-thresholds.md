# 0021 — Real-estate concentration: the 2006 regulator thresholds, fixed, code-written

**Date:** 2026-11-19
**Status:** Accepted (design approved by the owner; built in Phase 5d)

## Decision
Every bank note gets a section, **"Real-estate concentration (2006 regulator thresholds)"**. It checks whether the bank crossed the two lines US bank regulators have used since 2006 to flag commercial real estate (CRE) concentration for closer supervisory review. The test is **fixed by published sources**, not designed by Canary. The section is **written by code** (no AI text, no AI request, no facts for Claude) and has **no measured result**: no recall, catches, AUC, lead time or false-alarm rate for crossing a line appears in the notes, the README, RESULTS or anywhere else.

Code: `src/canary/analyst/concentration.py` (test and section), `src/canary/ingest_concentration.py` (the data pull). Format: [[data-dictionary/bank_notes]], [[data-dictionary/fdic_concentration]]. Design: [[specs/2026-11-19-phase5d-concentration-design]].

## Why it exists
Everything else in a memo is about funding or the overall score. SVB failed on funding and bond losses, not loan concentration. Heavy lending tied to commercial real estate is a different and more common way banks fail, so the section says so in its own text and asks one plain question: did the bank cross the regulators' lines at the as-of quarter?

## Sources, and what each supports
- **OCC Bulletin 2006-46 and 71 FR 74580** (Federal Register notice of the interagency guidance, December 2006). Supports the two lines: construction and land loans at 100% or more of total risk-based capital; total CRE at 300% or more of total risk-based capital **and** CRE growth of 50% or more over the prior 36 months. They are screens for further supervisory review, **not lending limits**.
- **Federal Reserve, "An Analysis of the Impact of the Commercial Real Estate Concentration Guidance" (2013), appendix.** Supports the Call Report items: F158 + F159 (construction and land development), + 1460 (multifamily), + F161 (non-owner-occupied nonfarm nonresidential), + 2746 (loans to finance CRE not secured by real estate); denominator RCFD3792 (total risk-based capital); growth measured against 12 quarters earlier.
- **FDIC FIL-31-2020 and Federal Reserve SR 20-8.** Support the denominator switch: from March 31, 2020, credit concentration ratios use Tier 1 capital plus the allowance for loan and lease losses (for CECL adopters, the allowance attributable to loans and leases). FIL-31-2020 applies to all FDIC-supervised institutions eligible to elect the community bank leverage ratio (CBLR); SR 20-8 applies to Federal Reserve-supervised institutions. **Neither restates the 2006 thresholds.**

## The fixed test
Set before any bank's result was looked at. **Do not change any of these after seeing results.** Changing one needs a new decision record that says why and states plainly that it was changed after seeing results.

- **Raw fields** (separate table, below): `CERT, REPDTE, LNRECONS, LNREMULT, LNRENROT, LNCOMRE, RBC, RBCT1J, LNATRES`.
- **Construction** = `LNRECONS`. **Total CRE** = `LNRECONS + LNREMULT + LNRENROT + LNCOMRE`. A null component makes that numerator missing; a reported 0 counts as 0.
- **Capital (denominator), by the as-of quarter:** before 2020-03-31, `RBC` (total risk-based capital, as the 2006 guidance specifies). On or after 2020-03-31, `RBCT1J + LNATRES` (null if either is null), for every bank. The section labels which measure it used and, from 2020 on, says the 2006 thresholds were not restated for it. Missing capital (reason: "the bank reported no capital figure for this quarter") or capital of zero or below (reason: "the bank's capital was zero or negative this quarter") means neither ratio can be computed; the two cases are worded differently so a negative-capital (insolvent) bank is not described as having no data.
- **Line 1:** construction / capital x 100 **>= 100**.
- **Line 2:** total CRE / capital x 100 **>= 300** **and** growth **>= 50**.
- **Growth** = (total CRE at the as-of quarter / total CRE at the same calendar quarter 12 quarters earlier - 1) x 100. If the earlier figure is missing (no row, or a null component) the reason is "there is no figure from 12 quarters earlier"; if the earlier total is 0, "it reported no commercial real estate loans 12 quarters earlier".
- **Comparisons are `>=` on unrounded values** (the guidance says "or more"). Percentages are shown to one decimal.
- **Each line is judged separately.** A missing CRE component never hides the line-1 result.
- **No "approaching" label.** The guidance says "approaching or exceeds" but gives no number for approaching; choosing one would be Canary's own threshold. The ratios are shown, so a reader sees how close a bank is.
- The section copy (lead, capital lines, table, every summary sentence, definitions line, closing) is fixed in the spec, section 6, and in the code.

## The capital switch is keyed to the as-of quarter
A memo as of 2019-12-31 uses `RBC` and the 2006 capital wording; a memo as of 2020-03-31 uses `RBCT1J + LNATRES` and the 2020 wording. The switch uses the regulators' own documents, labelled as such. It never implies that Tier 1 plus allowance is the 2006 guidance's denominator.

`RBC` is 0 for 1,669 of 4,773 banks at 2022-12-31: banks on the community bank leverage ratio framework do not report Tier 2 capital. That does not matter to the test, because from 2020-03-31 every bank is measured on `RBCT1J + LNATRES`. CBLR began in 2020, so no memo quarter before 2020-03-31 has `RBC` of 0 (checked: zero count for 2014-2019).

## Separate data pull, not decision 0003's recipe
The fields come from the same `financials` endpoint but are a **separate raw table**, `data/raw/concentration/` (one file per quarter, `python -m canary.ingest concentration`), for the same reason as 0020: decision 0003's way to add a field re-pulls all 45 financial fields with `--force`, which would replace the raw values the warehouse, features and model were built from with today's amended FDIC values. `LNRECONS` is pulled again so every number in the test comes from one pull. The 45-field files and the specialty table were not touched.

Pull of 2026-11-19: 710,691 rows, 102 quarters (2001-03-31 to 2026-06-30), about 6 minutes. Null counts: `LNRECONS` 588, `LNREMULT` 588, `LNRENROT` 239,781 (reported from 2007 only), `LNCOMRE` 39,702, and `RBC`, `RBCT1J` and `LNATRES` 1,810 each. Not uploaded to S3 and not in Athena or dbt, so AWS cost is $0.

## Code only, and why
Two yes/no tests against published lines need no interpretation. Templates cannot misstate them, and the section adds no AI tokens, no retry risk and no new checker rules. Rejected: a short AI paragraph like 5b and 5c (more natural prose, but more cost and another first-attempt failure point on every note). Phase 5's fourth part is therefore a code-written section, not an AI agent, and the README says so. 5d adds **no Claude API cost**.

## Limits (honest list)
- **Negative allowances are used as reported.** 4 bank-quarters: cert 30746 in 2020Q1-Q3 and cert 4134 at 2024-09-30, where it cuts capital from 11,170 to 3,743.
- **Negative capital appears in 6 memo-era bank-quarters** (certs 9956, 19328, 57564, 58302 twice, 17719). The section now states this as "the bank's capital was zero or negative this quarter" rather than as missing data.
- **A screen, not a prediction.** Crossing a line is a supervisory screen for closer review. It has not been tested as a warning signal in Canary, and the section says so.
- **`LNCOMRE` is 0 for most small banks** (3,817 of 4,773 at 2022-12-31). It is used as reported, so total CRE for small banks is mostly the other three components.
- **The owner-occupied split exists only from 2007** (`LNRENROT` is null before that, so total CRE is missing for earlier quarters). This does not affect memos, which are written only for quarters from 2016-03-31.
- **2008-era failures have no memos.** Earlier rows were the model's training data, so the failures this failure mode is best known for are not covered. The section covers the 2016-2024 test-period failures and today's banks.
- **The guidance's "approaching" has no number, so none is used.** A bank at 290% shows no flag.
- **Display rounding:** comparisons use unrounded values, so a value such as 299.99% displays as "300.0%" with "no" in the table. The table and the summary sentences agree because both use the unrounded value.
- **The 2020 measure is not the 2006 measure.** After 2020-03-31 the denominator differs from the one the thresholds were written for, and the regulators did not restate the thresholds. The section says so.
- **Growth needs the same calendar quarter 12 quarters earlier.** Banks formed or merged recently, or with a null component then, can't be checked on growth. A merger that grows CRE by acquisition counts as growth.
- **The test is applied to the bank as it reported.** Amended filings are the FDIC's current values, as for the other tables.

## No tuning
The thresholds, the capital measures, the growth window and the wording are not adjusted to make a known failure stand out. That includes SVB, which crosses neither line at 2022-12-31 and is reported as such.

## Not in the committed notes yet
Notes in `banks/` do not have this section until the showcase is re-run, once, with both the 5c and 5d sections, and only with the owner's approval of a dry-run estimate.
