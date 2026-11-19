# Phase 5d Spec: Real-estate Concentration (2006 regulator thresholds)

**Date:** 2026-11-19
**Status:** Built (approved by Victor 2026-11-19, builder check done)
**Phase:** 5d of Phase 5 (5a risk analyst → 5b trends → 5c peers → **5d concentration**).
Builds on the 5a section registry and the 5b/5c hooks (`code_only`, `render_before`, `render`).

## 1. Intent: why this exists

Everything else in a Canary memo is about the bank's funding side or its overall score. 5d adds one
section on the **asset side**: did this bank cross the lines US bank regulators have used since 2006
to flag **commercial real estate (CRE) concentration** for closer review?

This is a different and more common way banks fail than SVB's (SVB failed on funding and bond
losses, not loan concentration). The section says so in its own text, so a reader doesn't take it
as repeating the SVB-flavoured sections above it.

**Everything in the test is external and published** (Victor): the thresholds, the loan categories
and the capital measure come from regulator documents (§5), not from Canary. Nothing is tuned.

**Note on coverage:** memos are written only for quarters from 2016-03-31 on (earlier rows were the
model's training data), so the 2008-era failures that this failure mode is best known for don't get
notes. The section covers the 2016-2024 test-period failures and today's banks.

## 2. Goals
- G1. A new, separate raw pull `data/raw/concentration/` of the FDIC fields the test needs (§4).
- G2. A **code-only** section "Real-estate concentration (2006 regulator thresholds)" in every memo
  (no AI text, no AI request, no facts for Claude), placed after 5c's peer section (§6).
- G3. Pure functions computing the two tests per §5 for a bank at its as-of quarter.
- G4. Tests for all code with no network or API; data checks on the real table.
- G5. Docs: decision record 0021, data dictionary (new raw table, note section), runbooks
  (ingestion, analyst), glossary, README/RESULTS, roadmap, daily log.

## 3. Non-goals
- Funding concentration (covered by Warning signs, trends and peers) and geographic concentration.
- Any measured result (no recall, catches, AUC, lead time for crossing a line).
- An "approaching the line" label (the guidance says "approaching or exceeds" but gives no number
  for approaching; choosing one would be Canary's own threshold). The ratios are shown, so a reader
  sees how close a bank is.
- Changing the model, the features export, `data/model/`, the 45-field raw pull or 5c's specialty
  table. No S3/Athena/dbt changes; AWS cost $0.
- Any Claude API cost: the section is code-only, so 5d adds no AI tokens and no live memo is needed.
- Re-running the showcase (one paid run after 5d, with Victor's approval of a dry run, is separate).

## 4. Data (new raw table)
- **Source:** `https://api.fdic.gov/banks/financials`, fields
  `CERT, REPDTE, LNRECONS, LNREMULT, LNRENROT, LNCOMRE, RBC, RBCT1J, LNATRES`, one request set per
  quarter, all quarters Phase 1 covers.
- **Storage:** `data/raw/concentration/repdte=YYYYMMDD/part.parquet`, same rules as decisions 0002,
  0004 and the 5c specialty pull (values unchanged, types set, `ingested_at`, atomic writes, latest 2
  quarters re-pulled, `--force` re-pulls all; 0 rows or duplicate CERT in a quarter → error). CLI
  `python -m canary.ingest concentration [--force]`.
- **Why separate:** the same reason as 5c (decision 0020): extending the 45-field pull would replace
  the raw values the warehouse and features were built from. `LNRECONS` is pulled again here so every
  number in the test comes from the same pull.
- **Field meanings** (FDIC / Call Report):
  `LNRECONS` construction, land development and other land loans (1-4 family construction plus other
  construction and land; Call Report F158 + F159); `LNREMULT` loans secured by multifamily property
  (1460); `LNRENROT` loans secured by other (non-owner-occupied) nonfarm nonresidential property
  (F161; reported from 2007); `LNCOMRE` loans to finance commercial real estate, construction and
  land development not secured by real estate (2746); `RBC` total risk-based capital (3792);
  `RBCT1J` Tier 1 capital; `LNATRES` allowance for loan and lease losses (for CECL adopters, the
  allowance for credit losses on loans and leases), $ thousands.
- **Checked 2026-11-19:** all fields present per quarter. `RBC` is 0 for 1,669 of 4,773 banks at
  2022-12-31 (banks on the community bank leverage ratio framework don't report Tier 2), which the
  2020 denominator (§5.2) makes irrelevant. `LNCOMRE` is 0 for most small banks (e.g. 3,817 of 4,773
  at 2022-12-31); it is used as reported.
- Data tests (marked `data`, skipped without local files): every financials (CERT, REPDTE) has a
  concentration row; dollar fields are non-negative where present.

## 5. The test (fixed, from published sources)

### 5.1 Numerators
- **Construction:** `LNRECONS`.
- **Total CRE:** `LNRECONS + LNREMULT + LNRENROT + LNCOMRE` (owner-occupied nonfarm nonresidential
  loans excluded), as the Federal Reserve's 2013 analysis of the guidance computes it (Call Report
  F158 + F159 + 1460 + F161 + 2746).
- A missing component (null) makes that numerator missing; a reported 0 counts as 0.

### 5.2 Capital (denominator), by quarter
- **As-of quarter before 2020-03-31:** total risk-based capital, `RBC` (as the 2006 guidance
  specifies).
- **As-of quarter on or after 2020-03-31:** Tier 1 capital plus the loan-loss allowance,
  `RBCT1J + LNATRES` (the denominator the agencies use for credit concentration ratios from
  March 31, 2020: FDIC FIL-31-2020; Federal Reserve SR 20-8). Applies to every bank, not only those
  on the simplified framework.
- Missing, zero or negative capital → neither ratio can be computed ("can't apply").

### 5.3 The two lines (OCC Bulletin 2006-46; 71 FR 74580)
- **Line 1, construction:** construction ÷ capital × 100 **≥ 100%** → crossed.
- **Line 2, total CRE:** total CRE ÷ capital × 100 **≥ 300%** **and** CRE growth **≥ 50%** over
  the prior 36 months → crossed.
- **Growth:** (total CRE at as-of ÷ total CRE at the same calendar quarter 12 quarters earlier − 1)
  × 100. If the earlier figure is missing (bank didn't report, or a component is null) or is 0,
  growth can't be computed.
- Line 2 outcomes: crossed (both parts met); not crossed (ratio < 300%, regardless of growth); "met
  the 300% level but grew less than 50%" (ratio ≥ 300%, growth < 50%); "met the 300% level; growth
  can't be checked" (ratio ≥ 300%, growth unknown); can't apply (ratio unknown).
- "Or more" in the guidance → `>=` comparisons, compared on unrounded values.

## 6. What gets written (code only)

Section title **"Real-estate concentration (2006 regulator thresholds)"**, key `concentration`,
`window = "as_of"`, always in `sheet.code_only`, registered after `peers`. Lines in order (exact
copy; `{}` filled by code):

1. **Lead (fixed):** "This section checks a different, more common way banks have failed than
   SVB's: heavy lending tied to commercial real estate. It applies the screens the OCC, Federal
   Reserve and FDIC set in 2006 to flag a bank for closer supervisory review; they are not lending
   limits."
2. **Capital line:**
   - before 2020-03-31: "Capital measure: total risk-based capital, as the 2006 guidance specifies."
   - from 2020-03-31: "Capital measure: Tier 1 capital plus the loan-loss allowance, which the
     regulators have used for concentration ratios since March 31, 2020 (FDIC FIL-31-2020; Federal
     Reserve SR 20-8). The 2006 thresholds were not restated for this measure."
3. **Table** (each row shows whether the bank meets that part; the lines are decided in item 4):
   `| Test | Bank | Line | Meets it? |`
   - "Construction and land loans ÷ capital" · `{x}%` · "100% or more" · yes / no / n/a
   - "Total commercial real estate loans ÷ capital" · `{y}%` · "300% or more" · yes / no / n/a
   - "Growth in commercial real estate loans over the prior 36 months" · `{z}%` · "50% or more" · yes / no / n/a
   "n/a" (and "n/a" in the Bank cell) when that value can't be computed. Percentages to one decimal,
   with thousands separators and a minus sign where needed; dollars are not shown.
4. **Summary** (code-chosen; one sentence per line, line 1 first, except the two combined forms):
   - Line 1 (construction):
     - crossed: "It crossed the construction line (100% or more of capital)."
     - not crossed: "It did not cross the construction line."
     - can't apply: "The construction line can't be checked: {reason}."
   - Line 2 (total CRE with growth):
     - crossed: "It crossed the total commercial real estate line (300% or more of capital, with 50% or more growth over 36 months)."
     - ratio < 300%: "It did not cross the total commercial real estate line."
     - ratio ≥ 300%, growth < 50%: "Its commercial real estate loans reached 300% of capital, but grew less than 50% over 36 months, so it did not cross the second line."
     - ratio ≥ 300%, growth unknown: "Its commercial real estate loans reached 300% of capital, but the growth part can't be checked: {growth reason}."
     - ratio unknown: "The total commercial real estate line can't be checked: {reason}."
   - Combined forms (replace the two sentences): both not crossed → "It did not cross either line."; both crossed → "It crossed both lines: construction loans and total commercial real estate loans."
   - `{reason}`: "the bank reported no capital figure for this quarter" (capital null) / "the bank's capital was zero or negative this quarter" (capital 0 or below) / "a loan figure the test needs is missing for this quarter" (a needed component null) / "there is no concentration data for this bank this quarter" (no row in the table).
   - `{growth reason}`: "there is no figure from 12 quarters earlier" (bank didn't report then, or a component was null) / "it reported no commercial real estate loans 12 quarters earlier" (earlier total was 0).
   Line 1 and line 2 are judged separately: a missing CRE component never hides a line-1 result.
5. **Definitions line (fixed):** "Total commercial real estate here means construction and land,
   multifamily, and non-owner-occupied commercial property loans, plus loans to finance commercial
   real estate not secured by real estate (FDIC call report data)."
6. **Closing (fixed):** "Crossing a line is a supervisory screen, not a prediction: it has not been
   tested as a warning signal in Canary."

No AI paragraph and no facts are added for Claude. The writer's user message does not mention
this section.

## 7. Approaches considered
- **Data: separate table `data/raw/concentration/` (chosen, Victor).** Same discipline as 5c.
  Rejected: adding the fields to 5c's specialty table (mixes unrelated data; changes 5c's table and
  tests) or to the 45-field pull (overwrites the raw values the model results came from).
- **Writing: code-only section (chosen, Victor).** Two yes/no tests against published lines don't
  need interpretation; templates can't misstate them; adds no AI tokens or retry risk to the
  showcase. Rejected: a short AI paragraph like 5b/5c (more natural prose, but more cost and another
  first-attempt failure point on every note). Phase 5's fourth agent is therefore a code-written
  section, and the README says so.
- **Capital for banks without total capital:** settled by sources, not a stand-in: since 2020-03-31
  regulators use Tier 1 plus allowance for every bank (§5.2).

## 8. Decided by Victor
- Loan concentration only (CRE and construction vs capital, 2006 interagency thresholds).
- The section says it covers a different, more common failure mode than SVB's.
- Denominator is capital, not equity; multifamily pulled.
- Use the 2020 Tier 1 + allowance measure only because the regulators' own documents (FIL-31-2020,
  SR 20-8) specify it, labelled as such; never imply it is the 2006 guidance's own denominator.
- Separate raw table; code-only section.

## 9. Calls made by Claude (Victor to check)
- Denominator switch keyed to the **as-of quarter** (before vs on/after 2020-03-31).
- `LNRECONS` re-pulled into the new table for one data vintage.
- `LNCOMRE` used as reported (0 for most small banks).
- No "approaching" label; ratios shown instead.
- Growth needs the same calendar quarter 12 quarters earlier; otherwise "can't be checked".
- Exact section copy in §6 (title, lead, capital lines, summary sentences, definitions, closing).
- Table shows whether each part is met (yes/no/n/a); the lines are decided only in the summary, so the table and sentences can't contradict each other (builder check).
- Each line judged separately; separate wording for "no figure 12 quarters earlier" vs "reported no CRE loans then"; no concentration row → can't apply (builder check).
- Decision record 0021: sources (OCC Bulletin 2006-46 / 71 FR 74580; Fed 2013 CRE analysis
  appendix; FDIC FIL-31-2020; SR 20-8), the fixed test, the denominator rule, code-only, limits
  (`LNCOMRE` zeros; owner-occupied split from 2007 only, which doesn't affect 2016+ memos;
  2008-era failures not covered by memos).

## 10. Left to the builder
- Module layout (e.g. `canary/ingest_concentration.py`, `canary/analyst/concentration.py`), reuse of
  the 5c ingestion helpers, table formatting within §6.
- Whether the concentration table is loaded into `Context` or read per memo (either is fine; loading
  once like `ctx.specialty` is the obvious choice).
