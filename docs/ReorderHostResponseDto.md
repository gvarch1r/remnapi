# ReorderHostResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ReorderHostResponseDtoResponse**](ReorderHostResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.reorder_host_response_dto import ReorderHostResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderHostResponseDto from a JSON string
reorder_host_response_dto_instance = ReorderHostResponseDto.from_json(json)
# print the JSON string representation of the object
print(ReorderHostResponseDto.to_json())

# convert the object into a dict
reorder_host_response_dto_dict = reorder_host_response_dto_instance.to_dict()
# create an instance of ReorderHostResponseDto from a dict
reorder_host_response_dto_from_dict = ReorderHostResponseDto.from_dict(reorder_host_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


