# CreateHostResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CreateHostResponseDtoResponse**](CreateHostResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.create_host_response_dto import CreateHostResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHostResponseDto from a JSON string
create_host_response_dto_instance = CreateHostResponseDto.from_json(json)
# print the JSON string representation of the object
print(CreateHostResponseDto.to_json())

# convert the object into a dict
create_host_response_dto_dict = create_host_response_dto_instance.to_dict()
# create an instance of CreateHostResponseDto from a dict
create_host_response_dto_from_dict = CreateHostResponseDto.from_dict(create_host_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


