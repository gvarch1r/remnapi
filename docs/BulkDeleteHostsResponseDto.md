# BulkDeleteHostsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[CreateHostResponseDtoResponse]**](CreateHostResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_delete_hosts_response_dto import BulkDeleteHostsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteHostsResponseDto from a JSON string
bulk_delete_hosts_response_dto_instance = BulkDeleteHostsResponseDto.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteHostsResponseDto.to_json())

# convert the object into a dict
bulk_delete_hosts_response_dto_dict = bulk_delete_hosts_response_dto_instance.to_dict()
# create an instance of BulkDeleteHostsResponseDto from a dict
bulk_delete_hosts_response_dto_from_dict = BulkDeleteHostsResponseDto.from_dict(bulk_delete_hosts_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


