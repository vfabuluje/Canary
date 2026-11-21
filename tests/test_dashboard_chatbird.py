"""The corner canary (Ask Canary chat): its state, starters, source line, payload and question guards."""

import json
import logging
import re
from dataclasses import asdict
from datetime import date

import pytest

from canary.dashboard import ask, chat, chatbird, data
from canary.dashboard.ask import API_ERROR, RESTING, SESSION_LIMIT, DailyCounter
from canary.dashboard.chat import ChatResult, Conversation, PageContext, Turn
from canary.dashboard.chat_facts import FactLedger, bank_profile
from canary.dashboard.chatbird import WEB, bird_state, payload, source_line, starters
from canary.dashboard.copy import (CHAT_ASLEEP, CHAT_ASLEEP_PHONE, CHAT_BUBBLE, CHAT_BUBBLE_PHONE, CHAT_EMPTY,
                                   CHAT_GREETING, CHAT_SESSION_DONE, CHAT_STARTERS_GENERAL, CHAT_TOO_LONG)
from tests.dashboard_fixtures import REAL_DATA

TODAY = date(2026, 11, 21)
HOME = PageContext("home")


@pytest.fixture
def real_data(monkeypatch):
    monkeypatch.setenv("CANARY_DASHBOARD_DATA", str(REAL_DATA))


@pytest.fixture
def daily(monkeypatch):
    counter = DailyCounter()
    monkeypatch.setattr(chatbird, "DAILY", counter)
    return counter


def _result(ok=True, text="An answer.", outcome=ask.ANSWERED, cost=0.002, cited=(), lookups=()) -> ChatResult:
    return ChatResult(ok, text, list(cited), list(lookups), cost, outcome, 2, 1, 1200)


# ---- state --------------------------------------------------------------------------------------------------

def test_bird_hidden_awake_asleep():
    assert bird_state(False, False) == "hidden"
    assert bird_state(False, True) == "hidden"
    assert bird_state(True, False) == "awake"
    assert bird_state(True, True) == "asleep"


def test_resting_on_daily_cap_dollar_cap_or_api_error(daily, monkeypatch):
    assert not chatbird.is_resting(TODAY, None)
    assert not chatbird.is_resting(TODAY, _result())
    assert chatbird.is_resting(TODAY, _result(False, RESTING, "error:KeyError"))  # ruling R12
    assert not chatbird.is_resting(TODAY, _result(False, ask.CANT_CHECK, ask.CHECKER_FAILED))
    assert not chatbird.is_resting(TODAY, _result(False, CHAT_EMPTY, chatbird.GUARD))
    assert chatbird.is_resting(TODAY, _result(False, RESTING, f"{API_ERROR}:RateLimitError"))
    daily.add_cost(TODAY, 1.00)
    assert chatbird.is_resting(TODAY, None)
    fresh = DailyCounter(limit=1)
    fresh.take(TODAY)
    monkeypatch.setattr(chatbird, "DAILY", fresh)
    assert chatbird.is_resting(TODAY, None)


# ---- starters -----------------------------------------------------------------------------------------------

def test_starters_bank_page_first():
    s = starters(PageContext("bank", 24735, "Silicon Valley Bank"))
    assert len(s) == 3 and "Silicon Valley Bank" in s[0]
    assert s[1:] == CHAT_STARTERS_GENERAL[1:]
    assert starters(PageContext("home")) == CHAT_STARTERS_GENERAL
    assert starters(PageContext("cases")) == CHAT_STARTERS_GENERAL


def test_starters_never_flagged_vs_flagged_bank(real_data):
    hist = data.scores_history()
    flagged_cert = int(hist[hist["flagged"]]["cert"].iloc[0])
    assert starters(PageContext("bank", 24735, "Silicon Valley Bank"))[0] == "Why wasn't Silicon Valley Bank flagged?"
    assert starters(PageContext("bank", flagged_cert, "Some Bank"))[0] == "How has Some Bank's rank changed?"


