# DropConnectionsRequestDtoDropByOneOf

Drop by user UUIDs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**by** | **str** |  | 
**user_uuids** | **List[UUID]** |  | 

## Example

```python
from supn_remnawave_panel.models.drop_connections_request_dto_drop_by_one_of import DropConnectionsRequestDtoDropByOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of DropConnectionsRequestDtoDropByOneOf from a JSON string
drop_connections_request_dto_drop_by_one_of_instance = DropConnectionsRequestDtoDropByOneOf.from_json(json)
# print the JSON string representation of the object
print(DropConnectionsRequestDtoDropByOneOf.to_json())

# convert the object into a dict
drop_connections_request_dto_drop_by_one_of_dict = drop_connections_request_dto_drop_by_one_of_instance.to_dict()
# create an instance of DropConnectionsRequestDtoDropByOneOf from a dict
drop_connections_request_dto_drop_by_one_of_from_dict = DropConnectionsRequestDtoDropByOneOf.from_dict(drop_connections_request_dto_drop_by_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


