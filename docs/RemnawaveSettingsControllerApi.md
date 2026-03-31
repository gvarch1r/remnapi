# supn_remnawave_panel.RemnawaveSettingsControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remnawave_settings_controller_get_settings**](RemnawaveSettingsControllerApi.md#remnawave_settings_controller_get_settings) | **GET** /api/remnawave-settings | Get Remnawave settings
[**remnawave_settings_controller_update_settings**](RemnawaveSettingsControllerApi.md#remnawave_settings_controller_update_settings) | **PATCH** /api/remnawave-settings | Update Remnawave settings


# **remnawave_settings_controller_get_settings**
> GetRemnawaveSettingsResponseDto remnawave_settings_controller_get_settings()

Get Remnawave settings

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_remnawave_settings_response_dto import GetRemnawaveSettingsResponseDto
from supn_remnawave_panel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = supn_remnawave_panel.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Authorization
configuration = supn_remnawave_panel.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with supn_remnawave_panel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = supn_remnawave_panel.RemnawaveSettingsControllerApi(api_client)

    try:
        # Get Remnawave settings
        api_response = await api_instance.remnawave_settings_controller_get_settings()
        print("The response of RemnawaveSettingsControllerApi->remnawave_settings_controller_get_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemnawaveSettingsControllerApi->remnawave_settings_controller_get_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetRemnawaveSettingsResponseDto**](GetRemnawaveSettingsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Remnawave settings retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remnawave_settings_controller_update_settings**
> UpdateRemnawaveSettingsResponseDto remnawave_settings_controller_update_settings(update_remnawave_settings_request_dto)

Update Remnawave settings

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.update_remnawave_settings_request_dto import UpdateRemnawaveSettingsRequestDto
from supn_remnawave_panel.models.update_remnawave_settings_response_dto import UpdateRemnawaveSettingsResponseDto
from supn_remnawave_panel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = supn_remnawave_panel.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Authorization
configuration = supn_remnawave_panel.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with supn_remnawave_panel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = supn_remnawave_panel.RemnawaveSettingsControllerApi(api_client)
    update_remnawave_settings_request_dto = supn_remnawave_panel.UpdateRemnawaveSettingsRequestDto() # UpdateRemnawaveSettingsRequestDto | 

    try:
        # Update Remnawave settings
        api_response = await api_instance.remnawave_settings_controller_update_settings(update_remnawave_settings_request_dto)
        print("The response of RemnawaveSettingsControllerApi->remnawave_settings_controller_update_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemnawaveSettingsControllerApi->remnawave_settings_controller_update_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_remnawave_settings_request_dto** | [**UpdateRemnawaveSettingsRequestDto**](UpdateRemnawaveSettingsRequestDto.md)|  | 

### Return type

[**UpdateRemnawaveSettingsResponseDto**](UpdateRemnawaveSettingsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription settings updated successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

