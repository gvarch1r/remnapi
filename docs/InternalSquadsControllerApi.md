# supn_remnawave_panel.InternalSquadsControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**internal_squad_controller_add_users_to_internal_squad**](InternalSquadsControllerApi.md#internal_squad_controller_add_users_to_internal_squad) | **POST** /api/internal-squads/{uuid}/bulk-actions/add-users | Add all users to internal squad
[**internal_squad_controller_create_internal_squad**](InternalSquadsControllerApi.md#internal_squad_controller_create_internal_squad) | **POST** /api/internal-squads | Create internal squad
[**internal_squad_controller_delete_internal_squad**](InternalSquadsControllerApi.md#internal_squad_controller_delete_internal_squad) | **DELETE** /api/internal-squads/{uuid} | Delete internal squad
[**internal_squad_controller_get_internal_squad_accessible_nodes**](InternalSquadsControllerApi.md#internal_squad_controller_get_internal_squad_accessible_nodes) | **GET** /api/internal-squads/{uuid}/accessible-nodes | Get internal squad accessible nodes
[**internal_squad_controller_get_internal_squad_by_uuid**](InternalSquadsControllerApi.md#internal_squad_controller_get_internal_squad_by_uuid) | **GET** /api/internal-squads/{uuid} | Get internal squad by uuid
[**internal_squad_controller_get_internal_squads**](InternalSquadsControllerApi.md#internal_squad_controller_get_internal_squads) | **GET** /api/internal-squads | Get all internal squads
[**internal_squad_controller_remove_users_from_internal_squad**](InternalSquadsControllerApi.md#internal_squad_controller_remove_users_from_internal_squad) | **DELETE** /api/internal-squads/{uuid}/bulk-actions/remove-users | Delete users from internal squad
[**internal_squad_controller_reorder_internal_squads**](InternalSquadsControllerApi.md#internal_squad_controller_reorder_internal_squads) | **POST** /api/internal-squads/actions/reorder | Reorder internal squads
[**internal_squad_controller_update_internal_squad**](InternalSquadsControllerApi.md#internal_squad_controller_update_internal_squad) | **PATCH** /api/internal-squads | Update internal squad


# **internal_squad_controller_add_users_to_internal_squad**
> AddUsersToInternalSquadResponseDto internal_squad_controller_add_users_to_internal_squad(uuid)

Add all users to internal squad

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.add_users_to_internal_squad_response_dto import AddUsersToInternalSquadResponseDto
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
    api_instance = supn_remnawave_panel.InternalSquadsControllerApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Add all users to internal squad
        api_response = await api_instance.internal_squad_controller_add_users_to_internal_squad(uuid)
        print("The response of InternalSquadsControllerApi->internal_squad_controller_add_users_to_internal_squad:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalSquadsControllerApi->internal_squad_controller_add_users_to_internal_squad: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**AddUsersToInternalSquadResponseDto**](AddUsersToInternalSquadResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task added to internal job queue |  -  |
**400** | Validation error |  -  |
**404** | Internal squad not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_squad_controller_create_internal_squad**
> CreateInternalSquadResponseDto internal_squad_controller_create_internal_squad(create_internal_squad_request_dto)

Create internal squad

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.create_internal_squad_request_dto import CreateInternalSquadRequestDto
from supn_remnawave_panel.models.create_internal_squad_response_dto import CreateInternalSquadResponseDto
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
    api_instance = supn_remnawave_panel.InternalSquadsControllerApi(api_client)
    create_internal_squad_request_dto = supn_remnawave_panel.CreateInternalSquadRequestDto() # CreateInternalSquadRequestDto | 

    try:
        # Create internal squad
        api_response = await api_instance.internal_squad_controller_create_internal_squad(create_internal_squad_request_dto)
        print("The response of InternalSquadsControllerApi->internal_squad_controller_create_internal_squad:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalSquadsControllerApi->internal_squad_controller_create_internal_squad: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_internal_squad_request_dto** | [**CreateInternalSquadRequestDto**](CreateInternalSquadRequestDto.md)|  | 

### Return type

[**CreateInternalSquadResponseDto**](CreateInternalSquadResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Internal squad created successfully |  -  |
**400** | Validation error |  -  |
**409** | Internal squad already exists |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_squad_controller_delete_internal_squad**
> DeleteInternalSquadResponseDto internal_squad_controller_delete_internal_squad(uuid)

Delete internal squad

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_internal_squad_response_dto import DeleteInternalSquadResponseDto
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
    api_instance = supn_remnawave_panel.InternalSquadsControllerApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Delete internal squad
        api_response = await api_instance.internal_squad_controller_delete_internal_squad(uuid)
        print("The response of InternalSquadsControllerApi->internal_squad_controller_delete_internal_squad:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalSquadsControllerApi->internal_squad_controller_delete_internal_squad: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**DeleteInternalSquadResponseDto**](DeleteInternalSquadResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Internal squad deleted successfully |  -  |
**400** | Validation error |  -  |
**404** | Internal squad not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_squad_controller_get_internal_squad_accessible_nodes**
> GetInternalSquadAccessibleNodesResponseDto internal_squad_controller_get_internal_squad_accessible_nodes(uuid)

Get internal squad accessible nodes

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_internal_squad_accessible_nodes_response_dto import GetInternalSquadAccessibleNodesResponseDto
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
    api_instance = supn_remnawave_panel.InternalSquadsControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the internal squad

    try:
        # Get internal squad accessible nodes
        api_response = await api_instance.internal_squad_controller_get_internal_squad_accessible_nodes(uuid)
        print("The response of InternalSquadsControllerApi->internal_squad_controller_get_internal_squad_accessible_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalSquadsControllerApi->internal_squad_controller_get_internal_squad_accessible_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the internal squad | 

### Return type

[**GetInternalSquadAccessibleNodesResponseDto**](GetInternalSquadAccessibleNodesResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Internal squad accessible nodes fetched successfully |  -  |
**400** | Validation error |  -  |
**404** | Internal squad not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_squad_controller_get_internal_squad_by_uuid**
> GetInternalSquadByUuidResponseDto internal_squad_controller_get_internal_squad_by_uuid(uuid)

Get internal squad by uuid

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_internal_squad_by_uuid_response_dto import GetInternalSquadByUuidResponseDto
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
    api_instance = supn_remnawave_panel.InternalSquadsControllerApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Get internal squad by uuid
        api_response = await api_instance.internal_squad_controller_get_internal_squad_by_uuid(uuid)
        print("The response of InternalSquadsControllerApi->internal_squad_controller_get_internal_squad_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalSquadsControllerApi->internal_squad_controller_get_internal_squad_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**GetInternalSquadByUuidResponseDto**](GetInternalSquadByUuidResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Internal squad retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_squad_controller_get_internal_squads**
> GetInternalSquadsResponseDto internal_squad_controller_get_internal_squads()

Get all internal squads

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_internal_squads_response_dto import GetInternalSquadsResponseDto
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
    api_instance = supn_remnawave_panel.InternalSquadsControllerApi(api_client)

    try:
        # Get all internal squads
        api_response = await api_instance.internal_squad_controller_get_internal_squads()
        print("The response of InternalSquadsControllerApi->internal_squad_controller_get_internal_squads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalSquadsControllerApi->internal_squad_controller_get_internal_squads: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetInternalSquadsResponseDto**](GetInternalSquadsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Internal squads retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_squad_controller_remove_users_from_internal_squad**
> RemoveUsersFromInternalSquadResponseDto internal_squad_controller_remove_users_from_internal_squad(uuid)

Delete users from internal squad

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.remove_users_from_internal_squad_response_dto import RemoveUsersFromInternalSquadResponseDto
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
    api_instance = supn_remnawave_panel.InternalSquadsControllerApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Delete users from internal squad
        api_response = await api_instance.internal_squad_controller_remove_users_from_internal_squad(uuid)
        print("The response of InternalSquadsControllerApi->internal_squad_controller_remove_users_from_internal_squad:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalSquadsControllerApi->internal_squad_controller_remove_users_from_internal_squad: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**RemoveUsersFromInternalSquadResponseDto**](RemoveUsersFromInternalSquadResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task added to internal job queue |  -  |
**400** | Validation error |  -  |
**404** | Internal squad not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_squad_controller_reorder_internal_squads**
> ReorderInternalSquadsResponseDto internal_squad_controller_reorder_internal_squads(reorder_internal_squads_request_dto)

Reorder internal squads

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.reorder_internal_squads_request_dto import ReorderInternalSquadsRequestDto
from supn_remnawave_panel.models.reorder_internal_squads_response_dto import ReorderInternalSquadsResponseDto
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
    api_instance = supn_remnawave_panel.InternalSquadsControllerApi(api_client)
    reorder_internal_squads_request_dto = supn_remnawave_panel.ReorderInternalSquadsRequestDto() # ReorderInternalSquadsRequestDto | 

    try:
        # Reorder internal squads
        api_response = await api_instance.internal_squad_controller_reorder_internal_squads(reorder_internal_squads_request_dto)
        print("The response of InternalSquadsControllerApi->internal_squad_controller_reorder_internal_squads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalSquadsControllerApi->internal_squad_controller_reorder_internal_squads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reorder_internal_squads_request_dto** | [**ReorderInternalSquadsRequestDto**](ReorderInternalSquadsRequestDto.md)|  | 

### Return type

[**ReorderInternalSquadsResponseDto**](ReorderInternalSquadsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Internal squads reordered successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_squad_controller_update_internal_squad**
> UpdateInternalSquadResponseDto internal_squad_controller_update_internal_squad(update_internal_squad_request_dto)

Update internal squad

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.update_internal_squad_request_dto import UpdateInternalSquadRequestDto
from supn_remnawave_panel.models.update_internal_squad_response_dto import UpdateInternalSquadResponseDto
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
    api_instance = supn_remnawave_panel.InternalSquadsControllerApi(api_client)
    update_internal_squad_request_dto = supn_remnawave_panel.UpdateInternalSquadRequestDto() # UpdateInternalSquadRequestDto | 

    try:
        # Update internal squad
        api_response = await api_instance.internal_squad_controller_update_internal_squad(update_internal_squad_request_dto)
        print("The response of InternalSquadsControllerApi->internal_squad_controller_update_internal_squad:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalSquadsControllerApi->internal_squad_controller_update_internal_squad: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_internal_squad_request_dto** | [**UpdateInternalSquadRequestDto**](UpdateInternalSquadRequestDto.md)|  | 

### Return type

[**UpdateInternalSquadResponseDto**](UpdateInternalSquadResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Internal squad updated successfully |  -  |
**400** | Validation error |  -  |
**404** | Internal squad not found |  -  |
**409** | Internal squad already exists |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

