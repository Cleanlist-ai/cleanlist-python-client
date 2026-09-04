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

import os
from typing import Optional

from cleanlist_ai.aio.api_client import ApiClient
from cleanlist_ai.aio.configuration import Configuration
from cleanlist_ai.aio.api.public_enrichment_api import PublicEnrichmentApi
from cleanlist_ai.aio.api.public_export_api import PublicExportApi
from cleanlist_ai.aio.api.public_lead_lists_api import PublicLeadListsApi
from cleanlist_ai.aio.api.public_smart_agents_api import PublicSmartAgentsApi
from cleanlist_ai.aio.api.public_workspace_api import PublicWorkspaceApi

#: Production API base URL.
DEFAULT_HOST = "https://api.cleanlist.ai"

#: Environment variable read when ``access_token`` is not passed explicitly.
API_KEY_ENV_VAR = "CLEANLIST_API_KEY"


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

    Resource groups mirror the synchronous client: :attr:`workspace`,
    :attr:`lead_lists`, :attr:`enrichment`, :attr:`smart_agents`, :attr:`export`.
    """

    def __init__(
        self,
        access_token: Optional[str] = None,
        *,
        host: str = DEFAULT_HOST,
        configuration: Optional[Configuration] = None,
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
        self.api_client = ApiClient(configuration)

        self.workspace = PublicWorkspaceApi(self.api_client)
        self.lead_lists = PublicLeadListsApi(self.api_client)
        self.enrichment = PublicEnrichmentApi(self.api_client)
        self.smart_agents = PublicSmartAgentsApi(self.api_client)
        self.export = PublicExportApi(self.api_client)

    async def close(self) -> None:
        """Close the underlying aiohttp client session."""
        await self.api_client.close()

    async def __aenter__(self) -> "Cleanlist":
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        await self.close()
