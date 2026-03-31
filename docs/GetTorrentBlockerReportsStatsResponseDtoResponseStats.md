# GetTorrentBlockerReportsStatsResponseDtoResponseStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distinct_nodes** | **float** |  | 
**distinct_users** | **float** |  | 
**total_reports** | **float** |  | 
**reports_last24_hours** | **float** |  | 

## Example

```python
from supn_remnawave_panel.models.get_torrent_blocker_reports_stats_response_dto_response_stats import GetTorrentBlockerReportsStatsResponseDtoResponseStats

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentBlockerReportsStatsResponseDtoResponseStats from a JSON string
get_torrent_blocker_reports_stats_response_dto_response_stats_instance = GetTorrentBlockerReportsStatsResponseDtoResponseStats.from_json(json)
# print the JSON string representation of the object
print(GetTorrentBlockerReportsStatsResponseDtoResponseStats.to_json())

# convert the object into a dict
get_torrent_blocker_reports_stats_response_dto_response_stats_dict = get_torrent_blocker_reports_stats_response_dto_response_stats_instance.to_dict()
# create an instance of GetTorrentBlockerReportsStatsResponseDtoResponseStats from a dict
get_torrent_blocker_reports_stats_response_dto_response_stats_from_dict = GetTorrentBlockerReportsStatsResponseDtoResponseStats.from_dict(get_torrent_blocker_reports_stats_response_dto_response_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


