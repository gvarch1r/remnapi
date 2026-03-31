# GetConfigProfilesResponseDtoResponseConfigProfilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**view_position** | **int** |  | 
**name** | **str** |  | 
**config** | **object** |  | 
**inbounds** | [**List[GetConfigProfilesResponseDtoResponseConfigProfilesInnerInboundsInner]**](GetConfigProfilesResponseDtoResponseConfigProfilesInnerInboundsInner.md) |  | 
**nodes** | [**List[GetConfigProfilesResponseDtoResponseConfigProfilesInnerNodesInner]**](GetConfigProfilesResponseDtoResponseConfigProfilesInnerNodesInner.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from supn_remnawave_panel.models.get_config_profiles_response_dto_response_config_profiles_inner import GetConfigProfilesResponseDtoResponseConfigProfilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetConfigProfilesResponseDtoResponseConfigProfilesInner from a JSON string
get_config_profiles_response_dto_response_config_profiles_inner_instance = GetConfigProfilesResponseDtoResponseConfigProfilesInner.from_json(json)
# print the JSON string representation of the object
print(GetConfigProfilesResponseDtoResponseConfigProfilesInner.to_json())

# convert the object into a dict
get_config_profiles_response_dto_response_config_profiles_inner_dict = get_config_profiles_response_dto_response_config_profiles_inner_instance.to_dict()
# create an instance of GetConfigProfilesResponseDtoResponseConfigProfilesInner from a dict
get_config_profiles_response_dto_response_config_profiles_inner_from_dict = GetConfigProfilesResponseDtoResponseConfigProfilesInner.from_dict(get_config_profiles_response_dto_response_config_profiles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


