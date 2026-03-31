# Hand-maintained: совместимость дашборда/бота с ответами панели 2.7+ при ожидании полей remnapy 2.6.x.
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, TypeVar

from supn_remnawave_panel.models.create_host_response_dto_response import (
    CreateHostResponseDtoResponse,
)
from supn_remnawave_panel.models.create_node_response_dto_response import (
    CreateNodeResponseDtoResponse,
)
from supn_remnawave_panel.models.get_stats_response_dto_response import (
    GetStatsResponseDtoResponse,
)
from supn_remnawave_panel.models.get_stats_response_dto_response_cpu import (
    GetStatsResponseDtoResponseCpu,
)
from supn_remnawave_panel.models.get_stats_response_dto_response_memory import (
    GetStatsResponseDtoResponseMemory,
)

T = TypeVar("T")


@dataclass(slots=True)
class _CpuShim:
    _raw: GetStatsResponseDtoResponseCpu

    @property
    def cores(self) -> Any:
        return self._raw.cores

    @property
    def physical_cores(self) -> Any:
        ap = getattr(self._raw, "additional_properties", None) or {}
        if "physicalCores" in ap:
            return ap["physicalCores"]
        if "physical_cores" in ap:
            return ap["physical_cores"]
        return self._raw.cores


@dataclass(slots=True)
class _MemoryShim:
    _raw: GetStatsResponseDtoResponseMemory

    @property
    def total(self) -> Any:
        return self._raw.total

    @property
    def free(self) -> Any:
        return self._raw.free

    @property
    def used(self) -> Any:
        return self._raw.used

    @property
    def active(self) -> Any:
        ap = getattr(self._raw, "additional_properties", None) or {}
        if "active" in ap:
            return ap["active"]
        return self._raw.used


@dataclass(slots=True)
class StatsResponseShim:
    """Обёртка над ``GetStatsResponseDtoResponse`` с полями как у remnapy (CPU/memory)."""

    _raw: GetStatsResponseDtoResponse

    @property
    def cpu(self) -> _CpuShim:
        return _CpuShim(self._raw.cpu)

    @property
    def memory(self) -> _MemoryShim:
        return _MemoryShim(self._raw.memory)

    @property
    def uptime(self) -> Any:
        return self._raw.uptime

    @property
    def timestamp(self) -> Any:
        return self._raw.timestamp

    @property
    def users(self) -> Any:
        return self._raw.users

    @property
    def online_stats(self) -> Any:
        return self._raw.online_stats

    @property
    def nodes(self) -> Any:
        return self._raw.nodes


def adapt_panel_stats(raw: GetStatsResponseDtoResponse) -> StatsResponseShim:
    return StatsResponseShim(raw)


@dataclass(slots=True)
class HostRowShim:
    """Хост как в remnapy: свойство ``inbound_uuid`` из вложенного ``inbound``."""

    _raw: CreateHostResponseDtoResponse

    def __getattr__(self, name: str) -> Any:
        return getattr(self._raw, name)

    @property
    def inbound_uuid(self) -> Any:
        ib = self._raw.inbound
        if ib is None:
            return None
        return ib.config_profile_inbound_uuid


def adapt_hosts_response(hosts: List[CreateHostResponseDtoResponse]) -> List[HostRowShim]:
    return [HostRowShim(h) for h in hosts]


def adapt_nodes_response(nodes: List[CreateNodeResponseDtoResponse]) -> List[CreateNodeResponseDtoResponse]:
    """Панель уже отдаёт ноды в том же стиле имён (snake_case в Python)."""
    return nodes
