# GetStatsResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**GetStatsResponseDtoResponseCpu**](GetStatsResponseDtoResponseCpu.md) |  | 
**memory** | [**GetStatsResponseDtoResponseMemory**](GetStatsResponseDtoResponseMemory.md) |  | 
**uptime** | **float** |  | 
**timestamp** | **float** |  | 
**users** | [**GetStatsResponseDtoResponseUsers**](GetStatsResponseDtoResponseUsers.md) |  | 
**online_stats** | [**GetStatsResponseDtoResponseOnlineStats**](GetStatsResponseDtoResponseOnlineStats.md) |  | 
**nodes** | [**GetStatsResponseDtoResponseNodes**](GetStatsResponseDtoResponseNodes.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_stats_response_dto_response import GetStatsResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatsResponseDtoResponse from a JSON string
get_stats_response_dto_response_instance = GetStatsResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetStatsResponseDtoResponse.to_json())

# convert the object into a dict
get_stats_response_dto_response_dict = get_stats_response_dto_response_instance.to_dict()
# create an instance of GetStatsResponseDtoResponse from a dict
get_stats_response_dto_response_from_dict = GetStatsResponseDtoResponse.from_dict(get_stats_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


