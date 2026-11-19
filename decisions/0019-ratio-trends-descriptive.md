# 0019 — Ratio trends: descriptive only, with a fixed range rule

**Date:** 2026-11-18
**Status:** Accepted (design approved by the owner; built in Phase 5b)

## Decision
Every bank note gets a section, **"How its ratios moved"**, that shows which of the bank's own ratios are outside the range they held over the bank's own recent history, how fast they moved, and what the model did with that same ratio. It is **descriptive only**. It makes no claim that a ratio outside its range predicts failure, and there is **no measured result** for it (no recall, catches, AUC, lead time or false-alarm rate) in the notes, the README, RESULTS or anywhere else.

Code: `src/canary/analyst/trends.py` (rule and section), `checker.py` (three extra rules). Format: [[data-dictionary/bank_notes]]. Design: [[specs/2026-11-18-phase5b-trend-design]].

## Why descriptive only
The point of the section is a contrast: **what a ratio did vs. how much the model weighted it**. For Silicon Valley Bank, losses on bonds held to maturity (HTM) as a share of equity ranged from -11.7% to 6.6% over the 12 quarters to 2021-12-31, then reached 48.4% at 2022-03-31 (+41.8 percentage points in one quarter). That same feature's contribution to the score stayed slightly negative. The note puts the two side by side.

A threshold or window chosen after looking at SVB's numbers and then scored on 2016-2024 would be a worse version of the hindsight problem Phase 4 avoided ([[decisions/0013-run-risk-check]]). So the section is not a signal and is not scored.

## The fixed range rule
Set by plain convention before any further bank was looked at. **Do not change any of these after seeing results.** Changing one needs a new decision record that says why and states plainly that it was changed after seeing results.

- **Which ratios (`TREND_RATIOS`):** all 31 model features except `log_total_assets`, so 30. Size moves are not a ratio trend, and asset growth is already covered by `asset_growth_4q`.
- **Year-to-date ratios (`YTD_RATIOS`):** `return_on_assets`, `return_on_equity`, `net_interest_margin`, `efficiency_ratio`, `net_charge_offs_to_loans_ann`, `provision_to_assets_ann`, `interest_expense_to_assets_ann`. FDIC builds these from income that accumulates within the year, so a Q1 value is not comparable with a Q4 value. They are compared with the same quarter of earlier years. `efficiency_ratio` is treated this way because FDIC computes it from year-to-date income.
- **Point-in-time window (all other ratios):** the 12 calendar quarters before the as-of quarter (as-of excluded). At least 8 must have a value, or the ratio is not checked.
- **Year-to-date window:** the same calendar quarter in each of the 3 prior years. At least 2 must have a value.
- **Outside the range:** the as-of value is below the window minimum or above the maximum. Equal to a bound is inside.
- **Excess and ordering:** excess is the distance beyond the bound in percentage points. Ratios are ordered by excess divided by the larger of the range width and 1.0 pp (the floor stops a flat ratio, such as 0.0% for 12 quarters then 0.3%, from outranking a large move on a wide range). Ties break by plain name. **At most 6 are shown**; the count outside is stated.
- **Changes:** 1 quarter and 4 quarters for point-in-time ratios; 4 quarters only for year-to-date ratios. In percentage points. Ratios stored as percent are already percentage points; ratios stored as fractions are multiplied by 100.
- **Direction label** from the ratio's own contribution to the score (log-odds): +0.05 or more is "pushed the score up"; -0.05 or less is "pushed the score down"; anything between is "little effect on the score".
- **Rank phrase** (percentile now against the same quarter a year earlier): higher by more than 1.0 gives "the model rated it riskier than a year earlier"; lower by more than 1.0 gives "the model rated it safer than a year earlier"; otherwise "about the same as a year earlier". With no year-earlier score the phrase is left out.
- **Nothing outside, or too little history:** one code-written line ("None of this bank's ratios were outside their own prior range at {as_of}." or "This bank has too little history before {as_of} to compare its ratios with its own prior range.") plus the fixed sentence, and no AI request is made for the section.

Contributions and ranks are labelled as different quantities: the ratio is a level, the contribution is the model's weight in log-odds units. The fixed sentence, code-rendered at the end of the section, reads: "This section only describes how the bank's own ratios moved against its own history. The range rule was set by convention and has not been tested as a warning signal, so a ratio outside its range is not a prediction of failure."

## No tuning
The window length, the history minimums, the ordering, the cap of 6 and the direction cut-off are not adjusted to make a known failure stand out. That includes SVB.

## Known consequence: SVB's last-report note does not list the HTM ratio
The rule flags a ratio when it **breaks out** of its own prior range, not while it stays high. SVB's showcase note is as of its last report, 2022-12-31. By then the 12-quarter window already contains 48.4%, 73% and 105%, so HTM loss to equity (98.1%) is inside its range (-11.7% to 105.3%) and is not listed. The contrast shows in a note as of 2022-03-31, the quarter the ratio broke out. This was seen during spec review and **kept on purpose**: widening or shortening the window to make SVB appear would be tuning after seeing the answer. Two data tests pin both cases.

## One change from the design (recorded)
The spec's section 6.2 listed a per-ratio "window type" fact and year-earlier rank and banks-ranked facts. The build uses two sheet-level comparison-window facts (the 12-quarter and the 3-year windows), and one year-earlier **percentile** fact, because the table already shows the window per ratio and the rank phrase is defined by percentile. The spec was updated to match.

## What the checker enforces for this section
Three narrow rules, applied only to sentences in this section, feeding the existing single retry ([[decisions/0016-analyst-memo-design]]):

1. **Pairing.** A sentence that cites a ratio's contribution must also cite that ratio's own value or range, and must not cite another ratio's figures.
2. **Direction words.** A sentence about a ratio must not use a phrase opposite to the code's label for it (for example "pushed the score up" when the label is "pushed the score down").
3. **No prediction language.** "predict", "forecast", "warned/warning", "early warning", "would have caught/flagged", "should have caught/flagged", "foreshadow" and "signs of failure" are rejected anywhere in the section.

A change must be written in percentage points ("+41.8 pp"), never as "41.8%", so a change cannot be read as a level.

## Limits (honest list)
- **The rules are blunt regexes.** Paraphrases evade them: "pushed up the score" or "pulled the score up" gets past the direction rule; implied prediction without a banned word ("this is the kind of move that precedes trouble") gets past rule 3.
- **Rule 3 over-rejects.** It also rejects negations such as "this is not a prediction", which can waste the one retry.
- **"Little effect on the score" only rejects up-words.** A sentence that implies a downward push for such a ratio is not caught.
- As in 0016, the checker verifies numbers and some phrasing, not every claim. The prompt is the first line of defence and the checker the second.
- The range rule is a convention. It is not evidence that a ratio outside its range matters.

## Possible later version
A measured trend signal could be built after launch, as a separate piece of work: set the rule using **2001-2015 only**, then test it **once** on 2016-2024. Nothing in 5b is a step toward claiming a result.
