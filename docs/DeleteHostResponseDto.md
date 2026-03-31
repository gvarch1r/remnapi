# DeleteHostResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**DeleteSubscriptionPageConfigResponseDtoResponse**](DeleteSubscriptionPageConfigResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.delete_host_response_dto import DeleteHostResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteHostResponseDto from a JSON string
delete_host_response_dto_instance = DeleteHostResponseDto.from_json(json)
# print the JSON string representation of the object
print(DeleteHostResponseDto.to_json())

# convert the object into a dict
delete_host_response_dto_dict = delete_host_response_dto_instance.to_dict()
# create an instance of DeleteHostResponseDto from a dict
delete_host_response_dto_from_dict = DeleteHostResponseDto.from_dict(delete_host_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


