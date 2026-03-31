# UpdateUserResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateUserResponseDtoResponse**](CreateUserResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.update_user_response_dto import UpdateUserResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserResponseDto from a JSON string
update_user_response_dto_instance = UpdateUserResponseDto.from_json(json)
# print the JSON string representation of the object
print(UpdateUserResponseDto.to_json())

# convert the object into a dict
update_user_response_dto_dict = update_user_response_dto_instance.to_dict()
# create an instance of UpdateUserResponseDto from a dict
update_user_response_dto_from_dict = UpdateUserResponseDto.from_dict(update_user_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


