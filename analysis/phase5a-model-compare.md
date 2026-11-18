# Phase 5a: Opus 5.5 vs Sonnet 5.5 for the risk analyst

**Date:** 2026-11-17 · **Decision:** [[decisions/0016-analyst-memo-design]] · **Source:** `data/analyst/compare/compare.json` (local, not committed) · **Research tool, not financial advice.**

The same three banks (SVB, Signature, First Republic) were written up by both models through the normal API, then checked by the citation checker. "First try" means the memo passed the checker with no retry; "after retry" means it passed after one retry with the checker's complaints fed back.

## Results
| Run | Model | Passed first try | Passed after retry | Tokens in / out | Cost |
|---|---|---|---|---|---|
| 2 (kept) | Claude Opus 5.5 | 1 of 3 | 3 of 3 | 36,428 / 15,966 | $0.47 |
| 2 (kept) | Claude Sonnet 5.5 | 0 of 3 | 3 of 3 | 45,154 / 12,224 | $0.21 |
| 1 (discarded) | both | n/a | n/a | n/a | $0.80 |

**Why run 1 was discarded.** Every rejection in run 1 came from one checker bug: the "1" in "Tier 1" was read as an unsupported number. That penalised both models equally for something that was not their fault, so I fixed the checker and re-ran. Run 2 is the fair comparison. The $0.80 for run 1 is still part of the Claude API spend.

## Why memos failed the first try (run 2)
From `first_errors` in `compare.json`, in plain English:
- **The number 100.** Memos said the percentile scale runs to "100" (higher is riskier), but 100 was not one of the cited facts. Most common failure, for both models.
- **The number 90.** An Opus First Republic memo said loans "90 or more days late"; the checker read 90 as an unsupported number.
- **A figure not in the cited facts.** Sonnet quoted deposit shrinkage of 8.4% (SVB) and 16.5% (Signature) while citing facts that did not contain those values.
- **A missing label.** Sonnet's Signature memo discussed the post-hoc what-if checks and wrote "designed after the 2023 failures" in its own words, but did not include the exact required label "post-hoc check, designed after the 2023 failures". It also tripped on "2023" not being in the cited facts.

## Observations
- **Opus leads with the decisive figures.** Its SVB summary: "Its loan book looked clean, but uninsured deposits (money above the government insurance limit) made up 86.4% of deposits against a national median of 25.5%." ([Opus SVB note](phase5a-model-compare/claude-opus-5-5/Silicon%20Valley%20Bank%20(24735).md))
- **Sonnet's summary is vaguer.** Its SVB summary: "The bank's data showed a mix of strong capital ratios and unusual features in its funding and bond holdings." ([Sonnet SVB note](phase5a-model-compare/claude-sonnet-5-5/Silicon%20Valley%20Bank%20(24735).md)) It does not name the figures a reader needs.
- **Sonnet paraphrased the required post-hoc label once** (Signature), which the checker correctly rejected.
- **Cost.** Sonnet was cheaper ($0.21 vs $0.47 for three memos) but used more input tokens, mostly from its extra retries. Neither passed all three on the first try.

All six notes: [Opus: SVB](phase5a-model-compare/claude-opus-5-5/Silicon%20Valley%20Bank%20(24735).md), [Opus: Signature](phase5a-model-compare/claude-opus-5-5/Signature%20Bank%20(57053).md), [Opus: First Republic](phase5a-model-compare/claude-opus-5-5/First%20Republic%20Bank%20(59017).md), [Sonnet: SVB](phase5a-model-compare/claude-sonnet-5-5/Silicon%20Valley%20Bank%20(24735).md), [Sonnet: Signature](phase5a-model-compare/claude-sonnet-5-5/Signature%20Bank%20(57053).md), [Sonnet: First Republic](phase5a-model-compare/claude-sonnet-5-5/First%20Republic%20Bank%20(59017).md).

## Decision
**The owner chose Opus 5.5.** Its memos put the decisive numbers up front and it followed the labelling rule. The extra cost on three memos (about 26 cents) was judged worth it for readability. Recorded in [[decisions/0016-analyst-memo-design]].

## Fixes that followed (to cut retries)
1. The percentile scale (0 to 100, higher is riskier) became a fact the memo can cite, so "100" is no longer rejected.
2. "90 or more days" became an accepted spoken form of the 90-day past-due measure.
3. The prompt now asks for ordinals such as "the 26.8th percentile" instead of "26.8% percentile". (Opus and Sonnet both wrote it the second way.)

In the later 61-note showcase, 43 passed first try and 18 after one retry; none failed ([[decisions/0016-analyst-memo-design]], [[runbooks/analyst]]).
