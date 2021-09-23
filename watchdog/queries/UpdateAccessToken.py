from watchdog.queries.AccessToken import AccessToken
from watchdog.queries.MakeQuery import MakeQuery as q
import watchdog.logs.Logging as log
from watchdog.Const import SecretConst, SettingConst

import datetime


class UpdateAccessToken:

    _logger = log.get_logger(__name__)

    def __init__(self):
        self.token = AccessToken()
        self.oauth_url = SettingConst().get_oauth_url()
        self.secrets = SecretConst()

    def needs_to_be_updated(self):
        # WIP: enter the date checking and log the new token
        if self.token.age == "":
            self._logger.debug("UpdateAccessToken needs to be updated.")

            res = self.get_new_access_token()
            self._logger.info(res.text)

    def get_new_access_token(self):
        data = {
            "client_id": self.secrets.get_oauth_client_id(),
            "client_secret": self.secrets.get_oauth_client_secret(),
            "refresh_token": self.secrets.get_oauth_refresh_token(),
            "grant_type": "refresh_token"
        }
        res = q().post(self.oauth_url, data)

        text = f"Query to URL {self.oauth_url} and params {data}"
        if res.ok:
            self._logger.debug(f"{text} was successful.")
        else:
            self._logger.critical(f"{text} did not succeed.")

        return res
