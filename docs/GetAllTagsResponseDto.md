# GetAllTagsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetAllTagsResponseDtoResponse**](GetAllTagsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_all_tags_response_dto import GetAllTagsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllTagsResponseDto from a JSON string
get_all_tags_response_dto_instance = GetAllTagsResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetAllTagsResponseDto.to_json())

# convert the object into a dict
get_all_tags_response_dto_dict = get_all_tags_response_dto_instance.to_dict()
# create an instance of GetAllTagsResponseDto from a dict
get_all_tags_response_dto_from_dict = GetAllTagsResponseDto.from_dict(get_all_tags_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


