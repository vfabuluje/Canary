# 0011 — The watchlist flag and the metrics

**Date:** 2026-11-11
**Status:** Accepted

## Decision
**The flag is a 2% watchlist.** Each quarter, the model scores every bank, and the top 2% by score are flagged. This is how a supervisor works: a limited number of examiners can look closely at only a few banks per quarter, so the question is "who goes on the list this quarter?", not "is this bank above 50%?".

**Why not a probability cut-off.** Failures are rare, and the training years (2001-2014) include the 2009-2012 crisis, when many banks failed. A model trained on that base rate learns that failure is common, so its raw probabilities run high in calm test years. A fixed cut-off such as 0.5 would then behave very differently from year to year. A fixed share of banks per quarter stays meaningful in any year and keeps the number of false alarms predictable.

**The ceil and tie rule.**
- The number flagged per quarter is `k = ceil(round(n * 0.02, 9))`, where `n` is the number of banks that quarter. Rounding up means even a tiny quarter flags at least one bank. The `round(..., 9)` guards against float noise: `50 * 0.06` is stored as `3.0000000000000004`, and a plain ceil would wrongly give 4.
- Banks are sorted by score (highest first), then by `cert` ascending, and the first `k` are flagged. Ties therefore always resolve the same way and results are reproducible.
- A missing (NaN) score ranks lowest, so it is never flagged ahead of a bank with a real score.

**The metrics, one plain sentence each.** All are computed on test rows only (report dates 2016-03-31 to 2024-12-31).
- **AUC:** the chance that a randomly chosen row with `label = 1` gets a higher score than a randomly chosen row with `label = 0` (0.5 is a coin flip, 1.0 is perfect); it needs no cut-off.
- **Bank-level recall:** of the banks that failed and have at least one test row 1 to 4 quarters before failure (the eligible banks), the share flagged at least once on such a row. A bank counts once however many of its rows are flagged. The denominator (eligible banks) is always reported next to the share, so "2 of 3" is never hidden behind a percentage. A bank with no 1-4 quarter row in the test set (for example, its warning window falls in the dropped 2015 gap year) is not in the denominator.
- **Recall at 2+ quarters:** the same, but only rows 2 to 4 quarters before failure count, so it asks whether the bank was flagged with real notice and not only in its last quarter.
- **Lead time:** for each caught bank, the largest `quarters_until_failure` among its flagged rows, i.e. how early the first flag appeared (1 to 4 quarters).
- **False-alarm rate:** flagged rows that were not within 4 quarters of failing, divided by all flagged rows (that is, 1 minus precision).
- **False-alarm banks:** the number of distinct flagged banks that had not failed by 2025-12-31 (never failed, or failed later), shown because rows overstate how many different banks were wrongly flagged.

## Caveat: reporting lag
Banks file their call reports about a month after quarter-end. A flag on the 2022-12-31 report could not have been produced before roughly the end of January 2023. So real warning time is about the lead time minus roughly one month. Lead times in this project are measured from the report date, and the README should say so.

## Alternatives
1. **Fixed probability cut-off (for example 0.5).** Rejected: the crisis-heavy training base rate makes probabilities unreliable in calm years.
2. **Row-level recall.** Rejected: a bank with four flagged rows would count four times; the question is how many banks were caught.
3. **Round the flag count down.** Rejected: small quarters would flag nobody.

Related: [[decisions/0010-label-and-time-split]].
