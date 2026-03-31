# GetStatsNodesUsageResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetStatsUserUsageResponseDtoResponse**](GetStatsUserUsageResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_stats_nodes_usage_response_dto import GetStatsNodesUsageResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatsNodesUsageResponseDto from a JSON string
get_stats_nodes_usage_response_dto_instance = GetStatsNodesUsageResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetStatsNodesUsageResponseDto.to_json())

# convert the object into a dict
get_stats_nodes_usage_response_dto_dict = get_stats_nodes_usage_response_dto_instance.to_dict()
# create an instance of GetStatsNodesUsageResponseDto from a dict
get_stats_nodes_usage_response_dto_from_dict = GetStatsNodesUsageResponseDto.from_dict(get_stats_nodes_usage_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


