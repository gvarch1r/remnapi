# GetConfigProfileByUuidResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetConfigProfilesResponseDtoResponseConfigProfilesInner**](GetConfigProfilesResponseDtoResponseConfigProfilesInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_config_profile_by_uuid_response_dto import GetConfigProfileByUuidResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetConfigProfileByUuidResponseDto from a JSON string
get_config_profile_by_uuid_response_dto_instance = GetConfigProfileByUuidResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetConfigProfileByUuidResponseDto.to_json())

# convert the object into a dict
get_config_profile_by_uuid_response_dto_dict = get_config_profile_by_uuid_response_dto_instance.to_dict()
# create an instance of GetConfigProfileByUuidResponseDto from a dict
get_config_profile_by_uuid_response_dto_from_dict = GetConfigProfileByUuidResponseDto.from_dict(get_config_profile_by_uuid_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


