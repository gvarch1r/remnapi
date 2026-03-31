# GetStatsResponseDtoResponseUsers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_counts** | **Dict[str, float]** |  | 
**total_users** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.get_stats_response_dto_response_users import GetStatsResponseDtoResponseUsers

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatsResponseDtoResponseUsers from a JSON string
get_stats_response_dto_response_users_instance = GetStatsResponseDtoResponseUsers.from_json(json)
# print the JSON string representation of the object
print(GetStatsResponseDtoResponseUsers.to_json())

# convert the object into a dict
get_stats_response_dto_response_users_dict = get_stats_response_dto_response_users_instance.to_dict()
# create an instance of GetStatsResponseDtoResponseUsers from a dict
get_stats_response_dto_response_users_from_dict = GetStatsResponseDtoResponseUsers.from_dict(get_stats_response_dto_response_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


