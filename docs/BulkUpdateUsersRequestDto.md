# BulkUpdateUsersRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[UUID]** |  | 
**fields** | [**BulkUpdateUsersRequestDtoFields**](BulkUpdateUsersRequestDtoFields.md) |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_update_users_request_dto import BulkUpdateUsersRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateUsersRequestDto from a JSON string
bulk_update_users_request_dto_instance = BulkUpdateUsersRequestDto.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateUsersRequestDto.to_json())

# convert the object into a dict
bulk_update_users_request_dto_dict = bulk_update_users_request_dto_instance.to_dict()
# create an instance of BulkUpdateUsersRequestDto from a dict
bulk_update_users_request_dto_from_dict = BulkUpdateUsersRequestDto.from_dict(bulk_update_users_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


