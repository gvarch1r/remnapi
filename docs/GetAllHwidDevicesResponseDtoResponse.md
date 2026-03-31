# GetAllHwidDevicesResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[GetAllHwidDevicesResponseDtoResponseDevicesInner]**](GetAllHwidDevicesResponseDtoResponseDevicesInner.md) |  | 
**total** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.get_all_hwid_devices_response_dto_response import GetAllHwidDevicesResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllHwidDevicesResponseDtoResponse from a JSON string
get_all_hwid_devices_response_dto_response_instance = GetAllHwidDevicesResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllHwidDevicesResponseDtoResponse.to_json())

# convert the object into a dict
get_all_hwid_devices_response_dto_response_dict = get_all_hwid_devices_response_dto_response_instance.to_dict()
# create an instance of GetAllHwidDevicesResponseDtoResponse from a dict
get_all_hwid_devices_response_dto_response_from_dict = GetAllHwidDevicesResponseDtoResponse.from_dict(get_all_hwid_devices_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


