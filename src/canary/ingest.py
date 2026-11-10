"""Command-line entry point: python -m canary.ingest {financials,failures}."""
import argparse
import logging
from pathlib import Path

from canary.fdic_client import FDICAPIError, FDICClient
from canary.ingest_failures import run_failures
from canary.ingest_financials import run_financials
from canary.schema import SchemaError

log = logging.getLogger(__name__)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m canary.ingest")
    sub = parser.add_subparsers(dest="command", required=True)
    fin = sub.add_parser("financials", help="pull quarterly bank financials")
    fin.add_argument("--force", action="store_true", help="re-pull every quarter")
    fin.add_argument("--root", default="data/raw", help="raw data directory")
    fail = sub.add_parser("failures", help="pull the failed bank list")
    fail.add_argument("--root", default="data/raw", help="raw data directory")
    return parser


def main(argv: list[str] | None = None, client: FDICClient | None = None) -> int:
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )
    args = build_parser().parse_args(argv)
    root = Path(args.root)
    if client is None:
        client = FDICClient()
    try:
        if args.command == "financials":
            run_financials(root, client, force=args.force)
        else:
            run_failures(root, client)
    except (FDICAPIError, SchemaError) as exc:
        log.error("ingest %s failed: %s", args.command, exc)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
