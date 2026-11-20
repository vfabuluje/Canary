import pandas as pd
import pytest

from canary.fdic_client import FDICClient, IncompleteResponseError
from canary.ingest_websites import clean_domain, run_websites
from canary.storage import websites_path
from conftest import FakeSession, page


@pytest.mark.parametrize("raw, domain", [
    ("www.wellsfargo.com", "wellsfargo.com"),
    ("WWW.AuburnBank.com", "auburnbank.com"),
    ("https://www.jpmorganchase.com/", "jpmorganchase.com"),
    ("http://bank.example.com/personal?x=1", "bank.example.com"),
    ("  www.frazerbank.com  ", "frazerbank.com"),
    ("frazerbank.com:443", "frazerbank.com"),
    ("", None),
    (None, None),
    ("0", None),
    ("not a site", None),
    ("evil.com\");}body{x:url(", None),
    ("javascript:alert(1)", None),
    ("localhost", None),
])
def test_clean_domain(raw, domain):
    assert clean_domain(raw) == domain


def _client(rows):
    session = FakeSession([page(rows, len(rows))])
    return FDICClient(session=session, pause=0, sleep=lambda s: None), session


def test_run_websites_writes_cert_and_domain(tmp_path):
    client, session = _client([
        {"CERT": 3511, "WEBADDR": "www.wellsfargo.com", "ID": "a"},
        {"CERT": 24735, "WEBADDR": "", "ID": "b"},
        {"CERT": 46, "WEBADDR": None, "ID": "c"},
    ])
    assert run_websites(tmp_path, client) == 1
    df = pd.read_parquet(websites_path(tmp_path))
    assert df.to_dict("records") == [{"cert": 3511, "website": "wellsfargo.com"}]
    assert session.calls[0][1]["fields"] == "CERT,WEBADDR"


def test_run_websites_refuses_empty_answer(tmp_path):
    client, _ = _client([])
    with pytest.raises(IncompleteResponseError):
        run_websites(tmp_path, client)
