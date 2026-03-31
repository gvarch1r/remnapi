# RegisterResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**LoginResponseDtoResponse**](LoginResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.register_response_dto import RegisterResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterResponseDto from a JSON string
register_response_dto_instance = RegisterResponseDto.from_json(json)
# print the JSON string representation of the object
print(RegisterResponseDto.to_json())

# convert the object into a dict
register_response_dto_dict = register_response_dto_instance.to_dict()
# create an instance of RegisterResponseDto from a dict
register_response_dto_from_dict = RegisterResponseDto.from_dict(register_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


