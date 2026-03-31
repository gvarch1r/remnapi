# DeleteUserHwidDeviceResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateUserHwidDeviceResponseDtoResponse**](CreateUserHwidDeviceResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.delete_user_hwid_device_response_dto import DeleteUserHwidDeviceResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUserHwidDeviceResponseDto from a JSON string
delete_user_hwid_device_response_dto_instance = DeleteUserHwidDeviceResponseDto.from_json(json)
# print the JSON string representation of the object
print(DeleteUserHwidDeviceResponseDto.to_json())

# convert the object into a dict
delete_user_hwid_device_response_dto_dict = delete_user_hwid_device_response_dto_instance.to_dict()
# create an instance of DeleteUserHwidDeviceResponseDto from a dict
delete_user_hwid_device_response_dto_from_dict = DeleteUserHwidDeviceResponseDto.from_dict(delete_user_hwid_device_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


