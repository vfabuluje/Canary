# Phase 5b Spec: Ratio Trends (descriptive)

**Date:** 2026-11-18
**Status:** Built (Phase 5b, 2026-11-18). Design approved by Victor; see [[decisions/0019-ratio-trends-descriptive]] for the rule. Section 6.2 below was updated to match the build.
**Phase:** 5b of Phase 5 (5a risk analyst → **5b trends** → 5c peer comparison → 5d concentration risk).
Builds on [[specs/2026-11-17-phase5a-risk-analyst-design]] §7 (section registry).

## 1. Intent: why this exists

A 5a memo shows a bank at one quarter plus an 8-quarter rank table. It does not show **which
of the bank's own ratios are moving, how fast, and whether they have left the bank's normal
range**. Phase 5b adds one section to every memo that does that.

The point of the section is a contrast: **what a ratio actually did vs. how much the model
weighted it.** SVB is the example. Its losses on bonds held to maturity (HTM) as a share of equity
ranged from -11.7% to 6.6% over the 12 quarters to 2021-12-31, then reached 48.4% at 2022-03-31
(+41.8 percentage points in one quarter), far outside its own range. They kept rising to 73% and
105%, while that feature's contribution to the score stayed slightly negative (about -0.16 at
2022-09-30 and 2022-12-31) and SVB's rank fell. The memo should put the ratio's path and the
model's weight for **that same ratio** side by side.

**Known consequence of the fixed rule (seen before building, kept on purpose; Victor 2026-11-18).**
The rule flags a ratio when it *breaks out* of its own prior range, not while it stays high. SVB's
memo is as of its last report (2022-12-31); by then the 12-quarter window already contains 48%, 73%
and 105%, so the HTM ratio (98.1%) is inside its range and SVB's showcase note will **not** list it.
That is the honest output of a rule set in advance. Changing the window to make SVB appear would be
tuning after seeing results (§4), so the rule stays and decision 0019 records this.

Readers are the same as 5a: a recruiter or interviewer reading a note, and Victor explaining it.

## 2. Goals
- G1. A **trend specialist** module that registers with 5a's section registry
  (`canary.analyst.sections.register`) and adds facts plus sections, so the existing writer,
  checker and renderer cover it with no special path.
- G2. For each memo, code finds the ratios **outside the bank's own prior range** at the as-of
  quarter (rules in §5), with value, range, speed of change and the model's contribution for that
  ratio at as-of.
- G3. A **code-rendered table** of those ratios, then an **AI-written paragraph** that describes
  them and states the contrast (§6).
- G4. A **fixed, code-written sentence** saying the section is descriptive and not a tested
  warning signal (§6.3).
- G5. Tests for all non-AI code with no network (fake Claude, as in 5a).
- G6. Docs: decision record 0019, data dictionary (`bank_notes.md`), runbook (`runbooks/analyst.md`),
  glossary terms, README and RESULTS mention, roadmap and daily log.
- G7. After the build and with Victor's OK on cost, re-run the 5a showcase so the 61 notes gain
  the section.

## 3. Non-goals
- **Any measured result.** No "flagged X of Y failures early", no recall, AUC, lead time or false
  alarm rate for trend flags, in the notes, README, RESULTS or anywhere else.
