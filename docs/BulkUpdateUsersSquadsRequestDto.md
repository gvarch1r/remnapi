# BulkUpdateUsersSquadsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[UUID]** |  | 
**active_internal_squads** | **List[UUID]** |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_update_users_squads_request_dto import BulkUpdateUsersSquadsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateUsersSquadsRequestDto from a JSON string
bulk_update_users_squads_request_dto_instance = BulkUpdateUsersSquadsRequestDto.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateUsersSquadsRequestDto.to_json())

# convert the object into a dict
bulk_update_users_squads_request_dto_dict = bulk_update_users_squads_request_dto_instance.to_dict()
# create an instance of BulkUpdateUsersSquadsRequestDto from a dict
bulk_update_users_squads_request_dto_from_dict = BulkUpdateUsersSquadsRequestDto.from_dict(bulk_update_users_squads_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


