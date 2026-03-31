# UpdateNodePluginResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetNodePluginResponseDtoResponse**](GetNodePluginResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.update_node_plugin_response_dto import UpdateNodePluginResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNodePluginResponseDto from a JSON string
update_node_plugin_response_dto_instance = UpdateNodePluginResponseDto.from_json(json)
# print the JSON string representation of the object
print(UpdateNodePluginResponseDto.to_json())

# convert the object into a dict
update_node_plugin_response_dto_dict = update_node_plugin_response_dto_instance.to_dict()
# create an instance of UpdateNodePluginResponseDto from a dict
update_node_plugin_response_dto_from_dict = UpdateNodePluginResponseDto.from_dict(update_node_plugin_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


