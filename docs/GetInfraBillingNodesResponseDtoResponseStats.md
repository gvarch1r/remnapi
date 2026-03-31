# GetInfraBillingNodesResponseDtoResponseStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upcoming_nodes_count** | **float** |  | 
**current_month_payments** | **float** |  | 
**total_spent** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.get_infra_billing_nodes_response_dto_response_stats import GetInfraBillingNodesResponseDtoResponseStats

# TODO update the JSON string below
json = "{}"
# create an instance of GetInfraBillingNodesResponseDtoResponseStats from a JSON string
get_infra_billing_nodes_response_dto_response_stats_instance = GetInfraBillingNodesResponseDtoResponseStats.from_json(json)
# print the JSON string representation of the object
print(GetInfraBillingNodesResponseDtoResponseStats.to_json())

# convert the object into a dict
get_infra_billing_nodes_response_dto_response_stats_dict = get_infra_billing_nodes_response_dto_response_stats_instance.to_dict()
# create an instance of GetInfraBillingNodesResponseDtoResponseStats from a dict
get_infra_billing_nodes_response_dto_response_stats_from_dict = GetInfraBillingNodesResponseDtoResponseStats.from_dict(get_infra_billing_nodes_response_dto_response_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


