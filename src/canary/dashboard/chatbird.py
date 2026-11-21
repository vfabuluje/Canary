"""The corner canary (spec 5): Ask Canary's floating pixel bird and chat panel on every page.

A Streamlit v2 component (web/chatbird.js and web/chatbird.css) draws the bird bottom-right and the panel above
it; this module decides what it shows and answers its questions. The browser sends a question as the trigger
`question`; the callback only stores it, and `render_chat` (called once per run, after the page) applies the
guards, asks `chat.ask` and sends the new transcript back as the component's data. Python can't update the
component mid-run, so the browser shows its own "thinking" state until data with a new `nonce` arrives, and the
lookups are listed under the answer ("What I looked up").

Hidden entirely unless secrets hold ASK_ENABLED = true and an ANTHROPIC_API_KEY (ruling R22). The bird sleeps
("RESTING") once today's question or dollar limit is reached, or after an API or unexpected error this visit
(whose billed cost still counts toward the dollar limit); the visitor's own SESSION_LIMIT keeps it awake and only
disables the input. Each question sent logs one line (outcome, calls, lookups, cost and today's totals), never the
question, the answer or the key. The conversation lives in
`st.session_state["chat"]` for the visit only; `DAILY` is in memory for the process.
"""

import functools
import re
from dataclasses import asdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Literal

import streamlit as st
from streamlit.logger import get_logger

from canary.dashboard import ask, chat, data, search, theme
from canary.dashboard.ask import API_ERROR, MAX_CHARS, RESTING, SESSION_LIMIT
from canary.dashboard.chat import ChatResult, Conversation, PageContext
from canary.dashboard.chat_facts import FactLedger
from canary.dashboard.copy import (CHAT_ASLEEP, CHAT_ASLEEP_PHONE, CHAT_BUBBLE, CHAT_BUBBLE_PHONE, CHAT_BUTTON,
                                   CHAT_CLOSE, CHAT_EMPTY, CHAT_FOOTER, CHAT_GREETING, CHAT_LABEL, CHAT_LOOKED_UP,
                                   CHAT_OPEN, CHAT_PLACEHOLDER, CHAT_SESSION_DONE, CHAT_STARTER_BANK,
                                   CHAT_STARTER_BANK_FLAGGED, CHAT_STARTERS_GENERAL, CHAT_THINKING, CHAT_TITLE,
                                   CHAT_TOO_LONG, CHAT_TWEET)

log = get_logger(__name__)  # Streamlit's console handler, so info lines reach the Community Cloud log

WEB = Path(__file__).parent / "web"
STATE_KEY = "chat"  # the visit's conversation, questions used, last result and notices
COMPONENT_KEY = "chat-bird"
PENDING_KEY = "chat-question"  # set by the component callback, consumed by render_chat
DAILY = ask.DailyCounter()  # one per app process, shared by every visitor
MAX_PAIRS = 4  # "label display" pairs in a source line
MAX_NOTICES = 10  # failed or stopped questions kept in the visible transcript
GUARD = "guard"  # outcome of a question stopped before any call (never logged)
DAILY_REST = "daily_limit"  # outcome when today's question or dollar limit stopped it
ERROR = "error"  # followed by ":" and the exception type: an unexpected error (chat.ask's, or before any call)
SLEEP_OUTCOMES = (f"{API_ERROR}:", f"{ERROR}:")  # a result with one of these puts the bird to sleep for the visit

BirdState = Literal["hidden", "awake", "asleep"]


def utc_today() -> date:
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


# ---- what the bird shows ------------------------------------------------------------------------------------

def bird_state(enabled: bool, resting: bool) -> BirdState:
    if not enabled:
        return "hidden"
    return "asleep" if resting else "awake"


def is_resting(today: date, last: ChatResult | None) -> bool:
    """Asleep once today's question or dollar limit is reached, or after an API error or unexpected error this
    visit (ruling R12: so a failing path can't be re-triggered). The visitor's own per-visit limit is not
    resting."""
    return not DAILY.available(today) or (last is not None and last.outcome.startswith(SLEEP_OUTCOMES))


def _ever_flagged(cert: int) -> bool:
    try:
        hist = data.scores_history()
        return bool(hist.loc[hist["cert"] == int(cert), "flagged"].any())
    except Exception:  # a starter chip never breaks the page
        return False


def starters(page: PageContext) -> list[str]:
    """Three starter questions; on a bank's page the first is about that bank."""
    general = list(CHAT_STARTERS_GENERAL)
    if page.page != "bank" or page.cert is None:
        return general
    name = page.bank or f"bank {page.cert}"
    first = (CHAT_STARTER_BANK_FLAGGED if _ever_flagged(page.cert) else CHAT_STARTER_BANK).format(name=name)
    return [first] + general[1:]


_PAREN = re.compile(r"\s*\([^)]*\)")
_IDENTITY = {"Bank name", "Certificate number"}  # already in the line's bank part


def _short(label: str) -> str:
    return _PAREN.sub("", label).strip()


