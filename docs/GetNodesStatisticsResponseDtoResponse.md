# GetNodesStatisticsResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_seven_days** | [**List[GetNodesStatisticsResponseDtoResponseLastSevenDaysInner]**](GetNodesStatisticsResponseDtoResponseLastSevenDaysInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_nodes_statistics_response_dto_response import GetNodesStatisticsResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNodesStatisticsResponseDtoResponse from a JSON string
get_nodes_statistics_response_dto_response_instance = GetNodesStatisticsResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetNodesStatisticsResponseDtoResponse.to_json())

# convert the object into a dict
get_nodes_statistics_response_dto_response_dict = get_nodes_statistics_response_dto_response_instance.to_dict()
# create an instance of GetNodesStatisticsResponseDtoResponse from a dict
get_nodes_statistics_response_dto_response_from_dict = GetNodesStatisticsResponseDtoResponse.from_dict(get_nodes_statistics_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


