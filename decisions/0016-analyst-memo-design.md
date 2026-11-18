# 0016 — Analyst memo design: fact sheet, one Claude call, citation checker

**Date:** 2026-11-17
**Status:** Accepted (model picked by the owner after a live comparison)

## Decision
Each bank note is written in three steps:

1. **Code builds a fact sheet.** A list of facts with ids (`F1`, `F2`, ...): a label, a quarter, a value and the display forms a person could fairly write (0.9812 can be "98%", "98.1%" or "0.98"). Code: `src/canary/analyst/facts.py`.
2. **One Claude call writes the AI sections** as structured JSON: paragraphs of sentences, each sentence carrying the ids of the facts it uses. Code: `writer.py`.
3. **Code checks every sentence** (`checker.py`). If it passes, code renders the note (`render.py`). If not, there is one retry, and a memo that fails twice is **not saved**.

## Approaches considered (spec section 8)
- **A. Fact sheet + one AI call (chosen).** Code decides the facts, the AI only writes, code checks. The same bank and quarter always give the same inputs, it is cheap, and it can be tested without calling the API (tests use a fake client).
- **B. A fully tool-using agent writes each memo.** More flexible, but two runs on one bank could look at different facts, it is harder to test and it costs more. Rejected for memos. The owner wanted a real agent, so one fronts the writer instead: [[decisions/0017-analyst-agent-tool-runner]].
- **C. Templates, no AI.** Reliable, but it drops the AI analyst Phase 5 exists for.

## What the citation checker enforces
All in plain English. A rejected memo is never saved; the error list names the section, the sentence and the problem.

- **Every number and date must match a cited fact.** A number in a sentence has to equal one of the display forms of a fact *cited in that same sentence*. A sentence with a number and no cites is rejected, and so is a cited id that does not exist.
- **Dates in all their shapes.** ISO dates, "Q1 2023", "March 31, 2023", abbreviated months ("Sept."), "FY2022", and bare years. A bare year passes only if a cited fact's quarter is in that year. A lone capital "May" is ignored (it is usually the verb).
- **Spelled time spans.** "four quarters" or "a year" count as numbers and must match a cited fact (the lead time, or a label that says it). Other spelled counts ("five drivers") are not checked.
- **Units and signs.** `%`, `$`, `x`, "billion", "bps", `+`/`-` and ordinals ("26.8th") are part of the token, so a changed unit or sign does not match.
- **Hindsight is banned from the as-of sections.** Facts marked hindsight (anything after the as-of quarter) may not be cited in Summary, Warning signs or Understanding the score. Only the Outcome and "What happened next" sections may use them.
- **The post-hoc label.** A sentence that cites a post-hoc fact (for example the run-risk rank, [[decisions/0013-run-risk-check]]) must contain the exact words "post-hoc check, designed after the 2023 failures".
- **No probability-of-failure wording.** "chance/probability/likelihood of failing/failure" and "N% chance" are rejected, with one allowed exception: the exact disclaimer "not a probability of failure" (or "not the", or "likelihood", or "failing").
- **No hindsight words in as-of sections.** "failed", "collapsed", "was closed" and "was seized" are rejected there.
- **Digits that are part of a term name are skipped:** "Tier 1" (and "Tier 2"), "30-89 days", "90+ days" and its spoken forms "90 or more days" and "90 days or more". They come from the plain-English feature names in `labels.py`.

## The "as of" rule
A note is written *as of* one quarter and uses only data filed by then, so the Summary reads the way it would have on that date. For a failed bank that is its last report before failure. What actually happened goes in a labelled hindsight part, never in the as-of sections. Outcome comes from rules ([[decisions/0018-failures-after-test-window]]), not from which showcase group picked the bank.

## What code writes, not Claude
The outcome banner at the top (for example "Hindsight: failed 2023-03-10. Canary did not flag it."), the Score history table, the fixed sentence "The score ranks banks against each other; it is not a probability of failure, because the model was trained with extra weight on banks that failed.", the "What the model can't see" paragraph (chosen by code from Phase 4 findings, decisions 0013 to 0015) and the Sources list. Claude is told not to write them. Format: [[data-dictionary/bank_notes]].

## Score ranks, not a probability
The model was trained with `scale_pos_weight`, extra weight on the rare failing banks ([[decisions/0010-label-and-time-split]]), so its raw score is pushed up and is not a real chance of failing. The notes describe a bank by its national rank and percentile and say so. The percentile scale (0 to 100, higher is riskier) is itself a fact so Claude can mention it without the checker rejecting the "100".

## Model choice (live comparison, 2026-11-17)
Memos for SVB, Signature and First Republic were written with both models, after fixing a checker false rejection on "Tier 1":

| Model | Passed first try | Passed after one retry | Cost for 3 memos |
|---|---|---|---|
| Claude Opus 5.5 | 1 of 3 | 3 of 3 | $0.47 |
| Claude Sonnet 5.5 | 0 of 3 | 3 of 3 | $0.21 |

Opus summaries led with the decisive figures; Sonnet once paraphrased the required post-hoc label. **The owner picked Opus 5.5** (default `claude-opus-5-5`, effort `medium`, adaptive thinking). After the comparison, three changes cut retries: the percentile scale became a fact, "90 or more days" became an accepted spoken form, and the prompt asks for ordinals such as "the 26.8th percentile". Run it again with `python -m canary.analyst compare` ([[runbooks/analyst]]).

## Limits (honest list)
- The checker verifies **numbers and some phrasing**, not every claim. A sentence can be wrong in words while every number is right.
- One cited fact can be **relabelled as another cited fact in the same sentence** (say the bank's value described as the national median) and still pass, because both are cited.
- A **bare number that happens to equal a form of a cited fact** passes even if it means something else.
- Two attempts is a trade-off: more retries would cost more and raise the chance of the model arguing its way past a rule.
