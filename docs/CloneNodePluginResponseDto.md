# CloneNodePluginResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetNodePluginResponseDtoResponse**](GetNodePluginResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.clone_node_plugin_response_dto import CloneNodePluginResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CloneNodePluginResponseDto from a JSON string
clone_node_plugin_response_dto_instance = CloneNodePluginResponseDto.from_json(json)
# print the JSON string representation of the object
print(CloneNodePluginResponseDto.to_json())

# convert the object into a dict
clone_node_plugin_response_dto_dict = clone_node_plugin_response_dto_instance.to_dict()
# create an instance of CloneNodePluginResponseDto from a dict
clone_node_plugin_response_dto_from_dict = CloneNodePluginResponseDto.from_dict(clone_node_plugin_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


