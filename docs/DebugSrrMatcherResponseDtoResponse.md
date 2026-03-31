# DebugSrrMatcherResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matched** | **bool** |  | 
**response_type** | **str** |  | 
**matched_rule** | [**DebugSrrMatcherResponseDtoResponseMatchedRule**](DebugSrrMatcherResponseDtoResponseMatchedRule.md) |  | 
**input_headers** | **Dict[str, str]** |  | 
**output_headers** | **Dict[str, str]** |  | 

## Example

```python
from supn_remnawave_panel.models.debug_srr_matcher_response_dto_response import DebugSrrMatcherResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DebugSrrMatcherResponseDtoResponse from a JSON string
debug_srr_matcher_response_dto_response_instance = DebugSrrMatcherResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(DebugSrrMatcherResponseDtoResponse.to_json())

# convert the object into a dict
debug_srr_matcher_response_dto_response_dict = debug_srr_matcher_response_dto_response_instance.to_dict()
# create an instance of DebugSrrMatcherResponseDtoResponse from a dict
debug_srr_matcher_response_dto_response_from_dict = DebugSrrMatcherResponseDtoResponse.from_dict(debug_srr_matcher_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


