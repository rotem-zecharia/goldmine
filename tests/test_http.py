import pytest

from goldmine.http import Fetcher, RateLimited


class FakeResponse:
    def __init__(self, status_code, json_body=None, headers=None, text=""):
        self.status_code = status_code
        self._json = json_body if json_body is not None else {}
        self.headers = headers or {}
        self.text = text

    def json(self):
        return self._json


class FakeTransport:
    """Returns queued responses and records the requests it received."""

    def __init__(self, responses):
        self.responses = list(responses)
        self.requests = []

    def get(self, url, headers=None, timeout=None):
        self.requests.append({"url": url, "headers": headers or {}})
        return self.responses.pop(0)


def test_returns_parsed_json():
    fetcher = Fetcher(transport=FakeTransport([FakeResponse(200, {"ok": True})]), sleep=lambda s: None)

    assert fetcher.get_json("https://api.example/x") == {"ok": True}


def test_sends_stored_etag_on_the_second_call():
    transport = FakeTransport(
        [FakeResponse(200, {"v": 1}, headers={"ETag": "abc"}), FakeResponse(304)]
    )
    fetcher = Fetcher(transport=transport, sleep=lambda s: None)

    fetcher.get_json("https://api.example/x")
    fetcher.get_json("https://api.example/x")

    assert transport.requests[1]["headers"]["If-None-Match"] == "abc"


def test_304_replays_the_cached_body():
    transport = FakeTransport(
        [FakeResponse(200, {"v": 1}, headers={"ETag": "abc"}), FakeResponse(304)]
    )
    fetcher = Fetcher(transport=transport, sleep=lambda s: None)
    fetcher.get_json("https://api.example/x")

    assert fetcher.get_json("https://api.example/x") == {"v": 1}


def test_waits_until_reset_when_rate_limited_then_retries():
    slept = []
    transport = FakeTransport(
        [
            FakeResponse(403, headers={"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": "1000"}),
            FakeResponse(200, {"ok": True}),
        ]
    )
    fetcher = Fetcher(transport=transport, sleep=slept.append, now=lambda: 940.0)

    assert fetcher.get_json("https://api.example/x") == {"ok": True}
    assert slept and slept[0] >= 60


def test_gives_up_after_max_retries():
    responses = [
        FakeResponse(403, headers={"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": "10"})
        for _ in range(5)
    ]
    fetcher = Fetcher(
        transport=FakeTransport(responses), sleep=lambda s: None, now=lambda: 0.0, max_retries=3
    )

    with pytest.raises(RateLimited):
        fetcher.get_json("https://api.example/x")


def test_retries_server_errors_with_backoff():
    slept = []
    transport = FakeTransport([FakeResponse(502), FakeResponse(502), FakeResponse(200, {"ok": True})])
    fetcher = Fetcher(transport=transport, sleep=slept.append, now=lambda: 0.0)

    assert fetcher.get_json("https://api.example/x") == {"ok": True}
    assert slept == sorted(slept), "backoff must be non-decreasing"


def test_404_returns_none_rather_than_raising():
    fetcher = Fetcher(transport=FakeTransport([FakeResponse(404)]), sleep=lambda s: None)

    assert fetcher.get_json("https://api.example/gone") is None


def test_secondary_rate_limit_without_remaining_header_is_retried():
    # GitHub's abuse/secondary limit returns 403 with Retry-After and no
    # X-RateLimit-Remaining: 0. Treating that as fatal would abort a crawl.
    slept = []
    transport = FakeTransport(
        [FakeResponse(403, headers={"Retry-After": "3"}), FakeResponse(200, {"ok": True})]
    )
    fetcher = Fetcher(transport=transport, sleep=slept.append, now=lambda: 0.0)

    assert fetcher.get_json("https://api.example/x") == {"ok": True}
    assert slept[0] >= 3


def test_get_text_returns_the_body():
    fetcher = Fetcher(
        transport=FakeTransport([FakeResponse(200, text="# readme")]), sleep=lambda s: None
    )

    assert fetcher.get_text("https://raw.example/readme") == "# readme"


def test_get_text_returns_none_for_a_missing_file():
    fetcher = Fetcher(transport=FakeTransport([FakeResponse(404)]), sleep=lambda s: None)

    assert fetcher.get_text("https://raw.example/none") is None


def test_get_json_meta_returns_response_headers():
    transport = FakeTransport([FakeResponse(200, {"ok": True}, headers={"Link": '<x>; rel="last"'})])
    fetcher = Fetcher(transport=transport, sleep=lambda s: None)

    body, headers = fetcher.get_json_meta("https://api.example/x")

    assert body == {"ok": True} and 'rel="last"' in headers["Link"]


def test_a_cached_304_replays_the_headers_too():
    transport = FakeTransport(
        [FakeResponse(200, {"v": 1}, headers={"ETag": "abc", "Link": "L"}), FakeResponse(304)]
    )
    fetcher = Fetcher(transport=transport, sleep=lambda s: None)
    fetcher.get_json_meta("https://api.example/x")

    _, headers = fetcher.get_json_meta("https://api.example/x")

    assert headers["Link"] == "L"


def test_tracks_remaining_requests_from_the_rate_limit_header():
    transport = FakeTransport([FakeResponse(200, {}, headers={"X-RateLimit-Remaining": "4321"})])
    fetcher = Fetcher(transport=transport, sleep=lambda s: None)

    fetcher.get_json("https://api.example/x")

    assert fetcher.remaining == 4321


def test_remaining_is_unknown_before_any_request():
    assert Fetcher(transport=FakeTransport([]), sleep=lambda s: None).remaining is None
