# GetExternalSquadsResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**external_squads** | [**List[GetExternalSquadsResponseDtoResponseExternalSquadsInner]**](GetExternalSquadsResponseDtoResponseExternalSquadsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_external_squads_response_dto_response import GetExternalSquadsResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetExternalSquadsResponseDtoResponse from a JSON string
get_external_squads_response_dto_response_instance = GetExternalSquadsResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetExternalSquadsResponseDtoResponse.to_json())

# convert the object into a dict
get_external_squads_response_dto_response_dict = get_external_squads_response_dto_response_instance.to_dict()
# create an instance of GetExternalSquadsResponseDtoResponse from a dict
get_external_squads_response_dto_response_from_dict = GetExternalSquadsResponseDtoResponse.from_dict(get_external_squads_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


