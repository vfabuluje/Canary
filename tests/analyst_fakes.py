"""Fake Anthropic client for analyst tests. No network.

FakeClient(responses) exposes beta.messages.create(**kw): it records the kwargs and returns the
next response as a message with `stop_reason`, `content` (one text block), `usage` and `model`.
A response is a dict (sent as JSON text), a str (sent as-is) or a message made by fake_message.
Tasks 7-8 extend this with tool_runner and batches.
"""

import json
from types import SimpleNamespace

IN_TOKENS = 1000
OUT_TOKENS = 500


def fake_message(text: str, stop_reason: str = "end_turn", model: str | None = None,
                 input_tokens: int = IN_TOKENS, output_tokens: int = OUT_TOKENS) -> SimpleNamespace:
    return SimpleNamespace(
        stop_reason=stop_reason,
        stop_details=None,
        model=model,
        content=[SimpleNamespace(type="text", text=text)],
        usage=SimpleNamespace(input_tokens=input_tokens, output_tokens=output_tokens),
    )


class _Messages:
    def __init__(self, client: "FakeClient") -> None:
        self._client = client

    def create(self, **kw):
        self._client.calls.append(kw)
        item = self._client.responses.pop(0)
        if isinstance(item, BaseException):
            raise item
        if isinstance(item, SimpleNamespace):
            msg = item
        else:
            msg = fake_message(item if isinstance(item, str) else json.dumps(item))
        if msg.model is None:
            msg.model = kw.get("model")
        return msg


class FakeClient:
    def __init__(self, responses: list) -> None:
        self.responses = list(responses)
        self.calls: list[dict] = []
        self.beta = SimpleNamespace(messages=_Messages(self))
