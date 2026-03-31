# GetSubscriptionSettingsResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**profile_title** | **str** |  | 
**support_link** | **str** |  | 
**profile_update_interval** | **int** |  | 
**is_profile_webpage_url_enabled** | **bool** |  | 
**serve_json_at_base_subscription** | **bool** |  | 
**is_show_custom_remarks** | **bool** |  | 
**custom_remarks** | [**GetSubscriptionSettingsResponseDtoResponseCustomRemarks**](GetSubscriptionSettingsResponseDtoResponseCustomRemarks.md) |  | 
**happ_announce** | **str** |  | 
**happ_routing** | **str** |  | 
**custom_response_headers** | **Dict[str, str]** |  | 
**randomize_hosts** | **bool** |  | 
**response_rules** | [**GetSubscriptionSettingsResponseDtoResponseResponseRules**](GetSubscriptionSettingsResponseDtoResponseResponseRules.md) |  | 
**hwid_settings** | [**GetExternalSquadsResponseDtoResponseExternalSquadsInnerHwidSettings**](GetExternalSquadsResponseDtoResponseExternalSquadsInnerHwidSettings.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from supn_remnawave_panel.models.get_subscription_settings_response_dto_response import GetSubscriptionSettingsResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionSettingsResponseDtoResponse from a JSON string
get_subscription_settings_response_dto_response_instance = GetSubscriptionSettingsResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionSettingsResponseDtoResponse.to_json())

# convert the object into a dict
get_subscription_settings_response_dto_response_dict = get_subscription_settings_response_dto_response_instance.to_dict()
# create an instance of GetSubscriptionSettingsResponseDtoResponse from a dict
get_subscription_settings_response_dto_response_from_dict = GetSubscriptionSettingsResponseDtoResponse.from_dict(get_subscription_settings_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


