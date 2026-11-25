# 0025 — A GitHub Actions ping keeps the dashboard from going to sleep

**Date:** 2026-11-24
**Status:** Accepted

## Decision
A GitHub Actions workflow, `.github/workflows/keep-alive.yml`, visits https://canarybank.streamlit.app/ **every 8 hours** (00:00, 08:00 and 16:00 UTC). It can also be run by hand from the Actions tab ("Run workflow"), for example before someone is expected to look at the dashboard. In plain English:

- **One HTTP GET, checked for a 200.** It does not read the page. It retries twice and gives up after 60 seconds.
- **It keeps a cookie jar.** Streamlit sends a first-time visitor through an auth redirect that sets a cookie. Without the cookie, curl redirects forever (it stopped at 50). With it, the page answers 200 after 3 redirects.
- **It logs one line.** `OK: … responded 200` or `FAILED: … responded <code>`, in the run log and on the run's summary page. A failed run turns red, and GitHub emails the owner.

## Why
- **Every 8 hours, not 12 or every 3 days.** Streamlit Community Cloud is believed to put free apps to sleep after about 12 hours without traffic. GitHub often starts scheduled runs late (minutes, sometimes more), so a 12-hour gap would sometimes miss the window. Eight hours leaves room for that delay. The repo is public, so the runs cost nothing.
- **GitHub Actions, not AWS.** It is free, it needs no credentials and it is already part of the stack.

## Limitations
- **A plain GET may not count as a visit.** A Streamlit app only really runs once a browser opens a live connection to it, and curl does not. If the app still sleeps, the fix is a headless-browser step that loads the page and clicks "Yes, get this app back up!" when the sleep screen appears.
- **GitHub turns off scheduled workflows in public repos after 60 days without commits.** It emails a warning first. Re-enable the workflow from the Actions tab.
- Scheduled runs only fire from the default branch (`main`).
