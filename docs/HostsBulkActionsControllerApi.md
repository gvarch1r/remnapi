# supn_remnawave_panel.HostsBulkActionsControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hosts_bulk_actions_controller_delete_hosts**](HostsBulkActionsControllerApi.md#hosts_bulk_actions_controller_delete_hosts) | **POST** /api/hosts/bulk/delete | Delete hosts by UUIDs
[**hosts_bulk_actions_controller_disable_hosts**](HostsBulkActionsControllerApi.md#hosts_bulk_actions_controller_disable_hosts) | **POST** /api/hosts/bulk/disable | Disable hosts by UUIDs
[**hosts_bulk_actions_controller_enable_hosts**](HostsBulkActionsControllerApi.md#hosts_bulk_actions_controller_enable_hosts) | **POST** /api/hosts/bulk/enable | Enable hosts by UUIDs
[**hosts_bulk_actions_controller_set_inbound_to_hosts**](HostsBulkActionsControllerApi.md#hosts_bulk_actions_controller_set_inbound_to_hosts) | **POST** /api/hosts/bulk/set-inbound | Set inbound to hosts by UUIDs
[**hosts_bulk_actions_controller_set_port_to_hosts**](HostsBulkActionsControllerApi.md#hosts_bulk_actions_controller_set_port_to_hosts) | **POST** /api/hosts/bulk/set-port | Set port to hosts by UUIDs


# **hosts_bulk_actions_controller_delete_hosts**
> BulkDeleteHostsResponseDto hosts_bulk_actions_controller_delete_hosts(bulk_delete_hosts_request_dto)

Delete hosts by UUIDs

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.bulk_delete_hosts_request_dto import BulkDeleteHostsRequestDto
from supn_remnawave_panel.models.bulk_delete_hosts_response_dto import BulkDeleteHostsResponseDto
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
    api_instance = supn_remnawave_panel.HostsBulkActionsControllerApi(api_client)
    bulk_delete_hosts_request_dto = supn_remnawave_panel.BulkDeleteHostsRequestDto() # BulkDeleteHostsRequestDto | 

    try:
        # Delete hosts by UUIDs
        api_response = await api_instance.hosts_bulk_actions_controller_delete_hosts(bulk_delete_hosts_request_dto)
        print("The response of HostsBulkActionsControllerApi->hosts_bulk_actions_controller_delete_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsBulkActionsControllerApi->hosts_bulk_actions_controller_delete_hosts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_delete_hosts_request_dto** | [**BulkDeleteHostsRequestDto**](BulkDeleteHostsRequestDto.md)|  | 

### Return type

[**BulkDeleteHostsResponseDto**](BulkDeleteHostsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hosts deleted successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_bulk_actions_controller_disable_hosts**
> BulkDisableHostsResponseDto hosts_bulk_actions_controller_disable_hosts(bulk_disable_hosts_request_dto)

Disable hosts by UUIDs

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.bulk_disable_hosts_request_dto import BulkDisableHostsRequestDto
from supn_remnawave_panel.models.bulk_disable_hosts_response_dto import BulkDisableHostsResponseDto
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
    api_instance = supn_remnawave_panel.HostsBulkActionsControllerApi(api_client)
    bulk_disable_hosts_request_dto = supn_remnawave_panel.BulkDisableHostsRequestDto() # BulkDisableHostsRequestDto | 

    try:
        # Disable hosts by UUIDs
        api_response = await api_instance.hosts_bulk_actions_controller_disable_hosts(bulk_disable_hosts_request_dto)
        print("The response of HostsBulkActionsControllerApi->hosts_bulk_actions_controller_disable_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsBulkActionsControllerApi->hosts_bulk_actions_controller_disable_hosts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_disable_hosts_request_dto** | [**BulkDisableHostsRequestDto**](BulkDisableHostsRequestDto.md)|  | 

### Return type

[**BulkDisableHostsResponseDto**](BulkDisableHostsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hosts disabled successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_bulk_actions_controller_enable_hosts**
> BulkEnableHostsResponseDto hosts_bulk_actions_controller_enable_hosts(bulk_enable_hosts_request_dto)

Enable hosts by UUIDs

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.bulk_enable_hosts_request_dto import BulkEnableHostsRequestDto
from supn_remnawave_panel.models.bulk_enable_hosts_response_dto import BulkEnableHostsResponseDto
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
    api_instance = supn_remnawave_panel.HostsBulkActionsControllerApi(api_client)
    bulk_enable_hosts_request_dto = supn_remnawave_panel.BulkEnableHostsRequestDto() # BulkEnableHostsRequestDto | 

    try:
        # Enable hosts by UUIDs
        api_response = await api_instance.hosts_bulk_actions_controller_enable_hosts(bulk_enable_hosts_request_dto)
        print("The response of HostsBulkActionsControllerApi->hosts_bulk_actions_controller_enable_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsBulkActionsControllerApi->hosts_bulk_actions_controller_enable_hosts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_enable_hosts_request_dto** | [**BulkEnableHostsRequestDto**](BulkEnableHostsRequestDto.md)|  | 

### Return type

[**BulkEnableHostsResponseDto**](BulkEnableHostsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hosts enabled successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_bulk_actions_controller_set_inbound_to_hosts**
> SetInboundToManyHostsResponseDto hosts_bulk_actions_controller_set_inbound_to_hosts(set_inbound_to_many_hosts_request_dto)

Set inbound to hosts by UUIDs

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.set_inbound_to_many_hosts_request_dto import SetInboundToManyHostsRequestDto
from supn_remnawave_panel.models.set_inbound_to_many_hosts_response_dto import SetInboundToManyHostsResponseDto
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
    api_instance = supn_remnawave_panel.HostsBulkActionsControllerApi(api_client)
    set_inbound_to_many_hosts_request_dto = supn_remnawave_panel.SetInboundToManyHostsRequestDto() # SetInboundToManyHostsRequestDto | 

    try:
        # Set inbound to hosts by UUIDs
        api_response = await api_instance.hosts_bulk_actions_controller_set_inbound_to_hosts(set_inbound_to_many_hosts_request_dto)
        print("The response of HostsBulkActionsControllerApi->hosts_bulk_actions_controller_set_inbound_to_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsBulkActionsControllerApi->hosts_bulk_actions_controller_set_inbound_to_hosts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_inbound_to_many_hosts_request_dto** | [**SetInboundToManyHostsRequestDto**](SetInboundToManyHostsRequestDto.md)|  | 

### Return type

[**SetInboundToManyHostsResponseDto**](SetInboundToManyHostsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hosts inbound set successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_bulk_actions_controller_set_port_to_hosts**
> SetPortToManyHostsResponseDto hosts_bulk_actions_controller_set_port_to_hosts(set_port_to_many_hosts_request_dto)

Set port to hosts by UUIDs

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.set_port_to_many_hosts_request_dto import SetPortToManyHostsRequestDto
from supn_remnawave_panel.models.set_port_to_many_hosts_response_dto import SetPortToManyHostsResponseDto
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
    api_instance = supn_remnawave_panel.HostsBulkActionsControllerApi(api_client)
    set_port_to_many_hosts_request_dto = supn_remnawave_panel.SetPortToManyHostsRequestDto() # SetPortToManyHostsRequestDto | 

    try:
        # Set port to hosts by UUIDs
        api_response = await api_instance.hosts_bulk_actions_controller_set_port_to_hosts(set_port_to_many_hosts_request_dto)
        print("The response of HostsBulkActionsControllerApi->hosts_bulk_actions_controller_set_port_to_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsBulkActionsControllerApi->hosts_bulk_actions_controller_set_port_to_hosts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_port_to_many_hosts_request_dto** | [**SetPortToManyHostsRequestDto**](SetPortToManyHostsRequestDto.md)|  | 

### Return type

[**SetPortToManyHostsResponseDto**](SetPortToManyHostsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hosts port set successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

