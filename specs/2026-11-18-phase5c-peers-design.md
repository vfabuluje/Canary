# Phase 5c Spec: Peer Comparison (descriptive)

**Date:** 2026-11-18
**Status:** Built (Phase 5c, 2026-11-18). Approved by Victor 2026-11-18 (builder check done)
**Phase:** 5c of Phase 5 (5a risk analyst → 5b trends → **5c peer comparison** → 5d concentration risk).
Builds on [[specs/2026-11-17-phase5a-risk-analyst-design]] §7 (section registry) and the hooks added in
[[specs/2026-11-18-phase5b-trend-design]] (code-only sections, code-rendered section bodies).

## 1. Intent: why this exists

The 5a "Warning signs" section compares a bank with the **national median**. That can't tell two
things apart: a bank that is risky, and a bank that is simply a different kind of bank. A large
commercial lender looks unusual next to a median set by thousands of small community banks,
whether or not it is risky.

5c adds one section that answers: **is this bank an outlier within its own category, or just a
different category?** For each ratio where the bank is unusual nationally, the section shows
whether it is also unusual among comparable banks (same FDIC specialty group and size tier). A
ratio that is extreme nationally *and* among peers is a stronger signal than one that is only
extreme nationally; a ratio that is typical for the bank's group is explained by its business
model.

Readers are the same as 5a/5b: a recruiter or interviewer reading a note, and Victor explaining it.

**The FDIC label is used as published (Victor).** At 2022-12-31 the FDIC put SVB in group 9, "All
Other Over 1 Billion" (large banks that meet no specialty's concentration threshold), not in
"Commercial Lending" with Signature. That is the honest answer from an outside label we did not
design. SVB's note states it plainly as a finding of its own, and nothing is redefined to put SVB
with commercial lenders.

## 2. Goals
- G1. **Specialty data.** A new, separate raw pull of the FDIC specialty group (`SPECGRP`) and city
  (`CITY`) for every bank and quarter, from the same `financials` endpoint Phase 1 uses (§5).
- G2. A **peer specialist** module that registers with the 5a section registry, adds facts, and
  supplies a code-rendered table, so the existing writer, checker and renderer cover it.
- G3. For each memo, code builds the **peer group** (§6.1), finds the ratios where the bank is in
  the national top or bottom 10%, and for each gives the bank's percentile among its peers and a
  code-chosen reading (§6.2).
- G4. **Code-written lines** for the bank's specialty label, the peer group used, and the
  not-enough-peers case; a fixed descriptive sentence (§7.3).
- G5. **City search for every bank** in the `ask` agent's `find_bank` (the 5a spec deferred it to
  this pull).
- G6. Tests for all non-AI code with no network or API (fake FDIC client, fake Claude).
- G7. Docs: decision record 0020, data dictionary (new raw table and note section), runbooks
  (ingestion and analyst), glossary, README/RESULTS mention, roadmap and daily log.

## 3. Non-goals
- **Any measured result.** No recall, catches, AUC, lead time or false-alarm rate for peer readings.
- **Re-running the showcase.** Each memo gets longer, so a re-run costs about as much as 5b's
  ($8). It waits until 5d is built, so the notes are paid for once with both sections, and only
  with Victor's approval of a dry-run estimate. One live test memo is in scope.
- Changing the Phase 3 model, `data/model/`, the features export or the 45-field financials pull.
- Uploading the new raw table to S3 or adding it to Athena/dbt. Everything stays local; AWS cost $0.
- State as a peer dimension (that is a regional-concentration question, closer to 5d).
- Our own business-model classification (§9).

## 4. Anti-goals (a failure even if it "works")
- **Defining or tuning anything after seeing where SVB (or any known failure) lands.** The peer
  rule in §6 is fixed in this spec. Changing the size tiers, minimum, 10% cut-off or fallback after
  seeing results needs a new decision record saying results were seen.
- **Using today's label for an old quarter.** The specialty is the one the FDIC recorded for the
  as-of quarter, never the current `institutions` value (First Republic was "Consumer Lending" at
  2022-12-31 and is "All Other Over 1 Billion" today).
