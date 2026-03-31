# GetRemnawaveHealthResponseDtoResponseRuntimeMetricsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rss** | **float** |  | 
**heap_used** | **float** |  | 
**heap_total** | **float** |  | 
**external** | **float** |  | 
**array_buffers** | **float** |  | 
**event_loop_delay_ms** | **float** |  | 
**event_loop_p99_ms** | **float** |  | 
**active_handles** | **float** |  | 
**uptime** | **float** |  | 
**pid** | **float** |  | 
**timestamp** | **float** |  | 
**instance_id** | **str** |  | 
**instance_type** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.get_remnawave_health_response_dto_response_runtime_metrics_inner import GetRemnawaveHealthResponseDtoResponseRuntimeMetricsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRemnawaveHealthResponseDtoResponseRuntimeMetricsInner from a JSON string
get_remnawave_health_response_dto_response_runtime_metrics_inner_instance = GetRemnawaveHealthResponseDtoResponseRuntimeMetricsInner.from_json(json)
# print the JSON string representation of the object
print(GetRemnawaveHealthResponseDtoResponseRuntimeMetricsInner.to_json())

# convert the object into a dict
get_remnawave_health_response_dto_response_runtime_metrics_inner_dict = get_remnawave_health_response_dto_response_runtime_metrics_inner_instance.to_dict()
# create an instance of GetRemnawaveHealthResponseDtoResponseRuntimeMetricsInner from a dict
get_remnawave_health_response_dto_response_runtime_metrics_inner_from_dict = GetRemnawaveHealthResponseDtoResponseRuntimeMetricsInner.from_dict(get_remnawave_health_response_dto_response_runtime_metrics_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


