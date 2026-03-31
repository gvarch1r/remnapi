# GetRawSubscriptionByShortUuidResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**CreateUserResponseDtoResponse**](CreateUserResponseDtoResponse.md) |  | 
**converted_user_info** | [**GetRawSubscriptionByShortUuidResponseDtoResponseConvertedUserInfo**](GetRawSubscriptionByShortUuidResponseDtoResponseConvertedUserInfo.md) |  | 
**headers** | **Dict[str, str]** |  | 
**resolved_proxy_configs** | [**List[GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInner]**](GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_raw_subscription_by_short_uuid_response_dto_response import GetRawSubscriptionByShortUuidResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRawSubscriptionByShortUuidResponseDtoResponse from a JSON string
get_raw_subscription_by_short_uuid_response_dto_response_instance = GetRawSubscriptionByShortUuidResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetRawSubscriptionByShortUuidResponseDtoResponse.to_json())

# convert the object into a dict
get_raw_subscription_by_short_uuid_response_dto_response_dict = get_raw_subscription_by_short_uuid_response_dto_response_instance.to_dict()
# create an instance of GetRawSubscriptionByShortUuidResponseDtoResponse from a dict
get_raw_subscription_by_short_uuid_response_dto_response_from_dict = GetRawSubscriptionByShortUuidResponseDtoResponse.from_dict(get_raw_subscription_by_short_uuid_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


