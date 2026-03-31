# GetNodesMetricsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetNodesMetricsResponseDtoResponse**](GetNodesMetricsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_nodes_metrics_response_dto import GetNodesMetricsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetNodesMetricsResponseDto from a JSON string
get_nodes_metrics_response_dto_instance = GetNodesMetricsResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetNodesMetricsResponseDto.to_json())

# convert the object into a dict
get_nodes_metrics_response_dto_dict = get_nodes_metrics_response_dto_instance.to_dict()
# create an instance of GetNodesMetricsResponseDto from a dict
get_nodes_metrics_response_dto_from_dict = GetNodesMetricsResponseDto.from_dict(get_nodes_metrics_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


