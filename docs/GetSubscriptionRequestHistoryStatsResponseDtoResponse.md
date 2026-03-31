# GetSubscriptionRequestHistoryStatsResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**by_parsed_app** | [**List[GetHwidDevicesStatsResponseDtoResponseByAppInner]**](GetHwidDevicesStatsResponseDtoResponseByAppInner.md) |  | 
**hourly_request_stats** | [**List[GetSubscriptionRequestHistoryStatsResponseDtoResponseHourlyRequestStatsInner]**](GetSubscriptionRequestHistoryStatsResponseDtoResponseHourlyRequestStatsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_subscription_request_history_stats_response_dto_response import GetSubscriptionRequestHistoryStatsResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionRequestHistoryStatsResponseDtoResponse from a JSON string
get_subscription_request_history_stats_response_dto_response_instance = GetSubscriptionRequestHistoryStatsResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionRequestHistoryStatsResponseDtoResponse.to_json())

# convert the object into a dict
get_subscription_request_history_stats_response_dto_response_dict = get_subscription_request_history_stats_response_dto_response_instance.to_dict()
# create an instance of GetSubscriptionRequestHistoryStatsResponseDtoResponse from a dict
get_subscription_request_history_stats_response_dto_response_from_dict = GetSubscriptionRequestHistoryStatsResponseDtoResponse.from_dict(get_subscription_request_history_stats_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


