# ReorderConfigProfilesRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ReorderSubscriptionPageConfigsRequestDtoItemsInner]**](ReorderSubscriptionPageConfigsRequestDtoItemsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.reorder_config_profiles_request_dto import ReorderConfigProfilesRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReorderConfigProfilesRequestDto from a JSON string
reorder_config_profiles_request_dto_instance = ReorderConfigProfilesRequestDto.from_json(json)
# print the JSON string representation of the object
print(ReorderConfigProfilesRequestDto.to_json())

# convert the object into a dict
reorder_config_profiles_request_dto_dict = reorder_config_profiles_request_dto_instance.to_dict()
# create an instance of ReorderConfigProfilesRequestDto from a dict
reorder_config_profiles_request_dto_from_dict = ReorderConfigProfilesRequestDto.from_dict(reorder_config_profiles_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


