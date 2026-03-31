# GetMetadataResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**build** | [**GetMetadataResponseDtoResponseBuild**](GetMetadataResponseDtoResponseBuild.md) |  | 
**git** | [**GetMetadataResponseDtoResponseGit**](GetMetadataResponseDtoResponseGit.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_metadata_response_dto_response import GetMetadataResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetadataResponseDtoResponse from a JSON string
get_metadata_response_dto_response_instance = GetMetadataResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetMetadataResponseDtoResponse.to_json())

# convert the object into a dict
get_metadata_response_dto_response_dict = get_metadata_response_dto_response_instance.to_dict()
# create an instance of GetMetadataResponseDtoResponse from a dict
get_metadata_response_dto_response_from_dict = GetMetadataResponseDtoResponse.from_dict(get_metadata_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


