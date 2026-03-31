# CreateExternalSquadResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetExternalSquadsResponseDtoResponseExternalSquadsInner**](GetExternalSquadsResponseDtoResponseExternalSquadsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_external_squad_response_dto import CreateExternalSquadResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExternalSquadResponseDto from a JSON string
create_external_squad_response_dto_instance = CreateExternalSquadResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreateExternalSquadResponseDto.to_json())

# convert the object into a dict
create_external_squad_response_dto_dict = create_external_squad_response_dto_instance.to_dict()
# create an instance of CreateExternalSquadResponseDto from a dict
create_external_squad_response_dto_from_dict = CreateExternalSquadResponseDto.from_dict(create_external_squad_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


