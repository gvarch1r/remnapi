# UpdateSnippetResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetSnippetsResponseDtoResponse**](GetSnippetsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.update_snippet_response_dto import UpdateSnippetResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSnippetResponseDto from a JSON string
update_snippet_response_dto_instance = UpdateSnippetResponseDto.from_json(json)
# print the JSON string representation of the object
print(UpdateSnippetResponseDto.to_json())

# convert the object into a dict
update_snippet_response_dto_dict = update_snippet_response_dto_instance.to_dict()
# create an instance of UpdateSnippetResponseDto from a dict
update_snippet_response_dto_from_dict = UpdateSnippetResponseDto.from_dict(update_snippet_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


