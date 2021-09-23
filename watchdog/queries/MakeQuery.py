import watchdog.logs.Logging as log
import requests


class MakeQuery:

    _logger = log.get_logger(__name__)

    def post(self, url, params):
        self._logger.info(f"Posting to URL {url} with params {list(params.keys())}")
        return requests.post(url, params)
