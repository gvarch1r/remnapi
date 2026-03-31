# GetNodePluginsResponseDtoResponseNodePluginsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**view_position** | **int** |  | 
**name** | **str** |  | 
**plugin_config** | **object** |  | 

## Example

```python
from supn_remnawave_panel.models.get_node_plugins_response_dto_response_node_plugins_inner import GetNodePluginsResponseDtoResponseNodePluginsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetNodePluginsResponseDtoResponseNodePluginsInner from a JSON string
get_node_plugins_response_dto_response_node_plugins_inner_instance = GetNodePluginsResponseDtoResponseNodePluginsInner.from_json(json)
# print the JSON string representation of the object
print(GetNodePluginsResponseDtoResponseNodePluginsInner.to_json())

# convert the object into a dict
get_node_plugins_response_dto_response_node_plugins_inner_dict = get_node_plugins_response_dto_response_node_plugins_inner_instance.to_dict()
# create an instance of GetNodePluginsResponseDtoResponseNodePluginsInner from a dict
get_node_plugins_response_dto_response_node_plugins_inner_from_dict = GetNodePluginsResponseDtoResponseNodePluginsInner.from_dict(get_node_plugins_response_dto_response_node_plugins_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


