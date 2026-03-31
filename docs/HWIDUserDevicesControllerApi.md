# supn_remnawave_panel.HWIDUserDevicesControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hwid_user_devices_controller_create_user_hwid_device**](HWIDUserDevicesControllerApi.md#hwid_user_devices_controller_create_user_hwid_device) | **POST** /api/hwid/devices | Create a user HWID device
[**hwid_user_devices_controller_delete_all_user_hwid_devices**](HWIDUserDevicesControllerApi.md#hwid_user_devices_controller_delete_all_user_hwid_devices) | **POST** /api/hwid/devices/delete-all | Delete all user HWID devices
[**hwid_user_devices_controller_delete_user_hwid_device**](HWIDUserDevicesControllerApi.md#hwid_user_devices_controller_delete_user_hwid_device) | **POST** /api/hwid/devices/delete | Delete a user HWID device
[**hwid_user_devices_controller_get_all_users**](HWIDUserDevicesControllerApi.md#hwid_user_devices_controller_get_all_users) | **GET** /api/hwid/devices | Get all HWID devices
[**hwid_user_devices_controller_get_hwid_devices_stats**](HWIDUserDevicesControllerApi.md#hwid_user_devices_controller_get_hwid_devices_stats) | **GET** /api/hwid/devices/stats | Get HWID devices stats
[**hwid_user_devices_controller_get_top_users_by_hwid_devices**](HWIDUserDevicesControllerApi.md#hwid_user_devices_controller_get_top_users_by_hwid_devices) | **GET** /api/hwid/devices/top-users | Get top users by HWID devices
[**hwid_user_devices_controller_get_user_hwid_devices**](HWIDUserDevicesControllerApi.md#hwid_user_devices_controller_get_user_hwid_devices) | **GET** /api/hwid/devices/{userUuid} | Get user HWID devices


# **hwid_user_devices_controller_create_user_hwid_device**
> CreateUserHwidDeviceResponseDto hwid_user_devices_controller_create_user_hwid_device(create_user_hwid_device_request_dto)

Create a user HWID device

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.create_user_hwid_device_request_dto import CreateUserHwidDeviceRequestDto
from supn_remnawave_panel.models.create_user_hwid_device_response_dto import CreateUserHwidDeviceResponseDto
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
    api_instance = supn_remnawave_panel.HWIDUserDevicesControllerApi(api_client)
    create_user_hwid_device_request_dto = supn_remnawave_panel.CreateUserHwidDeviceRequestDto() # CreateUserHwidDeviceRequestDto | 

    try:
        # Create a user HWID device
        api_response = await api_instance.hwid_user_devices_controller_create_user_hwid_device(create_user_hwid_device_request_dto)
        print("The response of HWIDUserDevicesControllerApi->hwid_user_devices_controller_create_user_hwid_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HWIDUserDevicesControllerApi->hwid_user_devices_controller_create_user_hwid_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_hwid_device_request_dto** | [**CreateUserHwidDeviceRequestDto**](CreateUserHwidDeviceRequestDto.md)|  | 

### Return type

[**CreateUserHwidDeviceResponseDto**](CreateUserHwidDeviceResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User HWID device created successfully |  -  |
**400** | Validation error |  -  |
**404** | One of requested resources not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hwid_user_devices_controller_delete_all_user_hwid_devices**
> DeleteAllUserHwidDevicesResponseDto hwid_user_devices_controller_delete_all_user_hwid_devices(delete_all_user_hwid_devices_request_dto)

Delete all user HWID devices

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_all_user_hwid_devices_request_dto import DeleteAllUserHwidDevicesRequestDto
from supn_remnawave_panel.models.delete_all_user_hwid_devices_response_dto import DeleteAllUserHwidDevicesResponseDto
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
    api_instance = supn_remnawave_panel.HWIDUserDevicesControllerApi(api_client)
    delete_all_user_hwid_devices_request_dto = supn_remnawave_panel.DeleteAllUserHwidDevicesRequestDto() # DeleteAllUserHwidDevicesRequestDto | 

    try:
        # Delete all user HWID devices
        api_response = await api_instance.hwid_user_devices_controller_delete_all_user_hwid_devices(delete_all_user_hwid_devices_request_dto)
        print("The response of HWIDUserDevicesControllerApi->hwid_user_devices_controller_delete_all_user_hwid_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HWIDUserDevicesControllerApi->hwid_user_devices_controller_delete_all_user_hwid_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_all_user_hwid_devices_request_dto** | [**DeleteAllUserHwidDevicesRequestDto**](DeleteAllUserHwidDevicesRequestDto.md)|  | 

### Return type

[**DeleteAllUserHwidDevicesResponseDto**](DeleteAllUserHwidDevicesResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User HWID devices deleted successfully |  -  |
**400** | Validation error |  -  |
**404** | One of requested resources not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hwid_user_devices_controller_delete_user_hwid_device**
> DeleteUserHwidDeviceResponseDto hwid_user_devices_controller_delete_user_hwid_device(delete_user_hwid_device_request_dto)

Delete a user HWID device

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_user_hwid_device_request_dto import DeleteUserHwidDeviceRequestDto
from supn_remnawave_panel.models.delete_user_hwid_device_response_dto import DeleteUserHwidDeviceResponseDto
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
    api_instance = supn_remnawave_panel.HWIDUserDevicesControllerApi(api_client)
    delete_user_hwid_device_request_dto = supn_remnawave_panel.DeleteUserHwidDeviceRequestDto() # DeleteUserHwidDeviceRequestDto | 

    try:
        # Delete a user HWID device
        api_response = await api_instance.hwid_user_devices_controller_delete_user_hwid_device(delete_user_hwid_device_request_dto)
        print("The response of HWIDUserDevicesControllerApi->hwid_user_devices_controller_delete_user_hwid_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HWIDUserDevicesControllerApi->hwid_user_devices_controller_delete_user_hwid_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_user_hwid_device_request_dto** | [**DeleteUserHwidDeviceRequestDto**](DeleteUserHwidDeviceRequestDto.md)|  | 

### Return type

[**DeleteUserHwidDeviceResponseDto**](DeleteUserHwidDeviceResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User HWID device deleted successfully |  -  |
**400** | Validation error |  -  |
**404** | One of requested resources not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hwid_user_devices_controller_get_all_users**
> GetAllHwidDevicesResponseDto hwid_user_devices_controller_get_all_users(size=size, start=start)

Get all HWID devices

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_all_hwid_devices_response_dto import GetAllHwidDevicesResponseDto
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
    api_instance = supn_remnawave_panel.HWIDUserDevicesControllerApi(api_client)
    size = 3.4 # float | Page size for pagination (optional)
    start = 3.4 # float | Offset for pagination (optional)

    try:
        # Get all HWID devices
        api_response = await api_instance.hwid_user_devices_controller_get_all_users(size=size, start=start)
        print("The response of HWIDUserDevicesControllerApi->hwid_user_devices_controller_get_all_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HWIDUserDevicesControllerApi->hwid_user_devices_controller_get_all_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **float**| Page size for pagination | [optional] 
 **start** | **float**| Offset for pagination | [optional] 

### Return type

[**GetAllHwidDevicesResponseDto**](GetAllHwidDevicesResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hwid devices fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hwid_user_devices_controller_get_hwid_devices_stats**
> GetHwidDevicesStatsResponseDto hwid_user_devices_controller_get_hwid_devices_stats()

Get HWID devices stats

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_hwid_devices_stats_response_dto import GetHwidDevicesStatsResponseDto
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
    api_instance = supn_remnawave_panel.HWIDUserDevicesControllerApi(api_client)

    try:
        # Get HWID devices stats
        api_response = await api_instance.hwid_user_devices_controller_get_hwid_devices_stats()
        print("The response of HWIDUserDevicesControllerApi->hwid_user_devices_controller_get_hwid_devices_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HWIDUserDevicesControllerApi->hwid_user_devices_controller_get_hwid_devices_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetHwidDevicesStatsResponseDto**](GetHwidDevicesStatsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hwid devices stats fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hwid_user_devices_controller_get_top_users_by_hwid_devices**
> GetTopUsersByHwidDevicesResponseDto hwid_user_devices_controller_get_top_users_by_hwid_devices(size=size, start=start)

Get top users by HWID devices

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_top_users_by_hwid_devices_response_dto import GetTopUsersByHwidDevicesResponseDto
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
    api_instance = supn_remnawave_panel.HWIDUserDevicesControllerApi(api_client)
    size = 3.4 # float | Page size for pagination (optional)
    start = 3.4 # float | Offset for pagination (optional)

    try:
        # Get top users by HWID devices
        api_response = await api_instance.hwid_user_devices_controller_get_top_users_by_hwid_devices(size=size, start=start)
        print("The response of HWIDUserDevicesControllerApi->hwid_user_devices_controller_get_top_users_by_hwid_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HWIDUserDevicesControllerApi->hwid_user_devices_controller_get_top_users_by_hwid_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **float**| Page size for pagination | [optional] 
 **start** | **float**| Offset for pagination | [optional] 

### Return type

[**GetTopUsersByHwidDevicesResponseDto**](GetTopUsersByHwidDevicesResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Top users by HWID devices fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hwid_user_devices_controller_get_user_hwid_devices**
> GetUserHwidDevicesResponseDto hwid_user_devices_controller_get_user_hwid_devices(user_uuid)

Get user HWID devices

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_user_hwid_devices_response_dto import GetUserHwidDevicesResponseDto
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
    api_instance = supn_remnawave_panel.HWIDUserDevicesControllerApi(api_client)
    user_uuid = 'user_uuid_example' # str | UUID of the user

    try:
        # Get user HWID devices
        api_response = await api_instance.hwid_user_devices_controller_get_user_hwid_devices(user_uuid)
        print("The response of HWIDUserDevicesControllerApi->hwid_user_devices_controller_get_user_hwid_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HWIDUserDevicesControllerApi->hwid_user_devices_controller_get_user_hwid_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_uuid** | **str**| UUID of the user | 

### Return type

[**GetUserHwidDevicesResponseDto**](GetUserHwidDevicesResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User HWID devices fetched successfully |  -  |
**400** | Validation error |  -  |
**404** | One of requested resources not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

