# GetTemplatesResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**templates** | [**List[GetTemplatesResponseDtoResponseTemplatesInner]**](GetTemplatesResponseDtoResponseTemplatesInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_templates_response_dto_response import GetTemplatesResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTemplatesResponseDtoResponse from a JSON string
get_templates_response_dto_response_instance = GetTemplatesResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetTemplatesResponseDtoResponse.to_json())

# convert the object into a dict
get_templates_response_dto_response_dict = get_templates_response_dto_response_instance.to_dict()
# create an instance of GetTemplatesResponseDtoResponse from a dict
get_templates_response_dto_response_from_dict = GetTemplatesResponseDtoResponse.from_dict(get_templates_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


