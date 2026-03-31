# GetTorrentBlockerReportsResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**GetTorrentBlockerReportsResponseDtoResponse**](GetTorrentBlockerReportsResponseDtoResponse.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_torrent_blocker_reports_response_dto import GetTorrentBlockerReportsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentBlockerReportsResponseDto from a JSON string
get_torrent_blocker_reports_response_dto_instance = GetTorrentBlockerReportsResponseDto.from_json(json)
# print the JSON string representation of the object
print(GetTorrentBlockerReportsResponseDto.to_json())

# convert the object into a dict
get_torrent_blocker_reports_response_dto_dict = get_torrent_blocker_reports_response_dto_instance.to_dict()
# create an instance of GetTorrentBlockerReportsResponseDto from a dict
get_torrent_blocker_reports_response_dto_from_dict = GetTorrentBlockerReportsResponseDto.from_dict(get_torrent_blocker_reports_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


