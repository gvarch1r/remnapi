# GetNodesMetricsResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[GetNodesMetricsResponseDtoResponseNodesInner]**](GetNodesMetricsResponseDtoResponseNodesInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_nodes_metrics_response_dto_response import GetNodesMetricsResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNodesMetricsResponseDtoResponse from a JSON string
get_nodes_metrics_response_dto_response_instance = GetNodesMetricsResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetNodesMetricsResponseDtoResponse.to_json())

# convert the object into a dict
get_nodes_metrics_response_dto_response_dict = get_nodes_metrics_response_dto_response_instance.to_dict()
# create an instance of GetNodesMetricsResponseDtoResponse from a dict
get_nodes_metrics_response_dto_response_from_dict = GetNodesMetricsResponseDtoResponse.from_dict(get_nodes_metrics_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


