from watchdog.queries.HttpRequestExecutor import HttpRequestExecutor as q
import watchdog.logs.Logging as log
from watchdog.queries.AccessToken import AccessToken
from watchdog.constants.Constants import SecretConstants, SettingConstants
from watchdog.queries.AccessTokenUpdater import AccessTokenUpdater


class MostRecentYouTubeVideos:

    _logger = log.get_logger(__name__)

    def __init__(self):
        AccessTokenUpdater().needs_to_be_updated()
        self.sec_const = SecretConstants()
        self.set_const = SettingConstants()
        self.token = AccessToken()

    def get_json(self):
        res = self.exec_query()
        res_json = res.json()
        return res_json

    def exec_query(self):
        url, params, headers = self.build_query()
        return q().http_get(url, params=params, headers=headers)

    def build_query(self):
        url = f"{self.set_const.get_youtube_data_api_url()}/activities"
        params = {
            'part': 'contentDetails',
            'mine': True,
            'key': self.sec_const.get_yt_api_key()
        }
        headers = {
            'Authorization': f"Bearer {self.token.id}",
            'Accept': 'application/json'
        }
        return url, params, headers
