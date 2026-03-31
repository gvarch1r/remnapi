# GetSubscriptionPageConfigsResponseDtoResponseConfigsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**view_position** | **int** |  | 
**name** | **str** |  | 
**config** | **object** |  | 

## Example

```python
from supn_remnawave_panel.models.get_subscription_page_configs_response_dto_response_configs_inner import GetSubscriptionPageConfigsResponseDtoResponseConfigsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionPageConfigsResponseDtoResponseConfigsInner from a JSON string
get_subscription_page_configs_response_dto_response_configs_inner_instance = GetSubscriptionPageConfigsResponseDtoResponseConfigsInner.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionPageConfigsResponseDtoResponseConfigsInner.to_json())

# convert the object into a dict
get_subscription_page_configs_response_dto_response_configs_inner_dict = get_subscription_page_configs_response_dto_response_configs_inner_instance.to_dict()
# create an instance of GetSubscriptionPageConfigsResponseDtoResponseConfigsInner from a dict
get_subscription_page_configs_response_dto_response_configs_inner_from_dict = GetSubscriptionPageConfigsResponseDtoResponseConfigsInner.from_dict(get_subscription_page_configs_response_dto_response_configs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