- **Implying risk from "unusual".** A high percentile is not "risky" (high capital is unusual and
  good). The section says "unusually high/low", never "risky" or "a warning", and makes no
  prediction claim.
- **A precise-looking number against too few banks.** Below the minimum, no comparison is shown.
- **Mixing ratios.** A sentence giving a ratio's peer reading cites only that ratio's facts.
- **Hindsight.** The section is as-of only.
- **Changing the existing raw financials.** The 45-field pull and its files are not touched (§5).

## 5. Specialty data (new raw table)
- **Source:** `https://api.fdic.gov/banks/financials` (the endpoint Phase 1 already uses), fields
  `CERT, REPDTE, SPECGRP, CITY`, one request set per quarter, all quarters Phase 1 covers.
  Checked 2026-11-18: `SPECGRP` and `CITY` are present per quarter (SVB: `SPECGRP` 9 at
  2010-12-31 and 2022-12-31, `CITY` "SANTA CLARA" at 2022-12-31; First Republic: 6 at 2022-12-31). `SPECGRPN` (the name) is not in this endpoint; names come from a
  fixed code table in code (§6.1), taken from the FDIC's published group names.
- **Storage:** `data/raw/specialty/repdte=YYYYMMDD/part.parquet`, same layout and rules as decisions
  0002 and 0004 (values unchanged, types set, `ingested_at` added, latest 2 quarters re-pulled on
  each run, `--force` re-pulls all).
- **Why a separate pull, not decision 0003's "add a field" recipe:** that recipe re-pulls all 45
  fields with `--force`, replacing the raw values the Phase 2-4 warehouse and features were built
  from with today's amended FDIC values. A separate table adds the two fields without touching
  them.
- **CLI:** `python -m canary.ingest specialty [--force]`, reusing `FDICClient` and the quarter list.
- Data tests (marked `data`, skipped without local files): every financials (CERT, REPDTE) has a
  specialty row; `SPECGRP` codes are within 1-9 (or null, counted and reported).

## 6. The peer rule (fixed)

### 6.1 Peer group for a bank at the as-of quarter
- **Specialty:** the bank's `SPECGRP` at the as-of quarter. Names (FDIC):
  1 International Specialization; 2 Agricultural Specialization; 3 Credit-card Specialization;
  4 Commercial Lending Specialization; 5 Mortgage Lending Specialization; 6 Consumer Lending
  Specialization; 7 Other Specialized Under 1 Billion; 8 All Other Under 1 Billion;
  9 All Other Over 1 Billion.
- **Size tier** from total assets at the as-of quarter (from `log_total_assets`, ln of $ thousands),
  the FDIC Quarterly Banking Profile's asset bands: under $100 million; $100 million to $1 billion;
  $1 billion to $10 billion; over $10 billion. Lower bound inclusive.
- **Universe:** every bank in the features export at that quarter (the same banks the national
  comparison uses), joined with its specialty that quarter.
- **Minimum peer group: 15 banks** (including the bank itself).
- **Order:** (1) same specialty and same size tier; if fewer than 15 banks, (2) same specialty, any
  size; if still fewer than 15, (3) no comparison: the section says there aren't enough comparable
  peers for a reliable comparison (§7.1).
- A bank with no specialty value at the as-of quarter gets a code line saying the FDIC recorded no
  specialty group for that quarter, and no comparison.
- Groups 7, 8 and 9 carry size in their names; the order above handles them with no special case.

### 6.2 Which ratios, and the reading
- **Ratios:** the 30 model features used in 5b (`trends.TREND_RATIOS`, all features except
  `log_total_assets`).
- **Banks counted:** for a ratio and a set of banks, only banks with a value (NaN left out of both
  the set and the count).
