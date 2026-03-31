# GetExternalSquadsResponseDtoResponseExternalSquadsInnerSubscriptionSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_title** | **str** |  | [optional] 
**support_link** | **str** |  | [optional] 
**profile_update_interval** | **int** |  | [optional] 
**is_profile_webpage_url_enabled** | **bool** |  | [optional] 
**serve_json_at_base_subscription** | **bool** |  | [optional] 
**is_show_custom_remarks** | **bool** |  | [optional] 
**happ_announce** | **str** |  | [optional] 
**happ_routing** | **str** |  | [optional] 
**randomize_hosts** | **bool** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.get_external_squads_response_dto_response_external_squads_inner_subscription_settings import GetExternalSquadsResponseDtoResponseExternalSquadsInnerSubscriptionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of GetExternalSquadsResponseDtoResponseExternalSquadsInnerSubscriptionSettings from a JSON string
get_external_squads_response_dto_response_external_squads_inner_subscription_settings_instance = GetExternalSquadsResponseDtoResponseExternalSquadsInnerSubscriptionSettings.from_json(json)
# print the JSON string representation of the object
print(GetExternalSquadsResponseDtoResponseExternalSquadsInnerSubscriptionSettings.to_json())

# convert the object into a dict
get_external_squads_response_dto_response_external_squads_inner_subscription_settings_dict = get_external_squads_response_dto_response_external_squads_inner_subscription_settings_instance.to_dict()
# create an instance of GetExternalSquadsResponseDtoResponseExternalSquadsInnerSubscriptionSettings from a dict
get_external_squads_response_dto_response_external_squads_inner_subscription_settings_from_dict = GetExternalSquadsResponseDtoResponseExternalSquadsInnerSubscriptionSettings.from_dict(get_external_squads_response_dto_response_external_squads_inner_subscription_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


