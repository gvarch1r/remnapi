# GetSnippetsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetSnippetsResponseDtoResponse**](GetSnippetsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_snippets_response_dto import GetSnippetsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetSnippetsResponseDto from a JSON string
get_snippets_response_dto_instance = GetSnippetsResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetSnippetsResponseDto.to_json())

# convert the object into a dict
get_snippets_response_dto_dict = get_snippets_response_dto_instance.to_dict()
# create an instance of GetSnippetsResponseDto from a dict
get_snippets_response_dto_from_dict = GetSnippetsResponseDto.from_dict(get_snippets_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


