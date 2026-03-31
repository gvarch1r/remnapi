# GetNodeMetadataResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetUserMetadataResponseDtoResponse**](GetUserMetadataResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_node_metadata_response_dto import GetNodeMetadataResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetNodeMetadataResponseDto from a JSON string
get_node_metadata_response_dto_instance = GetNodeMetadataResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetNodeMetadataResponseDto.to_json())

# convert the object into a dict
get_node_metadata_response_dto_dict = get_node_metadata_response_dto_instance.to_dict()
# create an instance of GetNodeMetadataResponseDto from a dict
get_node_metadata_response_dto_from_dict = GetNodeMetadataResponseDto.from_dict(get_node_metadata_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


