# GetUserSubscriptionRequestHistoryResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**records** | [**List[GetUserSubscriptionRequestHistoryResponseDtoResponseRecordsInner]**](GetUserSubscriptionRequestHistoryResponseDtoResponseRecordsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_user_subscription_request_history_response_dto_response import GetUserSubscriptionRequestHistoryResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserSubscriptionRequestHistoryResponseDtoResponse from a JSON string
get_user_subscription_request_history_response_dto_response_instance = GetUserSubscriptionRequestHistoryResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserSubscriptionRequestHistoryResponseDtoResponse.to_json())

# convert the object into a dict
get_user_subscription_request_history_response_dto_response_dict = get_user_subscription_request_history_response_dto_response_instance.to_dict()
# create an instance of GetUserSubscriptionRequestHistoryResponseDtoResponse from a dict
get_user_subscription_request_history_response_dto_response_from_dict = GetUserSubscriptionRequestHistoryResponseDtoResponse.from_dict(get_user_subscription_request_history_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


