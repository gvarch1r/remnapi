# UpsertNodeMetadataResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetUserMetadataResponseDtoResponse**](GetUserMetadataResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.upsert_node_metadata_response_dto import UpsertNodeMetadataResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertNodeMetadataResponseDto from a JSON string
upsert_node_metadata_response_dto_instance = UpsertNodeMetadataResponseDto.from_json(json)
# print the JSON string representation of the object
print(UpsertNodeMetadataResponseDto.to_json())

# convert the object into a dict
upsert_node_metadata_response_dto_dict = upsert_node_metadata_response_dto_instance.to_dict()
# create an instance of UpsertNodeMetadataResponseDto from a dict
upsert_node_metadata_response_dto_from_dict = UpsertNodeMetadataResponseDto.from_dict(upsert_node_metadata_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


