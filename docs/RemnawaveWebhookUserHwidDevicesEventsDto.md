# RemnawaveWebhookUserHwidDevicesEventsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**event** | **str** |  | 
**timestamp** | **datetime** |  | 
**data** | [**RemnawaveWebhookUserHwidDevicesEventsDtoData**](RemnawaveWebhookUserHwidDevicesEventsDtoData.md) |  | 

## Example

```python
from supn_remnawave_panel.models.remnawave_webhook_user_hwid_devices_events_dto import RemnawaveWebhookUserHwidDevicesEventsDto

# TODO update the JSON string below
json = "{}"
# create an instance of RemnawaveWebhookUserHwidDevicesEventsDto from a JSON string
remnawave_webhook_user_hwid_devices_events_dto_instance = RemnawaveWebhookUserHwidDevicesEventsDto.from_json(json)
# print the JSON string representation of the object
print(RemnawaveWebhookUserHwidDevicesEventsDto.to_json())

# convert the object into a dict
remnawave_webhook_user_hwid_devices_events_dto_dict = remnawave_webhook_user_hwid_devices_events_dto_instance.to_dict()
# create an instance of RemnawaveWebhookUserHwidDevicesEventsDto from a dict
remnawave_webhook_user_hwid_devices_events_dto_from_dict = RemnawaveWebhookUserHwidDevicesEventsDto.from_dict(remnawave_webhook_user_hwid_devices_events_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


