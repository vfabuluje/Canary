# Phase 6 Spec: Canary dashboard

**Date:** 2026-11-19
**Status:** Draft for Victor's approval
**Phase:** 6 (dashboard). Builds on Phases 1-5e. The approved visual design is
`dashboard/design/report-replay-v6.html` (the "v6" mockup), which is the reference for look and
behavior wherever this spec says "v6 style".

## 1. Intent

A public, free, read-only Streamlit dashboard that lets anyone (a recruiter, an interviewer, a
non-technical friend) understand what Canary does and what it found, in this order of importance:

1. **What Canary is** (big title, one plain line), then **the honest miss:** it did not flag the three 2023 bank collapses, and why.
2. **The 2023 case studies:** watch the score fall while a bank's real weak spot grew.
3. **How a report is made:** a short, playful loading-screen replay of a real run of the three AI
   agents plus the code checks, then the report in plain English.
4. **The trade-off:** how the watchlist size trades failures caught against false alarms.
5. **Find any bank.**

It must be easy to follow for someone with no finance or tech background (Victor tested this with
a non-technical viewer; the v6 two-screen design came from her feedback).

## 2. Goals
- G1. **Read-only and free to run**, with one exception: everything is served from small,
  committed, pre-computed data files, and the only per-visitor AI is the capped **Ask Canary**
  box (§5.6, Claude Haiku 5.5), which spends from Victor's prepaid balance and can be switched off.
- G2. **Hosting:** Streamlit Community Cloud from the public repo (Victor).
- G3. **Data export:** `python -m canary.dashboard export` writes the read-only files under
  `dashboard/data/` (committed); the app reads only those (never `data/`).
- G4. **Six features** (§5), Ask Canary last: home page with the honest miss, bank search, case-study replay, watchlist-size
  slider, and the report replay + report page.
- G5. **v6 style everywhere** (§4), with the detective / basketball theme switch.
- G6. Tests (export, data integrity, app pages via Streamlit's `AppTest`), no network.
- G7. Docs: decision 0023, data dictionary for the exported files, runbook (export, run locally,
  deploy), README link to the live app.

## 3. Non-goals and anti-goals
- **Non-goals:** new model or memo work; new written reports (the 61 stay as they are); AWS hosting; user
  accounts; scheduled re-runs; a separate modern-style theme (the "modern draft" was rejected).
- **Anti-goals:**
  - any per-visitor cost or live API call outside the Ask Canary module (only that module imports
    `anthropic`, and the app runs fully with it switched off or with no API key);
  - any number on screen that isn't from the exported data (no hand-typed figures in the app,
    except the fixed honest-miss and case-study copy, which is checked against the data in a test);
  - a dual-axis chart (two y-scales);
  - wording that implies a descriptive section predicts failure;
  - the animation implying things the pipeline didn't do (e.g. agents running in sequence when
    they ran in parallel, or the concentration check running after the agents).

## 4. Look and feel (v6 style)
- Grey page background (`#d5d7db`), navy (`#1e2240`) 3-4px borders with hard offset shadows,
  yellow (`#ffe066`) highlights, "Press Start 2P" for headings and buttons, a clean sans-serif for
  body text (16-17px, plain English).
- Pixel-art characters drawn from sprite grids (the v6 engine), never images.
- **Three themes (Victor)**, switched by a "Theme" control in the top bar on every page (and on
  the home page), remembered for the visit. The theme changes the **page background** everywhere
  and the characters in the report replay:
  - **Standard:** the grey page (`#d5d7db`); the replay uses the detective cast (Claude's call).
  - **Detectives:** a cork-board background with a red pixel pin on each card, dark top bar.
  - **Basketball:** a hardwood-court background with white court lines (center circle behind the
    title), blue top bar.
  Cards stay white with navy borders in every theme so text stays readable. The casts:
  - **Detectives:** Trend Detective (deerstalker, magnifier), Peer Detective (striped beanie,
    folder), Lead Detective (fedora, notepad), the Fact Checker (glasses), the Rule Stamp (a
    stamp object).
  - **Basketball** (white jerseys, light-blue numbers and shorts): **#5 Trend** (brown skin, black
    leg sleeve, black sneakers), **#13 Peer** (light skin, light-blue headband, white sneakers),
    **#23 Captain** (Caucasian, light-blue arm sleeve, light-blue sneakers), **the Referee**
    (black-and-white stripes, whistle) for the rule check, **Replay Review** (glasses, light-blue
    polo) for the fact checker.
