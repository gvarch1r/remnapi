# ProfileModificationResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BulkAllUpdateUsersResponseDtoResponse**](BulkAllUpdateUsersResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.profile_modification_response_dto import ProfileModificationResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileModificationResponseDto from a JSON string
profile_modification_response_dto_instance = ProfileModificationResponseDto.from_json(json)
# print the JSON string representation of the object
print(ProfileModificationResponseDto.to_json())

# convert the object into a dict
profile_modification_response_dto_dict = profile_modification_response_dto_instance.to_dict()
# create an instance of ProfileModificationResponseDto from a dict
profile_modification_response_dto_from_dict = ProfileModificationResponseDto.from_dict(profile_modification_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


