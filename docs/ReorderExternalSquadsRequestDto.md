# ReorderExternalSquadsRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ReorderSubscriptionPageConfigsRequestDtoItemsInner]**](ReorderSubscriptionPageConfigsRequestDtoItemsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.reorder_external_squads_request_dto import ReorderExternalSquadsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderExternalSquadsRequestDto from a JSON string
reorder_external_squads_request_dto_instance = ReorderExternalSquadsRequestDto.from_json(json)
# print the JSON string representation of the object
print(ReorderExternalSquadsRequestDto.to_json())

# convert the object into a dict
reorder_external_squads_request_dto_dict = reorder_external_squads_request_dto_instance.to_dict()
# create an instance of ReorderExternalSquadsRequestDto from a dict
reorder_external_squads_request_dto_from_dict = ReorderExternalSquadsRequestDto.from_dict(reorder_external_squads_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


