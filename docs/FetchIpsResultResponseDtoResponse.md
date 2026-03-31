# FetchIpsResultResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_completed** | **bool** |  | 
**is_failed** | **bool** |  | 
**progress** | [**FetchIpsResultResponseDtoResponseProgress**](FetchIpsResultResponseDtoResponseProgress.md) |  | 
**result** | [**FetchIpsResultResponseDtoResponseResult**](FetchIpsResultResponseDtoResponseResult.md) |  | 

## Example

```python
from supn_remnawave_panel.models.fetch_ips_result_response_dto_response import FetchIpsResultResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FetchIpsResultResponseDtoResponse from a JSON string
fetch_ips_result_response_dto_response_instance = FetchIpsResultResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(FetchIpsResultResponseDtoResponse.to_json())

# convert the object into a dict
fetch_ips_result_response_dto_response_dict = fetch_ips_result_response_dto_response_instance.to_dict()
# create an instance of FetchIpsResultResponseDtoResponse from a dict
fetch_ips_result_response_dto_response_from_dict = FetchIpsResultResponseDtoResponse.from_dict(fetch_ips_result_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


