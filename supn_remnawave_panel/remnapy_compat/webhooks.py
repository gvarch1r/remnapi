# Hand-maintained: API как remnapy.controllers.WebhookUtility (данные — OpenAPI 2.7+).
from __future__ import annotations

import json
from typing import Any, Optional, Union

from supn_remnawave_panel.webhook_support import (
    WebhookHeaders,
    WebhookPayload,
    is_crm_event as _is_crm_event,
    is_errors_event as _is_errors_event,
    is_infra_billing_event as _is_infra_billing_event,
    is_node_event as _is_node_event,
    is_service_event as _is_service_event,
    is_user_event as _is_user_event,
    is_user_hwid_devices_event as _is_user_hwid_devices_event,
    parse_webhook as _parse_webhook,
    user_hwid_pair_from_data,
    verify_webhook_hmac,
    verify_webhook_request,
)

__all__ = [
    "WebhookHeadersDto",
    "WebhookPayloadDto",
    "WebhookUtility",
    "user_hwid_pair_from_data",
]


class WebhookHeadersDto(WebhookHeaders):
    """Совместимость с remnapy ``WebhookHeadersDto``."""

    @classmethod
    def from_headers(cls, headers: dict[str, str]) -> WebhookHeadersDto:
        return super().from_headers(headers)  # type: ignore[return-value]


class WebhookPayloadDto(WebhookPayload):
    """Как remnapy ``WebhookPayloadDto``; ``data`` без жёсткой схемы."""

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> WebhookPayloadDto:
        return cls.model_validate(data)


class WebhookUtility:
    @staticmethod
    def validate_webhook(
        body: Union[str, dict[str, Any]],
        signature: str,
        webhook_secret: str,
    ) -> bool:
        return verify_webhook_hmac(body, signature, webhook_secret)

    @staticmethod
    def validate_webhook_with_headers(
        body: Union[str, dict[str, Any]],
        headers: Union[dict[str, str], WebhookHeadersDto],
        webhook_secret: str,
    ) -> bool:
        h = headers if isinstance(headers, WebhookHeaders) else WebhookHeadersDto.from_headers(headers)
        if isinstance(body, dict):
            dumped = json.dumps(body, separators=(",", ":"))
            return verify_webhook_hmac(dumped, h.signature, webhook_secret)
        return verify_webhook_hmac(body, h.signature, webhook_secret)

    @staticmethod
    def parse_webhook(
        body: Union[str, dict[str, Any]],
        headers: Union[dict[str, str], WebhookHeadersDto],
        webhook_secret: str,
        validate: bool = True,
    ) -> Optional[WebhookPayloadDto]:
        if isinstance(headers, dict):
            raw_headers = headers
        else:
            raw_headers = {
                "X-Remnawave-Signature": headers.signature,
                "X-Remnawave-Timestamp": headers.timestamp,
            }
        if isinstance(body, dict):
            body_str = json.dumps(body, separators=(",", ":"))
        else:
            body_str = body
        if validate and not verify_webhook_request(body_str, raw_headers, webhook_secret):
            return None
        if isinstance(body, dict):
            return WebhookPayloadDto.model_validate(body)
        return WebhookPayloadDto.model_validate(json.loads(body_str))

    @staticmethod
    def is_user_event(event: str) -> bool:
        return _is_user_event(event)

    @staticmethod
    def is_user_hwid_devices_event(event: str) -> bool:
        return _is_user_hwid_devices_event(event)

    @staticmethod
    def is_node_event(event: str) -> bool:
        return _is_node_event(event)

    @staticmethod
    def is_infra_billing_event(event: str) -> bool:
        return _is_infra_billing_event(event)

    @staticmethod
    def is_crm_event(event: str) -> bool:
        return _is_crm_event(event)

    @staticmethod
    def is_service_event(event: str) -> bool:
        return _is_service_event(event)

    @staticmethod
    def is_errors_event(event: str) -> bool:
        return _is_errors_event(event)

    @staticmethod
    def get_typed_data(payload: WebhookPayloadDto) -> Any:
        return payload.data

    @staticmethod
    def extract_user_hwid_event_data(
        payload: WebhookPayloadDto,
    ) -> Optional[tuple[dict[str, Any], dict[str, Any]]]:
        if not WebhookUtility.is_user_hwid_devices_event(payload.event):
            return None
        pair = user_hwid_pair_from_data(payload.data)
        if pair is None:
            return None
        return pair
