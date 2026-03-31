# supn_remnawave_panel.KeygenControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keygen_controller_generate_key**](KeygenControllerApi.md#keygen_controller_generate_key) | **GET** /api/keygen | Get SECRET_KEY for Remnawave Node


# **keygen_controller_generate_key**
> GetPubKeyResponseDto keygen_controller_generate_key()

Get SECRET_KEY for Remnawave Node

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_pub_key_response_dto import GetPubKeyResponseDto
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
    api_instance = supn_remnawave_panel.KeygenControllerApi(api_client)

    try:
        # Get SECRET_KEY for Remnawave Node
        api_response = await api_instance.keygen_controller_generate_key()
        print("The response of KeygenControllerApi->keygen_controller_generate_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeygenControllerApi->keygen_controller_generate_key: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetPubKeyResponseDto**](GetPubKeyResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get SECRET_KEY for Remnawave Node |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

