# GetUserByIdResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateUserResponseDtoResponse**](CreateUserResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_user_by_id_response_dto import GetUserByIdResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserByIdResponseDto from a JSON string
get_user_by_id_response_dto_instance = GetUserByIdResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetUserByIdResponseDto.to_json())

# convert the object into a dict
get_user_by_id_response_dto_dict = get_user_by_id_response_dto_instance.to_dict()
# create an instance of GetUserByIdResponseDto from a dict
get_user_by_id_response_dto_from_dict = GetUserByIdResponseDto.from_dict(get_user_by_id_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


