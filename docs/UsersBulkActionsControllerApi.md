# supn_remnawave_panel.UsersBulkActionsControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_bulk_actions_controller_bulk_all_extend_expiration_date**](UsersBulkActionsControllerApi.md#users_bulk_actions_controller_bulk_all_extend_expiration_date) | **POST** /api/users/bulk/all/extend-expiration-date | Bulk Extend All Users Expiration Date
[**users_bulk_actions_controller_bulk_all_reset_user_traffic**](UsersBulkActionsControllerApi.md#users_bulk_actions_controller_bulk_all_reset_user_traffic) | **POST** /api/users/bulk/all/reset-traffic | Bulk Reset All Users Traffic
[**users_bulk_actions_controller_bulk_delete_users**](UsersBulkActionsControllerApi.md#users_bulk_actions_controller_bulk_delete_users) | **POST** /api/users/bulk/delete | Bulk delete users by UUIDs
[**users_bulk_actions_controller_bulk_delete_users_by_status**](UsersBulkActionsControllerApi.md#users_bulk_actions_controller_bulk_delete_users_by_status) | **POST** /api/users/bulk/delete-by-status | Bulk delete users by status
[**users_bulk_actions_controller_bulk_extend_expiration_date**](UsersBulkActionsControllerApi.md#users_bulk_actions_controller_bulk_extend_expiration_date) | **POST** /api/users/bulk/extend-expiration-date | Bulk Extend Users Expiration Date
[**users_bulk_actions_controller_bulk_reset_user_traffic**](UsersBulkActionsControllerApi.md#users_bulk_actions_controller_bulk_reset_user_traffic) | **POST** /api/users/bulk/reset-traffic | Bulk reset traffic users by UUIDs
[**users_bulk_actions_controller_bulk_revoke_users_subscription**](UsersBulkActionsControllerApi.md#users_bulk_actions_controller_bulk_revoke_users_subscription) | **POST** /api/users/bulk/revoke-subscription | Revoke users subscription by User UUIDs
[**users_bulk_actions_controller_bulk_update_all_users**](UsersBulkActionsControllerApi.md#users_bulk_actions_controller_bulk_update_all_users) | **POST** /api/users/bulk/all/update | Bulk update all users
[**users_bulk_actions_controller_bulk_update_users**](UsersBulkActionsControllerApi.md#users_bulk_actions_controller_bulk_update_users) | **POST** /api/users/bulk/update | Bulk update users by UUIDs
[**users_bulk_actions_controller_bulk_update_users_internal_squads**](UsersBulkActionsControllerApi.md#users_bulk_actions_controller_bulk_update_users_internal_squads) | **POST** /api/users/bulk/update-squads | Bulk update users internal squads by UUIDs


# **users_bulk_actions_controller_bulk_all_extend_expiration_date**
> BulkAllExtendExpirationDateResponseDto users_bulk_actions_controller_bulk_all_extend_expiration_date(bulk_all_extend_expiration_date_request_dto)

Bulk Extend All Users Expiration Date

Bulk extend all users expiration date

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.bulk_all_extend_expiration_date_request_dto import BulkAllExtendExpirationDateRequestDto
from supn_remnawave_panel.models.bulk_all_extend_expiration_date_response_dto import BulkAllExtendExpirationDateResponseDto
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
    api_instance = supn_remnawave_panel.UsersBulkActionsControllerApi(api_client)
    bulk_all_extend_expiration_date_request_dto = supn_remnawave_panel.BulkAllExtendExpirationDateRequestDto() # BulkAllExtendExpirationDateRequestDto | 

    try:
        # Bulk Extend All Users Expiration Date
        api_response = await api_instance.users_bulk_actions_controller_bulk_all_extend_expiration_date(bulk_all_extend_expiration_date_request_dto)
        print("The response of UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_all_extend_expiration_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_all_extend_expiration_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_all_extend_expiration_date_request_dto** | [**BulkAllExtendExpirationDateRequestDto**](BulkAllExtendExpirationDateRequestDto.md)|  | 

### Return type

[**BulkAllExtendExpirationDateResponseDto**](BulkAllExtendExpirationDateResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All users expiration date extended successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_bulk_actions_controller_bulk_all_reset_user_traffic**
> BulkAllResetTrafficUsersResponseDto users_bulk_actions_controller_bulk_all_reset_user_traffic()

Bulk Reset All Users Traffic

Bulk reset all users traffic

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.bulk_all_reset_traffic_users_response_dto import BulkAllResetTrafficUsersResponseDto
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
    api_instance = supn_remnawave_panel.UsersBulkActionsControllerApi(api_client)

    try:
        # Bulk Reset All Users Traffic
        api_response = await api_instance.users_bulk_actions_controller_bulk_all_reset_user_traffic()
        print("The response of UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_all_reset_user_traffic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_all_reset_user_traffic: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BulkAllResetTrafficUsersResponseDto**](BulkAllResetTrafficUsersResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All users traffic reset successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_bulk_actions_controller_bulk_delete_users**
> BulkDeleteUsersResponseDto users_bulk_actions_controller_bulk_delete_users(bulk_delete_users_request_dto)

Bulk delete users by UUIDs

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.bulk_delete_users_request_dto import BulkDeleteUsersRequestDto
from supn_remnawave_panel.models.bulk_delete_users_response_dto import BulkDeleteUsersResponseDto
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
    api_instance = supn_remnawave_panel.UsersBulkActionsControllerApi(api_client)
    bulk_delete_users_request_dto = supn_remnawave_panel.BulkDeleteUsersRequestDto() # BulkDeleteUsersRequestDto | 

    try:
        # Bulk delete users by UUIDs
        api_response = await api_instance.users_bulk_actions_controller_bulk_delete_users(bulk_delete_users_request_dto)
        print("The response of UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_delete_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_delete_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_delete_users_request_dto** | [**BulkDeleteUsersRequestDto**](BulkDeleteUsersRequestDto.md)|  | 

### Return type

[**BulkDeleteUsersResponseDto**](BulkDeleteUsersResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users deleted successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_bulk_actions_controller_bulk_delete_users_by_status**
> BulkDeleteUsersByStatusResponseDto users_bulk_actions_controller_bulk_delete_users_by_status(bulk_delete_users_by_status_request_dto)

Bulk delete users by status

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.bulk_delete_users_by_status_request_dto import BulkDeleteUsersByStatusRequestDto
from supn_remnawave_panel.models.bulk_delete_users_by_status_response_dto import BulkDeleteUsersByStatusResponseDto
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
    api_instance = supn_remnawave_panel.UsersBulkActionsControllerApi(api_client)
    bulk_delete_users_by_status_request_dto = supn_remnawave_panel.BulkDeleteUsersByStatusRequestDto() # BulkDeleteUsersByStatusRequestDto | 

    try:
        # Bulk delete users by status
        api_response = await api_instance.users_bulk_actions_controller_bulk_delete_users_by_status(bulk_delete_users_by_status_request_dto)
        print("The response of UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_delete_users_by_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_delete_users_by_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_delete_users_by_status_request_dto** | [**BulkDeleteUsersByStatusRequestDto**](BulkDeleteUsersByStatusRequestDto.md)|  | 

### Return type

[**BulkDeleteUsersByStatusResponseDto**](BulkDeleteUsersByStatusResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users deleted successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_bulk_actions_controller_bulk_extend_expiration_date**
> BulkExtendExpirationDateResponseDto users_bulk_actions_controller_bulk_extend_expiration_date(bulk_extend_expiration_date_request_dto)

Bulk Extend Users Expiration Date

Bulk extend all users expiration date

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.bulk_extend_expiration_date_request_dto import BulkExtendExpirationDateRequestDto
from supn_remnawave_panel.models.bulk_extend_expiration_date_response_dto import BulkExtendExpirationDateResponseDto
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
    api_instance = supn_remnawave_panel.UsersBulkActionsControllerApi(api_client)
    bulk_extend_expiration_date_request_dto = supn_remnawave_panel.BulkExtendExpirationDateRequestDto() # BulkExtendExpirationDateRequestDto | 

    try:
        # Bulk Extend Users Expiration Date
        api_response = await api_instance.users_bulk_actions_controller_bulk_extend_expiration_date(bulk_extend_expiration_date_request_dto)
        print("The response of UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_extend_expiration_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_extend_expiration_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_extend_expiration_date_request_dto** | [**BulkExtendExpirationDateRequestDto**](BulkExtendExpirationDateRequestDto.md)|  | 

### Return type

[**BulkExtendExpirationDateResponseDto**](BulkExtendExpirationDateResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users expiration date extended successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_bulk_actions_controller_bulk_reset_user_traffic**
> BulkResetTrafficUsersResponseDto users_bulk_actions_controller_bulk_reset_user_traffic(bulk_reset_traffic_users_request_dto)

Bulk reset traffic users by UUIDs

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.bulk_reset_traffic_users_request_dto import BulkResetTrafficUsersRequestDto
from supn_remnawave_panel.models.bulk_reset_traffic_users_response_dto import BulkResetTrafficUsersResponseDto
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
    api_instance = supn_remnawave_panel.UsersBulkActionsControllerApi(api_client)
    bulk_reset_traffic_users_request_dto = supn_remnawave_panel.BulkResetTrafficUsersRequestDto() # BulkResetTrafficUsersRequestDto | 

    try:
        # Bulk reset traffic users by UUIDs
        api_response = await api_instance.users_bulk_actions_controller_bulk_reset_user_traffic(bulk_reset_traffic_users_request_dto)
        print("The response of UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_reset_user_traffic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_reset_user_traffic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_reset_traffic_users_request_dto** | [**BulkResetTrafficUsersRequestDto**](BulkResetTrafficUsersRequestDto.md)|  | 

### Return type

[**BulkResetTrafficUsersResponseDto**](BulkResetTrafficUsersResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users traffic reset successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_bulk_actions_controller_bulk_revoke_users_subscription**
> BulkRevokeUsersSubscriptionResponseDto users_bulk_actions_controller_bulk_revoke_users_subscription(bulk_revoke_users_subscription_request_dto)

Revoke users subscription by User UUIDs

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.bulk_revoke_users_subscription_request_dto import BulkRevokeUsersSubscriptionRequestDto
from supn_remnawave_panel.models.bulk_revoke_users_subscription_response_dto import BulkRevokeUsersSubscriptionResponseDto
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
    api_instance = supn_remnawave_panel.UsersBulkActionsControllerApi(api_client)
    bulk_revoke_users_subscription_request_dto = supn_remnawave_panel.BulkRevokeUsersSubscriptionRequestDto() # BulkRevokeUsersSubscriptionRequestDto | 

    try:
        # Revoke users subscription by User UUIDs
        api_response = await api_instance.users_bulk_actions_controller_bulk_revoke_users_subscription(bulk_revoke_users_subscription_request_dto)
        print("The response of UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_revoke_users_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_revoke_users_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_revoke_users_subscription_request_dto** | [**BulkRevokeUsersSubscriptionRequestDto**](BulkRevokeUsersSubscriptionRequestDto.md)|  | 

### Return type

[**BulkRevokeUsersSubscriptionResponseDto**](BulkRevokeUsersSubscriptionResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users subscription revoked successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_bulk_actions_controller_bulk_update_all_users**
> BulkAllUpdateUsersResponseDto users_bulk_actions_controller_bulk_update_all_users(bulk_all_update_users_request_dto)

Bulk update all users

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.bulk_all_update_users_request_dto import BulkAllUpdateUsersRequestDto
from supn_remnawave_panel.models.bulk_all_update_users_response_dto import BulkAllUpdateUsersResponseDto
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
    api_instance = supn_remnawave_panel.UsersBulkActionsControllerApi(api_client)
    bulk_all_update_users_request_dto = supn_remnawave_panel.BulkAllUpdateUsersRequestDto() # BulkAllUpdateUsersRequestDto | 

    try:
        # Bulk update all users
        api_response = await api_instance.users_bulk_actions_controller_bulk_update_all_users(bulk_all_update_users_request_dto)
        print("The response of UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_update_all_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_update_all_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_all_update_users_request_dto** | [**BulkAllUpdateUsersRequestDto**](BulkAllUpdateUsersRequestDto.md)|  | 

### Return type

[**BulkAllUpdateUsersResponseDto**](BulkAllUpdateUsersResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All users updated successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_bulk_actions_controller_bulk_update_users**
> BulkUpdateUsersResponseDto users_bulk_actions_controller_bulk_update_users(bulk_update_users_request_dto)

Bulk update users by UUIDs

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.bulk_update_users_request_dto import BulkUpdateUsersRequestDto
from supn_remnawave_panel.models.bulk_update_users_response_dto import BulkUpdateUsersResponseDto
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
    api_instance = supn_remnawave_panel.UsersBulkActionsControllerApi(api_client)
    bulk_update_users_request_dto = supn_remnawave_panel.BulkUpdateUsersRequestDto() # BulkUpdateUsersRequestDto | 

    try:
        # Bulk update users by UUIDs
        api_response = await api_instance.users_bulk_actions_controller_bulk_update_users(bulk_update_users_request_dto)
        print("The response of UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_update_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_update_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_update_users_request_dto** | [**BulkUpdateUsersRequestDto**](BulkUpdateUsersRequestDto.md)|  | 

### Return type

[**BulkUpdateUsersResponseDto**](BulkUpdateUsersResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users updated successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_bulk_actions_controller_bulk_update_users_internal_squads**
> BulkUpdateUsersSquadsResponseDto users_bulk_actions_controller_bulk_update_users_internal_squads(bulk_update_users_squads_request_dto)

Bulk update users internal squads by UUIDs

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.bulk_update_users_squads_request_dto import BulkUpdateUsersSquadsRequestDto
from supn_remnawave_panel.models.bulk_update_users_squads_response_dto import BulkUpdateUsersSquadsResponseDto
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
    api_instance = supn_remnawave_panel.UsersBulkActionsControllerApi(api_client)
    bulk_update_users_squads_request_dto = supn_remnawave_panel.BulkUpdateUsersSquadsRequestDto() # BulkUpdateUsersSquadsRequestDto | 

    try:
        # Bulk update users internal squads by UUIDs
        api_response = await api_instance.users_bulk_actions_controller_bulk_update_users_internal_squads(bulk_update_users_squads_request_dto)
        print("The response of UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_update_users_internal_squads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersBulkActionsControllerApi->users_bulk_actions_controller_bulk_update_users_internal_squads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_update_users_squads_request_dto** | [**BulkUpdateUsersSquadsRequestDto**](BulkUpdateUsersSquadsRequestDto.md)|  | 

### Return type

[**BulkUpdateUsersSquadsResponseDto**](BulkUpdateUsersSquadsResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Internal squads updated successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

