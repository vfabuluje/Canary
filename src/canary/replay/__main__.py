"""Phase 4 replay: python -m canary.replay --features PATH --model-dir data/model --out data/replay.

Reads the Phase 3 feature export and saved model, and writes the post-hoc metrics and error
analysis tables to --out. It never writes into the model folder (refused, even by another
spelling of the path) and never changes the model. Re-running overwrites its own outputs;
the results are deterministic.
"""
import argparse
import hashlib
import json
import logging
from pathlib import Path

import pandas as pd
import xgboost

from canary.model.dataset import load_dataset
from canary.model.train import CASE_STUDY_CERTS, _jsonable, _score_test
from canary.replay.analysis import (
    distribution_table,
    failure_mix,
    false_alarm_profile,
    mix_summary,
    top_false_alarm_banks,
)
from canary.replay.probe import WHAT_IF_ROWS, contributions, replay_banks, test_misses, what_if
from canary.replay.runrisk import posthoc_metrics, score_posthoc

log = logging.getLogger(__name__)

OUTPUT_FILES = (
    "posthoc_metrics.json",
    "replay_banks.csv",
    "contributions.csv",
    "what_if.csv",
    "training_mix.csv",
    "distributions.csv",
    "test_misses.csv",
    "false_alarm_profile.csv",
    "top_false_alarm_banks.csv",
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m canary.replay")
    parser.add_argument("--features", required=True, help="Parquet export of fct_bank_features")
    parser.add_argument("--model-dir", default="data/model", help="Phase 3 model folder (read only)")
    parser.add_argument("--out", default="data/replay", help="output folder (not the model folder)")
    return parser


def _inside(path: Path, folder: Path) -> bool:
    return path == folder or folder in path.parents


def _last_two_reports(test_scored: pd.DataFrame) -> pd.DataFrame:
    cases = test_scored[test_scored["cert"].isin(CASE_STUDY_CERTS)]
    cases = cases.sort_values(["cert", "report_date"], kind="mergesort")
    return cases.groupby("cert", group_keys=False).tail(2)


def run(features: Path, model_dir: Path, out: Path) -> int:
    if _inside(out.resolve(), model_dir.resolve()):
        log.error("--out %s is the model folder %s (or inside it); refusing to write there", out, model_dir)
        return 1
    model_path = model_dir / "model.json"
    if not model_path.exists():
        log.error("%s not found; train the Phase 3 model first", model_path)
        return 1

    model = xgboost.XGBClassifier()
    model.load_model(model_path)
    df = load_dataset(features)
    test_scored = _score_test(df, model)
    scored = score_posthoc(df)

    metrics = posthoc_metrics(scored, test_scored[["cert", "report_date", "flagged"]])
    mix = failure_mix(scored)
    metrics["failure_mix"] = mix_summary(mix)
    fa_profile = false_alarm_profile(test_scored)
    metrics["false_alarm_rows"] = dict(fa_profile.attrs)
    metrics["model_sha256"] = hashlib.sha256(model_path.read_bytes()).hexdigest()

    out.mkdir(parents=True, exist_ok=True)
    (out / "posthoc_metrics.json").write_text(json.dumps(_jsonable(metrics), indent=2))
    replay_banks(test_scored, scored).to_csv(out / "replay_banks.csv", index=False)
    contributions(model, _last_two_reports(test_scored)).to_csv(out / "contributions.csv", index=False)
    pd.concat([what_if(model, test_scored, c, d) for c, d in WHAT_IF_ROWS], ignore_index=True).to_csv(
        out / "what_if.csv", index=False
    )
    mix.to_csv(out / "training_mix.csv", index=False)
    distribution_table(scored).to_csv(out / "distributions.csv", index=False)
    test_misses(model, test_scored).to_csv(out / "test_misses.csv", index=False)
    fa_profile.to_csv(out / "false_alarm_profile.csv", index=False)
    top_false_alarm_banks(test_scored).to_csv(out / "top_false_alarm_banks.csv", index=False)
    log.info("wrote %d files to %s (post-hoc; see posthoc_metrics.json note)", len(OUTPUT_FILES), out)
    return 0


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    args = build_parser().parse_args(argv)
    try:
        return run(Path(args.features), Path(args.model_dir), Path(args.out))
    except (KeyError, ValueError, FileNotFoundError) as exc:
        log.error("replay failed: %s", exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
