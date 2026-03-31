# CreateNodePluginResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetNodePluginsResponseDtoResponseNodePluginsInner**](GetNodePluginsResponseDtoResponseNodePluginsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_node_plugin_response_dto import CreateNodePluginResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNodePluginResponseDto from a JSON string
create_node_plugin_response_dto_instance = CreateNodePluginResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreateNodePluginResponseDto.to_json())

# convert the object into a dict
create_node_plugin_response_dto_dict = create_node_plugin_response_dto_instance.to_dict()
# create an instance of CreateNodePluginResponseDto from a dict
create_node_plugin_response_dto_from_dict = CreateNodePluginResponseDto.from_dict(create_node_plugin_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


