# GetAllHwidDevicesResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetAllHwidDevicesResponseDtoResponse**](GetAllHwidDevicesResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_all_hwid_devices_response_dto import GetAllHwidDevicesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllHwidDevicesResponseDto from a JSON string
get_all_hwid_devices_response_dto_instance = GetAllHwidDevicesResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetAllHwidDevicesResponseDto.to_json())

# convert the object into a dict
get_all_hwid_devices_response_dto_dict = get_all_hwid_devices_response_dto_instance.to_dict()
# create an instance of GetAllHwidDevicesResponseDto from a dict
get_all_hwid_devices_response_dto_from_dict = GetAllHwidDevicesResponseDto.from_dict(get_all_hwid_devices_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


