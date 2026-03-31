# GetConnectionKeysByUuidResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetConnectionKeysByUuidResponseDtoResponse**](GetConnectionKeysByUuidResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_connection_keys_by_uuid_response_dto import GetConnectionKeysByUuidResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetConnectionKeysByUuidResponseDto from a JSON string
get_connection_keys_by_uuid_response_dto_instance = GetConnectionKeysByUuidResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetConnectionKeysByUuidResponseDto.to_json())

# convert the object into a dict
get_connection_keys_by_uuid_response_dto_dict = get_connection_keys_by_uuid_response_dto_instance.to_dict()
# create an instance of GetConnectionKeysByUuidResponseDto from a dict
get_connection_keys_by_uuid_response_dto_from_dict = GetConnectionKeysByUuidResponseDto.from_dict(get_connection_keys_by_uuid_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


