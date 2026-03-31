# UpsertUserMetadataResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetUserMetadataResponseDtoResponse**](GetUserMetadataResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.upsert_user_metadata_response_dto import UpsertUserMetadataResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertUserMetadataResponseDto from a JSON string
upsert_user_metadata_response_dto_instance = UpsertUserMetadataResponseDto.from_json(json)
# print the JSON string representation of the object
print(UpsertUserMetadataResponseDto.to_json())

# convert the object into a dict
upsert_user_metadata_response_dto_dict = upsert_user_metadata_response_dto_instance.to_dict()
# create an instance of UpsertUserMetadataResponseDto from a dict
upsert_user_metadata_response_dto_from_dict = UpsertUserMetadataResponseDto.from_dict(upsert_user_metadata_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


