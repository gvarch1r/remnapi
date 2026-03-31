# GetTorrentBlockerReportsStatsResponseDtoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stats** | [**GetTorrentBlockerReportsStatsResponseDtoResponseStats**](GetTorrentBlockerReportsStatsResponseDtoResponseStats.md) |  | 
**top_users** | [**List[GetTorrentBlockerReportsStatsResponseDtoResponseTopUsersInner]**](GetTorrentBlockerReportsStatsResponseDtoResponseTopUsersInner.md) |  | 
**top_nodes** | [**List[GetTorrentBlockerReportsStatsResponseDtoResponseTopNodesInner]**](GetTorrentBlockerReportsStatsResponseDtoResponseTopNodesInner.md) |  | 

## Example

```python
from supn_remnawave_panel.models.get_torrent_blocker_reports_stats_response_dto_response import GetTorrentBlockerReportsStatsResponseDtoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentBlockerReportsStatsResponseDtoResponse from a JSON string
get_torrent_blocker_reports_stats_response_dto_response_instance = GetTorrentBlockerReportsStatsResponseDtoResponse.from_json(json)
# print the JSON string representation of the object
print(GetTorrentBlockerReportsStatsResponseDtoResponse.to_json())

# convert the object into a dict
get_torrent_blocker_reports_stats_response_dto_response_dict = get_torrent_blocker_reports_stats_response_dto_response_instance.to_dict()
# create an instance of GetTorrentBlockerReportsStatsResponseDtoResponse from a dict
get_torrent_blocker_reports_stats_response_dto_response_from_dict = GetTorrentBlockerReportsStatsResponseDtoResponse.from_dict(get_torrent_blocker_reports_stats_response_dto_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


