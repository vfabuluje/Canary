# bank_notes (Phase 5a risk-analyst notes)

One Markdown note per bank in `banks/`, written by `python -m canary.analyst memo` / `showcase` / `ask`. They are **notes in the vault, not warehouse tables**. Design: [[specs/2026-11-17-phase5a-risk-analyst-design]]. Decisions: [[decisions/0016-analyst-memo-design]], [[decisions/0018-failures-after-test-window]]. Runbook: [[runbooks/analyst]].

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
