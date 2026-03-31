# GetInternalSquadsResponseDtoResponseInternalSquadsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**view_position** | **int** |  | 
**name** | **str** |  | 
**info** | [**GetInternalSquadsResponseDtoResponseInternalSquadsInnerInfo**](GetInternalSquadsResponseDtoResponseInternalSquadsInnerInfo.md) |  | 
**inbounds** | [**List[GetConfigProfilesResponseDtoResponseConfigProfilesInnerInboundsInner]**](GetConfigProfilesResponseDtoResponseConfigProfilesInnerInboundsInner.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from supn_remnawave_panel.models.get_internal_squads_response_dto_response_internal_squads_inner import GetInternalSquadsResponseDtoResponseInternalSquadsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInternalSquadsResponseDtoResponseInternalSquadsInner from a JSON string
get_internal_squads_response_dto_response_internal_squads_inner_instance = GetInternalSquadsResponseDtoResponseInternalSquadsInner.from_json(json)
# print the JSON string representation of the object
print(GetInternalSquadsResponseDtoResponseInternalSquadsInner.to_json())

# convert the object into a dict
get_internal_squads_response_dto_response_internal_squads_inner_dict = get_internal_squads_response_dto_response_internal_squads_inner_instance.to_dict()
# create an instance of GetInternalSquadsResponseDtoResponseInternalSquadsInner from a dict
get_internal_squads_response_dto_response_internal_squads_inner_from_dict = GetInternalSquadsResponseDtoResponseInternalSquadsInner.from_dict(get_internal_squads_response_dto_response_internal_squads_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


