from pathlib import Path

import pytest

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
