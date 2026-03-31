# GetStatsUserUsageResponseDtoResponseSeriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**name** | **str** |  | 
**color** | **str** |  | 
**country_code** | **str** |  | 
**total** | **float** |  | 
**data** | **List[float]** |  | 

## Example

```python
from supn_remnawave_panel.models.get_stats_user_usage_response_dto_response_series_inner import GetStatsUserUsageResponseDtoResponseSeriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatsUserUsageResponseDtoResponseSeriesInner from a JSON string
get_stats_user_usage_response_dto_response_series_inner_instance = GetStatsUserUsageResponseDtoResponseSeriesInner.from_json(json)
# print the JSON string representation of the object
print(GetStatsUserUsageResponseDtoResponseSeriesInner.to_json())

# convert the object into a dict
get_stats_user_usage_response_dto_response_series_inner_dict = get_stats_user_usage_response_dto_response_series_inner_instance.to_dict()
# create an instance of GetStatsUserUsageResponseDtoResponseSeriesInner from a dict
get_stats_user_usage_response_dto_response_series_inner_from_dict = GetStatsUserUsageResponseDtoResponseSeriesInner.from_dict(get_stats_user_usage_response_dto_response_series_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


