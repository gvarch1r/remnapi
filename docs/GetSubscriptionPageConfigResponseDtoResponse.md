# GetSubscriptionPageConfigResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**view_position** | **int** |  | 
**name** | **str** |  | 
**config** | **object** |  | 

## Example

```python
from supn_remnawave_panel.models.get_subscription_page_config_response_dto_response import GetSubscriptionPageConfigResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionPageConfigResponseDtoResponse from a JSON string
get_subscription_page_config_response_dto_response_instance = GetSubscriptionPageConfigResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionPageConfigResponseDtoResponse.to_json())

# convert the object into a dict
get_subscription_page_config_response_dto_response_dict = get_subscription_page_config_response_dto_response_instance.to_dict()
# create an instance of GetSubscriptionPageConfigResponseDtoResponse from a dict
get_subscription_page_config_response_dto_response_from_dict = GetSubscriptionPageConfigResponseDtoResponse.from_dict(get_subscription_page_config_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


