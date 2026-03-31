# supn_remnawave_panel.PublicSubscriptionControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscription_controller_get_subscription**](PublicSubscriptionControllerApi.md#subscription_controller_get_subscription) | **GET** /api/sub/{shortUuid} | 
[**subscription_controller_get_subscription_by_client_type**](PublicSubscriptionControllerApi.md#subscription_controller_get_subscription_by_client_type) | **GET** /api/sub/{shortUuid}/{clientType} | 
[**subscription_controller_get_subscription_info_by_short_uuid**](PublicSubscriptionControllerApi.md#subscription_controller_get_subscription_info_by_short_uuid) | **GET** /api/sub/{shortUuid}/info | Get Subscription Info by Short UUID


# **subscription_controller_get_subscription**
> subscription_controller_get_subscription(short_uuid)

### Example


```python
import supn_remnawave_panel
from supn_remnawave_panel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = supn_remnawave_panel.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with supn_remnawave_panel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = supn_remnawave_panel.PublicSubscriptionControllerApi(api_client)
    short_uuid = 'short_uuid_example' # str | Short UUID of the user

    try:
        await api_instance.subscription_controller_get_subscription(short_uuid)
    except Exception as e:
        print("Exception when calling PublicSubscriptionControllerApi->subscription_controller_get_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_uuid** | **str**| Short UUID of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_controller_get_subscription_by_client_type**
> subscription_controller_get_subscription_by_client_type(client_type, short_uuid)

### Example


```python
import supn_remnawave_panel
from supn_remnawave_panel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = supn_remnawave_panel.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with supn_remnawave_panel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = supn_remnawave_panel.PublicSubscriptionControllerApi(api_client)
    client_type = 'client_type_example' # str | Client type
    short_uuid = 'short_uuid_example' # str | Short UUID of the user

    try:
        await api_instance.subscription_controller_get_subscription_by_client_type(client_type, short_uuid)
    except Exception as e:
        print("Exception when calling PublicSubscriptionControllerApi->subscription_controller_get_subscription_by_client_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_type** | **str**| Client type | 
 **short_uuid** | **str**| Short UUID of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_controller_get_subscription_info_by_short_uuid**
> GetSubscriptionInfoResponseDto subscription_controller_get_subscription_info_by_short_uuid(short_uuid)

Get Subscription Info by Short UUID

### Example


```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_subscription_info_response_dto import GetSubscriptionInfoResponseDto
from supn_remnawave_panel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = supn_remnawave_panel.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with supn_remnawave_panel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = supn_remnawave_panel.PublicSubscriptionControllerApi(api_client)
    short_uuid = 'short_uuid_example' # str | Short UUID of the user

    try:
        # Get Subscription Info by Short UUID
        api_response = await api_instance.subscription_controller_get_subscription_info_by_short_uuid(short_uuid)
        print("The response of PublicSubscriptionControllerApi->subscription_controller_get_subscription_info_by_short_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicSubscriptionControllerApi->subscription_controller_get_subscription_info_by_short_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_uuid** | **str**| Short UUID of the user | 

### Return type

[**GetSubscriptionInfoResponseDto**](GetSubscriptionInfoResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription info fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

