# GetBandwidthStatsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetBandwidthStatsResponseDtoResponse**](GetBandwidthStatsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_bandwidth_stats_response_dto import GetBandwidthStatsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetBandwidthStatsResponseDto from a JSON string
get_bandwidth_stats_response_dto_instance = GetBandwidthStatsResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetBandwidthStatsResponseDto.to_json())

# convert the object into a dict
get_bandwidth_stats_response_dto_dict = get_bandwidth_stats_response_dto_instance.to_dict()
# create an instance of GetBandwidthStatsResponseDto from a dict
get_bandwidth_stats_response_dto_from_dict = GetBandwidthStatsResponseDto.from_dict(get_bandwidth_stats_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


