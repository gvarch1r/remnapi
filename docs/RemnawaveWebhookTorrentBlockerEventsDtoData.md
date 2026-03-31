# RemnawaveWebhookTorrentBlockerEventsDtoData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | [**CreateNodeResponseDtoResponse**](CreateNodeResponseDtoResponse.md) |  | 
**user** | [**CreateUserResponseDtoResponse**](CreateUserResponseDtoResponse.md) |  | 
**report** | [**GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReport**](GetTorrentBlockerReportsResponseDtoResponseRecordsInnerReport.md) |  | 

## Example

```python
from supn_remnawave_panel.models.remnawave_webhook_torrent_blocker_events_dto_data import RemnawaveWebhookTorrentBlockerEventsDtoData

# TODO update the JSON string below
json = "{}"
# create an instance of RemnawaveWebhookTorrentBlockerEventsDtoData from a JSON string
remnawave_webhook_torrent_blocker_events_dto_data_instance = RemnawaveWebhookTorrentBlockerEventsDtoData.from_json(json)
# print the JSON string representation of the object
print(RemnawaveWebhookTorrentBlockerEventsDtoData.to_json())

# convert the object into a dict
remnawave_webhook_torrent_blocker_events_dto_data_dict = remnawave_webhook_torrent_blocker_events_dto_data_instance.to_dict()
# create an instance of RemnawaveWebhookTorrentBlockerEventsDtoData from a dict
remnawave_webhook_torrent_blocker_events_dto_data_from_dict = RemnawaveWebhookTorrentBlockerEventsDtoData.from_dict(remnawave_webhook_torrent_blocker_events_dto_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


