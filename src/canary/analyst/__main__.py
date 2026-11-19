"""Risk analyst: python -m canary.analyst ask "question" [--model M], memo --cert N [--as-of YYYY-MM-DD] [--model M] [--out banks],
showcase [--dry-run] [--resume BATCH_ID] [--watchlist-top N] (notes for the showcase set in one batch job), and
compare [--models A,B] (case-study notes with several models, pass rate and cost per model).

Builds the fact sheet from the feature export and the saved model (read only), asks Claude to
write the memo, checks every number, and saves the note only if it passes. Exit codes: 0 written,
1 memo failed the check / refused / truncated / malformed JSON / bad input files / Claude API error
(connection, auth, rate limit), 2 bad cert or as-of date.
ANTHROPIC_API_KEY is read from the environment, then the repo .env, or an `ant auth login` profile.
"""
import argparse
import json
import logging
import os
import sys
from datetime import date
from pathlib import Path

from canary.analyst.context import load_context
from canary.analyst.outcome import default_as_of, validate_as_of
from canary.analyst.writer import DEFAULT_MODEL, RefusalError, TruncatedError, write_memo
from canary.config import REPO_ROOT, _read_dotenv

log = logging.getLogger(__name__)
REPLAY_DIR = Path("data/replay")


NO_KEY = "No Anthropic API key found: set ANTHROPIC_API_KEY in .env or run `ant auth login`"


class NoCredentialsError(RuntimeError):
    """No API key, auth token or credentials profile the SDK can use."""


def make_client():
    import anthropic  # optional dependency group "analyst"

    if not os.environ.get("ANTHROPIC_API_KEY"):
        key = _read_dotenv(REPO_ROOT / ".env").get("ANTHROPIC_API_KEY")
        if key:
            os.environ["ANTHROPIC_API_KEY"] = key
    try:
        client = anthropic.Anthropic()
    except anthropic.CredentialsError as exc:  # e.g. a selected profile whose config file is missing
        raise NoCredentialsError(f"{NO_KEY} ({exc})") from exc
    # The SDK resolves api_key / auth_token from the environment and an `ant auth login` profile into a
    # token cache; with none of them it fails later with a TypeError mid-request. Check up front.
    if not (client.api_key or client.auth_token or getattr(client, "_token_cache", None) is not None):
        raise NoCredentialsError(NO_KEY)
    return client


def build_parser() -> argparse.ArgumentParser:
    shared = argparse.ArgumentParser(add_help=False)
    shared.add_argument("--features", default="data/features/fct_bank_features.parquet",
                        help="Parquet export of fct_bank_features")
    shared.add_argument("--model-dir", default="data/model", help="Phase 3 model folder (read only)")
    shared.add_argument("--failures", default="data/raw/failures/failures.parquet", help="FDIC failed bank list")
    parser = argparse.ArgumentParser(prog="python -m canary.analyst")
    sub = parser.add_subparsers(dest="command", required=True)
    memo = sub.add_parser("memo", parents=[shared], help="write one checked bank note")
    memo.add_argument("--cert", type=int, required=True)
    memo.add_argument("--as-of", type=date.fromisoformat, default=None, help="quarter end, YYYY-MM-DD")
    memo.add_argument("--model", default=DEFAULT_MODEL, help="writer model")
    memo.add_argument("--out", default="banks", help="notes folder")
    ask = sub.add_parser("ask", parents=[shared], help="answer a plain-English question about the banks")
    ask.add_argument("question")
    ask.add_argument("--model", default=DEFAULT_MODEL, help="agent model")
    show = sub.add_parser("showcase", parents=[shared], help="write notes for the showcase set in one batch job")
    show.add_argument("--model", default=DEFAULT_MODEL, help="writer model")
    show.add_argument("--out", default="banks", help="notes folder")
    show.add_argument("--replay-dir", default=str(REPLAY_DIR), help="Phase 4 replay folder")
    show.add_argument("--report", default="data/analyst/showcase_report.json", help="run report (JSON)")
    show.add_argument("--dry-run", action="store_true", help="list the banks and estimate the cost; no API calls")
    show.add_argument("--resume", metavar="BATCH_ID", default=None,
                      help="collect an existing batch (id from the log or the .state.json file) instead of creating one")
    show.add_argument("--watchlist-top", type=int, default=None, metavar="N",
                      help="only the N best-ranked banks of the latest-quarter watchlist (default: all); "
                           "used by --dry-run and the real run, ignored with --resume (the bank list comes "
                           "from the state file)")
    cmp_ = sub.add_parser("compare", parents=[shared], help="write the case-study notes with several models and compare")
    cmp_.add_argument("--models", default="claude-opus-5-5,claude-sonnet-5-5", help="comma-separated writer models")
    cmp_.add_argument("--out", default="data/analyst/compare", help="comparison folder (one subfolder per model)")
    return parser


def _compare(args) -> int:
    from canary.analyst import compare as cmp

    models = [m.strip() for m in args.models.split(",") if m.strip()]
    if not models:
        print("error: --models needs at least one model name", file=sys.stderr)
        return 2
    certs = tuple(cmp.CASE_STUDY_CERTS)
    ctx = load_context(Path(args.features), Path(args.model_dir), Path(args.failures))
    print(f"planned: {len(models) * len(certs)} calls ({len(models)} models x {len(certs)} banks {list(certs)})")
    for m in models:
        print(f"  {m} -> {Path(args.out) / m}")
    report = cmp.compare_models(ctx, make_client(), models, certs, Path(args.out), replay_dir=REPLAY_DIR)
    cols = ["model", "first try", "after retry", "failed", "in tokens", "out tokens", "cost"]
    rows = [[m, str(a["passed_first_try"]), str(a["passed_after_retry"]), str(a["failed"]),
             f"{a['input_tokens']:,}", f"{a['output_tokens']:,}", f"${a['cost_usd']:.2f}"]
            for m, a in report["models"].items()]
    widths = [max(len(r[i]) for r in [cols, *rows]) for i in range(len(cols))]
    for r in [cols, *rows]:
        print("  ".join(c.ljust(w) if i == 0 else c.rjust(w) for i, (c, w) in enumerate(zip(r, widths))))
    print("memos:")
    for e in report["memos"]:
        print(f"  {e['model']} {e['cert']}: " + (e["path"] if e["ok"] else f"FAILED {'; '.join(e['errors'])[:200]}"))
    print(f"report {Path(args.out) / 'compare.json'}")
    return 0


