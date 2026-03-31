# PluginExecutorRequestDtoCommandOneOf

Block IPs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** |  | 
**ips** | [**List[PluginExecutorRequestDtoCommandOneOfIpsInner]**](PluginExecutorRequestDtoCommandOneOfIpsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.plugin_executor_request_dto_command_one_of import PluginExecutorRequestDtoCommandOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of PluginExecutorRequestDtoCommandOneOf from a JSON string
plugin_executor_request_dto_command_one_of_instance = PluginExecutorRequestDtoCommandOneOf.from_json(json)
# print the JSON string representation of the object
print(PluginExecutorRequestDtoCommandOneOf.to_json())

# convert the object into a dict
plugin_executor_request_dto_command_one_of_dict = plugin_executor_request_dto_command_one_of_instance.to_dict()
# create an instance of PluginExecutorRequestDtoCommandOneOf from a dict
plugin_executor_request_dto_command_one_of_from_dict = PluginExecutorRequestDtoCommandOneOf.from_dict(plugin_executor_request_dto_command_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


