"""Train and evaluate: python -m canary.model train|evaluate --features PATH --out data/model.

`train` writes model.json and run_config.json. `evaluate` scores the 2016-2024 test years
and writes scores_test.parquet, metrics.json and case_studies.csv. Evaluate is meant to be
run once: it refuses to overwrite metrics.json unless --force is given.
"""
import argparse
import hashlib
import json
import logging
from pathlib import Path

import xgboost

from canary.model.dataset import load_dataset
from canary.model.train import _jsonable, _score_test, case_studies, evaluate, train

log = logging.getLogger(__name__)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m canary.model")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("train", "evaluate"):
        p = sub.add_parser(name)
        p.add_argument("--features", required=True, help="Parquet export of fct_bank_features")
        p.add_argument("--out", default="data/model", help="output folder")
    sub.choices["evaluate"].add_argument(
        "--force", action="store_true", help="overwrite existing metrics.json (marks it rerun)"
    )
    return parser


def _train(args) -> int:
    df = load_dataset(Path(args.features))
    model, config = train(df)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    model.save_model(out / "model.json")
    (out / "run_config.json").write_text(json.dumps(_jsonable(config), indent=2))
    log.info("trained %d trees on %d rows; wrote %s", config["n_trees"], config["n_train_rows"], out)
    return 0


def _evaluate(args) -> int:
    out = Path(args.out)
    metrics_path = out / "metrics.json"
    if metrics_path.exists() and not args.force:
        log.error("%s exists; the test years are scored once. Use --force to rerun.", metrics_path)
        return 1
    model_path = out / "model.json"
    if not model_path.exists():
        log.error("%s not found; run `train` first", model_path)
        return 1
    config_path = out / "run_config.json"
    if not config_path.exists():
        log.error("%s not found; run `train` first", config_path)
        return 1
    model = xgboost.XGBClassifier()
    model.load_model(model_path)
    df = load_dataset(Path(args.features))
    metrics = evaluate(df, model)
    metrics["run_config"] = json.loads(config_path.read_text())
    metrics["model_sha256"] = hashlib.sha256(model_path.read_bytes()).hexdigest()
    if metrics_path.exists():
        log.warning("--force: overwriting %s and marking the metrics as a rerun", metrics_path)
        metrics["rerun"] = True
    test = _score_test(df, model)
    keep = ["cert", "report_date", "quarters_until_failure", "label", "score", "flagged",
            "baseline_score", "baseline_flagged"]
    test[keep].to_parquet(out / "scores_test.parquet", index=False)
    case_studies(df, model).to_csv(out / "case_studies.csv", index=False)
    metrics_path.write_text(json.dumps(metrics, indent=2))
    log.info("wrote metrics, scores and case studies to %s", out)
    return 0


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    args = build_parser().parse_args(argv)
    try:
        return _train(args) if args.command == "train" else _evaluate(args)
    except (KeyError, ValueError, FileNotFoundError) as exc:
        log.error("%s failed: %s", args.command, exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
