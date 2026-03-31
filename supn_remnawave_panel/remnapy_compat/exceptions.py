# Hand-maintained: remnapy-compatible error types (snoups/remnapy style).
from __future__ import annotations

import json
from datetime import datetime
from typing import Any, List, Optional

from pydantic import AliasChoices, BaseModel, Field

from supn_remnawave_panel.exceptions import (
    ApiException,
    BadRequestException,
    ConflictException,
    ForbiddenException,
    NotFoundException,
    ServiceException,
    UnauthorizedException,
    UnprocessableEntityException,
)


class ApiErrorResponse(BaseModel):
    """Стандартное тело ошибки панели (как в remnapy)."""

    timestamp: Optional[datetime] = Field(None, description="Время возникновения ошибки")
    path: Optional[str] = Field(None, description="Путь запроса")
    message: str = Field("", description="Сообщение об ошибке")
    code: Optional[str] = Field(
        None,
        validation_alias=AliasChoices("errorCode", "code", "error_code"),
    )
    status_code: Optional[int] = Field(None, alias="statusCode")
    errors: Optional[List[Any]] = Field(None, description="Детали валидации")


def _error_from_openapi(exc: ApiException) -> ApiErrorResponse:
    body = exc.body
    if body:
        try:
            data = json.loads(body)
            if isinstance(data, dict):
                return ApiErrorResponse.model_validate(data)
        except Exception:
            pass
    return ApiErrorResponse(
        message=(exc.reason or str(exc) or "API error").strip(),
        status_code=exc.status,
    )


class ApiError(Exception):
    def __init__(self, status_code: int, error: ApiErrorResponse) -> None:
        self.status_code = status_code
        self.error = error
        super().__init__(f"API Error {error.code}: {error.message} (HTTP {status_code})")

    @property
    def code(self) -> Optional[str]:
        return self.error.code

    @property
    def message(self) -> str:
        return self.error.message


class BadRequestError(ApiError):
    pass


class UnauthorizedError(ApiError):
    pass


class ForbiddenError(ApiError):
    pass


class NotFoundError(ApiError):
    pass


class ConflictError(ApiError):
    pass


class ValidationError(ApiError):
    pass


class ServerError(ApiError):
    pass


class NetworkError(ApiError):
    pass


class AuthenticationError(ApiError):
    pass


class BusinessLogicError(ApiError):
    pass


class RateLimitError(BadRequestError):
    pass


class MaintenanceError(ServerError):
    pass


class QuotaExceededError(BusinessLogicError):
    pass


class FeatureNotAvailableError(BusinessLogicError):
    pass


def map_openapi_exception(exc: BaseException) -> BaseException:
    """Перевод исключений OpenAPI Generator в типы как в remnapy."""
    if isinstance(exc, NotFoundException):
        sc = int(exc.status or 404)
        return NotFoundError(sc, _error_from_openapi(exc))
    if isinstance(exc, UnauthorizedException):
        sc = int(exc.status or 401)
        return AuthenticationError(sc, _error_from_openapi(exc))
    if isinstance(exc, ForbiddenException):
        sc = int(exc.status or 403)
        return ForbiddenError(sc, _error_from_openapi(exc))
    if isinstance(exc, BadRequestException):
        sc = int(exc.status or 400)
        return BadRequestError(sc, _error_from_openapi(exc))
    if isinstance(exc, ConflictException):
        sc = int(exc.status or 409)
        return ConflictError(sc, _error_from_openapi(exc))
    if isinstance(exc, UnprocessableEntityException):
        sc = int(exc.status or 422)
        return ValidationError(sc, _error_from_openapi(exc))
    if isinstance(exc, ServiceException):
        sc = int(exc.status or 500)
        return ServerError(sc, _error_from_openapi(exc))
    return exc
