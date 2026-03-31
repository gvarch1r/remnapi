# DeleteUserHwidDeviceRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_uuid** | **UUID** |  | 
**hwid** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.delete_user_hwid_device_request_dto import DeleteUserHwidDeviceRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUserHwidDeviceRequestDto from a JSON string
delete_user_hwid_device_request_dto_instance = DeleteUserHwidDeviceRequestDto.from_json(json)
# print the JSON string representation of the object
print(DeleteUserHwidDeviceRequestDto.to_json())

# convert the object into a dict
delete_user_hwid_device_request_dto_dict = delete_user_hwid_device_request_dto_instance.to_dict()
# create an instance of DeleteUserHwidDeviceRequestDto from a dict
delete_user_hwid_device_request_dto_from_dict = DeleteUserHwidDeviceRequestDto.from_dict(delete_user_hwid_device_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


