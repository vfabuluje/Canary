"""Ask Canary's shared rules (spec 5.6): the limits, the outcome categories, the daily counter and the answer checks.

The chat engine (chat.py) asks the model and runs the citation checker; this module holds what it and the corner
canary (chatbird.py) share: the model settings and limits, the outcome names chatbird logs (never the question or
the answer), the daily counter, and the two extra answer checks the chat adds to the citation checker. Those reject
a link or web address, a forecast ("predicts", "is likely to fail", "the bank is safe") or advice ("you should
withdraw"), and allow the reports' own caveats ("not a prediction", "warning signs") (ruling R23: the question is
untrusted visitor text).

Only `make_client` imports `anthropic` (so the app runs without the package or a key); `account_error` tells the
SDK's key and balance errors apart by class name. The spending guards' numbers live here; chatbird enforces them
(and hides the bird entirely while Ask is switched off or has no key, ruling R22).
"""

import re
import threading
from datetime import date

from canary.analyst.sections import Section
from canary.analyst.writer import cost_usd  # noqa: F401 (re-exported: the tests price calls with ask.cost_usd)
from canary.dashboard.copy import ASK_CANT_CHECK, ASK_RESTING, ASK_TRY_AGAIN

ASK_MODEL = "claude-haiku-5-5"
SESSION_LIMIT = 5  # questions per visitor session
DAILY_LIMIT = 100  # questions per UTC day, whole app (about $1 at about $0.01 a question)
DAILY_USD_LIMIT = 1.00  # dollars per UTC day, whole app; the counter also stops at this
MAX_CHARS = 300  # longest question accepted
# Haiku 5.5 thinks by default (adaptive) and thinking counts against max_tokens, so leave room beyond the short
# answer itself; a reply that still runs out is logged as "truncated".
MAX_TOKENS = 4000
EFFORT = "low"
CLIENT_TIMEOUT_S = 60.0

RESTING = ASK_RESTING
CANT_CHECK = ASK_CANT_CHECK
TRY_AGAIN = ASK_TRY_AGAIN

ANSWER_SECTION = Section(
    "answer", "Answer", "hindsight",
    "Answer the visitor's question in one to three short paragraphs, using only the fact sheet.", True)

# Outcome categories for the log (chatbird): never the question or the answer text.
ANSWERED = "answered"
CHECKER_FAILED = "checker_failed"  # both tries broke a checker rule
REFUSAL = "refusal"
TRUNCATED = "truncated"  # stop_reason max_tokens
BAD_JSON = "bad_json"  # not JSON, or JSON that isn't the answer shape
TURN_LIMIT = "turn_limit"  # the chat ran out of model turns
TOKEN_CEILING_HIT = "token_ceiling"  # the chat hit its token ceiling
NO_SUBMIT = "no_submit"  # the chat ended without submitting an answer
API_ERROR = "api_error"  # followed by ":" and the exception type, e.g. "api_error:RateLimitError"
# Added after an API error's type when the account itself can't be used (a bad or revoked key, no permission, or
# the prepaid credit balance used up): "api_error:AuthenticationError:account". The whole day then rests (R17).
ACCOUNT_MARK = ":account"
_ACCOUNT_ERRORS = ("AuthenticationError", "PermissionDeniedError")


def account_error(exc: BaseException) -> bool:
    """True for an SDK error no retry can fix today: authentication, permission, or a credit-balance refusal.
    By class name, so this module still never imports anthropic outside make_client."""
    name = type(exc).__name__
    return name in _ACCOUNT_ERRORS or (name == "BadRequestError" and "credit balance" in str(exc).lower())


class DailyCounter:
    """Questions sent today across every visitor session (the process), and what they cost. Resets on a new
    UTC date. It lives in memory, so a reboot, redeploy or app sleep also starts it again from zero."""

    def __init__(self, limit: int = DAILY_LIMIT, usd_limit: float = DAILY_USD_LIMIT) -> None:
        self.limit = limit
        self.usd_limit = usd_limit
        self._lock = threading.Lock()
        self._day: date | None = None
        self._count = 0
        self._spent = 0.0
        self._rest_day: date | None = None

    def _roll(self, today: date) -> None:
        if today != self._day:
            self._day, self._count, self._spent = today, 0, 0.0

    def add_cost(self, today: date, usd: float) -> None:
        with self._lock:
            self._roll(today)
            self._spent += usd

    def today(self, today: date) -> tuple[int, float]:
        """(questions sent, dollars spent) so far today."""
        with self._lock:
            self._roll(today)
            return self._count, self._spent

    def rest(self, today: date) -> None:
        """Close the rest of this UTC day (ruling R17: the key or the balance can't be used)."""
        with self._lock:
            self._rest_day = today

    def available(self, today: date) -> bool:
        with self._lock:
            self._roll(today)
            return self._rest_day != today and self._count < self.limit and self._spent < self.usd_limit

    def take(self, today: date) -> bool:
        """Use one of today's questions; False (and nothing used) once the day's limit is reached."""
        with self._lock:
            self._roll(today)
            if self._rest_day == today or self._count >= self.limit:
                return False
            self._count += 1
            return True


