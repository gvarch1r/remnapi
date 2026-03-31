# RemnawaveWebhookCrmEventsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**event** | **str** |  | 
**timestamp** | **datetime** |  | 
**data** | [**RemnawaveWebhookCrmEventsDtoData**](RemnawaveWebhookCrmEventsDtoData.md) |  | 

## Example

```python
from supn_remnawave_panel.models.remnawave_webhook_crm_events_dto import RemnawaveWebhookCrmEventsDto

# TODO update the JSON string below
json = "{}"
# create an instance of RemnawaveWebhookCrmEventsDto from a JSON string
remnawave_webhook_crm_events_dto_instance = RemnawaveWebhookCrmEventsDto.from_json(json)
# print the JSON string representation of the object
print(RemnawaveWebhookCrmEventsDto.to_json())

# convert the object into a dict
remnawave_webhook_crm_events_dto_dict = remnawave_webhook_crm_events_dto_instance.to_dict()
# create an instance of RemnawaveWebhookCrmEventsDto from a dict
remnawave_webhook_crm_events_dto_from_dict = RemnawaveWebhookCrmEventsDto.from_dict(remnawave_webhook_crm_events_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


