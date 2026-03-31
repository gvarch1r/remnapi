# GetExternalSquadsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetExternalSquadsResponseDtoResponse**](GetExternalSquadsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_external_squads_response_dto import GetExternalSquadsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetExternalSquadsResponseDto from a JSON string
get_external_squads_response_dto_instance = GetExternalSquadsResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetExternalSquadsResponseDto.to_json())

# convert the object into a dict
get_external_squads_response_dto_dict = get_external_squads_response_dto_instance.to_dict()
# create an instance of GetExternalSquadsResponseDto from a dict
get_external_squads_response_dto_from_dict = GetExternalSquadsResponseDto.from_dict(get_external_squads_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


