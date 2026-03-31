# GetNodePluginsResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**node_plugins** | [**List[GetNodePluginsResponseDtoResponseNodePluginsInner]**](GetNodePluginsResponseDtoResponseNodePluginsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_node_plugins_response_dto_response import GetNodePluginsResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNodePluginsResponseDtoResponse from a JSON string
get_node_plugins_response_dto_response_instance = GetNodePluginsResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetNodePluginsResponseDtoResponse.to_json())

# convert the object into a dict
get_node_plugins_response_dto_response_dict = get_node_plugins_response_dto_response_instance.to_dict()
# create an instance of GetNodePluginsResponseDtoResponse from a dict
get_node_plugins_response_dto_response_from_dict = GetNodePluginsResponseDtoResponse.from_dict(get_node_plugins_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


