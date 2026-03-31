# supn_remnawave_panel.ExternalSquadsControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_squad_controller_add_users_to_external_squad**](ExternalSquadsControllerApi.md#external_squad_controller_add_users_to_external_squad) | **POST** /api/external-squads/{uuid}/bulk-actions/add-users | Add all users to external squad
[**external_squad_controller_create_external_squad**](ExternalSquadsControllerApi.md#external_squad_controller_create_external_squad) | **POST** /api/external-squads | Create external squad
[**external_squad_controller_delete_external_squad**](ExternalSquadsControllerApi.md#external_squad_controller_delete_external_squad) | **DELETE** /api/external-squads/{uuid} | Delete external squad
[**external_squad_controller_get_external_squad_by_uuid**](ExternalSquadsControllerApi.md#external_squad_controller_get_external_squad_by_uuid) | **GET** /api/external-squads/{uuid} | Get external squad by uuid
[**external_squad_controller_get_external_squads**](ExternalSquadsControllerApi.md#external_squad_controller_get_external_squads) | **GET** /api/external-squads | Get all external squads
[**external_squad_controller_remove_users_from_external_squad**](ExternalSquadsControllerApi.md#external_squad_controller_remove_users_from_external_squad) | **DELETE** /api/external-squads/{uuid}/bulk-actions/remove-users | Delete users from external squad
[**external_squad_controller_reorder_external_squads**](ExternalSquadsControllerApi.md#external_squad_controller_reorder_external_squads) | **POST** /api/external-squads/actions/reorder | Reorder external squads
[**external_squad_controller_update_external_squad**](ExternalSquadsControllerApi.md#external_squad_controller_update_external_squad) | **PATCH** /api/external-squads | Update external squad


# **external_squad_controller_add_users_to_external_squad**
> AddUsersToExternalSquadResponseDto external_squad_controller_add_users_to_external_squad(uuid)

Add all users to external squad

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.add_users_to_external_squad_response_dto import AddUsersToExternalSquadResponseDto
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
    api_instance = supn_remnawave_panel.ExternalSquadsControllerApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Add all users to external squad
        api_response = await api_instance.external_squad_controller_add_users_to_external_squad(uuid)
        print("The response of ExternalSquadsControllerApi->external_squad_controller_add_users_to_external_squad:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalSquadsControllerApi->external_squad_controller_add_users_to_external_squad: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**AddUsersToExternalSquadResponseDto**](AddUsersToExternalSquadResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task added to external job queue |  -  |
**400** | Validation error |  -  |
**404** | External squad not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_squad_controller_create_external_squad**
> CreateExternalSquadResponseDto external_squad_controller_create_external_squad(create_external_squad_request_dto)

Create external squad

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.create_external_squad_request_dto import CreateExternalSquadRequestDto
from supn_remnawave_panel.models.create_external_squad_response_dto import CreateExternalSquadResponseDto
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
    api_instance = supn_remnawave_panel.ExternalSquadsControllerApi(api_client)
    create_external_squad_request_dto = supn_remnawave_panel.CreateExternalSquadRequestDto() # CreateExternalSquadRequestDto | 

    try:
        # Create external squad
        api_response = await api_instance.external_squad_controller_create_external_squad(create_external_squad_request_dto)
        print("The response of ExternalSquadsControllerApi->external_squad_controller_create_external_squad:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalSquadsControllerApi->external_squad_controller_create_external_squad: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_external_squad_request_dto** | [**CreateExternalSquadRequestDto**](CreateExternalSquadRequestDto.md)|  | 

### Return type

[**CreateExternalSquadResponseDto**](CreateExternalSquadResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | External squad created successfully |  -  |
**400** | Validation error |  -  |
**409** | External squad already exists |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_squad_controller_delete_external_squad**
> DeleteExternalSquadResponseDto external_squad_controller_delete_external_squad(uuid)

Delete external squad

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_external_squad_response_dto import DeleteExternalSquadResponseDto
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
    api_instance = supn_remnawave_panel.ExternalSquadsControllerApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Delete external squad
        api_response = await api_instance.external_squad_controller_delete_external_squad(uuid)
        print("The response of ExternalSquadsControllerApi->external_squad_controller_delete_external_squad:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalSquadsControllerApi->external_squad_controller_delete_external_squad: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**DeleteExternalSquadResponseDto**](DeleteExternalSquadResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | External squad deleted successfully |  -  |
**400** | Validation error |  -  |
**404** | External squad not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_squad_controller_get_external_squad_by_uuid**
> GetExternalSquadByUuidResponseDto external_squad_controller_get_external_squad_by_uuid(uuid)

Get external squad by uuid

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_external_squad_by_uuid_response_dto import GetExternalSquadByUuidResponseDto
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
    api_instance = supn_remnawave_panel.ExternalSquadsControllerApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Get external squad by uuid
        api_response = await api_instance.external_squad_controller_get_external_squad_by_uuid(uuid)
        print("The response of ExternalSquadsControllerApi->external_squad_controller_get_external_squad_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalSquadsControllerApi->external_squad_controller_get_external_squad_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**GetExternalSquadByUuidResponseDto**](GetExternalSquadByUuidResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | External squad retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_squad_controller_get_external_squads**
> GetExternalSquadsResponseDto external_squad_controller_get_external_squads()

Get all external squads

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_external_squads_response_dto import GetExternalSquadsResponseDto
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
    api_instance = supn_remnawave_panel.ExternalSquadsControllerApi(api_client)

    try:
        # Get all external squads
        api_response = await api_instance.external_squad_controller_get_external_squads()
        print("The response of ExternalSquadsControllerApi->external_squad_controller_get_external_squads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalSquadsControllerApi->external_squad_controller_get_external_squads: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetExternalSquadsResponseDto**](GetExternalSquadsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | External squads retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_squad_controller_remove_users_from_external_squad**
> RemoveUsersFromExternalSquadResponseDto external_squad_controller_remove_users_from_external_squad(uuid)

Delete users from external squad

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.remove_users_from_external_squad_response_dto import RemoveUsersFromExternalSquadResponseDto
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
    api_instance = supn_remnawave_panel.ExternalSquadsControllerApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Delete users from external squad
        api_response = await api_instance.external_squad_controller_remove_users_from_external_squad(uuid)
        print("The response of ExternalSquadsControllerApi->external_squad_controller_remove_users_from_external_squad:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalSquadsControllerApi->external_squad_controller_remove_users_from_external_squad: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**RemoveUsersFromExternalSquadResponseDto**](RemoveUsersFromExternalSquadResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task added to external job queue |  -  |
**400** | Validation error |  -  |
**404** | External squad not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_squad_controller_reorder_external_squads**
> ReorderExternalSquadsResponseDto external_squad_controller_reorder_external_squads(reorder_external_squads_request_dto)

Reorder external squads

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.reorder_external_squads_request_dto import ReorderExternalSquadsRequestDto
from supn_remnawave_panel.models.reorder_external_squads_response_dto import ReorderExternalSquadsResponseDto
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
    api_instance = supn_remnawave_panel.ExternalSquadsControllerApi(api_client)
    reorder_external_squads_request_dto = supn_remnawave_panel.ReorderExternalSquadsRequestDto() # ReorderExternalSquadsRequestDto | 

    try:
        # Reorder external squads
        api_response = await api_instance.external_squad_controller_reorder_external_squads(reorder_external_squads_request_dto)
        print("The response of ExternalSquadsControllerApi->external_squad_controller_reorder_external_squads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalSquadsControllerApi->external_squad_controller_reorder_external_squads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reorder_external_squads_request_dto** | [**ReorderExternalSquadsRequestDto**](ReorderExternalSquadsRequestDto.md)|  | 

### Return type

[**ReorderExternalSquadsResponseDto**](ReorderExternalSquadsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | External squads reordered successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_squad_controller_update_external_squad**
> UpdateExternalSquadResponseDto external_squad_controller_update_external_squad(update_external_squad_request_dto)

Update external squad

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.update_external_squad_request_dto import UpdateExternalSquadRequestDto
from supn_remnawave_panel.models.update_external_squad_response_dto import UpdateExternalSquadResponseDto
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
    api_instance = supn_remnawave_panel.ExternalSquadsControllerApi(api_client)
    update_external_squad_request_dto = supn_remnawave_panel.UpdateExternalSquadRequestDto() # UpdateExternalSquadRequestDto | 

    try:
        # Update external squad
        api_response = await api_instance.external_squad_controller_update_external_squad(update_external_squad_request_dto)
        print("The response of ExternalSquadsControllerApi->external_squad_controller_update_external_squad:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalSquadsControllerApi->external_squad_controller_update_external_squad: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_external_squad_request_dto** | [**UpdateExternalSquadRequestDto**](UpdateExternalSquadRequestDto.md)|  | 

### Return type

[**UpdateExternalSquadResponseDto**](UpdateExternalSquadResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | External squad updated successfully |  -  |
**400** | Validation error |  -  |
**404** | External squad not found |  -  |
**409** | External squad already exists |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

