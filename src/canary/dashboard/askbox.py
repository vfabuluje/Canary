"""The Ask Canary box on a written-report page, with its spending guards (spec 5.6).

Hidden entirely unless secrets hold ASK_ENABLED = true and an ANTHROPIC_API_KEY (ruling R22). Once on,
the daily cap, an API error, a refusal or a bad reply shows "Ask Canary is resting for today." A
question is checked (not empty, at most MAX_CHARS) before anything is sent, and it counts against the
visit's SESSION_LIMIT and the app's DAILY_LIMIT only when a call is actually made. Questions and answers are shown once and never stored. The key is never shown.
"""

import html
import logging
from datetime import datetime, timezone

import streamlit as st

from canary.dashboard import ask, theme
from canary.dashboard.copy import (ASK_BUTTON, ASK_EMPTY, ASK_LABEL, ASK_LEFT, ASK_NOTE, ASK_PLACEHOLDER,
                                   ASK_SESSION_DONE, ASK_THINKING, ASK_TITLE, ASK_TOO_LONG)

log = logging.getLogger(__name__)

SESSION_KEY = "ask_used"  # questions sent this visit
DAILY = ask.DailyCounter()  # one per app process, shared by every visitor


def utc_today():
    return datetime.now(timezone.utc).date()


def _secret(name: str):
    """A value from Streamlit secrets, or None (also when there is no secrets file at all)."""
    try:
        return st.secrets.get(name)
    except Exception:  # Streamlit raises when no secrets file exists
        return None


def _enabled() -> bool:
    """On only for true or "true" (any case); anything else, or no setting, is off."""
    flag = _secret("ASK_ENABLED")
    return flag is True or (isinstance(flag, str) and flag.strip().lower() == "true")


def _api_key() -> str | None:
    key = _secret("ANTHROPIC_API_KEY")
    return key.strip() if isinstance(key, str) and key.strip() else None


def _say(text: str) -> None:
    st.markdown(text)


def answer_html(text: str) -> str:
    """The answer as one HTML block with no line breaks: whitespace is collapsed before escaping, so no blank
    line can end the block and let Markdown ($...$ maths, [x](url) links) render; "$" is an entity too."""
    paragraphs = (" ".join(p.split()) for p in text.split("\n\n"))
    return "".join(f'<p class="ask-answer">{html.escape(p).replace("$", "&#36;")}</p>' for p in paragraphs if p)


def _show_answer(text: str) -> None:
    theme.html_block(answer_html(text))


def _send(report: dict, question: str, key: str) -> None:
    question = question.strip()
    if not question:
        _say(ASK_EMPTY)
        return
    if len(question) > ask.MAX_CHARS:
        _say(ASK_TOO_LONG.format(count=len(question), limit=ask.MAX_CHARS))
        return
    try:
        client = ask.make_client(key)
    except Exception as exc:  # no anthropic package, bad key format, ...: rest, never show the key
        log.warning("Ask Canary client unavailable: %s", type(exc).__name__)
        _say(ask.RESTING)
        return
    if not DAILY.take(utc_today()):
        _say(ask.RESTING)
        return
    st.session_state[SESSION_KEY] = st.session_state.get(SESSION_KEY, 0) + 1
    with st.spinner(ASK_THINKING):
        result = ask.answer(report, question, client)
    _show_answer(result.text)


def render_askbox(report: dict) -> None:
    """Draw the box for one written-report page; nothing at all while Ask is off or has no key."""
    key = _api_key() if _enabled() else None
    if key is None:
        return
    with st.container(key="box-ask"):
        theme.html_block(f'<div class="ct">{html.escape(ASK_TITLE)}</div>')
        if not DAILY.available(utc_today()):
            _say(ask.RESTING)
        elif st.session_state.get(SESSION_KEY, 0) >= ask.SESSION_LIMIT:
            _say(ASK_SESSION_DONE.format(limit=ask.SESSION_LIMIT))
        else:
            _form(report, key)
        st.caption(ASK_NOTE)


def _form(report: dict, key: str) -> None:
    with st.form("ask-form", border=False):
        question = st.text_input(ASK_LABEL, placeholder=ASK_PLACEHOLDER, key="ask-question")
        sent = st.form_submit_button(ASK_BUTTON, key="ask-send")
    if sent:
        _send(report, question, key)
    used = st.session_state.get(SESSION_KEY, 0)
    if used >= ask.SESSION_LIMIT:
        _say(ASK_SESSION_DONE.format(limit=ask.SESSION_LIMIT))
    else:
        st.caption(ASK_LEFT.format(left=ask.SESSION_LIMIT - used, limit=ask.SESSION_LIMIT))