# ---- source line --------------------------------------------------------------------------------------------

def test_source_line_from_cited_facts_only(real_data):
    led = FactLedger()
    bank_profile(led, 24735)
    q4 = [f for f in led.facts.values() if f.quarter and f.quarter.isoformat() == "2022-12-31"]
    rank = next(f for f in q4 if f.label == "National rank (1 = highest score)")
    n = next(f for f in q4 if f.label == "Banks ranked that quarter")
    pct = next(f for f in q4 if f.label == "Percentile (100 = highest risk)")
    line = source_line(led, [rank.id, n.id])
    assert line == "Silicon Valley Bank, cert 24735 · 2022-12-31 · rank 3,494 / 4,773"
    assert pct.display not in line and "Percentile" not in line
    assert source_line(led, []) == ""
    assert source_line(led, ["F99999"]) == ""


def test_source_line_caps_pairs_and_names_other_facts():
    led = FactLedger()
    ids = [led.add(f"Label {i}", i, f"{i}.0%", [], "t", date(2022, 12, 31), cert=1, bank="A Bank").id
           for i in range(6)]
    other = led.add("Texas ratio (bad loans vs capital)", 0.5, "50.0%", [], "t", date(2023, 3, 31), cert=2,
                    bank="B Bank").id
    line = source_line(led, ids + [other])
    assert line.startswith("A Bank, cert 1 · B Bank, cert 2 · 2022-12-31 · 2023-03-31 · ")
    assert line.count("Label ") == 4 and "Label 4" not in line and "Texas ratio" not in line
    led2 = FactLedger()
    fid = led2.add("Texas ratio (bad loans vs capital)", 0.5, "50.0%", [], "t", date(2023, 3, 31)).id
    assert source_line(led2, [fid]) == "2023-03-31 · Texas ratio 50.0%"


# ---- payload ------------------------------------------------------------------------------------------------

def test_payload_first_open_greeting_and_starters():
    p = payload("awake", Conversation(), HOME, 0, None)
    assert p["state"] == "awake" and p["bubble"] == CHAT_BUBBLE and p["bubble_phone"] == CHAT_BUBBLE_PHONE
    greeting = CHAT_GREETING.format(report_count=len(data.report_certs()))
    assert p["messages"][0] == {"who": "bird", "text": greeting, "source": "", "lookups": []}
    assert "{" not in greeting
    assert p["starters"] == CHAT_STARTERS_GENERAL
    assert p["left"] == SESSION_LIMIT and p["limit"] == SESSION_LIMIT and p["max_chars"] == ask.MAX_CHARS
    json.dumps(p)  # it goes to the browser as JSON


def test_payload_hides_starters_after_first_question():
    conv = Conversation()
    conv.turns.append(Turn("Who's on the watchlist now?", "Twelve banks.", [], ["Checked the watchlist"]))
    p = payload("awake", conv, HOME, 1, _result())
    assert p["starters"] == []
    who = [(m["who"], m["text"]) for m in p["messages"]]
    assert who == [("bird", chatbird.greeting()), ("me", "Who's on the watchlist now?"), ("bird", "Twelve banks.")]
    assert p["messages"][2]["lookups"] == ["Checked the watchlist"]
    # a question the guards stopped also hides the starters
    assert payload("awake", Conversation(), HOME, 0, _result(False, CHAT_EMPTY, "guard"), question="")["starters"] == []


def test_payload_left_counts_down_and_limit_text():
    conv = Conversation()
    p = payload("awake", conv, HOME, 3, None)
    assert p["left"] == 2 and "2 questions left this visit" in p["footer"]
    assert payload("awake", conv, HOME, 4, None)["footer"].startswith("1 question left this visit ·")  # M5
    assert payload("awake", conv, HOME, 0, None)["footer"].startswith("5 questions left this visit ·")
    done = CHAT_SESSION_DONE.format(limit=SESSION_LIMIT)
    assert done not in json.dumps(p)
    p = payload("awake", conv, HOME, 5, None)
    assert p["left"] == 0 and p["state"] == "awake" and p["messages"][-1]["text"] == done
    assert payload("awake", conv, HOME, 7, None)["left"] == 0


