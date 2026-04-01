# Hand-maintained: «RemnawaveSDK» как в remnapy, поверх OpenAPI 2.7+ клиента.
from __future__ import annotations

import logging
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from supn_remnawave_panel.configuration import Configuration
from supn_remnawave_panel.facade import RemnawavePanelApis, bind_panel_apis
from supn_remnawave_panel.models.revoke_user_subscription_body_dto import (
    RevokeUserSubscriptionBodyDto,
)
from supn_remnawave_panel.api.users_controller_api import UsersControllerApi
from supn_remnawave_panel.api.system_controller_api import SystemControllerApi
from supn_remnawave_panel.api.hwid_user_devices_controller_api import (
    HWIDUserDevicesControllerApi,
)
from supn_remnawave_panel.api.config_profiles_controller_api import (
    ConfigProfilesControllerApi,
)
from supn_remnawave_panel.api.hosts_controller_api import HostsControllerApi
from supn_remnawave_panel.api.nodes_controller_api import NodesControllerApi

from supn_remnawave_panel.remnapy_compat.bot_shims import (
    adapt_hosts_response,
    adapt_nodes_response,
    adapt_panel_stats,
)
from supn_remnawave_panel.remnapy_compat.models import (
    TelegramUserResponseDto,
    coerce_user_response,
    unwrap_inner,
    unwrap_until_attr,
)
from supn_remnawave_panel.remnapy_compat.webhooks import WebhookUtility
from supn_remnawave_panel.remnapy_compat._remna_api_client import RemnaApiClient


def _host_from_httpx_base_url(client: httpx.AsyncClient) -> str:
    raw = str(client.base_url).rstrip("/")
    if raw.endswith("/api"):
        raw = raw[:-4]
    return raw


class _LegacyControllerStub:
    """Плейсхолдер для методов панели, отсутствующих в текущем OpenAPI."""

    __slots__ = ("_label",)

    def __init__(self, label: str) -> None:
        object.__setattr__(self, "_label", label)

    def __getattr__(self, name: str) -> Any:
        raise NotImplementedError(
            f"{self._label}.{name}: нет в публичном OpenAPI панели "
            f"(в remnapy это мог быть отдельный эндпоинт; проверьте документацию панели)."
        )


class PrefixProxy:
    """Делегирует ``{prefix}_{method}`` на сгенерированный *ControllerApi."""

    __slots__ = ("_api", "_prefix")

    def __init__(self, api: object, prefix: str) -> None:
        object.__setattr__(self, "_api", api)
        object.__setattr__(self, "_prefix", prefix)

    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):
            raise AttributeError(name)
        long = f"{self._prefix}_{name}"
        fn = getattr(self._api, long, None)
        if callable(fn):
            return fn
        if hasattr(self._api, name):
            return getattr(self._api, name)
        raise AttributeError(
            f"{type(self._api).__name__!r} has no attribute {long!r} or {name!r}"
        )


class InboundsCompat:
    __slots__ = ("_profiles",)

    def __init__(self, config_profiles: ConfigProfilesControllerApi) -> None:
        object.__setattr__(self, "_profiles", config_profiles)

    async def get_all_inbounds(self, *args: Any, **kwargs: Any):
        r = await self._profiles.config_profile_controller_get_all_inbounds(
            *args, **kwargs
        )
        return unwrap_inner(r)

    async def get_inbounds_by_profile_uuid(self, *args: Any, **kwargs: Any):
        return await self._profiles.config_profile_controller_get_inbounds_by_profile_uuid(
            *args, **kwargs
        )

    def __getattr__(self, name: str) -> Any:
        return getattr(self._profiles, name)


class HostsCompat:
    __slots__ = ("_api",)

    def __init__(self, api: HostsControllerApi) -> None:
        object.__setattr__(self, "_api", api)

    async def get_all_hosts(self, *args: Any, **kwargs: Any):
        r = await self._api.hosts_controller_get_all_hosts(*args, **kwargs)
        inner = unwrap_inner(r) or []
        return adapt_hosts_response(inner)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._api, name)


class NodesCompat:
    __slots__ = ("_api",)

    def __init__(self, api: NodesControllerApi) -> None:
        object.__setattr__(self, "_api", api)

    async def get_all_nodes(self, *args: Any, **kwargs: Any):
        r = await self._api.nodes_controller_get_all_nodes(*args, **kwargs)
        inner = unwrap_inner(r) or []
        return adapt_nodes_response(inner)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._api, name)


