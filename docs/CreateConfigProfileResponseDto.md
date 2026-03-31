# CreateConfigProfileResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetConfigProfilesResponseDtoResponseConfigProfilesInner**](GetConfigProfilesResponseDtoResponseConfigProfilesInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_config_profile_response_dto import CreateConfigProfileResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConfigProfileResponseDto from a JSON string
create_config_profile_response_dto_instance = CreateConfigProfileResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreateConfigProfileResponseDto.to_json())

# convert the object into a dict
create_config_profile_response_dto_dict = create_config_profile_response_dto_instance.to_dict()
# create an instance of CreateConfigProfileResponseDto from a dict
create_config_profile_response_dto_from_dict = CreateConfigProfileResponseDto.from_dict(create_config_profile_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


