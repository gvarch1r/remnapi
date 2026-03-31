# CreateUserHwidDeviceRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hwid** | **str** |  | 
**user_uuid** | **UUID** |  | 
**platform** | **str** |  | [optional] 
**os_version** | **str** |  | [optional] 
**device_model** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.create_user_hwid_device_request_dto import CreateUserHwidDeviceRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserHwidDeviceRequestDto from a JSON string
create_user_hwid_device_request_dto_instance = CreateUserHwidDeviceRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateUserHwidDeviceRequestDto.to_json())

# convert the object into a dict
create_user_hwid_device_request_dto_dict = create_user_hwid_device_request_dto_instance.to_dict()
# create an instance of CreateUserHwidDeviceRequestDto from a dict
create_user_hwid_device_request_dto_from_dict = CreateUserHwidDeviceRequestDto.from_dict(create_user_hwid_device_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


