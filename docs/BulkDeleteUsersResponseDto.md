# BulkDeleteUsersResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BulkDeleteUsersByStatusResponseDtoResponse**](BulkDeleteUsersByStatusResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_delete_users_response_dto import BulkDeleteUsersResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteUsersResponseDto from a JSON string
bulk_delete_users_response_dto_instance = BulkDeleteUsersResponseDto.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteUsersResponseDto.to_json())

# convert the object into a dict
bulk_delete_users_response_dto_dict = bulk_delete_users_response_dto_instance.to_dict()
# create an instance of BulkDeleteUsersResponseDto from a dict
bulk_delete_users_response_dto_from_dict = BulkDeleteUsersResponseDto.from_dict(bulk_delete_users_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


