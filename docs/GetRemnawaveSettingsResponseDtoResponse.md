# GetRemnawaveSettingsResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passkey_settings** | [**GetRemnawaveSettingsResponseDtoResponsePasskeySettings**](GetRemnawaveSettingsResponseDtoResponsePasskeySettings.md) |  | 
**oauth2_settings** | [**GetRemnawaveSettingsResponseDtoResponseOauth2Settings**](GetRemnawaveSettingsResponseDtoResponseOauth2Settings.md) |  | 
**password_settings** | [**GetRemnawaveSettingsResponseDtoResponsePasswordSettings**](GetRemnawaveSettingsResponseDtoResponsePasswordSettings.md) |  | 
**branding_settings** | [**GetRemnawaveSettingsResponseDtoResponseBrandingSettings**](GetRemnawaveSettingsResponseDtoResponseBrandingSettings.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_remnawave_settings_response_dto_response import GetRemnawaveSettingsResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRemnawaveSettingsResponseDtoResponse from a JSON string
get_remnawave_settings_response_dto_response_instance = GetRemnawaveSettingsResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetRemnawaveSettingsResponseDtoResponse.to_json())

# convert the object into a dict
get_remnawave_settings_response_dto_response_dict = get_remnawave_settings_response_dto_response_instance.to_dict()
# create an instance of GetRemnawaveSettingsResponseDtoResponse from a dict
get_remnawave_settings_response_dto_response_from_dict = GetRemnawaveSettingsResponseDtoResponse.from_dict(get_remnawave_settings_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


