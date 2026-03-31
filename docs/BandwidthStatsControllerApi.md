# supn_remnawave_panel.BandwidthStatsControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bandwidth_stats_nodes_controller_get_node_user_usage**](BandwidthStatsControllerApi.md#bandwidth_stats_nodes_controller_get_node_user_usage) | **GET** /api/bandwidth-stats/nodes/{uuid}/users/legacy | Get Node User Usage by Range and Node UUID (Legacy)
[**bandwidth_stats_nodes_controller_get_stats_node_users_usage**](BandwidthStatsControllerApi.md#bandwidth_stats_nodes_controller_get_stats_node_users_usage) | **GET** /api/bandwidth-stats/nodes/{uuid}/users | Get Node Users Usage by Node UUID
[**bandwidth_stats_users_controller_get_stats_nodes_usage**](BandwidthStatsControllerApi.md#bandwidth_stats_users_controller_get_stats_nodes_usage) | **GET** /api/bandwidth-stats/users/{uuid} | Get User Usage by Range
[**bandwidth_stats_users_controller_get_user_usage_by_range**](BandwidthStatsControllerApi.md#bandwidth_stats_users_controller_get_user_usage_by_range) | **GET** /api/bandwidth-stats/users/{uuid}/legacy | Get User Usage by Range (Legacy)
[**nodes_usage_history_controller_get_stats_nodes_usage**](BandwidthStatsControllerApi.md#nodes_usage_history_controller_get_stats_nodes_usage) | **GET** /api/bandwidth-stats/nodes | Get Nodes Usage by Range


# **bandwidth_stats_nodes_controller_get_node_user_usage**
> GetLegacyStatsNodesUsersUsageResponseDto bandwidth_stats_nodes_controller_get_node_user_usage(start, end, uuid)

Get Node User Usage by Range and Node UUID (Legacy)

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_legacy_stats_nodes_users_usage_response_dto import GetLegacyStatsNodesUsersUsageResponseDto
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
    api_instance = supn_remnawave_panel.BandwidthStatsControllerApi(api_client)
    start = '2013-10-20T19:20:30+01:00' # datetime | Start date
    end = '2013-10-20T19:20:30+01:00' # datetime | End date
    uuid = 'uuid_example' # str | UUID of the node

    try:
        # Get Node User Usage by Range and Node UUID (Legacy)
        api_response = await api_instance.bandwidth_stats_nodes_controller_get_node_user_usage(start, end, uuid)
        print("The response of BandwidthStatsControllerApi->bandwidth_stats_nodes_controller_get_node_user_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BandwidthStatsControllerApi->bandwidth_stats_nodes_controller_get_node_user_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **datetime**| Start date | 
 **end** | **datetime**| End date | 
 **uuid** | **str**| UUID of the node | 

### Return type

[**GetLegacyStatsNodesUsersUsageResponseDto**](GetLegacyStatsNodesUsersUsageResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Nodes users usage by range (legacy) fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bandwidth_stats_nodes_controller_get_stats_node_users_usage**
> GetStatsNodeUsersUsageResponseDto bandwidth_stats_nodes_controller_get_stats_node_users_usage(top_users_limit, start, end, uuid)

Get Node Users Usage by Node UUID

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_stats_node_users_usage_response_dto import GetStatsNodeUsersUsageResponseDto
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
    api_instance = supn_remnawave_panel.BandwidthStatsControllerApi(api_client)
    top_users_limit = 3.4 # float | Limit of top users to return
    start = 'Sat Jan 31 03:00:00 MSK 2026' # date | Start date (YYYY-MM-DD)
    end = 'Thu Jan 01 03:00:00 MSK 2026' # date | End date (YYYY-MM-DD)
    uuid = 'uuid_example' # str | UUID of the node

    try:
        # Get Node Users Usage by Node UUID
        api_response = await api_instance.bandwidth_stats_nodes_controller_get_stats_node_users_usage(top_users_limit, start, end, uuid)
        print("The response of BandwidthStatsControllerApi->bandwidth_stats_nodes_controller_get_stats_node_users_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BandwidthStatsControllerApi->bandwidth_stats_nodes_controller_get_stats_node_users_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **top_users_limit** | **float**| Limit of top users to return | 
 **start** | **date**| Start date (YYYY-MM-DD) | 
 **end** | **date**| End date (YYYY-MM-DD) | 
 **uuid** | **str**| UUID of the node | 

### Return type

[**GetStatsNodeUsersUsageResponseDto**](GetStatsNodeUsersUsageResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stats node users usage fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bandwidth_stats_users_controller_get_stats_nodes_usage**
> GetStatsUserUsageResponseDto bandwidth_stats_users_controller_get_stats_nodes_usage(top_nodes_limit, start, end, uuid)

Get User Usage by Range

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_stats_user_usage_response_dto import GetStatsUserUsageResponseDto
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
    api_instance = supn_remnawave_panel.BandwidthStatsControllerApi(api_client)
    top_nodes_limit = 3.4 # float | Limit of top nodes to return
    start = 'Sat Jan 31 03:00:00 MSK 2026' # date | Start date (YYYY-MM-DD)
    end = 'Thu Jan 01 03:00:00 MSK 2026' # date | End date (YYYY-MM-DD)
    uuid = 'uuid_example' # str | UUID of the user

    try:
        # Get User Usage by Range
        api_response = await api_instance.bandwidth_stats_users_controller_get_stats_nodes_usage(top_nodes_limit, start, end, uuid)
        print("The response of BandwidthStatsControllerApi->bandwidth_stats_users_controller_get_stats_nodes_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BandwidthStatsControllerApi->bandwidth_stats_users_controller_get_stats_nodes_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **top_nodes_limit** | **float**| Limit of top nodes to return | 
 **start** | **date**| Start date (YYYY-MM-DD) | 
 **end** | **date**| End date (YYYY-MM-DD) | 
 **uuid** | **str**| UUID of the user | 

### Return type

[**GetStatsUserUsageResponseDto**](GetStatsUserUsageResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stats user usage fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bandwidth_stats_users_controller_get_user_usage_by_range**
> GetLegacyStatsUserUsageResponseDto bandwidth_stats_users_controller_get_user_usage_by_range(start, end, uuid)

Get User Usage by Range (Legacy)

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_legacy_stats_user_usage_response_dto import GetLegacyStatsUserUsageResponseDto
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
    api_instance = supn_remnawave_panel.BandwidthStatsControllerApi(api_client)
    start = '2013-10-20T19:20:30+01:00' # datetime | Start date
    end = '2013-10-20T19:20:30+01:00' # datetime | End date
    uuid = 'uuid_example' # str | UUID of the user

    try:
        # Get User Usage by Range (Legacy)
        api_response = await api_instance.bandwidth_stats_users_controller_get_user_usage_by_range(start, end, uuid)
        print("The response of BandwidthStatsControllerApi->bandwidth_stats_users_controller_get_user_usage_by_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BandwidthStatsControllerApi->bandwidth_stats_users_controller_get_user_usage_by_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **datetime**| Start date | 
 **end** | **datetime**| End date | 
 **uuid** | **str**| UUID of the user | 

### Return type

[**GetLegacyStatsUserUsageResponseDto**](GetLegacyStatsUserUsageResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User usage by range (legacy) fetched successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nodes_usage_history_controller_get_stats_nodes_usage**
> GetStatsNodesUsageResponseDto nodes_usage_history_controller_get_stats_nodes_usage(top_nodes_limit, start, end)

Get Nodes Usage by Range

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_stats_nodes_usage_response_dto import GetStatsNodesUsageResponseDto
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
    api_instance = supn_remnawave_panel.BandwidthStatsControllerApi(api_client)
    top_nodes_limit = 3.4 # float | Limit of top nodes to return
    start = 'Sat Jan 31 03:00:00 MSK 2026' # date | Start date (YYYY-MM-DD)
    end = 'Thu Jan 01 03:00:00 MSK 2026' # date | End date (YYYY-MM-DD)

    try:
        # Get Nodes Usage by Range
        api_response = await api_instance.nodes_usage_history_controller_get_stats_nodes_usage(top_nodes_limit, start, end)
        print("The response of BandwidthStatsControllerApi->nodes_usage_history_controller_get_stats_nodes_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BandwidthStatsControllerApi->nodes_usage_history_controller_get_stats_nodes_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **top_nodes_limit** | **float**| Limit of top nodes to return | 
 **start** | **date**| Start date (YYYY-MM-DD) | 
 **end** | **date**| End date (YYYY-MM-DD) | 

### Return type

[**GetStatsNodesUsageResponseDto**](GetStatsNodesUsageResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stats nodes usage fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

