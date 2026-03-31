# GetSnippetsResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**snippets** | [**List[GetSnippetsResponseDtoResponseSnippetsInner]**](GetSnippetsResponseDtoResponseSnippetsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_snippets_response_dto_response import GetSnippetsResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSnippetsResponseDtoResponse from a JSON string
get_snippets_response_dto_response_instance = GetSnippetsResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetSnippetsResponseDtoResponse.to_json())

# convert the object into a dict
get_snippets_response_dto_response_dict = get_snippets_response_dto_response_instance.to_dict()
# create an instance of GetSnippetsResponseDtoResponse from a dict
get_snippets_response_dto_response_from_dict = GetSnippetsResponseDtoResponse.from_dict(get_snippets_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


