# CreateInternalSquadRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**inbounds** | **List[UUID]** |  | 

## Example

```python
from supn_remnawave_panel.models.create_internal_squad_request_dto import CreateInternalSquadRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInternalSquadRequestDto from a JSON string
create_internal_squad_request_dto_instance = CreateInternalSquadRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateInternalSquadRequestDto.to_json())

# convert the object into a dict
create_internal_squad_request_dto_dict = create_internal_squad_request_dto_instance.to_dict()
# create an instance of CreateInternalSquadRequestDto from a dict
create_internal_squad_request_dto_from_dict = CreateInternalSquadRequestDto.from_dict(create_internal_squad_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


