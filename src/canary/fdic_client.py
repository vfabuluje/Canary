"""HTTP client for the FDIC BankFind API with paging, retries, and a completeness check."""
import time

import requests

USER_AGENT = "canary-research-pipeline"


class FDICAPIError(Exception):
    """The FDIC API returned an error or an unusable response."""


class IncompleteResponseError(FDICAPIError):
    """We received fewer rows than the API said exist."""


class FDICClient:
    def __init__(self, session=None, base_url="https://api.fdic.gov/banks",
                 max_retries=3, backoff=1.0, pause=0.5, timeout=60,
                 sleep=time.sleep):
        if session is None:
            session = requests.Session()
            session.headers["User-Agent"] = USER_AGENT
        self.session = session
        self.base_url = base_url.rstrip("/")
        self.max_retries = max_retries
        self.backoff = backoff
        self.pause = pause
        self.timeout = timeout
        self.sleep = sleep
        self._requests_made = 0

    def get_page(self, endpoint, params):
        """One request, with retries on timeouts, connection errors, 429 and 5xx."""
        if self._requests_made > 0 and self.pause:
            self.sleep(self.pause)
        self._requests_made += 1

        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        last_error = None
        for attempt in range(self.max_retries + 1):
            if attempt > 0:
                self.sleep(self.backoff * 2 ** (attempt - 1))
            try:
                resp = self.session.get(url, params=params, timeout=self.timeout)
            except (requests.Timeout, requests.ConnectionError) as exc:
                last_error = exc
                continue
            if resp.status_code == 429 or resp.status_code >= 500:
                last_error = FDICAPIError(f"HTTP {resp.status_code} from {url}")
                continue
            if resp.status_code != 200:
                raise FDICAPIError(
                    f"HTTP {resp.status_code} from {url}: {resp.text[:200]}"
                )
            try:
                body = resp.json()
            except ValueError as exc:
                raise FDICAPIError(f"Non-JSON response from {url}") from exc
            if (not isinstance(body, dict) or "data" not in body
                    or not isinstance(body.get("meta"), dict)
                    or "total" not in body["meta"]):
                raise FDICAPIError(f"Response from {url} missing meta.total or data")
            return body
        raise FDICAPIError(
            f"Gave up after {self.max_retries + 1} attempts: {last_error}"
        ) from last_error

    def get_all(self, endpoint, params, page_size=10000):
        """Fetch every page; return the inner row dicts; verify the count."""
        rows = []
        total = None
        while total is None or len(rows) < total:
            q = dict(params, limit=page_size, offset=len(rows))
            body = self.get_page(endpoint, q)
            total = body["meta"]["total"]
            batch = [item["data"] for item in body["data"]]
            if not batch and len(rows) < total:
                raise IncompleteResponseError(
                    f"Empty page at offset {len(rows)}; got {len(rows)} of {total} rows"
                )
            rows.extend(batch)
        if len(rows) != total:
            raise IncompleteResponseError(f"Expected {total} rows, got {len(rows)}")
        return rows
