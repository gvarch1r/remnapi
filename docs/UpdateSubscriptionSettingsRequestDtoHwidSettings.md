# UpdateSubscriptionSettingsRequestDtoHwidSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**fallback_device_limit** | **float** |  | 
**max_devices_announce** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.update_subscription_settings_request_dto_hwid_settings import UpdateSubscriptionSettingsRequestDtoHwidSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriptionSettingsRequestDtoHwidSettings from a JSON string
update_subscription_settings_request_dto_hwid_settings_instance = UpdateSubscriptionSettingsRequestDtoHwidSettings.from_json(json)
# print the JSON string representation of the object
print(UpdateSubscriptionSettingsRequestDtoHwidSettings.to_json())

# convert the object into a dict
update_subscription_settings_request_dto_hwid_settings_dict = update_subscription_settings_request_dto_hwid_settings_instance.to_dict()
# create an instance of UpdateSubscriptionSettingsRequestDtoHwidSettings from a dict
update_subscription_settings_request_dto_hwid_settings_from_dict = UpdateSubscriptionSettingsRequestDtoHwidSettings.from_dict(update_subscription_settings_request_dto_hwid_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


