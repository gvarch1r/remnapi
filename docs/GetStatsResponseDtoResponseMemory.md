# GetStatsResponseDtoResponseMemory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**free** | **float** |  | 
**used** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.get_stats_response_dto_response_memory import GetStatsResponseDtoResponseMemory

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatsResponseDtoResponseMemory from a JSON string
get_stats_response_dto_response_memory_instance = GetStatsResponseDtoResponseMemory.from_json(json)
# print the JSON string representation of the object
print(GetStatsResponseDtoResponseMemory.to_json())

# convert the object into a dict
get_stats_response_dto_response_memory_dict = get_stats_response_dto_response_memory_instance.to_dict()
# create an instance of GetStatsResponseDtoResponseMemory from a dict
get_stats_response_dto_response_memory_from_dict = GetStatsResponseDtoResponseMemory.from_dict(get_stats_response_dto_response_memory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


