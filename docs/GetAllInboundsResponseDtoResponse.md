# GetAllInboundsResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | 
**inbounds** | [**List[GetAllInboundsResponseDtoResponseInboundsInner]**](GetAllInboundsResponseDtoResponseInboundsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_all_inbounds_response_dto_response import GetAllInboundsResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllInboundsResponseDtoResponse from a JSON string
get_all_inbounds_response_dto_response_instance = GetAllInboundsResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllInboundsResponseDtoResponse.to_json())

# convert the object into a dict
get_all_inbounds_response_dto_response_dict = get_all_inbounds_response_dto_response_instance.to_dict()
# create an instance of GetAllInboundsResponseDtoResponse from a dict
get_all_inbounds_response_dto_response_from_dict = GetAllInboundsResponseDtoResponse.from_dict(get_all_inbounds_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