def source_line(ledger: FactLedger, cited: list[str]) -> str:
    """The grey line under an answer, built from the cited facts only (never model text): the banks, then the
    quarters, then up to MAX_PAIRS "label display" pairs. A rank and that quarter's bank count read as
    "rank 3,494 / 4,773"."""
    facts = ledger.facts_for(dict.fromkeys(cited))
    if not facts:
        return ""
    banks = [f"{name}, cert {cert}" if name else f"cert {cert}"
             for cert, name in dict.fromkeys(ledger.bank_of[f.id] for f in facts if f.id in ledger.bank_of)]
    quarters = list(dict.fromkeys(f.quarter.isoformat() for f in facts if f.quarter))
    pairs: list[str] = []
    paired: set[str] = set()
    for f in facts:
        if f.id in paired or f.label in _IDENTITY:
            continue
        short = _short(f.label)
        if short.lower().endswith("national rank"):
            prefix = short[: -len("national rank")]
            bank = ledger.bank_of.get(f.id)
            count = next((g for g in facts if g.id not in paired and g.quarter == f.quarter
                          and _short(g.label).lower().endswith("banks ranked that quarter")
                          and ledger.bank_of.get(g.id, bank) == bank), None)
            text = f"{prefix}rank {f.display}"
            if count is not None:
                paired.add(count.id)
                text += f" / {count.display}"
        elif short.endswith("On the watchlist"):
            text = f.display  # "flagged" / "not flagged"
        else:
            text = f"{short} {f.display}"
        paired.add(f.id)
        pairs.append(text)
    pairs = list(dict.fromkeys(pairs))[:MAX_PAIRS]
    return " · ".join(banks + quarters + pairs)


def greeting() -> str:
    try:
        count = len(data.report_certs())
    except Exception:  # the greeting never breaks the page
        count = "many"
    return CHAT_GREETING.format(report_count=count)


def _msg(who: str, text: str, source: str = "", lookups=()) -> dict:
    return {"who": who, "text": text, "source": source, "lookups": list(lookups)}


def _notice(at: int, question: str, result: ChatResult) -> dict:
    return {"at": at, "question": question, "text": result.text, "lookups": list(result.lookups)}


def payload(state: BirdState, conv: Conversation, page: PageContext, used: int, last: ChatResult | None,
            question: str | None = None, nonce: int = 0, notices: list[dict] | None = None) -> dict:
    """The JSON the component draws from. `notices` are the visit's failed or stopped questions with the number
    of answered turns before each; when omitted, a failed `last` (with its `question`) is the only one."""
    if notices is None:
        notices = [_notice(len(conv.turns), question or "", last)] if last is not None and not last.ok else []
    messages = [_msg("bird", greeting())]
    for i in range(len(conv.turns) + 1):
        for n in (n for n in notices if n["at"] == i):
            if n["question"]:
                messages.append(_msg("me", n["question"]))
            messages.append(_msg("bird", n["text"], "", n["lookups"]))
        if i < len(conv.turns):
            t = conv.turns[i]
            messages += [_msg("me", t.question), _msg("bird", t.answer, source_line(conv.ledger, t.cited), t.lookups)]
    left = max(SESSION_LIMIT - used, 0)
    asleep = state == "asleep"
    closing = RESTING if asleep else CHAT_SESSION_DONE.format(limit=SESSION_LIMIT) if left == 0 else None
    if closing and messages[-1]["text"] != closing:
        messages.append(_msg("bird", closing))
    asked = bool(conv.turns) or used > 0 or last is not None
    return {
        "state": state,
        "bubble": CHAT_ASLEEP if asleep else CHAT_BUBBLE,
        "bubble_phone": CHAT_ASLEEP_PHONE if asleep else CHAT_BUBBLE_PHONE,
        "messages": messages,
        "starters": [] if asked or asleep else starters(page),
        "left": left,
        "limit": SESSION_LIMIT,
        "max_chars": MAX_CHARS,
        "footer": CHAT_FOOTER.format(left=left),
        "can_ask": not asleep and left > 0,
        "nonce": nonce,
        "sprite": {"grid": list(theme.BIRD), "palette": dict(theme.PALETTE)},
        "text": {"title": CHAT_TITLE, "open": CHAT_OPEN, "close": CHAT_CLOSE, "label": CHAT_LABEL,
                 "placeholder": CHAT_PLACEHOLDER, "button": CHAT_BUTTON, "tweet": CHAT_TWEET,
                 "looked_up": CHAT_LOOKED_UP, "thinking": CHAT_THINKING},
    }


# ---- answering a question -----------------------------------------------------------------------------------

def _stopped(text: str, outcome: str = GUARD) -> ChatResult:
    return ChatResult(False, text, [], [], 0.0, outcome, 0, 0, 0)


def _last(saved: dict) -> ChatResult | None:
    last = saved.get("last")
    return ChatResult(**last) if last else None


