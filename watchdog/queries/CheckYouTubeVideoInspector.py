from watchdog.queries.HttpRequestExecutor import HttpRequestExecutor as q
import watchdog.logs.Logging as log
from watchdog.queries.AccessToken import AccessToken
from watchdog.constants.Constants import SecretConstants, SettingConstants
from watchdog.queries.AccessTokenUpdater import AccessTokenUpdater


class CheckYouTubeVideoInspector:

    _logger = log.get_logger(__name__)

    def __init__(self):
        AccessTokenUpdater().needs_to_be_updated()
        self.sec_const = SecretConstants()
        self.set_const = SettingConstants()
        self.token = AccessToken()

    def get_json_from_youtube_id(self, id):
        res = self.exec_query(id)
        res_json = res.json()
        return res_json

    def exec_query(self, id):
        url, params, headers = self.build_query(id)
        return q().http_get(url, params=params, headers=headers)

    def build_query(self, id):
        url = f"{self.set_const.get_youtube_data_api_url()}/videos"
        params = {
            'part': ['contentDetails', 'id', 'liveStreamingDetails',
                     'processingDetails', 'snippet', 'status'],
            'id': id,
            'key': self.sec_const.get_yt_api_key()
        }
        headers = {
            'Authorization': f"Bearer {self.token.id}",
            'Accept': 'application/json'
        }
        return url, params, headers
