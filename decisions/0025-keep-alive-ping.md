# 0025 — A GitHub Actions browser visit keeps the dashboard from going to sleep

**Date:** 2026-11-24 (revised 2026-11-26)
**Status:** Accepted

## Decision
A GitHub Actions workflow, `.github/workflows/keep-alive.yml`, visits https://canarybank.streamlit.app/ **every 6 hours at 23 minutes past** (00:23, 06:23, 12:23 and 18:23 UTC) with a **headless Chromium browser** (Playwright, script `.github/scripts/keep_alive.py`). It can also be run by hand from the Actions tab ("Run workflow"). In plain English:

- **It loads the page like a person would.** The browser opens the site, which starts the app's live connection, and stays on the page for 15 seconds.
- **It checks that the app itself is showing.** The app runs inside an iframe at `/~/+/`; the run passes only when the `CANARY` heading appears there. If that heading is ever renamed, the script must be updated too.
- **If the sleep screen shows, it wakes the app.** It clicks "Yes, get this app back up!", waits up to 3 minutes for the app to boot, and then **fails the run on purpose** with `ASLEEP: … woke it, but the pings are not keeping it awake`. A red run means the schedule isn't working, and GitHub emails the owner.
- **It logs one line:** `OK`, `ASLEEP` or `FAILED`, in the run log and on the run's summary page.

## Why
- **A browser, not curl (the first version, 2026-11-24).** The first version sent a plain HTTP GET and checked for a 200. That page is Streamlit Cloud's own page shell (about 10 KB, the same whether the app is awake or asleep); the sleep screen is drawn inside it later by JavaScript. So every run was green even if the app was asleep, and curl never opens the app's live connection, so it most likely did not count as a visit.
- **Every 6 hours at :23, not every 8 hours on the hour.** Streamlit Community Cloud is believed to put free apps to sleep after about 12 hours without traffic. In the first 1.5 days the 8-hour schedule fired 3 times out of 5, with gaps of about 11.5 and 12 hours, because GitHub delays or skips scheduled runs set for the top of the hour when it is busy. An odd minute is less crowded, and a 6-hour gap still stays under 12 hours if one run is skipped.
- **GitHub Actions, not AWS.** It is free (public repo), it needs no credentials and it is already part of the stack. Each run takes about a minute, most of it installing Chromium. It never opens Ask Canary, so it makes no Claude API calls.

## Limitations
- **The wake-up click has not been seen working yet.** The app was awake on every test. If the button's text changes, the run fails with `FAILED` instead of `ASLEEP`; either way it is red.
- **GitHub turns off scheduled workflows in public repos after 60 days without commits.** It emails a warning first. Re-enable the workflow from the Actions tab.
- Scheduled runs only fire from the default branch (`main`).
- The visits show up in the app's viewer count on Streamlit Cloud.
