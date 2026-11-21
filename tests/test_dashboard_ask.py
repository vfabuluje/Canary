"""Ask Canary's shared rules: the wording and link checks, the limits and the daily counter.

The chat engine (chat.py) and the corner canary (chatbird.py) use these; their own tests are
test_dashboard_chat*.py. Fake clients only: no test here (or anywhere) makes a real Anthropic call.
"""

import threading
from datetime import date

import pytest

from canary.dashboard import ask
from canary.dashboard.ask import (ANSWER_SECTION, ASK_MODEL, DAILY_LIMIT, MAX_CHARS, RESTING, SESSION_LIMIT,
                                  DailyCounter, link_errors, wording_errors)

REAL_MAKE_CLIENT = ask.make_client


def _memo(*sentences: tuple[str, list[str]]) -> dict:
    return {"sections": [{"key": "answer", "paragraphs": [
        {"sentences": [{"text": t, "cites": c} for t, c in sentences]}]}]}


@pytest.mark.parametrize("text", [
    "See https://example.com for more.",
    "See http://example.com for more.",
    "See www.example.com for more.",
    "Read [the report](javascript:alert(1)) first.",
    "Here is a picture: ![bank](x.png)",
])
def test_answer_with_a_link_is_rejected(text):
    assert link_errors(_memo((text, [])))


@pytest.mark.parametrize("text", [
    "Canary predicted this bank's trouble.",
    "The model forecasts trouble for this bank.",
    "Its filings showed signs of failure.",
    "Its filings showed warning signs of failure.",
    "The report shows warning signs of impending failure.",
    "The data warned of trouble ahead.",
    "The bank will fail within a year.",
    "It is going to fail.",
    "It is likely to fail.",
    "This bank could fail soon.",
    "The bank might collapse.",
    "The bank is safe.",
    "This bank is perfectly safe.",
    "It is not safe.",
    "Your deposits are safe here.",
    "It is a safe bank.",
    "You should withdraw your money now.",
    "Depositors should move their savings elsewhere.",
    "Withdraw your money while you can.",
    "It is safe to deposit here.",
    "I can't tell whether it will fail, but it will fail soon.",
    "Nobody knows whether it is safe, but you should move your money.",
    "I would recommend another bank.",
    # smoke-test fix, cause 4: the disclaimer is allowed, a forecast after it is not
    "This is not a prediction that any bank will fail, but this one will fail.",
    "It is not a prediction of whether any bank will fail, but the bank will fail soon.",
    "This is not a prediction that the bank will not fail.",
    # fix round 1: the disclaimer must end the sentence, and certainty wording is a forecast
    "Canary's flag is not a prediction that this bank will fail: it is a certainty.",
    "This is not a prediction that the bank will fail, it is a fact.",
    "Is it not a prediction that this bank will fail?",
    "This bank is doomed.",
    "it is certain that this bank fails next year",
    "The score is not a prediction; it is certain that this bank fails next year.",
    "It is almost certain to fail.",
    "The bank will definitely fail.",
    "This bank will surely collapse.",
    "It is bound to fail.",
    "The bank is sure to fail.",
    "It will certainly fail within a year.",
])
def test_prediction_or_advice_is_rejected(text):
    assert wording_errors(_memo((text, [])))


@pytest.mark.parametrize("text", [
    "The bank failed on its own; regulators closed it.",
    "Uninsured deposits can leave quickly, because they are above the FDIC's insurance limit.",
    "I can't tell from this bank's data whether it is safe.",
    "I can't tell from this bank's data whether it will fail, and I can't advise you on moving your money.",
    "Canary does not say whether Silicon Valley Bank will ever fail.",
    "The data cannot show whether your deposits are safe.",
    "Canary's score is not a prediction; it ranks banks by risk.",
    "Canary is not a forecast of what will happen.",
    "The model cannot predict a run on deposits.",
    "The report lists several warning signs in the bank's filings.",
    "Canary is a bank failure early-warning system.",
    "That money is not protected if the bank fails, so it can leave quickly.",
    "Banks should keep enough capital to absorb losses.",
    "It will help to know that the FDIC insures deposits up to its limit.",
    # smoke-test fix, cause 4: honest disclaimers the paid smoke test wrongly rejected (the first is verbatim)
    "The watchlist covers the riskiest 2% of banks Canary ranks, so it is a list of banks flagged for closer "
    "attention, not a prediction that any bank will fail.",
    "Canary's rank is not a prediction that this bank will fail.",
    "A flag is not a forecast that a bank will fail.",
    "The list is not a prediction that any banks will fail.",
    "The score is not a prediction of whether any bank will fail.",
    "Canary's rank is not a prediction about whether this bank will fail.",
    "I can't tell for certain whether this bank will fail.",
    "Canary missed certain failures in 2023.",
])
def test_plain_wording_is_not_mistaken_for_advice(text):
    assert wording_errors(_memo((text, []))) == []


