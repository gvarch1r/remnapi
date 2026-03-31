# GetTopUsersByHwidDevicesResponseDtoResponseUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_uuid** | **UUID** |  | 
**id** | **float** |  | 
**username** | **str** |  | 
**devices_count** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.get_top_users_by_hwid_devices_response_dto_response_users_inner import GetTopUsersByHwidDevicesResponseDtoResponseUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTopUsersByHwidDevicesResponseDtoResponseUsersInner from a JSON string
get_top_users_by_hwid_devices_response_dto_response_users_inner_instance = GetTopUsersByHwidDevicesResponseDtoResponseUsersInner.from_json(json)
# print the JSON string representation of the object
print(GetTopUsersByHwidDevicesResponseDtoResponseUsersInner.to_json())

# convert the object into a dict
get_top_users_by_hwid_devices_response_dto_response_users_inner_dict = get_top_users_by_hwid_devices_response_dto_response_users_inner_instance.to_dict()
# create an instance of GetTopUsersByHwidDevicesResponseDtoResponseUsersInner from a dict
get_top_users_by_hwid_devices_response_dto_response_users_inner_from_dict = GetTopUsersByHwidDevicesResponseDtoResponseUsersInner.from_dict(get_top_users_by_hwid_devices_response_dto_response_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


