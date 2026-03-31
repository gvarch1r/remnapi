# UpdateTemplateResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetTemplatesResponseDtoResponseTemplatesInner**](GetTemplatesResponseDtoResponseTemplatesInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.update_template_response_dto import UpdateTemplateResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTemplateResponseDto from a JSON string
update_template_response_dto_instance = UpdateTemplateResponseDto.from_json(json)
# print the JSON string representation of the object
print(UpdateTemplateResponseDto.to_json())

# convert the object into a dict
update_template_response_dto_dict = update_template_response_dto_instance.to_dict()
# create an instance of UpdateTemplateResponseDto from a dict
update_template_response_dto_from_dict = UpdateTemplateResponseDto.from_dict(update_template_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