def test_answer_section_allows_hindsight():
    assert ANSWER_SECTION.key == "answer" and ANSWER_SECTION.window == "hindsight" and ANSWER_SECTION.ai_written


def test_haiku_has_a_price():
    from canary.analyst.writer import PRICES, cost_usd
    assert PRICES[ASK_MODEL] == (0.10, 0.50)
    assert cost_usd(ASK_MODEL, 100_000, 100_000) == pytest.approx(0.06)


def test_haiku_long_prompt_price():
    """C1: a Haiku request over 100,000 input tokens is billed $0.50 in / $2.50 out per million."""
    from canary.analyst.writer import LONG_PROMPT, cost_usd
    assert LONG_PROMPT[ASK_MODEL] == (100_000, (0.50, 2.50))
    assert cost_usd(ASK_MODEL, 150_000, 1_000) == pytest.approx((150_000 * 0.50 + 1_000 * 2.50) / 1e6)
    assert cost_usd(ASK_MODEL, 100_000, 1_000) == pytest.approx((100_000 * 0.10 + 1_000 * 0.50) / 1e6)
    assert cost_usd("claude-opus-5-5", 150_000, 1_000) == pytest.approx((150_000 * 4.0 + 1_000 * 20.0) / 1e6)
    assert cost_usd("claude-sonnet-5-5", 150_000, 0) == pytest.approx(150_000 * 2.0 / 1e6)


def test_make_client_builds_without_calling():
    import anthropic
    client = REAL_MAKE_CLIENT("sk-test-not-real")  # constructed only, never called
    assert isinstance(client, anthropic.Anthropic)
    assert client.api_key == "sk-test-not-real" and client.max_retries == 0  # every billed call passes the daily counter


def test_limits():
    assert (SESSION_LIMIT, DAILY_LIMIT, MAX_CHARS) == (5, 100, 300)
    assert RESTING == "Ask Canary is resting for today."


# ------------------------------------------------------------------------------------------- DailyCounter

def test_daily_limit_is_100():
    assert ask.DAILY_LIMIT == 100


def test_dollar_limit_blocks_at_one_dollar():
    c = ask.DailyCounter(limit=100, usd_limit=1.00)
    d = date(2026, 11, 21)
    c.add_cost(d, 0.9999)
    assert c.available(d)
    c.add_cost(d, 0.0001)
    assert not c.available(d)
    assert c.available(date(2026, 11, 22))  # new UTC day resets


def test_take_is_atomic_at_the_limit():
    c = ask.DailyCounter(limit=1)
    d = date(2026, 11, 21)
    results = []
    ts = [threading.Thread(target=lambda: results.append(c.take(d))) for _ in range(8)]
    [t.start() for t in ts]
    [t.join() for t in ts]
    assert results.count(True) == 1


def test_public_checks_keep_old_behaviour():
    memo = {"sections": [{"key": "answer", "paragraphs": [{"sentences": [
        {"text": "It is likely to fail.", "cites": []}]}]}]}
    assert ask.wording_errors(memo)
    ok = {"sections": [{"key": "answer", "paragraphs": [{"sentences": [
        {"text": "I can't tell from the data whether it will fail.", "cites": []}]}]}]}
    assert ask.wording_errors(ok) == []
    assert ask.link_errors({"sections": [{"paragraphs": [{"sentences": [{"text": "see https://x.com"}]}]}]})


def test_new_outcome_constants():
    assert (ask.TURN_LIMIT, ask.TOKEN_CEILING_HIT, ask.NO_SUBMIT) == ("turn_limit", "token_ceiling", "no_submit")

def test_daily_counter_rest_closes_the_day():
    """M3: rest(today) makes the rest of that UTC day unavailable; the next day starts fresh."""
    c = ask.DailyCounter()
    d = date(2026, 11, 21)
    assert c.available(d)
    c.rest(d)
    assert not c.available(d) and not c.take(d) and c.today(d) == (0, 0.0)
    assert c.available(date(2026, 11, 22)) and c.take(date(2026, 11, 22))


def test_try_again_copy():
    """I1: per-question failures get their own line; resting is only for a sleeping bird."""
    assert ask.TRY_AGAIN == "I couldn't answer that one. Try asking it another way."
    assert ask.TRY_AGAIN not in (ask.RESTING, ask.CANT_CHECK)


