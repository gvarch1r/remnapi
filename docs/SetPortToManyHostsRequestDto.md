# SetPortToManyHostsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[UUID]** |  | 
**port** | **int** |  | 

## Example

```python
from supn_remnawave_panel.models.set_port_to_many_hosts_request_dto import SetPortToManyHostsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetPortToManyHostsRequestDto from a JSON string
set_port_to_many_hosts_request_dto_instance = SetPortToManyHostsRequestDto.from_json(json)
# print the JSON string representation of the object
print(SetPortToManyHostsRequestDto.to_json())

# convert the object into a dict
set_port_to_many_hosts_request_dto_dict = set_port_to_many_hosts_request_dto_instance.to_dict()
# create an instance of SetPortToManyHostsRequestDto from a dict
set_port_to_many_hosts_request_dto_from_dict = SetPortToManyHostsRequestDto.from_dict(set_port_to_many_hosts_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


