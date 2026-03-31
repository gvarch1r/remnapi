# CreateSnippetRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**snippet** | **List[object]** |  | 

## Example

```python
from supn_remnawave_panel.models.create_snippet_request_dto import CreateSnippetRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnippetRequestDto from a JSON string
create_snippet_request_dto_instance = CreateSnippetRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateSnippetRequestDto.to_json())

# convert the object into a dict
create_snippet_request_dto_dict = create_snippet_request_dto_instance.to_dict()
# create an instance of CreateSnippetRequestDto from a dict
create_snippet_request_dto_from_dict = CreateSnippetRequestDto.from_dict(create_snippet_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


