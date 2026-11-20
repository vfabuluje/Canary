# bank_notes (Phase 5a risk-analyst notes)

One Markdown note per bank in `banks/`, written by `python -m canary.analyst memo` / `showcase` / `ask`. They are **notes in the vault, not warehouse tables**. Design: [[specs/2026-11-17-phase5a-risk-analyst-design]]. Decisions: [[decisions/0016-analyst-memo-design]], [[decisions/0018-failures-after-test-window]], [[decisions/0019-ratio-trends-descriptive]], [[decisions/0020-peer-comparison-descriptive]], [[decisions/0022-three-agent-memo-pipeline]]. Runbook: [[runbooks/analyst]].

| | |
|---|---|
| Inputs (read only) | `fct_bank_features` export, Phase 3 `model.json`, failures file, Phase 4 replay CSVs |
| Built by | `src/canary/analyst/` (`facts.py`, `writer.py`, `checker.py`, `render.py`) |
| One note per | Bank. Re-running a bank replaces its note. |
| Saved only if | Every AI sentence passed the citation checker. |

## File name
`banks/<Title Case Name> (<cert>).md`, for example `banks/Silicon Valley Bank (24735).md`. The name is the institution name in Title Case; the characters `/ \ : * ? " < > | # ^ [ ]` become `-`.

## Front matter

| Field | Type | Meaning |
|---|---|---|
| `cert` | integer | FDIC certificate number. |
| `name` | string | Institution name as the data shows it. |
| `as_of` | date | The quarter-end the note is written as of. Everything outside the hindsight sections uses only data up to here. |
| `rank` | integer or null | National rank at as-of, 1 = highest score among all banks that quarter. |
| `n_banks` | integer or null | Banks ranked that quarter. |
| `percentile` | number or null | `100 * (1 - (rank - 1) / n_banks)`; 100 is the riskiest. |
| `flagged` | boolean or null | True if the bank was on the top-2% watchlist at as-of ([[decisions/0011-watchlist-flag-and-metrics]]). |
| `outcome` | string | `caught`, `missed`, `false_alarm`, `quiet` or `open_watchlist`. See below. |
| `after_test_window` | boolean | True for a failure after 2025-12-31 (not part of the reported 2016-2024 results). |
| `failure_date` | date or null | Failure date; null if the bank had not failed by the data end. |
| `model_run` | string | First 12 characters of the SHA-256 of `model.json`: which saved model scored it. |
| `written_at` | string | Local time the note was written (ISO, seconds). |
| `writer_model` | string | The model that actually served the requests (can differ from the one asked for if a fallback was used). |
| `checked` | boolean | Always `true`; unchecked notes are never saved. |

## Outcome values
- `caught`: failed, and Canary flagged it 1 to 4 quarters before failure (Phase 3 lead-time rule).
- `missed`: failed, and no flag in that window.
- `false_alarm`: not failed, but flagged at as-of (an earlier quarter than the latest).
- `quiet`: not failed, not flagged.
- `open_watchlist`: flagged at the latest quarter; outcome not yet known.

## Sections, in order
Since Phase 5e three AI agents write the sections ([[decisions/0022-three-agent-memo-pipeline]]): the **trend agent** writes `trends`, the **peer agent** writes `peers`, and the **risk analyst** writes every other Claude section (summary, warning signs, the score, the outcome section, what happened next). The analyst never edits the specialists' text: it appears in the note as exactly the checked text of that agent's memo. "Claude" below means whichever of the three agent writes that section. Concentration is code-only.


