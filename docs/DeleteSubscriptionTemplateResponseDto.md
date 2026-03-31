# DeleteSubscriptionTemplateResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**DeleteSubscriptionPageConfigResponseDtoResponse**](DeleteSubscriptionPageConfigResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.delete_subscription_template_response_dto import DeleteSubscriptionTemplateResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSubscriptionTemplateResponseDto from a JSON string
delete_subscription_template_response_dto_instance = DeleteSubscriptionTemplateResponseDto.from_json(json)
# print the JSON string representation of the object
print(DeleteSubscriptionTemplateResponseDto.to_json())

# convert the object into a dict
delete_subscription_template_response_dto_dict = delete_subscription_template_response_dto_instance.to_dict()
# create an instance of DeleteSubscriptionTemplateResponseDto from a dict
delete_subscription_template_response_dto_from_dict = DeleteSubscriptionTemplateResponseDto.from_dict(delete_subscription_template_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


