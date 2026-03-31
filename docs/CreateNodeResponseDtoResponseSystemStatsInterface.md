# CreateNodeResponseDtoResponseSystemStatsInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** |  | 
**rx_bytes_per_sec** | **float** |  | 
**tx_bytes_per_sec** | **float** |  | 
**rx_total** | **float** |  | 
**tx_total** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.create_node_response_dto_response_system_stats_interface import CreateNodeResponseDtoResponseSystemStatsInterface

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNodeResponseDtoResponseSystemStatsInterface from a JSON string
create_node_response_dto_response_system_stats_interface_instance = CreateNodeResponseDtoResponseSystemStatsInterface.from_json(json)
# print the JSON string representation of the object
print(CreateNodeResponseDtoResponseSystemStatsInterface.to_json())

# convert the object into a dict
create_node_response_dto_response_system_stats_interface_dict = create_node_response_dto_response_system_stats_interface_instance.to_dict()
# create an instance of CreateNodeResponseDtoResponseSystemStatsInterface from a dict
create_node_response_dto_response_system_stats_interface_from_dict = CreateNodeResponseDtoResponseSystemStatsInterface.from_dict(create_node_response_dto_response_system_stats_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


