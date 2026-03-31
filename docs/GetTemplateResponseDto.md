# GetTemplateResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetTemplatesResponseDtoResponseTemplatesInner**](GetTemplatesResponseDtoResponseTemplatesInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_template_response_dto import GetTemplateResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetTemplateResponseDto from a JSON string
get_template_response_dto_instance = GetTemplateResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetTemplateResponseDto.to_json())

# convert the object into a dict
get_template_response_dto_dict = get_template_response_dto_instance.to_dict()
# create an instance of GetTemplateResponseDto from a dict
get_template_response_dto_from_dict = GetTemplateResponseDto.from_dict(get_template_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


