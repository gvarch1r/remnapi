# GetStatsNodeUsersUsageResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** |  | 
**sparkline_data** | **List[float]** |  | 
**top_users** | [**List[GetStatsNodeUsersUsageResponseDtoResponseTopUsersInner]**](GetStatsNodeUsersUsageResponseDtoResponseTopUsersInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_stats_node_users_usage_response_dto_response import GetStatsNodeUsersUsageResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatsNodeUsersUsageResponseDtoResponse from a JSON string
get_stats_node_users_usage_response_dto_response_instance = GetStatsNodeUsersUsageResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetStatsNodeUsersUsageResponseDtoResponse.to_json())

# convert the object into a dict
get_stats_node_users_usage_response_dto_response_dict = get_stats_node_users_usage_response_dto_response_instance.to_dict()
# create an instance of GetStatsNodeUsersUsageResponseDtoResponse from a dict
get_stats_node_users_usage_response_dto_response_from_dict = GetStatsNodeUsersUsageResponseDtoResponse.from_dict(get_stats_node_users_usage_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


