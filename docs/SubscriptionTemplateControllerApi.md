# supn_remnawave_panel.SubscriptionTemplateControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscription_template_controller_create_template**](SubscriptionTemplateControllerApi.md#subscription_template_controller_create_template) | **POST** /api/subscription-templates | Create subscription template
[**subscription_template_controller_delete_template**](SubscriptionTemplateControllerApi.md#subscription_template_controller_delete_template) | **DELETE** /api/subscription-templates/{uuid} | Delete subscription template
[**subscription_template_controller_get_all_templates**](SubscriptionTemplateControllerApi.md#subscription_template_controller_get_all_templates) | **GET** /api/subscription-templates | Get all subscription templates (wihout content)
[**subscription_template_controller_get_template_by_uuid**](SubscriptionTemplateControllerApi.md#subscription_template_controller_get_template_by_uuid) | **GET** /api/subscription-templates/{uuid} | Get subscription template by uuid
[**subscription_template_controller_reorder_subscription_templates**](SubscriptionTemplateControllerApi.md#subscription_template_controller_reorder_subscription_templates) | **POST** /api/subscription-templates/actions/reorder | Reorder subscription templates
[**subscription_template_controller_update_template**](SubscriptionTemplateControllerApi.md#subscription_template_controller_update_template) | **PATCH** /api/subscription-templates | Update subscription template


# **subscription_template_controller_create_template**
> CreateSubscriptionTemplateResponseDto subscription_template_controller_create_template(create_subscription_template_request_dto)

Create subscription template

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.create_subscription_template_request_dto import CreateSubscriptionTemplateRequestDto
from supn_remnawave_panel.models.create_subscription_template_response_dto import CreateSubscriptionTemplateResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionTemplateControllerApi(api_client)
    create_subscription_template_request_dto = supn_remnawave_panel.CreateSubscriptionTemplateRequestDto() # CreateSubscriptionTemplateRequestDto | 

    try:
        # Create subscription template
        api_response = await api_instance.subscription_template_controller_create_template(create_subscription_template_request_dto)
        print("The response of SubscriptionTemplateControllerApi->subscription_template_controller_create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionTemplateControllerApi->subscription_template_controller_create_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_subscription_template_request_dto** | [**CreateSubscriptionTemplateRequestDto**](CreateSubscriptionTemplateRequestDto.md)|  | 

### Return type

[**CreateSubscriptionTemplateResponseDto**](CreateSubscriptionTemplateResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template created successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_template_controller_delete_template**
> DeleteSubscriptionTemplateResponseDto subscription_template_controller_delete_template(uuid)

Delete subscription template

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.delete_subscription_template_response_dto import DeleteSubscriptionTemplateResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionTemplateControllerApi(api_client)
    uuid = 'uuid_example' # str | Template UUID

    try:
        # Delete subscription template
        api_response = await api_instance.subscription_template_controller_delete_template(uuid)
        print("The response of SubscriptionTemplateControllerApi->subscription_template_controller_delete_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionTemplateControllerApi->subscription_template_controller_delete_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Template UUID | 

### Return type

[**DeleteSubscriptionTemplateResponseDto**](DeleteSubscriptionTemplateResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template deleted successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_template_controller_get_all_templates**
> GetTemplatesResponseDto subscription_template_controller_get_all_templates()

Get all subscription templates (wihout content)

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_templates_response_dto import GetTemplatesResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionTemplateControllerApi(api_client)

    try:
        # Get all subscription templates (wihout content)
        api_response = await api_instance.subscription_template_controller_get_all_templates()
        print("The response of SubscriptionTemplateControllerApi->subscription_template_controller_get_all_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionTemplateControllerApi->subscription_template_controller_get_all_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetTemplatesResponseDto**](GetTemplatesResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Templates retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_template_controller_get_template_by_uuid**
> GetTemplateResponseDto subscription_template_controller_get_template_by_uuid(uuid)

Get subscription template by uuid

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.get_template_response_dto import GetTemplateResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionTemplateControllerApi(api_client)
    uuid = 'uuid_example' # str | Template UUID

    try:
        # Get subscription template by uuid
        api_response = await api_instance.subscription_template_controller_get_template_by_uuid(uuid)
        print("The response of SubscriptionTemplateControllerApi->subscription_template_controller_get_template_by_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionTemplateControllerApi->subscription_template_controller_get_template_by_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| Template UUID | 

### Return type

[**GetTemplateResponseDto**](GetTemplateResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template retrieved successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_template_controller_reorder_subscription_templates**
> ReorderSubscriptionTemplatesResponseDto subscription_template_controller_reorder_subscription_templates(reorder_subscription_templates_request_dto)

Reorder subscription templates

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.reorder_subscription_templates_request_dto import ReorderSubscriptionTemplatesRequestDto
from supn_remnawave_panel.models.reorder_subscription_templates_response_dto import ReorderSubscriptionTemplatesResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionTemplateControllerApi(api_client)
    reorder_subscription_templates_request_dto = supn_remnawave_panel.ReorderSubscriptionTemplatesRequestDto() # ReorderSubscriptionTemplatesRequestDto | 

    try:
        # Reorder subscription templates
        api_response = await api_instance.subscription_template_controller_reorder_subscription_templates(reorder_subscription_templates_request_dto)
        print("The response of SubscriptionTemplateControllerApi->subscription_template_controller_reorder_subscription_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionTemplateControllerApi->subscription_template_controller_reorder_subscription_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reorder_subscription_templates_request_dto** | [**ReorderSubscriptionTemplatesRequestDto**](ReorderSubscriptionTemplatesRequestDto.md)|  | 

### Return type

[**ReorderSubscriptionTemplatesResponseDto**](ReorderSubscriptionTemplatesResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription templates reordered successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_template_controller_update_template**
> UpdateTemplateResponseDto subscription_template_controller_update_template(update_template_request_dto)

Update subscription template

### Example

* Bearer (JWT) Authentication (Authorization):

```python
import supn_remnawave_panel
from supn_remnawave_panel.models.update_template_request_dto import UpdateTemplateRequestDto
from supn_remnawave_panel.models.update_template_response_dto import UpdateTemplateResponseDto
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
    api_instance = supn_remnawave_panel.SubscriptionTemplateControllerApi(api_client)
    update_template_request_dto = supn_remnawave_panel.UpdateTemplateRequestDto() # UpdateTemplateRequestDto | 

    try:
        # Update subscription template
        api_response = await api_instance.subscription_template_controller_update_template(update_template_request_dto)
        print("The response of SubscriptionTemplateControllerApi->subscription_template_controller_update_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionTemplateControllerApi->subscription_template_controller_update_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_template_request_dto** | [**UpdateTemplateRequestDto**](UpdateTemplateRequestDto.md)|  | 

### Return type

[**UpdateTemplateResponseDto**](UpdateTemplateResponseDto.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template updated successfully |  -  |
**400** | Validation error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

