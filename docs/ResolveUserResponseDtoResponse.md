# ResolveUserResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**username** | **str** |  | 
**id** | **float** |  | 
**short_uuid** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.resolve_user_response_dto_response import ResolveUserResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveUserResponseDtoResponse from a JSON string
resolve_user_response_dto_response_instance = ResolveUserResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(ResolveUserResponseDtoResponse.to_json())

# convert the object into a dict
resolve_user_response_dto_response_dict = resolve_user_response_dto_response_instance.to_dict()
# create an instance of ResolveUserResponseDtoResponse from a dict
resolve_user_response_dto_response_from_dict = ResolveUserResponseDtoResponse.from_dict(resolve_user_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


