# GetSubscriptionByUuidResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetSubscriptionInfoResponseDtoResponse**](GetSubscriptionInfoResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_subscription_by_uuid_response_dto import GetSubscriptionByUuidResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionByUuidResponseDto from a JSON string
get_subscription_by_uuid_response_dto_instance = GetSubscriptionByUuidResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionByUuidResponseDto.to_json())

# convert the object into a dict
get_subscription_by_uuid_response_dto_dict = get_subscription_by_uuid_response_dto_instance.to_dict()
# create an instance of GetSubscriptionByUuidResponseDto from a dict
get_subscription_by_uuid_response_dto_from_dict = GetSubscriptionByUuidResponseDto.from_dict(get_subscription_by_uuid_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


