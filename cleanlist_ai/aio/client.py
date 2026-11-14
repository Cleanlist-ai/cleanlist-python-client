# coding: utf-8
"""High-level convenience client for the Cleanlist API (asynchronous).

This thin facade is hand-authored (not generated) and re-applied on every
regeneration by ``scripts/generate.sh``. It wires an authenticated async
``ApiClient`` to every resource group so you can write::

    from cleanlist_ai.aio import Cleanlist

    async with Cleanlist(access_token="sk_live_...") as cl:
        me = await cl.workspace.whoami()
        lst = await cl.lead_lists.create_list(CreateListRequest(name="Q3 outbound"))

You can always drop down to the generated API classes directly if you prefer
(``from cleanlist_ai.aio.api import PublicWorkspaceApi``); this is just sugar.
"""
from __future__ import annotations

import asyncio
import os
from typing import Optional

from cleanlist_ai.aio.api_client import ApiClient
from cleanlist_ai.retry import (
    DEFAULT_MAX_ATTEMPTS,
    ResponseMeta,
    add_idempotency_key,
    can_retry,
    read_response_meta,
    retry_delay,
)
from cleanlist_ai.aio.configuration import Configuration
from cleanlist_ai.aio.api.public_accounts_data_api import PublicAccountsDataApi
from cleanlist_ai.aio.api.public_actions_api import PublicActionsApi
from cleanlist_ai.aio.api.public_enrichment_api import PublicEnrichmentApi
from cleanlist_ai.aio.api.public_export_api import PublicExportApi
from cleanlist_ai.aio.api.public_gtm_agents_api import PublicGTMAgentsApi
from cleanlist_ai.aio.api.public_gtm_tasks_api import PublicGTMTasksApi
from cleanlist_ai.aio.api.public_inbox_api import PublicInboxApi
from cleanlist_ai.aio.api.public_lead_lists_api import PublicLeadListsApi
from cleanlist_ai.aio.api.public_people_finder_api import PublicPeopleFinderApi
from cleanlist_ai.aio.api.public_plays_api import PublicPlaysApi
from cleanlist_ai.aio.api.public_signals_api import PublicSignalsApi
from cleanlist_ai.aio.api.public_smart_agents_api import PublicSmartAgentsApi
from cleanlist_ai.aio.api.public_webhooks_api import PublicWebhooksApi
from cleanlist_ai.aio.api.public_workspace_api import PublicWorkspaceApi

#: Production API base URL.
DEFAULT_HOST = "https://api.cleanlist.ai"

#: Environment variable read when ``access_token`` is not passed explicitly.
API_KEY_ENV_VAR = "CLEANLIST_API_KEY"


class RetryingApiClient(ApiClient):
    """``ApiClient`` that retries 429s and 5xx and keys writes for idempotency.

    Each write gets one ``Idempotency-Key`` (a key passed in ``_headers`` wins),
    reused on its retries so a retried write runs once. Waits honor
    ``Retry-After``; a wait over a minute returns the response instead.
    """

    def __init__(self, configuration: Configuration, max_attempts: int = DEFAULT_MAX_ATTEMPTS) -> None:
        super().__init__(configuration)
        self.max_attempts = max(1, int(max_attempts))
        #: Rate-limit, mode and replay headers of the most recent response.
        self.last_response: Optional[ResponseMeta] = None

    async def call_api(self, method, url, header_params=None, body=None, post_params=None, _request_timeout=None):
        header_params = add_idempotency_key(method, header_params)
        max_attempts = self.max_attempts if can_retry(method, header_params) else 1
        attempt = 1
        while True:
            response = await super().call_api(method, url, header_params, body, post_params, _request_timeout)
            delay = retry_delay(response.status, response.getheader("Retry-After"), attempt, max_attempts)
            if delay is None:
                break
            try:
                response.response.release()
            except Exception:  # noqa: BLE001 - nothing left to free
                pass
            await asyncio.sleep(delay)
            attempt += 1
        self.last_response = read_response_meta(response.status, response.getheaders())
        return response