def _showcase(args) -> int:
    from canary.analyst.showcase import (
        RETRY_SHARE,
        estimate_run,
        read_state,
        run_showcase,
        showcase_banks,
        state_path,
    )

    ctx = load_context(Path(args.features), Path(args.model_dir), Path(args.failures))
    banks = showcase_banks(ctx, Path(args.model_dir), Path(args.replay_dir), watchlist_top=args.watchlist_top)
    if args.dry_run:
        counts: dict[str, int] = {}
        for cert, as_of, group in banks:
            counts[group] = counts.get(group, 0) + 1
            print(f"{cert}\t{as_of}\t{group}")
        print(f"{len(banks)} banks: " + ", ".join(f"{g} {n}" for g, n in counts.items()))
        est = estimate_run(ctx, banks, args.model, Path(args.replay_dir))
        print(f"estimated tokens: {est['input']:,} input, {est['output']:,} output")
        print(f"estimated cost: ${est['cost']:.2f} (batch price, {args.model}; first tries only)")
        print(f"retry allowance: {est['retries']} banks ({round(100 * RETRY_SHARE)}%) retried at full price, "
              f"{est['retry_input']:,} input, {est['retry_output']:,} output tokens: ${est['retry_cost']:.2f}")
        print(f"estimated total with retries: ${est['total']:.2f}")
        return 0
    state = read_state(Path(args.report))
    if args.resume is None and state is not None and not state.get("complete"):
        print(f"error: batch {state['batch_id']} from {state_path(Path(args.report))} was not fully collected; "
              f"rerun with --resume {state['batch_id']} (or delete that file to start a new batch)",
              file=sys.stderr)
        return 1
    report = run_showcase(ctx, make_client(), args.model, Path(args.out), Path(args.report),
                          banks=banks, replay_dir=Path(args.replay_dir), resume=args.resume)
    print(f"{report['written']} written, {report['failed']} failed of {report['banks_total']} "
          f"(${report['cost_usd']:.2f}); report {args.report}")
    for e in report["banks"]:
        if not e["ok"]:
            print(f"  cert {e['cert']}: {'; '.join(e['errors'])}", file=sys.stderr)
    return 0 if report["failed"] == 0 else 1


def _ask(args) -> int:
    from canary.analyst.agent import ask_with_usage

    ctx = load_context(Path(args.features), Path(args.model_dir), Path(args.failures))
    answer, u = ask_with_usage(args.question, ctx, make_client(), args.model)
    print(answer)
    print(f"({u['model']}, {u['input_tokens']:,} in / {u['output_tokens']:,} out tokens, ${u['cost_usd']:.4f}; "
          "memos written by the agent are not included)", file=sys.stderr)
    return 0


def _memo(args) -> int:
    ctx = load_context(Path(args.features), Path(args.model_dir), Path(args.failures))
    try:
        as_of = args.as_of or default_as_of(ctx, args.cert)
        validate_as_of(ctx, args.cert, as_of)  # before the client, so bad input never needs a key
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    try:
        res = write_memo(ctx, args.cert, as_of, client=make_client(), model=args.model,
                         out_dir=Path(args.out), replay_dir=REPLAY_DIR)
    except json.JSONDecodeError as exc:
        print(f"error: cert {args.cert}: Claude returned malformed JSON ({exc}); no note written.",
              file=sys.stderr)
        return 1
    except ValueError as exc:  # not an input error: as-of was validated above
        print(f"error: cert {args.cert}: memo could not be written ({exc}); no note written.", file=sys.stderr)
        return 1
    except RefusalError as exc:
        print(f"error: cert {args.cert}: Claude refused to write this memo; no note written. {exc}",
              file=sys.stderr)
        return 1
    except TruncatedError as exc:
        print(f"error: cert {args.cert}: {exc}; no note written.", file=sys.stderr)
        return 1
    usage = f"{res.attempts} attempt(s), {res.input_tokens:,} in / {res.output_tokens:,} out tokens, ${res.cost_usd:.4f}"
    if not res.ok:
        print(f"cert {args.cert}: memo failed the citation check twice; no note written ({usage}).",
              file=sys.stderr)
        for e in res.errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print(f"wrote {res.path} (as of {res.as_of}, {res.model}, {usage})")
    return 0


def _api_errors() -> tuple[type[BaseException], ...]:
    try:
        import anthropic
    except ImportError:
        return ()
    return (anthropic.APIError,)  # connection, timeout, auth, rate limit, server errors


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    args = build_parser().parse_args(argv)
    api_errors = _api_errors()
    try:
        if args.command == "memo":
            return _memo(args)
        if args.command == "showcase":
            return _showcase(args)
        if args.command == "compare":
            return _compare(args)
        if args.command == "ask":
            return _ask(args)
    except (KeyError, FileNotFoundError) as exc:
        log.error("analyst failed: %s", exc)
        return 1
    except NoCredentialsError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except api_errors as exc:
        msg = " ".join(str(exc).split())[:300]
        print(f"error: Claude API call failed ({type(exc).__name__}): {msg}", file=sys.stderr)
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
