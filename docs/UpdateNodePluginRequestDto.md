# UpdateNodePluginRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**name** | **str** |  | [optional] 
**plugin_config** | **object** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.update_node_plugin_request_dto import UpdateNodePluginRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNodePluginRequestDto from a JSON string
update_node_plugin_request_dto_instance = UpdateNodePluginRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateNodePluginRequestDto.to_json())

# convert the object into a dict
update_node_plugin_request_dto_dict = update_node_plugin_request_dto_instance.to_dict()
# create an instance of UpdateNodePluginRequestDto from a dict
update_node_plugin_request_dto_from_dict = UpdateNodePluginRequestDto.from_dict(update_node_plugin_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


