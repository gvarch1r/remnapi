# BulkNodesUpdateRequestDtoFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | [optional] 
**consumption_multiplier** | **float** |  | [optional] 
**provider_uuid** | **UUID** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**active_plugin_uuid** | **UUID** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.bulk_nodes_update_request_dto_fields import BulkNodesUpdateRequestDtoFields

# TODO update the JSON string below
json = "{}"
# create an instance of BulkNodesUpdateRequestDtoFields from a JSON string
bulk_nodes_update_request_dto_fields_instance = BulkNodesUpdateRequestDtoFields.from_json(json)
# print the JSON string representation of the object
print(BulkNodesUpdateRequestDtoFields.to_json())

# convert the object into a dict
bulk_nodes_update_request_dto_fields_dict = bulk_nodes_update_request_dto_fields_instance.to_dict()
# create an instance of BulkNodesUpdateRequestDtoFields from a dict
bulk_nodes_update_request_dto_fields_from_dict = BulkNodesUpdateRequestDtoFields.from_dict(bulk_nodes_update_request_dto_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


