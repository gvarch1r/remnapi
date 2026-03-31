# supn_remnawave_panel.ConfigProfilesControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_profile_controller_create_config_profile**](ConfigProfilesControllerApi.md#config_profile_controller_create_config_profile) | **POST** /api/config-profiles | Create config profile
[**config_profile_controller_delete_config_profile_by_uuid**](ConfigProfilesControllerApi.md#config_profile_controller_delete_config_profile_by_uuid) | **DELETE** /api/config-profiles/{uuid} | Delete config profile
[**config_profile_controller_get_all_inbounds**](ConfigProfilesControllerApi.md#config_profile_controller_get_all_inbounds) | **GET** /api/config-profiles/inbounds | Get all inbounds from all config profiles
[**config_profile_controller_get_computed_config_profile_by_uuid**](ConfigProfilesControllerApi.md#config_profile_controller_get_computed_config_profile_by_uuid) | **GET** /api/config-profiles/{uuid}/computed-config | Get computed config profile by uuid
[**config_profile_controller_get_config_profile_by_uuid**](ConfigProfilesControllerApi.md#config_profile_controller_get_config_profile_by_uuid) | **GET** /api/config-profiles/{uuid} | Get config profile by uuid
[**config_profile_controller_get_config_profiles**](ConfigProfilesControllerApi.md#config_profile_controller_get_config_profiles) | **GET** /api/config-profiles | Get config profiles
[**config_profile_controller_get_inbounds_by_profile_uuid**](ConfigProfilesControllerApi.md#config_profile_controller_get_inbounds_by_profile_uuid) | **GET** /api/config-profiles/{uuid}/inbounds | Get inbounds by profile uuid
[**config_profile_controller_reorder_config_profiles**](ConfigProfilesControllerApi.md#config_profile_controller_reorder_config_profiles) | **POST** /api/config-profiles/actions/reorder | Reorder config profiles
[**config_profile_controller_update_config_profile**](ConfigProfilesControllerApi.md#config_profile_controller_update_config_profile) | **PATCH** /api/config-profiles | Update Core Config in specific config profile


# **config_profile_controller_create_config_profile**
> CreateConfigProfileResponseDto config_profile_controller_create_config_profile(create_config_profile_request_dto)

Create config profile

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.create_config_profile_request_dto import CreateConfigProfileRequestDto
from supn_remnawave_panel.models.create_config_profile_response_dto import CreateConfigProfileResponseDto
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
    api_instance = supn_remnawave_panel.ConfigProfilesControllerApi(api_client)
    create_config_profile_request_dto = supn_remnawave_panel.CreateConfigProfileRequestDto() # CreateConfigProfileRequestDto | 

    try:
        # Create config profile
        api_response = await api_instance.config_profile_controller_create_config_profile(create_config_profile_request_dto)
        print("The response of ConfigProfilesControllerApi->config_profile_controller_create_config_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigProfilesControllerApi->config_profile_controller_create_config_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_config_profile_request_dto** | [**CreateConfigProfileRequestDto**](CreateConfigProfileRequestDto.md)|  | 

### Return type

[**CreateConfigProfileResponseDto**](CreateConfigProfileResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Config profile created successfully |  -  |
**400** | Validation error |  -  |
**409** | Config profile name already exists or inbound tags are not unique. Inbound tags must be unique in global scope. |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_profile_controller_delete_config_profile_by_uuid**
> DeleteConfigProfileResponseDto config_profile_controller_delete_config_profile_by_uuid(uuid)

Delete config profile

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_config_profile_response_dto import DeleteConfigProfileResponseDto
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
    api_instance = supn_remnawave_panel.ConfigProfilesControllerApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Delete config profile
        api_response = await api_instance.config_profile_controller_delete_config_profile_by_uuid(uuid)
        print("The response of ConfigProfilesControllerApi->config_profile_controller_delete_config_profile_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigProfilesControllerApi->config_profile_controller_delete_config_profile_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**DeleteConfigProfileResponseDto**](DeleteConfigProfileResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Config profile deleted successfully |  -  |
**400** | Validation error |  -  |
**404** | Config profile not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_profile_controller_get_all_inbounds**
> GetAllInboundsResponseDto config_profile_controller_get_all_inbounds()

Get all inbounds from all config profiles

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_all_inbounds_response_dto import GetAllInboundsResponseDto
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
    api_instance = supn_remnawave_panel.ConfigProfilesControllerApi(api_client)

    try:
        # Get all inbounds from all config profiles
        api_response = await api_instance.config_profile_controller_get_all_inbounds()
        print("The response of ConfigProfilesControllerApi->config_profile_controller_get_all_inbounds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigProfilesControllerApi->config_profile_controller_get_all_inbounds: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllInboundsResponseDto**](GetAllInboundsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbounds retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_profile_controller_get_computed_config_profile_by_uuid**
> GetComputedConfigProfileByUuidResponseDto config_profile_controller_get_computed_config_profile_by_uuid(uuid)

Get computed config profile by uuid

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_computed_config_profile_by_uuid_response_dto import GetComputedConfigProfileByUuidResponseDto
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
    api_instance = supn_remnawave_panel.ConfigProfilesControllerApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Get computed config profile by uuid
        api_response = await api_instance.config_profile_controller_get_computed_config_profile_by_uuid(uuid)
        print("The response of ConfigProfilesControllerApi->config_profile_controller_get_computed_config_profile_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigProfilesControllerApi->config_profile_controller_get_computed_config_profile_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**GetComputedConfigProfileByUuidResponseDto**](GetComputedConfigProfileByUuidResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Computed config profile retrieved successfully |  -  |
**400** | Validation error |  -  |
**404** | Config profile not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_profile_controller_get_config_profile_by_uuid**
> GetConfigProfileByUuidResponseDto config_profile_controller_get_config_profile_by_uuid(uuid)

Get config profile by uuid

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_config_profile_by_uuid_response_dto import GetConfigProfileByUuidResponseDto
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
    api_instance = supn_remnawave_panel.ConfigProfilesControllerApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Get config profile by uuid
        api_response = await api_instance.config_profile_controller_get_config_profile_by_uuid(uuid)
        print("The response of ConfigProfilesControllerApi->config_profile_controller_get_config_profile_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigProfilesControllerApi->config_profile_controller_get_config_profile_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**GetConfigProfileByUuidResponseDto**](GetConfigProfileByUuidResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Config profile retrieved successfully |  -  |
**400** | Validation error |  -  |
**404** | Config profile not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_profile_controller_get_config_profiles**
> GetConfigProfilesResponseDto config_profile_controller_get_config_profiles()

Get config profiles

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_config_profiles_response_dto import GetConfigProfilesResponseDto
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
    api_instance = supn_remnawave_panel.ConfigProfilesControllerApi(api_client)

    try:
        # Get config profiles
        api_response = await api_instance.config_profile_controller_get_config_profiles()
        print("The response of ConfigProfilesControllerApi->config_profile_controller_get_config_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigProfilesControllerApi->config_profile_controller_get_config_profiles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetConfigProfilesResponseDto**](GetConfigProfilesResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Config profiles retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_profile_controller_get_inbounds_by_profile_uuid**
> GetInboundsByProfileUuidResponseDto config_profile_controller_get_inbounds_by_profile_uuid(uuid)

Get inbounds by profile uuid

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_inbounds_by_profile_uuid_response_dto import GetInboundsByProfileUuidResponseDto
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
    api_instance = supn_remnawave_panel.ConfigProfilesControllerApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Get inbounds by profile uuid
        api_response = await api_instance.config_profile_controller_get_inbounds_by_profile_uuid(uuid)
        print("The response of ConfigProfilesControllerApi->config_profile_controller_get_inbounds_by_profile_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigProfilesControllerApi->config_profile_controller_get_inbounds_by_profile_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**GetInboundsByProfileUuidResponseDto**](GetInboundsByProfileUuidResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Inbounds retrieved successfully |  -  |
**400** | Validation error |  -  |
**404** | Config profile not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_profile_controller_reorder_config_profiles**
> ReorderConfigProfilesResponseDto config_profile_controller_reorder_config_profiles(reorder_config_profiles_request_dto)

Reorder config profiles

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.reorder_config_profiles_request_dto import ReorderConfigProfilesRequestDto
from supn_remnawave_panel.models.reorder_config_profiles_response_dto import ReorderConfigProfilesResponseDto
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
    api_instance = supn_remnawave_panel.ConfigProfilesControllerApi(api_client)
    reorder_config_profiles_request_dto = supn_remnawave_panel.ReorderConfigProfilesRequestDto() # ReorderConfigProfilesRequestDto | 

    try:
        # Reorder config profiles
        api_response = await api_instance.config_profile_controller_reorder_config_profiles(reorder_config_profiles_request_dto)
        print("The response of ConfigProfilesControllerApi->config_profile_controller_reorder_config_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigProfilesControllerApi->config_profile_controller_reorder_config_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reorder_config_profiles_request_dto** | [**ReorderConfigProfilesRequestDto**](ReorderConfigProfilesRequestDto.md)|  | 

### Return type

[**ReorderConfigProfilesResponseDto**](ReorderConfigProfilesResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Config profiles reordered successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_profile_controller_update_config_profile**
> UpdateConfigProfileResponseDto config_profile_controller_update_config_profile(update_config_profile_request_dto)

Update Core Config in specific config profile

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.update_config_profile_request_dto import UpdateConfigProfileRequestDto
from supn_remnawave_panel.models.update_config_profile_response_dto import UpdateConfigProfileResponseDto
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
    api_instance = supn_remnawave_panel.ConfigProfilesControllerApi(api_client)
    update_config_profile_request_dto = supn_remnawave_panel.UpdateConfigProfileRequestDto() # UpdateConfigProfileRequestDto | 

    try:
        # Update Core Config in specific config profile
        api_response = await api_instance.config_profile_controller_update_config_profile(update_config_profile_request_dto)
        print("The response of ConfigProfilesControllerApi->config_profile_controller_update_config_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigProfilesControllerApi->config_profile_controller_update_config_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_config_profile_request_dto** | [**UpdateConfigProfileRequestDto**](UpdateConfigProfileRequestDto.md)|  | 

### Return type

[**UpdateConfigProfileResponseDto**](UpdateConfigProfileResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Config profile updated successfully |  -  |
**400** | Validation error |  -  |
**404** | Config profile not found |  -  |
**409** | Config profile name already exists or inbound tags are not unique. Inbound tags must be unique in global scope. |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

