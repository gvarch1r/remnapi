# RemnawaveWebhookServiceEventsDtoDataLoginAttempt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**ip** | **str** |  | 
**user_agent** | **str** |  | 
**description** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.remnawave_webhook_service_events_dto_data_login_attempt import RemnawaveWebhookServiceEventsDtoDataLoginAttempt

# TODO update the JSON string below
json = "{}"
# create an instance of RemnawaveWebhookServiceEventsDtoDataLoginAttempt from a JSON string
remnawave_webhook_service_events_dto_data_login_attempt_instance = RemnawaveWebhookServiceEventsDtoDataLoginAttempt.from_json(json)
# print the JSON string representation of the object
print(RemnawaveWebhookServiceEventsDtoDataLoginAttempt.to_json())

# convert the object into a dict
remnawave_webhook_service_events_dto_data_login_attempt_dict = remnawave_webhook_service_events_dto_data_login_attempt_instance.to_dict()
# create an instance of RemnawaveWebhookServiceEventsDtoDataLoginAttempt from a dict
remnawave_webhook_service_events_dto_data_login_attempt_from_dict = RemnawaveWebhookServiceEventsDtoDataLoginAttempt.from_dict(remnawave_webhook_service_events_dto_data_login_attempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


