# supn_remnawave_panel.UsersControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_controller_create_user**](UsersControllerApi.md#users_controller_create_user) | **POST** /api/users | Create a new user
[**users_controller_delete_user**](UsersControllerApi.md#users_controller_delete_user) | **DELETE** /api/users/{uuid} | Delete user
[**users_controller_disable_user**](UsersControllerApi.md#users_controller_disable_user) | **POST** /api/users/{uuid}/actions/disable | Disable user
[**users_controller_enable_user**](UsersControllerApi.md#users_controller_enable_user) | **POST** /api/users/{uuid}/actions/enable | Enable user
[**users_controller_get_all_tags**](UsersControllerApi.md#users_controller_get_all_tags) | **GET** /api/users/tags | Get all existing user tags
[**users_controller_get_all_users**](UsersControllerApi.md#users_controller_get_all_users) | **GET** /api/users | Get all users
[**users_controller_get_user_accessible_nodes**](UsersControllerApi.md#users_controller_get_user_accessible_nodes) | **GET** /api/users/{uuid}/accessible-nodes | Get user accessible nodes
[**users_controller_get_user_by_id**](UsersControllerApi.md#users_controller_get_user_by_id) | **GET** /api/users/by-id/{id} | Get user by ID
[**users_controller_get_user_by_short_uuid**](UsersControllerApi.md#users_controller_get_user_by_short_uuid) | **GET** /api/users/by-short-uuid/{shortUuid} | Get user by Short UUID
[**users_controller_get_user_by_telegram_id**](UsersControllerApi.md#users_controller_get_user_by_telegram_id) | **GET** /api/users/by-telegram-id/{telegramId} | Get users by telegram ID
[**users_controller_get_user_by_username**](UsersControllerApi.md#users_controller_get_user_by_username) | **GET** /api/users/by-username/{username} | Get user by username
[**users_controller_get_user_by_uuid**](UsersControllerApi.md#users_controller_get_user_by_uuid) | **GET** /api/users/{uuid} | Get user by UUID
[**users_controller_get_user_subscription_request_history**](UsersControllerApi.md#users_controller_get_user_subscription_request_history) | **GET** /api/users/{uuid}/subscription-request-history | Get user subscription request history, recent 24 records
[**users_controller_get_users_by_email**](UsersControllerApi.md#users_controller_get_users_by_email) | **GET** /api/users/by-email/{email} | Get users by email
[**users_controller_get_users_by_tag**](UsersControllerApi.md#users_controller_get_users_by_tag) | **GET** /api/users/by-tag/{tag} | Get users by tag
[**users_controller_reset_user_traffic**](UsersControllerApi.md#users_controller_reset_user_traffic) | **POST** /api/users/{uuid}/actions/reset-traffic | Reset user traffic
[**users_controller_resolve_user**](UsersControllerApi.md#users_controller_resolve_user) | **POST** /api/users/resolve | Resolve a user
[**users_controller_revoke_user_subscription**](UsersControllerApi.md#users_controller_revoke_user_subscription) | **POST** /api/users/{uuid}/actions/revoke | Revoke user subscription
[**users_controller_update_user**](UsersControllerApi.md#users_controller_update_user) | **PATCH** /api/users | Update a user by UUID or username


# **users_controller_create_user**
> CreateUserResponseDto users_controller_create_user(create_user_request_dto)

Create a new user

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.create_user_request_dto import CreateUserRequestDto
from supn_remnawave_panel.models.create_user_response_dto import CreateUserResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    create_user_request_dto = supn_remnawave_panel.CreateUserRequestDto() # CreateUserRequestDto | 

    try:
        # Create a new user
        api_response = await api_instance.users_controller_create_user(create_user_request_dto)
        print("The response of UsersControllerApi->users_controller_create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request_dto** | [**CreateUserRequestDto**](CreateUserRequestDto.md)|  | 

### Return type

[**CreateUserResponseDto**](CreateUserResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User created successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_delete_user**
> DeleteUserResponseDto users_controller_delete_user(uuid)

Delete user

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_user_response_dto import DeleteUserResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the user

    try:
        # Delete user
        api_response = await api_instance.users_controller_delete_user(uuid)
        print("The response of UsersControllerApi->users_controller_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the user | 

### Return type

[**DeleteUserResponseDto**](DeleteUserResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User deleted successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_disable_user**
> DisableUserResponseDto users_controller_disable_user(uuid)

Disable user

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.disable_user_response_dto import DisableUserResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the user

    try:
        # Disable user
        api_response = await api_instance.users_controller_disable_user(uuid)
        print("The response of UsersControllerApi->users_controller_disable_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_disable_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the user | 

### Return type

[**DisableUserResponseDto**](DisableUserResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User disabled successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_enable_user**
> EnableUserResponseDto users_controller_enable_user(uuid)

Enable user

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.enable_user_response_dto import EnableUserResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the user

    try:
        # Enable user
        api_response = await api_instance.users_controller_enable_user(uuid)
        print("The response of UsersControllerApi->users_controller_enable_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_enable_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the user | 

### Return type

[**EnableUserResponseDto**](EnableUserResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User enabled successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_get_all_tags**
> GetAllTagsResponseDto users_controller_get_all_tags()

Get all existing user tags

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_all_tags_response_dto import GetAllTagsResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)

    try:
        # Get all existing user tags
        api_response = await api_instance.users_controller_get_all_tags()
        print("The response of UsersControllerApi->users_controller_get_all_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_get_all_tags: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAllTagsResponseDto**](GetAllTagsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tags fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_get_all_users**
> GetAllUsersResponseDto users_controller_get_all_users(size=size, start=start)

Get all users

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_all_users_response_dto import GetAllUsersResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    size = 3.4 # float | Page size for pagination (optional)
    start = 3.4 # float | Offset for pagination (optional)

    try:
        # Get all users
        api_response = await api_instance.users_controller_get_all_users(size=size, start=start)
        print("The response of UsersControllerApi->users_controller_get_all_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_get_all_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **float**| Page size for pagination | [optional] 
 **start** | **float**| Offset for pagination | [optional] 

### Return type

[**GetAllUsersResponseDto**](GetAllUsersResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_get_user_accessible_nodes**
> GetUserAccessibleNodesResponseDto users_controller_get_user_accessible_nodes(uuid)

Get user accessible nodes

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_user_accessible_nodes_response_dto import GetUserAccessibleNodesResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the user

    try:
        # Get user accessible nodes
        api_response = await api_instance.users_controller_get_user_accessible_nodes(uuid)
        print("The response of UsersControllerApi->users_controller_get_user_accessible_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_get_user_accessible_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the user | 

### Return type

[**GetUserAccessibleNodesResponseDto**](GetUserAccessibleNodesResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User accessible nodes fetched successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_get_user_by_id**
> GetUserByIdResponseDto users_controller_get_user_by_id(id)

Get user by ID

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_user_by_id_response_dto import GetUserByIdResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    id = 'id_example' # str | ID of the user

    try:
        # Get user by ID
        api_response = await api_instance.users_controller_get_user_by_id(id)
        print("The response of UsersControllerApi->users_controller_get_user_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_get_user_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the user | 

### Return type

[**GetUserByIdResponseDto**](GetUserByIdResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User fetched successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_get_user_by_short_uuid**
> GetUserByShortUuidResponseDto users_controller_get_user_by_short_uuid(short_uuid)

Get user by Short UUID

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_user_by_short_uuid_response_dto import GetUserByShortUuidResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    short_uuid = 'short_uuid_example' # str | Short UUID of the user

    try:
        # Get user by Short UUID
        api_response = await api_instance.users_controller_get_user_by_short_uuid(short_uuid)
        print("The response of UsersControllerApi->users_controller_get_user_by_short_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_get_user_by_short_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_uuid** | **str**| Short UUID of the user | 

### Return type

[**GetUserByShortUuidResponseDto**](GetUserByShortUuidResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User fetched successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_get_user_by_telegram_id**
> GetUserByTelegramIdResponseDto users_controller_get_user_by_telegram_id(telegram_id)

Get users by telegram ID

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_user_by_telegram_id_response_dto import GetUserByTelegramIdResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    telegram_id = 'telegram_id_example' # str | Telegram ID of the user

    try:
        # Get users by telegram ID
        api_response = await api_instance.users_controller_get_user_by_telegram_id(telegram_id)
        print("The response of UsersControllerApi->users_controller_get_user_by_telegram_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_get_user_by_telegram_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telegram_id** | **str**| Telegram ID of the user | 

### Return type

[**GetUserByTelegramIdResponseDto**](GetUserByTelegramIdResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_get_user_by_username**
> GetUserByUsernameResponseDto users_controller_get_user_by_username(username)

Get user by username

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_user_by_username_response_dto import GetUserByUsernameResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    username = 'username_example' # str | Username of the user

    try:
        # Get user by username
        api_response = await api_instance.users_controller_get_user_by_username(username)
        print("The response of UsersControllerApi->users_controller_get_user_by_username:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_get_user_by_username: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username of the user | 

### Return type

[**GetUserByUsernameResponseDto**](GetUserByUsernameResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User fetched successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_get_user_by_uuid**
> GetUserByUuidResponseDto users_controller_get_user_by_uuid(uuid)

Get user by UUID

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_user_by_uuid_response_dto import GetUserByUuidResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the user

    try:
        # Get user by UUID
        api_response = await api_instance.users_controller_get_user_by_uuid(uuid)
        print("The response of UsersControllerApi->users_controller_get_user_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_get_user_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the user | 

### Return type

[**GetUserByUuidResponseDto**](GetUserByUuidResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User fetched successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_get_user_subscription_request_history**
> GetUserSubscriptionRequestHistoryResponseDto users_controller_get_user_subscription_request_history(uuid)

Get user subscription request history, recent 24 records

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_user_subscription_request_history_response_dto import GetUserSubscriptionRequestHistoryResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the user

    try:
        # Get user subscription request history, recent 24 records
        api_response = await api_instance.users_controller_get_user_subscription_request_history(uuid)
        print("The response of UsersControllerApi->users_controller_get_user_subscription_request_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_get_user_subscription_request_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the user | 

### Return type

[**GetUserSubscriptionRequestHistoryResponseDto**](GetUserSubscriptionRequestHistoryResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User subscription request history fetched successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_get_users_by_email**
> GetUserByEmailResponseDto users_controller_get_users_by_email(email)

Get users by email

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_user_by_email_response_dto import GetUserByEmailResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    email = 'email_example' # str | Email of the user

    try:
        # Get users by email
        api_response = await api_instance.users_controller_get_users_by_email(email)
        print("The response of UsersControllerApi->users_controller_get_users_by_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_get_users_by_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email of the user | 

### Return type

[**GetUserByEmailResponseDto**](GetUserByEmailResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_get_users_by_tag**
> GetUserByTagResponseDto users_controller_get_users_by_tag(tag)

Get users by tag

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_user_by_tag_response_dto import GetUserByTagResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    tag = 'PROMO_1' # str | Tag of the user

    try:
        # Get users by tag
        api_response = await api_instance.users_controller_get_users_by_tag(tag)
        print("The response of UsersControllerApi->users_controller_get_users_by_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_get_users_by_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Tag of the user | 

### Return type

[**GetUserByTagResponseDto**](GetUserByTagResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users fetched successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_reset_user_traffic**
> ResetUserTrafficResponseDto users_controller_reset_user_traffic(uuid)

Reset user traffic

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.reset_user_traffic_response_dto import ResetUserTrafficResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the user

    try:
        # Reset user traffic
        api_response = await api_instance.users_controller_reset_user_traffic(uuid)
        print("The response of UsersControllerApi->users_controller_reset_user_traffic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_reset_user_traffic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the user | 

### Return type

[**ResetUserTrafficResponseDto**](ResetUserTrafficResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User traffic reset successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_resolve_user**
> ResolveUserResponseDto users_controller_resolve_user(resolve_user_request_body_dto)

Resolve a user

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.resolve_user_request_body_dto import ResolveUserRequestBodyDto
from supn_remnawave_panel.models.resolve_user_response_dto import ResolveUserResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    resolve_user_request_body_dto = supn_remnawave_panel.ResolveUserRequestBodyDto() # ResolveUserRequestBodyDto | 

    try:
        # Resolve a user
        api_response = await api_instance.users_controller_resolve_user(resolve_user_request_body_dto)
        print("The response of UsersControllerApi->users_controller_resolve_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_resolve_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolve_user_request_body_dto** | [**ResolveUserRequestBodyDto**](ResolveUserRequestBodyDto.md)|  | 

### Return type

[**ResolveUserResponseDto**](ResolveUserResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User resolved successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_revoke_user_subscription**
> RevokeUserSubscriptionResponseDto users_controller_revoke_user_subscription(uuid, revoke_user_subscription_body_dto)

Revoke user subscription

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.revoke_user_subscription_body_dto import RevokeUserSubscriptionBodyDto
from supn_remnawave_panel.models.revoke_user_subscription_response_dto import RevokeUserSubscriptionResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    uuid = 'uuid_example' # str | UUID of the user
    revoke_user_subscription_body_dto = supn_remnawave_panel.RevokeUserSubscriptionBodyDto() # RevokeUserSubscriptionBodyDto | 

    try:
        # Revoke user subscription
        api_response = await api_instance.users_controller_revoke_user_subscription(uuid, revoke_user_subscription_body_dto)
        print("The response of UsersControllerApi->users_controller_revoke_user_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_revoke_user_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| UUID of the user | 
 **revoke_user_subscription_body_dto** | [**RevokeUserSubscriptionBodyDto**](RevokeUserSubscriptionBodyDto.md)|  | 

### Return type

[**RevokeUserSubscriptionResponseDto**](RevokeUserSubscriptionResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User subscription revoked successfully |  -  |
**400** | Validation error |  -  |
**404** | User not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_controller_update_user**
> UpdateUserResponseDto users_controller_update_user(update_user_request_dto)

Update a user by UUID or username

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.update_user_request_dto import UpdateUserRequestDto
from supn_remnawave_panel.models.update_user_response_dto import UpdateUserResponseDto
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
    api_instance = supn_remnawave_panel.UsersControllerApi(api_client)
    update_user_request_dto = supn_remnawave_panel.UpdateUserRequestDto() # UpdateUserRequestDto | 

    try:
        # Update a user by UUID or username
        api_response = await api_instance.users_controller_update_user(update_user_request_dto)
        print("The response of UsersControllerApi->users_controller_update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersControllerApi->users_controller_update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_user_request_dto** | [**UpdateUserRequestDto**](UpdateUserRequestDto.md)|  | 

### Return type

[**UpdateUserResponseDto**](UpdateUserResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User updated successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