class InternalSquadsCompat:
    """Как remnapy: ``get_internal_squads`` отдаёт объект с полем ``internal_squads``."""

    __slots__ = ("_api",)

    def __init__(self, api: object) -> None:
        object.__setattr__(self, "_api", api)

    async def get_internal_squads(self, *args: Any, **kwargs: Any):
        r = await self._api.internal_squad_controller_get_internal_squads(
            *args, **kwargs
        )
        return unwrap_until_attr(r, "internal_squads")

    def __getattr__(self, name: str) -> Any:
        return getattr(self._api, name)


class ExternalSquadsCompat:
    """Как remnapy: ``get_external_squads`` отдаёт объект с полем ``external_squads``."""

    __slots__ = ("_api", "_prefix")

    def __init__(self, api: object) -> None:
        object.__setattr__(self, "_api", api)
        object.__setattr__(self, "_prefix", "external_squad_controller")

    async def get_external_squads(self, *args: Any, **kwargs: Any):
        r = await self._api.external_squad_controller_get_external_squads(
            *args, **kwargs
        )
        return unwrap_until_attr(r, "external_squads")

    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):
            raise AttributeError(name)
        long = f"{self._prefix}_{name}"
        fn = getattr(self._api, long, None)
        if callable(fn):
            return fn
        if hasattr(self._api, name):
            return getattr(self._api, name)
        raise AttributeError(
            f"{type(self._api).__name__!r} has no attribute {long!r} or {name!r}"
        )


class UsersCompat:
    __slots__ = ("_api",)

    def __init__(self, api: UsersControllerApi) -> None:
        object.__setattr__(self, "_api", api)

    async def create_user(self, body, **_kw: Any):
        return coerce_user_response(
            unwrap_inner(await self._api.users_controller_create_user(body))
        )

    async def update_user(self, body, **_kw: Any):
        return coerce_user_response(
            unwrap_inner(await self._api.users_controller_update_user(body))
        )

    async def get_all_users(self, *args: Any, **kwargs: Any):
        return unwrap_inner(await self._api.users_controller_get_all_users(*args, **kwargs))

    async def delete_user(self, uuid: Union[str, UUID], *args: Any, **kwargs: Any):
        return unwrap_inner(
            await self._api.users_controller_delete_user(uuid, *args, **kwargs)
        )

    async def revoke_user_subscription(
        self,
        uuid: Union[str, UUID],
        body: Optional[RevokeUserSubscriptionBodyDto] = None,
        *args: Any,
        **kwargs: Any,
    ):
        b = body or RevokeUserSubscriptionBodyDto()
        return coerce_user_response(
            unwrap_inner(
                await self._api.users_controller_revoke_user_subscription(
                    str(uuid), b, *args, **kwargs
                )
            )
        )

    async def disable_user(self, uuid: Union[str, UUID], *args: Any, **kwargs: Any):
        return coerce_user_response(
            unwrap_inner(
                await self._api.users_controller_disable_user(uuid, *args, **kwargs)
            )
        )

    async def enable_user(self, uuid: Union[str, UUID], *args: Any, **kwargs: Any):
        return coerce_user_response(
            unwrap_inner(
                await self._api.users_controller_enable_user(uuid, *args, **kwargs)
            )
        )

    async def reset_user_traffic(self, uuid: Union[str, UUID], *args: Any, **kwargs: Any):
        return coerce_user_response(
            unwrap_inner(
                await self._api.users_controller_reset_user_traffic(uuid, *args, **kwargs)
            )
        )

    async def get_user_by_uuid(self, uuid: Union[str, UUID], *args: Any, **kwargs: Any):
        return coerce_user_response(
            unwrap_inner(
                await self._api.users_controller_get_user_by_uuid(uuid, *args, **kwargs)
            )
        )

    async def get_users_by_telegram_id(self, telegram_id: int, *args: Any, **kwargs: Any):
        r = await self._api.users_controller_get_user_by_telegram_id(
            str(telegram_id), *args, **kwargs
        )
        inner = unwrap_inner(r)
        if isinstance(inner, list):
            users = inner
        else:
            users = getattr(inner, "users", None) or []
        conv = [coerce_user_response(u) for u in users]
        return TelegramUserResponseDto([u for u in conv if u is not None])

    def __getattr__(self, name: str) -> Any:
        return getattr(self._api, name)


