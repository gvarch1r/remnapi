# EnableUserResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateUserResponseDtoResponse**](CreateUserResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.enable_user_response_dto import EnableUserResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of EnableUserResponseDto from a JSON string
enable_user_response_dto_instance = EnableUserResponseDto.from_json(json)
# print the JSON string representation of the object
print(EnableUserResponseDto.to_json())

# convert the object into a dict
enable_user_response_dto_dict = enable_user_response_dto_instance.to_dict()
# create an instance of EnableUserResponseDto from a dict
enable_user_response_dto_from_dict = EnableUserResponseDto.from_dict(enable_user_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


