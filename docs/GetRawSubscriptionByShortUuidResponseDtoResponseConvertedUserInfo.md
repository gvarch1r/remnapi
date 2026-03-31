# GetRawSubscriptionByShortUuidResponseDtoResponseConvertedUserInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_left** | **float** |  | 
**traffic_limit** | **str** |  | 
**traffic_used** | **str** |  | 
**lifetime_traffic_used** | **str** |  | 
**is_hwid_limited** | **bool** |  | 

## Example

```python
from supn_remnawave_panel.models.get_raw_subscription_by_short_uuid_response_dto_response_converted_user_info import GetRawSubscriptionByShortUuidResponseDtoResponseConvertedUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GetRawSubscriptionByShortUuidResponseDtoResponseConvertedUserInfo from a JSON string
get_raw_subscription_by_short_uuid_response_dto_response_converted_user_info_instance = GetRawSubscriptionByShortUuidResponseDtoResponseConvertedUserInfo.from_json(json)
# print the JSON string representation of the object
print(GetRawSubscriptionByShortUuidResponseDtoResponseConvertedUserInfo.to_json())

# convert the object into a dict
get_raw_subscription_by_short_uuid_response_dto_response_converted_user_info_dict = get_raw_subscription_by_short_uuid_response_dto_response_converted_user_info_instance.to_dict()
# create an instance of GetRawSubscriptionByShortUuidResponseDtoResponseConvertedUserInfo from a dict
get_raw_subscription_by_short_uuid_response_dto_response_converted_user_info_from_dict = GetRawSubscriptionByShortUuidResponseDtoResponseConvertedUserInfo.from_dict(get_raw_subscription_by_short_uuid_response_dto_response_converted_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


