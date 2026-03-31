# Hand-maintained: DTO вебхуков как remnapy.models.webhook для панели 2.7+.
from __future__ import annotations

from datetime import datetime
from typing import Any, List, Optional
from uuid import UUID

from pydantic import AliasChoices, BaseModel, ConfigDict, Field, field_validator

from supn_remnawave_panel.models.get_all_hwid_devices_response_dto_response_devices_inner import (
    GetAllHwidDevicesResponseDtoResponseDevicesInner,
)

from supn_remnawave_panel.remnapy_compat.models import UserResponseDto


class WebhookUserDto(UserResponseDto):
    """Пользователь в webhook; неизвестные поля панели игнорируются."""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        extra="ignore",
        protected_namespaces=(),
    )


class WebhookNodeDto(BaseModel):
    """Нода в событиях ``node.*`` (поля бота + запас по OpenAPI)."""

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    uuid: UUID
    name: str
    address: str
    port: Optional[int] = None
    is_connected: bool = Field(validation_alias=AliasChoices("is_connected", "isConnected"))
    is_connecting: bool = Field(default=False, validation_alias=AliasChoices("is_connecting", "isConnecting"))
    is_disabled: bool = Field(default=False, validation_alias=AliasChoices("is_disabled", "isDisabled"))
    last_status_change: Optional[datetime] = Field(
        default=None, validation_alias=AliasChoices("last_status_change", "lastStatusChange")
    )
    last_status_message: Optional[str] = Field(
        default=None, validation_alias=AliasChoices("last_status_message", "lastStatusMessage")
    )
    country_code: str = Field(validation_alias=AliasChoices("country_code", "countryCode"))
    traffic_limit_bytes: Optional[float] = Field(
        default=0.0, validation_alias=AliasChoices("traffic_limit_bytes", "trafficLimitBytes")
    )
    traffic_used_bytes: Optional[float] = Field(
        default=0.0, validation_alias=AliasChoices("traffic_used_bytes", "trafficUsedBytes")
    )
    xray_uptime: Optional[Any] = Field(default=None, validation_alias=AliasChoices("xray_uptime", "xrayUptime"))
    users_online: Optional[int] = Field(default=None, validation_alias=AliasChoices("users_online", "usersOnline"))
    tags: List[str] = Field(default_factory=list)
    created_at: Optional[datetime] = Field(default=None, validation_alias=AliasChoices("created_at", "createdAt"))
    updated_at: Optional[datetime] = Field(default=None, validation_alias=AliasChoices("updated_at", "updatedAt"))

    @field_validator("xray_uptime", mode="before")
    @classmethod
    def _coerce_uptime(cls, v: Any) -> Any:
        if v is None:
            return v
        if isinstance(v, (int, float)):
            return v
        if isinstance(v, str):
            try:
                return float(v)
            except ValueError:
                return v
        return v


HwidUserDeviceDto = GetAllHwidDevicesResponseDtoResponseDevicesInner


class UserHwidDeviceEventDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    user: WebhookUserDto
    hwid_user_device: HwidUserDeviceDto = Field(
        validation_alias=AliasChoices("hwid_user_device", "hwidUserDevice")
    )

    @classmethod
    def from_payload_data(cls, data: Any) -> UserHwidDeviceEventDto:
        if not isinstance(data, dict):
            raise TypeError(f"webhook data must be dict, got {type(data)}")
        return cls.model_validate(data)


UserDto = WebhookUserDto
NodeDto = WebhookNodeDto

__all__ = [
    "UserDto",
    "WebhookUserDto",
    "NodeDto",
    "WebhookNodeDto",
    "HwidUserDeviceDto",
    "UserHwidDeviceEventDto",
]
