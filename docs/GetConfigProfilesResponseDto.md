# GetConfigProfilesResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetConfigProfilesResponseDtoResponse**](GetConfigProfilesResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_config_profiles_response_dto import GetConfigProfilesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetConfigProfilesResponseDto from a JSON string
get_config_profiles_response_dto_instance = GetConfigProfilesResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetConfigProfilesResponseDto.to_json())

# convert the object into a dict
get_config_profiles_response_dto_dict = get_config_profiles_response_dto_instance.to_dict()
# create an instance of GetConfigProfilesResponseDto from a dict
get_config_profiles_response_dto_from_dict = GetConfigProfilesResponseDto.from_dict(get_config_profiles_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


