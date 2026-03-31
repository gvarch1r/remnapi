# GetSubscriptionInfoResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetSubscriptionInfoResponseDtoResponse**](GetSubscriptionInfoResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_subscription_info_response_dto import GetSubscriptionInfoResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionInfoResponseDto from a JSON string
get_subscription_info_response_dto_instance = GetSubscriptionInfoResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionInfoResponseDto.to_json())

# convert the object into a dict
get_subscription_info_response_dto_dict = get_subscription_info_response_dto_instance.to_dict()
# create an instance of GetSubscriptionInfoResponseDto from a dict
get_subscription_info_response_dto_from_dict = GetSubscriptionInfoResponseDto.from_dict(get_subscription_info_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


