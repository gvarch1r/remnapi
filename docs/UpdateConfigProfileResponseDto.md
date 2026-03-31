# UpdateConfigProfileResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetConfigProfilesResponseDtoResponseConfigProfilesInner**](GetConfigProfilesResponseDtoResponseConfigProfilesInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.update_config_profile_response_dto import UpdateConfigProfileResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConfigProfileResponseDto from a JSON string
update_config_profile_response_dto_instance = UpdateConfigProfileResponseDto.from_json(json)
# print the JSON string representation of the object
print(UpdateConfigProfileResponseDto.to_json())

# convert the object into a dict
update_config_profile_response_dto_dict = update_config_profile_response_dto_instance.to_dict()
# create an instance of UpdateConfigProfileResponseDto from a dict
update_config_profile_response_dto_from_dict = UpdateConfigProfileResponseDto.from_dict(update_config_profile_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


