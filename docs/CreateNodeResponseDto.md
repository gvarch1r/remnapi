# CreateNodeResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateNodeResponseDtoResponse**](CreateNodeResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_node_response_dto import CreateNodeResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNodeResponseDto from a JSON string
create_node_response_dto_instance = CreateNodeResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreateNodeResponseDto.to_json())

# convert the object into a dict
create_node_response_dto_dict = create_node_response_dto_instance.to_dict()
# create an instance of CreateNodeResponseDto from a dict
create_node_response_dto_from_dict = CreateNodeResponseDto.from_dict(create_node_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


