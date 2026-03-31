# supn_remnawave_panel.PasskeysControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**passkey_controller_delete_passkey**](PasskeysControllerApi.md#passkey_controller_delete_passkey) | **DELETE** /api/passkeys | Delete a passkey by ID
[**passkey_controller_get_active_passkeys**](PasskeysControllerApi.md#passkey_controller_get_active_passkeys) | **GET** /api/passkeys | Get all passkeys
[**passkey_controller_passkey_registration_options**](PasskeysControllerApi.md#passkey_controller_passkey_registration_options) | **GET** /api/passkeys/registration/options | Get registration options for passkey
[**passkey_controller_passkey_registration_verify**](PasskeysControllerApi.md#passkey_controller_passkey_registration_verify) | **POST** /api/passkeys/registration/verify | Verify registration for passkey
[**passkey_controller_update_passkey**](PasskeysControllerApi.md#passkey_controller_update_passkey) | **PATCH** /api/passkeys | Update passkey


# **passkey_controller_delete_passkey**
> DeletePasskeyResponseDto passkey_controller_delete_passkey(delete_passkey_request_dto)

Delete a passkey by ID

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_passkey_request_dto import DeletePasskeyRequestDto
from supn_remnawave_panel.models.delete_passkey_response_dto import DeletePasskeyResponseDto
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
    api_instance = supn_remnawave_panel.PasskeysControllerApi(api_client)
    delete_passkey_request_dto = supn_remnawave_panel.DeletePasskeyRequestDto() # DeletePasskeyRequestDto | 

    try:
        # Delete a passkey by ID
        api_response = await api_instance.passkey_controller_delete_passkey(delete_passkey_request_dto)
        print("The response of PasskeysControllerApi->passkey_controller_delete_passkey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasskeysControllerApi->passkey_controller_delete_passkey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_passkey_request_dto** | [**DeletePasskeyRequestDto**](DeletePasskeyRequestDto.md)|  | 

### Return type

[**DeletePasskeyResponseDto**](DeletePasskeyResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Validation error |  -  |
**500** | Server error |  -  |
**0** | Delete passkey result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **passkey_controller_get_active_passkeys**
> GetAllPasskeysResponseDto passkey_controller_get_active_passkeys()

Get all passkeys

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_all_passkeys_response_dto import GetAllPasskeysResponseDto
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
    api_instance = supn_remnawave_panel.PasskeysControllerApi(api_client)

    try:
        # Get all passkeys
        api_response = await api_instance.passkey_controller_get_active_passkeys()
        print("The response of PasskeysControllerApi->passkey_controller_get_active_passkeys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasskeysControllerApi->passkey_controller_get_active_passkeys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllPasskeysResponseDto**](GetAllPasskeysResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Validation error |  -  |
**500** | Server error |  -  |
**0** | Get all passkeys |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **passkey_controller_passkey_registration_options**
> GetPasskeyRegistrationOptionsResponseDto passkey_controller_passkey_registration_options()

Get registration options for passkey

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_passkey_registration_options_response_dto import GetPasskeyRegistrationOptionsResponseDto
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
    api_instance = supn_remnawave_panel.PasskeysControllerApi(api_client)

    try:
        # Get registration options for passkey
        api_response = await api_instance.passkey_controller_passkey_registration_options()
        print("The response of PasskeysControllerApi->passkey_controller_passkey_registration_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasskeysControllerApi->passkey_controller_passkey_registration_options: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetPasskeyRegistrationOptionsResponseDto**](GetPasskeyRegistrationOptionsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Validation error |  -  |
**500** | Server error |  -  |
**0** | Get passkey registration options |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **passkey_controller_passkey_registration_verify**
> VerifyPasskeyRegistrationResponseDto passkey_controller_passkey_registration_verify(verify_passkey_registration_request_dto)

Verify registration for passkey

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.verify_passkey_registration_request_dto import VerifyPasskeyRegistrationRequestDto
from supn_remnawave_panel.models.verify_passkey_registration_response_dto import VerifyPasskeyRegistrationResponseDto
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
    api_instance = supn_remnawave_panel.PasskeysControllerApi(api_client)
    verify_passkey_registration_request_dto = supn_remnawave_panel.VerifyPasskeyRegistrationRequestDto() # VerifyPasskeyRegistrationRequestDto | 

    try:
        # Verify registration for passkey
        api_response = await api_instance.passkey_controller_passkey_registration_verify(verify_passkey_registration_request_dto)
        print("The response of PasskeysControllerApi->passkey_controller_passkey_registration_verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasskeysControllerApi->passkey_controller_passkey_registration_verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_passkey_registration_request_dto** | [**VerifyPasskeyRegistrationRequestDto**](VerifyPasskeyRegistrationRequestDto.md)|  | 

### Return type

[**VerifyPasskeyRegistrationResponseDto**](VerifyPasskeyRegistrationResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Validation error |  -  |
**500** | Server error |  -  |
**0** | Verify passkey registration result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **passkey_controller_update_passkey**
> UpdatePasskeyResponseDto passkey_controller_update_passkey(update_passkey_request_dto)

Update passkey

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.update_passkey_request_dto import UpdatePasskeyRequestDto
from supn_remnawave_panel.models.update_passkey_response_dto import UpdatePasskeyResponseDto
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
    api_instance = supn_remnawave_panel.PasskeysControllerApi(api_client)
    update_passkey_request_dto = supn_remnawave_panel.UpdatePasskeyRequestDto() # UpdatePasskeyRequestDto | 

    try:
        # Update passkey
        api_response = await api_instance.passkey_controller_update_passkey(update_passkey_request_dto)
        print("The response of PasskeysControllerApi->passkey_controller_update_passkey:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PasskeysControllerApi->passkey_controller_update_passkey: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_passkey_request_dto** | [**UpdatePasskeyRequestDto**](UpdatePasskeyRequestDto.md)|  | 

### Return type

[**UpdatePasskeyResponseDto**](UpdatePasskeyResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Validation error |  -  |
**500** | Server error |  -  |
**0** | Update passkey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

