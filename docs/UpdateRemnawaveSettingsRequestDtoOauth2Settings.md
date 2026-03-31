# UpdateRemnawaveSettingsRequestDtoOauth2Settings


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
from supn_remnawave_panel.models.update_remnawave_settings_request_dto_oauth2_settings import UpdateRemnawaveSettingsRequestDtoOauth2Settings

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRemnawaveSettingsRequestDtoOauth2Settings from a JSON string
update_remnawave_settings_request_dto_oauth2_settings_instance = UpdateRemnawaveSettingsRequestDtoOauth2Settings.from_json(json)
# print the JSON string representation of the object
print(UpdateRemnawaveSettingsRequestDtoOauth2Settings.to_json())

# convert the object into a dict
update_remnawave_settings_request_dto_oauth2_settings_dict = update_remnawave_settings_request_dto_oauth2_settings_instance.to_dict()
# create an instance of UpdateRemnawaveSettingsRequestDtoOauth2Settings from a dict
update_remnawave_settings_request_dto_oauth2_settings_from_dict = UpdateRemnawaveSettingsRequestDtoOauth2Settings.from_dict(update_remnawave_settings_request_dto_oauth2_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


