# EnableNodeResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateNodeResponseDtoResponse**](CreateNodeResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.enable_node_response_dto import EnableNodeResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of EnableNodeResponseDto from a JSON string
enable_node_response_dto_instance = EnableNodeResponseDto.from_json(json)
# print the JSON string representation of the object
print(EnableNodeResponseDto.to_json())

# convert the object into a dict
enable_node_response_dto_dict = enable_node_response_dto_instance.to_dict()
# create an instance of EnableNodeResponseDto from a dict
enable_node_response_dto_from_dict = EnableNodeResponseDto.from_dict(enable_node_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


