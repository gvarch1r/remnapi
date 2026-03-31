# GetHwidDevicesStatsResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**by_platform** | [**List[GetHwidDevicesStatsResponseDtoResponseByPlatformInner]**](GetHwidDevicesStatsResponseDtoResponseByPlatformInner.md) |  | 
**by_app** | [**List[GetHwidDevicesStatsResponseDtoResponseByAppInner]**](GetHwidDevicesStatsResponseDtoResponseByAppInner.md) |  | 
**stats** | [**GetHwidDevicesStatsResponseDtoResponseStats**](GetHwidDevicesStatsResponseDtoResponseStats.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_hwid_devices_stats_response_dto_response import GetHwidDevicesStatsResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHwidDevicesStatsResponseDtoResponse from a JSON string
get_hwid_devices_stats_response_dto_response_instance = GetHwidDevicesStatsResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetHwidDevicesStatsResponseDtoResponse.to_json())

# convert the object into a dict
get_hwid_devices_stats_response_dto_response_dict = get_hwid_devices_stats_response_dto_response_instance.to_dict()
# create an instance of GetHwidDevicesStatsResponseDtoResponse from a dict
get_hwid_devices_stats_response_dto_response_from_dict = GetHwidDevicesStatsResponseDtoResponse.from_dict(get_hwid_devices_stats_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


