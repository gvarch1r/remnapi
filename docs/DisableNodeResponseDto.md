# DisableNodeResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateNodeResponseDtoResponse**](CreateNodeResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.disable_node_response_dto import DisableNodeResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DisableNodeResponseDto from a JSON string
disable_node_response_dto_instance = DisableNodeResponseDto.from_json(json)
# print the JSON string representation of the object
print(DisableNodeResponseDto.to_json())

# convert the object into a dict
disable_node_response_dto_dict = disable_node_response_dto_instance.to_dict()
# create an instance of DisableNodeResponseDto from a dict
disable_node_response_dto_from_dict = DisableNodeResponseDto.from_dict(disable_node_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


