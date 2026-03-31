# GetUserSubscriptionRequestHistoryResponseDtoResponseRecordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**user_uuid** | **UUID** |  | 
**request_at** | **datetime** |  | 
**request_ip** | **str** |  | 
**user_agent** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.get_user_subscription_request_history_response_dto_response_records_inner import GetUserSubscriptionRequestHistoryResponseDtoResponseRecordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserSubscriptionRequestHistoryResponseDtoResponseRecordsInner from a JSON string
get_user_subscription_request_history_response_dto_response_records_inner_instance = GetUserSubscriptionRequestHistoryResponseDtoResponseRecordsInner.from_json(json)
# print the JSON string representation of the object
print(GetUserSubscriptionRequestHistoryResponseDtoResponseRecordsInner.to_json())

# convert the object into a dict
get_user_subscription_request_history_response_dto_response_records_inner_dict = get_user_subscription_request_history_response_dto_response_records_inner_instance.to_dict()
# create an instance of GetUserSubscriptionRequestHistoryResponseDtoResponseRecordsInner from a dict
get_user_subscription_request_history_response_dto_response_records_inner_from_dict = GetUserSubscriptionRequestHistoryResponseDtoResponseRecordsInner.from_dict(get_user_subscription_request_history_response_dto_response_records_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


