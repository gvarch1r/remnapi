# GetStatsUserUsageResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetStatsUserUsageResponseDtoResponse**](GetStatsUserUsageResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_stats_user_usage_response_dto import GetStatsUserUsageResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatsUserUsageResponseDto from a JSON string
get_stats_user_usage_response_dto_instance = GetStatsUserUsageResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetStatsUserUsageResponseDto.to_json())

# convert the object into a dict
get_stats_user_usage_response_dto_dict = get_stats_user_usage_response_dto_instance.to_dict()
# create an instance of GetStatsUserUsageResponseDto from a dict
get_stats_user_usage_response_dto_from_dict = GetStatsUserUsageResponseDto.from_dict(get_stats_user_usage_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


