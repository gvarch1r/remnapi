# CloneSubscriptionPageConfigRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clone_from_uuid** | **UUID** |  | 

## Example

```python
from supn_remnawave_panel.models.clone_subscription_page_config_request_dto import CloneSubscriptionPageConfigRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CloneSubscriptionPageConfigRequestDto from a JSON string
clone_subscription_page_config_request_dto_instance = CloneSubscriptionPageConfigRequestDto.from_json(json)
# print the JSON string representation of the object
print(CloneSubscriptionPageConfigRequestDto.to_json())

# convert the object into a dict
clone_subscription_page_config_request_dto_dict = clone_subscription_page_config_request_dto_instance.to_dict()
# create an instance of CloneSubscriptionPageConfigRequestDto from a dict
clone_subscription_page_config_request_dto_from_dict = CloneSubscriptionPageConfigRequestDto.from_dict(clone_subscription_page_config_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


