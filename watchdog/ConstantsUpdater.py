import json
import watchdog.logs.Logging as log


class ConstantsUpdater:
    _logger = log.get_logger(__name__)

    def __init__(self):
        pass

    def write_this_dict(self, dictionary):
        # WIP
        json_object = json.dumps(dictionary, indent=4)

        with open("secrets2.json", "w") as outfile:
            outfile.write(json_object)
            self._logger.info(f"Updated {outfile}.")
