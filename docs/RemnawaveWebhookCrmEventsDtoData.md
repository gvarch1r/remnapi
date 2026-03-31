# RemnawaveWebhookCrmEventsDtoData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_name** | **str** |  | 
**node_name** | **str** |  | 
**next_billing_at** | **datetime** |  | 
**login_url** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.remnawave_webhook_crm_events_dto_data import RemnawaveWebhookCrmEventsDtoData

# TODO update the JSON string below
json = "{}"
# create an instance of RemnawaveWebhookCrmEventsDtoData from a JSON string
remnawave_webhook_crm_events_dto_data_instance = RemnawaveWebhookCrmEventsDtoData.from_json(json)
# print the JSON string representation of the object
print(RemnawaveWebhookCrmEventsDtoData.to_json())

# convert the object into a dict
remnawave_webhook_crm_events_dto_data_dict = remnawave_webhook_crm_events_dto_data_instance.to_dict()
# create an instance of RemnawaveWebhookCrmEventsDtoData from a dict
remnawave_webhook_crm_events_dto_data_from_dict = RemnawaveWebhookCrmEventsDtoData.from_dict(remnawave_webhook_crm_events_dto_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


