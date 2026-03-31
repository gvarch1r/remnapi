# GetTorrentBlockerReportsResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[GetTorrentBlockerReportsResponseDtoResponseRecordsInner]**](GetTorrentBlockerReportsResponseDtoResponseRecordsInner.md) |  | 
**total** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.get_torrent_blocker_reports_response_dto_response import GetTorrentBlockerReportsResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentBlockerReportsResponseDtoResponse from a JSON string
get_torrent_blocker_reports_response_dto_response_instance = GetTorrentBlockerReportsResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetTorrentBlockerReportsResponseDtoResponse.to_json())

# convert the object into a dict
get_torrent_blocker_reports_response_dto_response_dict = get_torrent_blocker_reports_response_dto_response_instance.to_dict()
# create an instance of GetTorrentBlockerReportsResponseDtoResponse from a dict
get_torrent_blocker_reports_response_dto_response_from_dict = GetTorrentBlockerReportsResponseDtoResponse.from_dict(get_torrent_blocker_reports_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


