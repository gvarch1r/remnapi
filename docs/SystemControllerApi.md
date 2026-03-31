# supn_remnawave_panel.SystemControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_controller_debug_srr_matcher**](SystemControllerApi.md#system_controller_debug_srr_matcher) | **POST** /api/system/testers/srr-matcher | Test SRR Matcher
[**system_controller_encrypt_happ_crypto_link**](SystemControllerApi.md#system_controller_encrypt_happ_crypto_link) | **POST** /api/system/tools/happ/encrypt | Encrypt Happ Crypto Link
[**system_controller_get_bandwidth_stats**](SystemControllerApi.md#system_controller_get_bandwidth_stats) | **GET** /api/system/stats/bandwidth | Get Bandwidth Stats
[**system_controller_get_metadata**](SystemControllerApi.md#system_controller_get_metadata) | **GET** /api/system/metadata | Get Remnawave Information
[**system_controller_get_nodes_metrics**](SystemControllerApi.md#system_controller_get_nodes_metrics) | **GET** /api/system/nodes/metrics | Get Nodes Metrics
[**system_controller_get_nodes_statistics**](SystemControllerApi.md#system_controller_get_nodes_statistics) | **GET** /api/system/stats/nodes | Get Nodes Statistics
[**system_controller_get_recap**](SystemControllerApi.md#system_controller_get_recap) | **GET** /api/system/stats/recap | Get Recap
[**system_controller_get_remnawave_health**](SystemControllerApi.md#system_controller_get_remnawave_health) | **GET** /api/system/health | Get Remnawave Health
[**system_controller_get_stats**](SystemControllerApi.md#system_controller_get_stats) | **GET** /api/system/stats | Get Stats
[**system_controller_get_x25519_keypairs**](SystemControllerApi.md#system_controller_get_x25519_keypairs) | **GET** /api/system/tools/x25519/generate | Generate 30 X25519 keypairs


# **system_controller_debug_srr_matcher**
> DebugSrrMatcherResponseDto system_controller_debug_srr_matcher(debug_srr_matcher_request_dto)

Test SRR Matcher

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.debug_srr_matcher_request_dto import DebugSrrMatcherRequestDto
from supn_remnawave_panel.models.debug_srr_matcher_response_dto import DebugSrrMatcherResponseDto
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
    api_instance = supn_remnawave_panel.SystemControllerApi(api_client)
    debug_srr_matcher_request_dto = supn_remnawave_panel.DebugSrrMatcherRequestDto() # DebugSrrMatcherRequestDto | 

    try:
        # Test SRR Matcher
        api_response = await api_instance.system_controller_debug_srr_matcher(debug_srr_matcher_request_dto)
        print("The response of SystemControllerApi->system_controller_debug_srr_matcher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemControllerApi->system_controller_debug_srr_matcher: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debug_srr_matcher_request_dto** | [**DebugSrrMatcherRequestDto**](DebugSrrMatcherRequestDto.md)|  | 

### Return type

[**DebugSrrMatcherResponseDto**](DebugSrrMatcherResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Debug SRR matcher information |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_controller_encrypt_happ_crypto_link**
> EncryptHappCryptoLinkResponseDto system_controller_encrypt_happ_crypto_link(encrypt_happ_crypto_link_request_dto)

Encrypt Happ Crypto Link

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.encrypt_happ_crypto_link_request_dto import EncryptHappCryptoLinkRequestDto
from supn_remnawave_panel.models.encrypt_happ_crypto_link_response_dto import EncryptHappCryptoLinkResponseDto
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
    api_instance = supn_remnawave_panel.SystemControllerApi(api_client)
    encrypt_happ_crypto_link_request_dto = supn_remnawave_panel.EncryptHappCryptoLinkRequestDto() # EncryptHappCryptoLinkRequestDto | 

    try:
        # Encrypt Happ Crypto Link
        api_response = await api_instance.system_controller_encrypt_happ_crypto_link(encrypt_happ_crypto_link_request_dto)
        print("The response of SystemControllerApi->system_controller_encrypt_happ_crypto_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemControllerApi->system_controller_encrypt_happ_crypto_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encrypt_happ_crypto_link_request_dto** | [**EncryptHappCryptoLinkRequestDto**](EncryptHappCryptoLinkRequestDto.md)|  | 

### Return type

[**EncryptHappCryptoLinkResponseDto**](EncryptHappCryptoLinkResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns encrypted Happ crypto link |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_controller_get_bandwidth_stats**
> GetBandwidthStatsResponseDto system_controller_get_bandwidth_stats()

Get Bandwidth Stats

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_bandwidth_stats_response_dto import GetBandwidthStatsResponseDto
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
    api_instance = supn_remnawave_panel.SystemControllerApi(api_client)

    try:
        # Get Bandwidth Stats
        api_response = await api_instance.system_controller_get_bandwidth_stats()
        print("The response of SystemControllerApi->system_controller_get_bandwidth_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemControllerApi->system_controller_get_bandwidth_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetBandwidthStatsResponseDto**](GetBandwidthStatsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns bandwidth statistics |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_controller_get_metadata**
> GetMetadataResponseDto system_controller_get_metadata()

Get Remnawave Information

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_metadata_response_dto import GetMetadataResponseDto
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
    api_instance = supn_remnawave_panel.SystemControllerApi(api_client)

    try:
        # Get Remnawave Information
        api_response = await api_instance.system_controller_get_metadata()
        print("The response of SystemControllerApi->system_controller_get_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemControllerApi->system_controller_get_metadata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMetadataResponseDto**](GetMetadataResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns system metadata |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_controller_get_nodes_metrics**
> GetNodesMetricsResponseDto system_controller_get_nodes_metrics()

Get Nodes Metrics

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_nodes_metrics_response_dto import GetNodesMetricsResponseDto
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
    api_instance = supn_remnawave_panel.SystemControllerApi(api_client)

    try:
        # Get Nodes Metrics
        api_response = await api_instance.system_controller_get_nodes_metrics()
        print("The response of SystemControllerApi->system_controller_get_nodes_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemControllerApi->system_controller_get_nodes_metrics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetNodesMetricsResponseDto**](GetNodesMetricsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns nodes metrics from Prometheus metrics endpoint |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_controller_get_nodes_statistics**
> GetNodesStatisticsResponseDto system_controller_get_nodes_statistics()

Get Nodes Statistics

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_nodes_statistics_response_dto import GetNodesStatisticsResponseDto
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
    api_instance = supn_remnawave_panel.SystemControllerApi(api_client)

    try:
        # Get Nodes Statistics
        api_response = await api_instance.system_controller_get_nodes_statistics()
        print("The response of SystemControllerApi->system_controller_get_nodes_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemControllerApi->system_controller_get_nodes_statistics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetNodesStatisticsResponseDto**](GetNodesStatisticsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns nodes statistics |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_controller_get_recap**
> GetRecapResponseDto system_controller_get_recap()

Get Recap

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_recap_response_dto import GetRecapResponseDto
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
    api_instance = supn_remnawave_panel.SystemControllerApi(api_client)

    try:
        # Get Recap
        api_response = await api_instance.system_controller_get_recap()
        print("The response of SystemControllerApi->system_controller_get_recap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemControllerApi->system_controller_get_recap: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetRecapResponseDto**](GetRecapResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns system recap |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_controller_get_remnawave_health**
> GetRemnawaveHealthResponseDto system_controller_get_remnawave_health()

Get Remnawave Health

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_remnawave_health_response_dto import GetRemnawaveHealthResponseDto
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
    api_instance = supn_remnawave_panel.SystemControllerApi(api_client)

    try:
        # Get Remnawave Health
        api_response = await api_instance.system_controller_get_remnawave_health()
        print("The response of SystemControllerApi->system_controller_get_remnawave_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemControllerApi->system_controller_get_remnawave_health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetRemnawaveHealthResponseDto**](GetRemnawaveHealthResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Remnawave health |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_controller_get_stats**
> GetStatsResponseDto system_controller_get_stats()

Get Stats

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_stats_response_dto import GetStatsResponseDto
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
    api_instance = supn_remnawave_panel.SystemControllerApi(api_client)

    try:
        # Get Stats
        api_response = await api_instance.system_controller_get_stats()
        print("The response of SystemControllerApi->system_controller_get_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemControllerApi->system_controller_get_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetStatsResponseDto**](GetStatsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns system statistics |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_controller_get_x25519_keypairs**
> GenerateX25519ResponseDto system_controller_get_x25519_keypairs()

Generate 30 X25519 keypairs

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.generate_x25519_response_dto import GenerateX25519ResponseDto
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
    api_instance = supn_remnawave_panel.SystemControllerApi(api_client)

    try:
        # Generate 30 X25519 keypairs
        api_response = await api_instance.system_controller_get_x25519_keypairs()
        print("The response of SystemControllerApi->system_controller_get_x25519_keypairs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemControllerApi->system_controller_get_x25519_keypairs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GenerateX25519ResponseDto**](GenerateX25519ResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns x25519 keypairs |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

