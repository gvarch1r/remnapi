# CloneNodePluginRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clone_from_uuid** | **UUID** |  | 

## Example

```python
from supn_remnawave_panel.models.clone_node_plugin_request_dto import CloneNodePluginRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CloneNodePluginRequestDto from a JSON string
clone_node_plugin_request_dto_instance = CloneNodePluginRequestDto.from_json(json)
# print the JSON string representation of the object
print(CloneNodePluginRequestDto.to_json())

# convert the object into a dict
clone_node_plugin_request_dto_dict = clone_node_plugin_request_dto_instance.to_dict()
# create an instance of CloneNodePluginRequestDto from a dict
clone_node_plugin_request_dto_from_dict = CloneNodePluginRequestDto.from_dict(clone_node_plugin_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


