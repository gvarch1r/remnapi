# supn_remnawave_panel.InfraBillingControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**infra_billing_controller_create_infra_billing_history_record**](InfraBillingControllerApi.md#infra_billing_controller_create_infra_billing_history_record) | **POST** /api/infra-billing/history | Create infra billing history
[**infra_billing_controller_create_infra_billing_node**](InfraBillingControllerApi.md#infra_billing_controller_create_infra_billing_node) | **POST** /api/infra-billing/nodes | Create infra billing node
[**infra_billing_controller_create_infra_provider**](InfraBillingControllerApi.md#infra_billing_controller_create_infra_provider) | **POST** /api/infra-billing/providers | Create infra provider
[**infra_billing_controller_delete_infra_billing_history_record_by_uuid**](InfraBillingControllerApi.md#infra_billing_controller_delete_infra_billing_history_record_by_uuid) | **DELETE** /api/infra-billing/history/{uuid} | Delete infra billing history
[**infra_billing_controller_delete_infra_billing_node_by_uuid**](InfraBillingControllerApi.md#infra_billing_controller_delete_infra_billing_node_by_uuid) | **DELETE** /api/infra-billing/nodes/{uuid} | Delete infra billing node
[**infra_billing_controller_delete_infra_provider_by_uuid**](InfraBillingControllerApi.md#infra_billing_controller_delete_infra_provider_by_uuid) | **DELETE** /api/infra-billing/providers/{uuid} | Delete infra provider by uuid
[**infra_billing_controller_get_billing_nodes**](InfraBillingControllerApi.md#infra_billing_controller_get_billing_nodes) | **GET** /api/infra-billing/nodes | Get infra billing nodes
[**infra_billing_controller_get_infra_billing_history_records**](InfraBillingControllerApi.md#infra_billing_controller_get_infra_billing_history_records) | **GET** /api/infra-billing/history | Get infra billing history
[**infra_billing_controller_get_infra_provider_by_uuid**](InfraBillingControllerApi.md#infra_billing_controller_get_infra_provider_by_uuid) | **GET** /api/infra-billing/providers/{uuid} | Get infra provider by uuid
[**infra_billing_controller_get_infra_providers**](InfraBillingControllerApi.md#infra_billing_controller_get_infra_providers) | **GET** /api/infra-billing/providers | Get all infra providers
[**infra_billing_controller_update_infra_billing_node**](InfraBillingControllerApi.md#infra_billing_controller_update_infra_billing_node) | **PATCH** /api/infra-billing/nodes | Update infra billing nodes
[**infra_billing_controller_update_infra_provider**](InfraBillingControllerApi.md#infra_billing_controller_update_infra_provider) | **PATCH** /api/infra-billing/providers | Update infra provider


# **infra_billing_controller_create_infra_billing_history_record**
> CreateInfraBillingHistoryRecordResponseDto infra_billing_controller_create_infra_billing_history_record(create_infra_billing_history_record_request_dto)

Create infra billing history

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.create_infra_billing_history_record_request_dto import CreateInfraBillingHistoryRecordRequestDto
from supn_remnawave_panel.models.create_infra_billing_history_record_response_dto import CreateInfraBillingHistoryRecordResponseDto
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
    api_instance = supn_remnawave_panel.InfraBillingControllerApi(api_client)
    create_infra_billing_history_record_request_dto = supn_remnawave_panel.CreateInfraBillingHistoryRecordRequestDto() # CreateInfraBillingHistoryRecordRequestDto | 

    try:
        # Create infra billing history
        api_response = await api_instance.infra_billing_controller_create_infra_billing_history_record(create_infra_billing_history_record_request_dto)
        print("The response of InfraBillingControllerApi->infra_billing_controller_create_infra_billing_history_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraBillingControllerApi->infra_billing_controller_create_infra_billing_history_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_infra_billing_history_record_request_dto** | [**CreateInfraBillingHistoryRecordRequestDto**](CreateInfraBillingHistoryRecordRequestDto.md)|  | 

### Return type

[**CreateInfraBillingHistoryRecordResponseDto**](CreateInfraBillingHistoryRecordResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Infra billing history record created successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **infra_billing_controller_create_infra_billing_node**
> CreateInfraBillingNodeResponseDto infra_billing_controller_create_infra_billing_node(create_infra_billing_node_request_dto)

Create infra billing node

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.create_infra_billing_node_request_dto import CreateInfraBillingNodeRequestDto
from supn_remnawave_panel.models.create_infra_billing_node_response_dto import CreateInfraBillingNodeResponseDto
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
    api_instance = supn_remnawave_panel.InfraBillingControllerApi(api_client)
    create_infra_billing_node_request_dto = supn_remnawave_panel.CreateInfraBillingNodeRequestDto() # CreateInfraBillingNodeRequestDto | 

    try:
        # Create infra billing node
        api_response = await api_instance.infra_billing_controller_create_infra_billing_node(create_infra_billing_node_request_dto)
        print("The response of InfraBillingControllerApi->infra_billing_controller_create_infra_billing_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraBillingControllerApi->infra_billing_controller_create_infra_billing_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_infra_billing_node_request_dto** | [**CreateInfraBillingNodeRequestDto**](CreateInfraBillingNodeRequestDto.md)|  | 

### Return type

[**CreateInfraBillingNodeResponseDto**](CreateInfraBillingNodeResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Infra billing node created successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **infra_billing_controller_create_infra_provider**
> CreateInfraProviderResponseDto infra_billing_controller_create_infra_provider(create_infra_provider_request_dto)

Create infra provider

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.create_infra_provider_request_dto import CreateInfraProviderRequestDto
from supn_remnawave_panel.models.create_infra_provider_response_dto import CreateInfraProviderResponseDto
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
    api_instance = supn_remnawave_panel.InfraBillingControllerApi(api_client)
    create_infra_provider_request_dto = supn_remnawave_panel.CreateInfraProviderRequestDto() # CreateInfraProviderRequestDto | 

    try:
        # Create infra provider
        api_response = await api_instance.infra_billing_controller_create_infra_provider(create_infra_provider_request_dto)
        print("The response of InfraBillingControllerApi->infra_billing_controller_create_infra_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraBillingControllerApi->infra_billing_controller_create_infra_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_infra_provider_request_dto** | [**CreateInfraProviderRequestDto**](CreateInfraProviderRequestDto.md)|  | 

### Return type

[**CreateInfraProviderResponseDto**](CreateInfraProviderResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Infra provider created successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **infra_billing_controller_delete_infra_billing_history_record_by_uuid**
> DeleteInfraBillingHistoryRecordByUuidResponseDto infra_billing_controller_delete_infra_billing_history_record_by_uuid(uuid)

Delete infra billing history

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_infra_billing_history_record_by_uuid_response_dto import DeleteInfraBillingHistoryRecordByUuidResponseDto
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
    api_instance = supn_remnawave_panel.InfraBillingControllerApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Delete infra billing history
        api_response = await api_instance.infra_billing_controller_delete_infra_billing_history_record_by_uuid(uuid)
        print("The response of InfraBillingControllerApi->infra_billing_controller_delete_infra_billing_history_record_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraBillingControllerApi->infra_billing_controller_delete_infra_billing_history_record_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**DeleteInfraBillingHistoryRecordByUuidResponseDto**](DeleteInfraBillingHistoryRecordByUuidResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Infra billing history record deleted successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **infra_billing_controller_delete_infra_billing_node_by_uuid**
> DeleteInfraBillingNodeByUuidResponseDto infra_billing_controller_delete_infra_billing_node_by_uuid(uuid)

Delete infra billing node

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_infra_billing_node_by_uuid_response_dto import DeleteInfraBillingNodeByUuidResponseDto
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
    api_instance = supn_remnawave_panel.InfraBillingControllerApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Delete infra billing node
        api_response = await api_instance.infra_billing_controller_delete_infra_billing_node_by_uuid(uuid)
        print("The response of InfraBillingControllerApi->infra_billing_controller_delete_infra_billing_node_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraBillingControllerApi->infra_billing_controller_delete_infra_billing_node_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**DeleteInfraBillingNodeByUuidResponseDto**](DeleteInfraBillingNodeByUuidResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Infra billing node deleted successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **infra_billing_controller_delete_infra_provider_by_uuid**
> DeleteInfraProviderByUuidResponseDto infra_billing_controller_delete_infra_provider_by_uuid(uuid)

Delete infra provider by uuid

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_infra_provider_by_uuid_response_dto import DeleteInfraProviderByUuidResponseDto
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
    api_instance = supn_remnawave_panel.InfraBillingControllerApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Delete infra provider by uuid
        api_response = await api_instance.infra_billing_controller_delete_infra_provider_by_uuid(uuid)
        print("The response of InfraBillingControllerApi->infra_billing_controller_delete_infra_provider_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraBillingControllerApi->infra_billing_controller_delete_infra_provider_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**DeleteInfraProviderByUuidResponseDto**](DeleteInfraProviderByUuidResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Infra provider deleted successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **infra_billing_controller_get_billing_nodes**
> GetInfraBillingNodesResponseDto infra_billing_controller_get_billing_nodes()

Get infra billing nodes

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_infra_billing_nodes_response_dto import GetInfraBillingNodesResponseDto
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
    api_instance = supn_remnawave_panel.InfraBillingControllerApi(api_client)

    try:
        # Get infra billing nodes
        api_response = await api_instance.infra_billing_controller_get_billing_nodes()
        print("The response of InfraBillingControllerApi->infra_billing_controller_get_billing_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraBillingControllerApi->infra_billing_controller_get_billing_nodes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetInfraBillingNodesResponseDto**](GetInfraBillingNodesResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Infra billing nodes retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **infra_billing_controller_get_infra_billing_history_records**
> GetInfraBillingHistoryRecordsResponseDto infra_billing_controller_get_infra_billing_history_records()

Get infra billing history

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_infra_billing_history_records_response_dto import GetInfraBillingHistoryRecordsResponseDto
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
    api_instance = supn_remnawave_panel.InfraBillingControllerApi(api_client)

    try:
        # Get infra billing history
        api_response = await api_instance.infra_billing_controller_get_infra_billing_history_records()
        print("The response of InfraBillingControllerApi->infra_billing_controller_get_infra_billing_history_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraBillingControllerApi->infra_billing_controller_get_infra_billing_history_records: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetInfraBillingHistoryRecordsResponseDto**](GetInfraBillingHistoryRecordsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Infra billing history records retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **infra_billing_controller_get_infra_provider_by_uuid**
> GetInfraProviderByUuidResponseDto infra_billing_controller_get_infra_provider_by_uuid(uuid)

Get infra provider by uuid

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_infra_provider_by_uuid_response_dto import GetInfraProviderByUuidResponseDto
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
    api_instance = supn_remnawave_panel.InfraBillingControllerApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Get infra provider by uuid
        api_response = await api_instance.infra_billing_controller_get_infra_provider_by_uuid(uuid)
        print("The response of InfraBillingControllerApi->infra_billing_controller_get_infra_provider_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraBillingControllerApi->infra_billing_controller_get_infra_provider_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**GetInfraProviderByUuidResponseDto**](GetInfraProviderByUuidResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Infra provider retrieved successfully |  -  |
**400** | Validation error |  -  |
**404** | Infra provider not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **infra_billing_controller_get_infra_providers**
> GetInfraProvidersResponseDto infra_billing_controller_get_infra_providers()

Get all infra providers

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_infra_providers_response_dto import GetInfraProvidersResponseDto
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
    api_instance = supn_remnawave_panel.InfraBillingControllerApi(api_client)

    try:
        # Get all infra providers
        api_response = await api_instance.infra_billing_controller_get_infra_providers()
        print("The response of InfraBillingControllerApi->infra_billing_controller_get_infra_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraBillingControllerApi->infra_billing_controller_get_infra_providers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetInfraProvidersResponseDto**](GetInfraProvidersResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Infra providers retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **infra_billing_controller_update_infra_billing_node**
> UpdateInfraBillingNodeResponseDto infra_billing_controller_update_infra_billing_node(update_infra_billing_node_request_dto)

Update infra billing nodes

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.update_infra_billing_node_request_dto import UpdateInfraBillingNodeRequestDto
from supn_remnawave_panel.models.update_infra_billing_node_response_dto import UpdateInfraBillingNodeResponseDto
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
    api_instance = supn_remnawave_panel.InfraBillingControllerApi(api_client)
    update_infra_billing_node_request_dto = supn_remnawave_panel.UpdateInfraBillingNodeRequestDto() # UpdateInfraBillingNodeRequestDto | 

    try:
        # Update infra billing nodes
        api_response = await api_instance.infra_billing_controller_update_infra_billing_node(update_infra_billing_node_request_dto)
        print("The response of InfraBillingControllerApi->infra_billing_controller_update_infra_billing_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraBillingControllerApi->infra_billing_controller_update_infra_billing_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_infra_billing_node_request_dto** | [**UpdateInfraBillingNodeRequestDto**](UpdateInfraBillingNodeRequestDto.md)|  | 

### Return type

[**UpdateInfraBillingNodeResponseDto**](UpdateInfraBillingNodeResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Infra billing node updated successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **infra_billing_controller_update_infra_provider**
> UpdateInfraProviderResponseDto infra_billing_controller_update_infra_provider(update_infra_provider_request_dto)

Update infra provider

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.update_infra_provider_request_dto import UpdateInfraProviderRequestDto
from supn_remnawave_panel.models.update_infra_provider_response_dto import UpdateInfraProviderResponseDto
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
    api_instance = supn_remnawave_panel.InfraBillingControllerApi(api_client)
    update_infra_provider_request_dto = supn_remnawave_panel.UpdateInfraProviderRequestDto() # UpdateInfraProviderRequestDto | 

    try:
        # Update infra provider
        api_response = await api_instance.infra_billing_controller_update_infra_provider(update_infra_provider_request_dto)
        print("The response of InfraBillingControllerApi->infra_billing_controller_update_infra_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfraBillingControllerApi->infra_billing_controller_update_infra_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_infra_provider_request_dto** | [**UpdateInfraProviderRequestDto**](UpdateInfraProviderRequestDto.md)|  | 

### Return type

[**UpdateInfraProviderResponseDto**](UpdateInfraProviderResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Infra provider updated successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

