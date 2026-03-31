# RemnawaveSettingsControllerGetSettings400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status_code** | **float** |  | [optional] 
**errors** | [**List[RemnawaveSettingsControllerGetSettings400ResponseErrorsInner]**](RemnawaveSettingsControllerGetSettings400ResponseErrorsInner.md) |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.remnawave_settings_controller_get_settings400_response import RemnawaveSettingsControllerGetSettings400Response

# TODO update the JSON string below
json = "{}"
# create an instance of RemnawaveSettingsControllerGetSettings400Response from a JSON string
remnawave_settings_controller_get_settings400_response_instance = RemnawaveSettingsControllerGetSettings400Response.from_json(json)
# print the JSON string representation of the object
print(RemnawaveSettingsControllerGetSettings400Response.to_json())

# convert the object into a dict
remnawave_settings_controller_get_settings400_response_dict = remnawave_settings_controller_get_settings400_response_instance.to_dict()
# create an instance of RemnawaveSettingsControllerGetSettings400Response from a dict
remnawave_settings_controller_get_settings400_response_from_dict = RemnawaveSettingsControllerGetSettings400Response.from_dict(remnawave_settings_controller_get_settings400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


