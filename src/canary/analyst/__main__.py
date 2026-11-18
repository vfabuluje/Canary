"""Risk analyst: python -m canary.analyst memo --cert N [--as-of YYYY-MM-DD] [--model M] [--out banks].

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
    return parser


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
    except (KeyError, FileNotFoundError) as exc:
        log.error("analyst failed: %s", exc)
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
