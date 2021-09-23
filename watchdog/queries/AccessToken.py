from watchdog.Constants import SecretConstants
import watchdog.logs.Logging as log


class AccessToken:
    _logger = log.get_logger(__name__)

    def __init__(self):
        access_token_dict = SecretConstants().get_oauth_access_token_dict()
        self.id = access_token_dict.get("token")
        self.age = access_token_dict.get("date")
        self._logger.debug(f"Loaded token '{self.id}' created on date '{self.age}'")
