# GetAllInboundsResponseDtoResponseInboundsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**profile_uuid** | **UUID** |  | 
**tag** | **str** |  | 
**type** | **str** |  | 
**network** | **str** |  | 
**security** | **str** |  | 
**port** | **float** |  | 
**raw_inbound** | **object** |  | 
**active_squads** | **List[UUID]** |  | 

## Example

```python
from supn_remnawave_panel.models.get_all_inbounds_response_dto_response_inbounds_inner import GetAllInboundsResponseDtoResponseInboundsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllInboundsResponseDtoResponseInboundsInner from a JSON string
get_all_inbounds_response_dto_response_inbounds_inner_instance = GetAllInboundsResponseDtoResponseInboundsInner.from_json(json)
# print the JSON string representation of the object
print(GetAllInboundsResponseDtoResponseInboundsInner.to_json())

# convert the object into a dict
get_all_inbounds_response_dto_response_inbounds_inner_dict = get_all_inbounds_response_dto_response_inbounds_inner_instance.to_dict()
# create an instance of GetAllInboundsResponseDtoResponseInboundsInner from a dict
get_all_inbounds_response_dto_response_inbounds_inner_from_dict = GetAllInboundsResponseDtoResponseInboundsInner.from_dict(get_all_inbounds_response_dto_response_inbounds_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


