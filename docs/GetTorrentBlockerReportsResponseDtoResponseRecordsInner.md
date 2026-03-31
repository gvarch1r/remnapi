# GetTorrentBlockerReportsResponseDtoResponseRecordsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**user_id** | **float** |  | 
**node_id** | **float** |  | 
**user** | [**GetTorrentBlockerReportsResponseDtoResponseRecordsInnerUser**](GetTorrentBlockerReportsResponseDtoResponseRecordsInnerUser.md) |  | 
**node** | [**GetConfigProfilesResponseDtoResponseConfigProfilesInnerNodesInner**](GetConfigProfilesResponseDtoResponseConfigProfilesInnerNodesInner.md) |  | 
**report** | [**GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReport**](GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReport.md) |  | 
**created_at** | **datetime** |  | 

## Example

```python
from supn_remnawave_panel.models.get_torrent_blocker_reports_response_dto_response_records_inner import GetTorrentBlockerReportsResponseDtoResponseRecordsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentBlockerReportsResponseDtoResponseRecordsInner from a JSON string
get_torrent_blocker_reports_response_dto_response_records_inner_instance = GetTorrentBlockerReportsResponseDtoResponseRecordsInner.from_json(json)
# print the JSON string representation of the object
print(GetTorrentBlockerReportsResponseDtoResponseRecordsInner.to_json())

# convert the object into a dict
get_torrent_blocker_reports_response_dto_response_records_inner_dict = get_torrent_blocker_reports_response_dto_response_records_inner_instance.to_dict()
# create an instance of GetTorrentBlockerReportsResponseDtoResponseRecordsInner from a dict
get_torrent_blocker_reports_response_dto_response_records_inner_from_dict = GetTorrentBlockerReportsResponseDtoResponseRecordsInner.from_dict(get_torrent_blocker_reports_response_dto_response_records_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


