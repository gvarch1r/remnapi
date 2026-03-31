# GetStatsResponseDtoResponseNodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_online** | **float** |  | 
**total_bytes_lifetime** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.get_stats_response_dto_response_nodes import GetStatsResponseDtoResponseNodes

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatsResponseDtoResponseNodes from a JSON string
get_stats_response_dto_response_nodes_instance = GetStatsResponseDtoResponseNodes.from_json(json)
# print the JSON string representation of the object
print(GetStatsResponseDtoResponseNodes.to_json())

# convert the object into a dict
get_stats_response_dto_response_nodes_dict = get_stats_response_dto_response_nodes_instance.to_dict()
# create an instance of GetStatsResponseDtoResponseNodes from a dict
get_stats_response_dto_response_nodes_from_dict = GetStatsResponseDtoResponseNodes.from_dict(get_stats_response_dto_response_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


