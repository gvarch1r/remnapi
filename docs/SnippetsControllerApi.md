# supn_remnawave_panel.SnippetsControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**snippets_controller_create_snippet**](SnippetsControllerApi.md#snippets_controller_create_snippet) | **POST** /api/snippets | Create snippet
[**snippets_controller_delete_snippet_by_name**](SnippetsControllerApi.md#snippets_controller_delete_snippet_by_name) | **DELETE** /api/snippets | Delete snippet
[**snippets_controller_get_snippets**](SnippetsControllerApi.md#snippets_controller_get_snippets) | **GET** /api/snippets | Get snippets
[**snippets_controller_update_snippet**](SnippetsControllerApi.md#snippets_controller_update_snippet) | **PATCH** /api/snippets | Update snippet


# **snippets_controller_create_snippet**
> CreateSnippetResponseDto snippets_controller_create_snippet(create_snippet_request_dto)

Create snippet

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.create_snippet_request_dto import CreateSnippetRequestDto
from supn_remnawave_panel.models.create_snippet_response_dto import CreateSnippetResponseDto
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
    api_instance = supn_remnawave_panel.SnippetsControllerApi(api_client)
    create_snippet_request_dto = supn_remnawave_panel.CreateSnippetRequestDto() # CreateSnippetRequestDto | 

    try:
        # Create snippet
        api_response = await api_instance.snippets_controller_create_snippet(create_snippet_request_dto)
        print("The response of SnippetsControllerApi->snippets_controller_create_snippet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetsControllerApi->snippets_controller_create_snippet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_snippet_request_dto** | [**CreateSnippetRequestDto**](CreateSnippetRequestDto.md)|  | 

### Return type

[**CreateSnippetResponseDto**](CreateSnippetResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Snippet created successfully |  -  |
**400** | Validation error |  -  |
**409** | Snippet name already exists. |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snippets_controller_delete_snippet_by_name**
> DeleteSnippetResponseDto snippets_controller_delete_snippet_by_name(delete_snippet_request_dto)

Delete snippet

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_snippet_request_dto import DeleteSnippetRequestDto
from supn_remnawave_panel.models.delete_snippet_response_dto import DeleteSnippetResponseDto
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
    api_instance = supn_remnawave_panel.SnippetsControllerApi(api_client)
    delete_snippet_request_dto = supn_remnawave_panel.DeleteSnippetRequestDto() # DeleteSnippetRequestDto | 

    try:
        # Delete snippet
        api_response = await api_instance.snippets_controller_delete_snippet_by_name(delete_snippet_request_dto)
        print("The response of SnippetsControllerApi->snippets_controller_delete_snippet_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetsControllerApi->snippets_controller_delete_snippet_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_snippet_request_dto** | [**DeleteSnippetRequestDto**](DeleteSnippetRequestDto.md)|  | 

### Return type

[**DeleteSnippetResponseDto**](DeleteSnippetResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Snippet deleted successfully |  -  |
**400** | Validation error |  -  |
**404** | Snippet not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snippets_controller_get_snippets**
> GetSnippetsResponseDto snippets_controller_get_snippets()

Get snippets

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_snippets_response_dto import GetSnippetsResponseDto
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
    api_instance = supn_remnawave_panel.SnippetsControllerApi(api_client)

    try:
        # Get snippets
        api_response = await api_instance.snippets_controller_get_snippets()
        print("The response of SnippetsControllerApi->snippets_controller_get_snippets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetsControllerApi->snippets_controller_get_snippets: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSnippetsResponseDto**](GetSnippetsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Snippets retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snippets_controller_update_snippet**
> UpdateSnippetResponseDto snippets_controller_update_snippet(update_snippet_request_dto)

Update snippet

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.update_snippet_request_dto import UpdateSnippetRequestDto
from supn_remnawave_panel.models.update_snippet_response_dto import UpdateSnippetResponseDto
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
    api_instance = supn_remnawave_panel.SnippetsControllerApi(api_client)
    update_snippet_request_dto = supn_remnawave_panel.UpdateSnippetRequestDto() # UpdateSnippetRequestDto | 

    try:
        # Update snippet
        api_response = await api_instance.snippets_controller_update_snippet(update_snippet_request_dto)
        print("The response of SnippetsControllerApi->snippets_controller_update_snippet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetsControllerApi->snippets_controller_update_snippet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_snippet_request_dto** | [**UpdateSnippetRequestDto**](UpdateSnippetRequestDto.md)|  | 

### Return type

[**UpdateSnippetResponseDto**](UpdateSnippetResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Snippet updated successfully |  -  |
**400** | Validation error |  -  |
**404** | Snippet not found |  -  |
**409** | Snippet name already exists. |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

