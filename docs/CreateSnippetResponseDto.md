# CreateSnippetResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetSnippetsResponseDtoResponse**](GetSnippetsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_snippet_response_dto import CreateSnippetResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnippetResponseDto from a JSON string
create_snippet_response_dto_instance = CreateSnippetResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreateSnippetResponseDto.to_json())

# convert the object into a dict
create_snippet_response_dto_dict = create_snippet_response_dto_instance.to_dict()
# create an instance of CreateSnippetResponseDto from a dict
create_snippet_response_dto_from_dict = CreateSnippetResponseDto.from_dict(create_snippet_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


