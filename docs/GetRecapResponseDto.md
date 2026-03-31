# GetRecapResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetRecapResponseDtoResponse**](GetRecapResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_recap_response_dto import GetRecapResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecapResponseDto from a JSON string
get_recap_response_dto_instance = GetRecapResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetRecapResponseDto.to_json())

# convert the object into a dict
get_recap_response_dto_dict = get_recap_response_dto_instance.to_dict()
# create an instance of GetRecapResponseDto from a dict
get_recap_response_dto_from_dict = GetRecapResponseDto.from_dict(get_recap_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


