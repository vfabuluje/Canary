from pathlib import Path

import pytest
import yaml

from canary.schema import FAILURE_FIELDS, FINANCIAL_FIELDS

REPO = Path(__file__).resolve().parent.parent


@pytest.mark.parametrize(
    "doc,fields",
    [("fdic_financials.md", FINANCIAL_FIELDS), ("fdic_failures.md", FAILURE_FIELDS)],
)
def test_every_field_documented(doc, fields):
    text = (REPO / "data-dictionary" / doc).read_text()
    missing = [f for f in [*fields, "ingested_at"] if f"| `{f}` |" not in text]
    assert missing == []


def _dbt_models():
    """Yield (model name, [column names]) from every dbt schema yml file."""
    for yml in sorted((REPO / "warehouse" / "models").rglob("*.yml")):
        data = yaml.safe_load(yml.read_text()) or {}
        for model in data.get("models", []):
            yield model["name"], [c["name"] for c in model.get("columns", [])]


def test_every_dbt_column_documented():
    models = list(_dbt_models())
    assert models, "no dbt models found"
    for name, columns in models:
        doc = REPO / "data-dictionary" / f"{name}.md"
        assert doc.exists(), f"missing {doc.name}"
        text = doc.read_text()
        missing = [c for c in columns if f"| `{c}` |" not in text]
        assert missing == [], f"{name}: {missing}"
