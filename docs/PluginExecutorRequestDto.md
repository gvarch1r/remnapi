# PluginExecutorRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | [**PluginExecutorRequestDtoCommand**](PluginExecutorRequestDtoCommand.md) |  | 
**target_nodes** | [**PluginExecutorRequestDtoTargetNodes**](PluginExecutorRequestDtoTargetNodes.md) |  | 

## Example

```python
from supn_remnawave_panel.models.plugin_executor_request_dto import PluginExecutorRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of PluginExecutorRequestDto from a JSON string
plugin_executor_request_dto_instance = PluginExecutorRequestDto.from_json(json)
# print the JSON string representation of the object
print(PluginExecutorRequestDto.to_json())

# convert the object into a dict
plugin_executor_request_dto_dict = plugin_executor_request_dto_instance.to_dict()
# create an instance of PluginExecutorRequestDto from a dict
plugin_executor_request_dto_from_dict = PluginExecutorRequestDto.from_dict(plugin_executor_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


