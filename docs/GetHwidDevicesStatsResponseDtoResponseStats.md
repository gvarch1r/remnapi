# GetHwidDevicesStatsResponseDtoResponseStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_unique_devices** | **float** |  | 
**total_hwid_devices** | **float** |  | 
**average_hwid_devices_per_user** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.get_hwid_devices_stats_response_dto_response_stats import GetHwidDevicesStatsResponseDtoResponseStats

# TODO update the JSON string below
json = "{}"
# create an instance of GetHwidDevicesStatsResponseDtoResponseStats from a JSON string
get_hwid_devices_stats_response_dto_response_stats_instance = GetHwidDevicesStatsResponseDtoResponseStats.from_json(json)
# print the JSON string representation of the object
print(GetHwidDevicesStatsResponseDtoResponseStats.to_json())

# convert the object into a dict
get_hwid_devices_stats_response_dto_response_stats_dict = get_hwid_devices_stats_response_dto_response_stats_instance.to_dict()
# create an instance of GetHwidDevicesStatsResponseDtoResponseStats from a dict
get_hwid_devices_stats_response_dto_response_stats_from_dict = GetHwidDevicesStatsResponseDtoResponseStats.from_dict(get_hwid_devices_stats_response_dto_response_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


