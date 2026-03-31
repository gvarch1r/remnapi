# SubscriptionsControllerGetSubscriptionByUsername404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | [optional] 
**path** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.subscriptions_controller_get_subscription_by_username404_response import SubscriptionsControllerGetSubscriptionByUsername404Response

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionsControllerGetSubscriptionByUsername404Response from a JSON string
subscriptions_controller_get_subscription_by_username404_response_instance = SubscriptionsControllerGetSubscriptionByUsername404Response.from_json(json)
# print the JSON string representation of the object
print(SubscriptionsControllerGetSubscriptionByUsername404Response.to_json())

# convert the object into a dict
subscriptions_controller_get_subscription_by_username404_response_dict = subscriptions_controller_get_subscription_by_username404_response_instance.to_dict()
# create an instance of SubscriptionsControllerGetSubscriptionByUsername404Response from a dict
subscriptions_controller_get_subscription_by_username404_response_from_dict = SubscriptionsControllerGetSubscriptionByUsername404Response.from_dict(subscriptions_controller_get_subscription_by_username404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


