# supn_remnawave_panel.NodePluginsControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**node_plugin_controller_clone_node_plugin**](NodePluginsControllerApi.md#node_plugin_controller_clone_node_plugin) | **POST** /api/node-plugins/actions/clone | Clone Node Plugin
[**node_plugin_controller_create_config**](NodePluginsControllerApi.md#node_plugin_controller_create_config) | **POST** /api/node-plugins | Create Node Plugin
[**node_plugin_controller_delete_config**](NodePluginsControllerApi.md#node_plugin_controller_delete_config) | **DELETE** /api/node-plugins/{uuid} | Delete Node Plugin
[**node_plugin_controller_get_all_configs**](NodePluginsControllerApi.md#node_plugin_controller_get_all_configs) | **GET** /api/node-plugins | Get all Node Plugins
[**node_plugin_controller_get_config_by_uuid**](NodePluginsControllerApi.md#node_plugin_controller_get_config_by_uuid) | **GET** /api/node-plugins/{uuid} | Get Node Plugin by uuid
[**node_plugin_controller_plugin_executor**](NodePluginsControllerApi.md#node_plugin_controller_plugin_executor) | **POST** /api/node-plugins/executor | Execute command on node plugins
[**node_plugin_controller_reorder_node_plugins**](NodePluginsControllerApi.md#node_plugin_controller_reorder_node_plugins) | **POST** /api/node-plugins/actions/reorder | Reorder Node Plugins
[**node_plugin_controller_update_config**](NodePluginsControllerApi.md#node_plugin_controller_update_config) | **PATCH** /api/node-plugins | Update Node Plugin
[**torrent_blocker_reports_controller_get_torrent_blocker_reports**](NodePluginsControllerApi.md#torrent_blocker_reports_controller_get_torrent_blocker_reports) | **GET** /api/node-plugins/torrent-blocker | Get Torrent Blocker Reports
[**torrent_blocker_reports_controller_get_torrent_blocker_reports_stats**](NodePluginsControllerApi.md#torrent_blocker_reports_controller_get_torrent_blocker_reports_stats) | **GET** /api/node-plugins/torrent-blocker/stats | Get Torrent Blocker Reports Stats
[**torrent_blocker_reports_controller_truncate_torrent_blocker_reports**](NodePluginsControllerApi.md#torrent_blocker_reports_controller_truncate_torrent_blocker_reports) | **DELETE** /api/node-plugins/torrent-blocker/truncate | Truncate Torrent Blocker Reports


# **node_plugin_controller_clone_node_plugin**
> CloneNodePluginResponseDto node_plugin_controller_clone_node_plugin(clone_node_plugin_request_dto)

Clone Node Plugin

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.clone_node_plugin_request_dto import CloneNodePluginRequestDto
from supn_remnawave_panel.models.clone_node_plugin_response_dto import CloneNodePluginResponseDto
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
    api_instance = supn_remnawave_panel.NodePluginsControllerApi(api_client)
    clone_node_plugin_request_dto = supn_remnawave_panel.CloneNodePluginRequestDto() # CloneNodePluginRequestDto | 

    try:
        # Clone Node Plugin
        api_response = await api_instance.node_plugin_controller_clone_node_plugin(clone_node_plugin_request_dto)
        print("The response of NodePluginsControllerApi->node_plugin_controller_clone_node_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodePluginsControllerApi->node_plugin_controller_clone_node_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clone_node_plugin_request_dto** | [**CloneNodePluginRequestDto**](CloneNodePluginRequestDto.md)|  | 

### Return type

[**CloneNodePluginResponseDto**](CloneNodePluginResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node plugin cloned successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_plugin_controller_create_config**
> CreateNodePluginResponseDto node_plugin_controller_create_config(create_node_plugin_request_dto)

Create Node Plugin

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.create_node_plugin_request_dto import CreateNodePluginRequestDto
from supn_remnawave_panel.models.create_node_plugin_response_dto import CreateNodePluginResponseDto
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
    api_instance = supn_remnawave_panel.NodePluginsControllerApi(api_client)
    create_node_plugin_request_dto = supn_remnawave_panel.CreateNodePluginRequestDto() # CreateNodePluginRequestDto | 

    try:
        # Create Node Plugin
        api_response = await api_instance.node_plugin_controller_create_config(create_node_plugin_request_dto)
        print("The response of NodePluginsControllerApi->node_plugin_controller_create_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodePluginsControllerApi->node_plugin_controller_create_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_node_plugin_request_dto** | [**CreateNodePluginRequestDto**](CreateNodePluginRequestDto.md)|  | 

### Return type

[**CreateNodePluginResponseDto**](CreateNodePluginResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node plugin created successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_plugin_controller_delete_config**
> DeleteNodePluginResponseDto node_plugin_controller_delete_config(uuid)

Delete Node Plugin

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_node_plugin_response_dto import DeleteNodePluginResponseDto
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
    api_instance = supn_remnawave_panel.NodePluginsControllerApi(api_client)
    uuid = 'uuid_example' # str | Node plugin UUID

    try:
        # Delete Node Plugin
        api_response = await api_instance.node_plugin_controller_delete_config(uuid)
        print("The response of NodePluginsControllerApi->node_plugin_controller_delete_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodePluginsControllerApi->node_plugin_controller_delete_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Node plugin UUID | 

### Return type

[**DeleteNodePluginResponseDto**](DeleteNodePluginResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node plugin deleted successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_plugin_controller_get_all_configs**
> GetNodePluginsResponseDto node_plugin_controller_get_all_configs()

Get all Node Plugins

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_node_plugins_response_dto import GetNodePluginsResponseDto
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
    api_instance = supn_remnawave_panel.NodePluginsControllerApi(api_client)

    try:
        # Get all Node Plugins
        api_response = await api_instance.node_plugin_controller_get_all_configs()
        print("The response of NodePluginsControllerApi->node_plugin_controller_get_all_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodePluginsControllerApi->node_plugin_controller_get_all_configs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetNodePluginsResponseDto**](GetNodePluginsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node plugins retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_plugin_controller_get_config_by_uuid**
> GetNodePluginResponseDto node_plugin_controller_get_config_by_uuid(uuid)

Get Node Plugin by uuid

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_node_plugin_response_dto import GetNodePluginResponseDto
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
    api_instance = supn_remnawave_panel.NodePluginsControllerApi(api_client)
    uuid = 'uuid_example' # str | Node plugin UUID

    try:
        # Get Node Plugin by uuid
        api_response = await api_instance.node_plugin_controller_get_config_by_uuid(uuid)
        print("The response of NodePluginsControllerApi->node_plugin_controller_get_config_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodePluginsControllerApi->node_plugin_controller_get_config_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Node plugin UUID | 

### Return type

[**GetNodePluginResponseDto**](GetNodePluginResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node plugin retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_plugin_controller_plugin_executor**
> PluginExecutorResponseDto node_plugin_controller_plugin_executor(plugin_executor_request_dto)

Execute command on node plugins

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.plugin_executor_request_dto import PluginExecutorRequestDto
from supn_remnawave_panel.models.plugin_executor_response_dto import PluginExecutorResponseDto
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
    api_instance = supn_remnawave_panel.NodePluginsControllerApi(api_client)
    plugin_executor_request_dto = supn_remnawave_panel.PluginExecutorRequestDto() # PluginExecutorRequestDto | 

    try:
        # Execute command on node plugins
        api_response = await api_instance.node_plugin_controller_plugin_executor(plugin_executor_request_dto)
        print("The response of NodePluginsControllerApi->node_plugin_controller_plugin_executor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodePluginsControllerApi->node_plugin_controller_plugin_executor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_executor_request_dto** | [**PluginExecutorRequestDto**](PluginExecutorRequestDto.md)|  | 

### Return type

[**PluginExecutorResponseDto**](PluginExecutorResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node plugin cloned successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_plugin_controller_reorder_node_plugins**
> ReorderNodePluginsResponseDto node_plugin_controller_reorder_node_plugins(reorder_node_plugins_request_dto)

Reorder Node Plugins

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.reorder_node_plugins_request_dto import ReorderNodePluginsRequestDto
from supn_remnawave_panel.models.reorder_node_plugins_response_dto import ReorderNodePluginsResponseDto
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
    api_instance = supn_remnawave_panel.NodePluginsControllerApi(api_client)
    reorder_node_plugins_request_dto = supn_remnawave_panel.ReorderNodePluginsRequestDto() # ReorderNodePluginsRequestDto | 

    try:
        # Reorder Node Plugins
        api_response = await api_instance.node_plugin_controller_reorder_node_plugins(reorder_node_plugins_request_dto)
        print("The response of NodePluginsControllerApi->node_plugin_controller_reorder_node_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodePluginsControllerApi->node_plugin_controller_reorder_node_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reorder_node_plugins_request_dto** | [**ReorderNodePluginsRequestDto**](ReorderNodePluginsRequestDto.md)|  | 

### Return type

[**ReorderNodePluginsResponseDto**](ReorderNodePluginsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node plugins reordered successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_plugin_controller_update_config**
> UpdateNodePluginResponseDto node_plugin_controller_update_config(update_node_plugin_request_dto)

Update Node Plugin

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.update_node_plugin_request_dto import UpdateNodePluginRequestDto
from supn_remnawave_panel.models.update_node_plugin_response_dto import UpdateNodePluginResponseDto
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
    api_instance = supn_remnawave_panel.NodePluginsControllerApi(api_client)
    update_node_plugin_request_dto = supn_remnawave_panel.UpdateNodePluginRequestDto() # UpdateNodePluginRequestDto | 

    try:
        # Update Node Plugin
        api_response = await api_instance.node_plugin_controller_update_config(update_node_plugin_request_dto)
        print("The response of NodePluginsControllerApi->node_plugin_controller_update_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodePluginsControllerApi->node_plugin_controller_update_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_node_plugin_request_dto** | [**UpdateNodePluginRequestDto**](UpdateNodePluginRequestDto.md)|  | 

### Return type

[**UpdateNodePluginResponseDto**](UpdateNodePluginResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Node plugin updated successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **torrent_blocker_reports_controller_get_torrent_blocker_reports**
> GetTorrentBlockerReportsResponseDto torrent_blocker_reports_controller_get_torrent_blocker_reports(size=size, start=start)

Get Torrent Blocker Reports

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_torrent_blocker_reports_response_dto import GetTorrentBlockerReportsResponseDto
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
    api_instance = supn_remnawave_panel.NodePluginsControllerApi(api_client)
    size = 3.4 # float | Page size for pagination (optional)
    start = 3.4 # float | Offset for pagination (optional)

    try:
        # Get Torrent Blocker Reports
        api_response = await api_instance.torrent_blocker_reports_controller_get_torrent_blocker_reports(size=size, start=start)
        print("The response of NodePluginsControllerApi->torrent_blocker_reports_controller_get_torrent_blocker_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodePluginsControllerApi->torrent_blocker_reports_controller_get_torrent_blocker_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **float**| Page size for pagination | [optional] 
 **start** | **float**| Offset for pagination | [optional] 

### Return type

[**GetTorrentBlockerReportsResponseDto**](GetTorrentBlockerReportsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Torrent blocker reports fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **torrent_blocker_reports_controller_get_torrent_blocker_reports_stats**
> GetTorrentBlockerReportsStatsResponseDto torrent_blocker_reports_controller_get_torrent_blocker_reports_stats()

Get Torrent Blocker Reports Stats

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_torrent_blocker_reports_stats_response_dto import GetTorrentBlockerReportsStatsResponseDto
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
    api_instance = supn_remnawave_panel.NodePluginsControllerApi(api_client)

    try:
        # Get Torrent Blocker Reports Stats
        api_response = await api_instance.torrent_blocker_reports_controller_get_torrent_blocker_reports_stats()
        print("The response of NodePluginsControllerApi->torrent_blocker_reports_controller_get_torrent_blocker_reports_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodePluginsControllerApi->torrent_blocker_reports_controller_get_torrent_blocker_reports_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetTorrentBlockerReportsStatsResponseDto**](GetTorrentBlockerReportsStatsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Torrent blocker reports stats fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **torrent_blocker_reports_controller_truncate_torrent_blocker_reports**
> TruncateTorrentBlockerReportsResponseDto torrent_blocker_reports_controller_truncate_torrent_blocker_reports()

Truncate Torrent Blocker Reports

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.truncate_torrent_blocker_reports_response_dto import TruncateTorrentBlockerReportsResponseDto
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
    api_instance = supn_remnawave_panel.NodePluginsControllerApi(api_client)

    try:
        # Truncate Torrent Blocker Reports
        api_response = await api_instance.torrent_blocker_reports_controller_truncate_torrent_blocker_reports()
        print("The response of NodePluginsControllerApi->torrent_blocker_reports_controller_truncate_torrent_blocker_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NodePluginsControllerApi->torrent_blocker_reports_controller_truncate_torrent_blocker_reports: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TruncateTorrentBlockerReportsResponseDto**](TruncateTorrentBlockerReportsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Torrent blocker reports truncated successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

