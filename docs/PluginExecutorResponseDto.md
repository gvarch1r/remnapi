# PluginExecutorResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BulkAllUpdateUsersResponseDtoResponse**](BulkAllUpdateUsersResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.plugin_executor_response_dto import PluginExecutorResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PluginExecutorResponseDto from a JSON string
plugin_executor_response_dto_instance = PluginExecutorResponseDto.from_json(json)
# print the JSON string representation of the object
print(PluginExecutorResponseDto.to_json())

# convert the object into a dict
plugin_executor_response_dto_dict = plugin_executor_response_dto_instance.to_dict()
# create an instance of PluginExecutorResponseDto from a dict
plugin_executor_response_dto_from_dict = PluginExecutorResponseDto.from_dict(plugin_executor_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


