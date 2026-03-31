# GetConfigProfilesResponseDtoResponseConfigProfilesInnerInboundsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**profile_uuid** | **UUID** |  | 
**tag** | **str** |  | 
**type** | **str** |  | 
**network** | **str** |  | 
**security** | **str** |  | 
**port** | **float** |  | 
**raw_inbound** | **object** |  | 

## Example

```python
from supn_remnawave_panel.models.get_config_profiles_response_dto_response_config_profiles_inner_inbounds_inner import GetConfigProfilesResponseDtoResponseConfigProfilesInnerInboundsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetConfigProfilesResponseDtoResponseConfigProfilesInnerInboundsInner from a JSON string
get_config_profiles_response_dto_response_config_profiles_inner_inbounds_inner_instance = GetConfigProfilesResponseDtoResponseConfigProfilesInnerInboundsInner.from_json(json)
# print the JSON string representation of the object
print(GetConfigProfilesResponseDtoResponseConfigProfilesInnerInboundsInner.to_json())

# convert the object into a dict
get_config_profiles_response_dto_response_config_profiles_inner_inbounds_inner_dict = get_config_profiles_response_dto_response_config_profiles_inner_inbounds_inner_instance.to_dict()
# create an instance of GetConfigProfilesResponseDtoResponseConfigProfilesInnerInboundsInner from a dict
get_config_profiles_response_dto_response_config_profiles_inner_inbounds_inner_from_dict = GetConfigProfilesResponseDtoResponseConfigProfilesInnerInboundsInner.from_dict(get_config_profiles_response_dto_response_config_profiles_inner_inbounds_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


