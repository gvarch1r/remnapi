# FetchIpsResultResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FetchIpsResultResponseDtoResponse**](FetchIpsResultResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.fetch_ips_result_response_dto import FetchIpsResultResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of FetchIpsResultResponseDto from a JSON string
fetch_ips_result_response_dto_instance = FetchIpsResultResponseDto.from_json(json)
# print the JSON string representation of the object
print(FetchIpsResultResponseDto.to_json())

# convert the object into a dict
fetch_ips_result_response_dto_dict = fetch_ips_result_response_dto_instance.to_dict()
# create an instance of FetchIpsResultResponseDto from a dict
fetch_ips_result_response_dto_from_dict = FetchIpsResultResponseDto.from_dict(fetch_ips_result_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


