# GetConnectionKeysByUuidResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled_keys** | **List[str]** |  | 
**hidden_keys** | **List[str]** |  | 
**disabled_keys** | **List[str]** |  | 

## Example

```python
from supn_remnawave_panel.models.get_connection_keys_by_uuid_response_dto_response import GetConnectionKeysByUuidResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetConnectionKeysByUuidResponseDtoResponse from a JSON string
get_connection_keys_by_uuid_response_dto_response_instance = GetConnectionKeysByUuidResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetConnectionKeysByUuidResponseDtoResponse.to_json())

# convert the object into a dict
get_connection_keys_by_uuid_response_dto_response_dict = get_connection_keys_by_uuid_response_dto_response_instance.to_dict()
# create an instance of GetConnectionKeysByUuidResponseDtoResponse from a dict
get_connection_keys_by_uuid_response_dto_response_from_dict = GetConnectionKeysByUuidResponseDtoResponse.from_dict(get_connection_keys_by_uuid_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


