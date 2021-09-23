import json
import watchdog.logs.Logging as log
from watchdog.constants.ConstantsPaths import secrets_json_path, settings_json_path


class ConstantsUpdater:
    _logger = log.get_logger(__name__)

    def __init__(self):
        pass

    def write_json_file(self, key, value, target_file):
        with open(target_file, "r") as jsonFile:
            data = json.load(jsonFile)

        data[key] = value

        with open(target_file, "w") as jsonFile:
            json.dump(data, jsonFile, indent=4)

        self._logger.info(f"Updated {target_file}")

    def write_secrets_json_file(self, key, value):
        self.write_json_file(key, value, secrets_json_path)

    def write_settings_json_file(self, key, value):
        self.write_json_file(key, value, settings_json_path)
