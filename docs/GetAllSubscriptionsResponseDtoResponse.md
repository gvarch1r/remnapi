# GetAllSubscriptionsResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriptions** | [**List[GetSubscriptionInfoResponseDtoResponse]**](GetSubscriptionInfoResponseDtoResponse.md) |  | 
**total** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.get_all_subscriptions_response_dto_response import GetAllSubscriptionsResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllSubscriptionsResponseDtoResponse from a JSON string
get_all_subscriptions_response_dto_response_instance = GetAllSubscriptionsResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllSubscriptionsResponseDtoResponse.to_json())

# convert the object into a dict
get_all_subscriptions_response_dto_response_dict = get_all_subscriptions_response_dto_response_instance.to_dict()
# create an instance of GetAllSubscriptionsResponseDtoResponse from a dict
get_all_subscriptions_response_dto_response_from_dict = GetAllSubscriptionsResponseDtoResponse.from_dict(get_all_subscriptions_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


