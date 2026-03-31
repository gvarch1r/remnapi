# FetchIpsResultResponseDtoResponseResultNodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_uuid** | **UUID** |  | 
**node_name** | **str** |  | 
**country_code** | **str** |  | 
**ips** | [**List[FetchIpsResultResponseDtoResponseResultNodesInnerIpsInner]**](FetchIpsResultResponseDtoResponseResultNodesInnerIpsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.fetch_ips_result_response_dto_response_result_nodes_inner import FetchIpsResultResponseDtoResponseResultNodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of FetchIpsResultResponseDtoResponseResultNodesInner from a JSON string
fetch_ips_result_response_dto_response_result_nodes_inner_instance = FetchIpsResultResponseDtoResponseResultNodesInner.from_json(json)
# print the JSON string representation of the object
print(FetchIpsResultResponseDtoResponseResultNodesInner.to_json())

# convert the object into a dict
fetch_ips_result_response_dto_response_result_nodes_inner_dict = fetch_ips_result_response_dto_response_result_nodes_inner_instance.to_dict()
# create an instance of FetchIpsResultResponseDtoResponseResultNodesInner from a dict
fetch_ips_result_response_dto_response_result_nodes_inner_from_dict = FetchIpsResultResponseDtoResponseResultNodesInner.from_dict(fetch_ips_result_response_dto_response_result_nodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


