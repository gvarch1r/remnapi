# GetRemnawaveSettingsResponseDtoResponseOauth2Settings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**github** | [**GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGithub**](GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGithub.md) |  | 
**pocketid** | [**GetRemnawaveSettingsResponseDtoResponseOauth2SettingsPocketid**](GetRemnawaveSettingsResponseDtoResponseOauth2SettingsPocketid.md) |  | 
**yandex** | [**GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGithub**](GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGithub.md) |  | 
**keycloak** | [**GetRemnawaveSettingsResponseDtoResponseOauth2SettingsKeycloak**](GetRemnawaveSettingsResponseDtoResponseOauth2SettingsKeycloak.md) |  | [optional] 
**generic** | [**GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGeneric**](GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGeneric.md) |  | [optional] 
**telegram** | [**GetRemnawaveSettingsResponseDtoResponseOauth2SettingsTelegram**](GetRemnawaveSettingsResponseDtoResponseOauth2SettingsTelegram.md) |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.get_remnawave_settings_response_dto_response_oauth2_settings import GetRemnawaveSettingsResponseDtoResponseOauth2Settings

# TODO update the JSON string below
json = "{}"
# create an instance of GetRemnawaveSettingsResponseDtoResponseOauth2Settings from a JSON string
get_remnawave_settings_response_dto_response_oauth2_settings_instance = GetRemnawaveSettingsResponseDtoResponseOauth2Settings.from_json(json)
# print the JSON string representation of the object
print(GetRemnawaveSettingsResponseDtoResponseOauth2Settings.to_json())

# convert the object into a dict
get_remnawave_settings_response_dto_response_oauth2_settings_dict = get_remnawave_settings_response_dto_response_oauth2_settings_instance.to_dict()
# create an instance of GetRemnawaveSettingsResponseDtoResponseOauth2Settings from a dict
get_remnawave_settings_response_dto_response_oauth2_settings_from_dict = GetRemnawaveSettingsResponseDtoResponseOauth2Settings.from_dict(get_remnawave_settings_response_dto_response_oauth2_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


