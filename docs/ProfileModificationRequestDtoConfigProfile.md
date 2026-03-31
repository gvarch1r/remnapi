# ProfileModificationRequestDtoConfigProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_config_profile_uuid** | **UUID** |  | 
**active_inbounds** | **List[UUID]** |  | 

## Example

```python
from supn_remnawave_panel.models.profile_modification_request_dto_config_profile import ProfileModificationRequestDtoConfigProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileModificationRequestDtoConfigProfile from a JSON string
profile_modification_request_dto_config_profile_instance = ProfileModificationRequestDtoConfigProfile.from_json(json)
# print the JSON string representation of the object
print(ProfileModificationRequestDtoConfigProfile.to_json())

# convert the object into a dict
profile_modification_request_dto_config_profile_dict = profile_modification_request_dto_config_profile_instance.to_dict()
# create an instance of ProfileModificationRequestDtoConfigProfile from a dict
profile_modification_request_dto_config_profile_from_dict = ProfileModificationRequestDtoConfigProfile.from_dict(profile_modification_request_dto_config_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


