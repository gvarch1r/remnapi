# GetExternalSquadsResponseDtoResponseExternalSquadsInnerCustomRemarks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expired_users** | **List[str]** |  | 
**limited_users** | **List[str]** |  | 
**disabled_users** | **List[str]** |  | 
**empty_hosts** | **List[str]** |  | 
**hwid_max_devices_exceeded** | **List[str]** |  | 
**hwid_not_supported** | **List[str]** |  | 

## Example

```python
from supn_remnawave_panel.models.get_external_squads_response_dto_response_external_squads_inner_custom_remarks import GetExternalSquadsResponseDtoResponseExternalSquadsInnerCustomRemarks

# TODO update the JSON string below
json = "{}"
# create an instance of GetExternalSquadsResponseDtoResponseExternalSquadsInnerCustomRemarks from a JSON string
get_external_squads_response_dto_response_external_squads_inner_custom_remarks_instance = GetExternalSquadsResponseDtoResponseExternalSquadsInnerCustomRemarks.from_json(json)
# print the JSON string representation of the object
print(GetExternalSquadsResponseDtoResponseExternalSquadsInnerCustomRemarks.to_json())

# convert the object into a dict
get_external_squads_response_dto_response_external_squads_inner_custom_remarks_dict = get_external_squads_response_dto_response_external_squads_inner_custom_remarks_instance.to_dict()
# create an instance of GetExternalSquadsResponseDtoResponseExternalSquadsInnerCustomRemarks from a dict
get_external_squads_response_dto_response_external_squads_inner_custom_remarks_from_dict = GetExternalSquadsResponseDtoResponseExternalSquadsInnerCustomRemarks.from_dict(get_external_squads_response_dto_response_external_squads_inner_custom_remarks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


