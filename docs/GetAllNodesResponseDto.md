# GetAllNodesResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[CreateNodeResponseDtoResponse]**](CreateNodeResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_all_nodes_response_dto import GetAllNodesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllNodesResponseDto from a JSON string
get_all_nodes_response_dto_instance = GetAllNodesResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetAllNodesResponseDto.to_json())

# convert the object into a dict
get_all_nodes_response_dto_dict = get_all_nodes_response_dto_instance.to_dict()
# create an instance of GetAllNodesResponseDto from a dict
get_all_nodes_response_dto_from_dict = GetAllNodesResponseDto.from_dict(get_all_nodes_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


