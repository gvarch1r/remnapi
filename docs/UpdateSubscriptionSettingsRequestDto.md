# UpdateSubscriptionSettingsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**profile_title** | **str** |  | [optional] 
**support_link** | **str** |  | [optional] 
**profile_update_interval** | **int** |  | [optional] 
**is_profile_webpage_url_enabled** | **bool** |  | [optional] 
**serve_json_at_base_subscription** | **bool** |  | [optional] 
**happ_announce** | **str** |  | [optional] 
**happ_routing** | **str** |  | [optional] 
**is_show_custom_remarks** | **bool** |  | [optional] 
**custom_remarks** | [**GetSubscriptionSettingsResponseDtoResponseCustomRemarks**](GetSubscriptionSettingsResponseDtoResponseCustomRemarks.md) |  | [optional] 
**custom_response_headers** | **Dict[str, str]** |  | [optional] 
**randomize_hosts** | **bool** |  | [optional] 
**response_rules** | [**DebugSrrMatcherRequestDtoResponseRules**](DebugSrrMatcherRequestDtoResponseRules.md) |  | [optional] 
**hwid_settings** | [**UpdateSubscriptionSettingsRequestDtoHwidSettings**](UpdateSubscriptionSettingsRequestDtoHwidSettings.md) |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.update_subscription_settings_request_dto import UpdateSubscriptionSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriptionSettingsRequestDto from a JSON string
update_subscription_settings_request_dto_instance = UpdateSubscriptionSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateSubscriptionSettingsRequestDto.to_json())

# convert the object into a dict
update_subscription_settings_request_dto_dict = update_subscription_settings_request_dto_instance.to_dict()
# create an instance of UpdateSubscriptionSettingsRequestDto from a dict
update_subscription_settings_request_dto_from_dict = UpdateSubscriptionSettingsRequestDto.from_dict(update_subscription_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