- Bank names in titles are big and bold (v6 "Building Canary's report on / **Bank**").

## 5. Features

### 5.1 Home page
- **Hero (Victor):** a big **"Canary"** centered on the page in the v6 pixel font, with one line
  under it: "Bank Failure Early-Warning System". (A small pixel canary beside or above the word is
  Claude's proposal.) Below it, a search box ("Find a bank") and the theme switch.
- **What it is**, in plain words, one or two sentences: every quarter Canary looks at every
  US bank's public numbers and ranks which ones look most likely to fail within a year.
- **Headline numbers** from `metrics.json`, each explained in everyday words (failures caught
  early 21 of 29; typical warning time 4 quarters; AUC 0.90 vs the corrected Texas-ratio rule;
  flags that didn't fail 98.3%).
- **The honest miss, explained for newcomers (Claude's proposal; replaces the original "banner
  first"):** a section below the numbers, not at the top, that sets the scene before naming
  names: "The big test: in 2023 three large US banks collapsed within two months. Canary did not
  flag any of them in time." Then one plain sentence on why and a button to the case studies.
- "Research tool, not financial advice", and links to the other features.

### 5.2 Find a bank
- Fuzzy match (`rapidfuzz`) on bank name over every bank in the features data; if one candidate
  clearly wins (score ≥ 90 and ≥ 10 points ahead of the next), open it directly; otherwise a "Did
  you mean" list (up to 8) with **name, state, and status** (active, or failed with date).
  Identical names are disambiguated by state and status; if still identical, by city (from the 5c
  specialty table) and certificate number.
- Alias map (hand-written, small): "SVB" → Silicon Valley Bank (24735), "Signature" → Signature
  Bank (57053), "First Republic"/"FRB" → First Republic Bank (59017).
- **Showcase banks (61):** open the report replay (§5.5) for that bank, then its report page.
- **Scored banks without a note (~6,200):** a page labeled "No written report for this bank"
  showing its latest score and rank, its rank history (code-built), and the concentration check
  (code-only, 5d). Scores come from `data/analyst/scores.parquet` (2016-03-31 to 2026-06-30); the
  page names the quarter, and quarters after 2024-12-31 are labeled "after the test period".
- **Banks never scored (~4,950, stopped reporting before 2016, e.g. IndyMac):** still searchable,
  with a short page: name, state, status, and "Canary only scores banks from 2016 on; this bank
  stopped reporting in <year>, before that. Earlier years were used to train the model, so
  scoring them would not be a fair test." No score is computed for them.

### 5.3 The 2023 case studies (replay)
- Bank chips: SVB, Signature, First Republic. A quarter slider over the 8 quarters before failure
  (First Republic: 9, through 2023-03-31).
- **Two stacked charts sharing the quarter axis** (never one dual-axis chart): Canary's risk
  percentile (with the 98th-percentile watchlist line), and the bank's real weak spot:
  - SVB: losses on bonds held to maturity as a share of equity (the ratio the model gave almost
    no weight; Victor);
  - Signature: losses on bonds available for sale as a share of equity (the model *did* react;
    a near miss, 94.9th percentile);
  - First Republic: uninsured deposits as a share of deposits, with the plain statement that its
    real losses were on home loans that FDIC data can't value.
- A side card for the selected quarter: rank of N, percentile, the weak-spot value, on the
  watchlist or not, and the top 3 features pushing the score up (plain names and values, from
  `case_studies.csv`), plus one plain-English sentence per bank and phase.
- Hover tooltips on every point; click a point to select that quarter.
- **Phases** (fixed by quarter): *before rates rose* (2021 quarters), *rates rising* (2022 quarters
  before the last report), *last report* (the final quarter shown). The text contains no numbers
  (numbers come from the data on the same card). Proposed copy, for Victor to approve:

  | Bank | Before rates rose | Rates rising | Last report |
  |---|---|---|---|
  | SVB | Rates were near zero. SVB's bond losses were tiny and Canary ranked it around the middle of the pack. Nothing stood out. | As rates rose, losses on the bonds SVB planned to hold grew fast. Canary's score went the other way and rated SVB safer. | SVB's last report before it failed: bond losses close to its entire equity, and Canary still rated it safer than most banks. The model learned from 2008-era failures, which looked nothing like this. |
  | Signature | Signature grew fast in 2021. Canary put it in the riskier part of the pack, but well short of the watchlist. | Losses on its bonds for sale grew, and this time the model reacted: the score climbed. | Its last report put it near the top of the list, just short of the watchlist. A bigger watchlist would have flagged it. |
  | First Republic | Much of First Republic's money came from uninsured deposits: balances above the FDIC limit, which can leave quickly. Canary put it in the riskier part of the pack. | Its real problem was home loans made at low rates, which lost value as rates rose. FDIC data reports what those loans cost, not what they are worth now, so the model could not see it. | This report came after SVB failed. The uninsured share dropped because depositors had already pulled their money out: the run had started. First Republic failed weeks later. |

### 5.4 Watchlist size
- Choose the share flagged per quarter: 0.5%, 1%, 2% (marked "published"), 3%, 5%, 7.5%, 10%.
- For each: failures caught early (of 29), share of flags that didn't fail, bank-quarters
  flagged, recomputed with `canary.model.metrics` (`flag_watchlist`, `bank_recall`,
  `false_alarm_rate`) on `scores_test.parquet` at export time. 2% must reproduce `metrics.json`
  exactly (21 of 29, 98.3%, 3,783), checked by a test.
- A single-series chart of failures caught by size, and a sentence that updates with the choice
  (e.g. at 10% Signature would have been caught; SVB and First Republic still not).

### 5.5 Report replay ("loading screen") and report page — per showcase bank
**Screen 1, the replay** (v6): "Building Canary's report on **<bank>**", one scene at a time,
about 5.5 seconds each, a progress bar, one big plain sentence ("what's happening now") and one
small line ("who"), a **"Who's on now" side panel** listing the five team members with their
AI/RULE badge, a plain one-line role, and a highlighted "Now: …" line for whoever is working.
Scenes, in the real pipeline order:
1. gathering the bank's numbers (no AI);
2. the rule check (stamp / referee) with that bank's real concentration result;
3. trend and peer agents **at the same time** (two balls dribbling in basketball);
4. the fact check on Trend's and Peer's sections (checkmarks over real numbers from them);
5. the lead / captain writing the summary, then, inside the same scene, the Fact Checker /
   Replay Review stepping in to check the summary (Victor: keep 6 scenes, ~33 s);
6. "Report ready!" (basketball: the captain shoots, "SWISH!"), then the **See the report** button.
For a bank with no peer section (e.g. Comenity, 57570: too few comparable banks), Peer sits out
on the bench with "not enough similar banks to compare", and only Trend works in scene 3.
A "Skip to the report" link is always available. If a section needed a retry in the real run, the
check that caught it shows "sent back once, fixed" for that agent (from the trace): scene 4 for
Trend/Peer, scene 5 for the lead.

**Screen 2, the report** (v6): bank name, "the short version" in plain words, a "What happened
next" box (for failed banks: the failure date and whether Canary flagged it), and one card per
finding (trend, peer, rule check, summary) with the character who found it, an AI/RULE badge, and
"✓ every number fact-checked". Highlighted numbers explain themselves on hover/tap. A "Watch how
it was made" button replays screen 1. A "Read the full report" link shows the whole committed note.

**Data for this feature** comes from the committed note (`banks/*.md`) and a **slim trace**
exported from `data/analyst/traces/` (agents, attempts, whether each passed first time, checker
errors, the section texts, the concentration result) — not the full prompts.
**Report-page text (Victor: the mix):**
- **All 61 banks, built by code at export time (no AI call):** each card takes the first finding
  sentence of its section, skipping sentences that only repeat the rank or the FDIC specialty group;
  numbers stay exactly as written. The "short version" headline comes from a template keyed on the
  note's outcome (missed / caught early / false alarm / on the watchlist / not flagged). Hover text
  for a highlighted number is built from its cited fact (label and quarter) plus a small
  hand-written glossary per ratio that contains no numbers.
- **SVB, Signature and First Republic:** v6-quality wording written by Claude, using only numbers
  that appear in their notes, approved by Victor before it ships. A test checks that every number
  in that copy appears in the bank's note.

### 5.6 Ask Canary (Victor: Claude Haiku 5.5)
- A question box on each of the 61 written-report pages ("Ask Canary about this bank"). Banks
  without a written report don't get it (their fact sheets aren't in the exported data).
- One Claude Haiku 5.5 call per question, sent that bank's fact sheet and note (about 15,000
  tokens) with instructions to answer in plain English, cite facts, and say "I can't tell from
  this bank's data" rather than guess. About $0.002 per question.
- The answer goes through the existing citation checker; numbers that don't match a cited fact
  mean one retry, then "I couldn't answer that with checked facts." Checked answers only.
- **Spending guards:** 5 questions per visitor session; a daily cap in the app (Claude's proposal:
  300 questions/day, about $0.60); questions capped at 300 characters; the API key lives only in
  Streamlit's secrets, never in the repo; an on/off switch in secrets; auto-reload stays off on the
  Anthropic account, so spend can never exceed the prepaid balance. When the cap or the balance is
  hit, the box says "Ask Canary is resting for today" and the rest of the app is unaffected.
- No questions or answers are stored. A one-line note under the box: answers are AI-written from
  this bank's public data, fact-checked, and not financial advice.
- Testing uses a fake client; one paid smoke test (a few cents) only with Victor's go-ahead.

## 6. Data export (`dashboard/data/`)
- `banks.parquet`: every bank's cert, name, state, city, first/last report, failure date, latest
  rank/percentile, and whether it has a showcase note.
- `scores_history.parquet`: rank, n_banks, percentile and flag per bank-quarter from 2016-03-31
  (for non-showcase bank pages).
- `concentration.parquet`: the 5d result per bank at its latest quarter (for non-showcase pages).
- `case_studies.json`: the three banks' quarters with percentile, rank, n, weak-spot value, top 3
  features.
- `threshold.json`: the seven watchlist sizes and their results.
- `metrics.json`: copy of the headline metrics.
- `reports/<cert>.json`: per showcase bank, the slim trace + the report-page content.
- Size budget: the whole folder under about 25 MB; the export prints the size and fails above 50 MB.

## 7. Approaches considered
- **Streamlit app with the v6 scenes embedded as HTML components (chosen).** Streamlit for pages,
  search and charts; the pixel scenes, side panel and report cards rendered by the v6 engine
  inside `st.components.v1.html`, fed the exported data.
- Plain static site (rejected): Victor chose Streamlit Community Cloud; search and data handling are
  simpler in Python.
- Modern professional style (rejected by Victor after a full draft).

## 8. Decided by Victor
- Read-only apart from Ask Canary on Claude Haiku 5.5; Streamlit Community Cloud.
- Three themes (Standard grey, Detectives, Basketball) that change the page background.
- v6 style and both themes; the specific player looks; striped referee distinct from Replay Review;
  ~5.5 s per scene; big bold bank name; loading screen then a separate report page; the "Who's on
  now" side panel; the hoop shot before the button.
- Case-study weak spots: SVB held-to-maturity losses; Signature available-for-sale losses; First
  Republic uninsured deposits with the loan-value caveat.
- Banks without a memo show the code-built parts only.
- Search: fuzzy matching, "Did you mean" with name/state/status, alias map.

## 9. Calls made by Claude (Victor to check)
- Fuzzy-match thresholds (≥ 90 and ≥ 10 points clear) and up to 8 suggestions.
- Home page: the honest miss moved below the hero and the numbers, reworded for newcomers; a
  small pixel canary next to the title.
- The rules for picking card sentences and the outcome headline templates.
- Slim traces, not full prompts, are committed.
- Charts in Altair (bundled with Streamlit) styled to v6; no extra chart library.
- Theme choice remembered per visit (session state), not stored anywhere; Standard uses the
  detective cast in the replay.
- Ask Canary guards: 5 per visitor, 300/day, 300-character questions, only on the 61 report pages.
- Never-scored banks (pre-2016) stay searchable with a short "not scored" page; latest scores from
  `scores.parquet`, with post-2024 quarters labeled; the watchlist page uses `scores_test.parquet`.
- Case-study phases and their copy (§5.3); Peer sitting out when a bank has no peer section.
- Decision record 0023.

## 10. Left to the builder
- Streamlit page layout and navigation details; how the v6 engine is packaged for reuse across
  pages; exact Altair styling within §4.
