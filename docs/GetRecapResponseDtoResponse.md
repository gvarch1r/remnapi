# GetRecapResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**this_month** | [**GetRecapResponseDtoResponseThisMonth**](GetRecapResponseDtoResponseThisMonth.md) |  | 
**total** | [**GetRecapResponseDtoResponseTotal**](GetRecapResponseDtoResponseTotal.md) |  | 
**version** | **str** |  | 
**init_date** | **datetime** |  | 

## Example

```python
from supn_remnawave_panel.models.get_recap_response_dto_response import GetRecapResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecapResponseDtoResponse from a JSON string
get_recap_response_dto_response_instance = GetRecapResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetRecapResponseDtoResponse.to_json())

# convert the object into a dict
get_recap_response_dto_response_dict = get_recap_response_dto_response_instance.to_dict()
# create an instance of GetRecapResponseDtoResponse from a dict
get_recap_response_dto_response_from_dict = GetRecapResponseDtoResponse.from_dict(get_recap_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