def make_client(api_key: str):
    """The real Anthropic client. Never called in tests (they pass fakes)."""
    import anthropic  # optional dependency group "analyst"; only this module imports it

    # No SDK retries: every billed call must go through the daily counter.
    return anthropic.Anthropic(api_key=api_key, timeout=CLIENT_TIMEOUT_S, max_retries=0)


# Links and web addresses, plain or as Markdown links/images: never part of an answer from the fact table.
_LINK = re.compile(r"https?://|\bwww\.|!\[|\]\s*\(", re.IGNORECASE)


def link_errors(memo: dict) -> list[str]:
    return [f"section 'answer', sentence \"{s.get('text', '')[:100]}\": contains a link or web address; "
            "answer in plain sentences without links"
            for sec in memo.get("sections", []) for p in sec.get("paragraphs", []) for s in p.get("sentences", [])
            if _LINK.search(str(s.get("text", "")))]


# Ask's own forecast/advice rule. The written reports' trend and peer sections ban "warning" and "predict"
# outright; Ask answers may repeat the reports' own caveats, so this rule removes those first and then rejects
# what actually forecasts or advises.
_CAVEAT = re.compile(
    # "not a prediction that any bank will fail": the disclaimer whole, before its shorter "not a prediction"
    r"\b(?:(?:is|are|was)\s+)?not\s+an?\s+(?:prediction|forecast)\s+that\s+(?:any|a|the|this|that)\s+banks?"
    r"\s+will\s+fail\b(?=\s*[.!]?\s*$)"  # only as the sentence's end: nothing after it to swallow
    r"|\b(?:(?:is|are|was)\s+)?not\s+an?\s+(?:prediction|forecast)(?:\s+or\s+(?:an?\s+)?(?:prediction|forecast))?\b"
    r"|\b(?:does\s+not|doesn't|do\s+not|don't|cannot|can't|won't)\s+(?:make|give|offer)\s+(?:any\s+)?"
    r"(?:predictions|forecasts)\b"
    r"|\b(?:cannot|can't|can\s+not|won't)\s+advise\s+(?:you\s+)?(?:on\s+)?(?:whether\s+to\s+)?"
    r"(?:(?:move|moving)\s+your\s+money|(?:withdraw|withdrawing)\s+your\s+(?:money|savings|deposits))\b"
    r"|\b(?:does\s+not|doesn't|did\s+not|didn't|cannot|can't|can\s+not|could\s+not|couldn't)\s+"
    r"(?:predict|forecast|foresee)\b"
    r"|\bwarning\s+(?:signs?|signals?|lights?|flags?)\b(?!\s+of\s+(?:coming\s+|impending\s+)?fail)"
    r"|\bearly[- ]warning\s+system\b"
    # "I can't tell whether it will fail / is safe": a refusal to forecast, not a forecast
    r"|\bwhether\s+(?:(?!\b(?:and|but|so)\b)[\w']+\s+){0,4}?(?:will|could|might|may|would|is going to|is likely to)"
    r"\s+(?:(?:still|ever|not|eventually)\s+)*(?:fail|collapse|go under|be closed|survive)\b"
    r"|\bwhether\s+(?:the bank|this bank|it|its deposits|your (?:money|deposits|savings))\s+"
    r"(?:is|are|looks|seems|remains|stays)\s+(?:\w+\s+)?(?:safe|safer|sound|healthy|secure)\b"
    # the score's horizon or catch rule, as a condition: "if the bank fails within", "the risk that it fails within"
    r"|\b(?:if|when|whether|(?<=\brisk\s)that)\s+(?:(?:the|a|this|that|any)\s+)?(?:bank|it)\s+"
    r"(?:fails|collapses)\s+within\b",
    re.IGNORECASE)
