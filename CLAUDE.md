# Canary — Bank Failure Early-Warning System

## Project goal
Build a pipeline + ML model that scores every FDIC-insured US bank's risk of failing within the next 4 quarters, using real public regulatory data, and test whether it would have flagged Silicon Valley Bank, Signature Bank, and First Republic before they failed in 2023. An AI analyst agent writes cited risk memos per bank.

## Why this project exists (the SVB story)
Silicon Valley Bank (SVB) served tech startups and investors. In 2020–2021 it took in billions in deposits and invested much of it in long-term government bonds while rates were low. In 2022 the Fed raised rates quickly, so those bonds lost value (large unrealized losses). Most of SVB's deposits were uninsured (above the FDIC's $250K limit). In March 2023 SVB announced it had sold bonds at a loss; customers panicked and pulled about $42B in a single day. Regulators closed SVB on March 10, 2023, then the second-largest bank failure in US history. Signature Bank failed two days later and First Republic failed in May 2023. The warning signs were visible in SVB's public filings months earlier. Canary asks: could a model built on public data have raised the alarm in time?

## Why the name
Coal miners once carried canaries underground. Canaries react to toxic gas before people do, so a sick canary was the early warning to get out. Canary is that early warning for banks.

## Data sources (all public)
- FDIC BankFind API — quarterly financials for every insured bank
- FFIEC bulk call reports: deferred, see decision 0005
- FDIC failed bank list — failure labels since 2000
- FRED (optional) — interest rates and macro context

## Tech stack
Python, pandas; AWS (S3, Athena, Glue, Lambda later); dbt (dbt-athena); XGBoost; Claude API for in-product agents; Streamlit; GitHub Actions; Obsidian vault (this folder).

## Reference
- reference/STACK.md: what each tool is and how Canary uses it.
- reference/GLOSSARY.md: banking and technical terms, tied to the repo's columns and decisions.

## Rules
- I must understand and be able to explain every piece of this project. Explain your choices in plain English and log them in decisions/.
- Develop locally first; use AWS only when needed. Keep AWS cost under $5/month. Never commit credentials.
- Time-based validation only: train on 2001–2015 failures (report dates through 2014; 2015 reports are dropped because their outcomes depend on 2016 failures), test 2016–2024. The model must never see 2023 failures during training.
- Every table and column goes in data-dictionary/. Every major choice goes in decisions/ with the reason.
- Write tests for pipeline code and dbt data tests for every model.
- Agent outputs must cite the bank, quarter, and numbers they rely on.
- Be honest about limitations; README must say "Research tool, not financial advice."
- Update daily-log.md at the end of every session: what was done, what's next, open questions.

## Phases
1. Vault + repo setup; pull FDIC financials and failed bank list
2. Call report pipeline to S3/Athena; dbt models and data tests
3. CAMELS-style features; train XGBoost; test on 2016–2024
4. SVB / Signature / First Republic replay; error analysis
5. AI risk analyst agent; one Obsidian note per bank
6. Streamlit dashboard; README with metrics and limitations; demo video

## Metrics to report
Recall (failures flagged ≥1 quarter early), lead time in quarters, false alarm rate, AUC on 2016–2024, case studies for SVB / Signature / First Republic, pipeline scale, AWS cost.
