# SetInboundToManyHostsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[CreateHostResponseDtoResponse]**](CreateHostResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.set_inbound_to_many_hosts_response_dto import SetInboundToManyHostsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetInboundToManyHostsResponseDto from a JSON string
set_inbound_to_many_hosts_response_dto_instance = SetInboundToManyHostsResponseDto.from_json(json)
# print the JSON string representation of the object
print(SetInboundToManyHostsResponseDto.to_json())

# convert the object into a dict
set_inbound_to_many_hosts_response_dto_dict = set_inbound_to_many_hosts_response_dto_instance.to_dict()
# create an instance of SetInboundToManyHostsResponseDto from a dict
set_inbound_to_many_hosts_response_dto_from_dict = SetInboundToManyHostsResponseDto.from_dict(set_inbound_to_many_hosts_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


