# GetSubscriptionSettingsResponseDtoResponseCustomRemarks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expired_users** | **List[str]** |  | 
**limited_users** | **List[str]** |  | 
**disabled_users** | **List[str]** |  | 
**empty_hosts** | **List[str]** |  | 
**hwid_max_devices_exceeded** | **List[str]** |  | 
**hwid_not_supported** | **List[str]** |  | 

## Example

```python
from supn_remnawave_panel.models.get_subscription_settings_response_dto_response_custom_remarks import GetSubscriptionSettingsResponseDtoResponseCustomRemarks

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionSettingsResponseDtoResponseCustomRemarks from a JSON string
get_subscription_settings_response_dto_response_custom_remarks_instance = GetSubscriptionSettingsResponseDtoResponseCustomRemarks.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionSettingsResponseDtoResponseCustomRemarks.to_json())

# convert the object into a dict
get_subscription_settings_response_dto_response_custom_remarks_dict = get_subscription_settings_response_dto_response_custom_remarks_instance.to_dict()
# create an instance of GetSubscriptionSettingsResponseDtoResponseCustomRemarks from a dict
get_subscription_settings_response_dto_response_custom_remarks_from_dict = GetSubscriptionSettingsResponseDtoResponseCustomRemarks.from_dict(get_subscription_settings_response_dto_response_custom_remarks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


