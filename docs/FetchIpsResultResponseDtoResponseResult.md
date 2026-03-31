# FetchIpsResultResponseDtoResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**user_uuid** | **UUID** |  | 
**user_id** | **str** |  | 
**nodes** | [**List[FetchIpsResultResponseDtoResponseResultNodesInner]**](FetchIpsResultResponseDtoResponseResultNodesInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.fetch_ips_result_response_dto_response_result import FetchIpsResultResponseDtoResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of FetchIpsResultResponseDtoResponseResult from a JSON string
fetch_ips_result_response_dto_response_result_instance = FetchIpsResultResponseDtoResponseResult.from_json(json)
# print the JSON string representation of the object
print(FetchIpsResultResponseDtoResponseResult.to_json())

# convert the object into a dict
fetch_ips_result_response_dto_response_result_dict = fetch_ips_result_response_dto_response_result_instance.to_dict()
# create an instance of FetchIpsResultResponseDtoResponseResult from a dict
fetch_ips_result_response_dto_response_result_from_dict = FetchIpsResultResponseDtoResponseResult.from_dict(fetch_ips_result_response_dto_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


