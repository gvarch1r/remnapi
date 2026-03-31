# GetStatsResponseDtoResponseOnlineStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_day** | **float** |  | 
**last_week** | **float** |  | 
**never_online** | **float** |  | 
**online_now** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.get_stats_response_dto_response_online_stats import GetStatsResponseDtoResponseOnlineStats

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatsResponseDtoResponseOnlineStats from a JSON string
get_stats_response_dto_response_online_stats_instance = GetStatsResponseDtoResponseOnlineStats.from_json(json)
# print the JSON string representation of the object
print(GetStatsResponseDtoResponseOnlineStats.to_json())

# convert the object into a dict
get_stats_response_dto_response_online_stats_dict = get_stats_response_dto_response_online_stats_instance.to_dict()
# create an instance of GetStatsResponseDtoResponseOnlineStats from a dict
get_stats_response_dto_response_online_stats_from_dict = GetStatsResponseDtoResponseOnlineStats.from_dict(get_stats_response_dto_response_online_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


