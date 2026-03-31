# supn_remnawave_panel.IPManagementControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ip_control_controller_drop_connections**](IPManagementControllerApi.md#ip_control_controller_drop_connections) | **POST** /api/ip-control/drop-connections | Drop Connections for Users or IPs
[**ip_control_controller_fetch_user_ips**](IPManagementControllerApi.md#ip_control_controller_fetch_user_ips) | **POST** /api/ip-control/fetch-ips/{uuid} | Request IP List for User
[**ip_control_controller_fetch_users_ips**](IPManagementControllerApi.md#ip_control_controller_fetch_users_ips) | **POST** /api/ip-control/fetch-users-ips/{nodeUuid} | Request Users IPs List for Node
[**ip_control_controller_get_fetch_ips_result**](IPManagementControllerApi.md#ip_control_controller_get_fetch_ips_result) | **GET** /api/ip-control/fetch-ips/result/{jobId} | Get IP List Result by Job ID
[**ip_control_controller_get_fetch_users_ips_result**](IPManagementControllerApi.md#ip_control_controller_get_fetch_users_ips_result) | **GET** /api/ip-control/fetch-users-ips/result/{jobId} | Get Users IPs List Result by Job ID


# **ip_control_controller_drop_connections**
> DropConnectionsResponseDto ip_control_controller_drop_connections(drop_connections_request_dto)

Drop Connections for Users or IPs

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.drop_connections_request_dto import DropConnectionsRequestDto
from supn_remnawave_panel.models.drop_connections_response_dto import DropConnectionsResponseDto
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
    api_instance = supn_remnawave_panel.IPManagementControllerApi(api_client)
    drop_connections_request_dto = supn_remnawave_panel.DropConnectionsRequestDto() # DropConnectionsRequestDto | 

    try:
        # Drop Connections for Users or IPs
        api_response = await api_instance.ip_control_controller_drop_connections(drop_connections_request_dto)
        print("The response of IPManagementControllerApi->ip_control_controller_drop_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPManagementControllerApi->ip_control_controller_drop_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drop_connections_request_dto** | [**DropConnectionsRequestDto**](DropConnectionsRequestDto.md)|  | 

### Return type

[**DropConnectionsResponseDto**](DropConnectionsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event sent to background executor |  -  |
**400** | Validation error |  -  |
**404** | User not found // Connected nodes not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_control_controller_fetch_user_ips**
> FetchIpsResponseDto ip_control_controller_fetch_user_ips(uuid)

Request IP List for User

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.fetch_ips_response_dto import FetchIpsResponseDto
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
    api_instance = supn_remnawave_panel.IPManagementControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the user

    try:
        # Request IP List for User
        api_response = await api_instance.ip_control_controller_fetch_user_ips(uuid)
        print("The response of IPManagementControllerApi->ip_control_controller_fetch_user_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPManagementControllerApi->ip_control_controller_fetch_user_ips: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the user | 

### Return type

[**FetchIpsResponseDto**](FetchIpsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return jobId for further processing |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_control_controller_fetch_users_ips**
> FetchUsersIpsResponseDto ip_control_controller_fetch_users_ips(node_uuid)

Request Users IPs List for Node

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.fetch_users_ips_response_dto import FetchUsersIpsResponseDto
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
    api_instance = supn_remnawave_panel.IPManagementControllerApi(api_client)
    node_uuid = 'node_uuid_example' # str | UUID of the node

    try:
        # Request Users IPs List for Node
        api_response = await api_instance.ip_control_controller_fetch_users_ips(node_uuid)
        print("The response of IPManagementControllerApi->ip_control_controller_fetch_users_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPManagementControllerApi->ip_control_controller_fetch_users_ips: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_uuid** | **str**| UUID of the node | 

### Return type

[**FetchUsersIpsResponseDto**](FetchUsersIpsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return jobId for further processing |  -  |
**400** | Validation error |  -  |
**404** | Node not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_control_controller_get_fetch_ips_result**
> FetchIpsResultResponseDto ip_control_controller_get_fetch_ips_result(job_id)

Get IP List Result by Job ID

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.fetch_ips_result_response_dto import FetchIpsResultResponseDto
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
    api_instance = supn_remnawave_panel.IPManagementControllerApi(api_client)
    job_id = 'job_id_example' # str | Job ID

    try:
        # Get IP List Result by Job ID
        api_response = await api_instance.ip_control_controller_get_fetch_ips_result(job_id)
        print("The response of IPManagementControllerApi->ip_control_controller_get_fetch_ips_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPManagementControllerApi->ip_control_controller_get_fetch_ips_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 

### Return type

[**FetchIpsResultResponseDto**](FetchIpsResultResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return result or status of the job |  -  |
**400** | Validation error |  -  |
**404** | Job not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_control_controller_get_fetch_users_ips_result**
> FetchUsersIpsResultResponseDto ip_control_controller_get_fetch_users_ips_result(job_id)

Get Users IPs List Result by Job ID

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.fetch_users_ips_result_response_dto import FetchUsersIpsResultResponseDto
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
    api_instance = supn_remnawave_panel.IPManagementControllerApi(api_client)
    job_id = 'job_id_example' # str | Job ID

    try:
        # Get Users IPs List Result by Job ID
        api_response = await api_instance.ip_control_controller_get_fetch_users_ips_result(job_id)
        print("The response of IPManagementControllerApi->ip_control_controller_get_fetch_users_ips_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPManagementControllerApi->ip_control_controller_get_fetch_users_ips_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 

### Return type

[**FetchUsersIpsResultResponseDto**](FetchUsersIpsResultResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return result or status of the job |  -  |
**400** | Validation error |  -  |
**404** | Job not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

