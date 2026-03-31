# UpdateSnippetRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**snippet** | **List[object]** |  | 

## Example

```python
from supn_remnawave_panel.models.update_snippet_request_dto import UpdateSnippetRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSnippetRequestDto from a JSON string
update_snippet_request_dto_instance = UpdateSnippetRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateSnippetRequestDto.to_json())

# convert the object into a dict
update_snippet_request_dto_dict = update_snippet_request_dto_instance.to_dict()
# create an instance of UpdateSnippetRequestDto from a dict
update_snippet_request_dto_from_dict = UpdateSnippetRequestDto.from_dict(update_snippet_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


