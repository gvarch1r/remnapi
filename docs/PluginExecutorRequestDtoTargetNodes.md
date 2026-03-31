# PluginExecutorRequestDtoTargetNodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** |  | 
**node_uuids** | **List[UUID]** |  | 

## Example

```python
from supn_remnawave_panel.models.plugin_executor_request_dto_target_nodes import PluginExecutorRequestDtoTargetNodes

# TODO update the JSON string below
json = "{}"
# create an instance of PluginExecutorRequestDtoTargetNodes from a JSON string
plugin_executor_request_dto_target_nodes_instance = PluginExecutorRequestDtoTargetNodes.from_json(json)
# print the JSON string representation of the object
print(PluginExecutorRequestDtoTargetNodes.to_json())

# convert the object into a dict
plugin_executor_request_dto_target_nodes_dict = plugin_executor_request_dto_target_nodes_instance.to_dict()
# create an instance of PluginExecutorRequestDtoTargetNodes from a dict
plugin_executor_request_dto_target_nodes_from_dict = PluginExecutorRequestDtoTargetNodes.from_dict(plugin_executor_request_dto_target_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


