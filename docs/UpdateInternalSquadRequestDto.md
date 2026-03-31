# UpdateInternalSquadRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **UUID** |  | 
**name** | **str** |  | [optional] 
**inbounds** | **List[UUID]** |  | [optional] 

## Example

```python
from supn_remnawave_panel.models.update_internal_squad_request_dto import UpdateInternalSquadRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInternalSquadRequestDto from a JSON string
update_internal_squad_request_dto_instance = UpdateInternalSquadRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateInternalSquadRequestDto.to_json())

# convert the object into a dict
update_internal_squad_request_dto_dict = update_internal_squad_request_dto_instance.to_dict()
# create an instance of UpdateInternalSquadRequestDto from a dict
update_internal_squad_request_dto_from_dict = UpdateInternalSquadRequestDto.from_dict(update_internal_squad_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


