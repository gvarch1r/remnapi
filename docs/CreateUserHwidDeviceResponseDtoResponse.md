# CreateUserHwidDeviceResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**devices** | [**List[GetAllHwidDevicesResponseDtoResponseDevicesInner]**](GetAllHwidDevicesResponseDtoResponseDevicesInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_user_hwid_device_response_dto_response import CreateUserHwidDeviceResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserHwidDeviceResponseDtoResponse from a JSON string
create_user_hwid_device_response_dto_response_instance = CreateUserHwidDeviceResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(CreateUserHwidDeviceResponseDtoResponse.to_json())

# convert the object into a dict
create_user_hwid_device_response_dto_response_dict = create_user_hwid_device_response_dto_response_instance.to_dict()
# create an instance of CreateUserHwidDeviceResponseDtoResponse from a dict
create_user_hwid_device_response_dto_response_from_dict = CreateUserHwidDeviceResponseDtoResponse.from_dict(create_user_hwid_device_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


