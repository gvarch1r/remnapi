# GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGeneric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**with_pkce** | **bool** |  | 
**authorization_url** | **str** |  | 
**token_url** | **str** |  | 
**frontend_domain** | **str** |  | 
**allowed_emails** | **List[str]** |  | 

## Example

```python
from supn_remnawave_panel.models.get_remnawave_settings_response_dto_response_oauth2_settings_generic import GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGeneric

# TODO update the JSON string below
json = "{}"
# create an instance of GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGeneric from a JSON string
get_remnawave_settings_response_dto_response_oauth2_settings_generic_instance = GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGeneric.from_json(json)
# print the JSON string representation of the object
print(GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGeneric.to_json())

# convert the object into a dict
get_remnawave_settings_response_dto_response_oauth2_settings_generic_dict = get_remnawave_settings_response_dto_response_oauth2_settings_generic_instance.to_dict()
# create an instance of GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGeneric from a dict
get_remnawave_settings_response_dto_response_oauth2_settings_generic_from_dict = GetRemnawaveSettingsResponseDtoResponseOauth2SettingsGeneric.from_dict(get_remnawave_settings_response_dto_response_oauth2_settings_generic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


