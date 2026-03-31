# UpdateRemnawaveSettingsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetRemnawaveSettingsResponseDtoResponse**](GetRemnawaveSettingsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.update_remnawave_settings_response_dto import UpdateRemnawaveSettingsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRemnawaveSettingsResponseDto from a JSON string
update_remnawave_settings_response_dto_instance = UpdateRemnawaveSettingsResponseDto.from_json(json)
# print the JSON string representation of the object
print(UpdateRemnawaveSettingsResponseDto.to_json())

# convert the object into a dict
update_remnawave_settings_response_dto_dict = update_remnawave_settings_response_dto_instance.to_dict()
# create an instance of UpdateRemnawaveSettingsResponseDto from a dict
update_remnawave_settings_response_dto_from_dict = UpdateRemnawaveSettingsResponseDto.from_dict(update_remnawave_settings_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


