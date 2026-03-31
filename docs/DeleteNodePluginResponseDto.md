# DeleteNodePluginResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**DeleteSubscriptionPageConfigResponseDtoResponse**](DeleteSubscriptionPageConfigResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.delete_node_plugin_response_dto import DeleteNodePluginResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteNodePluginResponseDto from a JSON string
delete_node_plugin_response_dto_instance = DeleteNodePluginResponseDto.from_json(json)
# print the JSON string representation of the object
print(DeleteNodePluginResponseDto.to_json())

# convert the object into a dict
delete_node_plugin_response_dto_dict = delete_node_plugin_response_dto_instance.to_dict()
# create an instance of DeleteNodePluginResponseDto from a dict
delete_node_plugin_response_dto_from_dict = DeleteNodePluginResponseDto.from_dict(delete_node_plugin_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


