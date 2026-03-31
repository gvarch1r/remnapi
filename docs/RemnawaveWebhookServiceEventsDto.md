# RemnawaveWebhookServiceEventsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**event** | **str** |  | 
**timestamp** | **datetime** |  | 
**data** | [**RemnawaveWebhookServiceEventsDtoData**](RemnawaveWebhookServiceEventsDtoData.md) |  | 

## Example

```python
from supn_remnawave_panel.models.remnawave_webhook_service_events_dto import RemnawaveWebhookServiceEventsDto

# TODO update the JSON string below
json = "{}"
# create an instance of RemnawaveWebhookServiceEventsDto from a JSON string
remnawave_webhook_service_events_dto_instance = RemnawaveWebhookServiceEventsDto.from_json(json)
# print the JSON string representation of the object
print(RemnawaveWebhookServiceEventsDto.to_json())

# convert the object into a dict
remnawave_webhook_service_events_dto_dict = remnawave_webhook_service_events_dto_instance.to_dict()
# create an instance of RemnawaveWebhookServiceEventsDto from a dict
remnawave_webhook_service_events_dto_from_dict = RemnawaveWebhookServiceEventsDto.from_dict(remnawave_webhook_service_events_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


