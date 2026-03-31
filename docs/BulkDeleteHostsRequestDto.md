# BulkDeleteHostsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[UUID]** |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_delete_hosts_request_dto import BulkDeleteHostsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteHostsRequestDto from a JSON string
bulk_delete_hosts_request_dto_instance = BulkDeleteHostsRequestDto.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteHostsRequestDto.to_json())

# convert the object into a dict
bulk_delete_hosts_request_dto_dict = bulk_delete_hosts_request_dto_instance.to_dict()
# create an instance of BulkDeleteHostsRequestDto from a dict
bulk_delete_hosts_request_dto_from_dict = BulkDeleteHostsRequestDto.from_dict(bulk_delete_hosts_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


