# supn_remnawave_panel.MetadataControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_controller_get_node_metadata**](MetadataControllerApi.md#metadata_controller_get_node_metadata) | **GET** /api/metadata/node/{uuid} | Get node metadata
[**metadata_controller_get_user_metadata**](MetadataControllerApi.md#metadata_controller_get_user_metadata) | **GET** /api/metadata/user/{uuid} | Get user metadata
[**metadata_controller_upsert_node_metadata**](MetadataControllerApi.md#metadata_controller_upsert_node_metadata) | **PUT** /api/metadata/node/{uuid} | Update or create Node Metadata
[**metadata_controller_upsert_user_metadata**](MetadataControllerApi.md#metadata_controller_upsert_user_metadata) | **PUT** /api/metadata/user/{uuid} | Update or create User Metadata


# **metadata_controller_get_node_metadata**
> GetNodeMetadataResponseDto metadata_controller_get_node_metadata(uuid)

Get node metadata

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_node_metadata_response_dto import GetNodeMetadataResponseDto
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
    api_instance = supn_remnawave_panel.MetadataControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the node

    try:
        # Get node metadata
        api_response = await api_instance.metadata_controller_get_node_metadata(uuid)
        print("The response of MetadataControllerApi->metadata_controller_get_node_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataControllerApi->metadata_controller_get_node_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the node | 

### Return type

[**GetNodeMetadataResponseDto**](GetNodeMetadataResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node Metadata retrieved successfully |  -  |
**400** | Validation error |  -  |
**404** | Node or Metadata not found (see errorCode for more details) |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_controller_get_user_metadata**
> GetUserMetadataResponseDto metadata_controller_get_user_metadata(uuid)

Get user metadata

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_user_metadata_response_dto import GetUserMetadataResponseDto
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
    api_instance = supn_remnawave_panel.MetadataControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the user

    try:
        # Get user metadata
        api_response = await api_instance.metadata_controller_get_user_metadata(uuid)
        print("The response of MetadataControllerApi->metadata_controller_get_user_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataControllerApi->metadata_controller_get_user_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the user | 

### Return type

[**GetUserMetadataResponseDto**](GetUserMetadataResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Metadata retrieved successfully |  -  |
**400** | Validation error |  -  |
**404** | User or Metadata not found (see errorCode for more details) |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_controller_upsert_node_metadata**
> UpsertNodeMetadataResponseDto metadata_controller_upsert_node_metadata(uuid, upsert_node_metadata_request_body_dto)

Update or create Node Metadata

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.upsert_node_metadata_request_body_dto import UpsertNodeMetadataRequestBodyDto
from supn_remnawave_panel.models.upsert_node_metadata_response_dto import UpsertNodeMetadataResponseDto
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
    api_instance = supn_remnawave_panel.MetadataControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the node
    upsert_node_metadata_request_body_dto = supn_remnawave_panel.UpsertNodeMetadataRequestBodyDto() # UpsertNodeMetadataRequestBodyDto | 

    try:
        # Update or create Node Metadata
        api_response = await api_instance.metadata_controller_upsert_node_metadata(uuid, upsert_node_metadata_request_body_dto)
        print("The response of MetadataControllerApi->metadata_controller_upsert_node_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataControllerApi->metadata_controller_upsert_node_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the node | 
 **upsert_node_metadata_request_body_dto** | [**UpsertNodeMetadataRequestBodyDto**](UpsertNodeMetadataRequestBodyDto.md)|  | 

### Return type

[**UpsertNodeMetadataResponseDto**](UpsertNodeMetadataResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node Metadata upserted successfully |  -  |
**400** | Validation error |  -  |
**404** | Node not found (see errorCode for more details) |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_controller_upsert_user_metadata**
> UpsertUserMetadataResponseDto metadata_controller_upsert_user_metadata(uuid, upsert_user_metadata_request_body_dto)

Update or create User Metadata

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.upsert_user_metadata_request_body_dto import UpsertUserMetadataRequestBodyDto
from supn_remnawave_panel.models.upsert_user_metadata_response_dto import UpsertUserMetadataResponseDto
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
    api_instance = supn_remnawave_panel.MetadataControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the user
    upsert_user_metadata_request_body_dto = supn_remnawave_panel.UpsertUserMetadataRequestBodyDto() # UpsertUserMetadataRequestBodyDto | 

    try:
        # Update or create User Metadata
        api_response = await api_instance.metadata_controller_upsert_user_metadata(uuid, upsert_user_metadata_request_body_dto)
        print("The response of MetadataControllerApi->metadata_controller_upsert_user_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataControllerApi->metadata_controller_upsert_user_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the user | 
 **upsert_user_metadata_request_body_dto** | [**UpsertUserMetadataRequestBodyDto**](UpsertUserMetadataRequestBodyDto.md)|  | 

### Return type

[**UpsertUserMetadataResponseDto**](UpsertUserMetadataResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Metadata upserted successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found (see errorCode for more details) |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

