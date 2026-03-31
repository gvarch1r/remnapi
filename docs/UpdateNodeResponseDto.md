# UpdateNodeResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateNodeResponseDtoResponse**](CreateNodeResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.update_node_response_dto import UpdateNodeResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNodeResponseDto from a JSON string
update_node_response_dto_instance = UpdateNodeResponseDto.from_json(json)
# print the JSON string representation of the object
print(UpdateNodeResponseDto.to_json())

# convert the object into a dict
update_node_response_dto_dict = update_node_response_dto_instance.to_dict()
# create an instance of UpdateNodeResponseDto from a dict
update_node_response_dto_from_dict = UpdateNodeResponseDto.from_dict(update_node_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