| Section | Who writes it | Time window |
|---|---|---|
| Banner (first line under the title) | Code | Hindsight, labelled |
| Summary | Claude | As-of only |
| Warning signs in the data | Claude | As-of only, with the national median for that quarter |
| Understanding the score | Claude, then code adds the fixed sentence "The score ranks banks against each other; it is not a probability of failure..." and **What the model can't see** | As-of only |
| Score history | Code (table: quarter, rank, of, watchlist; first flag marked) | The 8 quarters up to as-of |
| How its ratios moved (key `trends`, added in 5b) | Claude (one or two paragraphs), then a code table and the fixed sentence; or one code-written line | As-of only |
| Compared with similar banks (key `peers`, added in 5c) | Claude (one or two paragraphs), then a code table and the fixed sentence; or code-written lines only | As-of only |
| Real-estate concentration (2006 regulator thresholds) (key `concentration`, added in 5d) | Code only: lead, capital line, table, summary sentences, definitions line, closing | As-of only |
| Outcome (title depends on `outcome`: "How early Canary caught it", "Why the model missed it", "Why it was flagged, and what happened", "Why it's on the watchlist"; absent for `quiet`) | Claude | Hindsight, labelled |
| What happened next | Claude, plus a code table of later ranks when there are any | Hindsight, labelled |
| Sources | Code: every cited fact as `id · label · quarter · value · file` | n/a |

