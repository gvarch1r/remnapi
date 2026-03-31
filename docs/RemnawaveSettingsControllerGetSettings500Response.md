# RemnawaveSettingsControllerGetSettings500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.remnawave_settings_controller_get_settings500_response import RemnawaveSettingsControllerGetSettings500Response

# TODO update the JSON string below
json = "{}"
# create an instance of RemnawaveSettingsControllerGetSettings500Response from a JSON string
remnawave_settings_controller_get_settings500_response_instance = RemnawaveSettingsControllerGetSettings500Response.from_json(json)
# print the JSON string representation of the object
print(RemnawaveSettingsControllerGetSettings500Response.to_json())

# convert the object into a dict
remnawave_settings_controller_get_settings500_response_dict = remnawave_settings_controller_get_settings500_response_instance.to_dict()
# create an instance of RemnawaveSettingsControllerGetSettings500Response from a dict
remnawave_settings_controller_get_settings500_response_from_dict = RemnawaveSettingsControllerGetSettings500Response.from_dict(remnawave_settings_controller_get_settings500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


