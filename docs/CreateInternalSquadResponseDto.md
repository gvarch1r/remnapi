# CreateInternalSquadResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetInternalSquadsResponseDtoResponseInternalSquadsInner**](GetInternalSquadsResponseDtoResponseInternalSquadsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_internal_squad_response_dto import CreateInternalSquadResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInternalSquadResponseDto from a JSON string
create_internal_squad_response_dto_instance = CreateInternalSquadResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreateInternalSquadResponseDto.to_json())

# convert the object into a dict
create_internal_squad_response_dto_dict = create_internal_squad_response_dto_instance.to_dict()
# create an instance of CreateInternalSquadResponseDto from a dict
create_internal_squad_response_dto_from_dict = CreateInternalSquadResponseDto.from_dict(create_internal_squad_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


