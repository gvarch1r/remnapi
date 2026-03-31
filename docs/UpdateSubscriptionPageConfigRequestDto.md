# UpdateSubscriptionPageConfigRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**name** | **str** |  | [optional] 
**config** | **object** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.update_subscription_page_config_request_dto import UpdateSubscriptionPageConfigRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriptionPageConfigRequestDto from a JSON string
update_subscription_page_config_request_dto_instance = UpdateSubscriptionPageConfigRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateSubscriptionPageConfigRequestDto.to_json())

# convert the object into a dict
update_subscription_page_config_request_dto_dict = update_subscription_page_config_request_dto_instance.to_dict()
# create an instance of UpdateSubscriptionPageConfigRequestDto from a dict
update_subscription_page_config_request_dto_from_dict = UpdateSubscriptionPageConfigRequestDto.from_dict(update_subscription_page_config_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


