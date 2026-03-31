# GetStatsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetStatsResponseDtoResponse**](GetStatsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_stats_response_dto import GetStatsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatsResponseDto from a JSON string
get_stats_response_dto_instance = GetStatsResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetStatsResponseDto.to_json())

# convert the object into a dict
get_stats_response_dto_dict = get_stats_response_dto_instance.to_dict()
# create an instance of GetStatsResponseDto from a dict
get_stats_response_dto_from_dict = GetStatsResponseDto.from_dict(get_stats_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


