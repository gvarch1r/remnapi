# RemnawaveWebhookErrorsEventsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**event** | **str** |  | 
**timestamp** | **datetime** |  | 
**data** | [**RemnawaveWebhookErrorsEventsDtoData**](RemnawaveWebhookErrorsEventsDtoData.md) |  | 

## Example

```python
from supn_remnawave_panel.models.remnawave_webhook_errors_events_dto import RemnawaveWebhookErrorsEventsDto

# TODO update the JSON string below
json = "{}"
# create an instance of RemnawaveWebhookErrorsEventsDto from a JSON string
remnawave_webhook_errors_events_dto_instance = RemnawaveWebhookErrorsEventsDto.from_json(json)
# print the JSON string representation of the object
print(RemnawaveWebhookErrorsEventsDto.to_json())

# convert the object into a dict
remnawave_webhook_errors_events_dto_dict = remnawave_webhook_errors_events_dto_instance.to_dict()
# create an instance of RemnawaveWebhookErrorsEventsDto from a dict
remnawave_webhook_errors_events_dto_from_dict = RemnawaveWebhookErrorsEventsDto.from_dict(remnawave_webhook_errors_events_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


