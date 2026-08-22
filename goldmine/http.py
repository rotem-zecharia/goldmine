"""The only module that touches the network.

The transport, clock, and sleep function are injected so the whole test suite
runs offline and instantly.
"""

from __future__ import annotations

import time


class RateLimited(RuntimeError):
    """The rate limit did not clear within the retry budget."""


class Fetcher:
    def __init__(self, transport=None, sleep=time.sleep, now=time.time, max_retries=4, token=None):
        if transport is None:
            import requests

            transport = requests.Session()
        self._transport = transport
        self._sleep = sleep
        self._now = now
        self._max_retries = max_retries
        self._token = token
        self._cache: dict[str, tuple[str, object, dict]] = {}
        self.remaining: int | None = None

    def _headers(self, url: str) -> dict:
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "goldmine"}
        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"
        cached = self._cache.get(url)
        if cached:
            headers["If-None-Match"] = cached[0]
        return headers

    def _request(self, url: str, want: str):
        body, _ = self._request_meta(url, want)
        return body

    def _request_meta(self, url: str, want: str):
        for attempt in range(self._max_retries):
            response = self._transport.get(url, headers=self._headers(url), timeout=30)

            if response.status_code == 304:
                etag, body, headers = self._cache[url]
                return body, headers

            if response.status_code == 404:
                return None, {}

            if response.status_code == 200:
                body = response.json() if want == "json" else response.text
                headers = dict(response.headers)
                if "X-RateLimit-Remaining" in headers:
                    self.remaining = int(headers["X-RateLimit-Remaining"])
                etag = headers.get("ETag")
                if etag:
                    self._cache[url] = (etag, body, headers)
                return body, headers

            wait = self._throttle_seconds(response)
            if wait is not None:
                self._sleep(wait)
                continue

            if response.status_code >= 500:
                self._sleep(2**attempt)
                continue

            # 401 means a bad token and 422 a malformed query; both are our bug,
            # not a transient one, so surface them rather than burning retries.
            raise RuntimeError(
                f"{response.status_code} from {url}: {getattr(response, 'text', '')[:200]}"
            )

        raise RateLimited(f"gave up on {url} after {self._max_retries} attempts")

    def get_json(self, url: str):
        return self._request(url, want="json")

    def get_json_meta(self, url: str):
        """(body, response headers) - needed for pagination Link headers."""
        return self._request_meta(url, want="json")

    def get_text(self, url: str):
        return self._request(url, want="text")

    def _throttle_seconds(self, response) -> float | None:
        """Seconds to wait, or None when this response is not a throttle."""
        if response.status_code not in (403, 429):
            return None

        # Secondary (abuse) limits send Retry-After and no Remaining header.
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            return max(1.0, float(retry_after))

        if response.headers.get("X-RateLimit-Remaining") == "0":
            reset = float(response.headers.get("X-RateLimit-Reset", 0))
            return max(1.0, reset - self._now() + 1.0)

        return None
