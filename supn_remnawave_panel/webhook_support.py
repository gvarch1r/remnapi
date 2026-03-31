# Hand-maintained; see .openapi-generator-ignore.
"""
Проверка и разбор вебхуков панели Remnawave (HMAC-SHA256 по телу).

Заголовки и логика подписи совпадают с `WebhookUtility` из
`remnapy/controllers/webhooks.py` ([snoups/remnapy](https://github.com/snoups/remnapy)):
`X-Remnawave-Signature`, `X-Remnawave-Timestamp`; секрет — тот же, что
`WEBHOOK_SECRET_HEADER` / env панели.

Поле `data` в :class:`WebhookPayload` намеренно **без** жёсткой схемы по типу события:
панель 2.7+ меняет поля пользователя/ноды — сырой dict проще стыковать с вашим кодом
или с моделями из сгенерированного API.
"""

from __future__ import annotations

import hashlib
import hmac
import json
from datetime import datetime, timezone
from typing import Any, Mapping, Optional

from dateutil.parser import isoparse
from pydantic import BaseModel, ConfigDict, Field, field_validator

__all__ = [
    "WebhookHeaders",
    "WebhookPayload",
    "verify_webhook_hmac",
    "verify_webhook_request",
    "parse_webhook",
    "is_user_event",
    "is_user_hwid_devices_event",
    "is_node_event",
    "is_infra_billing_event",
    "is_crm_event",
    "is_service_event",
    "is_errors_event",
    "user_hwid_pair_from_data",
]


class WebhookHeaders:
    """Пара обязательных заголовков вебхука."""

    __slots__ = ("signature", "timestamp")

    def __init__(self, signature: str, timestamp: str) -> None:
        self.signature = signature
        self.timestamp = timestamp

    @classmethod
    def from_headers(cls, headers: Mapping[str, str]) -> WebhookHeaders:
        signature: str | None = None
        timestamp: str | None = None
        for key, value in headers.items():
            lk = key.lower()
            if lk == "x-remnawave-signature":
                signature = value
            elif lk == "x-remnawave-timestamp":
                timestamp = value
        if not signature or not timestamp:
            raise ValueError("Missing X-Remnawave-Signature or X-Remnawave-Timestamp")
        return cls(signature=signature, timestamp=timestamp)


def verify_webhook_hmac(body: str | dict[str, Any], signature: str, secret: str) -> bool:
    """Проверка подписи телом запроса (как в remnapy)."""
    if isinstance(body, dict):
        original = json.dumps(body, separators=(",", ":"))
    else:
        original = body
    computed = hmac.new(
        secret.encode("utf-8"),
        original.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(computed, signature)


def verify_webhook_request(body: str, headers: Mapping[str, str], secret: str) -> bool:
    wh = WebhookHeaders.from_headers(dict(headers))
    return verify_webhook_hmac(body, wh.signature, secret)


class WebhookPayload(BaseModel):
    """Тело вебхука после JSON parse/Pydantic."""

    model_config = ConfigDict(extra="ignore")

    event: str
    timestamp: datetime
    data: Any = Field(default=None)

    @field_validator("timestamp", mode="before")
    @classmethod
    def _coerce_timestamp(cls, v: Any) -> datetime:
        if isinstance(v, datetime):
            return v if v.tzinfo else v.replace(tzinfo=timezone.utc)
        if isinstance(v, (int, float)):
            return datetime.fromtimestamp(float(v), tz=timezone.utc)
        if isinstance(v, str):
            dt = isoparse(v)
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        raise TypeError(f"Unsupported timestamp type: {type(v)!r}")


def parse_webhook(
    body: str,
    headers: Mapping[str, str],
    webhook_secret: str,
    *,
    validate: bool = True,
) -> Optional[WebhookPayload]:
    """
    Проверка подписи (по желанию) и разбор JSON.

    :param body: сырая строка тела (как для HMAC — именно она должна совпасть с панелью).
    :return: None при validate=True и неверной подписи.
    """
    if validate and not verify_webhook_request(body, headers, webhook_secret):
        return None
    raw: dict[str, Any] = json.loads(body)
    return WebhookPayload.model_validate(raw)


def is_user_event(event: str) -> bool:
    return event.startswith("user.")


def is_user_hwid_devices_event(event: str) -> bool:
    return event.startswith("user_hwid_devices.")


def is_node_event(event: str) -> bool:
    return event.startswith("node.")


def is_infra_billing_event(event: str) -> bool:
    return event.startswith("crm.infra_billing")


def is_crm_event(event: str) -> bool:
    return event.startswith("crm.")


def is_service_event(event: str) -> bool:
    return event.startswith("service.")


def is_errors_event(event: str) -> bool:
    return event.startswith("errors.")


def user_hwid_pair_from_data(data: Any) -> Optional[tuple[dict[str, Any], dict[str, Any]]]:
    """Для событий ``user_hwid_devices.*``: ``(user dict, device dict)``."""
    if not isinstance(data, dict):
        return None
    u, h = data.get("user"), data.get("hwidUserDevice")
    if isinstance(u, dict) and isinstance(h, dict):
        return u, h
    return None
