# UpdateInternalSquadResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetInternalSquadsResponseDtoResponseInternalSquadsInner**](GetInternalSquadsResponseDtoResponseInternalSquadsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.update_internal_squad_response_dto import UpdateInternalSquadResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInternalSquadResponseDto from a JSON string
update_internal_squad_response_dto_instance = UpdateInternalSquadResponseDto.from_json(json)
# print the JSON string representation of the object
print(UpdateInternalSquadResponseDto.to_json())

# convert the object into a dict
update_internal_squad_response_dto_dict = update_internal_squad_response_dto_instance.to_dict()
# create an instance of UpdateInternalSquadResponseDto from a dict
update_internal_squad_response_dto_from_dict = UpdateInternalSquadResponseDto.from_dict(update_internal_squad_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


