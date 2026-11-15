import hashlib
import json

import pandas as pd
import pytest

from canary.model.__main__ import main as model_main
from canary.replay.__main__ import OUTPUT_FILES, main

pytestmark = pytest.mark.usefixtures("small_grid")


@pytest.fixture
def model_dir(features_path, tmp_path):
    out = tmp_path / "model"
    assert model_main(["train", "--features", str(features_path), "--out", str(out)]) == 0
    return out


def _snapshot(folder):
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(folder.iterdir())}


def test_cli_writes_every_output(features_path, model_dir, tmp_path):
    out = tmp_path / "replay"
    assert main(["--features", str(features_path), "--model-dir", str(model_dir), "--out", str(out)]) == 0
    assert len(OUTPUT_FILES) == 9
    for name in OUTPUT_FILES:
        assert (out / name).exists(), name
    metrics = json.loads((out / "posthoc_metrics.json").read_text())
    assert metrics["post_hoc"] is True
    assert set(metrics["failure_mix"]) == {"training", "2023", "training_by_year"}
    assert metrics["model_sha256"] == hashlib.sha256((model_dir / "model.json").read_bytes()).hexdigest()
    assert {"n_true_alarm_rows", "n_false_alarm_rows"} <= set(metrics["false_alarm_rows"])
    what_if = pd.read_csv(out / "what_if.csv")
    assert what_if["cert"].nunique() == 3
    contributions = pd.read_csv(out / "contributions.csv")
    assert contributions.groupby("cert").size().to_dict() == {24735: 2, 57053: 2, 59017: 2}


def test_cli_refuses_model_folder(features_path, model_dir):
    before = _snapshot(model_dir)
    assert main(["--features", str(features_path), "--model-dir", str(model_dir), "--out", str(model_dir)]) == 1
    assert _snapshot(model_dir) == before


@pytest.mark.parametrize("alias", ["{m}/", "{m}/.", "{m}/../model", "{m}/sub"])
def test_cli_refuses_model_folder_alias(features_path, model_dir, alias):
    before = _snapshot(model_dir)
    out = alias.format(m=model_dir)
    assert main(["--features", str(features_path), "--model-dir", str(model_dir), "--out", out]) == 1
    assert _snapshot(model_dir) == before
    assert not (model_dir / "sub").exists()


def test_cli_does_not_touch_model_folder(features_path, model_dir, tmp_path):
    before = _snapshot(model_dir)
    assert main(["--features", str(features_path), "--model-dir", str(model_dir), "--out", str(tmp_path / "r")]) == 0
    assert _snapshot(model_dir) == before


def test_cli_missing_model_fails(features_path, tmp_path):
    empty = tmp_path / "empty"
    empty.mkdir()
    assert main(["--features", str(features_path), "--model-dir", str(empty), "--out", str(tmp_path / "r")]) == 1
    assert not (tmp_path / "r").exists()


def test_every_output_column_documented(features_path, model_dir, tmp_path):
    """data-dictionary/replay_outputs.md must define every column the replay writes."""
    from pathlib import Path

    out = tmp_path / "replay"
    assert main(["--features", str(features_path), "--model-dir", str(model_dir), "--out", str(out)]) == 0
    doc = (Path(__file__).resolve().parent.parent / "data-dictionary" / "replay_outputs.md").read_text()
    missing = []
    for name in OUTPUT_FILES:
        if name.endswith(".csv"):
            columns = pd.read_csv(out / name, nrows=0).columns
        else:
            columns = json.loads((out / name).read_text()).keys()
        if f"## `{name}`" not in doc:
            missing.append(name)
        missing += [f"{name}:{c}" for c in columns if f"| `{c}` |" not in doc]
    assert missing == []
