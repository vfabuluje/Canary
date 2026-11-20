"""Dashboard data export: python -m canary.dashboard export [--out dashboard/data].

Writes the files the Streamlit app reads, prints each file's size and the folder total, and exits 1
if the folder is over 50 MB. No Claude calls. Every writer goes in write_all.
"""
import argparse
import json
import sys
from pathlib import Path

from canary.analyst.context import load_context
from canary.dashboard.cases import export_cases
from canary.dashboard.reports import write_reports
from canary.dashboard.tables import showcase_certs, write_tables

MAX_BYTES = 50 * 1024 * 1024


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m canary.dashboard")
    sub = parser.add_subparsers(dest="command", required=True)
    exp = sub.add_parser("export", help="write the dashboard data files")
    exp.add_argument("--out", default="dashboard/data", help="output folder")
    exp.add_argument("--features", default="data/features/fct_bank_features.parquet")
    exp.add_argument("--model-dir", default="data/model", help="Phase 3 model folder (read only)")
    exp.add_argument("--failures", default="data/raw/failures/failures.parquet")
    exp.add_argument("--notes", default="banks", help="analyst notes folder")
    exp.add_argument("--traces", default="data/analyst/traces", help="analyst trace folder")
    return parser


def write_all(ctx, args, out: Path, certs: set[int]) -> None:
    """Every export writer, in order. Add new writers here."""
    write_tables(ctx, Path(args.model_dir), out, certs)
    cases = export_cases(ctx, Path(args.model_dir) / "case_studies.csv")
    (out / "case_studies.json").write_text(json.dumps(cases))
    written = write_reports(ctx, Path(args.notes), Path(args.traces), out)
    if set(written) != certs:
        raise RuntimeError(f"report files {sorted(set(written) ^ certs)} disagree with banks.has_report")


def _sizes(out: Path) -> tuple[list[tuple[str, int]], int]:
    files = sorted((str(p.relative_to(out)), p.stat().st_size) for p in out.rglob("*") if p.is_file())
    return files, sum(n for _, n in files)


def _export(args) -> int:
    out = Path(args.out)
    ctx = load_context(Path(args.features), Path(args.model_dir), Path(args.failures))
    certs = showcase_certs(Path(args.notes), Path(args.traces))
    write_all(ctx, args, out, certs)
    files, total = _sizes(out)
    for name, size in files:
        print(f"{size / 1024:10.1f} KB  {name}")
    print(f"{total / 1024 / 1024:10.2f} MB  total in {out}")
    if total > MAX_BYTES:
        print(f"error: {out} is {total / 1024 / 1024:.1f} MB, over the 50 MB limit", file=sys.stderr)
        return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "export":
        return _export(args)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
