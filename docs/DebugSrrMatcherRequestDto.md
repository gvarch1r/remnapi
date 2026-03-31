# DebugSrrMatcherRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_rules** | [**DebugSrrMatcherRequestDtoResponseRules**](DebugSrrMatcherRequestDtoResponseRules.md) |  | 

## Example

```python
from supn_remnawave_panel.models.debug_srr_matcher_request_dto import DebugSrrMatcherRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DebugSrrMatcherRequestDto from a JSON string
debug_srr_matcher_request_dto_instance = DebugSrrMatcherRequestDto.from_json(json)
# print the JSON string representation of the object
print(DebugSrrMatcherRequestDto.to_json())

# convert the object into a dict
debug_srr_matcher_request_dto_dict = debug_srr_matcher_request_dto_instance.to_dict()
# create an instance of DebugSrrMatcherRequestDto from a dict
debug_srr_matcher_request_dto_from_dict = DebugSrrMatcherRequestDto.from_dict(debug_srr_matcher_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


