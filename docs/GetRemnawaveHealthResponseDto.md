# GetRemnawaveHealthResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetRemnawaveHealthResponseDtoResponse**](GetRemnawaveHealthResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_remnawave_health_response_dto import GetRemnawaveHealthResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetRemnawaveHealthResponseDto from a JSON string
get_remnawave_health_response_dto_instance = GetRemnawaveHealthResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetRemnawaveHealthResponseDto.to_json())

# convert the object into a dict
get_remnawave_health_response_dto_dict = get_remnawave_health_response_dto_instance.to_dict()
# create an instance of GetRemnawaveHealthResponseDto from a dict
get_remnawave_health_response_dto_from_dict = GetRemnawaveHealthResponseDto.from_dict(get_remnawave_health_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


