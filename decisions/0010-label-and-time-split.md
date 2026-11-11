# 0010 — The label and the time split

**Date:** 2026-11-11
**Status:** Accepted

## Decision
**Label.** A bank-quarter row gets `label = 1` if the bank fails 1 to 4 quarters after that report date (`quarters_until_failure` between 1 and 4). Everything else, including banks that never fail, gets 0. Zero quarters (failed in the same quarter) is not counted: the data is no longer an early warning by then.

**Four splits, by report date**
| Split | Report dates | Use |
|---|---|---|
| train | 2001-03-31 to 2014-12-31 | fit the model |
| gap | 2015-03-31 to 2015-12-31 | dropped, never used |
| test | 2016-03-31 to 2024-12-31 | the honest evaluation |
| not_scored | after 2024-12-31 | outside the study window |

**Why 2015 is a gap.** A 2015 report looks 4 quarters ahead, so its label depends on failures during 2016. If those rows were in training, the model would learn from 2016 outcomes, which belong to the test period. Dropping 2015 keeps training labels built only from failures through 2015-12-31 (`TRAINING_FAILURE_CUTOFF`). The test period then starts clean at 2016-03-31.

**CLAUDE.md wording.** CLAUDE.md now says "train on 2001-2015 failures (report dates through 2014; 2015 reports are dropped because their outcomes depend on 2016 failures), test 2016-2024". The earlier "train 2001-2015" was ambiguous about whether 2015 report dates were in; this is the precise version. The model still never sees 2023 failures during training.

**Inner validation split.** To choose settings (early stopping, tuning) without touching the test period, the training rows are split again by time: fit on report dates up to 2011-12-31 (`INNER_FIT_END`), validate on 2012-03-31 to 2014-12-31. Random splits are not used, because a bank's neighbouring quarters look alike and would leak.

**Feature list.** `FEATURE_COLUMNS` in `src/canary/model/dataset.py` holds the 31 features from decision 0009, in the same order as the dbt model. A test reads the dbt yml to prove they match. IDs, label and failure columns are never features.

## Alternatives
1. **Keep 2015 in training.** Rejected: leaks 2016 failures into training.
2. **Random train/validation split.** Rejected: leaks through time-adjacent rows of the same bank.
3. **Count same-quarter failures as positive.** Rejected: no warning left to give.

Related: [[decisions/0009-features-and-zero-handling]].
