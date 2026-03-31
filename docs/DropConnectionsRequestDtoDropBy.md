# DropConnectionsRequestDtoDropBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**by** | **str** |  | 
**user_uuids** | **List[UUID]** |  | 
**ip_addresses** | **List[str]** |  | 

## Example

```python
from supn_remnawave_panel.models.drop_connections_request_dto_drop_by import DropConnectionsRequestDtoDropBy

# TODO update the JSON string below
json = "{}"
# create an instance of DropConnectionsRequestDtoDropBy from a JSON string
drop_connections_request_dto_drop_by_instance = DropConnectionsRequestDtoDropBy.from_json(json)
# print the JSON string representation of the object
print(DropConnectionsRequestDtoDropBy.to_json())

# convert the object into a dict
drop_connections_request_dto_drop_by_dict = drop_connections_request_dto_drop_by_instance.to_dict()
# create an instance of DropConnectionsRequestDtoDropBy from a dict
drop_connections_request_dto_drop_by_from_dict = DropConnectionsRequestDtoDropBy.from_dict(drop_connections_request_dto_drop_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


