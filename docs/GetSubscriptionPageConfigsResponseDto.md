# GetSubscriptionPageConfigsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetSubscriptionPageConfigsResponseDtoResponse**](GetSubscriptionPageConfigsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_subscription_page_configs_response_dto import GetSubscriptionPageConfigsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionPageConfigsResponseDto from a JSON string
get_subscription_page_configs_response_dto_instance = GetSubscriptionPageConfigsResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionPageConfigsResponseDto.to_json())

# convert the object into a dict
get_subscription_page_configs_response_dto_dict = get_subscription_page_configs_response_dto_instance.to_dict()
# create an instance of GetSubscriptionPageConfigsResponseDto from a dict
get_subscription_page_configs_response_dto_from_dict = GetSubscriptionPageConfigsResponseDto.from_dict(get_subscription_page_configs_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


