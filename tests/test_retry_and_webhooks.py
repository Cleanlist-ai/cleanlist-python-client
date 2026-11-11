import asyncio
import hashlib
import hmac
import json

import pytest
from pydantic import ValidationError

import cleanlist_ai.aio.client as aio_client_module
import cleanlist_ai.client as client_module
from cleanlist_ai import ApiException, Cleanlist, CreateListRequest, verify_webhook_signature
from cleanlist_ai import rest
from cleanlist_ai.aio import Cleanlist as AsyncCleanlist
from cleanlist_ai.aio import CreateListRequest as AsyncCreateListRequest
from cleanlist_ai.aio import rest as aio_rest
from cleanlist_ai.retry import RateLimit, retry_delay

LIST = {"list_id": "l1", "name": "Q3", "lead_count": 0, "enriched_count": 0}
RATE_HEADERS = {
    "X-RateLimit-Limit": "600",
    "X-RateLimit-Remaining": "599",
    "X-RateLimit-Reset": "1762790400",
}


class FakeResp:
    def __init__(self, status, body=None, headers=None):
        self.status = status
        self.reason = "x"
        self.headers = {"Content-Type": "application/json", **(headers or {})}
        self.data = json.dumps(body if body is not None else {"error": {"code": "x"}}).encode()
        self.released = False

    def release_conn(self):
        self.released = True

    def release(self):
        self.released = True


class AsyncFakeResp(FakeResp):
    async def read(self):
        return self.data


def install(cl, responses, aio=False):
    calls = []

    def pick(method, url, headers):
        calls.append({"method": method, "url": url, "headers": dict(headers or {})})
        return responses[min(len(calls) - 1, len(responses) - 1)]

    if aio:

        async def request(method, url, headers=None, body=None, post_params=None, _request_timeout=None):
            return aio_rest.RESTResponse(pick(method, url, headers))

    else:

        def request(method, url, headers=None, body=None, post_params=None, _request_timeout=None):
            return rest.RESTResponse(pick(method, url, headers))

    cl.api_client.rest_client.request = request
    return calls


@pytest.fixture
def waits(monkeypatch):
    slept = []
    monkeypatch.setattr(client_module.time, "sleep", slept.append)

    async def fake_sleep(delay):
        slept.append(delay)

    monkeypatch.setattr(aio_client_module.asyncio, "sleep", fake_sleep)
    return slept


def test_retries_429_and_5xx_with_one_idempotency_key(waits):
    cl = Cleanlist("clapi_live_abc", host="https://x")
    first = FakeResp(429, headers={"Retry-After": "2"})
    calls = install(cl, [first, FakeResp(503, headers={"Retry-After": "0"}), FakeResp(200, LIST, RATE_HEADERS)])
    lst = cl.lead_lists.create_list(CreateListRequest(name="Q3"))
    assert lst.list_id == "l1"
    assert len(calls) == 3
    assert waits[0] == 2.0
    assert first.released
    keys = {c["headers"]["Idempotency-Key"] for c in calls}
    assert len(keys) == 1 and keys.pop()
    assert cl.last_response.rate_limit == RateLimit(600, 599, 1762790400)
    assert cl.mode == "live"


def test_caller_key_wins_and_reads_get_none(waits):
    cl = Cleanlist("clapi_live_abc", host="https://x")
    calls = install(cl, [FakeResp(200, LIST)])
    cl.lead_lists.create_list(CreateListRequest(name="Q3"), _headers={"Idempotency-Key": "order-1"})
    cl.lead_lists.create_list(CreateListRequest(name="Q3"))
    assert calls[0]["headers"]["Idempotency-Key"] == "order-1"
    assert calls[1]["headers"]["Idempotency-Key"] not in ("order-1", None)
    with pytest.raises(ValidationError):
        cl.workspace.whoami()  # body doesn't parse as WhoamiResponse; only the headers matter here
    assert "Idempotency-Key" not in calls[2]["headers"]


def test_gives_up_after_max_attempts_and_raises(waits):
    cl = Cleanlist("clapi_live_abc", host="https://x", max_attempts=2)
    calls = install(cl, [FakeResp(500, headers={"Retry-After": "0"})])
    with pytest.raises(ApiException) as err:
        cl.workspace.whoami()
    assert err.value.status == 500
    assert len(calls) == 2


