# 0018 — Failures after the test window

**Date:** 2026-11-17
**Status:** Accepted (owner's choice)

## Decision
The reported test is 2016-2024 ([[decisions/0010-label-and-time-split]]). The failure list now runs past it. Four banks failed after 2025-12-31 (certs 25796, 57488, 28722, 25744). Their notes get the **real caught or missed outcome**, tagged "After the test window: not part of the reported 2016-2024 results." in the banner, the front matter (`after_test_window: true`) and the Outcome section. The README headline numbers do **not** change; the README gets a separate short line on these banks as an extra out-of-sample check.

## The rule (code: `src/canary/analyst/outcome.py`)
- `AFTER_WINDOW_START = 2025-12-31`. A failure *after* that date is "after the test window". Its caught/missed verdict uses **all scored rows** (the model never trained on these quarters), by the same lead-time rule as Phase 3 (earliest flag 1-4 quarters before failure).
- A failure **on or before 2025-12-31** belongs to the reported test. Its verdict uses only rows up to `TEST_END` (2024-12-31), exactly what `metrics.json` scored, so the note and the metrics always agree.
- Example: cert 5520 (Santa Anna National Bank) failed in 2025. It is a reported **miss**, because its first flag came at the 2025-03-31 report, after the window. The note says "missed", and a hindsight fact says the later flag is not counted. That flag is kept in `late_flag`.

## Why
Hiding the later failures would waste a free out-of-sample check, and counting them in the headline would change numbers that were fixed before results were seen. Tagging keeps both honest. Notes and metrics cannot disagree, which was the main risk of mixing windows.

## Consequence
Outcome comes from these rules, not from the showcase group that picked the bank (two banks in the false-alarm list, 25796 and 57488, failed in 2026, so they are "caught", tagged after the test window). See [[data-dictionary/bank_notes]].
