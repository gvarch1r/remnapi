# GetSubscriptionRequestHistoryResponseDtoResponseRecordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**user_uuid** | **UUID** |  | 
**request_ip** | **str** |  | 
**user_agent** | **str** |  | 
**request_at** | **datetime** |  | 

## Example

```python
from supn_remnawave_panel.models.get_subscription_request_history_response_dto_response_records_inner import GetSubscriptionRequestHistoryResponseDtoResponseRecordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionRequestHistoryResponseDtoResponseRecordsInner from a JSON string
get_subscription_request_history_response_dto_response_records_inner_instance = GetSubscriptionRequestHistoryResponseDtoResponseRecordsInner.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionRequestHistoryResponseDtoResponseRecordsInner.to_json())

# convert the object into a dict
get_subscription_request_history_response_dto_response_records_inner_dict = get_subscription_request_history_response_dto_response_records_inner_instance.to_dict()
# create an instance of GetSubscriptionRequestHistoryResponseDtoResponseRecordsInner from a dict
get_subscription_request_history_response_dto_response_records_inner_from_dict = GetSubscriptionRequestHistoryResponseDtoResponseRecordsInner.from_dict(get_subscription_request_history_response_dto_response_records_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


