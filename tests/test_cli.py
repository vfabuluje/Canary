from canary import ingest
from canary.fdic_client import FDICAPIError
from canary.schema import SchemaError


def test_cli_financials_passes_force(monkeypatch, tmp_path):
    calls = {}

    def fake(root, client, force=False):
        calls.update(root=root, client=client, force=force)
        return []

    monkeypatch.setattr(ingest, "run_financials", fake)
    sentinel = object()
    code = ingest.main(["financials", "--force", "--root", str(tmp_path)], client=sentinel)
    assert code == 0
    assert calls == {"root": tmp_path, "client": sentinel, "force": True}


def test_cli_failures(monkeypatch, tmp_path):
    calls = {}

    def fake(root, client):
        calls.update(root=root, client=client)
        return 3

    monkeypatch.setattr(ingest, "run_failures", fake)
    sentinel = object()
    assert ingest.main(["failures", "--root", str(tmp_path)], client=sentinel) == 0
    assert calls == {"root": tmp_path, "client": sentinel}


def test_cli_returns_1_on_api_error(monkeypatch, tmp_path):
    def boom(root, client, force=False):
        raise FDICAPIError("down")

    monkeypatch.setattr(ingest, "run_financials", boom)
    assert ingest.main(["financials", "--root", str(tmp_path)], client=object()) == 1


def test_cli_returns_1_on_schema_error(monkeypatch, tmp_path):
    def boom(root, client, force=False):
        raise SchemaError("bad column")

    monkeypatch.setattr(ingest, "run_financials", boom)
    assert ingest.main(["financials", "--root", str(tmp_path)], client=object()) == 1
