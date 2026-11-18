"""Risk analyst: python -m canary.analyst ask "question" [--model M], and memo --cert N [--as-of YYYY-MM-DD] [--model M] [--out banks].

Builds the fact sheet from the feature export and the saved model (read only), asks Claude to
write the memo, checks every number, and saves the note only if it passes. Exit codes: 0 written,
1 memo failed the check / refused / truncated / malformed JSON / bad input files,
2 bad cert or as-of date.
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


def make_client():
    import anthropic  # optional dependency group "analyst"

    if not os.environ.get("ANTHROPIC_API_KEY"):
        key = _read_dotenv(REPO_ROOT / ".env").get("ANTHROPIC_API_KEY")
        if key:
            os.environ["ANTHROPIC_API_KEY"] = key
    return anthropic.Anthropic()


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
    return parser


def _showcase(args) -> int:
    from canary.analyst.showcase import estimate_cost, run_showcase, showcase_banks

    ctx = load_context(Path(args.features), Path(args.model_dir), Path(args.failures))
    banks = showcase_banks(ctx, Path(args.model_dir), Path(args.replay_dir))
    if args.dry_run:
        counts: dict[str, int] = {}
        for cert, as_of, group in banks:
            counts[group] = counts.get(group, 0) + 1
            print(f"{cert}\t{as_of}\t{group}")
        print(f"{len(banks)} banks: " + ", ".join(f"{g} {n}" for g, n in counts.items()))
        print(f"estimated cost: ${estimate_cost(len(banks), args.model):.2f} "
              f"(batch price, {args.model}, 2,000 input and 2,000 output tokens per bank)")
        return 0
    report = run_showcase(ctx, make_client(), args.model, Path(args.out), Path(args.report),
                          banks=banks, replay_dir=Path(args.replay_dir))
    print(f"{report['written']} written, {report['failed']} failed of {report['banks_total']} "
          f"(${report['cost_usd']:.2f}); report {args.report}")
    for e in report["banks"]:
        if not e["ok"]:
            print(f"  cert {e['cert']}: {'; '.join(e['errors'])}", file=sys.stderr)
    return 0 if report["failed"] == 0 else 1


def _ask(args) -> int:
    from canary.analyst.agent import ask

    ctx = load_context(Path(args.features), Path(args.model_dir), Path(args.failures))
    print(ask(args.question, ctx, make_client(), args.model))
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


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    args = build_parser().parse_args(argv)
    try:
        if args.command == "memo":
            return _memo(args)
        if args.command == "showcase":
            return _showcase(args)
        if args.command == "ask":
            return _ask(args)
    except (KeyError, FileNotFoundError) as exc:
        log.error("analyst failed: %s", exc)
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
