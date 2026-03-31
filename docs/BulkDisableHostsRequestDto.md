# BulkDisableHostsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[UUID]** |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_disable_hosts_request_dto import BulkDisableHostsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDisableHostsRequestDto from a JSON string
bulk_disable_hosts_request_dto_instance = BulkDisableHostsRequestDto.from_json(json)
# print the JSON string representation of the object
print(BulkDisableHostsRequestDto.to_json())

# convert the object into a dict
bulk_disable_hosts_request_dto_dict = bulk_disable_hosts_request_dto_instance.to_dict()
# create an instance of BulkDisableHostsRequestDto from a dict
bulk_disable_hosts_request_dto_from_dict = BulkDisableHostsRequestDto.from_dict(bulk_disable_hosts_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


