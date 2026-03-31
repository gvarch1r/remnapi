# DeleteSnippetResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetSnippetsResponseDtoResponse**](GetSnippetsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.delete_snippet_response_dto import DeleteSnippetResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSnippetResponseDto from a JSON string
delete_snippet_response_dto_instance = DeleteSnippetResponseDto.from_json(json)
# print the JSON string representation of the object
print(DeleteSnippetResponseDto.to_json())

# convert the object into a dict
delete_snippet_response_dto_dict = delete_snippet_response_dto_instance.to_dict()
# create an instance of DeleteSnippetResponseDto from a dict
delete_snippet_response_dto_from_dict = DeleteSnippetResponseDto.from_dict(delete_snippet_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


