# DeleteSnippetRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.delete_snippet_request_dto import DeleteSnippetRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSnippetRequestDto from a JSON string
delete_snippet_request_dto_instance = DeleteSnippetRequestDto.from_json(json)
# print the JSON string representation of the object
print(DeleteSnippetRequestDto.to_json())

# convert the object into a dict
delete_snippet_request_dto_dict = delete_snippet_request_dto_instance.to_dict()
# create an instance of DeleteSnippetRequestDto from a dict
delete_snippet_request_dto_from_dict = DeleteSnippetRequestDto.from_dict(delete_snippet_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


