from watchdog.queries.AccessToken import AccessToken
from watchdog.queries.HttpRequestExecutor import HttpRequestExecutor as q
import watchdog.logs.Logging as log
from watchdog.Constants import SecretConstants, SettingConstants

import datetime


class AccessTokenUpdater:

    _logger = log.get_logger(__name__)

    def __init__(self):
        self.token = AccessToken()
        self.oauth_url = SettingConstants().get_oauth_url()
        self.secrets = SecretConstants()

    def needs_to_be_updated(self):
        # WIP: enter the date checking and log the new token
        if self.token.age == "":
            self._logger.debug("UpdateAccessToken needs to be updated.")

            # res = self.get_new_access_token()
            # self._logger.info(res.text)

    def get_new_access_token(self):
        data = {
            "client_id": self.secrets.get_oauth_client_id(),
            "client_secret": self.secrets.get_oauth_client_secret(),
            "refresh_token": self.secrets.get_oauth_refresh_token(),
            "grant_type": "refresh_token"
        }
        res = q().post(self.oauth_url, data)

        if res.ok:
            self._logger.debug("Query was successful.")
        else:
            self._logger.critical("Query did not succeed.")

        return res
