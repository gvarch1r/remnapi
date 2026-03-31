# GetNodePluginResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**view_position** | **int** |  | 
**name** | **str** |  | 
**plugin_config** | **object** |  | 

## Example

```python
from supn_remnawave_panel.models.get_node_plugin_response_dto_response import GetNodePluginResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNodePluginResponseDtoResponse from a JSON string
get_node_plugin_response_dto_response_instance = GetNodePluginResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetNodePluginResponseDtoResponse.to_json())

# convert the object into a dict
get_node_plugin_response_dto_response_dict = get_node_plugin_response_dto_response_instance.to_dict()
# create an instance of GetNodePluginResponseDtoResponse from a dict
get_node_plugin_response_dto_response_from_dict = GetNodePluginResponseDtoResponse.from_dict(get_node_plugin_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


