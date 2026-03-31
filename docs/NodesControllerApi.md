# supn_remnawave_panel.NodesControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nodes_controller_bulk_nodes_actions**](NodesControllerApi.md#nodes_controller_bulk_nodes_actions) | **POST** /api/nodes/bulk-actions | Perform actions for many nodes
[**nodes_controller_bulk_nodes_update**](NodesControllerApi.md#nodes_controller_bulk_nodes_update) | **POST** /api/nodes/bulk-actions/update | Update many nodes
[**nodes_controller_create_node**](NodesControllerApi.md#nodes_controller_create_node) | **POST** /api/nodes | Create a new node
[**nodes_controller_delete_node**](NodesControllerApi.md#nodes_controller_delete_node) | **DELETE** /api/nodes/{uuid} | Delete a node
[**nodes_controller_disable_node**](NodesControllerApi.md#nodes_controller_disable_node) | **POST** /api/nodes/{uuid}/actions/disable | Disable a node
[**nodes_controller_enable_node**](NodesControllerApi.md#nodes_controller_enable_node) | **POST** /api/nodes/{uuid}/actions/enable | Enable a node
[**nodes_controller_get_all_nodes**](NodesControllerApi.md#nodes_controller_get_all_nodes) | **GET** /api/nodes | Get all nodes
[**nodes_controller_get_all_nodes_tags**](NodesControllerApi.md#nodes_controller_get_all_nodes_tags) | **GET** /api/nodes/tags | Get all existing nodes tags
[**nodes_controller_get_one_node**](NodesControllerApi.md#nodes_controller_get_one_node) | **GET** /api/nodes/{uuid} | Get node by UUID
[**nodes_controller_profile_modification**](NodesControllerApi.md#nodes_controller_profile_modification) | **POST** /api/nodes/bulk-actions/profile-modification | Modify Inbounds &amp; Profile for many nodes
[**nodes_controller_reorder_nodes**](NodesControllerApi.md#nodes_controller_reorder_nodes) | **POST** /api/nodes/actions/reorder | Reorder nodes
[**nodes_controller_reset_node_traffic**](NodesControllerApi.md#nodes_controller_reset_node_traffic) | **POST** /api/nodes/{uuid}/actions/reset-traffic | Reset Node Traffic
[**nodes_controller_restart_all_nodes**](NodesControllerApi.md#nodes_controller_restart_all_nodes) | **POST** /api/nodes/actions/restart-all | Restart all nodes
[**nodes_controller_restart_node**](NodesControllerApi.md#nodes_controller_restart_node) | **POST** /api/nodes/{uuid}/actions/restart | Restart node
[**nodes_controller_update_node**](NodesControllerApi.md#nodes_controller_update_node) | **PATCH** /api/nodes | Update node


# **nodes_controller_bulk_nodes_actions**
> BulkNodesActionsResponseDto nodes_controller_bulk_nodes_actions(bulk_nodes_actions_request_dto)

Perform actions for many nodes

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.bulk_nodes_actions_request_dto import BulkNodesActionsRequestDto
from supn_remnawave_panel.models.bulk_nodes_actions_response_dto import BulkNodesActionsResponseDto
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
    api_instance = supn_remnawave_panel.NodesControllerApi(api_client)
    bulk_nodes_actions_request_dto = supn_remnawave_panel.BulkNodesActionsRequestDto() # BulkNodesActionsRequestDto | 

    try:
        # Perform actions for many nodes
        api_response = await api_instance.nodes_controller_bulk_nodes_actions(bulk_nodes_actions_request_dto)
        print("The response of NodesControllerApi->nodes_controller_bulk_nodes_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesControllerApi->nodes_controller_bulk_nodes_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_nodes_actions_request_dto** | [**BulkNodesActionsRequestDto**](BulkNodesActionsRequestDto.md)|  | 

### Return type

[**BulkNodesActionsResponseDto**](BulkNodesActionsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event sent successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes_controller_bulk_nodes_update**
> BulkNodesUpdateResponseDto nodes_controller_bulk_nodes_update(bulk_nodes_update_request_dto)

Update many nodes

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.bulk_nodes_update_request_dto import BulkNodesUpdateRequestDto
from supn_remnawave_panel.models.bulk_nodes_update_response_dto import BulkNodesUpdateResponseDto
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
    api_instance = supn_remnawave_panel.NodesControllerApi(api_client)
    bulk_nodes_update_request_dto = supn_remnawave_panel.BulkNodesUpdateRequestDto() # BulkNodesUpdateRequestDto | 

    try:
        # Update many nodes
        api_response = await api_instance.nodes_controller_bulk_nodes_update(bulk_nodes_update_request_dto)
        print("The response of NodesControllerApi->nodes_controller_bulk_nodes_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesControllerApi->nodes_controller_bulk_nodes_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_nodes_update_request_dto** | [**BulkNodesUpdateRequestDto**](BulkNodesUpdateRequestDto.md)|  | 

### Return type

[**BulkNodesUpdateResponseDto**](BulkNodesUpdateResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event sent successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes_controller_create_node**
> CreateNodeResponseDto nodes_controller_create_node(create_node_request_dto)

Create a new node

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.create_node_request_dto import CreateNodeRequestDto
from supn_remnawave_panel.models.create_node_response_dto import CreateNodeResponseDto
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
    api_instance = supn_remnawave_panel.NodesControllerApi(api_client)
    create_node_request_dto = supn_remnawave_panel.CreateNodeRequestDto() # CreateNodeRequestDto | 

    try:
        # Create a new node
        api_response = await api_instance.nodes_controller_create_node(create_node_request_dto)
        print("The response of NodesControllerApi->nodes_controller_create_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesControllerApi->nodes_controller_create_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_node_request_dto** | [**CreateNodeRequestDto**](CreateNodeRequestDto.md)|  | 

### Return type

[**CreateNodeResponseDto**](CreateNodeResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Node created successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes_controller_delete_node**
> DeleteNodeResponseDto nodes_controller_delete_node(uuid)

Delete a node

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_node_response_dto import DeleteNodeResponseDto
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
    api_instance = supn_remnawave_panel.NodesControllerApi(api_client)
    uuid = 'uuid_example' # str | Node UUID

    try:
        # Delete a node
        api_response = await api_instance.nodes_controller_delete_node(uuid)
        print("The response of NodesControllerApi->nodes_controller_delete_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesControllerApi->nodes_controller_delete_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Node UUID | 

### Return type

[**DeleteNodeResponseDto**](DeleteNodeResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node deleted |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes_controller_disable_node**
> DisableNodeResponseDto nodes_controller_disable_node(uuid)

Disable a node

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.disable_node_response_dto import DisableNodeResponseDto
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
    api_instance = supn_remnawave_panel.NodesControllerApi(api_client)
    uuid = 'uuid_example' # str | Node UUID

    try:
        # Disable a node
        api_response = await api_instance.nodes_controller_disable_node(uuid)
        print("The response of NodesControllerApi->nodes_controller_disable_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesControllerApi->nodes_controller_disable_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Node UUID | 

### Return type

[**DisableNodeResponseDto**](DisableNodeResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node disabled |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes_controller_enable_node**
> EnableNodeResponseDto nodes_controller_enable_node(uuid)

Enable a node

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.enable_node_response_dto import EnableNodeResponseDto
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
    api_instance = supn_remnawave_panel.NodesControllerApi(api_client)
    uuid = 'uuid_example' # str | Node UUID

    try:
        # Enable a node
        api_response = await api_instance.nodes_controller_enable_node(uuid)
        print("The response of NodesControllerApi->nodes_controller_enable_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesControllerApi->nodes_controller_enable_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Node UUID | 

### Return type

[**EnableNodeResponseDto**](EnableNodeResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node enabled |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes_controller_get_all_nodes**
> GetAllNodesResponseDto nodes_controller_get_all_nodes()

Get all nodes

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_all_nodes_response_dto import GetAllNodesResponseDto
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
    api_instance = supn_remnawave_panel.NodesControllerApi(api_client)

    try:
        # Get all nodes
        api_response = await api_instance.nodes_controller_get_all_nodes()
        print("The response of NodesControllerApi->nodes_controller_get_all_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesControllerApi->nodes_controller_get_all_nodes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllNodesResponseDto**](GetAllNodesResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Nodes fetched |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes_controller_get_all_nodes_tags**
> GetAllNodesTagsResponseDto nodes_controller_get_all_nodes_tags()

Get all existing nodes tags

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_all_nodes_tags_response_dto import GetAllNodesTagsResponseDto
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
    api_instance = supn_remnawave_panel.NodesControllerApi(api_client)

    try:
        # Get all existing nodes tags
        api_response = await api_instance.nodes_controller_get_all_nodes_tags()
        print("The response of NodesControllerApi->nodes_controller_get_all_nodes_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesControllerApi->nodes_controller_get_all_nodes_tags: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllNodesTagsResponseDto**](GetAllNodesTagsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Nodes tags fetched |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes_controller_get_one_node**
> GetOneNodeResponseDto nodes_controller_get_one_node(uuid)

Get node by UUID

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_one_node_response_dto import GetOneNodeResponseDto
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
    api_instance = supn_remnawave_panel.NodesControllerApi(api_client)
    uuid = 'uuid_example' # str | Node UUID

    try:
        # Get node by UUID
        api_response = await api_instance.nodes_controller_get_one_node(uuid)
        print("The response of NodesControllerApi->nodes_controller_get_one_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesControllerApi->nodes_controller_get_one_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Node UUID | 

### Return type

[**GetOneNodeResponseDto**](GetOneNodeResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node fetched |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes_controller_profile_modification**
> ProfileModificationResponseDto nodes_controller_profile_modification(profile_modification_request_dto)

Modify Inbounds & Profile for many nodes

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.profile_modification_request_dto import ProfileModificationRequestDto
from supn_remnawave_panel.models.profile_modification_response_dto import ProfileModificationResponseDto
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
    api_instance = supn_remnawave_panel.NodesControllerApi(api_client)
    profile_modification_request_dto = supn_remnawave_panel.ProfileModificationRequestDto() # ProfileModificationRequestDto | 

    try:
        # Modify Inbounds & Profile for many nodes
        api_response = await api_instance.nodes_controller_profile_modification(profile_modification_request_dto)
        print("The response of NodesControllerApi->nodes_controller_profile_modification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesControllerApi->nodes_controller_profile_modification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_modification_request_dto** | [**ProfileModificationRequestDto**](ProfileModificationRequestDto.md)|  | 

### Return type

[**ProfileModificationResponseDto**](ProfileModificationResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event sent successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes_controller_reorder_nodes**
> ReorderNodeResponseDto nodes_controller_reorder_nodes(reorder_node_request_dto)

Reorder nodes

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.reorder_node_request_dto import ReorderNodeRequestDto
from supn_remnawave_panel.models.reorder_node_response_dto import ReorderNodeResponseDto
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
    api_instance = supn_remnawave_panel.NodesControllerApi(api_client)
    reorder_node_request_dto = supn_remnawave_panel.ReorderNodeRequestDto() # ReorderNodeRequestDto | 

    try:
        # Reorder nodes
        api_response = await api_instance.nodes_controller_reorder_nodes(reorder_node_request_dto)
        print("The response of NodesControllerApi->nodes_controller_reorder_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesControllerApi->nodes_controller_reorder_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reorder_node_request_dto** | [**ReorderNodeRequestDto**](ReorderNodeRequestDto.md)|  | 

### Return type

[**ReorderNodeResponseDto**](ReorderNodeResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Nodes reordered successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes_controller_reset_node_traffic**
> ResetNodeTrafficResponseDto nodes_controller_reset_node_traffic(uuid)

Reset Node Traffic

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.reset_node_traffic_response_dto import ResetNodeTrafficResponseDto
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
    api_instance = supn_remnawave_panel.NodesControllerApi(api_client)
    uuid = 'uuid_example' # str | Node UUID

    try:
        # Reset Node Traffic
        api_response = await api_instance.nodes_controller_reset_node_traffic(uuid)
        print("The response of NodesControllerApi->nodes_controller_reset_node_traffic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesControllerApi->nodes_controller_reset_node_traffic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Node UUID | 

### Return type

[**ResetNodeTrafficResponseDto**](ResetNodeTrafficResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event sent |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes_controller_restart_all_nodes**
> RestartAllNodesResponseDto nodes_controller_restart_all_nodes(restart_all_nodes_request_body_dto)

Restart all nodes

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.restart_all_nodes_request_body_dto import RestartAllNodesRequestBodyDto
from supn_remnawave_panel.models.restart_all_nodes_response_dto import RestartAllNodesResponseDto
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
    api_instance = supn_remnawave_panel.NodesControllerApi(api_client)
    restart_all_nodes_request_body_dto = supn_remnawave_panel.RestartAllNodesRequestBodyDto() # RestartAllNodesRequestBodyDto | 

    try:
        # Restart all nodes
        api_response = await api_instance.nodes_controller_restart_all_nodes(restart_all_nodes_request_body_dto)
        print("The response of NodesControllerApi->nodes_controller_restart_all_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesControllerApi->nodes_controller_restart_all_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restart_all_nodes_request_body_dto** | [**RestartAllNodesRequestBodyDto**](RestartAllNodesRequestBodyDto.md)|  | 

### Return type

[**RestartAllNodesResponseDto**](RestartAllNodesResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All nodes restarted |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes_controller_restart_node**
> RestartNodeResponseDto nodes_controller_restart_node(uuid)

Restart node

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.restart_node_response_dto import RestartNodeResponseDto
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
    api_instance = supn_remnawave_panel.NodesControllerApi(api_client)
    uuid = 'uuid_example' # str | Node UUID

    try:
        # Restart node
        api_response = await api_instance.nodes_controller_restart_node(uuid)
        print("The response of NodesControllerApi->nodes_controller_restart_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesControllerApi->nodes_controller_restart_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Node UUID | 

### Return type

[**RestartNodeResponseDto**](RestartNodeResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node restarted |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes_controller_update_node**
> UpdateNodeResponseDto nodes_controller_update_node(update_node_request_dto)

Update node

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.update_node_request_dto import UpdateNodeRequestDto
from supn_remnawave_panel.models.update_node_response_dto import UpdateNodeResponseDto
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
    api_instance = supn_remnawave_panel.NodesControllerApi(api_client)
    update_node_request_dto = supn_remnawave_panel.UpdateNodeRequestDto() # UpdateNodeRequestDto | 

    try:
        # Update node
        api_response = await api_instance.nodes_controller_update_node(update_node_request_dto)
        print("The response of NodesControllerApi->nodes_controller_update_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodesControllerApi->nodes_controller_update_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_node_request_dto** | [**UpdateNodeRequestDto**](UpdateNodeRequestDto.md)|  | 

### Return type

[**UpdateNodeResponseDto**](UpdateNodeResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node updated |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

