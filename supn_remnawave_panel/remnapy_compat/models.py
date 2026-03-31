# Hand-maintained: алиасы имён remnapy → сгенерированные DTO панели 2.7+.
from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import RootModel

from supn_remnawave_panel.models.create_user_request_dto import CreateUserRequestDto
from supn_remnawave_panel.models.create_user_response_dto_response import (
    CreateUserResponseDtoResponse,
)
from supn_remnawave_panel.models.delete_all_user_hwid_devices_request_dto import (
    DeleteAllUserHwidDevicesRequestDto,
)
from supn_remnawave_panel.models.delete_user_hwid_device_request_dto import (
    DeleteUserHwidDeviceRequestDto,
)
from supn_remnawave_panel.models.get_all_hwid_devices_response_dto_response_devices_inner import (
    GetAllHwidDevicesResponseDtoResponseDevicesInner,
)
from supn_remnawave_panel.models.get_external_squad_by_uuid_response_dto import (
    GetExternalSquadByUuidResponseDto,
)
from supn_remnawave_panel.models.get_stats_response_dto_response import (
    GetStatsResponseDtoResponse,
)
from supn_remnawave_panel.models.revoke_user_subscription_body_dto import (
    RevokeUserSubscriptionBodyDto,
)
from supn_remnawave_panel.models.update_user_request_dto import UpdateUserRequestDto

__all__ = [
    "CreateUserRequestDto",
    "DeleteUserAllHwidDeviceRequestDto",
    "DeleteUserHwidDeviceRequestDto",
    "GetExternalSquadByUuidResponseDto",
    "GetStatsResponseDto",
    "HWIDDeleteRequest",
    "HwidDeviceDto",
    "RevokeUserRequestDto",
    "TelegramUserResponseDto",
    "UpdateUserRequestDto",
    "UserResponseDto",
    "coerce_user_response",
    "unwrap_inner",
]


class UserResponseDto(CreateUserResponseDtoResponse):
    """Как remnapy.UserResponseDto: плоские свойства из ``user_traffic``."""

    @property
    def used_traffic_bytes(self) -> int:
        return int(self.user_traffic.used_traffic_bytes)

    @property
    def lifetime_used_traffic_bytes(self) -> int:
        return int(self.user_traffic.lifetime_used_traffic_bytes)

    @property
    def online_at(self) -> Optional[datetime]:
        return self.user_traffic.online_at

    @property
    def first_connected_at(self) -> Optional[datetime]:
        return self.user_traffic.first_connected_at

    @property
    def last_connected_node_uuid(self) -> Optional[UUID]:
        return self.user_traffic.last_connected_node_uuid


GetStatsResponseDto = GetStatsResponseDtoResponse
HwidDeviceDto = GetAllHwidDevicesResponseDtoResponseDevicesInner

DeleteUserAllHwidDeviceRequestDto = DeleteAllUserHwidDevicesRequestDto
HWIDDeleteRequest = DeleteUserHwidDeviceRequestDto
RevokeUserRequestDto = RevokeUserSubscriptionBodyDto


class TelegramUserResponseDto(RootModel[list[UserResponseDto]]):
    """Как remnapy.TelegramUserResponseDto: список пользователей в .root."""

    root: list[UserResponseDto]


def unwrap_inner(m: object | None) -> object | None:
    """Снять один уровень ``response``, если поле есть (формат панели 2.7+)."""
    if m is None:
        return None
    inner = getattr(m, "response", None)
    if inner is not None:
        return inner
    return m


def coerce_user_response(m: object | None) -> UserResponseDto | None:
    """Сгенерированный ответ пользователя → :class:`UserResponseDto` с совместимыми полями."""
    if m is None:
        return None
    if isinstance(m, UserResponseDto):
        return m
    if isinstance(m, CreateUserResponseDtoResponse):
        return UserResponseDto.model_validate(m.model_dump())
    if isinstance(m, dict):
        return UserResponseDto.model_validate(m)
    raise TypeError(f"Cannot coerce user response from {type(m)!r}")
