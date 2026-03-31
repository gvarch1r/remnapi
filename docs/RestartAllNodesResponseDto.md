# RestartAllNodesResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BulkAllUpdateUsersResponseDtoResponse**](BulkAllUpdateUsersResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.restart_all_nodes_response_dto import RestartAllNodesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of RestartAllNodesResponseDto from a JSON string
restart_all_nodes_response_dto_instance = RestartAllNodesResponseDto.from_json(json)
# print the JSON string representation of the object
print(RestartAllNodesResponseDto.to_json())

# convert the object into a dict
restart_all_nodes_response_dto_dict = restart_all_nodes_response_dto_instance.to_dict()
# create an instance of RestartAllNodesResponseDto from a dict
restart_all_nodes_response_dto_from_dict = RestartAllNodesResponseDto.from_dict(restart_all_nodes_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


