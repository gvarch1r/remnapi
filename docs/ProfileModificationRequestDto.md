# ProfileModificationRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[UUID]** |  | 
**config_profile** | [**ProfileModificationRequestDtoConfigProfile**](ProfileModificationRequestDtoConfigProfile.md) |  | 

## Example

```python
from supn_remnawave_panel.models.profile_modification_request_dto import ProfileModificationRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileModificationRequestDto from a JSON string
profile_modification_request_dto_instance = ProfileModificationRequestDto.from_json(json)
# print the JSON string representation of the object
print(ProfileModificationRequestDto.to_json())

# convert the object into a dict
profile_modification_request_dto_dict = profile_modification_request_dto_instance.to_dict()
# create an instance of ProfileModificationRequestDto from a dict
profile_modification_request_dto_from_dict = ProfileModificationRequestDto.from_dict(profile_modification_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


