# Hand-maintained: listed in .openapi-generator-ignore (not overwritten on generate).
"""Высокоуровневая группировка контроллеров в духе `RemnawaveSDK` / «одна точка входа».

Использование::

    async with open_remnawave_panel(host, token) as panel:
        stats = await panel.system.system_controller_get_stats()

Все атрибуты — те же классы `*ControllerApi`, что и в OpenAPI Generator; имена методов
не менялись (например ``users_controller_get_user_by_uuid``).
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import Any, AsyncIterator

from supn_remnawave_panel.api.api_tokens_controller_api import APITokensControllerApi
from supn_remnawave_panel.api.auth_controller_api import AuthControllerApi
from supn_remnawave_panel.api.bandwidth_stats_controller_api import BandwidthStatsControllerApi
from supn_remnawave_panel.api.config_profiles_controller_api import ConfigProfilesControllerApi
from supn_remnawave_panel.api.external_squads_controller_api import ExternalSquadsControllerApi
from supn_remnawave_panel.api.hosts_bulk_actions_controller_api import HostsBulkActionsControllerApi
from supn_remnawave_panel.api.hosts_controller_api import HostsControllerApi
from supn_remnawave_panel.api.hwid_user_devices_controller_api import HWIDUserDevicesControllerApi
from supn_remnawave_panel.api.infra_billing_controller_api import InfraBillingControllerApi
from supn_remnawave_panel.api.internal_squads_controller_api import InternalSquadsControllerApi
from supn_remnawave_panel.api.ip_management_controller_api import IPManagementControllerApi
from supn_remnawave_panel.api.keygen_controller_api import KeygenControllerApi
from supn_remnawave_panel.api.metadata_controller_api import MetadataControllerApi
from supn_remnawave_panel.api.node_plugins_controller_api import NodePluginsControllerApi
from supn_remnawave_panel.api.nodes_controller_api import NodesControllerApi
from supn_remnawave_panel.api.passkeys_controller_api import PasskeysControllerApi
from supn_remnawave_panel.api.protected_subscriptions_controller_api import (
    ProtectedSubscriptionsControllerApi,
)
from supn_remnawave_panel.api.public_subscription_controller_api import PublicSubscriptionControllerApi
from supn_remnawave_panel.api.remnawave_settings_controller_api import RemnawaveSettingsControllerApi
from supn_remnawave_panel.api.snippets_controller_api import SnippetsControllerApi
from supn_remnawave_panel.api.subscription_page_configs_controller_api import (
    SubscriptionPageConfigsControllerApi,
)
from supn_remnawave_panel.api.subscription_request_history_controller_api import (
    SubscriptionRequestHistoryControllerApi,
)
from supn_remnawave_panel.api.subscription_settings_controller_api import (
    SubscriptionSettingsControllerApi,
)
from supn_remnawave_panel.api.subscription_template_controller_api import (
    SubscriptionTemplateControllerApi,
)
from supn_remnawave_panel.api.system_controller_api import SystemControllerApi
from supn_remnawave_panel.api.users_bulk_actions_controller_api import UsersBulkActionsControllerApi
from supn_remnawave_panel.api.users_controller_api import UsersControllerApi
from supn_remnawave_panel.api_client import ApiClient
from supn_remnawave_panel.configuration import Configuration

__all__ = [
    "RemnawavePanelApis",
    "bind_panel_apis",
    "open_remnawave_panel",
]


@dataclass(frozen=True, slots=True)
class RemnawavePanelApis:
    """Согруппированные API; имена ближе к панели / remnapy, без обёрток над методами."""

    client: ApiClient
    api_tokens: APITokensControllerApi
    auth: AuthControllerApi
    bandwidth_stats: BandwidthStatsControllerApi
    config_profiles: ConfigProfilesControllerApi
    external_squads: ExternalSquadsControllerApi
    hosts: HostsControllerApi
    hosts_bulk: HostsBulkActionsControllerApi
    hwid_devices: HWIDUserDevicesControllerApi
    infra_billing: InfraBillingControllerApi
    internal_squads: InternalSquadsControllerApi
    ip_management: IPManagementControllerApi
    keygen: KeygenControllerApi
    metadata: MetadataControllerApi
    node_plugins: NodePluginsControllerApi
    nodes: NodesControllerApi
    passkeys: PasskeysControllerApi
    remnawave_settings: RemnawaveSettingsControllerApi
    snippets: SnippetsControllerApi
    subscription_page_configs: SubscriptionPageConfigsControllerApi
    subscription_request_history: SubscriptionRequestHistoryControllerApi
    subscription_settings: SubscriptionSettingsControllerApi
    subscription_template: SubscriptionTemplateControllerApi
    system: SystemControllerApi
    users: UsersControllerApi
    users_bulk: UsersBulkActionsControllerApi
    subscriptions_protected: ProtectedSubscriptionsControllerApi
    subscriptions_public: PublicSubscriptionControllerApi


def bind_panel_apis(client: ApiClient) -> RemnawavePanelApis:
    """Связать уже открытый ``ApiClient`` с группой контроллеров (например свой DI)."""
    return RemnawavePanelApis(
        client=client,
        api_tokens=APITokensControllerApi(client),
        auth=AuthControllerApi(client),
        bandwidth_stats=BandwidthStatsControllerApi(client),
        config_profiles=ConfigProfilesControllerApi(client),
        external_squads=ExternalSquadsControllerApi(client),
        hosts=HostsControllerApi(client),
        hosts_bulk=HostsBulkActionsControllerApi(client),
        hwid_devices=HWIDUserDevicesControllerApi(client),
        infra_billing=InfraBillingControllerApi(client),
        internal_squads=InternalSquadsControllerApi(client),
        ip_management=IPManagementControllerApi(client),
        keygen=KeygenControllerApi(client),
        metadata=MetadataControllerApi(client),
        node_plugins=NodePluginsControllerApi(client),
        nodes=NodesControllerApi(client),
        passkeys=PasskeysControllerApi(client),
        remnawave_settings=RemnawaveSettingsControllerApi(client),
        snippets=SnippetsControllerApi(client),
        subscription_page_configs=SubscriptionPageConfigsControllerApi(client),
        subscription_request_history=SubscriptionRequestHistoryControllerApi(client),
        subscription_settings=SubscriptionSettingsControllerApi(client),
        subscription_template=SubscriptionTemplateControllerApi(client),
        system=SystemControllerApi(client),
        users=UsersControllerApi(client),
        users_bulk=UsersBulkActionsControllerApi(client),
        subscriptions_protected=ProtectedSubscriptionsControllerApi(client),
        subscriptions_public=PublicSubscriptionControllerApi(client),
    )


@asynccontextmanager
async def open_remnawave_panel(
    host: str,
    access_token: str,
    **configuration_kwargs: Any,
) -> AsyncIterator[RemnawavePanelApis]:
    """Async context: корень панели ``host`` (без ``/api``), Bearer — ``access_token``."""
    config = Configuration(
        host=host.rstrip("/"),
        access_token=access_token,
        **configuration_kwargs,
    )
    async with ApiClient(config) as client:
        yield bind_panel_apis(client)
