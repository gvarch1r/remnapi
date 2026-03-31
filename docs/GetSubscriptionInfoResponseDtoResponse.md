# GetSubscriptionInfoResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_found** | **bool** |  | 
**user** | [**GetSubscriptionInfoResponseDtoResponseUser**](GetSubscriptionInfoResponseDtoResponseUser.md) |  | 
**links** | **List[str]** |  | 
**ss_conf_links** | **Dict[str, str]** |  | 
**subscription_url** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.get_subscription_info_response_dto_response import GetSubscriptionInfoResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionInfoResponseDtoResponse from a JSON string
get_subscription_info_response_dto_response_instance = GetSubscriptionInfoResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionInfoResponseDtoResponse.to_json())

# convert the object into a dict
get_subscription_info_response_dto_response_dict = get_subscription_info_response_dto_response_instance.to_dict()
# create an instance of GetSubscriptionInfoResponseDtoResponse from a dict
get_subscription_info_response_dto_response_from_dict = GetSubscriptionInfoResponseDtoResponse.from_dict(get_subscription_info_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


