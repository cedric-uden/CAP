import watchdog.logs.Logging as log
from watchdog.ConstantsValidator import ConstantsValidator

import json


path_prefix = "."


class SettingConstants:

    _logger = log.get_logger(__name__)

    def __init__(self):
        self.json_path = f"{path_prefix}/settings.json"
        file_settings = open(self.json_path, 'r')
        self.constants_json = json.load(file_settings)
        self.val = ConstantsValidator(self)
        file_settings.close()
        self._logger.debug(f"Loaded settings file {self.json_path}")

    def get_oauth_url(self):
        return self.val.get_or_throw_error("oauth_url")

    def get_time_format(self):
        return self.val.get_or_throw_error("time_format")


class SecretConstants:

    _logger = log.get_logger(__name__)

    def __init__(self):
        self.json_path = f"{path_prefix}/secrets.json"
        file_secrets = open(self.json_path, 'r')
        self.constants_json = json.load(file_secrets)
        self.val = ConstantsValidator(self)
        file_secrets.close()
        self._logger.debug(f"Loaded settings file {self.json_path}")

    def get_yt_api_key(self):
        return self.val.get_or_throw_error("YT_API_Key")

    def get_oauth_client_id(self):
        return self.val.get_or_throw_error("OAuth_Client_ID")

    def get_oauth_client_secret(self):
        return self.val.get_or_throw_error("OAuth_Client_Secret")

    def get_oauth_refresh_token(self):
        return self.val.get_or_throw_error("OAuth_Refresh_Token")

    def get_oauth_access_token_dict(self):
        """
        :return: the dict containing the access_token token and its date of creation.
        """
        return self.val.get_or_throw_error("OAuth_Access_Token_Details")
