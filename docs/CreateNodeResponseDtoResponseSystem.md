# CreateNodeResponseDtoResponseSystem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**CreateNodeResponseDtoResponseSystemInfo**](CreateNodeResponseDtoResponseSystemInfo.md) |  | 
**stats** | [**CreateNodeResponseDtoResponseSystemStats**](CreateNodeResponseDtoResponseSystemStats.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_node_response_dto_response_system import CreateNodeResponseDtoResponseSystem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNodeResponseDtoResponseSystem from a JSON string
create_node_response_dto_response_system_instance = CreateNodeResponseDtoResponseSystem.from_json(json)
# print the JSON string representation of the object
print(CreateNodeResponseDtoResponseSystem.to_json())

# convert the object into a dict
create_node_response_dto_response_system_dict = create_node_response_dto_response_system_instance.to_dict()
# create an instance of CreateNodeResponseDtoResponseSystem from a dict
create_node_response_dto_response_system_from_dict = CreateNodeResponseDtoResponseSystem.from_dict(create_node_response_dto_response_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


