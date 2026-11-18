"""The `ask` agent (spec 6): Claude picks among four local tools; the SDK's tool runner loops locally."""

from anthropic import beta_tool

from canary.analyst import tools
from canary.analyst.writer import DEFAULT_MODEL, EFFORT, MAX_TOKENS, PRICES, cost_usd

SYSTEM = """You are Canary's risk analyst. Canary ranks every FDIC-insured US bank by a machine-learning \
score of its risk of failing within the next 4 quarters, and answers questions about banks in plain English.

Rules:
- Answer only from tool results. Do not add outside knowledge about banks, news or causes.
- Use find_bank to turn a name, city or certificate number into a cert before asking for facts. If several \
banks match, list them and ask which one is meant; do not guess.
- Use get_bank_facts for numbers about one bank, and list_watchlist for the current or a past top-2% list.
- For anything memo-sized (a full write-up of a bank), call write_memo and report the saved path; do not \
write the memo yourself.
- The score ranks banks against each other; it is not a probability of failure. Describe banks by rank.
- If the data cannot answer the question, say so plainly."""

REFUSAL_LINE = "Sorry, I can't help with that request."
MAX_ITERATIONS = 10  # model turns per question; stops a runaway tool loop
STOPPED_LINE = f"(Stopped after {MAX_ITERATIONS} steps without a final answer.)"


def make_tools(ctx, client, model: str) -> list:
    @beta_tool
    def find_bank(query: str, state: str | None = None, failed_year: int | None = None) -> str:
        """Find banks by name, certificate number, or (for failed banks) city. Returns up to 10 matches.

        Args:
            query: Bank name fragment, FDIC certificate number (digits), or city of a failed bank.
            state: Optional two-letter state code to narrow the matches.
            failed_year: Optional year the bank failed, to narrow the matches.
        """
        return tools.find_bank(ctx, query, state, failed_year)

    @beta_tool
    def get_bank_facts(cert: int, as_of: str | None = None) -> str:
        """Get the cited facts, national rank and outcome for one bank as of a quarter.

        Args:
            cert: FDIC certificate number of the bank.
            as_of: Optional quarter-end date, YYYY-MM-DD; defaults to the latest quarter for an open bank,
                or the last quarter it reported before failing for a failed bank.
        """
        return tools.get_bank_facts(ctx, cert, as_of)

    @beta_tool
    def list_watchlist(quarter: str | None = None) -> str:
        """List the banks on the watchlist (top 2% by score) for a quarter.

        Args:
            quarter: Optional quarter-end date, YYYY-MM-DD; defaults to the latest quarter.
        """
        return tools.list_watchlist(ctx, quarter)

    @beta_tool
    def write_memo(cert: int, as_of: str | None = None) -> str:
        """Write a checked memo note for one bank and save it. Slow and costly; use only for memo requests.

        Args:
            cert: FDIC certificate number of the bank.
            as_of: Optional quarter-end date, YYYY-MM-DD; defaults to the bank's latest quarter.
        """
        return tools.write_memo_tool(ctx, client, model, cert, as_of)

    return [find_bank, get_bank_facts, list_watchlist, write_memo]


def ask_with_usage(question: str, ctx, client, model: str = DEFAULT_MODEL) -> tuple[str, dict]:
    """Answer and the agent's own token usage {input_tokens, output_tokens, cost_usd, model}, summed over
    every model turn (memos written by the write_memo tool are not included)."""
    runner = client.beta.messages.tool_runner(
        model=model,
        max_tokens=MAX_TOKENS,
        system=SYSTEM,
        tools=make_tools(ctx, client, model),
        messages=[{"role": "user", "content": question}],
        output_config={"effort": EFFORT},
        max_iterations=MAX_ITERATIONS,
    )
    usage = {"input_tokens": 0, "output_tokens": 0, "cost_usd": 0.0, "model": model}
    for msg in runner:  # one message per model turn; the runner runs the tools in between
        served = getattr(msg, "model", None) or model
        i, o = msg.usage.input_tokens, msg.usage.output_tokens
        usage["input_tokens"] += i
        usage["output_tokens"] += o
        usage["cost_usd"] += cost_usd(served if served in PRICES else model, i, o)
        usage["model"] = served
    final = runner.until_done()
    if final.stop_reason == "refusal":
        return REFUSAL_LINE, usage
    text = "".join(b.text for b in final.content if b.type == "text").strip()
    if final.stop_reason == "tool_use":  # max_iterations reached mid-loop
        text = (text + "\n" if text else "") + STOPPED_LINE
    return text, usage


def ask(question: str, ctx, client, model: str = DEFAULT_MODEL) -> str:
    return ask_with_usage(question, ctx, client, model)[0]
