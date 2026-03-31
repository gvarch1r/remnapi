# CreateHostResponseDtoResponseInbound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_profile_uuid** | **UUID** |  | 
**config_profile_inbound_uuid** | **UUID** |  | 

## Example

```python
from supn_remnawave_panel.models.create_host_response_dto_response_inbound import CreateHostResponseDtoResponseInbound

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHostResponseDtoResponseInbound from a JSON string
create_host_response_dto_response_inbound_instance = CreateHostResponseDtoResponseInbound.from_json(json)
# print the JSON string representation of the object
print(CreateHostResponseDtoResponseInbound.to_json())

# convert the object into a dict
create_host_response_dto_response_inbound_dict = create_host_response_dto_response_inbound_instance.to_dict()
# create an instance of CreateHostResponseDtoResponseInbound from a dict
create_host_response_dto_response_inbound_from_dict = CreateHostResponseDtoResponseInbound.from_dict(create_host_response_dto_response_inbound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


