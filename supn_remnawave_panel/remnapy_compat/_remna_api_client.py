# Hand-maintained: клиент с маппингом ошибок → remnapy_compat.exceptions.
from __future__ import annotations

import httpx

from supn_remnawave_panel.api_client import ApiClient
from supn_remnawave_panel.api_response import ApiResponse, T as ApiResponseT
from supn_remnawave_panel.exceptions import ApiException

from supn_remnawave_panel.remnapy_compat.exceptions import (
    ApiErrorResponse,
    NetworkError,
    map_openapi_exception,
)


class RemnaApiClient(ApiClient):
    async def call_api(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        try:
            return await super().call_api(*args, **kwargs)
        except ApiException:
            raise
        except httpx.RequestError as e:
            raise NetworkError(
                0,
                ApiErrorResponse(message=str(e)),
            ) from e

    def response_deserialize(
        self,
        response_data,
        response_types_map=None,
    ) -> ApiResponse[ApiResponseT]:
        try:
            return super().response_deserialize(
                response_data,
                response_types_map,
            )
        except ApiException as e:
            mapped = map_openapi_exception(e)
            raise mapped from e
