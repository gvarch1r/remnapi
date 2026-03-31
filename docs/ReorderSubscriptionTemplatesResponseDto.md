# ReorderSubscriptionTemplatesResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetTemplatesResponseDtoResponse**](GetTemplatesResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.reorder_subscription_templates_response_dto import ReorderSubscriptionTemplatesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderSubscriptionTemplatesResponseDto from a JSON string
reorder_subscription_templates_response_dto_instance = ReorderSubscriptionTemplatesResponseDto.from_json(json)
# print the JSON string representation of the object
print(ReorderSubscriptionTemplatesResponseDto.to_json())

# convert the object into a dict
reorder_subscription_templates_response_dto_dict = reorder_subscription_templates_response_dto_instance.to_dict()
# create an instance of ReorderSubscriptionTemplatesResponseDto from a dict
reorder_subscription_templates_response_dto_from_dict = ReorderSubscriptionTemplatesResponseDto.from_dict(reorder_subscription_templates_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


