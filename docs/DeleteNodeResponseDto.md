# DeleteNodeResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**DeleteSubscriptionPageConfigResponseDtoResponse**](DeleteSubscriptionPageConfigResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.delete_node_response_dto import DeleteNodeResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteNodeResponseDto from a JSON string
delete_node_response_dto_instance = DeleteNodeResponseDto.from_json(json)
# print the JSON string representation of the object
print(DeleteNodeResponseDto.to_json())

# convert the object into a dict
delete_node_response_dto_dict = delete_node_response_dto_instance.to_dict()
# create an instance of DeleteNodeResponseDto from a dict
delete_node_response_dto_from_dict = DeleteNodeResponseDto.from_dict(delete_node_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


