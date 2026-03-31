# UpdateTemplateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**name** | **str** |  | [optional] 
**template_json** | **object** |  | [optional] 
**encoded_template_yaml** | **str** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.update_template_request_dto import UpdateTemplateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTemplateRequestDto from a JSON string
update_template_request_dto_instance = UpdateTemplateRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateTemplateRequestDto.to_json())

# convert the object into a dict
update_template_request_dto_dict = update_template_request_dto_instance.to_dict()
# create an instance of UpdateTemplateRequestDto from a dict
update_template_request_dto_from_dict = UpdateTemplateRequestDto.from_dict(update_template_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