class Cleanlist:
    """Authenticated async entry point exposing every Cleanlist API resource group.

    Use it as an async context manager so the underlying aiohttp session is
    closed cleanly::

        async with Cleanlist() as cl:          # reads CLEANLIST_API_KEY
            me = await cl.workspace.whoami()

    :param access_token: Your Cleanlist API key (sent as ``Authorization:
        Bearer <token>``). Falls back to the ``CLEANLIST_API_KEY`` env var.
    :param host: API base URL. Defaults to production; point at
        ``http://localhost:8000`` for local development.
    :param configuration: Supply a fully-built :class:`Configuration` for
        advanced needs; ``access_token`` / ``host`` are applied on top of it.
    :param max_attempts: Tries per request, the first included (default 3).
        429s and 5xx are retried with backoff, honoring ``Retry-After``; writes
        carry an ``Idempotency-Key`` that stays the same across retries. Pass
        ``_headers={"Idempotency-Key": "..."}`` on a call to set your own.
        ``1`` turns retries off.

    Resource groups mirror the synchronous client: :attr:`workspace`,
    :attr:`lead_lists`, :attr:`people_finder`, :attr:`enrichment`,
    :attr:`smart_agents`, :attr:`export`, :attr:`actions`, :attr:`gtm_agents`,
    :attr:`plays`, :attr:`gtm_tasks`, :attr:`inbox`, :attr:`signals`,
    :attr:`accounts_data`, :attr:`webhooks`.
    """

    def __init__(
        self,
        access_token: Optional[str] = None,
        *,
        host: str = DEFAULT_HOST,
        configuration: Optional[Configuration] = None,
        max_attempts: int = DEFAULT_MAX_ATTEMPTS,
    ) -> None:
        access_token = access_token or os.getenv(API_KEY_ENV_VAR)
        if not access_token:
            raise ValueError(
                "A Cleanlist API key is required. Pass access_token=... or set "
                f"the {API_KEY_ENV_VAR} environment variable."
            )

        if configuration is None:
            configuration = Configuration(host=host, access_token=access_token)
        else:
            configuration.access_token = access_token
            if host != DEFAULT_HOST:
                configuration.host = host

        self.configuration = configuration
        self.api_client = RetryingApiClient(configuration, max_attempts)
        self._key_mode = "test" if access_token.startswith("clapi_test_") else "live"

        self.workspace = PublicWorkspaceApi(self.api_client)
        self.lead_lists = PublicLeadListsApi(self.api_client)
        self.people_finder = PublicPeopleFinderApi(self.api_client)
        self.enrichment = PublicEnrichmentApi(self.api_client)
        self.smart_agents = PublicSmartAgentsApi(self.api_client)
        self.export = PublicExportApi(self.api_client)
        self.actions = PublicActionsApi(self.api_client)
        self.gtm_agents = PublicGTMAgentsApi(self.api_client)
        self.plays = PublicPlaysApi(self.api_client)
        self.gtm_tasks = PublicGTMTasksApi(self.api_client)
        self.inbox = PublicInboxApi(self.api_client)
        self.signals = PublicSignalsApi(self.api_client)
        self.accounts_data = PublicAccountsDataApi(self.api_client)
        self.webhooks = PublicWebhooksApi(self.api_client)

    @property
    def last_response(self) -> Optional[ResponseMeta]:
        """Rate-limit, mode and replay headers of the most recent response."""
        return self.api_client.last_response

    @property
    def mode(self) -> str:
        """``"test"`` when the server says so (``Cleanlist-Mode: test``), else what the key prefix implies."""
        last = self.api_client.last_response
        return (last.mode if last is not None else None) or self._key_mode

    async def close(self) -> None:
        """Close the underlying aiohttp client session."""
        await self.api_client.close()

    async def __aenter__(self) -> "Cleanlist":
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        await self.close()
