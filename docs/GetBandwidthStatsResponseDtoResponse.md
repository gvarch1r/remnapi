# GetBandwidthStatsResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth_last_two_days** | [**GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays**](GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays.md) |  | 
**bandwidth_last_seven_days** | [**GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays**](GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays.md) |  | 
**bandwidth_last30_days** | [**GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays**](GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays.md) |  | 
**bandwidth_calendar_month** | [**GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays**](GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays.md) |  | 
**bandwidth_current_year** | [**GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays**](GetBandwidthStatsResponseDtoResponseBandwidthLastTwoDays.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_bandwidth_stats_response_dto_response import GetBandwidthStatsResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBandwidthStatsResponseDtoResponse from a JSON string
get_bandwidth_stats_response_dto_response_instance = GetBandwidthStatsResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetBandwidthStatsResponseDtoResponse.to_json())

# convert the object into a dict
get_bandwidth_stats_response_dto_response_dict = get_bandwidth_stats_response_dto_response_instance.to_dict()
# create an instance of GetBandwidthStatsResponseDtoResponse from a dict
get_bandwidth_stats_response_dto_response_from_dict = GetBandwidthStatsResponseDtoResponse.from_dict(get_bandwidth_stats_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


