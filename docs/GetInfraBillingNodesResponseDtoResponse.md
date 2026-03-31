# GetInfraBillingNodesResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_billing_nodes** | **float** |  | 
**billing_nodes** | [**List[GetInfraBillingNodesResponseDtoResponseBillingNodesInner]**](GetInfraBillingNodesResponseDtoResponseBillingNodesInner.md) |  | 
**available_billing_nodes** | [**List[GetConfigProfilesResponseDtoResponseConfigProfilesInnerNodesInner]**](GetConfigProfilesResponseDtoResponseConfigProfilesInnerNodesInner.md) |  | 
**total_available_billing_nodes** | **float** |  | 
**stats** | [**GetInfraBillingNodesResponseDtoResponseStats**](GetInfraBillingNodesResponseDtoResponseStats.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_infra_billing_nodes_response_dto_response import GetInfraBillingNodesResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInfraBillingNodesResponseDtoResponse from a JSON string
get_infra_billing_nodes_response_dto_response_instance = GetInfraBillingNodesResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetInfraBillingNodesResponseDtoResponse.to_json())

# convert the object into a dict
get_infra_billing_nodes_response_dto_response_dict = get_infra_billing_nodes_response_dto_response_instance.to_dict()
# create an instance of GetInfraBillingNodesResponseDtoResponse from a dict
get_infra_billing_nodes_response_dto_response_from_dict = GetInfraBillingNodesResponseDtoResponse.from_dict(get_infra_billing_nodes_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


