# SetPortToManyHostsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[CreateHostResponseDtoResponse]**](CreateHostResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.set_port_to_many_hosts_response_dto import SetPortToManyHostsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetPortToManyHostsResponseDto from a JSON string
set_port_to_many_hosts_response_dto_instance = SetPortToManyHostsResponseDto.from_json(json)
# print the JSON string representation of the object
print(SetPortToManyHostsResponseDto.to_json())

# convert the object into a dict
set_port_to_many_hosts_response_dto_dict = set_port_to_many_hosts_response_dto_instance.to_dict()
# create an instance of SetPortToManyHostsResponseDto from a dict
set_port_to_many_hosts_response_dto_from_dict = SetPortToManyHostsResponseDto.from_dict(set_port_to_many_hosts_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


