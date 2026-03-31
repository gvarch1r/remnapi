# DropConnectionsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drop_by** | [**DropConnectionsRequestDtoDropBy**](DropConnectionsRequestDtoDropBy.md) |  | 
**target_nodes** | [**PluginExecutorRequestDtoTargetNodes**](PluginExecutorRequestDtoTargetNodes.md) |  | 

## Example

```python
from supn_remnawave_panel.models.drop_connections_request_dto import DropConnectionsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DropConnectionsRequestDto from a JSON string
drop_connections_request_dto_instance = DropConnectionsRequestDto.from_json(json)
# print the JSON string representation of the object
print(DropConnectionsRequestDto.to_json())

# convert the object into a dict
drop_connections_request_dto_dict = drop_connections_request_dto_instance.to_dict()
# create an instance of DropConnectionsRequestDto from a dict
drop_connections_request_dto_from_dict = DropConnectionsRequestDto.from_dict(drop_connections_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


