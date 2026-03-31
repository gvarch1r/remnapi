# GetStatusResponseDtoResponseAuthentication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passkey** | [**UpdateRemnawaveSettingsRequestDtoPasswordSettings**](UpdateRemnawaveSettingsRequestDtoPasswordSettings.md) |  | 
**oauth2** | [**GetStatusResponseDtoResponseAuthenticationOauth2**](GetStatusResponseDtoResponseAuthenticationOauth2.md) |  | 
**password** | [**UpdateRemnawaveSettingsRequestDtoPasswordSettings**](UpdateRemnawaveSettingsRequestDtoPasswordSettings.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_status_response_dto_response_authentication import GetStatusResponseDtoResponseAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusResponseDtoResponseAuthentication from a JSON string
get_status_response_dto_response_authentication_instance = GetStatusResponseDtoResponseAuthentication.from_json(json)
# print the JSON string representation of the object
print(GetStatusResponseDtoResponseAuthentication.to_json())

# convert the object into a dict
get_status_response_dto_response_authentication_dict = get_status_response_dto_response_authentication_instance.to_dict()
# create an instance of GetStatusResponseDtoResponseAuthentication from a dict
get_status_response_dto_response_authentication_from_dict = GetStatusResponseDtoResponseAuthentication.from_dict(get_status_response_dto_response_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


