# CreateSubscriptionPageConfigResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetSubscriptionPageConfigsResponseDtoResponseConfigsInner**](GetSubscriptionPageConfigsResponseDtoResponseConfigsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_subscription_page_config_response_dto import CreateSubscriptionPageConfigResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionPageConfigResponseDto from a JSON string
create_subscription_page_config_response_dto_instance = CreateSubscriptionPageConfigResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreateSubscriptionPageConfigResponseDto.to_json())

# convert the object into a dict
create_subscription_page_config_response_dto_dict = create_subscription_page_config_response_dto_instance.to_dict()
# create an instance of CreateSubscriptionPageConfigResponseDto from a dict
create_subscription_page_config_response_dto_from_dict = CreateSubscriptionPageConfigResponseDto.from_dict(create_subscription_page_config_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