- **Displayed percentile:** true mid-rank, 0-100: (count below + 0.5 × count equal) / n × 100. (The first draft wrote `rank(pct=True, method="average") * 100`, which gives 100 for the maximum; corrected at build, see [[decisions/0020-peer-comparison-descriptive]]. It affects display and ordering only; the "unusual" test below is unchanged.)
- **Unusual (ties handled conservatively):** a value is **unusually low** in a set when the share of
  banks with a value **at or below** it is ≤ 10%, and **unusually high** when the share with a value
  **at or above** it is ≤ 10%. So a value shared by many banks (e.g. 0 for brokered deposits at 15%
  of banks) is never "unusual" just because of how ties are ranked, on either side.
- **Nationally unusual:** unusually high or unusually low among all banks that quarter.
- For each nationally unusual ratio, if the peer group has at least 15 banks with a value for that
  ratio: peer percentile and peer median, and a **reading** chosen by code, with its own direction
  (the same unusual test applied within the peer group):
  - unusually high among peers → **"unusually high among its peers too"** if it is also nationally
    high, or **"unusually high among its peers"** if it is nationally low;
  - unusually low among peers → **"unusually low among its peers too"** / **"unusually low among
    its peers"** likewise;
  - neither → **"typical for its peer group"**.
  (A ratio can be high nationally but low among peers, e.g. a card lender's charge-offs; the reading
  says so instead of calling it "unusual too".) If fewer than 15 peers have a value for that ratio
  → reading **"too few peers with this figure"**, no peer percentile shown.
- **National direction words:** "unusually high" or "unusually low" nationally, from the same test.
- **Order and cap:** by distance of the national (mid-rank) percentile from 50, largest first; ties by plain
  name; at most **8** shown. Counts of all unusual ratios and of those unusual among peers too are
  facts.

## 7. What gets written

### 7.1 Section and parts
One section, **"Compared with similar banks"**, in the specialist slot after 5b's "How its ratios
moved" (registration order), `window = "as_of"`. Parts in order:
1. **Code lines (always):**
   - "The FDIC's specialty group for this bank at {as_of}: {name}." For groups 8 and 9 add: "This is
     a general group: the FDIC did not record a lending specialty for this bank." (Group 7, "Other
     Specialized Under 1 Billion", is a specialized group and gets no such line.)
   - The peer group used: "Peers: {n} banks in the same specialty group and size tier ({tier})." or
     "Peers: {n} banks in the same specialty group (all sizes), because fewer than 15 shared its size
     tier." or the not-enough line: "There are not enough comparable banks ({n} in its specialty
     group) for a reliable comparison, so none is shown."
2. **AI paragraph(s)** (only when a comparison is shown and at least one ratio is nationally
   unusual): for the ratios it discusses, the bank's value, its national percentile, its peer
   percentile and the reading; then one plain sentence on the overall picture, using the two
   counts. No risk words, no prediction, no outcome.
3. **Code-rendered table:** Ratio · Bank · National percentile · Peer median · Peer percentile ·
   Reading.
4. **Fixed sentence** (§7.3).

When no ratio is nationally unusual, or there is no comparison, the section is code-only (5b's
`code_only` hook): the code lines, a line "None of this bank's ratios were in the national top or
bottom 10% at {as_of}." where it applies, and the fixed sentence. No AI request for the section.

### 7.2 Facts
As-of only (`hindsight=False`), with `feature` and `kind` set like 5b's:
per shown ratio: value (5a display forms), national percentile, peer percentile, peer median,
reading (text), direction words (text); sheet-level: specialty code and name (text), size tier
(text), peer group basis (text), peer count, counts of unusual and unusual-among-peers ratios,
count shown. Percentile facts get the 5a percentile forms including decimal ordinals ("98.2nd").

### 7.3 Fixed sentence
"This section only compares the bank with banks the FDIC groups with it; an unusual figure is not
a prediction of failure, and the comparison has not been tested as a warning signal."

### 7.4 Prompt and checker
- Instructions: use only the peer facts and the as-of rank facts; give one ratio per sentence when
  stating its peer reading; use the code's reading and direction words with the same meaning; say
  "unusually high/low", never "risky", "warning", "predict" or "forecast" (even negated); don't
  write a disclaimer; don't mention the outcome.
