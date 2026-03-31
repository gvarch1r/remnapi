# GetStatusResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetStatusResponseDtoResponse**](GetStatusResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_status_response_dto import GetStatusResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusResponseDto from a JSON string
get_status_response_dto_instance = GetStatusResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetStatusResponseDto.to_json())

# convert the object into a dict
get_status_response_dto_dict = get_status_response_dto_instance.to_dict()
# create an instance of GetStatusResponseDto from a dict
get_status_response_dto_from_dict = GetStatusResponseDto.from_dict(get_status_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


