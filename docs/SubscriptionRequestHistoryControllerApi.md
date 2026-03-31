# supn_remnawave_panel.SubscriptionRequestHistoryControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_subscription_request_history_controller_get_subscription_request_history**](SubscriptionRequestHistoryControllerApi.md#user_subscription_request_history_controller_get_subscription_request_history) | **GET** /api/subscription-request-history | Get all subscription request history
[**user_subscription_request_history_controller_get_subscription_request_history_stats**](SubscriptionRequestHistoryControllerApi.md#user_subscription_request_history_controller_get_subscription_request_history_stats) | **GET** /api/subscription-request-history/stats | Get subscription request history stats


# **user_subscription_request_history_controller_get_subscription_request_history**
> GetSubscriptionRequestHistoryResponseDto user_subscription_request_history_controller_get_subscription_request_history(size=size, start=start)

Get all subscription request history

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_subscription_request_history_response_dto import GetSubscriptionRequestHistoryResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionRequestHistoryControllerApi(api_client)
    size = 3.4 # float | Page size for pagination (optional)
    start = 3.4 # float | Offset for pagination (optional)

    try:
        # Get all subscription request history
        api_response = await api_instance.user_subscription_request_history_controller_get_subscription_request_history(size=size, start=start)
        print("The response of SubscriptionRequestHistoryControllerApi->user_subscription_request_history_controller_get_subscription_request_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionRequestHistoryControllerApi->user_subscription_request_history_controller_get_subscription_request_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **float**| Page size for pagination | [optional] 
 **start** | **float**| Offset for pagination | [optional] 

### Return type

[**GetSubscriptionRequestHistoryResponseDto**](GetSubscriptionRequestHistoryResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription request history fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_subscription_request_history_controller_get_subscription_request_history_stats**
> GetSubscriptionRequestHistoryStatsResponseDto user_subscription_request_history_controller_get_subscription_request_history_stats()

Get subscription request history stats

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_subscription_request_history_stats_response_dto import GetSubscriptionRequestHistoryStatsResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionRequestHistoryControllerApi(api_client)

    try:
        # Get subscription request history stats
        api_response = await api_instance.user_subscription_request_history_controller_get_subscription_request_history_stats()
        print("The response of SubscriptionRequestHistoryControllerApi->user_subscription_request_history_controller_get_subscription_request_history_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionRequestHistoryControllerApi->user_subscription_request_history_controller_get_subscription_request_history_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSubscriptionRequestHistoryStatsResponseDto**](GetSubscriptionRequestHistoryStatsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User subscription request history stats fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

