# GetSubscriptionInfoResponseDtoResponseUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_uuid** | **str** |  | 
**days_left** | **float** |  | 
**traffic_used** | **str** |  | 
**traffic_limit** | **str** |  | 
**lifetime_traffic_used** | **str** |  | 
**traffic_used_bytes** | **str** |  | 
**traffic_limit_bytes** | **str** |  | 
**lifetime_traffic_used_bytes** | **str** |  | 
**username** | **str** |  | 
**expires_at** | **datetime** |  | 
**is_active** | **bool** |  | 
**user_status** | **str** |  | 
**traffic_limit_strategy** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.get_subscription_info_response_dto_response_user import GetSubscriptionInfoResponseDtoResponseUser

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionInfoResponseDtoResponseUser from a JSON string
get_subscription_info_response_dto_response_user_instance = GetSubscriptionInfoResponseDtoResponseUser.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionInfoResponseDtoResponseUser.to_json())

# convert the object into a dict
get_subscription_info_response_dto_response_user_dict = get_subscription_info_response_dto_response_user_instance.to_dict()
# create an instance of GetSubscriptionInfoResponseDtoResponseUser from a dict
get_subscription_info_response_dto_response_user_from_dict = GetSubscriptionInfoResponseDtoResponseUser.from_dict(get_subscription_info_response_dto_response_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


