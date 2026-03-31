# ReorderNodeResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[CreateNodeResponseDtoResponse]**](CreateNodeResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.reorder_node_response_dto import ReorderNodeResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderNodeResponseDto from a JSON string
reorder_node_response_dto_instance = ReorderNodeResponseDto.from_json(json)
# print the JSON string representation of the object
print(ReorderNodeResponseDto.to_json())

# convert the object into a dict
reorder_node_response_dto_dict = reorder_node_response_dto_instance.to_dict()
# create an instance of ReorderNodeResponseDto from a dict
reorder_node_response_dto_from_dict = ReorderNodeResponseDto.from_dict(reorder_node_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


