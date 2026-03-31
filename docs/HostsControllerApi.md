# supn_remnawave_panel.HostsControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hosts_controller_create_host**](HostsControllerApi.md#hosts_controller_create_host) | **POST** /api/hosts | Create a new host
[**hosts_controller_delete_host**](HostsControllerApi.md#hosts_controller_delete_host) | **DELETE** /api/hosts/{uuid} | Delete a host by UUID
[**hosts_controller_get_all_host_tags**](HostsControllerApi.md#hosts_controller_get_all_host_tags) | **GET** /api/hosts/tags | Get all existing host tags
[**hosts_controller_get_all_hosts**](HostsControllerApi.md#hosts_controller_get_all_hosts) | **GET** /api/hosts | Get all hosts
[**hosts_controller_get_one_host**](HostsControllerApi.md#hosts_controller_get_one_host) | **GET** /api/hosts/{uuid} | Get a host by UUID
[**hosts_controller_reorder_hosts**](HostsControllerApi.md#hosts_controller_reorder_hosts) | **POST** /api/hosts/actions/reorder | Reorder hosts
[**hosts_controller_update_host**](HostsControllerApi.md#hosts_controller_update_host) | **PATCH** /api/hosts | Update a host


# **hosts_controller_create_host**
> CreateHostResponseDto hosts_controller_create_host(create_host_request_dto)

Create a new host

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.create_host_request_dto import CreateHostRequestDto
from supn_remnawave_panel.models.create_host_response_dto import CreateHostResponseDto
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
    api_instance = supn_remnawave_panel.HostsControllerApi(api_client)
    create_host_request_dto = supn_remnawave_panel.CreateHostRequestDto() # CreateHostRequestDto | 

    try:
        # Create a new host
        api_response = await api_instance.hosts_controller_create_host(create_host_request_dto)
        print("The response of HostsControllerApi->hosts_controller_create_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsControllerApi->hosts_controller_create_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_host_request_dto** | [**CreateHostRequestDto**](CreateHostRequestDto.md)|  | 

### Return type

[**CreateHostResponseDto**](CreateHostResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Host created successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_controller_delete_host**
> DeleteHostResponseDto hosts_controller_delete_host(uuid)

Delete a host by UUID

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_host_response_dto import DeleteHostResponseDto
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
    api_instance = supn_remnawave_panel.HostsControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the host

    try:
        # Delete a host by UUID
        api_response = await api_instance.hosts_controller_delete_host(uuid)
        print("The response of HostsControllerApi->hosts_controller_delete_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsControllerApi->hosts_controller_delete_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the host | 

### Return type

[**DeleteHostResponseDto**](DeleteHostResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Host deleted successfully |  -  |
**400** | Validation error |  -  |
**404** | Host not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_controller_get_all_host_tags**
> GetAllHostTagsResponseDto hosts_controller_get_all_host_tags()

Get all existing host tags

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_all_host_tags_response_dto import GetAllHostTagsResponseDto
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
    api_instance = supn_remnawave_panel.HostsControllerApi(api_client)

    try:
        # Get all existing host tags
        api_response = await api_instance.hosts_controller_get_all_host_tags()
        print("The response of HostsControllerApi->hosts_controller_get_all_host_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsControllerApi->hosts_controller_get_all_host_tags: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllHostTagsResponseDto**](GetAllHostTagsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Host tags fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_controller_get_all_hosts**
> GetAllHostsResponseDto hosts_controller_get_all_hosts()

Get all hosts

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_all_hosts_response_dto import GetAllHostsResponseDto
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
    api_instance = supn_remnawave_panel.HostsControllerApi(api_client)

    try:
        # Get all hosts
        api_response = await api_instance.hosts_controller_get_all_hosts()
        print("The response of HostsControllerApi->hosts_controller_get_all_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsControllerApi->hosts_controller_get_all_hosts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllHostsResponseDto**](GetAllHostsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hosts fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_controller_get_one_host**
> GetOneHostResponseDto hosts_controller_get_one_host(uuid)

Get a host by UUID

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_one_host_response_dto import GetOneHostResponseDto
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
    api_instance = supn_remnawave_panel.HostsControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the host

    try:
        # Get a host by UUID
        api_response = await api_instance.hosts_controller_get_one_host(uuid)
        print("The response of HostsControllerApi->hosts_controller_get_one_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsControllerApi->hosts_controller_get_one_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the host | 

### Return type

[**GetOneHostResponseDto**](GetOneHostResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Host fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_controller_reorder_hosts**
> ReorderHostResponseDto hosts_controller_reorder_hosts(reorder_host_request_dto)

Reorder hosts

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.reorder_host_request_dto import ReorderHostRequestDto
from supn_remnawave_panel.models.reorder_host_response_dto import ReorderHostResponseDto
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
    api_instance = supn_remnawave_panel.HostsControllerApi(api_client)
    reorder_host_request_dto = supn_remnawave_panel.ReorderHostRequestDto() # ReorderHostRequestDto | 

    try:
        # Reorder hosts
        api_response = await api_instance.hosts_controller_reorder_hosts(reorder_host_request_dto)
        print("The response of HostsControllerApi->hosts_controller_reorder_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsControllerApi->hosts_controller_reorder_hosts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reorder_host_request_dto** | [**ReorderHostRequestDto**](ReorderHostRequestDto.md)|  | 

### Return type

[**ReorderHostResponseDto**](ReorderHostResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hosts reordered successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_controller_update_host**
> UpdateHostResponseDto hosts_controller_update_host(update_host_request_dto)

Update a host

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.update_host_request_dto import UpdateHostRequestDto
from supn_remnawave_panel.models.update_host_response_dto import UpdateHostResponseDto
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
    api_instance = supn_remnawave_panel.HostsControllerApi(api_client)
    update_host_request_dto = supn_remnawave_panel.UpdateHostRequestDto() # UpdateHostRequestDto | 

    try:
        # Update a host
        api_response = await api_instance.hosts_controller_update_host(update_host_request_dto)
        print("The response of HostsControllerApi->hosts_controller_update_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsControllerApi->hosts_controller_update_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_host_request_dto** | [**UpdateHostRequestDto**](UpdateHostRequestDto.md)|  | 

### Return type

[**UpdateHostResponseDto**](UpdateHostResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Host updated successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

