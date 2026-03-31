# BulkDisableHostsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[CreateHostResponseDtoResponse]**](CreateHostResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.bulk_disable_hosts_response_dto import BulkDisableHostsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDisableHostsResponseDto from a JSON string
bulk_disable_hosts_response_dto_instance = BulkDisableHostsResponseDto.from_json(json)
# print the JSON string representation of the object
print(BulkDisableHostsResponseDto.to_json())

# convert the object into a dict
bulk_disable_hosts_response_dto_dict = bulk_disable_hosts_response_dto_instance.to_dict()
# create an instance of BulkDisableHostsResponseDto from a dict
bulk_disable_hosts_response_dto_from_dict = BulkDisableHostsResponseDto.from_dict(bulk_disable_hosts_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


