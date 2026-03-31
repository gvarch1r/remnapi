# GetHwidDevicesStatsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetHwidDevicesStatsResponseDtoResponse**](GetHwidDevicesStatsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_hwid_devices_stats_response_dto import GetHwidDevicesStatsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetHwidDevicesStatsResponseDto from a JSON string
get_hwid_devices_stats_response_dto_instance = GetHwidDevicesStatsResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetHwidDevicesStatsResponseDto.to_json())

# convert the object into a dict
get_hwid_devices_stats_response_dto_dict = get_hwid_devices_stats_response_dto_instance.to_dict()
# create an instance of GetHwidDevicesStatsResponseDto from a dict
get_hwid_devices_stats_response_dto_from_dict = GetHwidDevicesStatsResponseDto.from_dict(get_hwid_devices_stats_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


