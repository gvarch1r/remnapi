# supn_remnawave_panel.ProtectedSubscriptionsControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptions_controller_get_all_subscriptions**](ProtectedSubscriptionsControllerApi.md#subscriptions_controller_get_all_subscriptions) | **GET** /api/subscriptions | Get all subscriptions
[**subscriptions_controller_get_connection_keys_by_uuid**](ProtectedSubscriptionsControllerApi.md#subscriptions_controller_get_connection_keys_by_uuid) | **GET** /api/subscriptions/connection-keys/{uuid} | Get connection keys (base64 format) by uuid
[**subscriptions_controller_get_raw_subscription_by_short_uuid**](ProtectedSubscriptionsControllerApi.md#subscriptions_controller_get_raw_subscription_by_short_uuid) | **GET** /api/subscriptions/by-short-uuid/{shortUuid}/raw | Get Raw Subscription by Short UUID
[**subscriptions_controller_get_subpage_config_by_short_uuid**](ProtectedSubscriptionsControllerApi.md#subscriptions_controller_get_subpage_config_by_short_uuid) | **GET** /api/subscriptions/subpage-config/{shortUuid} | Get Subpage Config by Short UUID
[**subscriptions_controller_get_subscription_by_short_uuid_protected**](ProtectedSubscriptionsControllerApi.md#subscriptions_controller_get_subscription_by_short_uuid_protected) | **GET** /api/subscriptions/by-short-uuid/{shortUuid} | Get subscription by short uuid (protected route)
[**subscriptions_controller_get_subscription_by_username**](ProtectedSubscriptionsControllerApi.md#subscriptions_controller_get_subscription_by_username) | **GET** /api/subscriptions/by-username/{username} | Get subscription by username
[**subscriptions_controller_get_subscription_by_uuid**](ProtectedSubscriptionsControllerApi.md#subscriptions_controller_get_subscription_by_uuid) | **GET** /api/subscriptions/by-uuid/{uuid} | Get subscription by uuid


# **subscriptions_controller_get_all_subscriptions**
> GetAllSubscriptionsResponseDto subscriptions_controller_get_all_subscriptions(size=size, start=start)

Get all subscriptions

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_all_subscriptions_response_dto import GetAllSubscriptionsResponseDto
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
    api_instance = supn_remnawave_panel.ProtectedSubscriptionsControllerApi(api_client)
    size = 25 # float | Number of subscriptions to return, no more than 500 (optional)
    start = 0 # float | Start index (offset) of the users to return, default is 0 (optional)

    try:
        # Get all subscriptions
        api_response = await api_instance.subscriptions_controller_get_all_subscriptions(size=size, start=start)
        print("The response of ProtectedSubscriptionsControllerApi->subscriptions_controller_get_all_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectedSubscriptionsControllerApi->subscriptions_controller_get_all_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **float**| Number of subscriptions to return, no more than 500 | [optional] 
 **start** | **float**| Start index (offset) of the users to return, default is 0 | [optional] 

### Return type

[**GetAllSubscriptionsResponseDto**](GetAllSubscriptionsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_controller_get_connection_keys_by_uuid**
> GetConnectionKeysByUuidResponseDto subscriptions_controller_get_connection_keys_by_uuid(uuid)

Get connection keys (base64 format) by uuid

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_connection_keys_by_uuid_response_dto import GetConnectionKeysByUuidResponseDto
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
    api_instance = supn_remnawave_panel.ProtectedSubscriptionsControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the user

    try:
        # Get connection keys (base64 format) by uuid
        api_response = await api_instance.subscriptions_controller_get_connection_keys_by_uuid(uuid)
        print("The response of ProtectedSubscriptionsControllerApi->subscriptions_controller_get_connection_keys_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectedSubscriptionsControllerApi->subscriptions_controller_get_connection_keys_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the user | 

### Return type

[**GetConnectionKeysByUuidResponseDto**](GetConnectionKeysByUuidResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection keys fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_controller_get_raw_subscription_by_short_uuid**
> GetRawSubscriptionByShortUuidResponseDto subscriptions_controller_get_raw_subscription_by_short_uuid(short_uuid, with_disabled_hosts=with_disabled_hosts)

Get Raw Subscription by Short UUID

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_raw_subscription_by_short_uuid_response_dto import GetRawSubscriptionByShortUuidResponseDto
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
    api_instance = supn_remnawave_panel.ProtectedSubscriptionsControllerApi(api_client)
    short_uuid = 'short_uuid_example' # str | Short UUID of the user
    with_disabled_hosts = True # bool | Include disabled hosts in the subscription. Default is false. (optional)

    try:
        # Get Raw Subscription by Short UUID
        api_response = await api_instance.subscriptions_controller_get_raw_subscription_by_short_uuid(short_uuid, with_disabled_hosts=with_disabled_hosts)
        print("The response of ProtectedSubscriptionsControllerApi->subscriptions_controller_get_raw_subscription_by_short_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectedSubscriptionsControllerApi->subscriptions_controller_get_raw_subscription_by_short_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_uuid** | **str**| Short UUID of the user | 
 **with_disabled_hosts** | **bool**| Include disabled hosts in the subscription. Default is false. | [optional] 

### Return type

[**GetRawSubscriptionByShortUuidResponseDto**](GetRawSubscriptionByShortUuidResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw subscription fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_controller_get_subpage_config_by_short_uuid**
> GetSubpageConfigByShortUuidResponseDto subscriptions_controller_get_subpage_config_by_short_uuid(short_uuid, get_subpage_config_by_short_uuid_request_body_dto)

Get Subpage Config by Short UUID

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_subpage_config_by_short_uuid_request_body_dto import GetSubpageConfigByShortUuidRequestBodyDto
from supn_remnawave_panel.models.get_subpage_config_by_short_uuid_response_dto import GetSubpageConfigByShortUuidResponseDto
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
    api_instance = supn_remnawave_panel.ProtectedSubscriptionsControllerApi(api_client)
    short_uuid = 'short_uuid_example' # str | Short UUID of the user
    get_subpage_config_by_short_uuid_request_body_dto = supn_remnawave_panel.GetSubpageConfigByShortUuidRequestBodyDto() # GetSubpageConfigByShortUuidRequestBodyDto | 

    try:
        # Get Subpage Config by Short UUID
        api_response = await api_instance.subscriptions_controller_get_subpage_config_by_short_uuid(short_uuid, get_subpage_config_by_short_uuid_request_body_dto)
        print("The response of ProtectedSubscriptionsControllerApi->subscriptions_controller_get_subpage_config_by_short_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectedSubscriptionsControllerApi->subscriptions_controller_get_subpage_config_by_short_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_uuid** | **str**| Short UUID of the user | 
 **get_subpage_config_by_short_uuid_request_body_dto** | [**GetSubpageConfigByShortUuidRequestBodyDto**](GetSubpageConfigByShortUuidRequestBodyDto.md)|  | 

### Return type

[**GetSubpageConfigByShortUuidResponseDto**](GetSubpageConfigByShortUuidResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subpage config fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_controller_get_subscription_by_short_uuid_protected**
> GetSubscriptionByShortUuidProtectedResponseDto subscriptions_controller_get_subscription_by_short_uuid_protected(short_uuid)

Get subscription by short uuid (protected route)

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_subscription_by_short_uuid_protected_response_dto import GetSubscriptionByShortUuidProtectedResponseDto
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
    api_instance = supn_remnawave_panel.ProtectedSubscriptionsControllerApi(api_client)
    short_uuid = 'short_uuid_example' # str | Short uuid of the user

    try:
        # Get subscription by short uuid (protected route)
        api_response = await api_instance.subscriptions_controller_get_subscription_by_short_uuid_protected(short_uuid)
        print("The response of ProtectedSubscriptionsControllerApi->subscriptions_controller_get_subscription_by_short_uuid_protected:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectedSubscriptionsControllerApi->subscriptions_controller_get_subscription_by_short_uuid_protected: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_uuid** | **str**| Short uuid of the user | 

### Return type

[**GetSubscriptionByShortUuidProtectedResponseDto**](GetSubscriptionByShortUuidProtectedResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription fetched successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_controller_get_subscription_by_username**
> GetSubscriptionByUsernameResponseDto subscriptions_controller_get_subscription_by_username(username)

Get subscription by username

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_subscription_by_username_response_dto import GetSubscriptionByUsernameResponseDto
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
    api_instance = supn_remnawave_panel.ProtectedSubscriptionsControllerApi(api_client)
    username = 'username_example' # str | Username of the user

    try:
        # Get subscription by username
        api_response = await api_instance.subscriptions_controller_get_subscription_by_username(username)
        print("The response of ProtectedSubscriptionsControllerApi->subscriptions_controller_get_subscription_by_username:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectedSubscriptionsControllerApi->subscriptions_controller_get_subscription_by_username: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username of the user | 

### Return type

[**GetSubscriptionByUsernameResponseDto**](GetSubscriptionByUsernameResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription fetched successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_controller_get_subscription_by_uuid**
> GetSubscriptionByUuidResponseDto subscriptions_controller_get_subscription_by_uuid(uuid)

Get subscription by uuid

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_subscription_by_uuid_response_dto import GetSubscriptionByUuidResponseDto
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
    api_instance = supn_remnawave_panel.ProtectedSubscriptionsControllerApi(api_client)
    uuid = 'uuid_example' # str | Uuid of the user

    try:
        # Get subscription by uuid
        api_response = await api_instance.subscriptions_controller_get_subscription_by_uuid(uuid)
        print("The response of ProtectedSubscriptionsControllerApi->subscriptions_controller_get_subscription_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProtectedSubscriptionsControllerApi->subscriptions_controller_get_subscription_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Uuid of the user | 

### Return type

[**GetSubscriptionByUuidResponseDto**](GetSubscriptionByUuidResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription fetched successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

