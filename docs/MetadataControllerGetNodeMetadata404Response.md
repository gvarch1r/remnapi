# MetadataControllerGetNodeMetadata404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.metadata_controller_get_node_metadata404_response import MetadataControllerGetNodeMetadata404Response

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataControllerGetNodeMetadata404Response from a JSON string
metadata_controller_get_node_metadata404_response_instance = MetadataControllerGetNodeMetadata404Response.from_json(json)
# print the JSON string representation of the object
print(MetadataControllerGetNodeMetadata404Response.to_json())

# convert the object into a dict
metadata_controller_get_node_metadata404_response_dict = metadata_controller_get_node_metadata404_response_instance.to_dict()
# create an instance of MetadataControllerGetNodeMetadata404Response from a dict
metadata_controller_get_node_metadata404_response_from_dict = MetadataControllerGetNodeMetadata404Response.from_dict(metadata_controller_get_node_metadata404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