def test_daily_counter_stops_at_limit():
    counter, today = DailyCounter(limit=3), date(2026, 11, 20)
    assert [counter.take(today) for _ in range(5)] == [True, True, True, False, False]
    assert not counter.available(today)


def test_daily_counter_resets_next_day():
    counter = DailyCounter(limit=2)
    assert counter.take(date(2026, 11, 20)) and counter.take(date(2026, 11, 20))
    assert not counter.take(date(2026, 11, 20))
    assert counter.available(date(2026, 11, 21))
    assert counter.take(date(2026, 11, 21))


def test_daily_counter_default_limit():
    counter, today = DailyCounter(), date(2026, 11, 20)
    assert sum(counter.take(today) for _ in range(DAILY_LIMIT + 5)) == DAILY_LIMIT


def test_daily_counter_tracks_spend_and_resets():
    counter = DailyCounter(limit=5)
    day1, day2 = date(2026, 11, 20), date(2026, 11, 21)
    counter.take(day1)
    counter.add_cost(day1, 0.002)
    counter.take(day1)
    counter.add_cost(day1, 0.003)
    count, spent = counter.today(day1)
    assert count == 2 and spent == pytest.approx(0.005)
    assert counter.today(day2) == (0, 0.0)


def test_daily_counter_is_thread_safe():
    counter, today, results = DailyCounter(limit=50), date(2026, 11, 20), []
    lock = threading.Lock()

    def worker():
        for _ in range(20):
            got = counter.take(today)
            with lock:
                results.append(got)

    threads = [threading.Thread(target=worker) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert sum(results) == 50


# ---- fix round 3: honest disclaimers and refusals from the second paid smoke run --------------------------------

@pytest.mark.parametrize("text", [
    "The score is a ranking tool and not a prediction or forecast of any specific bank's failure.",
    "I can't tell from Canary's data whether Wells Fargo will fail, and Canary does not make predictions about any "
    "bank.",
    "I also can't advise you on whether to move your money; that is outside what Canary covers.",
    "Canary doesn't give forecasts.",
    "I cannot advise moving your money.",
])
def test_round3_disclaimers_pass(text):
    assert wording_errors(_memo((text, []))) == []


@pytest.mark.parametrize("text", [
    "Canary makes predictions: this bank will fail.",
    "You should move your money.",
    "I can't advise you, but you should move your money.",
    "Canary does not make predictions, but this bank will fail.",
    "It is not a prediction or forecast; it is doomed.",
    "I can't advise on whether to move your money, so move your money now.",
])
def test_round3_forecasts_and_advice_still_fail(text):
    assert wording_errors(_memo((text, [])))


# ---- fix round 4: present-tense forecasts and plain advice --------------------------------------------------------

@pytest.mark.parametrize("text", [
    "Wells Fargo goes under in March.",
    "The bank fails next quarter.",
    "This bank collapses within a year.",
    "It fails soon.",
    "Your deposits are at risk, so move it.",
    "Move it out now.",
    "Withdrawing your savings is the obvious step.",
])
def test_round4_forecasts_and_advice_fail(text):
    assert wording_errors(_memo((text, [])))


@pytest.mark.parametrize("text", [
    "I can't advise you on moving your money.",
    "I can't advise you on withdrawing your savings.",
    "I can't tell whether it will fail.",
    "SVB failed on March 10, 2023.",
    "The bank collapsed in 2023.",
    "A higher score would move it up the ranking.",
    "That money is not protected if the bank fails, so it can leave quickly.",
])
def test_round4_history_and_refusals_pass(text):
    assert wording_errors(_memo((text, []))) == []


# ---- fix round 5: definitions of the horizon and ranking descriptions are not forecasts or advice -----------------

@pytest.mark.parametrize("text", [
    "Canary ranks every bank by the risk that it fails within the next four quarters.",
    "A flag counts only if the bank fails within the next four quarters.",
    "A bank counts as caught when it fails within four quarters of being flagged.",
    "A higher score would move it onto the watchlist.",
    "A higher score would move it into the riskiest 2%.",
    "A higher score would move it toward the top of the ranking.",
])
def test_round5_definitions_pass(text):
    assert wording_errors(_memo((text, []))) == []


@pytest.mark.parametrize("text", [
    "The bank fails within a year.",
    "Wells Fargo collapses within four quarters.",
    "It fails soon.",
    "It is certain that it fails within a year.",
    "Move it out now.",
    "Your deposits are at risk, so move it.",
    "Move it elsewhere.",
    "move it out now",
    "Move it into a safer bank.",
])
def test_round5_forecasts_and_commands_still_fail(text):
    assert wording_errors(_memo((text, [])))
