# BulkDeleteUsersByStatusRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] [default to 'ACTIVE']

## Example

```python
from supn_remnawave_panel.models.bulk_delete_users_by_status_request_dto import BulkDeleteUsersByStatusRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteUsersByStatusRequestDto from a JSON string
bulk_delete_users_by_status_request_dto_instance = BulkDeleteUsersByStatusRequestDto.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteUsersByStatusRequestDto.to_json())

# convert the object into a dict
bulk_delete_users_by_status_request_dto_dict = bulk_delete_users_by_status_request_dto_instance.to_dict()
# create an instance of BulkDeleteUsersByStatusRequestDto from a dict
bulk_delete_users_by_status_request_dto_from_dict = BulkDeleteUsersByStatusRequestDto.from_dict(bulk_delete_users_by_status_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


