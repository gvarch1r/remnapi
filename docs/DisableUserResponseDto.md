# DisableUserResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateUserResponseDtoResponse**](CreateUserResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.disable_user_response_dto import DisableUserResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DisableUserResponseDto from a JSON string
disable_user_response_dto_instance = DisableUserResponseDto.from_json(json)
# print the JSON string representation of the object
print(DisableUserResponseDto.to_json())

# convert the object into a dict
disable_user_response_dto_dict = disable_user_response_dto_instance.to_dict()
# create an instance of DisableUserResponseDto from a dict
disable_user_response_dto_from_dict = DisableUserResponseDto.from_dict(disable_user_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