def test_payload_failed_question_and_answer_sources(real_data):
    conv = Conversation()
    bank_profile(conv.ledger, 24735)
    rank = next(f for f in conv.ledger.facts.values() if f.label == "National rank (1 = highest score)"
                and f.quarter.isoformat() == "2022-12-31")
    n = next(f for f in conv.ledger.facts.values() if f.label == "Banks ranked that quarter"
             and f.quarter.isoformat() == "2022-12-31")
    conv.turns.append(Turn("Why wasn't SVB flagged?", "It ranked 3,494 of 4,773.", [rank.id, n.id], []))
    p = payload("awake", conv, HOME, 1, _result(cited=[rank.id, n.id]))
    assert p["messages"][-1]["source"] == "Silicon Valley Bank, cert 24735 · 2022-12-31 · rank 3,494 / 4,773"
    # a failed answer is not a Turn: the payload shows the question and the bird's reply from `last`
    p = payload("awake", conv, HOME, 2, _result(False, ask.CANT_CHECK, ask.CHECKER_FAILED, lookups=["Looked up x"]),
                question="And Signature?")
    assert [m["text"] for m in p["messages"][-2:]] == ["And Signature?", ask.CANT_CHECK]
    assert p["messages"][-1]["lookups"] == ["Looked up x"] and p["messages"][-1]["source"] == ""


def test_payload_asleep_says_resting_once():
    p = payload("asleep", Conversation(), HOME, 0, None)
    assert p["bubble"] == CHAT_ASLEEP and p["bubble_phone"] == CHAT_ASLEEP_PHONE
    assert p["messages"][-1]["text"] == RESTING and p["starters"] == []
    p = payload("asleep", Conversation(), HOME, 1, _result(False, RESTING, f"{API_ERROR}:APIConnectionError"),
                question="Hi")
    assert [m["text"] for m in p["messages"]].count(RESTING) == 1


def test_payload_carries_sprite_and_nonce():
    p = payload("awake", Conversation(), HOME, 0, None, nonce=4)
    assert p["nonce"] == 4
    assert p["sprite"]["grid"] == chatbird.theme.BIRD and p["sprite"]["palette"]["K"] == chatbird.theme.PALETTE["K"]


# ---- the question guards ------------------------------------------------------------------------------------

class _Calls:
    def __init__(self, result=None, exc=None):
        self.result, self.exc, self.calls, self.keys, self.partial = result, exc, [], [], 0.0

    def client(self, key):
        self.keys.append(key)
        return object()

    def ask(self, conv, page, question, client, on_cost=None):
        self.calls.append((page, question))
        if self.exc is not None:
            if not isinstance(self.exc, Exception) and on_cost is not None:
                on_cost(self.partial)  # what chat.ask does before re-raising an interrupt
            raise self.exc
        if self.result.ok:
            conv.turns.append(Turn(question, self.result.text, self.result.cited, self.result.lookups))
        return self.result


class _Lines(logging.Handler):
    def __init__(self) -> None:
        super().__init__(logging.DEBUG)
        self.records: list[logging.LogRecord] = []

    def emit(self, record) -> None:
        self.records.append(record)


@pytest.fixture
def fake(monkeypatch, daily):
    calls = _Calls(_result())
    monkeypatch.setattr(ask, "make_client", calls.client)
    monkeypatch.setattr(chat, "ask", calls.ask)
    handler = _Lines()
    chatbird.log.addHandler(handler)
    calls.log = handler.records
    yield calls
    chatbird.log.removeHandler(handler)


def _send(saved, question, page=HOME):
    return chatbird.handle_question(saved, page, question, "sk-test-not-real", TODAY)


