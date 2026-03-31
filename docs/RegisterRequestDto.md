# RegisterRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.register_request_dto import RegisterRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterRequestDto from a JSON string
register_request_dto_instance = RegisterRequestDto.from_json(json)
# print the JSON string representation of the object
print(RegisterRequestDto.to_json())

# convert the object into a dict
register_request_dto_dict = register_request_dto_instance.to_dict()
# create an instance of RegisterRequestDto from a dict
register_request_dto_from_dict = RegisterRequestDto.from_dict(register_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


