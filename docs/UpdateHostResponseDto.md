# UpdateHostResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateHostResponseDtoResponse**](CreateHostResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.update_host_response_dto import UpdateHostResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHostResponseDto from a JSON string
update_host_response_dto_instance = UpdateHostResponseDto.from_json(json)
# print the JSON string representation of the object
print(UpdateHostResponseDto.to_json())

# convert the object into a dict
update_host_response_dto_dict = update_host_response_dto_instance.to_dict()
# create an instance of UpdateHostResponseDto from a dict
update_host_response_dto_from_dict = UpdateHostResponseDto.from_dict(update_host_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