class SystemCompat:
    __slots__ = ("_api",)

    def __init__(self, api: SystemControllerApi) -> None:
        object.__setattr__(self, "_api", api)

    async def get_stats(self, *args: Any, **kwargs: Any):
        raw = unwrap_inner(await self._api.system_controller_get_stats(*args, **kwargs))
        if raw is None:
            return None
        return adapt_panel_stats(raw)

    async def get_metadata(self, *args: Any, **kwargs: Any):
        return unwrap_inner(
            await self._api.system_controller_get_metadata(*args, **kwargs)
        )

    def __getattr__(self, name: str) -> Any:
        return getattr(self._api, name)


class HWIDCompat:
    __slots__ = ("_api",)

    def __init__(self, api: HWIDUserDevicesControllerApi) -> None:
        object.__setattr__(self, "_api", api)

    async def get_hwid_user(self, uuid: Union[str, UUID], *args: Any, **kwargs: Any):
        return unwrap_inner(
            await self._api.hwid_user_devices_controller_get_user_hwid_devices(
                uuid, *args, **kwargs
            )
        )

    async def delete_hwid_to_user(self, body, *args: Any, **kwargs: Any):
        return unwrap_inner(
            await self._api.hwid_user_devices_controller_delete_user_hwid_device(
                body, *args, **kwargs
            )
        )

    async def delete_all_hwid_user(self, body, *args: Any, **kwargs: Any):
        return unwrap_inner(
            await self._api.hwid_user_devices_controller_delete_all_user_hwid_devices(
                body, *args, **kwargs
            )
        )

    async def get_hwid_users(self, *args: Any, **kwargs: Any):
        return await self._api.hwid_user_devices_controller_get_all_users(*args, **kwargs)

    async def get_hwid_stats(self, *args: Any, **kwargs: Any):
        return await self._api.hwid_user_devices_controller_get_hwid_devices_stats(
            *args, **kwargs
        )

    async def add_hwid_to_users(self, *args: Any, **kwargs: Any):
        return await self._api.hwid_user_devices_controller_create_user_hwid_device(
            *args, **kwargs
        )

    async def get_top_users_by_hwid_devices(self, *args: Any, **kwargs: Any):
        return await self._api.hwid_user_devices_controller_get_top_users_by_hwid_devices(
            *args, **kwargs
        )

    def __getattr__(self, name: str) -> Any:
        return getattr(self._api, name)


