# PluginExecutorRequestDtoCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** |  | 
**ips** | **List[str]** |  | 

## Example

```python
from supn_remnawave_panel.models.plugin_executor_request_dto_command import PluginExecutorRequestDtoCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PluginExecutorRequestDtoCommand from a JSON string
plugin_executor_request_dto_command_instance = PluginExecutorRequestDtoCommand.from_json(json)
# print the JSON string representation of the object
print(PluginExecutorRequestDtoCommand.to_json())

# convert the object into a dict
plugin_executor_request_dto_command_dict = plugin_executor_request_dto_command_instance.to_dict()
# create an instance of PluginExecutorRequestDtoCommand from a dict
plugin_executor_request_dto_command_from_dict = PluginExecutorRequestDtoCommand.from_dict(plugin_executor_request_dto_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