- Changing the Phase 3 model or anything in `data/model/`.
- Score or rank trajectory (the 5a score history table covers it).
- Comparisons with other banks (that is 5c) or the national median (5a's "Warning signs" does it).
- New data, FDIC fields or AWS use. AWS cost for 5b is $0.
- The 5a follow-ups (renaming "(first flag)", dry-run constants, checker residuals). Separate work.

## 4. Anti-goals (a failure even if it "works")
- **Tuning the range rule to make SVB (or any known failure) stand out.** The rule in §5 is fixed by
  plain convention in this spec, before any further bank is looked at. The builder must not change
  the window, history minimums or ordering after seeing results. Changing them needs a new decision
  record that says why and that results had been seen.
- **Any sentence implying a trend flag predicts failure** ("this should have been a warning",
  "would have caught"). The section describes; it does not forecast.
- **Mixing up the two numbers.** A ratio's value (e.g. 105% of equity) and the model's
  contribution for that ratio (e.g. -0.16 in log-odds units) are different quantities. They are
  always labeled, never merged, and a contribution is only ever paired with its own ratio (not,
  for example, HTM's path with the AFS contribution).
- **Wrong direction words.** "The model's score did not rise" must never appear where it is false.
  Direction comes from code (§6.1), not from Claude's judgment.
- **Hindsight.** The section is as-of only: no data after the as-of quarter.

## 5. The range rule (fixed)

### 5.1 Which ratios
All 31 model features except `log_total_assets` (30 ratios), using the plain names in
`canary.analyst.labels.PLAIN_NAMES` and the units in `labels.UNIT`.

They split into two groups:
- **Year-to-date ratios** (built from year-to-date income, so they reset each January and drift
  through the year): `return_on_assets`, `return_on_equity`, `net_interest_margin`,
  `efficiency_ratio`, `net_charge_offs_to_loans_ann`, `provision_to_assets_ann`,
  `interest_expense_to_assets_ann`.
- **Point-in-time ratios**: the other 23.

### 5.2 The bank's own prior range
- **Point-in-time ratios:** the lowest and highest value of that ratio for the bank in the **12
  calendar quarters before** the as-of quarter (as-of excluded). At least **8** of those 12 must have
  a value; otherwise the ratio is "too little history".
- **Year-to-date ratios:** the lowest and highest value in the **same calendar quarter of the 3 prior
  years** (e.g. as-of 2022-09-30 → 2021-09-30, 2020-09-30, 2019-09-30). At least **2** of the 3 must
  have a value; otherwise "too little history".
- Missing values (NaN) are skipped, not treated as zero. Quarters are calendar quarters, so a bank
  that skipped reports has fewer values, not an older window.
- Features come from `data/features/fct_bank_features.parquet`, so history before 2016 (back to
  2001) is available and as-of dates from 2016-03-31 have full windows.

### 5.3 Outside the range
A ratio is **outside its range** when its as-of value is below the minimum or above the maximum.
- **Excess** = distance past the nearest bound, in the ratio's display unit (percentage points for
  both percent and fraction ratios).
- **Ordering:** by excess ÷ range width, with the width floored at 1 percentage point (so a ratio
  that was flat at 0.0% and moves to 0.3% doesn't outrank a large move on a wide range). Ties by
  plain name.
- **Shown:** at most **6** ratios outside the range, in that order. The count of all ratios outside the
  range is a fact (so "8 ratios were outside their range; the 6 furthest are shown" is citable).

### 5.4 Speed of change
- Point-in-time ratios: change over **1 quarter** (as-of minus the quarter before) and over
  **4 quarters** (as-of minus the same quarter a year earlier), in percentage points.
- Year-to-date ratios: **4-quarter change only** (a 1-quarter change mostly reflects the calendar).
- A change is omitted when either end is missing.

### 5.5 The model's weight for the same ratio
- The contribution of that ratio's feature to the score at as-of, from the same
  `canary.replay.probe.contribution_matrix` call 5a uses for drivers (log-odds units; positive
  pushes the score up, toward riskier).
- **Direction label** (code-chosen, from the contribution):
  - contribution ≥ +0.05 → "pushed the score up"
  - contribution ≤ -0.05 → "pushed the score down"
  - otherwise → "little effect on the score"
  The ±0.05 cut-off is a display rule for wording only, fixed here.

### 5.6 Rank change (the overall model response)
- Rank and banks-ranked at as-of (5a facts already) and at the **same quarter a year earlier**, from
  `data/analyst/scores.parquet`. Scores only exist from 2016-03-31, so for as-of dates in 2016 (or a
  bank with no report a year earlier) the comparison is omitted and the section says so.
- Code-chosen phrase, by **percentile** (not raw rank, because the number of banks changes each
  quarter): percentile higher than a year earlier → "the model rated it riskier than a year
  earlier"; lower → "the model rated it safer than a year earlier"; within 1 percentile point →
  "about the same as a year earlier".

## 6. What gets written

### 6.1 Section position and parts
The specialist adds one section, **"How its ratios moved"**, in the 5a specialist slot (after
"Score history", before the outcome section). `window = "as_of"`. Parts, in order:

1. **AI paragraph(s)** (1-2 paragraphs). Must, for each shown ratio it discusses: name it, give its
   as-of value and its prior range, and the model's contribution with the code-provided direction
   label. Must state the overall model response using the code-chosen rank phrase (§5.6). Where a
   ratio is outside its range and its direction label is "pushed the score down" or "little effect",
   the paragraph states that contrast plainly, e.g. (SVB as of 2022-03-31) "HTM losses rose to 48.4%
   of equity, far above this bank's prior range of -11.7% to 6.6%, yet the model's weight on that
   ratio was <its contribution at that quarter>, <its direction label>." Every number cites fact ids; the 5a checker applies, plus the trend rules in §6.5.
2. **Code-rendered table**: Ratio · As-of value · Prior range · Window · Change 1q · Change 4q ·
   Model contribution · Direction. "Window" says "prior 12 quarters" or "same quarter, prior 3
   years". Missing changes show "n/a".
3. **Fixed sentence** (code, not AI; §6.3).

When no ratio is outside its range, the section is one code-written line: "None of this bank's
ratios were outside their own prior range at <as-of>." (plus §6.3), and no AI paragraph is
requested. When the bank has too little history for every ratio, one line says so.

The two parts that need code rendering mean the registry gains, if needed, the ability for a
specialist section to have a code-rendered body after its AI text. How is left to the builder
(§10), as long as `sections.Section` and the renderer stay the single path.

### 6.2 Facts added to the sheet
Per shown ratio (all `hindsight=False`, as-of only, `source` naming the parquet column):
value at as-of; range min; range max; 1q change; 4q change (year-to-date ratios have 4q only);
contribution; direction label (text fact, no number). Sheet-level: count of ratios outside the
range; count of ratios checked; two comparison-window facts (the 12-quarter window and the
3-year year-to-date window); the year-earlier percentile; the rank-phrase text fact (both omitted
without a year-earlier score). The window type per ratio shows in the code-rendered table, not as
a fact, and the rank phrase is by percentile, so there are no year-earlier rank or banks-ranked
facts (decision 0019).
Display forms reuse `labels.display_forms` for values and bounds. Changes get forms in percentage
points ("+28.0 pp", "28.0 percentage points", "28 percentage points", and the plain
"28.0%"-style form is **not** allowed for a change, so a change can't be read as a level).
Contributions get forms like 5a drivers ("-0.16", "-0.157").

### 6.3 The fixed sentence
"This section only describes how the bank's own ratios moved against its own history. The range
rule was set by convention and has not been tested as a warning signal, so a ratio outside its
range is not a prediction of failure."

### 6.4 Prompt instructions (section spec)
The section instructions tell Claude: use only the facts given; always pair a ratio's value with
its **own** contribution; use the given direction label and rank phrase word for word in meaning
(no stronger or weaker claim); never say a trend predicted, warned of, or would have caught a
failure; do not mention the outcome.

### 6.5 Checker additions (trend facts only)
The 5a checker only matches numbers to the facts a sentence cites, so it can't enforce the §4
anti-goals on its own. Three narrow rules are added, applied only to sentences in the trend
section, with their errors fed into the existing single retry:
1. **Pairing.** Each trend fact carries the feature it belongs to. A sentence that cites a
   contribution fact must also cite at least one value/range fact of the **same** feature, and must
   not cite a contribution fact of a different feature than the value facts it cites.
2. **Direction words.** A sentence that cites a contribution fact must not contain the opposite
   direction phrase from that fact's code label (e.g. "pushed the score up" / "raised the score" when
   the label is "pushed the score down"). The phrase list is short and fixed in code.
3. **No prediction language.** A fixed list of banned phrases ("predict", "warned", "warning sign of
   failure", "would have caught", "should have flagged", "early warning", and close variants) is
   rejected anywhere in the trend section.
These are blunt string rules, not understanding; the prompt (§6.4) remains the first line, and
decision 0019 lists what they can't catch.

## 7. Data and code layout
- New module `src/canary/analyst/trends.py`: pure functions for §5 (range, outside, ordering,
  speed, direction) on a single bank's feature history, plus the specialist class that
  `build_facts(ctx, sheet)` and registers its section.
- Registration happens where 5a's writer imports specialists, so `memo`, `showcase` and `ask`'s
  `write_memo` all get the section.
- No new data files. Nothing written to `data/model/`.

## 8. Testing
- Unit tests on small synthetic histories for: point-in-time window and 8-of-12 minimum;
  year-to-date same-quarter window and 2-of-3 minimum; NaN skipping; gaps in reporting; excess and
  ordering with the 1 pp width floor; cap at 6 and the total count; 1q/4q changes and year-to-date
  4q-only; direction cut-offs at ±0.05; rank phrase by percentile, and omission before 2016.
- Fact tests: change forms in "pp" accepted, a change written as "28%" rejected by the checker.
- Checker tests for §6.5: HTM value cited with AFS contribution rejected; opposite direction phrase
  rejected; each banned prediction phrase rejected; a correct contrast sentence accepted.
- Writer/render tests with the fake Claude: section placed after score history; table and fixed
  sentence rendered by code; the "none outside range" path makes no AI request for the section.
- Data tests (like 5a's), read from real files. They check the code, not the rule; the rule is not
  changed based on them:
  - SVB 24735 as of **2022-03-31**: HTM loss to equity is outside its range, value 48.4%, range
    -11.7% to 6.6%, 1q change +41.8 pp, 4q change +48.6 pp, with its contribution.
  - SVB 24735 as of **2022-12-31**: HTM loss to equity is **inside** its range (98.1% within -11.7% to
    105.3%), so it is not listed. This pins the known consequence in §1.

## 9. Approaches considered
- **A. Specialist in 5a's registry: code computes trend facts, Claude writes, checker verifies
  (chosen).** Same discipline as 5a, one call per memo, testable without the API.
- **B. Code-only table, no AI text (rejected).** Reliable, but drops the analyst prose that states
  the contrast, which is the point of the section.
- **C. Tool-using agent explores the history (rejected).** Two runs could look at different ratios;
  harder to test; the same reason 5a rejected it for memos.
- **Measured trend signal (rejected for 5b, possible later).** A threshold chosen after seeing SVB's
  numbers and then scored on 2016-2024 is a worse version of the hindsight problem Phase 4 avoided.
  A real version would set its rule only on 2001-2015 and test once on 2016-2024, as a separate
  post-launch build.

## 10. Decided by Victor
- Ratio-level trajectory per bank, not score/rank trajectory.
- Descriptive only; no measured or evaluated result; not an extension toward one.
- Year-to-date ratios compared with the same quarter in prior years.
- The section states the ratio's value and the model's contribution side by side, labeled as
  different quantities; the contrast is the point.
- A measured trend signal, if ever, is a separate post-launch build calibrated on 2001-2015.
- Keep the fixed range rule even though it leaves SVB's last-report note without the HTM contrast
  (§1); the data test moves to 2022-03-31 (§8).

## 11. Calls made by Claude (Victor to check)
- Range windows and minimums (12 prior quarters, need 8; same quarter of 3 prior years, need 2).
- At most 6 ratios shown, ordered by excess ÷ range width with a 1 pp floor.
- `log_total_assets` excluded (size moves aren't a ratio trend; asset growth is covered by
  `asset_growth_4q`).
- `efficiency_ratio` treated as year-to-date (FDIC computes it from year-to-date income).
- Direction cut-off ±0.05 log-odds for wording.
- Rank comparison by percentile vs. the same quarter a year earlier.
- Section title "How its ratios moved"; code-rendered table plus fixed sentence.
- Three narrow checker rules for the trend section (§6.5: pairing, direction words, no prediction
  language), so the anti-goals aren't left to the prompt alone.
- Re-run the showcase after the build (about $4-5 at 5a's measured cost plus the longer prompt),
  only after Victor approves the cost estimate shown by the dry run.
- Decision record 0019 covers: descriptive only and why, the fixed range rule, the
  "no tuning after seeing results" rule, and the SVB consequence seen during review and kept.

## 12. Left to the builder
- How the registry supports a code-rendered table after AI text (§6.1).
- Exact fact labels, prompt wording and table formatting, within §5-§6.
- Whether the trend computation for a bank is cached (not needed for correctness).