def _guard(saved: dict, question: str, today: date) -> ChatResult | None:
    """The checks before any call, in order: empty, too long, the visit's limit, today's limits (and a bird
    asleep after an error this visit)."""
    if not question:
        return _stopped(CHAT_EMPTY)
    if len(question) > MAX_CHARS:
        return _stopped(CHAT_TOO_LONG.format(count=len(question), limit=MAX_CHARS))
    if saved.get("used", 0) >= SESSION_LIMIT:
        return _stopped(CHAT_SESSION_DONE.format(limit=SESSION_LIMIT))
    if not DAILY.available(today):  # the question count and the dollar limit
        return _stopped(RESTING, DAILY_REST)
    if is_resting(today, _last(saved)):  # asleep after an error this visit
        return _stopped(RESTING)
    return None


def _log_result(result: ChatResult, today: date) -> None:
    """One line per question sent: outcome, calls, lookups, cost and today's totals (never the question, answer
    or key)."""
    count, spent = DAILY.today(today)
    line = ("Ask Canary: outcome=%s calls=%d tools=%d cost=$%.5f; today %d/%d questions, $%.4f/$%.2f spent",
            result.outcome, result.calls, result.tool_calls, result.cost_usd, count, DAILY.limit, spent,
            DAILY.usd_limit)
    (log.info if result.ok else log.warning)(*line)


def _call(saved: dict, page: PageContext, question: str, key: str, today: date) -> ChatResult:
    try:
        client = ask.make_client(key)
    except Exception as exc:  # no anthropic package, bad key format, ...: rest, never show the key
        result = _stopped(RESTING, f"{ERROR}:{type(exc).__name__}")  # before any call, so cost 0
        _log_result(result, today)
        return result
    if not DAILY.take(today):
        return _stopped(RESTING, DAILY_REST)
    saved["used"] = saved.get("used", 0) + 1
    conv = Conversation.from_state(saved.get("conv", {}))
    try:
        result = chat.ask(conv, page, question, client)
    except Exception as exc:  # last resort; chat.ask itself returns error:* with the partial cost (ruling R12)
        result = _stopped(RESTING, f"{ERROR}:{type(exc).__name__}")
    saved["conv"] = conv.to_state()
    DAILY.add_cost(today, result.cost_usd)
    _log_result(result, today)
    return result


def handle_question(saved: dict, page: PageContext, question: str, key: str, today: date) -> ChatResult:
    """Guard, then ask, one question; `saved` (the visit's chat state) is updated in place."""
    saved["nonce"] = saved.get("nonce", 0) + 1
    question = (question or "").strip()
    turns_before = len(saved.get("conv", {}).get("turns", []))
    result = _guard(saved, question, today) or _call(saved, page, question, key, today)
    saved["last"] = asdict(result)
    saved["question"] = question
    if not result.ok:
        notices = saved.setdefault("notices", [])
        notices.append(_notice(turns_before, question, result))
        del notices[:-MAX_NOTICES]
    return result


# ---- mounting -----------------------------------------------------------------------------------------------

@functools.cache
def _component():
    return st.components.v2.component(
        "canary_chatbird",
        css=(WEB / "chatbird.css").read_text(encoding="utf-8"),
        js=(WEB / "chatbird.js").read_text(encoding="utf-8"),
        isolate_styles=True,
    )


def _asked() -> None:
    """Component callback: store the question; render_chat answers it after the page has drawn."""
    value = st.session_state.get(COMPONENT_KEY)
    question = getattr(value, "question", None)
    if question is None and isinstance(value, dict):
        question = value.get("question")
    if question is not None:
        st.session_state[PENDING_KEY] = str(question)


def page_context(page) -> PageContext:
    """Where the visitor is, from `st.navigation`'s page (its `url_path` is "" for Home). On Find a bank with a
    valid `?cert=N` that names a bank in the data (the same rule views/find.py uses to open it) the page is
    "bank", with the bank's name."""
    path = getattr(page, "url_path", "") or ""
    if path == "":
        return PageContext("home")
    if path != "find":
        return PageContext(path)
    raw = st.query_params.get("cert")
    cert = search.parse_cert(raw) if isinstance(raw, str) else None
    if cert is not None:
        try:
            banks = data.banks()
            match = banks.loc[banks["cert"] == cert, "name"]
        except Exception:  # the bird never breaks the page
            match = []
        if len(match):
            return PageContext("bank", cert, str(match.iloc[0]))
    return PageContext("find")


def render_chat(page: PageContext) -> None:
    """Mount the corner canary (once per run, after the page); nothing at all while Ask is off or has no key."""
    key = _api_key() if _enabled() else None
    if key is None:
        return
    saved = st.session_state.setdefault(STATE_KEY, {})
    today = utc_today()
    question = st.session_state.pop(PENDING_KEY, None)
    if question is not None:
        handle_question(saved, page, question, key, today)
    last = _last(saved)
    state = bird_state(True, is_resting(today, last))
    conv = Conversation.from_state(saved.get("conv", {}))
    data_ = payload(state, conv, page, saved.get("used", 0), last, saved.get("question"), saved.get("nonce", 0),
                    saved.get("notices", []))
    _component()(key=COMPONENT_KEY, data=data_, on_question_change=_asked)
