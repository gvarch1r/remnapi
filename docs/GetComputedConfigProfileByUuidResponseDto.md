# GetComputedConfigProfileByUuidResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetConfigProfilesResponseDtoResponseConfigProfilesInner**](GetConfigProfilesResponseDtoResponseConfigProfilesInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_computed_config_profile_by_uuid_response_dto import GetComputedConfigProfileByUuidResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetComputedConfigProfileByUuidResponseDto from a JSON string
get_computed_config_profile_by_uuid_response_dto_instance = GetComputedConfigProfileByUuidResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetComputedConfigProfileByUuidResponseDto.to_json())

# convert the object into a dict
get_computed_config_profile_by_uuid_response_dto_dict = get_computed_config_profile_by_uuid_response_dto_instance.to_dict()
# create an instance of GetComputedConfigProfileByUuidResponseDto from a dict
get_computed_config_profile_by_uuid_response_dto_from_dict = GetComputedConfigProfileByUuidResponseDto.from_dict(get_computed_config_profile_by_uuid_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


