# GetSubscriptionRequestHistoryResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[GetSubscriptionRequestHistoryResponseDtoResponseRecordsInner]**](GetSubscriptionRequestHistoryResponseDtoResponseRecordsInner.md) |  | 
**total** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.get_subscription_request_history_response_dto_response import GetSubscriptionRequestHistoryResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionRequestHistoryResponseDtoResponse from a JSON string
get_subscription_request_history_response_dto_response_instance = GetSubscriptionRequestHistoryResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionRequestHistoryResponseDtoResponse.to_json())

# convert the object into a dict
get_subscription_request_history_response_dto_response_dict = get_subscription_request_history_response_dto_response_instance.to_dict()
# create an instance of GetSubscriptionRequestHistoryResponseDtoResponse from a dict
get_subscription_request_history_response_dto_response_from_dict = GetSubscriptionRequestHistoryResponseDtoResponse.from_dict(get_subscription_request_history_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


