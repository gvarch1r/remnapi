# GetUserByUsernameResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateUserResponseDtoResponse**](CreateUserResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_user_by_username_response_dto import GetUserByUsernameResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserByUsernameResponseDto from a JSON string
get_user_by_username_response_dto_instance = GetUserByUsernameResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetUserByUsernameResponseDto.to_json())

# convert the object into a dict
get_user_by_username_response_dto_dict = get_user_by_username_response_dto_instance.to_dict()
# create an instance of GetUserByUsernameResponseDto from a dict
get_user_by_username_response_dto_from_dict = GetUserByUsernameResponseDto.from_dict(get_user_by_username_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


