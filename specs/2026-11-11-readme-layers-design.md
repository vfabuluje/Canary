# README Layers: Short Design

**Date:** 2026-11-11
**Status:** Approved by Victor 2026-11-11

## Intent
The README reads as too technical: a reader has trouble seeing what the project is about. It must work for two readers at once: a tech recruiter at a bank who skims, and a bank data or ML engineer who reads closely. The answer is one README layered from plain to deep, not a cut-down page.

## Goals
- The top section (about one screen) says what Canary is, the SVB story, what was found, why the three 2023 banks were missed, what's next and what it's built with, in plain English with the real numbers.
- Every technical term is explained in plain words where it first appears (AUC, recall, false-alarm rate, HTM, uninsured deposits, watchlist).
- A clear divider, then the technical detail for engineers, kept largely intact.

## Non-goals / anti-goals
- No numbers lost or changed; every number stays traceable to `metrics.json`, `case_studies.csv` or the data.
- No overclaiming in the friendlier wording (e.g. "caught 21 of 29" keeps its "at least once, 1-4 quarters before" meaning).
- "Research tool, not financial advice" stays near the top.
- Nothing personal in the committed files.
- No Phase 4 results (Phase 4 is paused).

## Approaches (decided: 1, with more detail kept)
1. **Layered README, longest tables moved out (chosen, adjusted).** Plain top, technical detail below. Victor asked for more detail to stay, so only the case-study signal strings and the long contribution paragraphs move to a new `RESULTS.md`; compact per-bank case-study tables stay in the README.
2. Layered README, nothing moved: complete, but the 25 rows of signal strings dominate the page.
3. Short README, everything technical in `RESULTS.md`: rejected, Victor wants the engineer detail in the README.

## Design
- **Top, plain:** What it is (3 sentences). The SVB story plus the existing SVB numbers table. What I found: 21 of 29 caught, usually about a year early; AUC 0.902 vs 0.774 with a one-line gloss; ~98% false alarms and why that's expected (2% of ~5,200 banks flagged each quarter vs ~3 failures a year; a flagged bank is ~32x likelier to fail soon than a random one); missed SVB, Signature, First Republic. Why it missed them: the model learned from 2001-2014 failures; SVB's HTM bond loss was ~98% of equity while the 99th percentile among training failures was ~17%; cheap funding, strong capital and a big bond book looked safe. What's next (Phase 4 in one or two lines). Built with (one line).
- **Technical detail:** results table and "Reading the numbers" (tightened, all facts kept); case studies as one compact table per bank (report, quarters before failure, percentile, rank / banks, flagged); a shortened "what was caught and why" that links to `RESULTS.md`; limitations, architecture, scale, run it yourself, roadmap, reference, largely unchanged.
- **`RESULTS.md`:** the full case-study tables with top signals, the full SVB contribution analysis and the training-data evidence, as they are in today's README.
- **Left to the builder:** exact wording, section titles, order within the technical part.
