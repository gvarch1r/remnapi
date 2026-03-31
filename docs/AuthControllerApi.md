# supn_remnawave_panel.AuthControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_controller_get_status**](AuthControllerApi.md#auth_controller_get_status) | **GET** /api/auth/status | Get the status of the authentication
[**auth_controller_login**](AuthControllerApi.md#auth_controller_login) | **POST** /api/auth/login | Login as superadmin
[**auth_controller_oauth2_authorize**](AuthControllerApi.md#auth_controller_oauth2_authorize) | **POST** /api/auth/oauth2/authorize | Initiate OAuth2 authorization
[**auth_controller_oauth2_callback**](AuthControllerApi.md#auth_controller_oauth2_callback) | **POST** /api/auth/oauth2/callback | Callback from OAuth2
[**auth_controller_passkey_authentication_options**](AuthControllerApi.md#auth_controller_passkey_authentication_options) | **GET** /api/auth/passkey/authentication/options | Get the authentication options for passkey
[**auth_controller_passkey_authentication_verify**](AuthControllerApi.md#auth_controller_passkey_authentication_verify) | **POST** /api/auth/passkey/authentication/verify | Verify the authentication for passkey
[**auth_controller_register**](AuthControllerApi.md#auth_controller_register) | **POST** /api/auth/register | Register as superadmin


# **auth_controller_get_status**
> GetStatusResponseDto auth_controller_get_status()

Get the status of the authentication

### Example


```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_status_response_dto import GetStatusResponseDto
from supn_remnawave_panel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = supn_remnawave_panel.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with supn_remnawave_panel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = supn_remnawave_panel.AuthControllerApi(api_client)

    try:
        # Get the status of the authentication
        api_response = await api_instance.auth_controller_get_status()
        print("The response of AuthControllerApi->auth_controller_get_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthControllerApi->auth_controller_get_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetStatusResponseDto**](GetStatusResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Validation error |  -  |
**500** | Server error |  -  |
**0** | Status of the system |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_controller_login**
> LoginResponseDto auth_controller_login(login_request_dto)

Login as superadmin

### Example


```python
import supn_remnawave_panel
from supn_remnawave_panel.models.login_request_dto import LoginRequestDto
from supn_remnawave_panel.models.login_response_dto import LoginResponseDto
from supn_remnawave_panel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = supn_remnawave_panel.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with supn_remnawave_panel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = supn_remnawave_panel.AuthControllerApi(api_client)
    login_request_dto = supn_remnawave_panel.LoginRequestDto() # LoginRequestDto | 

    try:
        # Login as superadmin
        api_response = await api_instance.auth_controller_login(login_request_dto)
        print("The response of AuthControllerApi->auth_controller_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthControllerApi->auth_controller_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request_dto** | [**LoginRequestDto**](LoginRequestDto.md)|  | 

### Return type

[**LoginResponseDto**](LoginResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Validation error |  -  |
**401** | Unauthorized - Invalid credentials |  -  |
**500** | Server error |  -  |
**0** | Access token for further requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_controller_oauth2_authorize**
> OAuth2AuthorizeResponseDto auth_controller_oauth2_authorize(o_auth2_authorize_request_dto)

Initiate OAuth2 authorization

### Example


```python
import supn_remnawave_panel
from supn_remnawave_panel.models.o_auth2_authorize_request_dto import OAuth2AuthorizeRequestDto
from supn_remnawave_panel.models.o_auth2_authorize_response_dto import OAuth2AuthorizeResponseDto
from supn_remnawave_panel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = supn_remnawave_panel.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with supn_remnawave_panel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = supn_remnawave_panel.AuthControllerApi(api_client)
    o_auth2_authorize_request_dto = supn_remnawave_panel.OAuth2AuthorizeRequestDto() # OAuth2AuthorizeRequestDto | 

    try:
        # Initiate OAuth2 authorization
        api_response = await api_instance.auth_controller_oauth2_authorize(o_auth2_authorize_request_dto)
        print("The response of AuthControllerApi->auth_controller_oauth2_authorize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthControllerApi->auth_controller_oauth2_authorize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth2_authorize_request_dto** | [**OAuth2AuthorizeRequestDto**](OAuth2AuthorizeRequestDto.md)|  | 

### Return type

[**OAuth2AuthorizeResponseDto**](OAuth2AuthorizeResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Validation error |  -  |
**500** | Server error |  -  |
**0** | OAuth2 authorization URL |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_controller_oauth2_callback**
> OAuth2CallbackResponseDto auth_controller_oauth2_callback(o_auth2_callback_request_dto)

Callback from OAuth2

### Example


```python
import supn_remnawave_panel
from supn_remnawave_panel.models.o_auth2_callback_request_dto import OAuth2CallbackRequestDto
from supn_remnawave_panel.models.o_auth2_callback_response_dto import OAuth2CallbackResponseDto
from supn_remnawave_panel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = supn_remnawave_panel.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with supn_remnawave_panel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = supn_remnawave_panel.AuthControllerApi(api_client)
    o_auth2_callback_request_dto = supn_remnawave_panel.OAuth2CallbackRequestDto() # OAuth2CallbackRequestDto | 

    try:
        # Callback from OAuth2
        api_response = await api_instance.auth_controller_oauth2_callback(o_auth2_callback_request_dto)
        print("The response of AuthControllerApi->auth_controller_oauth2_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthControllerApi->auth_controller_oauth2_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth2_callback_request_dto** | [**OAuth2CallbackRequestDto**](OAuth2CallbackRequestDto.md)|  | 

### Return type

[**OAuth2CallbackResponseDto**](OAuth2CallbackResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Validation error |  -  |
**500** | Server error |  -  |
**0** | Access token for further requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_controller_passkey_authentication_options**
> GetPasskeyAuthenticationOptionsResponseDto auth_controller_passkey_authentication_options()

Get the authentication options for passkey

### Example


```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_passkey_authentication_options_response_dto import GetPasskeyAuthenticationOptionsResponseDto
from supn_remnawave_panel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = supn_remnawave_panel.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with supn_remnawave_panel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = supn_remnawave_panel.AuthControllerApi(api_client)

    try:
        # Get the authentication options for passkey
        api_response = await api_instance.auth_controller_passkey_authentication_options()
        print("The response of AuthControllerApi->auth_controller_passkey_authentication_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthControllerApi->auth_controller_passkey_authentication_options: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetPasskeyAuthenticationOptionsResponseDto**](GetPasskeyAuthenticationOptionsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Validation error |  -  |
**500** | Server error |  -  |
**0** | Passkey authentication options |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_controller_passkey_authentication_verify**
> VerifyPasskeyAuthenticationResponseDto auth_controller_passkey_authentication_verify(verify_passkey_authentication_request_dto)

Verify the authentication for passkey

### Example


```python
import supn_remnawave_panel
from supn_remnawave_panel.models.verify_passkey_authentication_request_dto import VerifyPasskeyAuthenticationRequestDto
from supn_remnawave_panel.models.verify_passkey_authentication_response_dto import VerifyPasskeyAuthenticationResponseDto
from supn_remnawave_panel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = supn_remnawave_panel.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with supn_remnawave_panel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = supn_remnawave_panel.AuthControllerApi(api_client)
    verify_passkey_authentication_request_dto = supn_remnawave_panel.VerifyPasskeyAuthenticationRequestDto() # VerifyPasskeyAuthenticationRequestDto | 

    try:
        # Verify the authentication for passkey
        api_response = await api_instance.auth_controller_passkey_authentication_verify(verify_passkey_authentication_request_dto)
        print("The response of AuthControllerApi->auth_controller_passkey_authentication_verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthControllerApi->auth_controller_passkey_authentication_verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_passkey_authentication_request_dto** | [**VerifyPasskeyAuthenticationRequestDto**](VerifyPasskeyAuthenticationRequestDto.md)|  | 

### Return type

[**VerifyPasskeyAuthenticationResponseDto**](VerifyPasskeyAuthenticationResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Validation error |  -  |
**500** | Server error |  -  |
**0** | JWT access token after successful passkey authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_controller_register**
> RegisterResponseDto auth_controller_register(register_request_dto)

Register as superadmin

### Example


```python
import supn_remnawave_panel
from supn_remnawave_panel.models.register_request_dto import RegisterRequestDto
from supn_remnawave_panel.models.register_response_dto import RegisterResponseDto
from supn_remnawave_panel.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = supn_remnawave_panel.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with supn_remnawave_panel.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = supn_remnawave_panel.AuthControllerApi(api_client)
    register_request_dto = supn_remnawave_panel.RegisterRequestDto() # RegisterRequestDto | 

    try:
        # Register as superadmin
        api_response = await api_instance.auth_controller_register(register_request_dto)
        print("The response of AuthControllerApi->auth_controller_register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthControllerApi->auth_controller_register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_request_dto** | [**RegisterRequestDto**](RegisterRequestDto.md)|  | 

### Return type

[**RegisterResponseDto**](RegisterResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Validation error |  -  |
**403** | Forbidden - Registration is not allowed |  -  |
**500** | Server error |  -  |
**0** | Access token for further requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

