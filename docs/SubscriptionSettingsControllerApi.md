# supn_remnawave_panel.SubscriptionSettingsControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscription_settings_controller_get_settings**](SubscriptionSettingsControllerApi.md#subscription_settings_controller_get_settings) | **GET** /api/subscription-settings | Get subscription settings
[**subscription_settings_controller_update_settings**](SubscriptionSettingsControllerApi.md#subscription_settings_controller_update_settings) | **PATCH** /api/subscription-settings | Update subscription settings


# **subscription_settings_controller_get_settings**
> GetSubscriptionSettingsResponseDto subscription_settings_controller_get_settings()

Get subscription settings

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_subscription_settings_response_dto import GetSubscriptionSettingsResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionSettingsControllerApi(api_client)

    try:
        # Get subscription settings
        api_response = await api_instance.subscription_settings_controller_get_settings()
        print("The response of SubscriptionSettingsControllerApi->subscription_settings_controller_get_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionSettingsControllerApi->subscription_settings_controller_get_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSubscriptionSettingsResponseDto**](GetSubscriptionSettingsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription settings retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_settings_controller_update_settings**
> UpdateSubscriptionSettingsResponseDto subscription_settings_controller_update_settings(update_subscription_settings_request_dto)

Update subscription settings

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.update_subscription_settings_request_dto import UpdateSubscriptionSettingsRequestDto
from supn_remnawave_panel.models.update_subscription_settings_response_dto import UpdateSubscriptionSettingsResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionSettingsControllerApi(api_client)
    update_subscription_settings_request_dto = supn_remnawave_panel.UpdateSubscriptionSettingsRequestDto() # UpdateSubscriptionSettingsRequestDto | 

    try:
        # Update subscription settings
        api_response = await api_instance.subscription_settings_controller_update_settings(update_subscription_settings_request_dto)
        print("The response of SubscriptionSettingsControllerApi->subscription_settings_controller_update_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionSettingsControllerApi->subscription_settings_controller_update_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_subscription_settings_request_dto** | [**UpdateSubscriptionSettingsRequestDto**](UpdateSubscriptionSettingsRequestDto.md)|  | 

### Return type

[**UpdateSubscriptionSettingsResponseDto**](UpdateSubscriptionSettingsResponseDto.md)

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

