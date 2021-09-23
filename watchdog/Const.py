import watchdog.logs.Logging as log

import json


path_prefix = "."


class Const:

    _logger = log.get_logger(__name__)

    def __init__(self):
        self.my_json = None
        self.json_path = None

    def get_from_dict_error_handling(self, key):
        res = self.my_json.get(key, None)
        if res is None:
            self._logger.critical(f"Failed to load key: '{key}' from {self.json_path}")
        return res


class SettingConst(Const):

    def __init__(self):
        self.json_path = f"{path_prefix}/settings.json"
        file_settings = open(self.json_path, 'r')
        self.my_json = json.load(file_settings)
        file_settings.close()
        super()._logger.debug(f"Loaded settings file {self.json_path}")

    def get_oauth_url(self):
        return self.my_json.get("oauth_url")


class SecretConst(Const):

    def __init__(self):
        self.json_path = f"{path_prefix}/secrets.json"
        file_secrets = open(self.json_path, 'r')
        self.my_json = json.load(file_secrets)
        file_secrets.close()
        super()._logger.debug(f"Loaded settings file {self.json_path}")

    def get_yt_api_key(self):
        return self.get_from_dict_error_handling("YT_API_Key")

    def get_oauth_client_id(self):
        return self.get_from_dict_error_handling("OAuth_Client_ID")

    def get_oauth_client_secret(self):
        return self.get_from_dict_error_handling("OAuth_Client_Secret")

    def get_oauth_refresh_token(self):
        return self.get_from_dict_error_handling("OAuth_Refresh_Token")

    def get_oauth_access_token_dict(self):
        """
        :return: the dict containing the access_token token and its date of creation.
        """
        return self.get_from_dict_error_handling("OAuth_Access_Token_Details")
