# UpdateExternalSquadResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetExternalSquadsResponseDtoResponseExternalSquadsInner**](GetExternalSquadsResponseDtoResponseExternalSquadsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.update_external_squad_response_dto import UpdateExternalSquadResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExternalSquadResponseDto from a JSON string
update_external_squad_response_dto_instance = UpdateExternalSquadResponseDto.from_json(json)
# print the JSON string representation of the object
print(UpdateExternalSquadResponseDto.to_json())

# convert the object into a dict
update_external_squad_response_dto_dict = update_external_squad_response_dto_instance.to_dict()
# create an instance of UpdateExternalSquadResponseDto from a dict
update_external_squad_response_dto_from_dict = UpdateExternalSquadResponseDto.from_dict(update_external_squad_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


