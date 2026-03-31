# ReorderNodePluginsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetNodePluginsResponseDtoResponse**](GetNodePluginsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.reorder_node_plugins_response_dto import ReorderNodePluginsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderNodePluginsResponseDto from a JSON string
reorder_node_plugins_response_dto_instance = ReorderNodePluginsResponseDto.from_json(json)
# print the JSON string representation of the object
print(ReorderNodePluginsResponseDto.to_json())

# convert the object into a dict
reorder_node_plugins_response_dto_dict = reorder_node_plugins_response_dto_instance.to_dict()
# create an instance of ReorderNodePluginsResponseDto from a dict
reorder_node_plugins_response_dto_from_dict = ReorderNodePluginsResponseDto.from_dict(reorder_node_plugins_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


