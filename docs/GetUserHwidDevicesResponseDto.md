# GetUserHwidDevicesResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateUserHwidDeviceResponseDtoResponse**](CreateUserHwidDeviceResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_user_hwid_devices_response_dto import GetUserHwidDevicesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserHwidDevicesResponseDto from a JSON string
get_user_hwid_devices_response_dto_instance = GetUserHwidDevicesResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetUserHwidDevicesResponseDto.to_json())

# convert the object into a dict
get_user_hwid_devices_response_dto_dict = get_user_hwid_devices_response_dto_instance.to_dict()
# create an instance of GetUserHwidDevicesResponseDto from a dict
get_user_hwid_devices_response_dto_from_dict = GetUserHwidDevicesResponseDto.from_dict(get_user_hwid_devices_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


