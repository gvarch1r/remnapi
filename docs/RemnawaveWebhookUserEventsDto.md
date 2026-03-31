# RemnawaveWebhookUserEventsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**event** | **str** |  | 
**timestamp** | **datetime** |  | 
**data** | [**CreateUserResponseDtoResponse**](CreateUserResponseDtoResponse.md) |  | 
**meta** | [**RemnawaveWebhookUserEventsDtoMeta**](RemnawaveWebhookUserEventsDtoMeta.md) |  | 

## Example

```python
from supn_remnawave_panel.models.remnawave_webhook_user_events_dto import RemnawaveWebhookUserEventsDto

# TODO update the JSON string below
json = "{}"
# create an instance of RemnawaveWebhookUserEventsDto from a JSON string
remnawave_webhook_user_events_dto_instance = RemnawaveWebhookUserEventsDto.from_json(json)
# print the JSON string representation of the object
print(RemnawaveWebhookUserEventsDto.to_json())

# convert the object into a dict
remnawave_webhook_user_events_dto_dict = remnawave_webhook_user_events_dto_instance.to_dict()
# create an instance of RemnawaveWebhookUserEventsDto from a dict
remnawave_webhook_user_events_dto_from_dict = RemnawaveWebhookUserEventsDto.from_dict(remnawave_webhook_user_events_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


