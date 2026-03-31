# GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerTransportOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | [**GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerTransportOptionsOneOfHeader**](GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerTransportOptionsOneOfHeader.md) |  | 
**path** | **str** |  | 
**host** | **str** |  | 
**mode** | **str** |  | 
**extra** | **Dict[str, object]** |  | 
**headers** | **Dict[str, str]** |  | 
**heartbeat_period** | **float** |  | 
**authority** | **str** |  | 
**service_name** | **str** |  | 
**multi_mode** | **bool** |  | 
**client_mtu** | **int** |  | 
**tti** | **int** |  | 
**congestion** | **bool** |  | 
**version** | **int** |  | 
**auth** | **str** |  | 

## Example

```python
from supn_remnawave_panel.models.get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_transport_options import GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerTransportOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerTransportOptions from a JSON string
get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_transport_options_instance = GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerTransportOptions.from_json(json)
# print the JSON string representation of the object
print(GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerTransportOptions.to_json())

# convert the object into a dict
get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_transport_options_dict = get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_transport_options_instance.to_dict()
# create an instance of GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerTransportOptions from a dict
get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_transport_options_from_dict = GetRawSubscriptionByShortUuidResponseDtoResponseResolvedProxyConfigsInnerTransportOptions.from_dict(get_raw_subscription_by_short_uuid_response_dto_response_resolved_proxy_configs_inner_transport_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