## Banner wording
- caught: `*Hindsight: failed YYYY-MM-DD. Canary flagged it N quarters ahead.*` ("quarter" when N is 1)
- missed: `*Hindsight: failed YYYY-MM-DD. Canary did not flag it.*`
- false_alarm: `*Hindsight: flagged, but had not failed as of YYYY-MM-DD.*` (the bank's last report)
- open_watchlist: `*Outcome not yet known.*`
- quiet: no outcome line.
- After the test window (any failure after 2025-12-31) adds a second line: `*After the test window: not part of the reported 2016-2024 results.*`, repeated inside the Outcome section.

## How its ratios moved (Phase 5b)
Sits after Score history in every memo. Descriptive only: it compares the bank's ratios with the bank's own past and has **no measured result** ([[decisions/0019-ratio-trends-descriptive]]). Code: `src/canary/analyst/trends.py`.

**Which ratios are shown.** Of the 30 model ratios (all features except `log_total_assets`), those whose as-of value is below the minimum or above the maximum of the bank's own comparison window. Point-in-time ratios use the 12 quarters before as-of (at least 8 with a value); year-to-date ratios (return on assets, return on equity, net interest margin, efficiency ratio, net charge-offs, provision, interest expense) use the same quarter of the 3 prior years (at least 2). At most 6 are shown, furthest outside first (excess in percentage points divided by the range width, with a 1 pp floor). If more are outside, a line says "N of M ratios were outside their prior range; the 6 furthest are shown."

**Table columns (code-rendered).**

| Column | Meaning |
|---|---|
| Ratio | Plain-English name. |
| As-of value | The ratio at the as-of quarter, in its usual unit. |
| Prior range | Lowest to highest value in the comparison window. |
| Window | "prior 12 quarters" or "same quarter, prior 3 years". |
| Change 1q | Change from the previous quarter in percentage points (pp); `n/a` for year-to-date ratios. |
| Change 4q | Change from four quarters earlier in pp; `n/a` if there is no value then. |
| Model contribution | The ratio's own contribution to the score, in model log-odds units, to 3 decimals. Positive pushes the score up. |
| Direction | From the contribution: +0.05 or more "pushed the score up"; -0.05 or less "pushed the score down"; otherwise "little effect on the score". |

A change is always written in pp (a ratio that moved from 6.6% to 48.4% changed by +41.8 pp, not "41.8%").

**Facts added to the sheet** (all as-of, none hindsight), with a `kind` the checker uses: per shown ratio, `trend_value`, `trend_lo`, `trend_hi`, `trend_change_1q`, `trend_change_4q` (when present), `trend_contribution`, `trend_direction` (text, no number); sheet-level, `trend_count_outside`, `trend_count_checked`, `trend_count_shown` (how many ratios the table shows, at most 6), `trend_window_pit` (12 quarters, min 8), `trend_window_ytd` (3 years, min 2), `trend_prior_percentile` (percentile at the same quarter a year earlier) and `trend_rank_phrase` ("the model rated it riskier / safer than a year earlier" or "about the same as a year earlier", by a 1.0 percentile threshold). The last two are absent when there is no year-earlier score; code then renders the line "There is no score from a year earlier to compare with (scores start 2016-03-31, or the bank did not report then)." first in the code part of the section. A negative zero is never printed ("-0.0%", "-0.00 pp" and "-0.000" appear as "0.0%", "+0.00 pp" and "+0.000").

**Code-written text.**
- Fixed sentence, last in the section: "This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure."
- If no ratio is outside its range: "None of this bank's ratios were outside their own prior range at {as_of}." plus the fixed sentence. No Claude request is made for the section.
- If no ratio has enough history: "This bank has too little history before {as_of} to compare its ratios with its own prior range." plus the fixed sentence.

**Extra checker rules for this section only:** a sentence that cites a contribution or direction fact must cite one ratio only, and every per-ratio trend fact it cites must be that ratio ("give one ratio per sentence when stating its contribution or direction"); a contribution must be cited with its own ratio's value or range; the direction wording must not contradict the code's label; a cited rank phrase must not be contradicted ("riskier" vs "safer"); prediction language ("predict", "warned", "early warning", "would have caught" and close variants) is rejected. The rules are blunt and miss paraphrases ([[decisions/0019-ratio-trends-descriptive]]).

**A ratio that was high for a while is not listed.** The rule flags a break-out of the bank's own past range. SVB's last-report note (2022-12-31) therefore does not list its HTM loss ratio, which had already been high for three quarters. Note as of 2022-03-31 does.

## Compared with similar banks (Phase 5c)
Sits after "How its ratios moved". Descriptive only: it compares the bank with banks the FDIC groups with it and has **no measured result** ([[decisions/0020-peer-comparison-descriptive]]). Code: `src/canary/analyst/peers.py`. Specialty data: [[data-dictionary/fdic_specialty]].

**Which ratios are shown.** Of the 30 model ratios, those where the bank is in the national top or bottom 10% at the as-of quarter (the share of banks with a value at or below the bank's, or at or above it, is at most 10%; tied values are never unusual). At most 8 are shown, furthest from the national middle first (distance of the national percentile from 50, ties by plain name). Percentiles are true mid-rank: (count below + 0.5 x count equal) / n x 100.

**Peer group.** Same FDIC specialty group (at the as-of quarter) and size tier ("under $100 million", "$100 million to $1 billion", "$1 billion to $10 billion", "over $10 billion"; lower bound inclusive), at least 15 banks including the bank. If fewer, the same specialty at all sizes; if still fewer, no comparison. A ratio needs at least 15 peers with a value, or its reading is "too few peers with this figure".

**Table columns (code-rendered).**

| Column | Meaning |
|---|---|
| Ratio | Plain-English name. |
| Bank | The bank's value at the as-of quarter. |
| National percentile | Mid-rank percentile among all banks that quarter, with "(unusually high)" or "(unusually low)". |
| Peer median | Median among the peer group's banks with a value. |
| Peer percentile | Mid-rank percentile among peers (blank if too few). |
| Reading | One of: "unusually high among its peers too", "unusually high among its peers", "unusually low among its peers too", "unusually low among its peers", "typical for its peer group", "too few peers with this figure". "Too" means the same side as nationally. |

**Facts added to the sheet** (all as-of, none hindsight), with a `kind` the checker uses: per shown ratio, `peer_value`, `peer_nat_pct`, `peer_nat_dir` (text), `peer_pct` and `peer_median` (when enough peers) and `peer_reading` (text); sheet-level, `peer_specialty` (group code and name), `peer_tier`, `peer_basis` (how the group was formed), `peer_count` (label "Peers: banks in the peer group (including this bank)"), `peer_count_unusual`, `peer_count_unusual_peers`, `peer_count_shown`, `peer_cutoff` (display "10%", forms "10%", "10", "10 percent") and `peer_min` (display "15", forms "15", "fifteen").

**Code-written text.**
- "The FDIC's specialty group for this bank at {as_of}: {name}." For groups 8 and 9 only: "This is a general group: the FDIC did not record a lending specialty for this bank." Example: SVB at 2022-12-31 is "All Other Over 1 Billion".
- "Peers: {n} banks in the same specialty group and size tier ({tier})." or "Peers: {n} banks in the same specialty group (all sizes), because fewer than 15 shared its size tier." or "There are not enough comparable banks ({n} in its specialty group) for a reliable comparison, so none is shown."
- No specialty value that quarter: "The FDIC recorded no specialty group for this bank at {as_of}, so no peer comparison is shown."
- Nothing nationally unusual: "None of this bank's ratios were in the national top or bottom 10% at {as_of}." No Claude request is made when the section is code-only.
- Fixed sentence, last in the section: "This section only compares the bank with banks the FDIC groups with it; an unusual figure is not a prediction of failure, and the comparison has not been tested as a warning signal."

**Extra checker rules for this section only:** one ratio per sentence when a peer reading or percentile is cited; the opposite reading is rejected (a "typical" reading rules out contiguous "unusually high/low among its peers"; a high reading rules out "unusually low among its peers" and "typical for its peer group"; the national word may not contradict the national direction, except inside "among its peers" or "among peers"); prediction language and "risky"/"riskier" are rejected. The rules are blunt, paraphrases evade them ([[decisions/0020-peer-comparison-descriptive]]).

**Not in the committed notes yet.** Notes in `banks/` do not have this section until the showcase is re-run after Phase 5d.

## Real-estate concentration (2006 regulator thresholds) (Phase 5d)
Sits after "Compared with similar banks". **Written entirely by code**: no AI text, no AI request, and no facts added for Claude (it is always in the sheet's `code_only` list; the writer's user message does not mention it). It has **no measured result** ([[decisions/0021-cre-concentration-2006-thresholds]]). Code: `src/canary/analyst/concentration.py`. Data: [[data-dictionary/fdic_concentration]]. As-of only, never hindsight.

Lines, in order:
1. **Lead (fixed):** says this checks a different, more common way banks have failed than SVB's, applying the 2006 OCC, Federal Reserve and FDIC screens, which are not lending limits.
2. **Capital line:** before 2020-03-31, "total risk-based capital, as the 2006 guidance specifies"; from 2020-03-31, "Tier 1 capital plus the loan-loss allowance" (FDIC FIL-31-2020; Federal Reserve SR 20-8), noting the 2006 thresholds were not restated for it.
3. **Table** `| Test | Bank | Line | Meets it? |` with three rows:

| Test | Bank | Line | Meets it? |
|---|---|---|---|
| Construction and land loans ÷ capital | the bank's percentage | 100% or more | yes / no / n/a |
| Total commercial real estate loans ÷ capital | the bank's percentage | 300% or more | yes / no / n/a |
| Growth in commercial real estate loans over the prior 36 months | the bank's percentage | 50% or more | yes / no / n/a |

   The Bank cell and the last cell show "n/a" when the value can't be computed. Percentages have one decimal, thousands separators and a minus sign where needed (`1,234.5%`, `-12.0%`); dollars are not shown. Comparisons use unrounded values, so 299.99% displays as "300.0%" with "no".
4. **Summary:** one code-chosen sentence per line (construction first), or a combined form ("It did not cross either line." / "It crossed both lines: construction loans and total commercial real estate loans."). Each line is judged separately. Line 2 can read: crossed; did not cross; reached 300% but grew less than 50% (so did not cross); reached 300% but the growth part can't be checked; or can't be checked. Reasons: "the bank reported no capital figure for this quarter", "the bank's capital was zero or negative this quarter", "a loan figure the test needs is missing for this quarter", "there is no concentration data for this bank this quarter"; growth reasons: "there is no figure from 12 quarters earlier", "it reported no commercial real estate loans 12 quarters earlier".
5. **Definitions line (fixed)** for "total commercial real estate".
6. **Closing (fixed):** "Crossing a line is a supervisory screen, not a prediction: it has not been tested as a warning signal in Canary."

Example: SVB at 2022-12-31 (Tier 1 plus allowance): construction 2.4%, total CRE 13.7%, growth 953.0%; "It did not cross either line." The section has no "approaching" label. Memos exist only from 2016-03-31, so 2008-era failures are not covered.

**Not in the committed notes yet.** Notes in `banks/` do not have this section until the showcase is re-run.
