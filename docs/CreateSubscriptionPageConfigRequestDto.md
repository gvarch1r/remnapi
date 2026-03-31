# CreateSubscriptionPageConfigRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.create_subscription_page_config_request_dto import CreateSubscriptionPageConfigRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionPageConfigRequestDto from a JSON string
create_subscription_page_config_request_dto_instance = CreateSubscriptionPageConfigRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateSubscriptionPageConfigRequestDto.to_json())

# convert the object into a dict
create_subscription_page_config_request_dto_dict = create_subscription_page_config_request_dto_instance.to_dict()
# create an instance of CreateSubscriptionPageConfigRequestDto from a dict
create_subscription_page_config_request_dto_from_dict = CreateSubscriptionPageConfigRequestDto.from_dict(create_subscription_page_config_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


