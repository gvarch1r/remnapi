# GetUserByTagResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[CreateUserResponseDtoResponse]**](CreateUserResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_user_by_tag_response_dto import GetUserByTagResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserByTagResponseDto from a JSON string
get_user_by_tag_response_dto_instance = GetUserByTagResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetUserByTagResponseDto.to_json())

# convert the object into a dict
get_user_by_tag_response_dto_dict = get_user_by_tag_response_dto_instance.to_dict()
# create an instance of GetUserByTagResponseDto from a dict
get_user_by_tag_response_dto_from_dict = GetUserByTagResponseDto.from_dict(get_user_by_tag_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