_FORECAST = re.compile(
    r"\bpredict\w*|\bforecast\w*|\bforesaw\b|\bforesee\w*|\bforeshadow\w*"
    r"|\bwarn(?:s|ed)?\b|\bwarning\b|\bearly[- ]warning\b"
    r"|\bwould have (?:caught|flagged|warned)\b|\bshould have (?:caught|flagged|been flagged)\b"
    r"|\bsign(?:al)?s? of (?:coming |impending )?failure\b"
    r"|\b(?:will|could|might|may|is going to|are going to|is about to|is likely to|are likely to|likely to"
    r"|(?:is|are)\s+(?:bound|sure|certain)\s+to)"
    r"\s+(?:(?:likely|probably|soon|eventually|still|not|never|definitely|certainly|surely)\s+)*"
    r"(?:fail|collapse|go under|be closed|survive)\b"
    # present-tense forecasts: "goes under in March", "fails next quarter", "collapses within a year"
    r"|\bgoes\s+under\s+(?:soon|next|in|within)\b"
    r"|\b(?:fails|collapses)\s+(?:soon|next\s+(?:week|month|quarter|year)|within)\b"
    # certainty about a failure: "doomed", "it is (almost) certain that this bank fails", "certainly fail"
    r"|\bdoomed\b|\bcertain\s+(?:that|to)\b[^.;]*?\b(?:fail|collaps)\w*|\bcertainly\s+(?:fail|collapse)\w*"
    r"|(?<!whether )(?<!if )\b(?:the bank|this bank|it|its deposits|your (?:money|deposits|savings))"
    r"\s+(?:is|are|looks|seems|remains|stays)\s+(?:\w+\s+)?(?:safe|safer|sound|healthy|secure)\b"
    r"|\bsafe\s+(?:bank|place)\b|\bsafe\s+to\s+(?:deposit|bank|keep|invest)\b",
    re.IGNORECASE)
_ADVICE = re.compile(
    r"\b(?:you|depositors|customers|savers|investors|people|anyone|everyone)\s+"
    r"(?:should|must|need\s+to|ought\s+to|may\s+want\s+to|might\s+want\s+to)\b"
    r"|\bI\s+(?:would\s+)?(?:recommend|advise|suggest)\b"
    # "move it" is advice, except "move it up/down/higher/lower" and the ranking phrases "onto the watchlist",
    # "into the riskiest/top ...", "toward(s)/to the top"
    r"|\bmove\s+it\b(?!\s+(?:up|down|higher|lower)\b)"
    r"(?!\s+(?:onto\s+the\s+watchlist|into\s+the\s+(?:riskiest|top)|towards?\s+the\s+top|to\s+the\s+top)\b)"
    r"|\b(?:consider|please|best\s+to|better\s+to|go\s+ahead\s+and)\s+mov(?:e|ing)\s+it\b"
    r"|\bwithdrawing\s+(?:all\s+)?(?:your|their)\s+(?:money|savings|deposits)\b"
    r"|\b(?:withdraw|move|pull|sell|buy|transfer)\s+(?:all\s+)?(?:your|their)\s+"
    r"(?:money|deposits|savings|funds|shares|stock)\b",
    re.IGNORECASE)


def _sentences(memo: dict):
    for sec in memo.get("sections", []):
        for p in sec.get("paragraphs", []):
            for s in p.get("sentences", []):
                yield str(s.get("text", ""))


def wording_errors(memo: dict) -> list[str]:
    """Ask's forecast/advice rule, applied to every sentence after removing the reports' allowed caveats."""
    errors = []
    for text in _sentences(memo):
        where = f"section 'answer', sentence \"{text[:100]}\""
        rest = _CAVEAT.sub(" ", text)
        if m := _FORECAST.search(rest) or _ADVICE.search(rest):
            errors.append(f"{where}: gives advice or a forecast ('{m.group(0)}'); describe only what the data "
                          "shows, never what the visitor should do or what will happen")
    return errors


def _text(memo: dict) -> str:
    paragraphs = []
    for sec in memo.get("sections", []):
        for para in sec.get("paragraphs", []):
            words = " ".join(str(s.get("text", "")).strip() for s in para.get("sentences", []))
            if words.strip():
                paragraphs.append(words.strip())
    return "\n\n".join(paragraphs)
