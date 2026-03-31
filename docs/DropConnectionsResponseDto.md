# DropConnectionsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BulkAllUpdateUsersResponseDtoResponse**](BulkAllUpdateUsersResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.drop_connections_response_dto import DropConnectionsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DropConnectionsResponseDto from a JSON string
drop_connections_response_dto_instance = DropConnectionsResponseDto.from_json(json)
# print the JSON string representation of the object
print(DropConnectionsResponseDto.to_json())

# convert the object into a dict
drop_connections_response_dto_dict = drop_connections_response_dto_instance.to_dict()
# create an instance of DropConnectionsResponseDto from a dict
drop_connections_response_dto_from_dict = DropConnectionsResponseDto.from_dict(drop_connections_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


