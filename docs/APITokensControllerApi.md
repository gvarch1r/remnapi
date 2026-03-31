# supn_remnawave_panel.APITokensControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_tokens_controller_create**](APITokensControllerApi.md#api_tokens_controller_create) | **POST** /api/tokens | Create a new API token
[**api_tokens_controller_delete**](APITokensControllerApi.md#api_tokens_controller_delete) | **DELETE** /api/tokens/{uuid} | Delete an API token by UUID
[**api_tokens_controller_find_all**](APITokensControllerApi.md#api_tokens_controller_find_all) | **GET** /api/tokens | Get all API tokens


# **api_tokens_controller_create**
> CreateApiTokenResponseDto api_tokens_controller_create(create_api_token_request_dto)

Create a new API token

This endpoint is forbidden to use via "API-key". It can only be used with an admin JWT-token.

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.create_api_token_request_dto import CreateApiTokenRequestDto
from supn_remnawave_panel.models.create_api_token_response_dto import CreateApiTokenResponseDto
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
    api_instance = supn_remnawave_panel.APITokensControllerApi(api_client)
    create_api_token_request_dto = supn_remnawave_panel.CreateApiTokenRequestDto() # CreateApiTokenRequestDto | 

    try:
        # Create a new API token
        api_response = await api_instance.api_tokens_controller_create(create_api_token_request_dto)
        print("The response of APITokensControllerApi->api_tokens_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APITokensControllerApi->api_tokens_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_api_token_request_dto** | [**CreateApiTokenRequestDto**](CreateApiTokenRequestDto.md)|  | 

### Return type

[**CreateApiTokenResponseDto**](CreateApiTokenResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Token created successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tokens_controller_delete**
> DeleteApiTokenResponseDto api_tokens_controller_delete(uuid)

Delete an API token by UUID

This endpoint is forbidden to use via "API-key". It can be used only with an admin JWT-token.

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_api_token_response_dto import DeleteApiTokenResponseDto
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
    api_instance = supn_remnawave_panel.APITokensControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the API token

    try:
        # Delete an API token by UUID
        api_response = await api_instance.api_tokens_controller_delete(uuid)
        print("The response of APITokensControllerApi->api_tokens_controller_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APITokensControllerApi->api_tokens_controller_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the API token | 

### Return type

[**DeleteApiTokenResponseDto**](DeleteApiTokenResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token deleted successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tokens_controller_find_all**
> FindAllApiTokensResponseDto api_tokens_controller_find_all()

Get all API tokens

This endpoint is forbidden to use via "API-key". It can only be used with admin JWT-token.

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.find_all_api_tokens_response_dto import FindAllApiTokensResponseDto
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
    api_instance = supn_remnawave_panel.APITokensControllerApi(api_client)

    try:
        # Get all API tokens
        api_response = await api_instance.api_tokens_controller_find_all()
        print("The response of APITokensControllerApi->api_tokens_controller_find_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APITokensControllerApi->api_tokens_controller_find_all: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FindAllApiTokensResponseDto**](FindAllApiTokensResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tokens fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

