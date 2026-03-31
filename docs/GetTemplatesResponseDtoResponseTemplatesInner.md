# GetTemplatesResponseDtoResponseTemplatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**view_position** | **int** |  | 
**name** | **str** |  | 
**template_type** | **str** |  | 
**template_json** | **object** |  | 
**encoded_template_yaml** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.get_templates_response_dto_response_templates_inner import GetTemplatesResponseDtoResponseTemplatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTemplatesResponseDtoResponseTemplatesInner from a JSON string
get_templates_response_dto_response_templates_inner_instance = GetTemplatesResponseDtoResponseTemplatesInner.from_json(json)
# print the JSON string representation of the object
print(GetTemplatesResponseDtoResponseTemplatesInner.to_json())

# convert the object into a dict
get_templates_response_dto_response_templates_inner_dict = get_templates_response_dto_response_templates_inner_instance.to_dict()
# create an instance of GetTemplatesResponseDtoResponseTemplatesInner from a dict
get_templates_response_dto_response_templates_inner_from_dict = GetTemplatesResponseDtoResponseTemplatesInner.from_dict(get_templates_response_dto_response_templates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


