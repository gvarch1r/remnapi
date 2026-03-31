# GetSubscriptionPageConfigsResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**configs** | [**List[GetSubscriptionPageConfigsResponseDtoResponseConfigsInner]**](GetSubscriptionPageConfigsResponseDtoResponseConfigsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_subscription_page_configs_response_dto_response import GetSubscriptionPageConfigsResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionPageConfigsResponseDtoResponse from a JSON string
get_subscription_page_configs_response_dto_response_instance = GetSubscriptionPageConfigsResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionPageConfigsResponseDtoResponse.to_json())

# convert the object into a dict
get_subscription_page_configs_response_dto_response_dict = get_subscription_page_configs_response_dto_response_instance.to_dict()
# create an instance of GetSubscriptionPageConfigsResponseDtoResponse from a dict
get_subscription_page_configs_response_dto_response_from_dict = GetSubscriptionPageConfigsResponseDtoResponse.from_dict(get_subscription_page_configs_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


