# bank_notes (Phase 5a risk-analyst notes)

One Markdown note per bank in `banks/`, written by `python -m canary.analyst memo` / `showcase` / `ask`. They are **notes in the vault, not warehouse tables**. Design: [[specs/2026-11-17-phase5a-risk-analyst-design]]. Decisions: [[decisions/0016-analyst-memo-design]], [[decisions/0018-failures-after-test-window]], [[decisions/0019-ratio-trends-descriptive]]. Runbook: [[runbooks/analyst]].

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
| `writer_model` | string | The model that actually served the request (can differ from the one asked for if a fallback was used). |
| `checked` | boolean | Always `true`; unchecked notes are never saved. |

## Outcome values
- `caught`: failed, and Canary flagged it 1 to 4 quarters before failure (Phase 3 lead-time rule).
- `missed`: failed, and no flag in that window.
- `false_alarm`: not failed, but flagged at as-of (an earlier quarter than the latest).
- `quiet`: not failed, not flagged.
- `open_watchlist`: flagged at the latest quarter; outcome not yet known.

## Sections, in order

| Section | Who writes it | Time window |
|---|---|---|
| Banner (first line under the title) | Code | Hindsight, labelled |
| Summary | Claude | As-of only |
| Warning signs in the data | Claude | As-of only, with the national median for that quarter |
| Understanding the score | Claude, then code adds the fixed sentence "The score ranks banks against each other; it is not a probability of failure..." and **What the model can't see** | As-of only |
| Score history | Code (table: quarter, rank, of, watchlist; first flag marked) | The 8 quarters up to as-of |
| How its ratios moved (key `trends`, added in 5b) | Claude (one or two paragraphs), then a code table and the fixed sentence; or one code-written line | As-of only |
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
