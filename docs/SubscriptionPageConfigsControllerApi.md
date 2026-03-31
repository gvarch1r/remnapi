# supn_remnawave_panel.SubscriptionPageConfigsControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscription_page_config_controller_clone_subscription_page_config**](SubscriptionPageConfigsControllerApi.md#subscription_page_config_controller_clone_subscription_page_config) | **POST** /api/subscription-page-configs/actions/clone | Clone subscription page config
[**subscription_page_config_controller_create_config**](SubscriptionPageConfigsControllerApi.md#subscription_page_config_controller_create_config) | **POST** /api/subscription-page-configs | Create subscription page config
[**subscription_page_config_controller_delete_config**](SubscriptionPageConfigsControllerApi.md#subscription_page_config_controller_delete_config) | **DELETE** /api/subscription-page-configs/{uuid} | Delete subscription page config
[**subscription_page_config_controller_get_all_configs**](SubscriptionPageConfigsControllerApi.md#subscription_page_config_controller_get_all_configs) | **GET** /api/subscription-page-configs | Get all subscription page configs
[**subscription_page_config_controller_get_config_by_uuid**](SubscriptionPageConfigsControllerApi.md#subscription_page_config_controller_get_config_by_uuid) | **GET** /api/subscription-page-configs/{uuid} | Get subscription page config by uuid
[**subscription_page_config_controller_reorder_subscription_page_configs**](SubscriptionPageConfigsControllerApi.md#subscription_page_config_controller_reorder_subscription_page_configs) | **POST** /api/subscription-page-configs/actions/reorder | Reorder subscription page configs
[**subscription_page_config_controller_update_config**](SubscriptionPageConfigsControllerApi.md#subscription_page_config_controller_update_config) | **PATCH** /api/subscription-page-configs | Update subscription page config


# **subscription_page_config_controller_clone_subscription_page_config**
> CloneSubscriptionPageConfigResponseDto subscription_page_config_controller_clone_subscription_page_config(clone_subscription_page_config_request_dto)

Clone subscription page config

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.clone_subscription_page_config_request_dto import CloneSubscriptionPageConfigRequestDto
from supn_remnawave_panel.models.clone_subscription_page_config_response_dto import CloneSubscriptionPageConfigResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionPageConfigsControllerApi(api_client)
    clone_subscription_page_config_request_dto = supn_remnawave_panel.CloneSubscriptionPageConfigRequestDto() # CloneSubscriptionPageConfigRequestDto | 

    try:
        # Clone subscription page config
        api_response = await api_instance.subscription_page_config_controller_clone_subscription_page_config(clone_subscription_page_config_request_dto)
        print("The response of SubscriptionPageConfigsControllerApi->subscription_page_config_controller_clone_subscription_page_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPageConfigsControllerApi->subscription_page_config_controller_clone_subscription_page_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clone_subscription_page_config_request_dto** | [**CloneSubscriptionPageConfigRequestDto**](CloneSubscriptionPageConfigRequestDto.md)|  | 

### Return type

[**CloneSubscriptionPageConfigResponseDto**](CloneSubscriptionPageConfigResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription page config cloned successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_page_config_controller_create_config**
> CreateSubscriptionPageConfigResponseDto subscription_page_config_controller_create_config(create_subscription_page_config_request_dto)

Create subscription page config

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.create_subscription_page_config_request_dto import CreateSubscriptionPageConfigRequestDto
from supn_remnawave_panel.models.create_subscription_page_config_response_dto import CreateSubscriptionPageConfigResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionPageConfigsControllerApi(api_client)
    create_subscription_page_config_request_dto = supn_remnawave_panel.CreateSubscriptionPageConfigRequestDto() # CreateSubscriptionPageConfigRequestDto | 

    try:
        # Create subscription page config
        api_response = await api_instance.subscription_page_config_controller_create_config(create_subscription_page_config_request_dto)
        print("The response of SubscriptionPageConfigsControllerApi->subscription_page_config_controller_create_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPageConfigsControllerApi->subscription_page_config_controller_create_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_subscription_page_config_request_dto** | [**CreateSubscriptionPageConfigRequestDto**](CreateSubscriptionPageConfigRequestDto.md)|  | 

### Return type

[**CreateSubscriptionPageConfigResponseDto**](CreateSubscriptionPageConfigResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription page config created successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_page_config_controller_delete_config**
> DeleteSubscriptionPageConfigResponseDto subscription_page_config_controller_delete_config(uuid)

Delete subscription page config

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_subscription_page_config_response_dto import DeleteSubscriptionPageConfigResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionPageConfigsControllerApi(api_client)
    uuid = 'uuid_example' # str | Subscription page config UUID

    try:
        # Delete subscription page config
        api_response = await api_instance.subscription_page_config_controller_delete_config(uuid)
        print("The response of SubscriptionPageConfigsControllerApi->subscription_page_config_controller_delete_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPageConfigsControllerApi->subscription_page_config_controller_delete_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Subscription page config UUID | 

### Return type

[**DeleteSubscriptionPageConfigResponseDto**](DeleteSubscriptionPageConfigResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription page config deleted successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_page_config_controller_get_all_configs**
> GetSubscriptionPageConfigsResponseDto subscription_page_config_controller_get_all_configs()

Get all subscription page configs

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_subscription_page_configs_response_dto import GetSubscriptionPageConfigsResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionPageConfigsControllerApi(api_client)

    try:
        # Get all subscription page configs
        api_response = await api_instance.subscription_page_config_controller_get_all_configs()
        print("The response of SubscriptionPageConfigsControllerApi->subscription_page_config_controller_get_all_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPageConfigsControllerApi->subscription_page_config_controller_get_all_configs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSubscriptionPageConfigsResponseDto**](GetSubscriptionPageConfigsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription page configs retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_page_config_controller_get_config_by_uuid**
> GetSubscriptionPageConfigResponseDto subscription_page_config_controller_get_config_by_uuid(uuid)

Get subscription page config by uuid

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_subscription_page_config_response_dto import GetSubscriptionPageConfigResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionPageConfigsControllerApi(api_client)
    uuid = 'uuid_example' # str | Subscription page config UUID

    try:
        # Get subscription page config by uuid
        api_response = await api_instance.subscription_page_config_controller_get_config_by_uuid(uuid)
        print("The response of SubscriptionPageConfigsControllerApi->subscription_page_config_controller_get_config_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPageConfigsControllerApi->subscription_page_config_controller_get_config_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Subscription page config UUID | 

### Return type

[**GetSubscriptionPageConfigResponseDto**](GetSubscriptionPageConfigResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription page config retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_page_config_controller_reorder_subscription_page_configs**
> ReorderSubscriptionPageConfigsResponseDto subscription_page_config_controller_reorder_subscription_page_configs(reorder_subscription_page_configs_request_dto)

Reorder subscription page configs

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.reorder_subscription_page_configs_request_dto import ReorderSubscriptionPageConfigsRequestDto
from supn_remnawave_panel.models.reorder_subscription_page_configs_response_dto import ReorderSubscriptionPageConfigsResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionPageConfigsControllerApi(api_client)
    reorder_subscription_page_configs_request_dto = supn_remnawave_panel.ReorderSubscriptionPageConfigsRequestDto() # ReorderSubscriptionPageConfigsRequestDto | 

    try:
        # Reorder subscription page configs
        api_response = await api_instance.subscription_page_config_controller_reorder_subscription_page_configs(reorder_subscription_page_configs_request_dto)
        print("The response of SubscriptionPageConfigsControllerApi->subscription_page_config_controller_reorder_subscription_page_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPageConfigsControllerApi->subscription_page_config_controller_reorder_subscription_page_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reorder_subscription_page_configs_request_dto** | [**ReorderSubscriptionPageConfigsRequestDto**](ReorderSubscriptionPageConfigsRequestDto.md)|  | 

### Return type

[**ReorderSubscriptionPageConfigsResponseDto**](ReorderSubscriptionPageConfigsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription page configs reordered successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_page_config_controller_update_config**
> UpdateSubscriptionPageConfigResponseDto subscription_page_config_controller_update_config(update_subscription_page_config_request_dto)

Update subscription page config

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.update_subscription_page_config_request_dto import UpdateSubscriptionPageConfigRequestDto
from supn_remnawave_panel.models.update_subscription_page_config_response_dto import UpdateSubscriptionPageConfigResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionPageConfigsControllerApi(api_client)
    update_subscription_page_config_request_dto = supn_remnawave_panel.UpdateSubscriptionPageConfigRequestDto() # UpdateSubscriptionPageConfigRequestDto | 

    try:
        # Update subscription page config
        api_response = await api_instance.subscription_page_config_controller_update_config(update_subscription_page_config_request_dto)
        print("The response of SubscriptionPageConfigsControllerApi->subscription_page_config_controller_update_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionPageConfigsControllerApi->subscription_page_config_controller_update_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_subscription_page_config_request_dto** | [**UpdateSubscriptionPageConfigRequestDto**](UpdateSubscriptionPageConfigRequestDto.md)|  | 

### Return type

[**UpdateSubscriptionPageConfigResponseDto**](UpdateSubscriptionPageConfigResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription page config updated successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

