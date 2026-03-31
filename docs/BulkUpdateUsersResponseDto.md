# BulkUpdateUsersResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**BulkDeleteUsersByStatusResponseDtoResponse**](BulkDeleteUsersByStatusResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_update_users_response_dto import BulkUpdateUsersResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateUsersResponseDto from a JSON string
bulk_update_users_response_dto_instance = BulkUpdateUsersResponseDto.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateUsersResponseDto.to_json())

# convert the object into a dict
bulk_update_users_response_dto_dict = bulk_update_users_response_dto_instance.to_dict()
# create an instance of BulkUpdateUsersResponseDto from a dict
bulk_update_users_response_dto_from_dict = BulkUpdateUsersResponseDto.from_dict(bulk_update_users_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


