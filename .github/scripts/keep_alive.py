"""Visit the Canary dashboard in a real (headless) browser so it stays awake.

A plain HTTP GET only fetches Streamlit Cloud's page shell, which answers 200
whether the app is awake or asleep, and never opens the app's live connection.
This script loads the page like a visitor, clicks the wake-up button if the
sleep screen is showing, and checks that the app itself actually rendered.

Exit codes:
  0  the app was awake and rendered
  1  the app was asleep (woken now, so the pings are not keeping it awake),
     or it could not be loaded at all
"""

import os
import re
import sys
from datetime import datetime, timezone

from playwright.sync_api import TimeoutError as PlaywrightTimeout
from playwright.sync_api import sync_playwright

APP_URL = os.environ.get("APP_URL", "https://canarybank.streamlit.app/")
# The app runs in an iframe at /~/+/. Its home page heading is "CANARY";
# if that heading changes, change this too.
APP_FRAME = re.compile(r"/~/\+/")
APP_HEADING = "CANARY"
WAKE_BUTTON = re.compile(r"get this app back up", re.IGNORECASE)

LOAD_TIMEOUT_MS = 60_000  # first page load
WAKE_LOOK_MS = 15_000  # how long to look for the sleep screen
BOOT_TIMEOUT_MS = int(os.environ.get("BOOT_TIMEOUT_MS", 180_000))  # a woken app can take a few minutes to boot
STAY_MS = 15_000  # keep the session open so it counts as a visit


def log(status: str, message: str) -> None:
    line = f"{status}: {message} ({datetime.now(timezone.utc):%Y-%m-%dT%H:%M:%SZ})"
    print(line if status == "OK" else f"::error::{line}")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as fh:
            fh.write(line + "\n")


def app_rendered(page, timeout_ms: int) -> bool:
    """Wait for the app's iframe to show its home-page heading."""
    deadline = datetime.now().timestamp() + timeout_ms / 1000
    while datetime.now().timestamp() < deadline:
        for frame in page.frames:
            if APP_FRAME.search(frame.url):
                heading = frame.locator("h1", has_text=APP_HEADING)
                try:
                    heading.first.wait_for(state="visible", timeout=5_000)
                    return True
                except PlaywrightTimeout:
                    pass
        page.wait_for_timeout(2_000)
    return False


def main() -> int:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            page.goto(APP_URL, wait_until="domcontentloaded", timeout=LOAD_TIMEOUT_MS)
        except PlaywrightTimeout:
            log("FAILED", f"{APP_URL} did not load within {LOAD_TIMEOUT_MS // 1000} s")
            return 1

        # Either the app renders, or the sleep screen shows its wake-up button.
        was_asleep = False
        wake = page.get_by_role("button", name=WAKE_BUTTON)
        if not app_rendered(page, WAKE_LOOK_MS):
            if wake.count() and wake.first.is_visible():
                was_asleep = True
                wake.first.click()

        if not app_rendered(page, BOOT_TIMEOUT_MS):
            log("FAILED", f"{APP_URL} did not render the app (asleep before: {was_asleep})")
            return 1

        page.wait_for_timeout(STAY_MS)
        browser.close()

    if was_asleep:
        log("ASLEEP", f"{APP_URL} was asleep; woke it, but the pings are not keeping it awake")
        return 1
    log("OK", f"{APP_URL} was awake and rendered")
    return 0


if __name__ == "__main__":
    sys.exit(main())
