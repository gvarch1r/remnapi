# CreateSubscriptionTemplateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**template_type** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.create_subscription_template_request_dto import CreateSubscriptionTemplateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionTemplateRequestDto from a JSON string
create_subscription_template_request_dto_instance = CreateSubscriptionTemplateRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateSubscriptionTemplateRequestDto.to_json())

# convert the object into a dict
create_subscription_template_request_dto_dict = create_subscription_template_request_dto_instance.to_dict()
# create an instance of CreateSubscriptionTemplateRequestDto from a dict
create_subscription_template_request_dto_from_dict = CreateSubscriptionTemplateRequestDto.from_dict(create_subscription_template_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


