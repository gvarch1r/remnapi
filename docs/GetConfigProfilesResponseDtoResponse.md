# GetConfigProfilesResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**config_profiles** | [**List[GetConfigProfilesResponseDtoResponseConfigProfilesInner]**](GetConfigProfilesResponseDtoResponseConfigProfilesInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_config_profiles_response_dto_response import GetConfigProfilesResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetConfigProfilesResponseDtoResponse from a JSON string
get_config_profiles_response_dto_response_instance = GetConfigProfilesResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetConfigProfilesResponseDtoResponse.to_json())

# convert the object into a dict
get_config_profiles_response_dto_response_dict = get_config_profiles_response_dto_response_instance.to_dict()
# create an instance of GetConfigProfilesResponseDtoResponse from a dict
get_config_profiles_response_dto_response_from_dict = GetConfigProfilesResponseDtoResponse.from_dict(get_config_profiles_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


