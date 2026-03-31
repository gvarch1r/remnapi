# GetInfraBillingNodesResponseDtoResponseBillingNodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**node_uuid** | **UUID** |  | 
**provider_uuid** | **UUID** |  | 
**provider** | [**GetInfraBillingNodesResponseDtoResponseBillingNodesInnerProvider**](GetInfraBillingNodesResponseDtoResponseBillingNodesInnerProvider.md) |  | 
**node** | [**GetConfigProfilesResponseDtoResponseConfigProfilesInnerNodesInner**](GetConfigProfilesResponseDtoResponseConfigProfilesInnerNodesInner.md) |  | 
**next_billing_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from supn_remnawave_panel.models.get_infra_billing_nodes_response_dto_response_billing_nodes_inner import GetInfraBillingNodesResponseDtoResponseBillingNodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInfraBillingNodesResponseDtoResponseBillingNodesInner from a JSON string
get_infra_billing_nodes_response_dto_response_billing_nodes_inner_instance = GetInfraBillingNodesResponseDtoResponseBillingNodesInner.from_json(json)
# print the JSON string representation of the object
print(GetInfraBillingNodesResponseDtoResponseBillingNodesInner.to_json())

# convert the object into a dict
get_infra_billing_nodes_response_dto_response_billing_nodes_inner_dict = get_infra_billing_nodes_response_dto_response_billing_nodes_inner_instance.to_dict()
# create an instance of GetInfraBillingNodesResponseDtoResponseBillingNodesInner from a dict
get_infra_billing_nodes_response_dto_response_billing_nodes_inner_from_dict = GetInfraBillingNodesResponseDtoResponseBillingNodesInner.from_dict(get_infra_billing_nodes_response_dto_response_billing_nodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


