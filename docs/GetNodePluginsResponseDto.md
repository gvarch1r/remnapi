# GetNodePluginsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetNodePluginsResponseDtoResponse**](GetNodePluginsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_node_plugins_response_dto import GetNodePluginsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetNodePluginsResponseDto from a JSON string
get_node_plugins_response_dto_instance = GetNodePluginsResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetNodePluginsResponseDto.to_json())

# convert the object into a dict
get_node_plugins_response_dto_dict = get_node_plugins_response_dto_instance.to_dict()
# create an instance of GetNodePluginsResponseDto from a dict
get_node_plugins_response_dto_from_dict = GetNodePluginsResponseDto.from_dict(get_node_plugins_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


