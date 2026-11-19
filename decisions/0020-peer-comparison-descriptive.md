# 0020 — Peer comparison: descriptive only, with a fixed peer rule

**Date:** 2026-11-18
**Status:** Accepted (design approved by the owner; built in Phase 5c)

## Decision
Every bank note gets a section, **"Compared with similar banks"**. For each ratio where the bank is in the national top or bottom 10% that quarter, it shows whether the bank is also unusual among banks the FDIC groups with it (same specialty group and size tier). It is **descriptive only**. It makes no claim that an unusual figure predicts failure, and there is **no measured result** for it (no recall, catches, AUC, lead time or false-alarm rate) in the notes, the README, RESULTS or anywhere else.

Code: `src/canary/analyst/peers.py` (rule and section), `checker.py` (peer rules), `ingest_specialty.py` (the data pull). Format: [[data-dictionary/bank_notes]], [[data-dictionary/fdic_specialty]]. Design: [[specs/2026-11-18-phase5c-peers-design]].

## Why it exists
The 5a "Warning signs" section compares a bank with the national median. That cannot tell a risky bank from a different kind of bank: a large commercial lender looks unusual next to a median set by thousands of small community banks. The peer section asks whether the bank is an outlier within its own category or just a different category. A ratio that is extreme nationally and among peers is a stronger observation than one that is extreme only nationally; a ratio that is typical for the group is explained by the group.

## Separate data pull, not decision 0003's recipe
The FDIC's specialty group (`SPECGRP`) and city (`CITY`) come from the same `financials` endpoint, but as a **separate raw table**, `data/raw/specialty/` (one file per quarter, `python -m canary.ingest specialty`). Decision 0003's way to add a field re-pulls all 45 financial fields with `--force`, which would replace the raw values the Phase 2-4 warehouse, features and model were built from with today's amended FDIC values. A separate table adds the two fields without touching them. The 45-field financials files were not touched.

Pull of 2026-11-18: 710,691 rows, 102 quarters (2001-03-31 to 2026-06-30), 0 null `SPECGRP`, about 5 minutes. Not uploaded to S3 and not in Athena or dbt, so AWS cost is $0.

## The label is used as published, per quarter
The specialty is the one the FDIC recorded for the **as-of quarter**, never today's value from the `institutions` endpoint. Example: First Republic was group 6 (Consumer Lending Specialization) at 2022-12-31 and is group 9 today; using today's label would be hindsight.

**Silicon Valley Bank is in group 9, "All Other Over 1 Billion", at 2022-12-31**, a general group for large banks that meet no specialty's concentration threshold. It is not in "Commercial Lending" with Signature. This is stated in SVB's note as a finding of its own. Nothing was redefined to put SVB with commercial lenders; our own business-model classification was considered and rejected because its categories would be designed after knowing where SVB should land.

Source of the grouping: it matches the FDIC's Quarterly Banking Profile (QBP) specialty groups and asset bands. It is **not** the FFIEC UBPR peer grouping, which uses size, branch count and metro/rural, not specialty.

## The fixed peer rule
Set before any bank's result was looked at. **Do not change any of these after seeing results.** Changing one needs a new decision record that says why and states plainly that it was changed after seeing results.

- **Specialty:** `SPECGRP` at the as-of quarter, from `data/raw/specialty/`. Names: 1 "International Specialization", 2 "Agricultural Specialization", 3 "Credit-card Specialization", 4 "Commercial Lending Specialization", 5 "Mortgage Lending Specialization", 6 "Consumer Lending Specialization", 7 "Other Specialized Under 1 Billion", 8 "All Other Under 1 Billion", 9 "All Other Over 1 Billion".
- **Size tiers** (assets = `exp(log_total_assets) * 1000` dollars; lower bound inclusive): "under $100 million" (below 1e8), "$100 million to $1 billion" (below 1e9), "$1 billion to $10 billion" (below 1e10), "over $10 billion".
- **Minimum peer group:** `MIN_PEERS = 15` banks, the bank included. Order: specialty + size tier; if fewer than 15, specialty with all sizes; if still fewer, no comparison.
- **Universe:** every bank in the features export that quarter (the banks the national comparison uses), joined with its specialty that quarter.
- **Ratios:** `canary.analyst.trends.TREND_RATIOS`, the same 30 as 5b.
- **Banks counted per ratio:** only banks with a value; NaN is left out of both the set and the count. If a bank's own `log_total_assets` is missing, `compute_peers` raises (0 such rows in the real data).
- **Displayed percentile:** true mid-rank, (count below + 0.5 x count equal) / n x 100.
- **Unusual (`UNUSUAL_SHARE = 0.10`):** unusually low when the share of banks with a value at or below the bank's is at most 10%; unusually high when the share at or above is at most 10%. Applied nationally and, with the same cut-off, within the peer group (which needs at least 15 banks with a value for that ratio).
- **Readings (exact):** "unusually high among its peers too", "unusually high among its peers", "unusually low among its peers too", "unusually low among its peers", "typical for its peer group", "too few peers with this figure". The "too" forms mean the bank is unusual on the same side nationally. National words (exact): "unusually high", "unusually low".
- **Order and cap:** rows ordered by `abs(national mid-rank percentile - 50)` descending, ties by plain name; at most `MAX_SHOWN_PEERS = 8` shown.
- **Fixed sentence, code-rendered at the end of the section:** "This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal."
- **Code-written lines:** the specialty line; for groups 8 and 9 only, "This is a general group: the FDIC did not record a lending specialty for this bank."; the peer-group line (specialty and tier, or specialty at all sizes "because fewer than 15 shared its size tier"); the not-enough-banks line; the no-specialty line; and "None of this bank's ratios were in the national top or bottom 10% at {as_of}." When nothing is nationally unusual or no comparison is shown, the section is code-only and no AI request is made for it.

