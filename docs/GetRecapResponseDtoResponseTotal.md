# GetRecapResponseDtoResponseTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **float** |  | 
**nodes** | **float** |  | 
**traffic** | **str** |  | 
**nodes_ram** | **str** |  | 
**nodes_cpu_cores** | **float** |  | 
**distinct_countries** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.get_recap_response_dto_response_total import GetRecapResponseDtoResponseTotal

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecapResponseDtoResponseTotal from a JSON string
get_recap_response_dto_response_total_instance = GetRecapResponseDtoResponseTotal.from_json(json)
# print the JSON string representation of the object
print(GetRecapResponseDtoResponseTotal.to_json())

# convert the object into a dict
get_recap_response_dto_response_total_dict = get_recap_response_dto_response_total_instance.to_dict()
# create an instance of GetRecapResponseDtoResponseTotal from a dict
get_recap_response_dto_response_total_from_dict = GetRecapResponseDtoResponseTotal.from_dict(get_recap_response_dto_response_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


