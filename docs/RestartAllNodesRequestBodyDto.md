# RestartAllNodesRequestBodyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_restart** | **bool** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.restart_all_nodes_request_body_dto import RestartAllNodesRequestBodyDto

# TODO update the JSON string below
json = "{}"
# create an instance of RestartAllNodesRequestBodyDto from a JSON string
restart_all_nodes_request_body_dto_instance = RestartAllNodesRequestBodyDto.from_json(json)
# print the JSON string representation of the object
print(RestartAllNodesRequestBodyDto.to_json())

# convert the object into a dict
restart_all_nodes_request_body_dto_dict = restart_all_nodes_request_body_dto_instance.to_dict()
# create an instance of RestartAllNodesRequestBodyDto from a dict
restart_all_nodes_request_body_dto_from_dict = RestartAllNodesRequestBodyDto.from_dict(restart_all_nodes_request_body_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


