# RestartNodeResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BulkAllUpdateUsersResponseDtoResponse**](BulkAllUpdateUsersResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.restart_node_response_dto import RestartNodeResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of RestartNodeResponseDto from a JSON string
restart_node_response_dto_instance = RestartNodeResponseDto.from_json(json)
# print the JSON string representation of the object
print(RestartNodeResponseDto.to_json())

# convert the object into a dict
restart_node_response_dto_dict = restart_node_response_dto_instance.to_dict()
# create an instance of RestartNodeResponseDto from a dict
restart_node_response_dto_from_dict = RestartNodeResponseDto.from_dict(restart_node_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


