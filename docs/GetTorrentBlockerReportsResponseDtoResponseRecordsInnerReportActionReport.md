# GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportActionReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked** | **bool** |  | 
**ip** | **str** |  | 
**block_duration** | **float** |  | 
**will_unblock_at** | **datetime** |  | 
**user_id** | **str** |  | 
**processed_at** | **datetime** |  | 

## Example

```python
from supn_remnawave_panel.models.get_torrent_blocker_reports_response_dto_response_records_inner_report_action_report import GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportActionReport

# TODO update the JSON string below
json = "{}"
# create an instance of GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportActionReport from a JSON string
get_torrent_blocker_reports_response_dto_response_records_inner_report_action_report_instance = GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportActionReport.from_json(json)
# print the JSON string representation of the object
print(GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportActionReport.to_json())

# convert the object into a dict
get_torrent_blocker_reports_response_dto_response_records_inner_report_action_report_dict = get_torrent_blocker_reports_response_dto_response_records_inner_report_action_report_instance.to_dict()
# create an instance of GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportActionReport from a dict
get_torrent_blocker_reports_response_dto_response_records_inner_report_action_report_from_dict = GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReportActionReport.from_dict(get_torrent_blocker_reports_response_dto_response_records_inner_report_action_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


