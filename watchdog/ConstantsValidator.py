import watchdog.logs.Logging as log


class ConstantsValidator:

    _logger = log.get_logger(__name__)

    def __init__(self, constants):
        self.constants = constants

    def get_or_throw_error(self, key):
        res = self.constants.constants_json.get(key, None)
        if res is None:
            self._logger.critical(f"Failed to load key: '{key}' from {self.constants.json_path}")
            raise KeyError("Key to set constants not found.")
        return res
