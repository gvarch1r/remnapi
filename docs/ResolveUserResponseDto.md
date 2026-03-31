# ResolveUserResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ResolveUserResponseDtoResponse**](ResolveUserResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.resolve_user_response_dto import ResolveUserResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveUserResponseDto from a JSON string
resolve_user_response_dto_instance = ResolveUserResponseDto.from_json(json)
# print the JSON string representation of the object
print(ResolveUserResponseDto.to_json())

# convert the object into a dict
resolve_user_response_dto_dict = resolve_user_response_dto_instance.to_dict()
# create an instance of ResolveUserResponseDto from a dict
resolve_user_response_dto_from_dict = ResolveUserResponseDto.from_dict(resolve_user_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


