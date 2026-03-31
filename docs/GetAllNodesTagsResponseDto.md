# GetAllNodesTagsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetAllTagsResponseDtoResponse**](GetAllTagsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_all_nodes_tags_response_dto import GetAllNodesTagsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllNodesTagsResponseDto from a JSON string
get_all_nodes_tags_response_dto_instance = GetAllNodesTagsResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetAllNodesTagsResponseDto.to_json())

# convert the object into a dict
get_all_nodes_tags_response_dto_dict = get_all_nodes_tags_response_dto_instance.to_dict()
# create an instance of GetAllNodesTagsResponseDto from a dict
get_all_nodes_tags_response_dto_from_dict = GetAllNodesTagsResponseDto.from_dict(get_all_nodes_tags_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


