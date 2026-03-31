# RemnawaveWebhookUserHwidDevicesEventsDtoData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**CreateUserResponseDtoResponse**](CreateUserResponseDtoResponse.md) |  | 
**hwid_user_device** | [**GetAllHwidDevicesResponseDtoResponseDevicesInner**](GetAllHwidDevicesResponseDtoResponseDevicesInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.remnawave_webhook_user_hwid_devices_events_dto_data import RemnawaveWebhookUserHwidDevicesEventsDtoData

# TODO update the JSON string below
json = "{}"
# create an instance of RemnawaveWebhookUserHwidDevicesEventsDtoData from a JSON string
remnawave_webhook_user_hwid_devices_events_dto_data_instance = RemnawaveWebhookUserHwidDevicesEventsDtoData.from_json(json)
# print the JSON string representation of the object
print(RemnawaveWebhookUserHwidDevicesEventsDtoData.to_json())

# convert the object into a dict
remnawave_webhook_user_hwid_devices_events_dto_data_dict = remnawave_webhook_user_hwid_devices_events_dto_data_instance.to_dict()
# create an instance of RemnawaveWebhookUserHwidDevicesEventsDtoData from a dict
remnawave_webhook_user_hwid_devices_events_dto_data_from_dict = RemnawaveWebhookUserHwidDevicesEventsDtoData.from_dict(remnawave_webhook_user_hwid_devices_events_dto_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


