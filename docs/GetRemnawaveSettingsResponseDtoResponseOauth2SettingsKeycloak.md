# GetRemnawaveSettingsResponseDtoResponseOauth2SettingsKeycloak


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**realm** | **str** |  | 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**frontend_domain** | **str** |  | 
**keycloak_domain** | **str** |  | 
**allowed_emails** | **List[str]** |  | 

## Example

```python
from supn_remnawave_panel.models.get_remnawave_settings_response_dto_response_oauth2_settings_keycloak import GetRemnawaveSettingsResponseDtoResponseOauth2SettingsKeycloak

# TODO update the JSON string below
json = "{}"
# create an instance of GetRemnawaveSettingsResponseDtoResponseOauth2SettingsKeycloak from a JSON string
get_remnawave_settings_response_dto_response_oauth2_settings_keycloak_instance = GetRemnawaveSettingsResponseDtoResponseOauth2SettingsKeycloak.from_json(json)
# print the JSON string representation of the object
print(GetRemnawaveSettingsResponseDtoResponseOauth2SettingsKeycloak.to_json())

# convert the object into a dict
get_remnawave_settings_response_dto_response_oauth2_settings_keycloak_dict = get_remnawave_settings_response_dto_response_oauth2_settings_keycloak_instance.to_dict()
# create an instance of GetRemnawaveSettingsResponseDtoResponseOauth2SettingsKeycloak from a dict
get_remnawave_settings_response_dto_response_oauth2_settings_keycloak_from_dict = GetRemnawaveSettingsResponseDtoResponseOauth2SettingsKeycloak.from_dict(get_remnawave_settings_response_dto_response_oauth2_settings_keycloak_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


