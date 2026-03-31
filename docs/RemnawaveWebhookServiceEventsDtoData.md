# RemnawaveWebhookServiceEventsDtoData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_attempt** | [**RemnawaveWebhookServiceEventsDtoDataLoginAttempt**](RemnawaveWebhookServiceEventsDtoDataLoginAttempt.md) |  | [optional] 
**panel_version** | **str** |  | [optional] 
**subpage_config** | [**RemnawaveWebhookServiceEventsDtoDataSubpageConfig**](RemnawaveWebhookServiceEventsDtoDataSubpageConfig.md) |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.remnawave_webhook_service_events_dto_data import RemnawaveWebhookServiceEventsDtoData

# TODO update the JSON string below
json = "{}"
# create an instance of RemnawaveWebhookServiceEventsDtoData from a JSON string
remnawave_webhook_service_events_dto_data_instance = RemnawaveWebhookServiceEventsDtoData.from_json(json)
# print the JSON string representation of the object
print(RemnawaveWebhookServiceEventsDtoData.to_json())

# convert the object into a dict
remnawave_webhook_service_events_dto_data_dict = remnawave_webhook_service_events_dto_data_instance.to_dict()
# create an instance of RemnawaveWebhookServiceEventsDtoData from a dict
remnawave_webhook_service_events_dto_data_from_dict = RemnawaveWebhookServiceEventsDtoData.from_dict(remnawave_webhook_service_events_dto_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


