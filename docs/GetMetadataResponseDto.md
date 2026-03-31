# GetMetadataResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetMetadataResponseDtoResponse**](GetMetadataResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_metadata_response_dto import GetMetadataResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetadataResponseDto from a JSON string
get_metadata_response_dto_instance = GetMetadataResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetMetadataResponseDto.to_json())

# convert the object into a dict
get_metadata_response_dto_dict = get_metadata_response_dto_instance.to_dict()
# create an instance of GetMetadataResponseDto from a dict
get_metadata_response_dto_from_dict = GetMetadataResponseDto.from_dict(get_metadata_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


