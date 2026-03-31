# CreateNodeResponseDtoResponseSystemStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_free** | **float** |  | 
**memory_used** | **float** |  | 
**uptime** | **float** |  | 
**load_avg** | **List[float]** |  | 
**interface** | [**CreateNodeResponseDtoResponseSystemStatsInterface**](CreateNodeResponseDtoResponseSystemStatsInterface.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_node_response_dto_response_system_stats import CreateNodeResponseDtoResponseSystemStats

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNodeResponseDtoResponseSystemStats from a JSON string
create_node_response_dto_response_system_stats_instance = CreateNodeResponseDtoResponseSystemStats.from_json(json)
# print the JSON string representation of the object
print(CreateNodeResponseDtoResponseSystemStats.to_json())

# convert the object into a dict
create_node_response_dto_response_system_stats_dict = create_node_response_dto_response_system_stats_instance.to_dict()
# create an instance of CreateNodeResponseDtoResponseSystemStats from a dict
create_node_response_dto_response_system_stats_from_dict = CreateNodeResponseDtoResponseSystemStats.from_dict(create_node_response_dto_response_system_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


