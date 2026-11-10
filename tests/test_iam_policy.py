import json
from pathlib import Path

POLICY = Path(__file__).resolve().parents[1] / "infra" / "iam-policy-canary-dev.json"


def _statements():
    return json.loads(POLICY.read_text())["Statement"]


def _list(x):
    return [x] if isinstance(x, str) else list(x)


def test_delete_only_on_scratch_prefixes():
    found = False
    for st in _statements():
        if st["Effect"] == "Allow" and "s3:DeleteObject" in _list(st["Action"]):
            found = True
            for r in _list(st["Resource"]):
                assert r.endswith("/athena-results/*") or r.endswith("/dbt/*"), r
    assert found


def test_no_wildcard_actions():
    for st in _statements():
        for a in _list(st["Action"]):
            assert a != "*" and a != "iam:*" and not a.startswith("iam:"), a


def test_s3_resources_use_bucket_placeholder():
    for st in _statements():
        if all(a.startswith("s3:") for a in _list(st["Action"])):
            for r in _list(st["Resource"]):
                assert "BUCKET_NAME" in r, r


def test_athena_scoped_to_canary_workgroup():
    for st in _statements():
        if all(a.startswith("athena:") for a in _list(st["Action"])):
            for r in _list(st["Resource"]):
                assert "workgroup/canary" in r, r


def test_glue_scoped_to_canary_databases():
    for st in _statements():
        if all(a.startswith("glue:") for a in _list(st["Action"])):
            for r in _list(st["Resource"]):
                tail = r.split(":", 5)[-1]
                assert (
                    tail == "catalog"
                    or tail.startswith("database/canary_")
                    or tail.startswith("table/canary_")
                ), r
