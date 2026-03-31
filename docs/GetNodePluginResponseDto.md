# GetNodePluginResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetNodePluginResponseDtoResponse**](GetNodePluginResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_node_plugin_response_dto import GetNodePluginResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetNodePluginResponseDto from a JSON string
get_node_plugin_response_dto_instance = GetNodePluginResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetNodePluginResponseDto.to_json())

# convert the object into a dict
get_node_plugin_response_dto_dict = get_node_plugin_response_dto_instance.to_dict()
# create an instance of GetNodePluginResponseDto from a dict
get_node_plugin_response_dto_from_dict = GetNodePluginResponseDto.from_dict(get_node_plugin_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


