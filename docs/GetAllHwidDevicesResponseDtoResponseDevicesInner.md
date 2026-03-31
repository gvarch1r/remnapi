# GetAllHwidDevicesResponseDtoResponseDevicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hwid** | **str** |  | 
**user_uuid** | **UUID** |  | 
**platform** | **str** |  | 
**os_version** | **str** |  | 
**device_model** | **str** |  | 
**user_agent** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from supn_remnawave_panel.models.get_all_hwid_devices_response_dto_response_devices_inner import GetAllHwidDevicesResponseDtoResponseDevicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllHwidDevicesResponseDtoResponseDevicesInner from a JSON string
get_all_hwid_devices_response_dto_response_devices_inner_instance = GetAllHwidDevicesResponseDtoResponseDevicesInner.from_json(json)
# print the JSON string representation of the object
print(GetAllHwidDevicesResponseDtoResponseDevicesInner.to_json())

# convert the object into a dict
get_all_hwid_devices_response_dto_response_devices_inner_dict = get_all_hwid_devices_response_dto_response_devices_inner_instance.to_dict()
# create an instance of GetAllHwidDevicesResponseDtoResponseDevicesInner from a dict
get_all_hwid_devices_response_dto_response_devices_inner_from_dict = GetAllHwidDevicesResponseDtoResponseDevicesInner.from_dict(get_all_hwid_devices_response_dto_response_devices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


