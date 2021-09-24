import src.logs.Logging as log
from src.constants.ConstantsValidator import ConstantsValidator
from src.constants.ConstantsPaths import secrets_json_path, settings_json_path

import json


class SettingConstants:

    _logger = log.get_logger(__name__)

    def __init__(self):
        self.json_path = settings_json_path
        file_settings = open(self.json_path, 'r')
        self.constants_json = json.load(file_settings)
        self.val = ConstantsValidator(self)
        file_settings.close()
        self._logger.debug(f"Loaded settings file {self.json_path}")

    def get_oauth_url(self):
        return self.val.get_or_throw_error("oauth_url")

    def get_time_format(self):
        return self.val.get_or_throw_error("time_format")

    def get_youtube_data_api_url(self):
        return self.val.get_or_throw_error("youtube_data_api_url")

    def get_podcast_min_duration(self):
        return self.val.get_or_throw_error("podcast_min_duration")

    def get_podcast_max_duration(self):
        return self.val.get_or_throw_error("podcast_max_duration")


class SecretConstants:

    _logger = log.get_logger(__name__)

    def __init__(self):
        self.json_path = secrets_json_path
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
