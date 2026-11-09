import pytest
import requests

from canary.fdic_client import FDICAPIError, FDICClient, IncompleteResponseError
from conftest import FakeResponse, FakeSession, page


def make(responses, sleeps=None, pause=0, **kw):
    sleeps = [] if sleeps is None else sleeps
    session = FakeSession(responses)
    client = FDICClient(session=session, pause=pause, sleep=sleeps.append, **kw)
    return client, session, sleeps


def test_get_all_single_page_unwraps_rows():
    client, _, _ = make([page([{"CERT": 1}, {"CERT": 2}], 2)])
    assert client.get_all("financials", {}) == [{"CERT": 1}, {"CERT": 2}]


def test_get_all_pages_with_offset():
    client, session, _ = make(
        [page([{"CERT": 1}, {"CERT": 2}], 5), page([{"CERT": 3}, {"CERT": 4}], 5),
         page([{"CERT": 5}], 5)]
    )
    rows = client.get_all("financials", {}, page_size=2)
    assert len(rows) == 5
    assert len(session.calls) == 3
    assert [c[1]["offset"] for c in session.calls] == [0, 2, 4]


def test_row_count_mismatch_raises():
    client, _, _ = make([page([{"CERT": 1}, {"CERT": 2}], 3), page([], 3)])
    with pytest.raises(IncompleteResponseError, match="3"):
        client.get_all("financials", {}, page_size=2)


def test_retries_then_succeeds():
    client, session, sleeps = make(
        [FakeResponse(503), requests.Timeout(), page([{"CERT": 1}], 1)]
    )
    assert client.get_all("financials", {}) == [{"CERT": 1}]
    assert sleeps == [1.0, 2.0]
    assert len(session.calls) == 3


def test_gives_up_after_three_retries():
    client, session, _ = make([FakeResponse(503)] * 4)
    with pytest.raises(FDICAPIError):
        client.get_page("financials", {})
    assert len(session.calls) == 4


def test_client_error_not_retried():
    client, session, _ = make([FakeResponse(400, text="bad")])
    with pytest.raises(FDICAPIError):
        client.get_page("financials", {})
    assert len(session.calls) == 1


def test_non_json_body_raises_api_error():
    client, _, _ = make([FakeResponse(200, None, "<html>")])
    with pytest.raises(FDICAPIError):
        client.get_page("financials", {})


def test_missing_meta_raises_api_error():
    client, _, _ = make([FakeResponse(200, {"data": []})])
    with pytest.raises(FDICAPIError):
        client.get_page("financials", {})


def test_sends_limit_offset_and_user_agent():
    client, session, _ = make([page([], 0)])
    client.get_all("financials", {"filters": "CERT:1"})
    url, params = session.calls[0]
    assert url == "https://api.fdic.gov/banks/financials"
    assert params["limit"] == 10000 and params["offset"] == 0
    assert params["filters"] == "CERT:1"
    default = FDICClient()
    assert default.session.headers["User-Agent"] == "canary-research-pipeline"


def test_pause_between_pages():
    client, _, sleeps = make(
        [page([{"CERT": 1}], 2), page([{"CERT": 2}], 2)], pause=0.5
    )
    client.get_all("financials", {}, page_size=1)
    assert sleeps == [0.5]


def test_pause_between_separate_calls():
    client, _, sleeps = make([page([], 0), page([], 0)], pause=0.5)
    client.get_all("financials", {})
    client.get_all("financials", {})
    assert sleeps == [0.5]
