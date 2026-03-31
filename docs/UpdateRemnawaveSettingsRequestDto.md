# UpdateRemnawaveSettingsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passkey_settings** | [**UpdateRemnawaveSettingsRequestDtoPasskeySettings**](UpdateRemnawaveSettingsRequestDtoPasskeySettings.md) |  | [optional] 
**oauth2_settings** | [**UpdateRemnawaveSettingsRequestDtoOauth2Settings**](UpdateRemnawaveSettingsRequestDtoOauth2Settings.md) |  | [optional] 
**password_settings** | [**UpdateRemnawaveSettingsRequestDtoPasswordSettings**](UpdateRemnawaveSettingsRequestDtoPasswordSettings.md) |  | [optional] 
**branding_settings** | [**UpdateRemnawaveSettingsRequestDtoBrandingSettings**](UpdateRemnawaveSettingsRequestDtoBrandingSettings.md) |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.update_remnawave_settings_request_dto import UpdateRemnawaveSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRemnawaveSettingsRequestDto from a JSON string
update_remnawave_settings_request_dto_instance = UpdateRemnawaveSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateRemnawaveSettingsRequestDto.to_json())

# convert the object into a dict
update_remnawave_settings_request_dto_dict = update_remnawave_settings_request_dto_instance.to_dict()
# create an instance of UpdateRemnawaveSettingsRequestDto from a dict
update_remnawave_settings_request_dto_from_dict = UpdateRemnawaveSettingsRequestDto.from_dict(update_remnawave_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