def test_guard_empty_and_too_long_are_not_sent(fake, daily):
    saved: dict = {}
    r = _send(saved, "   ")
    assert r.text == CHAT_EMPTY and not r.ok
    r = _send(saved, "x" * (ask.MAX_CHARS + 1))
    assert r.text == CHAT_TOO_LONG.format(count=ask.MAX_CHARS + 1, limit=ask.MAX_CHARS)
    assert fake.calls == [] and fake.keys == [] and daily.today(TODAY) == (0, 0.0)
    assert saved.get("used", 0) == 0 and saved["nonce"] == 2


def test_guard_visit_limit_before_daily(fake, daily):
    saved = {"used": SESSION_LIMIT}
    r = _send(saved, "One more?")
    assert r.text == CHAT_SESSION_DONE.format(limit=SESSION_LIMIT)
    assert fake.calls == [] and daily.today(TODAY) == (0, 0.0)


def test_guard_dollar_cap_rests_without_taking(fake, daily):
    daily.add_cost(TODAY, 1.00)
    saved: dict = {}
    r = _send(saved, "Hello?")
    assert r.text == RESTING and fake.calls == [] and daily.today(TODAY)[0] == 0 and saved.get("used", 0) == 0


def test_guard_daily_count_rests(fake, monkeypatch):
    full = DailyCounter(limit=0)
    monkeypatch.setattr(chatbird, "DAILY", full)
    r = _send({}, "Hello?")
    assert r.text == RESTING and fake.calls == []


def test_question_sent_counts_costs_logs_and_saves(fake, daily):
    saved: dict = {}
    page = PageContext("bank", 24735, "Silicon Valley Bank")
    r = _send(saved, "  Why wasn't it flagged?  ", page)
    assert r.ok and fake.calls == [(page, "Why wasn't it flagged?")] and fake.keys == ["sk-test-not-real"]
    assert saved["used"] == 1 and daily.today(TODAY) == (1, pytest.approx(0.002))
    conv = Conversation.from_state(saved["conv"])
    assert [t.question for t in conv.turns] == ["Why wasn't it flagged?"]
    assert saved["last"] == asdict(r) and saved["question"] == "Why wasn't it flagged?"
    (rec,) = fake.log
    assert rec.levelno == logging.INFO
    assert rec.getMessage() == ("Ask Canary: outcome=answered calls=2 tools=1 cost=$0.00200; "
                                "today 1/100 questions, $0.0020/$1.00 spent")
    assert "flagged" not in rec.getMessage() and "sk-test" not in rec.getMessage()


def test_try_again_outcome_keeps_the_bird_awake(fake, daily):
    """I1 (ruling R15): a per-question failure says try again and the bird stays awake."""
    fake.result = _result(False, ask.TRY_AGAIN, ask.TURN_LIMIT)
    saved: dict = {}
    r = _send(saved, "Hello?")
    assert r.text == ask.TRY_AGAIN != RESTING
    assert not chatbird.is_resting(TODAY, chatbird._last(saved)) and daily.available(TODAY)
    p = payload("awake", Conversation(), HOME, saved["used"], chatbird._last(saved), "Hello?")
    assert p["messages"][-1]["text"] == ask.TRY_AGAIN and RESTING not in json.dumps(p) and p["can_ask"]


@pytest.mark.parametrize("outcome", ["api_error:AuthenticationError:account", "api_error:BadRequestError:account"])
def test_account_error_rests_the_whole_day(fake, daily, outcome):
    """M3 (ruling R17): a key, permission or balance error puts every visitor's bird to sleep until tomorrow."""
    fake.result = _result(False, RESTING, outcome, cost=0.0)
    _send({}, "Hello?")
    assert not daily.available(TODAY)
    assert chatbird.is_resting(TODAY, None)  # a different visitor
    r = _send({}, "Anyone there?")
    assert r.text == RESTING and r.outcome == chatbird.DAILY_REST and len(fake.calls) == 1
    assert daily.available(date(2026, 11, 22))


