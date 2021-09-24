from src.queries.AccessToken import AccessToken
from src.queries.HttpRequestExecutor import HttpRequestExecutor as q
import src.logs.Logging as log
from src.constants.Constants import SecretConstants, SettingConstants
from src.constants.ConstantsUpdater import ConstantsUpdater
from src.utils.TimeHandler import get_current_time_string, get_current_time, get_datetime_from_string


class AccessTokenUpdater:

    _logger = log.get_logger(__name__)

    def __init__(self):
        self.token = AccessToken()
        self.oauth_url = SettingConstants().get_oauth_url()
        self.secrets = SecretConstants()

    def needs_to_be_updated(self):
        if self.token.date == "":
            self._logger.debug("`access_token` needs to be created.")
            self.make_new_access_token_request_and_update_json()
        elif self.check_if_token_older_than_1_hour():
            self._logger.debug("`access_token` needs to be refreshed.")
            self.make_new_access_token_request_and_update_json()
        else:
            self._logger.debug("`access_token` is valid.")

    def make_new_access_token_request_and_update_json(self):
        res = self.get_new_access_token()
        if res.ok:
            self.create_dict_entry_from_http_result(res)

    def create_dict_entry_from_http_result(self, res):
        current_time = get_current_time_string()
        res_json = res.json()
        dictionary = {
                "id": res_json['access_token'],
                "date": current_time

        }
        self._logger.debug(f"Updating `access_token` JSON at time {current_time}")
        ConstantsUpdater().write_secrets_json_file("OAuth_Access_Token_Details", dictionary)

    def check_if_token_older_than_1_hour(self):
        diff_in_seconds = (get_current_time() - get_datetime_from_string(self.token.date)).total_seconds()
        diff_in_minutes = int(diff_in_seconds / 60)
        self._logger.debug(f"Last check occurred {diff_in_minutes} minutes ago.")
        return diff_in_minutes > 55  # add a little buffer to request new token if close to renewal

    def get_new_access_token(self):
        data = {
            "client_id": self.secrets.get_oauth_client_id(),
            "client_secret": self.secrets.get_oauth_client_secret(),
            "refresh_token": self.secrets.get_oauth_refresh_token(),
            "grant_type": "refresh_token"
        }
        res = q().http_post(self.oauth_url, data=data)

        if res.ok:
            self._logger.debug("Query was successful.")
        else:
            self._logger.critical("Query did not succeed.")

        return res
