import math

from canary.analyst.labels import PLAIN_NAMES, UNIT, display_forms
from canary.model.dataset import FEATURE_COLUMNS


def test_plain_names_cover_all_features():
    assert set(PLAIN_NAMES) == set(FEATURE_COLUMNS) == set(UNIT)


def test_display_forms():
    assert display_forms("htm_unrealized_loss_to_equity", 0.9812) == ["98.1%", "98%", "0.98"]
    assert display_forms("equity_to_assets", 8.53) == ["8.5%", "9%", "8.53"]
    assert display_forms("log_total_assets", math.log(209_000_000))[0] == "$209.0 billion"
    assert display_forms("log_total_assets", math.log(209_000_000)) == ["$209.0 billion", "$209 billion"]
    assert display_forms("log_total_assets", math.log(850_000))[0] == "$850.0 million"


def test_display_forms_negative_keeps_sign():
    assert display_forms("return_on_assets", -2.5)[0] == "-2.5%"
    assert display_forms("asset_growth_4q", -0.2)[0] == "-20.0%"


def test_anthropic_pin_matches_tested_version():
    import tomllib
    from pathlib import Path

    deps = tomllib.loads((Path(__file__).parents[1] / "pyproject.toml").read_text())["project"]["optional-dependencies"]
    assert deps["analyst"] == ["anthropic>=1.17,<2"]
