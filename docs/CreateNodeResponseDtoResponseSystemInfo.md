# CreateNodeResponseDtoResponseSystemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arch** | **str** |  | 
**cpus** | **int** |  | 
**cpu_model** | **str** |  | 
**memory_total** | **float** |  | 
**hostname** | **str** |  | 
**platform** | **str** |  | 
**release** | **str** |  | 
**type** | **str** |  | 
**version** | **str** |  | 
**network_interfaces** | **List[str]** |  | 

## Example

```python
from supn_remnawave_panel.models.create_node_response_dto_response_system_info import CreateNodeResponseDtoResponseSystemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNodeResponseDtoResponseSystemInfo from a JSON string
create_node_response_dto_response_system_info_instance = CreateNodeResponseDtoResponseSystemInfo.from_json(json)
# print the JSON string representation of the object
print(CreateNodeResponseDtoResponseSystemInfo.to_json())

# convert the object into a dict
create_node_response_dto_response_system_info_dict = create_node_response_dto_response_system_info_instance.to_dict()
# create an instance of CreateNodeResponseDtoResponseSystemInfo from a dict
create_node_response_dto_response_system_info_from_dict = CreateNodeResponseDtoResponseSystemInfo.from_dict(create_node_response_dto_response_system_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


