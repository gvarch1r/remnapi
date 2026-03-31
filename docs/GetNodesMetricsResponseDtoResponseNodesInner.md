# GetNodesMetricsResponseDtoResponseNodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_uuid** | **str** |  | 
**node_name** | **str** |  | 
**country_emoji** | **str** |  | 
**provider_name** | **str** |  | 
**users_online** | **float** |  | 
**inbounds_stats** | [**List[GetNodesMetricsResponseDtoResponseNodesInnerInboundsStatsInner]**](GetNodesMetricsResponseDtoResponseNodesInnerInboundsStatsInner.md) |  | 
**outbounds_stats** | [**List[GetNodesMetricsResponseDtoResponseNodesInnerInboundsStatsInner]**](GetNodesMetricsResponseDtoResponseNodesInnerInboundsStatsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_nodes_metrics_response_dto_response_nodes_inner import GetNodesMetricsResponseDtoResponseNodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetNodesMetricsResponseDtoResponseNodesInner from a JSON string
get_nodes_metrics_response_dto_response_nodes_inner_instance = GetNodesMetricsResponseDtoResponseNodesInner.from_json(json)
# print the JSON string representation of the object
print(GetNodesMetricsResponseDtoResponseNodesInner.to_json())

# convert the object into a dict
get_nodes_metrics_response_dto_response_nodes_inner_dict = get_nodes_metrics_response_dto_response_nodes_inner_instance.to_dict()
# create an instance of GetNodesMetricsResponseDtoResponseNodesInner from a dict
get_nodes_metrics_response_dto_response_nodes_inner_from_dict = GetNodesMetricsResponseDtoResponseNodesInner.from_dict(get_nodes_metrics_response_dto_response_nodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


