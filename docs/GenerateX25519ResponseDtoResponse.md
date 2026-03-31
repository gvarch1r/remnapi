# GenerateX25519ResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keypairs** | [**List[GenerateX25519ResponseDtoResponseKeypairsInner]**](GenerateX25519ResponseDtoResponseKeypairsInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.generate_x25519_response_dto_response import GenerateX25519ResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateX25519ResponseDtoResponse from a JSON string
generate_x25519_response_dto_response_instance = GenerateX25519ResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateX25519ResponseDtoResponse.to_json())

# convert the object into a dict
generate_x25519_response_dto_response_dict = generate_x25519_response_dto_response_instance.to_dict()
# create an instance of GenerateX25519ResponseDtoResponse from a dict
generate_x25519_response_dto_response_from_dict = GenerateX25519ResponseDtoResponse.from_dict(generate_x25519_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


