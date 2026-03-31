# PluginExecutorRequestDtoCommandOneOf1

Unblock IPs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** |  | 
**ips** | **List[str]** |  | 

## Example

```python
from supn_remnawave_panel.models.plugin_executor_request_dto_command_one_of1 import PluginExecutorRequestDtoCommandOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of PluginExecutorRequestDtoCommandOneOf1 from a JSON string
plugin_executor_request_dto_command_one_of1_instance = PluginExecutorRequestDtoCommandOneOf1.from_json(json)
# print the JSON string representation of the object
print(PluginExecutorRequestDtoCommandOneOf1.to_json())

# convert the object into a dict
plugin_executor_request_dto_command_one_of1_dict = plugin_executor_request_dto_command_one_of1_instance.to_dict()
# create an instance of PluginExecutorRequestDtoCommandOneOf1 from a dict
plugin_executor_request_dto_command_one_of1_from_dict = PluginExecutorRequestDtoCommandOneOf1.from_dict(plugin_executor_request_dto_command_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