- Checker (reuse 5b's machinery, scoped to this section's key): (1) one ratio per sentence when a
  `peer_reading` or `peer_percentile` fact is cited, and every per-ratio peer fact cited is that
  ratio's; (2) the opposite reading is rejected (a sentence citing a "typical for its peer group"
  fact must not say "unusual among its peers" / "unusually high/low among its peers", and a sentence
  citing an "unusually high…" reading must not say "unusually low among its peers", and the reverse;
  the same for the national direction words); (3) 5b's prediction-phrase rule plus "risky"/"riskier" in this section.

## 8. City search (G5)
`ctx.banks.city` comes from the specialty table's `CITY` at each bank's last report, for every
bank (failed banks keep the failures list's city when the specialty table has none). `find_bank`
matches city for all banks, not only failed ones; its description and runbook are updated.

## 9. Approaches considered
- **A. Separate specialty pull + peer specialist in the 5a registry (chosen).** Same discipline as
  5a/5b; existing raw data untouched; the label is the FDIC's own, per quarter.
- **B. Add `SPECGRP`/`CITY` to the 45-field pull (decision 0003's recipe) (rejected).** Would
  overwrite the raw values the warehouse and features came from with today's amended values.
- **C. `institutions` endpoint (rejected).** Only today's label: hindsight for old quarters.
- **D. Our own classification, e.g. from loan mix (rejected by Victor).** Could put SVB with
  commercial lenders, but the categories would be designed after knowing where SVB should land.
- **E. All 30 ratios with a peer percentile each (rejected).** Complete but noisy; the question is
  about the ratios where the bank is unusual.

## 10. Decided by Victor
- The section answers "outlier within its own category, or just a different category?".
- FDIC specialty label as published; SVB's "All Other Over 1 Billion" stated plainly as a finding.
- Peer group = specialty + size tier; not state.
- Minimum peer group of 10-15 (15 chosen, §11); fallback specialty + size → specialty → no
  comparison with a plain statement.
- Ratios: nationally top/bottom 10%, each read against peers with the same 10% cut-off.
- Size tier from existing `ASSET` data (via `log_total_assets`); only the label is a new fetch.

## 11. Calls made by Claude (Victor to check)
- Minimum **15** banks (Credit-card, 10 banks at 2022-12-31, and International, 5, will usually get
  the not-enough line).
- Size tiers = FDIC Quarterly Banking Profile bands (<$100M, $100M-$1B, $1B-$10B, >$10B).
- Separate raw table `data/raw/specialty/` instead of extending the 45-field pull (§5, §9 B).
- Percentile and ties (§6.2): mid-rank for display; "unusual" tested with at-or-below / at-or-above
  shares ≤ 10%, so tied values (often zeros) aren't flagged by ranking accident; per-ratio minimum
  of 15 peers with a value.
- Readings carry their own peer direction (§6.2), so "high nationally, low among peers" is said as
  such (found in the builder check; the 10% cut-off itself is unchanged).
- The "general group, no lending specialty" line is for groups 8 and 9 only, not 7.
- Up to 8 ratios shown, ordered by distance from the national median percentile.
- Section title "Compared with similar banks"; placed after 5b's section.
- Descriptive only, with a fixed sentence; checker rules reused from 5b.
- No showcase re-run in 5c (wait for 5d, then one paid run with Victor's approval).
- Correction noted in conversation: FFIEC UBPR peer groups use size, branch count and metro/rural,
  not specialty; specialty + size matches the FDIC's Quarterly Banking Profile groupings, which is
  what decision 0020 cites.
- Decision record 0020 covers: the separate pull, the fixed peer rule, the FDIC label as published
  (with SVB's group as a stated finding), and descriptive only.

## 12. Left to the builder
- Module layout (e.g. `canary/analyst/peers.py`, `canary/ingest_specialty.py`), exact fact labels,
  prompt wording and table formatting within §6-§7.
- Whether peer computations for a quarter are cached (not needed for correctness).