## Ties
A value shared by many banks is never "unusual" because of how ties are ranked. If 15% of banks sit at 0.0 (brokered deposits, say), the share at or below and at or above 0.0 is above 10%, so a bank at 0.0 is not unusual on either side, nationally or among peers.

## Readings carry their own peer direction
A ratio can be high nationally and low among peers (for example a card lender's charge-offs). The reading says so ("unusually low among its peers") rather than calling every peer outlier "unusual too". The 10% cut-off is unchanged. The checker rejects the opposite reading for such a ratio.

## A correction recorded here
The design spec (section 6.2) and the build plan wrote the displayed percentile as `rank(pct=True, method="average") * 100`. That gives 100 for the maximum, which is not a mid-rank. The built rule is the true mid-rank above, (count below + 0.5 x count equal) / n x 100. The spec text was corrected. This affects display and ordering only; the "unusual" test (share at or below / at or above, at most 10%) is unchanged and was never based on the displayed percentile.

## No tuning
Size tiers, the 15-bank minimum, the 10% cut-off, the fallback order and the cap of 8 are not adjusted to make a known failure stand out. That includes SVB, and the live test memo below changed nothing.

## What the checker enforces for this section
Narrow rules, applied only to sentences in this section, feeding the existing single retry ([[decisions/0016-analyst-memo-design]]):

1. **One ratio per sentence** when a peer reading or peer percentile fact is cited, and every per-ratio peer fact cited is that ratio's ("give one ratio per sentence when stating its peer reading").
2. **No opposite reading.** A sentence citing "typical for its peer group" must not say "unusual among its peers" or "unusually high/low among its peers" (contiguous claims only, so "unusually high nationally, yet typical among its peers" is accepted). A sentence citing a high reading must not say "unusually low among its peers" or "typical for its peer group", and the reverse. A national direction fact rules out the opposite national word, except where that word is part of "... among its peers".
3. **No prediction language** (the 5b list) and no "risky"/"riskier" anywhere in the section.

## Limits (honest list)
- **The rules are blunt regexes.** Paraphrases evade them ("on the high side compared with similar banks", "out of line with the group").
- **The national-word rule exempts only "among its peers".** "Unusually low among peers" (no "its") is falsely rejected as a national word and can cost the one retry.
- **The checker reads cited ids, not prose.** A sentence that names a second ratio without citing it is not caught.
- As in 0016 and 0019, the checker verifies numbers and some phrasing, not every claim; the prompt is the first line of defence.
- **The peer group is the FDIC's grouping, not ours.** Group 9 mixes very different large banks, so "typical for its peer group" can mean little. A small group (15 to 25 banks) gives a coarse percentile.
- **"Unusual" is not "risky".** High capital is unusual and good. The section never calls anything risky and has not been tested as a warning signal.
- Specialty is the FDIC's label at the as-of quarter; banks can switch group between quarters.

## No showcase re-run until 5d
Each memo is longer, so a re-run costs about as much as 5b's ($8). The committed notes in `banks/` do not have this section yet. The showcase waits for 5d (concentration risk) so the notes are paid for once with both sections, and runs only with the owner's approval of a dry-run estimate. One live test memo was run in 5c (SVB as of 2022-12-31, written outside the committed notes): it passed the checker on the second attempt, 29,965 in / 11,292 out tokens, $0.3457.