def test_other_api_error_rests_only_this_visit(fake, daily):
    fake.result = _result(False, RESTING, f"{API_ERROR}:RateLimitError", cost=0.0)
    _send({}, "Hello?")
    assert daily.available(TODAY)


class _Interrupt(BaseException):
    """Stands in for Streamlit's RerunException / StopException."""


def test_interrupt_still_counts_the_billed_cost(fake, daily):
    """M2: a rerun or stop raised while chat.ask runs re-raises, but the billed cost reaches DAILY first."""
    fake.exc, fake.partial = _Interrupt(), 0.003
    with pytest.raises(_Interrupt):
        _send({}, "Hello?")
    assert daily.today(TODAY) == (1, pytest.approx(0.003))


def test_oversize_question_is_stored_and_shown_truncated(fake, daily):
    """M9: a forged trigger longer than MAX_CHARS is refused and only its first MAX_CHARS are kept."""
    saved: dict = {}
    r = _send(saved, "y" * 5000)
    assert r.text == CHAT_TOO_LONG.format(count=5000, limit=ask.MAX_CHARS) and fake.calls == []
    assert saved["question"] == "y" * ask.MAX_CHARS
    assert saved["notices"][-1]["question"] == "y" * ask.MAX_CHARS


def test_failed_answer_logs_warning_and_api_error_puts_bird_to_sleep(fake, daily):
    fake.result = _result(False, RESTING, f"{API_ERROR}:RateLimitError", cost=0.0)
    saved: dict = {}
    r = _send(saved, "Hello?")
    assert r.outcome == f"{API_ERROR}:RateLimitError" and saved["used"] == 1
    assert fake.log[-1].levelno == logging.WARNING
    assert chatbird.is_resting(TODAY, chatbird._last(saved))


def test_unexpected_exception_rests_and_logs_its_type(fake, daily):
    fake.exc = KeyError("boom-secret")
    saved: dict = {}
    r = _send(saved, "Hello?")
    assert not r.ok and r.text == RESTING and r.outcome == "error:KeyError"
    assert fake.log[-1].levelno == logging.WARNING and "outcome=error:KeyError" in fake.log[-1].getMessage()
    assert "boom-secret" not in fake.log[-1].getMessage()
    assert saved["used"] == 1 and daily.today(TODAY)[0] == 1
    assert chatbird.is_resting(TODAY, chatbird._last(saved))
    state = bird_state(True, chatbird.is_resting(TODAY, chatbird._last(saved)))
    p = payload(state, Conversation(), HOME, saved["used"], chatbird._last(saved))
    assert p["state"] == "asleep" and not p["can_ask"]


def test_error_result_cost_counts_toward_the_daily_cap(fake, daily):
    """chat.ask returns error:* with the partial cost of calls already billed (ruling R12): it is added to DAILY
    and the bird sleeps, so the same failure can't be re-triggered for free."""
    fake.result = _result(False, RESTING, "error:KeyError", cost=0.004)
    saved: dict = {}
    _send(saved, "Hello?")
    assert daily.today(TODAY) == (1, pytest.approx(0.004))
    assert "cost=$0.00400" in fake.log[-1].getMessage() and fake.log[-1].levelno == logging.WARNING
    assert chatbird.is_resting(TODAY, chatbird._last(saved))
    r = _send(saved, "Again?")
    assert r.text == RESTING and len(fake.calls) == 1  # asleep: nothing more is sent this visit


def test_client_failure_rests_without_using_the_day(fake, daily, monkeypatch):
    def broken(key):
        raise ImportError("no anthropic")
    monkeypatch.setattr(ask, "make_client", broken)
    saved: dict = {}
    r = _send(saved, "Hello?")
    assert r.text == RESTING and r.outcome == "error:ImportError" and fake.calls == []
    assert daily.today(TODAY) == (0, 0.0)
    assert "outcome=error:ImportError calls=0 tools=0 cost=$0.00000" in fake.log[-1].getMessage()
    assert chatbird.is_resting(TODAY, chatbird._last(saved))


