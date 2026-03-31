# ReorderSubscriptionPageConfigsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetSubscriptionPageConfigsResponseDtoResponse**](GetSubscriptionPageConfigsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.reorder_subscription_page_configs_response_dto import ReorderSubscriptionPageConfigsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderSubscriptionPageConfigsResponseDto from a JSON string
reorder_subscription_page_configs_response_dto_instance = ReorderSubscriptionPageConfigsResponseDto.from_json(json)
# print the JSON string representation of the object
print(ReorderSubscriptionPageConfigsResponseDto.to_json())

# convert the object into a dict
reorder_subscription_page_configs_response_dto_dict = reorder_subscription_page_configs_response_dto_instance.to_dict()
# create an instance of ReorderSubscriptionPageConfigsResponseDto from a dict
reorder_subscription_page_configs_response_dto_from_dict = ReorderSubscriptionPageConfigsResponseDto.from_dict(reorder_subscription_page_configs_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


