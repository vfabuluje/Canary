class FakeResponse:
    def __init__(self, status_code, payload=None, text=""):
        self.status_code = status_code
        self._payload = payload
        self.text = text

    def json(self):
        if self._payload is None:
            raise ValueError("no JSON body")
        return self._payload


class FakeSession:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []
        self.headers = {}

    def get(self, url, params=None, timeout=None):
        self.calls.append((url, dict(params) if params else params))
        item = self.responses.pop(0)
        if isinstance(item, BaseException):
            raise item
        return item


def page(rows, total):
    return FakeResponse(
        200, {"meta": {"total": total}, "data": [{"data": r} for r in rows]}
    )