# ---- mounting -----------------------------------------------------------------------------------------------

_MISSING = object()


def _flag(monkeypatch, value) -> None:
    monkeypatch.setattr(chatbird, "_secret", lambda name: None if value is _MISSING else value)


@pytest.mark.parametrize("flag", [False, "false", "False", "", "no", "yes", 1, None, _MISSING])
def test_ask_enabled_off(monkeypatch, flag):
    """I2: the kill switch is off for anything but true or "true"."""
    _flag(monkeypatch, flag)
    assert chatbird._enabled() is False


@pytest.mark.parametrize("flag", [True, "true", "TRUE", " true "])
def test_ask_enabled_on(monkeypatch, flag):
    _flag(monkeypatch, flag)
    assert chatbird._enabled() is True


@pytest.mark.parametrize("secrets", [{}, {"ASK_ENABLED": True}, {"ASK_ENABLED": "false", "ANTHROPIC_API_KEY": "k"},
                                     {"ASK_ENABLED": True, "ANTHROPIC_API_KEY": "  "}])
def test_render_chat_draws_nothing_when_off_or_keyless(monkeypatch, secrets):
    monkeypatch.setattr(chatbird, "_secret", lambda name: secrets.get(name))

    def no_mount(*a, **k):
        raise AssertionError("mounted while off")
    monkeypatch.setattr(chatbird, "_component", no_mount)
    chatbird.render_chat(HOME)


# ---- the browser side ---------------------------------------------------------------------------------------

def test_js_has_states_and_reduced_motion():
    js = (WEB / "chatbird.js").read_text()
    css = (WEB / "chatbird.css").read_text()
    assert "asleep" in js and "prefers-reduced-motion" in css and "max-width: 599px" in css
    assert "innerHTML" not in js.split("function renderMessage")[1].split("function")[0]  # model text set via textContent


def test_corner_canary_sits_bottom_left():
    """Bottom-left: Streamlit Cloud's "Manage app" button covers the bottom-right corner."""
    css = (WEB / "chatbird.css").read_text()
    root = css.split(".cb {", 1)[1].split("}", 1)[0]
    assert "left:var(--inset-l)" in root and "right:" not in root
    panel = css.split(".panel {", 1)[1].split("}", 1)[0]
    assert "left:var(--inset-l)" in panel and "right:" not in panel


def test_js_accessibility_and_storage_guards():
    js = (WEB / "chatbird.js").read_text()
    assert "aria-label" in js and "Escape" in js and "sessionStorage" in js and "focus()" in js
    text = payload("awake", Conversation(), HOME, 0, None)["text"]
    assert text["open"] == "Open Ask Canary" and text["placeholder"] == "Ask about any bank..."
    for line in js.splitlines():
        if "sessionStorage" in line:
            assert "try" in line, line  # every storage access is wrapped
    assert "innerHTML" not in js  # nothing is ever parsed as HTML
    assert "setTriggerValue('question'" in js
    # M6: the launcher says when the bird is asleep, and the close X is a 44px tap target
    asleep = payload("asleep", Conversation(), HOME, 0, None)["text"]
    assert asleep["open_asleep"] == "Ask Canary is resting"
    assert "asleep ? t.open_asleep : t.open" in js
    css = (WEB / "chatbird.css").read_text()
    x_rule = css.split(".cb .x {", 1)[1].split("}", 1)[0]
    assert "min-width:44px" in x_rule and "min-height:44px" in x_rule


def test_js_wait_limit_outlasts_the_python_worst_case():
    """M11: the browser keeps its thinking state longer than two attempts of MAX_TURNS calls at the timeout."""
    js = (WEB / "chatbird.js").read_text()
    wait_ms = int(re.search(r"const WAIT_LIMIT_MS = (\d+);", js).group(1))
    worst_ms = 2 * chat.MAX_TURNS * ask.CLIENT_TIMEOUT_S * 1000
    assert wait_ms >= worst_ms + 60_000  # a minute's margin for the lookups and the page
