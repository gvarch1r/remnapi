# ResolveUserRequestBodyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | [optional] 
**id** | **float** |  | [optional] 
**short_uuid** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.resolve_user_request_body_dto import ResolveUserRequestBodyDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveUserRequestBodyDto from a JSON string
resolve_user_request_body_dto_instance = ResolveUserRequestBodyDto.from_json(json)
# print the JSON string representation of the object
print(ResolveUserRequestBodyDto.to_json())

# convert the object into a dict
resolve_user_request_body_dto_dict = resolve_user_request_body_dto_instance.to_dict()
# create an instance of ResolveUserRequestBodyDto from a dict
resolve_user_request_body_dto_from_dict = ResolveUserRequestBodyDto.from_dict(resolve_user_request_body_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


