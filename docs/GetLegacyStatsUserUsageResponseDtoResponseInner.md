# GetLegacyStatsUserUsageResponseDtoResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_uuid** | **UUID** |  | 
**node_uuid** | **UUID** |  | 
**node_name** | **str** |  | 
**country_code** | **str** |  | 
**total** | **float** |  | 
**var_date** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.get_legacy_stats_user_usage_response_dto_response_inner import GetLegacyStatsUserUsageResponseDtoResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLegacyStatsUserUsageResponseDtoResponseInner from a JSON string
get_legacy_stats_user_usage_response_dto_response_inner_instance = GetLegacyStatsUserUsageResponseDtoResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetLegacyStatsUserUsageResponseDtoResponseInner.to_json())

# convert the object into a dict
get_legacy_stats_user_usage_response_dto_response_inner_dict = get_legacy_stats_user_usage_response_dto_response_inner_instance.to_dict()
# create an instance of GetLegacyStatsUserUsageResponseDtoResponseInner from a dict
get_legacy_stats_user_usage_response_dto_response_inner_from_dict = GetLegacyStatsUserUsageResponseDtoResponseInner.from_dict(get_legacy_stats_user_usage_response_dto_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


