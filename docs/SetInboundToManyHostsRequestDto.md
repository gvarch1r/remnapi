# SetInboundToManyHostsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[UUID]** |  | 
**config_profile_uuid** | **UUID** |  | 
**config_profile_inbound_uuid** | **UUID** |  | 

## Example

```python
from supn_remnawave_panel.models.set_inbound_to_many_hosts_request_dto import SetInboundToManyHostsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetInboundToManyHostsRequestDto from a JSON string
set_inbound_to_many_hosts_request_dto_instance = SetInboundToManyHostsRequestDto.from_json(json)
# print the JSON string representation of the object
print(SetInboundToManyHostsRequestDto.to_json())

# convert the object into a dict
set_inbound_to_many_hosts_request_dto_dict = set_inbound_to_many_hosts_request_dto_instance.to_dict()
# create an instance of SetInboundToManyHostsRequestDto from a dict
set_inbound_to_many_hosts_request_dto_from_dict = SetInboundToManyHostsRequestDto.from_dict(set_inbound_to_many_hosts_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


