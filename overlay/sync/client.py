# coding: utf-8
"""High-level convenience client for the Cleanlist API (synchronous).

This thin facade is hand-authored (not generated) and re-applied on every
regeneration by ``scripts/generate.sh``. It wires an authenticated
``ApiClient`` to every resource group so you can write::

    from cleanlist_ai import Cleanlist

    with Cleanlist(access_token="sk_live_...") as cl:
        me = cl.workspace.whoami()
        lst = cl.lead_lists.create_list(CreateListRequest(name="Q3 outbound"))

You can always drop down to the generated API classes directly if you prefer
(``from cleanlist_ai.api import PublicWorkspaceApi``); this is just sugar.
"""
from __future__ import annotations

import os
from typing import Optional

from cleanlist_ai.api_client import ApiClient
from cleanlist_ai.configuration import Configuration
from cleanlist_ai.api.public_enrichment_api import PublicEnrichmentApi
from cleanlist_ai.api.public_export_api import PublicExportApi
from cleanlist_ai.api.public_lead_lists_api import PublicLeadListsApi
from cleanlist_ai.api.public_smart_agents_api import PublicSmartAgentsApi
from cleanlist_ai.api.public_workspace_api import PublicWorkspaceApi

#: Production API base URL.
DEFAULT_HOST = "https://api.cleanlist.ai"

#: Environment variable read when ``access_token`` is not passed explicitly.
API_KEY_ENV_VAR = "CLEANLIST_API_KEY"


class Cleanlist:
    """Authenticated entry point exposing every Cleanlist API resource group.

    :param access_token: Your Cleanlist API key (sent as ``Authorization:
        Bearer <token>``). Falls back to the ``CLEANLIST_API_KEY`` env var.
    :param host: API base URL. Defaults to production; point at
        ``http://localhost:8000`` for local development.
    :param configuration: Supply a fully-built :class:`Configuration` for
        advanced needs (proxies, timeouts, retries); ``access_token`` / ``host``
        are applied on top of it when given.

    Resource groups:
        * :attr:`workspace`   – identity, credits, API keys, usage
        * :attr:`lead_lists`  – create/manage lists and their leads
        * :attr:`enrichment`  – person/company/bulk enrichment + status polling
        * :attr:`smart_agents`– run smart agents and fetch results
        * :attr:`export`      – CSV (signed URL) and JSON export
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

    def close(self) -> None:
        """Release the underlying urllib3 connection pool."""
        rest = getattr(self.api_client, "rest_client", None)
        pool = getattr(rest, "pool_manager", None)
        if pool is not None:
            pool.clear()

    def __enter__(self) -> "Cleanlist":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()