def test_no_retry_on_4xx_or_long_retry_after(waits):
    cl = Cleanlist("clapi_live_abc", host="https://x")
    calls = install(cl, [FakeResp(422)])
    with pytest.raises(ApiException):
        cl.workspace.whoami()
    calls_daily = install(cl, [FakeResp(429, headers={"Retry-After": "3600"})])
    with pytest.raises(ApiException):
        cl.workspace.whoami()
    assert len(calls) == 1 and len(calls_daily) == 1
    assert waits == []


def test_mode_from_key_then_from_server():
    assert Cleanlist("clapi_test_abc", host="https://x").mode == "test"
    cl = Cleanlist("clapi_live_abc", host="https://x")
    install(cl, [FakeResp(200, LIST, {"Cleanlist-Mode": "test", "Idempotent-Replayed": "true"})])
    cl.lead_lists.create_list(CreateListRequest(name="Q3"))
    assert cl.mode == "test"
    assert cl.last_response.idempotent_replayed is True
    assert cl.last_response.rate_limit is None


def test_async_client_retries_with_one_key(waits):
    async def run():
        cl = AsyncCleanlist("clapi_test_abc", host="https://x")
        responses = [AsyncFakeResp(429, headers={"Retry-After": "1"}), AsyncFakeResp(200, LIST, RATE_HEADERS)]
        calls = install(cl, responses, aio=True)
        lst = await cl.lead_lists.create_list(AsyncCreateListRequest(name="Q3"))
        await cl.close()
        return cl, calls, lst

    cl, calls, lst = asyncio.run(run())
    assert lst.list_id == "l1"
    assert waits == [1.0]
    assert calls[0]["headers"]["Idempotency-Key"] == calls[1]["headers"]["Idempotency-Key"]
    assert cl.last_response.rate_limit.remaining == 599
    assert cl.mode == "test"


def test_retry_delay_backoff_and_http_date():
    assert 0.5 <= retry_delay(503, None, 1, 3) <= 0.75
    assert 1.0 <= retry_delay(503, None, 2, 3) <= 1.25
    assert retry_delay(503, None, 3, 3) is None
    assert retry_delay(400, None, 1, 3) is None
    assert retry_delay(429, "Wed, 21 Oct 2015 07:28:00 GMT", 1, 3) == 0.0
    assert 0.5 <= retry_delay(429, "soon", 1, 3) <= 0.75


def _sign(secret, t, body):
    return f"t={t},v1=" + hmac.new(secret.encode(), f"{t}.".encode() + body, hashlib.sha256).hexdigest()


def test_verify_webhook_signature():
    body = b'{"id":"evt_1","type":"reply.received","data":{}}'
    now = 1762790400
    header = _sign("whsec", now, body)
    assert verify_webhook_signature(body, header, "whsec", now=now)
    assert verify_webhook_signature(body.decode(), header, "whsec", now=now)
    assert not verify_webhook_signature(body + b" ", header, "whsec", now=now)
    assert not verify_webhook_signature(body, header, "other", now=now)
    assert not verify_webhook_signature(body, header, "whsec", now=now + 301)
    assert verify_webhook_signature(body, "v1=" + "0" * 64 + "," + header, "whsec", now=now)
    for junk in (None, "", "garbage", "t=abc,v1=" + "0" * 64, f"t={now}", f"t={now},v1=zz", "t=²,v1=" + "0" * 64):
        assert not verify_webhook_signature(body, junk, "whsec", now=now)


def test_a_429_is_retried_only_max_attempts_times_over_a_real_connection():
    """urllib3 honors Retry-After on its own unless told not to: max_attempts=1
    made 4 requests and the default 12, past the one-minute wait cap."""
    import threading
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

    hits = []

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            hits.append(self.command)
            self.send_response(429)
            self.send_header("Retry-After", "0")
            self.send_header("Content-Length", "0")
            self.end_headers()

        def log_message(self, *_args):
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    host = f"http://127.0.0.1:{server.server_address[1]}"
    try:
        for attempts in (1, 2):
            hits.clear()
            cl = Cleanlist("clapi_test_stub", host=host, max_attempts=attempts)
            response = cl.api_client.call_api("GET", host + "/api/v2/whoami", {})
            assert response.status == 429
            assert len(hits) == attempts
    finally:
        server.shutdown()
