# GetTopUsersByHwidDevicesResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[GetTopUsersByHwidDevicesResponseDtoResponseUsersInner]**](GetTopUsersByHwidDevicesResponseDtoResponseUsersInner.md) |  | 
**total** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.get_top_users_by_hwid_devices_response_dto_response import GetTopUsersByHwidDevicesResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTopUsersByHwidDevicesResponseDtoResponse from a JSON string
get_top_users_by_hwid_devices_response_dto_response_instance = GetTopUsersByHwidDevicesResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetTopUsersByHwidDevicesResponseDtoResponse.to_json())

# convert the object into a dict
get_top_users_by_hwid_devices_response_dto_response_dict = get_top_users_by_hwid_devices_response_dto_response_instance.to_dict()
# create an instance of GetTopUsersByHwidDevicesResponseDtoResponse from a dict
get_top_users_by_hwid_devices_response_dto_response_from_dict = GetTopUsersByHwidDevicesResponseDtoResponse.from_dict(get_top_users_by_hwid_devices_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


