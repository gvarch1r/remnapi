# GetUserMetadataResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetUserMetadataResponseDtoResponse**](GetUserMetadataResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_user_metadata_response_dto import GetUserMetadataResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserMetadataResponseDto from a JSON string
get_user_metadata_response_dto_instance = GetUserMetadataResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetUserMetadataResponseDto.to_json())

# convert the object into a dict
get_user_metadata_response_dto_dict = get_user_metadata_response_dto_instance.to_dict()
# create an instance of GetUserMetadataResponseDto from a dict
get_user_metadata_response_dto_from_dict = GetUserMetadataResponseDto.from_dict(get_user_metadata_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