class RemnawaveSDK:
    """
    Точка входа в стиле ``remnapy.RemnawaveSDK``: те же имена групп и HTTP-клиент.

    Под капотом — сгенерированный OpenAPI-клиент (актуальный контракт панели).
    Для ``httpx.AsyncClient`` с ``base_url=.../api`` выполняется подмена пула запросов,
    чтобы использовались ваши заголовки (Cloudflare Access, Caddy и т.д.).
    """

    def __init__(
        self,
        client: Optional[httpx.AsyncClient] = None,
        base_url: Optional[str] = None,
        token: Optional[str] = None,
        caddy_token: Optional[str] = None,
        ssl_ignore: Optional[bool] = False,
        custom_headers: Optional[dict[str, str]] = None,
        cookies: Optional[dict[str, str]] = None,
    ) -> None:
        self._token = token
        self.base_url = base_url
        self.caddy_token = caddy_token
        self.ssl_ignore = ssl_ignore
        self.custom_headers = custom_headers or {}
        self.cookies = cookies

        self._owns_client = client is None
        self._httpx: httpx.AsyncClient
        self._api_client: RemnaApiClient
        self._panel: RemnawavePanelApis

        if client is None:
            if base_url is None or token is None:
                raise ValueError("base_url and token must be provided if client is not provided")
            host = base_url
            if host.endswith("/"):
                host = host[:-1]
            if host.endswith("/api"):
                host = host[:-4]
            cfg = Configuration(
                host=host,
                access_token=None,
                verify_ssl=not (ssl_ignore or False),
            )
            self._httpx = self._build_httpx_from_params(host + "/api")
            self._api_client = RemnaApiClient(cfg)
            self._api_client.rest_client.pool_manager = self._httpx
            self._panel = bind_panel_apis(self._api_client)
        else:
            if base_url is not None or token is not None:
                logging.warning("base_url and token are ignored when httpx client is provided")
            if cookies is not None:
                logging.warning("cookies are ignored when httpx client is provided")
            self._httpx = client
            host = _host_from_httpx_base_url(client)
            cfg = Configuration(host=host, access_token=None, verify_ssl=True)
            self._api_client = RemnaApiClient(cfg)
            self._api_client.rest_client.pool_manager = self._httpx
            self._panel = bind_panel_apis(self._api_client)

        # --- Группы как в remnapy ---
        self.api_tokens_management = PrefixProxy(
            self._panel.api_tokens, "api_tokens_controller"
        )
        self.auth = PrefixProxy(self._panel.auth, "auth_controller")
        self.bandwidthstats = self._panel.bandwidth_stats
        self.config_profiles = PrefixProxy(
            self._panel.config_profiles, "config_profile_controller"
        )
        self.hosts = HostsCompat(self._panel.hosts)
        self.hosts_bulk_actions = PrefixProxy(
            self._panel.hosts_bulk, "hosts_bulk_actions_controller"
        )
        self.hwid = HWIDCompat(self._panel.hwid_devices)
        self.inbounds = InboundsCompat(self._panel.config_profiles)
        self.inbounds_bulk_actions = _LegacyControllerStub("inbounds_bulk_actions")
        self.infra_billing = PrefixProxy(
            self._panel.infra_billing, "infra_billing_controller"
        )
        self.internal_squads = InternalSquadsCompat(self._panel.internal_squads)
        self.keygen = PrefixProxy(self._panel.keygen, "keygen_controller")
        self.node_plugins = PrefixProxy(self._panel.node_plugins, "node_plugin_controller")
        self.nodes = NodesCompat(self._panel.nodes)
        self.subscription = PrefixProxy(
            self._panel.subscriptions_public, "subscription_controller"
        )
        self.subscriptions = PrefixProxy(
            self._panel.subscriptions_protected, "subscriptions_controller"
        )
        self.subscriptions_settings = PrefixProxy(
            self._panel.subscription_settings, "subscription_settings_controller"
        )
        self.subscriptions_template = PrefixProxy(
            self._panel.subscription_template, "subscription_template_controller"
        )
        self.subscription_request_history = PrefixProxy(
            self._panel.subscription_request_history,
            "user_subscription_request_history_controller",
        )
        self.system = SystemCompat(self._panel.system)
        self.users = UsersCompat(self._panel.users)
        self.users_bulk_actions = PrefixProxy(
            self._panel.users_bulk, "users_bulk_actions_controller"
        )
        self.webhook_utility = WebhookUtility()
        self.xray_config = _LegacyControllerStub("xray_config")
        self.passkeys = PrefixProxy(self._panel.passkeys, "passkey_controller")
        self.external_squads = ExternalSquadsCompat(self._panel.external_squads)
        self.snippets = PrefixProxy(self._panel.snippets, "snippets_controller")
        self.remnawave_settings = PrefixProxy(
            self._panel.remnawave_settings, "remnawave_settings_controller"
        )
        self.subscription_page_config = PrefixProxy(
            self._panel.subscription_page_configs,
            "subscription_page_config_controller",
        )
        self.ip_control = PrefixProxy(
            self._panel.ip_management, "ip_control_controller"
        )

    @property
    def _client(self) -> httpx.AsyncClient:
        """Как в remnapy: исходный httpx-клиент."""
        return self._httpx

    def _build_httpx_from_params(self, base: str) -> httpx.AsyncClient:
        headers = self._prepare_headers_standalone()
        ck = self.cookies if self.cookies is not None else None
        return httpx.AsyncClient(
            base_url=base,
            headers=headers,
            cookies=ck,
            verify=not (self.ssl_ignore or False),
        )

    def _prepare_headers_standalone(self) -> dict[str, str]:
        headers: dict[str, str] = {}
        if self._token:
            t = self._token
            headers["Authorization"] = t if t.startswith("Bearer ") else f"Bearer {t}"
        if self.caddy_token is not None:
            headers["X-Api-Key"] = self.caddy_token
        headers.update(self.custom_headers)
        if self.base_url and "http://" in self.base_url:
            headers["x-forwarded-proto"] = "https"
            headers["x-forwarded-for"] = "127.0.0.1"
        return headers

    async def aclose(self) -> None:
        """Закрыть соединения SDK (если клиент создан внутри конструктора)."""
        if self._owns_client:
            await self._api_client.close()
