# GetRemnawaveSettingsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetRemnawaveSettingsResponseDtoResponse**](GetRemnawaveSettingsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_remnawave_settings_response_dto import GetRemnawaveSettingsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetRemnawaveSettingsResponseDto from a JSON string
get_remnawave_settings_response_dto_instance = GetRemnawaveSettingsResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetRemnawaveSettingsResponseDto.to_json())

# convert the object into a dict
get_remnawave_settings_response_dto_dict = get_remnawave_settings_response_dto_instance.to_dict()
# create an instance of GetRemnawaveSettingsResponseDto from a dict
get_remnawave_settings_response_dto_from_dict = GetRemnawaveSettingsResponseDto.from_dict(get_remnawave_settings_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


