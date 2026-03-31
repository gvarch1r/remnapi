# UpdateExternalSquadRequestDtoSubscriptionSettings


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
from supn_remnawave_panel.models.update_external_squad_request_dto_subscription_settings import UpdateExternalSquadRequestDtoSubscriptionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExternalSquadRequestDtoSubscriptionSettings from a JSON string
update_external_squad_request_dto_subscription_settings_instance = UpdateExternalSquadRequestDtoSubscriptionSettings.from_json(json)
# print the JSON string representation of the object
print(UpdateExternalSquadRequestDtoSubscriptionSettings.to_json())

# convert the object into a dict
update_external_squad_request_dto_subscription_settings_dict = update_external_squad_request_dto_subscription_settings_instance.to_dict()
# create an instance of UpdateExternalSquadRequestDtoSubscriptionSettings from a dict
update_external_squad_request_dto_subscription_settings_from_dict = UpdateExternalSquadRequestDtoSubscriptionSettings.from_dict(update_external_squad_request_dto_subscription_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


